from collections import deque
from functools import lru_cache

def check(k):
    n=2*k+5; adj=[set() for _ in range(n)]
    for u,v in [(i,i+1) for i in range(2*k)]+[(0,2*k+1),(0,2*k+2),(2*k,2*k+3),(2*k,2*k+4)]:
        adj[u].add(v);adj[v].add(u)
    def bfs(a,v):
        d={v:0}; q=deque([v])
        while q:
            x=q.popleft()
            for y in a[x]:
                if y not in d:d[y]=d[x]+1;q.append(y)
        return d
    dist=[bfs(adj,v) for v in range(n)]
    assert all(len(d)==n for d in dist) and sum(map(len,adj))==2*(n-1)
    sq=[{w for w,d in row.items() if 0<d<=2} for row in dist]
    M=[v for v in range(n) if len(sq[v])==max(map(len,sq))]
    masks=[sum(1<<w for w in a) for a in adj]
    @lru_cache(None)
    def opt(mask):
        if not mask:return 0,1
        bit=mask&-mask;v=bit.bit_length()-1;rest=mask^bit
        a,c=opt(rest);b,d=opt(rest&~masks[v]);b+=1
        return (a,c) if a>b else (b,d) if b>a else (a,c+d)
    alpha,count=opt((1<<n)-1)
    path=1+max(max(d.values()) for d in dist)
    assert M==[1,2*k-1] and max(map(len,sq))==5
    ds=bfs(sq,M[0])[M[1]];d=dist[M[0]][M[1]]
    assert (alpha,count,path,ds,d)==(k+4,1,2*k+3,k-1,2*k-2)
    assert path<3*ds<=3*d
    return path,ds

if __name__=='__main__':
    for k in (7,8,10,20,50,100):
        p,d=check(k);print(f'k={k}: independently verified {p} < {3*d}')
