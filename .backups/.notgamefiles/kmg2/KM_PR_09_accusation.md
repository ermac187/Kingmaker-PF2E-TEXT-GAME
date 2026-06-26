# KM_PR_09_accusation.md — Prologue Beat 09: THE ACCUSATION
## Atomic scene file | ~13 KB (six-proof exit + full accusation) | State: PR_09_ACCUSATION
## FILE_KEY: KMPR09:accusation-exit
## RULE_QUOTE: Six proofs on Prologue exit: XP audit + XP total + state final + save block (v1.7 exhaustive, 48 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.

---

> ⛔ DO NOT (1) skip any of the three rebuttals — run each in order; DCs come from save block flags
> ⛔ DO NOT (2) kill or detain Tartuccio — UNKILLABLE PROTOCOL active until he departs under his own power
> ⛔ DO NOT (3) skip the Malak gate scene if `malak_arrested = FALSE`
> ⛔ DO NOT (4) output the JSON Export without all six proofs delivered in the same response
> ⛔ DO NOT (5) auto-advance past `.continue` — player types it, then Chapter 1 begins
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load + audit-rigor prime)

Line 1: `[FILE_KEY: KMPR09:accusation-exit]`
Line 2: `[RULE_QUOTE: Six proofs on Prologue exit: XP audit + XP total + state final + save block (v1.7 exhaustive, 48 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.]`

Missing or wrong FILE_KEY = `.fail 9`. Missing or paraphrased RULE_QUOTE = `.fail 9`. VERBATIM ONLY — no compression, no rewording. Both keys exist only in this file's header.

---

## STATE IO

**READS:**
- `tartuccio_ring`, `tartuccio_gold`, `knowledge_world_dc9_passed` (from PR_05 / PR_06 / PR_02)
- `artoria_guards_saved`, `alignment_lawful_score`, `alignment_chaotic_score`
- `malak_arrested`, `malak_bribe_evidence`, `parchment_source`
- `companions_selected`, `companion_committed{}`
- `five_seekers_freed_by_player` / `five_seekers_freed_by_jamandi` / `five_seekers_released_late`

**WRITES:**
- `rebuttal_result` = `strong` (2–3 successes) / `weak` (0–1 successes)
- `malak_departure` = choice-dependent flag value
- `biggs_delivers_evidence = TRUE` (if applicable)
- `malak_inquiry_pending = TRUE` (if applicable)
- `prologue_complete = TRUE`
- `current_scene = "chapter_1_start"` (after `.continue`)

**EXIT TRIGGER → Chapter 1:**
- All six proofs delivered in one response
- Player types `.continue`
- Load `KM_Ch1.md` (Chapter 1)

---

## ⛔ ON PROLOGUE EXIT: ALL SIX PROOFS IN ONE RESPONSE

```
═══════════════════════════════════════════════════════════
PROLOGUE EXIT — six proofs required
═══════════════════════════════════════════════════════════
```

### PROOF 1 — XP AUDIT

```
[PROOF 1 — XP AUDIT]
Prologue XP conditions:
  First assassin solo (+30):                     NO/YES — <reason>
  Corridor: assassin + bowman (+60):             NO/YES — <reason>
  Library: 2 assassins (+60):                    NO/YES — <reason>
  Final battle: Leader + Giant + Channelers (+240): NO/YES — <reason>
  Rebuttal success 2–3 of 3 (+125):              NO/YES — <reason>
  Secret Room found (+75):                       NO/YES — <reason>
  Secret Room Puzzle 1 (+30):                    NO/YES — <reason>
  Secret Room Puzzle 2 (+30):                    NO/YES — <reason>
  Pre-Prologue XP carry-forward:                 +<N> (from save block)
```

### PROOF 2 — XP TOTAL BLOCK

