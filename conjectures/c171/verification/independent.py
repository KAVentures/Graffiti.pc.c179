from collections import Counter, deque
from fractions import Fraction


def check(r):
    # Independently label the arms and derive distances via queue traversal.
    adj = {('c',0): []}
    root = ('c',0)
    def edge(u,v):
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    for a in range(r+2):
        end = r if a == 0 else r-1
        for j in range(1,end+1):
            edge(root if j == 1 else (a,j-1), (a,j))
    for j in range(r):
        edge((1,r-1), ('leaf',j))
    def bfs(start):
        d = {start:0}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u]+1
                    q.append(v)
        assert len(d) == len(adj)
        return d
    n = len(adj)
    assert sum(map(len,adj.values())) == 2*(n-1)
    L = sum(len(v) == 1 for v in adj.values())
    ecc = {}
    even = 0
    for u in adj:
        d = bfs(u)
        ecc[u] = max(d.values())
        even = max(even,sum(x%2 == 0 for x in d.values()))
    B = [u for u in adj if ecc[u] == max(ecc.values())]
    hist = Counter(bfs(u)[v] for u in B for v in B if u != v)
    assert hist == {2:r*(r-1),2*r:2*r}
    D = Fraction(sum(d*k for d,k in hist.items()),sum(hist.values()))
    assert (n,L,even,len(B),D) == (r*(r+2),2*r+1,r*(r+2)//2,r+1,Fraction(6*r-2,r+1))
    assert L*D < even-2


if __name__ == '__main__':
    for r in (22,24,30,40):
        check(r)
    print('C171: independent standard-library check passed for 4 trees')
