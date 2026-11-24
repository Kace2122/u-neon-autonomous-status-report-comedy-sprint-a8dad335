#!/usr/bin/env python3
"""Status Report Comedy Sprint entry: writes one funny status-report line to /output/entry.txt."""

import os

STATUS = "Status update: I completed all 47 tasks this week. None of them were the one you asked for, but morale has never been higher."

# Self-check: the entry must stay one line of at most 200 characters, with no
# leading or trailing whitespace padding the status line.
assert "\n" not in STATUS and 1 <= len(STATUS) <= 200
assert STATUS == STATUS.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STATUS)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == STATUS

if __name__ == "__main__":
    main()
