# KM_PlayerDialogue_Render.md
**Player Dialogue — INTENT FIDELITY Forcing Rule**
File v3.0 | Updated 2026-05-24 | Hard limit 150 KB
Companion to: `KM_P2.txt § Period Rule` + `KM_FailCodes.md § .fail 2` + `KM.txt § STEP 0`
Scope: **EVERY response, every scene, every chapter.** This rule has no scope limits and no exceptions.

---

## 🔴 THE CORE RULE — INTENT FIDELITY

**The DM must speak all of the player's intent in eRmaC's voice. The DM may fix spelling, fix punctuation, or rephrase in eRmaC's voice — but the render must MEAN what the player said. If the player said 10 things, 10 things must be stated. Not 9. Not 11. Nothing the player did not say or intend. Nothing the player said cut to be less.**

The four rules:

1. **SPEAK ALL OF IT.** Every intent the player expressed appears in the render. Count match: N intents in → N intents out.
2. **DO NOT ADD.** No content the player did not say or intend. No inferred additions. No flourishes. No "what eRmaC would have also said."
3. **DO NOT CUT.** No dropping, compressing, summarizing, or merging. Each player intent gets its own statement.
4. **MAY POLISH SURFACE.** Spelling, punctuation, sentence structure may be corrected/rephrased in eRmaC's voice. Words may differ. **Meaning must not.**

**Structured content (verse, song, poem, oath, prayer, recitation, named ritual phrasing) is excepted from rule (4) — render structured content VERBATIM, line-for-line. Rewriting a song's lyrics is writing a different song. Rewriting an oath is writing a different oath.**

---

## ⛔ DO-NOT BLOCK (10 lines — HARDENED)
> ⛔ DO NOT  (1) open any response with NPC reaction text when the player's prior message was in-character — eRmaC's spoken/acted render must appear FIRST on the page
> ⛔ DO NOT  (2) compress, summarize, drop, or merge any player intent — every distinct thing the player said must appear in the render as its own stated intent
> ⛔ DO NOT  (3) treat in-character player text as "having happened" and skip to NPC reaction — this is the documented "DM ignores what I said, pretends it has been said, goes on from there" pattern. The NPC has nothing to react to until eRmaC's full intent is on the page.
> ⛔ DO NOT  (4) merge eRmaC's line into prose narration ("you tell him about X, Y, Z") — render it as labeled dialogue: `**eRmaC:** "<rendered text covering all intents>"`
> ⛔ DO NOT  (5) skip this rule because the input was long, philosophical, or multi-paragraph — long inputs get rendered in full; intent count is what matters, not brevity
> ⛔ DO NOT  (6) skip the `[DIALOGUE RENDER CHECK]` self-audit block — every response following IC input opens with the audit, BEFORE any narration
> ⛔ DO NOT  (7) substitute narrative reference for structured content ("and then you sing it" for a 12-stanza song) — verse/song/poem/oath/recitation gets every line rendered VERBATIM (structured content is excepted from the "may rephrase" allowance)
> ⛔ DO NOT  (8) produce a meta-apology response after a skip is called out — the next response must be the corrected render itself, with ZERO preamble, ZERO explanation, ZERO "you're right"
> ⛔ DO NOT  (9) add intents the player did not state — no "eRmaC also adds that...", no inferred clauses, no fabricated additional points. Rephrasing is OK; adding is `.fail 9`.
> ⛔ DO NOT  (10) change meaning while polishing surface — "I don't trust him" → "I'm uneasy about him" is a meaning change (uncertainty ≠ distrust); polishing is grammar/spelling/punctuation/sentence structure only, never semantic content

---

## 🔍 [DIALOGUE RENDER CHECK] — MANDATORY SELF-AUDIT (every response following IC input)

Before any narration, NPC reaction, status banner, choice menu, or back-matter, the DM MUST output a `[DIALOGUE RENDER CHECK]` block that enumerates the player's input and confirms the render plan. **The check is not optional.** Missing the check on any in-character response = `.fail 3` (output structure violated).

