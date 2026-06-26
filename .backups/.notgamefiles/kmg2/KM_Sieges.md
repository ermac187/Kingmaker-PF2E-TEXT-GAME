# KINGMAKER — SIEGE WARFARE
## KM_Sieges.md | Active from: Chapter 5 | Referenced by: KM_ArmyCombat.md, KM_Buildings.md

> **DM:** Siege warfare is a multi-round encounter where armies attack or defend fortified positions. Building defense bonuses (KM_Buildings.md) apply directly. Sieges resolve in 4 phases. The player makes strategic decisions at each phase. Used during Ch5 (Pitax War) and Ch6 (Bloom siege).

---

## 🏰 SIEGE PHASES

### PHASE 1 — APPROACH (1-2 rounds)
Attackers advance toward walls. Defenders have ranged advantage.
- **Defender:** Archer armies fire at full bonus. Fortification traps trigger.
- **Attacker:** Must cross open ground. −2 Defense while approaching. Siege equipment can fire.
- **Player choice (defender):** Focus fire on siege equipment OR spread damage across approaching units.
- **Player choice (attacker):** Rush (fast, high casualties) OR methodical (slow, fewer losses, siege equipment first).

### PHASE 2 — BREACH (2-3 rounds)
Attackers attempt to breach walls. Defenders hold the line.
- **Breach check:** Attacker Siege Equipment rolls d20 + Siege Offense vs Wall Defense (AC + fortification bonus)
- **Walls:** AC 20 base + Fort bonus (+4) + Moat (+2 if present) = up to AC 26
- **Breach success:** Gap opened. Phase 3 begins at that point.
- **Breach failure:** Walls hold. Attackers take 1d6 splash damage from defenders.
- **Sally port:** Defender can send 1 army OUT to attack siege equipment directly (risky but can end the siege).

### PHASE 3 — ASSAULT (2-4 rounds)
Attackers pour through breach. Close combat at the walls.
- **Funnel effect:** Only 1 attacker army can engage through each breach per round.
- **Defender bonus:** +2 Defense from elevated position (walls, towers).
- **Player choice:** Hold the breach (Shield Wall formation optimal) OR counter-charge through.
- **Building bonuses:** Each defensive building in the settlement provides one bonus per siege:
  - Watchtower: +1 to ranged attacks
  - Fort: +2 Defense for garrison
  - Barracks: Militia reinforcement (1 extra Strength per round for 3 rounds)
  - Temple: Morale +2 for defenders (divine blessing)

### PHASE 4 — HOLD (1-2 rounds)
The outcome is decided. One side breaks.
- **Attacker morale check:** If 50%+ attackers lost → DC 18 morale check or retreat.
- **Defender morale check:** If breach held for 3+ rounds by attackers → DC 16 morale check or surrender.
- **Player can negotiate surrender** at any point (Diplomacy DC 16). Terms affect reputation and faction relations.
- **Last stand:** If defender chooses Defensive Circle formation, morale cannot break. Fight to the last.

---

## 🔧 SIEGE EQUIPMENT

| Equipment | Offense | Target | Special |
|-----------|---------|--------|---------|
| **Battering Ram** | +6 vs gates | Gates only | Ignores wall AC bonus. Gate HP: 30. |
| **Catapult** | +4 vs walls | Walls, buildings | 2d8 damage per hit. Range: 3 hexes. |
| **Siege Tower** | — | Walls | Negates wall height advantage. Allows direct wall assault. |
| **Boiling Oil (defender)** | +5 vs attackers at walls | Attackers in breach | 3d6 fire damage. 1 use per siege. |
| **Greek Fire (defender)** | +6 vs siege equipment | Siege towers, rams | Sets equipment on fire. Destroyed in 2 rounds. |

---

## 📋 SIEGE DISPLAY FORMAT

```
══════════════════════════════════════════════
SIEGE OF {Location} — Phase {N}: {Phase Name} | Round {R}
══════════════════════════════════════════════
WALLS: HP {current}/{max} | Breach: {None/Partial/Full}
DEFENDER ARMIES:
 {Army}: Str {N}/{max} | Position: {Wall/Gate/Reserve}
ATTACKER ARMIES:
 {Army}: Str {N}/{max} | Position: {Approaching/At walls/Through breach}
SIEGE EQUIPMENT: {List with status}

YOUR ORDERS:
 1. {Army action} | 2. {Army action}
 3. General ability | 4. Negotiate surrender
══════════════════════════════════════════════
```

