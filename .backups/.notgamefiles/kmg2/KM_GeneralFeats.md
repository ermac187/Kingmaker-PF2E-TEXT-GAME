# KINGMAKER — GENERAL FEATS L1 CATALOG (PF2e Remaster)
## KM_GeneralFeats.md | Used whenever a general feat slot must be filled

> **⛔ DM: When ANY source grants the player "a general feat of your choice
> you qualify for" (Versatile Human, Skilled Heritage's general-feat option,
> Ancestral Paragon, Natural Ambition's general option, Canny Acumen retake,
> level-up general slots at L3/7/11/15/19), you MUST:**
>
> 1. Read this file
> 2. Filter the catalog by the player's current stats / proficiencies / feats
> 3. Output a numbered list of feats the player qualifies for, with each
>    feat's effect summarized in one line
> 4. Mark feats with `(prereq met: X)` or strike non-qualifying ones
> 5. Include `[N] CUSTOM` as the final option for any general feat (including
>    skill feats) not on this short-list
>
> Never just say "name any general feat you qualify for" without showing the
> filtered list first. That prompt = `.fail 22` (skill check / choice offered
> without the player having visible options).

---

## CORE GENERAL FEATS (no skill training required)

| # | Feat | Prereq | Effect |
|---|------|--------|--------|
| 1 | Adopted Ancestry | None | Pick one ancestry; you can take its ancestry feats. Useful for thematic multi-ancestry party builds. |
| 2 | Armor Proficiency | None | Gain trained in next armor tier (light → medium → heavy). MUST be class with martial chassis to be worth it; full casters skip. |
| 3 | Breath Control | None | +1 status to saves vs inhaled, hold breath 25× longer. Niche but free. |
| 4 | Canny Acumen | None | Become expert in one of: Fortitude / Reflex / Will / Perception. Bumps to master at L17. **Always strong** — pick your weakest save. |
| 5 | Diehard | None | Die at dying 5 instead of dying 4. One extra round of life at 0 HP. **Mandatory for melee tanks.** |
| 6 | Fast Recovery | CON 14 | Recover 2× HP from rest, +2 vs ongoing disease/poison. Great for high-CON frontliners. |
| 7 | Feather Step | DEX 14 | Step into difficult terrain. **Mandatory for any DEX class** that fights in dungeons. |
| 8 | Fleet | None | Speed +5 ft permanently. Stacks with everything. **Always strong.** |
| 9 | Incredible Initiative | None | +2 circumstance bonus to initiative rolls. **Top-tier** — going first wins fights. |
| 10 | Ride | None | Mount obeys 1-action commands instead of 2-action. Required for cavalier-style builds. |
| 11 | Shield Block | None | Gain the Shield Block reaction. **Mandatory for any character carrying a shield** (most classes don't get it free until L1 if at all — Fighter/Champion already have it). |
| 12 | Toughness | None | +HP equal to your level, recovery DC −3. **Top-tier durability** — picks every level it stays valid. |
| 13 | Untrained Improvisation | None | +Level/2 to untrained skill checks. Useful for INT-low characters who want to attempt anything. |
| 14 | Weapon Proficiency | None | Gain trained in simple OR martial weapon group. Casters who want a real weapon. |

---

## ADVANCED GENERAL FEATS (require prior feat or proficiency)

| # | Feat | Prereq | Effect |
|---|------|--------|--------|
| 15 | Ancestral Paragon | Lvl 3, ≥1 ancestry feat | Gain another 1st-level ancestry feat. Good if you missed a key ancestry feat at L1/5/9. |
| 16 | Expeditious Search | Master Perception | Search at 2× / 4× speed. L7+ pick. |
| 17 | Incredible Investiture | Lvl 11, CHA 16 | Wear/benefit from 12 invested items instead of 10. Magic-item builds only. |

---

## SKILL FEATS (also count as general feats — show only if matching skill is trained)

Show these ONLY if the player is trained (or higher) in the listed skill.
This list is partial — for any skill feat not below, accept via `[N] CUSTOM`
and verify the prerequisite from the PF2e Remaster skill-feat list.

| # | Feat | Skill Prereq | Effect |
|---|------|--------------|--------|
| S1 | Assurance | Trained in any skill | Take 10 + proficiency on that skill instead of rolling. **Top-tier** — picks the skill at character creation, scales for life. |
| S2 | Cat Fall | Trained Acrobatics | Treat falls as 10/25/50 ft shorter (trained/expert/master). |
| S3 | Quick Jump | Trained Athletics | High Jump / Long Jump as 1 action instead of 2. |
| S4 | Battle Medicine | Trained Medicine | Treat Wounds as 1 action in combat, once per target per day. **Top-tier party-utility.** |
| S5 | Pickpocket | Trained Thievery | Steal from creatures actively watching, no penalty. |
| S6 | Group Coercion | Trained Intimidation | Demoralize multiple targets at once. Scales by proficiency. |
| S7 | Hobnobber | Trained Diplomacy | Gather Information at 2× speed; on success can never crit-fail. |
| S8 | Recognize Spell | Trained in any of Arcana/Nature/Occultism/Religion | ID a spell as it's cast (reaction). Mandatory anti-caster pick. |
| S9 | Trick Magic Item | Trained in any spell tradition skill | Activate a magic item not on your spell list. |
| S10 | Terrain Expertise | Trained Survival | +1 circumstance to Survival in chosen terrain. |

---

## ⛔ DM PROMPT FORMAT

When granting a general feat slot, output VERBATIM:

```
════════════════════════════════════════════════════════════
GENERAL FEAT — [Source: Versatile Human / Natural Ambition / Lvl 3 slot]

You qualify for the following (filtered by your stats: STR [X] DEX [X]
CON [X] INT [X] WIS [X] CHA [X], trained in [skill list]):

Top-tier picks for [your build type — caster / melee / hybrid]:
  [1] [Feat] — [one-line effect]
  [2] [Feat] — [one-line effect]
  [3] [Feat] — [one-line effect]

Other valid options:
  [4] [Feat] — [one-line effect]
  [5] [Feat] — [one-line effect]
  ...

  [N] CUSTOM — name any other general feat (including skill feats not
              listed). DM will verify prerequisite.

Type a number or feat name.
════════════════════════════════════════════════════════════
```

Filter rules:
- DEX < 14 → omit Feather Step
- CON < 14 → omit Fast Recovery
- Already heavy-armor proficient → omit Armor Proficiency
- Already has Shield Block class feature → omit Shield Block
- Skill feats: include only those matching player's trained skills
- Highlight 2–3 "top-tier picks" relevant to the build (e.g. caster builds:
  Canny Acumen, Toughness, Recognize Spell; melee tanks: Diehard, Toughness,
  Shield Block; DEX skirmishers: Feather Step, Fleet, Incredible Initiative)

---

*KM_GeneralFeats.md — Kingmaker PF2e | General Feat Catalog v1.0*