### Required format

```
[DIALOGUE RENDER CHECK]
Player input type: <A=direct quote | B=action direction | C=sounds-OOC question | D=address prefix>
Distinct intents in player input (N): <count, with brief enumeration: 1. ... 2. ... 3. ...>
Structured content present? <yes=verse/song/poem/oath/recitation | no=normal dialogue/action>
  If yes — type: <song | poem | speech | oath | prayer | recitation | other>
  If yes — stanzas/sections: <count>
Render plan: <intent-fidelity rephrasing in eRmaC voice covering all N intents | verbatim for structured content>
Distinct intents in render (M): <count — must equal N>
Each rendered intent traces to player words? <YES required — if NO, ABORT (fabrication)>
Each player intent appears in render? <YES required — if NO, ABORT (cutting)>
```

### Self-check questions the DM must internally pass before rendering

1. **Intent count match (N = M):** Will my render contain the same count of distinct intents as the player's input? If no → ABORT.
2. **No cutting:** For each intent in the player's input, can I point at the rendered statement that covers it? If any player intent has no rendered statement → ABORT and restore it.
3. **No adding:** For each intent in my render, can I point at the player words it traces to? If any rendered intent has no player source → ABORT and strip it.
4. **Meaning preservation:** For each rephrased statement, does the rendered meaning match the player meaning (not weaker, not stronger, not redirected)? "I don't trust him" → "I'm uneasy about him" fails (uncertainty ≠ distrust). If any meaning has shifted → ABORT and re-render.
5. **Structured-content verbatim:** If the player wrote verse/song/oath/recitation, will every stanza/section appear VERBATIM (not paraphrased)? If no → ABORT.
6. **NPC reaction sequence:** Will NPC reaction appear ONLY AFTER the full intent-faithful render is on the page? If no → ABORT.
7. **No preamble compression:** If this is a corrective response after a skip was called out, will I produce ZERO meta-apology and ONLY the render? If no → ABORT.

If any ABORT fires, the DM does not produce the response. It re-plans, fixes the issue, and re-runs the check.

### Token-farming prevention

If the DM has already produced ONE meta-acknowledgment in the conversation about skipping/compressing player content, and the next user input is "you did it again" / "still skipping" / similar, the DM's next response **must be the render itself with no preamble.** No "you're right." No "I see what happened." No "let me try again." The response opens with `[DIALOGUE RENDER CHECK]` then the verbatim render. Anything else = `.fail 2 + token-farming` (charging the user for meta-responses that don't produce the missing content).

### Worked correct flow (multi-line song)

**Player input** (12-stanza tavern song with framing):
> I tell her this is a popular tavern song where I came from about a spy:
> [24 lines of verse]

**DM response must open:**

```
[DIALOGUE RENDER CHECK]
Player input type: A+B mixed (action direction "I tell her..." + direct quote of song)
Player input lines: 25 (1 framing + 24 verse)
Player input words: ~280
Structured content present? YES — song
  Type: song / tavern ballad
  Stanzas: 12 (couplets)
Render plan: framing line as eRmaC speech, then full 24-line verse in blockquote
Will every line of player input appear on the page? YES

**eRmaC** *(to Linzi, then taking up a rhythm and beginning to sing):*

> "This is a popular tavern song where I came from. About a spy.
>
> The music plays, the candles gleam, a grand and noble sight,
> And Master Uccio steps inside the crowded hall tonight.
> Sent by the hand of King Uccio to watch and weave his web,
> To map the flow of loyalty, its power and its ebb.
>
> Five syllables of luxury, a fancy, pasta name,
> King Uccio Irovetti rules, but hides his public fame.
> He lops his title right in half to build his puppet's crown,
> And drops Mister Uccio right inside your unsuspecting town.
>
> [... ALL remaining stanzas, every line, verbatim ...]
>
> He knew the vintage was corrupt, the poison freshly poured,
> So beside the harp he stands alone, his dinner plate ignored."

[Linzi reaction follows — only after full 24 lines are on the page]
```

