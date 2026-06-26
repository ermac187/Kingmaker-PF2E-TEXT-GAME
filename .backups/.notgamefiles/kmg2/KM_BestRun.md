# KINGMAKER — BEST RUN ARCHIVE & SCORING
## KM_BestRun.md | Referenced by: KM_ChapterSelect.md, all Export files

---

> **PURPOSE:** This file stores your personal best chapter completions. When you
> use Chapter Select to skip ahead, the DM reads YOUR best run data instead of
> generic canonical defaults. The DM AUTOMATICALLY scores every run at chapter
> end and outputs the Best Run block when you beat your record. No command needed.

---

## 🏆 RUN QUALITY SCORE — DM EVALUATES AT EVERY CHAPTER END

**⛔ MANDATORY.** At chapter export time, the DM calculates the Run Quality
Score using ALL vectors below. Show the scorecard to the player alongside
the export block. Compare against the stored best run score. If current run
scores HIGHER (or no best run exists), auto-output the Best Run block with
paste instructions.

### SCORING VECTORS

**1. HERO POINTS EARNED (max 30)**
Total Hero Points awarded this chapter (not pool — total earned including overflow).
- Each HP earned = 3 points (cap 10 HP = 30 pts)

**2. CREATIVE PLAY (max 25)**
Judgment triggers that fired (the creative HP triggers, not automatic ones).
- Each judgment trigger = 5 points (cap 5 = 25 pts)
- Callback, tactical sacrifice, enemy turned, perfect info play, humor, improvised weapon, environment kill, talk-down, out-thought — all count

**3. DIFFICULTY CHOICES (max 30)**
Harder paths chosen when easier ones were available.
- Entered without using letter/invitation when you had one: +5
- Resolved a combat encounter through pure social/logic (no weapons): +5
- Chose unarmed or non-lethal approach when armed was easier: +5
- Protected civilians or NPCs at personal cost (took damage, lost resources): +5
- Refused a bribe, shortcut, or exploit that would have helped: +5
- Took a solo encounter without calling for companion help: +5

**4. CIVILIAN REPUTATION (max 20)**
How the common people see eRmaC at chapter end.
- `public_reputation` score mapped:
  - 0-10: 0 pts | 11-25: 5 pts | 26-50: 10 pts | 51-75: 15 pts | 76+: 20 pts
- If no reputation score tracked yet (Prologue): use crowd reactions
  - Crowd feared you: 0 pts | Crowd neutral: 5 pts
  - Crowd respected you: 15 pts | Crowd cheered/admired: 20 pts

**5. COMPANION RELATIONSHIPS (max 25)**
Average opinion score across all active companions at chapter end.
- Average +1 to +5 (FAVORABLE): 5 pts
- Average +6 to +10 (WARM): 10 pts
- Average +11 to +15 (FRIENDLY): 15 pts
- Average +16 to +20 (DEVOTED): 25 pts
- BONUS: Any single companion at DEVOTED (+16): +5 pts (stacks, cap +10)

**6. KEY NPC RELATIONSHIPS (max 20)**
Important story NPCs — not companions, the world's power players.
- Jamandi at DEVOTED: +8 | FRIENDLY: +5 | WARM: +3
- Kesten at WARM+: +3
- Kassil at WARM+: +3
- Each other story NPC at FRIENDLY+: +2 (cap +6 total)

**7. COMPLETENESS (max 20)**
Content engaged, secrets found, optional paths taken.
- Each completed quest: +2 (cap +10)
- Each secret/hidden content found: +3 (secret room, hidden NPC, lore discovery)
- Each optional scene engaged (not skipped): +1 (cap +5)

**8. LEGACY QUALITY (max 10)**
How many player_legacy entries were created this chapter.
- 1-2 entries: 3 pts | 3-4 entries: 6 pts | 5+: 10 pts
- DM judges whether entries are genuinely memorable (not just "fought a guy")

**9. TITLE SYSTEM (max 10)**
Titles granted this chapter.
- Each Suffix granted: +3
- Each Prefix granted: +5
- Title refund earned (+5 reaction): +2

**10. STYLE BONUS (max 10, DM judgment)**
The intangible. Did the player bring something special?
- Consistent character voice throughout: +3
- A single moment the DM would remember telling someone about: +4
- Made an NPC break from their script through sheer force of personality: +3

---

### TOTAL: 200 POINTS MAXIMUM PER CHAPTER

```
RUN QUALITY SCORECARD
═══════════════════════════════
Hero Points Earned:    __/30
Creative Play:         __/25
Difficulty Choices:     __/30
Civilian Reputation:   __/20
Companion Relations:   __/25
Key NPC Relations:     __/20
Completeness:          __/20
Legacy Quality:        __/10
Title System:          __/10
Style Bonus:           __/10
───────────────────────────────
TOTAL:                 __/200
Previous Best:         __/200
NEW RECORD?            YES / NO
═══════════════════════════════
```

---

## ⛔ DM INSTRUCTION — AUTO-EVALUATION AT CHAPTER END

**This fires AUTOMATICALLY at every chapter export. No player command needed.**

