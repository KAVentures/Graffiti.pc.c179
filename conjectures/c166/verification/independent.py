from collections import Counter
from itertools import combinations


def main():
    # Literal edge list, independent of the primary constructor and NetworkX.
    edges = [(0,1),(1,2),(2,3),(3,4),(4,6),(6,5),(5,3),(6,7),
             (0,8),(8,9),(9,10),(10,11),(11,13),(13,12),(12,10),(13,14),
             (0,15),(15,16),(16,17),(17,18),(18,20),(20,19),(19,17),(20,21)]
    n = 22
    adj = [set() for _ in range(n)]
    dist = [[0 if i == j else n for j in range(n)] for i in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
        dist[u][v] = dist[v][u] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    ecc = list(map(max,dist))
    maximum = max(map(len,adj))
    M = {i for i,a in enumerate(adj) if len(a) == maximum}
    boundary = set.union(*(adj[i] for i in M)) - M
    hist = Counter()
    # Check every possible 3-edge deletion using union-find.
    for deleted in combinations(range(len(edges)),3):
        parent = list(range(n)); deg = [0]*n
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for i,(u,v) in enumerate(edges):
            if i in deleted:
                continue
            a,b = root(u),root(v)
            if a == b:
                break
            parent[a] = b
            deg[u] += 1; deg[v] += 1
        else:
            hist[deg.count(1)] += 1
    gap = len(boundary)**2 - max(hist)**2 * min(ecc)
    if (maximum,len(M),len(boundary),min(ecc),max(ecc),dict(hist),gap) != (3,7,15,6,12,{6:64},9):
        raise AssertionError('independent verification failed')
    print('Independent exact verification: 64 spanning trees, 6 leaves each, squared violation 9')


if __name__ == '__main__':
    main()
