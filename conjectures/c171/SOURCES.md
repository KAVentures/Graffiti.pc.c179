# Source and proof audit — Conjecture 171

- Ermelinda DeLaViña, [Written on the Wall II: Conjectures of Graffiti.pc](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 171, printed pp. 98–99/316; announced August 8, 2005, status open in the snapshot printed November 6, 2026. Indexed catalogue text checked on November 25, 2026. Direct PDF retrieval returned HTTP 404 and page-image retrieval failed; source fidelity is based on the indexed text, not a visually inspected PDF. The source formula uses the maximum even-distance count minus one, divided by dist_avg(B). The definitions distinguish dist_avg(B), averaging nonzero distances within the set of vertices of maximum eccentricity, from dist_avg(B,V), averaging distances to the whole graph. This construction addresses the former.
- DeLaViña and Waller, *Spanning Trees with Many Leaves and Average Distance*, Electronic Journal of Combinatorics 15 (2008), DOI [10.37236/757](https://doi.org/10.37236/757), discusses related bounds and the distinct boundary-to-whole-graph average; not a known prior resolution of C171.
- Targeted exact-number and invariant searches on November 25, 2026 (including "Graffiti.pc" "171" "peripheral", "conjecture 171" "spanning" "distance", and the boundary-distance definition) found no exact prior disproof. The catalogue is not a comprehensive literature index. This is a candidate disproof with priority unconfirmed; see [NOVELTY.md](../../NOVELTY.md).

## Referee checklist

1. Each path intersects others only at the common root; the added cluster consists of new leaves.
2. Verify order and leaf count; a tree has exactly one spanning tree.
3. Count the parity classes for even r, including the root; optionally exclude each root and check the strict inequality still fails.
4. Only the long-arm endpoint and cluster leaves reach depth r. The distance between opposite depth-r vertices is 2r, and any other vertex is at distance at most 2r-1 from every vertex.
5. Count unordered distinct peripheral pairs; ordered pairs give the same average.
6. Multiply by the positive denominator and verify the cubic inequality for all even r >= 22. The strict inequality is not a floating-point artifact.
7. Show the claimed lower bound is asymptotic to r^2/12 and the leaf count to 2r; no claim of minimal counterexample.

## Reproducibility and limitations

Two locally executed algorithms independently build and traverse the tree: NetworkX shortest paths and a standard-library adjacency-list queue traversal. Both use exact rational arithmetic, check four concrete parameters and agree with the closed forms. A universal symbolic proof, not the finite tests, establishes the infinite family. No independent peer review, proof-assistant verification or exhaustive priority search is claimed. AI assistance disclosed.