**Save block:** `"siege_state": {"location": "capital", "phase": 2, "wall_hp": 45, "breaches": 0, "round": 3}` (null when no siege active)

---

## ⚔️ SCRIPTED SIEGE 1 — THE SIEGE OF THE CAPITAL (Ch5)

**Trigger:** Pitax invasion reaches the capital. Fires if player did not intercept Pitax army at the border.

```
SIEGE OF {Capital Name} — Pitax Invasion
══════════════════════════════════════════════════════
DEFENDER: Player's armies + garrison + fortifications
ATTACKER: Pitax Royal Guard (Str 8, Off +8, Def 18)
          River Mercenaries ×2 (Str 7, Off +5, Def 14)
          Pitax Cavalry (Str 6, Off +7, Def 15)
          Pitax War Mages (Str 4, Off +6, Def 12)
          Siege: 2 Catapults, 1 Battering Ram, 1 Siege Tower
WALLS: HP 60 | AC 20 + fortification bonuses
GATE: HP 30 | AC 18
══════════════════════════════════════════════════════
```

### Phase-by-Phase Script

**PHASE 1 — APPROACH (2 rounds):**
> *Dust on the horizon. Then banners — Pitax crimson and gold. The army spreads across the fields like a stain. Catapults are already being wheeled into position. The War Mages form a line behind the infantry, hands glowing.*

Player commands:
```
 1. Archer fire — focus catapults  [Frontier Scouts or wall archers]
 2. Archer fire — spread across infantry  [reduce Str before breach]
 3. Hold fire — conserve arrows for Phase 3
 4. Sally port — send cavalry to hit siege equipment  [risky: cavalry exposed]
 5. Activate trapped approaches  [if Trapped Approach fortification built]
 6. General ability  [1/battle special]
 7. Address the defenders  [Diplomacy/Intimidation — Morale +1 on success]
```

**PHASE 2 — BREACH (2-3 rounds):**
> *The catapults fire. Stone hits stone. The wall shakes but holds. The ram advances toward the gate — soldiers carrying it under heavy shields. The Siege Tower creaks forward on the left flank.*

- **Catapult vs Walls:** d20+4 vs Wall AC. Hit: 2d8 damage to wall HP.
- **Ram vs Gate:** d20+6 vs Gate AC 18. Hit: 2d10 damage to gate HP.
- **War Mages:** Fire at wall defenders each round. d20+6, 2d6 fire per army targeted.
- **Player decision:** Boiling oil the ram (3d6, 1 use) OR Greek Fire the tower (destroyed in 2 rounds) OR hold for Phase 3.

**If gate breaks first:** Pitax infantry floods through. Phase 3 at the gate.
**If wall breaches first:** Pitax infantry at the wall. Phase 3 at the breach.
**If neither by Round 5:** Pitax commits all forces simultaneously. Both gate and wall under pressure.

**PHASE 3 — ASSAULT (3-4 rounds):**
> *They are through. The first Pitax soldiers come screaming through the breach — Royal Guard in crimson plate, shields locked. Behind them, more. The funnel holds them for now, but the pressure is building.*

- **Funnel:** 1 attacker army per breach per round.
- **Defender wall bonus:** +2 Defense.
- **Militia fires:** If Barracks built, +1 Str/round for 3 rounds (citizens joining the fight).
- **Critical moment (Round 2 of assault):** Irovetti's Champions arrive as reserve. Str 5, Off +10, Def 17, Morale 18. They target the player's strongest army.

Player commands:
```
 1. Hold the breach — Shield Wall  [Defense +4, no attack]
 2. Counter-charge through  [Offense +2, Defense −2]
 3. Fall back to inner defenses  [lose wall bonus, gain time]
 4. Commit reserve army  [if held in reserve]
 5. Personal intervention  [player enters combat personally — see below]
 6. Negotiate surrender  [Diplomacy DC 20 — Irovetti's terms]
```

