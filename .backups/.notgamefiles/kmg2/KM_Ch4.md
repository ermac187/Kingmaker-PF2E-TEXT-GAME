# KINGMAKER — CHAPTERS 4–7: WARLORD, WAR, BLOOM & FINALE
## KM_Ch4.md | Chapters 4, 5, 6, 7 Combined Reference

---

> **DM:** This file covers Chapters 4 through 7. Load alongside: KM.txt, KM_Companions.md, KM_Companions_B.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_Leveling.md. For Ch6+: also load KM_Linzi_Shrine.md. Chapter 7 contains bad ending and true ending conditions.

---

# ═══════════════════════════════════════════
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
```

**ARMAG — Final Boss:**
```
ARMAG — see KM_Bestiary_B.md for full stat block (CR 11, HP 205, AC 28)

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

### 🏆 SIDE QUEST — RUSHLIGHT TOURNAMENT

**Available:** Ch4, after coronation. Irovetti sends a formal invitation to compete in the Rushlight Tournament in Pitax — a River Kingdoms arms competition. Optional but rewarding.

**Events (player chooses which to enter):**

| Event | Check | 1st Place Prize |
|-------|-------|----------------|
| Archery | Ranged attack vs DC 22/26/30 (3 rounds) | Composite Longbow +2 |
| Axe Throwing | Athletics DC 18/22/26 | Belt of Giant Strength |
| Horse Race | Survival DC 16 + Athletics DC 14 | War-trained horse |
| Wrestling | Athletics DC 20 vs opponent ×3 | Ring of Feather Falling |
| Grand Melee | Combat vs 3 CR 9 opponents (non-lethal) | +2 Striking Weapon (choice) |

**Intelligence:** Attending grants access to Pitax. Perception DC 18 → spot Tartuccio in crowd (`tartuccio_pitax_sighted = TRUE`). Stealth DC 16 to investigate → find Irovetti's River Kingdom recruitment posters. `pitax_war_prep_discovered = TRUE` → Ch5 first army engagement +2.

**Irovetti** approaches after any event. Courteous, testing. Sense Motive DC 14: he is afraid of you and covering it well.

`rushlight_attended = TRUE` | `rushlight_events_won = [list]` | `pitax_intel_gathered = TRUE/FALSE`

**XP:** +200 attending. +100 per event won. +300 if `pitax_war_prep_discovered = TRUE`.

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
□ KM_Ch4.md loaded (this file — chapters 5-7 are in here)
□ All standard files loaded (see KM.txt How to Continue)
□ Ch4 Export Block imported and parsed
□ Player level 16+, inventory and kingdom state confirmed
□ Key flags read:
    political_allegiance    : aldori / surtova / independent
    coronation_complete     : TRUE
    pitax_irovetti_aware    : TRUE
    all companion quests    : [status of each]
    alignment_track         : [both axes]
□ Note: Lem's personal quest triggers this chapter
□ Note: Military path and infiltration path BOTH available — confirm preference
□ Game State Header output, then begin
```

---

# ═══════════════════════════════════════════
# CHAPTER 5 — WAR OF THE RIVER KINGS
# ═══════════════════════════════════════════

**Levels:** 16 → 18 | **Duration:** ~90 days
**New region:** Pitax, River Kingdoms, Irovetti's palace

## Overview
Irovetti of Pitax invades. Two parallel approaches: **military campaign** (army battles, siege warfare) and **infiltration** (assassination, political subversion). Both are available and can be combined. Irovetti must be defeated. His palace must be taken.

---

## Phase 1 — War Declaration

> **Herald:** *"Irovetti of Pitax declares that the Stolen Lands are an illegal territory, their ruler a bandit-king, and their kingdom a blight upon the River Kingdoms. He invades in the name of civilization."*

Kingdom events become war events — economy disrupted, borders threatened.
Lem's personal quest triggers here (Academy students in Pitax).

---

## Phase 2 — Military Campaign (available)

```
ARMY SYSTEM BECOMES ACTIVE:
  Player's armies engage Pitax forces on the hex map.
  Pitax has 3 initial army units:
    Pitax Royal Guard: Offense +8, Defense 18, Morale 16
    River Mercenaries ×2: Offense +5, Defense 14, Morale 12
  Player must match with equivalent armies or better.

