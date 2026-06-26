# KINGMAKER — TERRITORIAL RAIDS & BORDER CONFLICTS
## KM_BorderConflicts.md | Active from: Chapter 2 | Referenced by: KM_Kingdom.md, KM_StandingOrders.md

> **DM:** Between-chapter events where rival factions probe the kingdom's borders with raids. These fire automatically based on kingdom turn events and faction hostility. Resolution depends on garrison strength, fortifications (KM_Buildings.md), and standing orders (KM_StandingOrders.md). The player can delegate defense or handle raids personally.

---

## 📊 RAID GENERATION

### When Raids Fire
- **Every 2-3 kingdom turns** starting Chapter 2 (roll d6: raid fires on 5-6)
- **Automatic** if any faction is at Hostile (−6 or below) in KM_Reputation.md
- **Story-scripted** raids during specific chapter events (Troll Trouble, Pitax War)
- **Random** border encounters when no hex fortifications protect a border hex

### Raid Sources by Chapter

| Chapter | Primary Raider | Secondary Raider | Raid Level Range |
|---------|---------------|-----------------|-----------------|
| Ch2 | Bandit remnants | Kobold/Mite raiders | 2-4 |
| Ch3 | Trolls | Tiger Lord scouts | 4-7 |
| Ch4 | Tiger Lord warbands | Pitax infiltrators | 7-10 |
| Ch5 | Pitax army units | Mercenary companies | 10-14 |
| Ch6 | Nyrissa's fey | Bloom creatures | 12-16 |

---

## ⚔️ RAID RESOLUTION

### Automated Resolution (player delegates)
Used when player assigns standing orders to handle raids or has garrison forces in the target hex.

```
Raid Strength: d20 + Raid Level
Defense Strength: Garrison Offense + Fortification Bonus + Standing Order Bonus

Defense > Raid     = REPELLED. No damage. +1 Stability. Raider faction −1.
Defense = Raid     = STALEMATE. Fortification takes 1 damage tier. Garrison holds.
Defense < Raid     = BREACH. Settlement/hex takes damage:
                     - Unfortified hex: random building destroyed (if settlement)
                     - Fortified hex: fortification reduced 1 tier
                     - Unrest +1. Reputation −1 in nearest settlement.
Defense < Raid −5  = OVERRUN. Garrison routed. Hex control lost until reclaimed.
                     Unrest +2. Reputation −2.
```

### Bonuses to Defense

| Source | Bonus |
|--------|-------|
| Watchtower in hex or adjacent | +2 (early warning) |
| Palisade in hex | +1 AC bonus to garrison |
| Fort in hex | +4 AC, supplies for extended defense |
| Trapped Approach | Raid takes 2d6 damage before engagement |
| Marshal "Patrol Borders" order | +2 to detect, +1 to defense |
| General "Fortify Position" order | +1 defense per turn active |
| Army unit garrisoned | Add army's Offense to defense |

### Personal Resolution (player handles it)
If the player chooses to ride out and meet the raid:
- **Travel time:** Based on hex distance. Early warning from Watchtower = 1 extra day to prepare.
- **Encounter:** Standard combat encounter at Raid Level. DM runs from Bestiary + chapter raider stat blocks.
- **Victory:** +1 Stability, +1 Reputation in nearest settlement. Loot from defeated raiders. XP as normal encounter.
- **Retreat:** Raid succeeds as automated BREACH result.

---

## 📋 RAID EVENT FORMAT

```
[BORDER CONFLICT — {Raid Name}]
RAIDER: {Faction} — {Unit type} — Strength {Raid Level + d20 result}
TARGET: Hex [{x,y}] — {Settlement name or "wilderness hex"}
DEFENSE: {Garrison + Fortification + Orders = total}

RESULT: {REPELLED / STALEMATE / BREACH / OVERRUN}
DAMAGE: {What was lost}
RESPONSE OPTIONS:
 1. Accept result — move on
 2. Send army to pursue  [costs 1 army action]
 3. Ride out personally  [travel + combat encounter]
 4. Post bounty on Adventurer Board  [KM_AdventurerBoard.md]
```

---

## 🗺️ BORDER VULNERABILITY

### Unprotected Borders
A border hex with no fortification AND no patrol order is "exposed." Exposed hexes:
- Raid success chance +20%
- No early warning (player learns about raid AFTER damage)
- If 3+ border hexes are exposed simultaneously: +1 Unrest per turn ("the borders are undefended")

### Border Hardening
Placing 1 fortification every 3 border hexes covers the gap:
- **Chain rule:** A Watchtower covers its hex + 2 adjacent hexes for detection
- **Fort rule:** A Fort covers its hex only but at maximum defense
- **Optimal coverage:** Alternating Watchtowers and Forts along the border

---

## 📊 ESCALATION

If raids go unanswered for 3+ consecutive turns:
1. **Turn 1-2:** Raids are probing. Low strength. Easy to repel.
2. **Turn 3:** Raider faction commits more forces. Raid Level +2.
3. **Turn 4+:** Full incursion. Multiple hexes attacked simultaneously. Army response required.
4. **Turn 6+:** If still unanswered, raider faction claims the hex permanently. Kingdom Size −1.

### De-escalation
- Repel 3 consecutive raids: raider faction backs off for 4 turns
- Destroy raider source (clear the enemy camp/stronghold): raids from that source stop permanently
- Diplomatic solution: use faction reputation to negotiate cease-fire (requires Friendly or better)

