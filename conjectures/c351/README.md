# Graffiti.pc Conjecture 351 — counterexample family for total domination

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Archived open marker only; current primary entry unverified. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

The archived entry is dated February 18, 2009, with open marker O. The original catalogue entry remains unverified. No earlier exact disproof was identified in the bounded literature search; publication priority remains unconfirmed.

For a tree T on more than two vertices, write S for its support vertices, L for its leaves, Q for its degree-two vertices and c for the number of components. The conjecture asserts gamma_t(T) >= c(T[S union L]) + c(T[N(Q) union Q]).

Our family T_m, m >= 3, has order 18m+1, the two component counts 7m and 3m, and exact total domination number 9m+1. The conjectured lower bound exceeds gamma_t by m-1, which grows without bound. At m=3, a 55-vertex witness has gamma_t=28 and proposed bound 30. No claim of minimum counterexample order is made.

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Explicit witness](verification/witness.json) · [Primary verifier](verification/verify.py) · [Independent certificate checker](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local computation with NetworkX 3.6.1 confirmed the formulas and exact tree-DP total domination number on 100 family members (m=3 through 102). The supplied explicit witness also has a standard-library checker using disjoint forced-neighborhood certificates. The universal disproof is analytic; finite tests are supplementary. CI, manuscript compilation, external review and publication priority remain pending. AI-assisted research draft.
