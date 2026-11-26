#!/usr/bin/env python3
"""Everyday Things, Two Lines — a toaster explained to a 10-year-old.

Writes exactly two lines to /output/entry.txt:
  Line 1: one vivid sentence explaining a toaster through an analogy.
  Line 2: one sentence saying what the analogy maps and what it leaves out.
Pure standard library only; output is fixed and deterministic.
"""

import os

LINE_1 = (
    "A toaster is a little sun trapped in a metal box, browning your bread "
    "the way a summer afternoon browns your shoulders."
)
LINE_2 = (
    "It maps the heat that turns pale bread golden, but it leaves out "
    "that the real sun has no pop-up timer, never burns only one side, "
    "and cannot sit on a kitchen counter."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