BRINEHEART SIEGE:
  Border fortress — first major military engagement.
  Army combat OR player party assault on the fort directly.
  Fort AC 22, HP 120. Garrison: 8 soldiers + Linxia (Pitax captain).

LINXIA:
  HP: 96 | AC: 22 | Rapier d20+15 (1d6+8, Sneak Attack +5d6) | Evasion
  Persuade her to defect: Diplomacy DC 28 → +25,000 gp reward, fort surrenders
  Kill her: standard loot + fort taken

DARVEN — PITAX MERCHANT (SIDE QUEST):
  Darven Mourne approaches during Brineheart siege or at capital (infiltration path).
  Not a fighter. A businessman who backed the wrong king.

  DARVEN: "I funded Irovetti for six years. I would prefer my head stay attached.
           I can offer something worth more than my neck."

  Offer: 25,000 gp, four Pitax supply chain maps (army costs −10% for 2 turns),
  signed confession of war crimes (River Kingdoms diplomacy post-Ch5).
  In exchange: his life and safe conduct through the Stolen Lands.

  - Accept → `darven_deal = accepted` → 25,000 gp + maps + confession. Recurring Ch6 contact.
  - Negotiate (Diplomacy DC 18) → same + hidden palace basement cache. `darven_cache_location = TRUE`
  - Arrest → `darven_arrested = TRUE` → +1 Loyalty, +5,000 gp seized. No maps.
  - Kill → `darven_killed = TRUE` → nothing. Slight evil tendency.

  `darven_fate = [accepted / negotiated / arrested / killed]`
  XP: +200 any resolution except kill. +100 if negotiated.
```

---

## Phase 3 — Infiltration Path (available)

```
PITAX INTELLIGENCE:
  Spymaster role (if filled) provides advantages: maps, guard patrol timing
  Without Spymaster: Perception DC 20 checks throughout Pitax

IROVETTI'S PALACE APPROACH:
  Three infiltration options:
  A. Sewers (Athletics DC 16 per junction, multiple junctions)
  B. Noble disguise (Deception DC 24, requires noble outfit purchased for 500 gp)
  C. Servant disguise (Deception DC 18, servants are questioned less)

