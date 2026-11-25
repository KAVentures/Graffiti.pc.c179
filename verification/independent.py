"""Independent exact invariants; NetworkX is used only to supply Atlas graphs."""
from itertools import combinations
from collections import Counter
import networkx as nx


def invariants(n, edges):
    V = frozenset(range(n))
    E = frozenset(frozenset(e) for e in edges)
    neighbors = {v: frozenset(u for u in V if frozenset((u, v)) in E) for v in V}
    subsets = [frozenset(s) for k in range(n + 1) for s in combinations(range(n), k)]
    independent = [s for s in subsets if all(frozenset(e) not in E for e in combinations(s, 2))]
    b = max(len(a) + len(c) for a in independent for c in independent if not a & c)
    lam = max(len(s) for s in independent if any(s <= neighbors[v] for v in V))
    gamma = min(len(s) for s in subsets if all(v in s or neighbors[v] & s for v in V))
    delta = min(map(len, neighbors.values()))
    # Enumerate edge sets rather than connected dominating sets. Union-find tests acyclicity.
    L = 0
    for T in combinations(edges, n - 1):
        parent = list(range(n))
        degrees = [0] * n
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for u, v in T:
            a, c = root(u), root(v)
            if a == c:
                break
            parent[a] = c
            degrees[u] += 1
            degrees[v] += 1
        else:
            # n-1 acyclic edges on n vertices necessarily form a spanning tree.
            L = max(L, degrees.count(1))
            if L == max(2, n - 1):
                break
    return L, b, delta, gamma, lam


def main():
    from verify import invariants as primary
    counts = Counter()
    equality = 0
    for g in nx.graph_atlas_g():
        n = len(g)
        if n < 2:
            continue
        # Connectivity check independent of NetworkX graph algorithms.
        edges = list(g.edges())
        seen = {0}
        while True:
            more = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
            if more == seen:
                break
            seen = more
        if len(seen) != n:
            continue
        got = invariants(n, edges)
        if got != primary(g)[:5]:
            raise AssertionError((nx.to_graph6_bytes(g, header=False), got, primary(g)))
        L, b, delta, gamma, lam = got
        slack = L + b - delta - gamma - lam
        if slack < max(0, (lam + 1) // 2 - 2):
            raise AssertionError((edges, got))
        equality += slack == 0
        counts[n] += 1
    if dict(counts) != {2: 1, 3: 2, 4: 6, 5: 21, 6: 112, 7: 853} or equality != 8:
        raise AssertionError((counts, equality))
    print(f"Independent exact cross-check: {sum(counts.values())} graphs, {equality} equality cases, 0 disagreements or violations")


if __name__ == '__main__':
    main()
