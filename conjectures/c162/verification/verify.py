"""Exact supplementary verification of Graffiti.pc 162."""
from collections import Counter
from itertools import combinations
import networkx as nx

def require(condition, detail):
    if not condition:
        raise AssertionError(detail)

def local(g, v):
    ns = list(g[v])
    return max(k for k in range(len(ns)+1)
               if any(all(not g.has_edge(x,y) for x,y in combinations(s,2))
                      for s in combinations(ns,k)))

def leaves_dom(g):
    n = len(g)
    if n <= 2:
        return 2 if n == 2 else 0
    return n - next(k for k in range(1,n)
                    if any(nx.is_connected(g.subgraph(s)) and
                           all(v in s or any(u in g[v] for u in s) for v in g)
                           for s in combinations(g,k)))

def bound(g):
    vals = [local(g,v) for v in g]
    d = min(dict(g.degree()).values())
    return vals.count(min(vals)) * (1//d)

def main():
    counts, equality = Counter(), 0
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g):
            continue
        L, rhs = leaves_dom(g), bound(g)
        require(L >= rhs, (list(g.edges()), L, rhs))
        equality += min(dict(g.degree()).values()) == 1 and L == rhs
        counts[len(g)] += 1
    require(dict(counts) == {2:1,3:2,4:6,5:21,6:112,7:853}, counts)
    require(equality == 90, equality)
    print("C162: 995 connected graphs (orders 2–7); 90 equality cases with minimum degree 1; 0 violations")

if __name__ == "__main__":
    main()
