#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes exactly one original slogan to /output/entry.txt.
Deterministic, stdlib only, no network, no model calls.
"""

import os

SLOGAN = "Your Solana wallet finally grew a brain \u2014 it watches, moves, and minds your money while you sleep."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")


if __name__ == "__main__":
    main()
