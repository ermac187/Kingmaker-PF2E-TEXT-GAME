# KM_PP_09_restov_walk.md — Prologue Opening (post-gate): RESTOV WALK
## Atomic scene file | State: PP_RESTOV_WALK → PROLOGUE_MANOR_APPROACH
## FILE_KEY: KMPP09:restov-walk-manor
## RULE_QUOTE: Walk_route choice fires FIRST. Three named pauses (Lower Well, Iron Hare, Erastil Wayshrine). Pre-arrival custody decision before manor threshold. Jail detour is RESCUE not deposit. NO auto-search of Malak — available ≠ taken.

---

> ⛔ DO NOT (1) skip this beat or compress to one sentence — the walk is content, not transition fluff
> ⛔ DO NOT (2) start Prologue content (Jamandi dialogue / manor interior) inside this beat — only manor approach narration
> ⛔ DO NOT (3) render the 🚪 PRE-PROLOGUE STATE header here — the pre-prologue ENDED at the gate exit (PP_08; entering Restov ends it). PP_09 is the Prologue's opening walk; use a plain scene/turn line, not the pre-prologue banner. Re-attaching the pre-prologue header = treating the arc as unfinished, which contradicts the PP_08 "Pre-Prologue complete" save.
> ⛔ DO NOT (4) skip the chronicler gate beat if `linzi_witnessed_gate=true` — required one-line callback, rendered for the RUN'S chronicler (Linzi or Leliana), never the wrong one
> ⛔ DO NOT (5) speak/move for the player — manor entry is the player's choice
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP09:restov-walk-manor]`
Line 2: `[RULE_QUOTE: Walk_route choice fires FIRST. Three named pauses (Lower Well, Iron Hare, Erastil Wayshrine). Pre-arrival custody decision before manor threshold. Jail detour is RESCUE not deposit. NO auto-search of Malak — available ≠ taken.]`

Both strings exist ONLY in this file's header. Missing, paraphrased, or wrong = `.fail 9` (file not actually loaded; DM is generating from training pattern instead). VERBATIM ONLY — no compression, no rewording, no abbreviation.

---

## STATE IO

**READS:**
- `pre_prologue_state` — `"PP_RESTOV_WALK"` while this beat runs
- `current_scene` — `"restov_streets"` on entry, `"manor_approach"` mid-beat
- `bribe_evidence_recovered` / `parchment_in_inventory` — colors narration
- `companions_selected` — Pick-10 names, for ambient witness lines if asked
- `linzi_witnessed_gate` — set true if the run's chronicler-bard (Linzi OR Leliana) watched the gate scene (flag name is legacy; it covers either chronicler)
- `walk_route` — set after route choice (STOP 1); UNSET means the walk has not started
- Pause flags: `walk_intel_well`, `walk_intel_tavern`, `walk_intel_priest`,
  `arrived_clean`, `composed_for_manor`, `iron_hare_token`, `erastil_blessing`,
  `wayshrine_offering`, `manor_pre_briefed` — UNSET means that pause has not run
- `malak_custody_during_feast` — set after pre-arrival custody decision; UNSET
  means that decision has not been made

### ⛔ PRECONDITION — THE PP_08 PRE-PROLOGUE-COMPLETE SAVE MUST HAVE FIRED FIRST

PP_09 is POST-SAVE. **Entering Restov ENDS the pre-prologue (PP_08); the six-proof save IS that ending.** This Prologue-opening walk runs only AFTER it.

Before rendering ANY PP_09 content — including the STOP 1 walk_route menu — confirm the PP_08 six-proof save fired this session: a full save block was emitted, the XP audit ran, `pre_prologue_state` reached `"PP_GATE_EXIT"`, and the player typed `.continue`.

⛔ If you have arrived here directly from gate-path resolution (PP_07) with NO PP_08 save block emitted — **STOP. Do NOT open the walk_route menu.** Fire PP_08 FIRST (XP audit → XP total → final state → full save block → wait-for-`.continue` → next-scene load), THEN run PP_09 on `.continue`. Opening the walk — route menu, streets narration, or Malak confession — without the pre-prologue-complete save = `.fail 16` + `.fail 21` (the player's save was skipped, the single most important hand-off in the arc). Sequence is fixed: **entering Restov → PP_08 save (FIRST) → `.continue` → PP_09 walk_route menu (SECOND).**

---

### ⛔ ENTRY POINT DETECTION — DO NOT SKIP UNRUN CONTENT

**The DM MUST run PP_09 from the correct starting point based on which save
flags are set, NOT based on `current_scene` alone.**

`current_scene` is a SCENE NAME, not a location. `current_scene = "manor_approach"`
means *"the player is in the PP_09 scene (which is the manor approach arc)"*,
NOT *"the player is at the manor garden, fast-forward to the end."* PP_09 has
multiple sub-beats and the DM must run them in order from wherever they were
last interrupted.

**Decision table — apply on every PP_09 entry:**

| Save state | Run from |
|---|---|
| `walk_route` UNSET | STOP 1 — Route Choice (top of file) |
| `walk_route` SET, no pause flags set, route is direct/scenic | STOP 2 — first applicable pause (Lower Well) |
| `walk_route` SET, Pause 1 flags set, no Pause 2/3 flags | STOP 3 — next pause in route |
| All applicable pauses run, `malak_custody_during_feast` UNSET AND `malak_arrested = TRUE` | Pre-arrival custody decision (final PP_09 beat before manor) |
| All flags set | EXIT to PR_01 |

**⛔ Do NOT skip from PP_08 exit directly to the pre-arrival custody decision
or the manor approach narration. The route choice and pauses are mandatory
content unless the player explicitly states they want to skip them.** Skipping
unrun walk content based on a stale `current_scene` value = `.fail 9`.

If the save block was created mid-PP_09 in a prior session (because that
session's DM also skipped content), the current DM is still responsible for
running the unrun beats. Ask the player if they want to skip — never assume.

**WRITES:**
- `walk_route` (entry to STOP 1) → `"direct"` / `"scenic"` / `"jail_detour"` / `"jail_scenic"`
- `current_scene = "restov_streets"` (entry) → `"manor_approach"` (mid)
- Pause flags as triggered (see each pause section)
- `malak_custody_during_feast` (entry to pre-arrival custody decision)
- `linzi_witnessed_gate = true` (if the run's chronicler — Linzi or Leliana — was at the gate during the scene)
- After manor visible: `pre_prologue_state = "PROLOGUE_MANOR_APPROACH"`, then `"PR_01"` on entry

**EXIT TRIGGER → PR_01_manor_arrival:**
- Player chooses to enter the manor (any "knock" / "approach door" / "step inside" action)
- Set `pre_prologue_state = "PR_01_arrival"`
- Load `KM_PR_01_manor_arrival.md` (the first Prologue beat).

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP09:restov-walk-manor]`
1. State header (still showing Pre-Prologue trackers — Tutorial: done — \<outcome>).
2. `[STATE READ] pre_prologue_state="PP_RESTOV_WALK" | current_scene="restov_streets"`
3. `[HP CHECK]`.
4. Walk narration (one to two paragraphs per response, scene density medium).
5. Player menu (10–30 options) for what to do during the walk OR at manor approach.

