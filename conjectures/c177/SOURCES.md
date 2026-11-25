# Source and proof audit — conjecture 177

- Ermelinda DeLaViña, Written on the Wall II, conjecture 177, August 8, 2005. Catalogue updated November 5, 2026: https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . Indexed PDF text gives the formula and open status; the screenshot fetch failed with HTTP 404. Formula corroborated by the following two independent sources.
- Douglas West, Some Conjectures of Graffiti.pc (REGS 2009), https://dwest.web.illinois.edu/regs/graffiti.html . Confirms L+b >= 2 alpha + second-smallest degree, multiplicity counted.
- E. DeLaViña and B. Waller, Spanning Trees with Many Leaves and Average Distance, Electronic Journal of Combinatorics 15 (2008), R33, https://doi.org/10.37236/757 . Theorem 3 proves L+b >= 2 alpha + 1, explicitly noting the stronger conjecture is open. The proof is re-used with attribution for the case sigma_A=1, and its component method is extended for higher degrees.
- M. Chellali and O. Favaron, Connected Domination, Topics in Domination in Graphs (2020), https://doi.org/10.1007/978-3-030-51117-3_4 . Survey records the conjectured connected-domination form and earlier advances.
- Prior-art search on 2026-11-25: exact conjecture numbers, Graffiti.pc 177, WOWII 177, leaf/bipartite numbers and second-smallest degree, journal searches and public research indexes. No earlier complete proof identified. This is a bounded search, not a claim of exclusive priority.

## Mathematical referee checklist

1. Sigma_A counts multiplicities; all but at most one vertex of A have degree at least sigma_A. A need not be a maximum independent set.
2. All vertices of A have neighbors in B. A plus a maximum independent set of B induces a bipartite graph; beta is at least the component count m.
3. In the connection operation, every already used vertex of A touches only covered components. Contracting B components produces a connected incidence graph, guaranteeing a new connector.
4. Adding each connector costs at most one existing B leaf and gains at least one B leaf from each newly reached component.
5. In Case 2, the initial star has at least s leaves in B. Removing s-1 of the eventual B leaves while protecting a neighbor of the exceptional vertex preserves a connected dominating core.
6. Attach all outside vertices directly to the fixed core, not successively to one another.
7. If q=1 and beta=m, all B components are cliques and all high vertices touch exactly one component. If m>1 the sole possible exceptional vertex must meet every component.
8. In Case 3, retain at least one vertex in each clique and an exceptional-vertex neighbor in the modified clique if it has one there. The resulting core dominates and uses at most m-1 vertices of A.
9. Treat alpha=1 and K2 separately. The connected domination identity is stated for n>=3.
10. The new general argument is independent of finite enumeration. The 2008 weaker result is explicitly attributed, and exclusive priority is not claimed.

## Computation

Pinned NetworkX 3.6.1 supplies Atlas graphs. Primary verification uses exact connected domination, induced bipartite subset enumeration and constructive tree witnesses. The independent script uses direct edge-subset enumeration with union-find, disjoint independent-set pairs and bit-mask reachability. Both ran locally on Python 3.13.5. CI is configured for Python 3.12 and builds the manuscript PDF separately. No formal proof-assistant or independent human referee verification is claimed.
