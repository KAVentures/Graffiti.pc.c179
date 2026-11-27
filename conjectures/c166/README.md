# Conjecture 166 — disproof by a 22-vertex graph

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Catalogue: indexed text checked; image unavailable. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

**Status: candidate disproof, priority unconfirmed.** No earlier disproof of the exact WOW-II statement was identified in a bounded search. Craig Foster's 2005 diamond-chain construction under conjecture 165 is credited as prior related work; the diamond gadget itself is not claimed as novel. See [source audit](SOURCES.md) and [repository novelty audit](../../NOVELTY.md).

Conjecture 166, announced 2005-08-08, asserts that the maximum spanning-tree leaf number is at least the number of vertices outside but adjacent to the maximum-degree set, divided by the square root of the radius.

The counterexample has three identical arms attached to a central vertex c. Each arm has distinct vertices a,b,u,x,y,v,z and edges c-a, a-b, b-u, u-x, x-v, v-y, y-u, v-z. There are no other edges.

There are 22 vertices, 24 edges, 7 maximum-degree vertices, 15 external neighbors of that set, radius 6, diameter 12. Every spanning tree deletes one edge from each four-cycle and retains all bridges. It therefore has exactly four degree-three vertices and six leaves. This violates the bound because 15² > 6² × 6 (225 > 216).

[Standalone manuscript](paper/paper.tex) · [Primary verifier](verification/verify.py) · [Independent verifier](verification/independent.py) · [Recorded local run](verification/local-run.txt).

## Reproduce

From this folder:
```sh
python -m pip install -r requirements.txt
python verification/verify.py > /tmp/c166-output.txt
diff -u verification/expected.txt /tmp/c166-output.txt
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both implementations exhaustively check 2,024 possible edge subsets, yielding 64 spanning trees with six leaves each. All checks passed locally. CI is configured to rerun both programs and build the PDF. The proof does not depend on enumeration. No minimal-order, formal-certification, peer-review or guaranteed-priority claim is made. AI assistance is disclosed in the manuscript.
