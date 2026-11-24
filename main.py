"""Everyday Wonder, Two Days to Find the Line: writes the entry text to /output/entry.txt.

Why this line: a concrete everyday sight (a shadow on wet pavement) given a
strange, unread angle — the shadow knows where you are going before you do —
with the surprise landing in a single read.
"""

import os

# The entry itself: one sentence, punch at the end, no explanation.
ENTRY = 'On wet pavement my shadow walked half a step ahead of me, like it had somewhere better to be.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
