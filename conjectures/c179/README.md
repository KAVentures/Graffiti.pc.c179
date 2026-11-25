# Graffiti.pc Conjecture 179

**A Proof of Graffiti.pc Conjecture 179: Spanning-Tree Leaves, Bipartite Number and Domination** — Koyar Afrasyab, November 2026. Research preprint for author review.

For every finite simple connected graph of order at least two, the proof gives

`L_s + b >= delta + gamma + lambda + max(0, ceil(lambda/2)-2)`.

Here delta is minimum degree, gamma is ordinary domination number, and lambda is maximum neighborhood independence. See [manuscript](paper/paper.tex), [source audit](SOURCES.md), and [verification](verification/verify.py).

The analytic proof uses DeLaViña and Waller (2008), Theorem 5, and elementary domination arguments. Finite tests are supplementary, not the proof. Independent peer review and formal proof-assistant verification are not claimed. AI assistance is disclosed in the manuscript.

## Reproduce

Python 3.12 or later:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
```

Compare with [expected output](verification/expected.txt). Build the paper with TeX Live:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Both exact implementations passed locally, with zero disagreements on all 995 graphs. GitHub Actions is configured to check both calculations and build a downloadable PDF artifact when workflow permissions permit. See SOURCES.md for provenance and review limitations.

## Additional reproducibility check

The [cross-conjecture audit](../../audit/README.md) checks all three statements and proof constructions through direct enumeration, with recorded output. It supplements the standalone checks and is not needed for the proof.
