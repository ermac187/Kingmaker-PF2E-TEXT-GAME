# KINGMAKER — WAR TABLE
## KM_WarTable.md | Active from: Chapter 4 | Referenced by: KM_Commands_P2.md

> **DM:** The War Table aggregates all military and strategic information into one display. Command: `.wartable`. Shows armies, deployments, active raids, fortifications, bounties, and standing orders in a single panel. This is a display tool — it does not create new mechanics, only centralizes existing ones.

---

## 📋 COMMAND

`.wartable` — Display the full strategic overview.

---

## 📊 WAR TABLE DISPLAY

```
══════════════════════════════════════════════════════════
WAR TABLE — Kingdom of {Name} | Turn {N}
══════════════════════════════════════════════════════════

ARMIES:
 {Army Name} | Str {N}/{max} | Off +{N} | Def {N} | Morale {N}
   Formation: {X} | General: {Name} | Location: Hex [{x,y}]
   Status: {Garrison/Deployed/In Combat/Recovering}

 {Army Name} | Str {N}/{max} | Off +{N} | Def {N} | Morale {N}
   Formation: {X} | General: {Name} | Location: Hex [{x,y}]
   Status: {Garrison/Deployed/In Combat/Recovering}

───────────────────────────────────────────────
FORTIFICATIONS:
 Hex [{x,y}]: {Type} | Garrison: {unit or "none"} | Status: {Intact/Damaged}
 Hex [{x,y}]: {Type} | Garrison: {unit or "none"} | Status: {Intact/Damaged}

───────────────────────────────────────────────
ACTIVE THREATS:
 {Raid/Conflict}: {Description} | Target: Hex [{x,y}] | Severity: {Low/Med/High}
 {Raid/Conflict}: {Description} | Target: Hex [{x,y}] | Severity: {Low/Med/High}

───────────────────────────────────────────────
STANDING ORDERS (Military):
 Marshal: {Order} | General: {Order} | Warden: {Order}

───────────────────────────────────────────────
ADVENTURER BOARD:
 Active bounties: {N} | Missions in progress: {N}
 Reports pending: {N}

───────────────────────────────────────────────
FACTION MILITARY STATUS:
 Aldori: {attitude} | Surtova: {attitude} | Pitax: {attitude}
 Available allies: {faction units available if Revered}

══════════════════════════════════════════════════════════
Type .armies, .forts, .board, or .orders for detail views.
══════════════════════════════════════════════════════════
```

---

## ⚠️ DM RULES

1. **Always current.** The war table reflects the CURRENT state, not the last time it was checked.
2. **Auto-display** at the start of any Kingdom Turn from Ch4 onward.
3. **No new mechanics.** This file only defines the display format. All mechanics live in KM_ArmyCombat.md, KM_BorderConflicts.md, KM_StandingOrders.md, KM_AdventurerBoard.md, and KM_Buildings.md.
4. **Mobile Base integration:** If the Mobile Base has the War Room upgrade, `.wartable` is available during travel.

---

## 📋 EXAMPLE WAR TABLE OUTPUTS BY CHAPTER

### Chapter 4 Example (Pre-Tiger Lord War)
```
══════════════════════════════════════════════════════════
WAR TABLE — Kingdom of Shrike's Rest | Turn 14
══════════════════════════════════════════════════════════

ARMIES:
 Kingdom Militia    | Str 8/8  | Off +4 | Def 14 | Morale 10
   Formation: Line | General: Marshal | Location: Capital | Status: Garrison
 Royal Guard        | Str 6/6  | Off +7 | Def 17 | Morale 16
   Formation: Line | General: —       | Location: Capital | Status: Garrison
 Frontier Scouts    | Str 5/5  | Off +5 | Def 13 | Morale 12
   Formation: —    | General: —       | Location: Eastern border | Status: Deployed

───────────────────────────────────────────────
FORTIFICATIONS:
 Hex [3,2]: Watchtower | Garrison: Scouts | Status: Intact
 Hex [5,1]: Palisade   | Garrison: none   | Status: Intact

───────────────────────────────────────────────
ACTIVE THREATS:
 Tiger Lord scouts | Severity: HIGH | Target: Eastern border
 Pitax infiltrators | Severity: MED  | Target: Capital (sabotage)

───────────────────────────────────────────────
STANDING ORDERS (Military):
 Marshal: Patrol Borders | General: War Games (turn 2/3) | Warden: Survey Hex [6,3]

───────────────────────────────────────────────
ADVENTURER BOARD:
 Active bounties: 2 | Missions in progress: 1 | Reports pending: 0

───────────────────────────────────────────────
FACTIONS:
 Aldori: Honored (+6) | Surtova: Neutral (+1) | Kellid: Unfriendly (-2) | Pitax: Hostile (-7)
══════════════════════════════════════════════════════════
```

