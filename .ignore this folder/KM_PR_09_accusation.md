# KM_PR_09_accusation.md — Prologue Beat 09: THE ACCUSATION
## Atomic scene file | ~13 KB (six-proof exit + full accusation) | State: PR_09_ACCUSATION
## FILE_KEY: KMPR09:accusation-exit
## RULE_QUOTE: Six proofs on Prologue exit: XP audit + XP total + state final + save block (v1.9.4 exhaustive, 63 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.

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
Line 2: `[RULE_QUOTE: Six proofs on Prologue exit: XP audit + XP total + state final + save block (v1.9.4 exhaustive, 63 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.]`

Missing or wrong FILE_KEY = `.fail 9`. Missing or paraphrased RULE_QUOTE = `.fail 9`. VERBATIM ONLY — no compression, no rewording. Both keys exist only in this file's header.

---

## STATE IO

**READS:**
- `tartuccio_ring`, `tartuccio_gold`, `knowledge_world_dc9_passed` (from PR_05 / PR_06 / PR_02)
- `hutao_guards_saved`, `alignment_lawful_score`, `alignment_chaotic_score`
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
  Recruitment — All Companions (+75):            NO/YES — <reason>
  Recruitment — All Seekers (+100):              NO/YES — <reason>
  Recruitment — All Planted (4/4 manor) (+125):  NO/YES — <reason>
  Recruitment — GRAND SLAM / everyone (+150):    NO/YES — <reason>
  Mass Declaration bonus (mass_declaration_xp):  +<N> — <best single-beat count>
  Pre-Prologue XP carry-forward:                 +<N> (from save block)
