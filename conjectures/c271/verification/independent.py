from math import isqrt
import networkx as nx
from verify import total_domination, rhs


def independent(g):
    n = len(g)
    A = [[g.has_edge(u,v) for v in range(n)] for u in range(n)]
    masks = [sum(1<<j for j in range(n) if A[i][j]) for i in range(n)]
    k = min(m.bit_count() for m in range(1,1<<n) if all(m & a for a in masks))
    d = [[0 if i==j else 1 if A[i][j] else n+1 for j in range(n)] for i in range(n)]
    for h in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][h]+d[h][j])
    deg = [a.bit_count() for a in masks]
    M = [i for i in range(n) if deg[i] == max(deg)]
    D = max(d[i][j] for i in M for j in M)
    bound = next(t for t in range(n+1) if t*t >= 2*D)
    return k, bound


count = eq = 0
for g in nx.graph_atlas_g():
    if len(g) < 2 or not nx.is_connected(g):
        continue
    k, b = independent(g)
    assert (k,b) == (total_domination(g),rhs(g))
    assert k >= b
    count += 1
    eq += k == b
assert (count,eq) == (995,372)
print("Independent bitmask / Floyd-Warshall audit: 995 graphs; 372 equalities; no disagreements")
