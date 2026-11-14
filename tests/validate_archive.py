"""Validate public archive relationships and file integrity without network access.

Run from any directory: python tests/validate_archive.py
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

cards = read("catalog/source-cards.json")
references = read("catalog/references.json")
crosswalk = read("catalog/book-experience-crosswalk.json")
checks = read("originals/books/2026-11-13/C04_source_apparatus_extract.json")
coverage = read("catalog/coverage.json")["counts"]
provenance = read("provenance.json")
by_id = {row["source_card_id"]: row["card"] for row in cards}
assert len(by_id) == len(cards) == coverage["source_cards"]
assert len(references) == coverage["deduplicated_reference_records"]
assert len(crosswalk["rows"]) == coverage["book_rows"]
assert len(checks["records"]) == coverage["book_source_apparatus_records"]
seen = set()
for number in range(1, 13):
    section = read(f"doors/albaview/sections/{number:02d}/sources.json")
    assert section["section"]["id"] == f"C{number:02d}"
    for card_id, card in section["experience_cards"].items():
        assert card_id in by_id, card_id
        assert card == by_id[card_id], card_id
        seen.add(card_id)
unassigned = sorted(set(by_id) - seen)
assert seen <= set(by_id)
# Unassigned original cards remain inspectable in the viewer; do not assign them by inference.
assert len({row["row_id"] for row in crosswalk["rows"]}) == len(crosswalk["rows"])
for entry in provenance["files"]:
    content = (ROOT / entry["path"]).read_bytes()
    assert len(content) == entry["bytes"], entry["path"]
    assert hashlib.sha256(content).hexdigest() == entry["sha256"], entry["path"]
for path in ["index.html", "assets/archive.js", "assets/archive.css", ".nojekyll"]:
    assert (ROOT / path).is_file(), path
print(json.dumps({"result": "PASS", "sections": 12, "cards": len(cards),
                  "references": len(references), "book_rows": len(crosswalk["rows"]),
                  "check_notes": len(checks["records"]), "unassigned_source_cards": unassigned,
                  "files_with_verified_sha256": len(provenance["files"])}))
