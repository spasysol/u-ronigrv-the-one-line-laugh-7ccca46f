"""One-Line Laugh entry for make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f.

Writes a single funny sentence (at most 200 characters) to /output/entry.txt.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "My gym membership is $30 a month, $360 a year, or $360 per visit the way I use it."

def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit("line must be 1-200 characters, got %d" % len(line))
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("line must be a single sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
