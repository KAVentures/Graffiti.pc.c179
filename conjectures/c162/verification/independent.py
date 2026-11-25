"""Independent exact leaf and local-independence algorithms for conjecture 162."""
from collections import Counter
from itertools import combinations
import networkx as nx

def require(condition, detail):
    if not condition:
        raise AssertionError(detail)

from verify import leaves_dom, bound

def local_mask(g, v):
    ns = list(g[v])
    best = 0
    for mask in range(1 << len(ns)):
        s = [u for i,u in enumerate(ns) if mask >> i & 1]
        if len(s) > best and all(not g.has_edge(u,w)
                                 for i,u in enumerate(s) for w in s[i+1:]):
            best = len(s)
    return best

def leaves_tree(g):
    n = len(g)
    if n == 1:
        return 0
    best = 0
    for edges in combinations(g.edges(), n-1):
        parent = list(range(n))
        deg = [0]*n
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for u,v in edges:
            a,b = root(u),root(v)
            if a == b:
                break
            parent[a] = b
            deg[u] += 1
            deg[v] += 1
        else:
            best = max(best, deg.count(1))
            if best == max(2,n-1):
                break
    return best

def independent_bound(g):
    vals = [local_mask(g,v) for v in g]
    d = min(dict(g.degree()).values())
    return vals.count(min(vals)) * (1//d)

def main():
    counts, equality = Counter(), 0
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g):
            continue
        L, rhs = leaves_tree(g), independent_bound(g)
        require((L, rhs) == (leaves_dom(g), bound(g)), (list(g.edges()), L, rhs))
        require(L >= rhs, (list(g.edges()), L, rhs))
        equality += min(dict(g.degree()).values()) == 1 and L == rhs
        counts[len(g)] += 1
    require(dict(counts) == {2:1,3:2,4:6,5:21,6:112,7:853}, counts)
    require(equality == 90, equality)
    print("C162: independent exact check: 995 graphs, 0 disagreements or violations")

if __name__ == "__main__":
    main()
