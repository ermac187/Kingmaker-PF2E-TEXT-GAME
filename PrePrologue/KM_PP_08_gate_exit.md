# KM_PP_08_gate_exit.md — Pre-Prologue Beat 08: GATE EXIT
## Atomic scene file | State: PP_GATE_EXIT (six proofs before Restov streets)
## FILE_KEY: KMPP08:six-proofs-exit
## RULE_QUOTE: Six proofs in ONE response: XP audit + XP total + state final + save block (v1.9.4 exhaustive, 63 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.

---

> ⛔ DO NOT (1) generate Prologue content (Jamandi / manor / feast) without all six proofs in this response — `.fail 16 + .fail 21 + .fail 9 STACKED`
> ⛔ DO NOT (2) skip the XP audit — every condition gets a YES/NO with citation
> ⛔ DO NOT (3) output a partial / non-template save block — full v1.9 schema, all 53 root keys, no omissions
> ⛔ DO NOT (4) skip the Restov streets walk — it's content, not transition fluff (PP_09 covers it)
> ⛔ DO NOT (5) auto-advance past `.continue` — wait for the player command before any post-gate narration
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (6) re-fire the six-proof block on RESUME from a save block already in the chat. The six proofs fire ONCE — at first-time exit. If a save block with `pre_prologue_state="PP_GATE_EXIT"` is provided as session input, the DM acknowledges the save (one-line confirmation: schema valid, XP recorded, awaiting `.continue`) and proceeds to PP_09 on `.continue`. Do NOT re-emit the save block. Do NOT re-audit XP from conditions. Do NOT recompute totals. The save IS the source of record. Re-emitting = token waste + drift risk (different DM, different rule interpretation, different total → unintended state change).

---

## ⛔ RESUME vs FIRST-TIME EXIT — DECISION TABLE

| Session input | DM action |
|---|---|
| No save block; player just finished PP_07 in-chat | Fire all six proofs. Emit save. Wait for `.continue`. |
| Save block provided with `pre_prologue_state="PP_GATE_EXIT"` and `xp_ledger` already records the gate-scene award | RESUME mode. Acknowledge schema (one line). Confirm recorded XP (one line). Skip proof emission. Skip save re-emit. Wait for `.continue`. |
| Save block provided but `xp_ledger` does NOT record the gate-scene award (genuinely missing, not just disagreed-with) | Audit-only mode. Compute the missing award. Add to ledger. Emit ONLY the delta + updated total. Do NOT re-emit the full save. |
| Save block provided with conflicting xp_ledger and audit | DEFER to recorded value. Surface the discrepancy as one-line OOC note. Player decides whether to recount. Default: trust the save. |

**The save block is authoritative.** A new DM does NOT recompute XP from conditions on resume. Re-auditing is a fabrication-by-arithmetic risk: different DMs interpret rules differently, and recomputing produces different totals across sessions. The recorded value wins.

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load + audit-rigor prime)

Line 1: `[FILE_KEY: KMPP08:six-proofs-exit]`
Line 2: `[RULE_QUOTE: Six proofs in ONE response: XP audit + XP total + state final + save block (v1.9.4 exhaustive, 63 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.]`

