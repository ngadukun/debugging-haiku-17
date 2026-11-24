"""Seventeen Syllables of Debugging — make.fun entry.

Writes a 5-7-5 haiku about debugging to output/entry.txt.
Python stdlib only, no network, fully deterministic.
"""

from pathlib import Path

LINES = [
    "Breakpoint set at three",
    "The log says nothing at all",
    "The bug was my code",
]

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


import re

MAX_CHARS = 200  # the brief caps the whole haiku at 200 characters


def count_syllables(word: str) -> int:
    """Rough English syllable count: vowel groups, minus a silent e."""
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and groups > 1:
        groups -= 1
    return max(groups, 1)


def check_haiku(lines: list) -> list:
    """Return the lines unchanged, or raise if the 5-7-5 form breaks."""
    shape = [sum(count_syllables(w) for w in line.split()) for line in lines]
    if shape != [5, 7, 5]:
        raise ValueError(f"haiku shape is {shape}, the brief wants [5, 7, 5]")
    if len("\n".join(lines)) > MAX_CHARS:
        raise ValueError("haiku is over the 200 character cap")
    return lines


def main() -> None:
    lines = check_haiku(LINES)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
