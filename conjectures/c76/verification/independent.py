"""Exact block-cut dynamic program, independent of the closed forms."""
from functools import lru_cache
from itertools import combinations
import networkx as nx
from verify import build,require,parameters

def exact_tree(g):
    blocks=[tuple(sorted(b)) for b in nx.biconnected_components(g)]
    incident={v:[] for v in g}
    options={}
    for i,b in enumerate(blocks):
        for v in b:
            incident[v].append(i)
            options[i,v]=[s for k in range(1,len(b)+1) for s in combinations(b,k) if v in s and nx.is_tree(g.subgraph(s))]
    @lru_cache(None)
    def rooted(v,parent):
        total=1
        for i in incident[v]:
            if i==parent:continue
            total+=max(sum(rooted(w,i) for w in s if w!=v) for s in options[i,v])
        return total
    return max(rooted(v,-1) for v in g)

def brute(g):
    return next(k for k in range(len(g),0,-1) if any(nx.is_tree(g.subgraph(s)) for s in combinations(g,k)))

def main():
    small=0
    for g in nx.graph_atlas_g():
        if 0<len(g)<=6 and nx.is_connected(g):
            require(exact_tree(g)==brute(g),list(g.edges()));small+=1
    print(f'Block-cut DP versus exhaustive subsets: {small} connected Atlas graphs of order 1-6')
    for heights in [(2,2,2,1)]+[(h,)*4 for h in range(2,6)]:
        g=build(heights); t=exact_tree(g)
        require(t==parameters(heights)[2] and 2*t<len(g),heights)
        print(f'{heights}: independently verified t={t}, n={len(g)}')
if __name__=='__main__':main()
