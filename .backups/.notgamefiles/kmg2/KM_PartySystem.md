# KINGMAKER — PARTY MANAGEMENT SYSTEM
## KM_PartySystem.md | Referenced by: KM.txt, KM_P2.txt

> **DM:** Load this file every session from Chapter 1 onward.
> Apply party formation rules at all times. Enforce caps strictly.
> The `.party` command displays the current formation panel.

---

## ⚔️ PARTY FORMATION OVERVIEW

All recruited companions are distributed across three slots:

```
VANGUARD   : 6 members max — active combat party, player-controlled
REARGUARD  : 6 members max — scouting, independent missions, support
RESERVE    : unlimited — based at current home location, background characters
```

**Player always counts as 1 of the 6 Vanguard slots.**
Vanguard + Rearguard = active deployment. Reserve = home base.

---

## 🗡️ VANGUARD (Combat Party — Cap: 6)

- Player + up to 5 companions
- Player controls all Vanguard members in combat
- These are the characters at the player's side at all times
- Companion leveling, loot, and relationship scores apply normally

---

## 🔭 REARGUARD (Scouting / Independent — Cap: 6)

- Up to 6 companions operating separately from the Vanguard
- **Scouting:** Rearguard companions assigned to a hex report back intel (DM reveals one piece of information per hex scouted per session — terrain type, notable landmarks, enemy patrol size, or resource presence)
- **Independent missions:** Player may assign Rearguard to a named task (guard a location, negotiate with a faction, escort an NPC). DM resolves with a skill check using the assigned companion's relevant stat. Result arrives next session or after a set time period.
- **Mission assist:** Rearguard companions can arrive mid-mission as reinforcements. Player declares "call in Rearguard" — they arrive after 1d4 rounds. Player does NOT control them directly; DM runs them on their personality AI. This cannot be undone mid-combat.
- Rearguard companions are NOT present in the player's scene unless called in.
- Rearguard companions do NOT appear in ambient background beats while deployed.

---

## 🏕️ RESERVE (Home Base — Unlimited)

- All recruited companions not in Vanguard or Rearguard
- Located at the player's current primary base (Oleg's Trading Post in Ch1, Capital from Ch2 onward)
- **Ambient presence:** Reserve companions appear as background characters at the base. They have jobs, routines, and occasional ambient beats (see KM_Companions_Ambient.md)
- **Base activities:** Reserve companions take on tasks at the base automatically. DM assigns based on personality unless player specifies. Activities provide passive benefits.

### Reserve Activity Table
```
Companion type  → Default activity if unassigned
─────────────────────────────────────────────────────
TANK / FIGHTER  : Training yard — spars with guards.
                  Passive: guard morale +1 per session.
HEALER / CLERIC : Infirmary or shrine upkeep.
                  Passive: injured NPC recovery time −1 day.
ROGUE / RANGER  : Perimeter patrol or hunting.
                  Passive: 1 random food ration added per session.
WIZARD / CASTER : Library, lab, or magical maintenance.
                  Passive: one minor consumable crafted per session
                  (potion or scroll, Common tier, DM's choice).
BARD / SUPPORT  : Tavern, common room, or public space.
                  Passive: base morale +1; occasional rumor or
                  useful information surfaces.
INVESTIGATOR    : Records or intelligence work.
                  Passive: one local rumor or fact delivered
                  per session.
DRUID / NATURE  : Gardens, stables, or wilderness edge.
                  Passive: ration spoilage reduced; one
                  herbalism item added per session.
BARBARIAN       : Heavy labor — wall repair, hauling, clearing.
                  Passive: one structural repair completed per
                  session if base has damage.
```

Player may override any companion's default activity with a specific instruction. Reassignment takes effect the following session.

### Reserve Companion Interactions

Reserve companions are accessible whenever the player is at the base:

- Player may approach and speak to any Reserve companion at any time
- Conversations follow normal NPC thread rules (KM.txt)
- If a Reserve companion has a pending thread or question, they surface it within 2 player inputs of proximity
- Player may reassign their base activity through conversation or `.party` menu
- Relationship scores continue to develop through base interactions

---

## 🔄 PARTY SWAP MENU

Access via: `.party` → `[S] Swap` or say "open party menu"

```
═══════════════════════════════════════════════════
PARTY MANAGEMENT
═══════════════════════════════════════════════════
VANGUARD (X/6)     REARGUARD (X/6)    RESERVE (X)
[Player]           [Name — task]      [Name — activity]
[Name]             [Name — task]      [Name — activity]
[Name]             [Name — task]      [Name — activity]
[Name]             [Name — task]      [Name — activity]
[Name]             [Name — task]      [Name — activity]
[Name]             [Name — task]      [Name — activity]
───────────────────────────────────────────────────
[S] Swap members   [A] Assign task    [V] View companion
[R] Reassign base activity           [X] Close
═══════════════════════════════════════════════════
```

