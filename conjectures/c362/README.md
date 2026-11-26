# Graffiti.pc Conjecture 362 — total domination, support components and diameter

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Archived open marker only; current primary entry unverified. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

The archived statement is dated February 18, 2009. No earlier exact proof or sharp strengthening was identified in the recorded bounded searches. The official entry could not be retrieved; an August 2026 public report records finite screening without resolution.

For every tree T of order at least three, with q the number of components induced by its support vertices and leaves, the conjecture asserts gamma_t(T) >= q + (1 + rad(T))/3. We prove gamma_t(T) >= q + ceil((diam(T)+1)/5), hence gamma_t(T) >= q + ceil(2 rad(T)/5). An infinite family attains the diameter bound; the asymptotic diameter and radius coefficients 1/5 and 2/5 cannot be increased.

[Manuscript](paper/paper.tex) · [Sources](SOURCES.md) · [Primary verifier](verification/verify.py) · [Second verifier](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local exact enumeration with NetworkX 3.6.1: 985 nonisomorphic trees of orders 3–12, 465 equality cases for the stronger diameter bound, zero violations; bitmask and direct subset enumeration gave identical domination numbers. All 100 constructed sharp examples passed. The committed scripts include additional independent invariant calculations. CI and PDF compilation not yet certified. AI-assisted research draft; human review, formal verification and publication priority remain pending.
