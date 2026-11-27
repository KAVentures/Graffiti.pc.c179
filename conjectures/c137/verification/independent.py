from itertools import permutations
import networkx as nx
from verify import cover, induced_path

def longest(a):
    n = len(a)
    def extend(path):
        best = len(path)
        for v in range(n):
            if v not in path and a[path[-1]][v] and all(not a[u][v] for u in path[:-1]):
                best = max(best, extend(path + (v,)))
        return best
    return max(extend((i,)) for i in range(n))

def min_cover(a):
    # A permutation split at missing complement edges is a path cover;
    # concatenating any optimal cover gives a permutation with no more breaks.
    return min(1 + sum(a[u][v] for u, v in zip(p, p[1:]))
               for p in permutations(range(len(a))))

count = eq = 0
for g in nx.graph_atlas_g():
    if len(g) < 2 or not nx.is_connected(g):
        continue
    a = [[g.has_edge(i, j) for j in range(len(g))] for i in range(len(g))]
    l, k = longest(a), min_cover(a)
    assert (l, k) == (induced_path(g), cover(nx.complement(g)))
    assert l * k >= 4
    count += 1
    eq += l * k == 4
assert (count, eq) == (995, 304)
assert longest([[False]]) == min_cover([[False]]) == 1
print("Independent permutation/induced-path DFS audit: 995 graphs; 304 equalities; no disagreements")
