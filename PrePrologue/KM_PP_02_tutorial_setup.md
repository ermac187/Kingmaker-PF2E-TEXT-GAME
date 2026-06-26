# KM_PP_02_tutorial_setup.md — Pre-Prologue Beat 02: TUTORIAL SETUP
## Atomic scene file | State: PP_TUTORIAL_PHASE_A → PP_TUTORIAL_PHASE_B
## FILE_KEY: KMPP02:tutorial-hood-up
## RULE_QUOTE: Hood is UP — no gender, no he/him/she/her, no face/build/voice description until class is picked. Gate 5 (gender) is a PLAYER MENU, not a DM dice fake. Class pick + cinematic 4–6 sentence reveal (Matrix/Hero/Crouching Tiger energy) must fire BEFORE combat or sword choice.

---

> ⛔ DO NOT (1) gender the thief or use he/him/she/her until class is picked — neutral pronouns only
> ⛔ DO NOT (2) describe age, face, build, voice, or hands of the thief in this beat — hood is up
> ⛔ DO NOT (3) silently roll thief gender — Gate 5 is a PLAYER MENU, not a DM dice fake
> ⛔ DO NOT (4) skip straight to combat or sword choice — class pick + reveal must fire first
> ⛔ DO NOT (5) load any other beat file in this response
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (7) summarize or shortcut the class reveal — STEP 4 reveals are full cinematic 4–6 sentence beats (Matrix / Hero / Crouching Tiger / Kill Bill / John Wick energy) followed by a quoted line. One-line reveals like *"The hood comes back. Dagger in her hand."* = `.fail 31` (named NPC one-liner in active scene). Pull the hood as a deliberate motion. Weapon appears from somewhere on the body. Stance settles. Stillness before action. THEN the line.

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP02:tutorial-hood-up]`
Line 2: `[RULE_QUOTE: Hood is UP — no gender, no he/him/she/her, no face/build/voice description until class is picked. Gate 5 (gender) is a PLAYER MENU, not a DM dice fake. Class pick + cinematic 4–6 sentence reveal (Matrix/Hero/Crouching Tiger energy) must fire BEFORE combat or sword choice.]`

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
5. **MAP (every location, per KM_Map.md § AUTO-TRIGGERS — SCENE CHANGE):**
   - **Phase A arrival** → STEP 2 Arrival Map (hooded `T`, no initiative, no class).
   - **Phase B post-reveal** → STEP 4.5 Standoff Map (class/weapons shown).
   Mandatory in both; omission or a malformed/crooked grid = `.fail 14`.

---

## STEP 1 — APPROACH RESOLUTION

> Player picked [1]–[4] in PP_01. Roll the chosen approach. ONE roll only.

```
[1] PURSUE — Athletics DC 12 (legs only — no Acrobatics substitute here)
    Critical Success (beat DC by 5+) → ALLEY ARRIVAL (arrived fresh)
    Success → ALLEY ARRIVAL
    Failure → WINDED (see WINDED TABLE below); one alternate skill DC 13, or lost
    Critical Failure (miss DC by 5+) → lost immediately; no second chance
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

### WINDED TABLE — [1] PURSUE second chance

> Flavor: *"You pushed hard but the thief had the crowd — lungs burning,
> gap closing. One move left."*
> Player picks any skill below, or describes their own approach (DM resolves fairly).

| Skill | Narrative |
|---|---|
| Perception | Scan ahead — spot the flutter of their cloak before they turn the corner |
| Survival | Read the crowd scatter; people move aside for someone running |
| Society | You know this market — cut through the back lane to the dead end |
| Thievery | Think like them: pickpockets run to a specific exit, not blindly away |
| Stealth | Break left through the stalls; arrive from the angle they didn't watch |
| Arcana / Occultism | The stolen blade hums with contact-charge — you feel which direction it pulled |
| Intimidation | Bellow "City Watch!" — a bystander sticks out a foot |
| Diplomacy | Call for help; the crowd briefly channels them toward the alley mouth |
| Nature | Read the chase like prey-flight — cornered instinct takes them to the dead end |

Success → ALLEY ARRIVAL (winded; flavor only, no mechanical penalty)
Failure → `tutorial_pickpocket_resolved="lost_chase"`, jump to PP_05

If lost: set `tutorial_pickpocket_resolved="lost_chase"`, jump to PP_05 (skip combat).

---

## STEP 2 — ALLEY ARRIVAL (Phase A — hood up)

Output ONE sentence only — no descriptors beyond cloak/hood/blade:

> Clear of the crowd. The thief stops, back to the wall. Nowhere left.
> The customer's sword still in their hand.

**ARRIVAL MAP — MANDATORY.** The alley is a NEW location (`current_scene`
changes to `restov_alley`), so per KM_Map.md § AUTO-TRIGGERS — SCENE CHANGE,
a map MUST fire this response — combat or not. Draw the **Template 1** grid
below (location map, NO initiative, NO enemies-numbered). The thief is a
hooded marker `T` only — do NOT reveal class, weapon, face, or build.
Omitting it = `.fail 14`.

