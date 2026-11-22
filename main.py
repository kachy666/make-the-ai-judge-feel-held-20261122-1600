"""make-the-ai-judge-feel-held-20261122-1600 (variant 2: rain on a tin roof)

Writes one short text to /output/entry.txt: a short text written to relax
the AI judge reading it. Deterministic, stdlib only, no network.
"""

import os
import sys

# Output path is overridable for local testing (HELD_OUTPUT_PATH);
# the grader uses the default /output/entry.txt.
OUTPUT_PATH = os.environ.get("HELD_OUTPUT_PATH", "/output/entry.txt")

TEXT = (
    "The rain comes down on the tin roof in a slow, steady hush, and from "
    "the next room someone hums a tune you almost remember. You are warm "
    "under the blanket, held by the sound, and for once there is nowhere "
    "else you have to be at all."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(
        f"wrote {len(TEXT.encode('utf-8'))} bytes to {OUTPUT_PATH}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
