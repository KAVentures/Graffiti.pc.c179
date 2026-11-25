from itertools import combinations
from collections import Counter
import networkx as nx


def graph():
    g = nx.Graph()
    for i in range(3):
        a,b,u,x,y,v,z = range(1+7*i, 8+7*i)
        g.add_edges_from([(0,a),(a,b),(b,u),(u,x),(x,v),(v,y),(y,u),(v,z)])
    return g


def main():
    g = graph()
    n, m = g.number_of_nodes(), g.number_of_edges()
    delta = max(dict(g.degree()).values())
    M = {v for v,d in g.degree() if d == delta}
    boundary = {w for v in M for w in g[v]} - M
    radius, diameter = nx.radius(g), nx.diameter(g)
    counts = Counter()
    for edges in combinations(g.edges(), n-1):
        t = nx.Graph()
        t.add_nodes_from(g)
        t.add_edges_from(edges)
        if nx.is_tree(t):
            counts[sum(d == 1 for _,d in t.degree())] += 1
    L = max(counts)
    gap = len(boundary)**2 - L**2 * radius
    if (n,m,delta,len(M),len(boundary),radius,diameter,dict(counts),gap) != (22,24,3,7,15,6,12,{6:64},9):
        raise AssertionError('unexpected invariants')
    print(f'n={n} m={m} Delta={delta} |M|={len(M)} boundary={len(boundary)} radius={radius} diameter={diameter}')
    print(f'spanning trees={sum(counts.values())} leaf histogram={dict(counts)}')
    print(f'exact squared violation={gap}')


if __name__ == '__main__':
    main()