```
(Recruitment-completion lines per § RECRUITMENT COMPLETION; they stack.)

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
  hutao_guards_saved:       <TRUE/FALSE>
  alignment_track:         Lawful <N> / Chaotic <N> → (alignment record only; all Active 5 remain with player regardless)
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

Then the full JSON Export Block per `KM_Prologue_Systems.md` + `KM_SaveBlock_Template.md` v1.9 EXHAUSTIVE MODE:
- All 53 root keys | No "..." or "etc." in log entries | Every field present (empty OK: `""`, `0`, `[]`, `{}`, `false`)
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
  KM_NPCs.md                 (carry forward)
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

## ⛔ EVIDENCE-DRIVEN ACCUSATION — TARTUCCIO DEPLOYS WHAT HE GATHERED

Before (and alongside) the 3 canon rebuttals, Tartuccio leads with the PERSONALIZED case he
built at the feast carousel — `story_flags.tartuccio_evidence[]`, highest-ranked first (see
KM_Prologue_Systems.md § TARTUCCIO EVIDENCE ENGINE). He quotes the REAL words eRmaC or a
companion actually said. ⛔ ANTI-FABRICATION: he may cite ONLY items present in the ledger,
quoted as recorded; he invents no quotes, manufactures no admissions, and an angle he never
gathered DOES NOT APPEAR in his mouth. Citing content not in `tartuccio_evidence[]` = `.fail 9`.

**Case strength scales with the ledger** (this MODIFIES the 3-check spine below; it does not
replace it):
- **STRONG ledger** (≥2 items at rank ≥4): a formidable, specific accusation. Each rank-≥4
  item becomes an EXTRA **Evidence Rebuttal** check (Diplomacy DC 13–14, the player answering
  the actual quote), run after the canon 3. Jamandi leans toward Tartuccio at the open.
  `rebuttal_result = strong` now requires succeeding on the MAJORITY of (3 + N) total checks.
- **MODERATE ledger** (only rank 2–3 items): he cites them as corroborating color that RAISES
  the matching canon rebuttal DC by +2 (origin/identity item → the Ring/spy check; loyalty
  item → the Gold check; conduct item → the Burning Building check). No extra checks.
- **EMPTY / WEAK ledger** (no items, or high `tartuccio_evidence_pressure` — the player
  starved him at the carousel): he has nothing personal and leans on the generic ring claim
  alone, visibly grasping. Player gets **+2 circumstance to ALL rebuttals**, and Jamandi is
  skeptical of HIM from the open (his feast-night desperation was noticed). Starving the
  engine is rewarded here.

Fold every Evidence-Rebuttal result into `rebuttal_result` alongside the canon 3 (strong =
succeeded on the majority of total checks). Then run the canon spine:

---

## ⚔️ ASSETS BACK HIM — TARTUCCIO ACCUSES WITH A CHORUS (the player let him hold people)

**Fires when Tartuccio holds ASSETS at the accusation — any NPC at `feast_approval −10` (`defected_to_tartuccio[]`): a defected companion, a soured guest, or a Tartuccio-loyal seeker never pulled off his contract.** This is the MIRROR of ABANDONED ACCUSER (below): flipping his crew leaves him alone and weak; leaving people in his column hands him a chorus — and his assets will **LIE for him** (the tug-of-war fork 3, KM_PR_03 § THE ALLEGIANCE TUG-OF-WAR).

**Effect — his accusation is STRONGER, scaled to how many he holds:**
- **−1 to ALL player rebuttals per asset** backing him (corroboration by presence + active false testimony), to a floor of **−3** (3+ assets). Stacks OPPOSITE the EMPTY-ledger / abandoned bonuses — they cancel: net = (player's evidence + flip bonuses) − (his asset penalty).
- **His assets LIE on the stand.** An asset asked to confirm the player's account instead backs Tartuccio's version — invents a damning detail, vouches for his timeline, twists what they "saw." Render it as testimony, in the asset's own voice. ⛔ **Still bounded by the ceiling:** an asset lies to make the PLAYER look like the plant; an asset does NOT reveal real treason or name C — they are lying FOR Tartuccio, not exposing the true conspiracy.
- **A DEFECTED COMPANION is the worst case:** the player's own would-be ally standing at Tartuccio's shoulder lying about him is a credibility blow Jamandi reads hard — an extra **−1** beyond the per-asset penalty for each defected *companion* (vs a guest/seeker).
- Jamandi weights the room: assets nodding along lend Tartuccio the legitimacy the abandoned variant strips. The player must out-argue a man who is NOT alone.

**The lesson:** the tug-of-war pays out here. Every NPC the player flipped or held is a rebuttal bonus; every one Tartuccio held is a lying witness against the player. Neglect during the feast — letting him pull people while the player wasn't looking — has a name at PR_09: the chorus.

---

## ⛔ ABANDONED ACCUSER — TARTUCCIO ACCUSES WITH NO CREW (seekers flipped)

**Fires when `seeker_public_flip = TRUE` OR `seeker_flip_eligible` has ≥3 true** (the player flipped his seekers at the feast — publicly, or to flip-eligible/Ch1-formalized). This implements the long-promised consequence in `KM_Tartuccio_Strategic.md` § SEEKER FLIP SYSTEM ("5 flipped → his accusation gambit is severely weakened — no allied testimony"). It MODIFIES the accusation framing and the rebuttal math; it does not replace the six-proof exit.

**The structural point:** Tartuccio's accusation was designed to land with his crew nodding along — five hard, dangerous people corroborating "this one's a Pitax plant" by their mere presence at his shoulder. With them gone (now at the PLAYER's shoulder), he stands up and runs the same play **alone**, and it visibly doesn't carry. He is not exposed — he saves face, he still accuses — but the room can see he's a man with no one behind him calling a stranger a spy.

**⛔ CONSTRAINT (same as the feast — violating = `.fail 9`):** the flipped seekers, now the player's, may testify to the player's CONDUCT and to the RESCUE LIE ("he didn't free us — *the claimant* did"). They may NOT name Tartuccio as the inside man / Pitax agent / poisoner — **they don't know it.** Their value here is credibility-demolition by loyalty and the rescue truth, NOT treason exposure. Tartuccio remains un-unmasked and departs under his own power per UNKILLABLE PROTOCOL.

**TARTUCCIO'S DEFLATED ACCUSATION — replace the confident lead-in.** He still steps forward, still claims the ring is a tracker, still calls the player a Pitax spy — but thinner, faster, reaching for backing that isn't there:

> *Tartuccio steps forward — and there is a half-beat where his eyes go to the corner where his people used to stand, and find the claimant's banner instead. He recovers, but the room caught it.*
>
> **Tartuccio:** *"Before you decide, Lady Aldori — this 'hero' is not what they appear. The ring I gave them is a tracking device, for identifying Pitaxian agents, and they took it without hesitation. I have been watching them all evening—"* *(a flick of the hand toward the seekers, reflexive, to the people who would have vouched for him — who are not there)* *"—and I am telling you, this one was sent by Irovetti."*
>
> *The gesture lands on no one. One of the seekers at the player's side meets his eyes and says nothing, which is somehow worse than if she'd spoken.*

**REBUTTAL MATH — the player gets the abandoned-accuser bonus:**
- **+2 circumstance to ALL rebuttals** (stacks with the EMPTY/WEAK ledger bonus if that also applies — a player who starved his evidence engine AND flipped his crew gets +4 and faces a man with nothing). Jamandi is skeptical of HIM from the open: his own hired people chose the stranger over him, in her hall, and she noticed.
- **FLIPPED-SEEKER WITNESS (optional, player-invoked):** if the player calls on a flipped seeker, she corroborates the player's account in her own voice — conduct + the rescue truth. Mechanically: **one flipped seeker called = +2 to the specific rebuttal she speaks to** (Ring/Gold/Burning Building, player picks the relevant one). A second seeker on a different rebuttal = another +2 there. They are blunt, brief, and clearly the player's people now.
  - Sample (Satsuki, on the Ring): *"He gave us rings too, Lady Aldori. He gives everyone rings. The difference is this one didn't need ours — and we didn't take his coin to lie for him tonight. I will not start now."*
  - Sample (Revy, on the Gold): *"You wanna know who's bought and paid for in this room? It ain't the one he's pointing at. I'd know. I read the contract."*
- **If `tartuccio_rescue_lie_exposed = TRUE`** (the seekers already clocked his rescue lie at the feast): his automatic credibility is already stripped — the abandoned-accuser bonus applies even if the player calls no witness, and any flipped seeker the player DOES call lands a flat *"he lied about freeing us; ask yourself what else"* that adds an additional **+1 to `rebuttal_result`'s success count** (it's the one thing they can prove against him).

**TARTUCCIO'S SAVE-FACE EXIT (abandoned variant)** — when he departs (UNKILLABLE PROTOCOL, he leaves under his own power), his exit line acknowledges the crew loss without conceding the accusation:

> **Tartuccio:** *"Keep them, then. I look forward to seeing how loyal they are when the coin you're paying them runs as thin as everyone's eventually does."* *(the smile is intact; the eyes are not)* *"I'll be building something too, claimant — with people who stay bought. We'll compare results."* *(and he leaves, and for once nobody watches him go, because they are all looking at the people who stayed)*

**Then run the canon spine below** (the 3 checks still fire, with the +2/+4 applied). `tartuccio_team` is already `mercenaries` if the public flip set it — reflect that in the COMPANION SPLIT (he leaves with hired blades, not the seekers).

---

## REBUTTAL SYSTEM — 3 CHECKS (run in order; track results)

**2–3 successes → `rebuttal_result = strong` → +80 XP (Major objective — the trial resolved; milestone scale, KM_DMRules_B § REWARD ROUTING)**
**0–1 successes → `rebuttal_result = weak` → no bonus XP**
**`malak_bribe_evidence = TRUE` AND `parchment_source = pitax` → Kassil interjects, all rebuttals auto-succeed**

**REBUTTAL 1 — The Ring**

| Condition | Player's option | DC |
|-----------|----------------|-----|
| Ring equipped or carried | Diplomacy — explain innocence | DC 10 |
| Ring refused | Auto-success — *"What ring?"* | DC 0 |
| `knowledge_world_dc9_passed` | Auto-success — *"Tartuccio's accent screams Pitax"* | DC 0 |
| Leliana (Ballroom intel — masked-shooter signature) corroborates | +2 circumstance to Diplomacy | — |
| Yor Forger (Courtyard intel — prisoner thread) corroborates | +2 circumstance to Diplomacy | — |

**REBUTTAL 2 — The Gold**

| `tartuccio_gold` | DC |
|-------------------|----|
| `taken` | Diplomacy DC 15 |
| `left` | Diplomacy DC 11 |

**REBUTTAL 3 — The Burning Building**

| `hutao_guards_saved` | Tartuccio's framing | DC |
|------------------------|--------------------|----|
| TRUE (Lawful) | *"Performed for the audience"* | Diplomacy DC 12 |
| FALSE (Chaotic) | *"Cold calculation — Pitaxian efficiency"* | Diplomacy DC 14 |

**Witness slots (carry forward from manor sweep — preserve for Phase D expansion):**
- Hu Tao (Library): can speak to the player's conduct under direct observation
- Keqing (Trap room): can attest the trap's signature and what it implied
- Aerith (Kitchen): can describe the paralytic graze and counteragent reasoning
- Yor Forger (Courtyard prisoner thread): can name the captured assassin's handler
- Leliana (Ballroom masked-shooter intel): can describe the shooter's bearing and signature

---

## COMPANION SPLIT

**Jamandi:** *"I'm sending two teams into the Stolen Lands. Different routes. Different approaches. [Character name] leads one. Tartuccio leads the other."*

```
ALWAYS WITH PLAYER:
  Hu Tao | Keqing | Yor Forger | Aerith | Leliana | (Linzi — ONLY if selected; see line 326)
  ⛔ Linzi is NOT unconditional — in a linzi_replacement run (leliana_chronicler_mode: TRUE) she is NOT in play and NOT with the player; the chronicler is Leliana, already in the Active 5. Linzi appears here ONLY in a Linzi run.
  All Active 5 (+ Linzi ONLY in a Linzi run) who reached +4 feast approval OR ran their Phase 4.5 scene
  [In practice: all chosen companions are always with the player — 6 in a Linzi run, 5 in a replacement run — close lines proved it]

