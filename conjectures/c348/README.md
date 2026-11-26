# Graffiti.pc Conjecture 348 — total domination and degree-two neighborhoods

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Archived open marker only; current primary entry unverified. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

The archived entry is dated February 18, 2009 and marked open. The latest original entry could not be retrieved. No earlier exact proof or implication was identified in the bounded literature search; publication priority remains unconfirmed.

For a tree T of order at least three, let D2 denote its degree-two vertices and b = |N(D2) minus D2|. The conjecture asserts gamma_t(T) >= 2b/3. We prove that for any total dominating set D of size k inducing c components, 3b <= 3k+2c-2, and therefore gamma_t(T) >= ceil((3b+2)/4). The improvement from 2/3 to 3/4 is proved; optimality of the new coefficient is not claimed.

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Primary verifier](verification/verify.py) · [Independent verifier](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local enumeration with NetworkX 3.6.1: 2,286 nonisomorphic trees of orders 3–13, 103 strengthened equality cases and no violations. Exact exhaustive subset enumeration cross-checked all 985 trees of orders 3–12, with no disagreements on total domination. CI, manuscript compilation and human referee review remain pending. AI-assisted research draft.
