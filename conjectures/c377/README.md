# Graffiti.pc Conjecture 377 — isolated maximum-degree vertices and upper median degree

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Archived open marker only; current primary entry unverified. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

**Specific prior-art limitation:** Hongxing Jiang, *Some conjectures of Graffiti.pc on the total domination number of a tree*, Utilitas Mathematica 99 (2016), 33–42, may address this entry. Its bibliographic record was retrieved but its full text was not. No claim of first resolution is made.

For trees of order greater than two, let i count isolated vertices of the subgraph induced by the maximum-degree vertices. Conjecture 377 asserts that the total domination number is at least i plus the upper median of the degree sequence. We prove it, together with the common structural refinement: total domination is at least i+1, and if equality holds, both the number of distance medians and the upper median degree equal one. This also proves companion [#376](../c376/).

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Primary verifier](verification/verify.py) · [Second verifier](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local exact enumeration using bitmasks and direct subset enumeration agreed on all 985 nonisomorphic trees of orders 3–12, with 54 equality cases for this conjecture and no violations. The common excess-one condition occurred 35 times, all satisfying both conclusions. Finite tests supplement the analytic proof. CI, manuscript compilation, human review and publication priority remain pending. AI-assisted research draft.