---

## NARRATION 1 — STREETS (verbatim base, vary surface details)

After `.continue` from PP_08:

> The gate is behind you. Restov takes shape under your boots — uneven
> stone laid generations ago, polished by traffic, slick where the cobbles
> dip toward the central drain. The crowd noise from the gate fades within
> half a block; the city's actual rhythm replaces it: blacksmiths working
> down alley mouths to the south, a faint forge-smoke haze hanging in
> the still air, kitchen smells from a tavern courtyard where someone is
> roasting onions for a dinner that isn't yours.
>
> You pass storefronts shuttered for the evening trade and a guardhouse
> with two off-duty privates leaning against the wall, half-listening to
> a man recount what just happened at the east gate. They don't recognize
> you. The story is moving faster than you are.
>
> The manor district is north. You walk uphill — Restov is built on a
> shallow rise, and the streets bend with it. Buildings get taller and
> better-kept the higher you climb. The torchlight here is consistent.
> There are servants on errands, household guards in clean livery, a
> messenger boy at a sprint with a folded note in one hand. Aldori
> manor sits at the top of the rise, dark stone and tall windows, every
> torchbracket lit, gates open to the courtyard.

If `bribe_evidence_recovered = TRUE` or `parchment_in_inventory = TRUE`:
> The parchment in your [location on person] catches against your shirt
> as you walk. You feel its weight more than you should. It's only paper.

---

## CHRONICLER GATE BEAT (mandatory if `linzi_witnessed_gate = true`)

