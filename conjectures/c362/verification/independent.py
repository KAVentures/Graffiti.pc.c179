from itertools import combinations
import networkx as nx
from verify import invariants


def independent(T):
    n = len(T)
    A = [[T.has_edge(u, v) for v in range(n)] for u in range(n)]
    k = next(s for s in range(2, n+1)
             if any(all(any(A[v][u] for u in D) for v in range(n))
                    for D in combinations(range(n), s)))
    deg = [sum(row) for row in A]
    # Count components directly in the union of supports and leaves.
    U = {v for v in range(n) if deg[v] == 1 or
         any(A[v][u] and deg[u] == 1 for u in range(n))}
    q = len(U) - sum(A[u][v] for u in U for v in U if u < v)
    d = [[0 if u == v else 1 if A[u][v] else n+1
          for v in range(n)] for u in range(n)]
    for h in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][h]+d[h][v])
    e = [max(row) for row in d]
    return k, q, max(e), min(e)


count = eq = 0
for n in range(3, 13):
    for T in nx.nonisomorphic_trees(n):
        k, q, d, r = independent(T)
        assert (k, q, d, r) == invariants(T)
        assert 5*(k-q) >= d+1 and 5*(k-q) >= 2*r and 3*(k-q) >= r+1
        count += 1
        eq += k == q+(d+5)//5
assert (count, eq) == (985, 465)
print("Independent subset / Floyd-Warshall audit: 985 trees; 465 equalities; no disagreements")
