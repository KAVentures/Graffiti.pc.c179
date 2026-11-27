# Source and proof audit

**Correspondence update (2026-11-27):** Earlier solution submitted by another researcher, confirmed by the curator on 27 November 2026. Excluded from the candidate novelty count. Our independent derivations and refinements are retained without a priority claim. See [submission audit](../../SUBMISSION-AUDIT.md). The [current official WOWII website](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/) supersedes the historical temporary PDF cited below.

- Original source: Ermelinda DeLaViña, Written on the Wall II, conjecture 179, announced 2005-08-08, catalogue last updated 2026-11-05, PDF pp. 104–105 (printed numbering): https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . The displayed formula uses lowercase delta; an ancillary definition lists uppercase Delta as maximum degree. The catalogue's displayed formula uses standard minimum-degree notation; both minimum- and maximum-degree statements are now proved. The original statement is restricted to simple connected graphs on at least two vertices.
- Published dependency: E. DeLaViña and B. Waller, Spanning Trees with Many Leaves and Average Distance, EJC 15 (2008), R33, Theorem 5, p. 4 (proof starts p. 10): https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1r33 . The paper uses mu for maximum local independence. The theorem is not conjecture 174, which has a different stronger RHS.
- Survey: M. Chellali and O. Favaron, Connected Domination (2020), Section 6 item 5; https://doi.org/10.1007/978-3-030-51117-3_4 . The survey states the equivalent connected-domination form.
- Style reference: K. Afrasyab, A 50-Vertex Cubic Counterexample to the Domination-versus-Edge-Domination Conjecture, arXiv:2609.10783, https://arxiv.org/abs/2609.10783 ; concise theorem/proof, explicit computational evidence boundary.
- Literature search (2026-11-25): exact conjecture number and graph invariants, Graffiti.pc catalogue and related connected-domination literature. No earlier complete proof identified in this bounded search; priority is not guaranteed. The catalogue may be updated and is not an exhaustive index of all results.

## Referee checklist

1. Check lambda is maximum, not average or minimum local independence.
2. Verify A independent implies N(a) lies outside A; v belongs to N(a), a belongs to A, and the two inserted vertices are distinct and absent from B minus N(a).
3. The standard domination bound uses maximum degree. Equality with n minus minimum degree forces regularity.
4. Deleting x from D_v in the equality argument is valid since y remains and v still dominates all its neighbors.
5. A graph with clique neighborhoods has complete connected components, by the shortest-path argument.
6. In the exceptional complete multipartite graph, at least two parts exist; a pair of vertices in different parts dominates and forms an edge. The spanning tree construction is explicit.
7. The n=2 case is evaluated directly. The identity L_s = n - gamma_c is only used for n >= 3.
8. Integer rounding: ceil(lambda/2) is (lambda+1)//2 for positive integers.
9. Exhaustive Atlas enumeration checks only orders 2–7. The universal proof is independent of these checks. The leaf calculation via connected domination is additionally checked by enumerating all n-1 edge subsets on all connected Atlas graphs through order 6 and equality cases at order 7.
10. The mathematical proof is complete conditional only on the cited published theorem; no Lean certification, external peer review or guaranteed novelty is claimed. Author review remains required before submission.

## Data

NetworkX Graph Atlas is included in the pinned NetworkX distribution. It contains all nonisomorphic simple graphs up to order 7. No proprietary data, random seeds, solvers, floating-point tolerances or external APIs are used in verification.

## Independent computational audit

`verification/independent.py` uses NetworkX only for Atlas input and diagnostic graph6 output, not graph algorithms. It checks connectivity by reachability, computes the bipartite number by disjoint independent-set pairs, ordinary domination by direct subset tests, and the leaf number by enumerating acyclic sets of n-1 edges. It compares all five invariants to the primary implementation for all 995 graphs. Both passed in a local Python environment with NetworkX 3.6.1. See `verification/local-run.txt`.

## Source recheck (2026-11-25)

The formula was visually checked on printed page 104 of the catalogue PDF snapshot printed 6 November 2026; it uses lowercase delta. The dependency was visually checked on printed page 4 of the published 2008 paper. Stable DOI: https://doi.org/10.37236/757 . The earlier revision did not settle the uppercase-Delta interpretation. The current revision proves it, including the stronger independent-domination version, by extending the center of a maximum induced star to a maximal independent set outside its leaves. See the repository-wide audit for details.

## Novelty and source ambiguity

Douglas B. West, Some Conjectures of Graffiti.pc, REGS 2008, https://dwest.web.illinois.edu/regs/graffiti.html explicitly lists 179 using maximum degree. The new elementary theorem L_s+b >= Delta+i+lambda settles that statement, with independent domination i >= gamma. The argument is separate from the 2008 theorem used for the additive minimum-degree refinement. Kuberwastaken/c5-k4 (https://github.com/Kuberwastaken/c5-k4) reports a bounded, unfinished #179 trial, not a universal proof. Targeted searches found no earlier exact proof of the new inequality, but neither priority nor novelty of the constituent elementary observations is guaranteed. Local exact verification: 995 graphs, 453 equalities for both maximum-degree inequalities, zero violations.
