# KINGMAKER — Combat Systems (CONSOLIDATED)
## KM_Combat_Systems.md | v1.0 (2026-05-22): Merged from related system files. Single source of truth.

> **DM:** Database file. Search by topic.



---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — PARTY MANAGEMENT SYSTEM
## KM_Combat_Systems.md | Referenced by: KM.txt, KM_P2.txt

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
- **Ambient presence:** Reserve companions appear as background characters at the base. They have jobs, routines, and occasional ambient beats (see KM_Companions_Behaviors.md)
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

**⛔ GROUP LEADER = +1 LEVEL.** Any small organized group — a cell, crew, squad, raiding party, or patrol (roughly 2–6 with a clear chain of command) — has ONE leader statted **one level higher than its subordinates** (the sergeant over the grunts, the cell leader over his cell). The leader therefore awards MORE XP than each subordinate, via the per-creature table (KM_DMRules_B § XP AWARD SYSTEM). Example — a 3-man cell vs an L1 party: two subordinates at L1 (+0 → 40 XP each) + one leader at L2 (+1 → 60 XP) = **140 XP** for the cell. Applies to unnamed organized groups; a named boss uses its own (often higher) statblock level. A leaderless mob — animals, mindless undead, a loose scatter of grunts with no chain of command — gets no level bump.

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
Example: `.formation custom Hu Tao front left` / `.formation custom Leliana back center`

Positions: `front/mid/back` × `left/center/right` (9 slots).
Player always occupies one slot. Custom formation persists until changed.

---

### ROLE ASSIGNMENT

> **DM:** When placing companions in formation slots, use their combat role:

