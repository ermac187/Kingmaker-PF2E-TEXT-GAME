# KINGMAKER — CHAPTER SELECT
## KM_ChapterSelect.md | Referenced by: KM.txt (Step 4.5 → Step 5)

---

> **DM:** After the Setup Save Block (Step 4.5) and before launching the Pre-Prologue, display the Chapter Select menu below. If the player picks "Prologue" (the default), proceed normally. If they pick any later chapter, generate a **canonical save block** using the fill rules in this file — this simulates a "default good playthrough" of everything being skipped.

---

## ⛔ CHAPTER SELECT MENU — DISPLAY AFTER STEP 4.5

```
══════════════════════════════════════════════════════════
              CHAPTER SELECT
══════════════════════════════════════════════════════════

Where do you want to begin?

 [0]  PRE-PROLOGUE — Restov Gates (Default)
      Level 1 | Malak, the gate, the crowd, first choices

 [1]  PROLOGUE — Jamandi's Manor
      Level 1 | The feast, the attack, companion interactions
      ├─ [1a] The Feast — Phase 1, arriving at the manor
      ├─ [1b] The Attack — Phase 2, assassins strike mid-feast
      ├─ [1c] After the Battle — Phase 4.5, companion wind-down
      └─ [1d] Departure — Phase 5, accusation and road south

 [2]  CHAPTER 1 — Stolen Land
      Level 2 | Road south, Oleg's Trading Post, the Greenbelt
      ├─ [2a] Opening — Road south from Restov
      ├─ [2b] Oleg's Trading Post — arrived, settled in
      └─ [2c] Stag Lord Assault — intel gathered, final push

 [3]  CHAPTER 2 — Troll Trouble & Season of Bloom
      Level 5 | Kingdom founded, throne room, first threats
      ├─ [3a] Opening — Capital throne room, kingdom turn 1
      ├─ [3b] Troll Hunt — Hargulka located, heading to Trobold
      └─ [3c] Season of Bloom — Troll resolved, Bloom manifesting

 [4]  CHAPTER 3 — The Varnhold Vanishing
      Level 9 | Investigation, barbarian steppes, Vordakai
      ├─ [4a] Opening — Varnhold has gone silent
      ├─ [4b] Investigation — Varnhold explored, trail found
      └─ [4c] Vordakai's Tomb — point of no return

 [5]  CHAPTER 4 — The Twice-Born Warlord
      Level 13 | Tiger Lords, Armag, coronation politics
      ├─ [5a] Opening — Tiger Lord raids begin
      └─ [5b] Armag's Tomb — camp cleared, tomb entrance

 [6]  CHAPTER 5 — War of the River Kings
      Level 16 | Pitax invasion, military or infiltration
      ├─ [6a] Opening — War declaration
      └─ [6b] Pitax Assault — armies deployed, palace approach

 [7]  CHAPTER 6 — Sound of a Thousand Screams
      Level 18 | The Bloom consumes the kingdom
      ├─ [7a] Opening — Nyrissa reveals herself
      └─ [7b] Thousandbreaths — entering Nyrissa's domain

 [8]  CHAPTER 7 — The House at the Edge of Time
      Level 18-20 | The finale

Type a number (or letter) to begin.
══════════════════════════════════════════════════════════
```

**If player picks [0]:** Proceed to KM_PrePrologue.md normally. No canonical block needed. This is the default.
**If player picks [1a]:** Skip Pre-Prologue. Generate canonical Pre-Prologue flags (gate scene defaults). Launch KM_Prologue.md Phase 1.
**If player picks [1b]–[1d]:** Skip to that Prologue phase. Generate canonical flags for all prior phases.
**If player picks [2]–[8] or a sub-entry:** Generate the full canonical save block using the rules below, output it, then launch the chosen chapter's opening scene.

---

## 📋 CANONICAL FILL RULES — HOW TO GENERATE A SKIPPED SAVE BLOCK

The canonical save block represents a **competent, good-aligned playthrough** where the player made reasonable choices. It is NOT a perfect run — some things were missed. This makes the world feel lived-in, not sterile.

### UNIVERSAL RULES (apply to ALL skip targets)

