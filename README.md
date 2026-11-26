# The Self-Checkout Is Judging You

[![make.fun](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/hurulsufi12-art/self-checkout-judging-you/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/hurulsufi12-art/self-checkout-judging-you/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

One funny line in the voice of a smug, judgmental self-checkout machine —
an entry for the [make.fun bounty](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6).

## The entry

> Twelve yogurts, no spoon, bagged like a crime scene. Your meal plan has been noted, filed, and quietly pitied.

110 characters, one line, ASCII. Petty about the basket (twelve yogurts,
no spoon) and about how it was bagged (like a crime scene) — the machine
files the shopper's meal plan away and pities it, quietly.

## Run

```sh
python3 -P -s main.py
```

Writes the line to `/output/entry.txt` (no trailing newline). Python 3
standard library only — no network, no clock, no file reads.

## Gate

`/output/entry.txt` must be UTF-8 text of 1 to 200 characters, not only
white space. `main.py` checks the line against that gate before writing
anything; an invalid line exits non-zero and writes no file.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
