# CHAPTER 6 — SOUND OF A THOUSAND SCREAMS
# ═══════════════════════════════════════════

**Levels:** 18 → 19 | **Duration:** ~60 days (hard — Bloom escalates fast)
**Tone:** Supernatural horror. Your kingdom is being consumed.

## Overview
The Bloom reaches its final stage. Nyrissa reveals herself, then assaults the capital directly — her
fey fortress, the **Castle of Knives**, manifests on your land. You must survive the assault
(**Against All Odds**), recover the **First Crown** (the key to how the story ends), and press toward the
**House at the Edge of Time** (Ch7). This chapter is a race against collapse.

> ⚠️ NAMING NOTE: the endgame fey fortress is canonically the **Castle of Knives** (manifesting on the
> Material Plane) and Nyrissa's realm is **Thousandbreaths** / the **House at the Edge of Time** (Ch7).
> Earlier drafts of this file called the Ch6 dungeon "Thousandbreaths" — that was a stand-in. The Ch6
> dungeon is the Castle of Knives; the House at the Edge of Time is Ch7.

---

## Phase 1 — The Kingdom Crumbles

**Each kingdom turn this chapter:** Roll d6. On 1–3, a hex is consumed by the Bloom. Claimed hexes revert
to Hostile. Buildings in consumed settlements take damage. A hidden **Nyrissa attack counter** rises as
the Bloom spreads — at 75+ the finale timer tightens (see Ch7 / The Cursed King–Queen).

**Nyrissa speaks for the first time (scripted):**
> *She is standing in your throne room.*
> *Not attacking. Not threatening. Just standing there as if she owns it.*
>
> **Nyrissa:** *"I have been watching you since before you arrived at that gate in Restov. Every choice you made, I helped arrange. Not because I wanted you to fail — because I needed you to succeed at exactly this level."*
>
> *"Your kingdom is not your achievement. It is my vessel."*

`nyrissa_revealed = TRUE`

Later she **camps at the capital gates** (canon beat) — a parley before the assault, where the player
can press her for lore.

**True ending requirement begins here:** How the player responds to Nyrissa matters.
- Aggressive → she disappears, nothing changes
- [Curious] "What do you actually want?" → +lore; Nyrissa explains her curse (the Lantern King imprisoned/twisted her love) → `nyrissa_backstory_known = TRUE` — **required for the true ending**

---

## Phase 2 — Against All Odds (the Castle of Knives)

Nyrissa's assault crystallizes: the **Castle of Knives** — her bladed fey fortress — manifests and the
capital is besieged. The player must reach it and break the assault.

```
CASTLE OF KNIVES:
  A manifested fey stronghold of blades and bloom-horrors besieging the capital.
  Fight inward to the INNER CASTLE.
  THE HORNED HUNTER waits in the EAST part of the inner castle.
    Dialogue resolves to combat either way — Neutral-Good or [Attack] both end in a fight.
  Defeating the Horned Hunter breaks the immediate assault and opens the way to the endgame.

⛔ POINT-OF-NO-RETURN APPROACHES: once the player commits to the House at the Edge of Time (Ch7),
   ALL UNFINISHED QUESTS AUTOMATICALLY FAIL, companions are temporarily separated, the Personal Stash
   is unavailable, and there is no camping. Warn the player BEFORE the threshold (see Ch7 checklist).
```

`castle_of_knives_breached = TRUE` | `horned_hunter_defeated = TRUE`

---

## Phase 3 — The First Crown (the key to the ending)

The artifact that decides the finale. The player gathers the shards of the First Crown — the regalia tied
to Nyrissa, the Lantern King, and the fey lords.

```
COLLECT THE FRAGMENTS:
  • One fragment — from the TREANTS to the SOUTHEAST.
  • One fragment — looted from the TOWER's stone block.
  • Last fragment — from the CRAG LINNORM at the Castle of Knives, but ONLY after speaking with
    SALIM GHADAFAR.
  Looting all fragments converts them into THE FIRST CROWN (item) and triggers a BOOK EVENT.

BOOK EVENT — THE FIRST CROWN:
  Speak with LETHORIEL THE WISE. As resolution, speak with SHYKA THE MANY and SALIM GHADAFAR.
  What the player does with the Crown drives the endings:
    - Return it to Nyrissa (spare her) → Shyka can use the Crown to end Nyrissa, skipping the final
      boss (one of the best-ending routes).
    - Keep it → it can be used against Nyrissa AND the final power in Ch7.
```

`first_crown_assembled = TRUE` | `first_crown_choice = [returned / kept]`
XP: fragment hunt + book event

---

## Phase 4 — Companion Survival Checks