```
[PROOF 2 — XP TOTAL]
🎯 XP AWARD — Prologue Complete
<list every YES condition with its XP value>
─────────────────────────────────────────────
Pre-Prologue XP (carry-forward):  +<N>
Prologue XP this run:             +<N>
─────────────────────────────────────────────
Running total:   <N> / 1000 (Level 2 threshold)
```

### PROOF 3 — STATE FINAL VALUES

```
[PROOF 3 — STATE FINAL]
  tartuccio_ring:          <equipped/carried/refused>
  tartuccio_gold:          <taken/left>
  knowledge_world_dc9:     <passed/failed>
  rebuttal_result:         <strong/weak>
  artoria_guards_saved:    <TRUE/FALSE>
  alignment_track:         Lawful <N> / Chaotic <N> → <Artoria/Tatsumaki> stays with player
  companions_with_player:  [list all committed companions by name]
  malak_departure:         <flag value or "N/A — malak arrested">
  prologue_complete:       TRUE
```

### PROOF 4 — SAVE BLOCK

```
[PROOF 4 — SAVE BLOCK]
"Prologue complete. Copy the block below and save it.
 Type `.continue` to begin Chapter 1."
```

Then the full JSON Export Block per `KM_Prologue_Export.md` + `KM_SaveBlock_Template.md` v1.7 EXHAUSTIVE MODE:
- All 48 root keys | No "..." or "etc." in log entries | Every field present (empty OK: `""`, `0`, `[]`, `{}`, `false`)
- ≥ 350 lines / 12 KB minimum
- Required logs: prologue_state, scene_log, dice_log, dialogue_log_by_npc, decision_log, loot_log, hp_ledger, xp_ledger, companion_committed{}, fail_log
- v89 fields: tutorial_pickpocket_resolved, companion_leveling_mode
- v92 field: `current_scene = "chapter_1_start"` (set after `.continue`)

### PROOF 5 — WAIT-FOR-CONTINUE LOCK

```
[PROOF 5 — WAIT-FOR-CONTINUE]
DM does NOT generate any Chapter 1 content this response. Response ENDS
after the save block + the .continue prompt. No road, no Oleg's Post, no
Stolen Lands travel. Auto-advancing past save = .fail 16 + .fail 35.
```

### PROOF 6 — NEXT-SCENE FILE LOAD DECLARATION

```
[PROOF 6 — NEXT-SCENE FILE LOAD]
On `.continue`, the DM will load:
  KM_Ch1.md                          (Chapter 1 start)
  KM_DMRules.md                      (always active)
  KM_NPC_Profiles.md                 (carry forward)
  KM_Companions.md + _B + _C + _D   (all committed companions)
  [companion backstory files for each committed companion]
```

---

## PHASE 5 — THE ACCUSATION

> *Jamandi stands at the center of the ruined table. She is still bleeding slightly but upright. She looks at you — and then at Tartuccio, who has arranged himself beside her with the careful positioning of someone who has been waiting for this moment.*

**Jamandi:** *"You all survived. More than I expected, honestly. The question now is what I do with you."*

> *Tartuccio steps forward.*

**Tartuccio:** *"Before you decide, Lady Aldori — I think we should discuss something. Our new 'hero' here arrived with rather unusual motivation. In fact, I believe they may have been sent here by Irovetti of Pitax — as a spy."*

**Tartuccio:** *"The ring I gave them — Tartuccio's Present — is a tracking device. I gave it to identify Pitaxian agents. And they took it without hesitation."*

---

## REBUTTAL SYSTEM — 3 CHECKS (run in order; track results)

**2–3 successes → `rebuttal_result = strong` → +125 XP**
**0–1 successes → `rebuttal_result = weak` → no bonus XP**
**`malak_bribe_evidence = TRUE` AND `parchment_source = pitax` → Kassil interjects, all rebuttals auto-succeed**

**REBUTTAL 1 — The Ring**

