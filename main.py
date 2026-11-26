"""The Self-Checkout Is Judging You — entry program.

Writes one judgmental one-line remark, in the voice of a smug
self-checkout machine, to /output/entry.txt.

Gate (RULES.txt): the file must be UTF-8 text of 1 to 200 characters,
not only white space. The remark below is checked against that gate
in main() before anything is written, so an invalid remark can never
reach the output file.

Stdlib only. No network, no clock, no file reads.
Run: python3 -P -s main.py
"""

import argparse
import sys
from pathlib import Path

DEFAULT_OUT = Path("/output/entry.txt")
MAX_CHARS = 200

REMARK = (
    "Twelve yogurts, no spoon, bagged like a crime scene. "
    "Your meal plan has been noted, filed, and quietly pitied."
)


def validate_remark(text):
    """Check one remark against the gate; raise ValueError if it fails.

    Rules enforced (all from RULES.txt, plus single-line and
    control-character hygiene so the line stays one clean remark):
    - 1 to 200 characters (characters, not bytes)
    - not only white space
    - a single line, no line breaks
    - no control characters
    """
    if not isinstance(text, str):
        raise ValueError("remark must be text, got %s" % type(text).__name__)
    if len(text) < 1:
        raise ValueError("remark is empty (gate needs 1-200 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "remark is %d characters, over the 200-character gate" % len(text)
        )
    if not text.strip():
        raise ValueError("remark is only white space (gate refuses it)")
    if "\n" in text or "\r" in text:
        raise ValueError("remark must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("remark holds control characters")
    return True


def write_remark(text, out_path):
    """Validate, then write the remark exactly (no trailing newline)."""
    validate_remark(text)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return out_path


def build_parser():
    parser = argparse.ArgumentParser(
        description="Write the self-checkout remark to entry.txt."
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="output path (default: /output/entry.txt)",
    )
    return parser


def main(argv=None):
    """Validate the remark, then write it. Exit 2 if it fails the gate."""
    args = build_parser().parse_args(argv)
    try:
        validate_remark(REMARK)
    except ValueError as exc:
        print("error: refusing to write an invalid remark: %s" % exc,
              file=sys.stderr)
        return 2
    write_remark(REMARK, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

