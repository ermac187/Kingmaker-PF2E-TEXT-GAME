# KINGMAKER — PERSUASION DEBATE SYSTEM
## KM_Debates.md | Referenced by: KM_DMRules.md, KM_Commands_P2.md

> **DM:** When two characters have a fundamental disagreement that cannot be resolved by a single check or player fiat, use the Debate system. This is a structured social contest — best of 3 opposed checks. It replaces "DM decides" with a mechanical resolution that feels earned.

---

## ⚔️ WHEN TO USE DEBATES

**Use a Debate when:**
- Two companions disagree on a course of action and the player wants to settle it fairly
- The player is negotiating with a stubborn NPC who won't yield to a single Diplomacy check
- A kingdom advisor proposes something another advisor opposes (KM_AdvisorEvents.md)
- The player wants to convince a companion to change their mind on a deeply held belief

**Do NOT use a Debate when:**
- A simple skill check would resolve it (use the normal roll)
- The disagreement is trivial or one-sided
- Combat is imminent (switch to Initiative)
- The NPC is mindless, fanatical, or magically compelled (no debate possible)

---

## 📋 DEBATE PROCEDURE

### Step 1 — Frame the Debate
DM announces the debate, the stakes, and the two positions:
```
[DEBATE — {Topic}]
POSITION A: {Character A's stance} — championed by {Name}
POSITION B: {Character B's stance} — championed by {Name}
Stakes: {What happens if A wins / What happens if B wins}
Best of 3 rounds. Each round: opposed skill check.
```

### Step 2 — Three Rounds of Opposed Checks
Each round, both sides choose a social approach:

| Round | Approach Options | Skill Used |
|-------|-----------------|-----------|
| **Round 1 — Opening** | Argue (Diplomacy), Provoke (Intimidation), or Mislead (Deception) | Chosen skill vs. opponent's Will DC |
| **Round 2 — Rebuttal** | Any approach. Cannot repeat Round 1's exact skill. | Same mechanic |
| **Round 3 — Closing** | Any approach. Free choice — repetition allowed. | Same mechanic |

**Resolution per round:**
```
Roll: d20 + [skill mod] vs DC [10 + opponent's Will save bonus]
Success      = Win this round (+1 point)
Crit Success = Win this round (+2 points) — devastating argument
Failure      = Lose this round (opponent +1 point)
Crit Failure = Lose badly (opponent +2 points) — humiliating concession
```

### Step 3 — Determine Winner
- **First to 3 points wins.** (Can end early on Round 2 if someone scores crit success both rounds.)
- **Tie after 3 rounds:** Deadlock. Neither side concedes. DM presents compromise or player makes final call (relationship consequence for the loser).

### Step 4 — Consequences

| Outcome | Effect |
|---------|--------|
| **Player wins** | NPC/companion yields on the specific issue. No relationship penalty for graceful loss. +1 Cunning or Blunt disposition (DM choice based on approach used). |
| **Player wins by 3+ point margin** | Decisive victory. NPC/companion deeply reconsiders. +1 relationship with any witness who agreed with the player's position. |
| **Player loses** | NPC/companion's position prevails this time. Player can override (ruler authority) but takes −1 relationship with the companion AND −1 with any witness. |
| **Player loses by 3+ point margin** | Humbling defeat. −1 relationship with companion. +1 relationship with opponent (they respect you fought). Disposition tag gain: +1 Blunt (you tried). |
| **Deadlock** | Unresolved tension. Companion mood shifts to Troubled (KM_LivingWorld.md). Issue resurfaces in 1d4 sessions. |

---

## 🎯 VOLLEY MODE — BACK-AND-FORTH CONVERSATION

> **DM:** Use Volley Mode for any high-stakes conversation, argument, interrogation, or confrontation where the normal flow (NPC delivers full speech → player replies to all of it) would break the scene. One beat at a time. No walls of text.

---

### What It Is

**Normal mode:** NPC delivers a full speech → player reads it → player replies to everything at once.

**Volley Mode:** NPC speaks 1–3 sentences → stops → player responds → NPC reacts (1–3 sentences) → repeat. Each exchange is one beat. The conversation builds naturally and the player can react in the moment.

---

### How to Enter