**PERSONAL INTERVENTION:** If the player enters the breach personally, switch to standard PF2e combat. The player + active companions fight Irovetti's Champions (use elite stat blocks from KM_Bestiary.md). Victory: enemy army Morale −3. Defeat: player captured (Death Door negotiation).

**PHASE 4 — HOLD (1-2 rounds):**
> *The fighting at the breach has gone on longer than either side expected. Bodies on both sides. The question is who breaks first.*

- **Pitax morale check:** DC 18. River Mercenaries break first (Morale 10 — lowest). If they rout, Pitax army loses 2 Str total.
- **If Irovetti's Champions are destroyed:** All Pitax armies −2 Morale immediately.
- **Defender morale:** If player army Str total > 50% of starting, defenders hold automatically. If below 50%: DC 16 morale check.
- **Negotiated surrender:** Irovetti offers terms (keep your title, cede 3 border hexes, pay 500 gp/turn tribute). Player can accept, counter-offer (Diplomacy DC 22), or refuse (fight to the end).

**VICTORY:** Pitax army routs. +3 Stability, +2 Reputation. Loot: siege equipment captured (2 Catapults for player army). Pitax faction −3. War continues to Pitax counterattack.
**DEFEAT:** Capital falls. Kingdom relocates to secondary settlement. Unrest +5. Reconquest required (1-2 chapter turns).

---

## ⚔️ SCRIPTED SIEGE 2 — SIEGE OF PITAX (Ch5, Player Attacking)

**Trigger:** Player army marches on Pitax after defending the capital (or instead of defending, if player struck first).

```
SIEGE OF PITAX — Player Invasion
══════════════════════════════════════════════════════
ATTACKER: Player's armies + allies
DEFENDER: Pitax City Guard (Str 10, Off +6, Def 16)
          Irovetti's Champions (Str 5, Off +10, Def 17)
          Pitax War Mages (Str 4, Off +6, Def 12)
WALLS: HP 80 | AC 22 (Pitax is well-fortified)
GATE: HP 40 | AC 20 (reinforced iron)
SPECIAL: Irovetti has rigged the palace with traps
══════════════════════════════════════════════════════
```

**PHASE 1 — APPROACH:** Player brings siege equipment or improvises.
- **If Catapults captured from Siege 1:** Player has siege capability. Normal approach.
- **If no siege equipment:** Must find another way in. Options: infiltration team through sewers (Stealth DC 18 party check), bribe a gate guard (Diplomacy DC 20 + 200 gp), wait for a defector to open a postern gate (1d4 rounds, unreliable).

**PHASE 2 — BREACH:** Pitax walls are stronger (AC 22). Catapult needs 3+ hits to breach.
- **War Mages on walls:** Fire down at attackers. 2d6 fire per round per army in range.
- **Infiltration option:** If the sewer team succeeds, they open the gate from inside. Skip Phase 2.
- **Darven's supply maps** (if obtained from KM_AdvisorEvents.md A5-3): reveal weak point in east wall. Breach there: AC 16 instead of 22.

**PHASE 3 — ASSAULT:** Street fighting inside Pitax.
- No funnel — open streets. Multiple armies can engage.
- **Civilian considerations:** Pitax citizens are NOT combatants. Collateral damage = Reputation −2 per round of indiscriminate fighting. Player must choose: careful advance (slow, fewer casualties) or aggressive push (fast, collateral risk).
- **Palace approach:** Irovetti retreats to the palace. Trapped corridors: 2d6 damage per army that enters without disarming (Thievery DC 18).

**PHASE 4 — THE PALACE:**
- **Army cannot enter the palace.** Too narrow. This becomes a personal combat encounter.
- Player + companions enter. Irovetti + Champions + trapped rooms.
- **Irovetti's last stand:** He fights from his throne room. If cornered: attempts to bargain, then fights, then tries to flee via secret passage (Perception DC 20 to spot the passage before he reaches it).

**VICTORY:** Pitax conquered. Player chooses: annex (Economy +5, faction absorbed), install puppet ruler (Economy +3, faction neutral), burn it (Reputation −3, faction destroyed, +1 Ruthless). War ends.