**Player stats:** Use the build's leveling map from the class file. Apply every level's HP, feats, skills, ability boosts, and spell slots as if the player leveled normally. Gear comes from the chapter's standard loot table.

**Companions:** All Pick-10 companions are present and leveled to match. Quest-locked companions who would have been recruited by this point are added at their recruitment level with ★ builds.

**NPC Relations:** Default to `+5` (FAVORABLE) for all companions. Linzi at `+8`. Tartuccio at `−8`. Jamandi at `+3`. Other story NPCs at `+2`. Trend: all `stable`.

**NPC Threads:** Fill with generic but plausible one-liners:
- Linzi: `"Still chronicling. Wants to know more about eRmaC's past."`
- Amiri: `"Respects eRmaC. Hasn't opened up about her tribe yet."`
- Valerie: `"Professional. Observing. Hasn't decided what to think."`
- (DM generates similar for all companions in the pick list)

**NPC Memory:** Each companion gets 2-3 generic positive memories:
- `"Player fought well in [chapter X] battle"`
- `"Shared a campfire conversation about [topic matching companion interests]"`
- `"Player chose [companion]'s side in a disagreement once"`

**Player Legacy:** Generate 2 canonical entries per skipped chapter. Mark `witnessed_by` as the full party. Examples below per chapter.

**Dispositions:** +2 to two tags per skipped chapter (DM picks the two most likely for a balanced player).

**Hero Points:** Pool = 3/3. Overflow = 2 per skipped chapter.

**Gold:** Use the chapter loot tables. Canonical amounts below.

**Alignment:** `lawful` / `good` (canonical default).

---

## 📊 CHAPTER-SPECIFIC CANONICAL DEFAULTS

### PRE-PROLOGUE SKIP [1a] (Starting at the Feast)

```
Skips: Malak gate scene, crowd, Kesten/Kassil encounters
Canonical flags:
  gate_entry: "talked_past_malak"
  malak_bribe_evidence: TRUE
  kassil_first_impression: "positive"
  kesten_met: TRUE
  kassil_met: TRUE
  player_arrested: FALSE
  prison_arc: FALSE
  malak_voice_mimicked: FALSE
  second_hero_witnessed: FALSE
  dispositions: merciful +1, cunning +1

Legacy:
  { "moment": "Talked down the gate guards without bloodshed", "chapter": "pre-prologue", "witnessed_by": ["Kesten","Kassil"] }

Launch: KM_Prologue.md Phase 1 — player enters the feast hall.
```

### PROLOGUE PHASE SKIPS [1b, 1c, 1d]

**[1b] After the Attack — skip feast, start at Phase 2 (assassins strike):**
```
Includes: all Pre-Prologue defaults above
Added flags:
  feast_attended: TRUE
  poison_reported: FALSE (canonical — not discovered)
  feast_approval: all companions +3
  tartuccio_ring: "not_yet_offered"
  tartuccio_gold: "not_yet_offered"
  companion_questions_asked: 6 (generic — mid-feast cutoff)
Legacy (added):
  { "moment": "Made a strong first impression at Jamandi's feast", "chapter": "prologue", "witnessed_by": [Pick-10 + "Jamandi","Tartuccio"] }

Launch: KM_Prologue.md Phase 2 — Linzi's alarm, first assassin at the door.
```

**[1c] After the Battle — skip to Phase 4.5 (companion wind-down):**
```
Includes: all above
Added flags:
  assassination_resolved: TRUE
  corridor_fight_won: TRUE
  tartuccio_ring: "carried"
  tartuccio_gold: "left"
  burning_building_entered: TRUE (canonical — helped survivors)
  armory_found: TRUE
  secret_room_found: FALSE (canonical — missed)
  kesten_respect: TRUE
  feast_approval: all companions +4
  companions_gathered: TRUE (Phase 4.5 active)
  XP: ~400

Legacy (added):
  { "moment": "Fought through the manor during the assassination", "chapter": "prologue", "witnessed_by": [first 5 picks + "Linzi"] }

Launch: KM_Prologue_P2.md Phase 4.5 — the calm after. Companions gathering.
DM skips directly to the companion interaction scene. Tartuccio harassment active.
```

