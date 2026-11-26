# Graffiti.pc Conjecture 268 — Total Domination and Average Center Distance

**Prior-related documented resolution; priority unconfirmed. Excluded from novel count.** The catalogue lists this entry open, announced February 23, 2007. The proof uses the published total-domination spanning-tree diameter estimate (2007) with an additional center-pair argument. No prior exact numbered resolution identified in the bounded literature search; this does not certify novelty.

## Statement

For finite simple connected graphs of order at least two, gamma_t(G) >= floor(1 + average distance between distinct centers). A singleton center is assigned mean zero.

[Standalone proof](paper/paper.tex) · [Source audit](SOURCES.md) · [Primary verifier](verification/verify.py) · [Independent verifier](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local exhaustive check on 995 connected Atlas graphs of orders 2–7: 650 equalities, zero violations. The committed independent checker and PDF build are configured for CI; no claim of external peer review or formal verification. Author review pending. AI-assisted research.
