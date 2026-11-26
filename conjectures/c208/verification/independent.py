"""Matching subset recursion and exhaustive permutation path search."""
from functools import lru_cache
from itertools import permutations
import networkx as nx

def main():
    total=qualifying=non=0; sharp=[]
    for g in nx.graph_atlas_g():
        n=len(g)
        if n<2:continue
        adj=[set(g[v]) for v in range(n)]
        seen={0}
        while True:
            nxt=seen.union(*(adj[v] for v in seen))
            if nxt==seen:break
            seen=nxt
        if len(seen)!=n:continue
        total+=1
        masks=[sum(1<<w for w in a) for a in adj]
        @lru_cache(None)
        def match(mask):
            if not mask:return 0
            bit=mask&-mask; v=bit.bit_length()-1; rest=mask^bit
            return max([match(rest)]+[1+match(rest^(1<<w)) for w in adj[v] if rest>>w&1])
        mu=match((1<<n)-1)
        m=sum(v not in adj[u] for u in range(n) for v in range(u+1,n))
        has=any(all(v in adj[u] for u,v in zip(p,p[1:])) for p in permutations(range(n)))
        if m<=3*mu-2:
            qualifying+=1
            assert has
        if not has:
            non+=1
            assert m>=3*mu-1
            if m==3*mu-1:sharp.append(nx.to_graph6_bytes(g,header=False).decode().strip())
    assert (total,qualifying,non,sharp)==(995,235,144,['D@{','EtaG'])
    print('Independent check: 995 graphs, 235 qualifying, 144 nontraceable, 2 sharp witnesses; 0 violations')
if __name__=='__main__':main()
