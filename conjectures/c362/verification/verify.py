import networkx as nx


def invariants(T):
    n = len(T)
    S = {next(iter(T[v])) for v in T if T.degree(v) == 1}
    q = nx.number_connected_components(T.subgraph(S))
    d, r = nx.diameter(T), nx.radius(T)
    masks = [sum(1 << u for u in T[v]) for v in range(n)]
    forced = sum(1 << s for s in S)
    k = min(m.bit_count() for m in range(1, 1 << n)
            if m & forced == forced and all(m & a for a in masks))
    return k, q, d, r


def sharp_family(m):
    T = nx.path_graph(5*m)
    D = {5*j+i for j in range(m) for i in (1, 2, 3)}
    for i in range(5*m):
        if i % 5 in (1, 3):
            T.add_edge(i, len(T))
    return T, D


def main():
    count = eq = 0
    for n in range(3, 13):
        for T in nx.nonisomorphic_trees(n):
            k, q, d, r = invariants(T)
            assert 5*(k-q) >= d+1
            assert 5*(k-q) >= 2*r
            assert 3*(k-q) >= r+1
            count += 1
            eq += k == q+(d+5)//5
    assert (count, eq) == (985, 465)
    for m in range(1, 101):
        T, D = sharp_family(m)
        S = {next(iter(T[v])) for v in T if T.degree(v) == 1}
        q = nx.number_connected_components(T.subgraph(S))
        d = nx.diameter(T)
        assert nx.is_tree(T)
        assert (q, d, len(D)) == (2*m, 5*m-1, 3*m)
        assert all(D.intersection(T[v]) for v in T)
        assert len(D) == q+(d+5)//5
    print(f"C362: {count} nonisomorphic trees (orders 3–12); {eq} strengthened equality cases; 0 violations; 100 sharp examples")


if __name__ == "__main__":
    main()