### Chapter 5 Example (Active War with Pitax)
```
══════════════════════════════════════════════════════════
WAR TABLE — Kingdom of Shrike's Rest | Turn 22 | ⚔️ WAR FOOTING
══════════════════════════════════════════════════════════

ARMIES:
 Kingdom Militia    | Str 6/8  | Off +4 | Def 14 | Morale 8  | ⚠️ DAMAGED
   Formation: Shield Wall | General: Marshal | Location: Capital | Status: Garrison
 Royal Guard        | Str 6/6  | Off +7 | Def 17 | Morale 16
   Formation: Line | General: Legatus Regill | Location: Pitax Bridge | Status: Deployed
 Frontier Scouts    | Str 3/5  | Off +5 | Def 13 | Morale 10 | ⚠️ DAMAGED
   Formation: Skirmish | Location: Eastern flank | Status: Scouting
 Swordlord Duelists | Str 5/5  | Off +9 | Def 16 | Morale 18
   Formation: Line | Location: With Royal Guard | Status: Allied (Aldori)
 Mercenary Company  | Str 7/7  | Off +6 | Def 15 | Morale 10
   Formation: Line | Location: Western flank | Status: Hired (4 RP/turn)

───────────────────────────────────────────────
FORTIFICATIONS:
 Hex [3,2]: Watchtower | Status: DAMAGED (raid last turn)
 Hex [5,1]: Fort       | Garrison: Militia | Status: Intact
 Hex [4,3]: Palisade   | Status: Intact

───────────────────────────────────────────────
ACTIVE THREATS:
 Pitax Royal Guard     | Str 5/8  | Location: Pitax Bridge | ⚔️ ENGAGED
 River Mercenaries     | Str 4/7  | Location: Western approach | Advancing
 Pitax War Mages       | Str 4/4  | Location: Behind Pitax line | Ranged support
 Irovetti's Champions  | Str 5/5  | Location: Pitax Palace | Reserve

───────────────────────────────────────────────
SIEGE STATUS: None active — field battle in progress at Pitax Bridge

STANDING ORDERS: All suspended — WAR FOOTING (all resources to military)

ADVENTURER BOARD: Bounties suspended. 1 party (Ironwood Company) scouting enemy rear.

FACTIONS:
 Aldori: Revered (+8) ⚔️ ALLIED | Pitax: Hostile (-10) ⚔️ AT WAR
══════════════════════════════════════════════════════════
```

### Chapter 6 Example (Bloom Crisis)
```
══════════════════════════════════════════════════════════
WAR TABLE — Kingdom of Shrike's Rest | Turn 28 | 🌹 BLOOM CRISIS
══════════════════════════════════════════════════════════

ARMIES:
 Kingdom Militia    | Str 5/8  | Morale 6  | Status: Garrison (capital)
 Royal Guard        | Str 4/6  | Morale 12 | Status: Garrison (capital)
 Frontier Scouts    | Str 2/5  | Morale 8  | Status: ⚠️ RETREAT from eastern border

FORTIFICATIONS:
 Hex [3,2]: Watchtower | Status: OVERGROWN (Bloom consumed)
 Hex [5,1]: Fort       | Status: Intact — last eastern position
 Hex [4,3]: Palisade   | Status: OVERGROWN

ACTIVE THREATS:
 🌹 BLOOM — advancing 1 hex/turn from east and south
 Bloom Swarm    | Str 12 | Regenerating | 3 hexes from capital
 Nyrissa's Thorns | Str 8 | No morale  | 2 hexes from capital
 Fey Knights     | Str 6 | Teleporting | Inside kingdom borders

HEXES LOST TO BLOOM: 7 of 24 cleared hexes consumed
ESTIMATED TIME TO CAPITAL: 2-3 turns at current rate

STANDING ORDERS:
 Warden: Wildlife Management (animals fleeing Bloom — redirecting them)
 High Priest: Consecrate Land (slowing Bloom in 1 hex)
 Spymaster: Gathering intelligence on Nyrissa's domain entrance
══════════════════════════════════════════════════════════
```

---

*KM_WarTable.md — Kingmaker PF2e Text Adventure | War Table Display v2.0*
*Format + 3 example outputs (Ch4 buildup, Ch5 active war, Ch6 Bloom crisis).*
