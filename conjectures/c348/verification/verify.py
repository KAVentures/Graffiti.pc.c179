from itertools import product
import networkx as nx


def total_domination(T):
    """Tree DP: states are (parent selected, vertex selected)."""
    def solve(v, p):
        children = [solve(u, v) for u in T[v] if u != p]
        out = {}
        for x, y in product(range(2), repeat=2):
            z0, z1 = 0, float("inf")
            for child in children:
                a, b = child[x, 0], child[x, 1]
                z0, z1 = z0 + a, min(z1 + min(a, b), z0 + b)
            out[y, x] = x + (min(z0, z1) if y else z1)
        return out
    root = solve(next(iter(T)), None)
    return int(min(root[0, 0], root[0, 1]))


def boundary(T):
    return {v for v in T if T.degree(v) != 2
            and any(T.degree(u) == 2 for u in T[v])}


def main():
    count = eq = 0
    for n in range(3, 14):
        for T in nx.nonisomorphic_trees(n):
            k, b = total_domination(T), len(boundary(T))
            assert 4*k >= 3*b+2
            assert 3*k >= 2*b
            count += 1
            eq += k == (3*b+5)//4
    assert (count, eq) == (2286, 103)
    print(f"C348: {count} nonisomorphic trees (orders 3–13); {eq} strengthened equality cases; 0 violations")


if __name__ == "__main__":
    main()
