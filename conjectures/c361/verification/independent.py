from itertools import combinations
import networkx as nx
from verify import invariants


def independent(T):
    n = len(T)
    A = [[T.has_edge(u, v) for v in range(n)] for u in range(n)]
    k = next(s for s in range(1, n + 1)
             if any(all(any(A[v][u] for u in D) for v in range(n))
                    for D in combinations(range(n), s)))
    deg = [sum(row) for row in A]
    S = {v for v in range(n) if any(A[v][u] and deg[u] == 1
                                    for u in range(n))}
    i = sum(not any(A[v][u] for u in S) for v in S)
    d = [[0 if u == v else 1 if A[u][v] else n + 1
          for v in range(n)] for u in range(n)]
    for h in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][h] + d[h][v])
    e = [max(row) for row in d]
    c = e.count(min(e))
    return k, i, c, S


count = eq = 0
for n in range(3, 13):
    for T in nx.nonisomorphic_trees(n):
        k, i, c, S = independent(T)
        assert (k, i, c, S) == invariants(T)
        assert k >= i + c
        count += 1
        eq += k == i + c
assert (count, eq) == (985, 179)
print("Independent subset / Floyd-Warshall audit: 985 trees; 179 equalities; no disagreements")
