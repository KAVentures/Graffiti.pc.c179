from itertools import combinations
from math import isqrt
import networkx as nx


def total_domination(g):
    V = list(g)
    return next(s for s in range(2, len(V)+1)
                if any(all(any(g.has_edge(v,u) for u in S) for v in V)
                       for S in combinations(V,s)))


def rhs(g):
    d = dict(nx.all_pairs_shortest_path_length(g))
    M = [v for v in g if g.degree(v) == max(dict(g.degree()).values())]
    D = max(d[u][v] for u in M for v in M)
    return 0 if D == 0 else 1 + isqrt(2*D-1)


def main():
    count = eq = 0
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g):
            continue
        k, bound = total_domination(g), rhs(g)
        assert k >= bound, nx.to_graph6_bytes(g)
        count += 1
        eq += k == bound
    assert (count,eq) == (995,372)
    print(f"C271: {count} connected graphs (orders 2–7); {eq} equality cases; 0 violations")


if __name__ == "__main__":
    main()
