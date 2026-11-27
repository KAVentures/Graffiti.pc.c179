from functools import lru_cache
from itertools import combinations
import networkx as nx

def cover(g):
    n = len(g)
    full = (1 << n) - 1
    ends = [0] * (1 << n)
    for i in range(n):
        ends[1 << i] = 1 << i
    for m in range(1, full + 1):
        for i in range(n):
            if ends[m] & (1 << i):
                for j in g[i]:
                    if not m & (1 << j):
                        ends[m | (1 << j)] |= 1 << j
    @lru_cache(None)
    def p(m):
        if not m:
            return 0
        if ends[m]:
            return 1
        return 1 + min(p(m ^ s) for s in range(1, m + 1)
                       if s & m == s and s & (m & -m) and ends[s])
    return p(full)

def induced_path(g):
    for k in range(len(g), 0, -1):
        for s in combinations(g, k):
            h = g.subgraph(s)
            if nx.is_connected(h) and h.number_of_edges() == k - 1 and max(dict(h.degree()).values()) <= 2:
                return k
    raise AssertionError("empty graph")

def main():
    count = eq = 0
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g):
            continue
        l, k = induced_path(g), cover(nx.complement(g))
        assert l * k >= 4
        if len(g) >= 3 and k == 2:
            assert l >= 3
        if nx.is_connected(nx.complement(g)):
            assert l >= 4
        count += 1
        eq += l * k == 4
    g = nx.empty_graph(1)
    assert induced_path(g) == cover(nx.complement(g)) == 1
    assert (count, eq) == (995, 304)
    print(f"C137: {count} connected graphs (orders 2–7); {eq} equality cases; 0 violations; singleton exception checked")

if __name__ == "__main__":
    main()
