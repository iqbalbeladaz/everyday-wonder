#!/usr/bin/env python3
"""One Floor of Home — entry program.

Writes one sentence about a small moment of wonder in everyday life to
/output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The sentence: a lift door opens on a stranger humming the narrator's dead
grandmother's lullaby, and for one floor the whole building feels like
home. The wonder is the collision of the utterly ordinary (a lift, a
stranger humming) with the deeply personal (a dead grandmother's
lullaby) — a private memory arriving uninvited in a public box, turning
a building into home for exactly one floor. No worn image, no
explanation; the surprise is the phrasing itself.
"""

from pathlib import Path

ENTRY = (
    "The lift doors opened on a stranger humming my dead "
    "grandmother's lullaby, and for one floor the whole building "
    "felt like home.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
