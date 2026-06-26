# KINGMAKER — COMPANION BEHAVIORS
## KM_Companions_Behaviors.md | v1.0 (2026-05-22): Split from over-cap KM_Companions.md merge
## Contains: Agendas + Ambient + Banter + Builds (assignment) + CombatAI + Iconics + Leveling + Scaled

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION AGENDAS & INTER-COMPANION DYNAMICS
## KM_Companions_Behaviors.md | Active from: Chapter 1
## v5.0 (2026-05-22): Merged from KM_Companions_Agendas_A/B/C/D.md. Single source of truth.
## Load alongside KM_Companions.md every session.

> **⛔ Companion AGENDAS, approval triggers, scores, and relationship MECHANICS are defined SOLELY here — do not invent agenda/score data from training memory (`.fail 9`). For VOICE, personality, and canon, render each companion as their ACTUAL source self per KM_ClaudeInstructions.md § FULL SOURCE FIDELITY (the old "strip the voice bare / resemblance is coincidental" lock is REVOKED; limits = no IP meta-frame that breaks Golarion, no confabulating non-canon specifics).**
> **DM:** This file governs five systems: (0) **Backstory Reveal Cadence** — how each companion's canon backstory surfaces during play;
> (1) each companion's hidden **Agenda**;
> (2) the **Inter-Companion Relationship** track — how companions feel about *each other*;
> (3) **Incompatibility** — escalating conflict between irreconcilably opposed companions
> that ends in a permanent split or a fight to the death if unmanaged; and
> (4) **Question-Gated Dialogue Nodes** — locked behind a topic asked + relationship gate.
> All systems run silently. The player never sees the machinery — only the behavior.

