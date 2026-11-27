# Conjecture 137 — induced paths and complement path covers

> **Research status:** Prior implication; not novel. **Open-status evidence:** Catalogue: indexed text checked; image unavailable. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

**Prior implication; not counted as a novel theorem.** No separately documented resolution of the exact catalogue entry was identified in bounded searches on 2026-11-26. Priority unconfirmed.

For a simple connected graph G of order at least two, let L be the largest order of an induced path and k the minimum number of vertex-disjoint ordinary paths covering the complement. Then Lk >= 4. If k >= 2, any edge suffices. If k = 1, the complement is connected, and Seinsche's classical characterization gives an induced P4. A self-contained proof is in the manuscript. The literal singleton is an exception, since L=k=1; the catalogue's testing convention concerns nontrivial connected graphs.

For order >= 3, k=2 even implies L>=3 (a connected noncomplete graph contains an induced P3). More generally, connected and complement-connected graphs contain an induced P4 regardless of the path-cover number. The constant 4 is sharp at P4.

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Primary checker](verification/verify.py) · [Independent checker](verification/independent.py).

## Reproduce

Python 3.12; NetworkX 3.6.1.

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

The primary algorithm was run locally on 995 connected Atlas graphs of orders 2–7 (304 equalities, zero violations); the independent implementation and manuscript build are supplied for CI. Finite tests are not the universal proof. AI-assisted research note, human review and publication priority unconfirmed. No claim of independently certified novelty.