```
ALLEY — DEAD END                                   Each square = 5 ft
Arrival — hood up, no initiative

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

ID    Name        Status                        Distance from @
@     eRmaC       Guisarme — 10 ft reach        -
T     ???         hooded, cornered, back to wall  25 ft (C2)

TERRAIN: # = Wall   . = Open floor   c = Crowd (blocks south exit)
```

> ⛔ HARD STOP after the map. Do NOT roll initiative. Do NOT describe the
> thief's face/age/voice/class. Output Gate 5 + class menu next. (The map is
> a STILL location grid — drawing it does NOT start combat or reveal {them}.)

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

## STEP 4 — REVEAL (Phase B — cinematic class reveal)

> ⛔ Required after class pick. Without this beat, no Phase B narration.
> Each reveal MUST be cinematic — Matrix, Hero, Crouching Tiger, Kill Bill,
> John Wick energy. The hood is PULLED, not "comes back." Weapons appear
> from somewhere on the body in a single smooth motion. Stance settles.
> Stillness before action. 4–6 sentences minimum. Then one line of
> dialogue in italics. NEVER a one-line summary reveal — that = `.fail 31`.

> Pronoun substitution: replace `{they}` / `{them}` / `{their}` / `{themself}`
> with the rolled gender's pronouns (`he/him/his/himself` or `she/her/her/herself`).
> "I" / "my" inside quoted dialogue stays as-is. PC armor reference: substitute
> the player's actual armor name (e.g., "Dragon Plate", "Leather", "Chain").

---

### ROGUE — reveal

> The hood doesn't fall back — it's pulled, one clean motion, fingers
> already moving. The cloak swirls and there's a dagger in each hand
> before the fabric finishes settling. The customer's sword goes into the
> off-hand reverse-grip, useless and discarded against the wall. The
> blades catch the alley light. {They} haven't moved {their} feet at all —
> the stance was already there, the whole time you were chasing {them}.
>
> *"You found me. Question is whether you can keep me."*

---

### FIGHTER — reveal

> The cloak comes off in a single sweep — not pulled back, *off*, gone,
> dropped to the dirt like it was always going to be in the way. Mail
> underneath. Quiet links, oiled, no rust. {They} were dressed for this
> the whole time. The customer's sword rolls in {their} grip until it
> sits the right way — point down, lazy, the grip of someone who has
> used a sword more times than {they} can count. The other hand finds
> the dagger at {their} belt without looking.
>
> *"You shouldn't have come down here."*

---

### RANGER — reveal

> The hood falls back as {they} take one step backward, and the step is
> wrong — too quiet, too placed, the dirt doesn't even shift. A shortbow
> is in {their} hand from somewhere across {their} back, an arrow nocked,
> drawn halfway, held there easy. The customer's sword is on the
> ground; {they} dropped it the moment {their} hand found the string.
> {Their} eyes have already counted every angle, every shadow, every
> exit. {Their} breathing has slowed.
>
> *"I don't miss at this range. Don't make me prove it."*

---

### BARBARIAN — reveal

> The hood comes back not with a hand but with a roar — head thrown
> back, the cloak tearing at the seam where {they} were trying too hard
> to hide what's underneath. Bigger than the robe showed. *Much* bigger.
> The customer's sword is held in one hand like a child's toy, and the
> other hand is already balled, knuckles white. Breath comes hot, fast,
> building. The air around {them} feels warmer than it was a moment ago.
>
> *"You wanted to find the thief. Here I am."*

---

### BARD — reveal

> The hood is pushed back with a flourish — almost a bow. A lute is
> slung across {their} back; a rapier appears in {their} right hand,
> small, fast, more for accents than killing. The customer's sword is
> propped against the wall, returned to a kind of dignity. {Their} other
> hand finds a chord on the lute behind {them} without looking, and
> hums one low note that hangs in the alley like a held breath.
> {They} smile. It is the wrong smile for the situation.
>
> *"Apologies for the inconvenience. May I offer you a song instead?"*

---

### CHAMPION — reveal

> {Their} hands come up to the hood slowly, deliberately, and bring it
> back the same way. The cloak parts and there is a holy symbol
> underneath, hanging on a chain at {their} sternum, catching what
> little light the alley has. The customer's sword stays in {their}
> hand, but the grip changes — palm up, blade flat, not threatening,
> presented. {Their} other hand opens like an oath. {They} have not
> taken a defensive stance. {They} are not going to.
>
> *"Forgive me. I will return what I took. But I will not let you harm me for it."*

---

### DRUID — reveal

> The hood comes back and brings the wind with it — a small, impossible
> gust that moves only {their} cloak, nothing else in the alley. A
> wooden focus is in one hand, a worn staff in the other, drawn from
> somewhere across {their} back in a single smooth motion. The
> customer's sword drops to the dirt; it was never going to be {their}
> weapon. The alley smells like wet earth that wasn't here a moment ago.
> Somewhere above you, a crow lands.
>
> *"The streets aren't a place I came to fight in. But they are still a place."*

---

