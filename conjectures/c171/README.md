# Conjecture 171 — Infinite tree counterexamples

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Catalogue: indexed text checked; image unavailable. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

Source: Ermelinda DeLaViña, *Written on the Wall II*, entry 171, announced 2005-08-08; November 2026 snapshot, listed open. See [source audit](SOURCES.md).

For a finite simple connected graph of order at least two, let L_s be its maximum spanning-tree leaf count, E the maximum number of vertices at even distance from any vertex, and D the average nonzero distance between peripheral vertices (vertices of maximum eccentricity). The conjecture asserts L_s >= (E-1)/D.

## Construction and result

For every even integer r >= 22, start with a root c, attach one path of length r, one path of length r-1 whose endpoint receives r new pendant leaves, and r further disjoint paths of length r-1. All paths share only c.

The resulting tree has n=r(r+2), L_s=2r+1, E=n/2 (both parity classes have equal size), diameter 2r, and exactly r+1 peripheral vertices. One peripheral vertex is the endpoint of the long path; the other r are the cluster of new leaves. Their pair distances are 2r for r pairs and 2 for r(r-1)/2 pairs. Hence D=(6r-2)/(r+1).

The difference (E-1)(r+1)-(2r+1)(6r-2) equals r^2(r-21)/2-2r+1 > 0 for even r >= 22. This disproves the conjecture. If even-distance counts exclude the root, subtract r+1 from this positive expression; it remains positive. The ratio of the claimed lower bound to actual leaf count grows without bound.

The first member of this family has 528 vertices, 45 leaves, E=264, D=130/23 and claimed lower bound 6049/130 > 45. No minimum-order claim is made.

## Research package

**Infinite Tree Counterexamples to Graffiti.pc Conjecture 171** — Koyar Afrasyab, November 2026. [Manuscript](paper/paper.tex), [source audit](SOURCES.md), [primary verifier](verification/verify.py), [independent verifier](verification/independent.py), [expected output](verification/expected.txt).

## Reproduce

Python 3.12 and TeX Live:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both exact verifiers were run locally on r=22,24,30,40; the primary uses NetworkX 3.6.1, the independent verifier only Python's standard library. The mathematical argument covers infinitely many parameters. CI is configured to reproduce the checks and compile the PDF. AI-assisted research preprint for author review; no guarantee of publication priority or formal certification.
