"""Third exact cross-check of the three Graffiti.pc proofs; run without -O."""
from collections import Counter
from itertools import combinations
import networkx as nx
import sys
if sys.flags.optimize:
    raise RuntimeError("Run without -O: assertions are required")
if nx.__version__ != "3.6.1":
    raise RuntimeError("Install pinned NetworkX 3.6.1")
# Independent direct set enumeration and spanning trees.
def leaf_tree(g):
    n=len(g)
    best=0
    for es in combinations(g.edges(),n-1):
        parent=list(range(n)); deg=[0]*n
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for u,v in es:
            a,b=root(u),root(v)
            if a==b:break
            parent[a]=b;deg[u]+=1;deg[v]+=1
        else:
            best=max(best,deg.count(1))
            if best==max(2,n-1):break
    return best
counts=Counter();eq=Counter();alt=Counter();first=None;strong=0
for g in nx.graph_atlas_g():
    n=len(g)
    if n<2 or not nx.is_connected(g):continue
    V=set(g);N={v:set(g[v]) for v in g};d=min(map(len,N.values()));D=max(map(len,N.values()))
    sets=[set(s) for k in range(n+1) for s in combinations(g,k)]
    indep=[s for s in sets if all(not g.has_edge(u,v) for u,v in combinations(s,2))]
    gamma=min(len(s) for s in sets if all(v in s or N[v]&s for v in g))
    gc=min(len(s) for s in sets if s and nx.is_connected(g.subgraph(s)) and all(v in s or N[v]&s for v in g))
    b=max(len(a)+len(c) for a in indep for c in indep if not a&c)
    assert b==max(len(s) for s in sets if nx.is_bipartite(g.subgraph(s)))
    lamv={v:max(len(s) for s in indep if s<=N[v]) for v in g};lam=max(lamv.values());f=sum(k==min(lamv.values()) for k in lamv.values())
    Q=max((s for s in sets if any(s<=V-N[v]-{v} for v in g) and all(g.has_edge(u,w) for u,w in combinations(s,2))),key=len)
    L=leaf_tree(g);assert L==(2 if n==2 else n-gc)
    assert L>=len(Q) and L>=f*(1//d)
    if Q:
        q,w=next((q,w) for q in Q for w in N[q]-Q)
        t=nx.Graph();t.add_edges_from([(q,u) for u in Q-{q}]+[(q,w)])
        while len(t)<n:
            u,v=next((u,v) for u in t for v in g[u] if v not in t);t.add_edge(u,v)
        assert nx.is_tree(t) and sum(x==1 for _,x in t.degree())>=len(Q)
    if g.number_of_edges()!=n*(n-1)//2:
        S={v for v in g if lamv[v]==1};H=V-S
        assert H and nx.is_connected(g.subgraph(H)) and all(N[s]&H for s in S)
        t=nx.minimum_spanning_tree(g.subgraph(H));t.add_edges_from((s,min(N[s]&H)) for s in S)
        assert nx.is_tree(t) and all(t.degree(s)==1 for s in S)
    v=next(v for v in g if lamv[v]==lam);A=next(s for s in indep if len(s)==lam and s<=N[v])
    for a in A:
        dom=(V-A-N[a])|{v,a}
        assert len(dom)==n-lam-len(N[a])+2 and all(w in dom or N[w]&dom for w in g)
    assert gamma<=n-lam-d+2 and gamma<=n-D and L+b>=n+(lam+1)//2
    slack=L+b-d-gamma-lam; assert slack>=max(0,(lam+1)//2-2)
    assert gc<=n+b-d-gamma-lam-max(0,(lam+1)//2-2)
    if gamma==n-d and lam==2:assert all(x==1 for _,x in nx.complement(g).degree())
    if L+b<D+gamma+lam:
        alt[n]+=1
        if first is None:first=(nx.to_graph6_bytes(g,header=False).decode().strip(),list(g.edges()),L,b,D,gamma,lam)
    counts[n]+=1;eq[161]+=L==len(Q);eq[162]+=d==1 and L==f;eq[179]+=slack==0;strong+=slack==max(0,(lam+1)//2-2)
assert dict(counts)=={2:1,3:2,4:6,5:21,6:112,7:853}; assert dict(eq)=={161:44,162:90,179:8}
print('Graph counts:',dict(counts),'total',sum(counts.values()))
print('Equality counts:',dict(eq),'(162 restricted to delta=1)')
print('Strong c179 bound equality:',strong)
print('Uppercase Delta variant failures:',dict(alt),'first:',first)
print('All invariant, inequality and constructive witness checks passed')
