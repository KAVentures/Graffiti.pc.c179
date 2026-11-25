from itertools import combinations
from collections import Counter
import networkx as nx

def require(ok, detail):
    if not ok: raise AssertionError(detail)

def leaf_tree(n,edges):
    best=0
    for es in combinations(edges,n-1):
        parent=list(range(n)); deg=[0]*n
        def root(x):
            while parent[x]!=x: x=parent[x]
            return x
        for u,v in es:
            a,b=root(u),root(v)
            if a==b: break
            parent[a]=b;deg[u]+=1;deg[v]+=1
        else:
            best=max(best,deg.count(1))
            if best==max(2,n-1): break
    return best

def main():
    counts=Counter();eq=0; witnesses=0; stronger=0
    for g in nx.graph_atlas_g():
        n=len(g)
        if n<2: continue
        E=list(g.edges()); adj=[0]*n
        for u,v in E: adj[u]|=1<<v;adj[v]|=1<<u
        seen=1
        while True:
            new=seen
            for u in range(n):
                if seen>>u&1:new|=adj[u]
            if new==seen:break
            seen=new
        if seen!=(1<<n)-1:continue
        I=[s for s in range(1<<n) if all(not (s&adj[u]) for u in range(n) if s>>u&1)]
        a=max(s.bit_count() for s in I); deg=[x.bit_count() for x in adj]; sigma=sorted(deg)[1]
        b=max(s.bit_count()+t.bit_count() for s in I for t in I if not s&t)
        L=leaf_tree(n,E)
        require(L+b>=2*a+sigma,(E,L,b,a,sigma))
        counts[n]+=1;eq+=L+b==2*a+sigma
        if a==1:witnesses+=1
        for s in I:
            k=s.bit_count()
            if k<2:continue
            sigma_A=sorted(deg[u] for u in range(n) if s>>u&1)[1]
            require(L+b>=2*k+sigma_A,(E,s,L,b,k,sigma_A))
            witnesses+=1
            stronger+=k==a and sigma_A>sigma
    require(dict(counts)=={2:1,3:2,4:6,5:21,6:112,7:853} and eq==147 and witnesses==13067 and stronger==845,(counts,eq,witnesses,stronger))
    print('Independent exact check: 995 graphs, 147 equalities, 13067 witness domains, 845 strict degree-refinement witnesses; 0 violations')
if __name__=='__main__':main()
