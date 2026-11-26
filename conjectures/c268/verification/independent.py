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
    ecc = [max(row) for row in d]
    C = [i for i in range(n) if ecc[i] == min(ecc)]
    vals = [d[i][j] for i in C for j in C if i != j]
    bound = 1 + sum(vals)//max(1,len(vals))
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
assert (count,eq) == (995,650)
print("Independent bitmask / Floyd-Warshall audit: 995 graphs; 650 equalities; no disagreements")