INSIDE THE PALACE:
  Academy of Grand Arts: Lem's students here — rescue them (Stealth DC 14 each room)
  Irovetti's vault: 8,400 gp, Ring of the Archmagi
  Tartuccio's note: `tartuccio_pitax_connection_confirmed = TRUE`
    (A letter in Irovetti's desk — Tartuccio has been reporting on the player since Ch1)
```

---

## Phase 4 — Irovetti

> **⛔ GM EYES ONLY — IROVETTI'S FULL NAME — READ BEFORE RUNNING ANY SCENE WHERE HIS NAME COMES UP**
>
> **Full name: Castruccio Irovetti of Pitax**
> "Irovetti" is his house name. He rules exclusively as "Irovetti of Pitax" — his given name Castruccio is suppressed. He does not use it, sign with it, or acknowledge it publicly. Most of the River Kingdoms do not know it exists. Paizo buries it deliberately so players do not make the connection immediately.
>
> **THE TARTUCCIO CONNECTION — NEVER VOLUNTEER THIS:**
> Castruccio → Tartuccio. Same Taldan diminutive construction (-struccio / -tuccio). One letter apart. Same rhythm. Same origin.
> Tartuccio is named in deliberate echo of his patron's buried given name. It is a calling card legible only to someone who knows both names.
> When Tartuccio said *"my mother had aspirations"* — he was not lying. She named him after the part of the king that nobody says out loud.
>
> **DISCOVERY RULE — MANDATORY:**
> The DM never surfaces this connection unprompted. It exists to be found by the player through logical deduction: naming conventions → River Kings' full names → first name vs house name → what is Irovetti's given name → Castruccio → Castruccio/Tartuccio said aloud in the same breath.
> Linzi is the natural vector. She notices linguistic patterns. If the player leads her toward it, she can arrive at it. The DM's job is to follow the chain and let it land — not to shortcut it and not to stall when the player is clearly building toward it.
> The payoff is Linzi saying "Castruccio" out loud while Tartuccio is in the room and watching his face.

```
IROVETTI — see KM_Bestiary_B.md for full stat block (CR 13, HP 195, AC 32)

SPECIAL: Court musicians play during fight — Performance DC 20 to silence.

RESOLUTION:
  Kill → Kingdom gains Pitax as vassal.
  Capture → Public trial. Handed to Brevoy → Jamandi bonus.
  Recruit [Evil] → Impossible. Too vain.

LOOT: +2 Striking Rapier, Cloak of Resistance +4, Headband of Mental Perfection +4,
      Irovetti's Crown, 8,400 gp vault, 3,789 gp treasury
XP: 1,560
```

```
LINXIA — Pitax Captain (Rogue 9)
HP: 96 | AC: 22 (Studded Leather +2 + Dex) | Speed: 30 ft
Fort +12 | Ref +18 | Will +11
Rapier: d20+15 (1d6+8 P, Finesse) | Sneak Attack: +5d6
Evasion: On Ref success vs AoE — no damage
Gang Up: gains Flanking bonus even without an ally (her shadows count)
Persuade to defect: Diplomacy DC 28 → surrenders fort, joins as informant
XP: 480
```

---

## Ch5 → Ch6 Export
```json
{
  "export_from": "chapter_5", "import_to": "chapter_6",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "armies": [],
               "pitax_vassal": false },
  "story_flags": {
    "irovetti_fate": "",
    "pitax_vassal": false,
    "linxia_fate": "",
    "darven_fate": "",
    "lem_quest": "",
    "tartuccio_pitax_confirmed": true,
    "tartuccio_final_fate": "",
    "military_path_used": false,
    "infiltration_path_used": false,
    "brineheart_taken": false,
    "river_kingdoms_allied": [],
    "companion_quests": {},
    "alignment_track": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "standing_orders": {}, "crafting": {}, "mobile_base": {},
  "dream_log": [], "prestige": {}, "mythic_path": {}, "ending_flags": {}
}
```

## 📋 CH6 LOAD CHECKLIST
```
[GM CHAPTER 6 LOAD CHECK]
□ KM_Ch4.md loaded (this file — Ch6 is in here)
□ KM_Linzi_Shrine.md loaded — shrine quest may trigger this chapter
□ All standard files loaded (see KM.txt How to Continue)
□ Ch5 Export Block imported and parsed
□ Player level 16–18, kingdom state confirmed
□ Key flags read:
    irovetti_fate           : [value]
    pitax_vassal            : [TRUE/FALSE]
    tartuccio_final_fate    : [value — he should be resolved by now]
    all companion quests    : [status — CRITICAL for Ch7 survival]
    alignment_track         : [both axes]
    nyrissa_backstory_known : [TRUE/FALSE — affects true ending]
□ COMPANION QUEST AUDIT: list every companion and their quest status
   Any incomplete quests = risk of losing that companion in Ch6 or Ch7
□ Bloom escalation will consume hexes each kingdom turn — prepare defenses
□ Game State Header output, then begin
```

---

# ═══════════════════════════════════════════
# CHAPTER 6 — SOUND OF A THOUSAND SCREAMS
# ═══════════════════════════════════════════

**Levels:** 18 | **Duration:** ~60 days (hard — Bloom escalates fast)
**Tone:** Supernatural horror. Your kingdom is being consumed.

## Overview
The Bloom reaches its final stage. Nyrissa reveals herself directly. Your kingdom loses hexes to supernatural infestation each turn. You must: defend key settlements, find Nyrissa's lair (Thousandbreaths), and enter it. This chapter is a race against collapse.

---

## Phase 1 — The Kingdom Crumbles

**Each kingdom turn this chapter:** Roll d6. On 1–3, a hex is consumed by the Bloom. Claimed hexes revert to Hostile. Buildings in consumed settlements take damage.

**Nyrissa speaks for the first time (scripted):**
> *She is standing in your throne room.*
> *Not attacking. Not threatening. Just standing there as if she owns it.*
>
> **Nyrissa:** *"I have been watching you since before you arrived at that gate in Restov. Every choice you made, I helped arrange. Not because I wanted you to fail — because I needed you to succeed at exactly this level."*
>
> *"Your kingdom is not your achievement. It is my vessel."*

`nyrissa_revealed = TRUE`

**True ending requirement begins here:** How the player responds to Nyrissa matters.
- Aggressive → she disappears, nothing changes
- [Curious] "What do you actually want?" → +lore, Nyrissa explains her curse (Lantern King imprisoned her love) → `nyrissa_backstory_known = TRUE` — **this flag is required for the true ending**

---

## Phase 2 — Companion Survival Checks

This chapter triggers any incomplete companion quest consequences:
```
valerie_quest incomplete → Valerie trapped in burning prison this chapter
                           Player must choose: save Valerie or continue forward
                           Saving her: Perception DC 16 + Athletics DC 18

harrim_quest incomplete → Harrim wanders off during Ch6 dungeon exploration
                          Returns but misses critical fights

jaethal_quest incomplete → Jaethal briefly hostile (Urgathoa influence)
                           Diplomacy DC 20 to bring her back each scene

linzi_quest and 3 other conditions for save → see below
```

---

## Phase 3 — Thousandbreaths

**Thousandbreaths** — Nyrissa's domain. A pocket dimension accessible via a portal in the Narlmarches.

```
DUNGEON PROPERTIES:
  Extradimensional space — rules of normal reality are unstable
  Lighting: perpetual deep twilight — Dim Light conditions everywhere
             (Elves, Half-Elves immune via Low-Light Vision)
  Time distortion: every 2 rooms, party gains Fatigued unless Fort DC 16 succeeded

ENEMIES (all Nyrissa's servitors — fey and bloom-touched):
  Bloom Guardian ×6: HP 85 | AC 20 | Tendril ×2 d20+12 (2d6+8, Grab)
  Nyrissa's Archer ×4: HP 68 | AC 18 | Longbow d20+14 (2d8+6, Vital Strike)
  Verdant Nightmare (boss room guardian):
    HP: 145 | AC: 22 | Slam d20+15 (3d6+10) | Aura: Frightened 2 (Will DC 20)

LOOT: Staff of Nyrissa (Occultism +4 item bonus, cast Wall of Thorns at will),
      Ring of Regeneration, Cloak of Elvenkind, 4,400 gp
```

**LINZI'S DEATH — Ch6 trigger:**
The exact moment Nyrissa kills Linzi occurs at the end of Phase 3, just before the final confrontation room.

> *Nyrissa steps from the shadows. She is beautiful and entirely wrong.*
> *She looks at Linzi with something almost like pity.*
> **Nyrissa:** *"The little one. She has been writing everything down. That is a kind of immortality."*
> *She touches Linzi's chest. Linzi crumples.*

**OPTIONAL SAVE CHECK** (if all 4 conditions met — see KM_Companions.md):
Diplomacy DC 28 or 2 Hero Points to interpose before Nyrissa acts.
Success: `linzi_saved = TRUE` — she survives Ch6 physically. Skip shrine quest.
Failure or conditions not met: Linzi dies. `linzi_dead = TRUE`

**SHRINE QUEST TRIGGERS ON RETURN TO CAPITAL:**
If `linzi_dead = TRUE`: Jhod Kavken meets the player with three scrolls.
The player must choose ONE god's shrine to build. This is the only chance.
One choice. One price. One outcome.

> **See `KM_Linzi_Shrine.md` for the complete three-path resurrection quest:**
> - **Shelyn (Good)** — Give something you made that matters
> - **Pharasma (Neutral)** — Destroy an abomination against death
> - **Urgathoa (Evil)** — A feast, an ongoing kingdom tithe, and Linzi's consent

The shrine quest must be resolved before entering the House at the Edge of Time (Ch7).
If the player enters Ch7 without resolving it: the window closes. `linzi_dead = TRUE` permanently.

---

## Ch6 → Ch7 Export
```json
{
  "export_from": "chapter_6", "import_to": "chapter_7",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "bloom_consumed_hexes": 0 },
  "story_flags": {
    "nyrissa_revealed": true,
    "nyrissa_backstory_known": false,
    "thousandbreaths_entered": true,
    "linzi_dead": false,
    "linzi_saved_interpose": false,
    "linzi_shrine_completed": false,
    "linzi_mark": "",
    "valerie_survived_ch6": true,
    "harrim_quest": "",
    "jaethal_quest": "",
    "octavia_quest": "",
    "regongar_quest": "",
    "amiri_quest": "",
    "nilak_survived": false,
    "tristian_redeemed": false,
    "ekundayo_quest": "",
    "noknok_quest": "",
    "lem_quest": "",
    "kalikke_kanerah_quest": "",
    "storyteller_collection": false,
    "bloom_consumed_hexes": 0,
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
□ KM_Ch4.md loaded (this file — Ch7 is in here)
□ KM_Linzi_Shrine.md loaded (if shrine quest is active or pending)
□ All standard files loaded
□ Ch6 Export Block imported and parsed
□ Player level 18–20, full inventory confirmed

CRITICAL PRE-ENTRY AUDIT:
□ Read every companion's quest status aloud to the player:
  → "Amiri: [complete/incomplete] — [consequence if incomplete]"
  → "Linzi: [alive/dead/shrine-returned] — mark = [none/shelyn/pharasma/urgathoa]"
  → [repeat for all 11 companions]
□ Ask: "Are you ready to enter the House at the Edge of Time?
         Once inside, you cannot leave until it's over."

TRUE ENDING READINESS:
□ nyrissa_backstory_known = TRUE? (from Ch6 Phase 1 curiosity response)
□ If FALSE: warn player the true ending requires this flag.
             Last chance — they can ask Nyrissa now (she's in their throne room).

□ storyteller_collection = COMPLETE? (all 10 fragments)
   If yes and Linzi is alive + Devoted: Linzi save option still available inside.

□ Game State Header output, then ask player to confirm before writing any scene.
```

---

# ═══════════════════════════════════════════
# CHAPTER 7 — THE FINAL ACT
# ═══════════════════════════════════════════

**Levels:** 18–20 | **Final chapter**
**Location:** House at the Edge of Time — Nyrissa's true domain

## Overview
The final dungeon. The Lantern King's curse is the root of everything. Five endings exist based on accumulated flags — see `KM_Endings.md` for full requirements and scripted narration. The ending is NOT chosen from a menu — it emerges from play.

---

## The House at the Edge of Time

**Point of no return.** All companion quests must be resolved before entering.

> **DM:** Before the player enters, run the companion check:
> - List every companion's quest status
> - Warn: "Any incomplete quests mean that companion faces their Ch7 risk inside"
> - Ask: "Are you ready to proceed?"

```
DUNGEON PROPERTIES:
  Time flows differently — past and present overlap in different rooms
  Some rooms show the kingdom's founding; others show its destruction
  Companions see visions of their personal fears (roleplay opportunities)
```

---

## Companion Fates Inside

```
All quests complete → all companions present for the final fight

Incomplete quests trigger:
  Valerie → burning prison room — Perception 16 + Athletics 18 to save her
  Harrim  → wanders off, rejoins after Nyrissa fight
  Jaethal → Urgathoa influence — Diplomacy 20 each scene to keep her aligned
  Octavia + Regongar (one quest incomplete) → prison room, save one
  Octavia + Regongar (both incomplete) → both imprisoned, save one only
  Amiri (nilak_died) → present but leaves after Nyrissa is defeated (grief)
```

---

## Nyrissa — The True Fight

```
NYRISSA — see KM_Bestiary_B.md for full stat block (CR 20, HP 380, AC 43)

PHASE 1 (HP 380–190): Thorn Wall, Dominate (lowest Will), Wail of the Lost, Fey Step (teleport 60 ft).

PHASE 2 (below 190 — Lantern King intervenes):
  Heals Nyrissa to 190 HP. "Go on then. Finish her. That's what I've been waiting for."
  He wants you to kill her — that's part of the curse.

THE CHOICE (true ending gate):
  Kill Nyrissa (standard) → BAD ENDING
  [Requires: nyrissa_backstory_known = TRUE]:
    "I know what he did to you. I know what was taken."
    → Nyrissa pauses. She looks at the Lantern King.
    → Diplomacy DC 30 OR 2 Hero Points
    → SUCCESS: Break the curse. Confront the Lantern King. TRUE ENDING.
    → FAIL: Fight continues, bad ending.
```

---

## Default Ending (The Ruler's Ending)

Kill Nyrissa without meeting true ending requirements. Kingdom survives with reduced stats. No resolution to the Lantern King's curse. Full scripted narration in `KM_Endings.md` — Ending 1.

**Other endings** (Conquest, Transcendence, Golden) fire based on accumulated flags. See `KM_Endings.md` for all 5 ending variants and their flag checklists. DM checks eligibility at Ch6 opening.

---

## True Ending

> *Nyrissa stares at the Lantern King.*
> **Nyrissa:** *"You gave me a heart so you could take it. You cursed me to love what I destroy. For ten thousand years."*
>
> *The Lantern King is not laughing anymore.*
>
> *"You were supposed to kill her," he says to you. "That was the arrangement."*
>
> *The Lantern King waits for an answer. Present a choice menu — the player's response is their own.*

```
LANTERN KING — Eldest Fey (Trickster Divinity)
HP: 320 | AC: 30 | Cannot be permanently killed (he is a fundamental force)
His attacks deal Confused 1 (Will DC 26) on hit — trickery made manifest
His weakness: Honesty. The more directly the player speaks truth to him, the lower his DCs.

Each round: Player can attack OR speak truth:
  [Attack] → deals damage, no special effect
  [Truth] → Lore (Fey) DC 20 OR player identifies something real about him
    → His AC drops by 1 per truth told (cumulative, max −6)
    Examples: "You're afraid of what you created." (+1 AC reduction)
              "You've been alone since before this kingdom existed." (+1)
              "She loved something you made and you couldn't stand it." (+2)

At 0 HP: The Lantern King cannot die. He yields. For the first time in ten thousand years, someone made him yield.
He removes Nyrissa's curse. She is free.
```

> *Nyrissa kneels in the ruins of the House.*
> **Nyrissa:** *"I don't know what I am without the curse."*
> *She looks at you. And at the kingdom visible through the crumbling walls.*
> *"But I would like to find out."*

**True Ending outcomes:**
- Nyrissa can be offered a place in your kingdom (she becomes a permanent ally — unique advisor)
- Kingdom receives the Bloom's land back (all consumed hexes restored)
- `true_ending_achieved = TRUE`
- Linzi (if saved): writes the final chapter of the chronicle — the real one

---

## Final XP & Epilogue

| Source | XP |
|--------|----|
| Ch7 dungeon encounters | ~4,800 |
| Nyrissa (boss) | 2,000 |
| Lantern King (true ending) | 1,600 |
| Companion saves | 400–800 depending |
| **Chapter 7 Total** | **~9,200–10,000** |

**Final Kingdom State:**
- True Ending: All stats restored, Bloom land reclaimed, Nyrissa as optional advisor
- Bad Ending: Kingdom survives, permanently reduced Culture and Loyalty, cursed undercurrent

---

## 🎭 EPILOGUE SCENES (Linzi's Questions)

Linzi (or her book, if she died) asks the player a final series of questions about their reign. Answers generate the epilogue narrative.

```
1. What was your kingdom known for? (Culture / Economy / Military / Justice)
2. What happened to [key NPC]? (For each major NPC — outcomes based on flags)
3. Did you rule with the sword or the word? (Alignment-based)
4. What came next? (Open-ended — player describes what happens after)
```

---

*KM_Ch4.md — Kingmaker PF2e Text Adventure | Chapters 4–7 v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) + Owlcat Games | PF2e rules: 2e.aonprd.com*
