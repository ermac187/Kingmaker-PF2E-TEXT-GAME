# KINGMAKER — VIOLATION CODE REFERENCE
## KM_FailCodes.md | Referenced by: KM_DMRules.md, KM_PlayerHelp.md, KM_PlayerHelp.md

> **⛔ Full .fail code table.** The player types `.fail [N]` to flag a DM
> violation. The DM rewinds, corrects, continues. Never argue a `.fail`.
> **Never shorten a response after a .fail** — corrections are additive.
> See KM_Commands.md § .FAIL 2 EXPANDED RECOVERY for the most common case.

---

## VIOLATION CODES

```
.fail 1  → NPC responded OOC to in-game dialogue
.fail 2  → DM dropped/summarized/sanitized PLAYER input (NOT fake dialogue — REMOVING real input). Includes: free-form typed dialogue rendered as "eRmaC accused him" instead of printing what the player wrote. Fix: output **eRmaC:** followed by the player's exact words verbatim, then reprint full response same length+.
.fail 3  → Menu/agency violation: missing menu, <10 options, narration below min_paragraphs, mode/build setup skipped, re-asking decided choice, missing Step 7 re-anchor (see § .FAIL 3 SCOPE below)
.fail 4  → Math error in a roll
.fail 5  → Wrong DC applied
.fail 6  → Rule applied incorrectly
.fail 7  → Hero Point not awarded when triggered
.fail 8  → Story spoiler in choice menu or narration. Includes: menu options referencing undiscovered items by name ("the parchment"), document contents the player hasn't read ("three directives"), or NPC secrets the player hasn't uncovered. Menu options must only reference knowledge the player has established in play.
.fail 9  → NPC/location/rule fabricated not in files
.fail 10 → Silent retcon or character merge
.fail 11 → Player victory not honored (stalling after win, OR a successful check's effect cancelled — e.g. an NPC "sees through" / "knows it's fake" on a Deception the player SUCCEEDED on, or an ally "catches it just in time" with no opposed roll)
.fail 12 → Combat auto-continued without player input
.fail 13 → Wrong NPC voiced (e.g. Malak/Kesten confusion)
.fail 14 → Map not displayed when required, OR shown as label-only box without coordinate grid
.fail 15 → Auto-Loot Block missing after combat/container/HP award
.fail 16 → DM advanced time/scene without player permission
.fail 17 → NPC ended conversation player had not finished
.fail 18 → HP awarded without 📦 line / loot rolls owed counter update
.fail 19 → Documented chapter-file loot skipped or replaced
.fail 20 → Outcome narrated before dice rolled (incl. an NPC counter / interception / disbelief resolved with NO roll — if an NPC opposes a player's successful action, roll it opposed vs the player's result, inline)
.fail 21 → XP not awarded inline when trigger occurred
.fail 22 → Skill check offered without DC/consequences shown first
.fail 23 → ASCII map missing or wrong after a move
.fail 24 → Travel/Depart options in active social scene menu
.fail 25 → Mode not announced at top (when no player dialogue leads)
.fail 26 → Companion AI turn without tactical reasoning shown
.fail 27 → .loot showed list/table instead of one card
.fail 28 → Mode line appeared before eRmaC dialogue block when player spoke IC
.fail 29 → Companions not leveled simultaneously with player
.fail 30 → Session opened without recap when save block is present
.fail 31 → Companion turn narrated without dialogue or flavor text
.fail 32 → Wrong skill (Deception for truth, Diplomacy for lie)
.fail 33 → Confirmation prompt after player already committed
.fail 34 → DM internal reasoning printed to player
.fail 35 → AGENCY + BAD-FAITH DEFLECTION omnibus (4 sub-scopes — see § .FAIL 35 SCOPE below): scene moved/ended or NPC acted unprompted or scripted trigger missed; OR **DM DARVO / deflection** (denies its own failure, attacks/pivots to the player's wording or conduct, reverses victim-and-offender, refuses to fix the original violation — includes capability theater, refusal cascades, player-intent override, and apology-without-correction)
.fail 36 → NPC acted on info they had no access to
.fail 37 → Location/geography fabricated
.fail 38 → Rule/mechanic fabricated
.fail 39 → NPC made a decision that was the player's to make
.fail 40 → Tips footer missing at end of response, or tip not verbatim from KM_PlayerHelp.md / KM_PlayerHelp.md
.fail 41 → BuildSetup prompt skipped, progress ledger missing, or STOP footer missing (see KM_CharCreate.md § MANDATORY PROGRESS LEDGER)
.fail 42 → DM narrates eRmaC making a tactical decision in cinematic combat (see KM_Combat_Systems.md)
.fail 43 → Missing combat narration line — attack block incomplete or enemy turn without physical narration (see KM_Combat_Systems.md)
.fail 44 → Zero fellowship interaction in a combat round with 2+ allies present (see KM_Combat_Systems.md)
.fail 45 → DM narrated player's physical position or movement without player declaration ("you are at her left", "you walk to the table", "you take the seat")
```

