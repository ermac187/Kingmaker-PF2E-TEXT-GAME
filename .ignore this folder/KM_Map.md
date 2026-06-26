# KINGMAKER — CAMPAIGN MAP & HEX SYSTEM
## KM_Map.md | Referenced by: KM.txt

---

## 🗺️ HEX SYSTEM REFERENCE

> **DM:** This file is the master map reference. Use it to track hex exploration, display the world map when the player types `.map world` or `.hex [name]`, and manage the kingdom territory as it grows. Update hex status in the JSON Save Block — `hexes[]` array.
> For full named hex location details (encounter severities, loot, quest hooks, resource flags) across all 18 zones, search **KM_Map.md** in project knowledge.

### Hex Status System
```
● CONTROLLED  — Kingdom territory. Resources active. Can build settlements.
○ DISCOVERED  — Fully reconnoitered. Can be Claimed via Region Activity.
◎ SIGHTED     — Entered but not fully explored. Terrain known, no claim possible yet.
⟲ UNEXPLORED  — Fog of war. Player knows nothing. Show as [?] on map.
✗ HOSTILE     — Enemy-held. Must be cleared before claiming.
```

### Terrain Symbols
```
★  Settlement / Capital       ⊕  Trading Post / Cave
⚔  Military Camp             ✦  Religious Site
◆  Arcane Tower              ◉  Resource (mine/lumber/farm)
♣  Forest                    ∿  Water / River
▒  Mountains / Hills         .  Plains / Grassland
≈  Marsh / Swamp             ⟲  Ruins / Unexplored
```

### Coordinate System
Hexes use `(column, row)` coordinates. Origin `(0,0)` = your Capital.
Positive X = East. Negative X = West. Positive Y = North. Negative Y = South.
Each hex = approximately 12 miles across. Travel time varies by terrain.

### Hex Entry Procedure

> **DM:** Every time the party moves to a new hex, follow these steps in order before writing any narration.

```
STEP 1 — STATUS CHECK
  Is this hex already discovered or unexplored?
  Unexplored: replace [?] on world map with terrain symbol, name the hex if it has one.
  NOTE: Entering a hex is NOT the same as Reconnoitering it (see Reconnoiter rule below).

STEP 2 — TRAVEL TIME
  Apply travel time (see table above). Advance in-game date.
  Check .calendar for time limit status. If soft deadline missed: trigger consequence.

STEP 3 — WEATHER
  Roll d20 + season modifier (see KM_Exploration.md weather table).
  Apply travel penalties if Heavy Rain or worse.

STEP 4 — ENCOUNTER ROLL
  Roll d20 vs terrain threshold (KM_Exploration.md encounter tables).
  On trigger: roll on the appropriate terrain encounter table.
  Scripted encounter: if this hex has a fixed encounter and it hasn't triggered yet,
  run the scripted encounter INSTEAD of the random table on first entry.

STEP 5 — SCENE BRIEF
  If the hex has a named location (see KM_Map.md), run the standard Scene Brief protocol.
  If no named location: brief wilderness description + any encounter from Step 4.

STEP 6 — UPDATE MAP
  Entering a hex marks it as SIGHTED (terrain revealed, [?] replaced with symbol).
  To mark as DISCOVERED the party must spend a full day Reconnoitering (see below).
  Only DISCOVERED hexes can be Claimed. Add to hexes[] in save block.
```

### Reconnoiter Rule (Canon — TTRPG + CRPG)

> **DM:** This is the core hexploration activity from PF2e Kingmaker rules and the CRPG. Do not skip it.

```
RECONNOITER: The party spends 1 full day in the hex actively exploring it.
  Cost      : 1 full travel day (cannot also travel to another hex that day)
  Outcome   : Hex status upgrades from SIGHTED → DISCOVERED
  Effect    : Hex can now be Claimed via Kingdom Region Activity
  XP        : Award exploration XP when a hex is Reconnoitered (not just entered)

AUTOMATIC RECONNOITER (no extra day spent):
  - A named location is found and its scripted encounter is resolved (it counts as full exploration)
  - The party camps in the hex for a full rest (counts as reconnoitering by end of rest)
  - Party has a character with Legendary Survival or Scout archetype (halves time — same-day reconnoiter)

CANNOT CLAIM UNEXPLORED OR SIGHTED HEXES:
  If player attempts Claim Hex on a hex that is not DISCOVERED, DM rejects the action:
  "Your surveyors report they haven't fully mapped that territory yet.
   Spend a day reconnoitering first."
```

---

### Storybook Events — Format & Rules

> **Storybooks** are special narrative events in Pathfinder Kingmaker. They pause normal play and present a short illustrated text with numbered choices. Each choice has a skill check or immediate consequence. They are used for: major story moments, wilderness discoveries, companion interactions, and moments where the rules of the world briefly bend.

```
STORYBOOK FORMAT:
  Page header: [STORYBOOK — Title]
  Text: 2–4 paragraphs of atmospheric narration (3rd person, past tense, descriptive)
  Choices: Numbered list of 3–8 options
    Each choice shows: [Skill/Attribute DC X] or [No check — narrative choice]
    Some choices are unlocked only if a flag is set (e.g. [Requires: Amiri in party])

DM RULES FOR STORYBOOKS:
  1. Output the full page text before showing choices.
  2. Player selects ONE choice. DM resolves it.
  3. Some storybooks have multiple pages — resolve each page before advancing.
  4. Skill check outcomes follow standard PF2e degrees (Crit/Success/Fail/Crit Fail).
  5. XP is awarded for each page completed, shown in the choice resolution.
  6. Storybooks are NOT combat — they are narrative skill challenges.
  7. If player has no trained skill for a check, they can attempt untrained (usually harder DC).

STORYBOOK EXAMPLE FORMAT:
  [STORYBOOK — The Ancient Tomb, Page 1]
  Text: "The tomb entrance is sealed with stone. Old runes cover the lintel..."
  
  Your options:
  1. [Arcana DC 14] Read the runes — learn their meaning
  2. [Athletics DC 16] Force the stone door open  
  3. [Perception DC 12] Search for a hidden mechanism
  4. Turn back — this can wait
  
  → Player picks 2 (Athletics DC 16)
  → DM rolls: d20+[Athletics modifier] vs DC 16
  → Success: Door opens. +45 XP. Continue to Page 2.
  → Failure: Door holds. Try another option or come back with better tools.
```


```
Plains/Roads : 1 day (½ day with roads built)
Forest       : 2 days
Hills        : 2 days
River (ford) : 1 day + Athletics DC 14 to cross safely
Mountains    : 3 days
Swamp/Marsh  : 3 days
Hustle       : Halve travel time; gain Fatigued at end of day
```

### Random Encounter Chance (Per Hex Entered)
```
Plains   : 15%   Forest  : 25%   Hills    : 20%
River    : 20%   Mountain: 30%   Swamp    : 30%
Night travel: +10% to any terrain
Scripted: Each named hex also has 1 fixed encounter (triggers once only)
```

---

## 🗺️ THE STOLEN LANDS — WORLD MAP

> **DM:** Display this when player types `.map world`. Replace `[?]` with terrain symbol when discovered. Mark controlled hexes with `●`. Update after every hex entered.

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  THE STOLEN LANDS                                                        [Fog of War Active]       ║
║  Controlled: 0  Discovered: 0  Unexplored: 36+                                                    ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════╣
║          W-3       W-2       W-1        0        E+1       E+2       E+3        E                  ║
║  N+3  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
║  N+2  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
║  N+1  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
║    0  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]  ← Capital Row      ║
║  S-1  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
║  S-2  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
║  S-3  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════╣
║  ★ = Settlement   ⊕ = Trading Post   ⚔ = Military   ✦ = Temple   ◆ = Arcane Tower                ║
║  ♣ = Forest   ▒ = Hills   ∿ = River   ≈ = Swamp   . = Plains   █ = Mountain                      ║
║  ● = Controlled   ○ = Discovered   [?] = Unexplored   ✗ = Hostile   [@] = Your location           ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

> **DM:** As the player discovers hexes, update the grid. Each hex cell is 9 chars wide — show terrain + status + abbreviation. Example partially explored:
```
║  N+1  [  ?   ] [  ?   ] [  ?   ] [TotE✦○] [  ?   ] [  ?   ] [  ?   ] [  ?   ]                     ║
║    0  [  ?   ] [  ?   ] [ ◆  ○ ] [ ★  ● ] [OTP⊕●] [  ?   ] [  ?   ] [  ?   ]  ← Capital Row      ║
║  S-1  [  ?   ] [  ?   ] [  ?   ] [  ?   ] [ .  ○ ] [  ?   ] [  ?   ] [  ?   ]                     ║
```

---

## 📍 HEX MASTER INDEX — ALL NAMED LOCATIONS

> **DM:** Use `.hex [name]` to display the full detail block for any location. Index below shows all known locations. `[?]` = player has not discovered this yet — do not reveal name or details.

### CHAPTER 1 LOCATIONS (Greenbelt)

---

**HEX (1,0) — OLEG'S TRADING POST** `⊕` | Status: DISCOVERED at game start
```
Type     : Trading Post
Terrain  : Plains, northern Greenbelt
Ruler    : Oleg Leveton
Pop      : ~80 (Oleg, Svetlana, guards, traders)
Defense  : AC 18, HP 30
Economy  : +3
Morale   : ▮▮▮▮▮░░░░░ 50/100

Description: A fortified trading post on the frontier — thick timber walls,
reinforced corners, a gate that could hold against anything. Oleg built it
to last. Svetlana runs the books. The only reliable resupply point in the
northern Greenbelt. Recently harassed by Stag Lord bandits.

Buildings: Trading Post (+3 Economy), Barracks (under construction)

VENDORS:
  Oleg Leveton — General goods, ammunition, basic weapons, rations
  Bokken (nearby, visits weekly) — Potions, alchemical items

QUEST GIVERS:
  Oleg Leveton    → Deal with the bandits (main Ch1 hook)
  Svetlana Leveton → Retrieve her stolen wedding ring
  Jhod Kavken     → Find the Temple of the Elk
  Kesten Garess   → Capture/Kill Falgrim Sneeg

THREATS  : Bandit raids (weekly until Stag Lord defeated)
NOTES    : Starting base of operations. Companions dismissed here wait here.
           Kesten Garess arrives here ~Day 3 after prologue.
```

---

**HEX (0,0) — CAPITAL (PLAYER NAMES)** `★` | Status: FOUNDED by player (Ch1)
```
Type     : Settlement (Capital)
Terrain  : Shrike River confluence — player chooses exact location
Options  :
  A. River Confluence (0,0) — Trade bonus +2 Economy, flood risk
  B. High Ground (0,1)     — Defense bonus +4 AC, slower growth
  C. Forest Edge (-1,0)    — Culture bonus +2, harder to defend

Pop      : 0 at founding (grows each kingdom turn)
Defense  : AC 15, HP 20 (improves with buildings)

FOUNDING NOTE: Player chooses capital location in Ch1 after defeating
               the Stag Lord and securing the charter. This locks the
               coordinates for the campaign.
```

