"""Exact supplementary checks of Graffiti.pc 179. No search is needed by the proof."""
from collections import Counter
from itertools import combinations
import networkx as nx


def check(condition, graph, label):
    if not condition:
        raise AssertionError((label, nx.to_graph6_bytes(graph, header=False).decode().strip()))


def invariants(graph):
    n = len(graph)
    subsets = sorted(range(1, 1 << n), key=int.bit_count)
    adj = [sum(1 << u for u in graph[v]) for v in graph]
    full = (1 << n) - 1

    def vertices(s):
        return [i for i in range(n) if s >> i & 1]

    def dominates(s):
        covered = s
        for v in vertices(s):
            covered |= adj[v]
        return covered == full

    def independent(s):
        return all(not (adj[v] & s) for v in vertices(s))

    gamma = next(s.bit_count() for s in subsets if dominates(s))
    gamma_c = next(s.bit_count() for s in subsets if dominates(s)
                   and nx.is_connected(graph.subgraph(vertices(s))))
    b = max(s.bit_count() for s in subsets
            if nx.is_bipartite(graph.subgraph(vertices(s))))
    lam = max(s.bit_count() for s in subsets if independent(s)
              and any(s & ~a == 0 for a in adj))
    delta = min(map(int.bit_count, adj))
    Delta = max(map(int.bit_count, adj))
    L = 2 if n == 2 else n - gamma_c
    return L, b, delta, gamma, lam, Delta, gamma_c


def direct_leaf_count(graph):
    """Independent leaf computation: enumerate every n-1 edge subset."""
    n = len(graph)
    best = 0
    for edges in combinations(graph.edges(), n - 1):
        tree = nx.Graph()
        tree.add_nodes_from(graph)
        tree.add_edges_from(edges)
        if nx.is_connected(tree):
            # A connected n-vertex graph with n-1 edges is a tree.
            best = max(best, sum(d == 1 for _, d in tree.degree()))
    return best


def verify(graph):
    n = len(graph)
    L, b, delta, gamma, lam, Delta, gamma_c = invariants(graph)
    slack = L + b - delta - gamma - lam
    check(lam >= 1, graph, "positive local independence")
    check(gamma <= n - lam - delta + 2, graph, "domination lemma")
    check(gamma <= n - Delta, graph, "maximum degree bound")
    check(L + b >= n + (lam + 1) // 2, graph, "published theorem")
    check(slack >= max(0, (lam + 1) // 2 - 2), graph, "strengthened conjecture")
    check(gamma_c <= n + b - delta - gamma - lam - max(0, (lam + 1) // 2 - 2),
          graph, "connected domination corollary")
    if gamma == n - delta and lam == 2:
        check(all(d == 1 for _, d in nx.complement(graph).degree()),
              graph, "exceptional complete multipartite structure")
    return slack, L


def independent_domination(g):
    for k in range(1, len(g)+1):
        for s in combinations(g, k):
            if all(not g.has_edge(u,v) for u,v in combinations(s,2)) and all(v in s or any(u in g[v] for u in s) for v in g):
                return k
    raise AssertionError('no independent dominating set')


def main():
    counts = Counter()
    equalities = Counter()
    direct = 0
    max_eq = 0
    for graph in nx.graph_atlas_g():
        n = len(graph)
        if n < 2 or not nx.is_connected(graph):
            continue
        graph = nx.convert_node_labels_to_integers(graph, ordering="sorted")
        counts[n] += 1
        slack, L = verify(graph)
        _, b, _, gamma, lam, Delta, _ = invariants(graph)
        i = independent_domination(graph)
        check(b >= lam+i and L >= Delta and L+b >= Delta+i+lam >= Delta+gamma+lam, graph, 'maximum degree and independent domination')
        max_eq += L+b == Delta+i+lam
        if slack == 0:
            equalities[n] += 1
        if n <= 6 or slack == 0:
            check(direct_leaf_count(graph) == L, graph, "direct spanning-tree audit")
            direct += 1
    expected_counts = {2: 1, 3: 2, 4: 6, 5: 21, 6: 112, 7: 853}
    expected_equalities = {3: 1, 4: 2, 5: 2, 6: 2, 7: 1}
    if dict(counts) != expected_counts or dict(equalities) != expected_equalities or direct != 143:
        raise AssertionError((counts, equalities, direct))
    # Infinite sharpness families sampled separately.
    for n in range(3, 11):
        g = nx.complete_graph(n)
        check(verify(g)[0] == 0, g, "complete graph sharpness")
    for k in range(2, 6):
        g = nx.complete_multipartite_graph(*([2] * k))
        check(verify(g)[0] == 0, g, "multipartite sharpness")
    print("Graphs checked:", sum(counts.values()), dict(counts))
    print("Equality cases:", sum(equalities.values()), dict(equalities))
    print("Direct spanning-tree cross-checks:", direct)
    print("Sharpness family samples: 12")
    if max_eq != 453:
        raise AssertionError(max_eq)
    print("Violations: 0")
    print("Maximum-degree independent-domination equality cases: 453; violations: 0")


if __name__ == "__main__":
    main()