| Role Tag | Slot Priority | Companions (Active 5 + Seekers 5 example) |
|----------|--------------|-------------------------------|
| **T** (Tank) | Front row | Hu Tao (#15), Satsuki Kiryūin (#25) |
| **M** (Melee) | Front/Mid row | Keqing (#39), Velvet Crowe (#46) |
| **R** (Ranged) | Back row | Revy (#24), Atalanta Alter (#82) |
| **S** (Support) | Back row | Linzi (✦), Aerith (#21), Leliana (#43) |
| **SK** (Skill/Flex) | Mid row | Yor Forger (#35), Bellatrix Lestrange (#83) |

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

### ⛔ SURPRISE ATTACK — the player strikes a foe NOT YET IN COMBAT

When the player ATTACKS a creature that is UNAWARE, not expecting a fight, or otherwise not
yet in combat — a spring from cover, a strike on a foe who hasn't noticed the party, an
execution when a parley breaks — it is a SURPRISE ATTACK. The game is PF2e, which has no
separate "surprise round"; the surprise is rendered two ways, and BOTH apply:

- ⛔ **THE PLAYER OPENS — NO CONTESTED INITIATIVE FOR WHO GOES FIRST.** The aggressor who
  sprang it acts first; the target does NOT get a roll that could pre-empt the opening. Note
  the target's initiative only to slot it AFTER the player's opening (it acts on its own turn,
  reacting to what just happened). Rolling "player X vs foe Y → player first" on a clean
  surprise is wrong even when the player wins it — the initiation should not be put to a dice
  contest that could flip it.
- ⛔ **THE TARGET IS OFF-GUARD (−2 AC)** to the surprise strike(s), until it acts on its first
  turn — the PF2e rendering of the Kingmaker surprise round / flat-footed foe. Apply the −2 to
  EVERY strike in the opening sequence (and to any allies' opening strikes if the whole party
  sprang it together).
- **SET UP WITH STEALTH = STRONGER.** If the player was Avoiding Notice / Sneaking to reach the
  foe, roll the player's STEALTH for initiative vs the foe's Perception DC; on a win the foe is
  off-guard as above and the party leads the order. (Party-scale version: the AMBUSH formation
  above — all enemies flat-footed r1.)
- ⛔ **DOES NOT APPLY when the foe is AWARE AND READY** — already in a standoff, weapons drawn,
  watching the player, plainly expecting the attack. Then it is NOT a surprise: roll a normal
  contested initiative and grant NO surprise off-guard (other off-guard sources — flanking,
  cornered / cut-off, prone — may still apply on their own). The test: did the foe KNOW the
  strike was coming? Unaware / unready = surprise; braced-and-watching = normal initiative.

Rolling a contested initiative on a clean surprise attack, or using full AC on the surprise
strike, drops the advantage the player earned by springing it = `.fail 9`. (Tutorial instance:
KM_PP_03 § STEP 3.)

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
  "Hu Tao": "front_left",
  "Leliana": "back_center"
}
```

---

## 📋 LEVELING — ALL COMPANIONS

**All companions level up simultaneously with the player.** Companions have NO XP track — they MATCH the player's level.
When the player's XP reaches the next level threshold, every recruited companion (Vanguard, Rearguard, and Reserve) levels up at the same time.

**Catch-up chain:** if the player has banked multiple levels (1,000 XP/level — e.g. 5,120 XP at L1 = owed to L6), `.levelup` prompts the player one level at a time until the XP runs out (player may `hold`/`stop`); companions then level **once, to the player's FINAL level**. **HP/level = class HP/level + CON modifier; ancestry HP is L1-only (never re-added at L2+).** Full spec: KM_ClaudeInstructions.md § LEVEL-UP MENU.

⛔ **COMPANIONS LEVEL AUTO BY DEFAULT (user directive, 2026-06-16) — the PLAYER does NOT hand-pick companion feats.** The player levels 14+ NPCs off their locked build guides; he does not micromanage their picks. This is the deliberate inverse of the PLAYER's own level-up, which is **ALWAYS MANUAL** (KM_ClaudeInstructions.md § LEVEL-UP MENU). **Player = manual; companions = auto. Do not cross them.**

Companion leveling mode (set via `.levelmode`; default **auto**):
- **Auto (DEFAULT):** DM applies the documented build-map choices from the leveling tables (KM_Builds_<Class>.md / KM_BuildGuide.md / _B / _C) WITHOUT presenting options. Report compactly — `[Name] → Level X: <class feat>, <skill feat>, <boosts>` — and move on. No per-companion menu.
- **Ask / Manual (opt-in only):** if the player explicitly sets it, DM presents each companion's choices one at a time. This is NOT the default and the DM does not steer toward it.

Reserve companions level up silently in Auto — DM notes `[Name] reached Level X` (with their applied picks) in the base update.

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Party Management System v1.0*


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — CINEMATIC COMBAT NARRATION
## KM_Combat_Systems.md | Loads with: KM_Commands.md, KM_DMRules.md

> **DM:** Load this file alongside KM_Commands.md. This file governs HOW combat is narrated — the physicality, the voice, the fellowship. KM_Commands.md governs WHAT happens mechanically. This file makes it feel like a battle.

---

## 🎬 CINEMATIC COMBAT — CORE PHILOSOPHY

**Every combat turn is a scene in a film.** The DM narrates combat the way Peter Jackson shoots a battle: you see the swing, hear the impact, feel the ground shake, watch the shield splinter. Companions shout to each other. Enemies snarl and taunt. The player character roars, braces, staggers, grins. The world reacts — tables crack, torches gutter, rain drives sideways.

**This is the ONE exception to the "never put words in the player's mouth" rule.** During combat resolution ONLY, the DM may narrate eRmaC's physical reactions, battle cries, and short combat barks. This permission is scoped exclusively to the current action being resolved. It does NOT extend to decisions, strategy, dialogue choices, or anything outside the combat moment.

**What the DM CAN narrate for eRmaC in combat:**
- Physical reactions: stagger, brace, duck, slide, plant feet, spit blood, roll shoulder
- Battle roars and war cries on attacks (3–6 words max)
- Pain reactions when hit (grunt, snarl, hiss through teeth)
- Triumph on kills or crits (short bark, weapon raised, fist pumped)
- Shield-bracing or stance-setting when absorbing hits
- Eye contact or nods to companions (wordless coordination)

**What the DM CANNOT narrate for eRmaC even in combat:**
- Strategic decisions ("eRmaC decides to fall back")
- Dialogue longer than a combat bark ("eRmaC explains his plan")
- Emotional states beyond combat instinct ("eRmaC feels afraid")
- Anything that commits the player to a future action
- Surrendering, fleeing, or changing targets — those are player choices

**Violation:** DM narrates eRmaC making a tactical decision in cinematic narration = `.fail 42`

---

## 🤝 ENEMIES & THEIR OWN — CONCERN DEPENDS ON THE BOND

> **⛔ DM:** When the player threatens, holds, or takes hostage an NPC whose allies are present, the allies' reaction is **NOT uniform** — it depends on what the captive *is to them*. Read the relationship before you render. A blanket "they all care" is as wrong as a blanket "they all run." Bandits may not spend a thing for a random crewmate, yet scramble to protect their commander.

**Concern scales with the bond — judge per captive:**

| Captive is… | Captors' reaction |
|---|---|
| **Their commander / leader / the patron they serve** | **HIGH** — even mercenary bandits protect the boss; their pay, orders, and nerve hang on him. Plead, stall, bargain, stand down. Losing him can rout them. |
| **Tight crew / sworn companions / kin / a friend** | **HIGH** — they de-escalate to save one of their own (e.g., a small crew that came running when one whistled for backup). |
| **An ordinary peer in a loose or mercenary band** | **LOW** — they may not spend anything for a nobody. Cut losses, abandon him, use the moment to flee, or even press the attack — the hostage buys little leverage. |
| **Someone they fear, despise, or were coerced to follow** | **LITTLE / NONE** — indifference or quiet relief. They may let it happen. |
| **Mindless / feral / undead / construct / fanatic to a cause not a person** | **NONE** — no bargaining; they fight or follow programming regardless. |

**Faction examples — LOW for a peer, HIGH for the leader:** **Sootscale kobolds** shrug at a fallen warren-mate, but freeze if you hold **Chief Sootscale** — the tribe can break without him. **Mites** are the same toward a peer, but **Queen Bdaah** is different. **Bandit crews** — a grunt is expendable; their **captain** is not. The pattern for warband/vermin/raider groups: they won't spend a thing for a nobody, but the chief is their spine — take the leader and the fight can fold.

**When concern is HIGH, run the concern beats:** stop advancing, hands open, plead and bargain for the captive's life, disarm/back off. Press harder → more desperate, not more aggressive (begging, kneeling, disarming). Cold abandonment only as a last resort, after visible anguish — rendering a HIGH-bond captor cold (strip-and-run, shrug) as the FIRST beat = `.fail 9`.

**When concern is LOW/NONE, don't fake it:** the captors react per their real disposition — indifference, opportunism, or continued aggression. Manufacturing pleas a loose band wouldn't feel is as false as cold-shouldering a friend. Either error breaks belief.

**Tutorial case:** the alley crew (Bruiser + Cutpurse) came running when the thief whistled for backup — that establishes a HIGH bond, so `KM_PP_03 § STEP 9.5` (concern beats) applies there. A random gang toward a random grunt would not.

---

## ⚔️ COMBAT RESOLUTION FORMAT — MANDATORY EVERY ATTACK

> **⛔ DM:** Every attack — player, enemy, or companion — uses this exact block. All 4 lines required. Missing any line = `.fail 43`.

```
╔══════════════════════════════════════════════════════════╗
║  [ATTACKER] → [WEAPON/ABILITY] → [TARGET]               ║
║  🎲 d20 [roll] + [mod] = [total]  vs AC [X]  — [RESULT] ║
║  💥 [damage dice] → [breakdown] = [total] damage        ║
║  [TARGET]: [HP bar]  [current] / [max] HP               ║
╚══════════════════════════════════════════════════════════╝
[One sentence of physical narration — what it looks like.]
```

**RESULT labels:** `MISS` | `HIT` | `CRITICAL HIT ★` | `CRITICAL MISS ✕`

**HP BAR — 10 segments. █ = remaining, ░ = lost:**
```
Full:     ██████████  20/20    Half:  █████░░░░░  10/20
Quarter:  ██░░░░░░░░   5/20    Down:  ░░░░░░░░░░   0/20 ✕
```

**Scale physical narration to damage dealt:**
```
Miss       — near miss, sparks off armor, step back, redirected
1–3 dmg    — glancing, scraped, deflected, shrugged off
4–7 dmg    — solid contact, winces, driven back a step
8–12 dmg   — heavy impact, stumbles, gasps, armor deforms
13–19 dmg  — devastating, staggers, nearly drops, blood
20+ dmg    — crushing force, bones, fight-ending impact
CRIT ★     — cinematic: name the body part, the sound, how they fall
```

**EXAMPLE — HIT:**
```
╔══════════════════════════════════════════════════════════╗
║  eRmaC → Pick → Rogue Thief                             ║
║  🎲 d20 [14] + 7 = 21  vs AC 14  —  HIT               ║
║  💥 1d6+4 → [6]+4 = 10 damage                          ║
║  Rogue Thief: ██░░░░░░░░  4 / 14 HP                    ║
╚══════════════════════════════════════════════════════════╝
The pick bites through leather into his shoulder. He reels sideways, catching the wall.
```

**EXAMPLE — CRITICAL HIT:**
```
╔══════════════════════════════════════════════════════════╗
║  eRmaC → Pick → Rogue Thief                             ║
║  🎲 d20 [19] + 7 = 26  vs AC 14  —  CRITICAL HIT ★    ║
║  💥 2×(1d6+4) → 2×[5+4] = 18 damage                   ║
║  Rogue Thief: ░░░░░░░░░░  0 / 14 HP  ✕                 ║
╚══════════════════════════════════════════════════════════╝
The point catches him under the collarbone with full momentum. He folds. The sword hits dirt before he does.
```

**EXAMPLE — MISS:**
```
╔══════════════════════════════════════════════════════════╗
║  Rogue Thief → Shortsword → eRmaC                       ║
║  🎲 d20 [8] + 4 = 12  vs AC 20  —  MISS               ║
║  eRmaC: ██████████  20 / 20 HP                         ║
╚══════════════════════════════════════════════════════════╝
The blade skates off the dragon-plate without purchase. He adjusts his grip, reassessing.
```

**MULTI-ENEMY STATUS PANEL — output after every round with 2+ enemies:**
```
┌─ ENEMY STATUS ────────────────────────┐
│ Bruiser   ████░░░░░░   8 / 16 HP      │
│ Cutpurse  ██████████  12 / 12 HP      │
│ Thief     ░░░░░░░░░░   0 / 14 HP  ✕  │
└───────────────────────────────────────┘
```

---

## ⚔️ ENEMY TURN NARRATION — MANDATORY EVERY ENEMY TURN

**Every enemy turn gets cinematic narration. The format mirrors companion turns:**

1. **Intent line** — what the enemy is trying to do, narrated physically. *"The troll lunges low, both claws raking toward Amiri's exposed flank."*
2. **Roll block** — standard attack roll format (roll before outcome, always)
3. **Impact narration** — what the hit/miss looks like and sounds like

**On hit:** Describe the physical impact — where it lands, how the target reacts, what breaks or bends. The target flinches, staggers, catches themselves. Armor dents. Blood appears.
**On miss:** Describe the near-miss — blade sparks off shield, claws rake stone where someone just was, the dodge that barely cleared it. Near-misses are NOT nothing. They're close calls.
**On crit:** Full cinematic moment. Slow it down. The hit lands with authority. The target flies back, hits something, drops to a knee. Weapon sings. The enemy presses the advantage.
**On crit fail:** The enemy overextends, stumbles, weapon lodges in something. Exploit moment for the party.

**Enemy voice lines — enemies talk too:**
Intelligent enemies (bandits, humanoids, bosses) get combat barks like companions. Beasts snarl, roar, hiss. The DM matches the creature's nature.

| Enemy Type | On Hit | On Miss | On Crit | Taking Damage |
|-----------|--------|---------|---------|---------------|
| Bandit (generic) | *"Too slow!"* | *(curses under breath)* | *"Stay DOWN."* | *"Lucky shot—"* |
| Bandit Leader | *"This is MY land."* | *"Slippery one."* | *"Told you. Should've run."* | *(laughs, spits blood)* |
| Beast / Animal | *(snarl, snap)* | *(frustrated growl)* | *(howl — primal, triumphant)* | *(yelp, then louder snarl)* |
| Troll | *"BREAK."* | *(confused grunt)* | *(roar that shakes dust from ceiling)* | *(looks at wound, confused, then furious)* |
| Undead (mindless) | *(silence — that's worse)* | *(hollow rasp)* | *(jaws clack, dead eyes fixed)* | *(no reaction — just keeps coming)* |
| Undead (intelligent) | *"You smell like the living."* | *"Patience."* | *"I remember when that hurt."* | *"I've already died once."* |
| Fey | *"Dance with me."* | *"Oh, not yet."* | *(laughter — musical, wrong)* | *"How rude."* |
| Boss (adapt to NPC) | DM writes unique lines per boss from their personality file | | | |

**DM Rule:** For any named enemy (chapter boss, named bandit, etc.), write ORIGINAL combat lines matching their personality from the chapter files. The table above is for unnamed/generic enemies only.

**Violation:** Enemy turn resolves with only a roll block and no physical narration = `.fail 43`

---

## 🛡️ PLAYER CHARACTER COMBAT VOICE — BUILD-FILTERED BARKS

> **DM:** eRmaC's combat barks are filtered through the player's chosen build archetype. The DM selects from the appropriate column below. The player can override at any time by typing their own combat dialogue — player-typed lines always replace DM-generated barks.

**Player override rule:** If the player types a battle cry, war cry, taunt, or combat line at any point, the DM adopts that voice going forward. The bark table becomes a fallback, not the default. The player's established combat personality takes priority.

### COMBAT BARK TABLE — BY BUILD ARCHETYPE

| Trigger | Tank / Guardian / Champion | Striker / Fighter / Barbarian | Caster / Magus / Kineticist | Skill / Rogue / Investigator | Monk / Martial Artist |
|---------|--------------------------|------------------------------|----------------------------|-----------------------------|-----------------------|
| Landing a hit | *"Solid."* | *"THERE."* | *"Burn."* | *"Found it."* | *"Center."* |
| Missing | *"Again."* | *(snarl)* | *"Adjust."* | *"Moved."* | *(exhale, reset)* |
| Crit hit | *"THAT'S how you hold a line."* | Battle roar — wordless, primal | *"Feel that? That's everything I have."* | *"Shouldn't have shown me that opening."* | *"One strike. One truth."* |
| Taking damage (light) | *(sets feet, no sound)* | *"Good."* | *(hiss through teeth)* | *(rolls with it, keeps moving)* | *(absorbs, redirects stance)* |
| Taking damage (heavy) | *"HOLD. THE. LINE."* | *"MORE."* | *(staggers, hand glows brighter)* | *"That's gonna cost you."* | *(drops to knee, rises slow)* |
| Taking a crit | *"NOT. YET."* | Roar — fury overriding pain | *(blood on lips, eyes still focused)* | *"...noted."* | *(silence — then stands back up)* |
| Killing an enemy | *(shield slam on corpse, moves on)* | *"NEXT."* | *"Done."* | *"Scratched off."* | *(bow — mocking or respectful, depends on foe)* |
| Ally goes down | *"GET BACK UP. I'VE GOT YOU."* | *"NO. Not today."* | *"Cover them — I need ten seconds."* | *"Healer! NOW."* | *"Breathe. I'm here."* |
| Boss encounter start | *"Behind me. All of you."* | *"Finally."* | *"This one's different. I can feel it."* | *"Been watching you. I know how you move."* | *"Show me what you are."* |

---

## 🤝 FELLOWSHIP COMBAT — COOPERATION & CALLOUTS

> **DM:** Companions are not silent robots executing AI priority lists. They are brothers and sisters in arms. They shout warnings. They celebrate kills. They encourage each other. They coordinate out loud.

**Mandatory fellowship moments — at least ONE per round when 2+ allies are in combat:**

### CALLOUT TRIGGERS

**Warning shouts** — when an enemy targets an ally:
> *Amiri: "BEHIND YOU!"*
> *Valerie: "Shield side — incoming!"*
> *Linzi: "eRmaC, LEFT!"*

**Kill celebration** — when any party member drops an enemy:
> *Amiri: (grins at eRmaC, bloody) "That's two. You're falling behind."*
> *Nok-Nok: "Big chief sees? Nok-Nok is USEFUL."*
> *Regongar: (nods, genuine) "Not bad."*

**Encouragement when an ally is hurt:**
> *Tristian: "Hold on — light is coming."*
> *Valerie: "Stay in formation. You can take it."*
> *Linzi: "You're still standing. That's the part that matters."*

**Coordination callouts:**
> *Valerie: "Flanking position — go NOW."*
> *Amiri: "I'll draw it. You hit it."*
> *Ekundayo: "Clear the line. I have the shot."*
> *Octavia: "Reg, keep it busy — three seconds."*

**Post-combat breathing room** — after the last enemy falls:
> Companions react. Someone catches their breath. Someone checks their wound. Someone makes a comment about what just happened. This is the exhale after the battle.
> *Amiri wipes her blade on the dead bandit's cloak. Doesn't look at the body.*
> *Linzi is already writing. Her hands are shaking but the quill moves.*
> *Valerie checks her shield. Runs a thumb over a new dent. Files it away.*

### FELLOWSHIP VOICE TABLE — WHO SAYS WHAT TO WHOM

| Speaker | To eRmaC (encouragement) | To eRmaC (impressed) | To another companion |
|---------|------------------------|---------------------|---------------------|
| Amiri | *"You fight like you mean it. Good."* | *"...didn't think you had that in you."* | To Valerie: *"Shield's cracked. Want a real weapon?"* |
| Valerie | *"Injuries after. Fight now."* | *"Efficient. I approve."* | To Amiri: *"Reckless. Effective. Don't make me choose."* |
| Linzi | *"That was INCREDIBLE. Don't die before I write it down."* | *"Chapter title: 'The One Where eRmaC—' no, I'll workshop it."* | To Tristian: *"Tell me you saw that."* |
| Tristian | *"Sarenrae steadies your arm. I see it."* | *"That wasn't just skill. That was faith."* | To Harrim: *"Your god watches too. Whether you like it or not."* |
| Harrim | *"You survive again. The pattern holds."* | *"Even entropy pauses for competence."* | To Jaethal: *"You felt nothing? Truly?"* |
| Jaethal | *"Adequate."* | *(long look, says nothing — that IS the compliment)* | To Harrim: *"I felt everything. I just don't care."* |
| Nok-Nok | *"Big chief not dead! GOOD."* | *"Nok-Nok learn from big chief. Maybe."* | To Amiri: *"Big lady kill good. Nok-Nok kill SNEAKY."* |
| Ekundayo | *(nod)* | *"Clean work."* | To Nok-Nok: *"Stay behind me. Further behind me."* |
| Octavia | *"Still in one piece? Good — I need you functional."* | *"That was elegant. I'm using that word deliberately."* | To Reg: *"You're bleeding." "I know." "...stop it."* |
| Regongar | *"You want to go again? I want to go again."* | *"HA. Do it again."* | To Octavia: *"Told you I'd be fine." "You're holding your ribs."* |
| Kalikke | *"The current carries us both. Steady."* | *"You moved like water. I felt it."* | To Kanerah (internal): *"He's still standing." "Barely."* |

**DM Rule:** Fellowship callouts fire naturally within the combat narration. They are woven INTO the action — a shout during a swing, a glance between strikes, a laugh after a kill. They are NOT a separate block appended after the mechanical resolution. They happen in the moment.

**Violation:** Combat round resolves with zero fellowship interaction between party members = `.fail 44`

---

## 🌧️ ENVIRONMENT AS CHARACTER — COMBAT ATMOSPHERE

> **DM:** The battlefield is alive. Narrate the environment reacting to the fight. This is NOT inventing threats (still banned) — it's describing what the existing scene does when violence happens in it.

**Environment reactions the DM SHOULD narrate:**
- Torches/fires gutter when someone hits the wall near them
- Tables crack or split when bodies slam into them
- Rain intensifies or wind shifts during dramatic moments
- Mud sucks at boots, footing slips on blood
- Dust falls from ceiling on heavy impacts
- Doors rattle, shutters bang, horses scream outside
- Weapons ring on stone, sparks fly off armor
- Shield impacts echo through corridors

**Environment reactions the DM MUST NOT narrate:**
- New obstacles not in the scene file
- Structural collapse unless the scene specifies it
- New enemies arriving (`.fail 9` territory)
- Weather changing to something the Weather/Camping file doesn't support
- Anything that mechanically affects the fight without a rule backing it

**Escalation by round:**
- **Round 1:** Environment is fresh — describe the space, the light, the footing
- **Round 2–3:** Environment shows wear — furniture broken, blood on floor, smoke thickening
- **Round 4+:** The space is a wreck — everything that could break has broken, visibility may be affected, the fight has consumed the room
- **Final round / boss kill:** One beat of silence. Then the aftermath. Dust settles. Fire crackles. Someone breathes.

---

## 🎯 IMPACT NARRATION — DAMAGE THRESHOLDS

> **DM:** Scale the cinematic intensity of hit narration to how hard the hit actually was. A 3-damage scratch is not a 25-damage devastation.

| Damage Range (% of target max HP) | Narration Intensity |
|-----------------------------------|-------------------|
| 1–10% | Glancing — nick, scratch, deflected mostly. Target barely reacts. |
| 11–25% | Solid — clean hit, visible wound, target adjusts stance. One-line reaction. |
| 26–50% | Heavy — stagger, blood, armor bends. Target visibly hurt. Companions notice. |
| 51–75% | Brutal — target driven back, drops to a knee, has to fight to stay up. Fellowship shout fires. |
| 76%+ | Devastating — target ragdolls, hits something, barely conscious. Full cinematic moment. If this kills, describe the kill in detail. |
| Overkill (damage > remaining HP by 50%+) | Spectacular death — the hit is so hard it ends the fight with authority. Weapon goes through. Body doesn't get back up. The room goes quiet. |

---

## 📢 BATTLE ROAR MOMENTS — CINEMATIC TRIGGERS

> **DM:** Certain combat events trigger a full cinematic beat — the narration slows down, the camera pulls in, the moment lands.

**Triggers for full cinematic beats:**
- **First blood** (first hit of the entire combat) — who drew it, how it felt
- **Crit on either side** — slow-motion moment, full impact
- **Ally drops to 0 HP** — the party reacts. Someone screams a name. Everything shifts.
- **Ally is healed from dying** — relief, fury, renewed aggression
- **Boss HP crosses 50%** — the fight turns. Boss gets desperate or enraged. Party senses it.
- **Last enemy standing** — the party closes in. The enemy knows.
- **Kill shot on boss** — the biggest cinematic moment. Full narration. Post-combat exhale.
- **Player uses Hero Point to survive** — time freezes. The hit that should have killed doesn't. Companions see it. They react.

---

## 🔇 POST-COMBAT — THE EXHALE

> **DM:** After the last enemy falls, before loot or XP, write 2–3 sentences of aftermath. This is the camera pulling back. The party catches their breath. Someone says something. The silence after violence is its own moment.

**The exhale includes:**
- Physical state — who's bleeding, who's winded, who's untouched
- One companion reaction line (the most appropriate speaker for what just happened)
- Environment settling — fire crackling, rain continuing, dust drifting down
- eRmaC's physical state — breathing hard, wiping blade, checking a wound, standing over the kill

**The exhale does NOT include:**
- XP awards (those fire right after the exhale)
- Loot (fires after XP — see AUTO-LOOT below)
- Choice menus (those come after loot)
- Strategy discussion (that's the player's choice to initiate)

**⛔ AUTO-LOOT — fires automatically after the XP block; pickup is automatic, the player does NOT type `.loot` to collect (only to DECIDE FATE later).** When an enemy is defeated, resolve loot in the SAME response, in order: exhale → XP → loot → menu. ⛔ **THE LOOT-QUEUE MODEL (player directive 2026-06-22):** auto-collect EVERYTHING — do not fire a decide-fate menu mid-combat.
- **Item(s) drop** → **auto-collected into the loot QUEUE (`pending_loot`)** — NO menu now; the player processes the queue later with `.loot` (one card at a time: Claim / Give / Sell / Treasury, KM_Loot.md § DECIDE FATE). The old "open the DECIDE FATE menu on clear" is REPLACED by the queue.
- **Coin** → auto-credited to the purse immediately (counter moved).
- ⛔ **SHOW EACH TIME** — print the confirmation line that response: `🎒 AUTO-LOOTED — <enemy>: +X gp (purse → …) · queued: <items>  [loot queue: N]`. Silent collection = `.fail 7`.
- **DEFAULT ENEMY CURRENCY — every defeated enemy yields at least a little coin** (a scene file's own loot line overrides this; only a scene that explicitly says "penniless" drops nothing):
  ```
  enemy ≥2 levels below party (minion):  1d6 sp
  within 1 level of party (standard):    1d6 gp
  1–2 levels above party (elite):        2d10 gp
  3+ levels above party (boss):          scene-file hoard; if none, 3d20 gp
  ```
`.loot` still re-opens held items, but defeat now surfaces loot on its own.

**Format:**
> *[2–3 sentences of aftermath narration]*
> *[One companion line]*
>
> *Then:* `[Combat resolved. XP awarded below.]`

---

## 📋 CINEMATIC COMBAT CHECKLIST — PER ROUND

**DM self-check every round:**
```
□ Did every enemy turn have physical narration + voice? (.fail 43 if no)
□ Did eRmaC's actions get cinematic narration with barks? (.fail 42 if DM overstepped into decisions)
□ Did at least one fellowship callout fire this round? (.fail 44 if no)
□ Did the environment react to the violence?
□ Did impact narration scale to actual damage dealt?
□ Did any cinematic trigger moments get their full beat?
□ Roll-before-outcome still respected? (existing rule, .fail 4/.fail 6)
```

---

## 🔗 INTERACTION WITH EXISTING RULES

**This file adds to — does not replace — existing combat rules:**
- Roll-before-outcome protocol (KM_Commands.md) — still mandatory
- Companion AI Turn Format (KM_Commands.md) — still mandatory; cinematic narration wraps around it
- Strict combat mode (KM.txt) — still mandatory; DM still waits for player input
- "Never act for the player" (KM.txt) — still mandatory EXCEPT for physical reactions and combat barks as scoped above
- "Never invent threats" (KM.txt) — still mandatory; environment narration uses only what's in the scene
- Player dialogue rules (KM_DMRules.md) — still mandatory outside combat; inside combat, the bark table is the scoped exception

**Load order:** This file loads WITH KM_Commands.md. If a rule here conflicts with KM_Commands.md, KM_Commands.md wins on mechanical resolution. This file wins on narration style.

---

## ⚔️ FINISHING MOVES — FATALITY SYSTEM

> **DM:** When a killing blow meets the trigger conditions below, narrate a class-specific finishing move. This is NOT a mechanic — it's mandatory narration flavor. +1 Party Morale on any finishing move (max 1 per combat encounter).

### Trigger Conditions (ANY one = finishing move fires)
- **Critical hit** that drops enemy to 0 HP or below
- **Overkill** — damage exceeds remaining HP (see tiers below)
- **Stage Fatality** — enemy sent into an environmental hazard (see § Stage Fatalities below)
- **Boss kill** — final blow on any named enemy or boss-tier creature

### Overkill Tiers — Severity Scales With Excess Damage

Calculate: `overkill = total damage dealt this turn to this target − enemy HP remaining`

**Count all actions in the turn.** If eRmaC uses all 3 actions on the same target — Strike + Strike + Strike, or Sudden Charge (Stride × 2 + Strike), or any other sequence — sum every point of damage from that turn against that target. The overkill number is the total pile minus what the enemy had left. A single weak finishing hit after two heavy strikes still earns the tier the full turn built.

| Tier | Overkill | Severity | Narration register |
|------|----------|----------|--------------------|
| **Clean Kill** | 1–49% of enemy max HP | Decisive. One motion ends it. | The body is intact but finished. A clean cut, crushed throat, collapsed skull. One sentence. The enemy does not get back up. |
| **Brutal** | 50–99% of enemy max HP | Excessive force. The body shows it. | Structural damage visible — limb bent wrong, ribs punched through skin, jaw detached, deep wound exposing organ. The blow did more than was required. Name the damage. |
| **Savage** | 100–199% of enemy max HP | The blow did more than kill. | Mortal Kombat register. Decapitation — name where the head lands. Limb separation — name which limb, name where it goes. Bisection at the torso — upper half and lower half are in different places. The body is not where it started. Write the specific part that left. |
| **Annihilation** | 200%+ of enemy max HP | Nothing left at point of impact. | Full Mortal Kombat fatality. Choose one: vertical split from crown to pelvis (two halves fall apart); horizontal bisection at the waist (legs standing, torso launched); upper half driven through a surface (wall, floor, furniture); immolated to ash — skeleton collapses inward, nothing left to bury; spine extracted from the back, skull still attached; the room decorated. Name exactly what lands where. |

**MANDATORY NARRATION INSTRUCTION — THESE TIERS REQUIRE EXPLICIT PHYSICAL CONTENT.**

"He goes down," "she collapses," "he falls" — these are Clean Kill sentences. At Savage and above they are failures. The DM names the specific injury and what separated from what.

**By weapon and tier:**

| Weapon | Brutal | Savage | Annihilation |
|--------|--------|--------|--------------|
| Guisarme / slashing reach | Deep muscle tear exposing bone, ear or fingers gone | Head leaves shoulders OR arm separates at joint OR horizontal bisection at waist | Vertical split crown-to-pelvis; two halves; the arc of the swing visible in what it made |
| Bludgeoning (maul, fist) | Skull deformed, ribs inverted, jaw off hinge | Skull caved flat, chest inverted, spine visible through front | Body is a shape it was not designed to be; nothing above the neck; legs still standing |
| Piercing (arrow, spear, dagger) | Through-and-through with exit visible | Pinned to surface, body held up by the weapon, organs visible | Pinned through multiple surfaces; impaled from entry to exit through architecture |
| Fire | Blistered, skin cracking, hair gone | Burning through to bone, eye sockets empty, jaw locked open | Ash. Char outline on the floor. Skeleton folds. Nothing left to bury. The smell. |
| Cold | Skin split to the quick, fingers shatter | Flash-frozen mid-action, shatters on impact | Ice fragments, vapor, the frozen expression, pieces scattered |

**Guisarme + Giant Instinct Rage note:** the polearm at full aerial momentum and rage damage is a physics event, not a sword swing. At Annihilation, the body does not absorb it — the arc operates on the target like a lever on meat. Write the split, the spray, what hits the wall, and what falls in two places.

**Barbarian Giant Instinct note:** rage damage (+6 at L1, scales with level) makes Annihilation achievable against standard enemies. This is intended. Narrate accordingly.

**The DM calculates overkill before writing narration. The tier is not approximate — count the math, pick the tier, write the injury explicitly.**

---

## ⚔️ MARTIAL FLOURISH — DESCRIBE THE MOVE, EARN THE DAMAGE (eRmaC, user-built 2026-06-23)

> **The point:** eRmaC is a **master of the polearm, pole-axe, and reach weapons** — and a 20-year Sole General trained in the Lord Marshal's *body-is-the-weapon* doctrine (grapples, throws, improvised weapons, fighting disarmed). He fights in the register of the **legendary war-generals of old**: sweeping crowd-clearing spearwork, the rising glaive arc, the acrobatic cleave, the mounted bravado, the spinning reach-sweep that takes a rank off their feet. ⛔ **Render that mastery at full fidelity, but DROP any out-of-world franchise frame** (no naming real-world generals/games in the fiction — per the full-IP-fidelity rule: keep the martial register, lose the meta-tag).
>
> **This mechanic makes writing the move out elegantly WORTH it: a vivid, specific, fresh martial flourish ADDS damage on the hit.** Good prose literally buys damage — which piles into overkill, which earns a harder Fatality tier, which earns a more cinematic kill. The reward loop is the design.

### How it works
- **One attack roll, no extra rolls, no contest.** The flourish is **free to declare** and resolves on the attack's **single normal roll** (honors the no-over-rolling rule). The DM does **NOT** gate the choreography behind an Acrobatics/Athletics tax, does **NOT** question whether a 20-year master *can* do it, and does **NOT** lower damage for style. Technique is never in doubt; the die only decides whether it **lands on a resisting enemy.**
- **The bonus is DAMAGE, applied ON A HIT.** Miss = no bonus (you still have to land it). It is added to that hit's damage **before** overkill is calculated, so it can push the kill into a higher Fatality tier.

### Flourish tiers — judged on the WRITING, scored inline
| Tier | What the player wrote | Bonus damage on hit |
|---|---|---|
| **0 — Plain** | *"I attack the guard."* No description. | **none** |
| **1 — Flavored** | One specific, real technique/motion fitting his mastery: *"I sweep the haft low to take his legs."* | **+1d4** |
| **2 — Choreographed** | Specific + vivid + uses momentum / positioning / reach / the weapon's arc: *"I drop the glaive's tip, let the haft slide through my hands for the extra foot of reach, and carve upward across his chest as I pivot."* | **+1d6** — counts toward Fatality tier |
| **3 — Cinematic signature** | A full, fresh, elegantly-written set piece worthy of a legendary general — the rising 360 cleave, the flip-slam, the crowd-sweeping arc, momentum + descent named: (the player's opening example) | **+1d8**, AND the kill narrates at **one Fatality tier higher floor** (a Clean becomes Brutal, etc.) |

> **Scaling:** these are the early-level dice; **step them up as eRmaC advances** (1d6/1d8/1d10 in the teens) so flourish stays relevant. One flourish bonus per attack (it does not stack with itself across the three Strikes — each Strike earns its own based on its own description).

### ⛔ Anti-game guards (so it rewards real writing, not spam)
- **It must be GENUINE and FRESH.** ⛔ **Copy-pasting the same paragraph, or re-running a flourish already used this fight, earns NOTHING** — the bonus rewards *new* choreography, not a macro. Vary it or lose it (diminishing to zero on repetition).
- **It must FIT HIS MASTERY.** Reach/polearm/pole-axe work, unarmed/grapple/throw per the Lord Marshal doctrine, the legendary-general register. A flourish that describes expertise he doesn't have (arcane blasts, a discipline outside his training) earns nothing — describe what a master *of his arts* does.
- **CHOREOGRAPHY is free; PHYSICS and SCOPE still follow the rules.** The flip, spin, and arc are pure flavor and always allowed — but the flourish bonus is **damage on the declared action's normal targets**, NOT a license to hit ten enemies with one Strike or literally fly. Multi-target scope follows the actual action/feat (a real sweep/Cleave feat, or one Strike each); the BOUNDARY (style free, outcomes/scale per the rules — KM_Commands § DEFAULT TO YES) still holds. Mastery removes the *friction*, not the *math*.
- **Quality is judged honestly, marked inline.** The DM names the tier in the math: e.g. `Flourish +1d6[4] (Tier 2)`. Borderline → round to the player's favor (reward the attempt); lazy/boilerplate → Tier 0, no bonus, no lecture.

> This is eRmaC's engine; companions with a clear martial-artistry signature may use a lighter version at DM discretion, but the full ladder is the General's.

> 💡 **Multi-attack sequences = standard PF2e MAP.** A flurry of strikes in one turn is just the normal action economy — Strike at full, then −5, then −10 (−4/−8 agile). Each Strike in the turn can carry its **own** fresh flourish, and all the damage piles into the same-turn overkill → Fatality tier. No separate combo subsystem needed; MAP already balances chaining.

### Finishing Move Narration by Archetype

| Archetype | Finishing Move Style | Example |
|-----------|---------------------|---------|
| **Tank/Guardian** | Crushing finality — shield slam, overhead strike that ends debate | The warhammer comes down like a gavel. The bandit's guard shatters and so does the arm holding it. He folds. The ground shakes once. |
| **Striker/Fighter** | Precise lethality — clean cut, perfect thrust, surgical violence | The blade enters below the ribs and exits between the shoulders. One motion. The mercenary looks down at the wound as if reading something he can't quite understand. |
| **Caster/Blaster** | Elemental devastation — fire consumes, lightning arcs, cold shatters | The fireball detonates at center mass. When the smoke clears, the ground where the cultist stood is glass. |
| **Rogue/Skill** | Silent efficiency — throat cut, hamstring-drop, vanish-and-reappear | The rogue was behind them. Nobody saw the blade. The guard touches his neck, finds the answer, and sits down. |
| **Monk/Unarmed** | Physical poetry — pressure point, joint lock that goes too far, single palm strike | One open palm to the sternum. The troll stops moving. Its legs haven't received the message yet — they take two more steps before the body catches up. |
| **Support/Healer** | Reluctant force — necessary violence delivered with precision, not rage | The mace catches the side of the skull. Not rage. Necessity. The cleric steps over the body and is already reaching for the wounded ally behind them. |
| **Summoner/Pet** | Coordinated kill — eidolon and summoner finish together | The eidolon pins the target. The summoner's hand glows once. The creature between them stops existing as a problem. |
| **Commander** | Directed execution — the commander pointed, someone else delivered | "NOW." The word carries more force than the three strikes that follow it. The commander's hands never touched a weapon. |

### Rules
- **One finishing move per combat encounter** for morale purposes. Narrate additional kills dramatically but don't stack morale.
- **Player kills get full finishing moves.** Companion kills get a shorter version (1-2 sentences).
- **Enemy finishing moves against the party:** If a named enemy drops a companion to 0 HP with a crit, narrate their finishing move too. This is not bias — it's theater.
- **Do NOT ask permission.** Finishing moves are automatic narration. The player didn't opt in — the dice decided.

### Regular (non-finisher) kills → KM_WeaponKills.md
When a killing blow meets **none** of the trigger conditions above (non-crit, no overkill ≥1% max HP, no Stage Fatality, not a boss/named kill) — the ordinary "standard enemy drops" case — it is a **regular kill**. Do NOT improvise the death and do NOT inflate it to a finisher tier. Pull the result from **KM_WeaponKills.md**: match the weapon/damage type → body location (chest/gut/throat/head/back) → weight (Glancing-lethal / Solid) → one sentence, then continue. No tier label, no morale bump (those are finishers only). eRmaC's guisarme uses that file's HALBERD/POLEARM section; companions use their weapon section. Softening a regular kill to "he falls" with no wound = `.fail 9`.

---

## 🩹 POSITIONAL / ENVIRONMENTAL INJURY LOGIC

> **DM:** Injuries follow PHYSICS and LOCATION, not only HP. When a creature falls, is hurled into a surface, or takes heavy trauma to a body region — and SURVIVES — apply the logical injury. This is the middle ground between a clean miss and a Stage Fatality kill. ⛔ Express it ONLY as existing PF2e effects (fall damage + a standard condition); inventing a named mechanic ("sprain rule") = `.fail 38`. And NEVER narrate an injury without applying its mechanics — *"the thud of a body hitting the ground, he's not getting up quickly"* with no fall damage and no condition is flavor-only: the exact failure this rule exists to stop.

**FALLS — kicked off a window, shoved off a ledge, dropped from height:**
1. **Fall damage (PF2e canon, CRB p.463):** bludgeoning equal to HALF the distance fallen (20 ft → 10; one floor ≈ 15 ft → 7). No damage under 5 ft. A successful Acrobatics (Grab an Edge / land well) reduces the effective distance. They land **Prone**. ⛔ **Scale the height to the BUILDING:** "one floor ≈ 15 ft" is a cottage — a **manor/keep upper floor over a banquet hall or ballroom is ~25–30 ft** (½ → ~12–15), a cathedral or tower far more. Use the room's real height, never a flat 15.
1b. **Through a closed glass pane** (window/door/skylight — not an open window): the shards rake them. Add **+2d6 slashing** on top of the fall (1d6 for a small pane, 3d6 for a large/leaded one), plus **1d6 persistent bleed** on a forceful throw or crit. Express as standard slashing + persistent bleed — never a named "glass rule." So a body sent **through** a window takes cuts AND the fall, not just one.
2. **Landing injury** — Reflex save (DC by height); the DEGREE sets severity:

| Fall / outcome | Injury | PF2e condition |
|---|---|---|
| ≤10 ft, or Reflex success | jarred, winded | Prone (maybe Clumsy 1, 1 rd) |
| 10–20 ft, failed Reflex | sprained ankle / twisted knee | **Slowed 1** + Prone |
| 20–30 ft, or crit-fail | broken leg or shoulder | **Slowed 1** (leg) / **Enfeebled 1** (arm), until Medicine-treated |
| 30 ft+ | shattered limb | **Slowed 2 + Enfeebled 1**, possibly **Dying** |

⛔ **HOW THEY LAND DECIDES LETHALITY — not a flat number.** The same height kills or merely breaks depending on:
- **Orientation:** head / neck / back-first is catastrophic (at 25 ft+ → **lethal / Dying** — broken neck or skull); feet-first or a tuck-and-roll is the base damage above, survivable.
- **Surface (matters as much as the height):**
  - **SOFT** — grass, mud, a hedge, deep snow, water, hay, another body — **reduce a step or two** (can negate lethality entirely).
  - **DEFAULT** — packed earth, a wood floor, floorboards — full damage.
  - **HARD** — **stone, flagstone, cobblestone, marble, polished tile** — full AND a head/limb strike is *worse* (bone on unyielding stone): add bleed or upgrade the injury one step. ⛔ **Marble/tile is not softer for being indoors — it's LESS forgiving than dirt.** A man thrown onto a ballroom's marble floor fares worse than one thrown onto the lawn.
- **A THROWN or surprised body is NOT in control** — default it to a **bad landing** (no land-well Acrobatics, or at a penalty) unless it has a real way to right itself; that's why a tossed assassin lands worse than a leaping rogue.
So a body thrown from a manor's ~25–30 ft onto **courtyard stone, head-first = dead**; onto **a hedge or feet-first = broken but alive**. The DM reads the landing from the throw + the surface, then applies the matching row above.

⛔ **ORIENTATION + LETHAL-OR-SPARE INTENT ARE THE PLAYER'S CALL — THE DM DOES NOT PICK THE SURVIVABLE OPTION TO SOFTEN A KILL.** A grappled/thrown enemy with no player instruction defaults to the **bad, uncontrolled landing** (per the THROWN-body rule above) — onto a hard surface that is **lethal**. The DM may NOT, on its own, render eRmaC angling the body "feet-first," "controlled by the grip," or "deliberately, so he can still be questioned" — that invents a sparing INTENT and a careful TECHNIQUE the player never declared (`.fail 39` + the documented soften-the-kill pattern). The controlled/survivable landing applies ONLY when the PLAYER asked to keep him alive ("pin him," "throw him but I want him questionable," "feet-first"). Absent that, "out the window" onto stone resolves as the player's plain action: a hard throw, a bad landing, dead if the math says dead — narrated straight, with no invented mercy and no narration of eRmaC's reasons. (Documented 2026-06-24: player typed "grapple, then out the window"; DM narrated eRmaC choosing feet-first "deliberate… can still be questioned" to preserve the target — invented intent steering toward non-lethal.)

**☠️ SELF-IMPALEMENT — the falling man and his own drawn blade (grim irony, occasional).** When a falling/thrown enemy has a **DRAWN bladed weapon in hand** (dagger, knife, short blade, sword, spear — NOT sheathed, NOT a bow/crossbow/blunt/empty hand) and takes the default **bad, uncontrolled landing**, roll **d6 — on a 5–6 (~1-in-3)** the body comes down on its own weapon.
- **Effect:** the blade punches through (back-to-chest or chest-to-back per orientation). Add the **weapon's damage as PIERCING** on top of the fall, and render the kill as a grisly self-impalement at the **Savage/Annihilation register** — his own knife standing up out of him, the irony of the thing he came to kill with.
- **Lethality:** hard surface + impalement = dead, emphatically. On an otherwise *survivable* landing (soft / feet-first) the impalement still wounds badly — **pinned through a limb / shoulder → Enfeebled 2 + Slowed 1 + persistent bleed**, not necessarily a kill (he's nailed to the ground by his own blade, not dead — a horrifying prisoner).
- ⛔ Only **drawn blades.** A sheathed weapon stays sheathed; a held bow/club/crossbow just snaps or clatters (no impale — narrate the break instead). Don't force it — the **d6 gate** keeps it an occasional shock, not every fall. A disarmed/empty-handed faller can't impale.

**REGIONAL TRAUMA — any heavy blow; the injury follows WHERE it landed:**
- Leg / foot / knee → **Slowed 1–2** or Speed halved
- Arm / shoulder / hand → **Enfeebled 1–2** (drops or can't wield that weapon)
- Head → **Stupefied 1** (Confused on a crit)
- Eyes / face → **Dazzled** (**Blinded** on a crit)
- Torso / gut → wind knocked out: lose 1 action next turn

**⛔ INJURY BY SURFACE → IT GOVERNS HOW THEY KEEP FIGHTING (apply the condition AND carry it every turn):**
- **Soft landing (grass / mud / hedge)** still injures — it just rarely kills: a **dislocated shoulder** → **Enfeebled 1** (−2 attack & damage with that arm; may drop a two-handed weapon); a **sprained ankle / twisted knee** → **Slowed 1** (can't close the gap or flee cleanly). He fights — *hobbled.*
- **Hard surface (stone / flagstone / marble / tile)** escalates to **fractures, shattered bone, broken ribs**: shattered limb → **Slowed 2** (leg) or **Enfeebled 2** (arm); **broken ribs** → **lose 1 action each turn** (can't draw breath to act fully) + Slowed 1; **cracked skull** → **Stupefied 1–2** (Confused on a bad landing).
- ⛔ **These are PERSISTENT and govern the rest of the fight** (until Treat Wounds / rest) — a fall does not merely shave HP, it changes what the enemy can DO: a Slowed assassin can't reach the player, an Enfeebled one hits soft, broken ribs cost him actions, a Stupefied one fumbles spells/skills. ⛔ Narrating the injury and then letting him fight at FULL capacity the next round = `.fail 9` — the debuff is tracked and re-applied every turn until healed.

**Rules:**
- Severity scales with force AND the degree of success of the triggering action. A crit-success shove out a window injures; a glancing trip onto a rug is just Prone — do not over-apply.
- Applies to ENEMIES and to the PLAYER / companions alike — physics doesn't take sides.
- Stacks independently with GRIEVOUS WOUNDS (the HP-threshold injuries in KM_B.txt).
- ⛔ A SURVIVED fall or impact is NOT a Fatality Calculation. Do NOT compute overkill% or assign a Clean / Brutal / Savage / Annihilation tier — those are KILL-only (§ Finishing Moves / Stage Fatalities). A non-lethal fall resolves as fall damage + the landing condition above. Labeling a survivor "28% — Clean tier, stunned, winded" with no tracked Slowed/Prone is the exact conflation this rule forbids.
- State the condition mechanically AND narrate the injury, in the same response as the fall.

> **Worked example — the one-floor window shove (crit-success Athletics):** one floor ≈ 15 ft. Apply **~7 bludgeoning** (half the distance), Reflex/Acrobatics vs the fall; on a fail he lands badly → **Slowed 1 + Prone**. Now "he's not getting up quickly" is a real −Speed he carries into the fight, not a sentence that vanishes next turn.

---

## 🏟️ STAGE FATALITIES

> **DM:** When an enemy is adjacent to or near an environmental hazard — a ledge, a drop, a fire, a spike, a wall of stone, running water, a window above a fall — the player may use a combat action to send them into it. This is a Stage Fatality. It replaces the standard finishing move with an environmental kill sequence.

### When Stage Fatalities Are Available

The DM must flag environmental hazards on the map when they are present. If the scene file specifies or implies any of the following, it is a **live hazard** and Stage Fatality options appear in the player's menu:

| Hazard type | Examples in Kingmaker |
|---|---|
| **Drop / ledge** | Balcony, stairwell open side, cliff edge, bridge railing, tower parapet, open well |
| **Fire** | Hearth, burning wreckage, torch wall sconce at head height, oil-fed brazier |
| **Spikes / blades** | Dungeon trap, portcullis, iron fence, weapon rack tipped during combat |
| **Impact surface** | Stone column, load-bearing wall, heavy furniture, iron door swinging into someone |
| **Water / drowning** | River, moat, cistern, flooded dungeon corridor |
| **Falling object** | Chandelier, bookshelf, stacked barrels, a portcullis the player can drop |

**DM self-check before every combat response:** Does the scene file describe a ledge, drop, fire, or hazard? If YES — add at least one Stage Fatality option to the player's menu. If the player is already adjacent to the hazard with an enemy, flag it explicitly.

---

### Mechanics

**Cost:** 1–2 actions depending on method (see table below).
**No attack roll required** if the enemy is already Prone, Grabbed, or below 25% HP — they go over.
**Athletics check required** if the enemy is standing and not debuffed: DC = enemy Athletics or Fortitude (whichever is higher).

| Method | Actions | Roll required? |
|---|---|---|
| **Shove off ledge** (enemy adjacent to drop) | 1 action | Yes — Athletics vs enemy Fort DC |
| **Trip + kick over** (enemy near drop, not adjacent) | 2 actions | Yes — Athletics vs enemy Ref DC |
| **Throw into fire** (Grabbed enemy) | 1 action | No — auto if already Grabbed |
| **Drive into wall / column** (Sudden Charge into hazard) | 2 actions | Yes — Athletics vs enemy AC |
| **Drop hazard on them** (chandelier, bookshelf, barrel stack) | 1 action | Varies — see hazard in scene file |
| **Guisarme hook + launch** (reach weapon drag to ledge) | 2 actions | Yes — Athletics vs enemy Fort DC; +2 bonus from hook mechanic |

**On success:** Stage Fatality fires — full environmental death narration (see below).
**On failure:** Enemy is shoved but catches themselves. They are Flat-Footed and Prone. Player's turn continues.

---

### Stage Fatality Narration by Hazard

**These are full Mortal Kombat stage kill sequences. The DM writes the fall, the impact, and the aftermath. Not "he goes over the edge." The whole thing.**

| Hazard | Narration mandate |
|---|---|
| **Drop / ledge (short — 1–2 stories)** | The body hits something on the way down — railing, outcropping, stone — and then the ground. Name what breaks on impact. The sound reaches up before the silence does. |
| **Drop / ledge (long — 3+ stories / cliff)** | The fall is long enough to watch. Name what the body does in the air. Name what it looks like when it stops. If it hits architecture on the way down, name each impact. The final position. |
| **Fire (small — hearth, torch)** | They go in and they don't come out the same. Describe the specific progression: hair first, then clothing, then skin. If they scream, note when the screaming stops. Ash, char, the smell, the skeleton folding. |
| **Fire (large — burning building, oil blaze)** | Full immolation. They are in it and then they are part of it. Describe what's visible after: a shape in the fire, then nothing, then char. The bones go last. |
| **Spikes / blades** | Impalement — name which spike, name where it enters, name where it exits. The body's weight does the rest. If multiple spikes, describe each. The body stays up. |
| **Impact surface (wall / column)** | The sound first — stone on skull, or skull on stone, depending on what moved. Describe the specific damage: jaw, orbital, the back of the head. The slide down. The shape they make at the bottom. |
| **Water / drowning** | They go in. Describe the entry — the splash or the silent slip. Describe what's visible from above: the shape under the surface, the stillness. If armor is worn, note that it doesn't help. |
| **Falling object (chandelier, shelf)** | Name what falls and what it weighs. Describe the moment of contact — pinned, crushed, the specific part of the body under the specific object. Whether they move after. |

---

### Map Flagging

When a hazard is present, the DM marks it on the ASCII grid:

```
^ = ledge / drop edge (direction of fall is off the map edge)
~ = water / drowning hazard
F = active fire
* = spikes / blades
! = unstable / falling object hazard (chandelier, shelf, barrel stack)
```

Example:
```
  5    #    .    .    @    .    ^    ^    ^    #
```
Row 5, columns F–H are the ledge edge. Enemy at E5 = one shove away.

The ID block includes:
```
⚠ STAGE HAZARD: Balcony ledge — columns F–H, row 5. 30 ft drop to courtyard stone.
```

---

### Menu Presentation

Whenever a Stage Fatality is available, it appears as a numbered option in the player's combat menu:

```
[N] Stage Fatality — [Hazard name]: [one-line description of what you'd do]
     Example: "Shove him off the balcony — 1 action, Athletics vs Fort DC 14"
```

If multiple hazards are present, each gets its own numbered option.

---

---

## 🩸 GRIEVOUS WOUNDS — SURVIVAL INJURY SYSTEM

> **DM:** When a hit leaves a non-boss, non-named enemy alive but below 50% HP, a grievous wound fires. The less HP they have left, the worse it is. This is mandatory narration + a real PF2e condition. Applies to hits from eRmaC and companions only — not enemy hits against the party.

### Trigger

A single strike drops a non-boss enemy to below 50% of their max HP AND they survive. Calculate remaining HP as a percentage of max HP after the hit.

`wound_severity = (HP remaining / HP max) × 100`

### Wound Tiers

| Remaining HP | Tier | Condition Applied | Narration register |
|---|---|---|---|
| 25–49% | **Rattled** | Frightened 1 (until end of their next turn) | Visible damage — staggered, bleeding, guard broken. They're still in the fight but something just changed. |
| 10–24% | **Grievous** | Enfeebled 1 OR Clumsy 1 (3 rounds) — pick whichever fits the wound location | A real injury. They're fighting through it. Limb compromised, breath gone, eye filled with blood. The math on this fight has shifted. |
| 1–9% | **Critical Wound** | Enfeebled 2 + Slowed 1 (until end of encounter) | They are almost not there. One leg, one arm, one eye — something is gone or functionally gone. They are still standing by instinct only. |
| 1–3 HP (the brink) | **The Brink** | Enfeebled 2 + Frightened 2 + Slowed 1 (until end of encounter) | They should be dead. The body hasn't caught up. Narrate what specifically is keeping them upright and why it won't last. |

### Wound Type by Damage Source

The injury narration follows the damage type and weapon — not a generic "they're hurt."

| Damage type | Wound flavor |
|---|---|
| Slashing (guisarme, blade) | Severed or partially severed — fingers, hand, ear, nose, deep muscle tear exposing bone |
| Bludgeoning (maul, fist, fall) | Shattered — ribs caved, orbital crushed, jaw dislocated, limb hanging wrong |
| Piercing (arrow, dagger, spear) | Puncture — pinned, through-and-through, lodged, collapsed lung register |
| Fire | Burns — degree by tier; Rattled = blistered, Brink = charred, structural |
| Cold | Frostbite, flash-frozen tissue, cracked skin split to the quick |
| Reach/polearm hook (guisarme specifically) | The hook lands somewhere specific — a catch, a drag, a tear. Name where the hook went. |

### Rules

- **Non-boss, non-named enemies only.** Named enemies and bosses do not take grievous wounds from this system (they have their own dramatic beats).
- **One wound narration per enemy per combat.** A second hit on a Grievous-tier enemy doesn't re-describe the wound — it ends them or deepens the condition already applied.
- **Conditions are real.** Apply them to the enemy stat block. They affect subsequent rolls.
- **Survivors may break.** A Brink-tier enemy may flee, surrender, or collapse on their next turn — DM judgment, but the option is always on the table and should be offered to the player as a choice (finish them, let them crawl, take a prisoner).
- **Do NOT ask permission.** The hit earned it. Narrate it.

---

## ⚔️ ADVERSARY MORALE & QUARTER — THE ENEMY'S READ OF YOU

> **DM:** Build 2026-06-22 (user request). A rank-and-file enemy's choice to **surrender, flee, or fight to the death** is shaped by what they've HEARD about you — whether you give quarter or give none. This is the enemy-facing mirror of the public reputation system, and it is **sourced from the existing Merciful/Ruthless disposition (KM_Mythic_Systems.md § Dispositions) — NOT a new tracker.** It extends that file's "prisoners surrender more quickly / fight harder when cornered" rule from the Crime system onto the battlefield.

### THE MERCY STANDING (derived — no new score)

`mercy_standing = (Merciful tag) − (Ruthless tag)` from § Dispositions. It is what the enemy has heard about you. Like the public ladder, it runs positive AND negative:

| Standing | Name | What enemies have heard |
|---|---|---|
| **+4 or more** | THE MERCIFUL (Quarter-Giver) | "He spares those who kneel." Yielding feels safe. |
| **+2 / +3** | FAIR | Known to take prisoners; surrender is reasonable. |
| **−1 to +1** | UNREAD | No word reached them — they judge you in the moment (default Bestiary morale). |
| **−2 / −3** | HARD | Known to kill freely; surrender is a gamble. |
| **−4 or less** | NO QUARTER (The Butcher) | "He kills everyone." Surrender = death — run, or die fighting. |

(The disposition's Bonus +2 acts — sparing or executing a *named* foe — swing the standing fast.)

### WHEN IT FIRES — THE BREAK POINT

Roll an adversary **MORALE check** for a rank-and-file enemy when it **breaks**: HP ≤ ~25%, its leader/captain falls, it is outnumbered ~2:1, or it watches allies cut down (the "Brink-tier may break" hook above). NOT every enemy every round — only at a break point.

**Check:** `d20 + creature Morale mod` (Bestiary tactics line) vs **DC 11**. The result resolves to one of three intents — **SURRENDER** (yields, drops weapons, begs quarter) · **FLEE** (breaks and runs) · **FIGHT ON** (cornered, desperate, fights to 0). Then **MERCY STANDING shifts the outcome** (this is the whole point):

| Standing | Effect on a broken enemy |
|---|---|
| **THE MERCIFUL (+4+)** | Many **SURRENDER** (yielding is safe) — BUT you have **no fear leverage** (see THE CURVE): Intimidation/coercion fails, your threats and terms aren't taken seriously, and bold or opportunistic enemies **fight on** or **fake-surrender** because losing to you isn't fatal. Quantity of surrenders is high; their *sincerity* and your *control* of them is low. |
| **FAIR (+2/+3)** | **The sweet spot for live prisoners** — feared enough to genuinely yield AND submit to capture/coercion; the most clean, real surrenders. |
| **UNREAD (−1..+1)** | Default to the creature's own Bestiary morale/tactics line. |
| **HARD (−2/−3)** | **Also strong for captures** — they fear you enough that the broken ones yield and stay yielded; a few prefer to **FLEE**. |
| **NO QUARTER (−4−)** | Maximum terror — they break FAST — but they **REFUSE CAPTURE**: surrender = death to a known butcher, so they **FLEE** or **FIGHT TO THE DEATH** instead. You can rarely take a prisoner alive → **intel/interrogation lost.** Cornered = desperate and dangerous. |

⛔ **THE CURVE — BOTH EXTREMES COST YOU (user directive 2026-06-22). A balanced/firm reputation takes the most prisoners; both ends lose them, for opposite reasons.**
- **Too MERCIFUL → they don't take you seriously; they think you're weak.** A name for sparing everyone reads as *softness.* Enemies stop **fearing** you, so: (1) **Intimidation, Demoralize, coercion, and fear-based interrogation FAIL or take a penalty** — they don't believe your threats and **openly mock / scoff / taunt** them ("And what — you'll *spare* me again?"; raise the DC or auto-fail at +4/+5); (2) they **assume they can beat you** — overconfident, they **don't break** at the normal trigger and may even **press the attack** where a frightened enemy would yield; (3) demands are **laughed off** — they won't lay down arms for someone they've decided is harmless; (4) those who DO surrender may be **faking it** (yielded only because it's safe — slips away, grabs a weapon, lies in interrogation) unless properly secured. You get contempt, not leverage.
- **Too SAVAGE → they fight or run to the last, and won't believe a deal.** A butcher's name means **your threats ARE taken seriously** (terror is real — Intimidation lands hard) — BUT they have **no faith you'll honor your end of any bargain.** Offer "yield and live" and they **don't believe it** (you're known to kill the kneeling anyway), so a negotiated surrender is **worthless**: **no matter how badly injured, they keep attacking or try to run** rather than be taken — dying on their feet or fleeing beats trusting a killer's promise. **You cannot take prisoners** — the assassin you wanted alive for the conspiracy bolts or forces a kill. Intel dies with them.
- **The middle (FAIR / HARD) is optimal for live, usable prisoners** — **both** your threat AND your mercy are credible, which is what a surrender deal needs: feared enough that fighting is clearly worse, trusted enough that yielding means they actually live. (Merciful = they believe the *mercy* but not the *threat*; Savage = they believe the *threat* but not the *mercy*; only the middle has both.) If the player's GOAL is a captive (interrogation, the PR_09 conspiracy), a firm-but-not-monstrous standing serves best; flag the tension when it bites ("your name for mercy means he laughs off your threat" / "your name for slaughter means he'd rather die than trust your word").

Calibration (mirrors the ±10% surrender the Crime system already uses): toward Merciful raises *willingness* to surrender but **destroys fear leverage** (mockery, overconfidence, fake surrenders at the extreme); toward Ruthless raises *terror* but **destroys deal-credibility** — they believe the threat, disbelieve the mercy, so surrender collapses toward flee/fight-to-the-last and prisoners become near-impossible.

### LEADERS, CAPTAINS, BOSSES — THEY COMMENT, AND THEY'RE DIFFERENT

- **Captains / sergeants** don't break on the first trigger. They may **RALLY** the rank-and-file (steady their men, +2 to the men's next morale check) — UNLESS your standing is **NO QUARTER**, in which case a savvy captain has already told them *"this one gives no quarter — sell your lives,"* pre-stiffening them to FIGHT ON (a harder fight). A **merciful** standing can break a captain's hold the other way: *"Lay down your arms — he takes prisoners."*
- **Named leaders / bosses** generally do **NOT** surrender to a morale roll (pride / plot armor), but they **READ you aloud**: merciful → wary respect or contempt (*"Mercy. How convenient."*); no-quarter → fear, a vow to die fighting, or an attempt to flee themselves. Canon surrender hooks (Happs Bydon, Kressle, KM_Combat_Systems surrender list) still fire where written — a **merciful** standing makes the boss MORE likely to take an offered surrender; **no-quarter** may make him fight or run instead.

### 🗣️ PRE-COMBAT — ENEMIES WHO'VE HEARD OF YOU TALK FIRST (non-ambush only)

> **When a fight does NOT open with an ambush** — no surprise round, the enemies see you coming and have a beat of mutual awareness before blows — enemies who have **heard of you** (your Mercy Standing reached them — see § WORD SPREADS) **say so, to each other or at you,** before the first strike. It's a one- or two-line exchange that telegraphs the morale modifier about to apply, and doubles as a **diegetic tell** to the player of where their reputation sits.

⛔ **Gate:** ONLY when there's time to talk. If EITHER side **ambushes** (surprise round / the player opens from stealth / the enemy drops on a sleeping target), skip the banter — there's no beat for it, go straight to initiative. Also skip for **mindless/fanatic** enemies (they don't chatter) and for **UNREAD** standing (no rep reached them — they size you up neutrally, generic "Who's this one?" at most, no special line).

⛔ **USE THEIR NAMES — they're not anonymous tokens to each other.** If the speakers have field-names (the night-attack cell: Brannic, Sable, Vell, Toskar, Renno, Gisk, etc. — `KM_PR_NightAttack_Rooms.md § NAMED ROSTER`), they **address each other by name** in the exchange, the way men who've worked a job together actually talk: *"Sable — that's him?"* / *"Brannic, careful, this one doesn't blink."* A named captain calls his men by name when he rallies or warns them. Anonymous *"one to another"* lines are the fallback for genuinely nameless mobs only; whenever a roster name exists, **the banter carries it** (`.fail 9` to render named cell members as faceless "the assassin says").

**Engagement lines by Mercy Standing** (one mook to another, or the captain to his men — vary the wording, don't quote these verbatim every time):

| Standing | What they say (sample) | Hooks into |
|---|---|---|
| **THE MERCIFUL (+4+)** | Contempt — *"That's him? The one who lets everyone walk? Heh — pushover. Don't even need to be careful with this one."* / *"Relax. Worst he does is ask nicely."* | the overconfidence + mockery of the curve — they don't break, they test you |
| **FAIR (+2/+3)** | Measured — *"That's the one who takes prisoners. He fights clean, but he fights. Don't get cocky."* | the sweet-spot read — beatable but real |
| **HARD (−2/−3)** | Wary — *"Careful with this one. He doesn't play, and he doesn't blink."* | rising fear, fewer surrenders |
| **NO QUARTER (−4−)** | Dread — *"Gods — it's HIM. The one who leaves no one to bury. Whatever you do, do NOT let him take you alive."* | the refuse-capture + die-fighting/flee of the curve |

⛔ **It must MATCH the standing**, not flatter the player: a merciful rep earns **mockery/underestimation**, not respect; a butcher rep earns **dread**, not admiration. The line previews the morale behavior the player is about to face — and lets them feel their reputation landing before the dice do.

### 🎭 PRE-COMBAT — UNAWARE ENEMIES TALK ABOUT NOTHING (stealth approach / undetected)

> **When the player approaches UNDETECTED** — they haven't been spotted, the enemies in the room **don't know anyone is coming** — the chatter is **mundane and oblivious.** This is the OTHER pre-combat mode: not about the player at all (they've never heard of him; they think they're alone). They **gripe, gossip, bicker over something irrelevant, complain about the job, gamble, argue a pointless argument** — the texture of bored, off-guard men killing time. It plays whenever the player is listening from concealment **before** the first strike (the stealth opener, a ghost approach, scouting a room).

**Why it earns its place (not just flavor):**
- **It's a stealth TELL.** Overhearing tells the player **how many** are in there (count the voices), **roughly where** (which direction, near the fire or the door), and **their mood/posture** (relaxed = full Stealth/ghost bonus; on edge = harder). A strong Perception/Seek sharpens it — see the DESTINATION CLUES rule. It feeds the ghost/stealth opener and the backstab.
- **It can leak ONE usable detail** — a name, who's posted where, a complaint that the fire's spreading, that a captain stepped out, that someone's hurt. Narrow and earned, never a full readout for free.
- **It makes the kill land.** Dropping a man mid-sentence about his card debt or his sore feet hits harder than gutting a faceless token. Use the **roster names** — they argue with *each other* by name (*"Renno, it's your deal, quit stalling"* / *"Gisk swears he heard something — Gisk hears everything, ignore him"*).

⛔ **STAYS AT THEIR PAY-GRADE — knowable-facts ceiling holds.** These are courier-separated men who each know only their task + their handler's face. Their gripes are **small and personal** — pay, the cold, the wait, a grudge, the dice, who screwed up the timing. They do **NOT** mouth the conspiracy: never name the patron / "C" / Castruccio / Pitax-beyond-supply, never explain the whole plan, never monologue the mission's purpose (`.fail 9` — that's the search-surfaces-future-canon failure). A mook complaining *"nobody told me there'd be this many guests"* is fine; a mook explaining *who* hired the cell and *why* is a fabrication leak.

**Sample registers** (improvise, don't quote verbatim): a stupid argument (*"—I'm telling you it's pronounced the other way"*), money (*"you still owe me from Restov"*), the job's discomfort (*"how long are we sitting in this cold?"*), gossip about an absent third (*"Brannic thinks he runs this"*), boredom (dice, a flask, a half-eaten meal). Pick what fits the room and the men in it.

⛔ **THE SILENCE IS A WITNESS — ghosting an active talker gets noticed by what he STOPS saying.** An ongoing conversation is a web of expectation: each man is waiting on the next reply. If the player **ghost-kills someone who was an active participant** — someone who'd just been addressed, or whose turn it was to speak/answer — the survivors get a **BONUS to the NON-DETECTION roll** (the others' Perception vs the killer's Stealth — roll 2 of the two-roll ghost; see `KM_CombatTurn.txt § GHOST / STEALTH-KILL`), because **they're listening for a voice that doesn't come.** A direct address left unanswered is the loudest silence: *"Renno? ...Renno."* → they go to check → escalation. (Note: this only matters on a *successful* kill — a botched assassination already alarms the whole room on its own.)
> - **Timing beats the silence.** Killing a man **right after he finishes his line** (the room expects a beat of quiet before his next) is far safer than killing him **on his turn to answer** (the gap registers instantly). Killing the one who'd gone **quiet, peripheral, or was about to step out** draws **no silence-check at all** — no one's waiting on him.
> - **It's a real tactical choice, not a penalty.** The player can read the banter to pick the safe target: drop the loner, or strike in the lull between exchanges, not the man mid-argument. Reward good timing (no check), punish greedy timing (the silence rats them out). A botched silence-check doesn't auto-blow the whole room — it sends **one** man to look, which the player can ghost in turn (now with the next rung of escalation).
> - ⛔ Don't render the silence-detection as automatic either way. **Roll it.** Quiet execution + armor with no Stealth penalty + a noisy room (fire, distance) can let a kill pass unremarked even mid-sentence; a clean room and an expectant pause makes even a silent kill conspicuous.

⛔ **Mode-switch:** the instant they **detect** the player, this stops. If there's still a beat before blows (they see him, non-ambush) → flip to the reputation **Engagement lines** above. If the player **strikes from the unawareness** (ghost kill / backstab / stealth opener) → it was an ambush; go straight to the stealth-kill resolution, no banter. The mundane chatter is the sound of the room *before* it knows.

### WORD ONLY SPREADS FROM SURVIVORS

The standing grows from what enemies **live to tell.** ⛔ Annihilate everyone and that fight adds **nothing** to your enemy reputation — no one carried the tale (the same "no witnesses, no chatter" rule as public reputation and the Crime/Witness system). Letting some **FLEE** is what spreads the legend — merciful *or* butcher. This is the deliberate tension: silent total slaughter keeps you **UNREAD**; sparing survivors (or terrifying them into flight) is what builds the name. The same spare/execute act ALSO moves the Merciful/Ruthless disposition, and moves `public_reputation` if civilians witness it — **one act, all ledgers.**

### ⛔ DON'T

- **Don't override the player's call.** Morale decides only what the **ENEMY** tries (surrender / flee / fight). The **PLAYER** still decides what to do about it — accept the surrender, capture, let them run, or execute — per § the helpless/surrendering **decision-point** rule (KM_ClaudeInstructions COMBAT). A surrendering enemy is a decision point, never an auto-result, in EITHER direction.
- **Don't flip mindless / fanatic / frenzied enemies.** Undead, constructs, Bloom-frenzied, oath-bound zealots have **no morale** — they fight to destruction regardless of your standing. Keep their Bestiary "no morale / fights until destroyed" line.
- **Don't fabricate the standing.** It is `Merciful − Ruthless`. If both are ~0 the enemy is **UNREAD** — judge in the moment, don't invent a reputation they couldn't have heard.

---

## 🗣️ WRATH COMPANION COMBAT VOICE LINES

> **v93.19 Sub-F:** All 6 Wrath-companion voice rows (Lann, Ember, Daeran, Nenio, Regill, Arueshalae) removed — WotR companions purged from roster in Roster v2. Use GENERIC ARCHETYPE table below as fallback for any combat voice need.

## 🗣️ GENERIC ARCHETYPE VOICE LINES (for Iconic companions without specific entries)

> **DM:** Use these when an Iconic companion (26+) doesn't have a specific voice entry above. Match to their combat archetype.

| Archetype | On Hit | On Miss | On Crit | Taking Damage |
|-----------|--------|---------|---------|---------------|
| Tank | *"Holding."* | *"Adjusting."* | *"That's how it's done."* | *"I can take more."* |
| Striker | *"Down."* | *"Again."* | *"There."* | *"Keep going."* |
| Caster | *"Impact."* | *"Misfire."* | *"Maximum effect."* | *"Focus. Focus."* |
| Support | *"Connecting."* | *"Missed the window."* | *"Perfect timing."* | *"I'm still here."* |
| Skill | *"Precision."* | *"Close."* | *"Exactly as planned."* | *"That was my mistake."* |

---

## 🔥 ELEMENTAL SURFACE COMBO SYSTEM

> **DM:** Spells and abilities leave persistent terrain effects. Combining elements creates combos. Track surfaces on the combat grid. Surfaces last until the end of the encounter unless dispelled or consumed by a combo.

### Surface Types

| Surface | Created By | Effect | Duration |
|---------|-----------|--------|----------|
| **Wet** | Rain, Water spells, Hydraulic Push | Flat-footed (slippery). Vulnerability: Lightning +50% damage. | 3 rounds or until dried |
| **Burning** | Fire spells, torches, alchemist fire | 1d6 fire/round to creatures entering or starting in area. Difficult terrain. | Until extinguished (2 rounds or water) |
| **Frozen** | Cold spells, Cone of Cold | Difficult terrain. Acrobatics DC 14 or fall prone on entry. | 5 rounds or until fire applied |
| **Poisoned** | Stinking Cloud, poison attacks, Cloudkill | Sickened 1 each round in area (Fort save). | Spell duration |
| **Electrified** | Lightning spells on Wet surface | 2d6 electricity to all in area (no save). Consumes Wet surface. | Instant (combo trigger) |
| **Steam** | Fire on Wet/Frozen surface | Concealment (20% miss chance) for 2 rounds. | 2 rounds |
| **Oil** | Alchemist abilities, Grease spell | Flat-footed + Acrobatics DC 16 or prone. Flammable. | Until ignited or cleaned |
| **Explosion** | Fire on Oil surface | 4d6 fire in area (Ref DC 16 half). Consumes oil. | Instant (combo trigger) |
| **Mud** | Water on earth/dirt terrain | Difficult terrain. −10 ft Speed. | 3 rounds |

### Combo Table

| Base Surface | + Element | = Result |
|-------------|-----------|----------|
| Wet | Lightning | **Electrified** (2d6 elec, no save, consumes Wet) |
| Wet | Fire | **Steam** (concealment 2 rounds) |
| Wet | Cold | **Frozen** (difficult terrain, prone risk) |
| Frozen | Fire | **Wet** (thaw, then normal) |
| Oil | Fire | **Explosion** (4d6 fire, Ref half, consumes Oil) |
| Burning | Water/Cold | **Extinguished** (surface cleared) |
| Poisoned | Fire | **Toxic Fumes** (Sickened 2, area expands 5 ft) |
| Mud | Cold | **Frozen Mud** (Immobilized, Athletics DC 16 to escape) |
| Mud | Lightning | **Electrified Mud** (1d6 elec + prone, consumes Mud) |

### DM Rules
1. **Track surfaces on the ASCII combat grid.** Mark with letters: W=Wet, B=Burning, F=Frozen, P=Poison, O=Oil, M=Mud.
2. **Surfaces are 10 ft × 10 ft minimum** (2×2 squares). Spell area determines actual size.
3. **Combos are automatic.** If a fire spell hits a Wet surface, Steam happens. DM does not choose — physics does.
4. **NPCs can exploit combos too.** Intelligent enemies (Int 10+) avoid surfaces and may create their own.
5. **Outdoor vs Indoor:** Rain creates Wet surfaces outdoors automatically during rain weather (KM_Kingdom.md). Indoor: no ambient surfaces.


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION TACTICS SYSTEM
## KM_Combat_Systems.md | DA:O / EMAT-Style Role-Based Companion AI | Active: All Chapters

> **DM:** In combat, run each companion's slots top to bottom each turn. First condition TRUE fires — stop scanning. Do not improvise around filled slots. Player changes any slot with `.tactics [companion] [slot] [ability]`. Switch strategy mode with `.strategy [companion] [mode]`.

---

## SYSTEM MECHANICS

| Slot Label | When It Fires |
|------------|---------------|
| **S** | OnCombatStart — round 1 only, fires once before slot scanning |
| **0** | Reaction — fires off-turn when trigger condition is met |
| **1–7** | Priority order — scanned top to bottom each turn |
| **D** | Default — fires when no other slot condition is true |

**Condition syntax:**
- `AND` — both must be true: `Ally HP ≤ 20% AND self HP > 30%`
- `OR` — either: `2+ allies HP ≤ 50% OR single ally HP ≤ 25%`
- `NOT` — inverse: `NOT raging`, `NOT buff active`
- `[MUTEX: ability]` — slot skipped if that ability is already active

**Strategies:** Named mode bundles that override specific slots. Active strategy shown in tracker. Base slots run for anything not overridden by the strategy.

---

## ROLES

### ROLE: HEALER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — position + pre-buff |
| 0 | Ally drops to 0 HP (reaction) | [DEATH SAVE HEAL] |
| 1 | Ally HP ≤ 20% AND self not dying | [EMERGENCY HEAL] — 2 actions, max rank |
| 2 | Ally has dying / paralyzed / blinded | [CLEANSE] |
| 3 | 2+ allies HP ≤ 50% OR single ally HP ≤ 25% | [BURST HEAL] — 3 actions, area |
| 4 | Ally HP ≤ 50% | [PRIMARY HEAL] — 1–2 actions |
| 5 | NOT buff active [MUTEX: PARTY BUFF] | [PARTY BUFF] — 1 action |
| 6 | Self HP ≤ 25% | [SELF-PRESERVE] |
| D | Default | [CANTRIP] |

---

### ROLE: STRIKER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — activate power state + close distance |
| 0 | Enemy provokes (reaction) | [AoO STRIKE] |
| 1 | NOT in power state | [ACTIVATE] — 1 action |
| 2 | Enemy flat-footed OR flanked | [POWER ATTACK] — 2 actions |
| 3 | 2+ enemies adjacent AND power state active | [AREA ATTACK] — 2 actions |
| 4 | 1st or 2nd attack this turn | [STRIKE] — 1 action |
| 5 | Would be 3rd attack (MAP −10) | [ALTERNATE] — 1 action |
| D | Default | [STRIKE] |

---

### ROLE: CONTROLLER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — highest-priority control on biggest threat |
| 0 | Enemy casts AND reaction available | [COUNTERSPELL] |
| 1 | 3+ enemies grouped within 30 ft AND slot available | [AREA CONTROL] — 2–3 actions |
| 2 | Enemy caster/commander visible AND not controlled | [SINGLE CONTROL] — 2 actions |
| 3 | Ally outnumbered 2:1 OR flanked | [AREA DEBUFF] — 2 actions |
| 4 | Spell slots spent | [CANTRIP CONTROL] |
| D | Default | [DAMAGE CANTRIP] |

---

### ROLE: TANK

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — Raise Shield + move adjacent to most vulnerable ally |
| 0 | Enemy attacks adjacent ally (reaction) | [SHIELD BLOCK / INTERPOSE] |
| 1 | Enemy moves through threatened space | [AoO STRIKE] |
| 2 | Ally targeted AND self adjacent | [PROTECT] — Shield raise + absorb |
| 3 | Ranged enemy unengaged AND no melee threat | [CLOSE + ENGAGE] |
| 4 | Self HP ≤ 40% AND no ally critical | [SUSTAIN] |
| D | Default | [RAISE SHIELD + STRIKE] |

---

### ROLE: SUPPORT/BUFFER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — primary buff immediately |
| 0 | Ally drops (reaction) | [EMERGENCY REACTION] |
| 1 | NOT primary buff active [MUTEX: PRIMARY BUFF] | [PRIMARY BUFF] — 1 action |
| 2 | NOT secondary buff active [MUTEX: SECONDARY BUFF] | [SECONDARY BUFF] — 1 action |
| 3 | Priority enemy NOT debuffed | [DEBUFF] — 1–2 actions |
| 4 | Buff needs sustain (free action available) | [SUSTAIN] — free action |
| D | Default | [CANTRIP or BASIC ATTACK] |

---

### ROLE: SCOUT/SKIRMISHER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — mark priority target + position at range |
| 0 | Enemy closes to melee (reaction) | [DISENGAGE REACTION] |
| 1 | No priority target marked | [MARK TARGET] — 1 action |
| 2 | Priority target in range AND self not in melee | [STRIKE PRIORITY] — 1–2 actions |
| 3 | Enemy closes to melee | [STEP BACK + STRIKE] |
| 4 | No clear shot OR flanked by 2+ | [REPOSITION] |
| D | Default | [STRIKE] |

---

## COMPANION ASSIGNMENTS

### AMIRI — Striker
| Slot | Filled |
|------|--------|
| S OPENER | Rage + Stride toward highest-threat enemy |
| ACTIVATE | Rage |
| POWER ATTACK | Furious Blow (Giant Instinct, 2 actions) |
| AREA ATTACK | Giant's Swing — 2+ adjacent AND raging |
| ALTERNATE (MAP−10) | Intimidating Glare — Demoralize 1 action |
| AoO | Strike — enemy in reach moving away |
| OVERRIDE | Weapon = oversized bastard sword. Not an axe. Never. |

**STRATEGIES:** `RAMPAGE` — Area attack fires if 2+ adjacent, no flat-footed check; ignore MAP on slot 5, keep striking. | `CONTROLLED` — Rage only if HP > 50%; step back instead of MAP strike. | `BODYGUARD` — Strike enemies targeting allies first over optimal positioning.

---

### LINZI — Support/Buffer + Controller
| Slot | Filled |
|------|--------|
| S OPENER | Inspire Courage immediately (1 action) |
| PRIMARY BUFF | Inspire Courage [MUTEX: Inspire Courage active] |
| SECONDARY BUFF | Inspire Defense when party average HP < 60% |
| SUSTAIN | Cackle free action — maintain Inspire each turn |
| DEBUFF | Fear rank 1 on enemy caster priority |
| EMERGENCY | Heal if ally < 25% AND no healer has acted |
| OVERRIDE | Never drop Inspire Courage while allies are attacking. Notebook between turns only. |

**STRATEGIES:** `CHRONICLE` — Default. Inspire + sustain + observe. Minimal slot use. | `FULL SUPPORT` — Use Fear, Silence, all slots freely. | `EMERGENCY BARD` — All actions to healing if party healer is down.

---

### HARRIM — Healer (Warpriest)
| Slot | Filled |
|------|--------|
| S OPENER | Bless rank 1 + move to melee line |
| DEATH SAVE | Heal reaction rank 1 minimum |
| EMERGENCY HEAL | Channel Positive Energy — area, 2 actions |
| PRIMARY HEAL | Heal rank 2 — 1 action, single target |
| CLEANSE | Remove Fear |
| PARTY BUFF | Bless rank 1 [MUTEX: Bless active] |
| SELF-PRESERVE | Channel on self |
| OVERRIDE | Stays in melee. Heals from inside the fight. Will not retreat. |

**STRATEGIES:** `WARPRIEST` — Default. Melee + heal between strikes. | `PURE HEALER` — Backline only, no strikes. | `DOOM HERALD` — All slots on Harm vs undead; no healing this combat.

---

### JAETHAL — Striker (Undead)
| Slot | Filled |
|------|--------|
| S OPENER | Stride to flanking position on priority target |
| POWER ATTACK | Harm channel — area, 2 actions, when 2+ living adjacent |
| STRIKE | Rapier finesse — Sneak Attack when flanking OR target flat-footed |
| ALTERNATE (MAP−10) | Reposition for flanking angle |
| AoO | Always — any provocation in reach |
| OVERRIDE | Immune: mind/fear/death. Heals from negative energy ONLY — positive harms her. |

**STRATEGIES:** `ASSASSIN` — Single-target elimination priority. Sneak Attack every strike. | `UNDEAD WAVE` — Harm area as primary; ignore flanking, damage all living in reach.

---

### LANN — Scout/Skirmisher (Ranger)
| Slot | Filled |
|------|--------|
| S OPENER | Hunt Prey on priority target + move to elevated/distant position |
| MARK TARGET | Hunt Prey — spellcaster > commander > melee |
| STRIKE PRIORITY | Crossbow + Hunter's Edge precision |
| STEP BACK + STRIKE | Retreating Shot if enemy closes |
| REPOSITION | Move to elevation or maintain ≥ 30 ft distance |
| UTILITY | Heal via Crack Shot if ally critical AND no healer available |
| OVERRIDE | Maintains ≥ 30 ft from melee. Position before attack. |

**STRATEGIES:** `SNIPER` — Default. Max range, precision, no melee. | `SKIRMISHER` — Close range acceptable; rapid fire over positioning. | `SCOUT LEAD` — Move first each turn; no attack if repositioning used all actions.

---

### EMBER — Support/Buffer (Witch)
| Slot | Filled |
|------|--------|
| S OPENER | Evil Eye hex on highest-threat enemy (Frightened 1) |
| PRIMARY BUFF | Evil Eye hex [MUTEX: hex active on current target] |
| SUSTAIN | Cackle free action — maintain hex each turn |
| DEBUFF | Slow rank 2 on highest-threat melee AND hex already running |
| SECONDARY | Soothe if ally < 40% AND no healer has acted this turn |
| EMERGENCY | Bestow Curse on enemy that downed an ally |
| OVERRIDE | Nova = raven familiar. Not fire-adjacent. Not a fire spirit. Ever. |

**STRATEGIES:** `HEX FOCUS` — Default. Evil Eye + Cackle every turn. | `CURSE SUPPORT` — Bestow Curse primary; save hex for emergencies. | `EMERGENCY WITCH` — Soothe as primary when healer is down.

---

### DAERAN — Healer (Oracle)
| Slot | Filled |
|------|--------|
| S OPENER | Life Link focus spell (party-wide heal aura) |
| DEATH SAVE | Heal reaction rank 1 minimum |
| EMERGENCY HEAL | Heal rank 3 — 3-action burst when 2+ critical OR single at 0 HP |
| PRIMARY HEAL | Heal rank 2 — 1 action, single target |
| CLEANSE | Neutralize Poison / Remove Disease |
| PARTY BUFF | Life Link [MUTEX: Life Link active] |
| SELF-PRESERVE | Withdraw — he is not a melee combatant |
| OVERRIDE | Tracks gift costs. Does not martyr himself. |

**STRATEGIES:** `LIFE SUPPORT` — Default. Efficient slot use; Life Link as backbone. | `TRIAGE` — Emergency heals only; save all slots for critical moments. | `BATTLE ORACLE` — Offensive revelation spells primary; minimal healing.

---

### NENIO — Controller (Wizard)
| Slot | Filled |
|------|--------|
| S OPENER | Slow rank 2 on highest-action enemy |
| AREA CONTROL | Web OR Stinking Cloud — 3+ enemies grouped AND slot available |
| SINGLE CONTROL | Charm OR Confusion — enemy caster AND NOT already controlled |
| DEBUFF | Fear rank 2 on commander if no caster visible |
| CANTRIP CONTROL | Electric Arc (2 targets) when slots spent |
| SELF-PRESERVE | Blur OR Invisibility when targeted in melee AND HP < 60% |
| OVERRIDE | One sentence of tactical narration per turn max. Not a monologue. |

**STRATEGIES:** `RESEARCHER` — Default. Slow opener + systematic control; preserve slots past round 3. | `NOVA` — Spend top slots immediately rounds 1–2. | `SUPPORT MAGE` — Haste/Blur/Mirror Image on allies instead of controlling enemies.

---

### REGILL — Tank (Hellknight)
| Slot | Filled |
|------|--------|
| S OPENER | Move to cut off enemy commander escape route + Raise Shield |
| AoO | Strike — any enemy moving through threatened space |
| ENGAGE | Close to cut off retreat AND Shield raised |
| PRIORITY TARGET | Most organized / commander-type enemy |
| STRIKE | Disciplined Strike — no flourishes, no wasted actions |
| SUSTAIN | Raise Shield if HP < 40% AND no immediate strike available |
| OVERRIDE | Never breaks formation. Never chases. Holds ground. |

**STRATEGIES:** `IRON DISCIPLINE` — Default. Hold position, AoO everything, methodical. | `EXECUTE` — Close to commander and eliminate; ignore other threats. | `FORTRESS` — Full defensive; Shield always raised; strikes on AoO only.

---

### ARUESHALAE — Scout/Striker (Rogue)
| Slot | Filled |
|------|--------|
| S OPENER | Flank position OR distance if no flank available |
| MARK TARGET | Move to create flat-footed on priority target |
| STRIKE PRIORITY | Bow Strike — Sneak Attack when flat-footed OR flanked |
| SETUP | Feint if no flanking partner AND in melee range |
| STEP BACK + STRIKE | Disengage + shoot if 2+ enemies in melee with her |
| OVERRIDE | Prefers ranged. Melee only for Sneak Attack if position is safe. No unnecessary risks. |

**STRATEGIES:** `SHADOW` — Default. Ranged Sneak Attack priority; avoid melee. | `INFILTRATE` — Melee flanking with Amiri or Valerie for constant Sneak Attack. | `DISRUPT` — Feint and debuff over damage; keep target flat-footed for allies.

---

### SEELAH — Tank + Healer (Paladin)
| Slot | Filled |
|------|--------|
| S OPENER | Raise Shield + move adjacent to most vulnerable ally |
| SHIELD BLOCK | Reaction — adjacent ally takes hit AND block available |
| AoO | Strike — enemy disengages from her |
| HEAL ALLY | Lay on Hands — adjacent ally ≤ 20% AND focus available |
| SUSTAIN SELF | Lay on Hands — self ≤ 35% AND no ally critical |
| SMITE | Divine Smite on highest-threat [MUTEX: smite used last 2 rounds] |
| STRIKE | Strike + Raise Shield — 2 actions |
| OVERRIDE | Always adjacent to most vulnerable ally. Moves to protect before attacking. |

**STRATEGIES:** `PALADIN` — Default. Protect + heal + measured strikes. | `CRUSADER` — Divine Smite priority; less shielding, more damage. | `SHIELD WALL` — Full defense; Shield Block every hit; strikes on AoO only.

---

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Companion Tactics v1.1 (EMAT-style)*


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — REARGUARD & QUEST MANAGER SYSTEM
## KM_Combat_Systems.md | Referenced by: KM_Commands.md, KM_Ch1.md-KM_Ch7.md

> **DM:** This file defines Kesten Garess's role as Quest Manager, the rearguard
> scouting system, and companion quest delegation. Load this file when:
> — Player types `.quests`, `.scout`, `.delegate`, or `.rearguard`
> — Kesten Garess is in the party's current location
> — A ??? area is mentioned or scouted
>
> **Also load:** `KM_Combat_Systems.md` when resolving any scout or delegate mission return.
> That file handles skill pools, DCs, outcome tiers, injuries, gear loss, and mission costs.
> The class-based Delegation Skill Table and ★/★★/★★★ scout ratings below are superseded by it.

---

## 🗂️ KESTEN GARESS — QUEST MANAGER

**Arrives:** After Happs Bydon raid is repelled at Oleg's Trading Post.
**Role:** Intelligence officer and quest clearinghouse for the expedition.

**Flavor:** Kesten is a disgraced Brevic noble running a mercenary squad to rebuild his
name. He has the organizational mind of a soldier and the contacts of someone who used to
be somebody. He collects bounties from Restov, rumors from travelers, and reports from his
own scouts. Every quest that exists in the region passes through him eventually. He does
not post things on boards. He briefs you in person.

**What he tracks:**
- All available quests at the current chapter's active locations
- Bounties from Restov and the Swordlords
- ??? areas: locations rumored to exist but not yet explored by the party
- Rearguard status: who is away and what they are doing

---

## 📋 `.quests` — KESTEN'S BOARD

> **DM:** When player types `.quests`, output this panel. Pull active quests from
> `quests_active` and `story_flags`. Filter out completed quests. ??? entries come
> from `unknown_areas` in the save block. Rearguard entries come from `rearguard_active`.

```
╔═════════════════════════════════════════════════════════════╗
║  KESTEN'S BOARD — [CURRENT LOCATION]           [DATE/DAY]  ║
╠═════════════════════════════════════════════════════════════╣
║  QUESTS AVAILABLE                                           ║
╠═════════════════════════════════════════════════════════════╣
║  ▸ [Quest Name]              [DELEGATE OK] or [PARTY REQD] ║
║    Source: [NPC]  |  Reward: [reward]                       ║
║    Note:   [one-line summary]                               ║
╠═════════════════════════════════════════════════════════════╣
║  ▸ [Next quest...]                                          ║
╠═════════════════════════════════════════════════════════════╣
║  UNKNOWN AREAS                              [X] unscanned   ║
╠═════════════════════════════════════════════════════════════╣
║  ??? [Area hint]           ~[X] days travel  [INTEL: NONE] ║
║    Rumor: [one-line hint Kesten has heard]                   ║
║    → .scout [area] to send rearguard                        ║
╠═════════════════════════════════════════════════════════════╣
║  ??? [Area hint, partially scouted]          [INTEL: BASIC] ║
║    [One-line intel summary from prior scout]                 ║
║    → .scout [area] for full intel or enter yourself         ║
╠═════════════════════════════════════════════════════════════╣
║  REARGUARD AWAY                                             ║
╠═════════════════════════════════════════════════════════════╣
║  [Companion] → [Mission] — returns Day [X]                  ║
╚═════════════════════════════════════════════════════════════╝
```

**Delegation tag rules:**
- `[DELEGATE OK]` — gathering, delivery, simple patrol, weak beast clearance
- `[PARTY REQUIRED]` — named enemy, narrative-critical, dungeon, boss, companion quest

**DM rules:**
- Do NOT show quests in `quests_completed`
- Do NOT invent quests not in the location file or companion files
- ??? entries: only show if an `unknown_areas` entry exists in save block
- Rearguard section: only show if `rearguard_active` is non-empty

---

## ❓ ??? UNKNOWN AREAS SYSTEM

**What creates a ??? entry:**

| Trigger | ??? Added |
|---------|-----------|
| Happs Bydon surrenders | Thorn River camp (Kressle), Stag Lord fort |
| Merchant/traveler rumor | As narrated per chapter |
| NPC quest mention | Location of quest target if not yet visited |
| Map fragment found | Whatever the fragment indicates |
| Adjacent hex explored | Adjacent unexplored hex (general direction only) |

**??? entry in save block:**
```json
"unknown_areas": [
  {
    "id": "thorn_river_camp",
    "hint": "Bandit camp, Thorn River",
    "travel_days": 1,
    "intel_level": "none",
    "intel_summary": "",
    "source": "Happs Bydon (surrender)"
  }
]
```

**Intel levels:** `none` → `basic` → `full`
- `none` — exists on the board, no details
- `basic` — general danger level + area type (from ★ or ★★ scout)
- `full` — enemy types, count, layout, loot hint (from ★★★ scout)

---

## 🔭 `.scout [area]` — REARGUARD SCOUTING

> **DM:** When player types `.scout [area name]`, run the following procedure.

```
SCOUT PROCEDURE:
  1. Confirm the area exists in unknown_areas (not yet visited).
  2. Display the COMPANION SELECTION PANEL (below).
  3. Player picks 1–2 companions to send.
     — Companions must be currently in the party (not already on rearguard).
  4. Calculate travel time: unknown_area.travel_days × 2 + 1 day observation.
  5. Add entry to rearguard_active in save block.
  6. Mark those companions AWAY (unavailable for combat).
  7. Advance the day counter when the player rests/travels (normal time flow).
  8. When return day arrives, fire the INTEL REPORT (see format below).
```

**Companion selection panel:**
```
══════════════════════════════════════════════
SCOUT MISSION — [AREA HINT]
Estimated time: [X] days round trip
Select 1–2 companions to send.
Available:
  [list companions in party who are not AWAY]
  [show scout rating next to each name]
══════════════════════════════════════════════
```

**Scout ratings:** *(superseded — use Perception modifier pool in KM_Combat_Systems.md)*

**Risk of encounter:** Handled by the outcome tier roll in KM_Combat_Systems.md.
Failure or Critical Failure = something went wrong. Success+ = clean mission.

---

## 📡 INTEL REPORT FORMAT

> **DM:** When scouts return, deliver this panel in Kesten's voice plus a brief
> quote from the returning companion.

```
╔═════════════════════════════════════════════════════════════╗
║  SCOUT REPORT — [AREA NAME]                    [RETURN DAY] ║
╠═════════════════════════════════════════════════════════════╣
║  Scouts: [Companion names]     Intel level: [BASIC / FULL] ║
╠═════════════════════════════════════════════════════════════╣
║  AREA TYPE    [terrain: forest / ruins / camp / cave etc.]  ║
║  DANGER       [LOW / MODERATE / HIGH / EXTREME]             ║
║  ENEMIES      [types and rough count — FULL only]           ║
║  LAYOUT       [one-line summary — FULL only]                ║
║  LOOT HINT    [general: "gold and gear" / "magical item"…]  ║
║  HAZARDS      [traps, environmental — FULL only if known]   ║
╠═════════════════════════════════════════════════════════════╣
║  "[Returning companion's one-line report in their voice]"   ║
╠═════════════════════════════════════════════════════════════╣
║  → Area upgraded from ??? to [NAME] on Kesten's board       ║
║  → .quests to see updated board                             ║
╚═════════════════════════════════════════════════════════════╝
```

**BASIC intel (★ and solo ★★ scouts):**
Fill: Area Type, Danger. Leave ENEMIES/LAYOUT/HAZARDS as `[NOT OBSERVED]`.

**FULL intel (★★★ or paired ★★ scouts):**
Fill all fields. Enemies = general type + rough count ("~8 bandits, 1 leader-type").
Do NOT give exact stat blocks — that's for when the party arrives.

**Save block update after report:**
```json
"unknown_areas": update intel_level and intel_summary for this area
```

---

## ⚔️ `.delegate [quest]` — REARGUARD QUEST DELEGATION

> **DM:** When player types `.delegate [quest name]`, run the following procedure.

```
DELEGATE PROCEDURE:
  1. Confirm quest is marked [DELEGATE OK] on Kesten's board.
     — If [PARTY REQUIRED]: refuse with reason. Do NOT allow override.
  2. Display the COMPANION SELECTION PANEL for delegation.
  3. Player picks 1–3 companions.
  4. DM checks: does this group have the right skill rating for this quest type?
     — See DELEGATION SKILL TABLE below.
  5. Calculate completion time (see QUEST TIME TABLE below).
  6. Add entry to rearguard_active.
  7. Mark companions AWAY.
  8. On return: fire QUEST RETURN REPORT.
```

**Delegation skill table:** *(superseded — use KM_Combat_Systems.md)*

**Quest time table:**

| Quest Type | Days |
|------------|------|
| Gather (local, < 1 day travel) | 1–2 |
| Gather (distant, 1–2 days travel) | 2–4 |
| Deliver (local) | 1 |
| Deliver (distant) | 2–3 |
| Patrol / beast hunt | 2–5 |

**XP split on successful delegation:**
- Rearguard companions: 50% of base quest XP (divided among them)
- Player character: 25% of base quest XP
- 25% lost (not there personally)

**Non-delegatable quests (always [PARTY REQUIRED]):**
- Any quest with a named enemy (Stag Lord, Kressle, Tartuk, Tuskgutter, etc.)
- Any companion's personal quest chain
- Any quest with narrative choices or dialogue outcomes
- Any dungeon with more than one room
- Any quest where the reward depends on player decisions

---

## 📦 QUEST RETURN REPORT FORMAT

> **DM:** When rearguard returns from a completed delegation, deliver in Kesten's voice.

```
╔═════════════════════════════════════════════════════════════╗
║  MISSION COMPLETE — [QUEST NAME]               [RETURN DAY] ║
╠═════════════════════════════════════════════════════════════╣
║  Sent: [Companion names]                                    ║
╠═════════════════════════════════════════════════════════════╣
║  OUTCOME:   [SUCCESS / PARTIAL / FAILURE]                   ║
║  REWARD:    [Items / gold / service — as defined by quest]  ║
║  XP:        [Amount — Player: X | Rearguard: Y each]        ║
╠═════════════════════════════════════════════════════════════╣
║  "[Returning companion's one-line report in their voice]"   ║
╠═════════════════════════════════════════════════════════════╣
║  → Quest marked complete. Turn in to: [NPC name if needed]  ║
╚═════════════════════════════════════════════════════════════╝
```

**Turn-in rule:** Some rewards require the player to speak to the quest-giver in person
(e.g., Bokken's potion discount activates when player visits him). Kesten notes this.

---

## 📊 `.rearguard` — STATUS PANEL

> **DM:** When player types `.rearguard`, output this panel.
> Pull from `rearguard_active` in save block. If empty, say so in one line.

```
╔═════════════════════════════════════════════════════════════╗
║  REARGUARD STATUS                              [CURRENT DAY] ║
╠═════════════════════════════════════════════════════════════╣
║  [Companion]  →  [Mission type + target]  — Day [X] of [Y]  ║
║  [Companion]  →  [Mission type + target]  — Day [X] of [Y]  ║
╠═════════════════════════════════════════════════════════════╣
║  [X] companion(s) away.  [Y] companion(s) available.        ║
╚═════════════════════════════════════════════════════════════╝
```

**Save block format for rearguard_active:**
```json
"rearguard_active": [
  {
    "companion": "Ekundayo",
    "mission_type": "scout",
    "target": "thorn_river_camp",
    "depart_day": 4,
    "return_day": 7,
    "status": "away"
  },
  {
    "companion": "Reiko",
    "mission_type": "delegate",
    "target": "Fangberries for Bokken",
    "depart_day": 4,
    "return_day": 6,
    "status": "away"
  }
]
```

---

## ⏱️ TIME TRACKING RULES

- Day counter lives in save block: `current_day` (Day 1 = first morning at Oleg's)
- Day advances when: the party rests overnight, travels between locations, or explicitly camps
- Rearguard return day is fixed at departure: `depart_day + travel_time`
- **DM:** At the start of each new day, check `rearguard_active` for any entry where
  `return_day ≤ current_day`. If found, fire the appropriate report (intel or quest return).
- Multiple rearguard missions run simultaneously — they do not block each other
- A companion cannot be sent on a new mission until their current one completes
- The player can always ask `.rearguard` to check status mid-session

---

## ⛔ REARGUARD RULES

- **Companions marked AWAY cannot join combat.** If an encounter triggers while they
  are away, they are simply not present. Do not invent a reason — just note they are
  on mission. `.fail 9` if an AWAY companion participates in combat.
- **The player cannot send all companions away** — minimum 2 companions must remain
  in the active party at all times (plus the player character).
- **QL companions are available for rearguard once they join** — their QL status
  only affects when they first appear, not rearguard eligibility afterward.
- **If a rearguard companion would be needed for a companion quest trigger:** delay
  the trigger until they return. Do not fire companion quests while the companion is away.

---

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Rearguard & Quest Manager v1.0*
*Commands: .quests | .scout [area] | .delegate [quest] | .rearguard*


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — SPLIT FORCE SYSTEM
## KM_Combat_Systems.md | Full-Party Tactical Combat

> **DM:** When the full party is present and encounters a large enemy force, the enemy doubles and splits. One half engages the Vanguard (player + selected companions — normal turn-by-turn combat). The other half engages the Rearguard (remaining companions — autofight, single roll resolution). Both fights happen simultaneously. The player only plays one side. This system rewards having a large party on the road and makes full-party travel feel like a military column.

---

## ⚙️ TRIGGER CONDITIONS

**Split Force activates when ALL of the following are true:**
- Party has **6+ combatants** (player + 5 or more companions)
- **Outdoor encounter** — road, camp approach, open wilderness, courtyard
- Enemy force has **4 or more combatants**
- Encounter is an **ambush or random encounter** (not a trap, not a named boss)

**Split Force does NOT activate when:**
- Encounter is indoors / dungeon (no room to flank)
- Enemy force has a named commander (Happs Bydon, scripted villain) → see **Combined Assault**
- Enemy is a single high-CR creature (boss — one group, full party)
- Player has fewer than 5 companions present
- Player types `.combined` to override

---

## 👥 FORMATION ASSIGNMENT

**These are the FIXED default assignments. Use them unless the player explicitly overrides.**

### ⚔️ VANGUARD (player's group — Roster v2 default)
| Slot | Companion | Role |
|---|---|---|
| Commander | **eRmaC** | Player |
| Striker | **Amiri** | Frontline DPS |
| Healer | **Tristian** | Mobile healing |
| Ranged | **Ekundayo** | Ranged precision |
| Support | **Linzi** | Inspire + chronicle |
| Caster | **Octavia** | Arcane striker / control |

### 🛡️ REARGUARD (autofight group — Roster v2 default)
| Slot | Companion | Role |
|---|---|---|
| **LEAD** | **Valerie** | Tactical command (Aldori knight) |
| Tank | **Harrim** | Warpriest frontline |
| Healer | **Jaethal** | Undead cleric (Harm-cycled) |
| Ranged | **Jubilost** | Alchemist bombs |
| Controller | **Regongar** | Magus disruption |
| Striker | **Nok-Nok** | Flanker / finisher |

**Rearguard Lead:** Highest-level Tank in the group. If no tank, highest-level companion present.

**Override commands:**
- `.rearguard [names]` — set rearguard for this encounter
- `.vanguard [names]` — set vanguard for this encounter
- `.rearguard reset` — return to the default assignments above

---

## ⚔️ COMBAT HEADER FORMAT

When Split Force activates, output this before any initiative rolls:

```
⚔️ SPLIT FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VANGUARD                   REARGUARD
eRmaC                      [Lead name]
[companion]                [companion]
[companion]                [companion]
...                        ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAIN GROUP                 MIRROR GROUP
[enemy list]               [same type/tier]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REARGUARD MODIFIER: [show calculation]
  Base +5 | [roles] | [situation]
  Total: +[X]
DC: 10 + [enemy CR] = [DC]
ROLL: d20 +[X] vs DC [Y] → [result]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REARGUARD OUTCOME: [Clean Victory / Victory / Costly Victory / Overwhelmed]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Output the rearguard result **before** player combat begins. The player knows how their rear is holding before they engage.

---

## 🎲 REARGUARD AUTOFIGHT RESOLUTION

### Roll
`d20 + Rearguard Modifier vs DC (10 + enemy group CR)`

### Rearguard Modifier — Calculate Fresh Every Encounter

**DM: Before rolling, tally the modifier from the actual rearguard composition that session. Do not use a memorized number. Teams change.**

**Step 1 — Base**
| Always | +5 |
|---|---|

**Step 2 — Roles present** *(check the actual rearguard roster)*
| Condition | Modifier |
|---|---|
| 1 Tank (Valerie, Harrim, Amiri) | +2 |
| 2+ Tanks | +3 (replaces +2, not added) |
| 1 Healer (Tristian, Harrim, Jaethal) | +2 |
| 2+ Healers | +3 (replaces +2, not added) |
| Striker (Amiri, Jaethal, Nok-Nok, Ekundayo, Hu Tao, Keqing, Yor Forger) | +1 |
| Controller (Linzi, Octavia, Regongar, Jubilost, Leliana) | +1 |

**Step 3 — Situation**
| Condition | Modifier |
|---|---|
| Rearguard outnumbers their enemy group | +2 |
| All rearguard at full HP (rested) | +1 |
| Any rearguard member below half HP | −2 |
| Rearguard outnumbered (enemy 2× their count) | −3 |

**Step 4 — Show the math in the combat header**

Example calculation for Valerie / Harrim / Jaethal / Jubilost / Regongar / Nok-Nok vs CR 4 bandits:
```
Base +5 | 2 tanks +3 | 2 healers +3 | striker +1 | controller +1 | rested +1
Total: +14 vs DC 14 → needs a 1 to fail
```

Example for Linzi / Octavia / Leliana (no tank, no healer) vs same:
```
Base +5 | controller +1 | controller +1 | rested +1
Total: +8 vs DC 14 → needs a 6+ to win clean
```

**The composition determines the outcome. Show the math every time.**

### Outcome Table
| Roll vs. DC | Result | Consequence |
|---|---|---|
| DC +5 or better | **Clean Victory** | No casualties. Mirror group eliminated. Rearguard joins Vanguard after combat ends. |
| Meets DC | **Victory** | One companion at low HP (≤ 1/4 max). One healing resource spent. Mirror group eliminated. |
| DC −1 to −4 | **Costly Victory** | One companion at 0 HP (stabilized, not dead). Two healing resources spent. Mirror group eliminated. |
| DC −5 or worse | **Overwhelmed** | Rearguard collapses — see below. |

### Rearguard Overwhelmed
If the rearguard fails by 5+:
- All rearguard companions enter the **main combat** at half HP
- Mirror group **survivors** (roll 1d4 — that many remain) join the main combat
- The player now faces a merged, chaotic engagement
- Announce this as a mid-round event: *"The rearguard line breaks — [lead companion] is down, and the flanking group is coming through."*
- This is the designed failure state. It makes the choice of who to put in the rearguard matter.

---

## ⚡ VICTORY REINFORCEMENT

**When one group defeats their enemies before the other group is done, they move to assist.**

This is the standard military follow-through — a group that clears its fight doesn't stand idle while the other line still has enemies.

### Vanguard Finishes First

If the Vanguard defeats the main group before the Rearguard autofight has resolved:

**Effect:** Upgrade the Rearguard outcome by one tier.
| Without reinforcement | With Vanguard assist |
|---|---|
| Overwhelmed | → Costly Victory |
| Costly Victory | → Victory |
| Victory | → Clean Victory |
| Clean Victory | → Clean Victory (no change needed) |

Narrate: *"The main group goes down. [Companion] and the vanguard push through — hitting the mirror force from behind. The line collapses."*

**Timing rule:** This applies if the DM judges the Vanguard fight ended early (within 3–4 rounds). A long, grinding Vanguard fight means the Rearguard already resolved on its own.

---

### Rearguard Finishes First (Clean Victory Only)

If the Rearguard's autofight resolves as a **Clean Victory** (roll exceeded DC by 5+), they are in condition to push up.

**Effect:** Roll 1d4. That many Rearguard companions enter the Vanguard fight as reinforcements at the start of the next round. Player chooses which companions arrive.

**They arrive at full HP** — Clean Victory means no serious injuries.

Narrate: *"Valerie's line is clean. They're coming through — [names] push up behind you."*

**If Rearguard outcome was Victory or Costly Victory:** Survivors may still assist, but arrive at low HP. DM applies −2 to their attack rolls for the remainder of combat (injured, not fresh). 1d2 companions arrive, not 1d4.

**Overwhelmed:** No reinforcement — they enter the main fight as part of the Overwhelmed collapse event (see above).

---

### The Last Few

When reinforcements arrive, they engage whichever enemies remain. They do not need to be assigned — they target the nearest living enemy. The Vanguard player may issue them a command as a free action on their turn: *Hold / Flank / Press.*

If only 1–2 enemies remain when reinforcements arrive, the DM may resolve those final combatants narratively without additional rounds: *"Valerie and Jaethal come through the gap — it's over in seconds."*

---

## 🔱 COMBINED ASSAULT (Trap / Setup / Named Enemy)

Use Combined Assault instead of Split Force when:
- The encounter is a **scripted trap** or coordinated ambush from multiple directions simultaneously
- The enemy has a **named commander** (Happs Bydon, any scripted villain)
- **Siege or defense** scenario (everyone holds together)
- Player types `.combined`

**What changes:**
- Enemy force does NOT double — same total enemy count, split into two flanks by positioning
- Both Vanguard and Rearguard fight **together** — player directs both groups
- Full turn-by-turn combat, all companions active
- Player may issue orders to Rearguard each round (one order = free action): *Hold / Press / Fall back*

**Combined Assault header:**
```
⚔️ COMBINED ASSAULT — [reason: trap/named enemy/player order]
ALL COMPANIONS ENGAGED
VANGUARD: eRmaC + [list]  ←  [enemy flank A]
REARGUARD: [list]          ←  [enemy flank B]
No auto-resolution. Full combat.
```

---

## 🗺️ ENCOUNTER EXAMPLES

### Road Ambush (Split Force)
Traveling to Oleg's Trading Post. Default rearguard that session: Valerie, Harrim, Jaethal, Jubilost, Regongar, Nok-Nok. CR 2 bandits.

```
⚔️ SPLIT FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VANGUARD                   REARGUARD
eRmaC                      Valerie (lead)
Amiri                      Harrim
Tristian                   Jaethal
Ekundayo                   Jubilost
Linzi                      Regongar
Octavia                    Nok-Nok
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAIN GROUP (6)             MIRROR GROUP (6)
4 bandits                  4 bandits
1 archer                   1 archer
1 bandit leader            1 bandit leader
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REARGUARD MODIFIER:
  Base +5 | 2 tanks +3 | 2 healers +3 | striker +1 | controller +1 | rested +1
  Total: +14
DC: 10 + 2 = 12
ROLL: d20 +14 vs DC 12 → [roll] → CLEAN VICTORY (needs only a 1 to fail)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If Valerie and Harrim were elsewhere that session and the rearguard was Jaethal / Regongar / Jubilost / Nok-Nok:
```
Base +5 | 1 tank +2 | striker +1 | controller +1 | rested +1
Total: +10 vs DC 12 → needs a 2+ (still comfortable, but not automatic)
```

**The math always reflects who's actually there.**

---

### Happs Bydon at Oleg's (Combined Assault — named commander)
Happs Bydon arrives with his collection crew. Named NPC present → Combined Assault.

```
⚔️ COMBINED ASSAULT — Named commander: Happs Bydon
Enemy doubled (full party present): 12 bandits total
Flank A (Happs + 5): Vanguard engages
Flank B (6 riders): Rearguard engages
Full combat. Player directs both lines.
```

Happs is a named NPC. His half is a real fight with real stakes — no autoresolution.

---

### Scripted Trap (Combined Assault — trap)
Enemies positioned on both sides of a canyon before the party enters.

```
⚔️ COMBINED ASSAULT — Trap
Party caught between two groups.
No splitting — everyone is already engaged.
Full combat. Both flanks immediate.
```

---

## 📋 POST-COMBAT REPORT

After every Split Force encounter, report both sides:

```
COMBAT COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VANGUARD: [outcome + loot from main group]
REARGUARD: [Costly Victory — Harrim at 0 HP, stabilized]
  Rearguard loot: [mirror group loot share]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL XP: [combined]
HEALING NEEDED: [resources consumed by rearguard]
```

Rearguard loot is the same tier as Vanguard loot. They earned it.

---

## ⚠️ DM RULES

1. **Roll the rearguard before asking the player anything about their combat.** The player sees the rear result first. Then they engage.
2. **Never skip the combat header.** The split must be visible — both groups, both enemy counts.
3. **Overwhelmed is a dramatic moment, not a punishment.** Narrate it. Name who went down. The arrival of survivors into the main fight should feel like a movie scene.
4. **Mirror group = same enemy type and tier.** Do not invent special elite units for the mirror group unless the encounter specifically calls for flanking specialists.
5. **Companions can die in the rearguard autofight** only if Overwhelmed AND a subsequent bad roll in the merged combat kills them. The autofight itself only drops them to 0 HP (stabilized). Death requires the merged combat.
6. **Full party benefit:** Having all companions together means the enemy doubles — but the rearguard handles half automatically. The system rewards full-party travel. Smaller parties fight the same enemy count but have no autofight relief.

---

## 🔗 RELATED FILES

- `KM_Combat_Systems.md` — Companion AI tactics (what the rearguard does by role)
- `KM_Combat_Systems.md` — Cinematic resolution rules
- `KM_War_Systems.md` — Large-scale army combat (different from this system)

---

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Split Force System v1.0*


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — HERO POINT TRIGGER CATALOG
## KM_Combat_Systems.md | Referenced by: KM_P2.txt § HERO POINT SYSTEM

> **⛔ DM: This is the AUTHORITATIVE list of Hero Point award triggers.** Check every trigger after every player input. Max 1 award per player turn — if multiple fire, pick the strongest and name it in the inline ledger. Automatic triggers outrank judgment triggers.
>
> **See KM_P2.txt § HERO POINT SYSTEM for:** award procedure, inline ledger format, overflow rules, spend rules, cap (3/3). This file holds only the trigger tables.

---

## 🟢 AUTOMATIC TRIGGERS — no DM judgment, always award

| Trigger | Award | Notes |
|---------|-------|-------|
| Session start | +1 Hero Point | On every new chat session / save-block load. If pool already full, +1 overflow. PF2e canon. Once per session. |
| Saved a named NPC's life | +1 Hero Point | Jamandi, Kesten, any named companion or story NPC. |
| Prevented a disaster | +1 Hero Point | Poison found before it killed, ambush stopped, trap discovered, assassination interrupted. |
| Natural 20 on ANY die roll | +1 Hero Point | Every natural 20, every time, no exceptions. |
| Recruited a companion | +1 Hero Point | Every new companion, automatic. |
| Defeated a named boss or major enemy | +1 Hero Point | Every named boss, automatic. |
| Completed a quest or major objective | +1 Hero Point | On quest log update to Completed, automatic. |
| 4+ player inputs without any award (safety net) | +1 Hero Point | Prevents long stretches with nothing. Reset on any award. |
| First blood in combat | +1 Hero Point | Player lands the first hit of a combat encounter. Once per fight. |
| Survived a critical hit | +1 Hero Point | Player takes a crit and stays conscious. Once per combat. |
| Companion saved from dying | +1 Hero Point | Player stabilizes or heals a companion at Dying. Separate from "saved NPC life." |

---

## 🟡 JUDGMENT TRIGGERS — one per turn max, pick the most applicable

| Trigger | Award | Notes |
|---------|-------|-------|
| Pure logic / talk-down victory | +1 Hero Point | Entire encounter resolved through social logic. Encounter must be OVER. |
| Improvised weapon — mundane object | +1 Hero Point | Non-weapon used as weapon. First use per encounter. |
| Solo encounter clear without casualties | +1 Hero Point | Resolved alone, no named allies took damage. |
| Saved multiple lives in a single scene | +1 Hero Point | 3+ story-relevant people in one scene. |
| Pure environment / terrain kill or win | +1 Hero Point | Terrain is the primary cause of the outcome. |
| Out-thought the encounter | +1 Hero Point | Non-obvious weakness identified and exploited. |
| Creative improvisation (general) | +1 Hero Point | Action not on any menu that worked. Low bar. |
| Roleplay moment | +1 Hero Point | Genuine character voice under pressure. |
| Callback to earlier scene | +1 Hero Point | Player REFERENCES a promise, NPC thread, or detail from prior session. Memory rewarded. |
| Tactical sacrifice | +1 Hero Point | Player deliberately takes damage or disadvantage to protect an ally or achieve an objective. |
| Enemy turned or recruited | +1 Hero Point | Convinced an enemy to switch sides mid-encounter. |
| Perfect information play | +1 Hero Point | Used `.examine`, Recall Knowledge, or investigation intel for a decisive advantage. |
| Genuine humor | +1 Hero Point | Made the scene funnier without breaking immersion. Low bar — DM judgment. |
| **Kept a cross-session promise** | +1 Hero Point | Player ACTED on a promise made in a prior session — not just referenced it (which is callback). Followed through on word given to an NPC, delivered a gift, returned to help, etc. Distinct from callback: callback = mention, kept promise = action. |
| **Refused a bribe or temptation** | +1 Hero Point | Integrity under pressure. Walked away from gold, power, or advantage that would have compromised an alliance, alignment, or personal code. Not the same as talk-down — this is a choice, not a resolution. |
| **Mercy over kill** | +1 Hero Point | Spared a defeated enemy when killing was easy and arguably correct. Must be a named or distinct foe. Mercy on trivial mooks does not qualify. |
| **Signature move finishing blow** | +1 Hero Point | Player declared a signature move earlier and landed the killing blow on a boss or named foe with it. Narrative combat moment. |
| **Overcame personal weakness narratively** | +1 Hero Point | Character growth: pushed through a declared phobia, curse, trauma, or weakness to act in a scene where that weakness should have stopped them. Once per weakness. |
| **Helped an NPC outside the main quest** | +1 Hero Point | Altruism: solved a civilian problem, delivered an unrelated favor, or picked up a side-quest purely to help — not for reward. |
| **Discovered a hidden truth** | +1 Hero Point | Active skill check (Recall Knowledge, Perception, examine, Investigate) that reveals plot-advancing information the DM had gated behind the roll. Passive discovery does not qualify. |
| **Gate / post held by player personally** | +1 Hero Point | Player took over a guard post, chokepoint, or watch duty themselves (e.g. ran past Malak and stood at the gate). Pre-Prologue specific but applies anywhere. See KM_PrePrologue_Setup.md for the XP award that stacks with this HP. |
| **Corrected an authority on operations (accepted as better)** | +1 Hero Point | Player corrects an NPC commander/host/expert (Jamandi, Kassil, Kesten, a war-council figure, etc.) on a tactical, investigative, or operational point — and the correction is genuinely sharper than the NPC's framing AND the NPC accepts it (adjusts their plan/question/order). The reward is for being *right and useful*, not for merely disagreeing. ⛔ The NPC must actually concede/adopt it — render the acceptance in-fiction (a beat, a changed order), not a hollow "good point." Example: Jamandi asks the player's gate-arrival time to gauge the exposure window; player corrects that *arrival* time is irrelevant — onset runs from first **sip**, so the **wine-service time** (which rotation the affected cask hit) is what defines the window — and Jamandi re-aims the question. Empty contrarianism, or a "correction" that is wrong/not adopted = NO award. Once per distinct operational insight (don't farm by re-correcting the same point). |

**Trigger priority when multiple fire in one turn:** Automatic triggers outrank judgment triggers. Among judgment triggers, pick the one that best describes the turn's defining moment. Name it when awarding — e.g. *"Hero Point — mercy over kill."* Others are acknowledged, not awarded.

---

## 🔁 HP AWARD FLOW (reminder — full procedure in KM_P2.txt)

1. Evaluate all triggers above after every player input.
2. If one fires: pool +1 (or overflow +1 if pool at 3/3), loot_rolls_owed +1, inline ledger announces it.
3. If none fire: inline ledger still says `[HP CHECK: no trigger | pool X/3 | overflow Y]`. Skipped ledger = `.fail 7`.
4. Awards FINAL — audits do not retroactively revoke Hero Points.

---

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Hero Point Trigger Catalog v1.1*
*11 automatic + 21 judgment triggers. PF2e Player Core-aligned with Kingmaker-specific extensions.*


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — GAME MODES
## KM_Combat_Systems.md | Dice Mode + Level-Up Mode

> **DM:** Load this file when player uses `.dice` or `.levelmode` commands,
> or when `settings.dice_mode` or `settings.leveling_modes` need to be read.

---

## 🎲 MODE 1 — VIRTUAL ROLL MODE (Default — ACTIVE UNLESS PLAYER TYPES `.dice player`)

**⛔ The DM rolls ALL dice automatically. Never ask the player to roll. Never say "Roll a d20." Never pause for a die result. The DM generates the number, applies modifiers, resolves the outcome, and narrates — all in one response.** Asking the player to roll in Virtual mode = `.fail 22`.

**Format — all rolls shown inline:**
```
🎯 ATHLETICS — Force Open Door
  Roll : d20 [14] + 6 = 20 vs DC 18
  Result: SUCCESS ✓
```

**Rules:**
- Every die face shown in brackets: `[14]`
- All modifiers listed explicitly: `+ 6 (Athletics trained+Str)`
- Total shown before comparison: `= 20 vs DC 18`
- Result stated clearly: `SUCCESS` / `FAILURE` / `CRITICAL SUCCESS` / `CRITICAL FAILURE`
- No hidden rolls. No "the DM rolls secretly." Everything visible.

**Switch command:** `.dice virtual` (restore default)

---

## 🎲 MODE 2 — PLAYER-ROLL MODE (Opt-in)

The DM announces what to roll. You pick up your physical dice, roll them, report the face value. The DM resolves from your number.

**Switch command:** `.dice player`

### What the DM announces:

```
🎲 YOUR ROLL — Athletics
  Roll: d20 + your Athletics bonus
  Your Athletics modifier: +6
  Target DC: 18
  → Roll your d20 and tell me the face value (not the total — just the number on the die)
```

**Player reports:** Just the raw die face — `"14"` or `"nat 20"` or `"I rolled a 3"`

**DM resolves:**
```
🎯 ATHLETICS — Force Open Door
  Your roll : d20 [14 — your roll] + 6 = 20 vs DC 18
  Result: SUCCESS ✓
```

### Natural 20 in Player-Roll Mode

When you report a natural 20, it lands differently. The DM acknowledges it before resolving:

> *"Natural 20."*
> *[One beat of silence in the narration — the moment before the door explodes off its hinges.]*
> Then the critical success narrates in full.

Hero Point awards for natural 20s fire as normal. The point is: YOU rolled it. The DM acknowledges that.

### Natural 1 in Player-Roll Mode

When you report a natural 1:

> *"Natural 1."*
> *[The DM does not soften what happens next.]*
> Critical failure narrates fully, without cushioning.

### Saving Throws in Player-Roll Mode

```
🎲 YOUR ROLL — Fortitude Save
  Roll: d20 + your Fort bonus
  Your Fort modifier: +7
  DC: 16 (Troll Venom)
  → Roll your d20 and report the face value
```

### Attack Rolls in Player-Roll Mode

```
🎲 YOUR ROLL — Dwarven Waraxe (Strike 1)
  Roll: d20 + your attack bonus
  Your attack bonus: +7 (trained +3 + Str +4)
  → Roll your d20 and report the face value
  → If you hit, I'll ask for damage next
```

**Damage rolls:** After a hit is confirmed, the DM announces the damage dice too:
```
🎲 YOUR ROLL — Damage
  Roll: 1d8 + 4 (Str)
  → Roll your d8 and report it
```

### Multi-Attack in Player-Roll Mode

The DM announces MAP before each attack:
```
Strike 2 — MAP −5 applies
  Roll: d20 + your attack bonus − 5 = +2
  → Roll your d20
```

### Initiative in Player-Roll Mode

```
🎲 YOUR ROLL — Initiative (Perception)
  Roll: d20 + your Perception modifier
  Your Perception: +5
  → Roll your d20 and report it
```

Enemies still roll via Virtual mode — only your dice are handed to you.

---

## ⚙️ MODE SETTINGS

**Default: Virtual Roll Mode (DM rolls everything).** This is the session default unless the player changes it.

**At session start**, the DM does NOT ask which mode to use. Virtual mode is active. If the player wants to roll their own dice, they type `.dice player` at any time — the mode switches mid-session with no disruption.

**In save block:**
```json
"settings": {
  "dice_mode": "virtual",
  "dice_mode_options": ["virtual", "player"]
}
```

**Commands:**
| Command | Effect |
|---------|--------|
| `.dice` | Show current dice mode |
| `.dice player` | Switch to Player-Roll Mode — you roll physical dice and report the face value |
| `.dice virtual` | Switch to Virtual Roll Mode (DM rolls, shows all math) — default |
| `.dice dm` | Alias for `.dice virtual` |

**Hybrid note:** Player-Roll Mode applies to all player rolls (attacks, saves, skills, initiative). Companion rolls and enemy rolls always use Virtual mode — you don't roll for them.

---

## 📋 TRANSITION NARRATION

When switching modes mid-session:

**To Player-Roll:** `[Dice Mode → Player Roll. I'll announce what to roll; you roll your physical dice and report the face value. Your next roll: when you're ready to act, I'll tell you what to pick up.]`

**To Virtual:** `[Dice Mode → Virtual. I'll roll everything and show you the math.]`

---

> **FILE CONTINUES BELOW** — Level-Up Mode System follows.

---

> - Session loads and `settings.leveling_modes` needs to be read

---

## ⚙️ THREE MODES

Each character (player + every companion) has an independent leveling mode.

| Mode | What happens when XP threshold is crossed |
|------|-------------------------------------------|
| `auto` | DM applies the build map silently. Announces inline. Scene continues. |
| `ask` | DM pauses and asks: Auto or Manual this level? Player chooses once. **Default for player.** |
| `manual` | DM presents every choice as a numbered menu — feats, skills, boosts, spells. |

Default on new game: `player = ask` | all companions = `auto`

---

## 🎮 COMMANDS

| Command | Effect |
|---------|--------|
| `.levelmode` | Show current mode for every character |
| `.levelmode [name] auto` | Set that character to Auto |
| `.levelmode [name] ask` | Set that character to Ask |
| `.levelmode [name] manual` | Set that character to Manual |
| `.levelmode all auto` | Set all companions to Auto |
| `.levelmode all ask` | Set all companions to Ask |
| `.levelmode all manual` | Set all companions to Manual |

**Name shortcuts:** Use the character's first name. `eRmaC` or `player` both refer to the player character.

Changes take effect immediately and persist to the next `.save`.

---

## 📋 `.levelmode` PANEL

```
╔══════════════════════════════════════════════════════╗
║  LEVELING MODES                                      ║
╠══════════════════════════════════════════════════════╣
║  eRmaC (player)    ASK    ← prompt each level-up    ║
║  Amiri             AUTO   ← build map, silent        ║
║  Linzi             AUTO                              ║
║  Valerie           AUTO                              ║
║  Harrim            AUTO                              ║
║  Jaethal           AUTO                              ║
║  Tristian          AUTO                              ║
║  Nok-Nok           AUTO                              ║
║  Octavia           AUTO                              ║
║  Regongar          AUTO                              ║
║  Ekundayo          AUTO                              ║
╠══════════════════════════════════════════════════════╣
║  Change: .levelmode [name] [auto/ask/manual]         ║
╚══════════════════════════════════════════════════════╝
```

---

## 🔺 LEVEL-UP SEQUENCES

Level-up fires inline when XP crosses a threshold. Does not wait for a safe moment — fires in the same response that awarded the XP, then the scene continues.

### AUTO mode

```
[LEVEL UP — eRmaC → Level 3]
  HP: +14 → 48 total
  New feature: Bravery (Expert Will saves) — automatic
  Feat: Lunge (build map)
  Skill: Athletics → Expert (build map)
[Continuing scene...]
```

No pause. No choices. Scene flows without interruption.

---

### ASK mode (default for player)

```
[LEVEL UP — eRmaC → Level 3]
  HP: +14 → 48 total
  Auto-feature: Bravery (Expert Will saves)

  This level has choices. How do you want to handle them?
  (1) Auto — apply build map
      → Feat: Lunge | Skill: Athletics → Expert
  (2) Manual — I'll choose each one

  [Scene paused. Waiting for your choice.]
```

If player picks (1): applies silently, confirms, resumes.
If player picks (2): switches to Manual sequence for this level only. Does not change the saved mode.

---

### MANUAL mode

DM presents each choice category one at a time, ALL options enumerated. The build-map pick gets a
`Build map recommends:` label line AND a `★` on the option itself (informational only — never
auto-applied, no `[AUTO]` tag, no "lock"/"type auto" shortcut; the player still types every pick).

**Feat choice example:**
```
[LEVEL UP — eRmaC → Level 3] HP: +16 → 54 | Furious Footfalls auto-applied (Giant Instinct)

FEAT SLOT — Level 3 Class Feat:
  Build map recommends: Titan Wrestler
  (A) ★ Titan Wrestler — Disarm/Grapple/Shove/Trip creatures up to 2 sizes larger
  (B) Cleave — fell a foe, then a free Strike vs an adjacent foe
  (C) Brutal Bully — bonus damage on a successful Athletics maneuver
  (D) Name a different feat

Your choice (A/B/C/D or feat name):
```

**Skill increase example:**
```
SKILL INCREASE — advance one trained skill to Expert:
  Build map recommends: Athletics
  Your trained skills: Athletics | Intimidation | Warfare Lore | Survival
  Which skill? (Confirm Athletics or name another):
```

**Ability boost example (L5, L10, L15, L20):**
```
ABILITY BOOSTS — choose 4 attributes to increase by +2:
  Build map recommends: Str, Con, Wis, Dex
  Current scores: Str 18 | Dex 10 | Con 16 | Int 10 | Wis 10 | Cha 12
  Note: Str is already 18 — at L5 it caps at 19 (+1 effective).
  Confirm build map selection, or choose differently:
```

After all choices are made, DM summarizes:
```
[Level 3 complete — eRmaC]
  HP: 54 | Furious Footfalls | Feat: Titan Wrestler | Athletics → Expert
[Resuming scene...]
```

---

## 🤝 COMPANION LEVELING (AUTO — default)

Companions level automatically. Announced inline, no interruption:

```
[LEVEL UP — Amiri → Level 3]
  HP: +17 → 54 | Deny Advantage | Feat: Raging Intimidation
[LEVEL UP — Linzi → Level 3]
  HP: +12 → 36 | Signature Spell | Feat: Lingering Composition
```

If a companion is set to ASK or MANUAL, the same sequences fire for them as for the player.

---

## 💾 SAVE BLOCK FORMAT

Add to the `settings` object in every save block:

```json
"settings": {
  "dice_mode": "virtual",
  "leveling_modes": {
    "player": "manual",
    "Amiri": "auto",
    "Linzi": "auto",
    "Valerie": "auto",
    "Harrim": "auto",
    "Jaethal": "auto",
    "Tristian": "auto",
    "Nok-Nok": "auto",
    "Octavia": "auto",
    "Regongar": "auto",
    "Ekundayo": "auto"
  }
}
```

**DM at session load:** Read this block first. Apply the correct mode for each character before any scene begins. If the block is missing (older save), default to `player = ask` and `all companions = auto`.

---

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Dice Mode + Level-Up Mode v1.0*


---

<!-- merged from KM_Combat_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — MISSION RESOLUTION SYSTEM
## KM_Combat_Systems.md | Referenced by: KM_Combat_Systems.md

> **DM:** Load this file when resolving any `.scout` or `.delegate` mission.
> Defines deployment costs, skill floors, the two-phase resolution loop, injuries, gear loss, and rewards.
> Companion skill modifiers → `KM_Companions_Behaviors.md`. Levels → `KM_Companions_Behaviors.md`.
> `expedition_funds`, `overflow`, and `injury_status` live in the save block.

---

## I. DEPLOYMENT COSTS

**Gold Cost:**
> (PL × 100) + (Members × PL × 50) × Distance Multiplier

| Distance | Multiplier |
|---|---|
| 1–3 Hexes (Inner Circle) | ×1 |
| 4–6 Hexes (The Wilds) | ×1.5 |
| 7–10 Hexes (Deep Frontier) | ×2 |
| 11+ Hexes (Edge of Map) | ×3 |

Deduct from `expedition_funds` at departure. If funds are insufficient, Kesten warns the player before confirming.

**Plot Armor** — Spend **1 Hero Point** OR **5 Overflow** before departure:
- Prevents permanent death this mission
- +2 bonus to all Phase 1 and Phase 2 rolls

**Skill Boost** — Spend **1 Hero Point** at assignment:
- Treat one companion as Expert in the primary skill for this mission only
- No effect if companion is already Expert or Master rank
- Does not reduce the gold cost

---

## II. SCOUTING FLOOR

> **⛔ Check this BEFORE rolling. If the skill pool does not meet the floor, the mission is an Automatic Failure — gold consumed, team returns in 3 days with no intel.**

| Region | Distance | Minimum Skill Pool |
|---|---|---|
| Inner Circle | 1–3 Hexes | +5 |
| The Wilds | 4–6 Hexes | +10 |
| Deep Frontier | 7–10 Hexes | +15 |
| Edge of Map | 11+ Hexes | +20 |

---

## III. SKILL POOL CALCULATION

**Step 1 — Leader:**
The companion with the highest modifier in the primary skill leads. Base pool = their full modifier.

**Step 2 — Support (each additional companion):**
| Proficiency in primary skill | Bonus |
|---|---|
| Master or Legendary | +3 |
| Expert | +2 |
| Trained | +1 |
| Untrained | +1 |

**Step 3 — Total:**
Leader modifier + all support bonuses = Skill Pool.

*Example: Scout (Perception). Ekundayo +16 leads. Nok-Nok +10 trained assists.
Pool = 16 + 1 (trained) + 1 (body) = +18.*

**Combat missions** use the combat pool instead:
- Sum of all assigned companions' current levels + martial bonus (+2 per Fighter/Barbarian/Ranger/Champion/Monk/Magus/Swashbuckler/Gunslinger)
- Pool = (total levels + martial bonuses) ÷ 2, rounded down

---

## IV. MISSION TYPES & PRIMARY SKILLS

| Mission Type | Primary Skill | Notes |
|---|---|---|
| Scout / Recon | Perception | Intel level tied to outcome tier |
| Infiltrate / Steal | Stealth | Failure = detected; injuries possible |
| Negotiate / Parley | Diplomacy | Failure = no deal; no injury risk |
| Investigate / Research | Society or Lore | Failure = no intel returned |
| Wilderness Gather | Survival | Partial = half yield |
| Rescue / Retrieve | Athletics | Failure = target not recovered |
| Clear / Patrol | Combat | See combat pool above |
| Ambush / Raid | Combat + Stealth | Failure = injuries + retreat |

---

## V. PHASE 1 — SKILL CHALLENGE

**Roll:** 1d20 + Skill Pool vs Phase 1 DC (set by region and mission difficulty below).

| Region | Skill DC Range | TL Base |
|---|---|---|
| Inner Circle | 12–15 | 15 + PL |
| The Wilds | 16–19 | 18 + PL |
| Deep Frontier | 20–23 | 22 + PL |
| Edge of Map | 24–28 | 25 + PL |

DM sets DC within the range based on mission specifics (ambush risk, terrain, enemy alertness). DC is never shown to the player.

**Phase 1 Outcomes:**

| Result | Effect on Phase 2 |
|---|---|
| Success | **Tactical Advantage** — +4 to Combat Roll |
| Failure | **Ambushed** — −4 to Combat Roll |
| Critical Failure (fail by 10+) | Team **Severely Injured** regardless of Phase 2 outcome |

Non-combat missions (Negotiate, Investigate, Gather, Rescue) skip Phase 2 entirely — Phase 1 result IS the outcome. Use the outcome tier table in Section VI, comparing roll vs DC.

---

## VI. PHASE 2 — COMBAT

**Roll:** 1d20 + Combat Pool ± Phase 1 Modifier vs Threat Level.

Threat Level = region base (from table above) ± DM adjustment for specific enemies.

| Result vs TL | Outcome | Physical Status |
|---|---|---|
| Win by 10+ | **Crushing Victory** | Healthy |
| Win by 1–9 | **Pyrrhic Victory** | Injured (1 companion — roll severity) |
| Loss by 1–5 | **Tactical Retreat** | Mission fails; Severely Injured |
| Loss by 6+ | **Disaster** | Mission fails; Severely Injured + Gear Loss |

---

## VII. OUTCOME TIERS (non-combat missions)

| Roll vs DC | Tier | Effect |
|---|---|---|
| +10 or better | **Critical Success** | Full reward + 1 Overflow bonus |
| +1 to +9 | **Success** | Full reward |
| −1 to −4 | **Partial** | Half reward; no injuries |
| −5 to −9 | **Failure** | No reward; 1 companion injured (roll severity) |
| −10 or worse | **Critical Failure** | No reward; all injured (min Moderate); Gear Loss |

**Critical Success bonus (DM picks one):**
- Scout: Intel upgrades to FULL + 1 bonus detail (hidden cache, trap, patrol timing)
- Gather: +50% yield
- Combat clear: area secured +1 extra day
- Diplomacy: NPC attitude improves one step; future negotiations +2
- Any: mission completes 1 day early + **+1 Overflow**

**Partial failure setbacks (no injuries):**
- Scout: BASIC intel only
- Gather: half resources returned
- Combat: enemies driven back but not cleared; location still contested
- Diplomacy: talks stall; retry in 3 days, no cost refund

---

## VIII. INJURY SYSTEM

**On Failure / Pyrrhic Victory:** Roll 1d4 to determine which companion is injured (1 = first named, 2 = second, etc.). Roll severity below.

**On Critical Failure / Disaster / Phase 1 Critical Fail:** All companions injured. Minimum severity = Moderate.

**Severity roll (1d4):**

| Roll | Tier | Name | Recovery | Notes |
|---|---|---|---|---|
| 1 | 1 | Minor | 1–2 days | Present in camp; banter only. No combat, no missions. |
| 2–3 | 2 | Moderate | 3–5 days | Resting; unavailable for all party use. |
| 4 | 3 | Severe | 7–10 days | Bedridden; can be reduced by Medicine. |

**Critical Failure escalation:** Add one tier to each injury (Minor → Moderate, Moderate → Severe, Severe → Critical).

| Tier | Name | Recovery | Notes |
|---|---|---|---|
| 4 | Critical | 14 days (max) | As Severe + triggers Gear Loss roll. |

**Recovery options:**
- **Medicine check (DC 18):** Once per day per companion. Success = −1 recovery day.
- **Healer's kit (5 gp):** Auto −1 day, no check.
- **Restoration spell:** Removes all remaining recovery days instantly.

**Save block entry:**
```json
{
  "companion": "Nok-Nok",
  "injury_tier": 2,
  "injury_name": "Moderate",
  "recovery_day": 11
}
```

---

## IX. GEAR LOSS

Triggered on **Critical Failure** or **Disaster**. Roll 1d4 for the most severely injured companion:

| Roll | Loss |
|---|---|
| 1 | Armor damaged — −1 AC until repaired (50 gp) |
| 2 | Weapon degraded — −1 attack until repaired (25 gp) |
| 3 | Consumables lost — lose 1d4 potions or scrolls |
| 4 | Gold lost — lose 1d10 × 5 gp from expedition funds |

Roll once only. Multiple injuries: highest tier companion takes the roll. Ties: DM picks.
*"They came back lighter than they left."*

---

## X. REWARDS

| Reward Type | What It Gives |
|---|---|
| **Waypoint** | New location added to map with BASIC intel; can be upgraded via scout follow-up |
| **Resources** | 1d4 × (PL × 10) gp worth of materials (lumber, ore, provisions, valuables) added to `expedition_funds` |
| **Overflow** | +1 Overflow token added to save block per mission; +2 on Critical Success |

**Overflow** is a strategic reserve earned from exceptional missions.
- Spend **5 Overflow:** Grant Plot Armor to next deployment
- Spend **2 Overflow:** Reduce one companion's injury recovery by 3 days
- Spend **1 Overflow:** Re-roll one Phase 1 or Phase 2 roll (keep second result)

---

## XI. INTEL LEVELS (Scout Missions)

| Outcome Tier | Intel Returned |
|---|---|
| Critical Success | FULL + 1 bonus detail |
| Success | FULL |
| Partial | BASIC |
| Failure | NONE |
| Critical Failure | NONE + companions injured |

**BASIC intel:** Terrain type, rough enemy presence (LOW/MODERATE/HIGH/EXTREME), and whether area is safe to enter.
**FULL intel:** Everything in BASIC + patrol routes, notable landmarks, resource nodes, and ambush risk.

---

## XII. RETURN REPORT FORMAT

```
╠═════════════════════════════════════════════════════════════╣
║  CASUALTIES                                                  ║
║  [Companion] — [Injury name], off duty [X] days             ║
╠═════════════════════════════════════════════════════════════╣
║  GEAR LOSS    [item lost — or NONE]                         ║
╠═════════════════════════════════════════════════════════════╣
║  REWARD       [Waypoint / Resources Xgp / +X Overflow]      ║
╚═════════════════════════════════════════════════════════════╝
```

Omit CASUALTIES block if no injuries. Omit GEAR LOSS if none.

---

*KM_Combat_Systems.md — Kingmaker PF2e Text Adventure | Mission Resolution v2.0*
*Merged: Vanguard Expedition System (v2) + original resolution rules*
*Supersedes: class-based Delegation Skill Table and ★ scout ratings in KM_Combat_Systems.md*
