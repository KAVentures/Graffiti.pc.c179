import networkx as nx


def invariants(T):
    n = len(T)
    S = {next(iter(T[v])) for v in T if T.degree(v) == 1}
    I = {v for v in S if not S.intersection(T[v])}
    e = sum(T.degree(u) == T.degree(v) == 2 for u, v in T.edges)
    masks = [sum(1 << u for u in T[v]) for v in range(n)]
    forced = sum(1 << s for s in S)
    k = min(m.bit_count() for m in range(1, 1 << n)
            if m & forced == forced and all(m & a for a in masks))
    return k, len(I), e


def sharp_family(m):
    T = nx.Graph()
    T.add_edge(0, 1)
    D = {0, 1}
    for j in range(m):
        arm = list(range(2 + 5*j, 7 + 5*j))
        nx.add_path(T, [0] + arm)
        D.update(arm[2:4])
    return T, D


def main():
    count = eq = 0
    for n in range(3, 13):
        for T in nx.nonisomorphic_trees(n):
            k, i, e = invariants(T)
            assert 3*(k-i) >= e+1
            count += 1
            eq += k == i+(e+3)//3
    assert (count, eq) == (985, 95)
    for m in range(2, 101):
        T, D = sharp_family(m)
        S = {next(iter(T[v])) for v in T if T.degree(v) == 1}
        i = sum(not S.intersection(T[v]) for v in S)
        e = sum(T.degree(u) == T.degree(v) == 2 for u, v in T.edges)
        assert nx.is_tree(T)
        assert (i, e, len(D)) == (m+1, 3*m, 2*m+2)
        assert all(D.intersection(T[v]) for v in T)
        assert len(D) == i+(e+3)//3
    print(f"C365: {count} nonisomorphic trees (orders 3–12); {eq} strengthened equality cases; 0 violations")


if __name__ == "__main__":
    main()
