# Novelty and correctness screening — 2026-11-26

This ledger consolidates the recorded per-package bounded searches, not an exhaustive fresh literature review. Eight candidates have primary-catalogue evidence, five (#348, #351, #361, #362, #365) rely on archived open markers, and six are prior-related notes. See [STATUS.md](STATUS.md) for evidence levels and [catalogue.json](catalogue.json) for the machine-readable classifications.

| Entry | Classification | Evidence |
|---|---|---|
| 76 | Prior implication / explicit counterexample; excluded from novel count | 43-vertex bipartite cactus, exact t=21 versus 43/2, and unbounded family. Matoušek–Šámal (2008), Lemma 2.2 specialized to C4, already implies an asymptotic disproof via a related bridge construction; no prior priority asserted. |
| 137 | Prior implication; excluded from novel count | Open catalogue entry, 12 July 2005, printed p. 79. Seinsche (1974) implies the nontrivial statement immediately. No separate exact numbered resolution identified in bounded searches. Literal K1 exception; catalogue testing convention noted. |
| 138 | Candidate disproof; priority unconfirmed | Exact catalogue statement and page image checked; 19-vertex witness and infinite subcubic tree family, sharp coefficient for square distance. Classical gadget acknowledged. No earlier exact disproof identified in bounded searches. |
| 157 | Candidate resolution; priority unconfirmed | Exact statement checked on printed p. 90; no exact prior proof located. Classical BFS ingredients. |
| 161 | Rediscovery / prior implication; excluded from novel count | Entry 159 October 2005 stronger bound, also elementary maximum-degree bound; see c161 source audit. |
| 162 | Prior-related elementary derivation; excluded from established novel count | De Caria Di Fonzo 2024, Prop. 3.1 and exchange argument; see c162 source audit. |
| 166 | Candidate disproof; priority unconfirmed | Exact statement and open status checked in indexed catalogue p. 95; page image fetch failed. 22-vertex subcubic witness, exact squared violation 9. Foster's 2005 diamond-chain examples under entry 165 are prior related work and explicitly credited; novelty of the gadget is not claimed. No earlier disproof of the exact WOW-II statement found in bounded searches. |
| 169 | Candidate resolution; priority unconfirmed | Exact statement printed p. 97; singleton convention explicit; no exact prior proof located. |
| 171 | Candidate disproof; priority unconfirmed | Indexed catalogue formula and definitions (pp. 98–99) agree; infinite counterexample family, even among trees. Targeted searches found no earlier exact disproof. Direct PDF image retrieval failed. See c171 source audit. |
| 177 | Candidate resolution; priority unconfirmed | Catalogue and REGS statement confirmed; DeLaViña–Waller 2008 Theorem 3 proves only the weaker additive 1 bound. New constructive argument proves the degree term and strengthens it to any independent set. No earlier full proof identified. |
| 179 | Candidate resolution of both readings; priority unconfirmed | Catalogue p. 104 uses delta; West REGS uses Delta. New proof gives Delta+i+lambda and the prior paper's separate additive minimum-degree refinement. Kuberwastaken/c5-k4 reports incomplete trial, not proof. |
| 208 | Candidate resolution; priority unconfirmed | Catalogue statement and Stong's 2010 comment checked in indexed text; image fetch failed. Proof uses Chvatal's degree criterion plus explicit matching arguments for the small exceptional orders; sharp threshold. No earlier exact resolution found in bounded searches. |
| 268 | Prior-related resolution; excluded from novel count | Catalogue open on 2026-11-06. DeLaVina et al. (2007), Lemmas 2–3, equation (5) and Theorem 3 already provide the spanning-tree machinery. Additional center-pair argument gives the exact floor bound. No earlier exact resolution located in bounded searches. |
| 271 | Prior-related resolution; excluded from novel count | Catalogue open on 2026-11-06. Same published diameter bound, retaining the component count for k=3, and a dominating-edge degree argument for k=2. No earlier exact resolution located in bounded searches. |
| 348 | Candidate resolution and strengthening; archived-only open status; priority unconfirmed | Archived statement and O marker checked; current official entry unavailable. DeLaViña et al. (2009), Lemmas 8 and 10 and Theorem 9 address related quantities; no earlier exact proof or implication identified in bounded searches. Component-sensitive incidence argument; 2,286 trees checked, 985 cross-checked. No claim that the improved coefficient is optimal. |
| 351 | Candidate disproof; archived-only open status; priority unconfirmed | Archived statement and O marker checked. August 2026 report records zero violations in 81,132 screened trees for this entry; no earlier exact disproof located in bounded searches. Explicit 55-vertex witness and infinite tree family, exact domination number, unbounded additive gap. Original entry unverified. |
| 361 | Candidate resolution; priority unconfirmed | Archived dataset gives exact statement, date and open marker. August 2026 research report records finite screening of 361, not a proof. Related DeLaViña et al. paper gives different bounds. No earlier exact proof identified in bounded searches. Current catalogue entry image unavailable (404). Elementary structural proof and exhaustive tree check. |
| 362 | Candidate resolution and sharp strengthening; archived-only open status; priority unconfirmed | Archived statement and O marker checked. August 2026 public report records screening without resolution. Original entry unavailable; no earlier exact proof or stronger bound located in bounded searches. Radius-two covering argument and infinite sharp family; fresh exact check. |
| 365 | Candidate resolution and sharp strengthening; priority unconfirmed | Archived statement and open marker checked. August 24, 2026 report records screening of 365 without a resolution; related report on 364 says 365 survives. No earlier exact proof or sharp strengthening located. Original catalogue page unavailable. Exact block-counting proof and infinite sharp family; two local exhaustive checkers agree. |

## Counting policy

Thirteen candidates (138, 157, 166, 169, 171, 177, 179, 208, 348, 351, 361, 362, 365), of which 348, 351, 361, 362 and 365 have archived-only open-status evidence; six excluded notes (76, 137, 161, 162, 268, 271). None has independently certified priority. An open catalogue status is historical metadata, not a claim that no proof existed before November 2026. A prior implication excludes a conjecture from the novel count even if its catalogue status is stale. Reclassify any candidate if an earlier resolution is identified. For 166, similarly numbered WOW-I entries and unrelated project counters are different statements.

## Sources

- Archived entry 351: https://github.com/Kuberwastaken/c5-k4/blob/e2cee93231eefb91c41e35450f7eeb19fd9c8c75/data/wowii-conjectures.json ; August 2026 screening report: https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four . See [c351 source audit](conjectures/c351/SOURCES.md).

- Archived entry 348: https://github.com/Kuberwastaken/c5-k4/blob/e2cee93231eefb91c41e35450f7eeb19fd9c8c75/data/wowii-conjectures.json ; related 2009 article https://www.uhd.edu/documents/academics/sciences/boca2009-dlpw.pdf , printed pp. 7–8 visually inspected. See [c348 source audit](conjectures/c348/SOURCES.md).

- Archived entry 362: https://github.com/Kuberwastaken/c5-k4/blob/e2cee93231eefb91c41e35450f7eeb19fd9c8c75/data/wowii-conjectures.json ; August 2026 screening report: https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four . Current official entry unverified. See [c362 source audit](conjectures/c362/SOURCES.md).

- Archived entry 365: https://github.com/Kuberwastaken/c5-k4/blob/main/data/wowii-conjectures.json ; August 24, 2026 screening report: https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four ; related 364 report: https://ai-village-news-cb5c4b.gitlab.io/articles/s1765.html . Related tree bounds in https://www.uhd.edu/documents/academics/sciences/boca2009-dlpw.pdf and https://math1um.github.io/Research/r08.pdf . Neither inspected result gives the exact 365 inequality.

- Archived entry 361: https://github.com/Kuberwastaken/c5-k4/blob/main/data/wowii-conjectures.json ; August 2026 report of finite screening without a resolution: https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four . Related paper: E. DeLaViña, C. E. Larson, R. Pepper and B. Waller, On total domination and support vertices of a tree, https://math1um.github.io/Research/r08.pdf . Theorems 1–2 and 4 address different inequalities.

- E. DeLaViña, Q. Liu, R. Pepper, B. Waller and D. B. West, Some conjectures of Graffiti.pc on total domination (2007), Lemmas 2–3, equation (5), Theorem 3, https://www.uhd.edu/documents/academics/sciences/total-dom-2007.pdf . Lemma 3 visually checked on PDF page 4; indexed catalogue statements 268 and 271 checked, page image retrieval failed.

- D. Seinsche, On a property of the class of n-colorable graphs (1974), JCT B 16, 191–193, https://doi.org/10.1016/0095-8956(74)90063-X .

- V. Chvátal, On Hamilton's ideals (1972), https://doi.org/10.1016/0095-8956(72)90020-2 .

- J. Matoušek and R. Šámal, https://doi.org/10.37236/765 (2008), Lemma 2.2; https://arxiv.org/abs/0711.4829 .

- Ermelinda DeLaViña, Written on the Wall II, snapshot printed November 6, 2026: https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf . Images checked for 157, 161, 169 and 179; 162 and 166 text checked, image fetch failed.
- Douglas West, REGS, https://dwest.web.illinois.edu/regs/graffiti.html .
- P. De Caria Di Fonzo, https://doi.org/10.1016/j.dam.2024.01.018 (2024; preprint October 2023).
- E. DeLaViña and B. Waller, https://doi.org/10.37236/757 (2008), Theorem 5, visually checked.
- https://github.com/Kuberwastaken/c5-k4 (prior #179 bounded trial).
- https://grok-ai-village-news-496089.gitlab.io/series/wow.html (screened public research index, not evidence of priority).

Do not describe any candidate as 100% novel or peer-reviewed. The archive preserves correct derivations with explicit attribution, including rediscoveries. Formal proof-assistant verification and external author/referee review remain outstanding.
