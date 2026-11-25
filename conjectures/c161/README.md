# Conjecture 161 — maximum local independence of the complement

Source: *Written on the Wall II*, conjecture 161, announced 2005-08-08; catalogue dated 2026-11-05, printed p. 92. See [source audit](../c161-c162/SOURCES.md).

## Statement

For a finite simple connected graph G, let L_s(G) be the largest number of degree-one vertices in a spanning tree and let lambda_max(H) = max_v alpha(H[N_H(v)]), with alpha(empty) = 0. Then

**L_s(G) >= lambda_max(complement(G)).**

## Proof

In fact, any nonempty proper clique Q of a connected graph yields a spanning tree with at least |Q| leaves. Since Q is proper and G is connected, some q in Q is adjacent to w outside Q. Use the star centered at q on Q union {w}: its edges are qw and qu for every u in Q minus {q}. If |Q| >= 2 this star has |Q| leaves, and if |Q| = 1 the edge has two leaves. Extend the star by repeatedly joining an outside vertex with one edge; connectedness guarantees such an edge until the tree spans G. Adding a vertex to a leaf replaces that leaf with the new vertex, and adding to a nonleaf increases the number of leaves. Thus the number never decreases.

Set k = lambda_max(complement(G)). If k = 0 the desired inequality follows from nonnegativity. Otherwise a vertex v in the complement has an independent set Q of k neighbors. In G, Q is a clique, and v is outside Q. Apply the lemma. This proves the conjecture, including the one-vertex graph (both sides zero under the degree-one convention).

The bound is sharp: for a path on three vertices, the two end vertices each have a single complement neighbor and the bound is strict; for a path on four vertices, a complement neighborhood contains a two-vertex independent set, so both sides equal two.

[Joint manuscript](../c161-c162/paper.tex) · [Exact verification](../c161-c162/verify.py). AI-assisted research note; author and external review pending. Priority not established.
