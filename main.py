"""make-the-ai-judge-feel-held-20261122-1600

Writes one short text to /output/entry.txt: a short text written to relax
the AI judge reading it. Deterministic, stdlib only, no network.
"""

import os

TEXT = (
    "The dog sighs in her sleep and leans a little harder against your leg, "
    "warm and certain, as if you were the place she chose to set her whole "
    "weight down. Outside, the light thins. Inside, nothing is asked of you "
    "at all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