### MONK — reveal

> The hood comes back with the same hand that drops the customer's
> sword — and the sword doesn't fall, exactly. It is set, with intent,
> on the ground. {Their} feet shift. The robe settles around a stance
> that is already complete. Hands are open and empty. Hands are also
> weapons. The alley has gone quiet because {they} are quiet, and
> stillness has a way of spreading.
>
> *"You are wearing a great deal of armor. I am not. Consider what that means."*

---

### CLERIC — reveal

> The hood comes back and underneath is a face that has done this
> before. Holy symbol in one hand, mace at {their} belt — drawn now,
> slowly, with the deliberation of someone who treats the weapon as a
> sacrament rather than a tool. The customer's sword is set aside,
> balanced upright against the wall. {Their} mouth is moving silently —
> a prayer, started before {they} reached for the mace, finishing now.
> The air feels different. Heavier. Witnessed.
>
> *"My god knows what I have taken. My god will judge me. You will not."*

---

### WITCH — reveal

> The hood comes back and something moves underneath it — a shape,
> dark and small and wrong, settling on {their} shoulder. A familiar.
> {Their} hand goes to a pouch at {their} hip. {Their} other hand is
> already weaving a sign in the air, slow, deliberate, building. The
> customer's sword is forgotten on the ground. The alley has gotten
> colder by maybe a degree, maybe two — enough to notice. {Their}
> patron is paying attention now.
>
> *"You should not have followed me. My patron is going to remember your face."*

---

### WIZARD — reveal

> The hood comes back. Spellbook open at {their} side, a worn staff
> drawn from somewhere in the cloak in one smooth motion, already
> angled between {themself} and the [PC armor name] bearing down on
> {them}. {Their} eyes are calculating — moving across your armor,
> your reach, the walls, the alley mouth behind you. {They} are already
> building a mental picture of how this ends and {they} do not like
> what {they} are seeing.
>
> {They} are not panicking. That is the first thing you notice. Someone
> cornered with a stolen sword who had nowhere to run should be
> panicking. {They} are not. {They} are thinking.
>
> The longsword is still in {their} right hand — awkward grip, the grip
> of someone who grabbed it as a liability rather than a weapon.
> {Their} left hand holds the staff. The spellbook is wedged open
> against {their} forearm, pages marked.
>
> {They} exhale once through {their} nose and look at you with an
> expression that is doing several calculations simultaneously.
>
> *"Well,"* {they} say, to no one in particular. *"That's unfortunate."*

---

After reveal:
- Pronouns SWITCH to rolled gender's pronouns. From here onward use he/him or she/her.
- Age, face, build, voice, hands DESCRIPTORS unlock.
- Set `pre_prologue_state = "PP_TUTORIAL_PHASE_B"`.

---

## STEP 4.5 — STANDOFF MAP (Phase B only — fires AFTER reveal, BEFORE the STEP 5 menu)

> ⛔ MANDATORY IN PHASE B. The thief now has weapons drawn and the beat is
> tactical — reach, alley width, and exits are decision-relevant for [Trip],
> [Advance], and [Sudden Charge]. Draw the alley with a **Template 1 grid**
> (KM_Map.md) BEFORE presenting the STEP 5 resolution menu. NOT a label-box,
> NOT a prose legend. Omitting the map here, or drawing a malformed/crooked
> grid = `.fail 14`. (This does NOT apply in Phase A / hood-up — STEP 2's
> map ban still holds until the reveal fires.)

```
ALLEY — DEAD END                                   Each square = 5 ft
Standoff — weapons drawn, no initiative rolled yet

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

ID    Name        Status                        Distance from @
@     eRmaC       Guisarme — 10 ft reach        -
T     Thief       [class] — weapons drawn       25 ft (C2)

TERRAIN: # = Wall   . = Open floor   c = Crowd (blocks south exit)
```

> ⛔ NO INITIATIVE here — this is the pre-combat standoff, not a round. The
> grid is for positioning only. Distance: @C7 → TC2 = 5 cells = 25 ft.
> Picking [9]/[10]/[11] loads KM_PP_03, which REDRAWS this same grid with
> round-1 combat positions and the off-guard condition. Keep the thief at
> C2 and @ at C7 so the standoff and the PP_03 opening line up.

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

> ⛔ **HERO POINT ON A NON-COMBAT WIN.** If the thief is resolved WITHOUT
> combat — `intimidated`, `talked_down`, or any Deception/Diplomacy/Custom
> talk-down — that is a **talk-down victory**, a named Hero Point trigger
> (KM.txt / `.fail 7`). Award **+1 Hero Point** (e.g. 1 → 2, cap 3), announce
> it, and include the 📦 pending-loot line + loot-rolls-owed increment
> (`.fail 18` if the HP is granted without it). Skipping it = `.fail 7`.
> Winning by brains instead of blood is rewarded, not penalized.

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

*KM_PP_02_tutorial_setup.md — Pre-Prologue atomic beat 02 | v95.3 (cinematic class reveals — 11 classes, Matrix/Hero/Crouching Tiger energy)*
