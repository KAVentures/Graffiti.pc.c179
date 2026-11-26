# Source and novelty audit — conjecture 208

- E. DeLaViña, Written on the Wall II, entry 208, announced January 12, 2006; catalogue updated November 5, 2026. https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . Indexed PDF text gives the exact formula and open status; screenshot retrieval returned HTTP 404. The displayed inequality is mu >= (1/2)*[1+(2/3)*|E(complement G)|], equivalent to the manuscript's formula.
- The same entry records Stong's June 2010 observation that the conjectured condition does not imply Chvatal's sufficient condition. The present proof explicitly treats the remaining cases, not merely an application of the degree criterion.
- V. Chvátal, On Hamilton's ideals, JCTB 12 (1972), 163–168, https://doi.org/10.1016/0095-8956(72)90020-2 . The degree-sequence theorem is used in its standard contrapositive form on G joined with a universal vertex; it is not a new theorem.
- Related extremal Hamiltonian-path literature was screened, including https://arxiv.org/abs/math/0407292 and related edge-bound work. No claim of novelty for the classical degree estimate or the elementary equality graphs.
- Targeted searches for Graffiti.pc 208, WOW-II 208, Hamiltonian paths, matching number, and missing edges found no earlier exact complete resolution. Bounded search, not evidence of exclusive priority.

## Referee checklist

1. The missing-edge threshold m <= 3*mu-2 follows from the original inequality by integrality.
2. On adjoining a universal vertex, a Hamiltonian cycle is equivalent to a Hamiltonian path in G.
3. The Chvatal index satisfies 2 <= k <= floor(n/2), and the second degree index is n+1-k.
4. The complement-degree sum gives the stated concave quadratic; its endpoint values exclude n >= 9 and n=5,7.
5. For n=4, two disjoint edges and connectedness give a spanning path.
6. For n=6,k=2, equality forces both leaves to have the same universal neighbor.
7. For n=6,k=3, a perfect matching forces an internal edge in the four-vertex low-degree set. Counting missing edges forces the configuration with the explicit Hamiltonian path.
8. For n=8,k=4, the five low-degree vertices must form an independent set, ruling out a perfect matching.
9. Both equality graphs have a cut vertex leaving three components; their matching numbers and missing-edge counts are explicit.
10. The computations are supplementary. No formal proof-assistant or independent peer-review claim.