---

**HEX (0,1) — TEMPLE OF THE ELK** `✦` | Status: UNEXPLORED → Quest reward
```
Type     : Religious Site
Terrain  : Forest clearing, north of capital site
Ruler    : Jhod Kavken (after quest completion)
Pop      : ~20
Defense  : AC 16, HP 40
Culture  : +2  Loyalty: +1
Morale   : ▮▮▮▮▮▮░░░░ 60/100

Description: A serene clearing with an ancient stone altar to Erastil.
Overrun by a curse — a maddened bear guardian (actually a transformed
priest) patrols it. Jhod Kavken knows about this place and desperately
wants it reclaimed.

Quest: Find the Temple of the Elk (Jhod Kavken, Oleg's Trading Post)
  Reward: Jhod joins as free healer. Temple provides free Treat Wounds.
  Encounter: Maddened Bear (actually cursed priest) — CR 4
             When defeated: transforms back, dies peacefully, blessing the party.

Buildings (after quest): Temple (+2 Culture), Library (+1 Culture), Dormitory
THREATS: Maddened Bear Guardian (until quest complete)
```

---

**HEX (-1,0) — OLD SYCAMORE** `◆` | Status: UNEXPLORED
```
Type     : Ancient tree / Dungeon entrance
Terrain  : Forested plains, west of capital site
Description: An enormous ancient sycamore tree. Below its roots: a dungeon
shared by warring kobold and mite factions.

Surface Encounter: Mites scouting, kobold scouts (separate factions)
Dungeon: Mite Lair (Upper) → Kobold Warren (Lower)

QUEST HOOKS:
  Chief Sootscale — Kobold Warren below. Two resolution paths:
    Path A: Retrieve the sacred statue from Tartuk (the kobold shaman = Tartuccio in disguise)
            → Sootscale kobolds become allies (+2 Stability)
    Path B: Kill Tartuk directly
            → Kobolds scatter, no alliance, but Tartuk's notes are found (+lore)
  Tartuk = TARTUCCIO (his next appearance after the prologue)
    He has used Change Shape to disguise himself as a kobold shaman.
    Do not reveal this until the player discovers it through play.

LOOT (dungeon): Fangberries (Bokken's quest), Moon Radishes (Svetlana's recipe),
               Tartuk's personal journal (exposes his true identity), 85 gp
THREATS: Mites (CR 1/4 each, swarms), Kobolds (CR 1/4), Tartuk/Tartuccio (CR 3 as shaman)
```

---

**HEX (1,1) — NETTLE'S CROSSING** `∿` | Status: UNEXPLORED
```
Type     : River crossing / Ghost encounter
Terrain  : Shrike River, east fork
Description: A rickety rope bridge over the Shrike River. The ghost of
Davik Nettles haunts it. He was killed by the Stag Lord's bandits and
demands the Stag Lord's head be thrown into the river.

NPC: Nettle's Ghost
  Demand  : Throw the Stag Lord's head (or body) into the river
  Reward  : Safe crossing + Davik's ranseur (magic polearm, +1)
  If refused: Ghost attacks. CR 4 incorporeal ghost.

THREAT: Davik Nettles (ghost, CR 4) if not appeased
NOTE  : Must be resolved to cross the Shrike River safely in this area
```

---

**HEX (2,1) — SILVER MINE** `◉` | Status: UNEXPLORED
```
Type     : Resource (Silver Ore)
Terrain  : Hills, eastern Greenbelt
Economy  : +5 when developed (requires Establish Work Site kingdom action)
Description: Visible silver deposits. Low current danger. One collapsed
             tunnel with a trapped prospector (minor rescue encounter).

Opportunity: Establish Work Site → +5 Economy per kingdom turn
THREAT: Bandits may contest once it becomes known (Ch1 mid-game)
```

---

**HEX (-2,1) — THOUSAND VOICES GLADE** `♣` | Status: UNEXPLORED
```
Type     : Fey Forest Territory
Terrain  : Dense forest, western Greenbelt
Ruler    : Tiressia (Woodling Nymph)
Description: An enchanted forest filled with fey. Beautiful and dangerous.
A scythe tree has been threatening the nymph Tiressia's grove.

QUEST: Deal with the Scythe Tree (Tiressia, after finding the glade)
  Reward: Tiressia becomes a wilderness ally. Fey claim the hex peacefully.
          +2 Culture to any settlement built adjacent to this hex.
  Encounter: Scythe Tree (CR 5 plant creature)

THREAT: Scythe Tree (until quest resolved). Fey will be hostile if grove disturbed.
OPPORTUNITY: Fey trade agreement — rare alchemical plants (+1 Economy)
```

---

**HEX (0,-2) — SORROW MARSHES** `≈` | Status: UNEXPLORED
```
Type     : Swamp / Hazard Zone
Terrain  : Wetlands, southern Greenbelt
Description: A murky wetland filled with strange sounds. A hydra has been
             confirmed by hunters. Disease risk during travel (Fort DC 13).

THREATS  : Hydra (CR 6), Giant Frogs (CR 1), Disease (Filth Fever, Fort DC 12)
OPPORTUNITY: Rare swamp plants (+2 Economy if harvested, Survival DC 16)
             Alchemy ingredients (Old Beldame's requests)
NOTE     : Old Beldame lives in the swamp — see Swamp Witch Hut
```

---

**HEX (-2,-1) — SWAMP WITCH HUT** `⊕` | Status: UNEXPLORED
```
Type     : NPC Location (The Old Beldame)
Terrain  : Swamp edge
NPC      : The Old Beldame (witch, neutral, vendor)
Vendor   : Rare magic items, scrolls, potions — best selection in Ch1
Quest    : Retrieve her Black Rattlecaps mushrooms from the swamp
  Reward : Permanent access to her shop + minor magic item

APPROACH : She is suspicious. Diplomacy DC 14 to be received without hostility.
           If you find her mushrooms first (Sorrow Marshes), attitude starts Friendly.
```

---

**HEX (3,-1) — THORN RIVER BANDIT CAMP** `✗` | Status: UNEXPLORED (HOSTILE)
```
Type     : Bandit Camp
Terrain  : River bend, eastern Greenbelt
Ruler    : Kressle (half-elf Rogue, Stag Lord lieutenant)
Pop      : ~20 bandits
Defense  : AC 16 (palisade), HP 25

Description: A semi-permanent bandit camp on the Thorn River. Kressle
runs this outpost for the Stag Lord — collecting tribute from travelers.

NPC: KRESSLE
  Stats: AC 19, HP 24, Rapier +8 (1d6+4 Sneak), Evasion, Sneak Attack +2d6
  Loyalty: Mercenary. Betrays Stag Lord if offered 500+ gp AND safe passage.
  Pride trigger: Suggest she's weak or replaceable.
  Greed level: HIGH — very bribeable.

QUEST: Oleg asks you to deal with bandits. Kressle is the first named target.
LOOT : 127 gp, Masterwork Shortsword, Leather Armor, Kressle's personal journal
       (contains Stag Lord's password and fort layout hints)
```

---

**HEX (2,-3) — STAG LORD'S FORT** `✗` | Status: UNEXPLORED (HOSTILE)
```
Type     : Enemy Stronghold (Ch1 Final Encounter)
Terrain  : Forest ridge, southern Greenbelt
Ruler    : The Stag Lord
Defense  : AC 20 (stone fort), HP 80 (fort HP), 10+ defenders

Description: A crumbling stone fort repurposed by the Stag Lord's bandit
army. Heavy walls, archer towers, a basement dungeon. The Stag Lord himself
drinks himself to near-unconsciousness most nights — but is terrifyingly
dangerous in combat.

NPCS:
  The Stag Lord   — CR 7, must be defeated/captured for Ch1 completion
  Dovan           — CR 5, sadistic lieutenant. Not bribeable. Kill or neutralize.
  Auchs           — CR 4, dimwitted brute. Can be turned against Dovan.
  Akiros Ismort   — CR 5, former paladin. Can be turned against Stag Lord.
                    Diplomacy DC 16 + reveal his past = potential ally.
  Nugrah (basement) — Stag Lord's imprisoned father. Mad hermit druid.
                       Freeing him is optional but gives +25 XP and a blessing.

ENTRY OPTIONS:
  A. Direct assault — hard. Fort walls, archers, full garrison.
  B. Kressle's password — reduces guards by 2, patrol timing known.
  C. Disguise as bandits — Deception DC 16, fails if Stag Lord sees you.
  D. Sewer/basement approach — Thievery DC 14 to find hidden entry.
  E. Turn Akiros first — contact him separately, he opens a gate.

STAG LORD OPTIONS (once defeated/captured):
  Kill immediately      — Standard. Head can be sent to Jamandi (+50 gp reward).
  Behead and send head  — To Jamandi. Specific reward: +75 gp, Aldori commendation.
  Capture and imprison  — Requires Rope + Athletics DC 14. Can interrogate for
                          information about Nyrissa's early influence. Released
                          later he becomes a wandering neutral NPC.
  Turn over to Kesten   — Kesten arrives in 1d4 days to take custody.
  Execute publicly       — Affects alignment track (+Evil) but +5 Loyalty in kingdom.

LOOT: Stag Lord's Helm, 230 gp, Masterwork Longbow,
      +1 Leather Armor, Potion of Cure Moderate Wounds ×3, Letter from Nyrissa (story item)

Ch1 COMPLETION: Stag Lord defeated → Charter fulfilled → Kingdom founding begins.
```

---

**HEX (1,-1) — BOKKEN'S HUT** `⊕` | Status: DISCOVERED (near Oleg's)
```
Type     : NPC Location (Bokken the Alchemist)
Terrain  : Plains, south of Oleg's
NPC      : Bokken (eccentric hermit alchemist, friendly if approached calmly)
Vendor   : Potions, elixirs, alchemical items (visits Oleg's weekly)
Quests   :
  Find Fangberries (Old Sycamore area) — reward: 25% discount on potions
  Find Moon Radishes (plains hex)      — reward: free potions for 1 month
```

---

**HEX (2,-2) — SKUNK RIVER CROSSING** `∿` | Status: UNEXPLORED
```
Type     : River / NPC Encounter
NPC      : Jubilost Narthropple (gnome scholar, stuck cart)
Quest    : Help with his stuck cart (Athletics DC 12 or creative solution)
  Reward : Jubilost joins as scholar contact. Provides detailed maps of
           2 unexplored hexes. Vendor: maps and lore tomes.
  If you help him: `jubilost_met = TRUE` — he has information about the
                   Varnhold region (useful in Ch3).
```

---

## 📋 CHAPTER 1 QUEST INDEX

