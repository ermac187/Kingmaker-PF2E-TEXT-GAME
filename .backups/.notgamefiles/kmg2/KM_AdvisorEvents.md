# KINGMAKER — ADVISOR EVENTS & POLITICAL INTRIGUE
## KM_AdvisorEvents.md | Active from: Chapter 2 | Referenced by: KM_Kingdom.md

> **DM:** Load during Kingdom Turns. Each kingdom event now has 2–3 advisor-championed solutions. The player hears each advisor's pitch, then chooses. Choosing an advisor's solution: +1 relationship with that advisor, variable kingdom stat outcomes. Advisors with conflicting interests may sabotage each other's projects (Intrigue system, bottom of file). Use the Debate system (KM_Debates.md) if the player wants advisors to argue it out.

---

## 📋 ADVISOR EVENT FORMAT

```
[KINGDOM EVENT — {Event Name}]
{Description of the problem}

ADVISOR SOLUTIONS:
 A. {Advisor Name} ({Role}): "{Their pitch in 1-2 sentences}"
    → Effect: {Kingdom stat changes}
    → Cost: {RP or resource cost}
    → Risk: {What could go wrong}

 B. {Advisor Name} ({Role}): "{Their pitch}"
    → Effect: {Stats}
    → Cost: {Cost}
    → Risk: {Risk}

 C. Player's own solution (describe)
    → DM adjudicates based on skills and resources

Choose A, B, or C. Or use .debate to have the advisors argue.
```

---

## 🏛️ ADVISOR EVENTS — CHAPTER 2

### Event A2-1: The Bandit Resurgence
*Stag Lord loyalists regroup in the Narlmarches. Scouts report a new camp.*

**Councilor:** *"Amnesty. Offer pardons for any who lay down arms before the next moon. Most of these people are desperate farmers, not soldiers."*
→ Loyalty +2, Stability −1. 60% of bandits accept. Remainder hardens.

**General:** *"Send the army. Crush the camp before they organize. Every day we wait, they recruit."*
→ Stability +2, Loyalty −1. Camp destroyed. 1d4 prisoners for interrogation. RP cost: 4.

**Marshal:** *"Blockade. Cut their supply lines. They starve out in two turns without a fight."*
→ Economy −1 (trade disruption), Stability +1. Slow but bloodless. Bandits scatter.

---

### Event A2-2: The Trade Road Dispute
*Two merchant guilds claim exclusive rights to the kingdom's main trade road.*

**Treasurer:** *"Grant the contract to the Restov guild. They pay more and we need the revenue."*
→ Economy +3. Restov faction +1. Local merchants: Reputation −1.

**Councilor:** *"Split the road. Half to each guild. Nobody wins everything, nobody loses everything."*
→ Economy +1, Loyalty +1. Both guilds mildly annoyed. Stable compromise.

**Grand Diplomat:** *"Use this as leverage. Neither guild gets exclusivity — we open the road to all comers and take a crown toll."*
→ Economy +2, Stability +1. Both guilds: faction −1. Commoners: Reputation +1 (lower prices).

---

### Event A2-3: The Temple Petition
*A religious order requests land and tax exemption to build a temple in the capital.*

**High Priest:** *"Grant it. Divine favor brings pilgrims, tithes, and healers. The kingdom needs all three."*
→ Culture +2, Stability +1. Free Temple building (saves 8 RP). High Priest: +1 relationship.

**Treasurer:** *"Tax exemption for a building that generates income? Absolutely not. They can build, but they pay like everyone else."*
→ Economy +1. Clergy faction −1. Commoners neutral.

**Spymaster:** *"Let them build. But I want an observer inside. Religious orders collect secrets along with tithes."*
→ Culture +1, Stability +1. Spymaster network: +1 agent. Clergy faction −1 if discovered (25% chance per turn).

---

### Event A2-4: The Hex Dispute
*Two settlements both claim the same cleared hex for farmland expansion.*

