from itertools import combinations
import networkx as nx
from verify import invariants

count = eq = exceptional = 0
for n in range(3, 13):
    for T in nx.nonisomorphic_trees(n):
        k, i, med, up = invariants(T)
        k2 = next(j for j in range(2, n+1)
                  if any(all(any(u in T[v] for u in D) for v in T)
                         for D in combinations(T, j)))
        assert k == k2 and k >= i + up
        if k2 == i+1:
            assert med == up == 1
            exceptional += 1
        eq += k2 == i + up
        count += 1
assert (count, eq, exceptional) == (985, 54, 35)
print("Independent exact subset audit: 985 trees; 54 equalities; no disagreement")