| Condition | Player's option | DC |
|-----------|----------------|-----|
| Ring equipped or carried | Diplomacy — explain innocence | DC 10 |
| Ring refused | Auto-success — *"What ring?"* | DC 0 |
| `knowledge_world_dc9_passed` | Auto-success — *"Tartuccio's accent screams Pitax"* | DC 0 |

**REBUTTAL 2 — The Gold**

| `tartuccio_gold` | DC |
|-------------------|----|
| `taken` | Diplomacy DC 15 |
| `left` | Diplomacy DC 11 |

**REBUTTAL 3 — The Burning Building**

| `artoria_guards_saved` | Tartuccio's framing | DC |
|------------------------|--------------------|----|
| TRUE (Lawful) | *"Performed for the audience"* | Diplomacy DC 12 |
| FALSE (Chaotic) | *"Cold calculation — Pitaxian efficiency"* | Diplomacy DC 14 |

---

## COMPANION SPLIT

**Jamandi:** *"I'm sending two teams into the Stolen Lands. Different routes. Different approaches. [Character name] leads one. Tartuccio leads the other."*

```
ALWAYS WITH PLAYER:
  Linzi (unconditional) | Tika (unconditional) | Artoria | Tatsumaki | Morrigan
  All 6 active chosen companions (Goldmoon, Sucrose, Ryuko, Olivier, Yoko, Kyoko)
  who reached +4 feast approval OR ran their Phase 4.5 scene
  [In practice: all 11 chosen companions are always with the player — close lines proved it]

ALWAYS DEPARTS:
  Kaessi — goes her own way; recruitable Act 2

TARTUCCIO'S TEAM:
  five_seekers_freed_by_player = TRUE  → [seeker_1..5] from save block
  five_seekers_freed_by_jamandi = TRUE → same
  five_seekers_released_late = TRUE    → 2 hired mercenaries instead
```

---

## JAMANDI'S FINAL QUESTION (Good/Evil Axis)

**Jamandi:** *"Last question. Answer it honestly — I'll know if you don't. Why do you want the Stolen Lands?"*

```
GOOD responses: "To give people there a safe place to live." /
                "To build something that lasts beyond any one person." /
                "Because someone has to, and I'd rather it be someone who cares."
EVIL responses: "Power. Real, lasting power. I intend to use it." /
                "Judgment. That land has needed a reckoning for a long time." /
                "Because I take what I can hold, and I intend to hold it."
NEUTRAL:        "For the charter. For the opportunity." /
                "Honestly? I'm not sure yet. But I know I'll figure it out."
Custom action
```

---

## JAMANDI'S GIFTS

**Jamandi:** *"Here. You'll need these more than I will."*
- **Camping Supplies** ×1 | **Rations** ×4 | **Scroll of Raise Dead** (9th-level — do not waste)
- Three-month time limit to defeat the Stag Lord. *"Finish in under 30 days — reward waiting."*
- Destination: **Oleg's Trading Post**, Greenbelt, Stolen Lands.
- *"Kesten Garess will follow once he's secured the manor. He'll meet you at Oleg's."*

---

## TARTUCCIO DEPARTS

Full departure narration → `KM_Prologue_P5.md § Tartuccio Departure`. Check `tartuccio_team` flag.

**Exit line (both variants):**
**Tartuccio:** *"Well. This has been instructive. I look forward to seeing what you build, [character name]. I'll be building something too."* *(smiles — not pleasantly — and leaves)*

**⛔ He cannot be stopped, killed, or detained.** He surfaces in Chapter 1 as "Tartuk" the kobold shaman at the Ancient Tomb.

---

## BIGGS / WEDGE FAREWELL (fires if `malak_arrested = TRUE` before east gate)

If Biggs and Wedge escorted Malak through the feast and are now handing off custody,
they will say their piece before leaving. This is a player turn — not narration to push through.

Biggs delivers his farewell line (DM writes to character — something brief, genuine, earned).
**STOP. Output this menu before Biggs turns to leave:**

