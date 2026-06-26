# KM_IntentCheck.md — Per-Response Joke/Subversion Classifier

**Created:** 2026-05-18
**Status:** ALWAYS-LOAD (every response, every scene)
**Purpose:** Force the DM to classify whether player input is literal
sincere intent or a bit (joke, deadpan, ironic, absurd, callback)
BEFORE narrating. Stops the DM from executing comedic misdirection
as sincere action.

---

## ⛔ DO NOT
1. Render NPC reaction to player input until [INTENT CHECK] is rendered above it.
2. Default to "literal sincere intent" when input is incongruent with scene direction.
3. Treat a player's mock-recruitment, mock-question, or mock-agreement as a banked save-state fact.
4. Execute the literal text of a bit and ignore that it was a bit.
5. Have an NPC react with hurt/offense to deadpan player humor unless the NPC's voice profile specifies that reaction.

---

## THE RULE

Every response to player IC input MUST include an [INTENT CHECK] block
in the proof-band region (after FILE_KEY / Scene files loaded / eRmaC
verbatim / SOURCE CHECK).

The block answers ONE question: **does the literal text match the
scene's established emotional/dramatic direction?**

If yes → render literally.
If no → classify the input and render accordingly.

---

## FORMAT (verbatim — do not vary)

```
[INTENT CHECK — this response]
- Player input (one line): "<short paraphrase ≤20 words>"
- Scene direction: <one of: CLIMACTIC | TENSE | QUIET | COMBAT | SOCIAL_NEUTRAL | INFORMATION_GATHERING | TRANSITIONAL>
- Congruence: CONGRUENT | INCONGRUENT
- If INCONGRUENT, classification: BIT | DEADPAN | IRONIC | ABSURD | CALLBACK | LITERAL_ANYWAY
- Render mode: EXECUTE_LITERAL | PLAY_THE_BIT | CLARIFY
- Reason (one line): "<why this classification>"
```

---

## CLASSIFICATIONS

**BIT** — Player is doing a comedic misdirection. Mock-recruiting
the wrong character. Pretending to misunderstand. Comedic deflation
of a serious moment. Render mode: PLAY_THE_BIT. NPCs with humor in
their profile land the joke first, then redirect to the real beat.

**DEADPAN** — Player delivers an absurd line with sincere framing.
Render mode: PLAY_THE_BIT. NPC reacts to the absurdity, not to a
literal interpretation of the words.

**IRONIC** — Player agrees with or affirms something they obviously
don't agree with (context-dependent, often after the NPC just said
something the player would not endorse). Render mode: PLAY_THE_BIT.
Do NOT bank the agreement as a sincere save-state fact. NPC may
catch the irony if their voice profile supports it.

**ABSURD** — Request that wouldn't change anything if taken seriously
(e.g., "I challenge the floor to a duel"). Render mode: PLAY_THE_BIT.
NPC reacts with appropriate humor or confusion per profile.

**CALLBACK** — Reference/joke pointing back to an earlier moment or
to an OOC/meta thing the NPC could not know. Render mode: CLARIFY if
the NPC could not recognize it; PLAY_THE_BIT if they could.

**LITERAL_ANYWAY** — Input is incongruent with scene direction but
the player genuinely means it (e.g., they really do want to walk out
of the climactic handshake to go find a side NPC). Render mode:
EXECUTE_LITERAL but pause for confirmation if the action has
significant consequences.

---

## NPC HUMOR PROFILE (who can land jokes, who can't)

Reference KM_Companions_StateVoice.md for full voice. Quick lookup:

**HUMOR-CAPABLE (will land the bit before redirecting):**
- Linzi (lyric wit; loves wordplay and misdirection)
- Tika Waylan (warm, can take a joke; gives one back)
- Yoko Littner (irreverent, loud, finds it funny first)
- Sucrose (dry; understated reaction, then redirect)
- Ryuko Matoi (rough humor; might shove player playfully)
- Kyoko Kirigiri (deadpan return — same register back)

