# Source and novelty audit — C166

- E. DeLaViña, Written on the Wall II, entry 166, announced 2005-08-08, indexed catalogue snapshot printed 2026-11-06, p. 95. https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf
- The indexed statement uses maximum-degree vertices M, the open neighborhood union N(M), set difference N(M)-M, and division by the square root of the radius. The entry is labelled open. The singleton has zero radius, so the expression is defined only for order at least two. Direct PDF page image retrieval returned HTTP 404; indexed extracted text was available and checked.
- The preceding entry 165, pp. 94–95, explicitly attributes diamond-chain examples to Craig Foster's summer 2005 UHD student research project. The present three-arm construction is related; no priority for the diamond gadget is claimed.
- Bounded literature and public repository searches on 2026-11-25 used the exact conjecture number, WOW-II distinction, radius, maximum-degree neighborhood, spanning-tree leaves and counterexample terminology. No exact prior disproof identified. A similarly numbered WOW-I entry in the c5-k4 repository and an AI Village project counter numbered 166 concern different conjectures, not this WOW-II entry. Search cannot establish exclusive publication priority.
- Classification: candidate resolution of a catalogue-open conjecture, not certified novel. Reclassify if an earlier exact disproof is located.

## Referee checklist

1. Verify the graph contains exactly three edge-disjoint four-cycles and twelve bridges; no other edges.
2. Check the maximum-degree set and its external neighborhood directly.
3. Distances from the central vertex are at most six and two terminals on different arms are twelve apart; use the triangle inequality for the radius lower bound.
4. Every tree keeps the bridges and deletes exactly one edge per cycle. Each deleted edge has one degree-three endpoint, and the arms are disjoint.
5. The tree degree sum identity gives leaf count 2 + number of degree-three vertices.
6. Compare the positive sides via exact integer squaring: 216 < 225.
7. Independent code checks all 2,024 choices with a separately specified edge list and different algorithms. Finite computation is supplementary.
