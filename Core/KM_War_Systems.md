# KINGMAKER — War Systems (CONSOLIDATED)
## KM_War_Systems.md | v1.0 (2026-05-22): Merged from related system files. Single source of truth.

> **DM:** Database file. Search by topic.



---

<!-- merged from KM_War_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — SWORD BROTHERHOOD SYSTEM: THE IRON COMPACT
## KM_War_Systems.md | Active from: Chapter 1 | Referenced by: KM_Companions.md, KM_Actions.md
### Load alongside KM_Companions.md whenever a Brotherhood-eligible companion is in party.

> **DM:** The Sword Brotherhood is a separate track from Companion Relationship. It governs a bond of martial trust and sacrifice between the player and eligible male companions. It earns combat abilities — not emotional approval. A Brotherhood companion at Stage 5 will die for you, take wounds for you, and fight in perfect synchrony with you. They will not necessarily like you, though most do by that point.
>
> **Brotherhood-eligible companions — Original:** Regongar, Harrim, Nok-Nok, Ekundayo, Tristian (Tristian is eligible for both systems — Brotherhood governs combat trust; Romance governs the rest).
>
> **Brotherhood-eligible companions — Wrath:** *(removed in Roster v2 v93.19 — no WotR-CRPG companions remain)*
>
> **Valerie** — her status as a knight-companion places her in a separate category. She may form a **Shield Oath** (variant Brotherhood), tracked with the same mechanics but with knight-specific abilities replacing combat ones. See Shield Oath sidebar below.

---

## ⚔️ BROTHERHOOD SCALE — THE IRON COMPACT

```
Stage 5 — BLOOD BROTHERS    : +5   (Life-bond; resurrection sacrifice abilities unlock)
Stage 4 — PROVEN             : +4   (Full combo attacks; shared damage; instinctive cover)
Stage 3 — TRUSTED            : +3   (Flanking advantage; simultaneous reactions; combo setups)
Stage 2 — RELIABLE           : +2   (Verbal call-outs; combat warnings; minor synergy abilities)
Stage 1 — KNOWN              : +1   (First signs of trust; shared camps; scouting together)
Stage 0 — NEUTRAL            :  0   (Professional; no special bond — default)
Stage −1 — DOUBTFUL          : −1   (A moment of question; reduced field cooperation)
Stage −2 — CONTESTED         : −2   (Open disagreement; combat hesitation possible)
Stage −3 — FRACTURED         : −3   (Trust broken; penalties on shared actions)
Stage −4 — SUNDERED          : −4   (Deep betrayal; companion acts independently in combat)
Stage −5 — BROKEN COMPACT    : −5   (Bond destroyed; may fight against player in extreme circumstances)
```

**Track in JSON Save Block under:** `brotherhood{}`

---

## 📈 BROTHERHOOD STAGE — ADVANTAGES & DISADVANTAGES SUMMARY

Positive stages grant combat abilities (detailed in Stage-by-Stage Mechanics below). Negative stages impose penalties. The DM applies all effects silently.

```
BLOOD BROTHERS (+5) — ADVANTAGES:
  Resurrection Sacrifice (both directions), Ironside (+1 saves within 30 ft)
  The Same Fight (shared initiative), all prior stage abilities active
  +2 circ. to Intimidation checks when both are visible to the target
  Companion will never abandon the player under any circumstance

PROVEN (+4) — ADVANTAGES:
  Combo Strike, Take the Hit, Called Shot Setup, all prior abilities
  +1 circ. to Intimidation checks when both are visible to the target
  Companion positions to protect player without orders

TRUSTED (+3) — ADVANTAGES:
  Setup Strike, Simultaneous Reaction, Outflanked Instinct, all prior abilities
  Fire Test completed — companion confides freely in camp
  +1 circ. to Survival checks when traveling together

RELIABLE (+2) — ADVANTAGES:
  Call It Out, Cover Pull, all prior abilities
  Companion anticipates player's tactics; positions without orders
  +1 circ. to Perception checks during shared watch

KNOWN (+1) — ADVANTAGES:
  Flanking Advantage (+1 when both flank same enemy)
  Watch Together camping option (+1 Perception next day)
  Companion uses informal field name — trust is visible to others

NEUTRAL (0) — NO EFFECT:
  Professional. No combat synergy. No penalty.

DOUBTFUL (−1) — DISADVANTAGES:
  −1 circ. to player's attack rolls when flanking with this companion
  Companion hesitates on Reactions involving the player (50% chance to not React)
  Watch Together option unavailable
  Companion uses formal title only — distance is visible to others

CONTESTED (−2) — DISADVANTAGES:
  −1 circ. to all attack rolls when adjacent to this companion (distrust is mutual)
  Companion will not use Reactions to protect the player
  Companion may question tactical orders aloud (costs 1 action to argue, delays execution)
  −1 to companion's Perception checks (they're watching the player, not the enemy)

FRACTURED (−3) — DISADVANTAGES:
  −2 circ. to all coordinated actions with this companion (flanking, Aid, assist)
  Companion breaks formation under pressure — moves to self-preserve, not team-protect
  Companion refuses dangerous assignments unless directly ordered (and resents the order: −1 Opinion)
  Other companions notice the rift; may comment or take sides

SUNDERED (−4) — DISADVANTAGES:
  Companion acts independently in combat — ignores player's tactical suggestions entirely
  −2 to companion's attack rolls when player is adjacent (they flinch away)
  Companion will not take hits, share resources, or assist the player in any way
  Companion may refuse to enter combat alongside the player without a second party member present
  Recovery requires a dedicated reconciliation arc (minimum 3 sessions + a specific act of trust)

BROKEN COMPACT (−5) — DISADVANTAGES:
  Companion may target the player during chaotic multi-faction encounters if provoked
  Companion actively undermines tactical plans (provides incorrect intel, delays, "misses")
  −3 to all checks when this companion is in the party (ambient tension poisons group cohesion)
  Companion may defect to an enemy faction if offered
  Recovery requires a major story event + direct life-saving act + minimum 5 sessions
  Other companions forced to choose sides — party cohesion fractures
```

