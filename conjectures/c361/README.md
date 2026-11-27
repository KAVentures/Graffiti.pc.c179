# Graffiti.pc Conjecture 361 — isolated support vertices and centers

> **Research status:** Candidate; priority unconfirmed. **Open-status evidence:** Archived open marker only; current primary entry unverified. See [source audit](SOURCES.md) and [repository status policy](../../STATUS.md).

[All conjectures](../README.md) · [Main index](../../README.md) · [Reproduction guide](../../REPRODUCE.md)

**Candidate resolution; priority unconfirmed.** The archived catalogue dataset marks the conjecture open, announced February 18, 2009. No earlier exact proof was identified in bounded searches. The latest original catalogue page could not be retrieved; see the source audit. An August 2026 public report records finite screening of this entry without a resolution.

For every tree T on at least three vertices, let S be its support vertices, i the number of isolates of T[S], and C its center. Then gamma_t(T) >= i + |C|. The proof also characterizes all trees with i > 0 and gamma_t(T) = i + 1.

[Manuscript](paper/paper.tex) · [Source audit](SOURCES.md) · [Primary verifier](verification/verify.py) · [Independent verifier](verification/independent.py).

## Reproduce

Python 3.12 and NetworkX 3.6.1:

    python -m pip install -r requirements.txt
    python verification/verify.py
    python verification/independent.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Fresh local exact enumeration using the bitmask algorithm: 985 nonisomorphic trees of orders 3–12, 179 equality cases, no violations. The committed independent checker, classification test and PDF build are configured for CI. No external referee review, formal proof-assistant verification or certified publication priority. AI-assisted research draft for author review.
