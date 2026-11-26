import networkx as nx
from verify import total_domination, boundary


def exhaustive(T):
    nodes = list(T)
    ix = {v: j for j, v in enumerate(nodes)}
    masks = [sum(1 << ix[u] for u in T[v]) for v in nodes]
    return min(m.bit_count() for m in range(1, 1 << len(nodes))
               if all(m & a for a in masks))


def independent_boundary(T):
    deg = dict(T.degree())
    B = set()
    for u, v in T.edges():
        if deg[u] == 2 and deg[v] != 2:
            B.add(v)
        if deg[v] == 2 and deg[u] != 2:
            B.add(u)
    return B


count = 0
for n in range(3, 13):
    for T in nx.nonisomorphic_trees(n):
        k, B = exhaustive(T), independent_boundary(T)
        assert k == total_domination(T)
        assert B == boundary(T)
        assert 4*k >= 3*len(B)+2
        count += 1
assert count == 985
print("Independent bitmask audit: 985 trees; no disagreements or violations")
