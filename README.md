# Graffiti.pc conjectures — proofs and reproducibility

Research preprints for author review, November 2026. This collection contains three complete analytic arguments for conjectures announced on 8 August 2005 in Ermelinda DeLaViña's *Written on the Wall II*. The repository retains its original name and c179 file paths for compatibility.

| Conjecture | Result | Manuscript / proof |
| --- | --- | --- |
| 161 | Maximum spanning-tree leaf number is at least the maximum local independence of the complement | [Proof](conjectures/c161/README.md) |
| 162 | A lower bound involving minimum local independence and minimum degree | [Proof](conjectures/c162/README.md) |
| 179 | Spanning-tree leaves, bipartite number and domination; strengthened inequality | [Original manuscript](paper/paper.tex) · [Entry](conjectures/c179/README.md) |

[Joint manuscript for 161 and 162](conjectures/c161-c162/paper.tex) · [Source audit for 161/162](conjectures/c161-c162/SOURCES.md) · [Original c179 source audit](SOURCES.md).

**Status:** complete elementary or literature-dependent mathematical arguments, not claims of peer review, formal proof-assistant certification, or established publication priority. AI assistance is disclosed. Finite computation supports, but does not replace, the proofs.

## Reproduce the new results

From the repository root, Python 3.12:

```sh
python -m pip install -r requirements.txt
python conjectures/c161-c162/verify.py
```

The verifier computes local independence exactly and compares two independent leaf-number algorithms (connected domination and direct spanning-tree enumeration). See [expected output](conjectures/c161-c162/expected.txt). To build the joint manuscript:

```sh
cd conjectures/c161-c162
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

## Original c179 entry


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