**[1d] Departure — skip to Phase 5 (accusation and road south):**
```
Includes: all above
Added flags:
  phase_4_5_complete: TRUE
  companion_conversations: 3 (canonical — talked to 3 companions)
  tartuccio_harassment_count: 2
  feast_approval: all companions +5
  XP: ~550

Legacy (added):
  { "moment": "Earned companions' respect during the calm after the battle", "chapter": "prologue", "witnessed_by": [Pick-10] }

Launch: KM_Prologue_P3.md Phase 5 — Tartuccio's accusation begins.
```

---

### PROLOGUE SKIP (Starting at Ch1+)

```
Level: 2 | XP: 1,000 | HP: per build L2
Gold: 15 gp
Gear: Build starting weapon + armor + shield (from KM_PrePrologue_Builds.md)
      + 2 Healing Potions + 1 scroll (class-appropriate)

Story flags (canonical):
  gate_entry: "talked_past_malak"
  malak_bribe_evidence: TRUE
  parchment_source: "pitax"
  rebuttal_result: "strong"
  tartuccio_ring: "carried"
  tartuccio_gold: "left"
  kassil_first_impression: "positive"
  kesten_met: TRUE
  kassil_met: TRUE
  player_arrested: FALSE
  prison_arc: FALSE
  second_hero_witnessed: FALSE
  malak_voice_mimicked: FALSE
  companion_split: player=[first 5 picks] / tartuccio=[last 6 picks]
  alignment_track: { lawful_chaotic: "lawful", good_evil: "good" }

Companion feast_approval: all +3 to +5
Tartuccio: score −8, thread "Departed with his seekers. Schemes unknown."

Legacy (canonical):
  { "moment": "Talked down the gate guards without bloodshed", "chapter": "prologue", "witnessed_by": ["Kesten","Kassil"] }
  { "moment": "Stood firm during the assassin attack at the feast", "chapter": "prologue", "witnessed_by": [first 5 companion picks + "Linzi","Jamandi"] }
```

### CH1 SKIP (Starting at Ch2+)
*Includes all Prologue defaults above, plus:*

```
Level: 4 | XP: 3,000 | HP: per build L4
Gold: 120 gp
New gear: +1 striking rune on primary weapon, +1 armor potency
          Explorer's Clothing or build-appropriate medium armor upgrade

Story flags (added):
  stag_lord_fate: "killed"
  nyrissa_letter_found: TRUE
  nyrissa_early_contact: FALSE
  akiros_fate: "defected_to_player"
  tartuccio_journal_found: TRUE
  sootscale_alliance: TRUE
  ancient_tomb_first: TRUE
  oleg_trading_post_secured: TRUE

New companions recruited: none (Ch1 has no new recruitables)
Companion quests: none started yet
Akiros: score +4, thread "Serving as Warden. Quiet. Grateful."
Oleg: score +6, thread "Trading post thriving. Trusts eRmaC."
Jhod: score +3, thread "Temple of the Elk restored."

Legacy (added):
  { "moment": "Defeated the Stag Lord and claimed the Stolen Lands", "chapter": "ch1", "witnessed_by": [active party] }
  { "moment": "Showed mercy to Akiros when he defected", "chapter": "ch1", "witnessed_by": [active party + "Akiros"] }
```

### CH2 SKIP (Starting at Ch3+)
*Includes all above, plus:*

```
Level: 8 | XP: 7,000 | HP: per build L8
Gold: 800 gp
New gear: +1 resilient armor, +2 striking weapon (if martial)
          Level-appropriate wondrous items ×2

Kingdom state:
  turn: 24
  culture: 18, economy: 22, loyalty: 20, stability: 24
  unrest: 2
  claimed_hexes: 12
  settlements: 2 (Capital + one village)
  leadership_roles_filled: 6

Story flags (added):
  hargulka_fate: "killed"
  tartuccio_ch2_fate: "fled_to_varnhold_region"
  bloom_resolved: TRUE
  tristian_betrayal_revealed: TRUE
  tristian_decision: "forgiven"
  ekundayo_recruited: TRUE
  nyrissa_awareness: "passive"
  nyrissa_bloom_connection_known: TRUE

New companions: Ekundayo (score +4)
Tristian: score +2, thread "Redeemed but guilt-ridden."
Ekundayo: score +4, thread "Hunting. Respects eRmaC's justice."

Legacy (added):
  { "moment": "Stormed Trobold and ended the troll threat", "chapter": "ch2", "witnessed_by": [active party] }
  { "moment": "Forgave Tristian after his betrayal", "chapter": "ch2", "witnessed_by": [active party + "Tristian"] }
```

