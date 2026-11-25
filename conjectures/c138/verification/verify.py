import networkx as nx

def graph(k):
    g=nx.path_graph(2*k+1)
    g.add_edges_from([(0,2*k+1),(0,2*k+2),(2*k,2*k+3),(2*k,2*k+4)])
    return g

def mis(g,v,p):
    a,b=(1,1),(0,1)
    for w in g[v]:
        if w==p: continue
        x,y=mis(g,w,v)
        a=(a[0]+y[0],a[1]*y[1])
        z=x if x[0]>y[0] else y if y[0]>x[0] else (x[0],x[1]+y[1])
        b=(b[0]+z[0],b[1]*z[1])
    return a,b

def main():
    for k in (7,8,10,20,50,100):
        g=graph(k); sq=nx.power(g,2); delta=max(dict(sq.degree()).values()); M=sorted(v for v,d in sq.degree() if d==delta)
        a,b=mis(g,0,None); alpha,unique=max(a,b); count=a[1]+b[1] if a[0]==b[0] else unique
        path=nx.diameter(g)+1; d=nx.shortest_path_length(g,*M); ds=nx.shortest_path_length(sq,*M)
        assert nx.is_tree(g) and len(g)==2*k+5 and max(dict(g.degree()).values())==3
        assert (alpha,count,delta,M,path,d,ds)==(k+4,1,5,[1,2*k-1],2*k+3,2*k-2,k-1)
        assert path<3*ds<=3*d
        print(f'k={k}: n={len(g)}, alpha={alpha}, MIS count={count}, path={path}, square distance={ds}, deficit={3*ds-path}')
if __name__=='__main__':main()
