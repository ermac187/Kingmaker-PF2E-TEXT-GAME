# KM_PP_03_tutorial_combat.md — Pre-Prologue Beat 03: TUTORIAL COMBAT
## Atomic scene file | ≤ 8 KB | State: PP_TUTORIAL_PHASE_B
## FILE_KEY: KMPP03:alley-combat-3v1
## RULE_QUOTE: Alley is 5×9 grid, cols A–E only. Auto-resolve forbidden — every round is player-driven. Crew escalation is mandatory after thief surrenders. Map uses Template 1 grid, NOT label-box.

---

> ⛔ DO NOT (1) auto-resolve combat — every round is player-driven, decision by decision
> ⛔ DO NOT (2) widen the alley past cols A–E — alleys are 15 ft, NOT 70 ft (`.fail 9`)
> ⛔ DO NOT (3) pre-advance enemies on the initial map — they move on their own initiative turn
> ⛔ DO NOT (4) draw a label-box instead of the Template 1 grid (`.fail 14`)
> ⛔ DO NOT (5) skip the crew escalation — it's mandatory after the thief surrenders
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP03:alley-combat-3v1]`
Line 2: `[RULE_QUOTE: Alley is 5×9 grid, cols A–E only. Auto-resolve forbidden — every round is player-driven. Crew escalation is mandatory after thief surrenders. Map uses Template 1 grid, NOT label-box.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `tutorial_thief_class` — selects stat block from the table below
- `tutorial_thief_gender` — selects pronouns
- `player.build_id` — for tutorial-callout class-feature reminders

**WRITES:**
- `tutorial_pickpocket_resolved = "won"` (after solo + crew resolved by combat)
- `pre_prologue_state = "PP_TUTORIAL_OUTCOME"` (after both fights end)
- HP / damage tracking per round in `combat_state{}` if save fires mid-fight

**EXIT TRIGGER → PP_TUTORIAL_OUTCOME:**
- Thief surrendered (≤25% HP) AND crew (Bruiser + Cutpurse) resolved
- Load `KM_PP_04_tutorial_outcome.md`

---

## REQUIRED OUTPUTS (every combat response)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP03:alley-combat-3v1]`
1. State header.
2. `[STATE READ]`.
3. Round + initiative line: `Round N — [order]. It's your turn.`
4. Map (Template 1) on round 1 AND any round positions changed.
5. HP ledger lines for player + each enemy: `Player <N>/<max> | <enemy> <N>/<max>`.
6. Combat callouts as triggered (one each, not repeated).

---

## STEP 1 — COMBAT MAP (round 1, Template 1, ASCII)

ALLEY — DEAD END. cols A–E, rows 1–9. 15 ft wide.

```
        A    B    C    D    E
   1    #    #    #    #    #
   2    #    .    T    .    #
   3    #    .    .    .    #
   4    #    .    .    .    #
   5    #    .    .    .    #
   6    #    .    .    .    #
   7    #    .    @    .    #
   8    #    .    .    .    #
   9    #    c    c    c    #
```

`@` player, `T` thief, `#` wall, `.` floor, `c` crowd. Ranger thief: T at C2. Cut Off: thief flat-footed r1.

---

## STEP 2 — TUTORIAL BOX (round 1 only)

```
╔═══════════════════════════════════════════════════════════╗
║  HOW COMBAT WORKS — 3 ACTIONS + 1 REACTION               ║
╠═══════════════════════════════════════════════════════════╣
║  MOVE   — 1 action. Move up to your Speed.                ║
║  STRIKE — 1 action. d20 + atk vs AC. Hit: roll damage.    ║
║           2nd Strike: −5. 3rd Strike: −10.                ║
║  STEP   — 1 action. Move 5 ft, no reactions triggered.    ║
╠═══════════════════════════════════════════════════════════╣
║  CRIT HIT  — 10+ over AC: double damage.                  ║
║  CRIT MISS — 10+ under AC: fumble.                        ║
║  REACTION  — Once/round outside your turn.                ║
║   AoO: enemy moves out of reach without Stepping → Strike.║
║  RANGE: melee = adjacent (5 ft). Ranged: −2 if adjacent.  ║
╠═══════════════════════════════════════════════════════════╣
║  YOUR FEATURES (per build) — surface from Signatures file.║
║  HERO POINTS — you have 1. Reroll any die, take better.   ║
╚═══════════════════════════════════════════════════════════╝
```

DM customizes the YOUR FEATURES line from `player.build_id` + KM_Signatures_*.md.
For Build 2-04 (Barbarian Tactical Reach King): Dual Slice, AoO, reach 10 ft.

---

## STEP 3 — INITIATIVE + PROMPT

Roll initiative, announce order:
> "Round 1. [Initiative order]. It's your turn — what do you do?"

> ⛔ Even if thief has higher initiative, do NOT run his turn this response.
> Player needs to read the map + tutorial box first. (`.fail 12` if violated.)

---

## STEP 4 — THIEF STAT BLOCKS (Level 0, no feats)

Fort +3 | Ref +4 | Will +2 | Speed 25 ft (Monk: 30). Surrender ≤ 25% HP.

```
 #  Class      HP  AC  Attack                              Special
 1  Rogue      14  14  +4 shortsword 1d6+2                 Sneak Attack +1d6 if flanked
 2  Fighter    16  15  +5 shortsword 1d6+2                 AoO reaction
 3  Ranger     14  13  +4 shortbow 1d6+2 / +4 shortsword   Hunt Prey r1: +1 dmg
 4  Barbarian  18  12  +4 shortsword 1d8+3                 Rage r2: +2 dmg, −1 AC
 5  Bard       12  13  +3 dagger 1d4+1 agile finesse       Inspire Courage: +1 self
 6  Champion   18  16  +4 shortsword 1d6+2                 Divine Grace reaction: +2 save
 7  Druid      12  13  Produce Flame +3 1d4+2 fire 30 ft   Tanglefoot: Reflex DC 13 → Clumsy 1
 8  Monk       14  15  +4 fist 1d6+2 agile nonlethal       Flurry: 2 Strikes as 1 action
 9  Cleric     14  14  +3 mace 1d6+1                       Self-heal 1A 1d8+2 (1×/fight)
10  Witch      10  12  Produce Flame +2 1d4+1 fire 30 ft   Evil Eye: Will DC 12 Frightened 1
11  Wizard     10  12  Force Bolt +3 1d4+1 force 30 ft     Shield cantrip reaction +1 AC
```

---

## STEP 5 — ROUND LOOP

Each round: player states actions → DM rolls d20 inline → applies damage → narrates thief turn → updates HP/map → asks next action.

**Callouts (fire each ONCE):**
- First move: *"Moving = 1 action. You have [X] left."*
- First Strike: *"d20+[bonus] vs AC [X] — need [Y]."*
- 3rd Strike: *"−10 — legal, less likely."*
- Ranger at range: *"Close with Move, or use ranged."*
- Adjacent to Ranger: *"Melee range — he's −2 to bow shots."*
- Thief uses feature: *"That's his class feature."*
- Thief ≤50%: *"Below 25% he surrenders."*

---

## STEP 6 — THIEF SURRENDER + CREW ESCALATION

At thief HP ≤25%, output verbatim:

> He drops to one knee. The customer's blade hits the dirt. *"Keep it.
> Not worth dying over."*
>
> He doesn't run. A short whistle. Two shapes step out of the shadows at
> the alley mouth behind you. One built like a laborer, hatchet in hand.
> The other lighter, faster, circling to your left.
>
> The thief backs against the wall. *"Give us the sword and walk away."*

> ⛔ ALWAYS fire crew escalation. Skipping = `.fail 9`.

---

## STEP 7 — CREW MAP (cols A–N, rows 1–9)

```
 T at G2 (spent thief, against back wall, not fighting r1)
 B at G4 (Bruiser, hatchet, 15 ft N of player)
 @ at G7 (eRmaC)
 C at D7 (Cutpurse, shortsword, moving to flank east)
```

Symbols: `B` Bruiser, `C` Cutpurse, `T` spent thief.

---

## STEP 8 — CREW TUTORIAL BOX (round 1)

```
╔══════════════════════════════════════════════════════════╗
║  TWO ENEMIES — NEW RULES                                 ║
╠══════════════════════════════════════════════════════════╣
║  DUAL SLICE: Both in reach → Strike both with 1 action.  ║
║  Pick + Light Pick, one roll each. 2nd: −2, not −5.      ║
║  FLANKING: Enemies on opposite sides = Off-Guard −2 AC.  ║
║  POSITIONING: Back to a wall stops flanking.             ║
║  PRIORITY: Cutpurse flanks for Sneak Attack — drop her.  ║
║  STEP: 5 ft, 1 action, no reactions. Adjust safely.      ║
╚══════════════════════════════════════════════════════════╝
```

---

## STEP 9 — CREW STAT BLOCKS

```
BRUISER — Human Thug
HP: 16 | AC: 14 | Speed: 25 | Fort +4 Ref +2 Will +1
Hatchet d20+4, 1d6+3 (S), agile, thrown 10 ft
Tactics: advances directly; keeps Cutpurse free to flank

CUTPURSE — Human Rogue
HP: 12 | AC: 13 | Speed: 30 | Fort +2 Ref +5 Will +2
Shortsword d20+4, 1d6+2 (P/S), agile, finesse
Sneak Attack: +1d6 if you are Off-Guard (flanked or flat-footed)
Tactics: circles opposite from Bruiser; never adjacent to him
```

**Crew callouts (each once):**
- Flank: *"Off-Guard −2 AC. Sneak Attack live. Break the flank."*
- Player Steps: *"Step = 1A, no AoO trigger."*
- Cutpurse focused: *"Once she's down, no more Sneak Attack."*
- Distance fighting: *"Can't kite both. Pick an angle."*
- Thief rejoins: *"The thief found his legs. Now it's three."*

---

## STEP 10 — CREW RESOLUTION

- Both crew ≤25% HP, OR one dead and one ≤50%: they run. Thief runs with them.
- Player offers Intimidation DC 12: crew reassesses, backs off if they believe.
- Player exits alley south: crew doesn't follow into the crowd.

After crew resolves:
- Set `tutorial_pickpocket_resolved = "won"` (combat path).
- Set `pre_prologue_state = "PP_TUTORIAL_OUTCOME"`.
- Load `KM_PP_04_tutorial_outcome.md`.

---

## EXIT — TRANSITION TO PP_04

PP_04 handles: sword choice [A][B][C][IGNORE], armorer scene at the bench, Squire Aldric witness, reward + reputation deltas, then transition to PP_05 gate approach.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_04 (carries forward)

**Your next response after PP_03's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP04:sword-choice-armorer]
[RULE_QUOTE: Sword choice is player-driven (A/B/C/IGNORE). Armorer Corryn stays at his bench — does NOT enter the alley. Squire Aldric witnesses every outcome silently. Public reputation deltas MUST be listed in reputation_deeds[]. tutorial_pickpocket_resolved must be set before PP_05. Save offer fires before Malak gate.]
```

**Binding constraints:** Sword choice is player-driven. Corryn stays at his bench. Squire Aldric witnesses silently. Reputation deltas listed in reputation_deeds[]. Save offer fires before Malak gate.

---

*KM_PP_03_tutorial_combat.md — Pre-Prologue atomic beat 03 | v92.0*