```
Biggs is about to go.

 1. Let him go — say nothing.
 2. "Thank you, Biggs." [or any short acknowledgment]
 3. Give Biggs a final instruction about Malak.
 4. Ask where they're taking him.
 5. Shake his hand / clap his shoulder.
 6. Say something to Wedge.
 7. Custom — say or do something before they leave.
```

After player responds: Biggs nods (or responds briefly), then he and Wedge leave with Malak.
**STOP again.** The player watches them go — do NOT narrate the player moving or the scene
transitioning until the player acts next.

---

## MALAK — THE EAST GATE (run only if `malak_arrested = FALSE`)

**Skip entirely if:** `malak_fled = TRUE` and `malak_caught = FALSE` | OR `malak_in_player_custody = TRUE`

> *East gate of Restov. Early dawn. Malak is back at his post — of course he is.*
> **Malak** *(working hard to sound official)*: *"Leaving Restov, then. Safe travels."*

**STOP. Output this menu — player has not yet walked through the gate:**

```
 1. Walk past without a word        [malak_departure = "silent_walk"]
 2. Stop, say nothing — wait for him to speak first [malak_departure = "stare_down"]
 3. [malak_bribe_evidence] Show parchment to Biggs [malak_departure = "evidence_shown"
                            | biggs_knows_fully = TRUE]
 4. [Intimidation DC 12] "Enjoy the post, Captain. While you still have it."
    → Success: composure cracks [malak_departure = "threat_landed"]
    → Failure: straightens, but voice isn't steady [malak_departure = "threat_failed"]
 5. [Diplomacy DC 14] Order him to open the gate personally and hold it
    → Success: he does it, hands shaking — Tika / Artoria / Linzi scripted reactions
    [malak_departure = "gate_ordered"]
 6. Tell him to report to Kesten Garess today for a formal inquiry
    → BIGGS: "He'll be there." [malak_departure = "inquiry_ordered"
    | malak_inquiry_pending = TRUE]
 7. [malak_bribe_evidence] Hand parchment to Biggs to deliver to Kesten
    → BIGGS takes it. MALAK goes very still.
    [malak_departure = "evidence_delivered" | biggs_delivers_evidence = TRUE]
 8. Say nothing to Malak. Walk through without breaking stride.
```

After player acts: the gate opens. **STOP.** Player has not yet left Restov. Do NOT
write "Restov is behind you" or narrate movement south. Wait for player to act.

---

## DEPARTURE NARRATION

> *Dawn is coming. You can see it through the broken windows — gray light over Restov's rooftops.*
>
> *Your party stands in the ruined banquet hall of Jamandi Aldori's manor, charter in hand, companions at your side, a map to Oleg's Trading Post folded in your pack.*
>
> *The Stolen Lands are three days' travel south. Everything you built tonight — every alliance, every enemy made, every choice in the dark — comes with you.*

**STOP. Do NOT write "Load your packs. The road south begins now." or any line that
moves the player. Output this menu:**

```
 1. Leave now — head for the south gate.
 2. Take a moment before you go. [say something, look around, composure]
 3. Speak to one of your companions before departing.
 4. Check your gear / inventory before the road.
 5. Ask Jamandi one last thing before you leave.
 6. Custom action.
```

---

## PROLOGUE XP TABLE

| Source | XP |
|--------|----|
| First assassin (solo) | 30 |
| Corridor (assassin + bowman) | 60 |
| Library (2 assassins) | 60 |
| Final battle (Leader + Giant + Channelers) | 240 |
| Rebuttal success (2–3 of 3) | 125 |
| Secret Room found | 75 |
| Secret Room Puzzle 1 | 30 |
| Secret Room Puzzle 2 | 30 |
| **Total (full completion)** | **~650 XP** |
| **Minimum (no secrets, failed rebuttals)** | **~390 XP** |

Level 2 threshold: 1000 XP. Track running total including Pre-Prologue carry.

---

*KM_PR_09_accusation.md — Prologue atomic beat 09 | v92.0*