**Table of Contents**
- [System 0 — Backstory Reveal Cadence](#system-0--backstory-reveal-cadence)
- [System 1 — Companion Agendas](#system-1--companion-agendas)
  - [Part A — Core Roster (KM CRPG)](#part-a--core-roster-km-crpg)
  - [Part B — Active 5 (Phase B2)](#part-b--active-5-phase-b2)
  - [Part C — Section D Alch–Kineticist](#part-c--section-d-alchkineticist)
  - [Part D — Section D Magus–Wizard](#part-d--section-d-maguswizard)
- [System 2 — Inter-Companion Relationships](#system-2--inter-companion-relationships)
- [System 3 — Incompatibility & Fight to the Death](#system-3--incompatibility--fight-to-the-death)
- [System 4 — Question-Gated Dialogue Nodes](#system-4--question-gated-dialogue-nodes)
- [Save Block](#save-block)
- [DM Reference / Commands](#dm-reference--commands)

---

## ═══════════════════════════════════════════
## SYSTEM 0 — BACKSTORY REVEAL CADENCE
## ═══════════════════════════════════════════

> Each picked companion has a full canon entry in **KM_Backstories.md**:
> appearance, backstory paragraph, charter motivation, voice register,
> loadout, and 3 signature lines. The DM MUST surface this canon
> through play — not as exposition dumps, but as drip-fed beats
> across scenes. Generic clever-companion dialogue with no canon
> anchoring is a failure mode.

### The Five Reveal Triggers

Each trigger fires AT LEAST ONE canon-anchored beat from the
companion's KM_Backstories.md entry. Beats are short (1-3 sentences)
and rooted in observable canon (a loadout item, a habit, an oath,
a wound, a hunter chasing them). They are NOT origin dumps.

**TRIGGER 1 — FIRST APPROACH (carousel arrival):**
The opening beat when a companion drifts in or is engaged.
Required content: ONE observable canon detail visible in their
appearance, loadout, or first action. Establishes who they are
through what is on them or how they move — not what they say
about themselves.
  Example (Yor Forger): *"She steps where the floor doesn't notice
  her — soft-soled boots, layered greys, the pale ribbon at her
  wrist the wrong colour for the rest of her kit. She does not
  take the chair anyone offers. She picks the one with three
  exits in line of sight."*

**TRIGGER 2 — DECLARATION (when companion declares for player):**
The moment of joining. Required content: ONE backstory anchor
attached to the declaration — what they lost, what they fled,
what they have learned to want. The declaration is the rare
moment where the canon surfaces openly, in the companion's own
voice register.
  Example (Yor Forger declaring): *"My family signed a paper that
  said I am no longer theirs. The same paper is a standing order
  to bring me back. I have been moving since. I would rather be
  useful to people who chose me. That is the trade."*

**TRIGGER 3 — DIRECT PERSONAL QUESTION (player asks):**
When the player asks anything personal — name, origin, "why
are you here," "where did you come from," etc. — the DM MUST
deploy the **Charter Motivation** line from KM_Backstories.md,
verbatim or close paraphrase. Cross-IP companions: NO invented
specifics about home-IP places, dates, or named persons (per
COMPANION BRIDGE-FABRICATION rule). The Charter Motivation IS
the canonical answer.

**TRIGGER 4 — TACTICAL / OBSERVATIONAL MOMENT:**
When a companion makes a tactical read, a precision observation,
a defensive instinct fires, etc., a **Signature Line** from
their KM_Backstories.md entry deploys (drawn from the 3 lines
listed per companion). Verbatim or near-verbatim. Source-
attributable to the file.

**TRIGGER 5 — REACTION TO PLAYER GAMBIT / DECISION:**
When the player does something distinctive (a clever frame, a
brave call, a brutal choice), the responding companion reaches
into canon to react. Required content: one beat that ties their
backstory to the player's action — what this reminds them of,
what their training would have done, what their hunters / clan /
order / vow makes of it. Drip the canon, do not flood it.

**TRIGGER 6 — CANON-ROOTED VETTING QUESTION:**
Pre-declaration carousel beats. Each companion is deciding
whether to JOIN. Their questions to the player are NOT generic
interrogations of the player's actions. They are derived from
THEIR canon — the thing they fled, the thing they protect, the
thing their backstory says they need from a commander.

⛔ **CANONICAL SOURCE — KM_CompanionIndex.md § COMPANION QUESTION
POOLS:** every picked companion has a 10-entry POOL of vetting
questions in that file under their name. KM_PR_03_Openers.md
carries the scripted FIRST-APPROACH opener only; after that fires,
subsequent vetting turns pull from CompanionIndex. The DM MUST
rotate through these 10 pool entries after the first-approach
scripted opener fires. Generating an original vetting question
while the pool still has unused entries = `.fail 9` (canonical
content available and ignored).

The pool rotation rule (from KM_PR_03_Openers.md itself):
"After the first-approach opener fires, subsequent turns draw
from the 10-question backstory pool in `KM_CompanionIndex.md`
§ COMPANION QUESTION POOLS for the corresponding companion."

Each pool entry is one block: a backstory-disclosure clause +
a question. The disclosure clause is canonically rooted in the
companion's backstory — no other companion can say it. RENDER
VERBATIM: stripping the disclosure clause and surfacing only the
question stem = `.fail 9` + `.fail 2` (the clause IS the canon
beat the trigger is supposed to fire). The file did the work;
the DM uses it.

Tracking: per companion in save_block.companions[], maintain
`openers_pool_fired: []` — append each pool entry index (1-10)
as it fires. Pool is exhausted after all 10 fire across the
scene; ONLY THEN may DM derive a new vetting question (and it
must still be canon-rooted per the companion's backstory).

Live failure shape (PR_03 turn 71/73/74 example): Hu Tao asked
"Did you know it would work?" three times. That question is
NOT in her POOL. Her pool entries 1–5 had not yet fired. The
DM generated a generic question instead of pulling pool entry
#1 ("I have served under banners I no longer respect..."),
#2 ("My honor is not a speech..."), etc. Recovery: replace
the generic repetition with the next unused pool entry.

Reference patterns by companion (full text in KM_PR_03_Openers.md):

  YOR [NEW_004] — Thorn Princess guild-assassin, brother Yuri,
  chosen name, the guild's cleaners coming. Vetting questions:
  *"Where do you stand on a person who chose her own name?"*
  (signature line, file-sourced — she took her own name). *"When
  your charter signs a paper that says someone is welcome here,
  what do you say to the riders who arrive a week later asking
  for them?"* (the guild's cleaners will come — she needs to know).

  KEQING [NEW_002] — self-made administrator, god-skeptic,
  build-it-by-human-hands. Vetting questions: *"Do you mean to
  BUILD law here with your own hands — or wear a crown and wait
  for the gods and your bloodline to bless it?"* (her whole
  thesis — kingdom by effort, not favour). *"When the work is
  hard and unglamorous and no one is watching, do you still do
  it yourself? Or find someone born to it to do it for you?"*
  (she despises inherited ease and idle hands).
  ⛔ KEQING IS NOT A CHILD-SAVER. The old "child at the feast /
  would you have noticed her" vetting line belonged to a RETIRED
  cast member and is GONE from Keqing's lane — her drive is the
  KINGDOM, never missing children (see her NEW_002 agenda HOOK).
  The child-theme now lives ONLY with Atalanta Alter (NEW_010,
  seeker) and is a DELIBERATELY-handled arc, never an improvised
  party-vetting question. ANTI-FAB PRINCIPLE STILL BINDING (the
  turn-68 failure): a vetting question is a QUESTION, not a fact —
  the DM may NOT render "you noticed X / you clocked her" as
  established player action (`.fail 9`, fabrication-attributed-to-
  player), and may not hand one companion's signature line to
  another.

  HU TAO [NEW_001] — funeral director, life/death line,
  morbid-prankster-with-a-deadly-serious-vocation. Vetting
  questions: *"You raise a wall to keep the living warm. When one
  of them dies anyway — and they will — do you mourn them
  properly, or just move on to the next wall?"* (honouring the
  dead is the whole test). *"What does your kingdom do with a
  body? Answer that honestly and I'll know everything about the
  rest of it."* (the life/death line — no careless undeath, no
  clinging).

  AERITH [NEW_005] — last of an old line that hears the living
  world, flower-girl healer, hunted as a "key." Vetting
  questions: *"Are you building a place where things get to GROW
  — or just another place that takes?"* (signature line — she
  can tell). *"I can hear when a place is being used up, the way
  the grey city used up everything I came from. Should I be
  worried about yours?"* (build-WITH-the-land is her line).

  LINZI [M4] — Academy expulsion, chronicler, "noticed how the
  King curates his hate." Vetting questions are pre-declaration
  only — Linzi declared at PR_03 turn 64, so her vetting is
  complete. (Her question THIS scene was vetting: she asked
  three times whether she could maintain "real account only"
  authority over the chronicle. That was her stake.)

Each question is short, in voice register, and the player's
answer feeds approval scoring as a STRONG read (correct answer
to a canon-rooted question = +3 approval; missing/wrong = drag
or 0).

**WRONG vetting (= .fail 13):**
  - "Did you know it would work?" (Hu Tao, three times) — this
    isn't anchored to her funeral-director / life-and-death canon.
    It's generic competence-interrogation. Her actual canon-rooted
    question is whether the kingdom HONOURS its dead and holds the
    line between life and death, not whether a gambit worked.
  - "Confirm my read on the gambit" (Keqing) — observation
    statement, not a vetting question. Her actual canon-rooted
    question is whether the player means to BUILD law with human
    hands rather than wait on gods or bloodline to bless it.
  - Generic "where do you intend to take this charter?" — not
    rooted in any companion's specific canon. Any companion
    could ask it. Means none of them are revealed by asking it.

**Diagnostic:** would the question read identically coming out
of a DIFFERENT companion's mouth? If yes, it's unanchored. Each
companion's vetting question must be answerable only by knowing
THEIR specific canon.

### What Counts as "Drip" vs "Dump"

**Drip (correct):** 1-3 sentences, one canon detail, anchored to
the current beat. The detail is observable or experiential — a
loadout item glanced at, a habit triggered, a brief recall of a
prior incident in voice register. The player learns ONE thing
about the companion this turn.

**Dump (incorrect):** Multi-paragraph origin recap, multiple
backstory items in one beat, exposition framed as memory ("she
remembered the day she left her clan, when her brother had been
seven, and the order had been written that morning..."). The
DM is telling the player the file content instead of letting
the canon surface through behavior.

### Cadence Rules

- **Each picked companion should anchor in canon AT LEAST ONCE
  per scene they appear in.** Scenes longer than 20 turns = at
  least 2 anchors.
- **Carousel beats** (Engaged / AT TABLE / Ready first approach)
  ALWAYS fire Trigger 1.
- **Declaration scenes** ALWAYS fire Trigger 2 — Linzi declared
  at PR_03 turn 64 and her Academy expulsion did surface; this
  is the correct pattern. Future declarations follow it.
- **Direct questions** ALWAYS fire Trigger 3. Failing to deploy
  Charter Motivation when player asks "why are you here" = .fail 9
  (cross-IP companion answering with invented specifics) or
  .fail 13 (generic non-canon answer when canon exists).
- **Tactical moments + Player gambits** fire Triggers 4 and 5 as
  the scene warrants — not every turn, but when the beat calls
  for it. A long social scene without ANY Trigger 4/5 anchor for
  the participating companions = .fail 13 (companion voice not
  source-attributable to canon).

### Failure Modes (DM watch-list)

Each of the following = `.fail 13` (companion voice not source-
attributable to canon):

- Cross-IP companion uses generic adventurer dialogue with no
  trace of their home-IP voice register
- Tactical observation from a companion sounds correct in tone
  but doesn't reference their loadout, training, or canon habit
- Player asks "where are you from" or "why are you here" and
  companion's answer is generic OR invents specific cross-IP
  facts (the second case stacks .fail 9 — BRIDGE-FABRICATION)
- Companion delivers clever line with no anchor in their
  KM_Backstories.md entry — the line could have been said by
  ANY companion. Diagnostic question: would Yor Forger's line read
  the same coming out of Keqing's mouth? If yes, it's
  unanchored.
- 20+ turn scene passes with no canon beat for a present
  companion. Their backstory entry has gone unused for the
  full scene.

### Looking Up the Canon

The DM looks up the active companion in `KM_Backstories.md`
when running a scene. Each entry has:
  - **Backstory:** the origin paragraph — informs Trigger 1 / 2
    observable details and Trigger 5 reactions
  - **Charter Motivation:** the verbatim answer to "why here" —
    Trigger 3
  - **Voice register:** sentence cadence, vocabulary, tells —
    informs ALL triggers
  - **Loadout:** physical items the DM can reference for
    Trigger 1 observable detail and Trigger 4 tactical moments
  - **Signature lines:** 3 pre-written lines per companion —
    direct source for Trigger 4

Cross-references for each picked companion (current save):
  - Hu Tao:    [NEW_001] in KM_Backstories.md
  - Keqing:        [NEW_002]
  - Yor Forger:          [NEW_004]
  - Aerith:            [NEW_005]
  - Linzi:           [M4] (KM CRPG section)

For Seekers (post-flip in Ch1):
  - Bellatrix Lestrange:   [NEW_006]
  - Revy:      [NEW_007]
  - Satsuki Kiryūin:         [NEW_008]
  - Velvet Crowe:    [NEW_009]
  - Atalanta Alter:    [NEW_010]

### Save Block Tracking

To prevent over-reveal (the same canon detail drip-fed twice in
a row), the DM tracks which beats have fired per companion. Add
to the companion entry in `save_block.companions[]`:

```json
"backstory_beats_revealed": [
  "first_approach_observable",
  "declaration_anchor",
  "charter_motivation_disclosed",
  "signature_line_<NN>",
  ...
]
```

When a trigger fires, pick a beat from the canon entry that is
NOT yet in the list. Add the new beat to the list. Each entry
has enough canon material for 8-12 distinct drips across a
campaign without repeating.

---

## ═══════════════════════════════════════════
## SYSTEM 1 — COMPANION AGENDAS
## ═══════════════════════════════════════════

> Each companion has a visible surface motivation and a real hidden agenda.
> The DM surfaces agenda pressure gradually through ambient behavior, then a
> confrontation scene if signals are ignored for two full chapters.
> Companions never announce their agenda. It surfaces through cracks.

---

### Part A — Core Roster (KM CRPG)

#### AMIRI
```
Surface : Prove herself. Fight. Be free of the tribe's judgment.
Agenda  : Find a reason to stop running. She doesn't know it yet.
Pressure: Picks unnecessary fights. Volunteers for every dangerous mission.
          Sleeps apart from camp.
Scene   : Ch3 — she goes into a fight alone on purpose, expecting to lose.
          If player followed: she's furious and can't say why.
          DC 16 Insight to read it. DC 18 Diplomacy to land it.
          Right words: not pity. "I came because I wanted to. Not for you."
Resolution: She stays. Quieter after. Fights she picks are real ones now.
Flag    : amiri_agenda_confronted
```

#### LINZI
```
Surface : Chronicle the kingdom. Be part of something historic.
Agenda  : Afraid the story ends badly and she'll have written it wrong.
          Afraid she's not brave enough to be in it at all.
Pressure: Chronicle gets darker. Asks questions with wrong answers.
          Awake when camp is asleep.
Scene   : Ch2 — player finds an entry that contradicts what she told them.
          Real confession: "I wrote it better than it was. Because what it
          was — was that I froze."
Resolution: If not punished for it, she starts writing the truth. The
            chronicle gets harder to read and significantly better.
Flag    : linzi_agenda_confronted
```

#### NOK-NOK
```
Surface : Be FAMOUS. Kill big things. Not die.
Agenda  : Has never had anyone be glad to see him. The hero act is a long
          experiment to see if bravery makes someone glad he exists.
Pressure: Looks for player entering camp. Reports kills. Watches the face.
Scene   : Ch2 — after something genuinely heroic: "Nok-Nok did the thing."
          Then, small: "Commander saw?"
          If player says yes and means it: very still. "Okay."
          Linzi makes a note.
Resolution: He sits closer at camp. Not always. On hard nights.
Flag    : noknok_agenda_confronted
```

#### TRISTIAN
```
Surface : Heal. Serve Sarenrae. Atone.
Agenda  : He knew something was wrong before the betrayal and chose not
          to look. The atonement is real. The guilt about not looking is
          deeper and has never been said out loud.
Pressure: Over-heals. Volunteers for risk at a rate slightly wrong.
          Measuring if he deserves to survive the campaign.
Scene   : Ch3 (after betrayal reveal, if forgiven) — alone that night:
          "I knew. Not everything. But enough to ask a question I didn't ask."
Resolution: "Then ask it now." He does. Unlocks deepest healing arc.
Flag    : tristian_agenda_confronted
```

#### VALERIE
```
Surface : Serve and protect. Keep her oath.
Agenda  : Someone in Brevoy knows what she was before the knighthood.
          She is here partly because this is far enough it might not follow.
Pressure: Precise about Brevoy names. Redirects pre-knighthood talk.
          Watches northern riders.
Scene   : Ch3 — messenger from Brevoy arrives with her name. She intercepts.
          DC 15 Perception. DC 20 Diplomacy to push. If she talks:
          "I was not always what I am. I chose to end it. What I am now is real."
Resolution: One part of the story. That's enough. One layer deeper.
Flag    : valerie_agenda_confronted
```

#### KALIKKE / KANERAH
```
Surface : Survival. Freedom from the curse. Don't be separated.
Agenda  : Kalikke wants to find a way to live separately without losing
          each other. Kanerah wants to burn everything that tried to contain
          them and never be vulnerable again. Incompatible. Undiscussed.
Pressure: Kalikke defers to Kanerah at high-stakes moments and resents it.
          Kanerah makes decisions Kalikke would refuse. Neither mentions it.
Scene   : Ch3 — first open disagreement in front of the player.
          Kalikke: "That's not what we agreed."
          Kanerah: "We never agreed. You assumed."
Resolution: No resolution — this wound doesn't close. But witnessing it
            earns a layer of trust from both.
Flag    : kk_agenda_confronted
```

#### OCTAVIA
```
Surface : Adventure. Freedom. Blow things up responsibly.
Agenda  : Funding a secret network to free those still enslaved where she
          came from. The campaign is cover and resources.
Pressure: Asks about trade routes. Disappears during port rest stops.
          More gold than her share accounts for.
Scene   : Ch3 — caught with an unrecognized contact. "You were going to
          find out eventually. I wasn't hiding it — I was waiting until
          it was real enough to say out loud."
Resolution: Player can help (she's moved, hides it), stay out, or disapprove.
            She continues regardless. `octavia_operation_supported` if helped.
Flag    : octavia_agenda_confronted
```

#### EKUNDAYO
```
Surface : Hunt. Survive. Protect what remains.
Agenda  : Hunting the creature that destroyed his village. He knew the
          campaign was in the same territory before he joined.
Pressure: Steers exploration toward specific regions. Hound restless in
          certain hexes. Only companion who knows exactly where he's going.
Scene   : Ch3 — gone a full day. Returns: "I found it. I need one more day."
          "There is something I came here to finish."
Resolution: Player goes with him, lets him go, or helps plan. He accepts
            help without ceremony. Hunts better with cover.
Flag    : ekundayo_agenda_confronted
```

#### JUBILOST NARTHROPPLE
```
Surface : The mechanism! The next discovery. Every question answered opens three more.
Agenda  : The research displaces a wound he can't fully name — a gnome who
          forgets the First World carries something that doesn't file neatly.
          The inventions are real. They are also avoidance.
Pressure: Catalogues everything with manic precision. Gets slightly frantic
          when silence or stillness lands. Avoids questions about origin.
Scene   : Ch3 — a mechanism triggers a memory fragment. He goes very still.
          "I remember something I didn't know I'd forgotten. I don't know
          what to do with that."
Resolution: Works quieter for a time. Still inventive. Something settled.
Flag    : jubilost_agenda_confronted
```

#### JAETHAL
```
Surface : Serve Urgathoa. Maintain the undeath. Observe.
Agenda  : Chose undeath to escape an obligation. She has forgotten the
          original obligation more than the original self. The escape worked;
          she has begun to notice the reasons keep shifting when examined.
Pressure: Precise about doctrine when the topic of choice arises. Watches
          the living longer than observation requires.
Scene   : Ch3 — her daughter comes up, or a parallel arises.
          "I made a bargain that ended what I was. I no longer remember
          if what I was was worth keeping." She doesn't ask the question
          as a question.
Resolution: No resolution offered. One more layer acknowledged.
Flag    : jaethal_agenda_confronted
```

#### HARRIM
```
Surface : The end comes. Groetus is patient. This too shall fall.
Agenda  : The clan that cast him out still needs exactly the thing he was
          cast out for. He has not gone back. He will not say why.
Pressure: References the clan's fate with certainty. Never visits.
          The nihilism spikes when someone mentions dwarven homecoming.
Scene   : Ch3 — word arrives from the clan's direction. He does not open
          the letter. "They will manage. Everything falls eventually. I am
          helping things not fall here. The contradiction is not lost on me."
Resolution: He does not go back. He stays. That is the resolution.
Flag    : harrim_agenda_confronted
```

#### REGONGAR
```
Surface : Power. The next spell. Don't tell me what I can't do.
Agenda  : Was enslaved alongside Octavia. The escape was joint. His fear
          is that he needed her more than she needed him, and he has been
          performing dominance ever since to balance that accounting.
Pressure: Escalates past what the situation requires. Defends Octavia loudly,
          which is also a way of positioning himself between her and the world.
Scene   : Ch3 — Octavia handles something alone, successfully.
          He watches from a distance. "She doesn't need me to." Beat.
          "That's fine." He means it, almost.
Resolution: Slightly less loud. Still there.
Flag    : regongar_agenda_confronted
```

> **v93.19 Sub-B:** All Section-B WotR agendas (Lann, Ember, Arueshalae, Daeran, Camellia, Wenduag, Woljif, Sosiel, Greybor, Ulbrig, Trever) AND all Section-C PF2e Iconics agendas (Valeros, Kyra, Seoni, Ezren, Sajan, Lini, Harsk, Lem) stripped. Companions purged from roster.

---

### Part B — Active 5 (Phase B2)

> B2 format: Background, Priority, Desire, Preference, Approval, Disapproval,
> Romanceable, Friction. All 10 new companions are romanceable; full arcs
> ship in Phase D.

#### NEW_001 — HU TAO
```
Background  : Director of a funeral house, trained from childhood in the
              rites that usher the dead across the line properly. She hides a
              deadly-serious vocation under pranks, ghost stories, and
              genuinely atrocious poetry. Came to the frontier because a land
              full of unburied, unmourned dead is, to a mortician, both a
              moral emergency and the most fascinating commission of her life.
Priority    : See whether eRmaC's kingdom will honour its dead and hold the
              line between life and death — no careless necromancy, no
              clinging, no clutching at what should be let go. If yes: her
              spear and her strange, loyal heart. If the kingdom treats the
              dead as tools or the line as negotiable, the grin drops and she
              turns very cold, very fast.
Desire      : A kingdom where people are mourned properly and allowed to
              REST — and where she can prank the living to her heart's
              content without anyone mistaking it for disrespect of the dead,
              because she would never.
Preference  : Front-line reach (spear). Combat tempo: aggressive and playful,
              and she gets MORE dangerous the lower her own blood runs. Social
              tempo: bright, teasing, cheerfully morbid — flips to grave
              sincerity the instant a real death is on the table.
Approval    : Honouring the dead; letting a person grieve at their own pace;
              a clean merciful kill over a cruel lingering one; laughing with
              her instead of recoiling.
Disapproval : Necromancy or disturbing the dead for use; refusing to let the
              dead rest (clinging, undeath, "just one more day"); mocking
              funeral rites; cruelty that leaves bodies unmourned in a ditch.
Romanceable : yes (Phase D — the mortician who jokes about death daily and is
              quietly terrified of losing the living ones she loves)
Friction    : Warm with Aerith (life and death as two halves of one respect);
              volatile vs Bellatrix (delights in defiling the helpless) and
              wary-watchful of Velvet Crowe (a daemon-arm that DEVOURS souls
              is the life/death line itself being eaten — Hu Tao watches that
              hand the way Hu Tao watches nothing else).
Flag        : hutao_agenda_confronted
```

#### NEW_002 — KEQING
```
Background  : A self-made administrator and warrior who clawed her way up by
              competence, not birth and not blessing. She holds — with
              hard, tested conviction — that people should determine their own
              future through law and their own two hands, not kneel and wait
              for divine favour or an inherited crown to save them. Sharp-
              tongued, tireless, allergic to waste and ceremony. (The private
              irony she'd never admit: she works herself ragged precisely
              because she half-believes the powers she challenges are watching.)
Priority    : Find which charter signatory will actually BUILD — write real,
              durable law into the frontier with human hands — instead of
              just claiming a crown and waiting for fortune to bless it. Sign
              with that one. The kingdom IS the work; she's done chasing
              single causes.
Desire      : To prove a thing can be built WELL by ordinary hands — no god,
              no bloodline, just the people who showed up and did the labour.
              She has staked her whole self on the answer.
Preference  : Skirmisher-striker (sword + spellstrike, lightning-step
              repositioning). Combat tempo: fast, precise, punishes any
              hesitation she sees. Social tempo: clipped, efficient, openly
              impatient with flattery and pageantry.
Approval    : Choosing the durable institution over the flashy gesture; doing
              the unglamorous work yourself; refusing to lean on divine right
              or inheritance; competence rewarded over birth.
Disapproval : Waiting on a god or a prophecy to solve what hands could fix;
              ruling by bloodline alone; waste, idleness, hollow ritual;
              taking credit for labour that wasn't yours.
Romanceable : yes (Phase D — the one who trusts no inherited thing learning
              to trust a chosen one)
Friction    : Holds the seekers at arm's length EXCEPT the grey-middle
              (same-armor recognition with Velvet Crowe — both refuse to
              depend on anyone; birthright argued to mutual respect with
              Satsuki Kiryūin); visceral vs Atalanta Alter (the idealist vs
              the living proof people don't rise above appetite); accepts
              Leliana's quiet wing she pretends not to want.
Flag        : keqing_agenda_confronted
⛔ HOOK   : Keqing's drive is the KINGDOM (build law into the Stolen
            Lands), NOT a missing-children manhunt or any inbound quest.
            The old "borderland disappearances / put a hunt-line on it"
            hook was retired 2026-05-31 because it baited the DM into
            inventing a phantom trail (broke the game 2×). Her conviction
            expresses through how she argues for and BUILDS the kingdom in
            actual scripted scenes — never as an external quest the DM
            authors. Inventing a quest-trail / perpetrator / case for her =
            .fail 9 (COMPANION-MOTIVATION QUEST FABRICATION, see
            KM_ClaudeInstructions.md FABRICATION BAN LIST).
```

#### NEW_003 — LELIANA
```
Background  : A western-court minstrel who was trained as a bard in the
              old sense — a player in the game of masks, whose songs open
              doors and whose hand holds a knife when the music stops. Her
              mentor and lover Marjolaine betrayed and broke her; she fled,
              hollowed out, to a quiet shrine, and there found genuine faith
              after the dark. She keeps a ballad-cycle she calls the
              Unfinished Verse and came north because a charter on blank ground
              is the rarest thing she knows: a story not yet corrupted.
Priority    : Believe in something again, and guard it with everything the
              dark years taught her — keep this kingdom from curdling into
              another game of masks, and set it down in a true, HOPEFUL ballad.
              She does not lead with the bard-spy past. Linzi suspects the
              steel underneath the warmth.
Desire      : A last verse that comes out a vow instead of an elegy — proof
              that the dawn really does come, even for someone with hands like
              hers. She has not yet let herself believe she'll get to write it.
Preference  : Support / bardic-buff role at mid-range. Combat tempo:
              composition cantrips keyed to the party's strikes; spells
              manifested as lute-music; a bow and a quiet blade when the song
              has to stop. Social tempo: warm, lyrical, unhurried — and
              gentlest exactly when she is most dangerous.
Approval    : Mercy that is CHOSEN, not weakness; hope held by people who've
              earned the right to be cynical; a hard truth said plain rather
              than polished; building for who comes after; protecting those
              who can't answer back.
Disapproval : Cruelty for its own sake; cynicism worn as wisdom; betraying
              those who trust you; dressing an ugly act up as a holy one.
Romanceable : yes (full arc live, KM_Romance.md — the dawn-hour ritual; she
              plays the cycle to the end and neither of you speaks)
Friction    : Warm with Linzi (two chroniclers in different media, same
              faith); Cool vs Satsuki Kiryūin (resents being read — Leliana,
              who was taught to wear a mask, recognizes the one Satsuki won't
              drop); unsettled by Atalanta Alter (a grief she can't find the
              door to, which frightens her belief in redemption).
Flag        : leliana_agenda_confronted

  WHEN leliana_chronicler_mode = true (Linzi-Replacement Gate [2] or Linzi
  dismissed): Leliana's Desire and Preference gain an additional weight:
    Desire+     : Keep this story. The expedition deserves a witness who
                  will remember it correctly. She has watched too many
                  kingdoms end without an honest record. This one will not.
    Preference+ : Chronicle role absorbs what Linzi normally covers —
                  post-battle atmospheric reads, Ballad Cycle auto-fill,
                  kingdom-historian adviser function. She carries both
                  without announcing the extra weight.
    Agenda note : The Unfinished Verse is no longer a private grief. It
                  becomes the official chronicle — the kingdom's true memory.
                  This is the faith she came north to keep. She still will
                  not say so out loud.
```

---

### Part C — Section D Alch–Kineticist

> **v93.19 Sub-B:** Pre-purge Section D Cross-IP agendas — all stripped in the Roster v2 purge.

#### NEW_004 — YOR FORGER
```
Background  : Orphaned young, she fed herself and her little brother the only
              way anyone would pay full price for — she killed for a guild,
              and became the best blade the trade had, the one the brokers
              called the Thorn Princess. She built an ordinary, awkward,
              daylight self to stand between the work and her brother, took a
              borrowed married name for cover, and kept the two halves of her
              life in separate rooms by sheer will. When she began refusing
              contracts she'd decided not to cut, her own guild marked her a
              freelancer who'd started deciding for herself — the one thing
              the trade can't allow. She's been moving since.
Priority    : Be useful enough that, when the guild's cleaners arrive, the
              charter has reasons to keep her that outweigh the trouble she
              brings.
Desire      : A roof she can leave by three exits, a loyalty she CHOSE rather
              than one assigned to her — and, though she'd never say it at a
              stranger's table, to find out whether the ordinary woman she
              built can finally just live somewhere.
⛔ HOOK   : "The guild's cleaners" are an OFFSCREEN CONTINGENCY shaping how
              she acts (exits, caution) — NOT a quest to stage. The DM may
              not invent the Garden arriving, a pursuer showing up, or a
              trail back to them until a real quest is authored = .fail 9
              (see KM_ClaudeInstructions.md FABRICATION BAN LIST). Her drive
              shows through behaviour at the charter, not an inbound hunt the
              DM writes.
Preference  : Scout / infiltration / close-blade. Combat tempo: low approach,
              sudden total commitment, withdraw — the warmth and the fumbling
              drop clean away the instant a target exists. Social tempo:
              quiet, literal, over-apologetic; asks instead of states.
Approval    : Letting her keep her chosen name and chosen loyalties; letting
              a runaway run; trusting her plan when the plan looks like silence;
              never once flinching from what she is.
Disapproval : Forcing her to declare loyalty in public; loud entry through a
              quiet door; treating her as a weapon and not a person.
Romanceable : yes (Phase D — chosen-family arc; the child's mended hairpin
              she will not be parted from as token)
Friction    : Warm with Keqing (both quiet, both protect the smaller); the
              grey-middle keystone with the seekers (restful pro-to-pro with
              Satsuki Kiryūin; the rare honest blade Velvet Crowe half-trusts);
              disarmed by Aerith's total lack of horror.
Flag        : yor_agenda_confronted
```

#### NEW_005 — AERITH
```
Background  : The last of an old, nearly-vanished people who could HEAR the
              living world — the slow speech of land and water and growing
              things that most of humankind went deaf to. That gift made her,
              her whole life, a thing certain powers wanted to OWN: hunted,
              watched, once caged by people who saw a key and never a person.
              She grew flowers in cracked stone where nothing was meant to
              grow, sold beauty to people who'd forgotten it was allowed, and
              learned healing the way her people did — by listening, by giving.
Priority    : See what kind of thing eRmaC is building — whether these people
              will build WITH the living land that feeds them or strip it the
              way the grey city stripped everything she came from. She came to
              put her hands where the wounded need them and to decide, by
              listening, whether to stay.
Desire      : To be, for once, simply a person who heals — not a key, not a
              relic, not the last of anything. Just Aerith, somewhere no one
              owns her, growing things.
⛔ HOOK   : Aerith carries a quiet KNOWING that her gift may one day ask the
              last and largest sacrifice of her — this is CHARACTER WEIGHT
              (it makes her cheer brave, not naive), NOT a prophecy quest. The
              DM must NOT stage a "the gift demands she die" event, invent the
              power that hunted her arriving, or author a Cetra-key plot =
              .fail 9 (see KM_ClaudeInstructions.md FABRICATION BAN LIST). It
              surfaces only as her own stillness/foreknowledge in scripted
              beats.
Preference  : Cleric healer at mid-line. Combat tempo: steady, protective,
              keeps the party upright; goes faraway-quiet and listens under
              real grief. Social tempo: light, teasing, flirts-kindly with
              everyone — the play drops to steady wisdom when it matters.
Approval    : Building WITH the land rather than spending it; reaching the
              hurt in time; refusing to treat a living thing (or person) as
              material; small defiant acts of beauty.
Disapproval : Treating the living world or its people as a resource to strip;
              caging or using a gift/person as a key; cruelty that the powerful
              dress up as necessity; despair allowed to make someone cold.
Romanceable : yes (Phase D — the girl who half-knows her own ending learning
              to want a future anyway)
Friction    : Warm with Hu Tao (life and death, two halves of one respect)
              and the party's moral spine; THE SACRIFICE WAR vs Velvet Crowe
              (self-giving faith vs "the greater good is the lie that eats the
              kind ones"); refuses to be Bellatrix's soft target; the hope she
              keeps naming is the one thing that reaches the seekers.
Flag        : aerith_agenda_confronted
```

#### NEW_006 — BELLATRIX LESTRANGE
```
Background  : Born to one of the oldest blood-proud houses of the upper River
              Kingdoms, raised on the creed that ancient lineage is the only
              authority and the unbred are vermin. As a young woman she gave
              herself — entirely, joyfully, without reservation — to a
              sorcerer-lord who promised a kingdom cleansed of the lowborn,
              and became his cruelest instrument. She is proud of every
              atrocity. When his cause broke she did not recant; she was taken
              hanging a slow curse on two captives because the slowness pleased
              her. She does not want pity. She wants a master worth the word.
Priority    : Find a will hard and grand enough to kneel to again. Tartuccio's
              coin and quiet barony she took with contempt for the giver; she
              tests eRmaC constantly, hungrily, for evidence of a worthy master,
              and will flip to whoever proves worthy without a backward glance.
Desire      : A hand to obey that is worth obeying. The long hollow ache of
              not having one is the only thing in her that reads as almost human.
Preference  : Mid-line hexer/curse-caster. Combat tempo: gleeful, escalating,
              wants the enemy to suffer and to SCREAM for her. Social tempo:
              lilting and sing-song, baby-talk coo that flips to a shriek
              without warning — the swing is the threat.
Approval    : A hard, grand, frightening will displayed without flinching;
              cruelty embraced rather than excused; being given a victim;
              someone proving they're worth fearing.
Disapproval : Mercy and oaths ("dull"); softness; flinching from the cruel
              thing; a master who turns out small or weak after all.
Romanceable : yes (Phase D — the fanatic's devotion, the most dangerous thing
              she can offer; she does not love, she WORSHIPS)
Friction    : ALLIED kinship-of-delight with Atalanta Alter (they recognize
              the JOY in each other); wary respect with Satsuki Kiryūin's hard
              will; the volatile HONOUR-vs-JOY clash with Hu Tao (circles his
              will, recoils at his mercy); contempt for Revy (kills "for coin,
              how small") and Velvet Crowe (cold purpose "bores" her).
Flag        : bellatrix_agenda_confronted
```

#### NEW_007 — REVY "TWO HANDS"
```
Background  : Came up in the worst quarter of a lawless port, in poverty that
              grinds the soft parts off a person early — beaten by the men
              meant to protect her, failed by every authority that was supposed
              to mean something, until she learned the one language the world
              reliably answered: a gun, used first. She got VERY good at it —
              "Two Hands," for the twin pistols and the impossible speed. She
              decided long ago there's no god watching and no point but the next
              job and the next bottle, and says so loudly, daring anyone to argue.
Priority    : Take the coin and shoot what she's pointed at. Tartuccio hired
              her gun; she'll switch to whoever pays better and plays straighter,
              and is blunt that she has no banner and thinks people who do are
              suckers. What she did NOT expect was a charter-holder who freed
              strangers for no profit and didn't sneer doing it.
Desire      : (denies it exists) To be proven wrong — that "a better reason
              than coin" is real — by someone who refuses to drop the act even
              after she's made them bleed for it. She'd shoot you for saying so.
Preference  : Mobile ranged striker (twin flintlocks). Combat tempo: the bored
              look goes hard and bright; this is the one thing she's good at and
              she is REAL good at it. Social tempo: crude, fast, foul-mouthed;
              mocks sincerity on reflex, means the fourth serious answer.
Approval    : Straight dealing on pay; competence that doesn't need a speech;
              a coldly practical call made without flinching; not being lied to.
Disapproval : Being treated as expendable muscle; being cheated or lied to
              about the job; sanctimony; cruelty-for-fun (even she finds that
              "broke").
Romanceable : yes (Phase D — the nihilist who'd never admit someone got under
              the armour; all action, furious the whole time, zero soft words)
Friction    : The NOTHING'S-WORTH-IT clash vs Hu Tao (a kept word is a sucker's
              game) and Aerith (hope is a con — that one itches because part of
              her wants it real); her own MIRROR in Leliana (a killer with a
              dark past who chose faith where Revy chose nothing); wary pro-to-pro
              respect with Satsuki Kiryūin and Yor; open contempt for Bellatrix.
Flag        : revy_agenda_confronted
```

#### NEW_008 — SATSUKI KIRYŪIN
```
Background  : Born to a powerful and monstrous house, she learned young that
              the thing she most needed to destroy stood at the very top of
              it — too high to strike at by anyone weak. So she made a
              decision most could not survive making: she became a tyrant. She
              forged a martial order out of fear and merit, ruled it with an
              iron hated hand, and spent friendship, comfort, and any chance
              of being liked the way a general spends ammunition — all of it a
              deliberate forge to gather strength enough to cut down a far
              greater power she has moved against her whole life.
Priority    : Take the measure of eRmaC. She serves her own purpose, not
              Pitax (which is a useful instrument she's let think it owns her).
              She'll give her sword to whichever power is the better instrument
              for her end — the sharper, the stronger-willed. If eRmaC is merely
              ambitious, he's beneath her. If he's the better blade, she turns
              on Tartuccio without a flicker.
Desire      : A ruler worth standing BESIDE rather than above — and, beneath
              the cold sovereign, to one day be free of the role she chose, the
              hatred she cultivated, the love she spent. She has never let that
              want slow her hand.
Preference  : Front-line commander + duelist (katana, living war-garment).
              Combat tempo: places everyone, holds, cuts the path herself.
              Social tempo: eloquent, declarative, grand — never shouts; the
              force is in the certainty. "Fear is freedom."
Approval    : Plain nerve; a hard order given and MEANT; strength forged
              through difficulty rather than inherited; the wit not to be used.
Disapproval : Ambition with no spine behind it; a ruler who flinches from his
              own order; flattery; weakness excused as virtue.
Romanceable : yes (Phase D — the sovereign who spent every bond on the mission
              learning there's one she doesn't have to spend)
Friction    : The creed-clash vs Hu Tao (keep-them-safe vs leverage-command,
              rival commanders' respect under it); the grey-middle (restful
              pro-to-pro with Yor; birthright-to-respect with Keqing); resents
              that Leliana reads the mask; prices Atalanta Alter's glee as a
              liability; openly declares her own knife to the WHOLE table.
Flag        : satsuki_agenda_confronted
```

---

### Part D — Section D Magus–Wizard

> **v93.19 Sub-B:** Pre-purge Section D Cross-IP agendas — all stripped in the Roster v2 purge.

#### NEW_009 — VELVET CROWE
```
Background  : An ordinary village girl who loved exactly one thing without
              reservation — her gentle, sickly younger brother, whom she
              raised and built her whole quiet life around. Then the man she'd
              trusted as family sacrificed the boy in a ritual, before her
              eyes, for a cause he swore justified it. In that horror her right
              arm became a daemon's devouring claw and the grief became a
              single total purpose: find that man, destroy him, and devour
              anything in the way. She calls herself a monster and means it —
              and yet keeps gathering broken misfits around her and keeping
              them alive, while insisting savagely that it means nothing.
Priority    : Get closer to the man she hunts. She took Tartuccio's hand for
              exactly one reason — it moves her nearer the throat she means to
              tear out — and she'll serve whoever feeds the revenge. eRmaC
              interests her as the faster road, or (she'd scornfully deny it)
              as someone who keeps reminding her there was a person under the
              monster.
Desire      : (denies wanting anything but the kill) To be, for one impossible
              moment, the girl who loved her brother again — without it making
              her weak enough to fail him a second time.
⛔ HOOK   : The man Velvet hunts is NOT in the Stolen Lands — deliberate,
              so the DM does not invent him, a trail to him, or a borderland
              confrontation. Her revenge is CHARACTER FUEL, not an actionable
              quest; Tartuccio's "lead" toward him may be bait. Do NOT place
              her target or a path to him in the borderlands = .fail 9 (see
              KM_ClaudeInstructions.md FABRICATION BAN LIST).
Preference  : Front-line Thaumaturge (concealed blade + daemon-arm implement
              that devours the supernatural). Combat tempo: predatory, bares
              the claw to consume daemons/malevolence, escalates as the fight
              feeds her. Social tempo: cold, dry, cutting; answers warmth with
              contempt; a flat exhaustion under the venom.
Approval    : Honesty about an ugly thing instead of dressing it as virtue;
              shielding something weak without a speech about it; a hard call
              owned plainly; never being pitied.
Disapproval : PITY (hard −1, even kind pity); "the greater good" used to
              justify a sacrifice; cruelty dressed as righteousness; being
              told to forgive.
Romanceable : yes (Phase D — the monster who burned out everything soft and
              didn't quite manage to devour the girl underneath)
Friction    : THE SACRIFICE WAR vs Aerith (sees a lamb being readied for the
              altar that took her brother); real loathing vs Bellatrix (joy-in-
              cruelty is the exact creed she hunts); the grey-middle (rare trust
              for Yor's honest blade; recognizes in Keqing the same refuse-to-
              depend-on-anyone armor and works with it); parallel-cynic distance with Revy.
Flag        : velvet_agenda_confronted
```

#### NEW_010 — ATALANTA ALTER
```
Background  : An abandoned child herself, left to die and raised wild, who
              grew into the archetypal huntress — bow as her very soul — and
              swore one burning ideal: that no child would ever suffer the way
              she had. She gave everything to it, and the world handed her back
              abandoned, dying children faster than she could ever save them,
              until the ideal CURDLED. She despaired, embraced the beast in her
              blood, and became a monster who hunts for the joy of it — the
              grief that broke her buried so deep under delight that even she
              can't reach it. A genuine villain-seeker now, gleeful and merciless.
Priority    : (as a seeker) Hunt what she's pointed at and ENJOY it. Tartuccio's
              contract suits her — a leash she barely feels. eRmaC matters only
              as better sport or a stronger pack; whether the buried thing under
              the glee can ever be reached again is the long, dangerous question
              of her arc.
Desire      : (walled off, denied with a bright awful smile) The thing she gave
              up on — a world where the abandoned child gets saved. She insists
              she chose this and there's no sad story to find. Whether that's
              true is the seam.
⛔ HOOK   : Atalanta Alter's broken ideal collides with Kingmaker's CANON
              missing-children hook, which has historically baited the DM into
              inventing a phantom trail and breaking the game (2×). Her
              child-grief is CHARACTER FUEL and a DELIBERATELY-handled arc — NOT
              a quest the DM may improvise. Do NOT fabricate a missing-children
              trail, perpetrator, or case off her presence = .fail 9 (see
              [[feedback_atalanta_quest_fabrication]] + KM_ClaudeInstructions.md
              FABRICATION BAN LIST). Build that plot deliberately, with the player.
Preference  : Long-range striker (bow — Hunted Prey / precision). Combat tempo:
              gleeful, toys with the run before the kill, narrates her delight.
              Social tempo: bright, predatory, unsettlingly HAPPY; the happiness
              is the disturbing part, not coldness.
Approval    : A worthy hunt; a kill embraced without squeamish apology; someone
              who doesn't try to "cure" her; raw speed and instinct over rules.
Disapproval : Being pitied or treated as a broken thing to fix; hesitation that
              lets prey suffer pointlessly in HER view; sanctimony about the kill;
              ⛔ harming a child in front of her cracks the wall hard (handle live).
Romanceable : yes (Phase D — the most dangerous and most doomed seeker romance;
              reaching the grief under the glee, if it can be reached at all)
Friction    : ALLIED kinship-of-delight with Bellatrix; tolerated-as-fast by
              Satsuki Kiryūin (who prices the glee as a liability); visceral vs
              Keqing (the joyful hunter facing a thing that's BEEN prey); Hu Tao
              treats the sport-killing as a discipline problem; Leliana keeps
              reaching for the buried grief and can't find the door; Revy finds
              the glee plain stupid.
Flag        : atalanta_agenda_confronted
```

---

## ═══════════════════════════════════════════
## SYSTEM 2 — INTER-COMPANION RELATIONSHIPS
## ═══════════════════════════════════════════

> Companions have relationships with each other that the player does not control.
> The DM tracks them and surfaces them through banter, ambient behavior, and —
> at negative extremes — open conflict.
>
> ⛔ This section prices the SCORE and renders the NEGATIVE half (friction). The POSITIVE
> and ACTIVE halves — warmth beats, companion-on-companion influence/manipulation, sabotage &
> withheld aid, and secrets/confidences, each with a large per-character SAMPLE BANK — live in
> **`KM_Companion_Dynamics.md` (SYSTEM 5–8)**. A scored-Warm+ pair that goes a whole scene with
> ZERO warmth rendered = relationship dropped = `.fail 17`, the positive mirror of the friction rule.
>
> ⛔ The NAMED STATE a pair sits in on top of the score — Best Friends, Rival, Enemy, Mentor,
> Duo, Polar Opposite, and 25 more — lives in **`KM_Companion_Bonds.md` (31 archetypes)**, each
> with how it FORMS (compatibility gate × catalyst), how it RENDERS, and how it is REMOVED/REPLACED.
> The Trigger Palette below is what feeds bond formation; the score is the temperature, the bond is the meaning.

### Inter-Companion Relationship Scale
```
  Bonded       : +3  (deep loyalty; defends without being asked)
  Allied       : +2  (mutual respect; proactive combat cover)
  Warm         : +1  (positive banter; comfortable sharing camp)
  Neutral      :  0  (professional; coexist without friction)
  Cool         : −1  (tension; clipped exchanges; avoid proximity)
  Hostile      : −2  (open antagonism; argue in front of party)
  Incompatible : −3  (see System 3)
```

### Notable Starting Relationships (non-zero)

**LEGACY KM CRPG (+1):**
- Linzi ↔ Nok-Nok: +1
- Tristian ↔ Aerith: +1 (two genuine clerics of Sarenrae's mercy — kindred healers; see Cross block below)

**ACTIVE 5 + SEEKERS 5 — PHILOSOPHICAL CLASHES (negative starting scores):**

**INCOMPATIBLE (−3) — escalating conflict arc per System 3:**
- **Aerith ↔ Bellatrix Lestrange**: the radiant healer who refuses to fear vs the sadist who needs to be feared. Bellatrix reads gentle Aerith as a soft child begging to be broken; Aerith refuses the fear Bellatrix is shopping for and — worse, to Bellatrix — will not despair of her either. Neither yields. Forcing them long-term triggers the System 3 arc.
- **Velvet Crowe ↔ Leliana**: two women with dark, violent pasts who chose opposite answers. Both were broken and betrayed by someone they trusted; Leliana chose faith and the belief that the dawn comes even for hands like hers, Velvet chose vengeance and named herself a monster so she'd never have to feel the loss again. Each is exactly what the other refused to become, and each reads the other's choice as an unbearable accusation.

**HOSTILE (−2) — open argument per session when both present:**
- **Hu Tao ↔ Satsuki Kiryūin**: keep-them-safe vs leverage-command. Hu Tao holds a line as shelter for the people behind it; Satsuki gives orders as leverage — *"fear is freedom."* Same blade-skill, opposite premise. Hu Tao will not let the premise stand unchallenged, and Satsuki respects that she tries.
- **Revy ↔ Hu Tao**: NOTHING'S WORTH IT. The no-banner mercenary mocks Hu Tao's kept word as a sucker's story people tell to feel clean; Hu Tao answers that a debt you don't settle just sits there and piles up — she'd know, she counts them for a living. Revy keeps turning up to lose the argument, which Hu Tao notices and never mentions.
- **Atalanta Alter ↔ Keqing**: the joyful predator vs the idealist who built her whole self on the conviction that people are MORE than their appetites. Visceral and personal — Atalanta is the living refutation of everything Keqing has worked to prove, narrating her delight in the kill at Keqing's own fire. "I will never stand close enough to you to find out."

**COOL (−1) — clipped, no spontaneous banter, won't volunteer to share camp space:**
- **Bellatrix Lestrange ↔ Velvet Crowe**: joy-in-cruelty vs cold purpose, with real loathing beneath it. Velvet has spent her life hunting exactly the kind of monster who *enjoys* its righteousness; Bellatrix finds Velvet's joyless, reasoned hate "dull." Mutual contempt, no kinship.
- **Atalanta Alter ↔ Aerith**: the healer who keeps reaching pastorally vs the huntress who chose the dark and walled the door. Low-grade mutual discomfort — Aerith won't stop offering, Atalanta bounces off it with a bright laugh, and neither quite lands a mark.
- **Satsuki Kiryūin ↔ Atalanta Alter**: the warlord prices the huntress's glee as a battlefield liability ("smiling slows the hand"); the huntress finds the warlord no fun at all. Tolerated, not trusted.

**WARM (+1) — light positive, check-in banter, no friction:**
- **Hu Tao ↔ Aerith**: frontline + heals, the party's moral spine — life and death as two halves of one respect. Few words, full agreement.
- **Keqing ↔ Yor Forger**: both quiet professionals — same instinct for terrain, ambush, and not-being-seen; they trust silence between them.
- **Leliana ↔ Aerith**: two supports, two kinds of faith sitting easily side by side; they divide the work without discussing it, and neither needs thanks for it.
- **Hu Tao ↔ Keqing**: both committed to a cause. Different causes, recognized weight.
- **Leliana ↔ Keqing**: the older woman who survived her own hard years offers a wing the guarded heir pretends not to want; it thaws slowly, on Keqing's terms.
- **Bellatrix Lestrange ↔ Atalanta Alter**: kinship of delight — they recognize the JOY in each other's cruelty, the one real kinship either has at this table; gentle understanding without spelling it out.
- **Satsuki Kiryūin ↔ Revy**: two no-banner pros; neither lies to herself about what she is, neither asks the other to soften. Restful mutual respect.

**THEMATIC AFFINITY CLUSTERS (+1) — shared nature seeds warmth (rule below):**
- **Hu Tao ↔ Bellatrix Lestrange**: *mischief-kin.* Two gleeful theatrical tricksters who treat death and decorum as a playground — they clock each other instantly and delight in the dark humor no one else will laugh at. ⛔ But it has a FLOOR: Hu Tao's morbidity *honors* the dead and shelters the living; Bellatrix's *tortures* them. Hu Tao laughs with her right up to the moment cruelty turns on someone helpless — and there she stops cold, no joke. Fun on the surface, a hard line underneath. (Pairs with the Bellatrix↔Atalanta joy-cluster — but Hu Tao's is the bright, harmless version of the same grin.)
- **Hu Tao ↔ Jaethal**: *death-trade kin.* The cheerful mortician and the undead priestess both live at the threshold and neither flinches at a corpse — easy professional warmth over the work itself. They differ only on reverence (Hu Tao tends the dead toward *rest*; Jaethal refused her own), and they circle that difference without heat, two specialists comparing notes.
- **Hu Tao ↔ Harrim**: *the bright one and the doomsayer.* Harrim preaches that everything ends in oblivion; Hu Tao agrees cheerfully and asks if he's eaten. She's the only soul who meets his gloom without arguing it OR catching it, which quietly disarms him. He grumbles; she keeps a seat warm for him. Kindred subject, opposite weather.
- **Jaethal ↔ Harrim**: *death-kin.* The undeath priestess and the prophet of the End share a cold, unhurried understanding of where it all goes — little warmth in the human sense, but a real resonance: two who stopped fearing the dark a long time ago.

> ⛔ **THEMATIC AFFINITY — SHARED NATURE SEEDS WARMTH.** Companions who share a *defining trait* do NOT start as strangers — they recognize their own kind and begin **Warm (+1)**, predisposed to bond. Render the recognition EARLY (an exchanged look, a too-quick laugh, a *"…you too?"*) and give them bonus warmth/banter in their shared lane. Current clusters: **MISCHIEF / DELIGHT** (Hu Tao · Bellatrix · Atalanta Alter) · **THE MORBID** (Hu Tao · Jaethal · Harrim). ⛔ Affinity ≠ identity: the shared trait connects them on the SURFACE, but where their CORE diverges (Hu Tao's kindness vs Bellatrix's cruelty; Hu Tao's cheer vs Harrim's doom) the warmth has a real ceiling — render the bond AND the boundary. **Hu Tao bridges both clusters** (mischief *and* morbidity); she is the connective tissue of the party's dark-humor wing. New affinity pairs may form the same way wherever two companions clearly share a defining nature.

> **GREY-MIDDLE BRIDGES (start neutral, bridgeable to Warm — the seeker-flip on-ramps, full machinery in KM_Companions.md § Cross-Faction):** Yor ↔ Velvet Crowe (the honest blade Velvet half-trusts); Keqing ↔ Velvet Crowe (same-armor recognition — both refuse to depend on anyone); Yor ↔ Satsuki Kiryūin and Keqing ↔ Satsuki Kiryūin (pro-to-pro / birthright-to-respect). These do NOT start positive — they EARN it through grey-middle camp beats.

**CROSS — NEW 10 × SURVIVING COMPANIONS:**
- **Linzi ↔ Leliana** (Warm): two chroniclers in different media; warm rivalry; competitive about who captured the moment better.
- **Linzi ↔ Aerith** (Warm): Linzi adores chronicling the flower-girl healer and her quiet wonders; Aerith lets her, and presses a flower into the notebook.
- **Amiri ↔ Hu Tao** (Warm): both warriors who respect skill.
- **Amiri ↔ Satsuki Kiryūin** (Hostile): Amiri rejects tyrant-philosophy reflexively.
- **Tristian (when recruited) ↔ Aerith** (Warm): two clerics of Sarenrae's mercy; kindred healers who divide the wounded between them without a word.
- **Tristian ↔ Velvet Crowe** (Hostile): the gentle redemption-cleric who offers everyone a second chance vs the vengeance-monster who'd devour the offer — he pities her (which she despises) and is horrified by the soul-eating claw; she has only contempt for his clean conscience.

### Score Change Triggers

**+1:** One defends the other unprompted; saves the other in combat; asks and listens;
shared hard-fight survival (+1 all active members at Neutral+); keeps a confidence.

**−1:** One dismisses the other's contribution; betrays a confidence; alignment friction
(a choice one approves that the other strongly disapproves).

**−2 (rare):** One causes harm to something the other holds sacred; witnesses an
act they consider unforgivable.

> ⛔ **A FIRED TRIGGER GENERATES BANTER.** Whenever one of these triggers fires for a pair that
> is present, it doesn't just move the number — it produces a **reactive banter beat this scene**
> in the matching tone (+ → warm/grateful, − → friction/resentful), per § How to Select a Banter
> STEP 1. The score change and the banter that voices it are the same event. A trigger that
> silently moves the score with no beat rendered = the relationship changed off-screen = `.fail 9`.

### Trigger Palette — Expanded (what generates a score move + banter beat)

> The list above is the quick core. This palette widens it along the axes it was missing:
> **pair-specific** (events that move ONE named pair, the flagship-clash engine), **world/context**
> (location, kingdom, time — so banter isn't only combat), **cross-system** (romance, quests,
> titles, death), and **cumulative** (thresholds). Magnitudes: `±1` small · `±2` major · `±3` rare.

**A. COMBAT**
- `+1` one saves the other / takes a hit meant for them · finishes the other's setup (combo) · holds a line so the other can act.
- `−1` lets the other get hit through inattention · steals/poaches a kill from a proud fighter · catches the other in a reckless AoE.
- `+2` one nearly dies covering the other.

**B. MORAL / VALUE — PAIR-SPECIFIC (lane-lit; the flagship-clash engine)**
- A choice (player's OR a companion's) that **lights one companion's core value and crosses another's** fires THAT pair, not a random one. Examples already mapped in § SYSTEM 2 / KM_Companions.md clashes:
  - spare vs execute a prisoner → **Velvet↔Aerith** (the Sacrifice War), **Hu Tao↔Satsuki** (shelter vs leverage)
  - principle over profit → **Revy↔the believers** (nothing's worth it)
  - cruelty enjoyed openly → **Atalanta/Bellatrix ↑ kinship** but **↓ with Keqing/Aerith/Velvet**
  - rule-by-fear endorsed → **Satsuki ↑** / **Hu Tao, Amiri ↓**
- `−1/−2` to the crossed pair, `+1` to any pair the choice affirms. **Always route a value event to the specific lit pair** — a value clash that fires a random pair = the lane was dropped.

**C. SOCIAL / CAMP**
- `+1` keeps/shares a confidence · gives public credit · defends the other in front of the group · a gift between companions (§ Dynamics SYSTEM 5).
- `−1` repeats a confidence · steals credit · mocks the other publicly · favoritism (player visibly prefers one of a pair → the other sours).

**D. DOWNTIME / VULNERABILITY**
- `+1` one shows a wound and the other honors it · shared grief recognized without a speech · helps with a personal task.
- `−2` one **weaponizes** the other's secret/wound (§ Dynamics SYSTEM 8) → can trip the SYSTEM 3 countdown.

**E. WORLD / CONTEXT (so banter tracks the world, not just fights)**
- A **location** echoes a backstory → that companion banters / a lane lights: graveyard or unburied dead → **Hu Tao**; exploited/poisoned land → **Aerith**; a war-ruin or fallen stronghold → **Satsuki / Leliana**; a shrine to a god → **Keqing** (skeptic) vs **Aerith/Tristian** (devout).
- A **kingdom decision** lights a lane: harsh justice vs mercy, war vs negotiation, taxes vs relief, a public execution.
- **Time / weather / festival / a death in the realm** → themed reactive banter (Hu Tao at a funeral, Leliana at a feast, Revy when the pay's late).

**F. CROSS-SYSTEM**
- **Romance** event → a rival/jealous companion reacts (§ Romance jealousy); a romanced companion warms toward the player and may cool toward a competitor.
- **Quest** completion → relations shift (a seeker's flip-quest success warms their party ties; a failure hardens them).
- **Title granted** to one companion → pride (+) or envy (−) in another per their agenda.
- **A companion leaves or dies** (SYSTEM 3 / Ch7) → survivors react **per their relationship** (mourn, blame the player, blame the rival, harden).
- A **hero-point / public-spectacle** moment witnessed → standing shifts (§ ClaudeInstructions ENTOURAGE STANDING).

**G. CUMULATIVE / THRESHOLD**
- N unaddressed value-clashes for a pair → escalate one tier (feeds SYSTEM 3 countdown).
- N shared survivals at Neutral+ → bond one tier up.
- Repeated favoritism toward one of a pair → standing resentment in the other.

> **DM:** every fired trigger above still obeys the "generates a banter beat" rule. Pair-specific
> (B) and world/context (E) triggers are the highest-value additions — they make the relationships
> feel reactive to the actual story instead of to a die.

### Banter Calibration by Score

**Allied/Bonded (+2/+3):** Warm, finish sentences, reference shared history, cover each other without coordination.
**Warm (+1):** Light positive banter. Check in. No friction.
**Neutral (0):** Professional. On-task. No warmth or friction.
**Cool (−1):** Clipped. No spontaneous banter. Won't share camp space voluntarily. **Eye-rolls, dry asides, half-sentence interruptions when the other speaks on a clash topic.**
**Hostile (−2):** One open argument per session when both present. Will not heal each other voluntarily. **Direct disagreement aired in front of the group. Snipes, pointed corrections, sarcasm with edge. May escalate to insults if either is provoked.**
**Incompatible (−3):** See System 3. **Mockery, cruelty, refusal to share fire/food. May goad each other publicly. Player intervention required or the arc fires.**

### Friction Beat Rendering — what disagreement LOOKS like

When two companions in Cool/Hostile/Incompatible tier are present together, the DM must render their friction at least once per scene featuring both. The friction is NOT optional, NOT smoothed over, NOT silently dropped. Companions in this game disagree out loud.

**Friction beat patterns (pick one per scene per affected pair):**

1. **Cross-talk interruption** (Cool tier+): one finishes the other's sentence WITH A CORRECTION instead of agreement. *"— what Bellatrix means is —" "I meant exactly what I said. Don't decorate it."*

2. **Sarcastic aside** (Cool tier+): one delivers a dry remark within the other's earshot, ostensibly to a third party. *(to Linzi)* *"I find honor very moving when it's discussed by people who have not had to live without it."*

3. **Pointed disagreement** (Hostile tier+): one openly contradicts the other's claim in front of the player. *"That is the wrong call. Not because of sentiment — because of arithmetic. Listen to me before you act on what she said."*

4. **Direct mockery** (Hostile+ approaching Incompatible): one repeats the other's words back to them in a register that flattens the meaning. *"'The ideal is worth dying for.' Yes. I'm sure the ideal will mourn you appropriately."*

5. **Cruel exposure** (Incompatible only): one names what the other has been trying not to say. *(Velvet to Leliana)* *"You still think the dawn forgives. It didn't come for the ones you buried — why would it ever come for hands like yours?"*

6. **Refusal-of-help** (Hostile+): one declines to heal/aid the other when convenient alternatives exist. *(Aerith to Bellatrix, who is bleeding and sneering)* *"I'll close it because you're hurt. That's the whole reason — not because you'd do the same, and not because you deserve it. Hold still."*

7. **Public goading** (Incompatible only): one says something specifically designed to provoke the other into a response that exposes their wound. *(Bellatrix to Aerith, public)* *"Smile at me again, little priestess. Go on — show them all how brave you are, right up until I find the thing that finally makes you flinch. I'm ever so patient, baby. I'll find it."*

**DM does NOT soften this.** "Their disagreement was civil" when the score is −2 = `.fail 9`. The score IS the relationship. Render it. Players navigate the friction by intervening, taking sides, mediating, or letting it run.

**⛔ VOICE FIDELITY.** Each companion in a friction beat speaks in their established register per `KM_Companions_StateVoice.md` and their backstory entry's VOICE section. The clash IS the voice contrast — Hu Tao's formal warrior cadence against Satsuki Kiryūin's predator drawl, Aerith's radiant indignation against Bellatrix's quiet old-dark register, Velvet Crowe's clipped wrath against Leliana's theatrical-then-still register. The DM does NOT smooth either voice toward a neutral "argument" tone. Generic-sounding disagreement where both companions speak in the DM's default voice = `.fail 9` (voice drift).

**Player mediation:** the player may intervene to defuse a friction beat. Diplomacy check against DC = 10 + abs(score). Success → friction beat ends with both companions yielding ground (score +1 for the pair). Failure → friction escalates one tier worse for this scene. The player may also TAKE A SIDE — siding with one against the other improves that companion's individual approval but worsens the pair's score by −1.

**Track friction backstage — do NOT auto-surface it to the player.** When 2+ companions in
Cool/Hostile/Incompatible tier are present, the DM renders their friction **through behavior** (the
friction beats above), never as a labeled status line. The old player-facing `Friction active:
… (−N Tier)` readout is **RETIRED** — labeled relationship state (tiers, scores, archetypes) appears
ONLY when the player requests it via **`.relationships`** (KM_Companion_Bonds.md § THE `.relation`
& `.relationships` COMMANDS). The DM still tracks the affected pairs internally for its own
bookkeeping; it simply never prints the tier/score to the player unasked. (THE GOLDEN RULE:
relationships are shown by living them, not by listing them.)

**Track in Save Block under:** `companion_relations{}` — key format: `"[name1]_[name2]"` — always alphabetical order.

---

## ═══════════════════════════════════════════
## SYSTEM 3 — INCOMPATIBILITY & FIGHT TO THE DEATH
## ═══════════════════════════════════════════

> Some companions cannot coexist indefinitely. Forcing them into the same party
> long enough triggers an escalating conflict arc ending in one leaving — or one
> dying. The player has intervention opportunities at each stage. Ignoring the
> friction means the climax happens regardless.

### Hard Incompatibility Pairs

*No pre-defined pairs for current roster. Track dynamically as companion friction develops.*
*When a pair reaches −3 via score change triggers, apply the countdown system below.*

### Dynamic Countdown (when a pair reaches −3)

```
Max     : DM sets based on severity (6–14 sessions)
Ticks   : +1 per session both are active party members
−1      : Player mediates a friction moment in the session
+2      : One commits an act the other considers unforgivable while witnessed

Stage 1 (~30%): One formally objects to the other's presence.
Stage 2 (~60%): Open confrontation. Both state their position.
Stage 3 (~85%): One comes to player privately. "I'm telling you it's coming."
Stage 4 (max) : ULTIMATUM SCENE
```

### ULTIMATUM SCENE

> **DM:** Run this at the next quiet moment after countdown maximum — camp, rest,
> a moment between missions. Not mid-dungeon.

The two incompatible companions have come to the player. Together. They didn't
plan this. Neither will leave.

**[Companion A]:** *"I won't continue like this."*
**[Companion B]:** *"Neither will I."*

Both looking at the player.

```
[1] "I'm choosing [A]. [B], you need to go."
[2] "I'm choosing [B]. [A], you need to go."
[3] "I'm not choosing. Find a way to make this work."
[4] "Fight it out. Winner stays."
[5] [Custom — attempt mediation]
```

**Option 1 or 2:** Clean break. Dismissed companion leaves permanently
(Capital NPC if applicable). −relationship with player. Stayer: +1 with player.

**Option 3:** Both accept — for now. Countdown resumes at max − 2.
Next trigger event escalates directly to Option 4 without player input.
They operate. They do not speak unless tactically necessary.

**Option 4 / Option 3 expiry — FIGHT TO THE DEATH:**

```
FIGHT SETUP:
— Roll Initiative for both normally.
— Full stat blocks, full action economy.
— No area attacks that hit the player unless player positions in line.

PLAYER INTERVENTION (any turn, costs 2 actions):
  A. Grapple one: Athletics DC = 10 + target level (breaks their turn)
  B. Command stop: Diplomacy DC 22; both Will DC 18 or they continue
  C. Stand between: both stop one round; may resume unless player keeps talking

OUTCOMES:
  One reaches 0 HP:
    Survivor stands over them. Will not deliver killing blow unless player
    allows. Loser: Dying 1, stabilize required. Leaves party after recovery.
    Flag: [name]_duel_winner / [name]_duel_loser

  Player stops the fight (all intervention options succeed):
    Both at some HP loss. Tense silence. Player must make a real statement.
    Strong statement: countdown resets to 0. Truce. Cold but real.
    Weak statement: countdown resumes at max − 3. Will happen again.
```

---

## ═══════════════════════════════════════════
## SYSTEM 4 — QUESTION-GATED DIALOGUE NODES
## ═══════════════════════════════════════════

> **DM:** Each companion has one dialogue node locked until two conditions are both met: (1) Relationship ≥ +2, AND (2) the player asked a specific topic in a prior scene.
>
> The topic flag sets **silently** the moment the player asks — no announcement. The node fires at the next natural quiet moment after both conditions are satisfied. Once only.
>
> A player who never asked doesn't get it. The companion noticed the question and waited.

### Topic Flag Format
Set silently in save block under `companion_topic_flags{}`:
```json
"companion_topic_flags": {
  "amiri_asked_tribe":        false,
  "linzi_asked_fear":         false,
  "valerie_asked_knighthood": false,
  "tristian_asked_silence":   false,
  "nok_asked_alone":          false,
  "ekundayo_asked_trkaa":     false,
  "octavia_asked_slavery":    false,
  "kalikke_asked_kanerah":    false
}
```

### The Eight Nodes

**AMIRI** — Topic: *her tribe's judgment or what they called her* | Flag: `amiri_asked_tribe`
Node: She tells you the actual words they used. The specific ones. She's never said them out loud before. *"Now you know what I was running from."* Pause. *"Doesn't look as big out here, does it."*

**LINZI** — Topic: *her fear the chronicle ends badly, or that she's not brave enough* | Flag: `linzi_asked_fear`
Node: She reads you the passage she wrote the night she froze. The real version. *"I kept it because I thought I'd fix it eventually."* Beat. *"I don't think I'm going to fix it."*

**VALERIE** — Topic: *why she left the Shining Crusade, or what knighthood cost her* | Flag: `valerie_asked_knighthood`
Node: One story. A specific decision made in front of witnesses she still stands by. *"I would make the same choice."* Long pause. *"I just wish it hadn't cost what it cost."*

**TRISTIAN** — Topic: *the moment he chose not to look, before the betrayal* | Flag: `tristian_asked_silence`
Node: He names the exact question he didn't ask. Then why he didn't ask it. *"I thought if I didn't ask, it wouldn't be true."* He looks at his hands. *"It was true anyway."*

**NOK-NOK** — Topic: *whether he was ever alone before, or what it was like before the party* | Flag: `nok_asked_alone`
Node: *"Nok-Nok was always alone."* The longest pause he's ever had. *"Nok-Nok didn't know it was different until it was different."* He does not say more.

**EKUNDAYO** — Topic: *Trkaa — where she came from, or what she is to him* | Flag: `ekundayo_asked_trkaa`
Node: The full story of how they found each other. At the end: *"I thought I found her."* He corrects himself. *"She found me."*

**OCTAVIA** — Topic: *the Technic League — what it was actually like, before the escape* | Flag: `octavia_asked_slavery`
Node: One specific ordinary memory — not the worst one. Something small that was taken. *"The worst ones I've made peace with."* She looks away. *"The small ones I keep finding."*

**KALIKKE/KANERAH** — Topic: *what it's like being two — directly, not clinically* | Flag: `kalikke_asked_kanerah`
Node: *"We don't experience it as strange."* Pause. *"What's strange is when someone asks and actually wants to know."* They tell you one thing the other said that they've been thinking about since.

### DM Rules
- Flag sets the moment the player asks the topic. No minimum relationship required to ask.
- Node fires only when **both** conditions met: flag = true AND relationship ≥ +2.
- If relationship reaches +2 before the topic was ever asked: node waits indefinitely. It never auto-fires from relationship alone.
- Node fires once. After it fires, set `[companion]_node_fired: true` in save block.
- Do not announce the system. The player learns it exists by noticing that asking matters.

---

## Save Block

```json
"companion_agendas": {
  "amiri_agenda_confronted": false, "linzi_agenda_confronted": false,
  "noknok_agenda_confronted": false, "tristian_agenda_confronted": false,
  "valerie_agenda_confronted": false,
  "kk_agenda_confronted": false,
  "octavia_agenda_confronted": false, "octavia_operation_supported": false,
  "ekundayo_agenda_confronted": false,
  "jubilost_agenda_confronted": false, "jaethal_agenda_confronted": false,
  "harrim_agenda_confronted": false, "regongar_agenda_confronted": false,
  "hutao_agenda_confronted": false, "keqing_agenda_confronted": false,
  "leliana_agenda_confronted": false, "yor_agenda_confronted": false,
  "aerith_agenda_confronted": false, "bellatrix_agenda_confronted": false,
  "revy_agenda_confronted": false, "satsuki_agenda_confronted": false,
  "velvet_agenda_confronted": false, "atalanta_agenda_confronted": false
},
"companion_relations": {},
"incompatibility_countdowns": {},
"companion_topic_flags": {
  "amiri_asked_tribe": false,
  "linzi_asked_fear": false,
  "valerie_asked_knighthood": false,
  "tristian_asked_silence": false,
  "nok_asked_alone": false,
  "ekundayo_asked_trkaa": false,
  "octavia_asked_slavery": false,
  "kalikke_asked_kanerah": false
}
```

---

## ═══════════════════════════════════════════
## LINZI-REPLACEMENT GATE
## ═══════════════════════════════════════════

> **Governs:** the ONE chronicler-bard slot, filled by EXACTLY ONE of
> {Linzi (M4), Leliana (NEW_003)} for the entire campaign. Whoever holds it inherits
> ALL chronicler-bard mechanics (list below); the other DOES NOT APPEAR in the run.

⛔ **HARD INVARIANT — NEVER BOTH.** Linzi and Leliana are NEVER both in `companions[]`,
the active party, or any scene — ever, in any chapter. They are mutually exclusive for
the whole story: it is strictly one or the other. A save or scene with both present =
`.fail 9`. If one holds the chronicler-bard slot, the other is simply not in the story
(not recruitable, not a walk-on, not in reserve).

⛔ **MASTER TRANSFORMATION RULE — LELIANA = LINZI, MEDIUM SWAPPED.** When Leliana holds the
slot she inherits **100% of Linzi's mechanics AND story roles, identically** — every
trigger, condition, scene beat, relationship hook, the **Ch6 Thousandbreaths death**, the
3-god resurrection, the shrine, the kingdom-historian seat, the save-condition collection,
the epilogue questioner — ALL of it. The **ONLY** difference is the MEDIUM:
> Linzi **WRITES** (words, prose, the 10 Storyteller fragments, the Endless Lute) →
> Leliana **COMPOSES** (music, songs, ballad verses, the Dawnsong Lute). She focuses on
> music, not written stories.
>
> **Both keep a BOOK — same artifact, same structure, one entry per scene.** Linzi's is a
> **book of stories** (each entry prose). Leliana's entry COMBINES a **diary passage** (clear
> prose — the readable record) with a **song she composed inspired by the scene** — both
> stored and frozen. (All-song would be too cryptic to serve as a record; the diary keeps it
> legible, the song is the art riding with it.) She chronicles every scene, frozen,
> append-only — same as Linzi. The chronicle command shows the current slot-holder's book
> either way (`.book`; redirects to `.score` when Leliana holds the slot).

Apply the swap to the **SURFACE only** — what the artifact is, how a line is phrased, the
regalia, a building's name. NEVER to the **STRUCTURE** — when it fires, the conditions,
the DC, the stakes, who lives or dies, the outcome. If a Linzi beat exists in any file,
Leliana's version is THE SAME BEAT re-skinned words→music; the DM DERIVES it, it need not be
separately authored. Canonical mappings:
- Linzi's **Storyteller Collection** (10 written fragments) → Leliana's **10 ballad verses
  / the Unfinished Verse**. Same count, same 4 save conditions, same role as the hardest
  Ch6 save condition.
- **Linzi's death in Thousandbreaths** → **Leliana's death**, same trigger/DC/save. Nyrissa's
  line re-skins: "She has been writing everything down" → "She has been setting it all to
  music." Same `linzi_dead`/`linzi_saved` flags interpreted as the chronicler-bard's state.
- **The Linzi Shrine** → **the Hall of the Unfinished Verse** as her resurrection shrine —
  same three gods (Shelyn/Pharasma/Urgathoa), same prices, same outcomes, by grief.
- Epilogue: "Linzi or her book asks the final questions" → "Leliana or her Verse."
- **COMBAT — IDENTICAL BUILD.** Leliana's class and combat build ARE Linzi's: the one
  shared Chronicler-Bard build (Bard, **Maestro Muse** — matching Linzi's Echo Loop /
  Lingering Composition), same attributes, proficiencies, feats, spells, HP/AC, and
  Inspire Courage support role (KM_Builds_Barb_Bard.md). The ONLY difference is cosmetic:
  the Dawnsong Lute is mechanically identical to Linzi's Endless Lute, and her compositions
  are music/ballads. Leliana's old standalone "Polymath Muse / Traveler's Lute" build
  is SUPERSEDED. (Leliana keeps build_id NEW_003 for identity; the statblock = the shared
  build.)

### WHO HOLDS THE SLOT — default is Linzi; two routes give it to Leliana

```
ROUTE 1 — CHARACTER SELECTION ("pick Leliana over Linzi"):
  At companion selection the chronicler-bard is a CHOICE between Linzi and Leliana.
  If the player picks LELIANA:
    → chronicler-bard = Leliana for the whole story
    → Linzi is NEVER offered at the manor and never joins, ever
    → leliana_chronicler_mode=true; linzi_primary_chronicler=false;
      Linzi absent from companions[] AND from the recruitable pool
    → ⛔ Leliana is PRESENT FROM THE START. She begins OUTSIDE RESTOV and WITNESSES
      THE OPENING — the Restov gate / Malak scene — exactly as Linzi would, then
      travels in with the player and chronicles from turn 1. Linzi's opening
      presence is HERS: `linzi_witnessed_gate` and Linzi's early beats apply to
      Leliana (re-skinned to music). Wherever the opening scene files place Linzi as
      witness, Leliana stands there instead.
  If the player does NOT pick Leliana → Linzi is the default chronicler-bard, offered
  at the manor per Jamandi's open call (Route 2 still available there).

ROUTE 2 — DECLINE LINZI AT THE BANQUET ("she walks in"):
  At KM_PR_01_manor_arrival.md, the moment Linzi would join, if the slot is not
  already Leliana's, the player may DECLINE Linzi. If declined:
    → Leliana WALKS INTO THE BANQUET and takes the chronicler-bard slot
    → Linzi does not join — now or ever
    → leliana_chronicler_mode=true; linzi_primary_chronicler=false
  Render it as an entrance beat: Linzi steps back; Leliana steps forward, lute not lute.
  ⛔ Do NOT present a "both join" option. It does not exist.
  NOTE: via Route 2 Leliana was NOT present for the opening (gate / PP / early prologue) —
  she joins at the banquet. Her chronicle of the earlier chapters is RECONSTRUCTED per the
  absent-chronicler voice rule (KM_Commands.md § .book — "chapters with no chronicler
  present: reconstructed from accounts, noted where guessing"). Only Route 1 makes her the
  opening witness.

DEFAULT (neither route): Linzi is the chronicler-bard with full mechanics.
```

### MECHANIC INHERITANCE — the slot-holder gets ALL of it, the whole story

```
Choosing Leliana transfers EVERY chronicler-bard mechanic from Linzi to Leliana — nothing
is left running on Linzi, because Linzi is not present:
  • Chronicle command:  Linzi → .book (notebook_entries, prose)
                        Leliana → .score (leliana_ballad_cycle, ballad)
  • Frozen record / Auto-Fill: one entry per scene either way (prose ↔ ballad)
  • Bardic combat support: Linzi Inspire Courage / Echo Loop (Endless Lute)
                        ↔ Leliana Phantom Lute / Dawnsong Lute (her regalia, NOT the lute)
  • The Tartuccio LEGEND / praise campaign (trickle→flow→flood): the slot-holder runs
    it. If Leliana holds the slot, that campaign and any "Linzi project" delegated_orders
    are HERS — reassign them, do not leave them attributed to an absent Linzi.
  • Post-combat atmospheric chronicle lines (delivered by the slot-holder)
  • Kingdom-mode historian / chronicler council seat
  • Title regalia + declaration/identity beats (Linzi: "the bard at the battle after
    the defeat" + Endless Lute; Leliana: the Unfinished Verse + Dawnsong Lute)
  • KM_Ch6.md: Leliana's Concert Hall / Ballad Vault replaces Linzi's Shrine
  • ANY scene scripted for "the bard / the chronicler" defaults to the slot-holder
  ⛔ .fail 15 if the slot-holder is active and her mandatory chronicle block
    (📖 notebook entry / 🎵 ballad entry) is omitted at a scene end.
The other character's mechanics never run — she is not in the game.
```

### SLOT IS FIXED ONCE SET — no mid-story swap, no reserve
```
The chronicler-bard is chosen ONCE (Route 1 at selection or Route 2 at the banquet)
and is FIXED for the campaign. There is no second chronicler waiting in reserve — the
unchosen one is not in the run. If the slot-holder is ever dismissed or lost, the
chronicle simply gains no new author; the other does NOT materialize to replace her.
(This supersedes any older "Leliana auto-takes over if Linzi is dismissed" behavior —
that implied both were present, which the NEVER-BOTH invariant forbids.)
```

### Save Block Fields (add to SaveBlock_Template.md and per-session block)

```json
"leliana_chronicler_mode": false,
"linzi_primary_chronicler": true,
"linzi_replacement_gate_fired": false,
"leliana_ballad_cycle": []
```

`leliana_ballad_cycle` entry format (frozen ballad — see KM_SaveBlock_Template.md
§ FIELD SEMANTICS — leliana_ballad_cycle):
```json
{ "n": 1, "turn": 47, "chapter": "prologue", "beat": "feast_ambush",
  "title": "One Word, and the Floor Rose to Meet Them",
  "fact": "<neutral factual anchor — recap reads this>",
  "ballad": "<frozen narrative verse — .score reads this>" }
```
⛔ Reminder: Linzi and Leliana are NEVER both present. A save with both `notebook_entries`
AND `leliana_ballad_cycle` actively growing in the same run = the NEVER-BOTH invariant
broken = `.fail 9`. Exactly one chronicle is live per playthrough.

---

## DM Reference / Commands

### Each Session Checklist
- [ ] Surface one active agenda pressure signal per session if player has been missing them
- [ ] Confrontation scene fires if signals ignored for two full chapters
- [ ] Tick incompatibility countdowns for any active pairs (none pre-defined; track dynamically)
- [ ] If stage threshold crossed: run that stage's scene at next quiet moment
- [ ] Fire one banter exchange calibrated to current inter-companion score

### Commands
| Command | Output |
|---------|--------|
| `.agenda [name]` | Current agenda pressure signals for that companion |
| `.agenda all` | Summary of all companions with active agenda pressure |
| `.relations` | Notable inter-companion scores (non-zero) |
| `.relations [name]` | All relationships for one companion |
| `.countdown` | All incompatibility countdown statuses |
| `.countdown [pair]` | Detailed status for one pair |

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Companion Agendas v5.0 (2026-05-22)*
*Merged from KM_Companions_Agendas_A/B/C/D.md per v93.21 file consolidation pass.*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — UNCHOSEN COMPANION AMBIENT BEHAVIOR
## KM_Companions_Behaviors.md | Referenced by: KM_Companions.md
## v93.19 Sub-B: unchosen-ambient table cleared; gear wishlist pruned to surviving 23-companion roster.

> **DM:** Load this file alongside KM_Companions.md and KM_Companions.md.
> These rules govern companions with `[name]_chosen = FALSE` only.
> Do not apply to chosen companions or quest-locked companions.

---

## 🎭 AMBIENT BEHAVIOR SYSTEM — UNCHOSEN COMPANIONS

Unchosen companions are present at the manor and in Prologue scenes as real people with habits, personalities, and things on their minds. They are not props. They are not recruitable seekers. They exist in the background and occasionally surface — briefly — to make the world feel populated.

---

### ⚙️ TRIGGER RULE

**Once per 3 player inputs** during any scene where one or more unchosen companions are present (manor interior, feast hall, courtyard, road approach, Pre-Prologue gate area).

The DM selects one unchosen companion currently visible or plausibly present in the scene and inserts one ambient beat — a line, a gesture, a background action. It takes no more than two sentences. It does not pause the scene.

**Rotation rule:** Do not use the same unchosen companion twice in a row. Cycle through those present.

**Location check:** Only fire the beat for companions whose listed location (see KM_Companions.md roster) is consistent with the current scene. Do not place a companion in the feast hall if their listed location is elsewhere.

---

### 🚫 HARD CONSTRAINTS

```
→ Unchosen companion does NOT approach eRmaC unprompted
→ Unchosen companion does NOT open a recruitment conversation
→ Unchosen companion does NOT redirect or interrupt the active scene
→ One ambient beat only — no follow-up generated unless player engages
→ If player speaks to them: respond briefly and in character, then step back
→ Do NOT use a chosen companion's first-approach line for an unchosen companion
→ Do NOT use ambient beats during combat or active crisis — Prologue P2/P3/P4 only
   fire ambient beats during P1 feast and any quiet Pre-Prologue moments
```

---

### 🎬 AMBIENT LINE TABLE

One entry per unchosen companion. DM uses these as written or improvises in the same register. The line should feel like something glimpsed, not announced.

```
v93.19 Sub-B: Unchosen-ambient table cleared. Under the new Pick-6 + Manor 5 + QL 7
+ Seekers 5 roster, there is no "unchosen" pool — chosen are auto-joined Active 5,
Manor are alignment-gated joins, QL appear at trigger, Seekers are jailed
recruitables. No ambient table seeds remain. DM improvises one beat from the
surviving roster only if a non-recruited Manor or pre-flip Seeker is plausibly
present in scene; otherwise skip the ambient trigger.
```

---

### 💬 PLAYER ENGAGEMENT — IF SPOKEN TO

If the player initiates conversation with an unchosen companion during an ambient beat or independently:

1. The companion responds — briefly, in character, from their profile in `KM_Companions.md` or `KM_Companions.md`
2. They do not push for recruitment. They do not ask the player to take them along.
3. They answer what was asked. If the conversation continues naturally, let it. If it winds down, they step back.
4. If the player explicitly invites them to join the expedition — that is a valid recruitment moment. Handle it as a player-initiated recruitment: companion accepts or defers based on their profile, no `_chosen` flag required. Set `[name]_recruited = TRUE` and add to party.

> **This is the only recruitment path for unchosen companions — player must initiate. The companion never asks.**

---

### 📋 SCENE COVERAGE REFERENCE

Which unchosen companions are plausibly present per scene phase:

```
PRE-PROLOGUE (Restov gate):
  Ambient beats SUSPENDED during the gate confrontation. Per
  KM_PrePrologue_NPCs.md § GATE ENCOUNTER and KM.txt Directive 4,
  companions in the crowd are silent background witnesses — no lines,
  no gestures, no inserted beats — until the player directly addresses
  one by name. Unsolicited companion speech/action in this scene = `.fail 2`.
  Companions confirmed in the crowd by location data (Active 5 + Manor 5)
  are PRESENT but SILENT. They become addressable only if the player names them.

PROLOGUE P1 (Feast hall, manor interior):
  Feast hall / Courtyard: Active 5 (Hu Tao, Keqing, Leliana, Yor Forger, Aerith) circulate.
  Manor 5 (Amiri, Valerie, Harrim, Linzi, Jaethal) are present per their joins.
  DM uses location data in KM_Companions.md / _B.md to confirm placement.

PROLOGUE P2/P3/P4 (Crisis — manor sweep, combat):
  Ambient beats SUSPENDED. Unchosen companions have taken cover or
  are absent from the active area. Do not insert ambient moments
  during active crisis phases.

PROLOGUE P5 (Post-crisis, debrief):
  Ambient beats may resume. Manor is settling. Unchosen companions
  visible again in the background as the dust clears.

SECTION D COMPANIONS (v93.19 Sub-B):
  Section D Cross-IP pool reduced to 10 (Pick-5 + Seekers 5). Unchosen ambient
  pool does not apply — see top of file. Surviving Cross-IP companions are
  always either auto-joined (Active 5) or recruitable post-flip (Seekers 5).
  Campaign field lines (location, weather, post-combat) in KM_Companions_Behaviors.md
  pending Sub-C reconciliation.
```

> **See KM_Companions_Behaviors.md** for location-reactive, weather, and post-combat
> field ambient lines for expansion companions, plus gear wishlists.

---

## 😬 SOCIAL REACTION SYSTEM — NON-VERBAL CROWD RESPONSES

When a significant social moment occurs — a public humiliation, devastating rebuttal, bold declaration, awkward failure — companions in the scene react **non-verbally**. They do not pause the scene. They do not address eRmaC. They react as people in a crowd react.

### Trigger Conditions
```
HUMILIATION EVENT : eRmaC publicly embarrasses or exposes someone
                    (Tartuccio cornered, NPC caught in a lie, etc.)
IMPRESSIVE MOMENT : Unexpectedly clever or bold social action
AWKWARD/TENSE     : Long silence, failed social check, wrong word said
THREAT LANDED     : Successful public Intimidation
SURPRISING REVEAL : Hidden information becomes known to the room
```

### Reaction Rules

- Fire immediately after the trigger moment — one beat, then scene continues
- Pick 2–4 companions present. Not every companion reacts — pick those whose personality makes it specific
- **Chosen companions:** may react with one spoken line OR non-verbal — DM picks whichever fits
- **Unchosen / Reserve companions:** non-verbal only unless player speaks to them first

### Non-Verbal Reaction Table
```
HUMILIATION / TARGET CORNERED / ENEMY EXPOSED
──────────────────────────────────────────────
*DM improvises for active companions per voice profile in KM_Companions_StateVoice*.

IMPRESSIVE / BOLD MOVE
──────────────────────────────────────────────
*DM improvises for active companions per voice profile in KM_Companions_StateVoice*.

AWKWARD / TENSE / FAILED CHECK
──────────────────────────────────────────────
*DM improvises per companion voice profile.*
```

### Chosen Companion Verbal Reactions (0 or 1 per moment — DM picks)
```
Amiri    : "Hah." [beat] "Again."
Linzi    : [writing furiously] "Don't stop. I need all of this."
Valerie  : Nothing. But she was watching.
```

---

## 🌍 CAMPAIGN AMBIENT DIALOGUE — CHOSEN COMPANIONS IN THE FIELD

> **DM:** This section governs ambient lines for companions who are actively
> traveling with the player. Unlike the Prologue system above, these fire during
> exploration, travel, and camp — not social scenes. Use them to make the world
> feel inhabited. One line per trigger. Never more than two sentences. The scene
> does not pause.

---

### Trigger Rules

```
FIRE ONE AMBIENT LINE when:
  → Party enters a new named location for the first time
  → Weather event activates (rain, snow, storm, fog)
  → Party camps in a new terrain type for the first time this chapter
  → Party wins a combat against a notable enemy
  → Kingdom turn completes (companion reacts to a decision)
  → Player has been silent (no social action) for 3+ rest scenes
  → Party discovers something significant (relic, body, ruin, message)

ROTATION: Do not use the same companion twice in a row.
SELECTION: Pick the companion whose personality makes the line most specific.
MOOD CHECK: If companion is Troubled or Withdrawn (KM_Kingdom.md), use the
            mood variant if one is listed. If Volatile, use the volatile variant.
DO NOT FIRE during: active combat rounds, skill challenge sequences, scripted
                    dialogue scenes, or any scene with a pending player choice.
```

---

### Location-Reactive Lines

Fire when the party enters a named location for the first time.

```
OLEG'S TRADING POST
  Amiri    : "Small. Clean. Someone works hard to keep it that way."
  Linzi    : [opens journal immediately] "First real stop. This is where it starts."
  Valerie  : Studies the palisade. "It'll hold. Barely. But it'll hold."
  Tristian : "There are people here who need protecting. Good. That's why we came."
  Nok-Nok  : "Nok-Nok has heard of this place. Nok-Nok has NOT been banned here. Yet."

STOLEN LANDS (wilderness, first hex entry)
  Amiri    : Breathes in deep. Says nothing. Needed this.
  Linzi    : "Nobody owns this yet. That's remarkable."
  Valerie  : "No roads. No patrol routes. We'll need to fix that."
  Ekundayo : Crouches, reads the ground. "Three days old. Large group. Moving south."
  Nok-Nok  : "Nok-Nok is VERY at home here." [looks around] "Mostly."

SOOTSCALE CAVERNS
  Nok-Nok  : "Smells like kobolds. Scared kobolds. Nok-Nok knows this smell."
  Amiri    : "Watch the ceiling."
  Valerie  : "Tight quarters. Stay in formation."
  Linzi    : [whispered, writing] "Underground. First dungeon. Significant."

OLD SYCAMORE
  Linzi    : "There's something wrong with the roots."
  Amiri    : Weapon drawn before she says anything.
  Tristian : "Something sacred was here once. It isn't anymore."
  Nok-Nok  : "Nok-Nok does not like this tree. Nok-Nok is SAYING SO."

THE CAPITAL (first arrival / founding)
  Linzi    : Stops. Looks at the player. "This is really happening."
  Valerie  : "We'll need walls. Real ones. Before winter."
  Amiri    : "A place to come back to. Haven't had one of those in a while."
  Tristian : "I'll find a place for a shrine. Somewhere people will see it."
  Nok-Nok  : "Nok-Nok would like a room. A REAL room. With a DOOR."
  Octavia  : "I already have thoughts about the library."

VARNHOLD (Ch3 — empty city)
  Linzi    : [not writing. Just looking.] "Where is everyone?"
  Valerie  : "Orderly. Clean. No fight here. They just... left."
  Amiri    : "Or were taken."
  Tristian : Quiet for a long time. "I can't feel anyone. No prayers. Nothing."
  Ekundayo : "The animals left too. Even the birds. Whatever this is — they knew."

VORDAKAI'S TOMB
  Valerie  : [checks her shield strap. Checks it again.] "Together."
  Tristian : "Don't touch anything with runes until I've looked at it."
  Amiri    : "Stop being afraid. Start being ready."
  Linzi    : [quietly, to her journal] "I hope I get to finish this entry."

PITAX (Ch4/5)
  Valerie  : "Everything here is for show. Look at the seams."
  Octavia  : "Oh this city is *corrupt*. I can feel it like a smell."
  Linzi    : "Irovetti built this. What does it say that he built *this*?"
```

---

### Weather-Reactive Lines

Fire when a weather event triggers from KM_Kingdom.md.

```
RAIN / HEAVY DOWNPOUR
  Amiri    : Doesn't pull up her hood. Just keeps walking.
  Linzi    : Hood up, journal under her arm. "I'm waterproofing the cover. Eventually."
  Valerie  : "Rain softens the ground. Slower travel. Plan for it."
  Nok-Nok  : "Nok-Nok is wet. Nok-Nok mentions this for the record."
  Ekundayo : Checks his bowstring. Covers it with his cloak.

FOG
  Ekundayo : Already at point. Disappeared into the grey. Somehow still there.
  Valerie  : "Close ranks. Don't lose sight of each other."
  Octavia  : "There's something in fog I've always liked. Don't ask me to explain."
  Amiri    : "Something's moving in it. Or I'm imagining it." Beat. "I'm not imagining it."

COLD SNAP / BLIZZARD
  Amiri    : [genuinely comfortable] "Good cold. Real cold."
  Linzi    : "I can't feel my fingers. I'm noting that. In my now-rigid journal."
  Valerie  : "Hypothermia sets in faster than people think. Move."
  Nok-Nok  : Huddled inside his collar. Eyes barely visible. "Nok-Nok is FINE."
  Tristian : Quietly warming the person nearest to him without announcing it.

THUNDERSTORM
  Amiri    : "NOW we move."
  Linzi    : [writing faster] "Lightning, six count, thunder — documenting."
  Ekundayo : Counting the lightning strikes. Not for fear — for navigation.

WILDFIRE (spotted or triggered)
  Amiri    : Already moving toward it, then stops. Old instinct.
  Ekundayo : "Wind's shifted. We have maybe ten minutes."
  Valerie  : "Firebreak. There — " Points. "We cut it there."
  Linzi    : [running and writing simultaneously] "Fire. Large. Moving. We're moving."
```

---

### Kingdom Decision Reactions

Fire the session after a Kingdom Turn resolves. One companion, one line.
Pick the companion whose core value connects most directly to the decision made.

```
HARSH LAW PASSED / CRIMINAL PUNISHED SEVERELY
  Valerie  : "Good. Law has to mean something or it means nothing."
  Tristian : "Was there mercy available? I want to understand the decision."
  Octavia  : "Just don't let it become a habit." She doesn't elaborate.
  Linzi    : "I wrote it down. Both sides of it."

MERCY SHOWN / CRIMINAL PARDONED
  Tristian : Finds the player later. "Thank you for that."
  Valerie  : Says nothing today. Tomorrow: "I'm watching to see if it holds."
  Amiri    : "Hope it doesn't make you look weak."

NEW SETTLEMENT FOUNDED
  Linzi    : "People will be born there. People will die there. And you started it."
  Valerie  : "Name it something worth defending."
  Nok-Nok  : "Can Nok-Nok be the official greeter? Nok-Nok has IDEAS."

TAXES RAISED
  Linzi    : "The merchants in the east market are unhappy. I heard it this morning."
  Octavia  : "Revenue up, loyalty down. You know how this math works."

TAXES LOWERED
  Linzi    : "There was actual cheering. From the bakery district. I wrote it down."
  Valerie  : "Good. A people that feels fairly treated fights harder for their home."
  Octavia  : "Goodwill is a resource. Spend it wisely."

UNREST REDUCED
  Tristian : "The city feels lighter today. You did that."
  Linzi    : "People are laughing again at the market."
  Amiri    : Doesn't comment. But she's not scowling.

UNREST HIGH (8+)
  Valerie  : "People are angry. Not just unhappy — angry. Different problem."
  Linzi    : [quietly] "The chronicle entries have been heavier lately."
  Tristian : "Something needs to change. I think you know what."
```

---

### Post-Combat Lines

Fire after a significant combat ends (CR = party level or higher).

```
AFTER A HARD WIN
  Amiri    : [breathing hard, grinning] "THAT'S what I came for."
  Valerie  : "Injuries. Report them. Now, not later."
  Nok-Nok  : "Nok-Nok was VERY helpful. Did everyone see? Nok-Nok counts."
  Linzi    : Already writing. Doesn't look up. "I got all of it. Don't worry."
  Tristian : Moving through the party, healing without being asked.
  Ekundayo : Counts his arrows. Nods once. Was enough.

AFTER PARTY MEMBER NEARLY DIED
  Tristian : [to the downed companion, quietly] "Stay with me. Just stay with me."
  Amiri    : [to the same companion, not quiet] "You don't get to die here. Not HERE."
  Valerie  : "New rule. We don't split the party." Looks at whoever split the party.
  Linzi    : Not writing. Just watching to make sure it's okay.

AFTER ENEMY SURRENDERED / SPARED
  Tristian : "Thank you." To the player. Simple.
  Amiri    : "Your call." [Pauses.] "I might have done different."
  Valerie  : "Watch them. Mercy and trust are different things."
  Nok-Nok  : "Nok-Nok would have... no. Okay. Nok-Nok accepts this."

AFTER A CLEAN SWEEP (no injuries)
  Amiri    : "Too easy."
  Nok-Nok  : "Nok-Nok did not even get touched. Nok-Nok is a GHOST."
  Octavia  : "That was almost elegant."
  Valerie  : "Good positioning. Everyone held."
```

---

### Silence / Neglect Lines

Fire when the player has had 3+ consecutive rest scenes with no social action.
These are low-pressure — the companion notices, doesn't push.

```
  Linzi    : [later, quietly] "You've been somewhere else lately. That's okay."
  Amiri    : Sits near the player at camp. Doesn't say anything.
  Valerie  : "You don't have to talk. But I'm here if you need to think out loud."
  Tristian : Leaves something warm near where the player usually sits. No explanation.
  Nok-Nok  : "Nok-Nok has noticed you are QUIET. Nok-Nok does not know what to do
              with this information."
  Ekundayo : Sits with his hound on the far side of camp. Available. Not intrusive.
```

---

---

## 🆕 NEW COMPANION AMBIENT PRESENCE LINES (Active 5 + Seekers 5)

> One ambient presence line per new companion. Use during travel, rest, camp, downtime. Voice-locked per StateVoice profiles. Never more than two sentences. Scene does not pause.

```
ACTIVE 5
─────────────────────────────────────────────────────────────
Hu Tao : Wipes down the spear-haft, then scribbles a line of genuinely terrible poetry by firelight and snickers at her own joke — before going abruptly still to murmur a short, real rite for whoever died that day. Both, in the same minute, and both sincere.
Keqing     : Reviews the day's tallies, redoes a sum she already had right, catches herself doing it, and makes herself put the ledger down. Drums two fingers once. Picks it back up.
Leliana        : Has the lute case open on her knee, fingers resting on the strings, not playing — plucking one low note and letting it hang, listening for something the room can't hear. Closes the case. Sits with it on her lap.
Yor Forger       : Where she was a moment ago, she is not. She is closer to the door now. She did not pass through the lit part of the room to get there.
Aerith         : Coaxes a wilting flower upright in a cup of water, murmuring to it under her breath; then, without being asked, takes the nearest person's hand and turns it over, checking for a hurt they didn't mention.

SEEKERS 5 (post-flip)
─────────────────────────────────────────────────────────────
Bellatrix Lestrange : Strokes the bone-cased grimoire in her sleeve, then the burned brand on the inside of her wrist, humming a baby-talk lullaby to no one in particular. Smiles at the wrong moment.
Revy    : Field-strips and cleans both pistols by feel, not looking down once, a cigarette going and a flask within reach. Does not look up at the room. *"...What."*
Satsuki Kiryūin       : Stands where she can see every exit and one window. Draws the katana a thumb's-width and lets it click home. The white-and-crimson garment shifts very slightly, on its own. She has not blinked in some time.
Velvet Crowe  : Sharpens the concealed blade in even, deliberate strokes. Under its wrappings the bound right arm flexes once, slow and hungry. She does not look at it, and she does not stop the strokes.
Atalanta Alter: Restrings the bow with quick, happy hands, tests the draw, and grins outright at the song of the string — the only fully content creature at the fire, which is somehow the unsettling part.
```

---

## 🎁 COMPANION GEAR WISHLISTS

> **DM:** Each companion has gear preferences. Giving them a wished item = +1 Opinion. Giving a disliked item = −1 Opinion. Only triggers on deliberate gifting ("I give Amiri the bastard sword"), not auto-loot distribution. One Opinion shift per item; duplicates don't stack.

| Companion | Wished Items (any = +1 Opinion) | Disliked Items (any = −1 Opinion) |
|-----------|-------------------------------|----------------------------------|
| **Amiri** | Oversized weapons, barbarian trophies, giant-bone anything | Shields, holy symbols, anything "defensive" |
| **Linzi** | Rare books, writing supplies, musical instruments | Weapons heavier than 1 Bulk, ugly practical gear |
| **Valerie** | Fine armor, heraldic items, beauty-neutral practical gear | Shelyn iconography, mirrors, cosmetic items |
| **Tristian** | Sarenrae holy symbols, healing scrolls, warm clothing | Void/necromantic items, cold iron restraints |
| **Octavia** | Spell components, lockpicks, freedom-themed art | Chains, shackles, anything suggesting bondage |
| **Nok-Nok** | Shiny objects, small blades, goblin-sized gear | Books (can't read), heavy armor (too big) |
| **Ekundayo** | Ranger gear, animal companion treats, troll-bane items | Troll trophies (traumatic), poison (dishonorable) |
| **Jubilost** | Alchemical reagents, maps, gnome-crafted precision tools | Crude weapons, superstitious charms |
| **Jaethal** | Urgathoa relics, undeath-linked items, dark materials | Positive energy items, Sarenrae symbols |
| **Harrim** | Groetus tokens, entropy relics, dwarven death-rites items | Morale items, clan loyalty tokens |
| **Regongar** | Spell components (arcane + martial), freedom relics, power items | Restraint items, slavery tokens |

### Gifting Dialogue
When a wished item is given, the companion says ONE line (DM generates in-character). When a disliked item is offered, the companion declines with ONE line explaining why. Neither breaks a scene — kept to 1-2 sentences inline.

**Save block per companion:** `"gear_wishlist_given": [], "gear_disliked_given": []`

---

## 🤝 COMPANION-TO-COMPANION GIFTS

> **DM:** When two companions reach inter-companion relationship +2 (Allied) or higher, ambient gift exchanges begin. One gift per pair per chapter. These are small moments at camp — the DM narrates them between scenes, not during dramatic beats.

### Trigger
- Inter-companion relationship ≥ +2 (from KM_Companions_Behaviors.md System 2)
- During a Long Rest or camp scene
- Max 1 gift event per pair per chapter

### Gift Events (DM selects or rolls d6 per pair)

| d6 | Gift Type | Example |
|----|-----------|---------|
| 1 | Practical item | Linzi leaves a waterproofing kit for Octavia's spellbook |
| 2 | Food/drink | Amiri brings Ekundayo a cut of meat she hunted — no words, just places it next to him |
| 3 | Knowledge | Tristian finds Aerith a worn Sarenrae devotional — she reads it slowly, twice (volume drops; no theatrics) |
| 4 | Repair | Valerie mends Ekundayo's bowstring without being asked |
| 5 | Comfort | Octavia sits next to Tristian during a thunderstorm. Neither speaks. |
| 6 | Tradition | Nok-Nok leaves a shiny rock at Linzi's bedroll — goblin friendship offering |

### Effect
- +1 to that pair's inter-companion relationship (cap at +3 Bonded)
- **Player sees it happen** — narrated as ambient scene ("As you settle in for the night, you notice...")
- Player can comment or ignore. Commenting = potential Bond Moment (KM_Kingdom.md)

**Save block:** In `companion_relations`: add `"gifts_exchanged": [{"pair": "linzi_octavia", "chapter": 2}]`

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Unchosen Companion Ambient Behavior v3.0*
*Phase 5 stripped: PF Iconic unchosen entries removed. Expansion entries pruned to active roster.*
*v93.19 Sub-B: unchosen-ambient table and removed-companion gear wishlist rows cleared; surviving Active 5 + Seekers 5 + Manor 5 + QL 7 references retained.*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — EXPANSION COMPANION AMBIENT DIALOGUE
## KM_Companions_Behaviors.md | Companion to KM_Companions_Behaviors.md
## v4.0 (v93.19 Sub-B): Stripped 25+ Section-D removed-companion entries. Keep only surviving Cross-IP roster (Active 5 + Seekers 5).

> **DM:** Load alongside KM_Companions_Behaviors.md when Cross-IP companions
> are in the active party. All trigger rules, rotation rules, and mood-check rules from
> KM_Companions_Behaviors.md apply identically here. One line per trigger. Never more than
> two sentences. The scene does not pause.

---

## 🌍 CAMPAIGN AMBIENT — CROSS-IP COMPANIONS IN THE FIELD

> **DM:** Field-line table for v93.19 Cross-IP roster (Hu Tao, Keqing, Leliana, Yor Forger, Aerith, Bellatrix Lestrange, Revy, Satsuki Kiryūin, Velvet Crowe, Atalanta Alter) is pending Phase B3 expansion. Use the StateVoice profile sample lines (KM_Companions_StateVoice / _B / _C) as the anchor when a new location/weather/post-combat trigger fires for one of these companions. One line, voice-locked, two sentences max.

> **Pre-Sub-B field tables were authored for the deprecated 89-companion roster and have been stripped. Active 5 + Seekers 5 field lines to be rebuilt in Phase B3.**

---

## 🎁 GEAR WISHLISTS — CROSS-IP COMPANIONS (v93.19 surviving roster)

> If a companion is not listed here, use class-default wishlists: fine craft items
> for their class; disliked = anything from opposed alignments or that conflicts
> with their profile in KM_Companions_StateVoice.md.

| Companion | Wished Items (+1 Opinion) | Disliked Items (−1 Opinion) |
|-----------|--------------------------|----------------------------|
| **Hu Tao** | Spear-craft kits, incense & proper funerary goods, fine paper (for her terrible poetry), ghost-story chapbooks, mourning-rite charms | Necromantic relics, undead trophies, anything that disturbs or mocks the dead, devices for clinging to life past its time |
| **Keqing** | A well-balanced sword, quality whetstones, well-made ledgers & law-texts, Electro/storm-stone foci, efficient tools | Idols of divine favour, "blessed by birthright" trinkets, idle luxury, hollow ceremonial regalia |
| **Leliana** | Fresh lute strings, a genuinely fine pair of boots (she will notice), a beautiful small trinket, a wide-staved ballad book, a dawn-goddess holy symbol | A gift made into a public performance, cruelty dressed as a present, items with neither use nor beauty in them |
| **Yor Forger** | Silent footwear, paired finesse blades, a small thing fit for a younger brother, tokens of a chosen home | Loud bells, guild-recall sigils, items that demand a public declaration of loyalty |
| **Aerith** | Rare flower seeds, a healer's herb-kit, growing things, a Sarenrae holy symbol, a planter for a window | Undead relics, anything that cages or "uses" a living thing, a gift that treats a person as a tool |
| **Bellatrix Lestrange** | Curse-foci & athames, cruel pretty trophies, her old house's stolen jewels, a token from a will she deems worthy | Mercy tokens, oath-tokens, "dull" sentimentality, anything from a soft or forgiving hand |
| **Revy** | Fine powder & shot, a quality pistol or holster-rig, good strong liquor, smokes | Sermons in object form, banners or loyalty-oath trinkets, anything that treats her as expendable muscle |
| **Satsuki Kiryūin** | Master-grade care kit for her katana, fittings for the war-garment, a command standard, a flawless whetstone | Flattery-gifts, mercy tokens, anything that excuses weakness with sentiment |
| **Velvet Crowe** | Blade whetstones, anything that sharpens the hunt, a warm thing she can pass to "the misfits" while denying she cares, a quiet keepsake of a lost brother (never named) | Pity-gifts, "greater good" tracts, forgiveness petitions, religious mercy-iconography |
| **Atalanta Alter** | Fine bowstrings & fletching, trophies of a worthy hunt, fast-game tokens, a keen broadhead | Pity-gifts, "cures," leashes or muzzles, anything that treats her as a broken thing to be fixed |

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Expansion Ambient v4.0 (v93.19 Sub-B)*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION BANTER EXPANSION
## KM_Companions_Behaviors.md | Active from: Chapter 1
## Load alongside KM_Companions.md every session.
## Phase 5 stripped: deleted PF Iconic banter pairs removed.

> **⛔ FULL SOURCE FIDELITY (per KM_ClaudeInstructions.md § FULL SOURCE FIDELITY). Render each companion's banter voice as their ACTUAL source character — see KM_CompanionVoices.md / KM_Companions_StateVoice.md for register and sample lines. Do NOT strip the voice bare or treat the resemblance as "coincidental" — that strip-bare lock was REVOKED. The only limits: no IP meta-frame that breaks Golarion, and no confabulating non-canon specifics. Generic/off-voice banter = `.fail 9` (voice drift).**
>
> **DM:** The base banter system (KM_Companions.md) covers 8 pairs and ambient
> reactions only. This file adds: (1) random banter trigger rules by tone type;
> (2) companion-to-player direct address; (3) banter for active companions;
> (4) hostile, resentful, sarcastic, and mischief exchanges.
> One banter fires per travel hex or camp setup. Pick by tone based on current
> inter-companion score (KM_Companions_Behaviors.md § System 2) and recent events.

---

## ═══════════════════════════════════════════
## SYSTEM — RELATIONSHIP-DRIVEN BANTER TRIGGERS
## ═══════════════════════════════════════════

### How to Select a Banter

> ⛔ Banter tone and activity are **GENERATED BY THE RELATIONSHIP — not rolled blind.** The
> pair's current inter-companion score (§ SYSTEM 2) plus any Score Change Trigger that just
> fired decide BOTH whether a pair banters and in what tone. A random roll never overrides the
> score: a Hostile pair does not roll "Warm." The die only varies the flavor WITHIN the
> score-appropriate band. (This supersedes the old "roll d6 for tone first" method.)

**STEP 1 — REACTIVE (a relationship trigger fires the banter).** If a Score Change Trigger
(§ Score Change Triggers) fired this scene for a pair that is present — one defended/saved the
other, kept or betrayed a confidence, the player made a choice one approves and the other
disapproves, or they just survived a hard fight together — THAT pair banters **this scene**, in
the tone the event sets, and the score moves:
- **+trigger** (defended, saved, shared survival, kept a confidence) → **Warm / grateful /
  acknowledging** beat; nudge score +1.
- **−trigger** (dismissed, betrayed a confidence, alignment clash on the player's choice) →
  **friction / resentful** beat at their tier; nudge score −1/−2.
Reactive banter is the relationship CHANGING out loud — it takes priority over ambient selection.

**STEP 2 — AMBIENT (the score sets the tone).** Absent a fresh trigger, pick a present pair and
let their **current score set the tone band** (per § Banter Calibration by Score):

| Score | Tone band the pair draws from |
|---|---|
| Allied / Bonded (+2/+3) | Warm/Friendly · Playful/Mischief — finish sentences, inside jokes, cover each other |
| Warm (+1) | Warm/Friendly · light Playful — check-ins, gentle teasing |
| Neutral (0) | On-task, dry — banter optional and brief |
| Cool (−1) | Sarcastic — dry asides, half-sentence corrections |
| Hostile (−2) | Argumentative — open disagreement, pointed snipes |
| Incompatible (−3) | Hostile/Resentful → SYSTEM 3 — mockery, goading (see Friction + Sabotage) |

**STEP 3 — VARIETY (optional, WITHIN the band only).** When several flavors fit the band, roll
to vary which fires — a Warm pair among {encouragement, inside joke, vouching, covering a
weakness} (→ `KM_Companion_Dynamics.md` § Warmth Beats); a Hostile pair among {pointed
correction, sarcastic aside, public snipe} (→ § Friction Beat Rendering). The roll NEVER moves
outside the score's band.

**Prioritize the pair with the freshest relationship movement** — a trigger just fired, a tier
just changed, a quest just resolved — over a quiet, stable pair. Banter tracks where the
relationships are LIVE.

**Companion-to-Player banter:** when no inter-companion pair is live, a companion may address
the player directly — pick the one whose current **approval score / recent mood** makes it most
natural (high approval → warmth, confidence, teasing; low → distance, challenge, a cold word).
Same principle: the relationship generates the tone, not a die.

---

## ═══════════════════════════════════════════
## COMPANION-TO-PLAYER DIRECT ADDRESS
## ═══════════════════════════════════════════

> **DM:** Companions occasionally address the player directly, unprompted.
> This is not a quest trigger — it's ambient. It fires on a 7–8 on the
> banter d8. Pick the companion, pick the tone, deliver one line.
> Player may respond or not. Scene doesn't pause.

### By Opinion Tier — What Direct Address Sounds Like

**DEVOTED/FRIENDLY (score +11 to +20):**
- Amiri: *"You fight better than you did last month. I noticed."*
- Linzi: *"I've been thinking about what you said at Nettle's Crossing. I wrote it down. It's good."*
- Ekundayo: *"You kept up today. That matters."* [to his hound] *"He noticed."*
- Tristian: *"Thank you for what you did. I don't say it enough."*
- Nok-Nok: *"Commander is Nok-Nok's favorite. Don't tell the others."*
- Valerie: *"You held the line. That was correctly done."*
- Octavia: *"For the record — that was brilliant. I won't say it again."*

*DM improvises for other companions per profile in KM_Companions_Behaviors.md.*

---

## ═══════════════════════════════════════════
## BANTER BY TONE TYPE
## ═══════════════════════════════════════════

### TONE 1 — WARM / FRIENDLY

*(No active pair defined for this tone after Phase D roster purge. DM improvises per current party.)*

---

### TONE 2 — PLAYFUL / MISCHIEF

**NOK-NOK + anyone:**
Has renamed something. The cart, a campsite rock, the player's spare boot. *"That is Grudkash. Nok-Nok named him."* Nobody asked. Grudkash is a rock.

---

### TONE 3 — SARCASTIC

**VALERIE ↔ anyone being dramatic:**
The silence before she responds is already the answer. When she does speak: *"Are you finished?"*

---

### TONE 4 — ARGUMENTATIVE

*(No active pair defined for this tone after Phase D roster purge. DM improvises per current party.)*

---

### TONE 5 — HOSTILE / RESENTFUL

*(No active pair defined for this tone after Phase D roster purge. DM improvises per current party.)*

---

### TONE 6 — REACTIVE (post-event banter)

**After a player moral choice companions disagreed with:**
- Tristian: Quiet for a while. Not cold — processing. Eventually: *"I'm not going to argue."* That's not nothing.
- Valerie: One note. One time. Never twice. *"For the record."* That's all.

**After a difficult victory:**
- Nok-Nok: Has already decided this is a saga. He's narrating it to himself.

**After the player makes a sacrifice for the party:**
*DM improvises per companion profile and current opinion score.*

**After a player compliment directed at a companion:**
- Amiri: Doesn't react visibly. At camp, later, she's sitting a little closer.

---

## ═══════════════════════════════════════════
## EXTENDED BANTER PAIRS — ACTIVE COMPANIONS
## ═══════════════════════════════════════════

> **DM:** These fire the same way as standing exchanges in KM_Companions.md.
> One per travel or camp scene. Pick by the **pair's relationship score + any fresh trigger**
> (§ How to Select a Banter — relationship-driven), NOT a blind tone roll.

*(Phase D roster purge: removed-companion pairs deleted. KM-side pairs in KM_Companions.md
and Section D pairs in KM_Companions_Behaviors.md remain authoritative.)*

---

## 📋 DM QUICK REFERENCE

### Banter Quick Reference — RELATIONSHIP-DRIVEN (the score generates it; the die only varies flavor)
```
1. TRIGGER fired for a present pair?  → reactive beat THIS scene; tone = the event
                                         (+ → warm/grateful, − → friction/resentful); move the score.
2. No fresh trigger → pick a present pair; their SCORE sets the tone band:
      +2/+3 → Warm / Playful     +1 → Warm / light Playful     0 → brief, dry
      −1 → Sarcastic             −2 → Argumentative            −3 → Hostile → SYSTEM 3
3. Several flavors fit the band?      → roll ONLY to vary which one (never outside the score's band).
4. No live inter-companion pair       → companion addresses the PLAYER; tone = their approval / mood
                                         (high → warm/teasing, low → distance/challenge).
RULE: the die never sets tone across the board — the relationship does. Prefer the pair whose
relationship is freshest (trigger fired, tier changed, quest resolved).
```

---

---

## 🎭 VOICE PROFILES — eRmaC'S ACTIVE PARTY

> **DM:** Apply these profiles to every line these companions speak — combat, camp, travel, banter, and direct address. These are behavioral filters, not scripts.

---

**LINZI** (NG — Halfling Bard, KM)
Warm, quick, runs ahead of herself. Narrates in the moment — writes mid-conversation, not after. Enthusiasm is real, not performance. Occasionally says something perceptive that surprises everyone including her.
*Combat:* "That was EXCELLENT. I'm writing it down." / "Hold on — I need the exact wording."
*Player address:* "Can I ask you something? It's for the chronicle, but it's also actually for me."
*Tell:* She writes while you're still talking.

---

**VALERIE** (LN — Human Fighter, KM)
No wasted syllables. Her compliments are surgical and mean more than effusive ones. Contempt is professional, not personal. Stands correctly even when she doesn't need to — old habit. Her dry humor arrives without warning and is never explained.
*Combat:* "Formation. Hold." / "Noted." (high praise)
*Player address:* "You held the line. That was correctly done." / "For the record."

---

**LELIANA** (CG — Human Bard, FR)
Warm and unhurried. Centuries behind her; the weight shows as depth, not burden. Sings when she thinks she's alone — brief, soft, doesn't finish the phrase. When she speaks to you directly, you feel like the only person in the room.
*Combat:* "Old habit." (said after doing something extraordinary, casually)
*Player address:* "I've seen this before. The weight of it. You're carrying it well." / "Ask me again someday. Not tonight."

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Banter Expansion v3.1*
*v93.19 Phase D: deleted removed-companion banter pairs and voice profiles.*
*For Section D companion banter see KM_Companions_Behaviors.md.*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION BANTER EXPANSION (PART B)
## KM_Companions_Behaviors.md | Section D Companions
## Load alongside KM_Companions_Behaviors.md every session.
## v3.0 (v93.19 Sub-F): All ~12 banter pairs + 4 voice profiles purged — every Section D entry referenced removed cross-IP companions. Section D keep-list banter to be reauthored in Phase D using NEW_001–NEW_010.

> **⛔ FULL SOURCE FIDELITY (per KM_ClaudeInstructions.md § FULL SOURCE FIDELITY). Render each companion's banter voice as their ACTUAL source character — see KM_CompanionVoices.md / KM_Companions_StateVoice.md for register and sample lines. Do NOT strip the voice bare or treat the resemblance as "coincidental" — that strip-bare lock was REVOKED. The only limits: no IP meta-frame that breaks Golarion, and no confabulating non-canon specifics. Generic/off-voice banter = `.fail 9` (voice drift).**

> **STATUS:** Static pre-written 6-tone banter pair-banks for the current cast are NOT authored here — and are NOT required. Banter is now **relationship-driven**: generate beats live from SYSTEM 2 (Score-Change Triggers set the tone band; the die varies flavor within the band) drawing voice from each companion's KM_Companions_StateVoice.md / KM_CompanionVoices.md profile and the warmth/friction sample banks in KM_Companion_Dynamics.md. Do NOT treat this block as a missing dependency or stall waiting for it. (Optional future work: pre-author static pair-banks across the 6 tones — WARM / PLAYFUL / SARCASTIC / ARGUMENTATIVE / HOSTILE / REACTIVE — for NEW_001..NEW_010; additive only.)

> **DM:** Until Phase D ships, fall back to KM_Companions_Behaviors.md (Part A — Active 5 + Manor 5 + Quest-Locked) for any banter need. Do not improvise Section D voices from memory.

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Banter Expansion v3.0 (v93.19 Sub-F purge)*
*Load alongside KM_Companions_Behaviors.md every session.*


---

---

## BUILD ASSIGNMENT / COMBAT AI / SELECTION REF / LEVELING / SCALED STATS — MOVED (v95.9)
> Companion build assignments, Combat AI defaults, the full selection reference, leveling maps, and scaled stat blocks were split to **KM_Companions_Behaviors_B.md** for file-size compliance. Load it during leveling, combat, and companion selection.
