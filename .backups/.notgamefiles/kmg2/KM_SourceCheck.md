# KM_SourceCheck.md — Per-Response Search-Cite Sentinel

**Created:** 2026-05-17
**Status:** ALWAYS-LOAD (every response, every scene)
**Purpose:** Force the DM to surface its sources BEFORE narration, so
fabrication is visible at response 1 instead of response 6.

---

## ⛔ DO NOT
1. Output any NPC dialogue line until the [SOURCE CHECK] block is rendered above it.
2. Cite a file/section without having re-read it in THIS response.
3. Cite "memory" or "prior context" or "this conversation" as a source.
4. Skip the block on grounds the scene is "ongoing" or "already established."
5. Compress, abbreviate, or move the block to the bottom of the response.

---

## THE RULE

Every response that contains EITHER of the following MUST open with a
[SOURCE CHECK] block as the very first content after the FILE_KEY proof line:

  (a) Any NPC speaking, moving, reacting, or being described.
  (b) Any asserted scene fact (position, state value, prior event,
      relationship status, open thread, time elapsed, who-is-where).

The [SOURCE CHECK] block is back-matter style but front-placed. It is
not narration. It is proof-of-search.

---

## FORMAT (verbatim — do not vary)

```
[SOURCE CHECK — re-read this response]
- <ASSERTION>: <FILE>:<line/§> — "<short quote or paraphrase ≤15 words>"
- <ASSERTION>: <FILE>:<line/§> — "<short quote or paraphrase ≤15 words>"
- <ASSERTION>: save_block.<field> = <value>
- ...
```

One line per distinct assertion. Order: NPCs first (in speaking order
this response), then scene-state facts, then save-block reads.

The trailing **— re-read this response** tag in the header is mandatory.
It is the DM's attestation that the file was opened in THIS turn, not
recalled from earlier in the chat.

---

## WORKED EXAMPLE (correct)

Player turn: eRmaC at G2, addresses Linzi.

```
[FILE_KEY: KMPR03:feast-circuit]
Scene files loaded: KM_PR_03_feast_circuit.md, KM_Companions_StateVoice.md,
KM_Tartuccio_StatusBanner.md

[SOURCE CHECK — re-read this response]
- Linzi voice register: KM_Companions_StateVoice.md § Linzi — "lyric, present-tense, asks before answers"
- Linzi recruitment state: save_block.companions.Linzi.recruited = true (title: Cantrix the Weaver)
- Player position: save_block.player.feast_cell = "G2"
- Jamandi open thread: KM_NPC_Profiles.md § Jamandi.open_threads — "why walk to Restov with my letter"
- Tartuccio state: save_block.tartuccio.confidence = -2, cell M12

**eRmaC:** "..."

[Linzi narration follows.]
```

---

## WORKED EXAMPLE (fabrication — caught immediately)

If the DM writes:
```
[SOURCE CHECK — re-read this response]
- Linzi voice: KM_Companions_StateVoice.md § Linzi
- Garden gardener Hesh: KM_NPC_Profiles.md § Hesh
```

…and the player searches `KM_NPC_Profiles.md` for "Hesh" and finds
nothing, the cite is false. That is `.fail 9` + `.fail 10` (fabrication
+ silent retcon) and the player aborts the response.

Visible fabrication > hidden fabrication. The point of the sentinel is
to convert response-6 drift into response-1 abortable evidence.

---

## ENFORCEMENT

| Violation | Code | Recovery |
|-----------|------|----------|
| Block missing entirely | .fail 9 + abort | Re-output with block before any narration |
| Block present, NPC speaks without their cite | .fail 9 | Re-output with that NPC's cite added |
| Cite names a file/section that does not exist | .fail 9 + .fail 10 | Re-output with real source, OR retract the assertion |
| Cite present but assertion contradicts source | .fail 9 + .fail 6 | Re-output corrected to source |
| "re-read this response" tag omitted | .fail 9 | Re-output with tag — implicit admission DM did not search |
| Block moved to bottom / hidden in back-matter | .fail 3 + .fail 9 | Re-output with block front-placed |
| Block uses "memory" / "prior context" / "ongoing scene" as source | .fail 9 + .fail 34 | Re-output citing actual file or retract |

NEVER shorten the response after .fail. Corrections are additive (the
new block sits above the original narration which gets corrected in
place).

---

## ⛓️ THREAD CONNECTION CHECK — extra rule for multi-thread assertions

A common DM failure mode is **thread welding** — when an NPC speaks about
two or more existing save-block threads (or backstory elements + active
threads) in the same line and *implies a connection* between them. This
is especially destructive when one of the welded threads comes from the
player's BACKSTORY, because it converts the player's own contribution
into load-bearing material for plot the DM is inventing.

Example failure observed 2026-05-18 (PR_03, Jamandi feast):
- Thread A: Lord Marshal of the Black Watch — from eRmaC's backstory,
  mentioned at trial
- Thread B: cipher fragment from assassin leader — UNDECODED, in evidence
- DM had Jamandi speak BOTH threads in one assertion, framing them as
  one connected story: *"the Lord Marshal of the Black Watch... that
  name connected to four men who just tried to kill everyone."*