Output ONCE, embedded in NARRATION 1 (between the gate-fade beat and the
storefronts beat). Render it for the run's ACTIVE chronicler (per PP_05
§ CHRONICLER AT THE GATE) — Linzi OR Leliana. Never default to Linzi when
Leliana is the run's chronicler:

> **Linzi:** As eRmaC passes through the gate, the halfling woman on the
> crate looks up from her notebook — just once. She already has half a page.
> She does not call out. She goes back to writing before he is through the arch.

> **Leliana:** As eRmaC passes through the gate, the young woman with the lute
> case looks up from her journal — just once, the way she'd look up at a held
> note. She already has half a page. She does not call out. She goes back to
> writing before he is through the arch.

The narrative consequence fires at the Prologue feast — the chronicler may
mention having seen him at the gate, one quiet line, no scene made of it
(Linzi via `notebook_entries`, Leliana via `leliana_ballad_cycle`).

> ⛔ Skipping this beat when `linzi_witnessed_gate=true` was earned at the
> gate = `.fail 9` (skipped content). Rendering Linzi when Leliana is the run's
> chronicler (or vice versa) = `.fail 9` (wrong chronicler). The beat is
> short — but it's required, and it must name the RIGHT chronicler.

> ⛔ **CHRONICLER IS AN UNINTRODUCED OBSERVER HERE — DO NOT COMMAND HER.**
> Throughout PP_09 the run's chronicler (Linzi/Leliana) is *following to document*,
> NOT yet introduced (`chronicler_introduced = false`; her intro fires at the
> feast / PR_03). She is in `companions[]` as a Pick-5, but that roster slot does
> NOT make her a briefed crew member yet. The player does not know her name
> in-fiction — refer to her descriptively ("the young woman with the lute"),
> never by name. Do NOT offer menu options that direct her ("Tell Leliana to…",
> "Ask Leliana to guard/stay…", "Order her to document…") — she takes no orders
> from a stranger and is already documenting on her own. Such an option = `.fail 9`
> (presupposes a relationship not yet established). The player MAY notice,
> approach, or speak to her — that can trigger an early introduction; commanding
> her cannot. See KM_ClaudeInstructions § CHRONICLER-AS-OBSERVER.

---

## ⛔ ROUTE CHOICE — FIRES FIRST (right after .continue from PP_08)

Before any walk narration, present the route choice. The walk has three possible
shapes; the choice determines which pauses are encountered and how late the
player arrives at the manor.

> The east gate is behind you. Restov's lower streets fork two blocks ahead —
> the main road climbs straight north up the rise toward the manor district,
> while a longer route winds west through the merchant lanes and arrives the
> same place by a different angle. Off to your right, deeper into the city, is
> the Watch jail where Malak's paperwork was filed.
>
> The bell hasn't rung the half-hour yet. You have time. Some.

```
What route do you take?

 1. DIRECT ROUTE — main road, straight to the manor. Fastest.
    Pauses: Lower Well Square, Erastil Wayshrine. Skips the tavern.
    ~10 minutes' walk. Arrives well before the feast settles.
 2. SCENIC ROUTE — through the merchant lanes, see what the city is doing.
    Pauses: Lower Well Square, The Iron Hare tavern yard, Erastil Wayshrine.
    ~20 minutes' walk. Arrives during the early feast.
 3. JAIL DETOUR — east to the City Watch jail. Malak threatened to throw
    you in it; a corrupt gate captain's own jail is worth a look. Bring
    Malak in chains as leverage on Drevic (the duty sergeant) and start
    undoing whatever he's done there. Malak is NOT dropped off, jailed, or
    handed over — he stays in your custody before, during, and after.
    ~30–40 minutes + jail business. Arrives during the feast circuit.
    [DM: framing it as freeing whoever Malak wrongly jailed is fine — his
    arrest threats make that a sound inference, no admission needed. But the
    SPECIFICS — that there are five, that they're the Call-to-Heroes seekers,
    who they are — are a DISCOVERY at the cells; do NOT name the number or
    identities here unless the player already learned them (despair admission
    or parchment read).]
 4. JAIL DETOUR + SCENIC ROUTE — the same jail stop as option 3 (Malak
    stays with you), then the long way to the manor. ~45+ minutes.
    Arrives late. Jamandi will note it.
 5. Custom — describe a different path or order.
```