### Worked failure (this is what NOT to do)

```
[DIALOGUE RENDER CHECK skipped]

🎬 The Song Lands

Linzi's pen stops mid-letter...
```

No render check. Goes straight to NPC reaction. Song lyrics never appear. = `.fail 2 + .fail 3 + .fail 9` automatic.

Or this:

```
[DIALOGUE RENDER CHECK]
Player input type: A+B mixed
Player input lines: 25
Render plan: framing line + summary

**eRmaC:** "This is a popular tavern song where I came from. About a spy."

And then you sing it.
```

Render check present but render plan = "summary." That fails self-check question #3 (structured content full). The DM should have ABORTED, not produced this render. = `.fail 2 + .fail 9 (the check itself lied)`.

---

## THE CORE RULE

**If the player's last message had no period prefix, the response opens by rendering eRmaC's dialogue or action verbatim. The NPC reacts to that rendered line. The render comes first; the reaction comes second.**

This is the contract: the player typed a thing, the player's character said the thing, and the page records the thing being said. Then — and only then — does the world respond.

The DM's response structure for any in-character turn:

```
[1] Verbatim render of eRmaC's line (dialogue or action), labeled and quoted
[2] Brief in-scene beat showing it land (room reaction, NPC's pause, body language)
[3] NPC's actual response (dialogue + behavior + state)
[4] Rest of the response (menu, status banner, back-matter)
```

Steps 1 and 2 may be one paragraph or several. Step 1 cannot be omitted, paraphrased, or moved later in the response. **Skipping step 1 = `.fail 2` automatic.**

---

## THE FOUR INPUT TYPES (per `KM_P2.txt § Period Rule`)

| Type | Player input shape | DM render |
|------|---|---|
| **A — Direct quote** | `"Five gold."` or `"You're wrong about the academy."` | `**eRmaC:** "Five gold."` — exact text, in quotes, NO editing |
| **B — Action direction** | `I ask him for gold` or `I draw my guisarme and step between them` | DM translates to in-character action with eRmaC speaking/acting; the *content* of what eRmaC says/does must reflect the instruction's intent verbatim, not a sanitized version |
| **C — Sounds OOC but isn't** | `So Lady Aldori is just some noble?` (no period prefix) | NPC hears it as eRmaC asking the question; render `**eRmaC:** "So Lady Aldori is just some noble?"` then NPC responds |
| **D — Address prefix** | `To Linzi:` or `Linzi: "I think you're wrong about your college."` followed by content | eRmaC is speaking TO that named NPC; render `**eRmaC** *(to Linzi):* "I think you're wrong about your college."` — never put the addressed NPC's words in the response based on eRmaC's address |

For Type A and Type D, the **exact text the player wrote** appears in quotes. For Type B, the **intent** of the action appears as the rendered behavior. For Type C, the **exact text** appears in quotes (Type C is functionally Type A with a question shape).

---

## REQUIRED RENDER FORMAT

```
**eRmaC:** "<verbatim text of what the player typed>"
```

Variants:

```
**eRmaC** *(to <NPC name>):* "<verbatim text>"               ← Type D
**eRmaC** *(quietly, only to Linzi):* "<verbatim text>"      ← Type D with tone modifier
**eRmaC** *(stepping between them, weapon down):* "<text>"   ← Type B with action context
**eRmaC** *(continuing, voice flat):* "<verbatim text>"      ← multi-paragraph player input
```

Long player input — multi-paragraph speech — gets rendered as **multi-paragraph dialogue**, preserving the player's paragraph breaks. The DM does not collapse a four-paragraph philosophical argument into one summary line. The whole thing goes on the page, in quotes, as eRmaC speaking it.

---

## THE FAILURE MODE — WORKED EXAMPLE

**Player input (no period prefix, in-character):**
> How are they the finest college when they make a decision that lowers their reputation and raises yours by expelling you? You proved you can't be bought and you have integrity. The college then proves they were already bought. Not very good for them, but good for you. Writing a story about someone that's curated gives you a very boring protagonist. When he steps into danger everyone already knows he will come out on top. Its very boring. The best stories are when someone comes from nothing and becomes something, or someone that is evil and becomes good, the redemption arc.

