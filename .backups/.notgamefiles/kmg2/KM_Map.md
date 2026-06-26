# KINGMAKER — CAMPAIGN MAP & HEX SYSTEM
## KM_Map.md | Referenced by: KM.txt

---

## 🗺️ HEX SYSTEM REFERENCE

> **DM:** This file is the master map reference. Use it to track hex exploration, display the world map when the player types `.map world` or `.hex [name]`, and manage the kingdom territory as it grows. Update hex status in the JSON Save Block — `hexes[]` array.
> For full named hex location details (encounter severities, loot, quest hooks, resource flags) across all 18 zones, search **KM_Map_B.md** in project knowledge.

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

> **➡️ CHAPTER 2–7 LOCATION DETAIL (Narlmarches, Kamelands, Varnhold, Glenebon, Pitax, Thousandbreaths, House at the Edge of Time) — see `KM_Map_C.md`. Pair-load with this file when entering Ch2+.**

---

*KM_Map.md — Kingmaker PF2e Text Adventure | Campaign Map v2.0 (split — pair-load with KM_Map_B.md and KM_Map_C.md)*
