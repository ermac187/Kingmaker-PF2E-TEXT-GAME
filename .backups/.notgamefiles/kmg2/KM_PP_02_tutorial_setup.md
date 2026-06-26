# KM_PP_02_tutorial_setup.md — Pre-Prologue Beat 02: TUTORIAL SETUP
## Atomic scene file | ≤ 8 KB | State: PP_TUTORIAL_PHASE_A → PP_TUTORIAL_PHASE_B
## FILE_KEY: KMPP02:tutorial-hood-up
## RULE_QUOTE: Hood is UP — no gender, no he/him/she/her, no face/build/voice description until class is picked. Gate 5 (gender) is a PLAYER MENU, not a DM dice fake. Class pick + reveal must fire BEFORE combat or sword choice.

---

> ⛔ DO NOT (1) gender the thief or use he/him/she/her until class is picked — neutral pronouns only
> ⛔ DO NOT (2) describe age, face, build, voice, or hands of the thief in this beat — hood is up
> ⛔ DO NOT (3) silently roll thief gender — Gate 5 is a PLAYER MENU, not a DM dice fake
> ⛔ DO NOT (4) skip straight to combat or sword choice — class pick + reveal must fire first
> ⛔ DO NOT (5) load any other beat file in this response
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP02:tutorial-hood-up]`
Line 2: `[RULE_QUOTE: Hood is UP — no gender, no he/him/she/her, no face/build/voice description until class is picked. Gate 5 (gender) is a PLAYER MENU, not a DM dice fake. Class pick + reveal must fire BEFORE combat or sword choice.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `pre_prologue_state` — should be `"PP_TUTORIAL_PHASE_A"` on entry
- `tutorial_thief_gender` — usually `""`; if already set, skip Gate 5
- `tutorial_thief_class` — usually `""`; player picks here
- `save_timestamp` — used if player picks dice option [3] in Gate 5

**WRITES:**
- `tutorial_thief_gender = "male" | "female"`
- `tutorial_thief_class = "<class name>"`
- `pre_prologue_state = "PP_TUTORIAL_PHASE_B"` (after class pick + reveal)
- `current_scene = "restov_alley"`

**EXIT TRIGGER → PP_TUTORIAL_PHASE_B:**
- Approach roll resolved (success → alley arrival; failure → handle below)
- `tutorial_thief_gender` set (Gate 5 resolved)
- `tutorial_thief_class` set (class menu resolved)
- "Hood comes back" reveal narration delivered
- THEN load `KM_PP_03_tutorial_combat.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP02:tutorial-hood-up]`
1. `🚪 PRE-PROLOGUE STATE` header (Tutorial: phase A or B).
2. `[STATE READ] pre_prologue_state="PP_TUTORIAL_PHASE_A" | gender=<value> | class=<value>`
3. `[TUTORIAL GATES] gender=<male|female|UNROLLED> | class=<class|UNPICKED> | proceed=<YES|NO>`
   - `proceed=YES` only when BOTH gender AND class are set.
   - Until then: NO thief description (age/build/voice/hands), NO armorer at alley, NO resolution menu.
4. `[HP CHECK]` ledger line.

---

## STEP 1 — APPROACH RESOLUTION

> Player picked [1]–[4] in PP_01. Roll the chosen approach. ONE roll only.

```
[1] PURSUE — Athletics or Acrobatics DC 12
    Success → ALLEY ARRIVAL
    Failure → one more attempt DC 14, or lost → tutorial_pickpocket_resolved="lost_chase"
[2] CUT OFF — Perception DC 13 or Warfare Lore DC 11
    Success → ALLEY ARRIVAL (thief flat-footed round 1)
    Failure → wrong alley; one Athletics/Acrobatics DC 14 or lost
[3] SHOUT — Intimidation DC 13
    Success → ALLEY ARRIVAL
    Failure → one Athletics/Acrobatics DC 14 or lost
[4] APPEAL — Diplomacy DC 12 or Society DC 11
    Success → ALLEY ARRIVAL, public_reputation +1
    Failure → one Athletics/Acrobatics DC 14 or lost
```

If lost: set `tutorial_pickpocket_resolved="lost_chase"`, jump to PP_05 (skip combat).

---

## STEP 2 — ALLEY ARRIVAL (Phase A — hood up)

Output ONE sentence only — no descriptors beyond cloak/hood/blade:

> Clear of the crowd. The thief stops, back to the wall. Nowhere left.
> The customer's sword still in their hand.

> ⛔ HARD STOP. Do NOT roll initiative. Do NOT draw a map. Do NOT
> describe the thief's face/age/voice. Output Gate 5 + class menu next.

---

## GATE 5 — THIEF GENDER (PLAYER MENU — fire once if `tutorial_thief_gender == ""`)

```
══════════════════════════════════════════════════
 THIEF — under the hood, behind the cloak.
 Gender is locked here for the rest of the tutorial.

 [1] Male   (he / him / his)
 [2] Female (she / her / hers)
 [3] Roll dice — DM uses save_timestamp last digit
     (even = female, odd = male)
══════════════════════════════════════════════════
```

**Resolution:**
- `1` → `tutorial_thief_gender="male"`
- `2` → `tutorial_thief_gender="female"`
- `3` → read `save_timestamp` last digit, output:
  `[DICE] save_timestamp last digit = <N> → <even=female|odd=male>`

> ⛔ DM may NOT pick gender silently. Generating "male" without the menu = `.fail 9`.

---

## STEP 3 — CHOOSE CLASS MENU (fire if `tutorial_thief_class == ""`)

> ⛔ Output verbatim. Wait for player input.

```
══════════════════════════════════════════════════
 CHOOSE THEIR CLASS — what do you see beneath the hood?

 [1]  Rogue      — nimble stance, dagger ready off-hand
 [2]  Fighter    — wide guard, short sword, no wasted movement
 [3]  Ranger     — backs to wall, reaches for a shortbow
 [4]  Barbarian  — bigger than the robe showed, rage building
 [5]  Bard       — lute across the back, smirking, dagger out
 [6]  Champion   — holy symbol flash, disciplined stance
 [7]  Druid      — gnarled staff, starts muttering
 [8]  Monk       — drops the robe, wrapped hands, fighting stance
 [9]  Cleric     — holy symbol in hand, mace at belt, calm authority
 [10] Witch      — familiar drops to shoulder, staff from sleeve
 [11] Wizard     — spellbook open at side, staff in hand, calculating
 [?]  Random     — DM rolls 1d11
══════════════════════════════════════════════════
```

Announce class through equipment and behavior — do not name the class.

---

## STEP 4 — REVEAL (Phase B — hood comes back)

> ⛔ Required after class pick. Without this beat, no Phase B narration.

Format:
> The hood comes back. <class-specific reveal beat>.

Examples:
- Rogue (female): *"The hood comes back. Nimble stance, dagger already in her off-hand. She's not running anymore — she's setting up."*
- Barbarian (male): *"The hood comes back. Bigger than the robe showed. Rage already building behind his eyes."*
- Cleric (male): *"The hood comes back. Holy symbol gripped tight, mace at his belt. Calm — too calm."*

After reveal:
- Pronouns SWITCH to rolled gender's pronouns. From here onward use he/him or she/her.
- Age, face, build, voice, hands DESCRIPTORS unlock.
- Set `pre_prologue_state = "PP_TUTORIAL_PHASE_B"`.

---

## STEP 5 — NON-COMBAT RESOLUTION (offer before combat fires)

After reveal, present a 10-30 option menu including:

- **Intimidation DC 14:** Looks at your armor, your weapons, the alley. Sword drops, runs. → `tutorial_pickpocket_resolved="intimidated"`. Skip combat.
- **Deception DC 13:** Claim city watch / archers cover the alley. Disarmed without combat.
- **Diplomacy DC 13:** Offer a way out — drop the sword, walk free. → `tutorial_pickpocket_resolved="talked_down"`. Unarmed retreat.
- **Strike / Draw weapon:** Initiates combat → load PP_03.
- **Wait / observe:** Thief breathes; offer the menu again next turn.
- **Custom action:** Any approach the player describes; resolve fairly.

> ⛔ Do NOT auto-fire combat after class pick. Combat starts ONLY when
> the player chooses a combat-initiating action.

---

## EXIT — TRANSITION TO PP_03

If player chose a combat-initiating action:
- Set `pre_prologue_state = "PP_TUTORIAL_PHASE_B"` (combat sub-state)
- Set `current_scene = "restov_alley_combat"`
- Load `KM_PP_03_tutorial_combat.md`
- Output Step 1 (map) + Step 2 (tutorial box) + Step 3 (initiative) per PP_03.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_03 (carries forward, on combat path)

**Your next response after PP_02's combat exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP03:alley-combat-3v1]
[RULE_QUOTE: Alley is 5×9 grid, cols A–E only. Auto-resolve forbidden — every round is player-driven. Crew escalation is mandatory after thief surrenders. Map uses Template 1 grid, NOT label-box.]
```

**Binding constraints:** 5×9 alley grid (cols A–E only). Player-driven combat — no auto-resolve. Crew escalation fires after thief surrenders. Template 1 grid mandatory.

If player resolved non-combat (Intimidation/Deception/Diplomacy success):
- Set `tutorial_pickpocket_resolved` per outcome
- Set `pre_prologue_state = "PP_TUTORIAL_OUTCOME"`
- Skip PP_03; load `KM_PP_04_tutorial_outcome.md` for the sword choice
- (No sword choice if thief fled with the sword — `intimidated`/`talked_down` paths
  return the sword to the armorer's bench; PP_04 handles the return scene.)

---

## ALLOWED IN PHASE A (proceed=NO):
- The pursuit roll outcome (success/failure)
- One sentence: "You catch up to the thief in the alley. Back to the wall."
- The Gate 5 gender menu + the class menu

## BANNED IN PHASE A (proceed=NO):
- Age descriptors ("young", "old", "teenage")
- Build/body descriptors
- Voice/behavior descriptors
- Equipment beyond the stolen blade
- Armorer in the alley (he stays at his bench — he can't abandon 12 customers' weapons)
- The sword-choice resolution menu

---

*KM_PP_02_tutorial_setup.md — Pre-Prologue atomic beat 02 | v92.0*
