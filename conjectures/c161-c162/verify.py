"""Exact supplementary checks of Graffiti.pc 161 and 162."""
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

def main():
    counts, eq = Counter(), Counter()
    single = nx.empty_graph(1)
    require(leaves_dom(single) == leaves_tree(single) == local(nx.complement(single),0) == 0, "singleton")
    for g in nx.graph_atlas_g():
        n = len(g)
        if n < 2 or not nx.is_connected(g):
            continue
        L = leaves_dom(g)
        require(L == leaves_tree(g), (g.edges(), "leaf disagreement"))
        complement = nx.complement(g)
        rhs1 = max(local(complement,v) for v in g)
        vals = [local(g,v) for v in g]
        d = min(dict(g.degree()).values())
        rhs2 = vals.count(min(vals)) * (1//d)
        require(L >= rhs1 and L >= rhs2, (g.edges(), L, rhs1, rhs2))
        counts[n] += 1
        eq[161] += L == rhs1
        eq[162] += d == 1 and L == rhs2
    require(dict(counts) == {2:1,3:2,4:6,5:21,6:112,7:853}, counts)
    require(dict(eq) == {161:44,162:90}, eq)
    print("995 connected graphs (orders 2–7); singleton checked separately")
    print("C161: 44 equality cases; 0 violations")
    print("C162: 90 equality cases with minimum degree 1; 0 violations")
    print("0 leaf-number disagreements")

if __name__ == "__main__":
    main()
