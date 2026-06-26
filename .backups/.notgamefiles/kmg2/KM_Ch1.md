# KINGMAKER — CHAPTER 1: STOLEN LAND
## KM_Ch1.md | Loads after: KM_Prologue_Export.md | Loads before: KM_Ch2.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions_B.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Leveling.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md. Import Prologue JSON Export Block before beginning. Ch1 ends on Stag Lord defeat + return to Oleg's. Output Ch1 Export Block (KM_Ch1_Export.md) at chapter end.

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
- Seekers released: rejoin at player's level (see KM_Malak_Jail.md leveling)
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

**If player accepts:** Run build assignment prompt (Cleric builds — KM_Builds_C.md) before continuing.
**If player declines:** Tristian travels to the Capital. Approaches player at throne room — Accept/Decline/Ask scene. On Accept: build prompt fires then.
**Flag:** `tristian_recruited = TRUE` | `tristian_build = [chosen]`

**Temple reward:** Jhod Kavken consecrates the temple. Grants free Treat Wounds (DC 20 = 2d8+10) once per day for entire party. `temple_elk_cleared = TRUE`

---

> **➡️ PHASE 7 (Stag Lord's Fort), PHASE 8 (Return to Oleg's & Kingdom Founding), CHAPTER 1 XP SUMMARY, and CHAPTER 1 RESOLUTION PATHS — see `KM_Ch1_B.md`.**

> **⚠️ DM: Chapter 1 ends when the player returns to Oleg's Trading Post after defeating the Stag Lord AND triggers the Kingdom Founding sequence. Output the Ch1 Export Block at this point. Full late-chapter content is in KM_Ch1_B.md.**

---

*KM_Ch1.md — Kingmaker PF2e Text Adventure | Ch1 v2.0 (split — pair-load with KM_Ch1_B.md)*
