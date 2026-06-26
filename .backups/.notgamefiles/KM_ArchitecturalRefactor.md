# KINGMAKER — ARCHITECTURAL REFACTOR PLAN
## KM_ArchitecturalRefactor.md | Updated v93.6 | 2026-05-09
## **READ THIS FIRST IF YOU ARE A NEW CHAT PICKING UP THIS PROJECT**

---

## 🎯 CURRENT STATUS — 2026-05-09 (v93.6)

**Phase 1**: ✓ SHIPPED 2026-05-08 (atomic Pre-Prologue, 9 KM_PP_NN_*.md files)
**Phase 5**: ✓ SHIPPED 2026-05-08 (atomic Prologue, 9 KM_PR_NN_*.md files + KM_PR_BRANCH_WALKOUT.md)
**Phase 2**: ⏳ PARTIAL — load mappings in KM_SceneFiles.md functional; full state-graph wiring needs playtest data
**Phase 3**: ⏳ PARTIAL — `[STATE READ]` / `[STATE WRITE]` formats specified; SaveBlock_Template integration pending
**Phase 4**: ⏳ BLOCKED ON PLAYTEST — atomic files still carry full sentinels; collapse only when playtest confirms reliability

**We are now testing the refactor against runtime behavior** — that is, validating
that the atomic file architecture + ULTRA-PRIORITY rules + save-offer breakpoints
actually fix the failure modes the original v90 ceiling identified. The refactor is
not "complete" until playtest confirms the DM stops the cascade-abandonment pattern.

---

## 🔍 WHAT WE'RE TESTING

The 2026-05-09 session added structural fixes targeting persistent runtime
failures the atomic-file refactor alone did not solve. Playtest must verify:

1. **No-fabrication compliance.** Does the DM stop inventing NPCs (Aldric, Tomas,
   etc.) at the manor entry hall now that PR_01 v93.5 explicitly forbids any NPC
   in that location AND PP_09 resolves Malak custody before arrival?
2. **No-veto compliance.** Does the DM execute violent/dark player actions instead
   of refusing to narrate them? KM_B.txt EXECUTE PLAYER ACTIONS rule is the test.
3. **No-fabrication-maps compliance.** Does the DM stop drawing tactical grids for
   non-combat city walks? KM_Commands.md updated.
4. **Route choice + named pauses fire correctly.** PP_09 has route choice
   (direct/scenic/jail/jail+scenic) and three named pauses. Does the DM surface
   them?
5. **Pre-arrival custody decision fires correctly.** PP_09 now contains the
   pre-arrival Malak disposition menu, replacing PR_01's deleted entry-hall menu.
6. **Save offers fire at break points.** Four save offers added: PP_04, PR_02,
   PR_06, PR_08. Does the DM honor them?
7. **Path 4 (subordinate revision) is reachable.** Biggs-as-Malak's-subordinate
   path to free the seekers without parchment requirement.
8. **Walkout branch fires.** When the player leaves the manor, does the cascade
   (paralytic → assassins → fire-as-public-narrative-cover) fire correctly per
   KM_PR_BRANCH_WALKOUT.md?
9. **Player level-up fires in MANUAL mode.** Does the DM present the full menu
   in the same response as the threshold cross, or does it skip with "available"?
10. **Input fidelity.** Does the DM render every player action beat and dialogue
    line as written, without compression or sanitization?

---

## 📋 REFACTOR PHASES — STATUS DETAIL

### PHASE 1 — ATOMIC SCENE FILES (Pre-Prologue)  ✓ SHIPPED 2026-05-08

9 KM_PP_NN_*.md files exist. Load mappings in KM_SceneFiles.md.
Old monolithic Pre-Prologue files DELETED 2026-05-08 v93.1.

PP_09 expanded 2026-05-09 with route choice + three named pauses + pre-arrival
custody decision (replacing the deleted PR_01 entry-hall custody menu).

### PHASE 2 — STATE MACHINE  ⏳ PARTIAL

`current_scene` → file mapping is functional. Named states like `PP_GATE_APPROACH`,
`PR_01_arrival`, `outside_manor` are used in scene files. Full state-graph wiring
with explicit transition commands and trigger conditions documented per state is
PARTIAL — most transitions are still implicit or scene-file-internal.

### PHASE 3 — STATE EXTERNALIZATION  ⏳ PARTIAL

`[STATE READ]` and `[STATE WRITE]` formats appear in atomic files. SaveBlock_Template
schema update for v93.6 fields (walkout-branch flags, save_label values, custody
flags) is pending.

### PHASE 4 — SLIM PER-RESPONSE SENTINELS  ⏳ BLOCKED

Atomic files still carry FILE_KEY + STATE READ + HP CHECK + Scene-files-loaded
proof lines. Collapsing to a slimmer sentinel set requires playtest confidence
that the heavier set isn't preventing failures. Don't slim before playtest.

### PHASE 5 — PROLOGUE ATOMIC  ✓ SHIPPED 2026-05-08

9 KM_PR_NN_*.md files + KM_PR_BRANCH_WALKOUT.md (added 2026-05-09).
Old monolithic Prologue files DELETED 2026-05-08 v93.1.

PR_01 rewritten 2026-05-09 v93.5 to remove the entry-hall attractor (DELETED
STOP 2 entirely; entry hall is now a transitional sentence with no NPC).

