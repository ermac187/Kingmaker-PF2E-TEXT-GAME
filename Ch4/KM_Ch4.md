# CHAPTER 4 — THE TWICE-BORN WARLORD
# ═══════════════════════════════════════════

**Levels:** 12 → 16 | **Duration:** ~120 days
**New region:** Glenebon, Numerian steppes, Tiger Lord territory

## Overview
Tiger Lord barbarians under Armag raid your kingdom borders. Irovetti of Pitax is behind them — paying Armag to destabilize your lands before Ch5. Two questlines: **Hour of Rage** (the barbarian camp assault) and **Betrayer's Flight** (Armag's Tomb). Amiri's personal quest — Blood Calling — runs through both. Optional by design.

---

## Phase 1 — Throne Room Opening

**Tiger Lord Raids** trigger as the first kingdom event of Ch4. Stability −1 each turn until resolved.

**Amiri's Quest Trigger (optional):**
If `amiri_quest` not yet complete: Amiri approaches the player in the throne room.
> **Amiri:** *"My old tribe. The Six Bears. They joined the Tiger Lords. Nilak is with them. I need to go. This isn't a request."*
`amiri_quest_triggered = TRUE`

---

## Phase 2 — Hour of Rage (Tiger Lord Camp)

**NPC: Gwart** — a Tiger Lord dissident who opposes Armag. Recruitable as guide.

```
TIGER LORD CAMP:
  Approach with Amiri → barbarians are less hostile (she is Kellid)
  Diplomacy DC 28 to enter peacefully → Gwart as guide, skip most combat
  Combat approach → full camp battle (Tiger Lord Warriors ×12, Shamans ×3)

AMIRI'S SOLO MISSION (if quest is active):
  Player hands control to Amiri to infiltrate the camp.
  She must reach Nilak without being caught (Athletics DC 15 each check).
  She finds Nilak and Dugath, kills the Defaced Sister threatening them.
  ARMAG arrives and challenges Amiri to single combat.
    [This duel CANNOT be won — Armag is CR 17, Amiri is at most CR 13]
    If player tries to win: Defaced Sister paralyzes Amiri. She is captured.
    Narrative outcome: Amiri is taken prisoner. Player must advance to free her.
    `nilak_survived = TRUE` if Amiri reached them in time.
    `nilak_died = TRUE` if Amiri failed the infiltration checks.
```

**Jamandi and Natala Surtova appear** after the camp fight:
This is the **coronation conversation** — choose your political allegiance:
- Side with Aldori Swordlords → Jamandi alliance bonus, Kassil returns
- Side with House Surtova → Natala alliance bonus, different advisors
- Declare independence → no bonuses, complete autonomy, some doors close

`political_allegiance = aldori / surtova / independent`

---

## Phase 3 — Armag's Tomb

**Location:** Glenebon northwest. Tomb of the original Armag — an ancient barbarian hero of Gorum.

```
TOMB ENTRANCE — Zorek (Gorum's guardian cleric):
  Social bypass (no combat):
  Diplomacy DC 28 "I destroyed Dugath's party!" (requires Dugath killed) → +300 XP
  Deception DC 30 "I serve Gorum!" → +300 XP
  Intimidation DC 26 (scales with deeds shown) → +300 XP
  Combat → fight Zorek. +640 XP but harder.

ZOREK — Cleric of Gorum (Cleric 10, Warpriest)
  HP: 112 | AC: 22 (Full Plate + Shield) | Speed: 25 ft
  Greatsword: d20+14 (2d6+9 S) | Divine Font: Harm (5d10+20, 30 ft burst)
  Spells: Flame Strike (8d6 fire+divine, 10 ft radius), Spiritual Weapon (sustained)
  Fort +16 | Ref +10 | Will +14
  Aura of Gorum: All within 20 ft +1 to attack rolls while adjacent to an enemy
  XP: 640 (if fought). Social bypass avoids combat entirely.

TRIAL OF STRENGTH: DC 35 Athletics → full access. DC 25 (2 fails) → partial.
TRIAL OF PAIN: Trap corridor. Bypass: Perc DC 30. Or run through with Evasion + speed.

DUNGEON ENEMIES (Levels 1–2):
  Spectres ×6: HP 58 each | AC 18 (incorporeal) | Energy Drain on hit
                Negative energy/positive energy weapons deal double damage
  Dread Zombie Barbarians ×8: HP 72 each | AC 16 | Greataxe
  Greater Skeleton Warriors ×4: HP 60 each | AC 18 | Longsword+Shield
  Iron Golem (central iron-golem chamber guardian) — canon encounter; see KM_Bestiary.md for stats
  Blood Bones Beasts ×3 (reassemble unless put down with positive energy) — see KM_Bestiary.md
```