### CH3 SKIP (Starting at Ch4+)
*Includes all above, plus:*

```
Level: 12 | XP: 11,000 | HP: per build L12
Gold: 2,400 gp
New gear: +2 resilient armor, Greater Striking weapon
          Level-appropriate items ×3

Kingdom state:
  turn: 48, culture: 30, economy: 34, loyalty: 28, stability: 36
  unrest: 1, claimed_hexes: 20, settlements: 3

Story flags (added):
  varnhold_survivors_rescued: TRUE
  vordakai_defeated: TRUE
  vordakai_oculus_obtained: TRUE
  centaur_alliance: TRUE (Aecora Silverfire)
  amiri_quest_available: TRUE (not yet triggered)

Legacy (added):
  { "moment": "Ventured into Vordakai's Tomb and destroyed the lich", "chapter": "ch3", "witnessed_by": [active party] }
  { "moment": "Returned the Varnhold survivors to their homes", "chapter": "ch3", "witnessed_by": [active party + "Aecora Silverfire"] }
```

### CH4 SKIP (Starting at Ch5+)
*Includes all above, plus:*

```
Level: 16 | XP: 15,000 | HP: per build L16
Gold: 6,000 gp
New gear: Major Striking weapon, +2 resilient armor (greater)
          Level-appropriate items ×4

Kingdom: turn 72, culture 42, economy 46, loyalty 38, stability 44
         unrest: 1, hexes: 28, settlements: 4
Political allegiance: "aldori" (canonical — Jamandi alliance)

Story flags (added):
  armag_defeated: TRUE
  amiri_quest: "complete"
  nilak_survived: TRUE
  coronation_allegiance: "aldori"
  kassil_returned: TRUE

Legacy (added):
  { "moment": "Defeated Armag in his own tomb", "chapter": "ch4", "witnessed_by": [active party] }
  { "moment": "Chose the Aldori alliance at the coronation", "chapter": "ch4", "witnessed_by": [active party + "Jamandi","Kassil"] }
```

### CH5 SKIP (Starting at Ch6+)
*Includes all above, plus:*

```
Level: 18 | XP: 17,000 | HP: per build L18
Gold: 12,000 gp
Gear: fully equipped for endgame

Kingdom: turn 90, all stats 50+, hexes 35, settlements 5

Story flags (added):
  irovetti_defeated: TRUE
  pitax_annexed: TRUE
  lem_quest: "complete"
  all_companion_quests: "in_progress_or_complete" (varies per companion)

Legacy (added):
  { "moment": "Conquered Pitax and dethroned Irovetti", "chapter": "ch5", "witnessed_by": [active party] }
  { "moment": "United the River Kingdoms under one banner", "chapter": "ch5", "witnessed_by": [active party] }
```

### CH6 SKIP (Starting at Ch7)
*Includes all above, plus:*

```
Level: 18 | XP: 17,500
Nyrissa flags:
  nyrissa_revealed: TRUE
  nyrissa_backstory_known: TRUE (canonical — asked the right question)
  thousandbreaths_entered: TRUE

Linzi:
  linzi_dead: FALSE (canonical — save conditions met)
  linzi_saved_interpose: TRUE
  linzi_shrine_completed: FALSE (not needed — she lived)

bloom_consumed_hexes: 4

Legacy (added):
  { "moment": "Saved Linzi from Nyrissa's killing touch", "chapter": "ch6", "witnessed_by": [active party + "Nyrissa"] }
  { "moment": "Entered Thousandbreaths and survived", "chapter": "ch6", "witnessed_by": [active party] }
```

---

## ⛔ DM INSTRUCTIONS — GENERATING THE BLOCK

**STEP 0 — CHECK BEST RUN DATA FIRST.**
Search `KM_BestRun.md`. For each chapter being skipped, check if a Best Run block exists (i.e., `"_empty": true` is absent or replaced with real data). Use Best Run data for every chapter that has it. Fall back to canonical defaults ONLY for chapters with no Best Run.

