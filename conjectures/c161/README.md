# Conjecture 161 — maximum local independence of the complement

**Status: NOT NOVEL — rediscovery of a previously implied bound. Excluded from the novel-resolution count.** See [novelty audit](../../NOVELTY.md).

Source: *Written on the Wall II*, conjecture 161, announced 2005-08-08; catalogue dated 2026-11-05, printed p. 92. See [source audit](SOURCES.md).

## Statement

For a finite simple connected graph G, let L_s(G) be the largest number of degree-one vertices in a spanning tree and let lambda_max(H) = max_v alpha(H[N_H(v)]), with alpha(empty) = 0. Then

**L_s(G) >= lambda_max(complement(G)).**

## Proof

In fact, any nonempty proper clique Q of a connected graph yields a spanning tree with at least |Q| leaves. Since Q is proper and G is connected, some q in Q is adjacent to w outside Q. Use the star centered at q on Q union {w}: its edges are qw and qu for every u in Q minus {q}. If |Q| >= 2 this star has |Q| leaves, and if |Q| = 1 the edge has two leaves. Extend the star by repeatedly joining an outside vertex with one edge; connectedness guarantees such an edge until the tree spans G. Adding a vertex to a leaf replaces that leaf with the new vertex, and adding to a nonleaf increases the number of leaves. Thus the number never decreases.

Set k = lambda_max(complement(G)). If k = 0 the desired inequality follows from nonnegativity. Otherwise a vertex v in the complement has an independent set Q of k neighbors. In G, Q is a clique, and v is outside Q. Apply the lemma. This proves the conjecture, including the one-vertex graph (both sides zero under the degree-one convention).

The bound is sharp: for a path on three vertices, the two end vertices each have a single complement neighbor and the bound is strict; for a path on four vertices, a complement neighborhood contains a two-vertex independent set, so both sides equal two.


## Research package

**An Elementary Note on Graffiti.pc Conjecture 161: Spanning-Tree Leaves and Complement Local Independence** — Koyar Afrasyab, November 2026. [Standalone manuscript](paper/paper.tex), [source audit](SOURCES.md), [primary verifier](verification/verify.py), [independent verifier](verification/independent.py), [expected output](verification/expected.txt).

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

## Prior result and novelty

The catalogue's October 2005 comment on conjecture 159 already records the stronger inequality L_s >= lambda_max(G)+omega(G)-2 for nontrivial graphs. For any connected noncomplete graph lambda_max(G)>=2 (use an internal vertex of a shortest path between nonadjacent vertices), hence L_s>=omega(G)>=lambda_max(complement(G)). For complete graphs the complement parameter is zero, including K1. In fact the elementary bound L_s>=Delta already suffices: a maximum proper clique has a boundary vertex of degree at least omega(G). This is therefore an independently presented proof of a previously implied result, not a claim of a new theorem.