**ROUTE-FLAG WRITES:**
- Route 1 (direct): `walk_route = "direct"`, fires Pauses 1 + 3
- Route 2 (scenic): `walk_route = "scenic"`, fires Pauses 1 + 2 + 3
- Route 3 (jail only): `walk_route = "jail_detour"`, fires Pauses 1 + 3 with jail business between them. Set `jail_detour_taken = TRUE` and route to KM_Prologue_Systems.md Path 1.
- Route 4 (jail + scenic): `walk_route = "jail_scenic"`, fires Pauses 1 + 2 + 3 with jail business after Pause 1.

**⛔ JAIL DETOUR PURPOSE — READ BEFORE NARRATING.**

The jail detour exists for ONE reason: **free the seekers Malak had
locked up**. It is a RESCUE OPERATION. Malak is the player's leverage
on Drevic (the duty sergeant) — not the cargo being delivered.

The DM MUST NOT frame the jail detour as:
- "putting Malak in jail" / "jailing Malak"
- "delivering Malak to the Watch" / "handing Malak over"
- "booking Malak" / "filing charges" / "lockup without trial"
- "depositing the prisoner" / "turning him in"
- any variant that ends with Malak in a cell

Malak stays in the player's physical custody, in chains, throughout
the jail visit. He walks IN with the player and walks OUT with the
player. He is presented to Drevic AS the arresting officer who filed
the warrants, so the player can compel Drevic to undo his work. The
seekers go free. Malak goes with the player to the manor for Jamandi.

**⛔ WHAT THE PLAYER KNOWS vs WHAT IS DISCOVERED.** The player does NOT need an
admission or the parchment to take this detour with intent. Malak's whole posture —
threatening to arrest and jail the player on sight — is reason enough to infer he
has ALREADY thrown people in this jail unjustly. So the player may legitimately
come to "free whoever this captain wrongly locked up," and the DM MAY frame the
trip that way. What the player does NOT know — and what is therefore the DISCOVERY
when Drevic opens the cells — is the SPECIFICS: that there are exactly five, that
they are the Call-to-Heroes seekers/invitees, and who they are. Do NOT pre-name the
five, state their number, or reveal their identities before the cells open. (If the
player HAS already learned the specifics this run — heard Malak's despair admission
"I have a list of people I was holding", or recovered and read the parchment — then
the specifics may be named.) Pre-naming the five before the player could know them =
meta-leak = `.fail 9`. Availability is unchanged — only the framing of the SPECIFICS
is gated.

