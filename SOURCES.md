# Source and proof audit

- Original source: Ermelinda DeLaViña, Written on the Wall II, conjecture 179, announced 2005-08-08, catalogue last updated 2026-11-05, PDF pp. 104–105 (printed numbering): https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . The displayed formula uses lowercase delta; an ancillary definition lists uppercase Delta as maximum degree. This note follows the displayed formula and standard minimum-degree notation. The original statement is restricted to simple connected graphs on at least two vertices.
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
