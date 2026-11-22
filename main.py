"""Write one short text to /output/entry.txt.

Entry for the make.fun competition
make-the-ai-judge-feel-held-20261122-1600: a short text written to
relax the AI judge reading it.

Deterministic, no network, no input: the text is embedded below and
written byte-for-byte to /output/entry.txt as UTF-8.
"""

from pathlib import Path

ENTRY = (
    "My daughter fell asleep\n"
    "in my arms on the train.\n"
    "Her cheek warm\n"
    "against my chest.\n"
    "The carriage went quiet\n"
    "around us.\n"
    "I held her\n"
    "so she could sleep.\n"
    "She held me\n"
    "so I could stay."
)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    code_points = len(ENTRY)
    assert 1 <= code_points <= 280, f"entry is {code_points} code points"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
