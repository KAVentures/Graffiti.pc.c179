# Graffiti.pc Conjecture 138 — disproof and sharp coefficient

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Catalogue: page image checked. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

Candidate resolution, priority unconfirmed. Announced July 12, 2005; listed open in the November 2026 catalogue.

Start with a path x0,...,x(2k), attach two leaves to each endpoint, k>=7. The resulting subcubic tree has order 2k+5, unique maximum independent set of size k+4, largest induced path of order 2k+3, and exactly two square-degree maximizers x1 and x(2k-1) of square degree 5. Their square distance is k-1 and original distance 2k-2. Thus the conjectured bound with coefficient 3 fails by k-6 even for square distances. The smallest witness in this family has 19 vertices. No global minimality claim.

For square distances, coefficient 2 is universally valid and asymptotically sharp even on subcubic trees with unique maximum independent sets.

[Paper](paper/paper.tex) · [Source and novelty audit](SOURCES.md) · [Local run](verification/local-run.txt)

## Reproduce

From this directory with Python 3.12+:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both algorithms executed locally with Python 3.13.5 and NetworkX 3.6.1 for the primary implementation, through order 205. The second implementation uses only the Python standard library. The paper gives a universal analytic proof. CI and formal certification are unconfirmed; independent peer review and priority are not established. AI assistance is disclosed.