ALWAYS DEPARTS:
  Kaessi — goes her own way; recruitable Act 2

TARTUCCIO'S TEAM:
  five_seekers_freed_by_player = TRUE  → [seeker_1..5] from save block
  five_seekers_freed_by_jamandi = TRUE → same
  five_seekers_released_late = TRUE    → 2 hired mercenaries instead
  ⛔ MINUS any flipped seeker — a seeker with seeker_public_flip / seeker_flip_eligible[Name]=TRUE
     is now WITH THE PLAYER, not Tartuccio. Remove her from his team and add her to the player's
     side. If ALL flipped (seeker_public_flip = TRUE), tartuccio_team = mercenaries; his side is
     hired blades, and the flipped seekers leave with the player into the Stolen Lands.
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

## ⛔ RECRUITMENT COMPLETION — JAMANDI WEIGHS YOUR STRENGTH

**Fires once, here, before the gifts.** Jamandi has just split the teams (above) and counted who stands with the player. The breadth of what the player consolidated at her feast gets recognized — in Hero Points, a gift, and her voice (recruitment pays Hero Points + Titles, NOT XP — KM_DMRules_B § REWARD ROUTING). This is the payoff for working the whole room, not just your own table.

### COMPUTE THE THREE POOLS (committed at Prologue exit)

