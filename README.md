# Graffiti.pc conjectures — proofs and reproducibility

Research preprints by Koyar Afrasyab, November 2026. Fifteen conjecture packages, each with its own manuscript, source audit, pinned dependencies, exact verification and reproduction instructions. Eight were announced on 8 August 2005; entry 76 dates to 4 April 2004, entries 137 and 138 to 12 July 2005, entry 208 to 12 January 2006, entries 268 and 271 to 23 February 2007, and entry 361 to 18 February 2009.

## Status at a glance (2026-11-26)

**Nine candidate resolutions (priority unconfirmed); six prior-related notes excluded from the novel count. Zero independently certified first resolutions.** The November 2026 catalogue and archived conjecture data label the entries open (the latest primary-source status of 361 could not be independently retrieved), but an open catalogue label is not proof that a result was unknown. See [NOVELTY.md](NOVELTY.md) for evidence and distinctions.

## Candidate resolutions — no exact earlier resolution identified in bounded searches

| Entry | Result | Package |
|---|---|---|
| 138 | Disproof: infinite family of subcubic trees with unique maximum independent sets; sharp coefficient for square distance | [Research package](conjectures/c138/) · [Paper](conjectures/c138/paper/paper.tex) |
| 157 | Proof and strengthening: radial circles | [Research package](conjectures/c157/) · [Paper](conjectures/c157/paper/paper.tex) |
| 166 | Disproof: 22-vertex counterexample; Foster's earlier diamond-chain construction acknowledged | [Research package](conjectures/c166/) · [Paper](conjectures/c166/paper/paper.tex) |
| 169 | Proof for order at least two; singleton convention documented | [Research package](conjectures/c169/) · [Paper](conjectures/c169/paper/paper.tex) |
| 171 | Disproof: infinite family of trees | [Research package](conjectures/c171/) · [Paper](conjectures/c171/paper/paper.tex) |
| 177 | Proof and strengthening: second-smallest degree | [Research package](conjectures/c177/) · [Paper](conjectures/c177/paper/paper.tex) |
| 179 | Proof of both degree interpretations and two separate strengthenings | [Research package](conjectures/c179/) · [Paper](conjectures/c179/paper/paper.tex) |

| 208 | Proof: sharp matching-number and missing-edge threshold for traceability | [Research package](conjectures/c208/) · [Paper](conjectures/c208/paper/paper.tex) |

| 361 | Proof: total domination, isolated support vertices and tree centers; characterizes the minimal excess case | [Research package](conjectures/c361/) · [Paper](conjectures/c361/paper/paper.tex) |

## Prior-related notes — NOT counted as novel resolutions

| Entry | Classification | Package |
|---|---|---|
| 76 | **Prior implication:** exact 43-vertex disproof and infinite family; Matoušek–Šámal's 2008 construction already implies an asymptotic refutation. | [Research package](conjectures/c76/) · [Paper](conjectures/c76/paper/paper.tex) |
| 137 | **Prior implication:** proof by Seinsche's 1974 cograph characterization; literal singleton exception and sharp bound documented. | [Research package](conjectures/c137/) · [Paper](conjectures/c137/paper/paper.tex) |
| 161 | **Not novel:** rediscovery of an implication of a stronger bound recorded in October 2005; also follows from an elementary degree bound. | [Research package](conjectures/c161/) · [Paper](conjectures/c161/paper/paper.tex) |
| 162 | **Prior-related:** closely related to a 2024 published theorem and its exchange argument. Priority not claimed; excluded from novel count. | [Research package](conjectures/c162/) · [Paper](conjectures/c162/paper/paper.tex) |

| 268 | **Prior-related:** total domination versus average center distance; proof uses a classical spanning-tree bound and its equality case. | [Research package](conjectures/c268/) · [Paper](conjectures/c268/paper/paper.tex) |
| 271 | **Prior-related:** total domination versus maximum-degree vertex distance; diameter bound and a separate dominating-edge argument. | [Research package](conjectures/c271/) · [Paper](conjectures/c271/paper/paper.tex) |

These six notes remain available for attribution, transparency and reproducibility, not as new solutions to previously unsolved problems.

## Reproducibility and status

Each package uses Python 3.12, pinned NetworkX and TeX Live. See its README for instructions. The matrix GitHub Actions workflow verifies and builds each paper, uploading separate PDF artifacts when the jobs run successfully. Original root-level c179 files remain as compatibility copies; the workflow checks that these match the canonical package. The former joint 161/162 manuscript remains in Git history, superseded by the two standalone papers.

Complete mathematical arguments are provided for author review; AI assistance is disclosed. No claim of independent peer review, formal proof-assistant verification, or established publication priority is made. Finite tests supplement the proofs rather than replacing them.

## Additional audit

The [cross-conjecture audit](audit/README.md) independently checks three inequalities, proof constructions, and equality counts on all 995 connected Atlas graphs of orders two through seven. The individual packages provide their own verification. CI checks the expected outputs.