### Swap Rules

- To move a companion INTO Vanguard: a Vanguard member (not the player) must move to Rearguard or Reserve simultaneously. Vanguard cannot exceed 6.
- To move a companion INTO Rearguard: a Rearguard member must move to Vanguard or Reserve if Rearguard is full (6 cap).
- Reserve has no cap — any number of companions may be in Reserve.
- Swaps take effect at the start of the next scene (not mid-combat, not mid-encounter).
- **Exception:** After a mission where a new companion is found, the swap offer fires immediately (see New Companion Found below).

---

## 👥 NEW COMPANION FOUND — IMMEDIATE SWAP OFFER

When the player encounters and recruits a new companion during a mission:

```
[COMPANION FOUND — PARTY MANAGEMENT]
[Name] is ready to join. Your current formation:
  VANGUARD  (X/6): [list]
  REARGUARD (X/6): [list]

Options:
  1. Add to Vanguard → move [Name] to Rearguard/Reserve
  2. Add to Rearguard → specify slot or displace member
  3. Send to Reserve → [Name] goes directly to base
  4. Decline recruitment (companion defers, remains in area)
```

Player must resolve this before the scene continues.
If Vanguard is not full, player may add directly without displacing anyone.

---

## ⚔️ DIFFICULTY — ENCOUNTER SCALING

> **DM:** Read `game_options.difficulty` at session start and apply the matching tier to ALL encounters for the entire session. Applies regardless of party size. Do not announce the scaling to the player mid-scene.
> Default: **Easy**. Player sets with `.difficulty [easy/medium/hard]`.

| Stat | Easy | Medium | Hard |
|---|---|---|---|
| AC | +0 | +1 | +2 |
| Attack Bonus | +0 | +1 | +2 |
| Saving Throws | +0 | +1 | +2 |
| HP | baseline | +20% | +40% |
| Damage | baseline | +10% | +25% |
| Standard Encounters | baseline (1–3 mobs) | +2 mobs (3–5 total) | +3–4 mobs (4–7 total) |
| Boss Encounters | Boss + 1–2 minions | Boss + 2–3 guards (melee + ranged) | Boss + 3–5 guards (melee, ranged, caster) |

**Design intent:** Added guards and mobs exist to soak up extra party actions and force frontline splitting. Ranged and caster guards threaten the backline — the party cannot ignore them and dog-pile the boss. On Hard, large encounters may reach 8–10 total combatants.

**Named enemies (Tartuccio, the Stag Lord, quest bosses, etc.) receive all stat adjustments but are NEVER duplicated.** Count scaling applies to unnamed mobs only. Named bosses always remain singular.

**Guard types by difficulty:**
- Medium guards: 1 melee blocker + 1–2 ranged (archers, crossbowmen, thrown weapon users)
- Hard guards: 1–2 melee blockers + 1–2 ranged + 1 caster or specialist (a dog handler, a shaman, a trap-setter)

**Guard placement:** Guards enter pre-placed on the map flanking or behind the boss. They do not arrive as reinforcements — they are already there when combat begins.

**HP rounding:** Round up to nearest 5. Damage rounding: round to nearest whole number.

**Save block field:**
```json
"game_options": {
  "difficulty": "easy"
}
```

**Command:** `.difficulty` → show current setting | `.difficulty [easy/medium/hard]` → change

---

## 💎 LOOT QUALITY — ITEM DROP SETTING

> **DM:** Read `game_options.loot_quality` at session start. Controls both drop frequency and item tier. Independent of difficulty setting.
> Default: **Plentiful**. Player sets with `.loot [sustained/plentiful/saturated]`.

### Item Quality Tiers

| Tier | Description |
|---|---|
| **Rare** | Multi-affix magic items with random high-level rolls. Variable power — a well-rolled Rare can rival higher tiers. May be specific to certain monster types. |
| **Epic** | Named unique items with fixed stats. More powerful than most Rares. Cannot be modified with runes or charms. |
| **Legendary** | Apex items with the highest stats and unique proc effects. Cannot be modified. Extremely rare. |

### Drop Rate by Setting

| Setting | Rare | Epic | Legendary |
|---|---|---|---|
| **Sustained** | Major encounters + bosses only | Boss kills only | Almost never |
| **Plentiful** | Most encounters | Named enemies + bosses | Major bosses only |
| **Saturated** | Every enemy | Named enemies | Bosses + rare world drops |

