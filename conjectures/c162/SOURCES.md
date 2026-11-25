# Source and proof audit — Graffiti.pc conjecture 162

- Original source: Ermelinda DeLaViña, *Written on the Wall II — Conjectures of Graffiti.pc*, [catalogue PDF](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 162, announced 2005-08-08, catalogue updated 2026-11-05. Listed open in that snapshot; this is not proof of priority. The statement was checked against extracted catalogue text; the page-image retrieval was unsuccessful.
- The universal proof is elementary and needs no external theorem. The manuscript states all definitions and edge cases.
- The NetworkX 3.6.1 Graph Atlas contains every nonisomorphic simple graph of order at most seven. The verification uses its 995 connected graphs of orders 2–7. Primary: connected domination and exact subset enumeration. Independent: spanning-tree edge enumeration and bit-mask independent-set enumeration. For n>=3 the identity L_s=n-gamma_c follows from the internal vertices of a spanning tree forming a connected dominating set and the converse construction attaching outside vertices to a tree of a connected dominating set. The smaller cases are explicit.

## Referee checklist

1. Restrict to order at least two, since the reciprocal of minimum degree must be defined.
2. For minimum degree one, verify that minimum local independence is one and the attaining vertices are simplicial.
3. Check shortest-path connectivity of the nonsimplicial core and the closed-neighborhood argument for attachment.
4. Handle K2 separately.

## Limitations

Local cross-check of both exact algorithms found no disagreements or violations. No peer review, proof-assistant certification or exhaustive priority determination is claimed. AI-assisted preprint for author review.

## Source recheck (2026-11-25)

Catalogue entry 162, printed page 93 of 316, in the snapshot printed 6 November 2026. Historical catalogue index: https://cms.uhd.edu/faculty/delavinae/research/wowll/index.htm . A direct PDF fetch returned 404 on recheck; the indexed PDF snapshot was available. See the [cross-conjecture audit](../../audit/README.md) for additional checks.