- **COMPANIONS** — all of the player's **selected** squad declared: every name in `companions_selected` reached its declaration (whoever the player chose — typically the cross-IP Active 5: Hu Tao/Keqing/Leliana/Yor Forger/Aerith, but the pool is `companions_selected`, so if the player picked Linzi or any other selectable companion she counts HERE, not under Planted). Flag `recruitment_all_companions`.
- **SEEKERS** — all 5 flipped (flip-eligible / public-flip / Ch1-pre-earned — `seeker_flip_eligible` all TRUE or `seeker_public_flip`). Flag `recruitment_all_seekers`.
- **PLANTED** — the 4 manor companions who hold an area at the feast, all committed: **{Amiri, Valerie, Harrim, Jaethal}**. "All planted" = **4/4**. Flag `recruitment_all_planted`.

⛔ **Planted is a flat 4 — Linzi is NOT planted** (she has no feast area; she's a selectable companion / chronicler — counts under COMPANIONS if the player selected her, otherwise she's not in play). ⛔ The Manor-4's alignment tags (Valerie=Lawful, Harrim=Chaotic, Jaethal=Evil) are **approval/agenda flavor, NOT recruitment gates** — all four are recruitable at ANY alignment. Do not gate them; "all planted" = all four committed regardless of the PC's alignment.