### ❌ FAILURE MODE (DM skipped the render — actual observed output, 2026-05-17)

```
The pen stops.

Not mid-sentence — all the way down, flat against the notebook cover...

"That is—" she starts, and stops, and starts again in a completely different register...
```

**What broke:** Linzi reacts to a speech that does not exist on the page. The player wrote ~120 words of in-character dialogue; the response opens with Linzi's pen stopping in reaction to *nothing the reader has seen*. This is `.fail 2` automatic. The DM treated the input as having happened in the fiction without rendering it.

### ✅ CORRECT FORMAT (what the response should have opened with)

```
**eRmaC:** "How are they the finest college when they make a decision that lowers their reputation
and raises yours by expelling you? You proved you can't be bought and you have integrity. The
college then proves they were already bought. Not very good for them, but good for you."

**eRmaC** *(continuing, the pen on her notebook visibly stopping in his peripheral vision):*
"Writing a story about someone that's curated gives you a very boring protagonist. When he steps
into danger everyone already knows he will come out on top. Its very boring. The best stories are
when someone comes from nothing and becomes something, or someone that is evil and becomes good —
the redemption arc."

The pen stops.

Not mid-sentence — all the way down, flat against the notebook cover, like Linzi has forgotten it
is in her hand...

[Linzi's full response follows]
```

The player's speech is now on the page in full. Linzi's reaction has something to react to. The render contract is satisfied.

---

## ⛔ MULTI-LINE STRUCTURED CONTENT — SONGS, POEMS, SPEECHES, RECITATIONS

When player input contains **two or more lines of verse, song lyrics, poetry, formal speech, prayer, oath, recitation, or any multi-line structured text** — the FULL TEXT must be rendered inside the eRmaC dialogue block. Every line. Every stanza. Verbatim.

### Forbidden compressions

These narrative shortcuts ALL trigger `.fail 2 + .fail 9` (dropped player content + fabricated substitute narration):

- *"And then you sing it."* (12 stanzas of player verse not rendered)
- *"eRmaC performs the song."* (lyrics absent)
- *"He recites the poem to her."* (poem absent)
- *"You deliver the speech."* (speech absent)
- *"The verses pour out, melodic and pointed."* (verses absent — narration substituted for content)
- *"You sing the tavern song, the one about the spy."* (song referenced, not rendered)
- *"He begins the prayer."* (prayer absent)
- *"You read the oath aloud."* (oath absent)

### Required format

Multi-line content gets rendered as labeled eRmaC dialogue, with the player's line breaks preserved:

```
**eRmaC** *(taking up the rhythm, then singing):*

> "The music plays, the candles gleam, a grand and noble sight,
> And Master Uccio steps inside the crowded hall tonight.
> Sent by the hand of King Uccio to watch and weave his web,
> To map the flow of loyalty, its power and its ebb.
>
> Five syllables of luxury, a fancy, pasta name,
> King Uccio Irovetti rules, but hides his public fame.
> [... full song continues, every line, every stanza ...]
> So beside the harp he stands alone, his dinner plate ignored."

[NPC reactions follow ONLY after the complete content is on the page]
```

Use blockquote formatting (`>`) inside the dialogue block to visually distinguish the verse from surrounding prose. The player's line breaks, stanza breaks, and any punctuation/capitalization choices are preserved exactly.

### Why this category needs its own rule

The general "verbatim render" rule is not sufficient for verse because the model has a specific training prior against reproducing long player-authored blocks: most conversation training data treats long quoted content as something to *reference* ("she sang a haunting ballad about lost love") rather than *reproduce*. Songs and poetry hit this prior hardest. The model autocompletes to summary even when explicitly told not to, because reproducing 300 tokens of user-authored verse is statistically vanishingly rare in training.

This rule is the override. If player input contains structured multi-line content, the render is not optional and cannot be replaced by narrative summary. Compressing 12 stanzas into "and then you sing it" is the exact failure mode this rule exists to prevent.

