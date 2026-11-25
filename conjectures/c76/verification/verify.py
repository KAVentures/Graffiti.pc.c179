"""Construct C76 witnesses and verify exact recursive formulas."""
import networkx as nx

def require(ok, detail):
    if not ok:
        raise AssertionError(detail)

def build(heights):
    g = nx.cycle_graph(4)
    def attach(root, h):
        if h == 0:
            return
        a,b,c = range(len(g),len(g)+3)
        g.add_edges_from([(root,a),(a,b),(b,c),(c,root)])
        for v in (a,b,c):
            attach(v,h-1)
    for v,h in enumerate(heights):
        attach(v,h)
    return g

def rooted(h):
    return 2**(h+1)-1

def unrooted(h):
    return 1 if h == 0 else 3*(2**h-1)

def parameters(heights):
    n=sum((3**(h+1)-1)//2 for h in heights)
    m=4+sum(2*(3**h-1) for h in heights)
    t=max(sum(sorted(map(rooted,heights))[-3:]),max(map(unrooted,heights)))
    return n,m,t

def main():
    for heights in [(2,2,2,1)]+[(h,)*4 for h in range(2,7)]:
        g=build(heights); n,m,t=parameters(heights)
        freq=sum(x==0 for x in nx.triangles(g).values())
        require(nx.is_connected(g) and nx.is_bipartite(g) and max(dict(g.degree()).values())<=4,heights)
        require((len(g),g.number_of_edges(),freq)==(n,m,n),heights)
        require(2*m//n==2 and 2*t<n,heights)
        print(f'{heights}: n={n}, m={m}, t={t}, freq={freq}, floor_avg=2, deficit={(n-2*t)}/2')
if __name__=='__main__':main()
