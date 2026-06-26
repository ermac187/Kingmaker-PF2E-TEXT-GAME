# KINGMAKER — SWORD BROTHERHOOD SYSTEM: THE IRON COMPACT
## KM_Brotherhood.md | Active from: Chapter 1 | Referenced by: KM_Companions.md, KM_Actions.md
### Load alongside KM_Companions.md whenever a Brotherhood-eligible companion is in party.

> **DM:** The Sword Brotherhood is a separate track from Companion Relationship. It governs a bond of martial trust and sacrifice between the player and eligible male companions. It earns combat abilities — not emotional approval. A Brotherhood companion at Stage 5 will die for you, take wounds for you, and fight in perfect synchrony with you. They will not necessarily like you, though most do by that point.
>
> **Brotherhood-eligible companions — Original:** Regongar, Harrim, Nok-Nok, Ekundayo, Tristian (Tristian is eligible for both systems — Brotherhood governs combat trust; Romance governs the rest).
>
> **Brotherhood-eligible companions — Wrath:** Lann, Regill.
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
| Lann | Fight beside him without giving orders. Acknowledge what the tunnels cost him. Never treat his ancestry as something to overlook. |
| Regill | Follow a rule he's set without arguing. Match his precision in the field. Acknowledge when he was right. |

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
| Lann | *"I spent years in the dark convincing myself I didn't need anyone to see me. Why does it matter that you do?"* |
| Regill | *"I follow the law because it is correct. You follow it when you choose to. I want to understand how that works."* |

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
| Lann | *"I came up from underground alone. I'm not going back down. If you go — I go with you. That's not noble. That's just how it is now."* |
| Regill | *"I have assessed the situation. The correct action, by any regulation I know, is to ensure you survive. I intend to follow the correct action. Always."* |

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

*KM_Brotherhood.md — Kingmaker PF2e Text Adventure | Sword Brotherhood System v1.0*
*Design: The Iron Compact — Five Stages, Combat Synergies, Resurrection Sacrifice*
