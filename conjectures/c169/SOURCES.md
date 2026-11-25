# Source and proof audit — Conjecture 169

- Original: Ermelinda DeLaViña, [Written on the Wall II](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 169, printed page 97/316. Announced August 8, 2005; snapshot printed November 6, 2026, status open. Both page image and extracted text were checked on November 25, 2026.
- The formula is the maximum-leaf number at least one plus the range of the even-distance vertex count. Whether the root is counted in the even-distance count does not affect the range.
- The source does not explicitly exclude the singleton. Under strict degree-one leaves, K1 refutes the unrestricted formula; the proof establishes the entire nontrivial domain and the singleton convention is explicit.
- Targeted searches for the conjecture number and distance-parity formulation did not identify an earlier proof. A separate computational research repository has reportedly tested the inequality; that is not a priority guarantee. No claim of exhaustive novelty.
- The only mathematical ingredients are breadth-first spanning trees and degree sums in a bipartite tree.

## Referee checklist
1. Distances in a breadth-first tree equal original root distances.
2. Every edge joins distinct parity classes.
3. The degree sum on each class equals n-1.
4. All nonleaves have degree at least two for n>=2.
5. Subtract endpoints of the resulting interval and handle the singleton separately.
6. Stars attain equality for every n>=3.

The primary Atlas check ran locally with NetworkX 3.6.1: 995 graphs, 85 equalities, zero violations. The packaged independent verifier additionally checks direct spanning-tree enumeration and Floyd-Warshall distances; CI is configured to execute both. No formal certification or peer review is claimed.

## Novelty recheck

Targeted exact-number, invariant-expression, spanning-tree and GitHub searches on 2026-11-25 did not identify an earlier complete proof of the exact statement. The proof uses classical elementary ideas, so the result is a candidate resolution, not certified novel. Catalogue status is not proof of priority. See [NOVELTY.md](../../NOVELTY.md).