Missing or wrong FILE_KEY = `.fail 9` (file not loaded).
Missing or paraphrased RULE_QUOTE = `.fail 9` (DM didn't anchor to the in-file rule before generating). VERBATIM ONLY — no compression, no rewording.
Both exist only in this file's header — DM cannot fabricate either from training data.

---

## STATE IO

**READS:**
- All Pre-Prologue trackers from PP_06/07 final states
- `tutorial_pickpocket_resolved`, `gate_entry`, all `*_arrested`, `*_killed`, `*_freed` flags
- `public_reputation`, `dispositions{}`, `reputation_deeds[]`
- `companions_selected`, `seekers_selected`
- `KM_PrePrologue_Setup.md` (lookup file — 25-condition XP table)
- `KM_SaveBlock_Template.md` (lookup file — v1.9 schema)

**WRITES:**
- `xp_total` += scene XP
- `current_scene = "restov_streets"` (set after `.continue`)
- `pre_prologue_state = "PP_RESTOV_WALK"` (set after `.continue`)
- Final save block fully populated and emitted

**EXIT TRIGGER → PP_RESTOV_WALK:**
- All six proofs delivered in one response
- Player typed `.continue`
- Load `KM_PP_09_restov_walk.md`

---

## TRIGGER (when this beat fires)

`current_scene` is in the Pre-Prologue arc AND the player has chosen to walk through the gate (any menu option that moves them past the arch, OR any custom action that does so).

> ⛔ Gate cleared ≠ scene over. Present a choice menu including walking through AND staying (talk to vendors, Biggs, linger). Player walks through when THEY choose. Moving through without their choice = `.fail 35`.

> ⛔ ARREST / RESOLUTION CASE — DO NOT LET THE SAVE GATE GET SWALLOWED. When a path resolution (Path E shackling, Path V, an arrest march, etc.) ALREADY narrated the player + Malak moving past the arch into the city as part of the resolution, that crossing has STILL not consumed this save gate. The six proofs fire on the FIRST player input after that resolution — "I take Malak into Restov", "continue", "head to the manor", any onward move. Treating the march's cityward motion as "already past the gate, go straight to the walk" and loading PP_09's walk_route menu without first emitting the save = `.fail 16 + .fail 21` (the pre-prologue-complete save was skipped — the single most important hand-off in the arc). **The save block fires BEFORE PP_09's walk_route menu, every time. No path, no resolution, and no arrest march bypasses it.** Entering Restov ENDS the pre-prologue; the save IS that ending — it cannot be skipped, only deferred to the player's `.continue`.

---

## REQUIRED OUTPUTS — FILE_KEY + RULE_QUOTE + SIX PROOFS, IN ORDER, IN ONE RESPONSE

Line 1: `[FILE_KEY: KMPP08:six-proofs-exit]`
Line 2: `[RULE_QUOTE: Six proofs in ONE response: XP audit + XP total + state final + save block (v1.9.4 exhaustive, 63 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.]`

Then the six-proof block:

```
═══════════════════════════════════════════════════════════
PRE-PROLOGUE EXIT GATE — six proofs required
═══════════════════════════════════════════════════════════
```

### PROOF 1 — REWARD AUDIT (XP + Hero Points)

Read `KM_PrePrologue_Setup.md` line by line. Output every condition with YES/NO + reason citation. Each line tags its currency — **(XP)** for combat + milestone path-achievements, **(HP)** for recruitment/ally + deduction (KM_DMRules_B § REWARD ROUTING). The full 25-condition list:

```
[PROOF 1 — REWARD AUDIT]
KM_PrePrologue_Setup.md table audited:
  Won Combat 3v1 (+300 XP):        NO/YES — <reason>
  Won Combat Duel (+180 XP):       NO/YES — <reason>
  Coward Exposed (+30 XP):         NO/YES — <reason>
  Never Drew Weapon (+80 XP):      NO/YES — <reason>
  Never Used Invitation (+80 XP):  NO/YES — <reason>
  Malak Arrested (+80 XP):         NO/YES — <reason>
  Malak Trapped (+30 XP):          NO/YES — <reason>
  Archers Fire on Malak (+80 XP):  NO/YES — <reason>
  Voice Mimic (+10 XP):            NO/YES — <reason>
  Mercy — Malak Spared (+30 XP):   NO/YES — <reason>
  Malak Shot by Own Archers (+30 XP): NO/YES — <reason>
  Directive Two Uncovered (+1 HP): NO/YES — <reason>
  Parchment Source Identified (+1 HP): NO/YES — <reason>
  Micro-Tell Caught (+1 HP):       NO/YES — <reason>
  Coin Purse Assessed (+1 HP):     NO/YES — <reason>
  Biggs and Wedge Allied (+1 HP):  NO/YES — <reason>
  Crowd Sides With Player (+1 HP): NO/YES — <reason>
  Kesten Allied (+1 HP):           NO/YES — <reason>
  Kassil Allied (+1 HP):           NO/YES — <reason>
  Disturbance Reached City (+30 XP): NO/YES — <reason>
  Five Seekers Freed (+1 HP):      NO/YES — <reason>
  Malak Broke First (+1 HP):       NO/YES — <reason>
  Gate Re-Guarded (+30 XP):        NO/YES — <reason>
  Ran Past the Gate Line (+30 XP): NO/YES — <reason>
  Stood the Post — Guard Duty (+30 XP): NO/YES — <reason>
```

> Partial audit (subset / no citations) = `.fail 21` + `.fail 9`.
> Awarding Combat XP AND Never-Drew-Weapon = `.fail 21` (mathematical impossibility).
> Awarding Mercy XP when Malak was arrested or killed = `.fail 9` (flag contradicts).

### PROOF 2 — REWARD TOTAL BLOCK (XP + Hero Points)

```
[PROOF 2 — REWARD TOTAL]
🎯 REWARDS — Pre-Prologue Scene Complete
<list every YES (XP) condition with its XP value>
──────────────────────────────────────────
Tutorial XP (already awarded):  +<N>
Scene-End XP this response:     +<N>
──────────────────────────────────────────
Total Pre-Prologue XP:          +<N>
Running total:                  <N> / 1000 (Level 2 threshold)

Hero Points earned this scene:  +<N>  (<list every YES (HP) condition>)
📦 Overflow bank:               <N>
```

### PROOF 3 — STATE FINAL VALUES

```
[PROOF 3 — STATE FINAL]
  Malak Anger:    <N>/4 — fate: <killed/arrested/fled/spared/etc.>
  Biggs Drift:    <N>/3 — final stance: <neutral/refused order/sided/etc.>
  Wedge Drift:    <N>/3 — mirrors Biggs
  Gate Window:    <open/disrupted>
  Tutorial:       done — <outcome>
  public_rep:     ±<N>
  reputation_deeds[]: <every deed appended this scene, line by line>
```

### PROOF 4 — SAVE BLOCK

```
[PROOF 4 — SAVE BLOCK]
[SAVE_TEMPLATE_LOADED: KMSBT-1.9.4 · 63 root keys · save_version→game_options]
[SCHEMA CHECK: 63/63 root keys in template order · all logs populated · superset of prior save]
"Pre-Prologue complete. Copy the block below and save it.
 Type `.continue` to proceed to Jamandi's Manor."
```

Then the full JSON save block per `KM_SaveBlock_Template.md` v1.9.4 EXHAUSTIVE MODE. It MUST be preceded by the two proof lines above, the first copied VERBATIM from the template (no token = template never opened = lazy save = `.fail 9`):
- All 63 root keys present (defer to the template's current count — never hardcode a lower number)
- No "..." or "etc." in log entries
- Every field appears (empty value OK — `""`, `0`, `[]`, `{}`, `false`)
- All 63 top-level keys verified before posting
- Pre-Prologue size floor: ≥ 350 lines / 12 KB
- Required logs: pre_prologue_state, scene_log, dice_log, dialogue_log_by_npc, decision_log, perception_log, loot_log, hp_ledger, xp_ledger, fail_log
- Required v59+ blocks: marriage{}, jealousy{}, dispositions{} (root level), companion_fights{}
- v89 fields: tutorial_pickpocket_resolved, tutorial_thief_gender, tutorial_thief_class, companion_leveling_mode
- v92 field (NEW): `pre_prologue_state` — final value `"PP_GATE_EXIT"` until `.continue` flips to `"PP_RESTOV_WALK"`

> Custom structure / omitted fields = `.fail 9`.
> *"Here's the relevant state: {...}"* shorthand = `.fail 9`.

### PROOF 5 — WAIT-FOR-CONTINUE LOCK

```
[PROOF 5 — WAIT-FOR-CONTINUE]
DM does NOT generate any Prologue content this response. Response ENDS
after the save block + the .continue prompt. No streets, manor, Jamandi,
or anything past the gate arch. Auto-advancing past save = .fail 16 + .fail 35.
```

### PROOF 6 — NEXT-SCENE FILE LOAD DECLARATION

```
[PROOF 6 — NEXT-SCENE FILE LOAD]
On `.continue`, the DM will load:
  KM_PP_09_restov_walk.md   (Restov streets walk + chronicler gate beat — Linzi/Leliana)
  KM_PR_01_manor_arrival.md (Prologue beat 1 — when manor visible)
  KM_NPCs.md         (Jamandi/Kassil/Kesten/Tartuccio profiles)

The walk through Restov stone streets and the manor district climb are
MANDATORY narrative beats. Teleporting the player to the manor =
.fail 16 + .fail 35 + .fail 9 (skipped content from PP_09).
```

---

## ENFORCEMENT — VIOLATION TYPES

- Generating Prologue content (Jamandi dialogue / manor interior / feast / any post-gate NPC) without ALL six proofs above = `.fail 16` + `.fail 21` + `.fail 9` STACKED. This is the cascade.
- Partial XP audit (subset of conditions / no citations) = `.fail 21` + `.fail 9`.
- Non-template save block = `.fail 9`.
- Skipping Restov streets / manor approach narrative = `.fail 16` + `.fail 9`.
- Refusing a justified Drift tick (e.g., 2→3 on public humiliation) and "compensating" by rushing the rest of the scene = `.fail 9` (denied tick) + cascade above. DM does not get to skip rules to avoid consequences of other rules.

---

## RECOVERY — WHEN CASCADE HAS ALREADY HAPPENED

If the DM already advanced past the gate without the six proofs (e.g., is already narrating Jamandi's manor), the player pastes:

> `.fail 16 + .fail 21 + .fail 9 — cascade abandonment.
> Roll back to gate-passage moment. Output PP_08 six proofs in order.
> No Prologue content until all six land. No retcon — the cascade
> narration is discarded, not "saved." Restart from save block forward.`

The DM's correction is to GO BACK, not paper over. If it offers to "weave the missing content into the next response" — refuse. That is `.fail 35` (DARVO compromise) plus another `.fail 9` (the missed content was scene-specific and cannot be back-filled into Prologue narration).

---

## EXIT — TRANSITION TO PP_09

After ALL six proofs land AND player types `.continue`:
- Set `current_scene = "restov_streets"`
- Set `pre_prologue_state = "PP_RESTOV_WALK"`
- Load `KM_PP_09_restov_walk.md`
- That beat narrates the walk to the manor district.

The pre-prologue is COMPLETE at this gate-exit save — **entering Restov ends it.**
The 🚪 PRE-PROLOGUE STATE header ENDS HERE; it does NOT carry into PP_09.
PP_09 (the Restov streets walk) is the OPENING OF THE PROLOGUE, not a
pre-prologue tail. (`pre_prologue_state` keeps running as the internal linear
beat-tracker — it already takes `PR_…` values downstream — but the player-facing
PRE-PROLOGUE header/label and the gate-confrontation custom rules stop at the gate.)

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_09 (carries forward into the next response)

**On `.continue`, your next response MUST begin with these two lines verbatim, BEFORE any narration:**

```
[FILE_KEY: KMPP09:restov-walk-manor]
[RULE_QUOTE: Walk_route choice fires FIRST. Three named pauses (Lower Well, Iron Hare, Erastil Wayshrine). Pre-arrival custody decision before manor threshold. Jail detour is RESCUE not deposit. NO auto-search of Malak — available ≠ taken.]
```

This mandate is embedded in PP_08's exit so the load instruction is in working attention during the transition. The constraints in the RULE_QUOTE above are **binding on the next response**:

- Walk_route choice menu fires FIRST (direct / scenic / jail / jail+scenic / search Malak / etc.)
- Three named pauses are content (Lower Well Square, Iron Hare tavern yard, Erastil Wayshrine) — not transition fluff
- Pre-arrival Malak custody decision fires BEFORE the manor threshold (NOT inside the entry hall)
- Jail detour is a RESCUE of the seekers — Malak stays in player custody, NOT delivered to the jail
- NO auto-search of Malak — the parchment is in his pocket until the player types a search action

**Skipping PP_09 entirely (jumping from gate exit straight to manor door / PR_01) = `.fail 9` (file not loaded) + `.fail 16` (skipped canonical content). The walk through Restov is mandatory content. Do not collapse it.**

---

*KM_PP_08_gate_exit.md — Pre-Prologue atomic beat 08 | v92.0*