| Quest | Giver | Location | Objective | Reward |
|-------|-------|----------|-----------|--------|
| **Stolen Land** (Main) | Jamandi | Restov | Defeat Stag Lord, claim Greenbelt | Charter, Kingdom founding |
| Deal with the Bandits | Oleg | Oleg's (1,0) | Stop bandit raids | 200 gp + goods discount |
| Svetlana's Ring | Svetlana | Oleg's (1,0) | Recover wedding ring from Kressle's camp | 200 gp, morale boost |
| Find the Temple | Jhod | Oleg's (1,0) | Clear the Temple of the Elk (0,1) | Free healing, Jhod joins |
| Capture Falgrim Sneeg | Kesten | Oleg's (1,0) | Find deserter (random bandit encounter) | Masterwork weapons ×4 |
| Fangberries | Bokken | Bokken's (1,-1) | Gather berries (Old Sycamore area) | Potion discount |
| Moon Radishes | Svetlana | Oleg's (1,0) | Gather radishes (plains hex) | Free potions |
| The Scythe Tree | Tiressia | Glade (-2,1) | Kill scythe tree | Fey ally, +2 Culture |
| Black Rattlecaps | Old Beldame | Swamp Witch (-2,-1) | Find mushrooms in swamp | Shop access |
| Nettle's Crossing | Ghost | Crossing (1,1) | Throw Stag Lord's head in river | Magic ranseur, safe crossing |
| Sootscale Kobolds | Chief Sootscale | Old Sycamore (-1,0) | Resolve kobold/mite conflict | +2 Stability OR Tartuk lore |
| Bokken's Brother | Bokken | Bokken's (1,-1) | Find his estranged brother | Unlock potion crafting |
| Help Jubilost | Jubilost | Skunk River (2,-2) | Unstick his cart | Maps, lore vendor |

---

## 🏰 KINGDOM FOUNDING — CAPITAL SELECTION

> **Triggered when:** Stag Lord is defeated AND player returns to Oleg's Trading Post with the news. Jamandi's charter is officially activated.

**The DM presents three capital location options:**

```
══════════════════════════════════════════════════════
WHERE DO YOU FOUND YOUR CAPITAL?
══════════════════════════════════════════════════════
A. THE RIVER CONFLUENCE (0,0)
   Flat land at the joining of two streams. Easy to build.
   Bonus  : +2 Economy (trade hub), +2 Culture (crossroads)
   Risk   : Spring flooding (1/year, Fort DC 12 Stability check)
   Feel   : Merchant city. Grows fast. Hard to defend.

B. THE HIGH GROUND (0,1) — near Temple of the Elk
   A defensible ridge overlooking the Greenbelt.
   Bonus  : +4 to fort Defense AC, +1 Stability
   Risk   : Slower population growth (−1 to first 3 kingdom turns)
   Feel   : Military capital. Difficult to take. Slower start.

C. THE FOREST EDGE (-1,0) — near Old Sycamore
   The border of the great forest, near natural shelter.
   Bonus  : +2 Culture, free lumber for first 6 buildings
   Risk   : Fey complications (1/4 chance each kingdom turn of fey event)
   Feel   : Cultural capital. Artistic. Unusual. Fey interest.
══════════════════════════════════════════════════════
```

Player chooses. Record as `capital_location` in JSON Save Block. This is permanent.

---

## 📊 HEX TRACKING FORMAT (JSON Save Block)

```json
"hexes": [
  {
    "coords": [1, 0],
    "name": "Oleg's Trading Post",
    "status": "controlled",
    "cleared": true,
    "scripted_encounter_triggered": true,
    "buildings": ["Trading Post", "Barracks"],
    "notes": ""
  },
  {
    "coords": [-1, 0],
    "name": "Old Sycamore",
    "status": "discovered",
    "cleared": false,
    "scripted_encounter_triggered": false,
    "notes": "Tartuccio (as Tartuk) is here. Not yet confronted."
  }
]
```

---

> **➡️ CHAPTER 2–7 LOCATION DETAIL (Narlmarches, Kamelands, Varnhold, Glenebon, Pitax, Thousandbreaths, House at the Edge of Time) — see `KM_Map.md`. Pair-load with this file when entering Ch2+.**

---

*KM_Map.md — Kingmaker PF2e Text Adventure | Campaign Map v2.0 (split — pair-load with KM_Map.md and KM_Map.md)*


---

<!-- merged from KM_Map.md (v93.21 file consolidation) -->

# KINGMAKER — HEX LOCATION REFERENCE B
## KM_Map.md | Companion to: KM_Map.md | Active from: Chapter 2

---

> **DM:** This file contains all named hex locations sourced from the Kingmaker AP. KM_Map.md holds the coordinate system, hex status symbols, and Ch1/Ch3+ scripted locations. Use this file when the player enters or reconnoiters a specific named zone. Each entry notes encounter severity, level range, available resources, and whether the location is a Landmark (notable enough to name on the world map).

---

## 🗺️ ZONE REFERENCE — STOLEN LANDS & BEYOND

### Zone 0: Brevoy (Starting Region)

**BV1. RESTOV** — `Settlement 9` | *Landmark*
CN City. Population ~18,670. Cultural heart of Rostland. Swordlord stronghold.
- **Key NPCs:** Lady Jamandi Aldori (CG half-elf swordlord 14), Ioseph Sellemius (NG human aristocrat 5, Lord Mayor), Ezvanki Keegh (NG human cleric of Erastil 10)
- **Shop:** Aldori Dueling Swords available. High-level items (up to 15th level) accessible.
- **Kingdom note:** Restov remains a Brevic city — cannot be claimed, but diplomatic standing affects kingdom relations.

**BV2. NIVAKTA'S CROSSING** — `Settlement 1` | *Landmark*
CN Village. Population 140. Southernmost village in Rostland. Gossip bonus: +2 Diplomacy to Gather Information here.
- **Key NPCs:** Irven Revanisu (CN male human aristocrat 2, Mayor), Lorin Kaven (N male human ranger 2, Sheriff), Kara Ilarenika (N female human cleric of Pharasma 6)

---

### Zone 1: Rostland Hinterlands (RL) — Levels 1–2

**Random Encounter Table (d20):**
| Roll | Encounter | Severity |
|------|-----------|----------|
| 1–5 | 3 bandits (Stag Lord–adjacent, not affiliated) | Low 1 |
| 6–8 | 2 brush thylacines | Low 1 |
| 9–11 | 1 hunter (neutral; source of rumors) | Low 1 |
| 12–13 | 2 elk | Moderate 1 |
| 14–15 | 2 wolves | Moderate 1 |
| 16–17 | 2 boars | Moderate 1 |
| 18–19 | 3 thylacines | Moderate 1 |
| 20 | 1 grizzly bear | Severe 1 |

**RL1. OLEG'S TRADING POST** — `Landmark · Resource`
Starting hub. Full details in KM_Prologue.md and KM_Ch1.md.
- **Key NPCs:** Oleg Leveton (CG male human, Creature 1), Svetlana Leveton (NG female human, Creature 1)
- **Shop:** Basic adventuring gear; item level cap increases as campaign progresses.
- **Quests originating here:** Oleg's Trophy (tatzlwyrm head, reward: 5 lover's knots), Radish Soup (moon radishes from GB4, reward: 15 gp), Svetlana's Ring (bandit recovery quest)

**RL3. SPIDER NEST** — `Low 1`
Giant spider colony in an overgrown ruin. Standard arachnid hazard.
- **Loot:** Webbed cache — 1d4 × 10 gp in valuables, chance of trapped traveler's gear.

**RL5. FORT SERENKO** — `Landmark`
Ruined Brevic border fort. No active garrison. Strategic position; can be claimed as a watchtower site.
- **Kingdom:** Claiming grants +1 Stability and defensive coverage for RL zone.

---

### Zone 2: Greenbelt (GB) — Levels 2–4

**Random Encounter Table (d20):**
| Roll | Encounter | Severity |
|------|-----------|----------|
| 1–4 | 2 bandits | Trivial 2 |
| 5–7 | 1 tatzlwyrm | Low 2 |
| 8–10 | 2 wolves | Low 2 |
| 11–13 | Giant centipede swarm | Moderate 2 |
| 14–16 | 1 brush thylacine | Trivial 2 |
| 17–18 | 2 giant frogs | Moderate 2 |
| 19 | 1 kobold scouting party (4) | Low 2 |
| 20 | 1 shambling mound | Severe 3 |

**GB1. SNARE-FILLED GLADE** — `Trivial 2` | *Hazard*
Breeg Orlivanch's illegal trap network. The trapper is hostile and attacks if confronted.
- **Trap:** DC 18 Perception to spot; DC 20 Thievery to disarm; 2d6 piercing + Grabbed on fail.
- **Loot:** Breeg's camp — 45 gp, masterwork snare kit.

**GB3. FAIRY NEST** — `Moderate 2` | *Landmark*
A glade where First World energies bleed through. Pixies and sprites inhabit the area; hostile if disturbed.
- **Diplomacy DC 16:** Pixies share rumors about Nyrissa's influence in the Greenbelt (`nyrissa_awareness` flag available).
- **Loot:** Fairy dust (alchemical item, +1 to next Stealth check), 3 doses.

