# Source and proof audit — Graffiti.pc conjecture 157

- Ermelinda DeLaViña, *Written on the Wall II — Conjectures of Graffiti.pc*, [catalogue PDF](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 157, printed page 90 of 316, announced 2005-08-08. The catalogue updated November 5, 2026 and printed November 6, 2026 lists the entry as open. The original formula and four definitions were checked against both extracted text and the page image. The catalogue is not a priority guarantee. Its [landing page](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/index.html) notes an ongoing server migration.
- The argument uses only breadth-first spanning trees and the elementary maximum edge count on a given number of vertices.
- NetworkX 3.6.1 Graph Atlas includes all nonisomorphic simple graphs through order seven. The primary exact leaf-number calculation uses connected domination; the independent implementation enumerates spanning-tree edge sets with union-find and computes distances by Floyd–Warshall. Both check every root, a stronger scope than central roots alone. The primary also checks the constructive tree and a parameter grid of sharp examples.
- For n >= 3, L_s = n - gamma_c: the internal vertices of a spanning tree form a connected dominating set, and a spanning tree of any connected dominating set extends by attaching outside vertices individually. Orders one and two are explicit.

## Referee checklist

1. Last-layer vertices are not the root for n >= 2 and have exactly one tree edge.
2. Original degree-one vertices remain degree one in every spanning tree.
3. Count the union, not the sum, of pendant vertices and last-layer vertices.
4. A pendant vertex in the last layer has its only neighbor in the previous layer; it cannot contribute an induced edge.
5. Handle K1 and M = 0 separately; the inverse binomial formula is for M > 0.
6. Check that the distinguished clique vertex in the sharpness family is the unique center and its spanning star achieves the universal n-1 upper bound.

## Limitations

Both exact verifiers ran locally with NetworkX 3.6.1, with zero disagreements or violations on 996 graphs; the primary also checked 110 sharp-family cases. No independent peer review, proof-assistant certification, or exhaustive publication-priority determination is claimed. AI-assisted manuscript for author review.

## Novelty recheck

Targeted exact-number, invariant-expression, spanning-tree and GitHub searches on 2026-11-25 did not identify an earlier complete proof of the exact statement. The proof uses classical elementary ideas, so the result is a candidate resolution, not certified novel. Catalogue status is not proof of priority. See [NOVELTY.md](../../NOVELTY.md).