**Sustained** — drops feel earned. Inventory stays lean.
**Plentiful** — well-stocked without clutter. Standard play experience.
**Saturated** — inventory filler. Sorting and selling is part of the loop.

**Save block field:**
```json
"game_options": {
  "loot_quality": "plentiful"
}
```

**Command:** `.loot` → show current setting | `.loot [sustained/plentiful/saturated]` → change

---

## 📊 PARTY SAVE BLOCK FORMAT

Add to every JSON Save Block under `"party_formation"`:

```json
"party_formation": {
  "vanguard": ["player", "", "", "", "", ""],
  "rearguard": ["", "", "", "", "", ""],
  "reserve": [],
  "reserve_activities": {}
}
```

`reserve_activities` format: `{ "CompanionName": "activity description" }`

---

## 🛡️ COMBAT FORMATION SYSTEM

> **DM:** When combat begins, place the Vanguard party on the ASCII grid according
> to the player's active formation preset. Formation determines starting positions
> ONLY — once combat begins, all movement is normal PF2e tactical movement.
> The player sets formation out of combat; it persists until changed.

### FORMATION PRESETS

**Access:** `.formation` → view current | `.formation [name]` → switch

```
╔══════════════════════════════════════════════════════════════════╗
║  COMBAT FORMATION                           Current: [PRESET]   ║
╠══════════════════════════════════════════════════════════════════╣
║  [1] Shield Wall    — tanks front, casters rear, tight cluster  ║
║  [2] Skirmish Line  — spread wide, no clustering, flanking      ║
║  [3] Wedge          — player point, party fans behind           ║
║  [4] Defensive Ring — casters center, melee surrounding         ║
║  [5] Ambush         — split two groups, pincer on contact       ║
║  [6] Custom         — player assigns each slot manually         ║
║──────────────────────────────────────────────────────────────────║
║  [V] View grid preview    [X] Close                             ║
╚══════════════════════════════════════════════════════════════════╝
```

---

### PRESET DETAILS

**Each preset defines a 10×8 deployment zone placed at the party's entry edge of
the combat grid. @ = player. Numbered slots = companion positions by role.**

#### [1] SHIELD WALL (default)
Tanks and melee hold a tight front line. Ranged and casters 15 ft behind.
Best against: head-on encounters, corridor fights, chokepoints.

```
  FRONT (toward enemies)
  ─────────────────────────
  Row 1:  [T1]  [@]  [T2]         ← tanks + player, shoulder-to-shoulder
  Row 2:  [M1]       [M2]         ← melee flankers, 5 ft behind
  Row 3:  [R1]  [S1] [R2]         ← ranged + support, 15 ft behind front
  ─────────────────────────
  REAR (entry side)
```
Bonus: Front row gains +1 circumstance to AC vs ranged attacks (shield overlap).
Penalty: Flanking from sides is easier — no side coverage.

#### [2] SKIRMISH LINE
Everyone 10 ft apart. Wide coverage, hard to AoE.
Best against: casters, AoE-heavy enemies, open terrain.

```
  FRONT
  ─────────────────────────────────
  Row 1:  [M1]     [@]      [M2]       ← melee spread 10 ft apart
  Row 2:     [T1]       [T2]           ← tanks staggered 5 ft back
  Row 3:  [R1]    [S1]      [R2]       ← ranged/support spread wide
  ─────────────────────────────────
  REAR
```
Bonus: AoE spells/breath weapons hit max 2 party members.
Penalty: No adjacent allies for flanking bonuses on round 1.

#### [3] WEDGE
Player at the point. Party fans out behind in a V.
Best against: charges, breaking through enemy lines, narrow approaches.

```
  FRONT
  ─────────────────────────
  Row 1:        [@]                ← player at the tip
  Row 2:    [T1]     [T2]         ← tanks flanking 5 ft back
  Row 3:  [M1]         [M2]       ← melee wider, 10 ft back
  Row 4:    [R1] [S1] [R2]        ← ranged/support at the base
  ─────────────────────────
  REAR
```
Bonus: Player gets +5 ft to first-round movement (momentum).
Penalty: If player is dropped, formation has no frontline — enemies reach casters in 1 move.

#### [4] DEFENSIVE RING
Casters and support in the center. Melee forms a perimeter.
Best against: ambushes, surrounded encounters, protecting a VIP.

