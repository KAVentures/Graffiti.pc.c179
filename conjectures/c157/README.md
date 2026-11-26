# Conjecture 157 — Spanning-tree leaves and edges in radial circles

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Catalogue: page image checked. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

Source: *Written on the Wall II*, conjecture 157, announced 2005-08-08, catalogue updated 2026-11-05, printed page 90. See [source audit](SOURCES.md).

For a finite simple connected graph G let L_s be the maximum number of degree-one vertices in a spanning tree, P the degree-one vertices, C the center, and R(v) the vertices at distance rad(G) from v in C. Write M = max_{v in C} |E(G[R(v)])|.

**Conjecture:** L_s >= |P| + sqrt(2M).

**Proof:** For any root v in a connected graph of order at least two, all vertices in its last distance layer F(v) are leaves of a breadth-first spanning tree; every vertex of P is also a leaf of that tree. Thus L_s >= |P| + |F(v) minus P|. No pendant vertex in the last layer has an edge within it, since its sole neighbor lies in the preceding layer. If s = |F(v) minus P| and m counts edges within F(v), then 2m <= s(s-1) <= s^2. Choose a central root maximizing m; F(v) = R(v). The singleton graph has L_s = |P| = M = 0, so the original conjecture also holds there.

For M > 0, the stronger integer bound is L_s >= |P| + ceil((1 + sqrt(1+8M))/2); for M = 0 the additive term is zero. This is sharp: take a clique K_{k+1}, k >= 2, and attach t >= 1 pendant vertices to one of its vertices. That vertex is the unique center, M = k(k-1)/2, |P| = t, and a spanning star achieves L_s = k+t. The structural inequality holds for every root when the graph has at least two vertices.

## Research package

**A Proof of Graffiti.pc Conjecture 157: Spanning-Tree Leaves and Radial Circles** — Koyar Afrasyab, November 2026. [Standalone manuscript](paper/paper.tex), [source audit](SOURCES.md), [primary verifier](verification/verify.py), [independent verifier](verification/independent.py), [expected output](verification/expected.txt).

## Reproduce

From this folder, using Python 3.12 and TeX Live:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both exact algorithms were run locally with NetworkX 3.6.1 on all 996 connected Atlas graphs of orders 1–7; 110 sharp-family instances were also checked by the primary verifier. CI is configured to reproduce the standalone package and build the PDF. Finite tests supplement the proof. AI assistance is disclosed; no claim of independent peer review, formal proof-assistant certification or guaranteed publication priority is made.
