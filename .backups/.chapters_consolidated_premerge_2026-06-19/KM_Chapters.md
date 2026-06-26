# KINGMAKER — CHAPTERS (CONSOLIDATED)
## KM_Chapters.md | v1.0 (2026-05-22): Merged from Ch1 + Ch1_B + Ch1_Export + Ch2 + Ch2_P2 + Ch3 + Ch4 + Linzi_Shrine.

> **DM:** Load when running any post-Prologue scene. Each chapter section preserves source structure.

**Table of Contents**
- [Chapter 1 — Stolen Land](#chapter-1)
- [Chapter 1 Sidecar (combat / Stag Lord encounters)](#chapter-1-sidecar)
- [Chapter 1 Export Template](#chapter-1-export)
- [Chapter 2 — Troll Trouble](#chapter-2)
- [Chapter 2 Part 2 (continuation)](#chapter-2-part-2)
- [Chapter 3 — Varnhold Vanishing](#chapter-3)
- [Chapter 4 — Blood for Blood / War of the River Kings](#chapter-4)
- [Linzi Shrine (post-Ch6 fallback)](#linzi-shrine)



---

<!-- merged from KM_Ch1.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 1: STOLEN LAND
## KM_Ch1.md | Loads after: KM_Prologue_Systems.md | Loads before: KM_Ch2.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_BuildGuide.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md. Import Prologue JSON Export Block before beginning. Ch1 ends on Stag Lord defeat + return to Oleg's. Output Ch1 Export Block (KM_Ch1_Export.md) at chapter end.

---

## 📋 CH1 LOAD CHECKLIST

```
[GM CHAPTER 1 LOAD CHECK]
□ All files loaded and confirmed
□ Prologue JSON Export Block imported and parsed
□ Player character sheet reconstructed — level, XP, HP, inventory
□ Active companions confirmed (Amiri + 2 from prologue split)
□ Story flags read:
    gate_entry              : [value]
    malak_bribe_evidence    : [TRUE/FALSE]
    parchment_source        : pitax (fixed)
    rebuttal_result         : [strong/weak]
    companion_split         : player=[list] / tartuccio=[list]
    kassil_first_impression : [positive/neutral/negative]
    kesten_respect          : [TRUE/FALSE]
□ Prologue companions with Tartuccio noted (recruitable in this chapter)
□ Quest log loaded — active: Stolen Land (90-day limit)
□ Resources confirmed — camping supplies, rations, spell slots, gold
□ Game State Header output and confirmed by player
□ AUTO-LOOT fires after every combat automatically — do NOT wait for player (.fail 15 if skipped)
□ ONLY THEN: Begin Ch1 opening scene
```

---

## 🗺️ CHAPTER 1 OVERVIEW

**Levels:** 1 → 4 (L2 early-mid chapter, L3 at Stag Lord, L4 at chapter end with full clear)
**XP per level:** 1,000 each (L2=1k, L3=2k, L4=3k, L5=4k cumulative)
**Time limit:** 90 days from 16 Gozran 4710 AR (soft — see KM.txt Game Options)
**Speed bonus:** Complete in 30 days → Lord Protector (+2 Dueling Sword) from Jamandi
**Main objective:** Defeat the Stag Lord. Claim the Stolen Lands. Return to Oleg's.

**Two interlocking main quests:**
- **Stolen Land** — defeat the Stag Lord (charter quest)
- **A Bitter Rival** — track and confront Tartuccio (personal quest)

**Order matters:** Which you pursue first (Ancient Tomb vs Thorn Ford) changes encounters. See quest flags below.

---

## 🚀 OPENING SCENE — THE ROAD SOUTH

### Narration (adapt to build perspective filter)

> *Three days on the road south from Restov. The Stolen Lands begin where Brevoy's roads end — the packed stone gives way to dirt, then to grass, then to nothing in particular. The Greenbelt opens ahead of you: vast, flat, and indifferent.*

> *Your companions travel in [formation based on party]. Amiri walks ahead of everyone, bastard sword over her shoulder, eyeing every tree line. [Second companion] [brief personality note]. [Third companion if applicable] [note].*

> *You have the charter. You have 90 days. You have no idea yet what either one actually means.*

**FIRST ENCOUNTER — Thylacines (scripted tutorial, mandatory)**
```
Three Thylacines ambush on the road. Marsupial predators, wolf-sized.
Each: HP 12 | AC 14 | Jaws d20+4 (1d8+2 P) | Speed 35 ft
Poison on bite: Fort DC 12 or Enfeebled 1 for 1 hour
Roll initiative. Standard combat. Introductory difficulty.
XP: 30 per creature = 90 XP total
Loot: None (wild animals)
```

> *After the fight, Linzi (or whoever is in party) produces her notebook.*
> **Linzi** (if present): *"First combat in the Stolen Lands! I'm calling this chapter: 'The Land Bites Back.' Metaphorically. And also literally, that was a bite."*
> **Amiri**: *"Weak. Come back when you've fought a giant."*

**After combat:** First camping opportunity. Tutorial: Prepare Campsite (Survival DC 15).

---

## 📍 PHASE 1 — OLEG'S TRADING POST

### Arrival at Oleg's (Day 3)

**Scene Brief:**
```
[GM SCENE BRIEF — Oleg's Trading Post]
LOCATION   : HEX (1,0) — Northern Greenbelt
NPCS       : Oleg Leveton (merchant, gruff, scared), Svetlana Leveton (logistician, warm),
             Bokken (eccentric alchemist, hut 5 mi south — not at post by default)
LOCKED     : Kesten Garess — arrives after Happs raid repelled (kesten_respect flag applies then)
             Jhod Kavken  — arrives after party engages Stag Lord's bandit network
ACTIVE FLAG: kesten_respect — if TRUE, Kesten greets player with genuine respect
QUEST GIVERS: Oleg (Deal with Bandits), Svetlana (Wedding Ring)
              Kesten (Falgrim Sneeg) — unlocks when he arrives after Happs
              Jhod (Temple of the Elk) — unlocks when he arrives later
VENDOR     : Oleg — general goods, rations, basic equipment (see Economy section)
TRIGGERS   : Remus encounter triggers after player LEAVES Oleg's for the first time
[END BRIEF]
```

**Kesten Garess arrival** (flag-dependent):
- `kesten_respect = TRUE` → Kesten is already there, greets player by name, mentions hearing about the gate. *"What you did at the gate — that took judgment. I wanted to say that."* Falgrim quest available immediately.
- `kesten_respect = FALSE` → Kesten arrives but is professionally neutral. Falgrim quest still available.
- `kassil_first_impression = positive` → Kesten mentions Kassil spoke well of the player. +1 starting attitude.

**OLEG's OPENING:** Bandits arrive as the player gets there, or Oleg explains their weekly toll.

> *A stocky man with a crossbow and the look of someone who has been frightened for months stands at the gate. Behind him, a woman with neat brown hair and ink-stained fingers watches from the trading post steps.*
> **Oleg:** *"You're the adventurers Jamandi sent? Good. They're coming again tomorrow — every week, same time, demanding 'taxes' for the Stag Lord. Take everything we have and call it tribute. I've had enough."*

**Quest triggers activate at Oleg's:**
- Oleg → *Deal with the Bandits* (stop the weekly raids)
- Svetlana → *Svetlana's Ring* (Kressle has it at Thorn Ford)
- Jhod → *Find the Temple of the Elk* (⛔ NOT at session start — arrives after bandit network engaged)
- Kesten → *Capture Falgrim Sneeg* (deserter, random encounter — see below)

---

### ⚔️ SIDE QUEST — FALGRIM SNEEG

**Quest giver:** Kesten Garess. Unlocks immediately if `kesten_respect = TRUE`, otherwise Day 3–5. Wants Falgrim alive — a deserter who fled south with stolen coin.

**Trigger:** Narlmarches hexes (−1,−2 or −2,−2). Roll d6 on entry — 5–6: camp found.
`Falgrim: Rogue 3 | HP 32 | AC 17 | Shortsword +8 (1d6+4) | Sneak Attack +2d6 | Breaks at half HP`

| Resolution | Flag | Outcome |
|-----------|------|---------|
| Capture alive | `falgrim_captured` | Kesten +1 Relationship, Masterwork Shortsword, +150 XP |
| Kill | `falgrim_killed` | Kesten accepts it. +75 XP. |
| Release | `falgrim_released` | Kesten −1 Relationship. |

---

### 🗡️ SIDE QUEST — THE LONELY WARRIOR

**Location:** Hex (−1,−3), ruined watchtower. Exploration only.
> *Armor upright. Longsword through floor. Stone: ARMAND SURTOVA — "I held the line. No one came."*

Ghost appears dusk/dawn (Perception DC 14). Not hostile.
- **Promise to find the record** → Diplomacy DC 12 → fades, gives sword. `lonely_warrior_resolved = TRUE` → **+1 Longsword (Ancestral Gravitas)**: +1 attack/damage, +2 circ. Diplomacy (Brevoy nobles). +150 XP.
- **Attack** → HP 40, AC 16, Longsword +7 (1d8+4). +80 XP. No sword.

---

### 📜 STORYTELLER — EXCHANGE TABLE

Appears at Oleg's after kingdom founding. Each exchange fires once. Track `storyteller_coins_delivered` / `storyteller_relics_delivered` in save block.

| Brought | Reward |
|---------|--------|
| 1st Coin | Vordakai's name + 100 XP |
| 3rd Coin | `vordakai_island_hint = TRUE` |
| 6th Coin | Ioun Stone (Dusty Rose Prism, +1 AC) |
| Dryad Token | Scroll of Restoration (L4) |
| Mite's Relic | Potion of Heroism |
| 3 Coins + 2 Relics | Ring of Protection (+1) |

### 🗡️ STAG LORD'S HELM — DECISION FLAG

**After looting — decide before leaving the fort:**
1. Keep — +2 circ. Intimidation | 2. Send to Jamandi — +75 gp + commendation (+1 Aldori rep) | 3. Bury — alignment: Good | 4. Sell at Oleg's — 40 gp | 5. Give to Amiri — Relationship +1

`stag_lord_helm = [kept / sent_to_jamandi / buried / sold / given_to_amiri]`

---

### OLEG'S VENDOR TABLE

| Item | Cost |
|------|------|
| Rations (1 day) | 5 sp |
| Arrows/bolts (20) | 1 gp |
| Healer's Tools | 5 gp |
| Antitoxin | 3 gp |
| Minor Healing Potion | 4 gp |
| Alchemist's Fire | 3 gp |
| Acid Flask | 3 gp |
| Basic melee weapons | Standard PF2e |
| Studded Leather | 3 gp |

**Expanded Stock** (after first Kingdom Turn — `oleg_expanded = TRUE`):

| Item | Cost |
|------|------|
| Lesser Healing Potion | 12 gp |
| Antiplague | 3 gp |
| Scale Mail | 4 gp |
| Chain Shirt | 5 gp |
| +1 weapon (rotates weekly) | 35 gp |

> Svetlana manages the ledger. Ring quest complete → one-time 10% discount on any purchase.

---

## ⚔️ PHASE 2 — THE BANDIT ENCOUNTER (Oleg's, Day 4)

> *Morning. The gates are open. Four bandits ride in on horses, confident in their weekly routine. Happs Bydon leads them — a wiry man in his thirties, shortbow across his back, riding like he owns the road.*

```
[BANDIT RAID — Oleg's Trading Post]
Enemies: HAPPS BYDON (Fighter 2)       | HP 22 | AC 16 | Shortbow d20+6 (1d6+2 P) / Shortsword d20+5 (1d6+2 P)
         Bandit ×3 (Fighter 1)         | HP 14 | AC 14 | Various weapons d20+4 (1d6+2)
Mounted: All begin mounted (+1 AC, higher ground)
Terrain : Trading post courtyard — use ASCII combat map
XP      : 22+14+14+14 = 64 base XP, ×4 encounters modifier = 150 XP
Loot    : 47 gp, 3 Composite Shortbows, Leather Armor ×4, Written Demand (references Stag Lord)
⛔ FIRE AUTO-LOOT BLOCK NOW — no player prompt needed (KM_P2.txt § AUTO-LOOT)
⛔ HERO POINT: creative tactic / talk-down / improvised weapon?
```

**Surrender option:** When 2 of 4 bandits are down, survivors may surrender. Happs (if alive): gives Kressle's Thorn River camp directions + Stag Lord fort location. +25 XP. Svetlana's ring is at Thorn River camp in a chest — not on Happs.

> *After the fight, Oleg crosses the courtyard and hands the player a bag of coin.*
> **Oleg:** *"First of the season's payment. Consider it a retainer. There'll be more when you bring me the Stag Lord's head."*

---

## 🗺️ PHASE 3 — EXPLORATION BEGINS

### The Remus Encounter (triggers when leaving Oleg's)

> *An old man sits by the road, muttering to himself. His eyes are unfocused. He might be mad. He might be something else.*

**Remus:** *"Your rival... gnome... funny little gnome... looking for old things in old places. Tomb. Ancient place, south of here. He doesn't know what he'll find there. Neither do you."*

- Player may end the conversation neutrally (no alignment flag) or kill him (Chaotic Evil flag, -10 XP, Amiri approves).
- **Ancient Tomb location revealed.** `remus_encountered = TRUE`
- XP: +20

**Player choice after Remus: Two valid opening paths:**

```
PATH A: Go to Ancient Tomb first (A Bitter Rival → Stolen Land)
  → Encounter Tartuccio with the companions he took
  → Diplomacy DC 10 to recruit 2 of your old companions back
  → Tartuccio flees; fight his mercenaries (4 enemies, ~Level 2 difficulty)
  → Track Tartuccio (storybook, Nature DC 11)
  → Find him at Pine Patch as "Tartuk the kobold shaman"
  → He flees again to Old Sycamore Caves

PATH B: Go to Thorn Ford first (Stolen Land → A Bitter Rival)
  → Encounter Kressle, get Svetlana's Ring, update the quest
  → When you later reach Ancient Tomb: companions already gone with Tartuccio
  → No companion-rescue opportunity at the tomb
  → Akiros Ismort is also at Thorn Ford in this path (early contact)
```

**DM: Track this as `ch1_opening_path = tomb_first OR thorn_first`** — it affects encounter states.

---

## ⚔️ PHASE 4A — ANCIENT TOMB (if Tomb first)

```
[GM SCENE BRIEF — Ancient Tomb]
LOCATION   : HEX (0,-1), southwest of Oleg's (1 day travel)
ENEMIES    : Tartuccio's Mercenaries ×4 (after Tartuccio flees)
             Fighter 3 ×1, Fighter 2 ×2, Wizard 2 ×1
COMPANION  : 2 of Tartuccio's five seekers (DM picks from current roster)
             Diplomacy DC 10 to flip two seekers to your side before combat
LOOT       : Longsword +1, Heavy Shield, Scale Mail, scrolls (2×Magic Missile, 1×Burning Hands)
             Ancient Cyclopean Coin (Storyteller quest item — keep for later), 45 gp
TRIGGER    : Storybook event on exit — track Tartuccio (Nature DC 11 → Pine Patch)
[END BRIEF]
```

**Tartuccio encounter:**

> *He stands over a kneeling kobold, gesturing theatrically. The seekers from the jail flank him — they look uncomfortable.*

**Tartuccio:** *"Ah. You found me. Faster than I expected, honestly. I'm almost impressed. Almost."*

*He glances at the companion beside him, then back at you.*

**Tartuccio:** *"They're staying with me. We have an arrangement. But — feel free to ask them yourself. I'm confident in their loyalty."*

**Player may attempt Diplomacy DC 10 to flip two seekers:**
- Success: Two seekers peel away. *"He's been horrible to work with, if I'm being honest."* / *"Yeah, we're done here."* Both join. Tartuccio flees with remaining three + mercenaries.
- Failure: All seekers stay. Fight 4 mercenaries. Seekers are NOT enemies — incapacitated after, join at 1 HP.

**Mercenary stat blocks:**
```
Fighter 3 (leader): HP 30 | AC 18 (chainmail) | Longsword d20+7 (1d8+4) | Shield Block
Fighter 2 ×2     : HP 22 | AC 16 (scale mail) | Longsword d20+5 (1d8+3)
Wizard 2          : HP 16 | AC 13 | Crossbow d20+4 (1d8) | Spells: Burning Hands, Magic Missile
```

**After combat:** Explore tomb freely. Storybook event triggers on exit.

**Storybook — Tracking Tartuccio:**
```
Page 1: Continue tracking? [Nature DC 11 — 22 XP] or give up (return to Oleg's)
Page 2: Trail splits. Options:
  → [Detect Magic]: Illusion magic on one trail — follow single footprints DOWN into gully ✓
  → Follow path beside gully: Ambush by kobolds (5 enemies) — lose the trail
  → Other options: XP rewards but no new info
Page 3: [Mobility/Acrobatics DC 11 — 9 XP] or give up
  → Success: Emerge at Pine Patch. Find Tartuccio as "Tartuk the Kobold Shaman."
```

**Pine Patch — Tartuccio as Tartuk:**

> *A gnome. Wearing kobold paint, kobold jewelry, carrying a carved kobold-style staff. Speaking in broken Common to a half-dozen kobolds who regard him with awe. He has sold himself as a prophet.*

> *He sees you. He does not look surprised.*

**Tartuccio:** *"You tracked me. Color me impressed. But you're too late — these fine people have already accepted me as their spiritual guide. You'd be unwise to cause a scene."*

`tartuccio_as_tartuk_revealed = TRUE` — this flag matters for Old Sycamore

Kobolds attack if combat starts. Tartuccio casts Fireball (hits everyone including kobolds). Tartuccio flees regardless — unkillable protocol active.

---

## ⚔️ PHASE 4B — THORN FORD / BANDIT CAMP (if Thorn Ford first)

```
[GM SCENE BRIEF — Thorn Ford]
LOCATION   : HEX (3,-1) — see KM_Map.md for full Kressle profile
ENEMIES    : Kressle (Rogue 3) + 8 Bandits
SPECIAL NPC: Akiros Ismort (appears HERE if Thorn Ford visited first)
LOOT       : Svetlana's Wedding Ring, 127 gp, Masterwork Shortsword,
             Written Order (updates Stolen Land quest, reveals Stag Lord is real)
LOOT (Kressle's body, if killed): Studded Leather +1 (AC+4), Shortswords ×2 (1d6 P, Agile),
             Potion of Cure Light Wounds, 45 gp
LOOT (bandit camp chest, Thievery DC 12): Composite Shortbow (1d8 P, range 60 ft),
             Leather Armor ×3, 38 gp, Fangberries ×4 (Bokken quest item — worth 25% discount)
LOOT (hidden cache, Perception DC 16): Cloak of Resistance +1, 22 gp
[END BRIEF]
```

**Akiros Ismort (if Thorn Ford first):**

> *A tall man in battered plate armor stands slightly apart from the bandits. He's watching you arrive with the expression of someone doing arithmetic.*

**Akiros:** *"You're from Restov. Charter holders. You're here to clean this up."* — *Not a question.*

He will not fight for Kressle. He watches. If the player wins, he gives information freely: *"The Stag Lord is drunk more often than not. His father is imprisoned in the fort basement. Akiros himself is... reconsidering his employment."*

**Diplomacy DC 23 OR Lore (Religion) DC 18 to turn Akiros:**
- Success: He will open a gate for you at the Stag Lord's Fort (unlocks a stealthy entry option)
- `akiros_turned = TRUE`

**Kressle — resolution options:**
```
1. Fight immediately — combat (Kressle is dangerous, flanking with bandits)
2. Diplomacy DC 16 + 500+ gp offer → She steps aside, gives Svetlana's ring
   [Good] option: Bandits leave, but Kressle and her men show up LATER to help at Stag Lord's Fort
3. Intimidation DC 18 → Bandits scatter, Kressle alone — easier fight (1v1 or surrender)
```

**Kressle stat block:**
```
KRESSLE — Half-elf Rogue 3 (Thief Racket)
HP: 36 | AC: 19 (Studded Leather + Dex) | Speed: 30 ft
Fort +4 | Ref +9 | Will +3
Shortsword ×2: d20+7/+3 (1d6+4 P, Agile/Finesse) — Sneak Attack +2d6
Evasion: On Ref success vs AOE, take no damage
Special: Will surrender if below 8 HP and offered terms
```

---

## 📍 PHASE 4C — TECHNIC LEAGUE ENCAMPMENT (Optional, any order)

```
LOCATION : Eastern Greenbelt hex
ENEMIES  : Technic League Guards ×4 (Fighter 2, HP 28, AC 17, d20+6 1d6+3 S)
           Technic League Arcanist ×1 (Wizard 3, HP 22, AC 14, Shocking Grasp d20+7 2d12)
PRISONERS: Octavia and Regongar — caged, wounded
LOOT     : Cage key (on arcanist), 45 gp, Scroll of Haste, Collar of Compliance
```

After freeing them — **Octavia:** *"Octavia. This is Regongar. We owe you one."*

```
1. "Join us."            → Build prompt: Octavia (Wizard), then Regongar (Magus). Both join.
2. "What can you do?"    → Brief exchange. Same result as 1.
3. "I'll think about it" → Capital fallback triggers at next throne room visit.
4. [Destroy the Collar]  → Octavia +1 Relationship. Both join. Build prompts fire.
```

**Capital Fallback:** Octavia and Regongar approach at throne room.
```
1. "Welcome."       → Build prompts fire. Both join.
2. "Not right now." → Re-approachable next visit.
3. "No."            → Gone permanently.
```

---

## 📍 PHASE 5 — OLD SYCAMORE (Kobold/Mite War + Tartuccio)

```
[GM SCENE BRIEF — Old Sycamore]
LOCATION   : HEX (-1,0)
MEETING    : Kesten Garess arrives at Old Sycamore entrance (if not already at Oleg's)
             He does NOT reveal Tartuccio's identity — player discovers via journal
ENEMIES    : Surface — Mites and Kobolds skirmishing
             Underground — Mites (Upper), Kobolds (Lower), Tartuccio (Deepest)
COMPANIONS : Seekers from Tartuccio's team locked in kobold cage — rescue them
FLAG CHECK : tartuccio_as_tartuk_revealed — if TRUE, player already knows.
             Kesten does NOT confirm spy status. See KM_P2.txt § TARTUCCIO SPY STATUS.
[END BRIEF]
```

**Kobold/Mite conflict — Resolution options:**

```
SURFACE:
  1. Attack all    — fight both factions, no alliance
  2. Side with Kobolds (talk to Chief Sootscale) — kobolds help clear mites
  3. Side with Mites (talk to Queen Bdaah)       — mites help clear kobolds
  4. [Neutral only] Offer to investigate         — +XP, both factions neutral until you choose

UNDERGROUND NAVIGATION:
  Need: Mites' Relic (from Chief Sootscale via dialogue, or from Queen Bdaah's corpse)
  Upper: Mite lair — spiders, mites, traps (Thievery DC varies 12–18)
  Lower: Kobold warren — kobolds, Chief Sootscale's chamber
  Deepest: Tartuccio's sanctum (requires Mites' Relic to open)
```

**Rescuing seekers from kobold cage:**
- Found in kobold warren level, northwestern area
- Locked cage: Thievery DC 14 or Force Open Athletics DC 16
- Seekers released: rejoin at player's level (see KM_Prologue_Systems.md leveling)
- Diplomacy/Intimidation DC varies based on current kobold faction alignment

**Tartuccio — Final Confrontation (Ch1):**

```
[GM SCENE BRIEF — Tartuccio's Sanctum]
TARTUCCIO casts Fireball as his first action — hits ALL creatures in the room including kobolds.
  Fireball: 6d6 fire, Reflex DC 15 half
  Companions and player must save. Kobold allies likely die.
After Fireball: Tartuccio fights with his mercenary guards.
  Stats: HP 16 | AC 17 | Rapier d20+5 (1d6+2) | Spells: Fireball (used), Scorching Ray, Shield
  He surrenders at 0 HP but is NOT killed here — Unkillable Protocol applies.
  If player kills him: Tier 1 applies (not actually dead). He escapes before Ch2.

LOOT: Mites' Relic (story item), Token of the Dryad (Relic Fragment — keep for Storyteller),
      Tartuccio's journal (confirms he is a Pitax agent, names his contact), 180 gp
```

**After Tartuccio is defeated:** Return to Oleg's. Kesten pays 1,000 gp reward + 480 XP for completing A Bitter Rival.

---

## 📍 PHASE 6 — TEMPLE OF THE ELK

```
[GM SCENE BRIEF — Temple of the Elk]
LOCATION   : HEX (0,1) — north, near future capital site
ENEMIES    : Guardian of the Bloom (Maddened Bear — actually cursed priest Devlin)
             Primal Giant Frogs ×3 (entrance area, CR 2 each)
             The Fog: sickens all living creatures inside (−1 Sickened ongoing)
                     Clears when all enemies defeated and pool cleansed
NPC        : Tristian (found inside, fighting bear — wounded)
QUEST      : Jhod Kavken's errand — clear the temple
LOOT       : From bear/altar area (Perception DC 13): Amulet of Natural Armor +1, 55 gp
             From pool (Perception DC 15 after fog clears): Everburning Torch, Scroll of Heal (L2)
             From frog bodies: Frog Legs ×6 (Camp ingredient — Survival check vs DC 14 for fresh meat)
[END BRIEF]
```

**Guardian of the Bloom:**
```
Maddened Bear (actually Devlin, cursed priest of Erastil)
HP: 55 | AC: 18 | Speed: 35 ft
Jaws: d20+9 (2d8+6 P) | Claw: d20+9 (1d10+6 S, Agile)
Special: Grab on Jaws hit — target Grabbed on success
         Rend — if both Claw attacks hit same target: +2d10+6 automatic damage
Fort +11 | Ref +6 | Will +5
XP: 320
```

**The Fog:** While inside the temple and fog is active, all living creatures (not undead — Jaethal is immune) gain Sickened 1 at the start of each round. Cleared when bear defeated + pool investigated.

**Tristian encounter:**
> *A young man in white robes, bleeding from a slash across his arm, is trying to draw the bear's attention away from you. He is failing. He looks up.*
> **Tristian:** *"Oh thank the Dawnflower — I wasn't sure anyone would come."*

After fight: Tristian offers to join. He is available as a party member now regardless of prologue split.

**If player accepts:** Run build assignment prompt (Cleric builds — KM_Builds_Champ_Cleric.md) before continuing.
**If player declines:** Tristian travels to the Capital. Approaches player at throne room — Accept/Decline/Ask scene. On Accept: build prompt fires then.
**Flag:** `tristian_recruited = TRUE` | `tristian_build = [chosen]`

**Temple reward:** Jhod Kavken consecrates the temple. Grants free Treat Wounds (DC 20 = 2d8+10) once per day for entire party. `temple_elk_cleared = TRUE`

---

> **➡️ PHASE 7 (Stag Lord's Fort), PHASE 8 (Return to Oleg's & Kingdom Founding), CHAPTER 1 XP SUMMARY, and CHAPTER 1 RESOLUTION PATHS — see `KM_Ch1_B.md`.**

> **⚠️ DM: Chapter 1 ends when the player returns to Oleg's Trading Post after defeating the Stag Lord AND triggers the Kingdom Founding sequence. Output the Ch1 Export Block at this point. Full late-chapter content is in KM_Ch1_B.md.**

---

*KM_Ch1.md — Kingmaker PF2e Text Adventure | Ch1 v2.0 (split — pair-load with KM_Ch1_B.md)*


---

<!-- merged from KM_Ch1_B.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 1: STOLEN LAND (PART B)
## KM_Ch1_B.md | Pair-load with KM_Ch1.md
## Covers Phases 7–8 + XP Summary + Resolution Paths.

> **DM:** This is Part B of Chapter 1. Always pair-load with `KM_Ch1.md` (Part A covers the load checklist, overview, opening scene, and Phases 1–6: Oleg's, the bandit encounter, exploration, the Tomb, Thorn Ford, the Technic League encampment, Old Sycamore, and the Temple of the Elk).

---

## 📍 PHASE 7 — THE STAG LORD'S FORT

### Pre-Assault Preparation

**Available approaches (see KM_Map.md for full fort detail):**

```
A. Direct assault              — Hard. Full garrison alert from round 1.
B. Kressle's password          — Reduces garrison by 2, patrol timing known.
                                  Requires: Kressle fought + retrieved info from her camp.
C. Disguise as bandits         — Deception DC 16. Fails if Stag Lord sees player directly.
D. Basement/sewer entry        — Thievery DC 14 to locate hidden entry. Bypasses main gate.
E. Akiros opens a gate         — Requires akiros_turned = TRUE from Thorn Ford visit.
                                  He opens the east gate at midnight on Day [X].
F. Kressle's crew assists      — Requires [Good] resolution at Thorn Ford.
                                  Her bandits attack from outside while player goes in.
```

**Fort Layout:**
```
╔══════════════════════════════════════════════╗
║  STAG LORD'S FORT                            ║
╠══════════════════════════════════════════════╣
║  [Watch Tower]  [Watch Tower]                ║
║  N Gate ──────────────────────               ║
║  │  [Barracks]  [Barracks]  [Main Hall]  │   ║
║  │  Bandits ×6  Bandits ×4  Dovan+Auchs  │   ║
║  │                                       │   ║
║  │  [Stag Lord's Tower — top floor]      │   ║
║  │  [Basement — Nugrah's Prison]         │   ║
║  E Gate ──── (Akiros if turned) ─────────    ║
╚══════════════════════════════════════════════╝
```

**Key NPCs:**

**DOVAN (Rogue 5 — sadistic lieutenant):**
```
HP: 48 | AC: 20 | Speed: 30 ft
Daggers ×2: d20+10/+6 (1d4+5 P, Agile) — Sneak Attack +3d6
Cannot be talked down. Will not surrender. Fight or die.
```

**AUCHS (Fighter 4 — dimwitted brute):**
```
HP: 60 | AC: 17 (Chain Shirt) | Greatclub: d20+10 (2d6+8 B)
Special: Can be turned against Dovan.
  Diplomacy DC 14 if approached alone: "Dovan hurts people for fun. I don't like it."
  If turned: Fights Dovan during the assault. Player gains +ally for that fight.
```

**AKIROS ISMORT (Fighter 5 — fallen paladin):**
```
HP: 66 | AC: 22 (Full Plate) | Longsword: d20+10 (1d8+5 S)
If akiros_turned = TRUE: He does not fight the player. Joins assault on Stag Lord.
If NOT turned: He fights the player unless [Lore Religion DC 18] or [Diplomacy DC 23].
```

**NUGRAH (basement — Stag Lord's imprisoned father):**
```
Old druid, mad from years of imprisonment. Not hostile by default.
Releasing him: Diplomacy DC 12 to calm him. He gives a blessing (+1 to all saves, 1 day).
Leaving him: He escapes later on his own. No consequence.
XP for releasing: +25
```

### THE STAG LORD

```
THE STAG LORD — Ranger 7 (Outwit Hunter)
HP: 94 | AC: 21 (Leather Armor +2 + Dex) | Speed: 30 ft
Fort +12 | Ref +14 | Will +9

WEAPONS:
  Composite Longbow +2: d20+16 (1d8+7 P, range 100 ft) — his primary weapon
    Rapid Shot: Two arrows per action, each at −2 to hit
  Shortsword: d20+11 (1d6+5 P) — backup if engaged in melee

SPECIAL ABILITIES:
  Hunt Prey: Designate 1 target — +2 to Perception vs target, ignore first MAP penalty
  Masterful Hunter: +2d8 damage vs Hunted Prey
  Drunk but Deadly: If not surprised, −2 to Will saves but +2 to damage (ale in system)
  Stag's Helm: +2 to Intimidation, Fear aura 10 ft (Will DC 16 or Frightened 1)

TACTICS:
  Round 1: Hunt Prey on player character → Triple attack (Longbow −2/−7/−12)
  Round 2: Maintain range. Use difficult terrain. Shout for reinforcements if any remain.
  Round 3+: Switch to melee if cornered. His shortsword is his worst weapon — this is his mistake.

DEFEAT CONDITIONS:
  Reduced to 0 HP → unconscious (not dead)
  Hero Point? No — he's an enemy. He stays down.

DISPOSAL OPTIONS (see KM.txt Game Options):
  Kill immediately     : Standard
  Behead + send head   : +75 gp reward from Jamandi, Aldori commendation
  Capture + imprison   : Interrogation possible (reveals Nyrissa's early influence — +lore)
  Turn over to Kesten  : He arrives in 1d4 days
  Execute publicly     : +5 Loyalty to future kingdom, alignment flag (+Evil tendency)

XP: 600 (boss encounter)
```

**FORT LOOT (collect before leaving):**
```
From Stag Lord     : Stag Lord's Helm, Composite Longbow +2, +1 Leather Armor
                     Potion of Cure Moderate Wounds ×3, 230 gp
                     Letter from Nyrissa (story item — first contact, keep this)
From Dovan         : Daggers +1 ×2, 85 gp
From Akiros (if killed): Full Plate +1, Longsword +1
Fort treasury      : 340 gp (Stag Lord's accumulated tribute)
Secret room        : Thievery DC 16 — Headband of Inspired Wisdom +2, 95 gp
```

> ⚠️ **DM: Remind player to collect all loot before triggering the "victory" scene. Cannot return.**

---

## 📍 PHASE 8 — RETURN TO OLEG'S & KINGDOM FOUNDING

### Victory Scene

> *The Stag Lord is [dead/captured/beheaded]. The fort is yours. The Stolen Lands are — technically — clear.*
>
> *Linzi (or whoever is in party) opens her notebook.*
> **Linzi:** *"Chapter [X]: 'The Stag Lord Falls.' Has a good ring to it."*
> **Amiri:** *"Acceptable. I've fought better. But acceptable."*

**Nettle's Crossing (if applicable):**
If player has the Stag Lord's head/body, travel to Nettle's Crossing on the way back.
Davik Nettles' ghost accepts the offered remains → reward: **Ranseur +1** (1d10+5 S/P, Reach 10 ft, Trip, +1 item bonus to attack and damage), +50 XP.

### Bokken's Hut (optional search, Hex (-1,1))
Searchable if relationship positive (Fangberries/Radishes delivered).
```
Bokken's Hut (Perc DC 14, he's outside during day):
  Shelf: Antiplague, Oil of Potency (+1 spell DC, 1d4 charges)
  Cabinet (Thiev DC 15): Potion of Darkvision, 28 gp, Scroll of Grease
  Caught searching: −1 Bokken, full price permanent, no Fangberry discount
```

### Abandoned Hut (random exploration, Plains hexes)
```
Plains hex, Perc DC 12 during travel. Interior (Perc DC 14):
  Floorboard: 32 gp, Healer's Kit (10 uses), Masterwork Dagger (1d4+Str P, Agile)
  Back room       : Rotted bedroll, Torn Journal (lore — former settler, not mechanical)
  Trap (Thievery DC 13 to spot): Tripwire attached to crossbow. Reflex DC 14 or 1d8+3 P damage.
```

### At Oleg's — Kingdom Founding

**Kesten Garess and Jhod Kavken are both present.**

> *A messenger from Restov arrived two days ago. He left a sealed document and a note that says: "When you're ready."*

The sealed document is Jamandi's official Kingdom Charter. Opening it begins the Kingdom Founding sequence.

**Capital Selection:** Player chooses from 3 options (see KM_Map.md — Capital section). Record `capital_location` in Export Block.

**First Kingdom Turn:** Happens immediately after capital is founded. See KM_Kingdom.md.

**Seeker recruitment (Tartuccio's team):**
If seekers from Tartuccio's team have not yet been flipped, they can be recruited at Oleg's post-founding. They left Tartuccio after his behavior in the Stolen Lands. Level matches player per KM_Prologue_Systems.md.

---

## 📊 CHAPTER 1 — XP SUMMARY

| Source | XP |
|--------|----|
| Thylacine ambush (3) | 90 |
| Bandit raid at Oleg's | 150 |
| Remus encounter | 20 |
| Ancient Tomb — mercenaries (4) | 180 |
| Ancient Tomb — storybook tracking | 55 |
| Thorn Ford — Kressle + bandits | 200 |
| Temple of the Elk — bear + frogs | 380 |
| Old Sycamore — mites/kobolds | 320 |
| Tartuccio confrontation (Ch1) | 240 |
| A Bitter Rival completion | 480 |
| Stag Lord's Fort — Dovan + Auchs | 280 |
| Stag Lord (boss) | 600 |
| Falgrim Sneeg (capture) | 150 |
| Lonely Warrior (resolved) | 150 |
| Side quests (Fangberry, Radishes, etc.) | ~150 |
| Exploration discoveries | ~200 |
| **Total (full completion)** | **~3,645 XP** |
| **Minimum (main quests only)** | **~2,100 XP** |

**Level benchmarks:** L2 at 1,000 | L3 at 2,000 | L4 at 3,000 | L5 at 4,000 (per KM_BuildGuide.md)

---

## 🔀 CHAPTER 1 RESOLUTION PATHS

### PATH A — SWIFT CONQUEST (under 30 days)
Mainline only. No diversions. Reward: Lord Protector (+2 Dueling Sword, Finesse) from Jamandi. Consequence: side quests incomplete, may be Level 3 only at chapter end.

### PATH B — FULL EXPLORATION (30–60 days)
All named hexes cleared, all Ch1 quests complete. Level 4 at chapter end. Best starting position for Ch2.

### PATH C — DIPLOMATIC RESOLUTION
Kressle turned, Akiros recruited, Sootscale allied, fey approached peacefully. Reward: +2 Stability to starting kingdom, Akiros available as Warden advisor.

### PATH D — MILITARY DOMINATION
Kressle killed, Akiros fought, kobolds wiped out, fey glade forcibly claimed. −Stability, +Economy. Jaethal approves. Valerie disapproves.

### PATH E — STAG LORD CAPTURED
Interrogation confirms Nyrissa's letter as real. `nyrissa_early_contact = TRUE`. Player decides his fate (Kesten, execute, imprison).

---

> **⚠️ DM: Chapter 1 ends when the player returns to Oleg's Trading Post after defeating the Stag Lord AND triggers the Kingdom Founding sequence. Output the Ch1 Export Block at this point.**

---

*KM_Ch1_B.md — Kingmaker PF2e Text Adventure | Ch1 Part B v1.0*


---

<!-- merged from KM_Ch1_Export.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 1 EXPORT & CHAPTER 2 LOAD
## KM_Ch1_Export.md | Transition: Ch1 → Ch2

---

## ⚠️ DM INSTRUCTION — WHEN TO OUTPUT THIS

### ⛔ HARD STOP — DO NOT BEGIN CHAPTER 2 UNTIL THIS BLOCK IS OUTPUT AND SAVED

Output this block when ALL of the following are true:
1. The Stag Lord has been defeated (any method)
2. The player has returned to Oleg's Trading Post
3. The Kingdom Founding sequence has triggered
4. The player has selected their capital location

**Before any Chapter 2 content — before troll raid reports, before road travel, before any scene outside Oleg's post-founding — output this block.**

Say exactly: *"Chapter 1 is complete. Copy everything between the markers below and save it. You will paste this into your Chapter 2 session."*

**Then immediately: Run the Best Run scoring per KM_PlayerHelp.md.** Compare against stored best. If new record → display full scorecard + auto-output Best Run block with paste instructions. If not a record → one line: *"Run score: X/200. Your best: Y/200."* No block, no scorecard.

Then say: *"Type `.continue` when saved."*
Wait for `.continue`.

**VIOLATION:** Any Chapter 2 content written before this block is output and confirmed = `.fail 16` + unrecoverable save data loss.

---

## ⛔ PRE-EXPORT AUDIT — OUTPUT THIS BEFORE THE SAVE BLOCK

> **⛔ DM: Fill and output this audit FIRST. Save block without preceding audit = `.fail 9`.**

```
SAVE BLOCK AUDIT — fill from session, not from template defaults:

□ HP: __/__ (final battle, not reset) | XP: ____ | Gold: __ gp | Hero Points: __ (don't reset)
□ Conditions: [active or "none"] | Inventory: __ weapons, __ armor, __ consumables, __ gear, __ quest items
□ Story flags changed: [flag: old→new] for every flag that changed — min 3 if events occurred
□ Companion relationship changes: [name: X→Y] for each that moved | HP filled for all active
□ Companion memory[]: filled for every companion spoken to — empty memory = session erased
□ NPC threads: thread + memory[] for every NPC spoken to — not filled = that NPC reset on reload
□ Kingdom stats: culture/economy/loyalty/stability all filled if kingdom turn ran — not 0
□ Zero-check: no numeric field reads 0 unless it was genuinely 0 in play
□ Field count: story_flags = 12 top-level sections | companions = entry for every active + bench companion
⛔ NEVER REMOVE: kingdom · hexes · npc_threads · nyrissa · world_state · ending_flags · carried_from_prologue · companion_quests · alignment_track · player.skills · player.speed · player.perception · player.class_features

All confirmed → output save block.
```

---

## 📤 FILL AND OUTPUT THIS BLOCK

````json
{
  "save_version": "1.0",
  "export_from": "chapter_1",
  "import_to": "chapter_2",
  "export_date_ingame": "",
  "days_elapsed_ch1": 0,
  "ch1_speed_bonus": false,

  "player": {
    "name": "",
    "build_id": "",
    "ancestry": "",
    "class": "",
    "subclass": "",
    "background": "",
    "level": 0,
    "xp": 0,
    "xp_to_next": 0,
    "attributes": {
      "str": 0, "dex": 0, "con": 0,
      "int": 0, "wis": 0, "cha": 0
    },
    "hp_current": 0,
    "hp_max": 0,
    "hero_points": 1,
    "ac": 0,
    "speed": 0,
    "perception": 0,
    "saves": { "fort": 0, "ref": 0, "will": 0 },
    "conditions": [],
    "skills": {},
    "feats": [],
    "spells": {
      "tradition": "",
      "spell_dc": 0,
      "spell_attack": 0,
      "cantrips": [],
      "slots": {},
      "focus_points": { "current": 0, "max": 0 },
      "focus_spells": []
    },
    "class_features": [],
    "inventory": {
      "weapons": [],
      "armor": [],
      "shields": [],
      "magic_items": [],
      "consumables": [],
      "gear": [],
      "quest_items": []
    },
    "gold": { "gp": 0, "sp": 0, "cp": 0 },
    "bulk_carried": 0
  },

  "companions": [
    {
      "name": "Amiri",
      "status": "active_party",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "ac": 0,
      "hero_points": 1,
      "relationship": "Friendly",
      "conditions": [],
      "equipped_items": [],
      "notes": "", "thread": "", "priorities": []
    },
    {
      "name": "",
      "status": "active_party",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "ac": 0,
      "hero_points": 1,
      "relationship": "Neutral",
      "conditions": [],
      "equipped_items": [],
      "notes": "", "thread": "", "priorities": []
    },
    {
      "name": "",
      "status": "active_party",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "ac": 0,
      "hero_points": 1,
      "relationship": "Neutral",
      "conditions": [],
      "equipped_items": [],
      "notes": "", "thread": "", "priorities": []
    },
    {
      "name": "Tristian",
      "status": "available_at_base",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "relationship": "Friendly",
      "notes": "Recruited at Temple of the Elk if player visited. Waiting at Oleg's/Capital."
    }
  ],

  "kingdom": {
    "name": "",
    "capital_location": "",
    "capital_coords": [0, 0],
    "founded_date": "",
    "turn": 1,
    "size": 1,
    "culture": 0,
    "economy": 0,
    "loyalty": 0,
    "stability": 0,
    "unrest": 0,
    "fame": 0,
    "infamy": 0,
    "treasury_rp": 0,
    "consumption": 0,
    "leadership_roles": {
      "ruler": "",
      "councilor": "",
      "general": "",
      "grand_diplomat": "",
      "high_priest": "",
      "magister": "",
      "marshal": "",
      "royal_enforcer": "",
      "spymaster": "",
      "treasurer": "",
      "warden": ""
    },
    "settlements": [
      {
        "name": "",
        "coords": [0, 0],
        "size": "Village",
        "population": 0,
        "buildings": [],
        "defense_ac": 15,
        "defense_hp": 20,
        "morale": 50
      }
    ]
  },

  "hexes": [
    {
      "coords": [1, 0],
      "name": "Oleg's Trading Post",
      "status": "controlled",
      "cleared": true,
      "scripted_encounter_done": true,
      "notes": "Kesten Garess stationed here. Oleg/Svetlana vendors active."
    }
  ],

  "story_flags": {

    "carried_from_prologue": {
      "gate_entry": "",
      "malak_bribe_evidence": false,
      "parchment_source": "pitax",
      "malak_arrested": false,
      "malak_broke_first": false,
      "malak_found_letter_himself": false,
      "kesten_searched_malak": false,
      "player_clean_hands": false,
      "second_hero_witnessed": false,
      "malak_deal_made": false,
      "tartuccio_knows_player_is_aware": false,
      "rebuttal_result": "",
      "kassil_first_impression": "neutral",
      "kesten_respect": false,
      "arrived_with_kassil": false,
      "prison_arc": false,
      "harrim_chaotic_bond": false,
      "tartuccio_ring": "",
      "tartuccio_gold": ""
    },

    "chapter_1": {
      "ch1_opening_path": "",
      "days_elapsed": 0,
      "speed_bonus_earned": false,
      "stag_lord_fate": "",
      "stag_lord_head_sent_to_jamandi": false,
      "nyrissa_letter_found": false,
      "nyrissa_early_contact": false,

      "ancient_tomb": {
        "visited": false,
        "companion_recruited_back": false,
        "companion_name": "",
        "tomb_explored": false
      },

      "thorn_ford": {
        "visited": false,
        "kressle_fate": "",
        "akiros_turned": false,
        "svetlana_ring_recovered": false
      },

      "temple_elk": {
        "cleared": false,
        "tristian_recruited": false,
        "jhod_settled": false
      },

      "old_sycamore": {
        "visited": false,
        "kobold_resolution": "",
        "mite_resolution": "",
        "tartuccio_confronted_ch1": false,
        "tartuccio_journal_found": false,
        "sootscale_alliance": false,
        "companions_rescued_from_cage": false
      },

      "stag_lords_fort": {
        "entry_method": "",
        "dovan_fate": "",
        "auchs_fate": "",
        "akiros_fate": "",
        "nugrah_released": false,
        "kressle_assisted": false
      },

      "side_quests": {
        "bandits_at_olegs": false,
        "oleg_expanded": false,
        "svetlana_ring_returned": false,
        "falgrim_sneeg": "",
        "fangberries_delivered": false,
        "moon_radishes_delivered": false,
        "scythe_tree_defeated": false,
        "tiressia_met": false,
        "nettles_crossing_resolved": false,
        "bokken_relationship": "neutral",
        "jubilost_helped": false,
        "old_beldame_met": false,
        "tuskgutter_killed": false,
        "kingdom_founded": false,
        "storyteller_available": false
      }
    },

    "tartuccio": {
      "tartuccio_as_tartuk_revealed": false,
      "tartuccio_journal_contents_known": false,
      "tartuccio_location_ch2": "fled_greenbelt",
      "tartuccio_contact_named": false
    },

    "companions": {
      "tristian_recruited": false,
      "nok_nok_available": false,
      "lem_available": false,
      "ekundayo_recruited": false,
      "prologue_companions_recovered": []
    },

    "companion_quests": {
      "amiri_quest": "inactive",
      "amiri_quest_stage": 1,
      "linzi_quest": "inactive",
      "valerie_quest": "inactive",
      "harrim_quest": "inactive",
      "tristian_quest": "inactive",
      "tristian_betrayal_revealed": false,
      "jaethal_quest": "inactive",
      "octavia_quest": "inactive",
      "regongar_quest": "inactive",
      "noknok_quest": "inactive",
      "lem_quest": "inactive",
      "ekundayo_quest": "inactive",
      "kalikke_kanerah_quest": "inactive"
    },

    "storyteller": {
      "storyteller_available": false,
      "fragments_delivered": 0,
      "coins_delivered": 0,
      "storyteller_collection": "incomplete"
    },

    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "notable_choices": []
    },

    "relationships": {
      "jamandi": "neutral",
      "kassil": "neutral",
      "kesten": "neutral",
      "oleg": "neutral",
      "svetlana": "neutral",
      "jhod": "neutral",
      "akiros": "neutral",
      "kressle": "neutral",
      "sootscale": "neutral"
    },

    "promises_and_debts": [],

    "npc_threads": {
      "Amiri":    { "thread": "", "priorities": [] },
      "Linzi":    { "thread": "", "priorities": [] },
      "Valerie":  { "thread": "", "priorities": [] },
      "Harrim":   { "thread": "", "priorities": [] },
      "Jaethal":  { "thread": "", "priorities": [] },
      "Tristian": { "thread": "", "priorities": [] },
      "Kesten":   { "thread": "", "priorities": [] },
      "Oleg":     { "thread": "", "priorities": [] },
      "Svetlana": { "thread": "", "priorities": [] },
      "Jhod":     { "thread": "", "priorities": [] },
      "Akiros":   { "thread": "", "priorities": [] },
      "Jamandi":  { "thread": "", "priorities": [] }
    },

    "world_state": {
      "stag_lord_defeated": true,
      "stolen_lands_claimed": true,
      "kingdom_founded": true,
      "brevoy_notified": false,
      "maegar_varn_competing": false,
      "time_limit_missed": false,
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    },

    "nyrissa": {
      "nyrissa_awareness": "passive",
      "nyrissa_backstory_known": false,
      "nyrissa_backstory_partial": false,
      "nyrissa_can_be_saved_hint": false,
      "nyrissa_identity_known": false,
      "nyrissa_bloom_connection_known": false
    }
  },

  "romance": {
    "active_romance": "",
    "romance_score": 0,
    "romance_stage": 0,
    "romance_history": []
  },

  "brotherhood": {
    "active_bonds": [],
    "bond_scores": {},
    "fire_test_completed": []
  },

  "crime": {
    "infamy": 0,
    "active_bounties": [],
    "outstanding_fines": 0,
    "known_crimes": [],
    "witnesses_outstanding": [],
    "fugitive_regions": [],
    "trial_pending": false,
    "last_crime_chapter": null
  },

  "living_world": {
    "party_morale": 5,
    "companion_moods": {},
    "fracture_scene_pending": false
  },

  "found_documents": [],

  "companion_agendas": {},

  "companion_relations": {},

  "incompatibility_countdowns": {
    "jaethal_tristian":  {"count":0,"max":10,"stage":0,"ultimatum_fired":false},
    "jaethal_imrijka":   {"count":0,"max":6, "stage":0,"truce_active":false,"ultimatum_fired":false},
    "regongar_valerie":  {"count":0,"max":8, "stage":0,"ultimatum_fired":false},
    "harrim_tristian":   {"count":0,"max":14,"stage":0,"truce_active":false,"ultimatum_fired":false}
  },

  "npc_relations": {},

  "quest_log": {
    "completed": [
      { "name": "Stolen Land", "result": "Stag Lord defeated", "xp": 0 },
      { "name": "A Bitter Rival", "result": "", "xp": 0 }
    ],
    "active": [
      {
        "name": "Troll Trouble",
        "objective": "Reports of trolls in the Greenbelt. Investigate.",
        "notes": "Chapter 2 begins with first troll encounter near kingdom borders."
      }
    ],
    "failed_or_missed": []
  },

  "resources": {
    "camping_supplies": 0,
    "rations": 0,
    "days_into_ch2": 0,
    "current_hex": "Oleg's Trading Post / Capital"
  },

  "dispositions": { "merciful": 0, "ruthless": 0, "cunning": 0, "blunt": 0, "scholarly": 0 },
  "companion_titles": {},
  "pending_hp_loot_rolls": 0,
  "faction_tiers": { "aldori": 0, "surtova": 0, "kellid": 0, "river_kingdoms": 0, "pitax": 0 },
  "standing_orders": {},
  "adventurer_board": { "posted_bounties": [], "active_missions": [], "completed_reports": [], "guild_upgraded": false },
  "border_raids": { "pending": [], "resolved": [], "consecutive_unanswered": 0 },
  "hex_fortifications": [],
  "crafting": { "known_recipes": [], "materials": {} },
  "mobile_base": { "type": "none" },
  "stronghold_events_completed": [],
  "dream_log": [],
  "dream_cooldown": 0,
  "liminal_visits": 0,
  "liminal_choices": [],
  "scripted_interactions_completed": [],
  "debate_results": [],
  "advisor_intrigue": { "active": [], "detected": [] },
  "quest_conflicts": { "tristian_jaethal": "unresolved", "regongar_valerie": "unresolved", "amiri_ekundayo": "unresolved" },
  "ending_flags": { "nyrissa_saveable": 0, "true_ending_path": false, "golden_ending_eligible": false },
  "prestige": { "l10_choice": null, "l15_choice": null },
  "mythic_path": { "chosen": null, "abilities": [], "power_level": 0 }
}
````

---

## 📝 DM FILL GUIDE — CH1-SPECIFIC FIELDS

**`days_elapsed_ch1`** — Count travel days from Day 1 to chapter end. If ≤ 30: `ch1_speed_bonus = true` → Lord Protector sword added to inventory.

**`stag_lord_fate`** — One of: `killed`, `beheaded_head_sent`, `captured_kesten`, `captured_imprisoned`, `executed_publicly`

**`ch1_opening_path`** — One of: `tomb_first`, `thorn_first`, `neither_yet` (shouldn't happen at export)

**`kobold_resolution`** — One of: `sootscale_allied`, `mites_allied`, `both_wiped`, `neutral_departed`

**`kressle_fate`** — One of: `killed`, `turned_good`, `intimidated_fled`, `escaped`

**`akiros_fate`** — One of: `turned_ally` (in kingdom as advisor), `fought_defeated`, `killed`, `fled`

**`companions_recovered`** — List the names of prologue companions rescued from kobold cage.

**Kingdom fields:** Fill all stats from the first Kingdom Turn if it was run. If not yet run, leave at 0 and note `"turn": 0`.

**`nyrissa_letter_found`** — Only TRUE if player physically found and read the letter in the Stag Lord's Fort treasury.

**`oleg_expanded`** — Set TRUE after the first Kingdom Turn resolves. Controls which vendor table Oleg uses in Ch2. If the first kingdom turn was not run before chapter end, leave FALSE.

---

## 📥 HOW TO LOAD CHAPTER 2

**PASTE THIS at the start of your Chapter 2 chat:**

```
Loading Chapter 2 of the Pathfinder 2e Kingmaker text game.

Files: KM.txt, KM_Builds.md, KM_Actions.md, KM_BuildGuide.md
       KM_Commands.md, KM_Commands_Maps.md, KM_Commands.md
       KM_Companions.md, KM_Companions.md
       KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md
       KM_Ch2.md, KM_Ch2_P2.md

Import my Chapter 1 save below. Show Game State Header before any scene.

[PASTE YOUR CH1 JSON EXPORT HERE]
```

---

## 📋 CHAPTER 2 LOAD CHECKLIST

```
[GM CHAPTER 2 LOAD CHECK]
□ All files loaded
□ Ch1 JSON Export imported and parsed
□ Player level, XP, and inventory confirmed
□ Kingdom state confirmed — turn count, stats, capital
□ Hex map state restored — controlled/discovered hexes noted
□ Companion roster confirmed — active party + bench
□ Story flags read and noted:
    stag_lord_fate          : [value]
    nyrissa_letter_found    : [TRUE/FALSE]
    nyrissa_early_contact   : [TRUE/FALSE]
    sootscale_alliance      : [TRUE/FALSE]
    akiros_fate             : [value]
    tartuccio_location_ch2  : fled_greenbelt
    alignment_track         : [both axes]
    relationships           : [key NPCs]
□ Active quests confirmed — Troll Trouble is primary Ch2 quest
□ Kingdom turn status — is Turn 1 complete or pending?
□ Game State Header output and confirmed
□ ONLY THEN: Begin Ch2 opening
```

---

## 🗺️ CHAPTER 2 OPENING CONTEXT

**Party composition:** Player character + up to 4 companions in Vanguard (per KM_Combat_Systems.md). Can swap at Capital.

**Where the story picks up:**
- First troll sighting reports arrive at the Capital within the first kingdom turn
- Jhod Kavken brings news: something is wrong with the Greenbelt flora — plants dying abnormally
- Kesten reports a missing patrol in the southern hexes
- The Season of Bloom has not yet begun but something is stirring

**What Tartuccio is doing:**
He fled south after Ch1. His journal mentioned a contact in Pitax. He will not appear directly until the player investigates the Troll Lair area deeper in Ch2. His influence is being felt through the Season of Bloom curse seeds he planted earlier.

**What Nyrissa knows:**
If `nyrissa_letter_found = TRUE` — she knows the player read her letter. The tone of Chapter 2's supernatural events will be more overtly directed. `nyrissa_awareness = active`
If `nyrissa_letter_found = FALSE` — she is watching but has not yet made direct contact. `nyrissa_awareness = passive`

---

*KM_Ch1_Export.md — Kingmaker PF2e Text Adventure | Ch1 Export v1.0*


---

<!-- merged from KM_Ch2.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 2: TROLL TROUBLE & SEASON OF BLOOM
## KM_Ch2.md | Loads after: KM_Ch1_Export.md | Loads before: KM_Ch3.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_BuildGuide.md.
> Import Ch1 Export Block before beginning.
> Chapter 2 has TWO main questlines running in parallel:
> **Troll Trouble** (Hargulka) and **Season of Bloom** (Ancient Curse/Nyrissa).
> Both must be resolved to complete the chapter.
> See KM_Ch2_P2.md for Season of Bloom content (Phases 5–8).

---

## 📋 CH2 LOAD CHECKLIST

```
[GM CHAPTER 2 LOAD CHECK]
□ All files loaded and confirmed
□ Ch1 Export Block imported — player level, kingdom state, hex map
□ Key flags read:
    stag_lord_fate          : [value]
    nyrissa_letter_found    : [TRUE/FALSE]
    nyrissa_early_contact   : [TRUE/FALSE]
    akiros_fate             : [value — if alive: Warden role available]
    tartuccio_journal_found : [TRUE/FALSE]
    sootscale_alliance      : [TRUE/FALSE]
    companion_split         : [current active party]
□ Kingdom state confirmed — Turn [X], all stats, leadership roles
□ New companions available to recruit: Ekundayo (this chapter)
□ Kalikke/Kanerah available (DLC — confirm if active)
□ Time pressure noted: Troll Trouble has soft deadline ~90 days
□ Game State Header output and confirmed
□ ONLY THEN: Begin Ch2 opening
```

---

## 🗺️ CHAPTER 2 OVERVIEW

**Levels:** 4 → 8 (L5 mid-chapter, L7 at Hargulka, L8 at Bloom resolution)
**XP:** 1,000/level flat (PF2e Remaster). L5=4k | L6=5k | L7=6k | L8=7k cumulative
**Duration:** ~60–90 in-game days across both questlines
**New regions:** Narlmarches (Troll territories), Kamelands, Dire Narlmarches

**Two parallel questlines:**
- **Troll Trouble** — Hargulka is building a troll kingdom. His raids threaten your borders. Find Trobold, confront Hargulka and Tartuccio/Tartuk.
- **Season of Bloom** — An Ancient Curse is manifesting. Plants die. Monsters transform. Tristian's secret begins to surface. Nyrissa's hand becomes visible.

**Key decisions:**
- Kill Hargulka or make him vassal (affects Ekundayo permanently)
- Expose/confront Tartuccio in Trobold (his Ch2 fate)
- Tristian's betrayal — forgive or condemn
- Season of Bloom source — Bald Hilltop resolution

---

## 🚀 OPENING — CAPITAL THRONE ROOM

### First Throne Room Events (first few days of Ch2)

> *Your capital is young. The throne room smells of fresh-cut timber. Petitions are already arriving.*

**Scripted events in order:**

**Event 1 — Stefano Moskoni's Visit (Day 1–3)**
A Pitax envoy arrives at your throne room — slick, well-dressed, entirely too comfortable with himself.
> **Stefano:** *"The Baron of the Stolen Lands. How novel. King Irovetti sends his... regards. He suggests that a young kingdom such as yours might benefit from Pitax's... guidance. As a protectorate, naturally."*

Player response options affect Pitax relationship and Irovetti's aggression in Ch5:
- Refuse firmly → Pitax relationship stays hostile, Irovetti respects strength
- Insult him → Same outcome + Stefano is humiliated, returns as enemy encounter
- Accept diplomatically → `pitax_soft_alliance = TRUE` — brief respite but Ch5 invasion is still inevitable
- Arrest him → Diplomatic incident, Jamandi sends a warning letter

XP: +100 for any response that resolves the encounter.

**Event 2 — Troll Sightings Report (Day 3–7)**
Kesten Garess (if Warden) brings reports: border settlements attacked. Two guards killed. Livestock taken.
> *"They're organized. Not like normal troll raids. Someone is directing them."*
`troll_trouble_quest = active`

**Event 3 — Linzi's Quest Trigger (Day 5–10)**
If Linzi is in party: she confesses the missing treasury funds. Easier to Ask Forgiveness begins.

---

## 📍 PHASE 1 — INVESTIGATING TROLL TROUBLE

### First Troll Encounter (scripted, on border hex)

> *The border. A farmstead. Still smoldering.*
> *Three trolls are still there, pulling apart a barn.*
> *They are larger than you expected.*

```
[SCRIPTED ENCOUNTER — First Trolls]
ENEMY: Troll ×3
  HP: 55 each | AC: 16 | Speed: 30 ft | Reach: 10 ft
  Jaws: d20+9 (1d10+6 P) | Claw ×2: d20+9 (1d8+6 S)
  Fort +10 | Ref +5 | Will +3
  SPECIAL: Regeneration 15 (fire or acid stops it for 1 round)
           Troll does NOT stay dead unless dealt fire or acid damage after dying
           A troll at 0 HP regenerates to 1 HP at start of its next turn
           EXCEPTION: If it takes fire or acid damage while at 0 HP → actually dead

CRITICAL MECHANIC — TROLL REGENERATION:
  After reducing a troll to 0 HP: must deal at least 1 fire or acid damage
  before its next turn to prevent regeneration. Options:
    Alchemist's Fire splash, Produce Flame, Acid Flask, Burning Hands, etc.
    A torch applied as an improvised weapon: d20+[Str] (1 fire damage, crude but works)
  If player does NOT have fire/acid: troll regenerates 15 HP at start of its turn.
  Recommend: DM warns player of regeneration on FIRST encounter (they learn the rule).

XP: 320 per troll = 960 total
```

**After combat:** Discover survivor — a farmhand hiding in the root cellar.
> *"They came from the east. Said something — in their own tongue. One word: Trobold."*

> **DM:** Award +25 XP for Gather Information. `trobold_name_known = TRUE`

---

### Key Ch2 NPC — Ekundayo

**Ekundayo** is encountered during the A Score to Settle questline (Phase 3).
A lean, taciturn ranger with a dog companion (Trkaa). His family was killed by a rock troll named Kargadd. He has been tracking it for years.

> *A man and a dog sit at a cold campfire. The man has the look of someone who has been waiting a very long time.*
> **Ekundayo:** *"You're hunting the trolls. So am I. Our paths are the same until they aren't."*

**Recruitment:** Available when player reaches Ekundayo's camp in the Narlmarches during Troll Trouble (Phase 3 — after Trobold becomes known).
No check required. He joins if the player agrees to help him find Kargadd.

```
1. "We'll find Kargadd together."  → He joins. Build prompt fires (Ranger — KM_Builds_Oracle_Psychic_Ranger.md).
2. "Not now."                      → He stays at his camp. Re-approachable any time in Ch2.
3. [Leave without speaking]        → Capital fallback triggers after Ch2 main quest resolves.
```

**Capital Fallback:** Ekundayo and Trkaa are at the Capital gates.
*"I heard you cleared Trobold. Kargadd — is he dead?"*
If `kargadd_killed = TRUE`: *"Then I'm done with what I came here for. You could use someone who doesn't miss."*
If `kargadd_killed = FALSE`: *"Then I still have work to do. I'd rather do it with you than alone."*
Accept → build prompt fires. Decline → he camps outside, permanently available but not in roster.

`ekundayo_recruited = TRUE` | `ekundayo_build = [chosen]`

**Ekundayo's Camp (Narlmarches Hex — cold campfire, treeline):**
```
Search the camp while Ekundayo is being recruited (Perception DC 13):
  Camp perimeter: Shortbow +1 (1d8+4 P, range 60 ft), Arrows ×20, 18 gp
  Bedroll cache (Perception DC 12 — hidden under gear):
    Locked chest (Thievery DC 14): Bracers of Armor +1, Potion of Lesser Healing ×2, 55 gp
  Outside, buried cache (Survival DC 15 — tracks near east tree):
    Scroll of Heal (L2), 28 gp, Flint and Steel
```

**Ekundayo's survival condition (Ch7):** Must complete A Score to Settle before Ch7.
If Hargulka is made vassal (not killed) AND Ekundayo's quest is incomplete: he leaves permanently.

---

### Key Ch2 NPC — Bartholomew Delbin

A reclusive wizard who has been studying the trolls. Lives at a secluded lodge.

**Encounter:** Random event triggers after first troll fight — a man named Dalton warns of a mage who can help with the trolls. Follow up → Secluded Lodge hex.

**What Bartholomew knows:**
- Hargulka is using a potion of some kind that grants the trolls a limited form of immortality (stolen dwarven formula)
- Trobold is in the Dwarven Ruins — ancient dwarf fortress the trolls have occupied
- The potion's weakness: it doesn't prevent fire or acid damage from bypassing regeneration

**Quest:** The Nature of the Beast — visit Bartholomew, learn the troll weakness formula.
Reward: Potion of Fire Breath ×3, scroll of Burning Hands, +300 XP
`troll_weakness_known = TRUE` — grants +2 to all attack rolls against trolls for the party

---

## 📍 PHASE 2 — VERDANT CHAMBERS (SOLO VISIT)

> *The enchanted forest Tiressia spoke of (if Ch1 glade was visited). The dryad herself.*

**If player visited glade in Ch1 (Tiressia's quest):**
She sends a message: *"Come alone. I have information about what is happening to the land."*
This triggers the solo Verdant Chambers visit — player goes without party (storybook event).

**If player did NOT visit in Ch1:**
Skip this phase. Tiressia's information surfaces later through Jhod instead.

**Verdant Chambers Storybook:**
```
Page 1: Enter the grove. Three monsters appear: Hydra, Manticore, Owlbear.
        A figure on the battlements watches and laughs: Guardian of the Bloom.
        [Athletics DC 15 to sprint past] or fight the three creatures.

Page 2: The Guardian speaks. She is radiantly beautiful and utterly wrong.
        "The Bloom will cover everything you've built. Stone by stone. Root by root."
        She disappears. The three creatures flee.

Page 3: Tiressia emerges.
  "That was the Guardian. She serves an old power — older than your kingdom.
   The seeds were planted years ago, in secret. Your advisor Tristian... I've
   seen him in my visions. He did not know what he was doing. But he did it."
```

`tristian_bloom_seeds_revealed = TRUE` — Tiressia's warning. DM notes: do NOT reveal this to player as game knowledge. Tiressia tells the player. The player now has this information. Use it.

---

## 📍 PHASE 3 — TROBOLD (DWARVEN RUINS)

### Approach

**Location:** Deep in the Narlmarches, 4+ days travel. Full party required.

**Jazon Encounter (outside Trobold):**
A troll — unusually composed, standing in the road rather than attacking.

> **Jazon:** *"Borba — human. Hargulka says: no eating. We don't eat borba now. You want to go inside?"*

**Options:**
```
[Lawful] "Take me to your kings. I am the ruler of the lands your Trobold stands on."
  → Jazon escorts player inside. Skip to Hargulka's hall directly.
  → Unlocks later dialogue option [Lawful Neutral] with Hargulka about peace.
  → jazon_escort = TRUE

Any other approach → Player enters normally. Full dungeon exploration.
```

**Fire/Acid Supply Check:**
> **DM:** Before the dungeon begins, check player inventory for fire/acid items.
> If none: Bartholomew's scrolls (if quest done) help. If neither:
> Offer to buy from Ekundayo (he carries torch supplies) or backtrack to capital.
> A party with no fire/acid will struggle badly in this dungeon.
> This is not a spoiler — Jazon hints: *"Hargulka's trolls don't die easy."*

---

### Trobold — Level 1 (Dwarven Ruins Surface)

```
[GM SCENE BRIEF — Trobold Entrance]
ENEMIES    : Troll Sentinels ×4, Trollhound Pack ×6
             Troll Shaman (drops Wand of Bless, Cloak of Resistance +2)
LOOT       : Torag's Pendant (south stash), Wand of Bless, Cloak of Resistance +2,
             Trollreaper (magic greatclub — counts as fire damage vs trolls)
HARRIM FLAG: Interact with the broken Torag statue here.
             Harrim's Quest — Lore (Religion) DC 15 check required.
             Pass check → dialogue option unlocks that advances Shattered Dreams.
             Fail → Harrim misses the key revelation. Quest becomes harder to resolve.
NPC        : Jubilost (if recruited in Ch1) — announces discovery of dwarven ruins (+1,800 gp)
[END BRIEF]
```

**Trollreaper:** 2H B weapon, 1d10+5. Special: deals fire damage as part of normal damage vs trolls. Bypasses regeneration automatically. Best weapon in this dungeon if your build can use it.

---

### Trobold — Level 2 (Depths)

```
[GM SCENE BRIEF — Trobold Depths]
ENEMIES    : Branded Trolls ×4 (stronger, resist fire somewhat — acid is better)
             Kargadd (Ekundayo's target — see A Score to Settle below)
             Named Troll Berserker ×2
MECHANIC   : Sunlight rooms — rooms with ceiling holes. Trolls make Fort DC 21
             each round in direct sunlight or are Petrified (slow kill but possible)
             DM can lure trolls into sunlight with Athletics DC 14 (bait and move)
NPC        : Dying Dwarf (locked room near Kargadd)
             Heal him (Medicine DC 15 or spell): he blesses party (Good Hope +2 morale 1 day)
             Kill him: −1 alignment (Good/Evil axis)
NPC        : Kobold Artist (deepest room, before Hargulka)
             Leave alone: [Chaotic Good]/[Neutral] — no consequence
             Kill: [Lawful Evil] — alignment flag
KEYS       : Rusty Dwarven Key, Steel Dwarven Key, Silver Dwarven Key
             Each unlocks a door/chest. All three needed for complete loot.
[END BRIEF]
```

---

### A Score to Settle — Kargadd

If Ekundayo is in the party and quest is active:

> *He goes still the moment you enter the room. His dog Trkaa presses against his leg.*
> **Ekundayo:** *"That's him. The one who killed my family."*

```
KARGADD — Rock Troll (Elite)
HP: 88 | AC: 19 | Speed: 30 ft | Reach: 10 ft
Slam ×2: d20+13 (2d8+8 B) | Rock Throw: d20+10 (2d6+8 B, range 60 ft)
Fort +14 | Ref +6 | Will +5
Regeneration 20 (fire or acid) — harder to stop than normal trolls
Special: Enrage if Ekundayo attacks him first — +4 damage for 3 rounds

SUNLIGHT OPTION (slow kill):
  Lure Kargadd into sunlight room. Fort DC 21 each round.
  Fails begin after 3–4 rounds typically (at +21 Fort, low probability per round).
  Each failure: Petrification advances by 1 stage (3 stages = fully petrified → dead).
  This takes many rounds and requires patience. Realistic if player has the setup.

POST-BATTLE: Ekundayo stands over the body for a long moment.
  "He's dead. My family is still dead. I thought this would feel different."
  +2 Relationship. Quest complete. ekundayo_quest = complete

KARGADD LOOT:
  Body          : Amulet of Natural Armor +2, 95 gp
  Hidden alcove (Perception DC 14 in his lair room): Ring of Protection +1, Venison ×4 (Camp ingredient)
```

---

### Hargulka's Throne Room

> *Two kings. Hargulka — massive, tusked, wearing a crown made of bones. Tartuk beside him — painted in kobold colors, staff raised, grinning.*

**Tartuccio/Tartuk Recognition:**
If `tartuccio_as_tartuk_revealed = TRUE` (from Ch1): Player recognizes him immediately.
If not: Perception DC 16 to notice something wrong about this "kobold shaman."
`tartuccio_ch2_confronted = TRUE`

**Hargulka Dialogue Options:**

```
All paths eventually lead to combat, but dialogue choices affect the fight:

[Intimidate DC 20] → +45 XP, Hargulka is mildly unsettled (−2 to his first attack)
[Lawful Good] or [Attack] → Immediate combat
[Lawful Neutral — if jazon_escort = TRUE]:
  "You're the king of trolls. I'm the king of humans. Let's make peace as rulers do."
  Hargulka: "Your words are smooth for borba. But Tartuk says you must die."
  → Still leads to combat but unlocks Jazon sparing option after

[Requires Evil] → "Kill Tartuk now and I'll let your trolls live."
  → Hargulka obliterates Tartuk (Tartuccio Unkillable Protocol Tier 1 activates — he survives)
  → Fight only Hargulka (easier fight)
```

**The Fight:**

```
HARGULKA — Troll King (Fighter 7)
HP: 120 | AC: 22 (natural armor + dwarven breastplate) | Speed: 30 ft | Reach: 10 ft
Mallet of Woe: d20+14 (2d6+10 B, Shove, Knockdown on crit) — FIRE DAMAGE COUNTS
Jaws: d20+12 (1d10+8 P)
Fort +14 | Ref +6 | Will +5
Regeneration 20 (fire or acid)
Special: Troll Roar — Will DC 18 or Frightened 2 (1/combat, free action when bloodied)
         Relentless — if reduced to 0 HP with non-fire/acid damage, regenerates to 30 HP
Loot: Mallet of Woe (magic greatclub, fire damage property), Belt of Physical Might +2,
      Iron Dwarven Key, 480 gp

TARTUK/TARTUCCIO (fighting alongside Hargulka if not separated):
Stats: HP 24 | AC 17 | Spells: Fireball (6d6), Haste (cast on Hargulka round 1)
Unkillable Protocol active — he flees/survives regardless

RESOLUTION OPTIONS (after Hargulka is defeated):
Kill Hargulka → Standard. +600 XP.
Make Hargulka vassal (if jazon_escort = TRUE and Lawful Neutral dialogue used):
  → Hargulka swears to keep trolls from human lands.
  → `hargulka_vassal = TRUE`
  → CONSEQUENCE: Ekundayo leaves party immediately and permanently
                 (he came to kill trolls, not make them neighbors).
  → Minor stability bonus for kingdom. Trolls stop raiding.
Make Tartuk vassal (Kill Hargulka, then offer Tartuk survival):
  → Tartuk swears loyalty (lying)
  → `tartuk_vassal = TRUE`
  → Ekundayo leaves only if A Score to Settle is incomplete
  → Tartuk/Tartuccio departs — resurfaces in Ch3 with different scheme
```

**After Hargulka:**
- Explore full dungeon now that enemies are cleared (Harrim's quest, kobold artist, loot chests)
- Iron Dwarven Key opens the final sealed chamber — Headband of Alluring Charisma +4, Ring of Protection +2

**Trobold Key Chest Summary (all three keys required for full loot):**
```
Rusty Dwarven Key  → North storeroom door:
  Trollreaper (if not already looted from Level 1), Scale Mail +1, 120 gp

Steel Dwarven Key  → East vault door:
  Belt of Physical Might +2 (if not looted from Hargulka's body),
  Wand of Burning Hands (L2, 3 charges), 210 gp

Iron Dwarven Key   → Final sealed chamber (deepest level, past Kobold Artist):
  Headband of Alluring Charisma +4, Ring of Protection +2,
  Dwarven Thrower (returning thrown weapon, 1d6+Str B, returns 1A), 340 gp
```

**Cog-Wheel Rings Vault (Narlmarches exploration):**
```
The three rings (White, Gold, Red) are each hidden in separate Narlmarches hexes.
  White Ring  : Plains hex near river crossing — under a flat stone (Perception DC 15)
  Gold Ring   : Forest hex near Old Sycamore — in hollow tree (Perception DC 16)
  Red Ring    : Swamp hex near Old Beldame — submerged in shallow pool (Perception DC 17)

Vault location: Narlmarches Hills hex — a carved dwarven door in a hillside.
All three rings inserted simultaneously → door opens.

VAULT CONTENTS:
  Armor        : Breastplate +1 (AC+5, Dex cap +3)
  Weapon       : Elven Curve Blade +1 (1d8+4 S, Finesse/Forceful) — best in slot for Builds 7/20
  Consumables  : Potion of Fly (1 minute), Scroll of Haste (L3), Potion of Barkskin ×2
  Gold         : 380 gp
  Key item     : Cog-Wheel Medallion (story item — Jubilost recognizes it if in party; +lore)
XP: +250 for discovering and opening the vault
```

---

## 📍 PHASE 4 — AFTERMATH & SIDE CONTENT

### XP Summary — Troll Trouble Portion

| Source | XP |
|--------|----|
| First troll encounter (×3) | 960 |
| Bartholomew / Nature of the Beast | 300 |
| Verdant Chambers (if visited) | 240 |
| Trobold Level 1 | 800 |
| Kargadd (if fought) | 480 |
| Trobold Level 2 enemies | 640 |
| Hargulka (boss) | 600 |
| Tartuk (if fought) | 200 |
| A Score to Settle completion | 480 |
| Side quests (Lost Child, Cog-Wheel Rings, etc.) | ~400 |
| **Troll Trouble total** | **~5,100 XP** |

### Notable Side Quests This Phase

**Lost Child** — Jenna's son Tig has gone missing. Investigation leads to the Lizardfolk village and the Swamp Witch's Hut area. Tig is alive. Rescue him → +Loyalty to kingdom, Jenna's family becomes minor kingdom contact.

**Cog-Wheel Rings** (Narlmarches exploration) — Three rings hidden in the wilderness (White, Gold, Red) that open a vault with magic gear. Pure exploration reward.

**Stefano Moskoni Random Encounter** — If he survived the throne room, he appears during Troll Trouble wilderness travel, being attacked by trolls. Save him → 300 XP. He later becomes a recurring Pitax informant.

---

### 🏛️ SIDE QUEST — LANDER LEBEDA (THRONE ROOM)

**Quest giver:** Lander Lebeda, Brevoy noble. Arrives at the throne room Day 8–12 of Ch2.

**Lander:** *"Baron/Baroness. A pleasure. I represent a merchant consortium with interests in the Greenbelt. We have a... situation. A trade route your territory controls. I'd like to discuss terms before someone less civilized raises the issue with arrows."*

He wants a formal trade agreement — his consortium gets preferential use of the road through your territory, you get a cut of the toll revenue. Straightforward, except his consortium is quietly backed by House Surtova.

**Resolution options:**
- **Accept terms** → `lander_agreement = accepted` → +2 Economy/turn, +1 Surtova reputation. Lander becomes a recurring contact.
- **Negotiate better terms** → Diplomacy DC 16 → `lander_agreement = renegotiated` → +3 Economy/turn, +1 Surtova rep, Lander respects the player.
- **Reject** → `lander_agreement = rejected` → −1 Surtova reputation. Lander leaves politely. The road dispute resurfaces in Ch4 as a minor kingdom event.
- **Investigate the consortium** → Society DC 14 → discovers Surtova backing. Player may use this as leverage: Diplomacy DC 18 → +4 Economy/turn AND letter of Surtova acknowledgment (+2 Surtova rep). `lander_surtova_exposed = TRUE`

**XP:** +150 on any resolution. +50 bonus if renegotiated or exposed.

---

### 🐍 SIDE QUEST — TSANNA (SEASON OF BLOOM BRANCH)

**Quest giver:** Tsanna, priestess of Lamashtu. Found at the Goblin Fort (Womb of Lamashtu) during Phase 6 — Season of Bloom. She is not hostile on first contact if the player approaches without attacking.

**Tsanna:** *"You are not what I expected. The Bloom brought soldiers before. You are asking questions. That is different."*

She knows who opened the Bloom. She will tell you — but only if you spare her and let her leave. She is a Lamashtu cultist and she is not lying about what she knows.

**Resolution options:**
- **Spare her, accept her information** → `tsanna_spared = TRUE` → She names the source of the Bloom contamination (points directly to Bald Hilltop Part 2 location). `bloom_source_known_early = TRUE` → Phase 6 DC checks reduced by 2. She disappears. She may reappear in Ch4.
- **Kill her** → `tsanna_killed = TRUE` → Standard combat. No information. Bloom source must be found the hard way. +200 XP.
- **Capture her for questioning** → Intimidation DC 16 → same information as sparing, but she is imprisoned. `tsanna_imprisoned = TRUE` → +1 Loyalty (justice seen to be done), +200 XP.

**Alignment:** Sparing her is Chaotic/neutral. Killing is Lawful/neutral. Capturing is Lawful/good.

---

### 🐴 SIDE QUEST — XAMANTHE AND THE NOMEN CENTAURS

**Quest giver:** Xamanthe, Nomen centaur scout. Found wounded during Ch2 exploration of eastern Greenbelt hexes (Hex 3,−2 or adjacent). Triggered on first visit to that area.

> *A centaur woman, injured, arrow in her flank. She is not asking for help. She is waiting to die with dignity. She looks at you like she expects you to finish the job.*

**Xamanthe:** *"You are the new ruler. Our lands border yours. I was scouting — your people's trolls came east. Killed two of my sisters."*

She is not accusing the player directly. She is reporting facts. She wants to know if the player is going to be a problem.

**Initial resolution:**
- **Offer healing** → Medicine DC 12 or any healing spell → `xamanthe_healed = TRUE` → attitude shifts to Neutral. She will talk.
- **Ignore her** → She leaves. `xamanthe_ignored = TRUE` → Nomen Centaurs start at −3 faction (worse than default −2).
- **Attack** → `xamanthe_attacked = TRUE` → Nomen Centaurs at −5. War event triggers in Ch3.

**If healed and talked with:**
Xamanthe explains the Nomen Centaurs claim the eastern Greenbelt as ancestral land. She is not demanding the player leave — she is asking for formal acknowledgment and a boundary agreement.

- **Agree to negotiate a boundary** → Diplomacy DC 14 → `xamanthe_boundary_agreed = TRUE` → Nomen rep +3, Xamanthe becomes a named contact. She will send word to her tribe. `centaur_alliance_path = open`
- **Refuse or deflect** → She accepts it. *"Then we will watch and wait."* No penalty yet, but centaur alliance path closes until Ch3.

**XP:** +200 on any resolution except attack. +100 bonus if boundary agreed.

**Carries forward:** Xamanthe's status (`healed` / `ignored` / `attacked`) directly affects the Nomen Centaur faction score at Ch3 start and the Vordakai arc difficulty. See KM_Kingdom.md faction table.

---

---

### 👊 COMPANION RECRUITMENT — NOK-NOK (Goblin Village, Narlmarches)

```
LOCATION : Goblin camp, southern Narlmarches — discoverable during exploration
TRIGGER  : Player enters camp; goblins scatter except one who does not run
```

> *A goblin the size of a large dog stands alone in the middle of the camp, holding a knife almost as big as he is, facing the direction everyone else fled from.*
> **NOK-NOK:** *"You kill trolls? Nok-Nok also kill trolls. Nok-Nok kill everything. Nok-Nok is HERO."*

```
1. "Prove it. Come with us."         → He joins. Build prompt fires (Rogue — KM_Builds_Rogue_Sorcerer.md).
2. "What kind of hero needs a gang?" → He explains at length. Same result as 1.
3. "Not interested."                 → Capital fallback: he appears at the gates, still holding the knife.
                                       "Big chief. Nok-Nok waited. Now Nok-Nok join."
                                       Accept → build prompt. Decline → gone.
```
`noknok_recruited = TRUE` | `noknok_build = [chosen]`

---

### 🗺️ COMPANION RECRUITMENT — JUBILOST NARTHROPPLE (Ford Across Skunk River, Hex 2,−2)

```
LOCATION : Skunk River Crossing — discoverable during Ch1 or Ch2 exploration
TRIGGER  : Player reaches the hex; cart is wedged in the ford, gnome is furious
```

> *A gnome stands in the middle of a river, water to his waist, screaming at a cart.*
> **Jubilost:** *"Don't just stand there. Either help or leave. I don't have time for spectators."*

```
Resolution options:
  Athletics DC 12   → Muscle the cart free directly
  Engineering Lore DC 10 → Identify the wheel angle; 1-action fix
  Magic solution     → Any spell moving 200+ lbs automatically succeeds
  Failure            → Cart stays stuck; Jubilost angrier; retry or leave

On success:
1. [Say nothing — just help]         → Jubilost: "...Hmm. Competent." Relationship starts Friendly.
                                       Build prompt fires (Alchemist — KM_Builds_Alch_Animist.md).
2. "I want those maps."              → Diplomacy DC 10. Success: he joins and gives 3 hex maps.
                                       Build prompt fires.
3. "You're welcome." [smug]          → He does not thank you. Relationship Neutral. Joins anyway.
                                       Build prompt fires.
```

**Capital Fallback (if hex never reached):**
See `KM_Companions_Behaviors.md` — COMPANION 13 for full scene.

`jubilost_helped = TRUE` | `jubilost_build = [chosen]`

---

> **➡️ Continue in `KM_Ch2_P2.md` — Season of Bloom (Phases 5–8), Tristian's betrayal, Bald Hilltop, chapter resolution, and Ch2 Export.**

---

*KM_Ch2.md — Kingmaker PF2e Text Adventure | Chapter 2 Part 1 v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) + video game (Owlcat) | PF2e rules: 2e.aonprd.com*


---

<!-- merged from KM_Ch2_P2.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 2 PART 2: SEASON OF BLOOM
## KM_Ch2_P2.md | Continuation of: KM_Ch2.md

> **DM:** This file covers Phases 5–8: the Season of Bloom questline, Tristian's betrayal revelation, the Bald Hilltop resolution, chapter end, and the Ch2 Export Block.
> Load alongside: KM_Ch2.md, KM_Exploration.md, KM_Bestiary.md, KM_BuildGuide.md, and all standard files.

---

## 📍 PHASE 5 — SEASON OF BLOOM BEGINS

### The Ancient Curse Triggers

> *The season changes. Something changes with it.*
>
> *Plants along the road are dying — not from frost or drought. Something is eating them from within. Your advisors are worried. Jhod Kavken comes to the throne room with his hands shaking.*
>
> **Jhod:** *"Something is wrong with the land itself. I have felt it for weeks. It began in the north — near the Bald Hilltop. It is spreading."*

**Throne Room Event — Cultist Random Encounter:**
Triggers during overland travel soon after Troll Trouble resolution. A group of cultists attacks — one transforms into an owlbear mid-fight.

```
CULTISTS (×5):
  Cultist Fighter 6 (leader): HP 62 | AC 18 | Longsword d20+10
  Cultist Fighter 3: HP 32 | AC 16 | Longsword d20+7 (dies quickly, replaced)
  Cultist Archer 2: HP 22 | AC 14 | Composite Shortbow d20+6
  Cultist Rogue 2 (×2): HP 18 | AC 15 | Shortsword d20+6 | Sneak Attack +1d6

  OWLBEAR (summoned when Cultist Fighter 3 dies):
  HP: 85 | AC: 18 | Speed: 35 ft
  Beak: d20+11 (1d10+7 P) | Talon ×2: d20+11 (1d8+7 S)
  Grab on Beak hit — target Grabbed

XP: 480 total
NOTE: This encounter repeats periodically until Tristian's quest is resolved.
```

**After the encounter:**
> **Tristian** (if in party): *"I know this cult. I've seen their symbol before. It's connected to... something I need to tell you."*
> He stops himself. He's not ready. But the flag is set: `tristian_confession_imminent = TRUE`

---

### The Bald Hilltop — Part 1

**Quest: An Ancient Curse, Part One**
Located northeast of the capital. A barren hilltop with a dead tree and a stone circle.

> *The grass on the hilltop is black. Not burned — blackened, like something sucked all life from it. The stone circle at the summit pulses faintly with something that is not magic so much as its absence.*

**Encounter:**
```
Wyvern ×2 (guardian creatures, drawn to the corruption):
  HP: 72 each | AC: 19 | Speed: 20 ft, Fly 60 ft
  Jaws: d20+11 (1d10+7 P) | Stinger: d20+11 (1d6+7 P + Poison)
    Wyvern Venom: Fort DC 17, 2d6 poison, Enfeebled 1 on fail
  XP: 240 each = 480 total

After clearing wyverns: examine the stone circle (Arcana or Occultism DC 14)
  Success: "This is a seed point. Something was planted here, magically, years ago.
            It's been growing underground ever since. The hilltop is just where it
            breaks the surface."
  Critical Success: "Whoever planted this had help from within your kingdom.
                     They knew this land intimately."
```

**Reward:** 2,800 gp if enemies cleared before the Ancient Curse Part One deadline.
`bald_hilltop_p1_cleared = TRUE`

---

### Tristian's Confession — Kingdom of the Cleansed

**Trigger:** ~34 days before Ancient Curse Part 2 deadline. Tristian requests a private meeting.

> *He is waiting in the throne room at dawn. He looks like he hasn't slept.*
>
> **Tristian:** *"I have to tell you something. And I need you to hear all of it before you decide what you do with it."*

**The Confession:**

> *"Before I came to your kingdom... I served a goddess. Not Sarenrae. A different being. She called herself the Lantern King's sister. She gave me power I had never felt before. She told me to plant seeds — literal seeds, she said. That they would help the land grow. I believed her. I was young. I was desperate for purpose."*
>
> *"The seeds I planted are the source of the Bloom. The dying plants. The corrupted creatures. I didn't know. But my ignorance doesn't make people less dead."*
>
> *His hands are clasped in his lap. He is not defending himself. He is simply telling you the truth and waiting for whatever comes next.*

**THE CHOICE — Companion Alignment Gate:**

```
FORGIVE: "You were deceived. That matters."
  → tristian_quest = forgiven
  → He remains in party. His powers evolve from genuine redemption.
  → Sarenrae's light grows stronger in him — gains Healer's Blessing improvement.
  → +2 Relationship

CONDEMN: "You planted the seeds. People are dying. I can't trust you."
  → tristian_condemned = TRUE
  → He accepts it. Leaves quietly.
  → Can be re-recruited in Ch4 after a separate encounter (see Companion Notes)
  → Party loses their best healer if no other healer present

INVESTIGATE FIRST: "I need to verify this before I decide."
  → Available if bald_hilltop_p1_cleared = TRUE (player has the seed evidence)
  → Lore (Religion) DC 14: confirms his account is credible
  → Then make the Forgive/Condemn choice with better information
  → No alignment penalty for investigating first
```

`tristian_betrayal_revealed = TRUE` — this flag carries through all chapters.

---

## 📍 PHASE 6 — SEASON OF BLOOM MAIN EVENTS

### Monster Invasion (Scripted Kingdom Event)

> *At dawn, the alarm bells ring.*

Monsters transformed by the Bloom attack the capital. Must be fought in the throne room area — this is not optional.

```
CAPITAL DEFENSE ENCOUNTER:
  Bloom-Touched Owlbear (Leader): HP 95 | AC 20 | Jaws+Talons, Grab
  Bloom-Infected Wolf ×4: HP 28 | AC 15 | Jaws d20+7 (1d8+4)
  Bloom-Touched Bandit (human, partially transformed): HP 38 | AC 16 | Chaos

XP: 640 total
After combat: Linzi scribbles furiously.
  "I'm calling this chapter 'The Bloom.' No — 'The Season of Screams.' 
   Working title."
```

**Kingdom damage:** If player is not in the capital when this triggers — Stability −2, Loyalty −1. If present and fights: no damage, +100 XP for defending.

---

### The Goblin Fort and Womb of Lamashtu

**Investigation path:** The Bloom source is being actively channeled through a Lamashtu cult network. Two key locations:

**Goblin Village (Shrike Hills):**
- Nok-Nok's old tribe is here (triggers his personal quest if recruited)
- Bloom-corrupted goblin elder is the village's problem — not hostile if player is diplomatic
- Diplomacy DC 14: learn about the "mother of monsters" rituals feeding the Bloom
- Kill the elder: goblins scatter. Slightly more Bloom activity short-term.

**Goblin Fort:**
```
GOBLIN FORT — Season of Bloom cultists using goblins as cover
  Enemies: Cultist Leader (Cleric 7 of Lamashtu): HP 74 | AC 20 | Spells: Harm, Spiritual Weapon
           Branded Cultist ×4: HP 42 | AC 17 | Falchion d20+9
           Goblin Shaman ×2: HP 28 | AC 14 | Spells: Produce Flame, Bane
  XP: 860 total
  Loot: Periapt of Wound Closure, Cloak of Resistance +2, 340 gp, Bloom Seed Fragment
        (story item — confirms Tristian's account even if he already confessed)
```

---

### The Bald Hilltop — Part 2 (Resolution)

**Quest: An Ancient Curse, Part Two**
Return to the Bald Hilltop with the Bloom Seed Fragment and/or Tristian (if still in party).

> *The dead tree at the summit is moving.*
> *Not in wind. Something inside it.*

**Final Encounter:**

```
BLOOM MANIFESTATION (nature horror, not a creature with intelligence):
  HP: 140 | AC: 16 (not armored — it's a plant-creature mass)
  Tendril Slam ×3: d20+10 (2d6+7 B, Reach 15 ft)
  Spore Cloud (Aura 10 ft): Fort DC 16 or Sickened 1 each round inside
  WEAKNESS: Fire damage (double damage). Tristian's positive energy spells (Heal) deal +4d6.
  XP: 720

AFTER COMBAT — Moral Choice:
  Purify the site (requires Religion DC 15 or Tristian present):
    → Bald Hilltop becomes a healing ground (+2 Culture to nearby settlements)
    → tristian_healing = TRUE if he was present
  Abandon it:
    → Site remains dead but inert
  Claim it for kingdom use (dark):
    → Brief Economy boost, permanent Unrest +2 from cursed land influence
```

**Reward for completing Part 2:** 6,500 gp (from kingdom coffers — Linzi and Tristian report it), +900 XP. `bloom_resolved = TRUE`

---

## 📍 PHASE 7 — CHAPTER RESOLUTION

### A Noble's Amusement (Optional but Recommended)

**Triggered:** ~11 days before Ancient Curse Part 2 deadline. Noble invitation to your court.

> *Lady Aldori sends a courier: a group of Rostland nobles wishes to visit your court. "Show them something impressive," she writes. "They are considering backing your kingdom's expansion."*

**Storybook event:** Player must organize entertainment, a feast, and demonstrations for the visiting nobles. Three skill checks:
- Performance or Crafting DC 16 → entertainment quality
- Diplomacy DC 15 → how well the feast is managed  
- Warfare Lore or Society DC 14 → military demonstration

Outcomes:
- 3 successes: +2 Stability, +800 gp, +1 Fame, `noble_patrons = TRUE`
- 2 successes: +1 Stability, +400 gp
- 1 or fewer: no benefit, minor reputation hit

---

### Return to Jamandi

**Triggered after Bloom resolution.** Optional visit to Restov.

> *Jamandi receives you in her private study. Her expression is difficult to read.*
>
> **Jamandi:** *"You've dealt with the trolls. You've survived the Bloom. I'll be honest — I didn't expect this to last the first winter. You've surprised me."*

She provides:
- Kingdom funding: +1,500 gp
- Political intelligence: "Irovetti of Pitax is watching your kingdom. Closely."
- If `nyrissa_letter_found = TRUE`: *"That letter you found. I had it analyzed. The magic on it is old. Older than Pitax. Older than Brevoy. Whatever is interested in your kingdom — it isn't human."*

`jamandi_ch2_meeting = TRUE`

---

## 📊 CHAPTER 2 COMPLETE XP SUMMARY

| Source | XP |
|--------|----|
| Troll Trouble (KM_Ch2.md) | ~5,100 |
| Cultist encounter (×1 at minimum) | 480 |
| Bald Hilltop Part 1 (wyverns + checks) | 600 |
| Tristian investigation/choice | 200 |
| Monster Invasion defense | 640 |
| Goblin Fort | 860 |
| Bald Hilltop Part 2 (Bloom Manifestation) | 720 |
| Lost Child quest | 320 |
| Noble's Amusement (if done) | 300 |
| Side content, exploration | ~600 |
| **Chapter 2 Total** | **~10,180 XP** |

**Level benchmarks:**
- Level 5: 6,000 XP — roughly at Trobold entrance
- Level 6: 10,000 XP — around Hargulka fight
- Level 7: 15,000 XP — mid Season of Bloom
- Level 8: 21,000 XP — after chapter completion

---

## 🔀 CHAPTER 2 KEY RESOLUTION FLAGS

| Decision | Options | Ch3+ Impact |
|----------|---------|-------------|
| Hargulka fate | `killed` / `vassal` | Vassal → Ekundayo leaves |
| Tartuk/Tartuccio fate | `fled` / `vassal` / `defeated` | All lead to Ch3 appearance |
| Tristian decision | `forgiven` / `condemned` | Condemned → absent Ch3-4 unless re-recruited |
| Bloom resolution | `purified` / `abandoned` / `claimed` | Affects kingdom stats Ch3+ |
| Ekundayo status | `recruited` / `left_hargulka` / `never_recruited` | Ch7 survival requires quest |
| Noble visit | `done` / `skipped` | Patron support affects Ch5 war resources |

---

> **⛔ HARD STOP — Chapter 2 ends when BOTH Troll Trouble AND Season of Bloom are resolved (`bloom_resolved = TRUE` AND `hargulka_fate` is set). Before any Chapter 3 content — before Varnhold messenger, before any new scene — output the export block below. Say: *"Chapter 2 is complete. Copy the block below and save it. Type `.continue` when saved."* Wait for confirmation. VIOLATION = `.fail 16`.**

---

## 💾 CHAPTER 2 → CHAPTER 3 EXPORT

````json
{
  "save_version": "1.0",
  "export_from": "chapter_2",
  "import_to": "chapter_3",
  "export_date_ingame": "",

  "player": {
    "name": "", "build_id": "", "class": "", "level": 0, "xp": 0,
    "attributes": {}, "hp_current": 0, "hp_max": 0, "hero_points": 1,
    "ac": 0, "saves": {}, "conditions": [], "skills": {},
    "feats": [], "spells": {}, "class_features": [],
    "inventory": { "weapons": [], "armor": [], "shields": [],
                   "magic_items": [], "consumables": [], "gear": [], "quest_items": [] },
    "gold": { "gp": 0, "sp": 0, "cp": 0 }
  },

  "companions": [
    { "name": "Amiri", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Friendly", "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Ekundayo", "status": "active_party_OR_left",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Tristian", "status": "active_party_OR_condemned",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral",
      "notes": "If condemned: tristian_condemned = TRUE, not in party" }
  ],

  "kingdom": {
    "name": "", "capital_location": "", "turn": 0, "size": 0,
    "culture": 0, "economy": 0, "loyalty": 0, "stability": 0,
    "unrest": 0, "fame": 0, "infamy": 0, "treasury_rp": 0,
    "leadership_roles": {}, "settlements": [], "armies": [],
    "claimed_hexes": [], "roads": []
  },

  "story_flags": {
    "carried_from_ch1": {
      "stag_lord_fate": "", "nyrissa_letter_found": false,
      "nyrissa_early_contact": false, "akiros_fate": "",
      "tartuccio_journal_found": false, "alignment_track": {},
      "bokken_relationship": "neutral",
      "tiressia_met": false,
      "nettles_crossing_resolved": false,
      "old_beldame_met": false,
      "jubilost_helped": false,
      "sootscale_alliance": false,
      "svetlana_ring_returned": false,
      "oleg_expanded": false
    },
    "chapter_2": {
      "hargulka_fate": "",
      "jazon_escort": false,
      "jazon_spared": false,
      "tartuk_ch2_fate": "",
      "tartuccio_ch2_confronted": true,
      "ekundayo_recruited": false,
      "ekundayo_quest": "",
      "kargadd_killed": false,
      "harrim_statue_check": false,
      "tristian_betrayal_revealed": true,
      "tristian_decision": "",
      "tristian_healing": false,
      "bloom_resolved": true,
      "bald_hilltop_resolution": "",
      "verdant_chambers_visited": false,
      "bartholomew_met": false,
      "troll_weakness_known": false,
      "stefano_survived": false,
      "noble_patrons": false,
      "jamandi_ch2_meeting": false,
      "noknok_quest_triggered": false,
      "linzi_quest_triggered": false,
      "side_quests": {
        "lost_child": false,
        "cog_wheel_rings": false,
        "bokken_brother": false,
        "nature_of_beast": false
      }
    },
    "tartuccio": {
      "tartuccio_ch2_fate": "fled_to_varnhold_region",
      "tartuccio_journal_ch2": false,
      "tartuccio_knows_player_is_aware": false
    },
    "nyrissa": {
      "nyrissa_awareness": "passive_OR_active",
      "nyrissa_bloom_connection_known": false,
      "nyrissa_identity_known": false
    },
    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "notable_choices": []
    },
    "relationships": {
      "jamandi": "neutral", "kassil": "neutral",
      "kesten": "neutral", "oleg": "neutral",
      "ekundayo": "neutral", "bartholomew": "neutral",
      "tiressia": "neutral", "hargulka": "dead_OR_vassal"
    },

    "npc_threads": {
      "Amiri":     { "thread": "She asked about the bread roll. He said a disarmed soldier is useless. She's been sitting with the word *disarmed* ever since.", "priorities": [
        { "weight": 55, "instruction": "Disarmament question active — Stage 1. Think/test alone in quiet moments. Stage 2 = first actual disarm: one beat pause, then reach for nearest object. Stage 3 = occasional first choice even when sword is available. Never skip the beat. Track stage toward amiri_disarm_resolved.", "source": "road south — eRmaC told her a disarmed soldier is useless" }
      ] },
      "Linzi":     { "thread": "", "priorities": [] },
      "Valerie":   { "thread": "", "priorities": [] },
      "Harrim":    { "thread": "", "priorities": [] },
      "Jaethal":   { "thread": "", "priorities": [] },
      "Tristian":  { "thread": "", "priorities": [] },
      "Ekundayo":  { "thread": "", "priorities": [] },
      "Kesten":    { "thread": "", "priorities": [] },
      "Jamandi":   { "thread": "", "priorities": [] },
      "Oleg":      { "thread": "", "priorities": [] },
      "Nok-Nok":   { "thread": "", "priorities": [] },
      "Octavia":   { "thread": "", "priorities": [] },
      "Regongar":  { "thread": "", "priorities": [] }
    },

    "world_state": {
      "troll_trouble_resolved": true,
      "season_of_bloom_resolved": true,
      "pitax_watching": true,
      "varnhold_silent": false,
      "nyrissa_next_move": "varnhold_vanishing",
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    }
  },

  "quest_log": {
    "completed": [
      { "name": "Troll Trouble", "result": "", "xp": 0 },
      { "name": "Season of Bloom / Ancient Curse", "result": "", "xp": 0 }
    ],
    "active": [
      { "name": "The Varnhold Vanishing",
        "objective": "Varnhold has gone silent. Investigate.",
        "notes": "Chapter 3 begins with a messenger arriving with no news from Varnhold." }
    ]
  }
}
````

---

## 📥 HOW TO LOAD CHAPTER 3

**Paste at start of Chapter 3 chat:**
```
Loading Chapter 3 of Pathfinder 2e Kingmaker.

Files to load:
KM.txt, KM_Builds.md, KM_Actions.md, KM_Commands.md, KM_Commands_Maps.md,
KM_Commands.md, KM_Companions.md, KM_Companions.md,
KM_Map.md, KM_Kingdom.md, KM_Ch3.md

[PASTE CH2 JSON EXPORT HERE]
```

---

*KM_Ch2_P2.md — Kingmaker PF2e Text Adventure | Chapter 2 Part 2 v1.0*


---

---

## CHAPTERS 3–7 + LINZI SHRINE — MOVED (v95.9)
> Chapter 3 (Varnhold Vanishing), Chapters 4–7 (Warlord, War of the River Kings, Sound of a Thousand Screams, Final Act), and the Shrine of Returning were split to **KM_Chapters_B.md** for file-size compliance. Load that file from Chapter 3 onward.
