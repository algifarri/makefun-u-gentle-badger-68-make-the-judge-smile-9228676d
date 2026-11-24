#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

Writes the line to /output/entry.txt (UTF-8, 148 Unicode code points,
inside the 1-200 gate). Deterministic, standard library only, no network.

The line itself: the grey tabby next door, who has ignored me for two
years, walked in this morning, sat on my laptop, and purred like we had
been friends all along. Warmth in the sudden acceptance, surprise in the
two-year cold shoulder melting in a single morning, one concrete detail
(the laptop), told in plain words with its own rhythm.
"""

import os

TEXT = (
    "The grey tabby next door, who has ignored me for two years, walked "
    "in this morning, sat on my laptop, and purred like we had been "
    "friends all along."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # TEXT is exactly 148 Unicode code points: inside the 1-200 gate.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