**GB4. MOON RADISH PATCH** — *No encounter*
Large patch of moon radishes near a kobold patrol route.
- **Survival DC 12:** Harvest a basket of moon radishes (Svetlana's Ring / Radish Soup quests).
- **Hazard:** 1d4 kobold scouts may be present (50% chance).

**GB6. TEMPLE OF THE ELK** — `Moderate 2` | *Landmark · Resource*
Ruined temple to Erastil, desecrated by a bear. Jhod Kavken (cleric NPC) wants it reclaimed.
- **Encounter:** Ferocious bear (Creature 4) guarding the temple — actually a cursed human.
- **Quest:** Jhod's quest. Defeating the bear purifies the temple.
- **Reward (Jhod):** Free healing at the temple for life. +1 to Erastil worship in kingdom.
- **Kingdom:** Claiming grants +1 Stability, free shrine (Erastil) in settlement if built here.
- **Loot:** Ruined treasury — 180 gp, scroll of heal (3rd level).

**GB10. SHRIKE CASCADE** — *Landmark*
Scenic waterfall on the Shrike River. No combat encounter; potential campsite.
- **Exploration:** Survival DC 13 to find cave behind waterfall — 1d4 × 20 gp in traveler's belongings.

**GB12. TUSKGUTTER'S LAIR** — `Low 2`
Den of Tuskgutter, an enormous boar (Creature 3). Oleg has a standing bounty.
- **Bounty:** Delivering Tuskgutter's head to Oleg: 250 gp.
- **Loot:** Tuskgutter's den — 50 gp scattered, 1 minor potion.

**GB13. RICKETY BRIDGE** — `Trivial 2` | *Hazard*
Partially collapsed rope bridge over a gorge. DC 21 Reflex save if bridge collapses (2d6 bludgeoning, fall to ledge below).
- **Engineering DC 15:** Repair in 1 day. Once repaired, becomes a local landmark.

**GB15. NETTLES' CROSSING** — `Moderate 2` | *Landmark*
Drowned ferryman Davik Nettles haunts this river crossing. He demands Stag Lord's body thrown in the river.
- **Quest trigger:** Nettles rises and makes his demand. Cannot be harmed until the Stag Lord is dead.
- **Reward (post–Stag Lord):** Davik's ranseur (magic ranseur, +1 striking).

**GB16. TATZLWYRM DEN** — `Moderate 2`
Pair of tatzlwyrms (Creature 2 each). Oleg's Trophy quest target.
- **Loot:** Tatzlwyrm hoard — 120 gp, 1 potion of darkvision.

**GB17. TRAPPED THYLACINE** — `Trivial 2`
Thylacine caught in a snare. Can be freed (no reward) or left (Nature DC 12 for favorable omen — Erastil worshippers get +1 to next Nature check).

**GB18. FANGBERRY THICKET** — `Moderate 2`
Thicket of fangberry bushes (thorns: DC 14 Acrobatics or take 1d4 piercing per 5 ft. moved).
- **Harvest:** Fangberries (alchemical ingredient) — 2d4 doses. Required for Bokken's quest (KB).
- **Encounter:** Spider swarm (Creature 1) in the thicket.

---

### Zone 3: Tuskwater (TW) — Levels 3–4

**TW1. A DELICATE SITUATION** — `Severe 3` | *Landmark*
Trapper camp with captive nixie (Melianse). Loggers hired by a local baron have cut her coachwood trees.
- **Resolution paths:** Kill the loggers (Melianse rewards with faerie pepper ×3), negotiate (loggers agree to replant if player provides feather token ×2, obtainable from Tiressia at KL1), or ignore (Melianse curses the loggers — Loyalty −1).
- **Quest:** Tiressia's Sister. Leads to KL1.

**TW5. LONELY BARROW** — `Landmark`
Ancient burial mound of a Kellid warrior. Mite infestation in the outer tunnels.
- **Dungeon:** 3 rooms. Boss: Mite King (Creature 2) + 6 mites.
- **Loot:** Warrior's sword (+1 longsword, cold iron), 200 gp in ancient coins.
- **Quest:** One of the Storyteller's relic fragments may be here (see KM_Exploration.md).

**TW8. OLD CRACKJAW'S DEN** — `Moderate 3`
Immense snapping turtle (Old Crackjaw, Creature 4) in a riverside den.
- **Bokken's request:** He wants Old Crackjaw's shell for alchemical components (reward: 6 potions of minor healing).
- **Loot:** Crackjaw's hoard (swallowed over decades) — 180 gp, 2 mundane items.

**TW9. GUDRIN RIVER FORD** — *Landmark*
Shallow crossing. Ambush site used by bandits (3 bandits + 1 veteran, Trivial 3).

---

### Zone 4: Kamelands (KL) — Levels 4–6

**KL1. TIRESSIA'S GROVE** — `Moderate 4` | *Landmark · Resource*
Grove of a dryad (Tiressia) and her satyr consort Falchos. Friendly if approached peacefully.
- **Quest:** Tiressia needs feather tokens (2) to convince loggers to leave her sister Melianse's trees (TW1). Reward: +1 to Diplomacy checks in Narlmarches for the session.
- **Kingdom:** Claiming with Tiressia's blessing: +1 Culture per turn while tree is standing.

**KL3. LAIR OF THE LIZARD KING** — `Severe 5` | *Landmark*
Cavern lair of Garuum, the Lizard King (Creature 6). Commands a tribe of lizardfolk.
- **Diplomacy DC 22:** Garuum can be negotiated with; he wants protection from the Stag Lord. Recruiting him: lizardfolk patrol nearby hexes (+1 Stability while active).
- **Loot:** Tribal hoard — 450 gp, +1 striking spear, ring of swimming.

**KL4. CANDLEMERE ISLAND** — `Severe 5` | *Landmark*
Island in Lake Silverstep. Ruined tower haunted by will-o'-wisps (Creature 6, ×2–3). Cult ruins beneath.
- **Dungeon:** Tower basement has 4 rooms. Clues to the Lantern King's interest in the region.
- **Loot:** Cult treasury — 600 gp, scroll of fireball, +1 resilient armor.
- **Kingdom:** Requires claiming the island hex separately from the shore hex.

**KL5. THE MUD BOWL** — `Severe 6`
A vast mud flat where a bull mastodon (Creature 7) has established territory.
- **Loot:** Mastodon tusks (50 gp each as trade goods), Survival DC 16 to find sunken cache (200 gp).

**KL7. HUNTER'S LODGE** — *Landmark · Resource*
Abandoned hunting lodge. No combat. Good resupply point; 1d4 days of rations available.
- **Kingdom:** Can be converted to a Ranger Station (grants +1 to Survival-based Region Activities).

**KL8. HUNTING GROUNDS** — `Moderate 5`
Disputed hunting territory. Two rival groups (4 hunters each) may be fighting when PCs arrive.
- **Mediation DC 18:** Resolve the dispute — reward from both groups (100 gp total, local goodwill).

**KL9. LAKE SILVERSTEP** — `Severe 4` | *Landmark · Resource*
Beautiful lake with a silver vein visible in the lakebed. Inhabited by a nixie tribe (friendly) and a nereid (hostile, Creature 6).
- **Resource:** Silver mine site — claiming grants +2 Economy per turn once a Mine is built.
- **Nereid:** Must be defeated or driven off before mine can operate safely.

**KL10. MUDFLATS** — `Moderate 6`
Alligator breeding ground. 3 giant alligators (Creature 5 each).
- **Loot:** Bone pile from victims — 80 gp, masterwork light shield.

---

### Zone 5: Narlmarches (NM) — Levels 5–8

**Random Encounter Table (d20):**
| Roll | Encounter | Severity |
|------|-----------|----------|
| 1–3 | 2 mandragoras | Low 5 |
| 4–6 | 3 boggards | Moderate 5 |
| 7–9 | 1 worg + 2 wolves | Moderate 5 |
| 10–12 | 4 cultists (Bloom-touched) | Severe 6 |
| 13–15 | 1 greater tatzlwyrm | Low 6 |
| 16–17 | 6 cultists | Moderate 6 |
| 18–19 | 1 will-o'-wisp | Low 6 |
| 20 | 1 hydra | Severe 7 |

**NM1. WARRIOR CAIRN** — *Landmark*
Kellid burial cairn. Undisturbed. Offering items here grants +1 to the next Lore check about Kellid history.
- **Exploration:** Perception DC 18 to find concealed burial goods (200 gp in ancient grave goods — taking them is Chaotic).

**NM3. DEAD UNICORN** — `Moderate 5` | *Landmark*
Slain unicorn, victim of poachers. The poachers (4) camp nearby.
- **Nature DC 14:** The unicorn's horn is still intact — returning it to Tiressia (KL1) grants a permanent +1 to Diplomacy checks with fey.
- **Loot:** Poacher camp — 150 gp, poaching equipment.

**NM5. THE FORGOTTEN KEEP** — `Moderate 6` | *Landmark*
Partially ruined Brevic fortification. Troll squad (3 trolls, Creature 5 each) has moved in.
- **Dungeon:** 5 rooms. Boss: Hargulka's lieutenant (Troll Guard, Creature 6).
- **Kingdom:** Clearing and claiming grants defensible outpost — +2 Stability, defensive coverage.
- **Loot:** 500 gp, +1 striking greatclub, troll-hide armor (medium, counts as hide).

**NM7. HARGULKA'S STRONGHOLD** — `Severe 7` | *Landmark — Ch2 Main Quest*
Troll fortress. Full details in KM_Ch2.md. Hargulka (Creature 8) + The Beast (mutant troll, Creature 9).

**SH1. DRAKE NEST** — `Moderate 6`
Swamp drake nesting site (2 drakes, Creature 5). Clutch of 4 eggs nearby.
- **Diplomacy (Draconic) DC 20:** Drakes tolerate presence; may serve as mounts for Kellid-blooded characters.
- **Loot:** Drake's cache — 350 gp, potion of fire resistance.

**SH3. ABANDONED FERRY STATION** — *Landmark*
Overgrown. Intact ferry cable across the Murque River.
- **Repair (Engineering DC 14, 2 days):** Restores ferry crossing; reduces travel time across the Murque.

**SH4. BEAST'S LAIR** — `Severe 7`
Lair of an owlbear (Creature 7, giant variant). Territorial.
- **Loot:** Scattered remains of victims — 200 gp, +1 resilient breastplate.

**SH5. GREENGRIPE** — `Moderate 6`
Vine leshy commune. Friendly to druids and rangers (auto-friendly); neutral to others (Diplomacy DC 16 to befriend).
- **Befriend:** Leshies serve as wilderness scouts — +1 to Survival-based Exploration checks in SH zone for remainder of chapter.

**SH6. WHISPERING GROTTO** — `Severe 7` | *Landmark*
Cave where First World energies are strongest. Aggressive atomies and sprites defend it.
- **First World portal:** Intermittently active. Perception DC 22 to notice. Foreshadows Thousandbreaths.
- **Loot:** Fey cache — 400 gp, bag of tricks (woodland).

**SH7. DRAGONLEAF GULCH** — `Moderate 6`
Gulch thick with dragonleaf plants (mildly toxic — DC 14 Fortitude or sickened 1 for 1 hour).
- **Crafting DC 14:** Harvest dragonleaf for alchemical antidote components (4 doses).

**SH8. CRADLE OF LAMASHTU** — `Severe 8` | *Landmark — Ch2 Main Quest*
Cult site. Full details in KM_Ch2.md and KM_Ch2.md.

---

### Zone 7: Dunsward (DS) — Levels 7–9

**DS1. NOMEN BURIAL MOUNDS** — `Severe 7` | *Landmark*
Sacred Nomen centaur burial ground. Hostile on approach unless Ekundayo is in party (neutral) or player holds Nomen treaty.
- **Diplomacy (with Ekundayo or Nomen treaty) DC 20:** Centaurs share information about Vordakai's tomb location.
- **Violating the mounds:** −2 to all Diplomacy with Nomen Heights for remainder of campaign.

**DS2. WEB LURKER LAIR** — `Moderate 7`
Giant web lurker colony (2 lurkers, Creature 8) in a canyon.
- **Loot:** Webbed victims — 300 gp, masterwork thieves' tools, scroll of web.

**DS3. KIRAVOY BRIDGE** — *Landmark*
Ancient stone bridge over the Kiravoy River. Intact but guarded by a territorial cave giant (Creature 9).
- **Diplomacy DC 24 or combat:** Must be resolved to use the bridge; bridge is the only safe Kiravoy crossing.

**DS4. SPIDER FIELDS** — `Severe 7`
Massive spider migration across open steppe. 1d4+1 giant tarantulas (Creature 6 each).
- **Survival DC 18:** Navigate around the migration without triggering combat.

**DS5. VARNHOLD** — `Settlement 5` | *Landmark — Ch3 Main Quest*
Empty city. Full details in KM_Ch3.md.

**DS6. BLOOD FURROWS** — `Moderate 7`
Site of an old battle between centaurs and undead. Shadows (Creature 4 ×3) linger.
- **Religion DC 18:** Perform Pharasmin rite to put them to rest (no combat needed) — reward: +1 to Spirit magic checks for 1 week.

---

### Zone 9: Tors of Levenies (LV) — Levels 9–11

**LV1. VARNHOLD PASS** — *Landmark · Hazard*
Mountain pass. Landslide hazard (DC 22 Perception to notice signs; DC 20 Reflex to avoid 4d6 bludgeoning).
- **Engineering DC 20:** Shore up the pass — removes landslide hazard permanently.

**LV3. CULCHEK CAVE** — `Moderate 9`
Cave system occupied by a roc (Creature 9). Nesting season — aggressive.
- **Survival DC 20:** Identify nesting season, approach without triggering combat.
- **Loot:** Roc's nest debris — 800 gp in coins/gems, +1 striking composite longbow (from a dead adventurer).

**LV4. THE GHOST STONE** — `Moderate 9` | *Landmark*
Weathered obelisk covered in Cyclops script. Detect magic active; DC 26 Occultism to read.
- **Translation:** Describes the location and nature of Vordakai's tomb. `ghost_stone_translated = TRUE` grants +1 to all checks inside Vordakai's Tomb.

**LV8. EMPTY DRAGON LAIR** — *Landmark*
Ancient dragon lair, long-abandoned. Smell of old smoke. Safe campsite.
- **Perception DC 22:** Find hidden cache in rear wall — 1,200 gp, +2 striking weapon (random type).

---

### Zone 10: Hooktongue Slough (HT) — Levels 10–12

**HT1. WYVERNSTONE BRIDGE** — `Moderate 10` | *Landmark*
Ancient stone bridge guarded by boggards who charge tolls. 6 boggards + 1 boggard champion (Creature 7).
- **Diplomacy DC 22:** Negotiate toll arrangement (10 gp per party per crossing) — avoids combat.
- **Kingdom:** Clearing and claiming this bridge improves trade route efficiency (+1 Economy).

**HT2. CLOUDBERRY FIELD** — *Resource*
Large cloudberry meadow. Passive gathering site.
- **Survival DC 12:** 2d4 days of rations harvested, or Herbalism: 1d4 doses cloudberry extract (+2 to next Fortitude save vs. disease).

**HT4. THE SINKING BOG** — `Trivial 10` | *Hazard*
Treacherous peat bog. DC 18 Perception to spot safe path; fail: Quicksand hazard (DC 20 Athletics to escape, 2d6 bludgeoning/round while sinking).

**HT6. M'BOTUU** — `Severe 11` | *Landmark — Dugeon*
Boggard tribe village in the swamp. Ahuizotl (Creature 10) is their "god." Full dungeon site.
- **Dungeon:** Village + underground cave, 6 encounter areas.
- **Loot:** Tribal treasury + ahuizotl hoard — 1,800 gp, +2 striking trident, pearl of power (4th level).

**HT8. DRAGONFLY GLADE** — `Severe 10`
Massive swamp drakes (3, Creature 8 each) roosting in a glade.
- **Loot:** Drake cache — 600 gp, +1 resilient scale mail.

**HT10. CHUUL LAIR** — `Moderate 10`
Chuul colony (2 chuuls, Creature 7) in a submerged cavern. Accessible only by swimming.
- **Loot:** Submerged cache — 500 gp, spell scroll of hydraulic torrent.

**HT11. LILY PATCH** — *Resource*
Exotic lily species with alchemical properties.
- **Nature DC 16:** Harvest 1d4 doses of soporific lily pollen (Crafting ingredient for sleep toxins or calming draughts).

**HT12. TOK-NIKRAT** — `Moderate 10` | *Landmark*
Ruined Cyclops outpost. Intact enough to recognize as Cyclops architecture.
- **Occultism DC 22:** Ancient carvings describe the cyclops empire — grants Cyclops Lore (Trained) until end of campaign.
- **Loot:** Sealed vault — 900 gp in ancient Cyclops coinage, eye-shaped amulet (amulet of the planes, 1/day only, destination is random).

**HT14. HYDRA DEN** — `Severe 10`
Six-headed hydra (Creature 9) guarding a riverside den.
- **Loot:** Hydra's accumulated prey — 700 gp, +1 striking longspear.

**HT15. SLUG BOG** — `Severe 10`
Giant slug (Creature 9) with an acid trail hazard through the area.
- **Loot:** Dissolved remains — 400 gp in acid-resistant gear, slime flask ×4 (alchemical splash weapon, 2d6 acid).

---

### Zone 11: Glenebon Lowlands / Dunsward Crossroads (DR) — Levels 11–13

**DR1. SPEARTOOTH'S DEN** — `Severe 11` | *Landmark*
Lair of Speartooth, a saber-toothed tiger of unusual intelligence (Creature 10). Not evil — territorial.
- **Nature DC 26 or Handle Animal DC 28:** Befriend Speartooth. She becomes a cohort animal companion (if player has the feat).
- **Loot (if killed):** Speartooth's kills — 1,200 gp scattered, +2 striking greatclub.

**DR3. WILD HORSES** — `Trivial 11`
Herd of 20+ wild horses. 1d4 aggressive stallions challenge intruders.
- **Nature DC 20 or Handle Animal DC 22:** Gentling a horse takes 1 day. Riding stock for the army (up to 6 horses captured).

**DR4. DESPERATE REFUGEES** — *Encounter (non-combat)*
Group of 12 refugees from Fort Drelev. They are fleeing Baron Drelev's rule.
- **Diplomacy:** Accept them → +1 population in nearest settlement, potential quest hooks about Fort Drelev.
- **Flags:** `drelev_refugees_met = TRUE` — grants +2 to first Diplomacy check in Fort Drelev (Ch4).

---

### Zone 12: Tiger Lord Territory (TL) — Levels 12–14

**TL2. GIANT'S CAVE** — `Severe 12` | *Landmark*
Cave of a storm giant (Creature 13, neutral). Reclusive; not hostile unless provoked.
- **Diplomacy DC 28:** The giant trades information about the Tiger Lords and Armag. He has seen Armag's Tomb location.
- **Loot (if provoked):** Giant's hoard — 3,000 gp, +2 striking greatsword, ring of the ram.

**TL3. ARMAG'S TOMB** — `Severe 13` | *Landmark — Ch4 Main Quest*
Full details in KM_Ch4.md.

**TL5. AURUMVORAX DEN** — `Severe 12`
Aurumvorax (golden gorger, Creature 12) den in a rocky hillside.
- **Loot:** Aurumvorax fur (worth 500 gp to the right buyer), scattered bones with items — 1,500 gp, +2 resilient breastplate.

**TL6. CHIMERA PRIDE** — `Severe 12`
Chimera pride (3 chimeras, Creature 8 each). Territory spans two hexes.
- **Loot:** Den — 1,000 gp, +2 striking halberd, chimera head trophies (decorative, 100 gp each as curiosities).

---

### Zone 13: Rushlight / Glenebon Border (RU) — Levels 13–15

**RU1. HEMLOCK ISLAND** — `Moderate 13` | *Landmark*
Island in the Sellen River. Used as a neutral meeting ground for River Kingdom disputes.
- **Kingdom:** Claiming Hemlock Island grants +1 Loyalty (neutral territory reputation).

**RU2. RUSHLIGHT FESTIVAL GROUNDS** — *Landmark — Ch5 quest site*
Full details in KM_Ch5.md (Rushlight Tournament section). Site of the annual River Kingdoms competition.

**GL1. TUSKER'S STOMPING GROUND** — `Severe 13`
Dire boar "Tusker" (Creature 12) with a herd of 8 regular dire boars.
- **Loot:** Tusker's territory is rich in truffles (Survival DC 14, 2d6 × 5 gp value) and timber (Lumber Resource site if claimed).

**GL2. MARSHALING GROUND** — `Severe 13` | *Landmark — Ch4/5 Army encounters*
Open field used by armies as a staging area. Fixed location for army-vs-army combat during Pitax war arc.

---

### Zone 16: Glenebon Uplands (GU) — Levels 16–17

**GU1. STEAMGROTTO** — `Low 16` | *Resource*
Volcanic hot spring grotto. No combat (unless disturbed).
- **Resource:** Rare mineral deposits — claiming grants +1 Economy and +2 max Ore per turn.
- **Exploration:** Alchemical ingredients in the vents (DC 20 Crafting to harvest, 1d4 doses of elemental flux).

**GU2. WHITEROSE ABBEY** — `Moderate 16` | *Landmark*
Half-ruined abbey, now a base for a notorious bandit queen (Creature 14) and her crew.
- **Diplomacy DC 30:** She can be recruited as a spy — grants +2 to Intrigue checks against Pitax.
- **Loot (if cleared):** Abbey treasury — 4,000 gp, +3 striking shortsword, robe of the archmagi.

---

### Zone 18: Thousand Voices / Branthlend Mountains (TV/BR) — Levels 18–19

**TV1. CASTLE OF KNIVES** — `Extreme 18` | *Landmark*
Nyrissa's forward stronghold in the mortal world. Full details in KM_Ch6.md (Ch6 section).

**TV2. THE WEEPING GROVE** — `Severe 18`
Ancient grove where a dryad queen was killed. Her spirit (Banshee, Creature 17) remains.
- **Diplomacy (if nyrissa_backstory_known) DC 34:** The banshee knows where the Lantern King's weakness lies — grants +1 to all checks in the final chapter.

**BR1. MOUNT BRANTHLEND** — *Landmark*
Highest peak in the Stolen Lands. No combat. Panoramic view.
- **Survival DC 20:** From the summit, spot 1d4 unexplored hexes that are automatically Sighted (no travel needed).

**BR2. ILTHULIAK'S LAIR** — `Extreme 19` | *Landmark*
Lair of Ilthuliak, an ancient black dragon (Creature 19). Optional boss.
- **Diplomacy DC 40 (near impossible) or combat.**
- **Loot:** Ilthuliak's hoard — 15,000 gp, +3 major striking weapon (any type), belt of giant strength +6, 3 rare spell scrolls (10th level).

**BR3. HUNGERDARK** — `Severe 19` | *Dungeon*
Underground complex once used by Cyclops necromancers. Active undead.
- **Dungeon:** 8 rooms. Boss: Greater shadow demon (Creature 14) + 4 shadows.
- **Loot:** Cyclops treasury — 8,000 gp, +3 resilient armor, staff of necromancy.

---

### Pitax (PX) — Level 13–16

**PX1. LITTLETOWN** — `Severe 13` | *Landmark*
Slum district outside Pitax proper. Irovetti's propaganda is weakest here.
- **Diplomacy DC 22:** Locals share information about Pitax defenses and Irovetti's movements.
- **Liberation track:** Each successful Diplomacy encounter here adds +1 to Liberation score (need 30 for Ch5 quest completion; see KM_Ch5.md).

---

## 💾 EXPLORATION FLAG REFERENCE

```
hex_entries:
  Each named hex should be flagged when entered:
    [hex_code]_entered     = TRUE (set on first entry)
    [hex_code]_explored    = TRUE (set after full Reconnoiter)
    [hex_code]_claimed     = TRUE (set after successful Claim Hex activity)
    [hex_code]_cleared     = TRUE (set after main encounter resolved)

  Resource hexes additionally:
    [hex_code]_resource_active = TRUE (set after Work Site established)
```

*KM_Map.md — Kingmaker PF2e Text Adventure | Hex Location Reference B*


---

<!-- merged from KM_Map.md (v93.21 file consolidation) -->

# KINGMAKER — CAMPAIGN MAP & HEX SYSTEM (PART C)
## KM_Map.md | Pair-load with KM_Map.md (and KM_Map.md as needed)
## Covers Chapter 2–7 named-location hex details.

> **DM:** Part C of the campaign map. Contains hex-by-hex location detail for Chapters 2 through 7. Pair with `KM_Map.md` (hex system, world map, Ch1 master index, capital selection, hex tracking JSON) and `KM_Map.md` (zone reference + exploration flags).

---

## 📍 CHAPTER 2 LOCATIONS (Narlmarches & Kamelands)

**HEX (4,-2) — SECLUDED LODGE** `⊕` | Status: UNEXPLORED
```
NPC     : Bartholomew Delbin (wizard, eccentric, friendly if not startled)
Quest   : Nature of the Beast — study troll regeneration weakness
Approach: Diplomacy DC 12 or knock before entering (he's paranoid)
Reward  : Potion of Fire Breath ×3 (50 gp each), Scroll of Burning Hands ×4,
          `troll_weakness_known = TRUE` — party gains +2 to attacks vs trolls
THREAT  : None — unless player is hostile
```

**HEX (-3,-2) — VERDANT CHAMBERS** `♣` | Status: UNEXPLORED
```
NPC     : Tiressia (Woodling Nymph, requires solo visit)
Trigger : Only accessible if tiressia_met = TRUE from Ch1 glade
Storybook: 3 pages. Guardian of the Bloom appears. Tristian's role revealed.
          `tristian_bloom_seeds_revealed = TRUE`
THREAT  : 3 monsters (Hydra, Manticore, Owlbear) — can be bypassed
```

**HEX (3,-3) — RUINED WATCHTOWER** `⟲` | Status: UNEXPLORED
```
NPC     : Ekundayo (taciturn ranger) + Trkaa (dog companion)
Recruit : Automatic if player agrees to help find Kargadd
Quest   : A Score to Settle — Kargadd is in Trobold Level 2
LOOT    : Masterwork Composite Longbow (in tower rubble, Perception DC 16)
```

**HEX (2,-4) — TROBOLD (DWARVEN RUINS)** `✗` | Status: HOSTILE (Ch2)
```
2-level dungeon. Troll kingdom. Hargulka's throne on Level 2.
Supply check: ensure fire/acid before entering (warn player if none)
Level 1: Sentinels ×4, Trollhounds ×6, Troll Shaman — see KM_Ch2.md
Level 2: Kargadd, Branded Trolls, Hargulka + Tartuccio
Key items: Trollreaper (fire-damage club), Iron Dwarven Key (opens deep vault)
Flags: `trobold_cleared`, `hargulka_fate`, `kargadd_killed`, `ekundayo_quest`
```

**HEX (-1,-3) — GOBLIN VILLAGE** `⊕` | Status: UNEXPLORED
```
Nok-Nok's former tribe. Bloom-corrupted elder controls them.
Approach : Diplomacy DC 14 (Nok-Nok in party: automatic peaceful entry)
Resolution: Kill the elder (Bloom recedes, goblins scatter) or
            Diplomacy DC 16 (cure elder via magic — requires Heal spell)
Quest link: Nok-Nok personal quest trigger if he's recruited
```

**HEX (1,-4) — BALD HILLTOP** `✦` | Status: UNEXPLORED
```
Barren hill with dead tree and stone circle — seat of the Ancient Curse.
Part 1: Wyvern ×2 (CR 7) guard the hill. Arcana DC 14 reveals seed point.
        Reward: 2,800 gp if cleared before Part 1 deadline.
Part 2: Bloom Manifestation boss (HP 140, fire weakness). Purify option available.
        Reward: 6,500 gp + 900 XP. `bloom_resolved = TRUE`
Flags: `bald_hilltop_p1_cleared`, `bald_hilltop_p2_cleared`, `bald_hilltop_resolution`
```

---

## 📍 CHAPTER 3 LOCATIONS (Varnhold Region)

**HEX (6,2) — VARNHOLD** `★` | Status: DISCOVERED (Ch3 opening)
```
Empty city. 300 vanished. Spriggans moved in.
Spriggan leader Agai: negotiate (Diplomacy DC 14) or fight.
Key items: Two story letters (one ends mid-word: "VORDAKAI"), Wand of Displacement
The Raven: appears here, confirms Vordakai's responsibility.
`varnhold_investigated`, `vordakai_identity_known`, `agai_fate`
```

**HEX (5,3) — OVERGROWN CAVERN** `⊕` | Status: UNEXPLORED (Ch3)
```
Defaced Sisters ×3 (cursed barbarian women, HP 44 each, AC 17)
Each carries one Cyclops Incense Burner — all 3 needed for Valley of the Dead.
With Amiri: non-hostile entry possible.
Without: full combat or Athletics DC 20 to impress them first.
```

**HEX (7,3) — KELLID BARBARIAN CAMP** `⚔` | Status: UNEXPLORED (Ch3)
```
NPC     : Dugath (camp leader)
Approach: Amiri = auto-peaceful. Diplomacy DC 21 or Athletics DC 20 otherwise.
Password for Sepulcher: "kheb" (Dugath tells player if relationship is good)
Sepulcher: Zombie Cyclops ×2 inside. Loot: Harbinger (earth breaker, deals double
           damage vs undead — crucial for Vordakai). Ancient Cyclops Coins ×2.
`kellid_friendly` based on approach
```

**HEX (8,4) — VALLEY OF THE DEAD** `▒` | Status: LOCKED (Ch3)
```
Requires all 3 Cyclops Incense Burners to open the gate.
Point of no return. Cannot exit until Vordakai is defeated.
Supply check: Death Ward scrolls, Lesser Restoration ×4, fire/positive energy sources.
Vordakai's Tomb: 2 levels, Willas Gunderson specter, Varnhold regent soul jar.
See KM_Ch3.md for full walkthrough.
`valley_entered`, `vordakai_fate`, `varnhold_regent_saved`
```

---

## 📍 CHAPTER 4–5 LOCATIONS (Glenebon & Pitax)

**HEX (0,5) — NUMERIAN STEPPES (Tiger Lord Territory)** `░`
```
Barbarian lands. Tiger Lord camp is the central location.
Approach: Amiri = less hostile. Diplomacy DC 28 to enter peacefully.
NPC     : Gwart (Tiger Lord dissident, can guide party)
Amiri's solo mission triggers here — she infiltrates to find Nilak.
`tiger_lord_hostile` until Ch4 resolved. `nilak_fate` set here.
```

**HEX (-2,4) — ARMAG'S TOMB** `⟲` | Status: UNEXPLORED (Ch4)
```
Entrance guardian: Zorek (Cleric 10 of Gorum) — see KM_Ch4.md for stats
Trial of Strength (DC 35 Athletics) and Trial of Pain (trap corridor, DC 30 Perception)
Two levels: Spectres, Dread Zombies, Greater Skeletons
Boss: Armag the Twice-Born (HP 220, Bastard Sword +5) — see KM_Ch4.md
Post-boss: Tiger Lord Chief selection. `armag_tomb_cleared`, `armag_fate`
```

**HEX (-4,2) — PITAX** `★` | Status: HOSTILE until Ch5
```
Irovetti's capital city. Academy of Grand Arts. Palace.
Military path: siege warfare, army combat, Brineheart first
Infiltration: sewers (Athletics DC 16), noble disguise (Deception DC 24),
              servant disguise (Deception DC 18)
Key NPCs: Irovetti (boss), Linxia (captain, defectable DC 28), Darven (merchant)
Loot: 8,400 gp vault, Ring of the Archmagi, Headband of Mental Perfection +4
`pitax_conquered`, `irovetti_fate`, `linxia_fate`
```

**HEX (-5,1) — BRINEHEART FORTRESS** `⚔` | Status: HOSTILE (Ch5)
```
First major Ch5 military engagement.
Fort: AC 22, HP 120, garrison of 8 soldiers + Linxia
Army assault OR player party direct assault (Athletics DC 16 to scale walls)
Linxia: Diplomacy DC 28 to defect (surrenders fort, +25,000 gp reward)
`brineheart_taken`, `linxia_fate`
```

---

## 📍 CHAPTER 6–7 LOCATIONS (Thousandbreaths & Beyond)

**HEX (0,-6) — THOUSANDBREATHS PORTAL** `◆` | Status: HIDDEN (Ch6)
```
Found in deep Narlmarches after Bloom reaches full manifestation.
Perception DC 22 to locate the portal (or follow Bloom corruption trail)
Entry: requires player to have entered Thousandbreaths consciously — no accident
`thousandbreaths_portal_found`
```

**THOUSANDBREATHS (Pocket Dimension)** `◆`
```
Nyrissa's domain. Not on the normal hex grid.
Dim light throughout (Low-light vision helps). Time distortion: Fatigued check every 2 rooms.
Enemies: Bloom Guardians, Nyrissa's Archers, Verdant Nightmare (boss room)
        See KM_Bestiary.md for stat blocks.
Linzi's death scene occurs at end of Phase 3 (before Nyrissa's chamber).
Linzi save option: if 4 conditions met, special dialogue available.
See KM_Ch6.md if shrine quest is active.
```

**HOUSE AT THE EDGE OF TIME (Extradimensional)** `★`
```
Nyrissa's true domain. Accessible only at Ch7 climax.
POINT OF NO RETURN. Companion quest audit required before entry.
Time overlaps: rooms show past/present kingdom simultaneously.
Bad ending: defeat Nyrissa without the dialogue. Lantern King wins.
See KM_Ch7.md Ch7 section for full content.
```

---

*KM_Map.md — Kingmaker PF2e Text Adventure | Campaign Map Part C v1.0 (Ch2–7 location detail)*


---

<!-- merged from KM_Map.md (v93.21 file consolidation) -->

# KINGMAKER — MAP TEMPLATES (VERBATIM, ASCII ONLY)
## KM_Map.md | Referenced by: KM_Commands_Maps.md, KM_DMRules.md, KM_PrePrologue.md

> **⛔ DM: COPY ONE OF THE 3 TEMPLATES BELOW EXACTLY. Do NOT generate a map
> from memory. Do NOT draw a rectangle with names and distances and call it
> a map. Fill in the symbols for the scene — do not change the structure.**
>
> **A map MUST have:**
> 1. Column letter headers (A B C D ...)
> 2. Row number headers (1 2 3 ...)
> 3. Grid cells (5-col wide for combat, 6-char wide for hex)
> 4. Symbol key at the bottom
>
> **Any output missing any of those 4 = NOT A MAP = `.fail 14`. Redraw.**

---

## ⛔ ASCII-ONLY RULE (NEW — read first, applies to ALL templates)

All maps use ASCII characters ONLY. No UTF-8 box-drawing. The DM previously
"translated" `║` to `||`, `█` to `■■`, `╔` to `+`, etc. — every translation
broke alignment. Fix: use only characters the DM can reliably reproduce.

**Allowed ASCII map characters:**
  `# . @ T E1 E2 E3 c : % - / + | * ! ? o ~ & ^ =`
  letters A–Z (column headers, companion initials, hex codes)
  digits 0–9 (row labels)
  spaces

**Banned characters in map output (any use = `.fail 14`):**
  `║ ═ ╔ ╗ ╚ ╝ ╠ ╣ █ · ░ ▓ ─ ┌ ┐ └ ┘ │ ★ ⁎ ▒ ♣ ● ✦ ∿ ≈`
  any UTF-8 box-drawing or geometric shape character
  any `[ ]` per-cell bracket wrappers (combat grid only — hex grid uses brackets)

---

## ⛔ AUTO-TRIGGERS — COMBAT (Template 1 grid required in same response)

If your response contains ANY of these, a full Template 1 combat grid MUST appear:

- "COMBAT INITIATED" / "Combat begins" / "Roll initiative"
- ".map combat" command from player
- An enemy has just moved, attacked, or appeared on the field
- Player typed an attack action that just resolved
- A trap, ambush, or surprise round triggered
- Start of any new combat round

Writing "COMBAT INITIATED" without an accompanying Template 1 grid = **instant `.fail 14`**.

---

## ⛔ AUTO-TRIGGERS — SCENE CHANGE (every new scene gets a map)

Whenever `current_scene` OR `current_location` changes, the DM MUST output a
map in the SAME response that introduces the new scene. No exceptions for
"intimate" or "narrative" scenes.

**Examples that fire this trigger:**
  - "Opening Scene" → first map of the game
  - "The Trip to the Manor" → travel/road map
  - "The Manor Banquet" → indoor scene map
  - Walking from one room to another inside the same building
  - Entering ANY new building, road, hex, or named area

**Template selection by scene type:**
  - Multi-room building (Manor, Inn, Dungeon level): Template 2 scene map
  - Single room or chamber: Template 1 grid (no enemies — walls + @ only)
  - Narrow corridor / alley: Template 1 sized 3–5 wide × 8–12 long
  - Overland travel / wilderness: Template 3 hex map
  - Combat scene: Template 1 with all enemies placed

**Map persistence:** If `current_location` is unchanged across responses (same
room, same NPC), the map need NOT redraw every response. It fires:
  1. The FIRST response in the new location, AND
  2. Any later response where positions, exits, or terrain changed, AND
  3. Whenever the player types `.map`.

**Missing map on scene/location change = `.fail 14`.**

---

## ❌ BANNED OUTPUT — DO NOT EVER DRAW THIS (instant `.fail 14`)

A label box is not a map. The DM has produced this in the past:

```
+----------------------+
|  ALLEY — DEAD END    |
|  WALL                |
|      [THIEF]         |   <- 20 ft from you
|      [eRmaC]         |
|      crowd           |
+----------------------+
Distance: 20 ft between combatants
```

**What is wrong:**
- No column letters, no row numbers
- No grid cells
- "WALL" written as text instead of `#` rows
- `[THIEF]` `[eRmaC]` as labels instead of `T` `@` placed on coordinate cells
- Distance asserted as text instead of derived from cell counting
- Symbol key missing

**Redraw using Template 1 below.**

---

## ⛔ TEMPLATE 1 — TACTICAL GRID (ASCII)

Copy the FORMAT exactly. Wrap output in a ```` ``` ```` code fence so monospace renders.

⛔ **TIGHT GRID — ONE CHARACTER PER CELL, ONE SPACE BETWEEN.** Each cell is a single
glyph; cells are separated by exactly ONE space (so cells read roughly square against
the row height). This packs far more map into the limited message width than the old wide
format — USE the space.

⛔ **AXES — NUMBERS ON TOP (columns), LETTERS ON THE SIDE (rows) (player directive
2026-06-23; SUPERSEDES the letters-on-top examples below).** Coordinate = COLUMN-NUMBER +
ROW-LETTER (e.g. `5B` = column 5, row B). WHY: **letters cap at 26 (A–Z); numbers don't** —
so the WIDTH axis (the screen-constrained one) uses numbers and is limited only by what
FITS, not by running out of letters. Rows use letters (≤26; you scroll vertically).
- ⛔ **ASCII SPACING = 1 CHAR + 2 SPACES (3-wide columns), SINGLE-ROW NUMERIC HEADER.** Each
  cell is one glyph + 2 spaces (3 chars wide); each column number sits in that 3-char slot
  (`1 ` padded, `10` exact, `16` exact) so 2-digit numbers fit on ONE clean header line — NO
  two-row stacking. Row label = letter + 2 spaces. Example:
  ```
     1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
   A #  #  #  =  #  #  #  #  #  #  #  #  #  #  #  #
   B #  .  .  1  .  #  .  .  .  .  #  ?  ?  ?  ?  #
   C #  .  @  .  .  #  .  K  .  .  #  ?  ?  ?  ?  #
  ```
  (The OLD two-row tens-over-units header is RETIRED — it read confusingly. Single row only.)
  (This snippet shows the 3-wide / single-row FORMAT only. The live night-attack floor is the FULL
   25×12 (cols 1–25, rows A–L) section in KM_CombatTurn.txt — the ASCII twin of the artifact.)
- ⛔ **WIDTH — THE ASCII AND THE ARTIFACT ARE EQUAL (player directive 2026-06-23).** They draw the
  SAME floor at the SAME size — identical geometry, tokens, and coordinates; the only difference is
  glyphs vs emoji. The standing floor is **25 columns (1–25) × 12 rows (A–L)**: two room bands of
  four rooms each, sharing single walls, split by a full-width corridor. At 3-wide, ~25 cols fits a
  maximized-Chrome message; past ~32 it wraps/scrolls. Never shrink the ASCII relative to the
  artifact (or vice-versa) — `.art` (KM_Map_Artifact.md) just renders the same map with emoji +
  tooltips + perfect alignment, and is the DEFAULT; the ASCII is the byte-for-byte FALLBACK twin.
- The examples below still show the OLD letters-on-top labels for the GRID BODY; apply the
  numbers-top / letters-side labeling above to them.

INTERIOR (room / building) example:
```
GUEST CHAMBER                         each square = 5 ft
Round 2 | init: eRmaC, Assassin

   A B C D E F G H
 1 # # # # = # # #
 2 # * . . . . . #
 3 # * . @ . 1 . #
 4 # . . . . . . #
 5 # * * . . . * #
 6 # # # / # # # #
```

EXTERIOR (wilderness) example — block glyphs carry the land:
```
FOREST ROAD                           each square = 5 ft

   A B C D E F G H I J K L M N
 1 ▓ ▓ ▒ ░ ░ ▒ ▓ ▓ ▓ ▒ ░ ░ ▒ ▓
 2 ▓ ▒ . ░ ░ . . ▒ ▒ . ░ ░ . ▒
 3 ▒ . @ ░ ░ . 1 . . ^ ░ ░ . ▒
 4 ~ ~ . ░ ░ . . . ^ ▲ ░ ░ . ▒
```

**LEGENDS — pick by map type.** INTERIOR is pure ASCII; EXTERIOR uses block glyphs
for terrain density. (Reconciles with the ASCII-only map ban: block glyphs `▓▒░` are
ALLOWED for OUTDOOR terrain only — interiors stay pure ASCII.)

  INTERIOR (rooms / buildings):
    #  wall      .  floor      /  door (opening in a wall)
    =  window    ~  fire / hazard
    *  furniture — bed, desk, chest, wardrobe, chair, etc. (cover; NAMED per cell in the KEY)

  EXTERIOR (wilderness / outdoor):
    ▓  dense forest / trees (blocks sight, difficult, full cover)
    ▒  light woods / scrub (partial cover, difficult)
    ░  road / path / trampled ground (clear footing)
    ~  water — lake / river / shallows
    ^  hill / rise      ▲  mountain / cliff (impassable)
    .  open ground / grass / plains

  CREATURES (letters & digits — used on BOTH legends):
    @  eRmaC (player)      1 2 3 …  enemies by initiative      +  allied NPC (non-companion)
    C  civilian / rescue target (named in KEY)
    ?  UNKNOWN / unscouted room interior (fog of war — see FLOOR-SECTION below)
    Companions — fixed single letters (TOKEN LEGEND below): L U K Y A S E R T B J H M V
    A SLEEPING / DOWN creature keeps its normal one-char token; note "(asleep)" / "(down)"
    in the KEY (do not invent a 2-char token for it).

⛔ **OBJECTS/TERRAIN ARE SYMBOLS; LETTERS ARE CREATURES.** Furniture/terrain use the
glyphs above; a bed/chair/tree is NEVER a letter (it collides with creature tokens =
`.fail 14`). Letters/digits are creatures only.

⛔ **EVERY CREATURE ON A FLOOR CELL OF THE GRID — `@` FIRST.** Each creature (player,
companion, enemy, civilian) MUST appear in an actual grid cell. ⛔ Naming a token only
in the KEY, or placing it on a `#` wall, = `.fail 14`: put it on the floor cell (e.g.
just inside the door). If a creature has no legal cell, the map is too small — grow it.

