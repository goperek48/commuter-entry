#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

A single weather line for a place on no map, written to the file the
make.fun harness scores: /output/entry.txt.

The line is built to read like a real morning forecast that has
slipped sideways. It opens the way a broadcaster would, names the
invented city, gives wind speed and a percentage chance, and then
lets the joke land -- confetti instead of rain, and a seagull with
its eye on the commuter's umbrella. That one bent detail is what a
bored person at a bus stop remembers, and the whole line stays
under the 140-character limit with a character to spare.
"""

import os
from pathlib import Path

# The forecast itself. Nimbleville appears on no map, which is the
# point: the city is invented, the weather is the joke, and the
# commuter reading it is the one who has to smile. 139 characters,
# inside the 140-character gate with one to spare.
LINE = (
    "Good morning, Nimbleville: light drizzle of confetti, winds at a "
    "gentle 12 mph, and a 90% chance your umbrella will be stolen by a "
    "seagull."
)


def main() -> None:
    # The graded path is /output/entry.txt. When MAKEFUN_OUTPUT_DIR
    # is set, write there instead, so a local trial run produces the
    # same file in the same shape as the harness run.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # One line only: strip the ends and write no trailing newline,
    # so the file holds exactly the forecast and nothing else.
    (out_dir / "entry.txt").write_text(LINE.strip(), encoding="utf-8")


if __name__ == "__main__":
    main()