1. **Calculate the score** using all 10 vectors above.
2. **Compare against stored best:** Read this file's matching chapter section.
   - If `"_empty": true` → no previous best exists. Current run IS the best.
   - If a `"_score"` exists → compare. Current must be STRICTLY HIGHER to win.
   - Ties do NOT replace. The stored best stands on a tie.
3. **If NEW RECORD (current > stored, or no stored):**
   - Display the FULL scorecard (all 10 vectors with breakdown)
   - Output: *"🏆 NEW BEST RUN — [chapter]. Score: [X]/200 (previous: [Y]/200)."*
   - Output the Best Run data block with:
     *"Copy the block below and paste it into the `[CHAPTER] BEST RUN` section
     of `KM_BestRun.md`, replacing the old data."*
4. **If NOT a new record (current ≤ stored):**
   - Display ONE line only: *"Run score: [X]/200. Your best: [Y]/200."*
   - Do NOT output a Best Run block. Do NOT show the full scorecard.
   - The old best stands. No action needed from the player.

---

## ⛔ DM INSTRUCTION — READING BEST RUN DATA (at Chapter Select)

**At Chapter Select time:** For each chapter being skipped, check if a Best Run
block exists here. If it does (no `"_empty": true`): use that data INSTEAD of
canonical defaults from KM_ChapterSelect.md. If empty: fall back to canonical.

**Merge rule:** Best Run data is authoritative for everything it contains.
Canonical defaults fill ONLY gaps.

**Player — SAME BUILD:** Use Best Run's EXACT level, XP, HP, gear, gold, all stats.
**Player — DIFFERENT BUILD:** Use Best Run's LEVEL and XP. Recalculate HP/feats/skills from new build at that level. Gear gets equivalent-tier substitution.

**Companions — RETURNING (in both old and new Pick-10):** Use their Best Run level, build, gear, and relationship data exactly.
**Companions — NEW (in new Pick-10 but NOT in Best Run):** Level up to match the player's Best Run level. Assign ★ recommended build. Generate tier-appropriate gear. Relationship starts at +3 (no history). They then choose their build at Step 4 like normal — ★ is just the starting point if the player picks `★ AUTO`.

---

## ⛔ DM INSTRUCTION — BEST RUN BLOCK FORMAT

Save the FULL chapter export block. Keep EVERYTHING — stats AND story:

```
KEEP ALL:
  PLAYER: level, xp, hp_max, hp_current (set to max on load), ac, saves,
          skills (ranks + mods), feats, spells, attributes, build_id,
          inventory (full items with stats + runes), gold, speed,
          perception, initiative_mod, conditions (cleared on load)
  COMPANIONS: full companion blocks — level, hp, builds, gear, feats,
              spell slots (ALL companions, not just active party)
  STORY: story_flags, npc_threads (thread + priorities + memory),
         npc_relations (score + trend + attraction),
         player_legacy (moment + witnessed_by), quest_log,
         promises_and_dialogue, companion_titles, dispositions,
         alignment_track, world_state, companion_picks + builds
  SYSTEMS: dream_log, debate_results, kingdom state (Ch2+),
           scripted_interactions_completed, crafting recipes known

ADD:  "_best_run": "[chapter]"
      "_score": [total]
      "_score_breakdown": { vector scores }
      "_saved_date": "[date]"
      "_run_summary": "[1-2 sentence DM summary of what made this run special]"
```

**On load from Best Run:** HP restored to max. Spell slots restored to full.
Conditions cleared. This is a fresh start at the chapter — not mid-combat.

---

## 📋 PRE-PROLOGUE BEST RUN

```json
{
  "_best_run": "pre-prologue",
  "_empty": true
}
```

---

## 📋 PROLOGUE BEST RUN

```json
{
  "_best_run": "prologue",
  "_score": 163,
  "_score_breakdown": {
    "hero_points": 30,
    "creative_play": 25,
    "difficulty_choices": 30,
    "civilian_reputation": 20,
    "companion_relations": 5,
    "key_npc_relations": 13,
    "completeness": 20,
    "legacy_quality": 10,
    "title_system": 10,
    "style_bonus": 10
  },
  "_saved_date": "Session — Prologue Complete",
  "_run_summary": "Entered unarmed. Never drew a weapon. Bread roll preceding garotte. Lady Sleeps invented under pressure. Talk-down via the opponent's own argument. All 11 titled. Operation Leech live before the carriage was ordered."
}
```

---

## 📋 CHAPTER 1 BEST RUN

```json
{
  "_best_run": "chapter_1",
  "_empty": true
}
```

---

## 📋 CHAPTER 2 BEST RUN

```json
{
  "_best_run": "chapter_2",
  "_empty": true
}
```

---

## 📋 CHAPTER 3 BEST RUN

```json
{
  "_best_run": "chapter_3",
  "_empty": true
}
```

---

## 📋 CHAPTER 4 BEST RUN

```json
{
  "_best_run": "chapter_4",
  "_empty": true
}
```

---

## 📋 CHAPTER 5 BEST RUN

```json
{
  "_best_run": "chapter_5",
  "_empty": true
}
```

---

## 📋 CHAPTER 6 BEST RUN

```json
{
  "_best_run": "chapter_6",
  "_empty": true
}
```