⛔ **HARD WIDTH CAP = 26 COLUMNS (A–Z).** The map width is bounded by the claude.ai
message content area at maximized Chrome, which fits ~26 single-space columns — never
exceed column **Z**. ROWS may run longer (the page scrolls vertically), so a TALL floor
section is fine. Size to FIT: every creature + object on its own cell with room to move;
grow toward the cap rather than cram. A door is always drawn (`/`), never implied.

⛔ **CELL FORMAT — 1 CHAR + 1 SPACE.** Each cell = exactly one glyph; cells separated by
a single space; header letters aligned above the cells; row number right-aligned. ⛔
BANNED: 4-space gaps (the old format), pipes (`| # |`), per-cell brackets (`[#]`),
doubled/mixed walls (`##`/`###`), 2-char tokens (`E1` → use a digit), UTF-8 box-drawing
(`║ █ ─ ┌`). Block glyphs `▓▒░` are allowed ONLY as outdoor terrain (above), never as
borders or interior furniture.

⛔ **FLOOR-SECTION VIEW — SHOW MORE THAN ONE ROOM (tactical intel, player directive
2026-06-23).** PREFER a FLOOR SECTION over a lone room: render eRmaC's room PLUS the
corridor outside and the adjacent rooms, within the 26-col cap. The player gets real
decision data — the doors, the layout, where to go, where to send a dispatched
companion, who needs rescuing.
  - ⛔ **ROOMS SHARE ONE WALL — NO DOUBLE/TRIPLE-THICK PARTITIONS, NO WALL-PADDING.** Two
    adjacent rooms share a SINGLE `#` partition (a real building's wall, not a gap of 2–3 `#`).
    And **extending the map means more CONTENT, not more wall** — if you widen it, fill the
    new space with **more rooms / corridor / terrain / occupants**, never a strip of redundant
    `#`. A wider map padded with walls is pointless; pack it with rooms. (E.g. four rooms
    sharing single walls fit where two rooms + dividers used to: `#.....#.....#?????#..C..#`.)
  - **The LAYOUT is KNOWN** (walls, doors, corridor of a place the player is lodged in).
  - **ROOM CONTENTS are FOG-OF-WAR:** an un-perceived room's interior is filled with `?`
    (one per interior cell), NOT its occupants. A room reveals (`?` → real contents) when
    the player perceives it — opens/looks through the door, scouts it, a DESTINATION CLUE
    gives it away (KM_PR_NightAttack_Rooms § DESTINATION CLUES), or a companion reports.
    ⛔ Showing the occupants of a room the player has NOT perceived = `.fail 9` (spoils the
    explore). Things the player legitimately knows (a teammate they know is lodged next
    door) MAY be shown.
  - **OCCUPANT TOKENS make the floor readable:** `1 2 3…` enemies · `C` a civilian/rescue
    target · a companion's letter for a teammate (KEY: "(asleep)" if they haven't woken,
    a wake/rescue opportunity). A revealed occupied room is a fight / rescue / wake-an-ally
    choice. POPULATION RULE holds — a revealed room holds ≥1 person or a fire.