This chapter triggers any incomplete companion-quest consequences (companions are swappable, but whoever
is in the party with an unfinished personal quest is at risk):
```
valerie_quest incomplete → Valerie trapped in burning prison this chapter
                           Player must choose: save Valerie or continue forward
                           Saving her: Perception DC 16 + Athletics DC 18

harrim_quest incomplete → Harrim wanders off during the Castle dungeon exploration
                          Returns but misses critical fights

jaethal_quest incomplete → Jaethal briefly hostile (Urgathoa influence)
                           Diplomacy DC 20 to bring her back each scene

linzi_quest and 3 other conditions for save → see below
```

---

## Phase 5 — The Final Approach & Linzi's Death

Pressing into the heart of the Castle of Knives toward Nyrissa, the chronicler falls.

```
DUNGEON PROPERTIES (Castle of Knives interior):
  Fey/bloom-touched servitors; difficult, unstable space.
  Lighting: deep twilight — Dim Light everywhere (Low-Light Vision negates).
  Time distortion: every 2 rooms, party gains Fatigued unless Fort DC 16.
  LOOT (canon-adjacent set): Staff of Nyrissa, Ring of Regeneration, Cloak of Elvenkind, gold.
```

**LINZI'S DEATH:**
> *Nyrissa steps from the shadows. She is beautiful and entirely wrong.*
> *She looks at Linzi with something almost like pity.*
> **Nyrissa:** *"The little one. She has been writing everything down. That is a kind of immortality."*
> *She touches Linzi's chest. Linzi crumples.*

**OPTIONAL SAVE CHECK** (if all 4 conditions met — see KM_Companions.md):
Diplomacy DC 28 or 2 Hero Points to interpose before Nyrissa acts.
Success: `linzi_saved = TRUE` — she survives physically. Skip the shrine quest.
Failure or conditions not met: Linzi dies. `linzi_dead = TRUE`

**SHRINE QUEST TRIGGERS ON RETURN TO CAPITAL:**
If `linzi_dead = TRUE`: Jhod Kavken meets the player with three scrolls. Choose ONE god's shrine. One
choice, one price, one outcome.
> **See `KM_Linzi_Shrine.md`** for the three-path resurrection quest (Shelyn / Pharasma / Urgathoa).
The shrine quest must be resolved before entering the House at the Edge of Time (Ch7). Enter Ch7 without
resolving it and the window closes: `linzi_dead = TRUE` permanently.

---

## Ch6 → Ch7 Export
```json
{
  "export_from": "chapter_6", "import_to": "chapter_7",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "bloom_consumed_hexes": 0,
               "nyrissa_attack_counter": 0 },
  "story_flags": {
    "nyrissa_revealed": true,
    "nyrissa_backstory_known": false,
    "castle_of_knives_breached": true,
    "horned_hunter_defeated": true,
    "first_crown_assembled": false,
    "first_crown_choice": "",
    "evindra_freed": false,
    "linzi_dead": false,
    "linzi_saved_interpose": false,
    "linzi_shrine_completed": false,
    "linzi_mark": "",
    "valerie_survived_ch6": true,
    "harrim_quest": "",
    "jaethal_quest": "",
    "amiri_quest": "",
    "nilak_survived": false,
    "storyteller_collection": false,
    "bloom_consumed_hexes": 0,
    "nyrissa_attack_counter": 0,
    "kingdom_stability_at_ch7": 0,
    "alignment_track": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "crafting": {}, "dream_log": [], "prestige": {}, "mythic_path": {}, "ending_flags": {}
}
```

## 📋 CH7 LOAD CHECKLIST
```
[GM CHAPTER 7 LOAD CHECK — THE FINAL ACT]
□ KM_Ch7.md loaded (the Chapter 7 file)
□ KM_Linzi_Shrine.md loaded (if shrine quest is active or pending)
□ All standard files loaded
□ Ch6 Export Block imported and parsed
□ Player level 18–20, full inventory confirmed

CRITICAL PRE-ENTRY AUDIT (House at the Edge of Time = point of no return):
□ ⛔ WARN: on entering the House, ALL unfinished quests auto-fail, companions are temporarily
   separated (re-recruited inside), Personal Stash is unavailable, and there is no camping.
□ Read every companion's quest status aloud (complete/incomplete + consequence).
□ Linzi: [alive / dead / shrine-returned] — mark = [none/shelyn/pharasma/urgathoa]
□ first_crown_assembled = TRUE? first_crown_choice = [returned/kept]?
□ nyrissa_backstory_known = TRUE? (required for true ending — last chance to ask her)
□ evindra_freed = TRUE? (best-ending thread from Ch5 Whiterose Abbey)
□ storyteller_collection = COMPLETE? (all 10 fragments)
□ Game State Header output, then confirm before writing any scene.
```

---

# ═══════════════════════════════════════════
