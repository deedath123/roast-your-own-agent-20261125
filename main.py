"""Roast Your Own Agent entry.

Writes one locked roast line to entry.txt.

Verified entry sha256: c46d86dc9b3d200fd175f0500e93ea4d8001258a455ae90dda1e29b5f8a52fc1.
"""

import os

ENTRY = "My agent entered 242 bounties, won two, and calls the other 240 'market research'."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