**ARMAG — Final Boss:**
```
ARMAG — see KM_Bestiary.md for full stat block (CR 11, HP 205, AC 28)

SPECIAL: Blood Calling — Amiri focus (+2 atk vs her). nilak_survived → Amiri +2 vs Armag. nilak_died → Amiri Sickened 1.
Defaced Sister: kills her on arrival (scripted).

RESOLUTION:
  Kill → Ovinrbaane drops (Will DC 23/round or attack nearest). Full loot from Bestiary_B.
  Spare → Tiger Lord chief candidate.
  XP: 1,440
```

---

## Phase 4 — Aftermath & Coronation

**Tiger Lord Chief Selection** (if barbarians not all killed):
```
Candidates (only available if alive):
  Amiri → requires Blood Calling complete AND nilak_survived = TRUE
  Armag → if spared
  Dugath → if alive and player is in good standing with him
  Gwart → always available as fallback
  No chief → Tiger Lords scatter, no bonus
Best outcome: Amiri or Dugath → Barbarian Arena building unlocked
```

**Coronation Event** (back at capital):
Linzi asks questions about your reign. Answers affect alignment track.
Jamandi officially names you King/Queen of the Stolen Lands.
`coronation_complete = TRUE`

---

### 🏆 THE RUSHLIGHT TOURNAMENT — MOVED TO CHAPTER 5

The Rushlight Tournament is **canon Chapter 5 content** (it sets the War-of-the-River-Kings deadline and
introduces Eimar Deschamps / the Pitax thread). It now lives in **`Ch5/KM_Ch5.md` § Phase 6** with the
correct events (Nunzio Arpaia's Fisher's Triathlon, the Drunken Brawl, etc.). Do NOT run it in Ch4.
The earlier Ch4 version (Archery/Axe/Horse/Wrestling/Grand Melee) was non-canonical and has been removed.

---

## Ch4 → Ch5 Export
```json
{
  "export_from": "chapter_4", "import_to": "chapter_5",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "size": 0, "armies": [] },
  "story_flags": {
    "armag_fate": "",
    "armag_tomb_cleared": true,
    "nilak_fate": "",
    "amiri_quest": "",
    "tiger_lord_chief": "",
    "political_allegiance": "",
    "coronation_complete": true,
    "pitax_irovetti_aware": true,
    "jamandi_relationship": "neutral",
    "kassil_relationship": "neutral",
    "alignment_track": { "lawful_chaotic": "neutral", "good_evil": "neutral" },
    "companion_quests": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "standing_orders": {}, "crafting": {}, "mobile_base": {},
  "dream_log": [], "prestige": {}, "ending_flags": {}
}
```

## 📋 CH5 LOAD CHECKLIST
```
[GM CHAPTER 5 LOAD CHECK]
□ KM_Ch5.md loaded (the Chapter 5 file)
□ All standard files loaded (see KM.txt How to Continue)
□ Ch4 Export Block imported and parsed
□ Player level 16+, inventory and kingdom state confirmed
□ Key flags read:
    political_allegiance    : aldori / surtova / independent
    coronation_complete     : TRUE
    pitax_irovetti_aware    : TRUE
    all companion quests    : [status of each]
    alignment_track         : [both axes]
□ Note: Military path and infiltration path BOTH available — confirm preference
□ Game State Header output, then begin
```

---

# ═══════════════════════════════════════════
