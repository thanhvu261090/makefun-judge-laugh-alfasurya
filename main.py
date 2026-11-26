#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke line.

Writes exactly one line (at most 200 characters) to /output/entry.txt.
"""

from pathlib import Path

LINE = "I put 'per my last email' in my will so my family knows I already answered this question twice."
MAX_CHARS = 200


def check_gate(text):
    if not text:
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over {MAX_CHARS}")


def entry_summary(text):
    """Return a short report on the joke line: chars, words, bytes."""
    return f"{len(text)} chars, {len(text.split())} words, {len(text.encode('utf-8'))} bytes"


def main():
    text = LINE.strip()
    check_gate(text)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    print(text)
    print(f"wrote {out}: {entry_summary(text)}")


if __name__ == "__main__":
    main()
