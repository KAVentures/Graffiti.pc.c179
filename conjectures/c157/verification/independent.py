"""Independent exact spanning-tree and distance algorithms for C157."""
from itertools import combinations
import networkx as nx
from verify import leaves_dom, require, sharp


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
    count = 0
    for g in nx.graph_atlas_g():
        if not g or not nx.is_connected(g):
            continue
        n = len(g)
        L = leaves_tree(g)
        require(L == leaves_dom(g), list(g.edges()))
        p = {u for u in g if sum(u in e for e in g.edges()) == 1}
        d = [[0 if u == v else 1 if g.has_edge(u,v) else n for v in g] for u in g]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k]+d[k][j])
        for i in range(n):
            r = {j for j in range(n) if d[i][j] == max(d[i])}
            m = sum(u in r and v in r for u,v in g.edges())
            b = next(s for s in range(n+1) if s*(s-1)//2 >= m)
            require(b == sharp(m) and L >= len(p)+b and (L-len(p))**2 >= 2*m, (g,i))
            if n > 1:
                require(L >= len(p)+len(r-p), (g,i))
        count += 1
    require(count == 996, count)
    print("C157: independent exact check: 996 graphs, 0 disagreements or violations")


if __name__ == "__main__":
    main()