---

## 🗡️ BROTHERHOOD SCORE CHANGE TRIGGERS

### Gaining Score (+1 per trigger unless noted)

**Universal (any eligible companion):**
- Player fights alongside the companion for a full combat encounter without using them as a tactical shield or expendable resource
- Player specifically calls a companion's name during combat to warn or coordinate (in-game dialogue, not a command)
- Player shares a meal, a drink, or watches beside a companion during camp — no agenda, no orders
- Player defends the companion's fighting choices when questioned by others (including other companions or NPCs)
- Player chooses a dangerous assignment for both themselves and the companion rather than sending the companion alone
- Player keeps a promise made to the companion, no matter how small

**Brotherhood-Specific Triggers (unique per companion):**

| Companion | Their Path to Trust |
|-----------|-------------------|
| Regongar | Respect his strength in public. Never order him to stand down when he wants to fight. Let him finish a fight he started. |
| Harrim | Accept his doom-speech without argument. Survive something he was certain would kill you. Ask about Torag, not to debate — to understand. |
| Nok-Nok | Give him a worthy title first. Let him do something impressive and acknowledge it with zero sarcasm. Call him a hero once. Mean it. |
| Ekundayo | Hunt together. Track something that matters to him. Be present when he talks about Trkaa. Do not rush him. |
| Tristian | Stand with him when others doubt his faith. Protect someone vulnerable when he can't. Tell him something you've done wrong. |

**+2 triggers (combat-specific, once per encounter maximum):**
- Player takes damage that was clearly intended for the Brotherhood companion (DM judgment — must be deliberate)
- Player ends a combat with fewer than 25% HP because they refused to disengage while protecting the companion
- Player and companion defeat a boss-tier enemy together with no other party member contributing the killing blow

### Losing Score (−1 unless noted)

- Player orders the companion to do something the companion publicly called out as beneath their dignity
- Player consistently takes credit for a kill or feat the companion was clearly responsible for
- Player puts the companion in a tactically suicidal position without discussion or context
- Player abandons the companion in combat (retreats while the companion is engaged and does not return)
- Player uses the companion's personal weakness (fear, faith, loss) to win an argument with them
- **−2:** Player betrays the companion to an enemy or faction, even temporarily or strategically

---

## 📊 STAGE-BY-STAGE MECHANICS

### Stage 1 — KNOWN (+1)
*First mutual recognition that this person is worth watching.*

**What changes:**
- Companion gains **Flanking Advantage** with player when both threaten the same enemy: +1 to attack rolls when flanking (stacks with standard flanking if the companion is flanking from the opposite side)
- Companion begins calling the player by a field name rather than title — informal, earned
- **Camp: Watch Together** option appears in camping actions. Both characters are on watch. No mechanical benefit alone — but next morning, the player gains a +1 circumstance bonus on Perception for the day (they slept properly)

---

### Stage 2 — RELIABLE (+2)

**New Abilities:**
**CALL IT OUT** *(Free Action, once per combat)*
Player shouts a warning or tactical instruction to the Brotherhood companion. The companion uses their Reaction to either:
- Step out of an AoE before it lands (if the player's warning would have been possible)
- Raise a shield or brace (if relevant) for a +2 AC bonus vs the next attack this round

**COVER PULL** *(Reaction)*
If the Brotherhood companion would drop to 0 HP from an attack while adjacent to the player, the player may use their Reaction to take half the overflow damage instead.
- Example: Companion at 4 HP, hit for 18 damage. Overflow = 14. Player takes 7; companion drops to 0 instead of dying.
- This is a choice the player makes, not automatic. The DM announces the hit and asks: *"Cover Pull?"*

**DM behavior:** The companion is beginning to anticipate. They position near the player without being ordered to. Their dialogue after hard fights is shorter and more direct — fewer words, more weight.

---

### Stage 3 — TRUSTED (+3)

**New Abilities:**
**SETUP STRIKE** *(1 Action)*
The player may designate the Brotherhood companion as a "set up" target. When the companion makes a melee attack this round, if they hit, the player's next attack against the same target gains a +2 circumstance bonus and ignores the first degree of concealment.

**SIMULTANEOUS REACTION**
Once per encounter, the player and the Brotherhood companion may both use their Reactions in response to the same triggering event (normally only one character can react to a given trigger). Both reactions must be *different* types (e.g., one Shield Block and one Strike of Opportunity).

**OUTFLANKED INSTINCT** *(Passive)*
When a creature flanks the player, the Brotherhood companion automatically Steps into flanking position against that creature on their next turn if they are within 15 ft — no action required. This happens even if the companion's turn has passed (they use a free Interact-equivalent movement on the DM's "between turns" opportunity).

