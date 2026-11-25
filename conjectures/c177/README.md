# Graffiti.pc Conjecture 177

**The Second-Smallest Degree, Independence, and Spanning-Tree Leaves: A Proof of Graffiti.pc Conjecture 177** — Koyar Afrasyab, November 2026 (AI-assisted preprint for author review).

For a finite simple connected graph with at least two vertices, the paper proves

`L_s + b >= 2*alpha + sigma(G)`.

Here sigma(G) is the second-smallest degree with multiplicity. DeLaViña and Waller (2008), Theorem 3, proved the weaker bound with 1 replacing sigma. The new proof extends their component method by reserving removable leaves in the complement of an independent set and using a separate clique-component case.

**Stronger result:** for every independent set A with at least two vertices, L_s + b >= 2*|A| + sigma_A, where sigma_A is the second-smallest of the original graph degrees of members of A. This implies the conjecture by choosing a maximum independent set. Equality holds for complete graphs and stars of order at least three.

[Paper](paper/paper.tex) · [Source and prior-art audit](SOURCES.md) · [Verification](verification/) · [Local run](verification/local-run.txt).

## Reproduce

From this folder, use Python 3.12+ and TeX Live.

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Primary and independent algorithms ran locally with Python 3.13.5, NetworkX 3.6.1: 995 connected Atlas graphs, 147 equality cases, 13,067 constructive witness domains and 845 maximum-independent-set choices where the refinement uses a strictly larger degree. Zero violations. The universal proof does not rely on these finite checks.

**Status:** candidate novel resolution of the stated conjecture. No earlier full proof identified in bounded searches; independent peer review, formal certification and exclusive publication priority are not established. CI PDF compilation and execution for the new revision are unconfirmed.
