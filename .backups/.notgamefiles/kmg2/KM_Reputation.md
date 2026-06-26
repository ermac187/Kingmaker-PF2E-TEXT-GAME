# KINGMAKER — REPUTATION & NOTORIETY SYSTEM: THE PEOPLE'S VERDICT
## KM_Reputation.md | Active from: Chapter 1 | Referenced by: KM_Kingdom.md, KM_Exploration.md, KM_Commands.md
### Load whenever the player enters a settlement, interacts with civilians, or receives a reaction from civilians.

> **DM:** This system tracks civilian perception of the player. It uses the `public_reputation` integer (−100 to +100) from KM_P2.txt as its source score. The stages below map to that score. **KM_P2.txt is authoritative for the score and deed log.** This file is authoritative for civilian behavioral reactions at each tier.
>
> **What this system governs:** Anonymous reactions from unnamed civilians. Shopkeepers, tavern patrons, road workers, farmers, city guards who don't know the player personally, travelers, refugees. Basically: everyone who isn't on a named NPC card.
>
> **What this system does NOT govern:** Named NPC relationships (use individual NPC scores). Faction standing (use faction tables in KM_Kingdom.md). Army morale (separate track).

---

## 👁️ REPUTATION SCALE — THE PEOPLE'S VERDICT

```
Stage 5 — BELOVED       : public_reputation +76 to +100
Stage 4 — RESPECTED     : public_reputation +51 to +75
Stage 3 — KNOWN         : public_reputation +26 to +50
Stage 2 — FAVORABLE     : public_reputation +1 to +25
Stage 0 — UNKNOWN       : public_reputation 0
Stage −1 — CAUTIOUS     : public_reputation −1 to −25
Stage −2 — WARY         : public_reputation −26 to −50
Stage −3 — FEARED       : public_reputation −51 to −75
Stage −4 — NOTORIOUS    : public_reputation −76 to −100
```

**Track in JSON Save Block under:** `public_reputation` (integer) and `reputation_deeds[]` — both defined in KM_P2.txt. This file reads from that score.

> **SCOPE:** Reputation scores are tracked per region/settlement-type, not universally. Behavior in the Stolen Lands is not instantly known in Brevoy. Build a modular reputation — each region stores its own score, modified by how fast word travels.

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

*KM_Reputation.md — Kingmaker PF2e Text Adventure | Reputation System v2.0*
*Systems: Civilian Reputation (5-stage), Regional Propagation, Faction Reward Tiers*
