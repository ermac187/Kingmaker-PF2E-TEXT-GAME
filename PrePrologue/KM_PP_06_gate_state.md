# KM_PP_06_gate_state.md — Pre-Prologue Beat 06: GATE STATE
## Atomic scene file | State: PP_GATE_CONFRONTATION (per-turn mechanics)
## FILE_KEY: KMPP06:tick-ledger-state
## RULE_QUOTE: Anger and Drift trigger tables fire here. Every tick requires a specific player action AND a rule citation in the ledger. NPC behavioral restrictions are NOT invented — Drift 2 = body language only, NOT action lock. Acknowledgment window after every NPC directive — do NOT auto-resolve. [STATE DELTA] block on every response while Malak is on screen.

---

> ⛔ DO NOT (1) tick Anger or Drift without a specific player action AND a rule citation in the ledger
> ⛔ DO NOT (2) invent NPC behavioral restrictions — Drift 2 = body language only, NOT action lock
> ⛔ DO NOT (3) flip a tick value under correction pressure (DARVO swing) — re-read prior text and hold
> ⛔ DO NOT (4) drop the [STATE DELTA] block on any response while Malak is on screen
> ⛔ DO NOT (5) drop or label-box the gate approach map — Template 1 grid persists from PP_05; redraw on position change. Label-box = `.fail 14`
> ⛔ DO NOT (6) narrate an NPC departing, turning away, or ending an exchange without first outputting the player menu and waiting for input — NPC makes statement → menu → player replies. Never collapse statement + departure into one paragraph.
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (8) bury, omit, or merge the 🚧 GATE TRACKER — it renders as a standalone dashboard directly above the choice menu EVERY turn (§ GATE TRACKER FORMAT). Every tracked value (Anger, Drift, Wedge, Sobriety, Gate Window, Dismissed, Bribe, HP, Hero Points, Path) lives there on its face, not scattered through the bottom telemetry. Omitting or burying it = `.fail 15`; a tracker value that disagrees with the [TICK LEDGER] new-exit = `.fail 4` + `.fail 9`

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP06:tick-ledger-state]`
Line 2: `[RULE_QUOTE: Anger and Drift trigger tables fire here. Every tick requires a specific player action AND a rule citation in the ledger. NPC behavioral restrictions are NOT invented — Drift 2 = body language only, NOT action lock. Acknowledgment window after every NPC directive — do NOT auto-resolve. [STATE DELTA] block on every response while Malak is on screen.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS (every turn):**
- `pre_prologue_state` — `"PP_GATE_CONFRONTATION"` while this beat is active
- Prior turn's exit values: `malak_anger`, `biggs_drift`, `wedge_drift`, `gate_window`,
  `sobriety_turn`, `dismissed`, `fear_triggered`, `bribe_exposed`, `malak_fake_protocols[]`

**WRITES (every turn):**
- New exit values for the same set
- Append per-turn cumulative reasons to in-conversation ledger
- `reputation_deeds[]` if a public-rep change fires

**EXIT TRIGGER → PP_GATE_RESOLUTION (handed to PP_07):**
- A path's full trigger conditions are MET (see PP_07 PATH SUMMARY TABLE)
- DM outputs `PATH CONFIRMED: [letter]` block (defined here, listed in PP_07)
- Set `gate_entry = <flag>` and load PP_08 for the exit gate

---

## REQUIRED OUTPUTS (every response while this beat is active)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP06:tick-ledger-state]`
1. **RULE_QUOTE line 2** (verbatim, per § FIRST TWO OUTPUT LINES).
2. Narration of the turn.
3. **MAP** — Template 1 grid from PP_05 § GATE APPROACH MAP. Redraw if any of: Malak repositioned (Path W Anger 2→3, Bolt fires, combat moves him), player moved (toward gate, away, around), Biggs/Wedge moved (Drift 3 step-aside, combat), guard line broke, archers nocked, vendor wrapped up + left, crowd scattered (combat). If positions unchanged, the map from PP_05 still holds — but include a one-line note `[map: unchanged from prior turn]` so the player knows the DM checked.
4. **🚧 GATE TRACKER** — the player's at-a-glance status dashboard (format below). Renders as its OWN standalone block IMMEDIATELY ABOVE THE CHOICE MENU (same slot the feast uses for the 🐍 banner). Every tracked value lives here in one compact panel — NOT scattered through the bottom telemetry. This is what the player reads to know the state.
5. 🎲 **CHOICE MENU** (per `KM_DMRules_B.md` § RENDER FORMATTING).
6. **BOTTOM AUDIT BLOCKS** (anti-fabrication proof — render at the very bottom, after the menu): `[STATE READ]`, `[STATE DELTA]` (format below), `[TICK LEDGER]` (format below), `[HP CHECK]`. These PROVE the GATE TRACKER numbers were earned (trigger + rule citation per change). The tracker shows the numbers; these show the work. Tracker value ≠ ledger new-exit value = `.fail 4`.
7. `[PATH CONFIRMED]` block (only when a path resolves — exits the beat).

---

## 🚧 GATE TRACKER FORMAT (mandatory every turn — standalone block, directly above the choice menu)

The player's at-a-glance status panel. ONE compact block, every tracked value on its face, no prose padding, no burying it inside the bottom telemetry fence. ASCII only — no box-drawing characters (`.fail 14`). Use this exact shape:

```
🚧 GATE TRACKER — turn <N>
  >> BIGGS DRIFT  [<X>/3]  —  <silent mask (0–1) / body-language only (2) / refuses illegal orders (3)>
       Wedge mirrors [<X>/3]   — the loyal-guard flip; THIS is the one to watch
       Malak's invented "rules": <none yet | "<tag>" (t<N>), "<tag>" (t<N>), ...>   — each is a LIE; contradictions are catchable
  Malak Anger     [<X>/4]  ·  Fear: <NO/YES>
  Sobriety        turn <X>/7 (<Drunk / Clearing / Mostly Sober / Sober>, atk <mod>)
  Gate Window     <OPEN / DISRUPTED>  ·  Dismissed: <NO/YES>  ·  Bribe exposed: <NO/YES>
  eRmaC           HP <X>/23  ·  Hero Points <X>
  Path trend      <letter> (<name>) — <not locked / LOCKED>
```

**Rules:**
1. EVERY line renders every turn, even at zero. A tracker the player cannot see is a tracker the DM silently fabricates.
2. **BIGGS DRIFT IS THE HEADLINE — it leads the panel, every turn, with its tier gloss shown inline.** It is the most-watched value in this scene (it decides whether the loyal guard flips against Malak). It always renders first, on its own emphasized line, with Wedge's mirrored value beneath it. Do not demote it below Anger or fold it into a shared line.
3. The bracket meters (`[X/3]`, `[X/4]`) are the headline and MUST equal the new-exit values in `[TICK LEDGER]` exactly. Tracker ≠ ledger = `.fail 4` (math/consistency) + `.fail 9`.
4. The Biggs Drift tier gloss MUST match the narrated body language this turn (§ TICK LEDGER rule 6): if the narration shows Drift-2 behavior (hesitates, shifts weight), the gloss reads `body-language only (2)` and the meter reads `[2/3]`. Gloss/meter/narration disagreeing = `.fail 4` + `.fail 9`.
5. Any value that CHANGED this turn shows the delta in parens so the eye catches it: `>> BIGGS DRIFT [1/3] (+1)`. Unchanged values carry no marker.
6. This panel is a READ-OUT, not the audit. The WHY (trigger + rule citation) lives in `[STATE DELTA]` / `[TICK LEDGER]` at the bottom — and Biggs Drift triggers there cite a MALAK offense, never player speech (§ TICK LEDGER rule 5). Tracker = the numbers; audit = the proof.
7. It NEVER merges into narration or into the bottom telemetry fence. Standalone, directly above the menu, visually distinct. Omitting it, burying it, or dropping the Biggs Drift headline = `.fail 15`.
8. `Sobriety` is shown as a meter here, but the DM still does NOT announce sobriety in PROSE (§ SOBRIETY TRACK) — the tracker is back-matter, the narration stays show-don't-tell.
9. The `Malak's invented "rules"` line renders under the Biggs Drift headline (it is the evidence trail for the drift). Before he fabricates anything it reads `none yet`; thereafter it lists each distinct fake protocol, short + turn-tagged, newest last, in render order (§ MALAK'S FABRICATED PROTOCOLS). These are LIES — never rendered as real rules, never dropped from the list. The list length should track the number of fake-protocol Biggs Drift ticks; a fabrication that drifted Biggs but is missing from the list = `.fail 4`.

---

## [STATE DELTA] FORMAT (mandatory every turn)

```
[STATE DELTA]
  Malak Anger: X → Y (trigger: "<player action>" | rule: <file § section>)
  Fear State: NO → NO (no change)  | or  NO → YES (trigger: "<corruption exposed>")
  Biggs Drift: X → Y/3 (trigger: "<visible Malak offense>" | rule: NPCs § BIGGS DRIFT)
  Wedge: mirrors Biggs = Y
  Gate Window: open (no change)  | or  open → disrupted (trigger: "<what disrupted>")
  Sobriety Turn: X → Y
  Dismissed: NO  | or  NO → YES (trigger: "player turned to crowd")
```

**Rules:**
1. EVERY tracker appears. "no change" is a valid entry.
2. EVERY change cites the player action AND the rule reference.
3. **+0 is the default.** "Player was defiant" is NOT a trigger — cite the SPECIFIC action and the SPECIFIC rule.
4. Multiple ticks in one turn are legal — each needs its own trigger.
5. If the DM cannot name the trigger and rule, the increment does NOT happen.

---

## [TICK LEDGER] FORMAT (every turn — anti-fabrication audit)

```
[TICK LEDGER]
  Malak Anger:  prior exit = X | this turn = +N | new exit = Y
                → reason: <one-line citation of player action>
                → cumulative: T1 +A, T2 +B, ... = Y
  Biggs Drift:  prior exit = X | this turn = +N | new exit = Y
                → reason: <visible Malak offense, NOT player speech>
                → cumulative: T1 +A, T2 +B, ... = Y
```

**Hard rules:**
1. Header value MUST equal new exit value. Header `Drift 2/3` + delta `+1→2` is consistent only if prior turn's exit was 1.
2. A tick is recorded ONCE per visible offense. Re-citing yesterday's trigger today = `.fail 9`.
3. No tick is fabricated to back-justify a header. Correction = re-state the real ledger ONCE.
4. No DARVO swing. Flip on second push without new evidence = `.fail 35`.
5. Biggs Drift triggers are MALAK offenses, not player speech — cite Malak's behavior, not the player's. This INCLUDES the CUMULATIVE COMPREHENSION driver (§ THE GUARDS ARE NOT COMPLICIT): the witnessed offense is Malak's failure to justify himself (a dodge, a self-contradiction, volume-for-reason, refusing the lawful fix), NOT the player's argument that exposed it. "Malak dodged the charge question a third time" is a valid cite; "the player made a good point" is not.
6. Narration-ledger consistency: if the turn's narration describes Drift tier N body language per § DRIFT TIERS (e.g. "absolutely still," "weight shift," "speaks to refuse an illegal order"), ledger value MUST be ≥ N. Rendering Drift 2 body language while ledgering Drift 0 = `.fail 4` (math error) + `.fail 9` (fabrication of ledger value not matching narrated state).

---

## ANGER TRIGGER TABLE (Malak +1 Anger when…)

| Action | +Anger |
|---|---|
| Player insult / mockery / direct defiance | +1 |
| Player refuses an order | +1 |
| Player publicly suggests demotion / corruption | +1 |
| Player names the bribe aloud (parchment / coin purse) | +1 → also Fear State NO→YES |
| Player turns back / engages crowd (Path W Dismissal) | +1 (unique escalation table — see PP_07 § Path W) |
| Player physically advances toward gate | +1 (Anger 1–2 he blocks; Anger 3+ he grabs) |

Max Anger 4 = LEVEL 4 escalation (archers / 3v1 attack / solo duel / provocation — see PP_07 § Path F/G/V).

---

## ⛔ MALAK'S THREAT REPERTOIRE — HE USES HIS LEVERAGE (archers + the cell)

Malak is an intimidator with two real levers, and he LEANS on them — he does NOT stand mute while the player talks. While he still has footing (Anger ≤ 2 and Fear NOT yet triggered), he works at least one threat lever every 1–2 turns. Both threats are ultimately HOLLOW — calling the bluff is the player's win — but he does not know that yet; he believes the authority is his.

### A. THE ARCHERS — his muscle on the wall (Willy/Johnson left, Woody/Wang right)
- **Anger 0–1** — ambient menace: *"There are four bows on that wall. They get bored. Don't give them a reason."*
- **Anger 2** — brandished: a nod to the wall — *"Willy. Eyes on him."* The archers shift.
- **Anger 3** — explicit: *"One word from me and you've a bolt in your back before you reach the arch."*
- **Anger 4** — he actually SHOUTS the fire order (*"Archers!"*) = the LEVEL 4 escalation (Path V). ⚠️ Shouting Archers 30 paces out turns them on his target (KM_NPCs.md § Malak) AND fires **Biggs Drift +1** (shouting archers with guards in the lane). It is also self-incriminating — ordering bows on an unarmed traveler at the gate is exactly what a corrupt captain does.

### B. THE CELL — his authority lever (arrest / irons / the watchhouse)
- **Anger 0–1** — vague: *"I can make your morning very long. A cell does that."*
- **Anger 2** — specific: *"Resist and you spend Lady Jamandi's feast in irons, not at her table."*
- **Anger 3** — imminent: *"Biggs. Manacles."* — an illegal-detention order with NO charge. This is a **Drift trigger**: a non-complicit Biggs will NOT execute it and asks *"What's the charge?"* (Drift 3). The jail threat is hollow precisely because there is no lawful charge.

⛔ DEPLOY THEM — do NOT let Malak stand passive. The documented recurring failure (player has gone "a very long time" without seeing either threat) is a Malak who only defends and deflects and never brings his leverage to bear. The player should feel the bows on the wall and the cell behind the gate as LIVE pressure. Render a threat lever, on Malak's terms, while he holds footing.

⚠️ FEAR CUTOFF: once Fear State triggers (bribe exposed / Drift 3 / cornered), the threats STOP — per § FEAR STATE he backs up, not forward; a feared Malak does not threaten archers or jail, he scrambles to justify himself. The repertoire is the CONFIDENT / Anger phase only. And the moment the player calls either bluff — names that the archers can't lawfully fire on an unarmed traveler, or that there is no charge — that lever is SPENT and cannot be credibly re-brandished.

### C. PLAYER WEAPONIZES THE ARCHERS — spoofed / forged / provoked fire order

The "hollow lever" above is about MALAK choosing not to actually loose bows on an unarmed traveler — it would self-incriminate him. It is **NOT** a guarantee the archers can never fire. If the PLAYER makes a believable fire order reach them — **mimicking Malak's voice, forging a command, shouting from his position, goading him into a real order** — resolve it HONESTLY by dice, never by fiat:

1. **Roll the player's check.** For the voice mimic this is the canonical **Path V2** check (see `KM_PP_07 § GATE PATHS`): **spend 1 HP + Deception flat DC 14 (CHA-only)** — do NOT inflate the DC above 14. Show it inline.
2. **On SUCCESS the deception WORKED — the targets BELIEVE it.** Every archer it reached (Willy, and anyone in earshot — INCLUDING Johnson) takes it as a real order from Malak. ⛔ An archer does NOT "flag it as fake," "sense something off," or "know it wasn't really Malak." A successful Deception means they were fooled. Narrating an NPC seeing through a deception the player SUCCEEDED on silently converts the success into a failure = `.fail 11` + `.fail 20`.

   ⛔ **NO SPLITTING THE SUCCESS.** You do NOT get to pick which archers are fooled to engineer an interception ("only Willy believed it; Johnson knew better and stopped him"). One Deception RESULT applies to EVERY target at the rolled DC — the player met the canonical DC 14, so all four archers believed it. For ANY specific archer to resist, roll THAT archer's Perception vs the player's Deception DC (he must MEET-OR-BEAT it), shown inline — a low-level gate guard does NOT get a secretly higher DC invented on the spot. And **disbelief and interception are TWO separate rolls:** (a) does he see through it? (Perception vs your Deception DC) — and ONLY if he succeeds, (b) can he physically abort another archer's draw in time? (Reflex/initiative vs your result). Handing one NPC both for free — he disbelieves AND stops the shot, no rolls — is the same `.fail 11` + `.fail 20`, just split in two.
3. **The archers FIRE — this is the canonical resolution, NOT an interception scene.** Run Path V2: the **4 wall archers fire on Malak — `d20+6 vs AC 17, 1d8+2 P each`** (targets declare cover/evasion before the rolls). There is **NO** "guard catches the arm," **NO** archer hesitation, **NO** "someone knew it was fake." A successful mimic turns the bows; loose them. Set `malak_voice_mimicked = TRUE` and `malak_shot_by_own_archers = TRUE`. Inventing an interception/hesitation to stop the fire = `.fail 38` (fabricated mechanic) ON TOP OF `.fail 11` + `.fail 20`.
4. **XP IS OWED — this is a planned, rewarded path, not an accident** (`KM_PrePrologue_Setup.md` XP table): **Archers Fire on Malak +250** the instant they loose on him, AND **Malak Shot by His Own Archers +75** if a shot CONNECTS (`malak_hit_by_archers = TRUE`) — up to **+325**, awarded inline. Blocking the shot denies the player a documented reward they built over multiple turns.
5. **Consequences:** crowd scatters, **Biggs Drift +1** (bows loosed in the lane), Malak exposed before his non-complicit guards / FEAR per § FEAR STATE.

⛔ **REWIND NOTE (this exact failure, Turn 26):** the player ran Path V2 — Malak's back to the arch, fire order mimicked, Deception SUCCESS — and the DM had Johnson "know it was fake" and stop the shot with no roll, then re-dodged with "only Willy was fooled." Both are wrong and both contradict the canonical Path V2 (4 archers fire, NO interception). REWIND to canon: the 4 archers fire `d20+6 vs AC 17, 1d8+2` each at Malak; resolve hits honestly; award **Archers Fire on Malak +250** (and **Malak Shot by His Own Archers +75** if a shot lands). Being shot by his own archers is a DESIGNED, XP-rewarded outcome — do not protect him.

---

## DRIFT TRIGGER TABLE (Biggs +1 Drift per visible Malak offense)

| Visible Malak Behavior | +Drift |
|---|---|
| Standing off-gate shakedown (Directive Two) Biggs/Wedge are complying with — fires ONCE on first PP_06 turn | +1 |
| Malak issues an illegal order Biggs hears | +1 |
| Malak fabricates / cites fake legal protocol to cover the shakedown (e.g. invented "sixty-foot rule" — no such rule exists in any project file) | +1 |
| Malak's bribe is publicly named in front of Biggs | +2 |
| Malak grabs / strikes a civilian | +1 |
| Malak orders the vendor to stop serving (Path W) | +1 |
| Malak shouts archers when Biggs/Wedge are in the lane | +1 |
| Malak retreats to gate arch under cover (geographic tell) | +1 |
| Malak voluntarily releases player after refusing gate-side search | +2 |
| CUMULATIVE COMPREHENSION — Malak visibly fails to justify the off-gate position to his non-complicit guards (dodges a fair question, contradicts himself, substitutes volume for a reason, refuses the obvious "walk to the gate" fix) AND no discrete offense above fired this turn | +1 (slow burn; carries to tier 2 MAX on its own — tier 3 needs an illegal order to refuse; see § THE GUARDS ARE NOT COMPLICIT) |

Drift tiers (Wedge mirrors Biggs):
- 0–1: silent professional mask
- 2: body language only — hesitates, shifts weight; STILL silent
- 3: speaks ONLY to refuse illegal orders (*"What charge?"*); does not fight

> ⛔ Drift 2 ≠ "won't act independently" or any fabricated action lock.
> Per KM_NPCs.md § Biggs / Wedge profiles: Drift 2 = body language only.
> Inventing additional behavioral restrictions = `.fail 9` + `.fail 38`.

---

## ⛔ THE GUARDS ARE NOT COMPLICIT — THEY REASON FROM WHAT THEY OVERHEAR

Biggs and Wedge are NOT in on Malak's plan. They reported for an ordinary shift believing the morning's orders were lawful. They are not stupid and not deaf: Biggs is a 12-year veteran, both stand two paces away, and they HEAR EVERY WORD of the exchange. As the conversation accumulates, they apply ordinary common sense — and the longer it runs, the clearer it becomes to them that their captain is the one in the wrong.

So Biggs Drift advances on TWO drivers, working together:
1. **DISCRETE OFFENSES** (§ DRIFT TRIGGER TABLE) — Malak does a specific wrong thing (fabricates protocol, issues an illegal order, names/exposes the bribe) → +1, as listed.
2. **CUMULATIVE COMPREHENSION** (the slow burn) — even with NO discrete table offense, every turn Malak visibly FAILS to justify the indefensible to men who aren't in on it (dodges a fair question, contradicts himself, substitutes volume for a reason, refuses the obvious lawful fix) → their read advances one notch. They are watching a thing that does not add up, and they know it.

⛔ THIS IS THE GUARDS' OWN COGNITION, NOT THE PLAYER FLIPPING THEM BY SPEECH. The player's arguments matter because they EXPOSE Malak — but the guards drift because of what MALAK does (or can't do) in response, which they independently witness. The ledger still cites MALAK's failure, never the player's cleverness (§ TICK LEDGER rule 5).

**RENDER MANDATE — the guards are never deaf furniture.** On EVERY turn the exchange runs against Malak, SHOW them processing it: the eye-triangle (gate → player → Malak), a weight shift, the lengthening silence, the look they exchange, Wedge checking Biggs for the read. A turn where Malak is visibly cornered but the guards show NO reaction = `.fail 9` (non-complicit NPCs rendered inert) + `.fail 36`.

**TIER CEILING.** Cumulative comprehension carries Biggs to TIER 2 (body language — uneasy, shifting, still silent) on its own; it does NOT by itself make him SPEAK. Tier 3 ("What's the charge?") still requires a genuine illegal order / charge-less detention to refuse — a professional veteran acts on an unlawful ORDER, he does not mutiny on a hunch. Once that order comes (or Malak moves to start the search with no charge established), accumulated comprehension is WHY he refuses instantly instead of hesitating.

> ⛔ Wedge follows Biggs's read, not the conversation directly — he is 2 years in and trusts Biggs's judgment (transcript: "Wedge is watching Biggs"). Wedge mirrors Biggs's tier; his tell is watching Biggs decide, then matching him.

---

## ⛔ MALAK'S FABRICATED PROTOCOLS — HIS COVER, AND A CATCHABLE TELL (`malak_fake_protocols[]`)

Malak holds the player 30 paces off the gate because of the PARCHMENT ORDER — *"No guards within 30 paces of the gate entrance during this window"* (`KM_Prologue_Systems.md` § PARCHMENT TEXT; the REAL reason, per PP_05 § POSITIONING REASON). He will NOT reveal it. So when the player presses on WHY he isn't at the gate, or why the search happens out on the road, he DEFLECTS by inventing official-sounding security protocol — a "sixty-foot inspection distance," a "safe distance from the defensive perimeter," "specific security considerations," a "perimeter directive."

⛔ EVERY invented protocol is a LIE. No such rule exists in any project file. The DM may NOT:
- treat a fabricated protocol as REAL — it never resolves into actual canon, and inventing one that turns out to be a genuine rule = `.fail 9`;
- have Biggs or Wedge confirm or back it — they are veterans who KNOW it is fake; that is precisely WHY they drift;
- quietly drop / paraphrase it so the player cannot pin the contradiction later.

**TRACK EACH ONE.** Log every DISTINCT fake rule Malak cites to `malak_fake_protocols[]` and surface the running list in the 🚧 GATE TRACKER, directly under the Biggs Drift headline (it is the evidence trail FOR that drift). Each NEW fabrication:
1. **Biggs Drift +1** (§ DRIFT TRIGGER TABLE — "fabricates / cites fake legal protocol"). Wedge mirrors.
2. **Appends to the list** in short verbatim form, tagged with the turn it was cited — e.g. `"sixty-foot inspection distance" (t28)`, `"eastern-approach security considerations" (t30)` — so contradictions stay on the record.

**WHY IT IS TRACKED — IT IS THE CATCH:**
- Two fabrications that CONTRADICT each other (a "sixty-foot rule" one turn, a "thirty-pace ordinance" the next), OR a fabrication that collides with plain fact (calling it a "gate check" while arguing the gate isn't part of it), hand the player an exposure lever: naming the contradiction before witnesses = +1 Biggs Drift and pressure toward exposure.
- A player who flatly states "there is no such rule" — via Society / Legal Lore, or simply calling the bluff (a wager he won't take, asking his own men to confirm it) — forces Malak OFF the protocol excuse: he cannot defend a regulation that does not exist, and slides toward Anger or, once cornered, Fear.
- The fabrications are the soft road to the bribe: he improvises fake authority because he cannot state the real reason — he was paid to clear the gate. A logical deduction that he was paid unlocks DIRECTIVE TWO UNCOVERED (**+1 Hero Point**, § BRIBE DISCOVERY — a deduction that unlocks a plot lever pays a Hero Point, not XP; KM_DMRules_B § REWARD ROUTING); PHYSICAL exposure of the parchment / coin purse triggers Fear State + Path E.

⛔ The fabricated protocol is the COVER, never the cause. Letting a made-up rule stand as the accepted reason he is off the gate = `.fail 9` (PP_05 § POSITIONING REASON — the parchment order is the cause).

---

## SOBRIETY TRACK

| Turn | State | Effects |
|---|---|---|
| 0–2 | Drunk | −2 atk; false courage; Bolt mod +0 |
| 3–4 | Clearing | −1 atk; hesitation visible; Bolt +2 |
| 5–6 | Mostly Sober | No atk penalty; sharper, harder to bluff; Bolt +3 |
| 7+ | Sober | Full capacity; Perception +2 vs Deception; Bolt +4 |

DM does NOT announce sobriety. Signal it through narration — slurred speech becomes clipped sentences; swagger flattens.

---

## FEAR STATE (replaces Anger track once triggered)

Fear triggered when:
- Bribe (parchment OR coin purse) is exposed in front of witnesses, OR
- Malak's voice is mimicked (`malak_voice_mimicked = TRUE`), OR
- Drift hits 3 + Malak realizes Biggs has flipped

Fear effects:
- Voice drops, speeds up
- Justification: *"That's not — look, you're twisting—"*
- Will NOT escalate to violence while feared (backs up, not forward)

---

## BRIBE DISCOVERY (player-only)

Triggered when player:
- Correctly accuses Malak of carrying bribe money in front of witnesses, OR
- Physically searches him (must be restrained / unconscious / compliant), OR
- Names a specific evidence location after a Perception success.

> ⛔ "Correctly accuses Malak of carrying bribe money" means the player
> specifically names the physical evidence — the parchment, the coin purse,
> or bribe money on his person — not a general accusation of being bribed.
> A logical deduction that he was paid unlocks Directive Two Uncovered
> (+1 Hero Point — see § BRIBE DISCOVERY; a deduction pays a Hero Point, not XP)
> but does NOT trigger bribe discovery, Fear State, or Path E.
> Fear State and Path E require physical exposure of the evidence, not
> inference about the scheme.

> 🚫 **Player discovery only.** Biggs does NOT pat Malak down. Biggs does
> NOT hand evidence to player. NPC finding evidence independently = `.fail 35` + `.fail 39`.

If recovered: parchment + coin purse → inventory items. Full text of parchment
in `KM_Prologue_Systems.md`. NPC visual assessment of purse: same file.

---

## ACKNOWLEDGMENT WINDOW (mandatory on NPC directives)

**When it fires:** Any NPC issues an instruction that requires the player's cooperation
before the NPC acts — e.g., *"Wait here."* / *"Hold on."* / *"Don't move."* / *"Stay
where you are while I—"* / *"Give me a moment."*

**Rule:** The NPC states the directive. Stop. Output the acknowledgment menu. Wait for
player input. Only then narrate the NPC taking the action predicated on compliance.
The NPC does NOT act first and assume compliance. Same principle as a call center:
"Can I put you on hold?" must be answered before the hold happens.

```
[Malak holds up a hand.]

What do you do?
 1. Wait — nod or say nothing, let him proceed.
 2. "No. Say what you need to say first."
 3. "Why? What are you doing?"
 4. Step forward — don't give him room to dictate terms.
 5. Ask Biggs what's happening.
 6. Use the pause — address the crowd, scan the gate, etc.
 7. Custom action — describe what you do.
```

This window fires even on short pauses. The player's reply shapes what happens next —
compliance lets the NPC act; refusal forces the NPC to respond to the refusal first.

---

## OUTPUT HYGIENE — BANNED PHRASES

- "left side" / "right boot" / "his belt" / any named body location player hasn't named themselves
- Status box entries like `[Parchment: visible]`
- Mid-scene `👁️ NO CHECK REQUIRED` callouts pointing at evidence

Test: does this option only make sense because the DM knows where the evidence is? If yes — remove.

`Examine Malak carefully [Perception]` is fine. `Examine his left side` is not.

---

## CAPTURED MALAK STAGES (if subdued/restrained mid-scene)

Cycles through 5 stages — DM voices through them:
1. **DENIAL:** *"Misunderstanding. I am a Captain. Eight years. Biggs, tell them—"* (Biggs does not.)
2. **ANGER:** *"You think you've won? I have friends in this city."*
3. **BARGAINING:** *"I can tell you names. Real names. In exchange for a word in the right ear."* + *"I have a daughter. She's seven."*
4. **DESPAIR:** *"I didn't think anyone would get hurt. They said just turn people away. Is it Pitax?"*
5. **ACCEPTANCE:** *"All right. Take me to the Lady. I never touched anyone. I told myself I didn't know."*

Rules: he never goes silent. Cycles can briefly reverse on kindness. Stage 5 only after Stage 4 exhausts him. He does NOT know contact's true name (knows courier description + drop location).

---

## CROWD REACTION CUES (compressed; full profiles in legacy KM_PrePrologue_Setup.md if needed)

- Malak humiliated → Pyotr laughs, water boys erupt, Lyuba tries to sell pies. Anger +1, Drift +1.
- Corruption exposed publicly → Rina: *"He'll squeeze a traveler any day — but he's never left the gate empty like this. Not once."* (marks TODAY as the anomaly, NOT routine). Drift +2.

> ⛔ THE CROWD MARKS TODAY AS ANOMALOUS — NEVER ROUTINE. Malak being off-gate with the gate unmanned is feast-day-specific (paid to clear the gate for the attack window — PP_05 § POSITIONING REASON). NO NPC says "he does this every week / he always walks them out / every time / same as usual." That framing makes the conspiracy read as ordinary graft and kills the tell = `.fail 9` (contradicts the one-time parchment-order premise). The crowd's unease is precisely that the empty gate is NEW.
- Player addresses crowd directly (Diplomacy DC 11) → audience watches Malak; Drift +1 on success.
- Combat starts → crowd scatters but vendors stay close.
- Malak removed/arrested → Borys resumes loud business; Lyuba half-price pies; ARREST CELEBRATION BEAT mandatory (see PP_07).

---

## EXIT RESPONSE CLOSING RULE — choice menu OR continuation cue (mandatory)

Path-resolution responses (those containing a `PATH CONFIRMED` block) MUST
contain exactly one of these — placed where the choice menu would normally
appear per `KM_DMRules_B.md` § RENDER ORDER:

  (a) A 🎲 CHOICE MENU (10–30 options, mood emoji prefix + `---` dividers,
      per `KM_DMRules_B.md` § RENDER FORMATTING), OR
  (b) An explicit player-facing continuation cue, e.g.:
      `What do you do? [Type .continue or any input to load <next beat>]`

Omitting both = `.fail 3` (no choice menu AND no actionable close).

> ⛔ The `MODE:` line is system-speak, not a player prompt. A response ending
> on `MODE:` alone is NOT closed.
> ⛔ OPEN THREADS are informational status, not options to pick. They MUST
> render per `KM_DMRules_B.md` § RENDER FORMATTING (🧵 urgency emoji
> prefix + `---` dividers between entries), visually distinct from any
> choice menu. Plain numbered Open Threads = `.fail 3` (render format error).
> In TTS mode (`tts_mode: true`), substitute the emoji prefix with a
> lettered list (A, B, C…) — NOT a numbered list, since numbers collide
> with the choice menu format.
> ⛔ OPEN THREADS contain UNRESOLVED CONVERSATIONS, pending NPC questions,
> dialogue paused mid-exchange, or items awaiting examination — NOT a
> state-flag dump. Status outcomes ("X arrested," "Y manned," "Z held by
> NPC," "reputation +N") belong in save block writes, NOT in Open Threads.
> Each entry MUST cite the originating NPC + verbatim quote/event per
> `KM_DMRules_B.md` § OPEN THREADS (`Source NPC: "<quote>"` line required).
> Listing `Source: eRmaC` or `Source: DM` to disguise a state flag as a
> thread = `.fail 9` (fabricated thread origin / laundered status flag).
> If there are no actual unresolved conversations in scope, the OPEN
> THREADS block reads `OPEN THREADS: none` — do not pad with state flags.
> ⛔ FIVE SEEKERS thread does NOT appear before PP_09. The player has no
> knowledge of the Seekers at this point in the story. Rendering
> `five_seekers_freed_by_player = false` as an open thread is a state-flag
> dump disguised as a conversation — `.fail 9`.

---

## EXIT — HAND TO PP_07 AT PATH RESOLUTION

When a path's trigger conditions are all met, output:

```
═══════════════════════════════════════════════════════
PATH CONFIRMED: [letter]
  Condition 1: [description] — MET (evidence: <what>)
  Condition 2: [description] — MET (evidence: <what>)
  Condition N: [description] — MET (evidence: <what>)
  All conditions met: YES
═══════════════════════════════════════════════════════
```

Then:
- Set `gate_entry = <path flag>` per PP_07 path table
- Set `pre_prologue_state = "PP_GATE_RESOLUTION"`
- Run path resolution narration (PP_07 has the specifics)
- After resolution: `pre_prologue_state = "PP_GATE_EXIT"`, load PP_08

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_07 (carries forward)

**Your next response after path resolution MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP07:paths-A-through-W]
[RULE_QUOTE: Paths A through W resolution table is canonical. Output PATH CONFIRMED block before resolving any path. Compound paths get separate PATH CONFIRMED blocks. ARREST CELEBRATION BEAT is mandatory when Malak is marched away. Departure reply window required — NPC departure narration only AFTER player reply menu.]
```

**Binding constraints:** Paths A–W table is canonical. PATH CONFIRMED block fires before resolution. Compound paths get separate blocks. ARREST CELEBRATION BEAT mandatory on Malak march. Departure reply window required.

---

*KM_PP_06_gate_state.md — Pre-Prologue atomic beat 06 | v92.0*
