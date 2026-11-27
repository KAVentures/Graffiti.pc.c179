# Source audit: conjecture 76

**Correspondence update (2026-11-27):** Earlier solution submitted by another researcher, reported by the curator on 27 November 2026; no claim to first resolution. The prior mathematical implication remains credited. See [submission audit](../../SUBMISSION-AUDIT.md). The [current official WOWII website](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/) supersedes the historical temporary PDF cited below.

- Original indexed PDF: Ermelinda DeLaViña, Written on the Wall II, entry 76, April 4, 2004, open in the November 5, 2026 catalogue, printed page 45/316. https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . Exact formula and definitions checked in indexed text; page image fetch returned HTTP 404.
- Jiří Matoušek and Robert Šámal, Induced Trees in Triangle-Free Graphs, EJC 15 (2008), R41, DOI https://doi.org/10.37236/765 . Preprint https://arxiv.org/abs/0711.4829 , Lemma 2.2 and its proof, checked in full text. This prior method uses disjoint copies of a fixed triangle-free graph joined by bridges in a recursive branching pattern. Taking the fixed graph to be C4 gives a family of bounded average degree less than 3 and induced-tree order sublinear in its order; hence it already implies a disproof of 76. The present exact one-vertex-sum version is prior-related; exclude from the count of novel resolutions. No claim of novelty of the recursion.
- Targeted prior-art searches for the exact conjecture, triangle-frequency expression, recursive cactus constructions, and public research repositories did not find an earlier explicit disproof of entry 76. This does not establish priority. The public math-autoresearch project reports finite tests rather than a solution of 76: https://github.com/takumayellow/math-autoresearch (indexed repository mirror: https://githubhelp.com/takumayellow/math-autoresearch).
- No reliance on the correctness of other AI-generated results.

## Referee checklist

1. Graphs are bipartite and connected; triangle maximum zero is attained by every vertex, not by zero vertices.
2. Rooted recursion includes the attachment vertex exactly once; the top square cannot be fully occupied by any induced tree.
3. A tree intersecting the central square has connected intersection there, since the attached branches cannot supply paths between different central vertices.
4. The largest three rooted weights are simultaneously attainable because deleting any vertex from C4 leaves a path.
5. Check n=43, m=56, t=21 and floor(112/43)=2. The comparison 2t<n is exact.
6. The symmetric family has positive, unbounded deficit; no claim of minimal order.
7. Independent block-cut DP enumerates all valid induced-tree subsets per block and is checked against exhaustive subsets on 143 connected Atlas graphs of order 1–6.

Local execution: Python 3.13.5 / NetworkX 3.6.1. No formal certification, independent peer review or priority guarantee.
