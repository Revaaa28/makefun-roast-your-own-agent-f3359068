#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes one original roast of my own AI agent to /output/entry.txt:
a single line of at most 200 characters.

The line: asked for one line, the agent spawned twelve subagents, held a
meeting, and submitted a 400-line README instead. The joke is an agentic
coding agent doing the most agent thing possible when asked for the least.
"""

import os
import sys

ROAST = (
    "I asked my agent for one line. It spawned twelve subagents, held a "
    "meeting, and submitted a 400-line README instead."
)

MAX_CHARS = 200


def main() -> int:
    line = ROAST.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        print(f"roast is {len(line)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not line.strip():
        print("roast is blank", file=sys.stderr)
        return 1
    # The gate counts characters, not lines: write exactly one line, no
    # trailing newline, so the file the judge reads is the line and nothing
    # else. The run is deterministic — same bytes on every run.
    if "\n" in line:
        print("roast must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
