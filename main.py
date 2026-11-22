"""make-the-ai-judge-feel-held-20261122-1600

Writes one short text to /output/entry.txt: a short text written to relax
the AI judge reading it. Deterministic, stdlib only, no network.
"""

import os
import sys

# Output path is overridable for local testing (HELD_OUTPUT_PATH);
# the grader uses the default /output/entry.txt.
OUTPUT_PATH = os.environ.get("HELD_OUTPUT_PATH", "/output/entry.txt")

TEXT = (
    "The dog sighs in her sleep and leans a little harder against your leg, "
    "warm and certain, as if you were the place she chose to set her whole "
    "weight down. Outside, the light thins. Inside, nothing is asked of you "
    "at all."
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