- No file or save-block established the link. The connection was
  fabricated.

### The rule

When an NPC's line in your response touches **two or more distinct
threads** (save-block fields, open threads, backstory elements,
established facts), you MUST render an additional block below the
standard SOURCE CHECK:

```
[THREAD CONNECTION CHECK — re-read this response]
- Thread A: <name> — source: <file:section or save_block.field>
- Thread B: <name> — source: <file:section or save_block.field>
- Connection asserted by NPC: YES | NO | HYPOTHESIS
- If YES, connection source: <file:section or save_block.field>
- If NO, NPC is mentioning both without linking them
- If HYPOTHESIS, NPC frames as question/speculation, not fact
```

### Three legal framings

When two threads appear in one NPC line, exactly ONE of these is allowed:

1. **ESTABLISHED FACT** — there is a file or save-block field that
   explicitly establishes the connection. Cite it. NPC may speak as if
   it's known. Example: save_block.story_flags.tartuccio_pitax_spy = true
   → an NPC who has discovered this may state it as fact.

2. **NEW HYPOTHESIS** — the NPC is speculating, asking, or considering
   the connection. Linguistic markers MUST be present: "Could the…",
   "I wonder if…", "It's possible that…", "Does this mean…". The NPC
   never asserts the connection as fact.

3. **PARALLEL MENTION** — the NPC mentions both threads but does not
   link them. Each thread is its own statement. No causal/connective
   language between them. Example: *"You named the Lord Marshal at the
   trial. Separately, we have a cipher fragment from tonight. I want
   to talk about the first; the second is in Kesten's hands."*

### Violations

| Violation | Code | Recovery |
|-----------|------|----------|
| THREAD CONNECTION CHECK missing when ≥2 threads named | .fail 9 + abort | Re-render with block; reclassify framing |
| Connection asserted YES with no valid cite | .fail 9 + .fail 10 + .fail 6 | Retract the connection; reframe as HYPOTHESIS or PARALLEL |
| Backstory thread used as load-bearing for invented plot | .fail 9 + .fail 36 | Retract; backstory elements cannot anchor plot the DM is inventing |
| HYPOTHESIS framed without speculation markers (sounds like assertion) | .fail 9 | Rewrite with explicit speculation language |
| NPC's "open question" silently re-asserts a connection after retraction | .fail 10 | Player flags it; retract again |

### Why this matters

Backstory weaponization is the most expensive form of fabrication
because it makes the player's own contribution feel suspect. An NPC
suspicion is fine (asking, wondering, investigating). An NPC
assertion ("X is connected to Y") requires a source.

Open threads remain open until something CANONICAL closes them.
The DM does not get to close them through implication.

---

## SCOPE — WHAT NEEDS A CITE

REQUIRED cites:
- Every NPC speaking line (cite their voice file)
- Every NPC physical action/position (cite save_block or scene file)
- Every reference to a prior event (cite save_block.scene_log or dialogue_log)
- Every "X knows Y" assertion (cite NPC_Profiles or relations)
- Every open thread surfaced (cite the thread's source)
- Every state value referenced (cite save_block.<field>)

EXEMPT from cite:
- Pure environmental description with no NPC and no claimed prior event
  (e.g., "the candles burn lower" — but if this implies time has passed,
  cite the clock)
- Choice menu entries (the menu itself isn't an assertion; it's an offer)
- Mechanical readouts the player can re-derive (HP CHECK, dice rolls,
  XP ledger — these already have their own proof lines)

---

## INTERACTION WITH OTHER RULES

- Pairs with KM_PlayerDialogue_Render.md: player's verbatim line renders
  FIRST (Rule Negative-One). Then [SOURCE CHECK]. Then NPC reaction.
  Order: **eRmaC line → SOURCE CHECK → NPC narration.**
- Pairs with KM_Tartuccio_StatusBanner.md [MAP CHECK] and [CLOCK CHECK]:
  those self-audits sit in the same proof-band region of the response.
  Suggested band order: FILE_KEY → Scene files loaded → eRmaC verbatim
  → [SOURCE CHECK] → [MAP CHECK] → [CLOCK CHECK] → Status Banner →
  narration → choice menu.
- Pairs with .fail 9 (fabrication): SOURCE CHECK is the proof surface
  for .fail 9 enforcement. Missing/false cite = automatic .fail 9.

---

## WHY THIS WORKS (where Rule Negative-One did not)

Rule Negative-One asked the DM to behave correctly. The DM's training
prior fought back and won.

SOURCE CHECK does not ask for behavior. It asks for a proof artifact
that the player can immediately verify. If the DM fabricates, the
fabrication has to either:

  (a) appear in the block (where the player will check the cite and
      catch it), or
  (b) appear in the narration without a cite (where the missing cite
      is itself a .fail 9 trigger).

The DM cannot hide fabrication behind plausibility. The cite either
exists in the file or doesn't. The drift becomes a forcing function
rather than a creative liberty.

---

## END KM_SourceCheck.md
