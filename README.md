# Graffiti.pc Conjecture 179

Koyar Afrasyab — research preprint and reproducibility materials. See `paper/paper.tex` for the proof and `verification/verify.py` for the finite checks.

The proof uses DeLaViña and Waller (2008), Theorem 5, and elementary domination arguments. Finite tests are supplementary, not the proof. Independent peer review and formal proof-assistant verification are not claimed.

## Reproduce

Python 3.12 or later:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
```

Build the paper using a standard TeX Live installation (amsmath, amsthm, geometry, hyperref):

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

See `SOURCES.md` for provenance, assumptions, and review limitations.
