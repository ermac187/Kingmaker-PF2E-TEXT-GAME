# KINGMAKER — ARMY TACTICAL COMBAT
## KM_ArmyCombat.md | Active from: Chapter 4 | Referenced by: KM_Kingdom.md, KM_BorderConflicts.md

> **DM:** Text-based army combat for kingdom-scale battles. Simplified round structure with formations, morale, and general abilities. Used during chapter army encounters (Ch4 Tiger Lords, Ch5 Pitax War) and border conflicts. Not a replacement for personal combat — armies fight while the player handles the command layer.

---

## 📊 ARMY STAT BLOCK FORMAT

```
{Army Name} — {Faction}
Strength: {1-20} | Offense: +{N} | Defense: {AC}
Morale: {1-20} | Speed: {1-3 hexes/turn}
Type: {Infantry/Cavalry/Archers/Siege/Elite}
General: {Companion name or NPC}
Formation: {Current formation}
Special: {Any unique abilities}
```

---

## ⚔️ ARMY COMBAT PROCEDURE

### Round Structure
1. **Command Phase:** Player chooses formation and target for each army
2. **Engagement Phase:** Armies attack (opposed rolls)
3. **Morale Phase:** Check morale for armies that took losses
4. **Movement Phase:** Armies reposition on hex map

### Attack Resolution
```
Attacker rolls: d20 + Offense + Formation bonus vs Defender's Defense
Hit:  Defender Strength −1 (−2 on crit)
Miss: No effect
Crit: Strength −2 + Morale −1
```

### Formations

| Formation | Offense Mod | Defense Mod | Special |
|-----------|------------|------------|---------|
| **Line** | +0 | +0 | Default. Balanced. |
| **Shield Wall** | −2 | +4 | Infantry only. Cannot charge. |
| **Skirmish** | +1 | −2 | Can disengage without penalty. |
| **Hammer & Anvil** | +3 | −1 | Requires 2 armies coordinating. Flanking bonus. |
| **Charge** | +4 | −3 | Cavalry only. First round only. Must have clear approach. |
| **Arrow Rain** | +2 (ranged) | −2 | Archers only. Range: 2 hexes. Cannot melee. |
| **Defensive Circle** | −3 | +5 | Last stand. Cannot move. Morale +2. |

### Morale Checks
**Trigger:** Army loses 25%+ Strength in one round, or General killed/captured.
```
Morale Check: d20 + current Morale vs DC 15
Success: Army holds. Morale −1.
Failure: Army BREAKS. Retreats 1 hex. Cannot attack next round.
Crit Fail: Army ROUTS. Retreats 2 hexes. Strength −2 (desertion). Will not fight again this battle without rally.
```

**Rally:** General uses Command Phase to rally (Diplomacy or Intimidation DC 16). Success: broken army re-engages. Failure: army retreats further.

### General Abilities
The companion assigned as General grants one special ability per battle:

| Companion Type | General Ability | Effect |
|---------------|-----------------|--------|
| **Martial (Fighter, Barb, Ranger)** | Inspire Troops | +2 Morale for 1 round. 1/battle. |
| **Caster (Wizard, Druid, Cleric)** | Magical Barrage | +1d6 damage to one enemy army. 1/battle. |
| **Skill (Rogue, Investigator, Bard)** | Tactical Feint | Enemy formation bonus negated for 1 round. 1/battle. |
| **Leader (Commander, Champion)** | Hold the Line | One army ignores morale check. 1/battle. |

---

## 🏰 PLAYER ARMY ROSTER (Base)

Starting armies available from Chapter 4:

| Army | Str | Off | Def | Morale | Type | Notes |
|------|-----|-----|-----|--------|------|-------|
| Kingdom Militia | 8 | +4 | 14 | 10 | Infantry | Cheap, expendable, loyal |
| Royal Guard | 6 | +7 | 17 | 16 | Elite | Player's best unit |
| Frontier Scouts | 5 | +5 | 13 | 12 | Archers | Range 2 hexes, +2 in forests |
| Cavalry Lancers | 5 | +6 | 15 | 14 | Cavalry | Charge +4 first round |

Additional armies from faction rewards (KM_Reputation.md), recruitment orders (KM_StandingOrders.md), and adventurer board hires.

---

## 📋 BATTLE DISPLAY FORMAT

```
══════════════════════════════════════════════
ARMY BATTLE — {Battle Name} | Round {N}
══════════════════════════════════════════════
YOUR FORCES:
 1. {Army}: Str {N}/{max} | Formation: {X} | General: {Name}
 2. {Army}: Str {N}/{max} | Formation: {X}

ENEMY FORCES:
 A. {Army}: Str {N}/{max} | Formation: {X}
 B. {Army}: Str {N}/{max} | Formation: {X}

COMMAND:
 Army 1 → Target: [A/B] | Formation: [change?]
 Army 2 → Target: [A/B] | Formation: [change?]
 General Action: [Ability / Rally / Command]
══════════════════════════════════════════════
```

---

## 🏴 ENEMY ARMY ROSTER BY CHAPTER

### Chapter 4 — Tiger Lord Armies
| Army | Str | Off | Def | Morale | Type | Special |
|------|-----|-----|-----|--------|------|---------|
| Tiger Lord Warband | 10 | +7 | 14 | 16 | Infantry | Rage: +2 Off first round, −2 Def |
| Tiger Lord Raiders | 6 | +8 | 12 | 14 | Cavalry | Charge +4. Hit-and-run: disengage free |
| Armag's Elite | 8 | +9 | 16 | 18 | Elite | Fearless (immune to morale break). Last unit standing fights to death |
| Kellid Archers | 5 | +5 | 11 | 12 | Archers | Range 2. Poison arrows: −1 Morale on hit |

