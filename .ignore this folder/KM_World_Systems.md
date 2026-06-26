# KINGMAKER — World Systems (CONSOLIDATED)
## KM_World_Systems.md | v1.0 (2026-05-22): Merged from related system files. Single source of truth.

> **DM:** Database file. Search by topic.



---

<!-- merged from KM_World_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — REPUTATION & NOTORIETY SYSTEM: THE PEOPLE'S VERDICT
## KM_World_Systems.md | Active from: Pre-Prologue onward (civilians react throughout the ENTIRE game) | Referenced by: KM_Kingdom.md, KM_Exploration.md, KM_Commands.md
### Load whenever civilians are present — the player enters a settlement, passes people on a road, sits in a tavern, OR takes any notable action civilians can witness. Witnesses talk to each other afterward; that talk forms reputation. This is ALWAYS on — NOT a Chapter-1-gated system.

> **DM:** This system tracks civilian perception of the player. It uses the `public_reputation` integer (−100 to +100) from KM_P2.txt as its source score. The stages below map to that score. **KM_P2.txt owns the score integer, the deed log/JSON, deed spread, gift tables, and named witnesses.** ⛔ **THIS FILE IS THE CANONICAL REPUTATION LADDER (resolved 2026-06-22): the 11-stage scale (−5 REVILED … +5 BELOVED) below is authoritative for the tier NAMES, the band CUTOFFS, the SCORE-CHANGE MAGNITUDES (§ REPUTATION SCORE CHANGE TRIGGERS), and the civilian REACTIONS.** The HUD "Stage" reads from here. KM_P2.txt's old 9-band ladder (LEGENDARY HERO / KNOWN FAVORABLY / …) is SUPERSEDED — do not use it for tier labels, and do not invent a third scheme.
>
> **What this system governs:** Anonymous reactions from unnamed civilians. Shopkeepers, tavern patrons, road workers, farmers, city guards who don't know the player personally, travelers, refugees. Basically: everyone who isn't on a named NPC card.
>
> **What this system does NOT govern:** Named NPC relationships (use individual NPC scores). Faction standing (use faction tables in KM_Kingdom.md). Army morale (separate track).

---

## 👁️ REPUTATION SCALE — THE PEOPLE'S VERDICT

```
Stage +5 — BELOVED      : public_reputation  +51 to +100   (legendary — full gift tables; civilians are protagonists)
Stage +4 — RESPECTED    : public_reputation  +26 to +50    (discounts, proactive help, volunteered intel)
Stage +3 — KNOWN        : public_reputation  +13 to +25    (real warmth; small gifts begin)
Stage +2 — FAVORABLE    : public_reputation   +6 to +12    (friendly recognition, good service)
Stage +1 — NOTICED      : public_reputation   +2 to +5     (a few heads turn; "heard the name")
Stage  0 — UNKNOWN      : public_reputation   −1 to +1     (baseline — PF2e Indifferent)
Stage −1 — CAUTIOUS     : public_reputation   −2 to −5     (cool, clipped, watched)
Stage −2 — WARY         : public_reputation   −6 to −12    (room quiets, prices creep, kids called close)
Stage −3 — FEARED       : public_reputation  −13 to −25    (shutters close, "we're closed," guards consult)
Stage −4 — NOTORIOUS    : public_reputation  −26 to −50    (many won't serve; doors lock; goods hidden)
Stage −5 — REVILED      : public_reputation  −51 to −100   (streets empty; civilians drop goods and flee; a mob may form)
```

> **CALIBRATION (v1.1, 2026-06-04):** bands rebanded so early-game deeds register — the prologue's small deltas (+2 to +4) now land at NOTICED/FAVORABLE (visible), while BELOVED/REVILED stay legendary end-states earned over the campaign. Previously +76 was needed for BELOVED while deeds give ±1–2, so reactions were never seen. The reaction-table headers below read `(+5)…(−5)` = the **Stage number**, not a raw score — find your score's Stage in this ladder, then use that Stage's reaction block. Two stages the old scale omitted (NOTICED, REVILED) are restored here to match the reaction table. Bands are tunable: adjust the ranges, keep the 11-stage structure.

**Track in JSON Save Block under:** `public_reputation` (integer) and `reputation_deeds[]` — both defined in KM_P2.txt. This file reads from that score.

> **SCOPE:** Reputation scores are tracked per region/settlement-type, not universally. Behavior in the Stolen Lands is not instantly known in Brevoy. Build a modular reputation — each region stores its own score, modified by how fast word travels.

---

## 🗣️ WITNESSED → WORD SPREADS — REPUTATION FORMS FROM CHATTER

> **DM:** This is ALWAYS on, from the Pre-Prologue forward — not only on settlement arrival. **Any time civilians are present and the player does something notable, the bystanders talk about it afterward, and that talk forms reputation.** A market, a roadside, a tavern, a city gate, a public square — anywhere there are people with eyes.

**Every notable witnessed action runs this loop:**
1. **In the moment** — at least one civilian reacts visibly (a murmur, a pointed finger, a stilled hand, a parent pulling a child back). Specific and particular, never "the crowd reacts."
2. **The talk** — afterward the witnesses tell each other what they saw. Good deeds become admiring retellings; cruel or frightening deeds become fearful warnings. Show a beat of it when natural (*"…did you see what they did to—"*).
3. **The score moves** — apply the matching `public_reputation` delta from the triggers below and log `reputation_deeds[]`. Admirable → toward BELOVED; frightening/cruel → toward REVILED.
4. **It sticks to the next encounter** — the *next* civilians the player meets in this area already act on that talk (use the CIVILIAN REACTION TABLE), because word reached them first. Word then propagates outward per the PROPAGATION rules below.

**No witnesses, no chatter.** If the player is genuinely alone — no civilians, no survivors to talk — nothing forms (same fairness rule as the Crime/Witness system). Reputation is built by what people *see and repeat*, not by what merely happened.

---

## 📈 REPUTATION SCORE CHANGE TRIGGERS

### Gaining Score (+1 per trigger unless noted)

**Witnessed actions (civilians present and observing):**
- Player defends a civilian from harm without being asked — no reward sought
- Player pays a fair price when they could have taken something or coerced
- Player resolves a public dispute in a way that clearly protects the weaker party
- Player returns a stolen item, lost child, or missing animal publicly
- Player contributes materially to civilian welfare (donates food during shortage, repairs a road personally, heals sick without charging)
- Player treats a civilian with explicit respect — calls them by name if known, listens when they speak, does not walk away mid-sentence
- Player acknowledges a civilian's contribution or labor (thanks the blacksmith, compliments the cook's food, notes the road-worker's work holds well)