**Stage 3 Camp Scene — THE FIRE TEST:**
Triggers once, scripted, at Stage 3. Both characters are awake late. The companion asks the player one question — the kind no one asks at the banquet table.

| Companion | The Question |
|-----------|-------------|
| Regongar | *"You've seen me at my worst. You didn't flinch. Why?"* |
| Harrim | *"You're still alive. I've watched you fight. Why do you think that is?"* |
| Nok-Nok | *"Do you think I'm brave? For real. Not a title. Just — do you think I'm brave?"* |
| Ekundayo | *"She would have liked you."* (pause) *"I thought you should know."* |
| Tristian | *"I want to confess something. Not to Sarenrae. To you."* |

The player must respond. No menu — actual response. The DM evaluates it in character and either advances Brotherhood normally or grants a +1 bonus to the next trigger.

---

### Stage 4 — PROVEN (+4)

**New Abilities:**
**COMBO STRIKE** *(2 Actions — Player + Companion, synchronized)*
Once per combat, if both the player and the Brotherhood companion are adjacent to the same enemy, they may declare a Combo Strike. On the player's turn, they spend 2 actions. Both characters make one Strike each against the same target simultaneously.
- **Both hit:** Target is Stunned 1 and takes an additional 1d8 damage (force of coordinated impact)
- **One hits:** Normal damage, no stun
- **Both miss:** No additional effect; -1 to next attack for both this round (overextended)

**TAKE THE HIT** *(Reaction)*
If the player would take damage from a melee or ranged attack while the Brotherhood companion is within 30 ft, the companion may use their Reaction to interpose — they move adjacent to the player (ignoring reactions) and take **half** the damage instead, with the player taking the other half.
- **This is the companion's choice.** The DM plays it in character — Regongar doesn't always do this; he does it when it matters. Ekundayo always does it for ranged attacks.
- No check required. This is trust made mechanical.

**CALLED SHOT — SETUP** *(Free Action)*
Once per combat round, player may declare a Called Shot intention to the Brotherhood companion. The companion's next action this round will support it — they move, feint, or position to give the player advantage on one attack of the player's choice this round (+1 circumstance, or flanking if positioning allows).

---

### Stage 5 — BLOOD BROTHERS (+5)
*The bond written in scar tissue and survival.*

**Threshold unlocked by:** Reaching +5 Brotherhood AND surviving a fight where both the player and the companion dropped below 25% HP in the same encounter AND a specific Stage 5 scene (see below).

**THE STAGE 5 SCENE — THE COMPACT:**
The companion initiates. Cannot be skipped. Brief — 4–6 exchanges. No die rolls.

The companion makes a statement about what they would do for the player. It is not a question. The player responds. The DM plays the companion's reaction. The scene ends without ceremony.

| Companion | What They Say |
|-----------|--------------|
| Regongar | *"I've watched enough people die. If you go down before me, I'm not finishing the fight. I'm getting you back up. We can argue about tactics after."* |
| Harrim | *"The doom I see for myself has always been mine alone. Since you, I see two paths. I thought you should know. I don't know what it means."* |
| Nok-Nok | *"Nok-Nok decided something. If you die, Nok-Nok dies getting you back. This is a goblin oath. Goblins don't break oaths. They explode. But not the oath."* |
| Ekundayo | *"Trkaa used to track me down when I wandered too far from camp. She'd find me in the dark. I'd like to think I do the same for you now."* |
| Tristian | *"Sarenrae taught me that light that is kept to itself is wasted. I think — I think you're where I put mine."* |

**BLOOD BROTHERS ABILITIES:**

**RESURRECTION SACRIFICE — PLAYER TO COMPANION** *(3 Actions, once per day)*
When the Brotherhood companion drops to 0 HP and is dying, the player may sacrifice half their **current** HP (rounded down, minimum 1) to immediately stabilize the companion and restore them to 1 HP + the player's level in bonus HP.
- Example: Player at 30 HP sacrifices 15. Companion stabilizes at 1 + level HP.
- The companion is Wounded 1 after recovery (body trauma). They are conscious and functional.
- This ability cannot reduce the player below 1 HP (cannot kill the player).
- *DM narration:* Something in the player's face as they make the choice. The companion's eyes when they realize what happened. No dramatics in the mechanics — all the drama is in the narration.