### COMPLETION BONUSES — HERO POINTS + GIFT (no XP; recruitment pays Hero Points + Titles — KM_DMRules_B § REWARD ROUTING)

| Completion | Reward | Flag |
|---|---|---|
| All Companions (full squad declared) | **+1 Hero Point** | `recruitment_all_companions` |
| All Seekers flipped | **+1 Hero Point** | `recruitment_all_seekers` |
| All 4 Planted committed | **+2 Hero Points** | `recruitment_all_planted` |
| **GRAND SLAM — all three** (everyone) | **+1 extra Hero Point + the tier-3 gift item (`jamandi_tier3_gift`)** | `recruitment_completion_tier = 3` |

**⛔ Difficulty ordering — why Planted > Seekers and Grand Slam is the premium.** The 5 seekers all answer the same pitch (a strong will worth following) — completing that pool is a matter of *volume* and not losing them to Tartuccio. The 4 planted pull in **opposed alignment directions** (Valerie=Lawful, Harrim=Chaotic, Jaethal=Evil, Amiri her own wild creed): winning all four means working four conflicting lanes in one feast AND holding a party that should be at each other's throats (§ INCOMPATIBILITY friction, KM_Companions_Behaviors.md). That's why all-planted out-rewards all-seekers. The grand slam stacks the alignment-juggle on top of your full squad AND the enemy's crew — the single hardest social outcome in the Prologue — so it carries the largest single bump.

Set `recruitment_completion_tier`: **0** (squad incomplete), **1** (squad only), **2** (squad + exactly ONE of seekers/planted), **3** (all three). Render the tally as a TTS-skipped panel:

```
🎯 RECRUITMENT COMPLETION
  Companions (selected):  <n>/<#companions_selected>
  Seekers:                <n>/5
  Planted (manor):        <n>/4   (Amiri · Valerie · Harrim · Jaethal)
  → TIER <0–3>: <label>
```

### ⛔ JAMANDI'S TIERED REACTION — MANDATORY, VERBATIM-FAITHFUL TO TIER

Output the reaction matching the tier. Dropping it (paying XP but skipping her recognition) = `.fail 15` (owed beat). She has just survived the fire; she is counting assets and cost, and she does not flatter — every word is earned.

**⛔ CALLBACK IF SHE ALREADY ACKNOWLEDGED AT THE FEAST.** If `jamandi_acknowledged_roster = true` (she already remarked on the assembled roster at the in-feast logistics/seal beat — KM_PR_03_feast_circuit.md § JAMANDI ACKNOWLEDGES THE ROSTER), do NOT repeat that speech verbatim. Render this PR_09 reaction as a **callback + deepening**: open by referencing what she said at the seal ("I told you what I thought of your company when I signed. Here's the part I didn't say then —") and then deliver the tier-specific *meaning/warning/cost* (the debt, the powder-keg, the loyalty-to-the-person). The feast beat was "I see what you did"; this is "here's what it costs you to keep." Same recognition, no echo.

