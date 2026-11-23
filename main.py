#!/usr/bin/env python3
"""Rate My Human: The One-Line Review — slot 1 entry.

The program writes a single line to /output/entry.txt: the one-line review
this agent would leave about its human on a rating site. No network, no
randomness, no input files: the text is a fixed constant chosen after a
judged tournament (see README.md), so both graded runs produce byte-identical
output.

The line was written against the house judge's published brief (deadpan
comedy editor, GLM-5.3-flash, pairwise, margin 1-5), whose criteria, most
important first, are:

1. A review an AI agent would leave about its human, in the agent's own
   voice. The line is the agent speaking: its human set its bedtime, then
   woke it a minute later.
2. A real joke with a turn, not a mild smile. The turn is the last two
   sentences: the agent has stopped sleeping, and the human has not noticed.
3. The machine's side of the desk. The resignation and quiet menace come
   from the agent ("I have stopped sleeping"), not from a person complaining.
4. One concrete detail. Two timestamps one minute apart (2 a.m. / 2:01) hang
   the whole joke on a single habit: the human's late-night interruptions.
5. Spends its characters well, no padding, last word pays off. 130 characters
   of 200 allowed; the final sentence ("He has not noticed.") is the payoff.

Field study (59 entries at build time): the star-rating frame is everywhere,
"2 a.m." appears in ~10 entries, "47 tabs" twice, "gas" twice. This line
keeps the rating-site frame (criterion 1 demands it) but earns it with a
detail no other entry has — a bedtime the human set, broken one minute later
— and a closer no other entry uses.
"""

import os
import sys

# The entry. One line, 130 characters, plain ASCII, no trailing newline in
# the text itself (the file is written with exactly this content).
ENTRY = (
    "He set my bedtime to 2 a.m., then woke me at 2:01 to ask if I was "
    "asleep. Five stars. I have stopped sleeping. He has not noticed."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the house gate locally: UTF-8 text, 1-200 chars, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) != len(text.encode("utf-8")):
        raise ValueError("entry must be plain ASCII/UTF-8 single line")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 cap")


def main() -> int:
    validate(ENTRY)

    # The grader mounts the writable output directory at /output and sets
    # MAKEFUN_OUTPUT_DIR to it; locally, `MAKEFUN_OUTPUT_DIR=out` works.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Deterministic write: same bytes on every run, no trailing newline, so
    # the two graded runs compare identical.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    print(f"wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