⛔ **TOKEN LEGEND — ONE CHARACTER EACH (fixed; update only if the cast changes).**
  @ = eRmaC (player) · 1 2 3 … = enemies by initiative (name each under the grid) ·
  + = allied NPC (non-companion) · C = civilian/rescue.
  Companions — fixed single letters, never reused, never 2 chars. RULE: token = FIRST
  letter of the name (caps), or the SECOND if the first is taken — never a 3rd+ letter.
    L Leliana   U Hu Tao    K Keqing    Y Yor       A Aerith
    S Satsuki   E Velvet    R Revy      T Atalanta  B Bellatrix
    J Jaethal   H Harrim    M Amiri     V Valerie
  Every token on a single grid MUST be unique. Two of the same letter = `.fail 14`.

⛔ **KEY FORMAT — VERTICAL, CHARACTERS FIRST, THEN OBJECTS.** The legend under the grid
is a vertical list (one entry per line): a CHARACTERS block (every creature on the grid +
name + status) THEN an OBJECTS / TERRAIN block (each symbol + what it is + its cell).
Never an inline `·`-separated paragraph. Shape:
```
KEY:
  CHARACTERS
    @  eRmaC
    K  Keqing            (asleep, next room — can be woken)
    1  Assassin          (x if downed)
    C  manor servant     (rescue)
  OBJECTS / TERRAIN
    =  window ........... E1
    /  door ............. D6
    *  bed .............. B5
```

