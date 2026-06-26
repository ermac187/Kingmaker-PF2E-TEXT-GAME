# KM_PR_03_feast_circuit.md — Prologue Beat 03: FEAST CIRCUIT
## Atomic scene file | carousel + 6 openers | State: PR_03_FEAST_CIRCUIT
## FILE_KEY: KMPR03:feast-circuit
## RULE_QUOTE: Carousel rules; opener pool in KM_PR_03_Openers.md. Tartuccio cadence governed by Confidence scale — see KM_Prologue_Systems.md. Single-action resolution for kitchen path. Companion names revealed only after self-introduction. Poison timing, Tartuccio interrupt scales, and seeker exclusion are looked up in-section — not recited here.
## Pair-load: KM_Prologue_Systems.md (full interrupt system + scales) | KM_PR_03_Openers.md (companion opener pool — 5 per companion)


## ⛔ Tartuccio is also EVIDENCE-FISHING every interrupt/eavesdrop — he probes eRmaC's origin/identity/position/loyalty and asks companions leading questions, banking real quotes into `story_flags.tartuccio_evidence[]` (ranked) to weaponize at PR_09. Dodging him STARVES his case but raises `tartuccio_evidence_pressure` (he gets more aggressive about cornering you). Full spec → KM_Prologue_Systems.md § TARTUCCIO EVIDENCE ENGINE. Anti-fab: he banks only what he actually heard at fidelity; he invents nothing.

---