**Councilor:** *"The hamlet that cleared it gets priority. First labor, first claim."*
→ Loyalty +1 in winning hamlet. Loyalty −1 in losing hamlet.

**Warden:** *"Neither. That hex is strategically important — build a fortification, not farms."*
→ Stability +2. Both hamlets: Loyalty −1. Hex becomes eligible for fortification (KM_Buildings.md).

**Ruler (player):** Can propose a third option. DM adjudicates with appropriate skill check.

---

## 🏛️ ADVISOR EVENTS — CHAPTER 3

### Event A3-1: The Troll Refugees
*Troll Trouble aftermath: displaced trolls seek territory in your borderlands.*

**General:** *"Trolls don't negotiate. Patrol the borders. Kill any that cross."*
→ Stability +2. Kellid faction +1. Culture −1 (brutal reputation). RP cost: 2/turn (patrols).

**Grand Diplomat:** *"Designate a wilderness hex as troll territory. Formal border. They stay out, we stay out."*
→ Stability +1, Loyalty +1. Kellid faction −1 ("You gave land to trolls?"). Saves RP long-term.

**High Priest:** *"The trolls are creatures of the wild. The druids can mediate. Let Jhod try."*
→ Culture +2 if Jhod succeeds (70%). Stability −1 if he fails (30%). No RP cost.

---

### Event A3-2: The Festival Question
*The capital is large enough for an annual festival. What kind?*

**Councilor:** *"A harvest festival. Food, drink, games. The people need joy."*
→ Loyalty +3, Culture +1, Economy −2 (festival costs). Reputation +1 in capital.