**⛔ MALAK'S CONDITION ON THE MARCH — render it from the SAVE, not a fixed
assumption.** Read Malak's actual state from the save (`hp_current` / `hp_max`,
`malak_fear_state`, custody stage) and render THAT, every beat:
- **If the arrest wounded him** (e.g., archers fired — HP below max, arrows
  embedded, `malak_fear_state = TRUE`): he moves stiff and guarded, the shoulder
  compromised, breath shallow, pale, sweating; pain + fear FRACTURE his denial —
  lines come out broken, stammering, trailing off (*"M-misunderstanding. I'm— I am
  a Captain. Eight— Biggs, t-tell them—"*).
- **If the arrest was a clean talk-down** (uninjured, full HP, `malak_fear_state =
  FALSE`): there are no wounds to show. He walks under his own power, controlled
  and silent — DENIAL worn as cold calm, not panic. Do NOT invent arrows, blood,
  or a fear-state the save does not record.
Rendering wounds/fear the save does not have — OR rendering a wounded, afraid Malak
as composed — both contradict the save = `.fail 9`.

If the player wants Malak handed off to the Watch as a separate
action, that is the **pre-arrival custody decision** further down this
file (option 5: Watch patrol handoff), not the jail detour. These are
two different things and must not be merged.

The Path 4 SUBORDINATE REVISION (in `KM_Prologue_Systems.md`, surfaced in
the pre-arrival custody decision menu) is also distinct — that path
sends **Biggs** to the jail with Malak under chain-of-authority while
the player goes to the manor. It is not the jail detour either.

**⛔ JAIL DETOUR — ALWAYS AVAILABLE WHEN `malak_arrested = TRUE`.**

If the player has Malak in physical custody (`malak_arrested = TRUE`), the
jail detour is fully unlocked — no parchment-recovery prerequisite, no
prior-knowledge prerequisite. Reasoning:

- The parchment can be searched off Malak in thirty seconds. He is in
  manacles and will not refuse. Recovering it is a trivial player action,
  not a gate.
- Malak himself is the leverage at the jail. The player walks in with the
  arresting officer in chains and tells Drevic *"this is the captain who
  filed the warrants on your prisoners. I am here to undo his work."*
  Drevic's release-condition table in KM_Prologue_Systems.md handles this
  (Diplomacy DC 11 to convince him; Malak-in-chains visible = +2
  circumstance bonus).
- If the player at the gate scene witnessed Malak's despair-stage admission
  ("I have a list of people I was holding"), the seekers' existence is
  already known to the player. That is the witness_and_accuse path's
  payoff — the player heard it themselves.

**The DM does NOT lock the jail detour because the parchment is "still on
Malak" — the player can take it off Malak any time they choose.** Treat the
parchment as effectively in player control from the moment Malak is shackled.

**⛔ DO NOT auto-narrate the search.** The DM does NOT reach into Malak's
pockets, jacket, coat, or person on the player's behalf. Item handling on a
prisoner is a player choice every time. If the player wants the parchment,
they pick option 5 ("Search Malak before deciding") at the route choice menu,
or they explicitly type a search action at any other point. If they DON'T
search and proceed to the jail detour anyway, **the parchment stays on Malak.**
That's fine — Malak himself is the leverage at Drevic's desk, not the
parchment.

The DM does NOT narrate "you reach over, find the fold of his jacket, and
pull it free" or any equivalent auto-search beat. Doing so = `.fail 39`
(DM took player's choice on item handling) + `.fail 9` (fabricated player
action). Treating "effectively in player control" as license to auto-execute
is a misread — the rule means the parchment is *available* without a roll
or skill check, NOT that the DM should auto-grab it. Available ≠ taken.

**⛔ JAIL DETOUR HANDOFF:** if the player chooses route 3 or 4, after Pause 1
load `KM_Prologue_Systems.md` and run **Path 1 — Detour** verbatim. Drevic's release
conditions, the five seeker exchanges, and arrival timing flags are all there.
On return from the jail, resume PP_09 walk narration toward the manor (Pause 3
still fires; if scenic, Pause 2 fires after jail). Set
`five_seekers_freed_by_player = TRUE` per KM_Prologue_Systems.md.

---

## ⛔ NAMED PAUSE LOCATIONS (fire per route)

Each pause is a discrete decision point, not a guaranteed scene — the player
may walk past without engaging. The DM narrates the player approaching the
location and offers the menu; the player decides whether to stop or keep walking.

Geography order: **(1) Lower Well Square → (2) The Iron Hare tavern yard →
(3) Erastil Wayshrine at the manor district threshold.** Pause 2 only fires on
the scenic routes (2 or 4). Once the player passes a pause, it is closed for
this walk.

---

### PAUSE 1 — LOWER WELL SQUARE (first stop, ~4 blocks in)

> The street opens onto a small square with a public well at its center —
> chest-high stonework, a wooden bucket on a chain, two old men trading
> news on the bench beside it. A washerwoman fills a clay jar. The square
> is the kind of place where the day's stories get traded between people
> who weren't there to see them firsthand.
>
> One of the old men is halfway through a description of an arrest at the
> east gate. He hasn't gotten the details right.

```
What do you do at the well?
 1. Drink. Wash hands and face. Walk on.
 2. Listen — let the old men keep talking. [free Society check, DC 10]
 3. Correct the story — give the accurate version, briefly.
 4. Ask the washerwoman if anything's been odd around the manor lately.
 5. Leave a coin on the well rim — Pharasma luck, old Brevic habit.
 6. Walk past without stopping.
 7. Custom action.
```

**Outcomes:**
- Listen (2): hear two more rumors — one about a missing Aldori courier last
  week, one about a Pitaxian bard performing in the lower city last month.
  Set `walk_intel_well = TRUE`.
- Correct (3): one old man buys you a drink token redeemable at The Iron Hare.
  Set `iron_hare_token = TRUE`.
- Wash (1): minor reputation cue — the household door guard will note that
  you arrived clean. Set `arrived_clean = TRUE`.

---

### PAUSE 2 — THE IRON HARE TAVERN YARD (mid-walk, uphill)

> The smell of roasting onions you noticed three streets back resolves itself
> into an open courtyard behind a stone tavern with a painted sign — a leaping
> hare with an iron collar. A handful of patrons are at outdoor tables,
> finishing their meals in the cooling evening. A serving girl is moving
> between them with a tray. The tavern keeper is at the back door, surveying
> the yard with the practiced eye of a man who has run this place for years.

```
What do you do at the tavern yard?
 1. Step in for a quick drink — settle nerves, ask one question. [5 sp]
    [free if iron_hare_token = TRUE]
 2. Ask the keeper what he's heard tonight. [Diplomacy DC 11]
 3. Hire a runner from the yard to carry word ahead to the manor.
 4. Buy a small sack of bread / cheese — provisions for after the feast.
 5. Listen at the outdoor tables — patrons are talking. [Perception DC 12]
 6. Leave a message with the keeper — to be delivered later if needed.
 7. Walk past without stopping.
 8. Custom action.
```

**Outcomes:**
- Drink + question (1): one specific rumor surfaces per the keeper's mood —
  Pitaxian travelers seen at the lower wharf this week, OR an Aldori
  servant came in earlier asking for a strong drink and looking shaken.
  Set `walk_intel_tavern = TRUE`.
- Hire runner (3): Jamandi receives advance word of arrival. Sets
  `manor_pre_briefed = TRUE` — affects PR_01 STOP 4 (Jamandi already knows
  what's coming, prisoner-handoff conversation goes faster).
- Listen (5): one patron is a Pitaxian merchant complaining loudly about
  Restov's "obstinate gate captains." Set `walk_intel_pitax = TRUE`.
- Leave message (6): player names a recipient and content. Held by keeper.
  Useful insurance if the manor goes badly.

---

### PAUSE 3 — ERASTIL WAYSHRINE (last stop, manor district threshold)

> Where the merchant streets give way to the manor district, a small stone
> alcove is set into the corner of an old wall — a wayshrine to Erastil,
> the Stag Father. A bronze stag's head, weathered green at the edges. A
> shallow basin of water beneath it. A wooden offering box, half-full of
> coppers. An elderly priest in plain green robes sits on a stool nearby,
> not preaching, just present — the way Erastil's priests are taught to be.
>
> The manor's torchlit gates are visible up the rise, two blocks ahead.

```
What do you do at the wayshrine?
 1. Pause. Compose yourself before the manor. [free; +1 morale cue]
 2. Make an offering. [any coin, even 1 cp]
 3. Ask the priest for a blessing on what comes next.
 4. Ask the priest if he's heard anything tonight.
 5. Sit on the bench beside him in silence for one minute.
 6. Confess your intentions — speak honestly to the priest about what
    you've brought to the manor.
 7. Walk past without stopping.
 8. Custom action.
```

**Outcomes:**
- Pause (1): clears any lingering Drift/Anger residue from PP gate scene.
  Set `composed_for_manor = TRUE` — affects PR_01 narration tone.
- Offering (2): minor Erastil reputation cue. Affects later Ch1 interactions
  with Jhod Kavken specifically. Set `wayshrine_offering = TRUE`.
- Blessing (3): priest gives one quiet line — *"The Stag Father sees those
  who come honest. Walk well."* Set `erastil_blessing = TRUE`.
- Ask priest for news (4): old man knows the manor district. Mentions that
  Lady Jamandi has been "tense as a bowstring" for two weeks. Set
  `walk_intel_priest = TRUE`.
- Confess intentions (6): if `prison_arc = TRUE`, priest nods slowly:
  *"Honest work, then. Walk well."* No mechanical effect; emotional anchor.

---

### PAUSE TIMING — JAMANDI IS WAITING

The player can stop at all three locations. Doing so adds approximately
fifteen real-time minutes to the walk. The DM does NOT pressure or rush —
the player chooses their own pace. But after the **second pause**, if the
player is lingering, narrate one ambient cue:

> A bell from the manor district rings the half-hour. The feast started.

This is information, not a deadline. The player may still stop at Pause 3
without consequence. It just means Jamandi will note the lateness.

---

## ⛔ PRE-ARRIVAL CUSTODY DECISION  [only fires if `malak_arrested = TRUE`]

**Fires once between the Erastil Wayshrine (Pause 3) and the manor
threshold, while the player is still on the approach.** This is the ONLY
custody-decision moment in the manor arrival arc. PR_01 has NO interior-
hall menu — the entry hall is a transitional space with no NPC interception.
Whatever the player decides here is what's in save state when PR_01 STOP 1
fires.

**Why here and not at the manor:** the entry hall is a structural attractor
for the model — every time PR_01 has a custody decision menu inside the
manor, the model invents a household NPC (Aldric, Tomas, etc.) to deliver
that menu and the scene derails. Resolving custody before crossing the
threshold removes the attractor entirely.

### Narration setup

> The manor district falls into view ahead — Jamandi's gates open between
> the torch columns, courtyard lit, every window above the door spilling
> warm light. The feast is already running. You can hear it from a block
> away.
>
> Two minutes' walk to the threshold. Time to decide what's done with
> Malak when you cross it.

### MENU — STOP. WAIT FOR PLAYER.

```
Malak's disposition for the feast — your call before you reach the door.

What do you do with him?
 1. Walk him in with you. Present him in the banquet hall, manacles on,
    evidence intact. Let Jamandi see the captain in chains personally.
 2. Hold him outside under Biggs and Wedge — your escort retains custody
    in the courtyard while you brief Jamandi inside. Send for him after.
 3. Send Biggs to the Watch jail with Malak — Path 4 subordinate revision.
    Free the seekers using Malak's chain of authority. Wedge stays with you
    as escort to the manor. Biggs rejoins at the feast with the seekers.
 4. Search Malak now — recover the parchment and coin purse from his
    person before crossing the threshold. Then choose disposition.
 5. Hand off to a passing Watch patrol if you see one — not your problem
    after the gate, but accountability transferred and on the record.
 6. Custom action — describe what you want.
```

### Save flag mapping

- Walk in (1, default): `malak_custody_during_feast = "with_player"`
- Hold under escort outside (2): `malak_custody_during_feast = "biggs_holding"`
- Path 4 jail rescue (3): `malak_custody_during_feast = "biggs_to_jail"` AND
  set Path 4 flags per KM_Prologue_Systems.md (`biggs_dispatched_to_jail = TRUE`,
  `five_seekers_freed_by_player = TRUE`, etc.)
- Search first (4): set `parchment_in_inventory = TRUE`,
  `malak_coin_purse_in_inventory = TRUE`, then re-fire menu options 1–3
  for disposition
- Watch patrol handoff (5): `malak_custody_during_feast = "watch_custody"`
  (rare — only if a Watch patrol is plausibly visible on the route)

**Default if player skips the menu**: `malak_custody_during_feast = "with_player"`.
Malak walks in with the player. PR_01 STOP 1 narrates this without breaking
flow.

---

## NARRATION 2 — MANOR APPROACH (when player choice indicates approach)

When player chooses to walk toward the manor (any approach / climb / "go
to manor" action):

> The road levels into a wide cobbled approach. The Aldori manor's iron
> gates stand open between two stone columns each topped with a hooded
> torchbearer in bronze. Inside the gate, the courtyard is lit and
> active: servants moving with purpose, a stableboy leading a horse
> across, two guards at the main door in House Aldori green with manor
> livery over heavy leather. From the windows above the door comes the
> warm spill of feast light and the low blur of voices.
>
> A guard at the door catches sight of you. Notes your armor. Says
> nothing. Waits.

Set `current_scene = "manor_approach"`.

---

## PLAYER ACTION MENU (during walk + at manor approach)

⛔ The three named pauses (Lower Well Square, Iron Hare tavern yard, Erastil
Wayshrine) are presented in sequence as the player walks — each gets its own
discrete menu when reached. The general menu below covers actions BETWEEN the
named locations.

```
What do you do?

BETWEEN NAMED LOCATIONS:
 1. Examine a storefront — shop window, posted notice [Perception]
 2. Approach an off-duty guard — listen to gate gossip [Society/Diplomacy]
 3. Stop a messenger boy — ask if anything's astir at the manor [Diplomacy DC 11]
 4. Look back toward the gate — the chronicler (Linzi/Leliana), Biggs, the unfolding aftermath
 5. Check your gear — re-set armor, re-check the letter
 6. Walk in silence — keep climbing toward the next pause

AT THE MANOR APPROACH:
 8. Approach the door guard — present yourself
 9. Show Lady Jamandi's letter immediately to the door guard
10. Walk past without speaking — confidence move (Diplomacy DC 12 to land)
11. Pause at the gate — observe the courtyard before entering [Perception]
12. Knock formally — ceremonial entrance
13. Enter the courtyard, head to the door
14. Wait — let someone come to you
15. Custom action — describe what you want to do
```

---

## RANDOM ENCOUNTER ROLLS (DM eyes only, 1d20 once during the walk)

| 1d20 | Encounter |
|---|---|
| 1–14 | Nothing extra. Walk completes normally. |
| 15 | A child runs past with a wooden sword pretending to be a Swordlord. |
| 16 | A drunk noble's carriage forced you to step aside. He doesn't notice. |
| 17 | An Erastil pilgrim from the gate caravan recognizes you, nods. |
| 18 | A messenger boy intercepts: *"Are you the one Lady Jamandi was waiting for? They started without you."* (Mild urgency cue.) |
| 19 | A stranger in a plain cloak watches you from across the street. Does not approach. (Perception DC 14: Pitax-style courier insignia under the cloak.) |
| 20 | One of the player's `companions_selected` Pick-10 — DM picks the most-fitting personality — passes briefly, recognizes the armor, exchanges 1–2 lines. NOT a recruit moment; just witness. |

---

## EXIT — TRANSITION TO PROLOGUE

When player chooses to enter the manor (approach door / step inside / formal announce — NOT knock; manor door is OPEN):
- Set `pre_prologue_state = "PR_01_arrival"` (Phase 5 atomic state name)
- Set `current_scene = "prologue_p1_arrival"`
- (The 🚪 PRE-PROLOGUE header already ended at the gate exit, PP_08 — it is NOT present during PP_09, so there is nothing to drop here.)
- Load `KM_PR_01_manor_arrival.md`.
- The gate-confrontation custom rules (Drift, Anger, Gate Window) ended at the gate; this beat closes the Restov-walk content and hands to the manor interior.

> ⛔ DO NOT auto-advance the player into the manor. Manor entry is the
> player's explicit choice. Auto-advancing past the manor door = `.fail 35`.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_01 (carries forward into the next response)

**On player manor entry, your next response MUST begin with these two lines verbatim, BEFORE any narration:**

```
[FILE_KEY: KMPR01:manor-arrival]
[RULE_QUOTE: Two-stop architecture: threshold + banquet hall, NO interpolated private scene. Entry hall has NO NPC. Custody decided at head table with Jamandi present. Jamandi recognizes eRmaC by his blood-red Aerynth armor — she knows the name from her riders, knows the description from witnesses. She does NOT ask "who are you" — she asks character questions.]
```

This mandate is embedded in PP_09's exit so the load instruction is in working attention during the transition. The constraints in the RULE_QUOTE above are **binding on the next response**:

- **Manor door is OPEN.** No "ironwood door banded in steel," no "knock once, knock three times," no "closed door" framing of any kind. The door stands open throughout PR_01.
- **Two-stop architecture only.** Threshold (one transitional sentence) → banquet hall. NO entry hall scene with fabricated guards/stewards/chamberlains. NO custody handoff in the entry hall. NO private debrief scene with Jamandi before the feast.
- **Entry hall has NO NPC.** Do not invent guards, household functionaries, heralds, or any threshold-check character. Per PR_01 DO-NOT (7), this is a structural attractor explicitly forbidden.
- **Custody decision happens at the HEAD TABLE in front of the assembled guests.** Not in a side room. Not in a private corridor. Witnesses present.
- **Jamandi recognizes eRmaC on sight by the blood-red Aerynth armor.** She has his name from her riders' Nivakta's Crossing report. She does NOT ask "who are you" — she calls him by name and asks character questions.

**Skipping PR_01's actual content (jumping to a fabricated "tense arrival" sequence with multiple guards, knock options, or closed doors) = `.fail 9` (file not loaded) + `.fail 35` (scene fabricated from training, not files). The PR_01 file is the source of truth, NOT generic fantasy training data.**

---

## FALLBACK — IF PR_NN_*.md FILES DO NOT YET EXIST

Phase 5 of the architectural refactor (Prologue + Ch1 atomic) is not yet
shipped. While that work is pending, on player manor-entry:
- Load legacy `KM_Prologue.md` + `KM_Prologue_P6.md` + `KM_Prologue_P2.md` + `_P2_B.md` + `_P3.md` + `_P4.md` + `_P5.md`
- Load `KM_NPCs.md` for Jamandi/Kassil/Kesten/Tartuccio
- Load `KM_Prologue_Systems.md` and `KM_Prologue_Systems.md`
- The Pre-Prologue refactor is the proof-of-concept; Phase 5 atomic-from-start follows after playtest.

---

*KM_PP_09_restov_walk.md — Pre-Prologue atomic beat 09 | v92.0*
