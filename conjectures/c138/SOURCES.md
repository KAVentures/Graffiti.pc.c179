# Source and novelty audit — conjecture 138

**Correspondence update (2026-11-27):** Candidate counterexample, independently proof-read on 27 November 2026. The curator mentioned #135, not #138; numbering and individual status remain unconfirmed. Do not equate the two. See [submission audit](../../SUBMISSION-AUDIT.md). The [current official WOWII website](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/) supersedes the historical temporary PDF cited below.

- Ermelinda DeLaViña, Written on the Wall II, entry 138, July 12, 2005, printed page 80, catalogue updated November 5, 2026: https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . Indexed statement and page image of formula checked. Open status in the catalogue is not proof of priority.
- Formula: largest induced path order >= (2+u(G)) times the minimum distance among distinct maximum-degree vertices of G^2, with u(G)=1 for unique maximum independent set. The counterexample has exactly two designated vertices and refutes both the original-distance and square-distance interpretations.
- https://github.com/Kuberwastaken/c5-k4 reports recovery and computational testing of entries 136–138; no prior disproof of 138 identified there. Also screened exact number, nearby formulas, graph-square and unique-independence terminology, and public research index https://grok-ai-village-news-496089.gitlab.io/series/wow.html . Search bounded; priority unconfirmed.
- The double-ended tree construction itself is classical. No novelty claim for the gadget or elementary shortest-path bound. Candidate contribution is applying the family to the exact conjecture and proving the sharp coefficient on the restricted class.

## Referee checklist

1. Four pendant leaves are distinct; the graph is a tree of order 2k+5 and maximum degree three.
2. The replacement of either selected endpoint by its two leaves strictly increases an independent set.
3. Once endpoints are excluded, all pendant leaves are mandatory and the odd-length internal path has a unique maximum independent set.
4. Degree 5 occurs only at x1 and x(2k-1) in the square; compute all other square degrees.
5. The exact tree diameter in edges is 2k+2; the induced-path order is one greater.
6. Square distance is the ceiling of half the original distance; the violation k-6 is positive for k>=7.
7. The shortest-path argument gives coefficient 2 for square distance and the ratio tends to 2 in this family.
8. The independent programs use different independence algorithms, tree dynamic programming versus memoized subset recursion; both executed locally.
