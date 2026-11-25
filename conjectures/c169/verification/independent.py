"""Independent direct spanning-tree and Floyd-Warshall checks for C169."""
from itertools import combinations
from collections import Counter
import networkx as nx
from verify import leaves_dom, require, even_counts

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
        for u, v in edges:
            a, b = root(u), root(v)
            if a == b:
                break
            parent[a] = b
            deg[u] += 1
            deg[v] += 1
        else:
            best = max(best, deg.count(1))
            if best == max(2, n-1):
                break
    return best


def main():
    counts, equality = Counter(), 0
    for g in nx.graph_atlas_g():
        n = len(g)
        if n < 2 or not nx.is_connected(g):
            continue
        L = leaves_tree(g)
        require(L == leaves_dom(g), list(g.edges()))
        vertices = list(g)
        d = [[0 if u == v else 1 if g.has_edge(u,v) else n for v in vertices] for u in vertices]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k]+d[k][j])
        es = [sum(x % 2 == 0 for x in row) for row in d]
        require(es == even_counts(g), list(g.edges()))
        require(all(abs(2*e-n) <= L-1 for e in es), list(g.edges()))
        rhs = 1 + max(es) - min(es)
        require(L >= rhs, list(g.edges()))
        counts[n] += 1
        equality += L == rhs
    require(dict(counts) == {2:1,3:2,4:6,5:21,6:112,7:853}, counts)
    require(equality == 85, equality)
    require(leaves_tree(nx.empty_graph(1)) == 0, "singleton")
    print("C169: independent exact check: 995 graphs, 85 equalities, 0 disagreements or violations")

if __name__ == "__main__":
    main()
