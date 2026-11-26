# Research status and evidence policy

Last consolidated 2026-11-26 from the per-package source audits. This is a conservative documentation audit, not a fresh exhaustive peer review of the entire literature.

Three independent questions must be kept separate:

1. **Mathematical result:** the manuscript contains a proof, a disproof, or a proof restricted to a stated domain. Singleton exceptions and ambiguous source notation must be stated, not silently discarded.
2. **Open-status evidence:** evidence of the original catalogue's open marker, not a claim that the mathematical literature contains no solution.
3. **Priority classification:** whether prior implications or close earlier results were identified. A bounded search cannot certify first discovery.

| Evidence level | Meaning |
|---|---|
| Catalogue: page image checked | The source audit records visual inspection of the original catalogue entry as well as its statement. Historical snapshot only. |
| Catalogue: indexed text checked; image unavailable | Indexed primary-source text was examined; direct page image retrieval failed or was not confirmed. Historical snapshot only. |
| Archived open marker only; current primary entry unverified | Statement and open marker were recovered from a secondary archive. The latest official entry could not be independently retrieved. These entries are #361, #362 and #365. |

| Priority class | Meaning |
|---|---|
| Candidate; priority unconfirmed | No earlier exact resolution located in the recorded bounded search. Not a guarantee of novelty. |
| Prior implication; not novel | Known result already implies the resolution; preserved for attribution and documentation. |
| Prior-related; excluded from novel count | Substantially related earlier result or proof machinery; no claim of a new theorem or first resolution. |

The primary-catalogue status dates to the November 2026 snapshot described in each source audit. "Open" is historical metadata, not present-day proof of unresolved status. An archived marker must never be upgraded solely because it is marked O, and a public screening report is not a proof of novelty. No package has independently certified priority or formal/human referee certification. CI, when green, establishes the reproducibility checks it actually runs, not mathematical correctness or novelty.

The machine-readable [catalogue](catalogue.json) records these distinctions. [NOVELTY.md](NOVELTY.md) retains the detailed research notes. If earlier work is identified, update the classification, source audit, package README, root index and catalogue in the same change; preserve credit and the mathematical package.
