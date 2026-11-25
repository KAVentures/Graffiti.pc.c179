"""Exact supplementary verification of Graffiti.pc 157."""
from collections import Counter
from itertools import combinations
from math import isqrt
import networkx as nx


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def leaves_dom(g):
    n = len(g)
    if n <= 2:
        return 2 if n == 2 else 0
    return n - next(k for k in range(1, n)
                    if any(nx.is_connected(g.subgraph(s)) and
                           all(v in s or any(u in g[v] for u in s) for v in g)
                           for s in combinations(g, k)))


def sharp(m):
    # Exact minimum s>=0 with binom(s,2)>=m.
    if m == 0:
        return 0
    s = (1 + isqrt(1 + 8*m)) // 2
    return s + (s*(s-1)//2 < m)


def radial(g, v):
    d = nx.single_source_shortest_path_length(g, v)
    return {u for u in g if d[u] == max(d.values())}


def check(g, L):
    p = {u for u in g if g.degree(u) == 1}
    for v in g:
        r = radial(g, v)
        t = nx.bfs_tree(g, v).to_undirected()
        s, m = len(r-p), g.subgraph(r).number_of_edges()
        require(nx.is_tree(t) and set(t) == set(g), (g, v))
        if len(g) > 1:
            require(p | r <= {u for u in t if t.degree(u) == 1}, (g, v))
            require(s*(s-1)//2 >= m and L >= len(p)+s, (g, v))
        require(L >= len(p)+sharp(m) and (L-len(p))**2 >= 2*m, (g, v))


def main():
    counts = Counter()
    for g in nx.graph_atlas_g():
        if not g or not nx.is_connected(g):
            continue
        check(g, leaves_dom(g))
        counts[len(g)] += 1
    require(dict(counts) == {1:1, 2:1, 3:2, 4:6, 5:21, 6:112, 7:853}, counts)
    for k in range(2, 12):
        for t in range(1, 12):
            g = nx.complete_graph(k+1)
            g.add_edges_from((0, k+i) for i in range(1, t+1))
            m = max(g.subgraph(radial(g, v)).number_of_edges() for v in nx.center(g))
            require(m == k*(k-1)//2 and sharp(m) == k, (k, t))
            check(g, len(g)-1)
    print("C157: 996 connected graphs (orders 1-7), 110 sharp-family cases; 0 violations")


if __name__ == "__main__":
    main()
