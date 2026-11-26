import networkx as nx


def invariants(T):
    n = len(T)
    S = {next(iter(T[v])) for v in T if T.degree(v) == 1}
    i = sum(not (set(T[v]) & S) for v in S)
    c = len(nx.center(T))
    masks = [sum(1 << u for u in T[v]) for v in range(n)]
    forced = sum(1 << s for s in S)
    k = min(m.bit_count() for m in range(1, 1 << n)
            if m & forced == forced and all(m & a for a in masks))
    return k, i, c, S


def minimal_excess_family(T, S):
    if len(S) == 1:
        return all(T.degree(v) == 1 for v in T if v not in S)
    for x in set(T) - S:
        if set(T[x]) != S:
            continue
        if all(T.degree(v) == 1 and next(iter(T[v])) in S
               for v in set(T) - S - {x}):
            return True
    return False


def main():
    count = eq = 0
    for n in range(3, 13):
        for T in nx.nonisomorphic_trees(n):
            k, i, c, S = invariants(T)
            assert k >= i + c
            if i > 0:
                assert (k == i + 1) == minimal_excess_family(T, S)
            count += 1
            eq += k == i + c
    assert (count, eq) == (985, 179)
    print(f"C361: {count} nonisomorphic trees (orders 3–12); {eq} equality cases; 0 violations")


if __name__ == "__main__":
    main()
