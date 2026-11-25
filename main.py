"""One Line, One Chill (u-azazex-one-line-one-chill-6d4d5488).

Writes a single horror sentence to /output/entry.txt. The angle is a calm,
unbothered narrator striking a house-share deal with the thing in the attic:
the chill is how relaxed the speaker stays while the dread quietly builds,
and the last word lands the scare.
"""

from pathlib import Path

LINE = "I told the thing in the attic it could stay if it kept quiet, and it has — except on nights when I hear it practicing my laugh."

TARGET = Path("/output/entry.txt")
LIMIT = 200


def run() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= LIMIT:
        raise SystemExit(f"entry must be 1-{LIMIT} chars, got {len(text)}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")


run()
