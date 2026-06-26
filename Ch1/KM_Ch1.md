# KINGMAKER — CHAPTERS (CONSOLIDATED)
## KM_Ch1.md | v1.0 (2026-05-22): Merged from Ch1 + Ch1_B + Ch1_Export + Ch2 + Ch2_P2 + Ch3 + Ch4 + Linzi_Shrine.

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