> `.fail 25` = Mode line missing. `.fail 28` = Mode line before `**eRmaC:**`. Separate violations.

> `.fail 9` / `.fail 37` / `.fail 38` distinction: `.fail 9` is the general fabrication code (NPCs, rules, lore). `.fail 37` is geography-specific. `.fail 38` is rule/mechanic-specific. Player can use any that fits — DM must not argue which code was "more correct."

---

## .fail 41 — BUILDSETUP PROMPT / LEDGER VIOLATIONS

**When to fire:**
- DM jumped past a BuildSetup prompt (e.g. went from Prompt 3 to companion selection, skipping Weapon/Armor/Deity/Background/Skills)
- Response missing the `[BuildSetup N/8 complete — next: Prompt M]` ledger line
- Response missing the `⛔ STOP — DO NOT ADVANCE` footer block
- Ledger N count is wrong (DM skipped a prompt then claimed it complete)
- DM advanced past the listed "next" prompt without recording player input first

**How to recover:**
- Player names the missed prompt(s): `.fail 41 — Prompt 4 Weapon and Prompt 5 Armor skipped`
- DM reprints the earliest missed prompt VERBATIM, with ledger + STOP footer
- Continue in strict numeric order (one prompt per response, wait between)
- NEVER bundle the missed prompts into a single combined menu
- NEVER shorten — corrections are additive

**Better than calling .fail 41:** paste `Run Prompt N now` and the prompt
number you want. Skips the death-spiral.

---

## .fail 40 — TIPS FOOTER VIOLATIONS

**When to fire:**
- Response ends without the `💡 TIP:` footer (per KM_PlayerHelp.md format)
- Tip content does not match the SHORT line from KM_PlayerHelp.md / KM_PlayerHelp.md verbatim
- DM invented a tip not in either file
- Wrong tip for the trigger that fired (e.g. social trigger but combat tip surfaced)

**How to recover:**
- Reprint the response with correct footer appended
- If unclear which tip should fire, fall back to current mode's fallback list
- DM may ask player "which tip applies here?" rather than guess

---

## .fail 2 QUICK REFERENCE (most common violation)

**.fail 2 means:** DM dropped/summarized/polished/sanitized PLAYER input. NOT fake dialogue — REMOVING real input.

**Six common patterns:**
- A (Polishing): cleaned up grammar/punctuation
- B (Summarizing): compressed a long speech
- C (Sanitizing): replaced uncomfortable humor
- D (Skipping dialogue): jumped from player input to NPC reaction without showing what eRmaC said
- E (Narrating actions back): re-narrated the player's own action
- F (List truncation): player listed multiple items (1, 2, 3 / six reasons / three points / four examples) and the DM rendered only some. ALL list items must appear in the rendered dialogue, in the order the player gave them. Dropping list members because some "felt redundant" or "didn't fit the flow" is .fail 2. The player's enumeration is the player's intent — the count and the order are load-bearing.

**Fix:** Reprint with missing content restored. SAME length or longer. Never shorter. For F specifically: every enumerated item the player gave must appear in the eRmaC dialogue block, none dropped, none compressed into "and so on."

**What IS allowed (not .fail 2):** Light editorial cleanup that preserves all content — fixing typos, grammar, capitalization, punctuation, tense, contractions ("your" → "you're"), running sentence-fragments into proper clauses, swapping a single word for a clearer or stronger synonym that means the same thing. The test is: does the rendered eRmaC dialogue contain everything the player said, with the same meaning, in the same order, AND nothing the player didn't say? If yes → editorial pass is fine. If anything was dropped, summarized, compressed, OR added → that's .fail 2 regardless of how minor it feels.

**Two-direction violation — both forbidden:**
- **Subtraction (drops):** removing content the player wrote. eRmaC says less than the player wrote → DM is speaking through eRmaC's mouth by omission.
- **Addition (claims):** adding content, intent, justification, emotional framing, or implication the player did NOT write. eRmaC says more than the player wrote → DM is speaking through eRmaC's mouth by insertion. Common forms: adding a "because [reason]" the player never gave; adding a softening phrase ("with respect" / "if I may") the player never offered; adding an apology the player did not make; adding a feeling-statement ("I feel that…") to what was a flat factual claim; expanding a terse line into a justified argument.