**Treasurer:** *"A trade fair. Invite merchants from Restov and the River Kingdoms."*
→ Economy +4, Culture +1. Faction +1 with trade partners. Loyalty +0 (merchants aren't fun).

**Magister:** *"An arcane symposium. Attract scholars and mages. The kingdom needs intellectual depth."*
→ Culture +3, Economy +1. Scholarly NPCs arrive (side quests). Commoners confused (Loyalty +0).

---

### Event A3-3: The Spy Report
*Spymaster reports Pitax has agents in the capital. Three suspects identified.*

**Spymaster:** *"Let me handle this quietly. Arrests, interrogation, expulsion. Nobody needs to know."*
→ Stability +2. Pitax faction −1. 100% success but −1 Loyalty if methods leak (20% chance).

**Marshal:** *"Public arrests. Show everyone that spies face justice."*
→ Loyalty +2 (deterrence), Stability +1. Pitax faction −2 (humiliated). Agents may warn others (50% of remaining network escapes).

**Grand Diplomat:** *"Turn them. Feed false information back to Pitax. A spy you know about is an asset."*
→ Stability +1. Pitax faction unchanged. Long-term: +2 to next Pitax-related intelligence check. 30% chance the double-agent is a triple-agent.

---

### Event A3-4: The Dwarven Miners
*A dwarven mining company offers to set up operations in a resource-rich hex — but they want autonomy.*

**Treasurer:** *"Their operation will triple our ore output. Give them the hex. We tax the output, not the process."*
→ Economy +3, Ore +2/turn. Dwarven faction +1. Loyalty −1 (citizens see foreign control over domestic land).

**Warden:** *"Our miners, our hex, our rules. Offer them contracts, not territory."*
→ Economy +1, Ore +1/turn. Loyalty +1. Dwarven faction −1 (insulted). Slower but sovereign.

**Councilor:** *"Joint venture. They run the mine, we staff it with our people. Both sides learn."*
→ Economy +2, Ore +1/turn, Culture +1. Dwarven faction +0 (acceptable). Build time: 2 turns.

---

### Event A3-5: The River Toll
*A bridge connecting two settlements needs repair. Who pays — the settlements or the crown?*

**Treasurer:** *"Toll bridge. Users pay for repairs. Self-sustaining infrastructure."*
→ Economy +2. Loyalty −1 in both settlements. Trade volume: −10% on that route.

**Councilor:** *"Crown pays. It's our bridge, our kingdom, our responsibility."*
→ Loyalty +2 in both settlements. Economy −2 (repair costs). Reputation +1.

**Marshal:** *"Military priority. Repair it, fortify it, and station guards. Bridges are chokepoints."*
→ Stability +2. Economy −1. Bridge becomes defensible position (KM_BorderConflicts.md bonus).

---

## 🏛️ ADVISOR EVENTS — CHAPTER 4

### Event A4-1: The Barbarian Alliance
*Tiger Lord scouts approach under flag of truce. They offer non-aggression — for a price.*

**General:** *"It's a trap. The Tiger Lords don't negotiate — they stall while they recruit. Reject and reinforce."*
→ Stability +2. Kellid faction −2. Tiger Lords attack 1 turn sooner. Army preparation: +1 Morale.

**Grand Diplomat:** *"Accept the truce. Buy time. We're not ready for a two-front war."*
→ Stability +1, Economy +1 (no war spending). Kellid faction +1. Tiger Lords delay attack 2 turns. Risk: they use the time too.

**Spymaster:** *"Accept publicly. Use the truce to infiltrate their camp. When the truce breaks, we know their numbers."*
→ Stability +1. Spymaster network: full Tiger Lord army intelligence. 20% chance they detect the spy (truce breaks immediately, faction −3).

---

### Event A4-2: The Refugee Wave
*War with the Tiger Lords displaces hundreds of Kellid civilians. They arrive at your borders.*

**Councilor:** *"Open the gates. These are people, not threats. Feed them, house them, make them citizens."*
→ Loyalty +3, Culture +1. Economy −3 (feeding costs). Population +500. Some refugees have useful skills (1 free building worker).

**Marshal:** *"Screen them first. Tiger Lord spies will be mixed in. Process, then admit."*
→ Stability +2, Loyalty +1. Economy −1 (processing costs). Spymaster detects 1d4 embedded spies.

**Treasurer:** *"We can't afford this. Redirect them to Restov. Brevoy has resources we don't."*
→ Economy stable. Loyalty −2 (cold). Kellid faction −2. Reputation −1. Restov faction +1 (they appreciate the warning).

---

### Event A4-3: The War Profiteers
*Arms dealers offer bulk weapon sales at inflated prices. Your army needs equipment.*

**Treasurer:** *"Haggle. We buy half now at their price, half later at ours, or we commission locally."*
→ Army gets half equipment now. Economy −2. Local smiths begin production (full equipment in 2 turns).

**General:** *"Pay the price. Men die while we negotiate. Equipment now saves lives."*
→ Army fully equipped. Economy −4. Morale +2. General: +1 relationship.

**Magister:** *"Let me examine their stock. I suspect some of these weapons are enchanted — badly. Cursed, even."*
→ Arcana DC 16 check. Success: 30% of stock is cursed — saved the army. Failure: bought cursed weapons, 1 army unit takes −1 Morale.

---

### Event A4-4: The Coronation Debate
*Jamandi and Natala Surtova pressure you to formalize your political alignment before the war.*

**Grand Diplomat:** *"Delay. Neither side gets a commitment until the war is won. We need both."*
→ Both factions: −1. Independence maintained. No alliance bonus but no obligation.

**Councilor:** *"The people should choose. Hold a public declaration ceremony. Let the kingdom decide its identity."*
→ Loyalty +3, Culture +2. Player chooses alignment publicly — all consequences transparent. +1 Blunt disposition.

**Spymaster:** *"Promise both. Privately. When the war ends, we choose the winner."*
→ Both factions: +1 (temporarily). Stability +1. Risk: if discovered (30% per chapter), both factions −3. +1 Cunning disposition.

---

## 🏛️ ADVISOR EVENTS — CHAPTER 5

### Event A5-1: The Pitax Ultimatum
*Irovetti sends a formal demand: surrender the Stolen Lands or face invasion.*

**General:** *"This is not a negotiation. This is a declaration. Mobilize everything."*
→ All armies activated. Stability +2. Economy −3 (war footing). War begins formally.

**Grand Diplomat:** *"Respond with a counter-proposal. We don't want war — but we don't bend either."*
→ Delay Pitax invasion by 1 turn. Diplomacy DC 20. Success: Pitax faction +1, delay 2 turns. Failure: Irovetti insulted, invasion accelerated.

**Spymaster:** *"Ignore the letter. Send assassins. Cut the head off the snake."*
→ Assassination attempt: 40% success. Success: Pitax army in disarray (−3 Morale all units, invasion delayed 3 turns). Failure: Spymaster agent captured, Pitax propaganda victory (Reputation −2).

---

### Event A5-2: The Supply Chain
*War stretches supply lines. Settlements closest to the front are running low.*

**Treasurer:** *"Ration distribution. Central control. Nobody starves, but nobody feasts."*
→ Economy stable. Loyalty −1 (rationing is unpopular). Stability +1. Food commodity: −2/turn but controlled.

**Warden:** *"Local foraging. My rangers can supplement supplies from the wilderness."*
→ Warden Survival DC 16. Success: Food +2/turn, no cost. Failure: rangers encounter enemy scouts, 1d4 casualties.

**Councilor:** *"Ask the people. Volunteer kitchens, community sharing. Make it a cause, not a burden."*
→ Loyalty +2 (community spirit). Food −1/turn (less efficient). Reputation +1. Morale +1 (everyone contributes).

---

### Event A5-3: The Mercenary Company
*A mercenary company offers their services. Professional, expensive, morally flexible.*

**General:** *"Hire them. Our army is stretched thin. Professional soldiers fill the gap."*
→ +1 army unit (Mercenary Company: Off +6, Def 15, Morale 10). Cost: 6 RP/turn. Mercenaries fight well but may loot settlements if unpaid.

**Treasurer:** *"Too expensive. That gold builds fortifications that last longer than hired swords."*
→ No mercenaries. 6 RP invested in fortifications instead: +1 to all hex defense bonuses.

**Marshal:** *"Hire them but assign them to the front line. If they prove loyal, integrate. If not, they absorb the first casualties."*
→ Mercenaries hired at 4 RP/turn (front-line discount). If first battle goes well: Mercenary Morale +2 (they respect competence). If badly: they desert.

---

### Event A5-4: The Siege Preparation
*Intelligence says Pitax will siege the capital within 2 turns.*

**General:** *"Defensive positions. Every building is a strongpoint. Every citizen who can hold a spear gets one."*
→ Capital defense: +4. Militia mobilized (1 temporary army unit, weak but present). Culture −1 (militarization).

**Magister:** *"I can ward the walls. Arcane defenses — detection, shields, counterspells at the gates."*
→ Capital defense: +2 vs magical attacks. Enemy casters: −2 to spell DCs within walls. Cost: 4 RP + Magister unavailable for 1 turn.

**Spymaster:** *"Let me evacuate the non-combatants. If they siege, I want civilians out of the crossfire."*
→ Civilians evacuated. If siege occurs: no civilian casualties. Loyalty +2 (they remember). Economy −1 (disruption). If siege doesn't occur: wasted effort but goodwill earned.

---

## 🏛️ ADVISOR EVENTS — CHAPTER 6

### Event A6-1: The Bloom Ultimatum
*Nyrissa's Bloom is consuming hexes. Three settlements are in its path.*

**Warden:** *"We can't fight the Bloom with swords. Druids and nature magic. Slow it down, buy time."*
→ Bloom advance: −1 hex per turn (slowed). Warden and druids committed for 2 turns. Nature DC 18 per turn to maintain.

**General:** *"Evacuate the settlements. Save the people. We can rebuild later."*
→ Settlements abandoned. Population relocated (Loyalty +1 — people saved). Economy −2 (lost infrastructure). 3 hexes lost to Bloom.

**High Priest:** *"The Bloom is fey corruption. Divine cleansing — coordinated prayer, holy ground, consecration."*
→ Culture +2 if Bloom is slowed. 50% chance per hex of full cleansing. Failure: Bloom accelerates in that hex (+1 hex consumed). Clergy committed for 3 turns.

---

### Event A6-2: The Final Alliance
*Before the final confrontation, choose who stands with you.*

**Grand Diplomat:** *"Call in every favor. Every faction we've helped. This is what alliances are for."*
→ Every faction at Honored+ sends 1 army unit. Total allies = number of factions at Honored or above.

**General:** *"Our army alone. Allies complicate command structure. We trained for this."*
→ Player armies only. +2 Morale (unity). +1 Offense (no coordination overhead). Fewer total troops.

**Councilor:** *"The people themselves. Arm the citizens. Everyone fights."*
→ Militia army units from every settlement (weak: Off +2, Def 12, Morale 8). Many units but fragile. Loyalty +3 (the kingdom fights as one).

---

### Event A6-3: The Nyrissa Question
*If nyrissa_backstory_known ≥ 2, advisors debate what to do about Nyrissa herself.*

**High Priest:** *"She is the source. Destroy her. End the Bloom at its root."*
→ Standard final battle path. Nyrissa destroyed. Bloom ends.

**Grand Diplomat:** *"She was cursed, not born evil. If there's a way to save her, we should try."*
→ True Ending path remains open. +1 Merciful disposition. Requires: nyrissa_saveable flags to complete.

**Spymaster:** *"Neither destroy nor save. Bind her. Use the Bloom as a weapon against our enemies, then contain it."*
→ Dark path. Bloom becomes a kingdom weapon for 1 chapter. Economy +5, Stability −3. Nyrissa: permanently hostile. Lantern King: amused (not good). Unique dark ending flag set.

---

## 🗡️ ADVISOR INTRIGUE SYSTEM

> **DM:** Advisors with opposing goals occasionally sabotage each other's projects. This runs in the background. The player notices when a project underperforms. The Spymaster can detect intrigue. Detecting and confronting an intriguing advisor is a choice point.

### Intrigue Trigger
- **Two advisors with opposing priorities** on a recently resolved event
- The LOSING advisor has a 25% chance per turn to sabotage the WINNING advisor's project
- Sabotage: the winning solution's positive effect is halved for 1 turn

### Intrigue Pairs (most common)
| Pair | Conflict Axis |
|------|--------------|
| Treasurer vs Councilor | Economy vs Loyalty |
| General vs Grand Diplomat | Force vs Diplomacy |
| High Priest vs Spymaster | Transparency vs Secrecy |
| Marshal vs Treasurer | Security spending vs Revenue |

### Detection
- **Spymaster detects intrigue** automatically if assigned "Monitor Advisors" standing order (KM_StandingOrders.md)
- **Without Spymaster monitoring:** Player must notice stat underperformance and investigate (Perception DC 16 or Society DC 14)

### Confrontation
When detected, player has 3 options:
1. **Warn** — Advisor stops sabotage for 2 chapters. No relationship penalty. May resume.
2. **Reprimand publicly** — Advisor stops permanently. −2 relationship with that advisor. +1 Stability (order restored).
3. **Use the Debate system** — Force the two advisors to argue it out (KM_Debates.md). Loser accepts result. No sabotage, no relationship loss.

**Save block:** `"advisor_intrigue": { "active": [], "detected": [], "resolved": [] }`

---

*KM_AdvisorEvents.md — Kingmaker PF2e Text Adventure | Advisor Events & Political Intrigue v1.0*
*Features #17 (Advisor Disagreements) and #26 (Advisor Intrigue) combined.*
*Inspired by Pathfinder: Kingmaker CRPG advisor system and Shadowbane guild politics.*
