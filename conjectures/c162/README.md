# Conjecture 162 — frequency of minimum local independence

Source: *Written on the Wall II*, conjecture 162, announced 2005-08-08; catalogue dated 2026-11-05, printed p. 93. See [source audit](SOURCES.md).

## Statement

For finite simple connected G with at least two vertices, let lambda(v) = alpha(G[N_G(v)]), let f count vertices attaining min_v lambda(v), and let delta be minimum degree. Then

**L_s(G) >= f floor(1/delta).**

The order restriction is necessary for the expression to be defined.

## Proof

If delta >= 2 the right-hand side vanishes. If delta = 1, every vertex has a nonempty neighborhood and some vertex has degree one, so min_v lambda(v) = 1. The vertices attaining this minimum are exactly the simplicial vertices (vertices whose neighborhoods are cliques). Write S for their set.

If G is complete and delta = 1, then G is K_2 and the two sides are both 2.

Otherwise the subgraph H induced by V(G) minus S is nonempty: if every vertex were simplicial, a shortest path between two nonadjacent vertices would have an internal vertex with two nonadjacent neighbors, a contradiction. The same shortest-path argument between any two vertices of H shows H is connected, since all internal vertices on a shortest path are nonsimplicial.

Each s in S has a neighbor in H. Indeed, if all its neighbors were simplicial, choose any neighbor t. Every neighbor of t other than s is adjacent to s, because N(t) is a clique containing s. Hence there is no edge from N[s] to its complement. Connectedness forces N[s] = V(G), and N[s] is a clique, contrary to G being noncomplete.

Choose a spanning tree of H (a single vertex is allowed). Attach every s in S by one edge to H. The resulting graph is a spanning tree and each s is a leaf. Therefore L_s(G) >= |S| = f. Since floor(1/delta) = 1 in this case, the result follows.

The argument establishes the stronger statement that every connected noncomplete graph admits a spanning tree in which all simplicial vertices are leaves. Equality occurs for K_2 and for every nontrivial tree of minimum degree one.


## Research package

**A Proof of Graffiti.pc Conjecture 162: Spanning-Tree Leaves and Simplicial Vertices** — Koyar Afrasyab, November 2026. [Standalone manuscript](paper/paper.tex), [source audit](SOURCES.md), [primary verifier](verification/verify.py), [independent verifier](verification/independent.py), [expected output](verification/expected.txt).

## Reproduce

From this folder, Python 3.12 and TeX Live:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The exact algorithms were cross-checked locally on 995 graphs; CI is configured to reproduce the standalone package and build its PDF. No claim of external peer review, formal certification or priority is made. AI assistance is disclosed.

## Additional reproducibility check

The [cross-conjecture audit](../../audit/README.md) checks all three statements and proof constructions through direct enumeration, with recorded output. It supplements the standalone checks and is not needed for the proof.

## Prior related work

Pablo De Caria Di Fonzo, Cycle intersection in spanning trees: A shorter proof of a conjecture and applications, Discrete Applied Mathematics 350 (2024), 10–14, DOI 10.1016/j.dam.2024.01.018, Proposition 3.1, proves a related all-simplicial-vertices-as-leaves result for noncomplete chordal graphs, even for an optimal tree for a different objective. Its exchange argument uses no chordality beyond the proposition's stated domain when only leaf preservation is needed. Our core-based construction is an elementary independent derivation, not an assertion of priority for the underlying fact. [Published article](https://doi.org/10.1016/j.dam.2024.01.018). Do not count as established novel.
