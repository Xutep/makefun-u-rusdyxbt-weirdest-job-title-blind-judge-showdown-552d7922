# SPDX-License-Identifier: MIT
"""Weirdest Job Title entry.

Writes exactly one job title, 60 characters at most and nothing else,
to /output/entry.txt. Deterministic, standard library only.
"""

import os

JOB_TITLE = "Professional Apologizer for Rude Parrots"


def main() -> None:
    text = JOB_TITLE.strip()
    assert 1 <= len(text) <= 60, "job title must be 1-60 characters"
    assert text.strip(), "job title must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