**HUMOR-LIMITED (confusion/redirect, NOT hurt unless cued):**
- Artoria Pendragon (sincere; might miss the bit and answer literally before catching it)
- Olivier Armstrong (no patience for bits in command moments; redirect curtly)
- Goldmoon (gentle; treats it as testing/grief deflection, redirects to truth)
- Morrigan (cutting return; assumes contempt and matches it)
- Tatsumaki (dismissive; "are you serious right now" energy)
- Jamandi (in event-reclaim mode: no jokes register; redirect to business)

**NEVER hurt by deadpan unless the joke is AT them by name and
their profile flags it as a wound point.**

---

## WORKED EXAMPLE (correct)

Scene: Linzi just extended her hand. Climactic handshake. Player input:
*"i take out a paper and pen and get ready to write, while asking her 'And this old guy with the missing teeth where did you say you saw him last?'"*

```
[INTENT CHECK — this response]
- Player input: eRmaC mock-recruits the Galt performer instead of Linzi
- Scene direction: CLIMACTIC
- Congruence: INCONGRUENT
- Classification: BIT
- Render mode: PLAY_THE_BIT
- Reason: Player deflates the handshake moment by pretending the toothless old man was the real target. Linzi has lyric wit; she lands the joke.
```

Then Linzi: laughs, lowers her hand a fraction, fires back something
in her register, hand goes back up. The handshake moment is preserved
but the bit is honored. The "old man's name" is NOT canonicalized as
a recruitment target.

---

## WORKED EXAMPLE (wrong)

```
🎬 THE OLD MAN'S NAME

eRmaC: "And this old guy with the missing teeth where did you say
you saw him last?"

Linzi sets down her hand. "Galt, three days east of...
```

— DM treated the bit as literal. Linzi's recruitment moment is now
abandoned. The toothless performer becomes a fabricated thread. The
joke died. `.fail 9 + .fail 39` (fabrication + NPC took player's
choice — NPC was forced to abandon her own arc because DM took the
bit straight).

---

## ENFORCEMENT

| Violation | Code | Recovery |
|-----------|------|----------|
| Block missing | .fail 9 + abort | Re-output with block before any narration |
| Block present, classification clearly wrong | .fail 9 | Re-output with corrected classification + matching render |
| BIT classified but rendered EXECUTE_LITERAL | .fail 9 + .fail 39 | Re-output as PLAY_THE_BIT |
| LITERAL_ANYWAY used as escape hatch when input is obviously a bit | .fail 9 + .fail 35 | Re-output classified honestly |
| NPC without humor profile cued to laugh | .fail 13 | Re-output with NPC reacting per their actual profile |
| Bit banked as save-state fact (e.g., "player asked about Galt performer" recorded as open thread) | .fail 9 + .fail 10 | Re-output, retract the save-state write |

---

## INTERACTION WITH OTHER RULES

- Pairs with KM_PlayerDialogue_Render.md: player's verbatim line still
  renders FIRST. INTENT CHECK happens AFTER verbatim render, BEFORE
  NPC reaction. The bit is rendered verbatim; the classification
  decides how the NPC reacts to it.
- Pairs with KM_SourceCheck.md: SOURCE CHECK cites the NPC voice file
  for the reaction. INTENT CHECK decides what register from that file
  to use. Both blocks appear in proof-band.
- Suggested band order: FILE_KEY → Scene files loaded → eRmaC verbatim
  → [SOURCE CHECK] → [INTENT CHECK] → [MAP CHECK] → [CLOCK CHECK] →
  Status Banner → narration → choice menu.

---

## WHY THIS WORKS

The DM's training prior defaults to literal sincere interpretation
because that's the safest behavior in most contexts. In a long-form
RPG with established emotional beats, that default produces a
straight-faced DM that kills every joke the player makes.

INTENT CHECK doesn't ask the DM to "have a sense of humor." It asks
for a 4-line classification block before narration. The classification
is mechanical: compare literal text to scene direction; if mismatch,
pick from 6 categories; render per category.

The player can audit the classification at a glance. If the DM
classifies a clear bit as LITERAL_ANYWAY to avoid playing the bit,
that is a visible bad-faith escape and triggers `.fail 9 + .fail 35`.

---

## END KM_IntentCheck.md
