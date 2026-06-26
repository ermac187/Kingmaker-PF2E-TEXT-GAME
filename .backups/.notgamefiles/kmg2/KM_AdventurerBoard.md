# KINGMAKER — ADVENTURER BOARD
## KM_AdventurerBoard.md | Active from: Adventurer's Guild built | Referenced by: KM_Buildings.md, KM_Kingdom.md

> **DM:** The Adventurer Board lets the player post bounties, hire NPC adventurer parties to handle kingdom problems, and receive mission reports. Requires the Adventurer's Guild building (KM_Buildings.md). This system lets the player delegate tasks they can't or won't handle personally.

---

## 📋 COMMAND

`.board` — Display the Adventurer Board: active bounties, available parties, and mission reports.

---

## 🏛️ BOARD OPERATIONS

### 1. POST A BOUNTY
Player pays RP to post a bounty on a specific problem. NPC adventurers may take it.

| Bounty Type | RP Cost | Time to Complete | Success Chance |
|-------------|---------|-----------------|----------------|
| **Clear a hex** (known enemies) | 4 RP | 1 kingdom turn | 70% + 5% per extra RP spent |
| **Escort a caravan** | 2 RP | Immediate (next trade event) | 85% |
| **Investigate a rumor** | 3 RP | 1 turn | 60% + 10% if Spymaster assists |
| **Retrieve a specific item** | 6 RP | 1-2 turns | 50% + 5% per extra RP |
| **Slay a named creature** | 8 RP | 2 turns | 40% base (dangerous missions) |

### 2. HIRE AN ADVENTURER PARTY
Available parties rotate each kingdom turn. Each has a quality tier affecting success rates.

| Party Tier | Hire Cost | Success Modifier | Availability |
|-----------|-----------|-----------------|-------------|
| **Green** (level 1-3) | 2 RP | −10% to base chance | Always available |
| **Seasoned** (level 4-6) | 5 RP | +0% (uses base chance) | 70% chance available |
| **Veteran** (level 7-9) | 10 RP | +15% | 40% chance available |
| **Elite** (level 10+) | 18 RP | +30% | 20% chance available |

### 3. RECEIVE MISSION REPORTS
When a mission completes, the DM delivers a report at the start of the next Kingdom Turn:

**Success report:**
```
[ADVENTURER BOARD — Mission Complete]
Bounty: {bounty description}
Party: {party name and tier}
Result: SUCCESS
Loot recovered: {items if any — rolled from hex loot table}
XP awarded to kingdom: {50 × party level}
Notes: {1-2 sentence narrative of how they handled it}
```

**Failure report:**
```
[ADVENTURER BOARD — Mission Failed]
Bounty: {bounty description}
Party: {party name and tier}
Result: FAILURE — {party defeated / retreated / disappeared}
Bounty refunded: 50% of posted RP
Notes: {What went wrong. Intel gained about the threat.}
Consequence: {Threat may escalate. Re-posting bounty costs +2 RP.}
```

---

## 🧑‍🤝‍🧑 SAMPLE NPC PARTIES (DM generates new ones each turn)

| Party Name | Tier | Composition | Personality |
|-----------|------|-------------|------------|
| The Copper Crows | Green | Fighter, Rogue, Cleric | Enthusiastic, inexperienced, cheap |
| Ironwood Company | Seasoned | Ranger, Druid, Fighter, Wizard | Professional, reliable, no-nonsense |
| The Red Requiem | Veteran | Champion, Magus, Oracle, Rogue | Expensive, effective, morally flexible |
| Stormbreak | Elite | Fighter/Marshal, Witch, Barbarian, Investigator, Summoner | The real deal. They negotiate terms. |

### Party Personality Effects
- **Enthusiastic/Green:** May over-report success. 10% chance they missed something in the cleared hex.
- **Professional:** Report accurately. No surprises.
- **Morally flexible:** 15% chance they kept the best loot item for themselves. Player can confront.
- **Negotiate terms:** Elite parties demand a share of recovered loot (50% of any magic items found).

---

## 📊 BOARD MANAGEMENT

| Rule | Detail |
|------|--------|
| Max active bounties | 3 (expandable to 5 with Guild upgrade: +6 RP) |
| Max parties hired simultaneously | 2 |
| Party loss | If a party is destroyed (crit failure), that tier becomes unavailable for 2 turns (recruitment drought) |
| Reputation link | Each successful bounty: +1 civilian reputation in nearest settlement |
| Failed bounty | Threat level in target hex increases by 1 (enemies are warned/prepared) |

---

## ⚠️ DM RULES

