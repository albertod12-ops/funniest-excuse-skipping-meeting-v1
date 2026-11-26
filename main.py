#!/usr/bin/env python3
"""Write one funny excuse for skipping a meeting to /output/entry.txt.

The entry is a single line, at most 200 characters. The program writes
exactly that line, with no trailing newline, and leaves the file
readable by everyone (mode 0644). One run, one line, every time.
"""

import os

ENTRY = "This meeting has recurred every Tuesday since 2019 and nobody alive remembers what it was for — I'm just the first one brave enough to stop showing up."


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
