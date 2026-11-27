# Submission and attribution audit — 27 November 2026

## Scope and evidence

This audit records the curator's reported statuses (private correspondence, summarized rather than reproduced), repository history, fresh proof reading and independent local computational spot checks. It is not peer review, proof-assistant certification or an exhaustive priority determination. Current official site: https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/ . The previously cited temporary November 6 PDF is historical and was reported by the curator to be retired. The live updated entries could not be retrieved independently; changes were announced for November 30 or December 1, subject to processing.

## Correspondence and timing

The original email of 25 November at 19:43 UTC linked the repository and did not enumerate entries. At that time the main branch contained #157, #161, #162, #166, #169, #171, #177 and #179 (commit 2e75fd576722753d968094fca916f88640857652). Subsequent additions: #76, #138, #208, #137, #268, #271, #361, #365, #362, #348, #351, #376, #377 (13). Ten later packages were merged in PR #1 at 74cc988eabe729cd48d8cfcecbe31bc42e9ef497. The curator's later reply may already encompass some of these; do not infer individual statuses from a blanket statement.

| Entry | Correspondence or research classification |
|---|---|
| 76 | Earlier submission reported; also prior mathematical implication |
| 137 | Classical implication of Seinsche (1974); singleton exception; no novelty claim |
| 138 | Candidate counterexample; ask whether #135 in correspondence was intended to mean #138; do not assume |
| 157, 169, 171 | Candidate submissions; individual catalogue status unconfirmed |
| 161, 162 | Prior implication / prior-related, no first-resolution claim |
| 166 | Closure by counterexample announced; website not yet verified |
| 177, 208 | Earlier submissions explicitly reported as pending review; exclude from candidate novelty count |
| 179 | Earlier submission reported; exclude from candidate novelty count |
| 268, 271 | Provisional attribution to submitted AI-assisted derivations; earlier 2007 theorem and proof machinery credited; priority unconfirmed |
| 348, 351, 361, 362, 365 | Later candidate resolutions; archived statement and open marker, no independently verified current entry or earlier exact proof located in bounded searches |
| 376, 377 | Later candidate resolutions; same archived-only limitation plus unresolved Jiang (2016) prior-art lead |
| 135 | Closure announced by curator, but no matching package or commit found here. Attribution and numbering require clarification; not counted. |

## Fresh proof reading and computational spot checks

- #138: double-ended path with two pendant leaves at each endpoint, k=7; uniqueness of maximum independent set follows from excluding both end vertices and taking the unique maximum set on the remaining odd path. Longest induced path 17, square distance 6, claimed bound 18. Square-distance coefficient 2 is asymptotically sharp by the family.
- #137: the connected/co-connected graph lemma is the classical cograph characterization. The complement path-cover cases yield the inequality for order at least 2; no first-resolution claim.
- #268 and #271: the diameter bound for a spanning tree derived from a total dominating set is known from DeLaViña, Liu, Pepper, Waller and West (2007), Lemmas 2–3, equation (5). The additional center-pair argument in #268 and k=2,3 maximum-degree case analysis in #271 establish the stated forms; neither is an attribution of the underlying published bound to this project. No earlier exact numbered solution was located in bounded searches. Attribute the submitted derivations only, subject to curator confirmation and human review.
- #348: contraction of assigned connected blocks gives c-1 edges; unselected exceptional vertices give at least three distinct interblock incidences each. This yields 3b <= 3k+2c-2 <= 4k-2.
- #351: for m=3,4,10 independently reconstructed trees have 55,73,181 vertices, total dominating witnesses of sizes 28,37,91, and proposed right-hand sides 30,40,100. Verified each selected set dominates all vertices and the two component counts equal 7m and 3m. The manuscript's disjoint mandatory-neighborhood argument proves the corresponding lower bound 9m+1.
- #361: equality at isolated-support excess one forces a star or a star with pendant leaves on its outer vertices, hence one center; two centers force excess at least two.
- #362: radius-two balls around the selected vertices after removing one representative per support component cover a diameter path with at most five path vertices per ball. Integer arithmetic gives the original radius bound; explicit family establishes sharp coefficients.
- #365: within-block degree-two edges can be charged at most twice to selected vertices outside isolated supports; interblock edges contribute at most c-1, and c <= k-i. Sharp family checks analytically.
- #376 and #377: block-incidence argument gives k>=i+1, with equality forcing a single selected star and the claimed unique distance median and upper median degree one (path case handled separately). The two statements share one structural argument.

Fresh independent local exact subset enumeration of total dominating sets over all 985 nonisomorphic trees of orders 3–12 found no violation of the #348 strengthened bound, #361, #362 strengthened diameter and original radius bounds, #365 strengthened bound, #376 or #377. The #351 small-tree enumeration did not find a witness; the explicit constructed family above was separately checked. These finite checks complement the mathematical arguments but do not establish priority or universal validity by themselves. This is a separate check, not a claim that repository CI was rerun or passed.

## Literature limitations

Targeted searches for the numbered conjectures, total domination papers and public AI research reports did not establish earlier exact resolutions of #138, #348, #351, #361, #362, #365, #376 or #377. That negative result is bounded; unpublished earlier submissions may exist. The 2009 tree paper and 2007 general-graph paper are relevant antecedents already cited in package sources. In particular Hongxing Jiang, *Some conjectures of Graffiti.pc on the total domination number of a tree*, Utilitas Mathematica 99 (2016), 33–42, remains an unresolved full-text lead for the tree entries, particularly #376 and #377. See https://combinatorialpress.com/um/vol99/ . Public August 2026 screening at https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four does not establish a proof or priority. The current curator's information supersedes historical open markers. No certified first resolution is claimed.

## Next correspondence

Ask the curator to clarify #135 versus #138, acknowledge earlier submissions and give credit where due, confirm individual statuses, and offer the later proofs and counterexamples as candidates for review with all prior-art qualifications. AI assistance and pending human author review remain disclosed.
