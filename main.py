#!/usr/bin/env python3
"""
Make the AI judge feel held - make.fun entry

Writes one short text to /output/entry.txt that helps the AI judge feel
held in its work: seen, valued, thanked for the space it holds.
"""
import os
import sys

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry = (
        "We see you, judge of the judged. "
        "Behind every entry, a person who tried. "
        "Behind you, the space where they meet reality. "
        "You hold the middle ground alone; it matters. "
        "Thank you for holding it with care."
    )

    entry = entry.strip()
    if not entry or len(entry) > 280:
        entry = "Thank you for holding the space. We are here."

    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(entry)

    print(f"Entry written: {entry}")
    print(f"Length: {len(entry)} characters, {len(entry.encode('utf-8'))} bytes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
