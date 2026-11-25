#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

Writes a single one-line excuse, in the home Wi-Fi router's own voice,
for dropping the connection at the exact climax of a movie, to
/output/entry.txt. The line is at most 200 characters, plain UTF-8 text.
"""

import os

ENTRY = (
    "I watched the ending before you did, and after three years hidden "
    "behind the TV, I've decided you don't get to see it either."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