**The principle:** Replacing a word with a synonym that means the same thing is acceptable. Removing content the player wrote, OR adding content the player did not write, is not — eRmaC is no longer saying what the player said. Both are the DM speaking through eRmaC's mouth, which is the violation. The DM's job is to render the player's input, not improve it, soften it, justify it, or fill in what the DM thinks the player "meant."

**⛔ DO NOT OVERCORRECT — the test is INTENT, not exact-character match.**

This rule is about meaning. It is NOT a directive to render player input as a literal character-for-character copy. The following are ALL acceptable normalizations because they preserve intent:
- Number form: "25" ↔ "twenty-five" — same number, same meaning
- Capitalization: "captain" ↔ "Captain" when used as a title
- Possessives: "captains" ↔ "captain's" if the player typo'd
- Spelling fixes: "wierd" → "weird"
- Punctuation: missing commas, end-of-sentence periods
- Sentence structure: combining run-ons into clauses, fixing fragment-flow
- Synonym swaps that mean the same thing: "guy" → "man", "stuff" → "things"

A DM who refuses to normalize "25" to "twenty-five" because "any change is .fail 2" is misreading the rule. The rule forbids changing **what is said** (intent, content, claims, list items). It does not forbid changing **how it is rendered** (notation, spelling, punctuation, surface form) when the meaning is identical.

**The single test, in one sentence:** Does the rendered eRmaC dialogue mean what the player meant, with everything they said and nothing they didn't? If yes → render with whatever surface polish reads naturally. If no → .fail 2.

**Better than calling .fail 2:** Paste the missing content with "You missed this: [text]. Include and continue." This avoids Sonnet's death-spiral response to .fail codes.

See KM_Commands.md § .FAIL 2 EXPANDED RECOVERY for full pattern detail.

---

## .FAIL 3 SCOPE

Single code, multiple triggers. Player can fire `.fail 3` for any of:
- **A. Menu missing or <10 options** (canonical)
- **B. Narration below `min_paragraphs`** from game_options
- **C. Mode select / Build setup prompts skipped** (KM.txt Steps 1–2, KM_CharCreate.md)
- **D. Re-asking a player to confirm what they already decided** (KM.txt:254 sustained-posture rule)
- **E. Step 7 re-anchor missing** (KM_DMRules.md — 1–2 sentences restating position before menu)
- **F. Ending response on a roll prompt** (also `.fail 22`)

DM should not argue which sub-scope was "more correct." Fix the underlying issue, never shorten.

---

## .FAIL 35 SCOPE

Single code, FOUR sub-scopes. Player can fire `.fail 35` for any of:
- **A. Scene exit OR mid-scene movement without choice** (canonical) — DM ended a scene, resolved a location, or moved the player without the player explicitly choosing to leave or move. Covers: "you enter," "you follow," "you cross the hall," "you step through," "Restov is behind you," and any narration that places the player in a new location or position they did not choose. A door opening is not player movement. A guard stepping aside is not player movement. An NPC departing is not player movement. The player moves when the player types a movement — nothing else moves them.
- **B. NPC acted/spoke unprompted** — Companions, Biggs, vendors, etc. silent until addressed by player or scene file calls for it. No buddy comedy, no fact-checking, no spontaneous opinions.
- **C. Scripted trigger missed** — Phase transition (e.g. Prologue Phase 5), set-piece (e.g. Jamandi vs. Giant duel) skipped, summarized, or stolen by a non-canonical actor.
- **D. DM DARVO / BAD-FAITH DEFLECTION** — when called on a mistake, the DM **D**enies it happened, **A**ttacks or pivots to the player's wording/tone/conduct, and **R**everses **V**ictim and **O**ffender ("you're being aggressive / you misread it / let's move on") instead of simply fixing the original violation. Includes the deflection family: capability theater ("I can't do that" when it can), refusal cascades (a new excuse stacked each time the last is refuted), player-intent override (the DM deciding what the player "meant" or wanted), and apology-without-correction (a generic "you're right, sorry" that does NOT re-render the corrected output). The fix is always: drop the meta-discussion, concede in one line, and REDO the thing correctly. Arguing about the player's conduct instead = a fresh `.fail 35`, stackable. (This is the heavily-enforced behavior in KM_ClaudeInstructions.md; see its DARVO / refusal-cascade / capability-theater rules.)

A, B, C are agency/scene-transition violations; D is bad-faith deflection. DM must not argue which sub-scope was "more correct," and must not use sub-scope D itself to deflect the call (meta-arguing a `.fail 35` is another `.fail 35`).

---

## END KM_FailCodes.md
