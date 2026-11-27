from itertools import combinations
import networkx as nx
from verify import invariants


def independent(T):
    n = len(T)
    A = [[T.has_edge(u,v) for v in range(n)] for u in range(n)]
    k = next(s for s in range(1,n+1)
             if any(all(any(A[v][u] for u in D) for v in range(n))
                    for D in combinations(range(n),s)))
    deg = [sum(row) for row in A]
    S = {v for v in range(n) if any(A[v][u] and deg[u]==1
                                    for u in range(n))}
    i = sum(not any(A[v][u] for u in S) for v in S)
    e = sum(A[u][v] and deg[u]==deg[v]==2
            for u in range(n) for v in range(u+1,n))
    return k,i,e


count=eq=0
for n in range(3,13):
    for T in nx.nonisomorphic_trees(n):
        k,i,e = independent(T)
        assert (k,i,e)==invariants(T)
        assert 3*(k-i)>=e+1
        count+=1
        eq+=k==i+(e+3)//3
assert (count,eq)==(985,95)
print("Independent subset audit: 985 trees; 95 strengthened equalities; no disagreements")
