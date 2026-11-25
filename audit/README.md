# Cross-conjecture audit (2026-11-25)

This supplemental audit is separate from each standalone research package. It independently enumerates vertex subsets and spanning trees, checks both the bipartite definition and the connected-domination identity, constructs the witnesses used in the proofs of 161 and 162, and tests the domination construction and exceptional case used in 179.

## Reproduction

From the repository root:

```sh
python -m pip install -r requirements.txt
python audit/audit_all.py > /tmp/graffiti-observed.txt
diff -u audit/expected.txt /tmp/graffiti-observed.txt
```

Run without optimized Python (`-O`). The local run used CPython 3.13.5 and NetworkX 3.6.1. Its output, omitting the environment header, is in expected.txt. CI runs on Python 3.12. The audit does not require network access once NetworkX is installed. It does not certify claims beyond the enumerated graphs.

## Mathematical review

- 161: A complement-neighborhood independent set is a proper clique in the original graph; extending the star preserves or increases the leaf count. The singleton is treated separately in its standalone verifier.
- 162: The reciprocal degree formula requires at least two vertices; only minimum degree one is nontrivial. The nonsimplicial core of a connected noncomplete graph is nonempty and connected, and each simplicial vertex has a neighbor there. Thus all simplicial vertices can simultaneously be leaves of a spanning tree.
- 179: The two domination bounds and the regular complete-multipartite equality exception cover all cases when combined with DeLaViña–Waller (2008), Theorem 5. The theorem was checked against the published PDF. The displayed conjecture uses lowercase delta (minimum degree), whereas its ancillary glossary lists uppercase Delta (maximum degree). The current proof resolves both the displayed minimum-degree statement and the maximum-degree statement recorded by Douglas West, including the independent-domination strengthening. The supplemental audit tests the new constructive independent dominating set and 453 equality cases. The connected-domination identity requires order at least three; K2 is checked separately.

The catalogue snapshot printed 6 November 2026 lists all three as open. Catalogue entries 161 and 179 were inspected in page images; 162 was checked in the extracted PDF text (page image unavailable). This is not a guarantee of novelty or independent peer review. A direct fetch of the catalogue PDF returned 404 during the audit; the indexed snapshot was available. Original catalogue location and published theorem DOI are recorded in each source audit.

The previously recorded environment and output refer to the earlier audit; the new bound and witness were locally checked separately with NetworkX 3.6.1 on all 995 graphs. CI is configured to compare the extended audit output.

No universal mathematical claim is justified by finite enumeration alone. No formal proof-assistant certification or byte-identical PDF build is claimed.