```
  ─────────────────────────
       [T1]  [M1]  [T2]           ← melee north face
  [M2]                [M3]        ← melee east/west flanks (if 6 vanguard)
       [R1]  [S1]  [R2]           ← ranged + support in center
       [@]                         ← player south face (or center)
  ─────────────────────────
```
Bonus: Ranged/support cannot be engaged in melee without passing through a melee ally (triggers Reactive Strikes if available).
Penalty: Tight cluster — vulnerable to AoE.

#### [5] AMBUSH
Party splits into two groups placed on opposite sides of the encounter zone.
Only available when party initiates combat (not when surprised).
Best against: patrols, camps, enemies in the open.

```
  ═══════════════════════════════
  GROUP A (left flank):           GROUP B (right flank):
    [@]  [T1]  [M1]                [T2]  [M2]  [R1]
                                   [S1]  [R2]
  ═══════════════════════════════
           ENEMY ZONE
  ═══════════════════════════════
```
Bonus: All enemies are flat-footed on round 1 (flanked from two sides). +2 circumstance to initiative (Stealth-based).
Penalty: Groups cannot support each other for 1 round (15+ ft gap). If detected before combat, formation reverts to Shield Wall and ambush bonuses are lost.
Requirement: Stealth check (group's lowest Stealth modifier) vs enemies' Perception DC. Failure = detected, no ambush.

#### [6] CUSTOM
Player assigns each companion to a specific grid position.

```
.formation custom [Name] [row] [position]
```
Example: `.formation custom Artoria front left` / `.formation custom Sucrose back center`

Positions: `front/mid/back` × `left/center/right` (9 slots).
Player always occupies one slot. Custom formation persists until changed.

---

### ROLE ASSIGNMENT

> **DM:** When placing companions in formation slots, use their combat role:

| Role Tag | Slot Priority | Companions (Active 11 example) |
|----------|--------------|-------------------------------|
| **T** (Tank) | Front row | Artoria (#15), Tika Waylan (#35) |
| **M** (Melee) | Front/Mid row | Ryuko (#78), Olivier (#24) |
| **R** (Ranged) | Back row | Yoko (#39), Tatsumaki (#58) |
| **S** (Support) | Back row | Linzi (✦), Goldmoon (#21), Sucrose (#2) |
| **SK** (Skill/Flex) | Mid row | Kyoko (#43), Morrigan (#83) |

If a companion's role doesn't match a slot, DM places them in the nearest
appropriate position. The player can override any placement with `.formation custom`.

---

### FORMATION IN PLAY

**When combat starts, DM does the following:**
1. Check `party_formation.combat_formation` in save block.
2. Place all Vanguard members on the ASCII grid per the preset diagram.
3. Place enemies per the scene file.
4. If Ambush: resolve Stealth check first, then place groups.
5. Roll initiative normally.

**Formation does NOT:**
- Restrict movement after round 1 — companions move freely per AI/player orders
- Apply to Rearguard (they are not on the field unless called in)
- Stack with terrain bonuses (formation bonus is circumstance, follows PF2e stacking)
- Change mid-combat — it only determines starting positions

**Surprise encounters (party is ambushed):**
Formation is scrambled. DM places party members randomly within a 20 ft radius
of the party's travel position. No formation bonuses apply. Enemies get round 1
before initiative is rolled.

---

### SAVE BLOCK FORMAT

Add to `"party_formation"`:
```json
"party_formation": {
  "vanguard": ["player", "", "", "", "", ""],
  "rearguard": ["", "", "", "", "", ""],
  "reserve": [],
  "reserve_activities": {},
  "combat_formation": "shield_wall",
  "custom_positions": {}
}
```

Valid `combat_formation` values: `shield_wall` | `skirmish_line` | `wedge` | `defensive_ring` | `ambush` | `custom`

`custom_positions` format (only used when combat_formation = "custom"):
```json
"custom_positions": {
  "Artoria": "front_left",
  "Sucrose": "back_center"
}
```

---

## 📋 LEVELING — ALL COMPANIONS

**All companions level up simultaneously with the player.**
When the player's XP reaches the next level threshold, every recruited companion (Vanguard, Rearguard, and Reserve) levels up at the same time.

Leveling mode is set in game options (see KM_P2.txt):
- **Manual (default):** DM presents each companion's level-up choices one at a time. Player selects feat, skill increase, and ability boost for each. Uses tables from KM_Leveling.md / _B / _C.
- **Auto:** DM applies the documented automatic choices from the leveling tables without presenting options.

Reserve companions level up silently unless Manual mode is active — DM notes `[Name] reached Level X` in the base update, then presents their choices in Manual mode or applies auto silently.

*KM_PartySystem.md — Kingmaker PF2e Text Adventure | Party Management System v1.0*