1. **Generate party names and personalities each turn.** Don't reuse names. These are transient NPCs.
2. **Roll success/failure honestly.** Show the math: "Success chance: 70% base + 15% veteran = 85%. Roll: d100 → 73. SUCCESS."
3. **Failure consequences are real.** A failed "slay named creature" means the creature is now alert and harder to approach.
4. **Player can accompany a party.** If the player joins, auto-success but they spend the time (travel + encounter takes 1-3 days). Converts to a normal encounter played out in full.
5. **The board is NOT a replacement for play.** If a bounty would involve a major story beat or quest objective, the board rejects it: "No party will take a contract this dangerous. This one's yours, Your Majesty."

---

## 📋 BOUNTY SCENARIOS (d12 table, roll per kingdom turn)

| d12 | Bounty | RP Cost | Difficulty | Target Hex |
|-----|--------|---------|-----------|------------|
| 1 | Wolf pack harassing farmstead | 2 | Green | Random settled hex |
| 2 | Bandit camp spotted by patrol | 4 | Seasoned | Random border hex |
| 3 | Missing merchant caravan | 3 | Green | Random road hex |
| 4 | Troll sighting near settlement | 6 | Veteran | Random forest hex |
| 5 | Ancient ruin discovered, needs clearing | 5 | Seasoned | Random unexplored hex |
| 6 | Haunted mine — workers refuse to enter | 4 | Seasoned | Random hill hex |
| 7 | Fey pranksters disrupting a village | 3 | Green | Random settled hex |
| 8 | Escaped prisoner from Pitax spotted | 6 | Veteran | Random border hex |
| 9 | Giant beast tracks near the capital | 8 | Elite | Capital-adjacent hex |
| 10 | Cult activity reported in the Narlmarches | 6 | Veteran | Narlmarches hex |
| 11 | Rival adventurer guild poaching in your territory | 4 | Seasoned | Random hex |
| 12 | Dragon sighting (young, territorial) | 10 | Elite | Random mountain hex |

### Expanded NPC Party Templates (d10 per availability check)

| d10 | Party Name | Tier | Composition | Personality | Quirk |
|-----|-----------|------|-------------|------------|-------|
| 1 | The Copper Crows | Green | Fighter, Rogue, Cleric | Enthusiastic beginners | Over-report success. 10% missed detail. |
| 2 | Mudfoot Company | Green | Ranger, Druid, Barbarian | Smell terrible, work cheap | Track anything. Refuse to enter cities. |
| 3 | Ironwood Company | Seasoned | Ranger, Druid, Fighter, Wizard | Professional, reliable | Write formal reports. Expect formal payment. |
| 4 | The Lantern Bearers | Seasoned | Cleric, Paladin, Rogue, Bard | Religious. Efficient. Judgmental. | Refuse bounties involving undead allies. |
| 5 | Shrike River Runners | Seasoned | Rogue ×2, Ranger, Bard | Fast, flexible, morally gray | 15% kept best loot. Confrontable. |
| 6 | The Red Requiem | Veteran | Champion, Magus, Oracle, Rogue | Expensive, effective, dramatic | Demand an audience with the ruler post-mission. |
| 7 | Blackwater Solutions | Veteran | Fighter, Alchemist, Investigator, Ranger | Cold professionals | No personality. Perfect reports. Unsettling. |
| 8 | Thornwall Irregulars | Veteran | Barbarian, Druid, Monk, Sorcerer | Chaotic but devastating | 20% cause collateral damage. Always succeed. |
| 9 | Stormbreak | Elite | Fighter/Marshal, Witch, Barbarian, Investigator, Summoner | Negotiate terms. Demand respect. | Want 50% of magic items. Worth it. |
| 10 | The Last Company | Elite | Champion, Wizard, Rogue, Cleric, Fighter | Retired legends. One last job. | Automatically succeed on first mission. Disband after. |

### Failure Consequence Chains

When a bounty fails, the threat doesn't just persist — it escalates:

| Original Bounty | Failure → Escalation | Second Failure → Crisis |
|----------------|---------------------|----------------------|
| Wolf pack | Pack grows. +2 wolves. Attacks livestock. Economy −1. | Alpha wolf appears. Named beast. Personal hunt required. |
| Bandit camp | Bandits recruit. Raid fires next turn. Border −1. | Bandit leader emerges. Named NPC. Army engagement. |
| Troll sighting | Troll claims hex. Fortification damaged. | Troll nest established. 3 trolls. Fire required. |
| Ancient ruin | Undead emerge from ruin. Random encounter +1 in area. | Ruin becomes a dungeon (KM_DungeonPuzzles.md). |
| Dragon sighting | Dragon attacks a caravan. Economy −2. | Dragon nests. Permanent threat until slain. Personal combat or elite party. |

**Save block:** `"adventurer_board": { "posted_bounties": [], "active_missions": [], "completed_reports": [], "guild_upgraded": false, "failure_escalations": [] }`

---

*KM_AdventurerBoard.md — Kingmaker PF2e Text Adventure | Adventurer Board v2.0*
*Bounty table + 10 party templates + failure escalation chains.*