- Player types `.volley` — DM enters Volley Mode for the current conversation
- Player types `.end` to exit at any time
- DM should suggest it for: heated arguments, tense negotiations, Tartuccio confrontations, Phase 4.5 companion scenes, accusations, any conversation where pacing matters

**Phase 4.5 companion scenes default to Volley pacing.** Short beats. Player responds to each. Not speeches.

---

### Rules

1. **NPC maximum: 3 sentences per beat** — then stop and wait
2. **The NPC reacts to what the player actually said** — not what it expected
3. **Inline mechanical notes — one line max after each beat:** `[Tartuccio: credibility −1]` / `[Amiri: +1 relationship]`
4. **Player responds freely** — no choice menu required (optional). Say anything, go silent, stand up, leave
5. **No assumptions about what the player will say next** — the NPC does not pre-load a response to an answer it hasn't received

---

### Automatic Triggers

- Phase 4.5 companion scenes
- Tartuccio's Phase 4.5 slot (his one exchange per clock cycle = one volley)
- Any direct challenge from the player (`"You were standing there the whole time"` → volley)
- Any formal accusation or confrontation scene

---

### Example Rhythm

```
NPC: [1–3 sentences]
[pause — waiting]

> player says something

NPC: [reacts to what was actually said — 1–3 sentences]
[pause — waiting]

> player says something
```

No monologues. No walls. The scene builds one exchange at a time.

---

### Relationship to the Interrupt System

Volley Mode supersedes the interrupt system for conversational contexts. When the NPC only speaks 3 sentences before pausing, the player naturally responds before the next assumption lands — no mid-speech break mechanics needed. The interrupt fail codes remain active for cases where the DM delivers a full speech outside Volley Mode.

---

## 🤝 COMPANION ASSIST

If a third party wants to support one side:
- **Second:** One companion can "second" a debater. The debater gains +2 circumstance bonus to ONE round (declared before the roll).
- **Cost:** The seconding companion stakes their own reputation. If the side they support loses, −1 relationship with the winning side's champion.
- **Limit:** One second per side per debate.

---

## 📊 NPC DEBATE MODIFIERS

| NPC Type | Modifier | Reason |
|----------|----------|--------|
| **Nobles / Diplomats** | +2 to Diplomacy rounds | Professional arguers |
| **Barbarians / Warriors** | +2 to Intimidation rounds, −2 to Deception | Direct, honest, threatening |
| **Rogues / Spies** | +2 to Deception rounds | Trained liars |
| **Scholars / Clergy** | +2 to Diplomacy, −2 to Intimidation | Reason over force |
| **Merchants** | +2 to Deception, +1 to Diplomacy | Salespeople |

---

## 🎯 EXAMPLE DEBATES

### Companion Disagreement
```
[DEBATE — Prisoner Fate]
POSITION A: Execute the bandit leader — championed by Amiri
POSITION B: Imprison and interrogate — championed by Tristian
Stakes: A wins = execution, +1 Ruthless. B wins = prisoner lives, +1 Merciful.
```

### Kingdom Advisor Conflict
```
[DEBATE — Tax Policy]
POSITION A: Raise taxes to fund the army — championed by Treasurer
POSITION B: Keep taxes low to maintain loyalty — championed by Councilor
Stakes: A wins = Economy +2, Loyalty −1. B wins = Loyalty +1, Economy −1.
```

### NPC Negotiation
```
[DEBATE — Trade Agreement]
POSITION A: Favorable terms for our kingdom — championed by Player (eRmaC)
POSITION B: Favorable terms for Pitax — championed by Irovetti's Envoy
Stakes: A wins = +3 Economy for 2 turns. B wins = +1 Economy but Pitax spy network installed.
```

---

## ⚠️ DM RULES

1. **Debates are NOT combat.** They are social encounters. Choice menu rules still apply after the debate resolves (10-30 options for what to do next).
2. **Show all math.** Every roll is displayed with full breakdown, same as combat.
3. **NPCs argue back.** Between rounds, the DM narrates the NPC's counter-argument. This is not just rolling dice — it's a scene. The arguments should be in character.
4. **Player can forfeit.** At any point, the player can concede the debate. Same as losing, but no crit failure penalty.
5. **Debate frequency:** No more than 1 debate per session unless the player initiates additional ones. Overuse dilutes impact.
6. **Companion-vs-companion debates** (player not participating): Player watches and chooses which side to support via the Second mechanic, or stays neutral.

---