---

## ⚠️ DM RULES

1. **Raids should feel like pressure, not punishment.** A well-fortified kingdom handles most raids automatically. The system rewards preparation.
2. **Roll honestly.** Show the raid strength roll and defense calculation. The player should see why they won or lost.
3. **Personal combat raids are OPTIONAL.** The player can always delegate. Never force them to ride out.
4. **Narrative flavor:** Describe the raid briefly even when automated. "Tiger Lord riders tested your eastern watchtower at dawn. The garrison held. They left two dead and retreated into the Kamelands."
5. **Scale with kingdom size.** A large kingdom (Size 20+) faces raids more frequently but has more resources. Small kingdoms face fewer but have less defense.

---

## 🏴 NAMED RAIDER LEADERS

Each chapter's raiders have named leaders. If the leader is captured or killed, raids from that source stop for 2 chapters. If the leader escapes, raids escalate faster.

### Chapter 2 Raiders

**Kressle's Remnants** — Bandit Captain Drelev's Cousin
- If Kressle survived Ch1: she leads the remnants. Raid Level +1 (she knows the terrain).
- If Kressle was killed: a nameless lieutenant leads. Generic stats. Easier to break.
- **Capture reward:** Intel on remaining Stag Lord caches (1d4 × 50 gp loot). Reputation +1.

**Sootscale Renegades** — Chief Mikmek the Bitter (if kobold alliance failed)
- Only fires if `sootscale_alliance = FALSE`.
- Raid style: underground sabotage (mine collapses, road sinkholes). Not direct combat.
- **Resolution:** Negotiate (Diplomacy DC 14) or smoke them out (Athletics DC 16 + 2 days).

### Chapter 3 Raiders

**Troll Marauders** — Hargulka's Lieutenant
- Trolls hit farming hexes. Burn crops. Food commodity: −1 per unanswered raid.
- **Special:** Fire required. Non-fire garrison bonus halved.
- **Capture:** Interrogation reveals Hargulka's camp location (if not yet found).

**Kellid Scouts** — Dugath the Quiet
- Not hostile by default. Testing borders. If kingdom has Kellid faction ≥ Friendly: scouts report to you instead.
- If faction < Neutral: raids escalate to livestock theft (Economy −1/turn).
- **Personal encounter:** Player can meet Dugath at the border (Scripted Interaction). Diplomacy DC 16: alliance option.

### Chapter 4 Raiders

**Tiger Lord Vanguard** — War Chief Zorek
- Professional military raiders. Raid Level 8-10. Target fortified hexes specifically.
- **Strategy:** Zorek tests defenses, reports to Armag. Captured: full Tiger Lord army intelligence.
- **Combat:** If player intercepts personally — War Chief Zorek (Barbarian 8, HP 95, AC 20). Named NPC fight.

**Pitax Infiltrators** — The Masked Agent
- Not military raids — sabotage. Poison wells, burn barns, plant evidence of disloyalty.
- Detection: Spymaster "Counter-Espionage" order. Otherwise: effects appear as random bad luck.
- **Unmasking:** Perception DC 18 at the site of sabotage, or Spymaster investigation (2 turns).

### Chapter 5 Raiders

**Pitax Forward Units** — Captain Stefano
- Full military raids. Raid Level 10-14. Multiple simultaneous hexes.
- **Special:** War footing. These are not probes — this is the invasion's opening move.
- **If captured:** Stefano negotiates. Offers Pitax troop positions in exchange for release. Information is 80% accurate (20% deliberate misdirection).

### Chapter 6 Raiders

**Bloom Incursions** — No leader (the Bloom itself)
- Not intelligent raids. The Bloom spreads into border hexes like infection.
- **Defense:** Nature-based (druids, Warden standing order, fire). Military garrison: half effectiveness.
- **Escalation:** Unlike other raids, Bloom incursions never stop escalating until the source is destroyed.
- **Cleansing:** Cleared hexes require 1 turn + Nature DC 18 or divine cleansing to restore.

---

## 📊 RAID EVENT TABLE (d8 per chapter)

| d8 | Ch2 Raid | Ch3 Raid | Ch4 Raid | Ch5 Raid | Ch6 Raid |
|----|----------|----------|----------|----------|----------|
| 1-2 | Kressle's Remnants | Troll Marauders | Tiger Lord Vanguard | Pitax Forward Units | Bloom Incursion (1 hex) |
| 3-4 | Sootscale Renegades | Kellid Scouts | Pitax Infiltrators | Pitax Forward Units | Bloom Incursion (2 hexes) |
| 5-6 | Kressle's Remnants | Troll Marauders | Tiger Lord Vanguard | Mercenary Raid (hired by Pitax) | Fey Border Test |
| 7 | No raid this turn | Kellid Scouts | Both Tiger + Pitax | Coordinated 3-hex assault | Bloom Incursion (3 hexes) |
| 8 | No raid this turn | No raid this turn | No raid this turn | No raid this turn | No raid — calm before final battle |

**Save block:** `"border_raids": { "pending": [], "resolved": [], "consecutive_unanswered": 0, "last_raid_turn": 0, "named_leaders_captured": [], "named_leaders_killed": [] }`

---

*KM_BorderConflicts.md — Kingmaker PF2e Text Adventure | Territorial Raids & Border Conflicts v2.0*
*Named raiders, per-chapter tables. Inspired by Shadowbane territorial warfare.*