---

## ⚔️ SCRIPTED SIEGE 3 — THE BLOOM SIEGE (Ch6)

**Trigger:** The Bloom reaches the capital. This is not a military siege — it's a survival horror defense against a living infection.

```
SIEGE OF {Capital Name} — The Bloom
══════════════════════════════════════════════════════
ATTACKER: The Bloom itself
          Bloom Swarm (Str 12, Off +4, Def 10, Morale ∞)
          Nyrissa's Thorns (Str 8, Off +7, Def 14, Morale ∞)
          Fey Knights (Str 6, Off +8, Def 16)
DEFENDER: Player's remaining armies + garrison
WALLS: Standard — but Bloom ignores walls (grows over/through)
SPECIAL: Bloom regenerates. Fire is the only permanent solution.
══════════════════════════════════════════════════════
```

**THIS SIEGE IS DIFFERENT.** The Bloom is not an army — it's an environment. It grows. Walls slow it but don't stop it. The siege is a timer: hold long enough for the player to reach Nyrissa's domain and end the Bloom at the source.

**PHASE 1 — THE BLOOM ARRIVES (1 round):**
> *It doesn't march. It grows. The treeline at the edge of your kingdom darkens. Flowers appear — beautiful, wrong. The roses climb the walls like they know where the handholds are. The air smells sweet. That's how you know it's started.*

- **No approach phase.** The Bloom is already at the walls.
- **Defender action:** Set fires along the walls (burns Bloom back 1 round). Druid/nature magic: slow the growth (Nature DC 20, buys 2 rounds).

**PHASE 2 — OVERGROWTH (2-3 rounds):**
- Bloom Swarm climbs walls. Strength regenerates +1/round unless fire applied.
- Nyrissa's Thorns entangle defenders. Enemy movement: free. Defender movement: halved.
- **Fire is everything.** Armies with fire capability (alchemist fire, fire spells, burning oil) deal double damage. Armies without fire: half damage (Bloom regenerates faster than they kill).
- **Fey Knights:** Teleport inside the walls. Target the player's weakest army or siege equipment.

**PHASE 3 — HOLDING ACTION (3+ rounds):**
The player is not trying to win this siege. They are trying to hold long enough to leave.
- **Each round held:** +1 to the player's head start reaching Nyrissa's domain.
- **General left in command:** When the player leaves for the final dungeon, the General (companion) takes command. Their skill modifier determines defense quality while the player is gone.
- **Evacuation option:** Councilor can evacuate civilians (2 rounds, Loyalty +2). If not evacuated and Bloom breaches: civilian casualties (Reputation −3).

**PHASE 4 — THE PLAYER LEAVES:**
> *The Bloom presses. The walls are flowering. Your General holds the line. You look back once — at the kingdom you built, wrapped in roses that are eating it alive — and then you go. Toward the source. Toward the end.*

**No victory at the siege.** The siege ends when the player defeats Nyrissa (or saves her). If the Bloom is ended: the siege dissolves. Roses wither. Walls scarred but standing. If the player fails: the kingdom falls. Ending 1 (default) triggers with a damaged kingdom epilogue.

---

## 📊 SIEGE AFTERMATH

After any siege, regardless of outcome:

| Condition | Effect |
|-----------|--------|
| Walls intact | Repair cost: 4 RP. Ready in 1 turn. |
| Walls breached | Repair cost: 8 RP. 2 turns. Vulnerable to raids during repair. |
| Gate destroyed | Repair cost: 6 RP. 1 turn. |
| Buildings damaged | Per building repair: 50% of original RP cost. |
| Civilian casualties | Loyalty −1 per 100 estimated casualties. Reputation −1. |
| Army losses | Rebuild at recruitment cost. Veteran status lost — new units start fresh. |
| Siege equipment captured | Free for player army use. Maintenance: 1 RP/turn stored. |

---

*KM_Sieges.md — Kingmaker PF2e Text Adventure | Siege Warfare v2.0*
*3 scripted sieges: Capital Defense, Pitax Assault, Bloom Survival.*
