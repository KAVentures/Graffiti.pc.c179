from itertools import combinations
from collections import Counter
import networkx as nx

def require(ok, detail):
    if not ok: raise AssertionError(detail)

def independent(g):
    return next(set(s) for k in range(len(g),0,-1) for s in combinations(g,k) if not g.subgraph(s).number_of_edges())

def leaf_max(g):
    if len(g)==2:return 2
    return len(g)-next(k for k in range(1,len(g)) if any(nx.is_connected(g.subgraph(s)) and all(v in s or any(u in g[v] for u in s) for v in g) for s in combinations(g,k)))

def tree_from_core(g,t):
    t=t.copy()
    core=set(t)
    for u in sorted(set(g)-core):
        v=next(v for v in g[u] if v in core)
        t.add_edge(u,v)
    require(nx.is_tree(t) and set(t)==set(g),list(g.edges()))
    return t

def certificate(g,A):
    V=set(g); B=V-A; comps=[set(c) for c in nx.connected_components(g.subgraph(B))];m=len(comps)
    alpha=len(A);sigma=sorted(g.degree(u) for u in A)[1] if alpha>=2 else sorted(dict(g.degree()).values())[1]
    low=[u for u in A if g.degree(u)<sigma];require(len(low)<=1,low)
    def touched(a):return [c for c in comps if c&set(g[a])]
    def attach_comp(t,a,c):
        t.add_edge(a,min(c&set(g[a])))
        t.add_edges_from(nx.minimum_spanning_tree(g.subgraph(c)).edges())
    def connect(t,covered,used):
        while covered!=B:
            a=next(a for a in sorted(A-used) if set(g[a])&covered and set(g[a])&(B-covered))
            t.add_edge(a,min(set(g[a])&covered));used.add(a)
            for c in touched(a):
                if not c<=covered:
                    attach_comp(t,a,c);covered|=c
        return t,used
    if alpha==1:
        t=nx.Graph();v=min(V);t.add_edges_from((v,u) for u in g[v]);return t,'complete'
    if sigma==1:
        c=comps[0];t=nx.minimum_spanning_tree(g.subgraph(c));t,used=connect(t,c.copy(),set());require(len(used)<=m-1,used)
        return tree_from_core(g,t),'baseline'
    high=A-set(low);a=max(high,key=lambda u:len(touched(u)));q=len(touched(a));beta=sum(len(independent(g.subgraph(c))) for c in comps)
    if q>=2 or beta>=m+1:
        covered=set().union(*touched(a));H=g.subgraph(covered|{a});t=nx.Graph();t.add_edges_from((a,u) for u in g[a])
        while len(t)<len(H):
            u,v=next((u,v) for u in t for v in H[u] if v not in t);t.add_edge(u,v)
        require(sum(t.degree(u)==1 for u in covered)>=sigma,(g,a))
        t,used=connect(t,covered.copy(),{a});require(len(used)<=m-q+1,used)
        protected={min(g[low[0]])} if low else set()
        X=set(sorted(u for u in B-protected if t.degree(u)==1)[:sigma-1]);require(len(X)==sigma-1,(g,A))
        t.remove_nodes_from(X)
        return tree_from_core(g,t),'multi' if q>=2 else 'slack'
    c=touched(a)[0];require(len(c)>=sigma,c)
    protected=(set(g[low[0]])&c) if low else set()
    keep=min(protected) if protected else min(c)
    X=set(sorted(c-{keep})[:sigma-1]);require(len(X)==sigma-1,X)
    t=nx.Graph();t.add_nodes_from(B-X)
    for cc in comps:t.add_edges_from(nx.minimum_spanning_tree(g.subgraph(cc-X)).edges())
    if m>1:
        require(len(low)==1 and len(touched(low[0]))==m,(g,A))
        t.add_edges_from((low[0],min(set(g[low[0]])&(cc-X))) for cc in comps)
    require(nx.is_tree(t),list(g.edges()))
    return tree_from_core(g,t),'cliques'

def main():
    counts=Counter(); cases=Counter();eq=0; witnesses=0; stronger=0
    for g in nx.graph_atlas_g():
        n=len(g)
        if n<2 or not nx.is_connected(g):continue
        A=independent(g);alpha=len(A);sigma=sorted(dict(g.degree()).values())[1]
        b=max(k for k in range(n,0,-1) if any(nx.is_bipartite(g.subgraph(s)) for s in combinations(g,k)))
        L=leaf_max(g)
        for s in (s for k in range(2,alpha+1) for s in combinations(g,k)) if alpha>=2 else [(min(g),)]:
            if g.subgraph(s).number_of_edges():continue
            t,case=certificate(g,set(s));ell=sum(d==1 for _,d in t.degree());require(nx.is_tree(t) and set(t)==set(g) and ell+b>=2*len(s)+(sorted(g.degree(u) for u in s)[1] if len(s)>=2 else sigma) and L>=ell,(list(g.edges()),s,case,ell,b,sigma))
            cases[case]+=1;witnesses+=1
            if len(s)==alpha and len(s)>=2 and sorted(g.degree(u) for u in s)[1]>sigma: stronger+=1
        require(L+b>=2*alpha+sigma,list(g.edges()));eq+=L+b==2*alpha+sigma;counts[n]+=1
    require(dict(counts)=={2:1,3:2,4:6,5:21,6:112,7:853} and eq==147 and witnesses==13067 and stronger==845,(counts,eq,witnesses,stronger))
    print('Graphs:',sum(counts.values()),dict(counts));print('Equality cases:',eq);print('Constructive witnesses (independent subsets of size >=2; one star for each complete graph):',witnesses,dict(sorted(cases.items())));print('Strict degree-refinement witnesses:',stronger);print('Violations: 0')
if __name__=='__main__':main()
