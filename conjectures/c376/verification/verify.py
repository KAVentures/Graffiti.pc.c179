import networkx as nx

def invariants(T):
    n = len(T)
    deg = dict(T.degree())
    M = {v for v in T if deg[v] == max(deg.values())}
    i = sum(not (set(T[v]) & M) for v in M)
    sums = [sum(d.values()) for _, d in nx.all_pairs_shortest_path_length(T)]
    med = sums.count(min(sums))
    up = sorted(deg.values())[n//2]
    masks = [sum(1 << u for u in T[v]) for v in range(n)]
    k = min(x.bit_count() for x in range(1, 1 << n) if all(x & m for m in masks))
    return k, i, med, up

def main():
    count = eq = exceptional = 0
    for n in range(3, 13):
        for T in nx.nonisomorphic_trees(n):
            k, i, med, up = invariants(T)
            assert k >= i + max(med, up)
            if k == i+1:
                assert med == up == 1
                exceptional += 1
            count += 1
            eq += k == i + med
    assert (count, eq, exceptional) == (985, 70, 35)
    print(f"C376: {count} trees (orders 3–12); {eq} equalities; {exceptional} excess-one cases; no violations")

if __name__ == "__main__":
    main()
