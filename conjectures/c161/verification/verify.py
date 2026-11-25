"""Exact supplementary verification of Graffiti.pc 161."""
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
    return max(local(nx.complement(g),v) for v in g)

def main():
    counts, equality = Counter(), 0
    g = nx.empty_graph(1)
    require(leaves_dom(g) == bound(g) == 0, "singleton")
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g):
            continue
        L, rhs = leaves_dom(g), bound(g)
        require(L >= rhs, (list(g.edges()), L, rhs))
        equality += L == rhs
        counts[len(g)] += 1
    require(dict(counts) == {2:1,3:2,4:6,5:21,6:112,7:853}, counts)
    require(equality == 44, equality)
    print("C161: 995 connected graphs (orders 2–7); singleton checked separately; 44 equality cases; 0 violations")

if __name__ == "__main__":
    main()