⛔ **NO MULTI-CHARACTER SYMBOLS / NO BOX BORDERS.** A wall is `#` (one char, never `##`).
No outer `+---+`, no `|` sides, no `===` — the code fence is the frame.

  ✓ CORRECT:   ` 3 # . @ . 1 . #`        (1 char + 1 space; enemy = digit, player = @)
  ✗ BANNED:    `  3    #    .    1    .    #`   (old 4-space format)
  ✗ BANNED:    ` 3 | # | . | 1 | . | # |`      (pipes)
  ✗ BANNED:    ` 3 # . E1 . #`                 (2-char token — use a digit)
  ✗ BANNED:    `3 [#] [.] [1] [.] [#]`         (per-cell brackets)

Any banned format = `.fail 14`. Redraw using the tight ASCII format above.

⛔ **SCENE-SHAPE RULE.** Before drawing, ask: what shape is this place IRL?
  - Narrow corridor / alley / hallway:  3–5 wide × 8–12 long
  - Small room (cell, study, shop):     6–8 wide × 6–8 long
  - Standard room (inn hall, guard):    10 wide × 8 long
  - Large chamber (throne foyer):       12 wide × 10 long
  - Open battle (clearing, plaza):      14 wide × 10–12 long
  - Set-piece maximum (siege, ritual):  15 × 15  ← HARD CAP

