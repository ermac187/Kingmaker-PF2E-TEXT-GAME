# Data Directory — the single source of truth

Everything the GM is allowed to treat as fact lives here. If a rule or stat is
not in one of these files, the GM must say "that isn't in my data" rather than
invent it (see the root `CLAUDE.md`).

**Drop your desktop data into the folders below.** File names are suggestions —
what matters is that related content is grouped and discoverable. Markdown,
JSON, or plain text all work; prefer a format where the numbers are easy to read
and cite.

```
data/
├── rules/          Core PF2E mechanics the GM cites constantly
│   ├── dcs-by-level.md        Simple/level-based DC table (the anchor for ad-hoc calls)
│   ├── degrees-of-success.md  The crit/success/fail/crit-fail ladder + nat 20 / nat 1
│   ├── conditions.md          Every condition and its exact numeric effects
│   ├── actions.md             Basic & skill actions, their action cost and DCs
│   └── skills.md              Each skill, its actions, and trained/expert gating
│
├── bestiary/       Monster & NPC stat blocks (HP, AC, saves, attacks, abilities)
│   └── <creature>.md          One file per creature, or grouped by chapter
│
├── kingmaker/      Adventure Path content
│   ├── chapters/              Story beats, encounters, maps, read-aloud text
│   ├── hexes/                 Hex-by-hex exploration content
│   └── kingdom/               Kingdom-turn rules, events, activities, DCs
│
├── characters/     Player characters (the party sheet of record)
│   └── <name>.md              Full sheet: stats, skills, feats, gear, spells
│
└── state/          Live game state — the GM reads & writes this every session
    └── save.md                Current location, HP, conditions, slots, gold, kingdom state
```

## Rules of the road for this folder

1. **One fact, one home.** A creature's AC lives in its bestiary file, not also
   restated in a chapter file where the two can drift apart.
2. **Numbers must be unambiguous.** "DC 18" not "a moderate DC". The GM cannot
   cite what isn't written down precisely.
3. **State is a file, not a memory.** `state/save.md` is the truth about the
   current game. The GM updates it as play proceeds.
4. **When you add data, you expand what the GM is allowed to know.** The GM's
   honesty depends entirely on this folder being complete — gaps become "I don't
   have that," which is the correct behavior, not a bug.

## How to get your desktop data in here

Since your data is on your PC and these sessions run in the cloud, pick whichever
is easiest:

- **Push from your PC:** clone this repo on your desktop, copy your data into
  these folders, `git add/commit/push`.
- **Paste it to me in a Claude Code session** and I'll write it into the right
  files, normalizing the format as I go.
- **Upload/attach files** and I'll place and organize them.

Tell me roughly how your data is currently structured (one big doc? many files?
a Foundry/PDF export?) and I'll match the layout to it instead of forcing yours
to match mine.