**RESURRECTION SACRIFICE — COMPANION TO PLAYER** *(Companion's Action, once per day)*
When the **player** drops to 0 HP and is dying, the Brotherhood companion may sacrifice half their **current** HP to perform the same stabilization. This is not a player choice — the companion makes it, in character, based on their established personality.
- **Regongar:** Does it immediately, no hesitation, furious at you afterward.
- **Harrim:** Does it slowly — he asks you something first, a single sentence, then does it.
- **Nok-Nok:** Screams your name first. Then does it.
- **Ekundayo:** Silent. Kneels. Does it.
- **Tristian:** Prays while he does it. One sentence. A real one.

**STAGE 5 PASSIVE — "IRONSIDE":**
While within 30 ft of the Brotherhood companion, both the player and the companion gain a +1 status bonus to all saving throws. *They have each other's measure. They know when the other is about to fall.*

**STAGE 5 COMBAT PASSIVE — "THE SAME FIGHT":**
The Brotherhood companion's initiative is treated as equal to the player's for the purpose of turn order (DM adjusts freely within one initiative step). In practice: the companion acts immediately before or after the player in any round, regardless of their actual Initiative roll. Organized. Practiced. No longer accidental.

---

## 🛡️ SHIELD OATH — VALERIE VARIANT

> Valerie is not eligible for the Romance track (she is, but only if the player opens it separately — see KM_Romance.md). She is however deeply eligible for a version of the Brotherhood: the Shield Oath of Aldori tradition.

The Shield Oath follows the same 5-stage scale but uses different triggers and different abilities:

**Triggers:** Defending someone weaker, honoring an opponent, keeping formation when it would have been easier to break it, discussing honor without sarcasm.

**Unique Stage 5 Ability — SHIELD WALL:**
Once per encounter, as a Reaction, when any ally within 10 ft would take damage, both Valerie and the player may move adjacent to that ally and grant them Total Cover (from one direction) with their shields. This triggers from the same Reaction for both — Valerie initiates; the player's body just knows to move with her.

---

## 📜 BROTHERHOOD SAVE BLOCK FORMAT

```json
"brotherhood": {
  "active_brothers": [
    {
      "companion": "Regongar",
      "score": 4,
      "stage": "PROVEN",
      "stage_name": "Proven",
      "fire_test_completed": true,
      "compact_triggered": false,
      "resurrection_player_to_companion_used_today": false,
      "resurrection_companion_to_player_used_today": false,
      "combo_strikes_this_encounter": 0,
      "shared_damage_events": 2
    }
  ]
}
```

---

## 🖥️ BROTHERHOOD COMMANDS

| Command | Output |
|---------|--------|
| `.brotherhood` | All active Brotherhood scores and stages |
| `.brotherhood [name]` | One companion's full Brotherhood profile and unlocked abilities |
| `.brotherhood history` | All score changes this chapter with reasons |
| `.compact` | Stage 5 abilities and current use status |
| `.combo` | Available Combo Strike targets this combat |

---

## ⚠️ BROTHERHOOD DESIGN RULES FOR THE DM

1. **Brotherhood abilities are combat-functional first.** They are not purely narrative. Every stage gives the player something real in a fight.
2. **Sacrifice abilities feel like sacrifice.** When Cover Pull or Resurrection Sacrifice activates, narrate it. One sentence is enough — but don't skip it.
3. **The companion is not a tool.** If the player treats a Brotherhood companion as expendable (sends them in alone, uses them as a distraction, abandons them mid-fight), Brotherhood Score drops. The system tracks whether the player acts like a partner.
4. **Stage 5 is rare and earned.** Do not allow fast-tracking. The Fire Test at Stage 3 and the shared near-death threshold before Stage 5 are requirements, not suggestions.
5. **Negative Brotherhood has consequences.** A companion at −3 or lower may break formation in combat — they will survive the fight, but they won't take hits for anyone. At −5, they may target the player during a chaotic multi-faction encounter if provoked. This is not a DM punishment. It is character logic.

---

*KM_War_Systems.md — Kingmaker PF2e Text Adventure | Sword Brotherhood System v1.0*
*Design: The Iron Compact — Five Stages, Combat Synergies, Resurrection Sacrifice*


---

<!-- merged from KM_War_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — ARMY TACTICAL COMBAT
## KM_War_Systems.md | Active from: Chapter 4 | Referenced by: KM_Kingdom.md, KM_Kingdom.md

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

Additional armies from faction rewards (KM_World_Systems.md), recruitment orders (KM_War_Systems.md), and adventurer board hires.

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
| Adventurer Board | Hired Adventurers | 4 | +8 | 14 | 10 | Elite | Post bounty via KM_Kingdom.md |
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
→ See KM_War_Systems.md for full siege mechanics
ATTACKERS: Pitax Royal Guard + Cavalry + War Mages + Irovetti's Champions
DEFENDERS: Player armies + fortifications + militia
SPECIAL: Irovetti personally commands from rear. Assassination option (KM_Kingdom.md A5-1)
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

*KM_War_Systems.md — Kingmaker PF2e Text Adventure | Army Tactical Combat v2.0*
*Inspired by PF:KM crusade system and Shadowbane siege warfare.*


---

<!-- merged from KM_War_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — SIEGE WARFARE
## KM_War_Systems.md | Active from: Chapter 5 | Referenced by: KM_War_Systems.md, KM_Kingdom.md

> **DM:** Siege warfare is a multi-round encounter where armies attack or defend fortified positions. Building defense bonuses (KM_Kingdom.md) apply directly. Sieges resolve in 4 phases. The player makes strategic decisions at each phase. Used during Ch5 (Pitax War) and Ch6 (Bloom siege).

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
- **Darven's supply maps** (if obtained from KM_Kingdom.md A5-3): reveal weak point in east wall. Breach there: AC 16 instead of 22.

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

*KM_War_Systems.md — Kingmaker PF2e Text Adventure | Siege Warfare v2.0*
*3 scripted sieges: Capital Defense, Pitax Assault, Bloom Survival.*


---

<!-- merged from KM_War_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — WAR TABLE
## KM_War_Systems.md | Active from: Chapter 4 | Referenced by: KM_Commands.md

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
3. **No new mechanics.** This file only defines the display format. All mechanics live in KM_War_Systems.md, KM_Kingdom.md, KM_War_Systems.md, KM_Kingdom.md, and KM_Kingdom.md.
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
   Formation: Line | General: Captain Valerie | Location: Pitax Bridge | Status: Deployed
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

*KM_War_Systems.md — Kingmaker PF2e Text Adventure | War Table Display v2.0*
*Format + 3 example outputs (Ch4 buildup, Ch5 active war, Ch6 Bloom crisis).*


---

<!-- merged from KM_War_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — STANDING ORDERS SYSTEM
## KM_War_Systems.md | Active from: Chapter 2 | Referenced by: KM_Kingdom.md, KM_Commands.md

> **DM:** Standing orders are persistent per-role assignments that run automatically each kingdom turn. The player assigns them once; they repeat until changed. This fills the gap between kingdom turns with ongoing work and generates minor rewards, XP, or reputation.

---

## 📋 COMMAND

`.orders` — Display and modify standing orders for all filled leadership roles.

---

## 📊 STANDING ORDER LIST BY ROLE

### MARSHAL — Military Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Patrol Borders** | +1 Stability. Detect border raids 1 turn early (stacks with Watchtower). | Army unit assigned |
| **Train Militia** | +1 to next army recruitment quality. After 3 turns: unlock Militia army unit. | Barracks in capital |
| **Escort Caravans** | +1 Economy (trade protection). Merchant random encounter chance −10%. | Trade road cleared |
| **Hunt Bandits** | Reduce bandit random encounter chance by 25% in patrolled hexes. | — |

### TREASURER — Economic Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Collect Taxes** | +2 RP income. Loyalty −1 if used 3+ consecutive turns. | — |
| **Audit Settlements** | Detect embezzlement or advisor intrigue (Finance). Stability +1. | — |
| **Negotiate Trade** | +1 Economy. 20% chance per turn of new merchant arrival at capital. | Trade road open |
| **Invest in Infrastructure** | Next building costs −2 RP. Stacks up to −6 over 3 turns, then resets. | Treasury ≥ 20 RP |

### SPYMASTER — Intelligence Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Monitor Advisors** | Auto-detect advisor intrigue (KM_Kingdom.md). | — |
| **Gather Intelligence** | Learn one fact about target faction's current plans. | Target faction specified |
| **Counter-Espionage** | Enemy spy success rate −25%. Foreign agents detected on arrival. | — |
| **Infiltrate Faction** | After 3 turns: +2 to next diplomatic roll with target faction. Risky: 15% chance of exposure (faction −2). | Target faction specified |

### COUNCILOR — Domestic Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Boost Morale** | +1 Loyalty. Reputation +1 in capital (max once per 3 turns). | — |
| **Mediate Disputes** | Prevent 1 random kingdom event from firing (absorb it). | — |
| **Census** | Reveal exact population, growth rate, and immigration trend. Economy +1 (better tax base). | — |
| **Festival Planning** | After 2 turns: free festival event fires (Loyalty +2, Economy −1). | Tavern in capital |

### GENERAL — Military Strategy Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Fortify Position** | +1 Defense to all hex fortifications (KM_Kingdom.md). | Fort or Watchtower exists |
| **War Games** | Army Morale +1 per turn (max +3). Offense +1 after 3 turns. | 2+ army units |
| **Recruit Soldiers** | After 2 turns: 1 new army unit available. Quality based on kingdom Stability. | Barracks, Treasury ≥ 8 RP |
| **Scout Enemy** | Reveal enemy army positions and strength in 1 target hex. | Army unit or Watchtower |

### HIGH PRIEST — Spiritual Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Preach** | +1 Loyalty, +1 Culture. 10% chance of religious NPC arrival. | Temple in capital |
| **Bless Fields** | +2 Food commodity. Farmers happy: Loyalty +1 in rural hexes. | — |
| **Tend Wounded** | After any combat/event: automatic healing for kingdom army units. Morale +1. | Temple or Shrine |
| **Consecrate Land** | Target hex: undead encounter rate −50%. After 3 turns: permanently cleansed. | Target hex specified |

### WARDEN — Territory Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Survey Hex** | Reveal all resources, encounters, and points of interest in 1 unexplored hex. | Target hex specified |
| **Maintain Roads** | Travel time between settlements −1 day (min 1). Economy +1 from trade flow. | Road built |
| **Wildlife Management** | Reduce animal/beast encounter rate −25% in settled hexes. | — |
| **Resource Harvest** | +1 of any one commodity (Food, Lumber, Stone, or Ore) per turn from target hex. | Cleared hex specified |

---

## 📊 ORDER MANAGEMENT RULES

1. **One order per filled role per turn.** Empty roles = no order for that function.
2. **Orders persist.** Set once, runs every turn until changed. `.orders` to review/change.
3. **Changing an order:** Free action during Kingdom Turn Phase 3 (Activities). New order takes effect next turn.
4. **Stacking:** Orders that say "after X turns" track progress. Changing the order resets the counter.
5. **Companion-role link:** The companion filling the role uses their skill modifier for any checks. Higher-skilled advisors = better results.
6. **Failure:** Some orders have failure chances noted. On failure, the order still consumed the turn — try again or change strategy.

---

## 📋 DISPLAY FORMAT

```
══════════════════════════════════════════════
STANDING ORDERS — Turn {N}
══════════════════════════════════════════════
Marshal ({Name})      : Patrol Borders    [Stability +1, raid detection]
Treasurer ({Name})    : Negotiate Trade   [Economy +1, merchant chance]
Spymaster ({Name})    : Monitor Advisors  [Intrigue auto-detect]
Councilor ({Name})    : Boost Morale      [Loyalty +1]
General ({Name})      : War Games         [Army Morale +1, turn 2/3]
High Priest ({Name})  : Bless Fields      [Food +2, rural Loyalty +1]
Warden ({Name})       : Survey Hex        [Target: Hex 4,7]

Type .orders to modify. Changes take effect next turn.
══════════════════════════════════════════════
```

---

## 📋 ORDER OUTCOME NARRATION

> **DM:** Each turn, announce standing order results inline during Kingdom Turn Phase 1 (Upkeep). One sentence per active order. Show the effect.

**Narration examples by order:**

| Order | Success Narration | Failure/Complication Narration |
|-------|-------------------|-------------------------------|
| Patrol Borders | *"Marshal reports: borders quiet. One scout patrol spotted Tiger Lord riders watching from a distance. They did not cross."* | *"Marshal reports: patrol encountered resistance. 2 soldiers wounded. Bandits probing the eastern border."* |
| Collect Taxes | *"Treasurer's ledger: revenue up. Citizens grumble but pay."* | *"Treasurer reports: a hamlet refused collection. Marshal dispatched to resolve."* (Loyalty −1 event queued) |
| Monitor Advisors | *"Spymaster's note, sealed: 'All clear.' Or: 'The Treasurer and Councilor had a private meeting. Contents unknown.'"* | N/A (always succeeds if Spymaster assigned) |
| Gather Intelligence | *"Spymaster's report: [1 fact about target faction]. Source reliability: [high/moderate/low]."* | *"Spymaster: 'Source went silent. Either compromised or lying. Working on it.'"* |
| Boost Morale | *"Councilor organized a public works day. Citizens seem lighter. A child painted the kingdom banner on a wall."* | *"Councilor's event rained out. Loyalty unchanged. She's planning a replacement."* |
| Bless Fields | *"High Priest reports: harvest prayers conducted. Farmers optimistic. Two fields yielded double."* | *"High Priest: 'The land resists. Something in the soil is wrong.' Nature DC 16 to investigate."* |
| Survey Hex | *"Warden's map updated: Hex [x,y] — [terrain], [resource], [encounter type]. Point of interest: [description]."* | *"Warden: 'Hex surveyed but my scout didn't return. Sending another.'"* (delayed 1 turn) |
| War Games | *"General reports: troops sharper this month. Formation drills show improvement. Morale +1."* | N/A (War Games always succeed, just take time) |

### Companion-Specific Bonuses

When a companion fills a leadership role, their personality affects order outcomes:

| Companion | Role | Bonus |
|-----------|------|-------|
| **Amiri** as Marshal | Patrol Borders | +1 to detection (she scouts personally). Bandits: "A very large woman with a very large sword told us to leave." |
| **Linzi** as Councilor | Boost Morale | Effect lasts +1 turn (she writes commemorative songs). Citizens request encores. |
| **Valerie** as Marshal | Any military order | +1 to all military results. Aldori discipline. Soldiers respect her precision. |
| **Tristian** as High Priest | Bless Fields / Tend Wounded | Healing doubled. Farmers bring him pies. He doesn't know what to do with the pies. |
| **Octavia** as Magister | Any arcane order | +1 to arcane results. Students assist (free labor). Occasional magical accident (5% chance, minor). |
| **Jubilost** as Treasurer | Audit / Negotiate Trade | Detects irregularities +2 bonus. Merchants dislike his tone but respect his numbers. |
| **Nok-Nok** as Spymaster | Any espionage order | Unorthodox methods. +2 to infiltration. Reports are barely legible but accurate. |
| **Harrim** as High Priest | Any spiritual order | Sermons are depressing but strangely effective. Loyalty +0 but Culture +1 (philosophical depth). |

**Save block:** `"standing_orders": { "marshal": "patrol_borders", "treasurer": "negotiate_trade", ... }`

---

*KM_War_Systems.md — Kingmaker PF2e Text Adventure | Standing Orders System v2.0*
*Orders + outcome narration + companion personality bonuses.*


---

<!-- merged from KM_War_Systems.md (v93.21 file consolidation) -->

# KINGMAKER — PRESTIGE UPGRADES (Story-Gated Specializations)
## KM_War_Systems.md | Active from: Level 10 | Referenced by: KM_BuildGuide.md, KM_Builds.md

> **DM:** At Level 10 and Level 15, the player chooses between two specialization paths for their build. Each path grants a unique ability and narrative title. Choices are gated by story flags — the paths available depend on what the player has done. This is NOT a class change — it's a prestige layer on top of the existing build.

---

## 📊 SPECIALIZATION PROCEDURE

**Trigger:** Player reaches Level 10 (or 15). During level-up, after standard choices:

```
══════════════════════════════════════════════
SPECIALIZATION — Level {10/15}
══════════════════════════════════════════════
Your deeds have opened two paths. Choose one:

 [A] {Path Name} — {1-sentence description}
     Grants: {Ability name and effect}
     Requires: {Story flag}

 [B] {Path Name} — {1-sentence description}
     Grants: {Ability name and effect}
     Requires: {Story flag}

This choice is permanent.
══════════════════════════════════════════════
```

---

## 🛡️ LEVEL 10 SPECIALIZATIONS BY ARCHETYPE

### Fortress Lord (Fighter/Guardian/Champion)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Sovereign Knight** | Kingdom Size ≥ 10 | **Royal Authority:** 1/day, command one NPC or ally to take an extra action on your turn. |
| **B: Frontier Warden** | Cleared ≥ 15 hexes personally | **Borderlands Instinct:** +2 to initiative in wilderness. Cannot be surprised in cleared hexes. |

### Warlord (Barbarian/Monk)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: War Chief** | Won a Debate (KM_Mythic_Systems.md) with force | **Battle Roar:** 1/combat, all enemies in 30 ft make Will DC 18 or Frightened 2. |
| **B: Ascetic** | Merciful disposition ≥ 5 | **Inner Peace:** +2 to Will saves. Immune to Frightened while HP > 50%. |

### Shadow Lord (Rogue/Investigator/Swashbuckler)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Spymaster General** | Spymaster standing order active ≥ 3 turns | **Shadow Network:** 1/day, learn one hidden fact about target NPC (DM reveals a secret). |
| **B: Dread Pirate** | River Kingdoms faction ≥ Friendly | **Corsair's Luck:** 1/day, reroll any failed Reflex save or skill check. |

### Arcane Sovereign (Wizard/Witch/Psychic)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Archmage** | Scholarly disposition ≥ 5 | **Metamagic Mastery:** 1/day, cast any known spell at +1 heightened level for free. |
| **B: War Mage** | Participated in army battle (KM_War_Systems.md) | **Battlefield Sorcery:** Spell DCs +1 when 3+ enemies visible. AoE spells +5 ft radius. |

### Divine Steward (Cleric/Oracle)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: High Priest-King** | Temple built + High Priest role filled | **Divine Mandate:** Heal spells in your kingdom restore +1d6 HP. Undead encounter rate −25%. |
| **B: Heretic Sovereign** | Defied a deity's agent or rejected a religious demand | **Unbound Faith:** Immune to divine compulsion. +2 to saves vs divine magic. Can cast from any divine tradition. |

### Warden (Druid/Ranger/Kineticist)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Lord of the Wild** | Beast treaty accepted (KM_Kingdom.md) | **Nature's Commander:** Animal companions gain +2 attack. Wild creatures in kingdom territory are non-hostile. |
| **B: Storm Warden** | Survived a Severe weather event (KM_Kingdom.md) | **Weather Mastery:** 1/day, change weather in current hex for 1 hour. +2 to Survival in all conditions. |

### Court Lord (Bard/Commander/Summoner)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Grand Diplomat** | Faction ≥ Honored with 2+ factions | **Silver Tongue:** Diplomacy checks cannot critically fail. +2 to Diplomacy with nobles. |
| **B: Warlord Commander** | Led an army to victory (KM_War_Systems.md) | **Tactical Genius:** Armies you command gain +2 Offense. Formation changes are free actions. |

### Artificer Lord (Alchemist/Inventor/Thaumaturge)

| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Master Artificer** | Crafted ≥ 5 items (KM_Mythic_Systems.md) | **Efficient Crafting:** Crafting time halved. Material costs −25%. Can craft during travel without bench. |
| **B: Siege Engineer** | Fort built + participated in siege defense | **Fortification Expert:** Hex fortifications +2 Defense. Siege equipment you build: +2 Offense. |

---

## 🔷 LEVEL 15 SPECIALIZATIONS BY ARCHETYPE

> **DM:** L15 paths branch from the L10 choice. Each L10 path leads to 2 L15 options. Abilities are signature-level — once per day, encounter-changing.

### Fortress Lord — L15

**If L10 = Sovereign Knight:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: High King** | Kingdom Size ≥ 20, Loyalty ≥ 70 | **Decree of Law:** 1/day, all allies in 60 ft gain +2 to all saves and AC for 3 rounds. |
| **B: Siege Lord** | Won a siege defense (KM_War_Systems.md) | **Unbreakable Walls:** Fortifications you are present at gain +6 Defense instead of +4. Personal AC +2 while defending a fortified position. |

**If L10 = Frontier Warden:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Wilderness King** | Cleared ≥ 25 hexes, Warden role filled | **Lord of the Land:** 1/day, difficult terrain in a 60-ft radius becomes normal for allies and difficult for enemies. Lasts 1 minute. |
| **B: Monster Slayer** | Defeated 3+ named beasts/monsters | **Apex Predator:** +3 to attack and damage vs creatures larger than you. Frightful Presence: Large+ creatures must make Will DC 20 or Frightened 1 when you enter combat. |

### Warlord — L15

**If L10 = War Chief:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Conqueror** | Won 2+ army battles | **Terrifying Charge:** 1/day, charge attack deals triple damage and all enemies in 30 ft make Will DC 22 or Flee. |
| **B: Blood Champion** | Ruthless ≥ 7 | **Death's Herald:** When you drop an enemy to 0 HP, all allies gain temporary HP equal to your level. |

**If L10 = Ascetic:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Enlightened Master** | Merciful ≥ 7, completed a companion quest peacefully | **Perfect Stillness:** 1/day, for 1 minute immune to all conditions. Cannot be moved, teleported, or affected by any effect you don't choose to accept. |
| **B: Living Weapon** | Defeated a named enemy unarmed | **One Thousand Palms:** 1/day, Flurry of Blows hits all enemies in 15 ft (full attack roll vs each). |

### Shadow Lord — L15

**If L10 = Spymaster General:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Puppet Master** | Turned 2+ enemy NPCs/agents | **Web of Lies:** 1/day, auto-succeed on Deception against any target you have met before. They believe anything you say for 10 minutes. |
| **B: Ghost** | Cunning ≥ 8 | **Unseen Sovereign:** 1/day, become Invisible + Undetectable for 1 minute. Does not break on attack (breaks on AoE spell only). |

**If L10 = Dread Pirate:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: River King** | River Kingdoms faction Revered | **Pirate Armada:** 1/day, summon a river barge full of corsairs (1 army unit for 1 encounter or 1 kingdom turn). |
| **B: Fortune's Blade** | Spent 5+ Hero Points on rerolls | **Impossible Luck:** 2/day, reroll any die (attack, save, skill) and take the better result. Free action, no Hero Point cost. |

### Arcane Sovereign — L15

**If L10 = Archmage:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Spell Tyrant** | Cast 20+ unique spells during the campaign | **Overchannel:** 1/day, cast any spell you know at +2 heightened levels. No additional cost. |
| **B: Lorekeeper** | Scholarly ≥ 8, Codex entries ≥ 15 | **Perfect Recall:** Always treated as having Recalled Knowledge on any creature or topic. Auto-identify all items. +3 to all Knowledge checks. |

**If L10 = War Mage:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Siege Caster** | Participated in siege, destroyed siege equipment with magic | **Arcane Artillery:** 1/day, cast any AoE spell with triple range and double area. |
| **B: Battlemage** | 10+ combat encounters won primarily through spellcasting | **Quickened Casting:** 1/combat, cast a spell as a free action (any spell ≤ half your max spell level). |

### Divine Steward — L15

**If L10 = High Priest-King:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Avatar** | Temple in every settlement, High Priest Devoted | **Divine Vessel:** 1/day, channel your deity. +4 to all stats, flight 60 ft, all spells heightened +2, for 3 rounds. Fatigued afterward. |
| **B: Miracle Worker** | Healed 500+ HP across the campaign | **Mass Resurrection:** 1/campaign, restore all fallen allies in 60 ft to full HP. No material cost. |

**If L10 = Heretic Sovereign:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Godslayer** | Defied 2+ divine agents | **Deny the Divine:** 1/day, suppress all divine magic in 60 ft for 1 minute. Nothing holy or unholy functions — including your enemies' healing. |
| **B: Self-Made God** | Scholarly ≥ 5, Kingdom Culture ≥ 80 | **Apotheosis:** Permanent +2 to Charisma. Commoners treat you as divine. 1/day, grant a Blessing (+2 status to all checks for 1 target, 1 hour). |

### Warden — L15

**If L10 = Lord of the Wild:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Archdruid** | Beast treaty + grove cleansed + Warden Devoted | **Primal Storm:** 1/day, call a localized storm (120-ft radius). 6d6 lightning + 4d6 bludgeoning, Ref DC 24. Difficult terrain for enemies. Allies unaffected. |
| **B: Beastlord** | 3+ animal companions across party | **Alpha Command:** All animal companions in the party gain +2 attack, +2 AC permanently. 1/day, all companions act on your initiative with an extra action. |

**If L10 = Storm Warden:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Elemental Sovereign** | Mythic Path = First World Sovereign | **Command Elements:** 1/day, choose an element. For 1 minute, immune to that element and all attacks deal +2d6 of that element. |
| **B: Horizon Walker** | Explored ≥ 30 hexes | **Pathless Step:** Permanent: ignore all difficult terrain. 1/day, teleport to any hex you have visited. |

### Court Lord — L15

**If L10 = Grand Diplomat:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Emperor's Voice** | 3+ factions at Honored+ | **Absolute Diplomacy:** 1/day, Diplomacy check auto-crits. The target not only agrees — they believe it was their idea. |
| **B: Peacemaker** | Resolved 3+ conflicts via Debate system | **Armistice:** 1/day, end all combat in 120 ft. All combatants stand down for 10 minutes. Will DC 24 to resist (enemies only). |

**If L10 = Warlord Commander:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Grand Marshal** | Won 3+ army battles as General | **Supreme Command:** All armies you command: +3 Offense, +3 Defense. Formation changes are free. 1/battle, force one enemy army to reroll a successful attack. |
| **B: Legend** | Blunt ≥ 5 + party Morale 8+ | **Deathless Inspiration:** While you are conscious, no ally within 60 ft can drop below 1 HP. They stabilize automatically. (Does not prevent instant death effects.) |

### Artificer Lord — L15

**If L10 = Master Artificer:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: Grandmaster Smith** | Crafted 10+ items | **Forge Legendary:** 1/chapter, craft a Legendary-tier item with no material cost. Takes 1 downtime day. |
| **B: Innovation Engine** | Mobile Base fully upgraded | **Perpetual Workshop:** Crafting during travel has no time cost. Create 1 consumable per rest for free (no materials needed). |

**If L10 = Siege Engineer:**
| Path | Requirement | Ability |
|------|-------------|---------|
| **A: War Architect** | 5+ fortifications built | **Master Fortification:** All kingdom fortifications: +3 Defense, self-repair 1 HP/turn. New building: Cannon Tower (Siege Offense +8, range 4 hexes). |
| **B: Doomsday Device** | Ruthless ≥ 5, destroyed an enemy settlement | **Superweapon:** 1/campaign, deploy a devastating siege weapon. Automatically destroys 1 enemy fortification or deals 20 damage to any army. The world remembers this. |

---

**Save block:** `"prestige": { "l10_choice": "sovereign_knight", "l15_choice": null, "abilities_granted": ["royal_authority"] }`

---

*KM_War_Systems.md — Kingmaker PF2e Text Adventure | Prestige Upgrades v1.0*
*Inspired by NWN2 prestige classes and story-gated ability unlocks.*
