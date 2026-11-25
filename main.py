#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt: the verdict on an ex.
"""

import os

ENTRY = "Unsubscribe"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