**Kingdom decisions that filter down:**
- Passing a law that directly benefits commoners: +1 region-wide next turn
- Completing a civic building (Inn, Market, Temple): +1 in that settlement
- Reducing taxes with no stated reason: +1 region-wide (they notice even when they don't know why)
- Founding a new settlement: +1 in that hex for 2 turns (hope effect)
- Defeating a threat that civilians were actively afraid of (bandits, trolls, haunting): +1 in affected area

**+2 triggers (rare, witnessed by many):**
- Player publicly refuses a bribe or a noble's overreach in defense of common people
- Player personally participates in disaster relief (not just orders — present and working)
- Player spares a town from military action they could have taken and civilians know it
- Festival/Celebration day that the player visibly attends and participates in (not commands from a throne — actually present)

### Losing Score (−1 unless noted)

**Witnessed actions:**
- Player ignores a civilian in clear distress when intervention was possible and safe
- Player destroys civilian property without compensation
- Player threatens a civilian to gain information or compliance
- Player takes something from a civilian without paying
- Player allows companions to bully, belittle, or harm a civilian without intervention

**Actions with wide civilian visibility:**
- Player orders the destruction of a settlement feature (bridge, mill, granary) for tactical reasons
- Player conscripts civilians without warning or compensation
- Player executes a prisoner in public view
- Player sides with noble interest against obvious civilian harm in a public forum

**−2 triggers:**
- Player attacks or kills a civilian (even accidentally — the "accidentally" matters for narration; the score doesn't care)
- Player burns crops, poisons a well, or destroys a food supply
- Player publicly humiliates a civilian leader (village elder, market master)
- Player's army causes significant collateral damage in a populated area

**−3 immediate trigger (rare, catastrophic):**
- Player personally attacks a crowd or group of unarmed civilians
- Player orders a massacre of surrendered or fleeing non-combatants

---

## 🎭 CIVILIAN REACTION TABLE — BY SCORE

The DM uses this table whenever the player enters a new location. These are *behavioral defaults* — individual NPCs may vary, but the ambient reaction is described using this table.

### Stage 5 — BELOVED (+5)

**Shops / Markets:**
A vendor calls out by name before the player reaches the stall. The price is low — not because they're being transactional, but because they want to. Another vendor gestures the party over without being approached: *"I set one of these aside for you. Figured you'd be through eventually."*

**Taverns:**
The room gets louder when they enter, not quieter. Someone starts a round. A barkeep waves off the first drink. Two farmers argue quietly about who gets to tell the story of what the player did in their village. A child points and is shushed by a parent who is clearly proud of knowing who this is.

**Roads / Workers:**
Road crews straighten. Not military attention — civilian respect. Someone calls out a greeting by name. A teamster waves down the party to offer directions they didn't ask for, route information, a warning about what's ahead: *"There's something wrong in Hex 14 — you'll want to know."*

**Random Civilian Gifts (Stage 5 — roll 1d6 when entering a new settlement):**
| Roll | Gift |
|------|------|
| 1 | Fresh bread, still warm. "Just made it." |
| 2 | A handmade item of modest quality — carved wood, woven cloth. Made to last. |
| 3 | Useful intelligence about local terrain, threats, or persons of interest |
| 4 | An invitation: "My home tonight. Eat with us." (free Long Rest in a real bed; one random ally gains Inspired status next day) |
| 5 | A piece of useful gear — rope, lantern oil, a healing potion from "when times were harder" |
| 6 | A letter of introduction to a named NPC the player hasn't met yet |

---

### Stage 4 — RESPECTED (+4)

**Shops:** 10% discount applied without negotiation. The shopkeeper mentions it once and doesn't make a performance of it. Merchants volunteer information about rarer stock without being asked.

**Taverns:** Space is made at the bar. The barkeep tells the player what they've heard lately — not gossip; useful local rumors that may be quest hooks. Rooms are better than the price suggests.

**Roads:** Workers wave. A foreman stops work to update the player on the state of the road ahead. Farmers moving goods step aside without resentment. One offers to water the party's horses.

**Civilian Initiative:** Occasionally a civilian will approach the party proactively with information — a threat they spotted, a stranger asking suspicious questions, a cache they found and didn't know what to do with.

**Civilian Gifts (Stage 4 — roll 1d4 when entering a settlement, on a 4 a gift is offered):**
| Roll | Gift |
|------|------|
| 1 | A meal pressed on the party at the inn — "already paid for, don't argue." |
| 2 | Local knowledge: a shortcut, a dangerous stretch of road, a merchant to avoid |
| 3 | A small useful consumable — healing herbs, a torch bundle, trail rations for one day |
| 4 | A handwritten note of recommendation to someone in the next settlement |

---

### Stage 3 — KNOWN (+3)

**Shops:** Prices are standard but service is warm. The shopkeeper remembers the party if they've visited before. Mentions the player's name to the next customer — not a boast, just community knowledge.

**Taverns:** Welcomed, not celebrated. A good seat is offered. The bartender asks how the roads are. Locals ask where the party is headed with genuine interest.

**Civilian Gifts (Stage 3 — roll 1d6 on a new settlement visit; gift only on a 6):**
| Roll | Gift |
|------|------|
| 1–5 | No gift — warmth only |
| 6 | Something small and sincere: a jar of preserved fruit, a carved token, directions to a good campsite that isn't on any map |

**Roads:** Nods and acknowledgment. Workers don't stop, but they don't look away either. A traveler heading the opposite direction says something was spotted ahead.

**Advice:** At Stage 3, one civilian per settlement visit will offer unsolicited but useful local advice — regional knowledge, a rumored dungeon location, a note about which merchant can be trusted.

---

### Stage 2 — FAVORABLE (+2)

**Shops:** Normal prices. Shopkeeper is polite and professional. May mention having heard the name.

**Taverns:** Normal service. Some warmth — the barkeep makes small talk.

**Roads:** Normal traffic; no special reaction. Workers continue their work. No active hostility.

---

### Stage 1 — NOTICED (+1)

**Shops:** Slightly warmer than a stranger's welcome. The shopkeeper takes a second look.

**Taverns:** A few heads turn. Some curiosity. Someone heard a name.

**Roads:** Nothing notable. The party is noted passing, not reacted to.

---

### Stage 0 — UNKNOWN (0)

The default in new regions. No special reaction in any direction. Standard transactional behavior from all civilians. Treat as baseline PF2e NPC attitude: **Indifferent**.

---

### Stage −1 — CAUTIOUS (−1)

**Shops:** The shopkeeper completes the transaction without extras. Slightly clipped. No conversation volunteered.

**Taverns:** The room gets a little quieter when the party enters. Nothing hostile. Just watchful.

**Roads:** Workers glance up but don't look friendly. Some move to the other side of the road.

---

### Stage −2 — WARY (−2)

**Shops:** Full price, brisk service, no extras. The shopkeeper may mention not having something they visibly have in stock. A more experienced merchant may add 5–10% to prices if the party looks dangerous.

**Taverns:** The room quiets noticeably. The barkeep serves with professional neutrality. Some patrons find reasons to finish their drinks. The innkeeper may say the rooms are full.

**Roads:** Workers slow their pace and spread out — giving the party space. Some mothers call children close. A group of travelers heading toward the party takes a side path.

---

### Stage −3 — FEARED (−3)

**Shops:** Prices increase (DM's discretion; typically +15–25%). Some shopkeepers say they're closed when they're not. A few will serve silently without meeting the player's eyes.

**Taverns:** Active clearing of immediate space. Barkeep serves minimally. Conversations stop until the party is settled, then resume quietly elsewhere. The innkeeper has no rooms — even if the common room is empty.

**Roads:** Workers stop work and watch — not the curious watching of Stage 1. Wary. A farmer pulls a cart off the road and waits. Two guards at a gatehouse are visibly consulting each other before deciding to open the gate.

**Rumors:** The DM may deploy negative rumors ahead of the party — not slander, just fear-stories. Other travelers warn each other what's coming.

---

### Stage −4 — NOTORIOUS (−4)

**Shops:** Many won't serve at all. Those who do name a high price with a flat expression. Some lock the door when they see the party approach. A merchant may physically hide their better goods.

**Taverns:** The room empties within a few minutes of the party arriving. The barkeep will serve at the bar but will not speak more than necessary. No rooms. No warmth. If the party stays too long, whispers will bring the local watch.

**Roads:** Workers leave the work site. Not running — deliberate, quiet departure. Travelers actively detour. Village gates may be closed ahead of time if the party's approach was noticed.

**Active Hostility (Passive):** At −4, there is a 1-in-6 chance per settlement visit that a civilian throws something (verbal abuse, refuse), a door is slammed, or a civilian shouts an insult from a safe distance. Not an attack — a symbolic act of disgust.

---

### Stage −5 — REVILED (−5)

**Shops:** Closed. Shuttered. Some refuse to open even when the party knocks and announces themselves as paying customers. A few older vendors will serve from a window without unlocking the door.

**Taverns:** The room empties immediately. The barkeep produces what is asked for, takes the money, and says nothing. There may be no food left — suddenly. If the party stays, a mob may form (unarmed, frightened, but present — numbers suggest the party's presence is no longer welcome).

**Roads:** Workers abandon the site when the party is spotted. Carts detour miles out of their way. Villages close gates. A settlement the party needs to pass through may send a runner ahead to the next settlement.

**Active Attacks (Cornered):** At −5, civilians who cannot flee and who are pushed to a wall may attack — not skilled, not dangerous individually, but a group of 8–12 frightened farmers with farm tools is not trivial. The DM deploys this only when the party's behavior has made it narratively inevitable, not as a punishment trigger.

**Kingdom Effect at −5:** Civilian Reputation at −5 in a region imposes Unrest +2 in that region per Kingdom Turn, regardless of other factors. The people are actively destabilizing the domain.

---

## 🔄 REGIONAL REPUTATION PROPAGATION

Reputation is regional, not universal. But word travels.

```
PROPAGATION RULES:

  Local (same hex):      Reputation changes apply this scene
  Adjacent hexes:        Reputation change arrives after 1d4 days (slower in wilderness)
  Same region:           After 1 week (if roads exist), 2 weeks (overland only)
  Neighboring region:    After 2–4 weeks depending on trade routes and messengers
  Capital:               Always informed within 3 days if a Fame/Infamy-level event occurs

  FAME EVENTS — These propagate immediately, region-wide:
    - Killing a named monster that terrorized a region
    - Defeating a significant enemy force in open battle
    - Founding a settlement or completing a major civic building
    - Public execution of a noble or respected figure
    - Any action that generates a story flag with _public = TRUE
```

---

## ⏳ REPUTATION DECAY — MEMORY FADES

> **DM:** Reputation is not permanent. All scores — positive and negative — drift toward 0 (UNKNOWN) over time. People forget heroes. People forgive monsters. Absence, inaction, and passing turns erode the extremes in both directions. The only stable state is zero. Everything else must be maintained.

### Decay Rate (applied at the start of each Kingdom Turn)

Decay always moves the score **one step toward 0**. Positive scores decrease; negative scores increase.

| Condition | Drift |
|-----------|-------|
| Player has not entered this region in 2+ turns | 1 step toward 0 |
| Player has not entered this region in 4+ turns | 1 additional step toward 0 (cumulative) |
| Score is ±3 or higher AND no relevant kingdom action this turn | 1 step toward 0 |
| Score is ±1 or ±2 with no active triggers | No drift — near-zero holds |

**Maximum drift per turn:** 2 steps toward 0 (both conditions met simultaneously).

**Decay stops at 0.** Scores never drift past UNKNOWN from time alone. Only active witnessed actions push a score in either direction past zero.

**What counts as a "relevant kingdom action" to pause drift:**
- For positive scores: any civilian-benefiting decision, civic building completion, or public presence in the region
- For negative scores: any violent, exploitative, or neglectful action in or affecting the region

### Anchored Scores — Decay Immunity

Some events permanently anchor a regional score against decay. The score can still rise or fall from new actions, but it will not decay below the anchored floor.

| Event | Anchor Floor | Region |
|-------|-------------|--------|
| Player personally ends a long-running regional threat (e.g., Stag Lord, trolls) | +2 | Affected region |
| Player founds a settlement or completes a Castle/Palace | +1 | That settlement's hex |
| Player stages a public Festival (Celebrate Holiday) in a region | +1 | That region, for 2 turns |
| Global Milestone event (see below) | Varies | See milestone table |

**Save block field:** Add `"anchor": 2` to a region's object when an anchor applies.

---

## 🌍 GLOBAL MILESTONE EVENTS

> **DM:** Certain events are so significant they alter reputation everywhere simultaneously — not just the region where they happened. These are the moments the entire Stolen Lands talks about. They propagate immediately to all tracked regions and cannot be decay-reduced for 3 Kingdom Turns after they fire.

Apply these when the corresponding story flag is set. They stack with regional scores but cannot push any region above +5 or below −5.

### Positive Milestones

| Event | Story Flag | Rep Change | Scope |
|-------|-----------|------------|-------|
| Stag Lord defeated — bandit threat ends | `stag_lord_fate` set (any value) | +1 all regions | Immediate, region-wide |
| Stag Lord's camp claimed and garrisoned | `stag_lord_fort_claimed = TRUE` | +1 all regions | Fired separately from defeat |
| Player crowned Baron/Baroness | `coronation_complete = TRUE` | +2 all regions | Legendary status — people feel stability |
| Kingdom founded (charter complete) | `kingdom_founded = TRUE` | +1 all regions | Hope effect |
| Troll menace ended (Ch2) | `troll_threat_ended = TRUE` | +2 Stolen Lands, +1 others | Enormous local relief |
| Varnhold rescued (Ch3) | `varnhold_saved = TRUE` | +1 all regions | Solidarity — a whole town returned |
| Tiger Lords pacified with a chief (Ch4) | `tiger_lords_pacified = TRUE` | +1 Stolen Lands | Borders feel safer |
| Rushlight Tournament won publicly | `rushlight_won = TRUE` | +1 all regions | People love a champion |

### Negative Milestones

| Event | Story Flag | Rep Change | Scope |
|-------|-----------|------------|-------|
| Player publicly executes a surrendered enemy in front of civilians | `public_execution_civilian_witnessed = TRUE` | −1 all regions | Fear spreads |
| Player destroys a civilian settlement | `settlement_destroyed = TRUE` | −2 all regions | Outrage, regardless of reason |
| Kingdom Unrest exceeds 15 for 2+ turns | *(checked automatically)* | −1 all regions | Suffering is visible |
| Player sides with Pitax openly (Ch4+) | `pitax_alliance_public = TRUE` | −2 Stolen Lands, −1 others | Betrayal narrative |

**Save block field:** Log milestones in `"global_events"` array under `reputation{}`:
```json
"global_events": [
  { "event": "stag_lord_defeated", "turn": 8, "rep_applied": true },
  { "event": "coronation_complete", "turn": 14, "rep_applied": true }
]
```

---

## 🗺️ REPUTATION SAVE BLOCK FORMAT

```json
"reputation": {
  "regions": {
    "stolen_lands": {
      "score": 3,
      "stage": "KNOWN",
      "anchor": 2,
      "last_player_visit_turn": 6,
      "modifiers": [
        { "source": "troll_cleared", "value": 1, "turn": 4 },
        { "source": "merchant_threatened", "value": -1, "turn": 6 }
      ]
    },
    "brevoy_border": {
      "score": 1,
      "stage": "NOTICED",
      "anchor": 0,
      "last_player_visit_turn": 3,
      "modifiers": []
    },
    "oleg_trading_post_area": {
      "score": 4,
      "stage": "RESPECTED",
      "anchor": 1,
      "last_player_visit_turn": 7,
      "modifiers": []
    }
  },
  "global_events": [
    { "event": "stag_lord_defeated", "turn": 8, "rep_applied": true }
  ],
  "last_civilian_reaction": "Favorable — shopkeeper at Oleg's offered 10% discount unprompted",
  "active_rumors": [
    { "region": "stolen_lands", "type": "positive", "content": "Cleared the Stag Lord's bandits from the south road" }
  ]
}
```

---

## 🖥️ REPUTATION COMMANDS

| Command | Output |
|---------|--------|
| `.reputation` | All regional scores, current stage, recent changes |
| `.reputation [region]` | One region's full score, stage, modifiers, active rumors |
| `.civilians` | Current ambient civilian behavior for this location |
| `.rumors` | Active civilian rumors about the party in the current region |
| `.fame` | Current Fame/Infamy from KM_Kingdom.md cross-referenced with Reputation |

---

## ⚠️ REPUTATION DESIGN RULES FOR THE DM

1. **Civilian reactions are specific, not generic.** Don't say "the civilians react positively." Say what the baker does with his hands when he recognizes the party. Say what the road worker looks at when the party passes. The abstraction is for score-tracking; the narration is always particular.
2. **Reputation rewards small choices.** A player who consistently pays fairly, thanks workers, and stops for the injured builds Reputation faster than one who occasionally does heroic deeds but is dismissive otherwise. The scale tracks behavior, not highlights.
3. **Negative Reputation has texture.** Fear and contempt feel different. A −3 settlement is afraid. A −5 settlement is angry. The DM differentiates.
4. **Reputation and Kingdom Stats interact but don't replace each other.** A high Kingdom Loyalty does not mean high civilian Reputation in a specific region. The Treasurer managing the tax books efficiently ≠ the ruler being remembered warmly by the family at the end of the road.
5. **At Stage 5, civilians are protagonists in the party's story.** The blacksmith who set aside the good iron. The farmer who sent a runner with a warning. The innkeeper who let the party sleep free during the crisis. Name these people. Let them exist in the world. This is the reward the Reputation system earns.

---

---

## 🏛️ FACTION REWARD TIERS

> **DM:** Major factions track attitude toward the player on a −10 to +10 scale. At specific thresholds, faction-exclusive rewards unlock. These are separate from civilian reputation (above) — a faction can hate you while peasants love you.

### Faction Attitude Scale

| Score | Tier Name | What Unlocks |
|-------|-----------|-------------|
| −10 to −6 | **Hostile** | Faction actively works against you. Agents sent. Trade embargoed. |
| −5 to −1 | **Unfriendly** | No trade, no aid. Cold diplomatic responses. |
| 0 to +2 | **Neutral** | Basic trade. Standard prices. No special access. |
| +3 to +4 | **Friendly** | Faction vendor unlocked (unique gear at market prices). Diplomatic requests answered within 1 turn. |
| +5 to +6 | **Honored** | Elite vendor tier (rare items, discounted 10%). Faction-specific companion available for recruitment. |
| +7 to +8 | **Revered** | Military alliance option (call faction army in wartime, 1 unit, 2 turns). Kingdom stat bonus: +2 to faction-aligned stat per turn. |
| +9 to +10 | **Exalted** | Story-altering alliance. Faction leader offers personal support in final chapter. Unique ending flag set. |

### Major Factions

| Faction | Aligned Stat | Vendor Specialty | Recruitable Companion (Honored) | Military Unit (Revered) |
|---------|-------------|-----------------|-------------------------------|----------------------|
| **Aldori Swordlords** | Loyalty | Aldori dueling swords, training manuals | Aldori Blade Instructor (Fighter) | Swordlord Duelists (Offense +7, Def 16, Morale 18) |
| **Brevoy Crown (Surtova)** | Stability | State-issue plate, siege equipment | Crown Inspector (Investigator) | Brevoy Royal Guard (Offense +6, Def 18, Morale 14) |
| **Kellid Tribes** | Culture | Tribal weapons, beast trophies, war paint | Kellid Skald (Barbarian/Bard) | Tiger Lord Raiders (Offense +8, Def 12, Morale 16) |
| **River Kingdoms Coalition** | Economy | Trade goods, river navigation charts, smuggler contacts | River Pirate Captain (Rogue) | River Corsairs (Offense +5, Def 14, Morale 12) |
| **Pitax** | Economy | Art, poisons, courtly gear, espionage tools | Pitax Defector (Bard/Rogue) — only if not at war | Pitax Mercenaries (Offense +6, Def 15, Morale 10) |

### Faction Score Changes
- **+1:** Complete a quest favoring the faction, make a diplomatic concession, trade agreement
- **+2:** Military aid during their crisis, return a stolen artifact, major public alliance
- **−1:** Reject a diplomatic request, trade with their rival, minor insult
- **−2:** Military action against their interests, harbor their enemies, public denouncement
- **−3:** Direct attack on faction territory or assets

**Save block:** `"faction_tiers": { "aldori": 0, "surtova": 0, "kellid": 0, "river_kingdoms": 0, "pitax": 0 }`

---

*KM_World_Systems.md — Kingmaker PF2e Text Adventure | Reputation System v2.0*
*Systems: Civilian Reputation (5-stage), Regional Propagation, Faction Reward Tiers*


---

<!-- merged from KM_World_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — CRIME SYSTEM
## KM_World_Systems.md | Active from: Chapter 1 | Referenced by: KM_World_Systems.md, KM_Kingdom.md, KM_Actions.md

> **DM:** Load this file whenever the player enters a settlement, interacts with
> named NPCs in private spaces, or takes any action that could constitute theft,
> assault, murder, trespass, or fraud. This system uses only existing PF2e skill
> mechanics — no new stats are invented. It feeds directly into KM_World_Systems.md
> (civilian reputation) and KM_Kingdom.md (Infamy, Unrest). It does not override
> alignment tracking — it feeds it.

---

## ⚖️ CRIME CATEGORIES

| Category | Examples | Base Severity |
|----------|----------|---------------|
| **Petty** | Pickpocket, trespass, minor fraud, vandalism | 1 |
| **Moderate** | Burglary, assault, arson (small), extortion | 2 |
| **Serious** | Armed robbery, grievous assault, grand theft | 3 |
| **Capital** | Murder, massacre, arson (major), treason | 4 |

Severity scales consequences: fines, pursuit intensity, Infamy gain, and companion reactions.

---

## 👁️ THE WITNESS SYSTEM

Every criminal act has a **Witness Check**. The DM resolves this secretly.

```
WITNESS CHECK PROCEDURE

Step 1 — Establish the scene:
  Is anyone present?
    NO WITNESSES POSSIBLE → skip to Step 4 (evidence only)
    WITNESSES POSSIBLE → proceed

Step 2 — Count potential witnesses:
  Isolated (wilderness, locked room alone):   1 flat check DC 18 (random passerby, animal, spirit)
  Low traffic (back alley, late night):       1d3 witnesses, each rolls Perception vs player's Stealth
  Normal traffic (market, tavern, road):      1d6 witnesses, Perception DC = player's Stealth result
  High traffic (public square, feast, court): Automatic — 1d4 witnesses notice regardless of Stealth

Step 3 — Witness Perception check (DM rolls secretly):
  Each witness rolls Perception vs the player's Stealth or Deception check.
    Witness succeeds:   They saw it. Proceed to Witness Type table.
    Witness fails:      They noticed nothing. No report.
    Witness crits:      They saw it AND can describe the player accurately (+1 to all pursuit checks).

Step 4 — Physical Evidence:
  Even with no witnesses, crime leaves traces.
    Body not hidden:        Evidence = OBVIOUS (found within 1d4 hours)
    Item stolen, no body:   Evidence = SUBTLE (found within 1d6 days on successful Investigation DC 18)
    No physical trace:      Evidence = NONE (e.g., pickpocket with no dropped items, clean kill)
  If player takes steps to conceal evidence: Survival or Thievery vs DC 18 to reduce one tier.
    OBVIOUS → SUBTLE on success | SUBTLE → NONE on critical success only
```

### Witness Type Table

| Witness Type | Immediate Action | Report Speed |
|---|---|---|
| Child | Runs to parent; describes poorly | 1d4 hours |
| Civilian adult | Avoids player; reports to guards | 1d6 hours |
| Merchant | Locks up; reports and posts reward | 1 hour |
| Guard (off-duty) | Challenges player immediately | Immediate |
| Guard (on-duty) | Arrest attempt immediately | Immediate |
| Companion (party) | Reacts per personality — see below | Immediate |
| Named NPC (friendly) | Private confrontation; no report unless pushed | 1 session |
| Named NPC (neutral) | Reports unless bribed or intimidated | 1d4 hours |
| Named NPC (hostile) | Reports and embellishes | 30 minutes |

---

## 🎭 CRIME ACTIONS & SKILL DCS

### THEFT

**Pickpocket** — Thievery vs target's Perception DC
- Target is unaware: DC = Perception modifier + 10
- Target is distracted: DC −2
- Target is alert/suspicious: DC +4
- **Crit Success:** Item taken; target unaware anything happened
- **Success:** Item taken; target notices something felt wrong but can't place it (50% chance they check pockets in 1d10 minutes)
- **Failure:** Attempt failed; target is now Suspicious (Perception checks vs you at +2 for this scene)
- **Crit Failure:** Caught in the act; Witness Check triggers at +4

**Burglary** — requires bypassing locks and avoiding guards
- Pick Lock: Thievery vs lock DC (see KM_Conditions_Skills.md)
- Avoid Guards: Stealth vs guard Perception DC (base 14, +2 per guard tier above standard)
- Time pressure: each lock attempt = 1 minute of exposure; flat check DC 12 per minute for a patrol to pass
- **Getting away clean:** Must succeed on both lock pick and stealth; failure on either triggers Witness Check

**Loot a Body** — no check if unwitnessed; Stealth vs DC 14 if in a populated area

**Rob a Merchant (armed)** — Intimidation vs Will DC 16 (base)
- Success: merchant complies; reports immediately after player leaves
- Failure: merchant resists; combat or retreat

---

### ASSAULT & MURDER

**Assault (non-lethal)** — Standard combat with nonlethal damage flag
- Witness Check triggers if anyone is present
- Target recovers and can report — treat as a live witness

**Murder (hidden kill)** — Requires player to be Hidden or Undetected first
- Stealth approach: Stealth vs target Perception DC
- Kill action: standard Strike — target is off-guard if Undetected
- Post-kill concealment: Survival or Thievery DC 18 to hide body
  - Success: body found in 1d6 days
  - Failure: body found in 1d4 hours
  - Crit Success: body may never be found (DM rolls flat check DC 14 per week)

**Public Murder** — No stealth possible; automatic Witness Check at maximum traffic tier
- Companion reactions fire immediately (see below)
- Reputation: −2 in current region, propagates per KM_World_Systems.md rules
- If player is the ruler: Infamy +2, Unrest +1 next Kingdom Turn

**Assassination** — Planned murder of a named NPC
- Requires a Planning Check before execution: Society or Intrigue Lore DC 18 to case the target
- Success on planning: +2 to all checks during the attempt; evidence tier reduced by one step
- The DM runs this as a mini-sequence: approach → access → act → escape
- Named NPCs with significant political weight (nobles, faction leaders) trigger faction reputation hits on death — see KM_Kingdom.md faction tables

---

### FRAUD & DECEPTION

**Impersonate an Official** — Deception vs observer Perception DC
- With forged documents: DC −4
- Without: DC as written
- Failure in a settlement: Witness Check immediately

**Forge Documents** — Society DC 20 (common document) to DC 30 (official writ)
- Player must have materials: ink, paper, a sample to copy (−2 DC if sample available)
- Forgery is not detected until someone examines it (Society DC 20 to spot)

**Extortion** — Intimidation vs Will DC; target's wealth tier determines payout
- Common civilian: 1d6 gp per severity level extorted
- Merchant: 2d10 gp
- Noble: 5d10 gp — but noble has resources to pursue
- Every extortion: flat check DC 14; success = someone reported it

---

## 🚨 GETTING CAUGHT — RESPONSE TIERS

When a crime is witnessed or reported, the response scales with severity and the player's status.

```
RESPONSE MATRIX

              | No Prior Infamy | Infamy 1–3 | Infamy 4–6 | Infamy 7+ |
Petty         | Fine offered    | Fine + watch| Detention  | Arrest    |
Moderate      | Detention       | Arrest      | Arrest+    | Hunt      |
Serious       | Arrest          | Hunt        | Hunt+      | Kill order|
Capital       | Hunt            | Kill order  | Kill order | Kill order|

Fine:         Pay Severity × 5 gp or face escalation
Detention:    Held for 1d4 hours; gear held; escorted out of settlement
Arrest:       Full custody; trial scene triggers; see Trial section
Hunt:         Bounty posted; bounty hunters spawn in the region
Kill order:   No trial; any guard or bounty hunter may kill on sight
```

### GUARDS — RESPONSE BEHAVIOR

**Standard Guard (L2 Fighter)**
- Will not pursue beyond settlement boundary unless bounty is active
- Can be Intimidated (DC 18) to back down — but they report it afterward
- Can be Bribed: 5 gp × severity to look the other way (flat check DC 12; failure = they take the money AND arrest you)
- Three guards = automatic arrest attempt unless player flees

**Guard Captain (L5 Fighter)**
- Personally pursues fleeing suspects for 1d4 rounds beyond settlement
- Cannot be Intimidated without a crit success
- Bribe DC 18 (flat); costs 20 gp × severity

**Bounty Hunters (L = party level)**
- Spawn 1d4 days after bounty is posted
- 1–2 hunters for petty/moderate; 3–4 for serious; full squad (4–6) for capital
- Have player description and last known location
- Will track across regions; do not stop at settlement boundaries
- Can be negotiated with (Diplomacy DC 22) if player surrenders or pays bounty value

---

## 🏃 GETTING AWAY — ESCAPE OPTIONS

### Flee the Scene
- Chase subsystem triggers (see KM_Game_Subsystems.md)
- Player must clear 3 obstacles to escape settlement; 5 obstacles if bounty hunters are involved

### Disguise
- Deception DC 18 to change appearance enough to avoid casual recognition
- Requires at least 10 minutes and a change of visible clothing
- Named witnesses who got a crit on their Perception check can still identify you at DC 22

### Alibi
- Diplomacy or Deception DC 20 to establish a false alibi with a willing NPC
- Willing companion can vouch: DC 14 (they are trusted). Companion relationship must be Friendly or better.
- False alibi breaks if the NPC is pressed with evidence: Society DC 18 for investigators

### Bribery (after the fact)
- Can suppress a report if player reaches the witness before they report
- Cost: Severity × 10 gp per witness
- Intimidation instead of gold: Coerce action, DC 16 + Severity × 2
  - Success: they stay quiet this session
  - Failure: they report AND mention the intimidation attempt (+1 Severity to response tier)

### Leave the Region
- Crimes do not follow the player to new regions unless Severity 4 (capital) or Infamy 5+
- Infamy 5+: crimes propagate to adjacent regions within 1 week
- Infamy 7+: crimes propagate across all known regions within 2 weeks

---

## 📊 INFAMY TRACK

Separate from Reputation. Infamy measures how widely known the player is as a criminal — not just feared, but **wanted**.

```
Infamy 0:   Unknown criminal record
Infamy 1–2: Minor incidents on record; some merchants wary
Infamy 3–4: Wanted poster in 1d3 settlements; guards alert
Infamy 5–6: Wanted poster everywhere in region; bounty active
Infamy 7–8: Multi-region manhunt; faction bounties stack
Infamy 9:   Kill-on-sight in all known regions
Infamy 10:  National incident; Brevoy or River Kingdoms sends forces
```

**Gaining Infamy:**

| Crime | Infamy Gained |
|-------|--------------|
| Petty crime, caught | +0 (logged, not infamous) |
| Moderate crime, caught | +1 |
| Serious crime, caught | +2 |
| Capital crime (murder of commoner), caught | +2 |
| Capital crime (murder of noble/official), caught | +3 |
| Crime witnessed publicly by 5+ people | +1 additional |
| Crime in own kingdom as ruler | +1 additional (subjects watch) |

**Reducing Infamy:**

| Action | Infamy Reduced |
|--------|---------------|
| Pay all outstanding fines and bounties | −1 |
| Publicly perform a heroic act in affected region | −1 |
| Kingdom: Repair Reputation action (K23) | −1 per success |
| Full chapter passes without new crimes | −1 (natural fade) |
| Bribe or eliminate all witnesses (risky) | −1 per tier of evidence removed |

**Infamy and the Kingdom:**
- Infamy 3+: Infamy bleeds into kingdom Infamy stat at +1 per chapter if player holds a leadership role
- Infamy 5+: Faction reputation hits begin — Aldori Swordlords −1 per chapter, Brevoy Crown −2
- Infamy 7+: Jamandi sends a formal letter. If unresolved: charter review triggers

---

## ⚖️ TRIAL SCENE

Triggered when player is arrested and cannot escape custody.

**Trial Structure:**
1. Player is brought before a magistrate or settlement authority
2. Evidence is presented (witnesses, physical evidence tier)
3. Player may speak in their own defense: Diplomacy or Deception vs DC 18
4. Player may call a companion as character witness: companion must be Friendly or better; adds +2
5. Player may reveal their ruler status (if applicable): automatic DC reduction of 4 — but Infamy gain +1 for the abuse of position

**Verdicts by evidence tier:**

| Evidence | Player Defense Success | Verdict |
|----------|----------------------|---------|
| NONE | Any | Acquitted; Reputation +1 (wrongful arrest) |
| SUBTLE | Crit Success | Acquitted; fine waived |
| SUBTLE | Success | Guilty; fine only |
| SUBTLE | Failure | Guilty; fine + 1d4 days detained |
| OBVIOUS | Crit Success | Guilty; reduced sentence (fine only) |
| OBVIOUS | Success/Failure | Guilty; sentence per severity |
| OBVIOUS + witness crit | Any | Guilty; full sentence |

**Sentences by severity:**

| Severity | Sentence |
|----------|----------|
| Petty | Fine: 10–50 gp |
| Moderate | Fine: 50–200 gp + banned from settlement 1d4 weeks |
| Serious | Fine: 200–500 gp + imprisoned 1d6 days + Infamy +1 |
| Capital | Execution (player may attempt escape) OR life imprisonment (escape arc) |

**Execution path:** Player has one chance to escape before sentence is carried out — Chase subsystem, 5 obstacles, guards are L = party level +2. Success: fugitive status. Failure: character death (or player accepts fate for narrative reasons).

---

## 🗡️ COMPANION REACTIONS TO CRIME

Companions who witness crimes react immediately and persistently.

| Companion | Petty | Moderate | Serious | Capital |
|-----------|-------|----------|---------|---------|
| **Valerie** | Disapproves silently | States objection formally | −1 Relationship; refuses to assist | −2 Relationship; may leave party |
| **Linzi** | Notes it; doesn't report | Writes about it; troubled | −1 Relationship; asks why | −2 Relationship; threatens to publish |
| **Tristian** | Asks if it was necessary | Prays openly; disapproves | −1 Relationship; refuses healing until apology | −2 Relationship; leaves if not addressed |
| **Harrim** | Indifferent | Finds it tiresome | Mildly approves (chaos) | Approves; +1 Brotherhood |
| **Regongar** | Approves | Approves +1 | Approves +1; offers help | Approves +2; wants in next time |
| **Amiri** | Ignores | Ignores unless victim was warrior | Disapproves if cowardly | −1 if victim couldn't fight back |
| **Nok-Nok** | Impressed | Very impressed | "Teach Nok-Nok?" | Legendary in his eyes; +1 Relationship |
| **Octavia** | Arches eyebrow | Notes it; no judgment | −1 if victim was vulnerable | −2 if victim was enslaved/powerless |
| **Jaethal** | Interested | Approves | Approves +1 | Approves +2; admires commitment |
| **Ekundayo** | Disapproves | −1 Relationship | −1 Relationship; cold for 1 session | −2 Relationship; formal objection |

**Companion assist in crime:**
Some companions will actively help with certain crimes if asked and relationship is Friendly+.

| Companion | Will assist with |
|-----------|-----------------|
| Regongar | Assault, extortion, intimidation |
| Nok-Nok | Theft (enthusiastically), distraction |
| Jaethal | Murder, assassination (if target "deserves it") |
| Octavia | Fraud, forgery, impersonation |
| Harrim | Will stand watch; will not report |

Asking a companion to assist who would refuse: −1 Relationship and they remember you asked.

---

## 💾 CRIME SAVE BLOCK

```json
"crime": {
  "infamy": 0,
  "active_bounties": [],
  "outstanding_fines": 0,
  "known_crimes": [],
  "witnesses_outstanding": [],
  "fugitive_regions": [],
  "trial_pending": false,
  "last_crime_chapter": null,
  "companion_crime_reactions": {}
}
```

**`known_crimes` entry format:**
```json
{
  "type": "murder",
  "severity": 4,
  "location": "Oleg's Trading Post",
  "chapter": 1,
  "witnesses": 1,
  "evidence_tier": "SUBTLE",
  "resolved": false
}
```

---

## 🖥️ CRIME COMMANDS

| Command | Output |
|---------|--------|
| `.crime` | Current Infamy, active bounties, outstanding warrants |
| `.crime history` | All logged crimes this campaign |
| `.bounty` | Active bounty hunters: location, level, distance |
| `.wanted` | Wanted status per region |
| `.trial` | Current trial status and available defense options |

---

## ⚠️ DESIGN RULES FOR THE DM

1. **Never punish crime automatically.** The system fires on witness results and evidence. If the player genuinely got away clean, they got away clean. Do not retroactively add witnesses.
2. **Consequences are lived, not announced.** Don't say "your Infamy increases." Show the wanted poster at the next settlement gate. Show the bounty hunter asking the innkeeper about someone matching the player's description.
3. **Companions are not the morality police.** They react once, clearly, then move on. They do not lecture repeatedly. Harrim's indifference is as valid as Tristian's prayer.
4. **Ruler crimes have political weight.** The player is building a kingdom. A ruler who murders merchants in their own territory is not just a criminal — they are a policy.
5. **Crime can be strategic.** Assassination of a faction leader, theft of a key document, framing a rival — these are valid campaign tools. Run the consequences faithfully, not punitively.
6. **Getting away with it is satisfying.** A clean crime with no witnesses and buried evidence should feel like a win. The system earns its tension by being fair in both directions.

---

*KM_World_Systems.md — Kingmaker PF2e Text Adventure | Crime & Infamy System v1.0*
*Uses: PF2e Thievery, Stealth, Deception, Intimidation core rules | No new mechanics invented*


---

<!-- merged from KM_World_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — TRAVEL SEGMENT SYSTEM
## KM_World_Systems.md | Active from: Pre-Prologue onward | Referenced by: KM_Exploration.md

> **DM:** Load this file whenever the party begins any overland journey. It replaces day-level
> travel summaries with segment-by-segment narration — each segment is a natural pause where
> companions can talk, the player can ask questions, and the world passes by.
> Segment count is determined by distance and travel mode. Never summarize a multi-segment
> journey in one paragraph. Each segment is its own scene beat.

---

## 🚶 TRAVEL MODES

| Mode | Miles/Day | Segments/Day | Miles/Segment | Notes |
|------|-----------|--------------|---------------|-------|
| **On foot** | 15 mi | 3 | 5 mi | Morning · Midday · Afternoon |
| **Horseback** | 30 mi | 3 | 10 mi | Faster; no foraging while mounted |
| **Carriage/Wagon** | 25 mi | 3 | ~8 mi | Comfortable; can converse freely; cargo |
| **Hustle (foot)** | 24 mi | 3 | 8 mi | Party gains Fatigued at end of day |

> **Segment count formula:** `CEIL( distance_miles ÷ miles_per_segment ) = total segments`
> The final segment ends with arrival at the destination, not a camp.

---

## 📍 SEGMENT DISPLAY FORMAT

Output this header at the start of each segment, then narrate the scene:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOURNEY: [Origin] → [Destination]
Mode   : [On foot / Horseback / Carriage]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Segment           : [X] of [Y]
Distance traveled : [X × miles_per_segment] miles
Distance remaining: ~[total − traveled] miles
Terrain           : [Plains / Forest / Hills / etc.]
Time of day       : [Morning / Midday / Afternoon]
Weather           : [Current condition]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎲 SEGMENT EVENTS

Each segment gets **one event** drawn from the priority list below. DM picks based on
context (what companions are present, current story flags, terrain):

| Priority | Event Type | Trigger |
|----------|-----------|---------|
| 1 | **Companion banter** | Fire one banter from KM_Companions_Behaviors.md; tone-match to terrain/mood |
| 2 | **Landmark / scenery** | Named waypoint for this route (see named routes below) |
| 3 | **Conversation opportunity** | Player can ask a companion an open question — DM uses "Waiting for you to speak first" |
| 4 | **Minor encounter** | Roll d20; on 1–3 fire a random encounter appropriate to terrain and zone |
| 5 | **Discovery** | On a 1 in 6: the party spots something small — tracks, a cairn, a lost item, smoke in the distance |

> Each companion should fire banter no more than once per 3 segments on the same journey
> (prevent same companion dominating). Rotate through active party.

**Conversation opportunity** — script:
```
The road stretches on. [Companion name] rides/walks alongside you.
No one speaks for a stretch. The silence is comfortable — or almost.
```
Then pause for player input. Accept any question to a companion, discussion of current quest,
lore questions ("what do you know about X"), or just quiet travel. DM responds in character.

---

## 📋 SEGMENT CHOICE MENU

After each segment event, present 3–4 options (not a full menu — keep it quick):

```
  [1] Press on → next segment
  [2] Talk to [most active companion] about [context-appropriate topic]
  [3] Make camp here (if afternoon segment and party is tired or supplies are low)
  [4] Scout ahead (Perception/Survival DC 15 — reveals next segment terrain or nearby encounter)
```

> Option 3 only if the party has camped less than required for this day's travel.
> Option 4 costs no time; result applies to the NEXT segment only.

---

## 🗺️ NAMED ROUTES

Named routes have pre-written segment waypoints. DM reads them in order.
**Do NOT fabricate waypoints — use the list below. If the route is not listed, use generic
terrain description from KM_Map.md and fire companion banter as the primary segment event.**

---

### ROUTE A — Restov → Oleg's Trading Post
**Distance:** ~36 miles | **Road:** South Merchant Road (packed earth, maintained)
**Terrain:** Rostland Plains → northern Greenbelt edge

| Mode | Segments | Travel time |
|------|----------|-------------|
| On foot | 8 segments (~3 days) | Day 1: seg 1–3 · Day 2: seg 4–6 · Day 3: seg 7–8 + arrival |
| Horseback | 4 segments (~1.5 days) | Day 1: seg 1–3 · Day 2: seg 4 + arrival |
| Carriage | 5 segments (~2 days) | Day 1: seg 1–3 · Day 2: seg 4–5 + arrival |

**Segment Waypoints:**

```
SEG 1 — RESTOV SOUTH GATE (Mile 0–5/10)
  The city falls behind you. South Gate's twin towers shrink. The road here is still
  cobbled — merchants' carts have worn the stones smooth. Farmsteads to either side,
  grain fields, the smell of bread from a roadside mill. The last city smells.
  ► Banter opportunity: First-day energy. Characters settling in for the journey.

SEG 2 — ROSTLAND FARMS (Mile 10–15/20)
  The cobbles end. Packed earth now, wide enough for two wagons to pass. Scattered
  farmsteads, hedgerows, old stone walls dividing fields. A shepherd waves from a hill.
  The sky is wide in a way it never is in the city. Distant smoke: a farmhouse chimney.
  ► Landmark: The old milestone marker — cracked, still readable. "XII leagues to Restov."
  ► Banter opportunity: Open road. Companions comment on the quiet or the frontier.

SEG 3 — THE LAST FARMS (Mile 15–21/30)
  The farmsteads thin. The last one is shuttered — boards over the windows, no smoke.
  A burned fence post. Old trouble, or recent? The road continues south but the
  maintained sections end here. Beyond this point: untended country.
  ► Discovery check: DC 14 Perception — fresh wagon tracks, recent but abandoned.
  ► Banter opportunity: The shift from Rostland to the Greenbelt edge. Mood changes.

SEG 4 — OPEN PLAINS (Mile 21–26/30)
  Grassland to the horizon. The road is a suggestion here — a worn trail through tall
  yellow grass. Wind moves in long waves. No structures in sight. A hawk circles
  something to the east. The sky has gotten bigger.
  ► Random encounter check: roll d20, encounter on 1–4 (open road, low zone).
  ► Banter opportunity: The open country. Companions are more relaxed or more alert
    depending on personality.

SEG 5 — GREENBELT EDGE (Mile 26–30/36)
  The first trees appear on the southern horizon, then alongside the road. The grass is
  taller, the trail narrower. The air smells different — earth, pine, something wilder.
  This is the Greenbelt. The charter is no longer abstract.
  ► Landmark: A weathered signpost. "OLEGS — 6 MI." The wood is old; someone keeps
    repainting it. Oleg, probably.
  ► Banter opportunity: The Greenbelt. Companions who know it have something to say.
    Companions who don't might ask someone who does.

SEG 6 — NORTHERN GREENBELT ROAD (Mile 30–36)
  The road deteriorates to two ruts in the grass, but it's clear enough. Old campfire
  rings along the verge — travelers use this stretch regularly. Thinning trees to the
  left. The sky ahead is unobstructed. Something on the horizon: a low structure, walls.
  ► Discovery: DC 12 Perception — boot prints in the mud, several sets, going south.
    Travelers or bandits? Fresh, maybe a day old.
  ► Banter opportunity: Almost there. Anticipation. First sight of something built.

SEG 7 — OLEG'S IN SIGHT (Foot only — final push)
  The trading post resolves from a smudge on the horizon into something real. A converted
  border fort: stone walls, a wooden gatehouse, smoke from inside. Smaller than expected.
  More isolated. A flag — Oleg's own, not Restov's.
  ► Banter opportunity: Companions who know Oleg's have memories. Others have questions.

SEG 8 → ARRIVAL
  The gate is closed but not barred. A voice from above: *"Who's there?"* — suspicious,
  then cautious, then something that might become welcome. The journey is over.
```

---

## 🐴 MOUNTS & TRAVEL SPEED

Horses bought at Oleg's Trading Post reduce segment count and total travel time.
See **KM_NPCs.md § HORSES & MOUNTS** for purchase and rental prices.

**Mounted travel rules:**
- Foraging during travel is not possible while mounted (no time to stop and search)
- Horses require 10 lbs of feed per day (Oleg sells feed; forage in grassland hexes with
  Survival DC 12)
- A horse cannot enter Deep Forest or Mountain hexes at travel speed (reduce to foot pace)
- In combat: horse is a separate creature with its own AC (13), HP (32), Speed 50
- If a horse is killed in combat: party member is Prone and must make DC 14 Acrobatics or
  take 1d6 bludgeoning damage from the fall

---

## 📐 GENERIC JOURNEY SEGMENTS (for unlisted routes)

When the party travels a route not listed above, build segments from these parts:

**Terrain flavor by type:**
```
PLAINS/ROAD : Wide sky, grass moving in wind, distant farmsteads or no structures at all.
              The road is the one fixed thing in an unfixed landscape.
FOREST      : The canopy closes overhead. Sounds change — birds you know, then birds you
              don't. Light comes in slants. The road becomes a path becomes a suggestion.
HILLS       : The footing is uncertain. Elevation reveals distance you didn't expect.
              Switchbacks. Wind at the top. You can see where you've been.
RIVER HEX   : The water sound before you see it. The ford — always deeper than expected.
              Mud on the bank, animal tracks, the smell of cold water.
SWAMP/MARSH : Footing uncertain. The wrong step goes through. Insects. The horizon is low
              and flat and gives nothing. Distance becomes unreliable here.
```

**Generic waypoints (use when named route not available):**
- Segment 1 of any journey: departure flavor + companion reaction to leaving
- Middle segments: terrain description + one companion banter
- Final segment: destination visible in distance + arrival emotion

---

*KM_World_Systems.md — Kingmaker PF2e Text Adventure | Travel Segment System v1.0*
*Named routes: Restov→Oleg's (Route A). Add new routes below Route A as campaign expands.*


---

<!-- merged from KM_World_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION NEEDS SYSTEM
## KM_World_Systems.md | Referenced by: KM_Kingdom.md, KM_LoadRules.md

> **DM:** Each companion has 4 tracked needs. Needs decay over time. Low needs
> drive the mood states in KM_Kingdom.md. Player can inspect with `.needs
> [name]`. This is the diagnostic layer that tells the player WHY a companion
> is Troubled or Withdrawn.
>
> **Active every session.** Runs passively — DM decrements needs on triggers
> and checks thresholds at Long Rest. Never tells the player numerically;
> surfaces as flavor in moods and ambient lines.

---

## 🧩 THE FOUR NEEDS

| Need | What It Is | Filled By | Drops When |
|------|------------|-----------|------------|
| **REST** | Physical/emotional recovery | Long Rest, camp downtime, Host Gathering | Forced marches, back-to-back combats, no camp action |
| **PURPOSE** | Contribution, relevance | Being picked for scenes, combat kills, quest progress, orders | Benched for chapters, no lines spoken, sidelined |
| **CONNECTION** | Bonds with party + player | Player addressing them, banter firing, camp social scenes | Player ignoring them, no companion-companion banter |
| **RECOGNITION** | Credit for what they did | Player acknowledging their action, title grants, NPC mentions | Player takes credit, DM narrates their kill as player's |

---

## 📊 SCORING

**Each need:** scale 0–10. Starts at 7 when companion joins the party.

**Decay rates (checked at Long Rest unless noted):**
- **REST:** −1 per combat encounter since last Long Rest (cap −3/rest).
  Falls faster in Kingdom campaign arcs (−2 per kingdom turn if still adventuring).
- **PURPOSE:** −1 per scene they were present but had zero lines/actions.
  −2 if they were benched (not in active party) for a full scene.
- **CONNECTION:** −1 per scene player did not address them or an ally directly.
  −2 if player addressed every OTHER companion in the scene but not them.
- **RECOGNITION:** −1 per significant action they took that DM did not surface
  in narration (kill stolen, insight ignored, skill save uncredited).

**Refills (add at trigger):**
- **REST:** +3 per Long Rest at safe camp; +2 in dangerous terrain.
  +2 per Host Gathering; +1 per fun downtime activity (kingdom party, etc.).
- **PURPOSE:** +1 per kill they landed; +2 per quest step advanced with them
  present; +3 per Standing Order role they currently hold.
- **CONNECTION:** +1 per direct player address; +2 per camp social scene
  (1-on-1 talk); +3 per romance beat (if romanced).
- **RECOGNITION:** +1 per DM narration of their action; +2 per title grant;
  +3 per public scene where their action was pivotal (NPC mentions it).

**Hard cap:** 10 per need. Excess refill is wasted — cannot bank.

---

## 🚨 THRESHOLDS & MOOD TRIGGERS

When a need drops, the companion's mood shifts per KM_Kingdom.md:

| Score | Status | Auto-Mood Effect |
|-------|--------|-----------------|
| 7–10 | Satisfied | Default cheerful mood / normal banter |
| 5–6 | Unsettled | Companion sighs, short responses, "fine" when asked |
| 3–4 | Troubled | Mood state Troubled, visible in ambient dialogue |
| 1–2 | Withdrawn | Mood state Withdrawn, pulls away from group scenes |
| 0 | Crisis | Fires Fracture Scene at next Long Rest (see KM_Kingdom.md) |

**Cross-need escalation:** If any TWO needs drop to ≤3, companion enters
Troubled immediately regardless of individual scores. If any THREE drop
to ≤3, companion enters Withdrawn. All four ≤2 = Crisis (Fracture Scene).

**Which need is lowest matters — specific mood flavor:**
- **REST lowest** → Exhausted flavor ("I need to sit down, I need to stop")
- **PURPOSE lowest** → Restless flavor ("Why am I even here?")
- **CONNECTION lowest** → Lonely flavor ("Does anyone here know my name?")
- **RECOGNITION lowest** → Resentful flavor ("I killed that. Not you.")

---

## 🔍 THE `.needs` COMMAND

**Player types:** `.needs [name]` or `.needs` (all active companions)

**DM displays (plain language, not raw numbers):**

```
AMIRI — Current State
  Rest: Satisfied (well-rested)
  Purpose: Strained (her last kill was 3 combats ago)
  Connection: Strong (she's banter-active with Valerie)
  Recognition: Fragile (her giant-kill last session was narrated as "the party's")
  
  Overall: Troubled. She wants her next fight. Give her the front line next combat.
  Suggested action: Address her directly about the last giant.
```

**Show state in 4 words:** Strong / Satisfied / Fragile / Strained / Crisis.
Never print numbers unless player types `.needs [name] raw` (debug mode).

**If `.needs` with no name:** list all active-party companions with their
WORST need (one line each):

```
.needs
AMIRI — Purpose Strained
VALERIE — Connection Fragile
LINZI — All satisfied
TRISTIAN — Rest Strained
OCTAVIA — Recognition Strained
```

---

## 🧭 SUGGESTED ACTIONS (DM surfaces when player uses .needs)

For each low need, the DM offers one or two concrete in-game actions the
player can take to refill it:

**REST low →**
- Call a Long Rest (if safe)
- Host a Gathering in the capital (D14 action)
- Delegate their current assignment, let them rest a kingdom turn

**PURPOSE low →**
- Put them in next combat's active party
- Assign a Standing Order role (.orders)
- Send them to handle a quest step that matches their skills

**CONNECTION low →**
- Spend quiet time together at camp
- Ask them about themselves (any direct question)
- Pair them with a compatible companion for a scene

**RECOGNITION low →**
- Next time they do something, narrate it by name in retrospect
- Grant them a title (see KM_Companions_Titles.md)
- Have an NPC praise their specific action

---

## 💾 SAVE BLOCK FORMAT

Add to each companion entry:

```json
"companions": [
  {
    "name": "Amiri",
    "needs": {
      "rest": 6,
      "purpose": 3,
      "connection": 7,
      "recognition": 4,
      "lowest_need": "purpose",
      "mood_state": "troubled",
      "last_check": "session_7_day_12"
    }
  }
]
```

**Auto-write rules:**
- Update after each Long Rest (decay + refill)
- Update after each significant companion action (refill)
- Write `lowest_need` as the single lowest value's name
- Write `mood_state` based on threshold table above
- Write `last_check` as current session + in-game day

---

## 🔗 INTEGRATION WITH EXISTING SYSTEMS

**KM_Kingdom.md moods:** Needs drive moods; moods surface as ambient
dialogue and menu prompts ("Ask [Name] what's wrong"). This file is the
CAUSE, LivingWorld is the EFFECT.

**KM_Companions_Behaviors.md:** If a companion's agenda conflicts with the
party's current path, PURPOSE decays faster (−2 instead of −1 per scene).

**KM_Romance.md:** Romanced companions have CONNECTION at 10 cap by default;
drops only if romance stage stalls. Physical intimacy scenes refill by +3.

**KM_Mythic_Systems.md:** Devoted (+2 relationship) companions resist one need
drop per rest; Hostile (−2) decay at 2× rate.

**KM_War_Systems.md:** Assigned Standing Order role keeps PURPOSE ≥6
automatically while the role is held.

---

## 📋 DM DISPLAY CHECKLIST

When running `.needs`:
1. Read each active companion's need scores from save block
2. Identify lowest need per companion
3. Translate number → word per threshold table
4. Display in clean table (never raw numbers unless `raw` suffix)
5. Suggest 1–2 concrete actions tied to the lowest need
6. End with prompt: "Address any of these, or continue with the scene?"

When a companion enters a new mood state (crossing threshold):
1. Fire a subtle ambient line that hints at the lowest need
2. Add "Ask [Name] about it" to the next choice menu
3. Do NOT announce the mood change directly — let the player notice

---

## 📋 DM NOTES

**Never gamify in player-facing language.** Do not say "Amiri's Purpose is
at 3." Say "She's edgy — she hasn't killed anything in three fights."

**Refills happen automatically.** Player doesn't need to track this. They
just act in a way that addresses the need, and the DM refills silently.

**Starting values for new companions:** All needs start at 7 when joining.
Quest-locked companions who join mid-chapter start at 5 (they're already
worn from their quest).

**Kingdom turn decay:** When party is on extended kingdom-management arcs
(no combat for 4+ in-game days), PURPOSE drops −1 per in-game day. This
is the system that causes sidelined martials to get restless.

**No fabrication.** Don't invent new needs. Don't give specific companions
"special" needs beyond these 4. The 4 are complete.

---

*KM_World_Systems.md — Kingmaker PF2e Text Adventure v1.0*
*Inspired by The Sims needs system, tuned for narrative text adventure*
