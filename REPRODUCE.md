# Reproduce the research

## Canonical directory layout

```
conjectures/cNNN/
  README.md
  SOURCES.md
  requirements.txt
  paper/paper.tex
  verification/verify.py
  verification/independent.py
  verification/expected.txt
  verification/local-run.txt   # where an execution log was retained
```

All 17 packages use the same required paths. Run commands from a chosen numbered directory (for example c362). Root-level paper, verification, requirements and SOURCES files are legacy copies of #179; do not use them for other conjectures.

## Run one package

Use Python 3.12 and a fresh virtual environment. Install TeX Live separately for manuscript builds.

```sh
cd conjectures/c362
python -m pip install -r requirements.txt
python verification/verify.py > observed.txt
diff -u verification/expected.txt observed.txt
python verification/independent.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The exact commands and domains are also documented in individual README files. Compare actual output with expected output; the expected file alone does not demonstrate a successful run. Independent implementations mean independent algorithms, not independent researchers.

## Continuous integration

The [reproduction workflow](.github/workflows/reproduce.yml) runs both verifiers for every package, checks expected output, builds each manuscript and attaches a PDF artifact named manuscript-cNNN to successful runs. It also checks the #179 legacy copies, the cross-conjecture audit and repository metadata consistency. See [Actions](https://github.com/KAVentures/Graffiti.pc.c179/actions) for actual run status. A draft pull request or configured workflow does not imply passed checks or a built PDF.

## Repository consistency

From the repository root run `python audit/check_catalogue.py`. The check enforces matching package directories, required files, metadata labels, navigation links and the workflow matrices. This is structural validation, not a proof or a priority check.