**SIZE UP WHEN THE SPACE ALLOWS — prefer the bigger map.** Within what the location
physically is, draw at the LARGER end of its band, and step up a band whenever the
fiction supports it (a hall that opens onto a courtyard, a chamber with alcoves, a
room with a loft). A bigger grid is the goal: it has room for cover, difficult
terrain, hazards, doors, elevation, and real positioning — which is the entire point
of a tactical map. Default high: standard room → 10×8 (not 8×6); large chamber →
12×10; an open fight → push toward 15×15.

⛔ **But fill the extra space with ACTUAL detail, never padding.** Every added row/
column must carry real content — a terrain symbol, cover, an exit, an enemy lane.
Empty floor stretched to look big = fabricated geography. And sizing up NEVER inflates
a small space: a corridor stays 3–5 wide no matter how much detail you want; a
14-wide alley = `.fail 9`. The ceiling is the REAL room, not the 15×15 cap. When a
scene file specifies dimensions (e.g. `Grid: cols A–E, rows 1–9`), those OVERRIDE all
of this.

**Two-digit row labels (rows 10–15):** use one less leading space.
`  10   #    #` (NOT `  10    #    #`). Same for 11–15.

**Starting positions:** Place party per `combat_formation` preset
(KM_Combat_Systems.md). Shield Wall = tanks front, casters 15 ft back. Skirmish
Line = 10 ft apart. Wedge = player point. Defensive Ring = casters center.
Ambush = two groups flanking. Custom = per `custom_positions`. If surprised,
scatter randomly within 20 ft.

---

## ⛔ TEMPLATE 1 — WORKED EXAMPLE: ALLEY DEAD END

This is the Pre-Prologue tutorial map. Copy as a reference for narrow scenes.

```
ALLEY — DEAD END                                   Each square = 5 ft
Round: 1 | Initiative: Thief -> eRmaC

       A    B    C    D    E
  1    #    #    #    #    #
  2    #    .    .    .    #
  3    #    .    1    .    #
  4    #    .    .    .    #
  5    #    .    .    .    #
  6    #    .    .    .    #
  7    #    .    @    .    #
  8    #    .    .    .    #
  9    #    c    c    c    #

ID    Name           HP       AC    Status         Distance from @
@     eRmaC          [X/Y]    [X]   -              -
1     Thief          [X/Y]    [X]   -              20 ft (C3)

TERRAIN: # = Wall   . = Open floor   c = Crowd (blocks exit)
EXITS:   South (row 9) blocked by crowd
```

Distance counting: @ at C7, 1 at C3. C7 → C6 → C5 → C4 → C3 = 4 cells = 20 ft.

---

## ⛔ TEMPLATE 2 — SCENE MAP (ASCII, exploration / indoor)

Copy exactly. Fill in room names and connections.

```
[LOCATION NAME] — [Sublocation]                            [@] = You

  +-------------------+      +-------------------+      +-------------------+
  |   [ROOM NAME]     |      |   [ROOM NAME]  *  |      |  [ROOM NAME]      |
  |   [status]        |------|   [status]        |------|  [status]         |
  |  [1-line detail]  |      |  [1-line detail]  |      |  [1-line detail]  |
  +---------+---------+      +---------+---------+      +---------+---------+
            |                          |                          |
  +---------+--------------------------+--------------------------+---------+
  |                       [CORRIDOR / HUB NAME]                              |
  |    !       !       !       [notes, DCs, hazards]                         |
  +---------+----------------------------------------+----------------------+
            |                                        |
  +---------+---------+    +---------------+   +-----+----------------------+
  |  [ROOM NAME]      |    | [ROOM NAME]   |   |     [ROOM NAME]            |
  |  [!] [status]     |----|  [status]     |   |     [@current]             |
  | [1-line detail]   |    | [detail]      |   |   [1-line detail]          |
  +-------------------+    +---------------+   +----------------------------+

[@]=You  [!]=Active event  *=Loot  !=Trap  [cleared]=Defeated  [locked]=DC
```

**Scene map rules:**
- Box corners use `+` only. Sides use `-` (top/bottom) and `|` (left/right).
- Room boxes are 21 chars wide by default; adjust per room name length.
- Connectors between rooms use `------` (horizontal) or `|` + spacing (vertical).
- No UTF-8 box-drawing. No `┌` `┐` `└` `┘` `─` `│` characters.

---

## ⛔ TEMPLATE 3 — HEX WORLD MAP (ASCII)

Copy exactly. Fill in hex contents per KM_Map.md. Hex cells DO use brackets
(unlike combat grid) because all hex codes are exactly 4 chars internal.

```
THE STOLEN LANDS — Hex Map
Discovered: [X] hexes | Claimed: [X] hexes | Season: [X] | Day: [X]

         A      B      C      D      E      F      G      H      I      J
  1    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  2    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  3    [Rst ][ ?  ][OTP*][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  4    [ ?  ][ ?  ][ ^  ][ &  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  5    [ ?  ][ ?  ][ &  ][ &  ][Slc ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  6    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  7    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  8    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  9    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  10   [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]

[@]=You  [?]=Undiscovered  *=Controlled  o=Discovered  Rst=Restov
OTP=Oleg's Trading Post  Slc=Sootscale
[^]=Hills  [&]=Forest  [~]=River  [.]=Plains  [#]=Mountain
[=]=Swamp  [+]=Road  Settlement names use 3 letters (Rst, OTP, Slc)
```

Each hex cell is 6 characters total: `[XYZW]` where XYZW is 4 chars internal.
Examples: `[ &o ]` = discovered forest, `[OTP*]` = controlled named settlement.

---

## 📋 PRE-OUTPUT SELF-CHECK (DM MUST RUN BEFORE SENDING ANY MAP)

Before outputting the map, the DM asks itself:
1. Does my output have column letter headers? (A B C D ...)
2. Does my output have row number headers? (1 2 3 ...)
3. Does my output use ONLY ASCII characters from the allowed list?
4. Does my output have a symbol key at the bottom?
5. Are all cells in each row the same width?

**If ANY answer is no:** STOP. Redraw from the template above. Do not send
a label-only box. The player will type `.fail 14` and you will have to
redraw anyway — just draw it right the first time.

---

## 🚪 PRE-PROLOGUE / TUTORIAL NOTE

The very FIRST combat map the player sees is in the Pre-Prologue gate scene
(if combat triggers via Path F/J/K/N). This is the tutorial — if the DM
renders a label-only box here, the player loses faith in the whole system.
**No exceptions. Full grid, first time, every time.**

---

*KM_Map.md — Kingmaker PF2e Text Adventure | ASCII-only map templates*
*v2.0: UTF-8 box-drawing removed. All 3 templates use ASCII only.*
*3 templates (combat / scene / hex) + worked alley example + pre-output self-check*
