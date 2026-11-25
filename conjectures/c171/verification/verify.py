from fractions import Fraction
from itertools import combinations
import networkx as nx


def build(r):
    g = nx.Graph()
    g.add_node(0)
    def arm(length):
        v = 0
        for _ in range(length):
            w = len(g)
            g.add_edge(v, w)
            v = w
        return v
    arm(r)
    hub = arm(r-1)
    for _ in range(r):
        g.add_edge(hub, len(g))
    for _ in range(r):
        arm(r-1)
    return g


def check(r):
    g = build(r)
    assert nx.is_tree(g)
    n = len(g)
    L = sum(d == 1 for _, d in g.degree())
    ecc = {}
    even = 0
    for v, ds in nx.all_pairs_shortest_path_length(g):
        ecc[v] = max(ds.values())
        even = max(even, sum(d % 2 == 0 for d in ds.values()))
    diameter = max(ecc.values())
    B = [v for v in g if ecc[v] == diameter]
    pairs = list(combinations(B, 2))
    D = Fraction(sum(nx.shortest_path_length(g,u,v) for u,v in pairs), len(pairs))
    assert (n,L,even,diameter,len(B),D) == (r*(r+2),2*r+1,r*(r+2)//2,2*r,r+1,Fraction(6*r-2,r+1))
    rhs = (even-1)/D
    assert rhs > L and (even-2)/D > L
    print(f'r={r}: n={n}, L={L}, even={even}, B={len(B)}, D={D}, RHS={rhs}')


if __name__ == '__main__':
    for r in (22,24,30,40):
        check(r)