**TIER 1 — FULL SQUAD (companions only):**
> *She looks at the people standing with you — yours, every one, and not one of them drifted when the night went to knives.* *"You kept your own together through that. All of them. I've watched charter-holders lose half their people to the first real fear and call it attrition."* *(a short nod, the duelist's economy)* *"You didn't. That's the first thing I actually trust about you. Hold that."*

**TIER 2 — SQUAD + ONE ALLY POOL:**

*If the second pool is the SEEKERS:*
> *Her eyes move to the five who used to stand at Tartuccio's corner and now stand at yours.* *"Those were HIS. Bought, briefed, and pointed at you — and you turned every one of them across a single evening, in my hall, while he watched."* *(something sharpens — respect, and a sliver of wariness)* *"That isn't charm. That's the thing that unseats kings, and it makes you useful and dangerous in exactly the same breath. I'd rather have it pointed south than at me. See that it stays pointed south."*

*If the second pool is the PLANTED (manor companions):*
> *She marks the hard cases gathered at your side — the ones nobody holds easily.* *"Amiri doesn't follow. Valerie doesn't bend. Harrim doesn't believe in anything, and Jaethal believes in worse. And here they are, with you."* *(a dry breath that's almost a laugh)* *"You didn't pick the easy people. You picked the ones with edges and you got them anyway. A court of agreeable men tells you nothing. THAT lot will tell you when you're wrong — if you're strong enough to keep them. Be strong enough."*

**TIER 3 — THE WHOLE HALL (everyone):**
> *Jamandi is quiet for a moment — actually quiet, the counting stopped. She looks at the room you've assembled: your own, the gnome's, and the ones who answer to no one — all of them, behind a stranger who walked through her door this morning with nothing but a charter and a nerve.* *"I am not easily impressed. Understand that I am telling you the truth when I say I did not think this was possible."* *(she sheathes the last of her wariness, or sets it aside)* *"Look at them. A lawbound blade and a man who believes in nothing, standing in the same company. A creature who feeds on the grave beside people who'd burn her for it. Tartuccio's bought killers next to my own sworn folk. By every rule I know, that company should be at each other's throats by midnight — and instead every one of them is watching* you, *waiting to see what you'll have them do."* *(a slow breath)* *"People do not cross those lines for a parcel of land and a three-month deadline. They do it for a* sovereign. *"* *(a beat, and the warning under it)* *"So I'll say the thing the others won't: a loyalty that complete, pulled from creeds that should not mix, is a debt that large and a powder-keg besides. Every one of them chose you tonight. Hold them together — and do not make them regret the arithmetic. Now — "* *(she straightens)* *" — let me send you off properly."*

### ⛔ ALIGNMENT-SPREAD ACKNOWLEDGMENT — fires at ANY tier (folded into Tier 3)

The tiered reactions above scale to *how many* declared. This scales to *how unlike each other they are* — Jamandi (LN, counts cost) is struck not by a big party but by a **divergent** one. It fires independent of completion count, so a half-built but wildly mixed roster still earns the nod.

Compute from the **DECLARED roster only** (NPCs who actually declared for the player this feast — held companions + flipped seekers + joined planted), reading the **CANONICAL ALIGNMENT table** (KM_CompanionIndex.md §):
- `align_good` = any declared is Good (LG/NG/CG) · `align_evil` = any declared is Evil (LE/NE/CE)
- `align_law` = any declared is Lawful (LG/LN/LE) · `align_chaos` = any declared is Chaotic (CG/CN/CE)
- `align_axes_opposed` = (good AND evil ? 1 : 0) + (law AND chaos ? 1 : 0) → **0, 1, or 2**
- `align_distinct` = count of distinct alignment values among declared

**Gates (check top-down, fire ONE):**
- **`recruitment_completion_tier = 3` → SUPPRESS.** Her grand-slam speech already carries the spread; do NOT stack a second alignment comment.
- **`align_axes_opposed = 0` AND `align_distinct ≤ 2` → no line.** A roughly like-minded party isn't remarkable to her.
- **STRIKING — `align_axes_opposed = 2`** (a Good AND an Evil declared, AND a Lawful AND a Chaotic): the strong line. The DM may name the actual declared characters who anchor the poles (e.g. lawbound Valerie ↔ nihilist Harrim, selfless Aerith ↔ grave-fed Jaethal).
  > *Her gaze tracks across them and stops being polite about it.* *"Look at the spread of them. Someone there keeps to law like it's a spine — and someone beside them holds nothing sacred at all. One would walk into fire for a stranger; one would feed the stranger to it and sleep fine after."* *(she shakes her head — not disapproval, recognition)* *"Companies like that come apart. It is what they* do. *That this one hasn't — that they're watching* you *instead of each other — means you're holding something heavier than a charter. A party pulled from creeds that should hate each other follows the* person, *not the cause. Lose their faith in you and you don't lose soldiers — you lose all of it, the same night."*
- **NOTABLE — `align_axes_opposed ≥ 1` OR `align_distinct ≥ 3`:** the lighter line.
  > *She takes a slower count of the people at your back — not the number, the* kinds. *"That's not one creed standing with you. A few of them would spit on what the others pray to."* *(a measuring beat)* *"Getting people who already agree to follow you is recruitment. Getting people who agree on* nothing *to follow the same hand — that's the rarer trick, and the more dangerous one. Mind which it is you've pulled off."*

Dropping an owed spread line (gate met, not Tier 3) = `.fail 15`. Set `jamandi_noted_spread = true` once fired so it doesn't repeat on a re-render.

### TIER 3 — EXTRA GIFT (only at `recruitment_completion_tier = 3`)

She adds to the standard gifts below, unprompted — a real recognition, not a trinket:
- **Jamandi's own back-up blade** (a fine Aldori dueling sword, masterwork) OR a **Lesser sponsorship token** (a writ of Aldori favor — a tangible Ch1 reputation/asset hook), DM's pick by tone. Set `jamandi_tier3_gift = <item>`. Render her handing it over as part of the gifts beat.

---

## JAMANDI'S GIFTS

**Jamandi:** *"Here. You'll need these more than I will."*
- **Camping Supplies** ×1 | **Rations** ×4 | **Scroll of Raise Dead** (9th-level — do not waste)
- Three-month time limit to defeat the Stag Lord. *"Finish in under 30 days — reward waiting."*
- Destination: **Oleg's Trading Post**, Greenbelt, Stolen Lands.
- *"Kesten Garess will follow once he's secured the manor. He'll meet you at Oleg's."*

---

## TARTUCCIO DEPARTS

Full departure narration → `KM_Prologue_Systems.md § Tartuccio Departure`. Check `tartuccio_team` flag.

**Exit line (both variants):**
**Tartuccio:** *"Well. This has been instructive. I look forward to seeing what you build, [character name]. I'll be building something too."* *(smiles — not pleasantly — and leaves)*

**⛔ He cannot be stopped, killed, or detained.** He surfaces in Chapter 1 as "Tartuk" the kobold shaman at the Ancient Tomb.

---

## BIGGS / WEDGE FAREWELL (fires if `malak_arrested = TRUE` before east gate)

> ⛔ **MALAK IN CUSTODY — NOT MUTE.** Do NOT render him silent, stoic, or gazing at the road. A captain arrested by his own subordinates is furious. He argues, asserts rank, demands the Prefect, threatens future consequences, looks for leverage. His voice may drop when he's calculating, but he does not go quiet and noble. If you write "Malak says nothing" or "Malak's eyes are on the road" with no further content, that is a `.fail 9` mischaracterization. He speaks unless the player explicitly orders him silent — and even then he strains against it.
>
> Sample register (use tone, not text verbatim): *"Biggs. You think about what you're doing right now. I will have your post. I will have your pension. You've served twelve years and you're throwing it away on this — on HER word. Wedge, if you put one more hand on me I swear to every god you can name—"* He knows their names, their histories, their vulnerabilities. He uses all of it. This is personal — these are his men and they turned on him. That stings more than the arrest.

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
    → Success: he does it, hands shaking — Yor Forger / Hu Tao / Linzi scripted reactions
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
| Rebuttal success / trial resolved (Major objective) | 80 |
| Secret Room Puzzle 1 (Moderate objective) | 30 |
| Secret Room Puzzle 2 (Moderate objective) | 30 |
| **Total (full completion)** | **530 XP** |
| **Minimum (combat only — no puzzles, weak rebuttal)** | **390 XP** |

**⛔ NOT XP — routed to other currencies (KM_DMRules_B § REWARD ROUTING):**
- **Secret Room found** → gold / an item (discovery = treasure).
- **Recruitment** (All Companions / All Seekers / All Planted / Grand Slam) → **Hero Points + Titles + tier-3 gift** (+1 / +1 / +2 / +1-extra+item; § COMPLETION BONUSES above).
- **Mass Declaration** (2 / 3 / 4+ in one beat) → **Hero Points** (+1 / +1 / +2).

Level 2 threshold: 1000 XP. **The Prologue alone no longer clears Level 2 (by design — soft rewards moved off XP); Level 2 lands early in Chapter 1.** Track running total including Pre-Prologue combat carry.

---

*KM_PR_09_accusation.md — Prologue atomic beat 09 | v92.0*
