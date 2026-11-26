# Graffiti.pc — conjecture resolutions and reproducibility

An AI-assisted research collection of proofs, counterexamples and sharpened bounds for numbered conjectures from *Written on the Wall II* (Graffiti.pc). Manuscripts are drafts for human author and referee review, not peer-reviewed publications.

**17 research packages:** 8 candidate resolutions with primary-catalogue evidence, 3 candidate resolutions with archived-only open evidence, and 6 prior-related notes. **Zero independently certified first resolutions.** All counts distinguish mathematical resolution, catalogue status and publication priority.

## Start here

- [Browse by number and subject](conjectures/README.md) — compact alphabetical subject index and numerical directory.
- [Status and evidence policy](STATUS.md) — what each label means, including the distinction between an open catalogue and genuinely novel mathematics.
- [Novelty and source audit](NOVELTY.md) — detailed prior-art notes and limitations for every entry.
- [Reproduce the results](REPRODUCE.md) — commands, package structure, and CI artifacts.
- [Cross-conjecture audit](audit/README.md) — additional checks of selected inequalities.
- [Machine-readable catalogue](catalogue.json) — metadata for all packages.

## Candidate resolutions — primary catalogue checked

No earlier exact resolution was identified in the recorded bounded searches. Priority remains unconfirmed. Indexed text and visually inspected pages are distinguished.

| Entry | Topic and result | Open-status evidence | Links |
|---|---|---|---|
| **138** | Independent sets / distance — Disproof. Infinite subcubic tree family; sharp square-distance coefficient. | Catalogue: page image checked | [Overview](conjectures/c138/) · [Paper](conjectures/c138/paper/paper.tex) · [Sources](conjectures/c138/SOURCES.md) |
| **157** | Spanning-tree leaves / radial circles — Proof + strengthening. Breadth-first spanning tree; sharp integer refinement. | Catalogue: page image checked | [Overview](conjectures/c157/) · [Paper](conjectures/c157/paper/paper.tex) · [Sources](conjectures/c157/SOURCES.md) |
| **166** | Spanning-tree leaves / degree neighborhoods — Disproof. 22-vertex witness; earlier diamond-chain gadget credited. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c166/) · [Paper](conjectures/c166/paper/paper.tex) · [Sources](conjectures/c166/SOURCES.md) |
| **169** | Spanning-tree leaves / even distances — Proof (n ≥ 2); K1 exception. Singleton convention explicitly documented. | Catalogue: page image checked | [Overview](conjectures/c169/) · [Paper](conjectures/c169/paper/paper.tex) · [Sources](conjectures/c169/SOURCES.md) |
| **171** | Spanning-tree leaves / boundary distances — Disproof. Infinite tree counterexample family. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c171/) · [Paper](conjectures/c171/paper/paper.tex) · [Sources](conjectures/c171/SOURCES.md) |
| **177** | Spanning-tree leaves / induced bipartite subgraphs — Proof + strengthening. Second-smallest degree; prior weaker theorem credited. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c177/) · [Paper](conjectures/c177/paper/paper.tex) · [Sources](conjectures/c177/SOURCES.md) |
| **179** | Spanning-tree leaves / domination — Proof + strengthening. Both minimum- and maximum-degree interpretations. | Catalogue: page image checked | [Overview](conjectures/c179/) · [Paper](conjectures/c179/paper/paper.tex) · [Sources](conjectures/c179/SOURCES.md) |
| **208** | Hamiltonian paths / matchings — Proof. Sharp matching and missing-edge threshold. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c208/) · [Paper](conjectures/c208/paper/paper.tex) · [Sources](conjectures/c208/SOURCES.md) |

## Candidate resolutions — archived open marker only

These proofs and strengthenings are retained, but the latest official primary-source entry could not be independently retrieved. They must not be presented as confirmed-open or independently certified first resolutions.

| Entry | Topic and result | Open-status evidence | Links |
|---|---|---|---|
| **361** | Total domination in trees / isolated supports — Proof + characterization. Minimal-excess structural characterization. | Archived open marker only; current primary entry unverified | [Overview](conjectures/c361/) · [Paper](conjectures/c361/paper/paper.tex) · [Sources](conjectures/c361/SOURCES.md) |
| **362** | Total domination in trees / radius and diameter — Proof + sharp strengthening. Radius-two ball covering; optimal diameter and radius coefficients. | Archived open marker only; current primary entry unverified | [Overview](conjectures/c362/) · [Paper](conjectures/c362/paper/paper.tex) · [Sources](conjectures/c362/SOURCES.md) |
| **365** | Total domination in trees / degree-two edges — Proof + sharp strengthening. Component-sensitive counting; optimal coefficient. | Archived open marker only; current primary entry unverified | [Overview](conjectures/c365/) · [Paper](conjectures/c365/paper/paper.tex) · [Sources](conjectures/c365/SOURCES.md) |

## Prior-related notes — excluded from candidate novelty count

These entries remain available to document proofs, disproofs or implications of previously published results. The catalogue's open label may be stale.

| Entry | Topic and result | Open-status evidence | Links |
|---|---|---|---|
| **76** | Induced trees / triangles — Disproof. 43-vertex witness and unbounded family; earlier Matoušek–Šámal theorem implies refutation. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c76/) · [Paper](conjectures/c76/paper/paper.tex) · [Sources](conjectures/c76/SOURCES.md) |
| **137** | Induced paths / path covers — Proof (n ≥ 2); K1 exception. Seinsche’s cograph characterization. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c137/) · [Paper](conjectures/c137/paper/paper.tex) · [Sources](conjectures/c137/SOURCES.md) |
| **161** | Spanning-tree leaves / local independence — Proof. Earlier stronger bound and elementary degree bound. | Catalogue: page image checked | [Overview](conjectures/c161/) · [Paper](conjectures/c161/paper/paper.tex) · [Sources](conjectures/c161/SOURCES.md) |
| **162** | Spanning-tree leaves / minimum local independence — Proof. Related 2024 published exchange argument. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c162/) · [Paper](conjectures/c162/paper/paper.tex) · [Sources](conjectures/c162/SOURCES.md) |
| **268** | Total domination / center distances — Proof. 2007 diameter estimate and additional center-pair argument. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c268/) · [Paper](conjectures/c268/paper/paper.tex) · [Sources](conjectures/c268/SOURCES.md) |
| **271** | Total domination / maximum-degree distances — Proof. 2007 diameter estimate and dominating-edge argument. | Catalogue: indexed text checked; image unavailable | [Overview](conjectures/c271/) · [Paper](conjectures/c271/paper/paper.tex) · [Sources](conjectures/c271/SOURCES.md) |

## About the archive

Each numbered directory contains a standalone manuscript, source audit, pinned dependencies, exact verification scripts and expected output. Where possible, a second computational implementation is supplied. Finite tests complement universal mathematical arguments; they do not prove universal statements or establish priority. Existing root-level files for #179 are retained solely for backward compatibility. See [reproduction guide](REPRODUCE.md) for the canonical paths.

Corrections, prior proofs and better references are welcome. Cite the exact manuscript and commit, not a purported certified first solution. AI contributions are disclosed; human review and authorship confirmation remain pending where indicated in the manuscripts.