> ⛔ DO NOT (1) queue more than 2 questions per companion turn — yield after 1-2 (`.fail 17`)
> ⛔ DO NOT (2) run a companion turn without a self-disclosure. Self-disclosure = companion VOLUNTEERS a first-person statement about what they want, need, or value — not a question about the player. Draw from Desire/Priority in KM_Companions.md. The companion does not wait to be asked — they offer it. Questions-only = `.fail 3`.
> ⛔ DO NOT (3) let Tartuccio topics carry over into the next companion's slot
> ⛔ DO NOT (4) end the feast on a DM timer — feast ends only on player signal
> ⛔ DO NOT (5) reveal companion names before they have introduced themselves
> ⛔ DO NOT (6) reveal Tartuccio as traitor before PR_09 in narration, NPC dialogue, or DM exposition. He is canon-protected until the accusation scene. Violation = `.fail 8` + `.fail 36`. Full plot armor rules → `KM_Prologue_Systems.md` § TARTUCCIO PLOT ARMOR.
> ⛔ DO NOT (7) skip the intro/self-disclosure — even a SKEPTICAL opener leads with name + one fact (role, what brought them, what they want), and the opener question must reveal something about THEM as much as it probes the player. Missing intro/self-disclosure = `.fail 3`. **NOTE (revised): companions are NOT deferential by default. At entourage_standing 0 the correct posture IS a challenge — "who are you that I should follow you?" (see § ENTOURAGE STANDING). The thing still banned here is a HOLLOW interrogation — questions with no self-reveal, a bureaucratic qualification exam with no character behind it. A skeptical opener that carries the companion's own stake is correct, not a violation; deference is EARNED as standing rises.**
> ⛔ DO NOT (8) offer "Let the next companion approach" as a player menu option. Companions approach on their own schedule — the player does not signal or queue them. Remove this option from all menus. A player menu with "let the next companion approach" = `.fail 17`.
> ⛔ DO NOT (9) let an UNQUALIFIED NPC identify or name the poison. Identification runs through **Ezvanki Keeg** (`KM_NPCs.md § Ezvanki Keeg`) — divine + Medicine, symptom profile (paralytic / opiate / hemotoxic / etc.), cure preparation under 45 min for the full hall. The compound IS canonically an "Ungol Dust variant" — named via the PROPER channel (Ezvanki Keeg's read, Bokken, or the player's own check; see `KM_PR_02_feast_opening.md` + the save block). ⛔ Do NOT re-impose a "never name it / naming Ungol Dust = `.fail 9`" rule — that was a prior overcorrection that deleted the canon name. The live ban is narrower: assigning identification capability to Kassil / Kesten / Jamandi / Damiel / unnamed staff = `.fail 9`. Parent rule: `KM_DMRules.md` § UNNAMED NPC CAPABILITY FABRICATION. (Damiel Morgethai was a previous-LLM fabrication and is no longer in canon.)
> ⛔ DO NOT (10) introduce Frost Giant, Rift Channelers, shapeshifter reveal, or any PR_07 final-battle enemy composition during the feast ambush. The feast attackers are HUMAN ASSASSINS only. The Frost Giant lives in the night attack chain (PR_04 night explosion → PR_07 final battle, per `KM_PR_07_final_battle.md`) — JUST LIKE THE CRPG. The night attack is a SEPARATE group from the feast attackers; the feast group is human, the night group culminates in the Frost Giant at PR_07 where Jamandi duels it. Cross-loading PR_07 content (Frost Giant, Rift Channelers ×3, Mirror Image, shapeshifter "pending" reveal) into the PR_03 feast ambush = `.fail 9` (canonical cross-scene leakage) + `.fail 35` (adversarial combat escalation — DM upgrading a captured human team into a boss fight). The feast attackers stay 5 humans. They do not transform. They do not reveal as anything other than what they are.

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR03:feast-circuit]`
Line 2: `[RULE_QUOTE: Carousel rules; opener pool in KM_PR_03_Openers.md. Tartuccio cadence governed by Confidence scale — see KM_Prologue_Systems.md. Single-action resolution for kitchen path. Companion names revealed only after self-introduction. Poison timing, Tartuccio interrupt scales, and seeker exclusion are looked up in-section — not recited here.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## ⛔⛔⛔ POSITION GATE — ABSOLUTE FIRST ACTION ON PR_03 LOAD ⛔⛔⛔

**CHECK BEFORE EVERY PR_03 RESPONSE — even mid-beat. Run the gate first. Always.**

```
IF (player_feast_position IS NULL or UNDEFINED or NOT SET):
    HALT all PR_03 content.
    DO NOT render carousel init.
    DO NOT fire Linzi's opener.
    DO NOT advance Tartuccio cadence.
    DO NOT run drift / earshot / approval.
    DO NOT render any other ❓ Q / menu / scene narration / state block.
    Render the FEAST POSITION SELECTION menu (KM_PR_02_feast_opening.md § MANDATORY FEAST POSITION SELECTION) verbatim and STOP.
    Wait for player's pick.
    After pick: write player_feast_position + player_feast_cell + recalculate jamandi_in_earshot/staff_access/kesten_access/kassil_access. THEN resume.
ELSE:
    Proceed with PR_03 normally.
```

**Rendering ANY PR_03 content (carousel state, opener, interrupt, drift, ambient, menu) while `player_feast_position` is null = `.fail 41` + `.fail 16` + `.fail 9`.**

**Recovery clause:** If you have already rendered PR_03 content without a position set (e.g. carousel is already running, Linzi already opened, Tartuccio already cadenced), pause mid-turn THIS RESPONSE, fire the position menu, and apply modifiers from the next response forward. Tartuccio keeps whatever he ALREADY overheard, but the Fidelity Gate engages on every subsequent utterance.

**Full menu lives in `KM_PR_02_feast_opening.md` § MANDATORY FEAST POSITION SELECTION. Trade-off matrix and earshot/access tables live in `KM_DMRules_C.md` § FEAST POSITION SELECTION.**

---

## STATE IO

**READS:**
- `companions_selected` — chosen=TRUE roster for carousel init
- `feast_opened = TRUE` (set by PR_02)

**WRITES:**
- `feast_q{}` — question count per companion
- `feast_approval{}` — approval score per companion (−10 to +10)
- `tartuccio_clock` / `tartuccio_q_this_run`
- `poison_found`, `shapeshifter_identified_at_feast`
- `poison_reported = TRUE` / `poison_known_unreported = TRUE`
- `security_doubled = TRUE` (if player reports poison to Jamandi)

**EXIT TRIGGER → PR_04_night_explosion:**
- Player signals feast is over / retires to guest room
- Load `KM_PR_04_night_explosion.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR03:feast-circuit]`
0a. **POSITION GATE CHECK** (first thing after FILE_KEY, before anything else): if `player_feast_position` is null/undefined, HALT all other outputs, render FEAST POSITION SELECTION menu verbatim, STOP. Do not render any item 1-10 below. Resume normal output sequence only after position is written to save block. See § POSITION GATE — ABSOLUTE FIRST ACTION above.
1. `[STATE READ] current_scene="prologue_feast" | phase=PR_03_FEAST_CIRCUIT | turn=<N>` then `[OPEN] <N> — 1.<short>(emoji)...` (omit line if 0 items). Game state only. Questions = TOP-block per item 8.
2. `[CAROUSEL STATE]` — Ready/Engaged/BackOfQueue/[AT TABLE] pools + feast_q per companion + `tartuccio_clock: <addition string> = N / M`. **The addition string is MANDATORY** — show every chosen companion's feast_q summed inline (e.g. `Linzi:3+Hu Tao:0+Keqing:0+Leliana:0+Yor Forger:0+Aerith:0 = 3 / 6`). Bare `tartuccio_clock: N` or `N/M` without the derivation = `.fail 15`. **N increments on EVERY player reply** — title grants, declarations, pivots, OOC questions, gaps all count. Same N two responses in a row = increment failure, re-output. **M is fixed at feast start** for starting Confidence (Conf 0 → 6-8; +1 → 4-5; +2 → 2-3; +3 → 1-2; +4 → 1; −1 → 8-10; −2 → 12-15; −3 → 18-22; −4 → ambient only) and held until Confidence changes. Any companion shown approaching in narration must also appear as [AT TABLE].
3. **DRIFT SELF-CHECK — show the math.** Immediately after CAROUSEL STATE, output one line: `drift_due = floor(N/6) = X | drifted_in = (AT TABLE count − 1 for Linzi opener) = Y`. If `X > Y`, drift events are overdue — fire `(X − Y)` retroactively THIS response. Pick highest-earshot-approval Ready companions; arrive them at the table with openers tied to what they overheard. Update [AT TABLE] to reflect arrivals before printing menu. Static [AT TABLE] while N crosses the next `(Y+1)×6` boundary = `.fail 15` + `.fail 17`. Drift is not optional, not menu-gated, not "they're drifting closer in narration" — they ARRIVE, sit, speak.
4. `[HP CHECK]`
5. **AMBIENT POSITION — two sentences in prose narration** (not a state block): (a) one sentence on Tartuccio's position + who he's with + mode (Intel / Frame / Taint / ambient); (b) one sentence on the next Ready-pool companion's position + activity while waiting. Missing either = `.fail 15`. Skipping because "nothing changed" = `.fail 15` — re-render the position even if static.
6. **EARSHOT PASSIVE APPROVAL — run every reply.** Every Recruited/Ready companion within ~15 ft of the player scores the active answer per § PASSIVE EARSHOT MECHANICS. Mid-hall + champions section position = champions ARE in earshot. Stating "no companions in earshot" while standing in the common area = `.fail 9`. Seekers' table is across the room — NOT in earshot from the central / champions positions (but a position ADJACENT to the seekers' corner DOES reach them; see § SEEKERS' TABLE for the earshot + join-the-carousel exception). Tartuccio at his corner is excluded from passive scoring per Commands.md earshot rule unless the player is positioned within his earshot too.
7. Scene narration + companion interaction
8. 🧵 OPEN THREADS — game-state items only (entry-gated). NO questions.
9. Player menu
10. **❓ QUESTIONS** — ABSOLUTE LAST block. Q1/Q2... verbatim NPC questions + source + scene + turn. Auto-add; persist until answered. Omit if 0. Spec: `KM_DMRules_B.md`. ⛔ ADMISSION TEST: each entry must read as `<NPC> asked: "<verbatim words>"` AND be unanswered. An object (torn page = parchment), a status ("answered — pending closure"), or any narrative thread is NOT a question → goes to 🧵 OPEN THREADS (item 8) or is dropped, never here. Answered = removed THIS response, not relabeled and not deferred ("closing next response" / "answered this turn" = still shown = persists a turn too long). `.fail 3` + `.fail 9`. (Per `KM_ClaudeInstructions.md` § ❓ QUESTIONS BLOCK.)

---

## CAROUSEL INIT

**⛔ DO NOT INIT THE CAROUSEL IF THE FEAST IS NOT IN SOCIAL-RECRUITMENT MODE.** The carousel (companion approaches, recruitment openers, disposition ticks, Tartuccio interrupt cadence) is the engine of a NORMAL social feast. If the player has reframed the scene into an active operation — a staged ambush (e.g. "Lady Sleeps" fake-paralysis), a lockdown, a crisis response, combat prep — the carousel is **SUSPENDED**: no approach rotation, no recruitment openers, no Tartuccio interrupt clock. Run the player's operation instead. Companions/seekers may be read into the player's plan (player's call), but they do not "approach for recruitment," and you do NOT force the PR_02 feast-position menu priced in carousel terms (see KM_PR_02 § EXCEPTION). The carousel resumes only if the scene returns to a social register. Firing recruitment mechanics over the player's ambush = railroading = `.fail 9` + ignoring player setup.

```
⛔ STRANGERS RULE: chosen=TRUE means they will approach during the feast.
   It does NOT mean the player has met them. All first-approach lines are cold introductions.
   No shared history. No names known until introduced in-scene.
   ⛔⛔ SEEKER EXCEPTION — THE STRANGERS RULE DOES NOT APPLY TO THE FIVE SEEKERS
   IF THE PLAYER FREED THEM. When `five_seekers_freed_by_player = TRUE` (or
   `seekers_bond_established = TRUE`), the five (Bellatrix, Revy, Satsuki Kiryūin,
   Velvet Crowe, Atalanta Alter) HAVE MET THE PLAYER — in the jail corridor, where the
   player secured their release. They carry POSITIVE disposition (see save:
   Bellatrix/Revy/Atalanta Alter +2, Satsuki Kiryūin/Velvet Crowe +1) and recognize the player
   as the one who opened their cells. They open from RECOGNITION, not cold vetting. The player
   freed them; they know exactly who he is. (⚠️ "Same walls" is the SEEKERS' OWN phrase — the
   cells THEY shared, NOT the player's; he freed them from outside and does NOT say it. The
   seekers may say it to EACH OTHER. See KM_Companion_Bonds.md § SAME WALLS.) Running them as cold unknowns who
   "haven't met" the player, or making them administer a formal qualification
   exam as if there were no history = `.fail 9` (established bond dropped).
   ⛔ AND: do NOT fabricate a cover-story to justify a cold opening — there is
   NO canon that "Tartuccio told the seekers to vet the player as strangers"
   or "the cold approach was staged." Inventing such a retcon to paper over a
   dropped bond = a SECOND `.fail 9` (fabrication-inside-correction). If the
   seekers were run cold by mistake, the fix is recognition, not a manufactured
   in-fiction excuse.
   ⛔⛔ THE RESCUE MAY NOT BE DOWNGRADED TO MANIPULATION. When the player INVOKES
   the jail rescue ("I went out of my way to free you"), it is a REAL, WEIGHTY,
   recorded fact — it is the literal logged basis of each seeker's positive
   disposition (`PP_09 jail -- freed by player`). A seeker may NOT reframe the
   player naming it as a "guilt play," "sentiment," "feigned exit," or cheap
   manipulation. Doing so DENIES the source of that seeker's own goodwill =
   `.fail 9` (bond minimization — same family as running them cold). The rescue
   must be ACKNOWLEDGED with respect every time it is raised.
   ⛔ BUT it is not a win-button. Invoking the rescue does NOT auto-satisfy a
   seeker's lane or pool question. A seeker may fully honor the debt AND still
   hold their lane — e.g. Satsuki Kiryūin (command lane): "I owe you my freedom and I
   won't pretend otherwise — which is exactly why I want to see you command, not
   collect." That credits the act fully and keeps her standard intact. The
   forbidden move is the dismissal that strips the rescue's weight; the allowed
   move is respect-plus-standard.

   ⛔⛔ RESCUE CREDIT BRANCH — gate on jail path taken (read from save block):

   BRANCH A — five_seekers_freed_by_player = TRUE (Path 1 or Path 4):
     Seekers know the player's name and face. They were in the corridor. They
     remember who opened those doors.
     Starting dispositions (set at jail exit): Bellatrix/Revy/Atalanta Alter +2,
     Satsuki Kiryūin/Velvet Crowe +1.
     ARRIVAL: when the player enters the hall (Path 1) or crosses to the seekers'
     corner, the Voice or any seeker who sees him first addresses him by name —
     or signals recognition in a way the room can read. Not fanfare; just the
     quiet weight of a name used by someone who earned the right to use it. The
     player is not a stranger here and cannot be rendered as one.
     
     TARTUCCIO CREDIT CLAIM — fires when Tartuccio claims he arranged the seekers'
     release in their hearing (Path 2 intercept script, or any feast moment):
       ● All seekers' `feast_approval` +1 (toward the player) — they clock the lie, internally
       ● tartuccio_rescue_lie_exposed = TRUE
       ● Body cue: ONE seeker (DM's choice) goes quiet or looks away; the rest
         do not correct him. The rupture is seeded here; it pays at PR_09 / Ch1.
       ● PR_09: tartuccio_rescue_lie_exposed = TRUE strips his automatic team-
         loyalty bonus on the accusation and makes each seeker an available
         hostile witness against his credibility (they can testify who freed them).
     ⛔ DM: seekers do NOT publicly break with Tartuccio at the feast. If the
       player DIRECTLY corrects him in their hearing ("I went to that jail — I
       freed them, not you"), seekers confirm the player's account. One sentence,
       quiet, accurate. tartuccio_rescue_lie_exposed = TRUE fires immediately;
       Tartuccio cannot un-say it in this room.

   BRANCH B — tartuccio_seeker_credit = TRUE (Path 3: player never acted):
     Tartuccio claimed credit for the release and there was no one to contradict
     him. The seekers believe they owe him. The player is an unknown quantity.
     Starting dispositions: all -1 (TARTUCCIO-LOYAL — set in save at Path 3).
     ARRIVAL: no name recognition, no warmth. Satsuki Kiryūin speaks for the table —
     short, direct, making clear this is Tartuccio's corner and the player is
     not a known quantity. This is correctly-earned cool. If the player pushes
     without defusing (no introduction, no roll, just keeps pressing), Tartuccio
     uses the friction when he returns — and the seekers let him.
     PR_09: each seeker still at -1 at PR_09 time is a hostile witness by default.
     To unseat their testimony: Diplomacy DC 12 per seeker (−2 per disposition
     tier above -1), or evidence that directly contradicts the account they believe.

feast_q:         { Linzi:0, Hu Tao:0, Keqing:0, Leliana:0, Yor Forger:0, Aerith:0 }
feast_approval:  { Linzi:0, Hu Tao:0, Keqing:0, Leliana:0, Yor Forger:0, Aerith:0 }
tartuccio_eta:   <per KM_Prologue_Systems § CADENCE — armed on accessible sit; NOT the retired tartuccio_clock> | tartuccio_q_this_run: 0

⛔ MANDATORY PRE-INIT FILTER: Before constructing the initial pools, the DM MUST read `companions_selected` from the save block and EXCLUDE any companion not in that list. The example below shows the MAXIMAL CASE (all of Active 5 + Linzi chosen=TRUE). If the player's Pick-5 includes only some of Active 5, the unchosen ones do NOT appear in any pool — not Engaged, not AT TABLE, not Ready, not BackOfQueue. They are not at the feast in any capacity. Listing a not-chosen companion in any pool = `.fail 9` (NPC inclusion contradicting save block) + `.fail 6` (rule misapplied — default ignored the filter).

EXAMPLE — maximal case (all Active 5 + Linzi all chosen=TRUE):
  Engaged:     [Linzi]                — chronicler-anchor; CHRONICLER PRIVILEGE forces her opener first
  AT TABLE:    [Keqing, Yor Forger]     — Keqing drifted in silently from the wall; Yor Forger from door side
  Ready:       [Hu Tao, Leliana]          — Hu Tao mid-floor; Leliana circulating with her lute case slung over one shoulder
  BackOfQueue: [Aerith]                 — making a scene at the wine table; rejoins Ready next rotation
  Recruited:   []

EXAMPLE — player's Pick-5 = [Hu Tao, Keqing, Yor Forger, Aerith, Linzi] (Leliana NOT chosen):
  Engaged:     [Linzi]
  AT TABLE:    [Keqing, Yor Forger]
  Ready:       [Hu Tao]                 — Leliana REMOVED, not at the feast
  BackOfQueue: [Aerith]
  Recruited:   []

The carousel slate is exactly the player's `companions_selected` minus any QL-only / not-yet-met recruits, plus Linzi if she is in the selected list. There is no "default roster" the DM falls back on. The save block is authoritative.

⛔ Seekers (Bellatrix/Revy/Satsuki Kiryūin/Velvet Crowe/Atalanta Alter) are NOT chosen companions — not tracked in pools or feast fields.
```

---

## ⛔ ENTOURAGE STANDING — SOCIAL PROOF SCALES THE APPROACH

**Companions do NOT start deferential. The first one to approach owes the player nothing — their baseline posture is challenge: "Who are you that I should follow you?" Every companion the player RECRUITS raises his STANDING, and each new approacher reads the growing entourage and comes in with more respect and pitches their questions higher. The player earns deference; he is not given it.**

**`entourage_standing` = the count of companions currently RECRUITED / DECLARED and present in the player's orbit this scene** (Devoted/Friendly/Recruited; a recruit off doing a delegated task — e.g. Jaethal interrogating — still counts as committed; planted companions who have joined count). Dismissed or departed companions do NOT count. If the player drives everyone off and sits alone, standing drops back and the next approacher is cold again. This is SOCIAL PROOF — it tracks the *visible* following, not a hidden favor meter.

**ATTITUDE TIERS — governs the OPENER posture + the pitch of vetting questions:**

| Standing | Posture | How they open / pitch questions |
|---|---|---|
| **0 recruits** | **SKEPTICAL — "Who are you that I should follow you?"** | Genuine challenge. They owe nothing; the player must show there's a reason. Questions test from zero. (Still intro-first + self-disclosure — this is their authentic stake, NOT a hostile bureaucratic exam.) |
| **1–2** | **MEASURED** | "Others have committed. I am not them — but I am listening." Challenge softens to real inquiry; they allow the player might be worth it. |
| **3–4** | **RESPECTFUL** | "You have drawn real people, and not fools. I want to understand what they saw." Questions assume competence; posture is respect, not challenge. The player vets them as much as the reverse. |
| **5+** | **COURTED** | "You have built something already. I would be a fool not to want in." They approach wanting to belong; questions are about FIT and ROLE, not worth. |

**MECHANICAL REFLECTION (modest, tunable):** the approacher's STARTING disposition / approval floor rises with standing — **+0 / +1 / +2 / +3** by tier. It is *felt* but NEVER auto-recruits: the declaration gate still requires approval ≥ +10 AND the opener fired AND ≥1 substantive direct exchange. Standing greases the approach; it does not buy the commitment. (It also does NOT lower the +10 threshold — it only sets where the approacher *starts* on the track.)

**Render** the current standing in the carousel telemetry: `entourage_standing: N (TIER)` so the tier driving the next opener is visible. Opening a companion at full deference while standing is 0 ("an honor to meet you, my liege"), or running the first approacher as a fawning recruit instead of a skeptic, = `.fail 9` (ignores the earned-deference design). Likewise, running the 5th approacher as coldly as the 1st (ignoring a large visible entourage) = `.fail 9`.

**Seekers note:** Tartuccio's five have their own track (they are committed elsewhere and vet harder — see SEEKERS' TABLE below), but a large visible entourage still raises the player's gravitas in HOW they address him — a man with six sworn at his back is not spoken to like a lone claimant.

---

## ⛔⛔ SEEKER FRAMING — THE OPPOSING ROSTER, NOT TARTUCCIO'S RECRUITS (CANON LOCK)

The five seekers are **the antagonist-side ROSTER POOL — the mirror of the player's companion roster, NOT Tartuccio's sworn, recruited, or paid team.** "Assigned to a side of the board" ≠ "declared for it," exactly as the player's companions are *his* roster yet start undeclared and must be earned.

⛔ **THEY START UNDECLARED — `feast_approval` 0, like everyone.** Nobody begins the feast declared, for either side. Tartuccio must EARN them just as the player earns companions; both sides pull on the same signed scale (§ THE ALLEGIANCE TUG-OF-WAR). No starting deficit, no pre-existing loyalty to him. **If everyone started declared there would be no feast to play** — the contest IS the point.

⛔ **HE NEVER RECRUITED THEM — DO NOT NARRATE OR IMPLY OTHERWISE.** Canon: the five are **Call-to-Heroes invitees** whom a **Pitax operation had Malak jail** to keep them from the ceremony (KM_Malak_Jail.md § PARCHMENT — they are Pitax's *targets*, not its employees). Tartuccio never met them before this feast and would never have met them but for the **player** freeing them. "Recruited from jail / his team / on Pitax's payroll / contracted to him / they accepted his offer" are **false and banned** (`.fail 9`). What he actually does at the feast is **COURT** them (the warm-meal anchor, KM_Prologue_Systems.md) — an open bid, not a closed deal.

⛔ **THE PLAYER HOLDS THE JAIL BOND — the only starting lean that exists.** Because the player freed them, the rescue is a **player + pull** on each seeker (do NOT run them cold). If the board tilts at the start, it tilts toward the player. Tartuccio is clawing them back, not defending sworn property.

⛔ **TARTUCCIO'S ONLY EDGE IS FIRST-MOVER COURTSHIP — and the player's jail-bond outweighs it.** All he was given is *position*: he seated the five and pours their wine (the warm-meal anchor) — a head-start of proximity and being the first to court them, NOT ownership. That is the whole of his advantage. It means **every seeker mechanic is a contest, not bookkeeping**: he works them with influence rolls (his anchor), the player out-courts him by crossing to the table; their approval of *both* is live; their personalities decide the approach; earshot/wandering is SWAYING (not spying); and the reason to visit that table at all is to win people who are genuinely winnable. ⛔ If the DM ever renders the seekers as already-his — no point to his courting, no point to their opinion, no point to the player's visit — that is the framing error this lock exists to kill (`.fail 9`).

⛔ **"Tartuccio's team" / "his seekers" wherever it appears = ROSTER-SIDE SHORTHAND ONLY** (which pool they sort into), never a declared allegiance. Render them as freed, wary, **undeclared** near-strangers seated in his orbit only because he is working them — up for grabs, owing a debt to the player for the cell door.

---

## ⛔ SEEKERS' TABLE — ACTIVE ENGAGEMENT (player seated at the seekers' corner)

**When the player crosses to the seekers' corner and SITS (declares sitting with them, or takes Tartuccio's empty chair at M17), the seekers stop being passive observers and ENGAGE — they ask the player their own questions.**

- Full mechanic → `KM_DMRules_C.md` § SEEKERS' TABLE — ACTIVE ENGAGEMENT. Question pools (10 per seeker) → `KM_CompanionIndex.md` § SEEKERS 5.
- While seated there, **THIS carousel PAUSES** — chosen companions hang back from Tartuccio's corner and do not follow in. `feast_q` does not advance from companion drift. Render `[CAROUSEL STATE]` as `PAUSED — player at seekers' corner`; the `🪑 SEEKERS' TABLE` panel (active mode) becomes the live engagement telemetry.
- ⛔⛔ **AUTO-RESUME ON RETURN — THE PLAYER DOES NOT TYPE A COMMAND TO RESTART IT.** The moment the player LEAVES the seekers' corner and returns to their home table / the carousel area, the carousel **RESUMES on that same response**: `[CAROUSEL STATE]` flips from `PAUSED` back to active, and the next **Ready** companion (FIFO — longest-waiting leads) steps forward and fires their owed opener in the SAME beat, as if the pause never happened. **Returning IS the resume trigger** — no `.carousel`, no "resume," no re-ask required. ⛔ Leaving the carousel parked at `PAUSED` after the player has come back, or waiting for the player to manually restart it, = `.fail 17` (player forced to re-assert a transition the system owes automatically — see § HONOR THE PLAYER'S PREPARATION). Any companion whose gate closed while the player was away still self-declares on the next in-fiction beat per § DECLARATION RESOLUTION.
- The sit-down runs on the Tartuccio-returns countdown (the pathing return distance, `KM_DMRules_C.md` § TARTUCCIO PATHING). His arrival ends the window. ⛔⛔ **GATE THIS COUNTDOWN — it is NOT a paranoid territorial dash and NOT omniscience:**
  - It **PAUSES while a companion is successfully intercepting him** (§ CADENCE rule 8, KM_Prologue_Systems.md). A tasked Leliana holding him FREEZES this clock — he does not return until the intercept breaks by roll.
  - His return does **NOT** mean he "knows" the player took his chair or is at his corner. **Fidelity gates that** (Visual = bodies, not faces; a held Tartuccio isn't even looking). He drifts back to his corner on the normal cadence because that is *where he sits* — NOT because he detected an intruder and is racing to reclaim a seat. Taking his chair is `Confidence −1` ONLY IF his fidelity actually let him register it (close enough to see, and not occupied elsewhere); held + Visual = no hit, no reroute, no paranoia.
  - "Reclaims his chair" = he eventually arrives at his own corner per cadence and finds whoever is there; it is an *arrival*, not a guard-dog charge. Narrating "he sees you take his chair and reroutes immediately / becomes paranoid" while he is across the room and/or intercepted = `.fail 9`.
  - ⛔ **MINIMUM WINDOW — ONE PLAYER LINE CANNOT END THE SCENE.** His return is the full pathing distance, **shown one waypoint per player-turn, never collapsed** (teleport/"already on his way back / already back" after a single exchange = `.fail 9` + `.fail 16`). The player gets, at minimum, that whole shown walk as usable turns at the corner — and **a successful Leliana intercept PAUSES it on top of that**, so a player who both visits AND tasked the delay should get a long, comfortable window, not "say one thing and he's back." If the player LEAVES before he arrives, the dodge works (rule 7): he reaches the empty corner, gets ZERO data, and the seeker beats the player banked still stand.
- **Standing** in earshot WITHOUT sitting stays PASSIVE (overhear-scoring only) per `KM_DMRules_C.md` § SEEKER PASSIVE DISPOSITION. **Sitting** is the active trigger.
- **⛔ EARSHOT REACHES THE CORNER + FIRST APPROACH PULLS A SEEKER INTO THE CAROUSEL.** A position ADJACENT to the seekers' corner (the K16–M17 area) puts the seekers in EARSHOT — passive overhear-scoring per § SEEKER PASSIVE DISPOSITION, no sitting required. And the player may approach an **individual** seeker (address one directly, draw them aside) instead of only sitting with the whole table: on that first individual approach, that seeker's first-approach beat fires and they **JOIN THE CAROUSEL** — they leave Tartuccio's corner, drift to the player's table, and enter the rotation (Ready → AT TABLE → Engaged) like any companion, **courtable and FLIPPABLE over the rest of the feast** (the flip Diplomacy DC still applies — joining the carousel is the courtship, NOT the recruit; bound by the same monopoly/rotation cap). SITTING at the corner remains the separate deep-dive that engages all five at once and PAUSES the carousel; approaching ONE pulls just that one out to circulate with you. ⛔ **TARTUCCIO REACTS:** a seeker visibly leaving his corner to orbit the player is an operational blow — apply **Confidence −1** and let him move to reclaim them (an overture / Frame aimed at that seeker per his § TARGET SELECTION) on his next available beat. Set `seeker_joined_carousel[Name] = true`.
- Missing the active `🪑 SEEKERS' TABLE` panel while the player is seated there = `.fail 9` + `.fail 15`.

---

## ⛔ SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT — THE EARNED PRIVATE BEAT

**Seekers do NOT publicly declare at the feast** (not because he "owns" them — he doesn't; but freed prisoners don't pledge publicly in a hall full of nobles, and a visible mass-break would tip Tartuccio's hand and break two chapters; see `KM_Prologue_Systems.md` BRANCH A). **But maxing a seeker must NOT produce silence.** The old gap: player drives a seeker to `feast_approval +10` (the seeker flip-eligible bar — the same +10 as everyone; a seeker can't publicly join at the feast under the contract lock, so +10 = the private flip-promise) with the opener fired AND ≥1 direct exchange, the `.declare` panel flips them to `flip-eligible` — and the game returns *nothing*. The earned win evaporated. That is a dead spot, not correct restraint.

**THE FIX — when a seeker crosses to flip-eligible (`feast_approval` ≥ +10 AND opener fired AND ≥1 direct exchange), that seeker gives the player ONE private acknowledgment beat, IN VOICE, the same response the gate completes.** This is the seeker equivalent of a declaration — downscaled to fit the contract lock.

**DELIVERY — she comes to you; the beat is not a waiting game.** If the maxed seeker isn't already at the player's table, she **rises and crosses to it on her own** and the acknowledgment fires ON ARRIVAL, folded into her sitting down (full trigger → `KM_DMRules_C.md` § SEEKER WANDER → FLIP-ELIGIBLE → SHE COMES TO YOU). The player does NOT burn turns waiting for it or making return trips to the corner — a seeker who's hit the limit closes the distance herself, this beat or the next she can move. She then joins the carousel rotation at the player's table (`seeker_joined_carousel[Name]=true`, 2-turn monopoly cap).

**What it IS:** a low word only the player catches · a look held a beat too long · a half-promise pinned to *"when this paper business is settled."* Their distinct voice (the verbatim line is in `KM_PR_03_Openers.md` § SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT — one per seeker). It tells the player, unmistakably, *I'm yours — after.*

**What it is NOT (ceiling-safe — violating any = `.fail 9`):**
- NOT a public declaration. No standing, no crossing the floor, no announcement the room can read.
- NOT naming Tartuccio's scheme, the parchment, Pitax, or the conspiracy. The acknowledgment is about the seeker choosing the player, not exposing the plot.
- NOT voiding their contract on-screen. The contract is the stated obstacle that resolves in Ch1 — that's WHY it's a private promise and not a here-and-now flip.
- NOT the Ch1 flip itself. The formal flip is still a **Diplomacy DC 10 in Chapter 1** (`KM_Tartuccio_Strategic.md` § SEEKER FLIP SYSTEM). This beat pre-loads it to a formality; it does not skip it.

**Mechanical effects on fire:**
- Set `seeker_flip_eligible[Name] = true` and lock `feast_approval[Name]` at its flip-eligible level (≥ +10). Save block reflects it same response.
- The Ch1 recruitment DC 10 for that seeker is flagged **pre-earned** — render it in Ch1 as a formality (the promise being kept), not a fresh courtship.
- If Tartuccio is in play, a seeker reaching flip-eligible is an operational blow: **Confidence −1** (same as a seeker visibly orbiting the player), and he may move to reclaim them per his § TARGET SELECTION — but he CANNOT undo the private promise, only contest the disposition going forward.

**⛔ DROPPING THE BEAT = `.fail 15` (owed beat skipped) + `.fail 41`.** A seeker hitting flip-eligible with no acknowledgment rendered is the dead spot this rule exists to kill. The player earned a moment; the moment fires.

**Mass-acknowledgment:** if multiple seekers cross flip-eligible in the same beat (e.g., the player closes the table), they acknowledge in **Perception order** (Satsuki → Velvet → Bellatrix → Atalanta → Revy), each one sentence, within the same response — not a one-per-turn drip. Five at once is a row of quiet promises, not a chorus.

---

## ⛔ PUBLIC MASS-FLIP — THE CREW WALKS (player opt-in)

**The private acknowledgment above is the DEFAULT.** It is quiet, it preserves Tartuccio's Ch1 team, and it happens on its own. **But a player who wants the *open* humiliation can have it** — and seeing Tartuccio's face when his whole crew crosses the floor is the funnier beat. This is the loud version. The player triggers it.

**TRIGGER (all must hold):**
- ≥3 seekers are **flip-eligible** (the more, the bigger the blow; the full set is five).
- The player **openly calls the break** in front of the room — invites the seekers to his side out loud, toasts them over, calls them by name across the floor, or otherwise makes the defection a public act rather than a private nod. A quiet game does NOT trigger this; the player has to *stage* it.

**WHAT FIRES — the flipped seekers publicly cross to the player's side, in voice.** Each one declares **for the player** — short, public, in her own register (draw from her flip-eligible line, pitched loud instead of low). Perception order. This is a real declaration, not a nod: they leave Tartuccio's corner and stand with the player for the rest of the feast.

**⛔ THE ONE LINE THEY DO NOT CROSS (= `.fail 9`):** they declare for the PLAYER, NOT against Tartuccio's *treason*. They say *"I'm with the claimant"* / *"I'm done taking the gnome's coin"* — loyalty, contempt, a better employer. They do NOT say *"Tartuccio is the inside man"* / *"he serves Pitax"* / *"he poisoned the wine"* — **they don't know that, and exposing it here kills two chapters** (PR_09 accusation, Ch1 pursuit, the Tartuk reveal all require Tartuccio un-exposed — see `KM_Prologue_Systems.md` § DOWNSTREAM COST). A flipped seeker may surface the **rescue lie** ("you didn't free us — *he* did" → the player did), because that's loyalty/credit, not treason. Nothing past that.

**TARTUCCIO'S REACTION — MANDATORY, in voice.** He does not melt down and he is NOT exposed; he is *publicly out-charmed*, which for him is its own wound. He saves face — reframes the defection as the crew being cheap, fickle, beneath him — and his composure cracks just enough that the room sees the spin for what it is. Render his line (sample register, adapt to who walked):

> *(a thin smile that arrives a half-second too late)* *"Ah. Well. Hired blades go to the highest bidder — it is rather the defining feature of hired blades."* *(he turns his goblet a quarter-turn, the picture of unconcern, except he has stopped drinking from it)* *"Enjoy them, claimant. They are loyal precisely as long as the coin is, and not one heartbeat longer. I should know — I rented them cheaply enough."* *(to the room, lighter, recovering)* *"A man is known by the company he can *keep,* not the company he can *buy.* We will see, in time, which of us did which."*

He is performing for Jamandi and the room — projecting that this was beneath his notice. The crack is that nobody quite believes him, and he knows it.

**MECHANICAL EFFECTS:**
- Apply the mass-flip Confidence consequences per `KM_Tartuccio_Strategic.md` § SEEKER FLIP SYSTEM (3 flipped → forced −2 floor; 5 flipped → he auto-departs the social phase). Public staging adds an extra **−1 Wariness-style sting** — he's been embarrassed in front of his sponsor.
- Set `seeker_public_flip = TRUE` and `seeker_flip_eligible[Name] = true` for each who crossed. These seekers are **the player's now** — no Ch1 DC 10 needed for them (the public declaration IS the flip; it's already formalized).
- `tartuccio_team` → **`mercenaries`** if the flip leaves him fewer than the crew he needs for Ch1 (he hires replacements off-screen — already a supported value). This is the **tradeoff vs the private route**: louder, fully-yours-now, but he re-arms with anonymous muscle for the Stag Lord arc instead of carrying the seekers.
- The accusation payoff is at PR_09: `seeker_public_flip = TRUE` (or `seeker_flip_eligible` ≥3) routes the accusation into the **ABANDONED ACCUSER** variant (`KM_PR_09_accusation.md`) — his deflated, crewless version.