### Chapter 5 — Pitax Armies
| Army | Str | Off | Def | Morale | Type | Special |
|------|-----|-----|-----|--------|------|---------|
| Pitax Royal Guard | 8 | +8 | 18 | 16 | Elite | Shield Wall default. Disciplined. |
| River Mercenaries | 7 | +5 | 14 | 10 | Infantry | Desert at Morale 5 (low loyalty) |
| Pitax Cavalry | 6 | +7 | 15 | 14 | Cavalry | Charge +4. Lance: +2 vs infantry |
| Pitax War Mages | 4 | +6 | 12 | 12 | Archers (magical) | Range 3. AoE: hits 2 units. Fragile. |
| Irovetti's Champions | 5 | +10 | 17 | 18 | Elite | Irovetti's personal guard. Will not break while Irovetti lives |

### Chapter 6 — Bloom/Fey Armies
| Army | Str | Off | Def | Morale | Type | Special |
|------|-----|-----|-----|--------|------|---------|
| Bloom Swarm | 12 | +4 | 10 | 20 | Infantry | Mindless: immune to morale. Regenerate +1 Str/round unless fire applied |
| Fey Knights | 6 | +8 | 16 | 16 | Cavalry | Teleport: ignore terrain. Illusion: first attack against them auto-misses |
| Treant Guardians | 4 | +6 | 20 | 18 | Infantry | Massive: immune to Charge. Vulnerable: fire (+4 Off against them with fire) |
| Nyrissa's Thorns | 8 | +7 | 14 | — | Elite | No morale (Bloom-driven). Fight until Str 0. Entangle: enemy movement halved |

---

## 🛡️ ADDITIONAL PLAYER ARMIES (Recruitable)

| Source | Army | Str | Off | Def | Morale | Type | How to Get |
|--------|------|-----|-----|-----|--------|------|------------|
| Faction (Aldori) | Swordlord Duelists | 5 | +9 | 16 | 18 | Elite | Aldori faction ≥ Revered |
| Faction (Surtova) | Brevoy Royal Guard | 6 | +6 | 18 | 14 | Infantry | Surtova faction ≥ Revered |
| Faction (Kellid) | Tiger Lord Defectors | 6 | +7 | 13 | 12 | Cavalry | Kellid faction ≥ Honored + A4-1 truce |
| Adventurer Board | Hired Adventurers | 4 | +8 | 14 | 10 | Elite | Post bounty via KM_AdventurerBoard.md |
| Kingdom Building | Trained Militia | 10 | +3 | 12 | 8 | Infantry | Barracks + Marshal "Train Militia" 3 turns |
| Companion Quest | Ekundayo's Rangers | 4 | +7 | 13 | 16 | Archers | Ekundayo quest complete + Devoted |

---

## ⚔️ SCRIPTED BATTLES

### Battle of the Tiger Lords (Ch4)
```
SETUP: 2 player armies vs Tiger Lord Warband + Raiders + Kellid Archers
TERRAIN: Open plains, river on left flank
SPECIAL: Armag's Elite arrives Round 3 as reinforcement
VICTORY: Destroy all enemy units or break Armag's Elite morale
DEFEAT: All player units routed
REWARD: Kellid faction +2, Stability +3, loot from camp
```

### Battle of Pitax Bridge (Ch5)
```
SETUP: Player armies vs Pitax Royal Guard + River Mercenaries + Cavalry
TERRAIN: River crossing, bridge chokepoint
SPECIAL: Only 1 army can cross bridge per round (funnel). Pitax War Mages fire from far bank.
VICTORY: Cross the bridge AND rout enemy forces
TACTICAL OPTION: Send scouts upstream to find ford (Survival DC 16) — flank attack
REWARD: Bridge secured, advance to Pitax capital
```

### Siege of the Capital (Ch5, if Pitax invades)
```
→ See KM_Sieges.md for full siege mechanics
ATTACKERS: Pitax Royal Guard + Cavalry + War Mages + Irovetti's Champions
DEFENDERS: Player armies + fortifications + militia
SPECIAL: Irovetti personally commands from rear. Assassination option (KM_AdvisorEvents.md A5-1)
```

### Battle of the Bloom (Ch6, Final Army Engagement)
```
SETUP: All remaining player armies vs Bloom Swarm + Fey Knights + Treant Guardians + Nyrissa's Thorns
TERRAIN: Corrupted forest, difficult terrain everywhere
SPECIAL: Fire-based armies deal +2 Off vs all Bloom units. Bloom Swarm regenerates unless fire.
VICTORY: Clear the path to Nyrissa's domain (player enters final dungeon personally)
DEFEAT: Kingdom overrun. Last stand at capital (siege rules apply)
REWARD: Path to final chapter dungeon opened
```

**Save block:** `"armies": [{"name": "Kingdom Militia", "strength": 8, "strength_max": 8, "offense": 4, "defense": 14, "morale": 10, "type": "infantry", "general": "marshal", "formation": "line"}]`

---

*KM_ArmyCombat.md — Kingmaker PF2e Text Adventure | Army Tactical Combat v2.0*
*Inspired by PF:KM crusade system and Shadowbane siege warfare.*
