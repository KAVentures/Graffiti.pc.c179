# Graffiti.pc Conjecture 365 — isolated supports and degree-two edges

**Candidate resolution and sharp strengthening; priority unconfirmed.** The archived catalogue dataset marks the conjecture open, announced February 18, 2009. A public August 24, 2026 report records screening without a resolution. No earlier proof was identified in bounded searches. Current original entry could not be independently retrieved.

For every tree T of order at least three, let i count isolates in the induced subgraph of support vertices and e2 count edges whose endpoints both have degree two. We prove gamma_t(T) >= i + ceil((e2+1)/3), strengthening the conjectured gamma_t(T) >= i + e2/3. In fact for any total dominating set D with c induced components, e2 <= 2(|D|-i)+c-1. The coefficient 1/3 is optimal: a center with one leaf and m >= 2 paths of length five attached has i=m+1, e2=3m, gamma_t=2m+2.

[Manuscript](paper/paper.tex) · [Sources](SOURCES.md) · [Primary verifier](verification/verify.py) · [Second verifier](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local enumeration using bitmasks and direct subset enumeration: all 985 nonisomorphic trees of orders 3–12, 95 equality cases for the strengthened integer bound, zero violations, zero disagreement on the total domination number. The committed versions also verify the finite sharpness examples. CI and paper builds not yet certified. Human author review, formal verification and publication priority remain pending. AI-assisted research draft.
