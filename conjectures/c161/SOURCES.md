# Source and proof audit — Graffiti.pc conjecture 161

- Original source: Ermelinda DeLaViña, *Written on the Wall II — Conjectures of Graffiti.pc*, [catalogue PDF](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 161, announced 2005-08-08, catalogue updated 2026-11-05. Listed open in that snapshot; this is not proof of priority. The source statement was checked against the page image.
- The universal proof is elementary and needs no external theorem. The manuscript states all definitions and edge cases.
- The NetworkX 3.6.1 Graph Atlas contains every nonisomorphic simple graph of order at most seven. The verification uses its 995 connected graphs of orders 2–7, and separately checks the singleton. Primary: connected domination and exact subset enumeration. Independent: spanning-tree edge enumeration and bit-mask independent-set enumeration. For n>=3 the identity L_s=n-gamma_c follows from the internal vertices of a spanning tree forming a connected dominating set and the converse construction attaching outside vertices to a tree of a connected dominating set. The smaller cases are explicit.

## Referee checklist

1. Verify that independence in the complement is a clique in G.
2. Check that the selected clique is proper because the complement-neighborhood center is excluded.
3. Check the singleton, size-one clique, and star-extension cases separately.

## Limitations

Local cross-check of both exact algorithms found no disagreements or violations. No peer review, proof-assistant certification or exhaustive priority determination is claimed. AI-assisted preprint for author review.

## Source recheck (2026-11-25)

Catalogue entry 161, printed page 92 of 316, in the snapshot printed 6 November 2026. Historical catalogue index: https://cms.uhd.edu/faculty/delavinae/research/wowll/index.htm . A direct PDF fetch returned 404 on recheck; the indexed PDF snapshot was available. See the [cross-conjecture audit](../../audit/README.md) for additional checks.

## Prior result identified

The catalogue's October 2005 comment on conjecture 159 already records the stronger inequality L_s >= lambda_max(G)+omega(G)-2 for nontrivial graphs. For any connected noncomplete graph lambda_max(G)>=2 (use an internal vertex of a shortest path between nonadjacent vertices), hence L_s>=omega(G)>=lambda_max(complement(G)). For complete graphs the complement parameter is zero, including K1. In fact the elementary bound L_s>=Delta already suffices: a maximum proper clique has a boundary vertex of degree at least omega(G). This is therefore an independently presented proof of a previously implied result, not a claim of a new theorem.

Source: Written on the Wall II, entry 159, October 2005 comment, printed p. 91 of the November 2026 snapshot. Douglas West's REGS page https://dwest.web.illinois.edu/regs/graffiti.html also lists conjecture 161. Do not count this note as a novel resolution.
