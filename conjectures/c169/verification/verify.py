"""Exact supplementary verification of Graffiti.pc 169."""
from collections import Counter
from itertools import combinations
import networkx as nx

def require(condition, detail):
    if not condition:
        raise AssertionError(detail)

def leaves_dom(g):
    n = len(g)
    if n <= 2:
        return 2 if n == 2 else 0
    return n - next(k for k in range(1,n)
                    if any(nx.is_connected(g.subgraph(s)) and
                           all(v in s or any(u in g[v] for u in s) for v in g)
                           for s in combinations(g,k)))

def even_counts(g):
    return [sum(d % 2 == 0 for d in nx.single_source_shortest_path_length(g,v).values()) for v in g]

def main():
    counts, equality = Counter(), 0
    single = nx.empty_graph(1)
    require(leaves_dom(single) == 0 and even_counts(single) == [1], "singleton convention")
    for g in nx.graph_atlas_g():
        n = len(g)
        if n < 2 or not nx.is_connected(g):
            continue
        L, es = leaves_dom(g), even_counts(g)
        rhs = 1 + max(es) - min(es)
        require(L >= rhs, list(g.edges()))
        for v,e in zip(g,es):
            t = nx.bfs_tree(g,v).to_undirected()
            require(nx.is_tree(t) and set(t) == set(g), (g,v))
            leaves = sum(d == 1 for _,d in t.degree())
            require(abs(2*e-n) <= leaves-1 <= L-1, (g,v))
        counts[n] += 1
        equality += L == rhs
    require(dict(counts) == {2:1,3:2,4:6,5:21,6:112,7:853}, counts)
    require(equality == 85, equality)
    for n in range(3,101):
        g = nx.star_graph(n-1)
        es = even_counts(g)
        require(n-1 == 1+max(es)-min(es), n)
    print("C169: 995 connected graphs (orders 2-7), 85 equality cases; 0 violations")
    print("Singleton convention checked; 98 sharp star examples checked")

if __name__ == "__main__":
    main()
