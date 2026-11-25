#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke line.

The grader runs this in a sandbox with no network. It writes exactly one
line (at most 200 characters) to /output/entry.txt.
"""

import os

LINE = "I put 'per my last email' in my will so my family knows I already answered this question twice."


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
