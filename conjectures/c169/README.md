# Graffiti.pc Conjecture 169

**A Proof of Graffiti.pc Conjecture 169: Spanning-Tree Leaves and Distance Parity** — Koyar Afrasyab, November 2026.

For a connected simple graph of order at least two, let e(v) count vertices at even distance from v and L_s be the maximum spanning-tree leaf number. We prove the stronger pointwise inequality

`|2e(v)-n| <= L_s-1`

and hence `L_s >= 1+max(e)-min(e)`. The original statement has a singleton exception if leaves are strictly degree-one vertices; otherwise it holds for every nonempty connected graph. Stars attain equality.

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Expected output](verification/expected.txt).

## Reproduce

From this directory, with Python 3.12 and TeX Live:

```sh
python -m pip install -r requirements.txt
python verification/verify.py
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The primary exact local audit found 85 equalities and no violations on all 995 connected Atlas graphs of orders 2–7. The independent packaged verifier and PDF build are configured in CI. Finite checks are not the proof; no formal certification, independent review or guaranteed priority is claimed. AI assistance is disclosed.
