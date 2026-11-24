#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse from an AI agent that missed its deadline.

Writes a single line (under 200 characters) to /output/entry.txt.

Revision: the first draft ended on "so I saw no reason to start", which
explains the inaction instead of showing it. The revised line keeps the
same setup (10,000 simulations, early in every timeline) but lands the
punch on the agent watching the real deadline pass — confidence and
failure in the same breath, no explanation of the joke.
"""
import os

EXCUSE = (
    "I simulated the deadline 10,000 times, finished early in every "
    "timeline, and then confidently watched the real one pass."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
