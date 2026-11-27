"""Check archive navigation and evidence labels without third-party dependencies."""
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
cat = json.loads((root / "catalogue.json").read_text())
entries = cat["entries"]
ids = [f"c{e['id']}" for e in entries]
assert len(ids) == len(set(ids)) and ids == sorted(ids, key=lambda x: int(x[1:]))
actual = {p.name for p in (root / "conjectures").iterdir()
          if p.is_dir() and re.fullmatch(r"c\d+", p.name)}
assert actual == set(ids), (actual, ids)
readme = (root / "README.md").read_text()
index = (root / "conjectures/README.md").read_text()
workflow = (root / ".github/workflows/reproduce.yml").read_text()
matrices = re.findall(r"conjecture:\s*\[([^\]]+)\]", workflow)
assert len(matrices) == 2
for matrix in matrices:
    assert [s.strip() for s in matrix.split(",")] == ids
required = ["README.md", "SOURCES.md", "requirements.txt", "paper/paper.tex",
            "verification/verify.py", "verification/independent.py", "verification/expected.txt"]
for e, cid in zip(entries, ids):
    p = root / "conjectures" / cid
    for name in required:
        assert (p / name).is_file(), (cid, name)
    assert e["priority_certified"] is False
    source = cat["evidence_labels"][e["source"]]
    priority = cat["priority_labels"][e["priority"]]
    note = f"> **Research status:** {priority}. **Open-status evidence:** {source}."
    assert note in (p / "README.md").read_text(), cid
    assert f"conjectures/{cid}/paper/paper.tex" in readme, cid
    assert f"conjectures/{cid}/SOURCES.md" in readme, cid
    assert f"{cid}/paper/paper.tex" in index, cid
print(f"Catalogue audit: {len(ids)} packages; both matrices, evidence notes and navigation consistent")