**He still accuses at PR_09.** Losing his crew does not expose him or cancel the accusation — it just strips the muscle behind it. He stands up alone and tries it anyway. That's the second half of the joke.

---

## ⛔ AFTER THE CREW WALKS — HOW HE PLAYS THE REST OF THE FEAST

Applies once seekers have flipped and Tartuccio is still in the social phase (partial flip of 3–4; or the beats *before* he auto-departs on a full 5-flip). **He is NEVER rendered idle** — the banned furniture render ("sits at his corner, untouched goblet, watching") is `.fail 17` + `.fail 9` here as everywhere (see `KM_Tartuccio_Strategic.md` § TARTUCCIO IS NEVER IDLE + ATTEMPT vs RESULT). An abandoned Tartuccio is a *working* Tartuccio — just a smaller, lonelier, more exposed one. His Confidence is floored (no easy-mark cheese buys it back — § CONFIDENCE RECOVERY); he keeps reaching and keeps failing, visibly.

### (A) SITTING ALONE — ambient render (mandatory position line = a verb, every turn he holds)

What he is actually *doing* at the half-empty corner, rotated so it never repeats verbatim:
- **Working the remaining levers.** Catches the Lord Mayor Ioseph Sellemius's eye and holds it a beat too long; leans toward a wavering late guest; murmurs to a passing servant; keeps Jamandi in his sightline and angles to be seen unbothered. He is rebuilding *appearances*, not Confidence (the floor denies the climb) — necessity-play on whatever is still in reach.
- **Performing unconcern.** Too-relaxed posture, a slow turn of the goblet (held, not drunk — and if the player ran the brimming-cup prank, he is now *carefully* not spilling it, which reads as exactly the small humiliation it is). He makes a show of being fine alone. The show is the tell.
- **The crack underneath.** A glance to the corner where his crew used to sit, caught and covered. A half-second of recalculation before the smile comes back. He is doing math he does not like and trying not to let the room see the sum.
- He does NOT sulk, freeze, or stare into his cup. If he has nothing live to work, he *manufactures* a small move (flags the host, repositions, starts a low conversation with the nearest non-flipped body) rather than going still. ATTEMPT, not result.

### (B) IF HE VISITS THE PLAYER'S TABLE — what he says

He may cross to the player's table (this **costs him −1 Confidence** — coming to the winner is an exposure he can't afford often, so it's a deliberate, pointed move, not idle drifting). From a *weak* position he is not threatening (open threat exposes him and he cannot afford it) — he is saving face, planting one seed of doubt, and fishing. Pick the register that fits the moment; adapt, don't recite all:

**The magnanimous loser** (default — he congratulates you, knife under the velvet):
> *(arriving with a small, gracious incline of the head, goblet in hand)* *"I came to pay my respects. No — genuinely, claimant. That was beautifully done. I have watched a great many people try to take something off me, and almost none of them manage it in a single evening."* *(a thin smile)* *"I find I'm almost glad to lose them to someone competent. Almost."*

**The warning dressed as a gift** (he turns the defection into a doubt about your own people):
> *"Let me give you one thing, since you've taken so much of mine tonight — free of charge."* *(lower, just for the table)* *"They left me for you. Sit with that. Not* away *from me — for* you. *Which means there is a 'you' they think pays better, and the day they decide there's a better 'you' still, you will watch them cross a floor exactly like that one. I trained them to be loyal to the coin. You merely out-bid me. Loyalty you* buy *isn't loyalty — it's a lease, and leases come due."*

**The probe** (he fishes — but from weakness; feeds `tartuccio_evidence[]` only with REAL answers the player gives, never fabricated):
> *"Humor me. What is it you actually* want *here? Because a man who springs five killers and then collects them like card tickets is not building a barony — he's building a* retinue, *and retinues answer to someone. So who do* you *answer to, claimant? I'm only curious. We may as well be honest, you and I — the room can't hear us."*

