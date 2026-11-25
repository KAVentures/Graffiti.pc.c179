# Graffiti.pc conjectures — proofs and reproducibility

Research preprints by Koyar Afrasyab, November 2026. Eight conjecture packages, each with its own manuscript, source audit, pinned dependencies, exact verification and reproduction instructions. All eight were announced on 8 August 2005.

## Status at a glance (2026-11-25)

**Six candidate resolutions (priority unconfirmed); two prior-related notes excluded from the novel count. Zero independently certified first resolutions.** The November 2026 catalogue labels the entries open, but an open catalogue label is not proof that a result was unknown. See [NOVELTY.md](NOVELTY.md) for evidence and distinctions.

## Candidate resolutions — no exact earlier resolution identified in bounded searches

| Entry | Result | Package |
|---|---|---|
| 157 | Proof and strengthening: radial circles | [Research package](conjectures/c157/) · [Paper](conjectures/c157/paper/paper.tex) |
| 166 | Disproof: 22-vertex counterexample; Foster's earlier diamond-chain construction acknowledged | [Research package](conjectures/c166/) · [Paper](conjectures/c166/paper/paper.tex) |
| 169 | Proof for order at least two; singleton convention documented | [Research package](conjectures/c169/) · [Paper](conjectures/c169/paper/paper.tex) |
| 171 | Disproof: infinite family of trees | [Research package](conjectures/c171/) · [Paper](conjectures/c171/paper/paper.tex) |
| 177 | Proof and strengthening: second-smallest degree | [Research package](conjectures/c177/) · [Paper](conjectures/c177/paper/paper.tex) |
| 179 | Proof of both degree interpretations and two separate strengthenings | [Research package](conjectures/c179/) · [Paper](conjectures/c179/paper/paper.tex) |

## Prior-related notes — NOT counted as novel resolutions

| Entry | Classification | Package |
|---|---|---|
| 161 | **Not novel:** rediscovery of an implication of a stronger bound recorded in October 2005; also follows from an elementary degree bound. | [Research package](conjectures/c161/) · [Paper](conjectures/c161/paper/paper.tex) |
| 162 | **Prior-related:** closely related to a 2024 published theorem and its exchange argument. Priority not claimed; excluded from novel count. | [Research package](conjectures/c162/) · [Paper](conjectures/c162/paper/paper.tex) |

These two notes remain available for attribution, transparency and reproducibility, not as new solutions to previously unsolved problems.

## Reproducibility and status

Each package uses Python 3.12, pinned NetworkX and TeX Live. See its README for instructions. The matrix GitHub Actions workflow verifies and builds each paper, uploading separate PDF artifacts when the jobs run successfully. Original root-level c179 files remain as compatibility copies; the workflow checks that these match the canonical package. The former joint 161/162 manuscript remains in Git history, superseded by the two standalone papers.

Complete mathematical arguments are provided for author review; AI assistance is disclosed. No claim of independent peer review, formal proof-assistant verification, or established publication priority is made. Finite tests supplement the proofs rather than replacing them.

## Additional audit

The [cross-conjecture audit](audit/README.md) independently checks three inequalities, proof constructions, and equality counts on all 995 connected Atlas graphs of orders two through seven. The individual packages provide their own verification. CI checks the expected outputs.
