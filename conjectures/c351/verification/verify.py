import networkx as nx


def family(m):
    assert m >= 3
    T = nx.Graph()
    T.add_node("r")
    D = {"r"}
    for i in range(m):
        a, u, b = f"a{i}", f"u{i}", f"b{i}"
        nx.add_path(T, ["r", a, u, b])
        T.add_edge(a, f"la{i}")
        D.add(a)
        for j in range(2):
            c, d = f"c{i}_{j}", f"d{i}_{j}"
            nx.add_path(T, [b, c, d])
            T.add_edge(c, f"lc{i}_{j}")
            D.update([c, d])
            for h in range(2):
                e, f = f"e{i}_{j}_{h}", f"f{i}_{j}_{h}"
                nx.add_path(T, [d, e, f])
                D.add(e)
    return T, D


def invariants(T):
    L = {v for v in T if T.degree(v) == 1}
    S = {u for v in L for u in T[v]}
    Q = {v for v in T if T.degree(v) == 2}
    U = Q | {u for v in Q for u in T[v]}
    return len(S), nx.number_connected_components(T.subgraph(S | L)), nx.number_connected_components(T.subgraph(U))


def total_domination(T):
    """Four-state rooted tree DP; parent/vertex selection bits."""
    root = next(iter(T))
    parent = {root: None}
    order = [root]
    for v in order:
        for u in T[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    out = {}
    for v in reversed(order):
        states = {}
        for p in (0, 1):
            for x in (0, 1):
                no, yes = 0, float("inf")
                for u in T[v]:
                    if parent.get(u) != v:
                        continue
                    a, b = out[u][x, 0], out[u][x, 1]
                    no, yes = no+a, min(yes+min(a,b), no+b)
                states[p, x] = x + (min(no,yes) if p else yes)
        out[v] = states
    return min(out[root][0,0], out[root][0,1])


def main():
    for m in range(3, 103):
        T, D = family(m)
        assert nx.is_tree(T) and len(T) == 18*m+1
        assert invariants(T) == (7*m, 7*m, 3*m)
        assert len(D) == 9*m+1 and all(D.intersection(T[v]) for v in T)
        assert total_domination(T) == len(D)
        assert 10*m-len(D) == m-1 > 0
    print("C351: 100 counterexample family members (m=3–102); m=3: n=55, gamma_t=28, bound=30; all exact formulas verified")


if __name__ == "__main__":
    main()
