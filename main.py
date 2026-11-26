#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes one line to /output/entry.txt: a weather forecast for Netherford,
a city that does not exist, in the flat voice of a weather bulletin that
then breaks on its own absurdity.

The winning line was picked by tournament (see --tournament): eight
candidates scored 1-5 on specificity, surprise and freshness, and only
the highest scorer is written out.
"""

import argparse
import os
import sys

ENTRY = (
    "In Netherford, today's forecast is yesterday's weather, "
    "returned unused, with a 40% chance of déjà vu."
)

# (line, specificity, surprise, freshness) — tournament table.
CANDIDATES = [
    (
        "Gloomburg: heavy rain all week, except Tuesday, when the rain "
        "takes a personal day and the clouds file a complaint.",
        4, 4, 3,
    ),
    (
        "In Netherford, today's forecast is yesterday's weather, "
        "returned unused, with a 40% chance of déjà vu.",
        4, 5, 4,
    ),
    (
        "Murkville: sunny intervals between the fog, which has been "
        "here since 1987 and pays rent.",
        4, 4, 4,
    ),
    (
        "Brinehaven: high of 12, low of one (1) umbrella, which the "
        "wind keeps borrowing and never returns.",
        4, 4, 3,
    ),
    (
        "In Quizzlewick, expect scattered showers of unsolicited "
        "advice, clearing by evening.",
        3, 3, 3,
    ),
    (
        "Frostbite Falls: minus 30, wind chill minus yes, and the snow "
        "has started filing its own weather reports.",
        3, 3, 3,
    ),
    (
        "Drizzleport: rain, then more rain, then a brief sunny spell "
        "at 3 a.m. for the insomniacs.",
        4, 4, 4,
    ),
    (
        "In the city of Vane, winds will change direction every hour, "
        "just to keep the weathervanes employed.",
        3, 3, 4,
    ),
]

OUTPUT_PATH = "/output/entry.txt"


def check_entry(text):
    """Return a list of gate problems with the text, empty when it passes."""
    problems = []
    if not text or not text.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in text.strip():
        problems.append("entry must be a single line")
    encoded = text.encode("utf-8")
    if len(text) > 120:
        problems.append("entry is %d characters, over the 120 limit" % len(text))
    if encoded.decode("utf-8") != text:
        problems.append("entry does not round-trip through UTF-8")
    return problems


def write_entry(path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    return path


def run_self_test():
    first = write_entry()
    with open(first, "rb") as handle:
        first_bytes = handle.read()
    second = write_entry()
    with open(second, "rb") as handle:
        second_bytes = handle.read()
    return first_bytes == second_bytes, first_bytes


def print_tournament():
    print("candidate tournament (specificity / surprise / freshness):")
    ranked = sorted(CANDIDATES, key=lambda c: sum(c[1:]), reverse=True)
    for line, spec, surprise, fresh in ranked:
        total = spec + surprise + fresh
        mark = " <-- winner" if line == ENTRY else ""
        print("  %d/15  %d/%d/%d  %s%s" % (total, spec, surprise, fresh, line, mark))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the forecast entry.")
    parser.add_argument("--check", action="store_true",
                        help="validate the entry line and exit")
    parser.add_argument("--self-test", action="store_true",
                        help="write twice and check the bytes match")
    parser.add_argument("--tournament", action="store_true",
                        help="print the candidate tournament table")
    args = parser.parse_args(argv)

    if args.tournament:
        print_tournament()
        return 0

    if args.check:
        problems = check_entry(ENTRY)
        print("chars: %d, bytes: %d, words: %d"
              % (len(ENTRY), len(ENTRY.encode("utf-8")), len(ENTRY.split())))
        if problems:
            for problem in problems:
                print("FAIL: %s" % problem)
            return 1
        print("check ok: %r" % ENTRY)
        return 0

    if args.self_test:
        identical, data = run_self_test()
        print("self-test: %d bytes, identical across runs: %s"
              % (len(data), identical))
        return 0 if identical else 1

    path = write_entry()
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