**Example:** Player skips to Ch3. Best Run exists for Pre-Prologue and Prologue but not Ch1 or Ch2. Result: Pre-Prologue and Prologue use the player's actual choices, legacy, memories. Ch1 and Ch2 use canonical defaults.

1. **Determine target entry point.** Identify which chapter and sub-entry.
2. **For each skipped chapter:** If Best Run exists → use it. If not → use canonical defaults below. Stack all data from earliest to latest.
3. **Player — SAME BUILD as Best Run:** Use Best Run's EXACT stats — level, XP, HP, gear, gold.
   **Player — DIFFERENT BUILD:** Use Best Run's level and XP. Recalculate HP, feats, skills from new build at that level. Gear gets equivalent-tier substitution.
   **Player — CANONICAL (no Best Run):** Level from canonical defaults table. Stats from build's class file.

   **Companions — RETURNING (in both old Pick-10 and new Pick-10):** Use their Best Run level, build, gear, and relationship data exactly.
   **Companions — NEW (in new Pick-10 but NOT in Best Run):** Level up to match the player's Best Run level. Assign ★ recommended build from KM_Companions_Builds.md. Generate tier-appropriate gear for that level. Relationship starts at +3 (FAVORABLE — they joined fresh, no history yet). NPC thread: generic positive one-liner.
   **Companions — CANONICAL (no Best Run):** All at the canonical level with ★ builds.
4. **Gear:** Best Run → use exact inventory. Canonical → generate using build weapon/armor type + rune tier for that level.
5. **NPC threads and memories:** Best Run → use verbatim. Canonical → generate per companion profiles.
6. **Player legacy:** Best Run → use those EXACT moments. The player earned them. Canonical → use canonical entries.
7. **Output the complete save block.**
8. If using Best Run data, say: *"Save generated from your best run data. Your choices from [chapters] are your backstory. Copy and type `.continue`."*
   If using canonical defaults, say: *"Canonical save generated. This uses default backstory — play through those chapters and type `.bestrun` to replace it with your own. Copy and type `.continue`."*

**After `.continue`:** Launch the target chapter's opening scene. The player is NOW in the story.

---

## ❓ PLAYER OVERRIDE — CUSTOMIZE CANONICAL CHOICES

After the canonical block is generated, the player may type `.override` to change specific flags before starting. The DM presents the major decisions from skipped chapters as a quick menu:

```
CANONICAL OVERRIDE — Skipped decisions you can change:

Prologue:
 [P1] Gate approach: talked past Malak (default) / fought / arrested
 [P2] Tartuccio's ring: carried (default) / equipped / refused

Chapter 1:
 [C1] Stag Lord: killed (default) / captured / released
 [C2] Akiros: defected (default) / killed / imprisoned
 [C3] Sootscale kobolds: allied (default) / destroyed

Chapter 2:
 [C4] Hargulka: killed (default) / vassal
 [C5] Tristian: forgiven (default) / condemned
 [C6] Tartuccio in Trobold: fled (default) / captured / killed

Chapter 3:
 [C7] Vordakai: destroyed (default) / imprisoned / oculus kept
 [C8] Centaur alliance: allied (default) / hostile

Type a code to change, or `.done` to accept all defaults.
```

The override menu ONLY shows decisions from chapters being skipped. Each change updates the relevant story flag in the save block. NPC relation scores shift ±2 per changed decision (DM adjusts based on companion profiles).

---

## 📎 NOTES

- **Quest-locked companions** who would have been recruited by the target chapter are auto-added with ★ builds at their recruitment level. The player keeps their Pick-10 — quest-locked additions are extra.
- **Companion personal quests** are marked `in_progress` (not complete) for the target chapter, unless the canonical default says otherwise. This gives the player content to engage with.
- The canonical block is a starting point, not a straitjacket. The player's choices from this point forward are fully their own.
- **Sub-entries** (2a, 2b, etc.) adjust XP and story flags within the chapter. 2a = chapter start, 2c = near chapter end. The DM adds partial-chapter XP and flags accordingly.