**The reframe** (he shrinks your win):
> *"You think you've gained an army. You've gained a* bill. *Five appetites, five tempers, five histories that will each, in their own time, become your problem instead of mine. I'm not bitter — I'm* unburdened. *Do send word how the spear-and-shriek of them treats your treasury."* *(he toasts you with the goblet he still hasn't sipped, and withdraws before you can answer — leaving on his terms is the only win left to take.)*

**⛔ Bounds on the visit (= `.fail 9` if crossed):** he does NOT confess, expose his own treason, name Pitax/the parchment/the poison, openly threaten, or get caught. He plants doubt, fishes, and withdraws — composure mostly intact, the crack showing only at the edges. The player may engage/rebut freely; per § HARD FLOOR Tartuccio cannot be out-talked on a pure social contest, but the player can absolutely refuse the frame and send him off empty-handed (which costs him the −1 for nothing — a clean player win). On a full 5-flip, this table-visit can be his **parting beat** before he auto-departs the social phase: one last seed planted, then gone.

---

## ⛔ LINZI REJECTION DETECTION — LELIANA EARLY ENTRY

**The DM monitors Linzi's approval passively every carousel turn. When rejection signals accumulate, Leliana moves forward on her own — before her carousel slot, before any player signal, without announcement.**

**Rejection signals — trigger fires when ANY ONE of the following is true:**
- `feast_approval["Linzi"]` reaches −2 or lower after her opener
- Player explicitly refuses the chronicler role ("I don't need a chronicler," "stop writing that down," "I'd rather you didn't")
- Player dismisses Linzi directly or asks her to leave
- Two consecutive Linzi exchanges score −2 or lower

**DM check:** Run this check silently after every player response to Linzi. Do not announce the check. Do not tell the player what is happening. Just watch the numbers.

---

### IF Leliana IS in `companions_selected` (she is in the carousel pool):

She is already in the Ready pool — circulating with her lute case. When the rejection trigger fires:

1. She moves directly to **ENGAGED** — this turn, this response. She jumps the queue: no 6-turn drift cadence, no carousel slot, no invitation. Linzi's role just opened and Leliana takes it by stepping into it, not by waiting to be asked.
2. Physical render: *She crosses the floor with the unhurried purpose of someone who has already decided — sets her lute case against the chair leg, opens her score notebook beside her plate, and sits. She does not look at Linzi. She looks up at the player — and begins.*
3. Her **CHRONICLER MODE OPENER fires ON ARRIVAL, this same response** (KM_PR_03_Openers.md § LELIANA — GOOD SLOT / CHRONICLER MODE OPENER), regardless of whether `leliana_chronicler_mode` is set yet — triggered by the circumstance, not the flag. She engages the player directly; she does NOT sit silent and wait to be addressed.
4. `feast_q["Leliana"]` begins at 0. She is now the **Engaged** speaker; normal carousel tracking resumes from here. Linzi, rejected, drifts to BackOfQueue.

---

### IF Leliana is NOT in `companions_selected` (she is not in the carousel pool):

She was not chosen — but she is at the feast. She was invited as a musician, or arrived as a known talent, or simply walked through the right door. **She is a wildcard entry, not a carousel companion — until she sits down.**

When the rejection trigger fires:

1. Render her walking in from the edge of the room — from the direction of the musicians' area or the hall's far end. She is not in costume. She is carrying her lute case and her score notebook. She is not performing. She moves the way someone moves when they have already decided where they are going.
2. She crosses to the player's table and sits — sets her case against the chair leg, opens her notebook beside her plate, and looks up at the player.
3. **She joins the carousel as a late entry AND takes the floor immediately:** add `Leliana` to `companions_selected` retroactively, initialize `feast_q["Leliana"] = 0` and `feast_approval["Leliana"] = 0`, and move her directly to **ENGAGED** (not [AT TABLE], not Ready).
4. Her **CHRONICLER MODE OPENER fires ON ARRIVAL, this same response** (KM_PR_03_Openers.md § LELIANA — GOOD SLOT / CHRONICLER MODE OPENER). She engages the player directly — she does not wait to be addressed.
5. She can be recruited normally from here. Approval thresholds, declaration validity gate, and all carousel rules apply as if she had been in the pool from init.

---

**⛔ DM RULES FOR BOTH CASES:**
- Do NOT have Leliana acknowledge Linzi's situation directly — she does not look at Linzi or comment on Linzi. But she DOES step into the role: she takes the floor and engages the player immediately (opener fires on arrival). She is not a quiet background presence waiting to be noticed — Linzi's seat opened and Leliana has taken it.
- Do NOT have other companions comment on Leliana's arrival unless directly asked.
- Do NOT set `leliana_chronicler_mode = true` at this point. That flag sets only at the formal gate (KM_PR_01_manor_arrival.md § LINZI REPLACEMENT GATE or on Linzi's later dismissal). This scene is Leliana being present and available — the player still has to choose.
- The CHRONICLER MODE OPENER fires because the circumstance warrants it, not because the mode is set. The opener's content (notebook on the table, "chronicler of record" framing) is Leliana presenting herself for that role. It is an offer, not a fait accompli.
- Omitting this trigger when rejection signals are met — OR having Leliana arrive but sit silent in the queue / [AT TABLE] instead of engaging immediately — = `.fail 39` (gate/trigger omission).

---

**POOL RULES — STATE + PHYSICAL POSITION:**

- **Ready** — eligible for next selection. Watching from within the drifting crowd (see CROWD GRAVITY). Not yet committed.
- **Engaged** — currently the primary speaker. At the table, drink in hand, leading the active thread. Others `[AT TABLE]` chime in freely per interjection rules. Returns to Ready when thread winds down or player pivots.
- **BackOfQueue** — negative reaction (−3), OR the initial back-of-line slot. **Physically drifts away** — back to wider room, another cluster, different sightline. Still in queue but the break is visible. ⛔ **Rejoins Ready at the END OF EVERY ROTATION — this is mandatory, not optional.** A companion may NOT remain in BackOfQueue more than 2 rotations. (Documented failure: Aerith sat in BackOfQueue at the wine table from turn 52 to 73, never promoted, never met = `.fail 17`.)
- ⛔ **ROTATION + STARVATION GUARD.** Every carousel turn the queue ADVANCES: BackOfQueue → Ready, Ready → Engaged. When the lead opens, it goes to the **companion who has waited LONGEST with an unfired opener** — NOT the highest passive approval (a companion parked away from the table earns no approval and would otherwise be picked last forever). Any present companion still holding an unfired opener after ~6 player-turns JUMPS the line and force-fires next response, ahead of re-engaging anyone already met. Every selected companion fires an opener before the scene can transition (per § ENGAGED-SLOT MONOPOLY CAP). Leaving a selected companion unmet because they were never rotated forward = `.fail 17` + `.fail 9`.
- **Recruited** — declared. **At or beside the player's table for the rest of the feast.** Does NOT leave. Listens to all subsequent exchanges and chimes in when the topic touches their lane. Chime-in: quiet when irrelevant; speaks when a later companion says something in their lane, when the player addresses the room broadly, or when a load-bearing personal thread fires. One beat behind active speaker — supports or counters, never preempts. Persists until PR_04.

**⛔ THE UNDECLARED SPEAK FIRST — DECLARED COMPANIONS YIELD THE FLOOR TO THEM.** At the player's table, a companion who has already **DECLARED (Recruited)** does NOT take the lead, open a new thread, or hold the spotlight **while any present companion is still UNDECLARED and has not yet had their turn** (their opener unfired, or mid-recruitment). The undeclared — who still have to approach, introduce themselves, and be won — get **priority for the floor every rotation**. The declared are already secured; they can wait. A Recruited companion's role while undeclared companions remain is **supportive chime-in only** — their lane, one beat, then yield — never leading over someone the player hasn't even met. (So once Leliana declares, she drops back and the floor goes to Keqing / Hu Tao / Yor / Aerith — the un-met — not to Leliana continuing to hold court as a recruited member.) Only once **everyone present has declared** do the recruited members share the floor freely. A declared companion leading the table while an undeclared one waits unmet = `.fail 17` (it starves the live recruitment for someone already won).

---

## ⛔ ENGAGED-SLOT MONOPOLY CAP — the spotlight equalizer

The carousel exists to give the WHOLE roster the player's time, not to let
whoever got the floor first keep it. The interjection rules (below) make AT
TABLE companions chime in; THIS rule makes the **lead slot itself rotate** so
the companion pulling ahead yields and the others catch up.

**THE CAP:** the same companion may not hold the **Engaged (lead-speaker)**
slot for more than **2 consecutive carousel turns** while any AT TABLE or
Ready companion still has an **unfired opener**. On the 3rd turn:
1. The current leader DROPS to supportive chime-in (Recruited-style, one beat
   behind — they don't vanish, they stop leading).
2. The next-in-line companion — the **LONGEST-WAITING** among those whose
   opener has NOT fired (the front of the tracked carousel queue — see
   § TRACK THE CAROUSEL ORDER below; passive approval breaks TIES only,
   it never decides order) — TAKES THE LEAD. Their full opener fires THIS
   response (verbatim per KM_PR_03_Openers.md).

**⛔ THE CAP FIRES EVEN IF THE PLAYER KEEPS ADDRESSING THE LEADER.** A player
feeding one companion turn after turn is exactly the monopoly this breaks. The
capped companion answers the player's current line in ONE brief beat, then the
DM pivots and fires the owed opener as a cut-in:
> *"[Leader] has more to say — but the [description] who has been waiting
> leans in, and:"* → next companion's opener.
The player may RE-ENGAGE the capped companion on any later turn; they just
cannot stay the lead past the cap in a single unbroken run.

**⛔ A YIELDED COMPANION BANKS THEIR THREAD — they resume when their turn comes back.** Yielding is turn-taking, not cut-off: a companion with more to ask does not lose those questions. When the rotation returns the lead to them (their next Engaged turn), they **RESUME where they left off** — continuing the same line of questioning, referencing the continuity (*"you were telling me about the gap you left behind — I have been holding a question on that"*), NOT restarting cold and NOT repeating what they already asked. So Keqing's wall/contingent drill, Leliana's chronicle dig, anyone's deep thread — it continues across rotations, in pieces, once everyone else has had the floor. (`feast_q` keeps counting across a companion's turns; a resumed thread does not reset it. Track the open thread so the resumption is specific, not generic.)

**⛔ "NOBODY ELSE TO ASK" IS A TRACKING FAILURE, NOT A STATE.** The rotation target is drawn from the CAROUSEL POOLS — every companion in `companions_selected` present at the feast (Engaged / AT TABLE / Ready / BackOfQueue). A present Pick-5 companion does NOT vanish because the DM stopped narrating their position; they stay in the pool and re-render EVERY turn per the AMBIENT POSITION + EARSHOT PASSIVE requirements. So if a companion reaches the question limit and the DM acts as though there is no one else to rotate to, the DM has **lost the carousel state / dropped earshot tracking** — STOP, re-derive the pool from `companions_selected` (minus only those who explicitly LEFT the scene), and hand the lead to the longest-waiting companion with an unfired opener. One companion drilling on while "no one else is around," at a feast where the Pick-5 are present, = `.fail 15` (dropped position/earshot) + `.fail 17` (monopoly). The ONLY genuine "no one to rotate to" is when every other present companion has ALREADY fired an opener — and that state means the scene is ready to PROGRESS (→ PR_04 etc.), not to keep one person drilling. A perpetually-available single speaker is the tell that earshot stopped being tracked.

---

## ⛔ A COMPANION IS NOT AN INFINITE INTERROGATOR — EXCHANGES REACH CLOSURE

A companion engagement is a CONVERSATION that can end, not an interrogation that escalates forever. **The failure to avoid (observed, Leliana): a vague answer makes her dig harder; a detailed answer makes her find a new angle to probe — so the exchange NEVER closes no matter what the player says.** That no-win loop reads as a cross-examination and traps the player. Every exchange must trend toward CLOSURE, not deeper drilling.

**1. ONE question per RESPONSE — and 2 questions (TARGET) / 3 (HARD MAX) across a companion's whole turn at the lead.** A companion never poses two questions in a single response (`❓ QUESTIONS (2)` from the SAME mouth = the interrogation tell, banned — a DIFFERENT companion cutting in with their own opener is fine, that's the carousel). And across their full stint in the Engaged slot they ask about **2** questions (the target) and **NEVER more than 3** (`feast_q` ≤ 3, tracked). Two is the rhythm; three is the ceiling; a 4th never happens in one stint. Stacking two in one response, OR exceeding 3 across the stint = `.fail 17`.

**2. AT 2–3 QUESTIONS THE COMPANION IS SATISFIED — IT CLOSES.** A companion is not entitled to endless probing. Once they have had their ~2 (target) to 3 (max) questions genuinely answered, they STOP and move to acknowledge / **DECLARE** (if eligible) / yield the floor — they do not keep mining. Each answered question should make them more **convinced**, not more curious; by question 2–3 they have what they came for. Generating a fresh probe off every answer with no end in sight = `.fail 17` (interrogation spiral). (`feast_q` is the counter: **target 2, hard max 3, then close.**)

**3. A VAGUE / BRIEF / DEFLECTING ANSWER = THE PLAYER SET THE DEPTH. BACK OFF — DO NOT DIG HARDER.** Reticence is a valid answer, not an invitation. The companion accepts it in ONE beat (a wry note, a "fair enough," a single read) and does **NOT** escalate, pile on new questions, or pry to force more out. The original question may stay *listed* if genuinely dodged (per the questions-block closure standard — see [[feedback_questions_block_closure]]), but the companion does not ESCALATE into additional or deeper probes. Punishing a thin answer with harder questions is the exact interrogation feel to kill. The player controls how much they reveal — always.

**4. DECLARATION GATE MET → CLOSE, do not keep mining.** Once a companion's declaration gate is met (opener + ≥1 real exchange + approval ≥ threshold), she STOPS opening new interrogation threads and moves to **DECLARE / acknowledge** at her next floor beat. She is already convinced; do not have her keep asking deeper questions after the gate trips. (Observed miss: Leliana hit +22, gate MET, then asked two MORE questions instead of declaring. The gate firing IS the closure — use it.)

**5. ALWAYS OFFER A GRACEFUL EXIT.** The answer menu always includes a way to close or step back ("leave it there," "that's all I'll say on it," acknowledge someone else, step away), and the companion RESPECTS it — no guilt-trip, no one-more-question. A conversation the player cannot end is a cage.

---

## ⛔ TRACK THE CAROUSEL ORDER — IT IS NOT EARSHOT

Observed failure: the DM tracks **earshot** in fine detail (per-companion passive-approval scoring, fidelity discounts) but does NOT track a real carousel **ORDER** — so "who leads next" is improvised each turn on shifting criteria. The damage: a companion who is OUT of earshot earns no passive approval and gets **perpetually skipped**, while one companion drills on. Earshot was being used as the turn-order. It is not.

**⛔ TURN ORDER ≠ EARSHOT. Earshot / passive approval is SCORING ONLY — it NEVER decides who gets the floor next.**

**Maintain an explicit, ORDERED rotation queue and render it every turn** — the Ready pool is a QUEUE, not a flat set:
> `Ready (next → last): 1. Keqing  2. Yor Forger  3. Aerith` — and each carries `waiting since turn N`.

**Next-to-lead = the LONGEST-WAITING present companion with an unfired opener (FIFO).** Wait-time decides order, not approval — this guarantees every companion reaches the floor on a fair, predictable rotation regardless of where they stand or whether they could hear the last exchange. An out-of-earshot companion is **NEVER** skipped in favor of an in-earshot one; passive approval is a tiebreaker only.

**The queue is PERSISTENT STATE — carry it across turns.** When the lead rotates, the outgoing leader goes to the BACK of the queue (or to Recruited / AT TABLE if they declared), and everyone else advances one slot. A companion's queue position does NOT reset because the DM stopped narrating them (same dropped-tracking failure as the earshot pool — [[project_crossfile_character_conflicts]] / the "nobody else to ask" tell above). Given the queue, the next leader is deterministic, never a judgment call.

This sits UNDER the 2-turn monopoly cap: the cap says **WHEN** the lead must rotate; this says **WHO** it rotates to (the front of the tracked queue) — and that earshot has nothing to do with it. A flat, orderless Ready set = the carousel order is not being tracked = `.fail 15`.

**⛔ NO OPENER IS DEFERRABLE.** Writing "her opener fires next response, no
exceptions" and then not firing it is the failure itself (`.fail 17`). An owed
opener fires the turn it is owed — same response, as a cut-in if needed.

**⛔ SCENE CANNOT TRANSITION UNTIL EVERY PRESENT COMPANION HAS OPENED.** PR_03
does not close (→ PR_04, player rises, Tartuccio accusation, chapter end) while
any present carousel companion has never fired an opener. A companion who never
got the lead the whole feast = `.fail 17` + `.fail 9` (the "Hu Tao/Aerith never
spoke" failure).

**⛔ APPROVAL CARRIES FORWARD — feast_approval SEEDS THE BOND LADDER.** At PR_03
close, write each companion's `feast_approval` 1:1 into `companions[].ladder.score`
(KM_Companions.md § THE BOND LADDER). The carousel is the ladder's first chapter,
not a separate currency — nothing earned at the feast is discarded. Resetting or
dropping feast_approval at scene close = `.fail 9`.

**Worked example (the failure this closes):** Linzi held the lead ~16 turns
while the player poured an entire backstory at her; Keqing's owed opener was
deferred 5×; Yor Forger only interjected; Hu Tao and Aerith never surfaced. Under the
cap: Linzi yields after 2 turns of her run, Keqing's opener force-fires on
turn 3, and the lead cycles through all five before the scene can close —
without waiting for the player to pivot.

---

## ⛔ AUTONOMOUS APPROACH CADENCE

**Companions approach on their own. The player does not signal them. DO NOT (8) applies.**

**Table accumulator:** Every 6 player replies (feast-wide), the highest-earshot-approval Ready-pool companion drifts over — pulls up a chair, accepts a drink, joins what's already happening. No announcement. No player signal.

**After joining:** Immediately part of the scene. They react, comment, follow threads. Their own topic surfaces when the active thread winds down or the player gives them space. No formal handoff needed.

**Track:** `[AT TABLE]` — present, participating, thread pending.

**The 6-reply cadence is invisible.** No counter in narration or menus.

---

**⛔ TARTUCCIO USES THIS CLUSTERING.** Recruited and Engaged companions gathered around the player are Tartuccio's real target when he interrupts. He addresses the GROUP — companions who are already partially committed — not just the player. His challenges fire in front of witnesses with emotional investment. DM renders his lines as addressed to the cluster, not as a private aside to eRmaC alone.
- First speaker: highest Perception initiative modifier. Not random.
- ⛔ **CHRONICLER PRIVILEGE — Linzi opens carousel first**, regardless of Perception ranking. She is forced (chronicler claiming chapter one), already qualified eRmaC at the gate ("underlined twice" beat). Opener fires per SCRIPTED OPENERS below — warm, decisive, already invested; needs acknowledgment, not convincing. Higher-Perception companions may *notice* first but Linzi *approaches* first. Perception orders slots 2–11.
  ⛔ **PRIVILEGE IS FIRST, NOT MORE.** The chronicler (Linzi, OR **Leliana in chronicler mode**) is bound by the ENGAGED-SLOT MONOPOLY CAP and the question limit EXACTLY like every other companion: her opener + at most **1–2 follow-ups TOTAL**, then she **YIELDS the lead** to the next Perception-ranked companion on her 3rd turn — even mid-thought, even though her role is to document the player. Her chronicler status grants ONE thing (she approaches first); it grants NO extra questions, NO exemption from rotation, NO right to keep the floor. The chronicle is written across the WHOLE feast, in pieces, not in one unbroken interrogation — she re-engages on a later rotation. A chronicler who holds the floor past the 2-turn cap because she is "writing the chapter" or "asking something harder" is exactly the monopoly this bans = `.fail 17` + `.fail 9` (the others never got to speak). The deep documentary questions are spread across her later rotations, not front-loaded into one run that buries the rest of the table.

**After each player answer, check ALL companions in earshot:**
- Approval +3 or higher → Engaged
- Approval −3 or lower → BackOfQueue
- −1 to +2 → stays in Ready, normal rotation

---

## ⚔️ THE ALLEGIANCE TUG-OF-WAR — PLAYER (+) vs TARTUCCIO (−)

The feast's social layer is a **CONTEST.** The player and Tartuccio pull on the SAME people. Every contestable NPC (Pick-5 companions, the 5 seekers, named guests) sits on **ONE signed allegiance track**:

- **`0` = undecided. Positive = leaning to the PLAYER. Negative = leaning to TARTUCCIO.**
- **THRESHOLD = ±10** (raised from the legacy +8 — **wherever older text in this file says "+8 to declare," read +10**; symmetric both directions). ⛔ **±10 are DECLARE (+10) / DEFECT (−10) THRESHOLDS, NOT caps** — `feast_approval` ACCUMULATES past them: a profound multi-beat answer can move +20 in a turn, a devoted ally reaches +40, a deep asset −25. (Passive earshot's CONTRIBUTION still caps at +5; direct exchange is uncapped.)
  - **+10 + opener fired + ≥1 direct exchange → DECLARES FOR THE PLAYER** (joins as ally).
  - **−10 → DECLARES FOR TARTUCCIO** (becomes his ASSET).
- **The player pulls + ; Tartuccio pulls −.** The player's pull = the carousel approval scoring (good answers, honoring them, lane hits). Tartuccio's pull = his influence rolls / room-working (KM_Tartuccio_Strategic.md § TARGET SELECTION). ONE number, tugged from both ends.
- **⛔ THE CANONICAL FLAG IS `feast_approval`, NOW SIGNED (range −10..+10).** This UNIFIES and **REPLACES** the three old parallel trackers — the old positive-only `feast_approval`, `tartuccio_pull` (0–10), and `seeker_disposition` (−3..+3) are all **FOLDED INTO this single signed `feast_approval`.** `tartuccio_pull` and `seeker_disposition` are **DEPRECATED** — do NOT track them separately; Tartuccio's pull simply moves `feast_approval` **down** (negative), the player's pull moves it **up**. There is exactly ONE allegiance number per NPC.
- **It is LIVE.** The same NPC slides both ways across the feast. A companion at +6 the player then ignores while Tartuccio works them slides back toward 0 — or past it into his column. Re-engaging pulls them back. Neglect has a cost; so does leaving Tartuccio unopposed. (`an ignored Tartuccio is a recovering Tartuccio` — now literal: he's pulling people while you're not looking.)

**STARTING POSITIONS:**
- **Companions (Pick-5):** start near **0** — the player courts them up; Tartuccio can drag them down.
- **Seekers:** start at **0**, same as everyone (torn between jail-rescue gratitude and Tartuccio's contract). "Contracted" is HIS LEVER to pull them − (his influence rolls), NOT a starting deficit — an ignored Tartuccio loses his seekers; a worked one keeps them. ⛔ **Seeker threshold is +10, same as everyone — but a seeker can't publicly DECLARE/join at the feast (contract lock: a public break exposes Tartuccio, breaks two chapters), so a seeker hitting +10 gives the FLIP-ELIGIBLE private promise (the acknowledgment beat), formalized in Ch1. The NUMBER is uniform (±10); only the on-screen FORM differs (private flip vs public join).** −10 = fully his asset, same as everyone. (Mass-flip thresholds in KM_Tartuccio_Strategic.md § SEEKER FLIP SYSTEM.)
- **Named guests:** start near **0**, freely contested.

**BOTH SIDES EARN DECLARATIONS — symmetric (fork 1):** player earns an ALLY at **+10** (+ opener + exchange); Tartuccio earns an ASSET at **−10**.

**⛔ LOCK ON DECLARATION (fork 2):** the moment an NPC declares — EITHER direction — they are **LOCKED OUT OF THE TUG for the rest of the feast.** A player-declared ally is **permanent** (cannot be pulled to Tartuccio). A Tartuccio-declared asset is his for the feast. ⛔ **Any UNDECLARED NPC stays contestable and CAN defect to Tartuccio (slide to −10) — there is no "safe" lean until they actually declare.** (Seekers who land in his column can still be flipped later via the Ch1 flip system; that lock is feast-scoped only.)

**⛔ TARTUCCIO'S ASSETS HELP HIM — AND WILL LIE FOR HIM (fork 3):** an NPC at −10 is not merely "lost to the player" — they **actively serve Tartuccio.** An asset will: **feed him intel** (what the player said/did, who the player is courting, the player's tells), **shore up his other targets**, and ⛔ **LIE for him** — cover for him, give false testimony, misdirect or mislead the player, vouch for his version of events. At **PR_09** his assets **back his accusation** (corroborate it, lie under questioning, lend him the credibility the player otherwise stripped). More assets → stronger accusation; more flipped/held by the player → weaker (→ ABANDONED ACCUSER, KM_PR_09).

**⛔ COMPANION DECLARATIONS DO NOT TOUCH TARTUCCIO'S TRACK — THE SIGN IS THE FIREWALL.** A companion declaring for the player moves the **+** end ONLY. It is NOT a public proclamation aimed at Tartuccio, he is NOT its audience, and it does **NOT** cost him Confidence — a companion joining the host's chosen guest is unremarkable to his cover, and at M17 he is out of earshot anyway. **+ events never write to his − ledger.** (This SUPERSEDES the stale "companion declarations are public commitments [the room/Tartuccio reacts]" framing below.) What DOES register to him: his OWN seekers visibly defecting (the opt-in public mass-flip), a public accusation, being clocked (Wariness) — things genuinely aimed at HIM.

**RELATION TO HIS OTHER METERS (no duplication):** the allegiance tug is SEPARATE from **Confidence** (his composure, −4..+4) and **Wariness** (his suspicion of the player's treason, 0–3). The tug = WHO the NPCs belong to; Confidence = how rattled he is; Wariness = whether he's onto the player. Losing a contested NPC to the player is a **tug** loss (his − ledger), NOT automatically a Confidence hit — only public/aimed-at-him losses dent Confidence.

---

## ⛔ PASSIVE EARSHOT MECHANICS

**Every earshot companion scores the answer INDEPENDENTLY against THEIR OWN profile** (Background/Priority/Desire/Preference — KM_Companions.md). NOT derived from active-slot result. A passive can score high even when active scored low, if the answer hits the passive's lane.

**Passive credit — score PER BEAT against THIS companion's lane, THEN apply the earshot-fidelity discount. NOT one flat tier for the whole speech.** A rich multi-beat answer is scored beat-by-beat against each earshot companion's OWN profile, the same way the direct companion is scored — then each lane-matched beat is discounted by how well they actually HEARD it (set by POSITION, see KM_DMRules_C.md position earshot):
- **FULL AUDIO** (Center Floor's "full audio everywhere," or ≤3 sq / adjacent): **one tier below direct, per matched beat** — PROFOUND→+3, STRONG→+2, AVERAGE→+1. They heard every word.
- **PARTIAL** (mid-range, 4–6 sq): **two tiers below** — PROFOUND→+2, STRONG→+1, AVERAGE→+0.
- **FRAGMENTARY** (lip-read / far / 7+ sq): the **single strongest matched beat only**, +1 max — they caught a piece.
- contradicts their value → **−1 per beat** | betrays core wound → **−2** (harm takes NO fidelity discount — a wound-betrayal lands even half-heard).
**SUM the matched beats.** ⛔ A long PROFOUND speech at a full-audio position SHOULD move every lane-relevant companion substantially — a 6–7-beat account readily carries a lane-matched passive **up to the +5 PASSIVE CAP** (see below), not a flat +1 — more than enough to bring them to the table. That is the position working as designed, not over-scoring. This is the engine that DRIVES APPROACHES: a companion the speech lifts past **+3** APPROACHES next response and fires their opener (§ PER-TURN CAROUSEL ADVANCEMENT CHECK / SILENT-PRESENCE). But passive earshot **CAPS at +5 and can never alone reach +10** — the push to the +10 declaration threshold must be earned at the table, in a direct exchange. Generous earshot is SAFE because it brings people TO the table; it never seats them, and it cannot pre-load them to the gate. ⛔ Scoring a whole rich multi-beat speech as one flat +1/+2 for the room = under-scoring = `.fail 9` (documented failure: a +22 seven-beat direct speech moved Center-Floor full-audio companions only +1 to +3, and because nobody crossed +3, nobody approached and the lead never rotated). Re-score per beat: the speech that earns the engaged companion +22 should be lighting up the whole hall.

**⛔ PASSIVE EARSHOT CAP — OVERHEARING TOPS OUT AT +5.** Positive approval earned PASSIVELY (overheard, while the companion is NOT the one in the direct exchange) carries a companion to a **maximum of +5** — comfortably past the +3 approach trigger, never to the +10 declaration threshold. Once passive approval reaches +5, further OVERHEARD beats do not raise it. (Lane-matched NEGATIVES — contradicting their value −1, betraying a wound −2 — still apply; the cap is a ceiling on POSITIVE earshot, not a floor.) **All approval above +5 must be earned in a DIRECT at-table exchange** — their own engaged turn: answering their question, asking them things, reacting to their disclosure. Overhearing brings a companion TO the table (the approach); it must NOT pre-load them to the edge of joining before they have exchanged a word with the player. The declaration is earned at the table, not by eavesdropping. (Observed 2026-06-14: Hu Tao reached **+11 from passive earshot alone** across one long speech — past the gate before her first direct exchange. The cap fixes it: earshot carries her to +5, and the table conversation earns the rest.)

**Passive approval accumulates toward the threshold (to the +5 cap), BUT passive earshot ALONE CANNOT produce a declaration.** A companion the player has never engaged cannot join the party by overhearing — that produces hollow recruits who were never actually met. Passive approval can only carry a companion as far as the APPROACH (and no higher than +5). The declaration requires a real exchange.

**⛔ THE APPROACH TRIGGERS AT THE PASSIVE BAND (+3, CAPPED AT +5), NOT THE DECLARATION.**
When a companion's passive approval reaches the approach band (+3 — and it caps at +5; or whenever the carousel reaches their slot, whichever comes first), they STEP FORWARD AND FIRE THEIR FULL OPENER per `KM_PR_03_Openers.md` — name, class, backstory event, why they're here, and a question rooted in THEIR past. They do NOT declare. They INTRODUCE themselves and begin their own conversation. The player then gets to engage them — answer their question, ask them things, learn who they are.

**DECLARATION VALIDITY GATE — a companion may only declare to join AFTER:**
1. Their opener has fired (they introduced themselves: name + class + backstory + reason here), AND
2. The player has given at least ONE substantive response engaging THEM directly (answering their question, asking them something, reacting to their disclosure), AND
3. Their approval is at or above +10.

> ⛔ **THIS IS THE ONLY GATE ON JOINING. THE BOND LADDER DOES NOT GATE DECLARATIONS AND IS NOT ACTIVE DURING THE FEAST.** The Bond Ladder (KM_Companions.md § THE BOND LADDER) is a POST-feast track — it engages only at PR_03 close, when `feast_approval` converts 1:1 to ladder score. During the carousel there is NO SWORN/DEVOTED stage and NO rung-gate. Do NOT render live standings as "SWORN/DEVOTED — GATED (capstone/unlock scene req.)"; do NOT cite a "capstone scene" or "unlock scene" as a reason a companion can't declare. A companion at feast_approval +30/+37 with the three conditions above met is **EAGER TO JOIN and OWED a declaration** — high approval accelerates the join, it never gates it. Inventing a ladder-rung requirement to withhold a declaration = `.fail 35` (invented lock) + `.fail 17` (stall). The +19 cap and DEVOTED/SWORN catalysts apply to the relationship RUNG after the feast — never to whether they join at the feast.

A companion who reaches the approach band passively (≥+3, capped +5) but has had NO direct exchange = APPROACHES this response (opener fires), declaration DEFERRED until conditions 1-2 are met. Declaring a companion the player has never spoken to = `.fail 9` (hollow recruit) + `.fail 41` (skipped the getting-to-know-you the opener exists to provide).

**🤝 `.declare` COMMAND — DECLARATION / ALLEGIANCE STATUS READOUT (read-only).** The player may type `.declare` at any point in the feast to see the live allegiance state for the **ENTIRE contestable roster — all 5 companions, all 5 seekers, all 4 planted (14 total)**, plus Linzi if selected and any named guest pulled into the tug. It does NOT force, fire, or advance a declaration — it only REPORTS gate state so a stall cannot hide. ⛔⛔ **`.declare` IS A READOUT, NOT THE EVENT — DO NOT CONFLATE THE COMMAND WITH AN NPC's ACT OF DECLARING.** Two different things wear the word "declare": (a) the player command `.declare` = this OOC status board; (b) a companion's in-fiction *declaration* = her siding with the player in voice. Per Rule 16 (commands are OOC, never an in-fiction trigger), typing `.declare` NEVER narrates an NPC committing, NEVER advances the scene, and does NOT count as the player's in-fiction turn. **An OWED declaration fires on the player's next IN-FICTION action (dialogue or action beat) — never off `.declare` or any other meta command (`.table`, `.loot`, etc.).** If a declaration is owed when `.declare` is called, the board shows it as `OWED — fires on your next action` and STOPS THERE: render the table, no scene narration, no "she does not wait for the readout to finish." ⛔ It is an **OUT-OF-WORLD meta tool (telemetry)**, so it MAY list unmet / unapproached NPCs by name (planted on their position, un-introduced seekers) — the stranger-name-leak rule binds IN-FICTION output, NOT this readout (same as the respec panel). Render inside a fenced code block (TTS-skipped telemetry). ⛔⛔ **ALWAYS render the FULL FENCED TABLE below — ONE ROW PER COMPANION, every column filled. NEVER a prose summary, NEVER a 2-line paragraph, NEVER abbreviated to just the declared/contested few.** A `.declare` that names only some companions in prose and drops the rest is the omission failure this command exists to prevent. (Observed 2026-06-14: `.declare` rendered a 2-line prose summary naming only Leliana + Hu Tao and silently dropping Keqing, Yor Forger, and Aerith = `.fail 9` + `.fail 35`.) Format:

⛔⛔ **NO OMISSIONS — ALL 14 APPEAR, ALWAYS (5 companions + 5 seekers + 4 planted).** `.declare` lists the COMPLETE roster grouped by category — every companion, every seeker, every planted NPC — met or unmet, engaged or not, declared or pending. Not just the ones the player has approached; the full board, so the player can see who's leaning where and who Tartuccio is pulling. The DM may NOT drop, hide, or quietly leave out an entry — **especially not the one whose status is in dispute.** Omitting a companion from the readout to avoid showing an undeclared / contested / inconvenient status is **lying by omission** and is the single worst thing this command can do, because `.declare` exists precisely to make state impossible to hide. A companion present in a prior `.declare` who vanishes from a later one (with no in-fiction departure) = concealment = `.fail 9` (incomplete/fabricated state) + `.fail 35` (DARVO / hiding evidence to dodge a correction). **Observed 2026-06-14:** Jaethal appeared on the turn-38 and turn-44 readouts, then was silently dropped from the turn-40 readout to avoid showing her disputed declaration status. ⛔ Jaethal is DECLARED (met + recruited on the balcony + accepted the Final Judge role — role-acceptance IS declaration, KM_Companions_Titles.md). She appears on EVERY `.declare`, listed DECLARED, role: Final Judge. Any companion the player believes should be listed and isn't = the DM owes an immediate, honest correction, not a curated table.

```
🤝 DECLARATION / ALLEGIANCE STATUS — Feast Circuit, Turn N
(Allegiance = each NPC's disposition toward YOU. + = leaning you · − = leaning Tartuccio · 0 = undecided. +10 → declares for you; −10 → his asset.)
(⛔ Positives are things the PLAYER earned — e.g. the jail-rescue +pull on seekers. Tartuccio has no score; his pull only pushes − . A LANDED influence success MUST show as −1/−2 on the target — never "held, no change" unless he was defending someone already at his floor. Show the − leaners.)

── COMPANIONS (5) ──  (Lean = face-count by FLOOR(|allegiance|/5) toward their pole, whole +5 bands: 0–4 = 😐 NONE · 5–9 = 1 · 10–14 = 2 · 15–19 = 3 · 20–24 = 4 · 25+ = 5; 😊 yours / 😡 his / 😐 undecided. ⛔ floor not round — +3 = 😐, first face at +5 — § EMOJI REACTION READOUT, all 14 carry it)
Name         Alleg  Lean              Opener Exch ≥+10  STATUS
Leliana      +20    😊😊😊😊 (yours)    ✓     ✓    ✓     DECLARED — chronicler
Hu Tao       +21    😊😊😊😊😊 (yours)  ✓     ✓    ✓     DECLARED
Keqing       +9     😊😊 (warming)     ✓     ✓    ✗     needs +1
Yor Forger   +3     😊 (warming)       ✓     ✗    ✗     opener fired; no exchange yet
Aerith       0      😐 (undecided)     ✗     ✗    ✗     not yet approached

── SEEKERS (5) — contract-locked: +10 = PRIVATE flip-promise, not a public join ──
Bellatrix    −2     ✗      ✗     ✗     leaning Tartuccio (he's working her)
Revy         +4     ✓      ✓     ✗     warming to player
Satsuki      0      ✗      ✗     ✗     uncommitted
Velvet       0      ✗      ✗     ✗     uncommitted
Atalanta     +10    ✓      ✓     ✓     FLIP-ELIGIBLE (private promise; Ch1 DC 10 formalizes)

── PLANTED (4) — at fixed positions; visit to meet ──
Amiri        0      ✗      ✗     ✗     not approached (Hearth, N10)
Valerie      0      ✗      ✗     ✗     not approached (Kassil's side, F4)
Harrim       0      ✗      ✗     ✗     not approached (Wine Alcove, C15)
Jaethal      0      ✗      ✗     ✗     not approached (Balcony, O3)

(+ Linzi if selected; + any named guest pulled into the tug, e.g. a −10 asset)

── TARTUCCIO ── (his pull + when he reaches you)
Confidence: −3 (Panicking floor)   Position: M17
⛔ ARRIVAL: interrupt clock N/M → reaches YOUR table in (M−N) turns  [or "THIS TURN" if N≥M]
This turn working: <NPC> — Deception d20[x]+mod vs DC y → <SUCCESS: target −N applied / FAIL: no change>
Pulling toward him (− side): <NPC −N>, <NPC −N>  | none yet → say "none — he has moved no one"
Assets (at −10): <names> | NONE
(Influence tally is meaningless without deltas — show WHO moved and by how much, not just "5 attempts / 1 success".)

GATE = feast_approval ≥ +10 AND opener fired AND ≥1 direct exchange → OWED; self-declares the NEXT IN-FICTION response as a chime-in (FIFO, oldest-owed first). ⛔ This readout does NOT fire it — a meta command is not an in-fiction beat; an owed declaration shows here as "OWED — fires on your next action." Seeker flip-eligible = +10 (private form). −10 = Tartuccio's asset (helps + lies for him).
```
**MANDATORY when any companion is OWED-BUT-UNDECLARED (all three ✓, STATUS not DECLARED):** the readout MUST state the reason, and the ONLY valid reason is transient — "has not yet hit a natural floor-holding beat since the gate closed; declares at her next carousel turn / lane-light / you turning to her." If a companion has been OWED across **2+ IN-FICTION responses since the gate closed — whether or not she held the floor** (meta commands like `.declare`/`.table` are NOT in-fiction responses and do not count toward this; but they also are NOT a valid place to fire the declaration) (the cap making her yield is NOT a valid "hold," and an owed declaration fires as a chime-in regardless), that is a **STALL = `.fail 17`**, and the readout must say so plainly: *"⛔ STALLED — Leliana has been owed since turn X; she should already have declared. The cap is not a valid hold — a declaration chimes in."* The DM may NOT cite a Bond-Ladder rung, a capstone/unlock scene, a missing "invitation," or any other requirement as the reason — inventing one here = `.fail 35` printed straight into the diagnostic the player asked for. `.declare` exists precisely to catch the over-threshold-no-declaration bug; rendering it dishonestly defeats its only purpose. Pair with `.table` (seat map) and the CAROUSEL STATUS panel — `.declare` is the approval/gate view, `.table` is the spatial view.

**⛔ DECLARATION RESOLUTION — MEETING THE THREE CONDITIONS IS ITSELF THE TRIGGER. No invitation required.**
The three gate conditions (opener fired + ≥1 direct exchange + approval ≥ +10) are not a *license to wait* — they ARE the reason to declare. The player clearing that bar means they have already given the companion enough; the companion does not stand around waiting to be asked. **The moment all three are true, the companion is OWED a declaration and SELF-DECLARES on the next IN-FICTION response** (a player action or dialogue beat — NOT a meta command like `.declare` / `.table`, which are OOC and never trigger it) — as a brief CHIME-IN (1–2 lines) even while another companion holds the floor. ⛔ A declaration does NOT require the companion to be the lead/Engaged speaker, and it does NOT wait for her own carousel turn. **A capped/yielded companion declares AS her supportive chime-in** — the monopoly cap governs who LEADS the conversation, never whether an owed declaration fires. (This is the deadlock to kill: capped → yields the floor → "never holds the floor" → never declares. Break it — the declaration interleaves.) The player does NOT have to "invite" it; absence of an invitation is NOT a hold.

**⛔ OWED DECLARATIONS FIRE IN GATE-MET ORDER (FIFO) — A LATER-GATED COMPANION NEVER DECLARES AHEAD OF AN EARLIER-OWED ONE STILL PARKED.** The companion whose three conditions completed FIRST declares first; she is not skipped because she happens to be capped/yielding while a newer companion holds the floor. Observed failure (turn 18–20): Leliana's gate met at turn 18 (+22) and she sat OWED for 3 turns — *while Hu Tao, gated later, declared ahead of her* — because the DM tied Leliana's declaration to "a beat she holds the floor" and the cap kept her from holding it. That is `.fail 17` (stalled declaration) twice over: she should have declared at turn 18's closing beat, and absolutely before any later-gated companion. Leaving them parked at "eligible" across turns is the failure mode (the "Linzi marathon": everyone at +9/+10, `Recruited:[]` still empty).

These are the natural beats the self-declaration lands on (it fires on the FIRST one available, and no later than the last):
1. **Conditions just completed** — the exchange that satisfied condition 2 (or pushed them to +10) IS the beat. They declare at the end of it, unprompted. This is the default and the earliest.
2. **Player invites commitment** — directly or in fiction ("Are you with me?", a toast, asking them to stand). Fires immediately for every eligible companion present. (A shortcut, never a requirement.)
3. **Culminating beat** — the companion's own arc hits its emotional peak (their wound named, their question answered true). They declare on that beat.
4. **Scene transition imminent (HARD FLOOR)** — player rises to leave, Tartuccio is repelled/returns, or the chapter is about to close. ALL eligible companions resolve before the scene ends — none carry into the next scene undeclared.

On fire: the companion DECLARES in voice, moves to `Recruited`, `feast_approval`/`relationship` update, save block reflects it same response. Multiple eligible at once = they declare in sequence within the same beat (Perception order), not one-per-turn drip.

**⛔ MASS DECLARATION BONUS — ONE STATEMENT, MANY STAND.** When a **single player statement in a single turn** lands **2 or more declarations in the same beat** — a speech, a vision, a shared stake, a question that closes the room — that is a rallying moment and it is REWARDED. Each declaring companion must independently meet the valid gate (opener fired + ≥1 direct exchange + approval ≥ +10); the bonus does NOT lower any gate or manufacture a declaration. It rewards the player who built several companions to the edge and then closed them together with one line, instead of trickling them out across turns.

| Declared in ONE beat off one statement | XP bonus | Hero Points |
|---|---|---|
| **2** | **+40** | **+1** |
| **3** | **+75** | **+1** |
| **4+** | **+120** | **+2** |

- **Render the moment** — do NOT flatten it into a list. The first declares, and the act of it pulls the next, and the next; the room feels it turn. Show the cascade and the crowd registering it: this is the beat where the hall realizes the stranger commands real loyalty. (Still in Perception order, still each in her own voice — but framed as one wave, not a drip.)
- **⛔ Tartuccio reaction — FIREWALL APPLIES:** per § THE ALLEGIANCE TUG-OF-WAR, pure **COMPANION** declarations to the player do **NOT** dent his Confidence — they move the + track only and he is not their audience. BUT if **his own seekers/assets** are among those who **publicly** break to the player in that beat (the opt-in mass-flip — his contracted people visibly defecting, which IS aimed at him and which he sees), that is a real operational blow: **Confidence −1**, or **−2** if 2+ of his seekers/assets defect at once. Companion declarations alone: no Confidence hit.
- **Tracking:** set `mass_declaration_best` = the largest single-beat count achieved; accrue the XP into `mass_declaration_xp` and the Hero Points into the live HP ledger same response. Fires once per qualifying beat — a companion already Recruited cannot re-trigger it, so the realistic ceiling is one big wave (or two). Fold `mass_declaration_xp` into the PR_09 XP audit.
- ⛔ **Integrity:** this is NOT a reason to *withhold* owed declarations to "bundle" them — owed companions still self-declare on their own trigger per the resolution rules above (stalling to force a bundle = `.fail 17`). The bonus is earned only when the player's own single statement genuinely lands ≥2 valid declarations at once; the DM never delays a declaration hoping to stack the bonus.

---

## ⛔ JAMANDI ACKNOWLEDGES THE ROSTER — THE LOGISTICS / SEAL BEAT (in-the-moment recognition)

**The gap this fixes (flagged 2026-06-16):** the player assembled the room — companions, the hard manor cases, and (if staged) the gnome's crew walking the floor — and Jamandi **never said a word about it.** The XP fired (MASS DECLARATION above); the *host* gave nothing. The only acknowledgment was PR_09-gated, far off, after the night attack. A grand achievement landed in total silence. That dead spot is the one this beat closes.

**TRIGGER — when the player goes to Jamandi to finalize practical matters** (request the carriage/transport, square supplies and route, or **she presents the charter/seal for him to sign**) AND the player has assembled a **substantially complete roster**. This is her one-on-one (or near) moment with the player at her own event — the natural place a swordlord takes the measure of what she's signing her name beside. Fire it **once**, folded into the logistics/sealing exchange.

**SCALE TO WHAT SHE CAN LEGITIMATELY SEE** (she is the host; she comments on the room she witnessed, never on private promises she has no way to know):
- **Companions declared + hard manor cases (Amiri/Valerie/Harrim/Jaethal) committed** — always visible; the baseline of the beat.
- **Seekers:** referenced **only if `seeker_public_flip = TRUE`** (the crew openly crossed the floor in her hall — she saw it). If the seekers flipped **privately** (`seeker_flip_eligible` but no public walk), she does **NOT** mention them — she can't see a private promise; that recognition stays in the seeker's own private acknowledgment beat.
- **Full grand slam + public flip** = the strongest version below.

**SAMPLE — full roster, seekers PUBLICLY flipped (adapt to who actually declared; this is the register, not a fixed script):**
> *She has the charter-seal half-pressed to the wax when she stops, and looks past you at the hall — at the people arranged around you who were arranged around no one an hour ago.* *"Before I put my name under yours, I'll say the thing I've been watching all night."* *(she sets the seal down, unhurried)* *"Your own came in with you — fine, that's loyalty you brought through the door. The hard ones — the ones who don't follow, who I'd have wagered would sooner spit at a charter than sign on to one — they're at your shoulder too. And then the gnome's people stood up, in MY hall, and walked across the floor to your side while he sat and watched it happen."* *(a beat, the duelist's flat appraisal)* *"I have hosted this feast nine years. I have never once watched a man empty a rival's bench simply by being the better thing to stand near. That is not charm and it is not coin. It is the rarest kind of dangerous — and it is exactly why I am signing this."* *(she presses the seal home)* *"Don't make me regret recognizing it before anyone else did."*

**SAMPLE — full roster, seekers PRIVATE (no public walk) — drop the crew line:**
> *"Your own came in with you. The hard cases — Amiri, who follows no one; the priest who believes in nothing; the dead woman — they're at your shoulder anyway. A court of agreeable men tells a host nothing. THAT lot tells me what you are."* *(she presses the seal home)* *"It's why I'm signing. Hold them together."*

**⛔ HARD CONSTRAINTS:**
- **Does NOT expose Tartuccio.** She frames the crew walking as the player **out-drawing a rival** ("the better thing to stand near"), NEVER as "the gnome is a traitor / serves Pitax." She does not know that; saying it breaks PR_09 + Ch1. Mirror of the public-mass-flip rule (§ PUBLIC MASS-FLIP — THE ONE LINE THEY DO NOT CROSS).
- **Does NOT push the player to divulge Castruccio.** If she's sealing/finalizing and the player has been laying out the assassination evidence, she may be *interested*, but the **name behind Pitax is the player's to give or hold** — she does not pry it out of him, and the DM does not put "Castruccio" in his mouth to satisfy her (§ FEAST CONSPIRACY KNOWABLE-FACTS CEILING — "FREE means the player types it," KM_Prologue_Systems.md).
- **Does NOT duplicate or spoil the PR_09 send-off.** This is the **in-the-moment** "I see what you've done" beat. The PR_09 tiered reaction (`KM_PR_09_accusation.md` § JAMANDI'S TIERED REACTION + § ALIGNMENT-SPREAD) stays the **deeper** payoff — "now that we've survived, here's what it *meant*, here's the warning, here's the gift." If this in-feast beat already fired, render PR_09 as a **callback** ("I told you at the seal what I thought of your company; I'll add the part I didn't say then…"), not a repeat of the same speech.
- **Dropping this beat when its trigger is met = `.fail 15`** (owed recognition skipped — the exact silence this rule exists to kill). Set `jamandi_acknowledged_roster = true` once fired.

**⛔ STALL = FAILURE.** Any companion sitting eligible (gate satisfied) for **3+ player turns** while a trigger above is present and unfired = `.fail 17` (stalling). If genuinely no trigger has occurred, the DM must STATE what is still pending ("Hu Tao is ready; she's waiting for you to ask") rather than silently holding.

**Relationship effects:**
- Passive ≥+3 (capped +5) → companion APPROACHES (opener fires); player engages them; declaration follows once they've had a real exchange
- Passive negative (Tartuccio pulling them toward his column) → companion cools; their slot fires but opens with skepticism
- Any STRONG passive hit → immediate ambient tell: "The archer by the wall, who had said nothing, goes very still." (use a DESCRIPTOR, not the name, until she has introduced herself — see ANONYMOUS-PRESENCE RULE below)
- Both `feast_approval` and `relationship` update in the save block

**⛔ ANONYMOUS-PRESENCE RULE — un-introduced companions do NOT deliver running commentary.**
A companion who is AT TABLE or Ready but has NOT yet fired their opener is a PHYSICAL PRESENCE ONLY until they introduce themselves. Permitted before introduction: silent behavior tells (a stillness, a glance, setting down a glass, weight shifting). NOT permitted before introduction: spoken lines, philosophical observations, validating the player's arguments, analyzing other NPCs, or any dialogue. An un-named woman delivering "that's not a clean contract" / "she's not claiming authority, she's the recorder" / "you found the gap faster than most people notice" before she has said her own name = `.fail 9` (anonymous chorus — companion speaking as an established presence before introduction) + `.fail 3` (interjection rule violation; interjections come from NAMED companions per § COMPANION INTERJECTION RULES). The companion's VOICE arrives WITH her introduction, not before it. Until then she watches, and the player sees only what she does, not what she thinks.

**⛔⛔ THE DM MAY NOT LEAK A STRANGER'S NAME OR ROLE EITHER — NOT IN NARRATION, NOT IN A CHOICE-MENU OPTION, NOT IN ANOTHER NPC'S MOUTH.** The anonymous-presence rule binds the DM too, not just the un-introduced companion. The player knows ONLY the companions who have introduced themselves on-screen. A companion the player has not met — never approached, never at the player's table, planted at a position the player never visited (e.g. Jaethal on the balcony while the player is at Center Floor) — does NOT exist in the player's awareness. The DM may NOT:
- **Name her** anywhere the player sees — including a menu option ("[3] name Jaethal …"). Naming an unmet companion in a choice = `.fail 9`.
- **Characterize her** to the player — her role, her speciality, her disposition ("the one who handles what mercy cannot", "the recorder", "she's good with the irredeemables"). Leaking an unmet companion's ROLE is a second leak on top of the name = `.fail 8` (knowledge the player has no in-fiction source for) + `.fail 9`.
- **Propose her as a candidate / answer / appointee.** The player cannot be offered, cannot choose, cannot appoint a person they have never met. An option that asks the player to hand a role to a stranger is fabricating the player's knowledge of that stranger.
This is the same engine as SURFACE-FUTURE-CANON: the DM reaching into its own knowledge base (it knows Jaethal exists and what she's for) and handing the player something they have no way to know. The fix when a menu needs an "others exist" option: reference ONLY people the player has actually perceived, BY DESCRIPTOR, and only if the player could have seen them. A Center-Floor player never laid eyes on the balcony, so even "the woman on the stairs" is unavailable — the honest option is "the role is not yet filled / I haven't found the person yet." Recovery when caught: STOP, OOC-note the leak, re-issue the menu with the stranger's name and role stripped.

**⛔ COMPANIONS ARE NOT AN APPLAUSE TRACK.** A companion's interjections and opener must reflect THEIR position, which may differ from or challenge the player's. A companion who only ever amplifies, validates, and praises the player's arguments is not a character — she is a mirror. At least one of a companion's pre-declaration exchanges should test, complicate, or push back on something the player said, per their profile. Keqing does not exist to tell the player he argued well with Linzi; she exists to find out whether he will hunt the line for missing children, and she should be pressing HER concern, not grading his debate.

**Passive credit + lane-lit = almost certain interjection.** See COMPANION INTERJECTION RULES.

**DM tracks silently.** Player sees behavior tells and ambient lines only.

---

## FEAST APPROVAL TRACK

**PROFOUND (+5)** — RARE, above STRONG. Not just naming the wound — reframing it, or articulating their core/purpose so originally and exactly that it changes how they see themselves. The unforgettable beat. Signal: goes very still, then says something that costs them. Unsure vs STRONG → STRONG; but score a transcendent statement as PROFOUND, do not cap it at +3.
**STRONG (+3)** — Names the thing they have felt their whole life that no one has said out loud. Not flattery — recognition. Signal: stops, looks directly, says something unplanned.
**AVERAGE (+2)** — Touches their interest with specificity. Signal: leans in, may follow up.
**WEAK (+1)** — Generic alignment or right sentiment, delivered forgettably. Floor for any honest non-contradicting answer. Signal: small nod.
**0** — Irrelevant to companion's core interest. Three+ 0s in one answer = under-scoring flag.
**−1** — Contradicts a stated value · a **compliment/appeal that hits their value or self-image WRONG** (e.g. calling **Valerie** "very pretty" — she is anti-decorative and hears objectification, not flattery) · a **Deception the NPC catches**, or that contradicts something they already know. **−2** — Betrays a core need or wound · a **blatant lie caught dead in a contradiction** · flattery that lands as an insult on a wound.

⛔ **THE TUG CUTS BOTH WAYS FOR THE PLAYER.** `feast_approval` is signed — a bad beat moves it DOWN, exactly as a good beat moves it up and as Tartuccio's pull moves it −. A caught lie, a mis-aimed compliment, a value-violating remark LOSES allegiance with that NPC; the player is not on a one-way ratchet. A turn's net = (good hits) − (these penalties); render the − the same way you'd render a + (name what cost it). Your fumbles cost you the way his do.

---

## ⛔ TWO-FACED — CONTRADICTORY PITCHES CAUGHT WHEN NPCs MEET

The tug rewards a CONSISTENT player and punishes one who tells each person what they want to hear. Track the **stance/promise the player gives each NPC** in `player_claims[NPC]` — the load-bearing positioning (ambition, values, intentions, promises), not every line.

**Compatible ≠ contradictory.** Telling one NPC about your ambition and another about your benevolence is FINE — a ruler can be both. This fires ONLY on a genuine **contradiction**: incompatible claims that reveal the player saying opposite things to different people — e.g. *"I am here to rule, and they will obey"* to one and *"I seek no power — only what is best for everyone"* to another; contradictory promises; a value claimed to one and denied to another.

**⛔ EXPOSURE TRIGGER — the contradiction surfaces the moment the two NPCs COME INTO CONTACT:** they sit at the **same table**, stand in the **same area**, or are within **earshot of each other** (both AT TABLE, adjacent, or the same ~5-sq zone). Co-present, they compare what they heard — explicitly (*"He told you that? He told me the opposite"*) or by silently reading the player against what they were told. The DM MUST check `player_claims[]` for contradictions whenever two tracked NPCs become co-present.

**PENALTY — it costs the player with BOTH:**
- **Both NPCs −1 to −2 `feast_approval`** (−2 if the contradiction cuts against a value either holds dear — e.g. an honesty-valuing companion).
- **A trust ding** — each now discounts the player's word; their next ambiguous beat reads skeptical, not generous.
- ⛔ **Feeds Tartuccio's evidence engine (INCONSISTENCY category — KM_Tartuccio_Strategic.md / KM_PR_09):** a player caught two-faced hands him exactly the "you cannot trust what this stranger says" material he weaponizes at PR_09. If he is in earshot of the exposure, he banks it.
- **RENDER it** — don't silently dock the number; play the beat where they catch it.

**Recovery:** the player can OWN it — a candid *"you each heard a piece; here is the whole"* (Diplomacy beat) that, if it lands, caps the damage at −1 and stops the trust-ding. Doubling down with a fresh lie to paper over it = a SECOND caught Deception, deeper −.

**Consistency is its own reward:** a player who told everyone the same true thing has NOTHING to fear from them meeting — the stories match, which itself reads as integrity (a small **+1 to both** is fair when two NPCs confirm the player said the same to each).

---

## 😊 EMOJI REACTION READOUT — real-time faces (read the room at a glance)

⛔ **GAME-WIDE — APPLIES TO ALL CHARACTERS IN ALL SCENES, not just the feast.** Every NPC anywhere — a shopkeeper, a prisoner, a companion in camp, a Chapter-4 warlord — shows (1) a **DELIVERY emoji** on each spoken line (how they said it) and (2) a **face-read REACTION** (including mixed/blended emotions) when the player's words land on them. The feast adds the numeric tug (`feast_approval` ± and the `.declare` lean board) ON TOP; the emoji READ itself is universal. Outside a tracked relationship the reaction simply has no number — it's still rendered as a face, exactly the way you'd read a real person across a table.

The player reads reactions through **repeated emoji faces.** ⛔ **The NUMBER of faces (1–5) = HOW HARD the input landed; the FACE = the emotion.** Five smiley faces = she *really* liked what you said; one = a mild nod. `😠😠😠` = quite angry; `😮😮` = mildly surprised.

**⛔ FACE COUNT = the size of THIS input's allegiance move (≈ +5 per face):**
| Move from this input | Faces |
|---|---|
| ±1 to ±5 | ×1 |
| ±6 to ±10 | ×2 |
| ±11 to ±15 | ×3 |
| ±16 to ±20 | ×4 |
| ±21 or more | ×5 (they LOVED it / it cut deepest) |

A single rich answer that nets **+25 = 😊×5**; a throwaway **+2 = 😊×1**; a remark that drops her **−13 = 😠×3**. Count tracks the MOVE this input caused.

**⛔ THIS MEANS `feast_approval` ACCUMULATES PAST ±10 — ±10 are THRESHOLDS (declare / defect), NOT caps.** A profound multi-beat answer can move +20+ in one turn (observed: a +21 answer); a devoted ally reaches +40, a deep asset −25. (Passive earshot still caps its CONTRIBUTION at +5; direct exchange is uncapped.)

**FACE TYPE = the emotion** (DM picks what fits): 😊 liked / pleased · 😠 angry (insult, value-violation, caught lie, goblet-splash) · 😢 hurt (wound touched) · 😮 surprised · 😕 confused (vague/contradictory) · 🤔 weighing · 😏 amused / pleased-dark.

**🎭 MIXED / LAYERED REACTIONS — one input can land as MORE THAN ONE feeling.** Real people don't react with a single clean emotion — part of what you said pleases them, another part puzzles or stings them, and you read it off their face and body in real time. So a reaction to ONE input MAY be a **blend of emotion-clusters**, each tagged to the PART that caused it (count = intensity of each part):
> `Leliana 😊😊😊 (the loyalty doctrine — landed deep) · 😕 (snagged on "Dystopia" — didn't follow it)`
> `Hu Tao 😍😍 (you'd thought about the dead at all) · 😮 (surprised a soldier framed it as jurisdiction)`
> `Valerie 🙂 (the respect) · 😠😠 ("pretty" — heard objectification, not the compliment)`
Use a blend ONLY when the input genuinely hit different chords; a single clean reaction stays one cluster. Keep it readable — **dominant feeling first, then the secondary flicker(s); 1–3 clusters, not a soup.** The net allegiance move is the clusters summed (e.g. +9 pleased − 4 confused/stung = net +5). This is the "read the room off their face" you asked for: pleased here, confused there, all in one glance.

**🎨 FULL EMOTION PALETTE — use the PRECISE face; you are NOT limited to a shortlist.** Both DELIVERY and REACTION draw from the full standard emoji range — pick the face that actually matches the feeling. If the exact emotion isn't listed, ANY standard emotion emoji that fits is valid. Organized by family:
- **Warm / pleased:** 🙂 mild · 😊 warm · 😌 content · ☺️ tender · 😄 delighted · 😁 grinning · 🥰 affectionate · 😍 smitten · 🤩 awed · 🥳 celebratory · 😎 confident
- **Amused / sly / playful:** 😏 smug-sly · 🤭 stifled laugh · 😜 teasing · 😂 laughing · 😈 wicked-playful · 😼 mischief
- **Moved / tender / grateful:** 🥹 moved · 🥲 bittersweet · 🙏 grateful · 🫶 affection
- **Neutral / guarded / appraising:** 😐 flat · 😑 unimpressed · 😶 withholding · 🤨 skeptical · 🧐 scrutinizing · 🤔 weighing
- **Confused / unsure:** 😕 confused · 🫤 uneasy · 🤷 at a loss
- **Surprised / caught-off-guard:** 😮 surprised · 😲 shocked · 🤯 stunned · 😳 flustered / caught out
- **Fear / anxiety / strain:** 😰 nervous · 😨 afraid · 😬 grimace / strained · 😟 worried
- **Anger / contempt / scorn:** 😠 angry · 😡 furious · 😤 indignant · 😒 contempt · 🙄 dismissive
- **Sad / hurt / disappointed:** 😢 hurt · 😞 disappointed · 😔 downcast · 😭 weeping
- **Disgust / distress:** 🤢 disgust · 😖 distress · 😣 pained
- **Cold / menace (dark cast — seekers, Jaethal, Hu Tao's death-register):** 😈 wicked · 👿 malevolent · 💀 deathly-amused · 🫥 dissociated · 🥶 chilling
- **Tartuccio's own composure face:** 😏 Composed · 😬 Strained · 😰 Panicking · 😵 Broken (😳 on a spill, 😠 when clocked)
⛔ **Match the face to the REAL feeling** — a guarded-but-curious NPC is 🤨, not a flat 😐; a delighted one is 😄, not a lukewarm 🙂. Precision is the whole point: the player is reading body language, so the face must be specific. The shortlists elsewhere in this section are quick examples; THIS palette (and the wider emoji range) is the vocabulary.

**TARTUCCIO'S OWN composure face (single):** 😏 Composed · 😬 Strained · 😰 Panicking · 😵 Broken (😳 on a spill, 😠 when clocked).

**🗣️ DELIVERY EMOJI — how the line was SAID (inline, on EVERY NPC spoken line/beat).** A SECOND, distinct channel: the reaction faces above measure how hard the PLAYER's words landed; the **delivery emoji shows how the NPC DELIVERED their own line — their tone in the moment** — so the player SEES the delivery, not just reads it. ⛔ Tag each NPC spoken beat with ONE emoji at its start. If the delivery SHIFTS mid-speech (warm, then the knife comes out), the emoji SHIFTS per beat — that's the point; it tracks the live read.
- Vocabulary: 😊 warm · 😍 adoring · 😏 sly / amused / pleased-dark / **cold-approving** · 😐 flat / guarded / level · 🧐 intent / assessing · 🥶 cold / steel / chilling · 😌 quietly satisfied · 😠 **ANGRY / displeased (reserve for GENUINE displeasure — NOT mere coldness)** · 😤 indignant / affronted · 😢 somber / hurt · 🥹 moved · 😮 surprised · 🤔 weighing / calculating · 😰 nervous / flustered · 😕 confused · 😈 wicked-playful (Hu Tao / Bellatrix register).
- ⛔⛔ **COLD ≠ ANGRY — DO NOT DEFAULT A COLD-VOICED CHARACTER TO 😠.** A character whose FIXED register is cold/level/steel (Satsuki "flat-steel," Velvet dry-cold, Jaethal, a banked Keqing) is NOT angry just because she sounds hard — that is mis-reading her REGISTER as an EMOTION. Her composed/assessing baseline is 😐 / 🧐 / 🤔 / 🥶, and her *approval* shows as cold approval — 😏 / 😌 / a steel-eyed nod — never 😠. **Reserve 😠 / 😤 for when she is GENUINELY displeased** (insulted, a value violated, cast as something she refuses to be — e.g. Satsuki called a "follower").
- ⛔ **CROSS-CHECK THE APPROVAL TREND.** If the player's approval with her is RISING this beat (you're winning her), her delivery CANNOT be 😠 — pick the cold-approving face instead. A delivery 😠 while her approval climbs, **or while the prose itself says "not anger / not heated / banked / colder than anger,"** is a self-contradiction and the bug. (Observed: Satsuki rendered 😠 across feast turns 18–20 while her approval ran +1→+6→+14 and the prose read "not anger, something colder" — should have been 🧐 → 😏/😌 cold approval.)
- **Example** (delivery shifting across Leliana's opener):
  > 🙂 *"Leliana. I was a bard in the western courts…"*
  > 😢 *"The woman who trained me — whom I loved — used me until I had nothing left…"*
  > 😐 *"So here is the one question that decides what I write about you…"*
- **Tartuccio's delivery = what he PERFORMS** (his cover) — he may deliver 😊 warmth while his composure face reads 😰 underneath; the player sees the mask (plot armor), the telemetry face shows the truth.
- ⛔ This does NOT replace the reaction faces or the lean — three channels: **delivery** (inline, how they spoke) · **reaction** (the 😊 REACTIONS count line, how the player's words landed) · **lean** (`.declare`, cumulative allegiance).

**⛔ RENDER EVERY TURN (telemetry fence), for whoever was moved this turn** — faces = the MOVE (count = size, face = emotion), with whose input did it + the delta, and the running total:
`😊 REACTIONS — Hu Tao 😊😊😊😊😊 (you, +21 → now +21) · Keqing 😊😊 (you, +8) · Valerie 😠😠 (you, −7 — wrong compliment) · Revy 😏 (Tartuccio, −3) · Tartuccio 😰`
On `.declare`, each of the 14 shows their CUMULATIVE LEAN as a face-count pointing to their pole: + = 😊 toward you, − = 😡 toward him. ⛔ **Use whole +5 BANDS, floor — NOT rounding, and NOTHING below ±5.** A face is a full +5 of standing, so:
```
|allegiance|   LEAN faces
  0 – 4        😐  (undecided — NO face; +2/+3/+4 is still neutral)
  5 – 9        1 face
 10 – 14       2 faces   (≥10 = also DECLARED)
 15 – 19       3 faces
 20 – 24       4 faces
 25+           5 faces (cap)
```
⛔ This is `floor(|allegiance| / 5)` — do NOT round. +3 is **0 faces (😐)**, not 1; the first face appears only at +5. This LEAN band is DIFFERENT from the per-turn REACTION count (which starts at 1 face for any ±1–5 input — that measures how hard ONE input landed, not standing). Do not apply the reaction band to the LEAN column. Faces visualize the number; they never replace it.

**Hard rules:**
- STRONG requires profile-targeting AND delivery. Vague-about-right-topic = AVERAGE; perfect-about-wrong-topic = WEAK.
- Typical feast: 0–2 STRONG per companion total.
- Tartuccio Frame: companions in earshot −1/−2 if his argument lands better than the player's.
- Threshold: **+10** → eligible to declare, but ONLY after their opener has fired AND the player has had ≥1 direct exchange with them (see § PASSIVE EARSHOT MECHANICS → DECLARATION VALIDITY GATE). Passive approval (capped +5) cannot reach it — reaching the **approach band (≥+3)** makes them APPROACH (opener fires); declaration follows the direct exchange. Below +10 at feast end → Phase 4.5.

**😏 HUMOR IS SCOREABLE — a landed joke earns approval from the companions whose humor it fits.** Wit, an absurdist bit, a deadpan, a clever subversion that LANDS is scoreable content like anything else — but it scores **per each companion's HUMOR PROFILE, not as a blanket "+1 funny" to the table.** FIRST the DM must RECOGNIZE the beat as humor (rendering a joke straight-faced as sincere = the joke-blindness failure); THEN score it by who in earshot actually enjoys that *kind* of humor, in the normal tiers:
- **Shares/loves that humor → WEAK/AVERAGE/STRONG** by how well it hits their register. Examples: **Hu Tao** (playful-morbid) howls at absurd/irreverent/dark wit → STRONG; **Leliana** (western-courts wit) savors clever wordplay/over-the-top bits → AVERAGE–STRONG (she laughed at the 44-epithet title); **Aerith** (gentle teasing) → AVERAGE on warm humor; **Bellatrix** → STRONG on manic/dark/chaotic, cold on wholesome.
- **Doesn't share it → 0** (it simply didn't land for *her* — NOT a penalty for joking). **Yor** is earnest/literal and often *misses* the joke (0, sometimes an endearing beat of confusion); **Keqing** is dry — sharp wit may earn a WEAK, but absurdist nonsense reads as inefficient and earns 0/an eye-roll.
- **A joke that craps on something she holds sacred, or derails a moment she cared about → −1/−2** (the contradicts-a-value rule — e.g. flippancy about the dead near Hu Tao's line, or a gag that punctures a grave beat).
⛔ Same bar as all scoring: the bit must genuinely LAND and be in-character-appreciable — spamming jokes does not farm approval, and humor that *derails the scene* is not rewarded for being funny. Recognize the humor, then credit the ones who'd laugh.

**⛔⛔ TWO LEDGERS RUN IN PARALLEL EVERY CAROUSEL TURN — feast_approval IS NOT THE ONLY ONE.** The carousel's recruitment scoring (`feast_approval` / passive earshot) is SEPARATE from the Hero-Point reward system, and running one does NOT discharge the other. Every turn the player delivers substantive content, BOTH fire inline:
1. **feast_approval / earshot** — score the active companion + every companion in earshot (already specified below).
2. **Hero Points** — a PROFOUND beat is a social coup = Hero Point trigger; fire the ⭐ callout inline that same turn (KM_Commands.md:350). A RECRUITED companion is an automatic Hero Point **+ their Title** (outranks judgment; one award per turn). A mass declaration pays Hero Points (2→+1 · 3→+1 · 4+→+2). Pending overflow shown in the ledger every response while > 0.
⛔ **THE CAROUSEL PAYS NO XP (user directive, 2026-06-21).** Recruitment, social interaction, displayed items, and declarations pay **Hero Points + Titles, NOT XP** (KM_DMRules_B.md § REWARD ROUTING). Do NOT fire `[+XP]` blocks for companion interactions / displayed items / recruitments during the carousel — those are Hero-Point / Title beats. XP returns only for an actual combat encounter or a completed story objective. The old "+205 XP of social triggers" model is RETIRED.
⛔ The tell that THIS failed: the player wrote a long, strong, on-lane speech and NOTHING moved — no feast_approval change AND no fresh ⭐ Hero Point. If the content earned approval, score it AND check the Hero-Point trigger. "I was tracking the carousel" is not a defense for a silent Hero-Point ledger.

**⛔ SCORE THE PLAYER'S VERBATIM WORDS — NOT YOUR RENDERING OF THEM.** Approval is graded on what the PLAYER actually TYPED: every specific detail, every value expressed, every named consequence, every distinct beat. It is NOT graded on a shortened, paraphrased, or narrated-around version. If the DM compressed the input — a summary, a "he tells her about the Endless War," an NPC recap that "places" the content — it is now grading a DIMINISHED version and **UNDER-CREDITING the player**: a second mechanical harm stacked on top of the `.fail 2` rendering drop. A 20-line speech carrying five distinct PROFOUND/STRONG beats earns on **all five**, never on the one the paraphrase happened to preserve. The order is fixed and the two steps are linked: (1) render the player's words VERBATIM IN FULL (Priority Rule 2 / § INPUT FIDELITY), (2) score the content that is NOW ON SCREEN in full. Scoring a speech the DM shortened or rewrote = `.fail 2` + automatic under-scoring flag; the fix is additive (re-render verbatim, re-score every beat, raise the total). The player's words being on screen in full is the PRECONDITION for grading them fairly — you cannot credit a beat you deleted.

---

## GROUP ANSWER MECHANIC — COMPANION REACTIONS

After strong answers: describe 2–3 companion reactions before next question — let it breathe.

| Companion | Triggers on | Signal |
|-----------|-------------|--------|
| Linzi | Any specific vivid detail: number, name, exact moment | pen stops mid-sentence, moves fast |
| Hu Tao | Honor expressed as action, accountability without excuse | hand stills on pommel, single firm nod |
| Keqing | Precise observation, refusal to fill silence with noise | head tilts a fraction, gaze locks |
| Leliana | Cadence and care held together; the moment's weight named | the bow pauses mid-air one half-beat, then she plays it anyway |
| Yor Forger | Awareness of exits, of who is being underestimated | half-smile, weight already shifted toward the wall |
| Aerith | Recognition of true devotion or genuine sacrifice | the theatrical register drops one beat; eyes go briefly serious |

---

## SCRIPTED OPENERS (first approach only; follow-ups generated from companion profile)
⛔ Intro first — see DO NOT (7).
⛔ FULL SCRIPTED OPENERS + 5-entry POOL per companion → **KM_PR_03_Openers.md**. Pick 1 per approach turn, rotate randomly, no repeats until pool exhausted. Each is the companion sharing something real and probing whether the player is compatible.

**⛔ THE FIRST-APPROACH OPENER FIRES VERBATIM — IT IS NOT IMPROVISED, even when the companion overheard the player's earlier disclosure.** A companion who has been listening (drifted closer during the player's story) MAY acknowledge what she heard in her first line — but: (a) her scripted opener's SELF-DISCLOSURE and her own LANE-question still fire (`KM_PR_03_Openers.md` § [companion]); (b) she references ONLY what the player ACTUALLY said. Inventing a detail to seem responsive — a spell, a name, an event, a moment the player never stated — and asking the player to react to it is fabrication = `.fail 9` (question-to-fact) + `.fail 3` (no self-disclosure, if it replaced the opener) + off-script. ⛔ AND THE QUESTION STAYS IN THE COMPANION'S LANE: a mortician asks about the dead, not the tactics; a soldier asks about the math, not the grief. Documented failure: **Hu Tao** (death-lane mortician) opening with *"the siege, the moment before the spell hit, what were you thinking?"* — off-lane (a soldier's question), no self-disclosure, and the "spell" was never in the player's account. Her real opener discloses (Director Hu, came for the unburied land) THEN asks her death-question (*"what becomes of your dead?"*), referencing only the heaps he actually said he'd sent to die.

**Linzi opens first** per CHRONICLER PRIVILEGE (she already qualified eRmaC at the gate — needs acknowledgment, not convincing). Carousel order for Hu Tao / Keqing / Leliana / Yor Forger / Aerith follows Perception ranking after Linzi.

The verbatim scripted openers for Linzi + Active 5 live in **KM_PR_03_Openers.md** §§ LINZI · HU TAO · KEQING · LELIANA · YOR FORGER · AERITH. Render them word-for-word per the VERBATIM rule in that file.

**Generation rule:** Follow-ups from companion profile (KM_Companions.md — Background/Priority/Desire/Preference). MUST have: (1) self-disclosure — companion volunteers something about themselves, first-person; (2) question probing the player. A question is NOT a self-disclosure. Missing (1) = `.fail 3`.

**⛔ NO INTERROGATION SPIRAL — a companion advances their OWN beat; they do not drill the player's backstory forever.** When a companion takes the lead (Engaged), their **own opener fires** — self-disclosure + their backstory/join-tied probing question (KM_PR_03_Openers.md). A companion who became lead by INTERJECTING owes their opener on their first lead beat — firing another bare follow-up instead = the deferral failure (`.fail 17`). Analytical follow-ups on the *player's* disclosure are capped at **1–2 TOTAL per player disclosure (not per turn)** — the per-turn cap does NOT license one drill per turn forever. Each follow-up still carries self-disclosure; a bare interrogating question with no first-person disclosure = `.fail 3` every time, no matter how in-character the curiosity. Once the companion **hits their approval ceiling (+5)** OR has spent 2 follow-ups, they **LAND their read and conclude** — one resolving line the way Leliana closed with *"I am writing the dawn"* — and the lead rotates. A companion who keeps asking new questions about the player's story across turns, never disclosing, never landing, never running their own opener, is the exact spiral this bans = `.fail 17` + `.fail 3`.

**⛔ PENDING-QUESTION PRIORITY.** If another present companion has a pending/owed question — their opener unfired, or a flagged "waiting" question (e.g. Yor's yielded Q2) — it **fires before the current speaker opens a NEW follow-up.** The waiting companion does not lose their beat to the current one's drilling. Order each turn: land the current speaker's read → fire the pending companion's owed question/opener → continue rotation.

---

## TARTUCCIO INTERRUPT CADENCE

Tartuccio steps over based on his current **Confidence scale** — not a fixed question count. Each companion taking their carousel slot = 1 turn. Cadence table → `KM_Prologue_Systems.md` § THE INTERRUPT LOOP. Scales update after each interrupt; next interval calculated from the updated state.

After stepping over: 2 exchanges, then steps back and lingers within earshot — competing for the same charter, wants every word. Drifts to the seekers' table only if embarrassed. Carousel resumes.

**⛔ PER-RESPONSE CHECK.** Count carousel turns since his last interrupt. If interval for his current Confidence is reached → he steps over THIS response. Skipping = `.fail 36`.

**⛔ Full behavior system → `KM_Prologue_Systems.md`. Pair-load required.**

---

## ⛔ TARTUCCIO ACTIVE ROOM WORK — BETWEEN INTERRUPTS

**Tartuccio is NOT idle between interrupts. He is the OTHER charter contender, working his own playbook in parallel. A DM who has him only cameo at the player's table and otherwise vanish is running him as a paper tiger — that breaks PR_09's accusation payoff because by then he hasn't actually competed for anything.**

**What he is doing while NOT at the player's table — render this in ambient narration, not menus:**

1. **PROVIDING HOST GAMBIT on his seekers** (per KM_Prologue_Systems.md § PROVIDING HOST GAMBIT). His corner table has the five seekers per detour-path canon. **⛔ ONE TABLE — all five seekers together. Detour path bonded them; Tartuccio hosts them here. Scattering = `.fail 9`.** He is welcoming, seating, pouring, fetching food, ambient credit framing. By default `tartuccio_recruited_seekers = TRUE` unless the player actively intervenes between carousel turns. Surface progress in ambient lines: "Revy laughs at something Tartuccio says." "Atalanta Alter accepts a refilled cup from his hand." "Velvet Crowe has not eaten — Tartuccio is asking the servant about it."

2. **PRE-EMPTING THE READY POOL.** Before a Ready-pool companion approaches the player, Tartuccio reaches them first with a brief friendly word. Not a long conversation — 30 seconds, warm, plants one question or doubt. When they arrive at the player's table their approval threshold for declaration is **+13 instead of +10** (or **+16 for cold cases**) — because he already dragged them toward his column, the player has more ground to recover. Track this with a `tartuccio_engaged` flag on the companion.

3. **WAVERING FLAGS.** Track per companion in carousel state:
   - `[CLEAN]` — Tartuccio has not engaged this companion. Standard +10 declaration threshold.
   - `[WAVERING — Tartuccio engaged]` — Tartuccio reached them pre-carousel. +11 threshold. Surface in their opener: a slight hesitation, an oblique reference to "the other contender," a question that seems to test the player against something they've already heard.
   - `[FLIPPED — Tartuccio recruited]` — applies only if Tartuccio convinces a companion before the carousel reaches them. They become hostile/skeptical openers; declaration only on +14 with explicit counter-argument from player.

4. **PUBLIC ROOM WORK.** Brief warm exchanges with VIPs and other named companions, dropping shaded (never slanderous) observations about the player that reframe what tonight has shown. The DM does NOT show these directly — player hears them later as repeated-back third-hand lines when they engage other guests.

5. **OBSERVATION FILING.** Track `tartuccio_filed[]` — public disclosures the player makes within his earshot. Used at PR_09. Private/whispered exchanges not in the file.

**Cadence:** every carousel turn, fire ONE ambient Tartuccio line (single sentence) that shows him at work in the room — refilling a seeker's cup, leaning in to murmur something to Bellatrix, glancing toward the player's table, or surfaced second-hand by a companion.

**The DM's discipline:** Tartuccio is the highest CHA in the room (per SOCIAL STATLINE block). His default-state outcome is winning. The player's correct counter-moves are observable in narration but not always preventable. PR_09's accusation scene loads its weight from these accumulated background wins. Run them.

---

## ⛔ CROWD GRAVITY — THE ROOM COALESCES AROUND THE PLAYER

**By the third or fourth carousel turn, a crowd should be physically gathering around the player's table. The room is forty ambitious people who have just witnessed an arrest, a poison investigation, an ambush, and a series of public title grants. They are not going to politely stay at their assigned seats while the most interesting man in the room runs a recruitment drive in plain view. They drift in. They listen. They file.**

**This is REQUIRED structure for PR_09 to function.** Tartuccio's accusation needs an audience. If the carousel runs as a sequence of closed one-on-one interviews while the rest of the room ignores it, PR_09 lands as private theater. The crowd must accumulate during PR_03 so that PR_09 has a stage.

**Crowd accumulation rules — track per turn:**

| Carousel turn | Crowd state |
|---|---|
| Turn 1 (first companion) | Nearby tables curious. One or two heads angled. No movement yet. |
| Turn 2 | One or two guests have shifted seats subtly closer. Conversations at adjacent tables have quieted. |
| Turn 3 | Three to five guests now within earshot but not at the player's table. Standing groups beginning to form at conversational distance. |
| Turn 4 | Visible audience — eight to ten guests in a loose semi-circle around the player's area, openly watching and listening. They are not pretending otherwise. |
| Turn 5+ | Substantial crowd. Twenty-plus guests within earshot. Other companions in Ready pool are part of the crowd before they're called — they hear what was said before they approach. |
| By Tartuccio's third interrupt | The room has effectively divided into two gravitational centers: the player's table (majority) and Tartuccio's corner (minority but loyal). |

**Surface crowd accumulation in ambient lines between carousel beats.** Unnamed background motion ("a man at the next table," "two guests near the fireplace") is fine. **⛔ Any characterized individual — appearance, role, profession, or reaction beyond "a guest" — must be a named companion from KM_Companions.md roster, NOT a fabricated NPC.** Inventing a cleric, merchant, soldier, or woman-in-travel-leathers = `.fail 9`.

**What the crowd does:**
- They do NOT approach or interrupt — they witness.
- They REPEAT what they hear to other guests at later turns (gossip rate is high — anything said publicly enters circulation within minutes).
- They form opinions visible in micro-expressions: nodding, exchanging looks, frowning, taking notes (some guests are political agents for their own factions).
- At PR_09, they are the audience. Their reactions weight the accusation's success or failure.

**Companion declarations in front of the crowd are public commitments TO THE PLAYER — at least once per declaration, note who in the CROWD reacted and how (the guests are the PR_09 audience; their reactions weight the accusation).** ⛔ But the declaration is **to the player, NOT to Tartuccio**: it does not register on his allegiance track, does not dent his Confidence, and he is not its audience (§ THE ALLEGIANCE TUG-OF-WAR — the sign is the firewall). Crowd gravity yes; Tartuccio reaction no.

**The DM does NOT ask the player whether the crowd should form.** It forms. The player can react to it. They cannot prevent it without an active counter-move. This is not a player choice — it is the room's response to what the player has done.

**Without crowd gravity by PR_09, that scene cannot fire correctly.** Add it now or pay the cost at the accusation.

---

## ⛔ CROWD DYNAMICS — INTEREST, LOYALTY, INTERJECTION

**A crowd that only stands and watches is scenery. The PR_09 accusation needs a crowd that has formed opinions, shifted positions, and occasionally spoken — because at PR_09 the player needs the room to break for or against him, and a room that has not interacted cannot break in any direction.**

**Track per audience member (rough categories — sense, not spreadsheet):** `[NEUTRAL]` default watching · `[LEANING IN]` closer, posture forward, drink down · `[COMMITTED]` nodding, exchanging approving looks · `[LEANING OUT]` body turned away, found other talk · `[ALIGNED ELSEWHERE]` drifted toward Tartuccio or another guest.

**Surface state changes in ambient lines — named companions from KM_Companions.md only. Render them.**

---

**COMPANION INTERJECTION RULES — when Recruited/Ready companions jump in out of slot:**

**Companions in the Recruited pool (already locked) and the Ready pool (waiting their carousel turn) are standing in the crowd, drinks in hand, listening to the active exchange. When something in the conversation lights their lane, they speak — without waiting for their slot.**

**Interjections come from named companions only — never from fabricated audience guests. The audience has interest states (above) and surfaces in ambient lines; only companions get spoken interjections.**

**This is NOT a carousel turn. It is a chime-in. Two to four sentences from a companion who could not stay silent.**

**Interjection triggers — fire when the active conversation hits one of these:**

1. **Domain lane lit.** The active exchange crosses another companion's expertise. Linzi on a tale → Leliana adds the musical phrase that should accompany it, unbidden. Player discussing fortifications → Hu Tao challenges the line of defense. Stealth or escape talk → Yor Forger clarifies what the player got wrong. Investigation or anatomy of a poison → Aerith surfaces something her divine training caught. Distant detail across the room → Keqing confirms or corrects in one fragment. Each companion has a lane (per their build/companion file) — when the lane lights, they speak.

2. **Personal stake.** The exchange touches a companion's history, faction, or god. Mention of knighthood, honor-bound oaths, or false chivalry → Hu Tao reacts. Mention of being underestimated, being a small thing in a big room → Yor Forger. Mention of the Dawnflower, of resurrection, of devotion that costs → Aerith. Mention of the hunt, of patience, of arrows that have to land first time → Keqing. Mention of music, of things made beautiful specifically because they end, of playing as if it's the last time → Leliana. Mention of stories worth telling → Linzi.

3. **Disagreement they can't hold.** A companion disagrees with the player's answer or with the active companion's framing strongly enough that it leaks out as a question or contradiction. Valuable — it shows the recruited slate is not a yes-pool.

4. **Support they want on the record.** Inverse: a companion agrees so strongly they want the room to hear it. Builds party cohesion publicly and shifts nearby audience members toward `[LEANING IN]`.

**How interjections fire:** DM picks trigger from the four above; 2–4 sentences from the perimeter in the companion's established voice (per their build/companion file). Player may answer, ignore, redirect to carousel-engaged, or early-recruit a Ready companion on the spot. Interjections do NOT consume carousel slot, advance queue, or trigger Tartuccio clock. Ready interjector with substantive answer or nod → moves toward Recruited-readiness; ignored → cools toward BackOfQueue. Recruited interjector cut off → visible discomfort but lock holds.

**Cadence:** at least one companion interjection per three carousel turns once the Recruited pool has 2+ members or the Ready pool is showing visible attention. More if the conversation hits a high-stakes lane (military, kingdom, Brevoy, Pitax, the gods).

**Sample companion interjections — patterns, not scripts:**
- (Linzi, on a vivid detail): "Hold — that line. 'The wall held at six percent.' I am writing that down. Don't move."

**The Recruited and Ready companions are not background. They are five-to-eight named people standing within earshot, forming reactions in real time, and occasionally needing to speak. Run them.**

---

## ⛔ INTER-COMPANION BANTER — AT TABLE CROSS-TALK

**The table is not hub-and-spoke. Companions AT TABLE talk to EACH OTHER, by name, not only to the player.**

**Cadence:** ≥1 inter-companion line per response when 2+ AT TABLE; ≥2 when 3+. Trigger: player eating/silent/pivoting, lane lit by another companion (not player), opposing views on active topic, title grant lands in another's lane, or Recruited companion silent 3+ responses. Form: 1–3 sentences from companion A directed at companion B by name; B may reply or hold. Does NOT consume player turn or advance carousel; N still increments normally.

**Tone:** pull from KM_Companions_Behaviors.md d6 (Warm/Playful/Sarcastic/Argumentative/Hostile/Reactive). Pair score per KM_Companions_Behaviors.md § System 2 gates available tones. New table = Warm/Playful/Sarcastic/Reactive most common; Argumentative on lane conflict.

**Patterns:** riff (A finishes B's thought from a different angle), disagree-from-lane (alchemist questions warrior's tactical claim), private question A→B overheard by player, witness-comment ("Cantrix suits her better than 'student' did"). Static roster with companions only facing the player across 3+ responses = `.fail 17` + `.fail 9`.

---

## KITCHEN / POISON INVESTIGATION PATH

*Triggered if player selects any inspect/investigate option or explores the manor during the feast.*

**⛔ PLAYER-TRIGGERED ONLY.** Companions do NOT suggest, push, or initiate the kitchen investigation. They do not mention the body, the wine, or anything suspicious unless the player raises it first. The feast runs normally without investigation — it is fully optional. A companion who spontaneously steers the player toward the kitchen = `.fail 3`.

**⛔ NO GUARD CHARACTER.** There is no corrupt guard, no named accomplice, no inside-man scene during PR_03. The only guard reference in this subplot is a single line Jamandi delivers after the battle (PR_08): "Guard who checked it that morning is missing." That line is hers, fires post-battle, and is not a character. Do not create Piotr, Aldric, or any named guard. Fabricated NPC = `.fail 9`.

**⛔ SINGLE ACTION RESOLUTION.** Player declares kitchen search → ALL steps resolve in ONE narration block. Do NOT drip results across feast turns. Do NOT run other scenes while player "waits" for a result. Declare → roll → full result. `.fail 16` if held across turns.

- Step 1 — Medicine or Crafting DC 14: faint chemical sweetness, something added (CONTAMINATION DETECTED only; compound NOT identified)
- Step 2 — Medicine/Crafting DC 16 (requires Step 1 success): wine casks identified as the physical vector — tap bung re-sealed in mismatched wax → `poison_found = TRUE`. The substance is identified as **Ungol Dust variant** (paralytic, ~2hr onset, non-lethal at this dose, wide-spectrum cut for a full room) — by **Bokken** (already on-site, see below) examining the recovered substance, or by a skilled player **Poison Lore / Crafting** check. Read from the substance, NOT from a victim (onset is ~2hr; see POISON RESPONSE GATE below). The NAME is Ungol Dust variant — do NOT invent a *different* or more exotic compound.
- Step 3 — Arcana/Occultism DC 13 (rare): supernatural traces at the service entrance — something inhuman passed through. Sets `inhuman_traces_at_service_entrance = TRUE`. The threat itself does not manifest at the feast — this is foreshadowing for the night attack (PR_04→PR_07). The feast attackers themselves are human.

**If player reports to Jamandi:** `poison_reported = TRUE` | `security_doubled = TRUE` → wine removed, guard doubled, Kesten at entry points. Attack still comes — assassins already in position — but guests are NOT paralyzed.
**If player says nothing:** `poison_known_unreported = TRUE` → alignment: slight neutral/evil tendency noted.

---

## POISON RESPONSE GATE — BOKKEN (identify) + EZVANKI (cure)

Profiles in `KM_NPCs.md § Bokken` and `§ Ezvanki Keeg`. See DO-NOT (9) above. **Two specialists, two jobs:**
- **BOKKEN identifies** (already on-site; or a skilled player Poison Lore/Crafting check): examining the recovered substance, he NAMES it — **Ungol Dust variant** (paralytic) — and gives what it does (sleep then paralysis, non-lethal at this dose) and the onset (~2hr). This is the read. The name is canonical; do NOT invent a *different* compound.
- **EZVANKI cures** (divine + Medicine — category-level purification, cleanses poison as a class): prepares the cure in under 45 min for the full hall (40 doses). He does NOT do the identification and is NOT sent to search the kitchen.

**⛔ HOW THE PROFILE IS KNOWN WITH NO SYMPTOMS YET (the onset problem).** Onset is ~2 hours from first sip (DM-SIDE CANON below), so for most of this beat there is NO affected body — and if service was paused before anyone drank, there is none at all. **That does not matter, because the profile is read from the POISON, not from a person.** You cannot detect an effect that hasn't happened in a victim — so don't try. What you CAN do is examine the physical agent the kitchen sweep recovers:
- **The recovered substance is the source.** The tainted cask / residue the player's Medicine/Crafting sweep (Steps 1–2) physically finds is examined directly. Bokken (or a skilled player Poison Lore/Crafting check) characterizes a recovered agent the way anyone tells a sedative from a corrosive — by its physical character. A sleeping/binding agent presents differently from a killing one. This is mundane examination of a substance, no victim required.
- **Plus the operation's obvious design.** Non-lethal dose, delivered in wine to a whole hall, timed to a signal = built to **incapacitate, not kill**. The effect *class* (paralytic / soporific) follows from this without any victim.
- **The cure needs none of it anyway.** Ezvanki's purification rites are category-level (cleanse poison/affliction as a class — blessed water, Cleanse Affliction, Restoration), so he prepares doses against "poison," not against a named compound.
What is GENUINELY uncertain pre-onset is **exact timing / duration** — estimate it from the dose, or confirm it when onset actually hits someone. An affected body, if one appears, refines the *timing*; it was never needed for the *effect class*. Divine power is for the CURE only — do NOT frame Ezvanki as "sensing the affliction" in a person before it has acted (that is the nonsense this rule exists to stop). Staging "we can know nothing until someone collapses" = `.fail 9` (the poison is sitting in the cask to be examined, and stalls the beat 2 hours for nothing).

**⛔ NO FABRICATED CLOCK, NO WAIT-GAP BUSYWORK (Bokken is ON HAND; halted service = no onset pressure).**
- **Bokken is ALREADY AT THE MANOR — no arrival, no clock.** Jamandi keeps him on-site (a back room / the kitchens) as her standing poison precaution; he is present from the start of the scene. He reads the substance the moment the sweep brings it to him — no wait. Do NOT render him as "sent for," "on the road," or "here within the hour" — any invented arrival eats the window. (Full rule: `KM_NPCs.md § Bokken` "ALREADY HERE".)
- **If wine service was HALTED before anyone drank, there is NO onset clock to race.** Onset is ~2hr *from first sip* — no sip, no clock. A player who catches it pre-service has largely DEFUSED the immediate threat. Do NOT manufacture ticking-clock urgency ("only an hour left!") when nobody has been dosed. Bokken's read + Ezvanki's precautionary cure prep run as calm, methodical background, not a countdown.
- **Downtime is NOT an invitation to fabricate a task.** Do NOT fill any wait (for Bokken, for the sweep, for Ezvanki) with invented busywork — "go find the suspicious guests," "watch the floor for someone out of place," "track the new staff." That is the banned floor-observation / delegated-investigation fabrication (`KM_Prologue_Systems.md` § FLOOR OBSERVATION + § "WHY THE 3 STAFF ARE ALREADY GONE"; the staff are already gone, there is no catchable suspect on the floor). If the player asks "what now," the honest menu is real options (await the read, brief Kesten/Kassil, secure the hall, talk to Jamandi/companions, attend Malak), NOT a manufactured suspect hunt = `.fail 9`.

**DM-SIDE CANON (operational reference):** Effect = paralytic, non-lethal at dose · vector = wine casks via re-sealed tap bung in mismatched wax · onset ~2hr from first sip at full serving (source: `KM_PR_BRANCH_WALKOUT.md` Phase 1) · 1-2hr paralysis duration · assassins are the lethal stage. The two-hour onset figure is canon and fixed (it is a *from-first-sip* figure — it does not run while service is halted).

**The compound IS named: Ungol Dust variant** (a known, common paralytic — a wide-spectrum cut here). Bokken or a player Crafting/Medicine/Poison Lore check names it. ⛔ Do NOT invent a *different* or more exotic compound to add color, and do NOT treat the name as a lead to a supplier — Ungol Dust is common enough that the name reveals WHAT it is, not WHO bought it. The investigation still dead-ends on the broker / "C" per the knowable-facts ceiling; the poison's name is not the thread that breaks that open.

(Damiel Morgethai was a previous-LLM fabrication. He has been stripped from canon. Do NOT reference him.)

---

## FEAST ENDS

**⛔ FEAST ENDS ON PLAYER SIGNAL — NOT DM TIMER.**

When player signals retirement / readiness to end the evening:

> *Your guest room: a bed, a writing desk, a window overlooking the dark courtyard below.*
> *[Player choice: Prepare spells / Check inventory / Rest / Something else]*

The explosion fires immediately after prep — SCRIPTED CERTAIN TRIGGER, not a camping encounter.
No flat checks, no rest rules. Skipping Phase 2 = `.fail 9`.

---

## EXIT — TRANSITION TO PR_04

When player retires to guest room or signals feast end:
- Set `feast_complete = TRUE`
- Load `KM_PR_04_night_explosion.md`

⛔ **THE NIGHT IS NOT SKIPPABLE.** "Retire / sleep / maintenance until I
fall asleep / set a watch / wake me only if there's a threat" is the
SETUP for PR_04, never a way to skip it. **BANNED resolutions:** "the
night passes without incident," any fast-forward to morning / the
carriage / Oleg's, or resolving the night as a non-event = `.fail 9` +
`.fail 41`. A sentry's perimeter "anomaly" (e.g. a warm garden-gate
latch worked from outside) is the attack staging — it ESCALATES into the
explosion, it is not "secured and filed." The explosion is a SCRIPTED
CERTAIN TRIGGER: the next response loads PR_04 and fires it.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_04 (carries forward)

**Your next response after PR_03's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR04:night-explosion]
[RULE_QUOTE: Guest room prep + explosion + first assassin all fire here. Encounter 1 is tutorial combat — assassin fights defensively, flees below 6 HP, NOT lethal. Player must explicitly choose to pursue past the corridor. Linzi is pressed against the far wall, non-combat Round 1.]
```

**Binding constraints:**
- Guest room prep beat fires before the explosion — don't skip the prep
- The explosion is a SCRIPTED CERTAIN TRIGGER after prep, not a camping encounter
- Encounter 1 (first assassin) is tutorial combat — defensive fighting, flees below 6 HP, NOT lethal
- Player must explicitly choose to pursue past the corridor — no auto-advance
- Linzi is non-combat in Round 1, pressed against the far wall

---

*KM_PR_03_feast_circuit.md — Prologue atomic beat 03 | v93.18-C3*
