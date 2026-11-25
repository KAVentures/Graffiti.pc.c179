# Graffiti.pc Conjecture 76 — exact counterexample; prior implication

Announced April 4, 2004; still labelled open in the November 2026 catalogue.

The bound `tree(G) >= freq(T_max)/floor(avg_degree(G))` is false. A 43-vertex bipartite cactus has 56 edges, every vertex attains the triangle-count maximum zero, floor(avg_degree)=2, and largest induced tree order 21. Thus 21 < 43/2. A symmetric infinite family has n=2(3^(h+1)-1), m=8*3^h-4 and t=3(2^(h+1)-1); for h>=2 the violation grows without bound.

**Novelty classification:** related bridge-based recursive construction from Matoušek and Šámal (2008), Lemma 2.2, already implies an asymptotic disproof. Our explicit 43-vertex one-vertex-sum witness and exact formulas are documented, but this entry is excluded from the novel-resolution count. No minimality or first-priority claim.

[Standalone paper](paper/paper.tex) · [Source audit](SOURCES.md) · [Local execution output](verification/local-run.txt).

## Reproduce

From this folder (Python 3.12+):

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both exact scripts passed locally using Python 3.13.5 and NetworkX 3.6.1. Independent block-cut DP verifies the 43-vertex example and symmetric graphs through order 1456 and agrees with exhaustive induced-subset enumeration on 143 small connected Atlas graphs. The primary construction checks parameters through order 4372. The paper provides an analytic proof; computations are supplementary. New CI execution, formal certification and independent human review remain unconfirmed. AI assistance is disclosed.