## 📋 CHAPTER-SPECIFIC SCRIPTED DEBATES

### DB-1: The Bandit Captain's Fate (Ch1)
```
[DEBATE — What to do with a captured bandit leader]
POSITION A: Execute — championed by Amiri
  "Dead bandits don't recruit. Dead bandits don't escape."
POSITION B: Imprison and interrogate — championed by Tristian
  "A dead man tells no tales. A living one tells everything."
Stakes: A = +1 Ruthless, bandit intel lost | B = +1 Merciful, intel gained
```

### DB-2: The Troll Treaty (Ch2-3)
```
[DEBATE — Negotiate with trolls or exterminate]
POSITION A: Negotiate territory — championed by Grand Diplomat
  "Every war we avoid is gold we keep and soldiers who live."
POSITION B: Exterminate — championed by General
  "Trolls don't honor treaties. They honor fire."
Stakes: A = Loyalty +1, Stability +1, risk of troll betrayal | B = Stability +2, Culture −1
```

### DB-3: The Coronation Speech (Ch4)
```
[DEBATE — What kind of ruler to declare yourself]
POSITION A: Servant of the people — championed by Councilor
  "A ruler who serves earns loyalty no crown can buy."
POSITION B: Sovereign by right of conquest — championed by General
  "You took these lands with blood and will. Own it."
Stakes: A = Loyalty +3, +1 Merciful | B = Stability +3, +1 Ruthless
```

### DB-4: The Spy's Fate (Ch3-4)
```
[DEBATE — What to do with a captured Pitax agent]
POSITION A: Turn them — championed by Spymaster
  "A spy you control is worth ten you kill."
POSITION B: Public execution — championed by Marshal
  "A dead spy sends a message. A turned spy sends doubt."
Stakes: A = +1 Cunning, Spymaster network +1, 20% double-agent risk | B = +1 Blunt, Pitax faction −1, deterrence
```

### DB-5: The Alliance Price (Ch4-5)
```
[DEBATE — Accept Aldori military aid with strings attached]
POSITION A: Accept — championed by Grand Diplomat
  "We need their swords more than we need our pride."
POSITION B: Refuse — championed by Ruler (player argues against themselves)
  "Their swords come with chains. We fight alone or not at all."
Stakes: A = Aldori army unit joins, Aldori faction +2, kingdom owes a future favor | B = No allies, +2 Morale (independence), +1 Blunt
NOTE: Player can champion either side or delegate.
```

### DB-6: The Mercy Question (Ch5, during war)
```
[DEBATE — Spare surrendered Pitax soldiers]
POSITION A: Spare and recruit — championed by Seelah
  "They fought for a tyrant. Now the tyrant is gone. Give them a choice."
POSITION B: Prisoner camp — championed by Regill
  "Mercy to the enemy is cruelty to our dead. Contain them."
Stakes: A = +1 army unit (Pitax Defectors, low morale), +1 Merciful | B = Stability +2, no risk, +1 Ruthless
```

### DB-7: The Nyrissa Debate (Ch6, if nyrissa_backstory_known ≥ 2)
```
[DEBATE — Can Nyrissa be saved?]
POSITION A: Save her — championed by Tristian or player
  "She was cursed. She did not choose this. If there is a way to undo it, we must try."
POSITION B: Destroy her — championed by Jaethal or General
  "A thousand years of murder. The Bloom ate kingdoms. Sympathy does not resurrect the dead."
Stakes: A = True Ending path confirmed, +1 Merciful | B = Standard ending, +1 Blunt
NOTE: This is the most important debate in the game. The DM narrates it with full weight.
```

### DB-8: The Legacy Debate (Ch6, pre-finale)
```
[DEBATE — What happens to the kingdom if you don't come back]
POSITION A: Succession plan — championed by Councilor
  "Name an heir. Write a charter of succession. The kingdom survives you."
POSITION B: No plan — championed by Amiri
  "If you die, you die. The kingdom figures it out. That's what kingdoms do."
Stakes: A = Kingdom stability post-game, Councilor +1 | B = Nothing changes. +1 Blunt. Amiri: "Finally, someone who doesn't plan for their own funeral."
```

---

*KM_Debates.md — Kingmaker PF2e Text Adventure | Persuasion Debate System v2.0*
*Rules + 11 scripted debates. Inspired by Divinity: Original Sin.*
