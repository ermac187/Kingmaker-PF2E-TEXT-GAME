# Kingmaker PF2E Text Game

A text-based Pathfinder Second Edition game running the *Kingmaker* Adventure
Path, **played conversationally with an AI Game Master** (Claude / Claude Code).

## The problem this repo solves

When you run a TTRPG through an AI, the AI tends to **invent the rules** — it
recites DCs, action costs, and condition effects from fuzzy memory and gets them
wrong, confidently. ("Lying about the law.") This repo fixes that by separating
two things:

- **The rules and content are data** (`/data`) — the single source of truth.
- **The AI is only the narrator and adjudicator** — bound by `CLAUDE.md` to use
  the data and to say *"that isn't in my data"* instead of guessing.

## How to play

1. Open this repo in a **Claude Code** session (web or CLI).
2. `CLAUDE.md` loads automatically — it's the GM contract that forbids invented
   rules and requires the AI to cite the data file behind every number.
3. Tell the GM to start (or continue) the game. It reads `data/state/save.md`
   for where you left off.

## What's here

| Path | What it is |
|---|---|
| `CLAUDE.md` | The Game Master contract — the anti-hallucination rules |
| `data/` | All rules + Kingmaker content + characters + live save state |
| `data/README.md` | The data layout and how to add your content |

## Status

Scaffolding is in place. The two foundational rules tables (level-based DCs,
degrees of success) are seeded from core PF2E. **The bulk of the content —
your bestiary, Kingmaker chapters, characters, full rules — still needs to be
added from your data.** See `data/README.md` for how to get it in.
