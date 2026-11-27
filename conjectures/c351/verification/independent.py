"""Standard-library verification of the explicit 55-vertex witness.
Exact lower bound: forced supports and disjoint support neighborhoods.
"""
import json
from pathlib import Path

w = json.loads(Path(__file__).with_name("witness.json").read_text())
V = set(w["vertices"])
assert len(V) == len(w["vertices"])
A = {v: set() for v in V}
for u, v in w["edges"]:
    assert u in V and v in V and u != v and v not in A[u]
    A[u].add(v)
    A[v].add(u)


def components(U):
    left = set(U)
    count = 0
    while left:
        count += 1
        stack = [left.pop()]
        while stack:
            v = stack.pop()
            neighbors = A[v] & left
            left -= neighbors
            stack.extend(neighbors)
    return count


assert components(V) == 1 and len(w["edges"]) == len(V)-1
L = {v for v in V if len(A[v]) == 1}
S = {u for v in L for u in A[v]}
Q = {v for v in V if len(A[v]) == 2}
b1 = components(S | L)
b2 = components(Q | {u for v in Q for u in A[v]})
D = set(w["selected"])
assert D <= V and len(D) == len(w["selected"])
assert all(A[v] & D for v in V)
# Each chosen support requires a vertex from its open neighborhood.
# The neighborhoods below are pairwise disjoint and disjoint from S.
m = w["m"]
chosen = ["a0"] + [f"e{i}_{j}_0" for i in range(m) for j in range(2)]
used = set(S)
for v in chosen:
    assert v in S and A[v] and not (used & A[v])
    used |= A[v]
lower = len(S) + len(chosen)
assert lower == len(D)
actual = dict(order=len(V), supports=len(S), support_components=b1,
              degree_two_neighborhood_components=b2,
              total_domination=lower, conjectured_bound=b1+b2)
assert actual == w["expected"] and b1+b2 > lower
print("Independent explicit-witness audit: n=55; exact gamma_t=28; bound=30; violation=2")
