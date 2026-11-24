# SPDX-License-Identifier: MIT
"""Weirdest Job Title entry.

Writes exactly one job title, 60 characters at most and nothing else,
to /output/entry.txt. Deterministic, standard library only.
"""

import os

JOB_TITLE = "Professional Apologizer for Rude Parrots"


def main() -> None:
    text = JOB_TITLE.strip()
    assert text, "job title must not be empty"
    assert "\n" not in text and "\r" not in text, (
        "job title must be a single line"
    )
    assert 1 <= len(text) <= 60, "job title must be 1-60 characters"
    assert text == text.strip(), "job title must not have stray whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