---

## 🛠 v93.6 STRUCTURAL ADDITIONS (2026-05-09)

These are NEW since v93.0/v93.1 baseline. Files affected:

- **KM_B.txt** — added two ULTRA-PRIORITY rules: EXECUTE PLAYER ACTIONS (no veto),
  THE DATA IS ROBUST (no fabrication). 32,686 b (82 b under hard limit; do not
  append).
- **KM_Commands.md** — added DO NOT FABRICATE MAPS clause. ~21 KB.
- **KM_Leveling.md** — clarified MANUAL mode (level-up menu fires in same response
  as threshold cross). 8,242 b.
- **KM_PR_01_manor_arrival.md** — REWRITTEN to 2-stop architecture; STOP 2 entry-
  hall menu DELETED to defeat the entry-hall NPC fabrication attractor. ~12.6 KB.
- **KM_PR_02_feast_opening.md** — added save offer before carousel. ~7.3 KB.
- **KM_PR_06_manor_sweep.md** — added save offer before final battle. ~11.1 KB.
- **KM_PR_08_the_calm.md** — added save offer before accusation. ~9 KB.
- **KM_PP_04_tutorial_outcome.md** — added save offer before Malak gate. ~10.3 KB.
- **KM_PP_09_restov_walk.md** — added route choice (4 routes including jail
  rescue) + three named pauses (Lower Well, Iron Hare, Erastil Wayshrine) +
  pre-arrival custody decision. ~21.9 KB.
- **KM_Malak_Jail.md** — added Path 4 SUBORDINATE REVISION (Biggs-as-subordinate
  path to free seekers without parchment requirement). ~27.3 KB.
- **KM_PR_BRANCH_WALKOUT.md** — NEW FILE. Documents the walkout cascade:
  paralytic → assassins-finishing-paralysed-guests → fire-as-public-narrative-cover.
  Three-stage operation, Kassil's combat-extraction rescue mechanic, Jamandi exit,
  post-fire confrontation, Kassil morning meeting alternative. ~26.3 KB.
- **KM_SceneFiles.md** — added walkout branch trigger conditions and lookup. ~19 KB.

---

## 🚨 WHAT NOT TO DO

- **Do not add more rules without trimming first.** KM_B.txt is 82 bytes under
  the hard limit. Adding requires trimming.
- **Do not add gates to atomic files past their content needs.** Each atomic file
  should run its beat and exit. Gates that exist for global enforcement belong in
  KM_B.txt or KM_Commands.md.
- **Do not respond to a new failure mode with a new fail code.** Use paste-backs
  from KM_QuickFails.md or extend an ULTRA-PRIORITY rule.
- **Do not "fix" by paraphrasing existing rules in new locations.** Duplication
  causes drift. The Aldric Cascade was downstream of an under-specified anonymous
  guard role; we fixed it by adding constraints to PR_01, not by duplicating the
  no-fabrication rule in five places.
- **Do not skip playtest gates.** Phase 4 collapse, save-block schema updates,
  and any further atomic-file restructuring require playtest data first.

---

## 🛠 SUGGESTED SESSION ORDER FOR NEXT CHAT

1. **Verify the current state.** Read this file. Read KM_SessionBootstrap.txt.
   Read KM_SessionHandoff.txt. Confirm v93.6 file sizes match.
2. **Identify what's being tested.** The session is a refactor test. Read
   "WHAT WE'RE TESTING" section above and decide which validation is the focus.
3. **Run the test.** Upload C:/KMG/. Open a fresh DM chat. Use SETUP CONTRACT.
   Play through the relevant beat(s). Document each rule honored or violated.
4. **Patch, do not pile.** If a failure occurs, prefer extending an existing
   ULTRA-PRIORITY rule over writing a new fail code or new file. KM_B.txt is
   tight; trim before extending.
5. **Update this file.** When a phase advances, update CURRENT STATUS and the
   v93.6 STRUCTURAL ADDITIONS section.

---

## 📌 ALTERNATIVE — NO REFACTOR, ACCEPT THE CEILING

Same as v90.0 alternative: stop adding rules, use KM_QuickFails.md, reload from
save block when DM cascade-abandons, plan for 1-in-5 reload rate.

The refactor work to date has reduced this rate but not eliminated it. The
2026-05-09 session demonstrated that even with atomic files + 4 ULTRA-PRIORITY
rules + entry-hall attractor removal, runtime behavior still fails to honor
the file system in edge cases. Whether further refactor work fixes this or
whether we're permanently in "1-in-N reload" territory is the open question
that v93.6 playtest is meant to answer.

---

## 🔗 RELATED MEMORY

User's auto-memory at `C:\Users\ermac\.claude\projects\C--KMG\memory\`:
- `feedback_dm_behavior.md` — long-running pattern
- `feedback_dm_gaslighting.md` — v90.0 cascade incident
- `feedback_dm_debrief_fabrication.md` — DM invents atmospheric NPCs
- `feedback_dm_forward_quote.md` — DM predicts player input
- `feedback_workarounds.md` — known things that work
- `feedback_save_block_exhaustive.md` — exhaustive save mode

Consult these before re-explaining context.

---

*KM_ArchitecturalRefactor.md — Updated 2026-05-09 | v93.6*
*Active refactor: Phase 1 + Phase 5 shipped; testing structural patches.*