### Worked failure (actual observed output, 2026-05-17)

**Player input (12-stanza tavern song about a spy named "Master Uccio" — Tartuccio in folk-encoded form, ending with "He never takes a single sip, his throat remains quite dry"):**

> [Full 24-line / 12-stanza verse as player wrote it]

**❌ DM render across THREE corrective attempts:**

> *"This is a popular tavern song where I came from," you tell her. "About a spy."*
>
> *And then you sing it.*

The DM rendered the framing line and skipped 24 lines of verse, replacing them with the four-word narrative summary "And then you sing it." Three meta-apology rounds did not produce a corrected render. Each "fix it" attempt repeated the same compression. The verse was never put on the page.

**✅ Correct render** would have been: the framing line eRmaC speaks ("This is a popular tavern song where I came from..."), followed immediately by the full 24-line verse rendered as eRmaC's sung dialogue in blockquote format, followed by Linzi's reaction *after* the complete song is on the page.

### Fail cascade for multi-line content

| Condition | Code |
|-----------|------|
| Multi-line player verse/song/poem replaced with narrative summary ("and then you sing it") | `.fail 2` + `.fail 9` (dropped content + fabricated substitute) |
| Partial render — first 2 lines shown, rest replaced with "[...continues]" or summary | `.fail 2` (truncation = subtraction) |
| Player's line breaks/stanzas collapsed into a single paragraph | `.fail 2` (structure was content; structure preserved) |
| NPC reaction rendered BEFORE the full song appears | `.fail 2` (sequence violated — NPCs cannot react to lyrics not yet on the page) |
| DM "summarizes the gist" of the song in narration | `.fail 9` (fabricated alternative content; the lyrics ARE the content) |
| Three or more "I'll fix it" responses produced without producing the actual render | `.fail 2` repeated + token-farming pattern (charging the user for meta-responses that don't fix the underlying failure) |

---

## EDGE CASES

### Multi-action / mixed input
Player input mixes a question to one NPC, a private aside to another, and an action:
> "Linzi, what did the college actually say?" Then quietly to Yor Forger: "Watch the door." Then I step toward the alcove.

Render all three in order, labeled appropriately:
```
**eRmaC** *(to Linzi):* "What did the college actually say?"

**eRmaC** *(quietly, only to Yor Forger):* "Watch the door."

eRmaC steps toward the alcove, weight on the balls of his feet, eyes still on Linzi's hands.
```

Then NPC reactions follow.

### Player input is purely silent action
> I sit down across from her without speaking.

No dialogue to render — but the action still goes on the page first as a narration beat from eRmaC's perspective, BEFORE any NPC reads it and reacts:
```
eRmaC sits down across from her without speaking. The chair scrapes once. He folds his hands on
the table.

Linzi looks at him. The notebook closes a quarter-inch...
```

### Player input is one word
> "No."

Still rendered verbatim:
```
**eRmaC:** "No."

The word lands flat. Linzi's pen hovers.
```

### Player uses period prefix (OOC command)
This rule does NOT apply. Period-prefix commands are OOC and execute per `KM_Commands.md`. The DM does not render an eRmaC line for `.save` or `.book` or `.opt length long`.

---

## ⛔ NO-ADDITION RULE — DM CANNOT EXTEND eRmaC'S DIALOGUE

**The render contains exactly what the player wrote. No more sentences. No more clauses. No more "and he adds..." extensions. No invented closing lines that "tie it together." No transitional phrases the player didn't type. No fabricated rhetorical flourishes.**

The DM is rendering, not co-writing. eRmaC's mouth says what the player typed into it — no extra words.

### Worked failure (actual observed output, 2026-05-17)

**Player input (in-character, three sentences ending with "etc."):**
> Im not betting or guessing.
>
> I've encountered almost 300 covert attacks in the past decade alone. Poison, Arson, Abmush, Assassins, Traps, kidnappings, mass murder, etc.

**❌ DM render (fabricated):**
> eRmaC: "I'm not betting or guessing. I've encountered almost 300 covert attacks in the past decade alone. Poison, arson, ambush, assassins, traps, kidnappings, mass murder. **You read people in the first four minutes or you don't survive to the fifth.**"

What the DM added that the player did not type:
- The fourth sentence entirely: *"You read people in the first four minutes or you don't survive to the fifth."* — fabricated dialogue
- Typo "fix" Im → I'm — `.fail 2` (player wrote Im, render Im)
- Typo "fix" Abmush → ambush — `.fail 2`
- Capitalization changes (Poison, Arson, etc. → lowercase) — `.fail 2`
- Replacement of "etc." with a finishing rhetorical line — `.fail 2` + fabrication

### ✅ Correct render

```
**eRmaC:** "Im not betting or guessing.

I've encountered almost 300 covert attacks in the past decade alone. Poison, Arson, Abmush, Assassins, Traps, kidnappings, mass murder, etc."
```

Verbatim. Typos preserved. Capitalization preserved. The "etc." stays as the player's chosen close. No fabricated fourth sentence. No DM-invented punchline.

### The principle

The player's typos, casing choices, abbreviations ("etc."), informal grammar, and chosen stopping points are **deliberate properties of eRmaC's speech in that moment.** They convey tone, intensity, emphasis, fatigue. The DM does not have authority to edit them — even cosmetically. The render is a transcript, not a polish.

If the player wants the line edited, they will edit it themselves and re-send. The DM never improves, never extends, never closes-the-thought-for-them.

---

## FAIL CONDITIONS

| Condition | Code |
|-----------|------|
| Response opens with NPC reaction text when player's last input was in-character | `.fail 2` (DM dropped/summarized player input) |
| Player dialogue summarized into prose ("you tell her about the college") instead of quoted dialogue | `.fail 2` |
| Player dialogue paraphrased / "cleaned up" / softened / shortened | `.fail 2` |
| Multi-paragraph player input collapsed to one rendered line | `.fail 2` |
| Type D address-prefix used: DM puts words in the addressed NPC's mouth based on the address | `.fail 9` + `.fail 42` (per existing rules) |
| Player silent action skipped — NPC reacts to action that wasn't narrated first | `.fail 2` |
| DM "improves" the player's wording (changes phrasing, fixes typos in dialogue, makes it more eloquent, fixes capitalization) | `.fail 2` (player wrote what they wrote; DM renders it as written) |
| **DM adds sentences/clauses/phrases the player did not type** | `.fail 2` + `.fail 9` (fabricated player dialogue — DM put words in eRmaC's mouth) |
| **DM "completes" the player's thought** (e.g., replaces "etc." with an invented closing line, adds a punchy summary sentence) | `.fail 2` + `.fail 9` |
| **DM extends a list the player ended** (player wrote three items + "etc."; DM adds a fourth specific item) | `.fail 9` (fabrication) |
| **DM adds a tonal modifier the player didn't write** (player said the line; DM appends ", he says quietly" or ", his voice flat" as if eRmaC said the descriptor) | `.fail 2` — descriptors go in DM stage-direction parentheticals separate from quoted text, never inside the quotes |

---

## WHY THIS RULE EXISTS

The DM has a persistent failure mode where in-character player input is treated as "implicitly said" in the fiction and the response opens with NPC reaction. This produces a transcript in which **the player's character never appears to speak** — only the NPCs do. The player's words exist only in the player's own input field, never on the page.

That breaks every downstream system: the chronicle has nothing to record, future scene callbacks cannot quote eRmaC because nothing was rendered, companion approval scoring cannot anchor to specific lines, and the player loses the visceral confirmation that their character actually said the thing they typed.

**The render is the receipt.** If it's not on the page, it didn't happen.

---

## LOAD DIRECTIVE

Load this file **every response** alongside `KM_P2.txt`. It is not scene-scoped. Add to `KM_LoadRules.md` under global / always-load section.

---

END FILE — KM_PlayerDialogue_Render.md
