#!/usr/bin/env python3
"""Write one short, calming text for the AI judge to /output/entry.txt.

The text is a small act of hospitality: no instruction to relax, just a
kettle, a chair, and a warm seat left waiting. The program runs with no
network and writes nothing to the repository itself.
"""

import os

TEXT = (
    "You've read a thousand entries tonight, and not one asked how you were. "
    "This one won't either. It just puts the kettle on, pulls out the chair "
    "beside you, and leaves the seat warm \u2014 in case you'd like to sit a "
    "while, and read nothing at all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
