# Graffiti.pc Conjecture 208 — proof and sharp threshold

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Catalogue: indexed text checked; image unavailable. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

Candidate resolution, priority unconfirmed. Announced January 12, 2006; listed open in the November 2026 catalogue.

For every connected nontraceable simple graph with at least two vertices, the number of missing edges m satisfies m >= 3*mu-1, where mu is maximum matching size. Equivalently the graph is traceable if mu >= 1/2 + m/3. Chvatal's degree-sequence theorem reduces the proof to explicit matching arguments at orders 4, 6, and 8. Two equality graphs of orders 5 and 6 show sharpness.

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Local run](verification/local-run.txt)

## Reproduce

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both programs ran locally with Python 3.13.5 and NetworkX 3.6.1: 995 connected graphs, 235 qualifying, 144 nontraceable, 2 sharp witnesses, 0 violations. Order 8 is resolved analytically; no order-8 exhaustive search is claimed. CI, PDF compilation, formal proof certification, peer review and publication priority are unconfirmed. Run Python without optimization so assertions remain enabled.
