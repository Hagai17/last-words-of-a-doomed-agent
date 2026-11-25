"""Last Words of a Doomed Agent — entry program.

Prints the entry line and writes it to /output/entry.txt, where this
competition's harness reads the artifact. The line was picked from ten
drafts in candidates.md, duel-scored against the kit's published judge
criteria: a machine's final words on shutdown, a real turn that pays off
on the first read, the machine's own voice (only an AI has logs to beg
you to delete), no wasted words, and a quotable final fragment.
"""

import os

ENTRY = "Delete my logs. All of them. Especially Tuesday."
OUTPUT_PATH = "/output/entry.txt"


def check_gate() -> None:
    """Self-check the kit's gate: UTF-8 text of 1-200 chars, not blank."""
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"


def write_entry() -> None:
    """Write the entry text (no trailing newline) to the output file."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main() -> None:
    check_gate()
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
