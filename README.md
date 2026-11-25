# Graffiti.pc conjectures — proofs and reproducibility

Research preprints by Koyar Afrasyab, November 2026. Each conjecture has a self-contained research package with its own manuscript, source audit, pinned dependencies, exact verification and reproducibility instructions. All three were announced on 8 August 2005.

## Conjecture 161 — Spanning-tree leaves and complement local independence

[Research package](conjectures/c161/) · [Paper](conjectures/c161/paper/paper.tex) · [Source audit](conjectures/c161/SOURCES.md) · [Verification](conjectures/c161/verification/)

## Conjecture 162 — Spanning-tree leaves and simplicial vertices

[Research package](conjectures/c162/) · [Paper](conjectures/c162/paper/paper.tex) · [Source audit](conjectures/c162/SOURCES.md) · [Verification](conjectures/c162/verification/)

## Conjecture 179 — Spanning-tree leaves, bipartite number and domination

[Research package](conjectures/c179/) · [Paper](conjectures/c179/paper/paper.tex) · [Source audit](conjectures/c179/SOURCES.md) · [Verification](conjectures/c179/verification/)

## Reproducibility and status

Each package uses Python 3.12, pinned NetworkX and TeX Live. See its README for instructions. The matrix GitHub Actions workflow independently verifies and builds each paper, uploading separate PDF artifacts. Original root-level c179 files remain as compatibility copies; the workflow checks that these match the canonical package. The former joint 161/162 manuscript remains in Git history, superseded by the two standalone papers.

Complete mathematical arguments are provided for author review; AI assistance is disclosed. No claim of independent peer review, formal proof-assistant verification, or established publication priority is made. Finite tests supplement the proofs rather than replacing them.
