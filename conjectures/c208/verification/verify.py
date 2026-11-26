"""Exact supplementary checks of Graffiti.pc 208."""
from collections import Counter
from functools import lru_cache
import networkx as nx

def traceable(g):
    n=len(g); full=(1<<n)-1
    adj=[sum(1<<w for w in g[v]) for v in range(n)]
    @lru_cache(None)
    def path(mask,v):
        if mask==full:return True
        return any(path(mask|1<<w,w) for w in range(n) if adj[v]>>w&1 and not mask>>w&1)
    return any(path(1<<v,v) for v in range(n))

def main():
    counts=Counter(); qualifying=Counter(); non=Counter(); sharp=[]
    for g in nx.graph_atlas_g():
        n=len(g)
        if n<2 or not nx.is_connected(g):continue
        counts[n]+=1
        m=n*(n-1)//2-g.number_of_edges(); mu=len(nx.max_weight_matching(g,maxcardinality=True))
        has=traceable(g)
        if m<=3*mu-2:
            qualifying[n]+=1
            assert has
        if not has:
            non[n]+=1
            assert m>=3*mu-1
            ds=sorted(dict(g.degree()).values())
            assert any(ds[k-1]<=k-1 and ds[n-k]<=n-k-1 and 2*m>=k*(2*n+1-3*k) for k in range(2,n//2+1))
            if m==3*mu-1:sharp.append(nx.to_graph6_bytes(g,header=False).decode().strip())
    assert (sum(counts.values()),sum(qualifying.values()),sum(non.values()),sharp)==(995,235,144,['D@{','EtaG'])
    print('Connected graphs:',sum(counts.values()))
    print('Hypothesis satisfied:',sum(qualifying.values()))
    print('Nontraceable graphs:',sum(non.values()))
    print('Sharp graph6 witnesses:',sharp)
    print('Violations: 0')
if __name__=='__main__':main()
