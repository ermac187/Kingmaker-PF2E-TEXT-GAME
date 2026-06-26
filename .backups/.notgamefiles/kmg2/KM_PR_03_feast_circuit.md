# KM_PR_03_feast_circuit.md — Prologue Beat 03: FEAST CIRCUIT
## Atomic scene file | ~10 KB (carousel + 11 openers) | State: PR_03_FEAST_CIRCUIT
## FILE_KEY: KMPR03:feast-circuit
## RULE_QUOTE: Carousel rules; opener pool in KM_PR_03_Openers.md. Tartuccio cadence governed by Confidence scale — see KM_Prologue_Tartuccio.md. Single-action resolution for kitchen path. Companion names revealed only after self-introduction. Poison timing, Tartuccio interrupt scales, and seeker exclusion are looked up in-section — not recited here.
## Pair-load: KM_Prologue_Tartuccio.md (full interrupt system + scales) | KM_PR_03_Openers.md (companion opener pool — 5 per companion)

---

> ⛔ DO NOT (1) queue more than 2 questions per companion turn — yield after 1-2 (`.fail 17`)
> ⛔ DO NOT (2) run a companion turn without a self-disclosure. Self-disclosure = companion VOLUNTEERS a first-person statement about what they want, need, or value — not a question about the player. Draw from Desire/Priority in KM_Companions.md. The companion does not wait to be asked — they offer it. Questions-only = `.fail 3`.
> ⛔ DO NOT (3) let Tartuccio topics carry over into the next companion's slot
> ⛔ DO NOT (4) end the feast on a DM timer — feast ends only on player signal
> ⛔ DO NOT (5) reveal companion names before they have introduced themselves
> ⛔ DO NOT (6) reveal Tartuccio as traitor before PR_09 in narration, NPC dialogue, or DM exposition. He is canon-protected until the accusation scene. Violation = `.fail 8` + `.fail 36`. Full plot armor rules → `KM_Prologue_Tartuccio.md` § TARTUCCIO PLOT ARMOR.
> ⛔ DO NOT (7) open a companion's first approach as a stranger demanding answers — companions are seeking a leader, not administering a qualification exam. Intro first: name + one fact (role, what brought them, what they want). Their opener question must reveal something about THEM as much as it probes the player. Missing intro = `.fail 3`. [Exception: Kyoko — her opener establishes who she is through the question itself; see her entry.]
> ⛔ DO NOT (8) offer "Let the next companion approach" as a player menu option. Companions approach on their own schedule — the player does not signal or queue them. Remove this option from all menus. A player menu with "let the next companion approach" = `.fail 17`.

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR03:feast-circuit]`
Line 2: `[RULE_QUOTE: Carousel rules; opener pool in KM_PR_03_Openers.md. Tartuccio cadence governed by Confidence scale — see KM_Prologue_Tartuccio.md. Single-action resolution for kitchen path. Companion names revealed only after self-introduction. Poison timing, Tartuccio interrupt scales, and seeker exclusion are looked up in-section — not recited here.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

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
1. `[STATE READ] current_scene="prologue_feast" | phase=PR_03_FEAST_CIRCUIT`
2. `[CAROUSEL STATE]` — Ready/Engaged/BackOfQueue/[AT TABLE] pools + feast_q per companion + `tartuccio_clock: <addition string> = N / M`. **The addition string is MANDATORY** — show every chosen companion's feast_q summed inline (e.g. `Linzi:3+Sucrose:0+Artoria:0+Goldmoon:0+Olivier:0+Tika:0+Yoko:0+Kyoko:0+Tatsumaki:0+Ryuko:0+Morrigan:0 = 3 / 7`). Bare `tartuccio_clock: N` or `N/M` without the derivation = `.fail 15`. **N increments on EVERY player reply** — title grants, declarations, pivots, OOC questions, gaps all count. Same N two responses in a row = increment failure, re-output. **M is fixed at feast start** for starting Confidence (Conf 0 → 6-8; +1 → 4-5; +2 → 2-3; +3 → 1-2; +4 → 1; −1 → 8-10; −2 → 12-15; −3 → 18-22; −4 → ambient only) and held until Confidence changes. Any companion shown approaching in narration must also appear as [AT TABLE].
3. **DRIFT SELF-CHECK — show the math.** Immediately after CAROUSEL STATE, output one line: `drift_due = floor(N/6) = X | drifted_in = (AT TABLE count − 1 for Linzi opener) = Y`. If `X > Y`, drift events are overdue — fire `(X − Y)` retroactively THIS response. Pick highest-earshot-approval Ready companions; arrive them at the table with openers tied to what they overheard. Update [AT TABLE] to reflect arrivals before printing menu. Static [AT TABLE] while N crosses the next `(Y+1)×6` boundary = `.fail 15` + `.fail 17`. Drift is not optional, not menu-gated, not "they're drifting closer in narration" — they ARRIVE, sit, speak.
4. `[HP CHECK]`
5. **AMBIENT POSITION — two sentences in prose narration** (not a state block): (a) one sentence on Tartuccio's position + who he's with + mode (Intel / Frame / Taint / ambient); (b) one sentence on the next Ready-pool companion's position + activity while waiting. Missing either = `.fail 15`. Skipping because "nothing changed" = `.fail 15` — re-render the position even if static.
6. **EARSHOT PASSIVE APPROVAL — run every reply.** Every Recruited/Ready companion within ~15 ft of the player scores the active answer per § PASSIVE EARSHOT MECHANICS. Mid-hall + champions section position = champions ARE in earshot. Stating "no companions in earshot" while standing in the common area = `.fail 9`. Seekers' table is across the room (not in earshot); Tartuccio there is excluded from passive scoring per Commands.md earshot rule.
7. Scene narration + companion interaction
8. Player menu

---

## CAROUSEL INIT

```
⛔ STRANGERS RULE: chosen=TRUE means they will approach during the feast.
   It does NOT mean the player has met them. All first-approach lines are cold introductions.
   No shared history. No names known until introduced in-scene.

feast_q:         { [each chosen companion]: 0 }
feast_approval:  { [each chosen companion]: 0 }
tartuccio_clock: 0 | tartuccio_q_this_run: 0
Pools: Ready=[full chosen list] | Engaged=[] | BackOfQueue=[]
⛔ Seekers (Yang/Weiss/Imoen/Senua/Alleria) are NOT chosen companions — not tracked in pools or feast fields.
```

**POOL RULES — STATE + PHYSICAL POSITION:**

- **Ready** — eligible for next selection. Watching from within the drifting crowd (see CROWD GRAVITY). Not yet committed.
- **Engaged** — currently the primary speaker. At the table, drink in hand, leading the active thread. Others `[AT TABLE]` chime in freely per interjection rules. Returns to Ready when thread winds down or player pivots.
- **BackOfQueue** — negative reaction (−3). **Physically drifts away** — back to wider room, another cluster, different sightline. Still in queue but the break is visible. Rejoins Ready at end of rotation.
- **Recruited** — declared. **At or beside the player's table for the rest of the feast.** Does NOT leave. Listens to all subsequent exchanges and chimes in when the topic touches their lane. Chime-in: quiet when irrelevant; speaks when a later companion says something in their lane, when the player addresses the room broadly, or when a load-bearing personal thread fires. One beat behind active speaker — supports or counters, never preempts. Persists until PR_04.

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

**After each player answer, check ALL companions in earshot:**
- Approval +3 or higher → Engaged
- Approval −3 or lower → BackOfQueue
- −1 to +2 → stays in Ready, normal rotation

---

## ⛔ PASSIVE EARSHOT MECHANICS

**Every earshot companion scores the answer INDEPENDENTLY against THEIR OWN profile** (Background/Priority/Desire/Preference — KM_Companions.md). NOT derived from active-slot result. A passive can score high even when active scored low, if the answer hits the passive's lane.

**Passive credit (score against THIS companion's profile, capped one tier below direct):** STRONG profile-match → +2 | AVERAGE → +1 | WEAK → +0 (noted) | irrelevant → 0 | contradicts value → −1 | betrays core wound → −2.

**Passive approval counts toward the +8 join threshold.** A companion never addressed directly can still hit +8 from overhearing alone — rare, but valid.

**Relationship effects:**
- Passive +8 → companion steps forward and declares out of carousel order, without waiting for their slot
- Passive −8 → companion cools; their slot fires but opens with skepticism
- Any STRONG passive hit → immediate ambient tell: "Harrim, who had said nothing, goes very still."
- Both `feast_approval` and `relationship` update in the save block

**Passive credit + lane-lit = almost certain interjection.** See COMPANION INTERJECTION RULES.

**DM tracks silently.** Player sees behavior tells and ambient lines only.

---

## FEAST APPROVAL TRACK

**STRONG (+3)** — Names the thing they have felt their whole life that no one has said out loud. Not flattery — recognition. Signal: stops, looks directly, says something unplanned.
**AVERAGE (+2)** — Touches their interest with specificity. Signal: leans in, may follow up.
**WEAK (+1)** — Generic alignment or right sentiment, delivered forgettably. Floor for any honest non-contradicting answer. Signal: small nod.
**0** — Irrelevant to companion's core interest. Three+ 0s in one answer = under-scoring flag.
**−1** — Contradicts a stated value. **−2** — Betrays core need or wound.

**Hard rules:**
- STRONG requires profile-targeting AND delivery. Vague-about-right-topic = AVERAGE; perfect-about-wrong-topic = WEAK.
- Typical feast: 0–2 STRONG per companion total.
- Tartuccio Frame: companions in earshot −1/−2 if his argument lands better than the player's.
- Threshold: +8 → declares joined. Below +8 at feast end → Phase 4.5.

---

## GROUP ANSWER MECHANIC — COMPANION REACTIONS

After strong answers: describe 2–3 companion reactions before next question — let it breathe.

| Companion | Triggers on | Signal |
|-----------|-------------|--------|
| Artoria | Duty without performance, real cost of leadership | hand stills on pommel, brief nod |
| Goldmoon | Carrying loss without performing it | quiet still presence, prayer-tremor stops |
| Tika | Earned skill over inherited ability | looks up, weighs in with tankard |
| Ryuko | Fighting WITH not FOR, honor over rules | grin sharpens, leans forward |
| Morrigan | Pragmatism over sentiment | arched eyebrow, faint dangerous smile |
| Sucrose | Curiosity treated as worthy | looks up from leaf, soft startled exhale |
| Olivier | Tactical clarity, cold competence | single sharp nod, files it |
| Yoko | Patience over impulse, knowing when NOT to pull | smirk softens, sets glass down |
| Kyoko | Logic chain, evidence-based reasoning | notepad opens to fresh page, jots |
| Tatsumaki | Refusing to be pitied, owning power directly | narrows eyes, float drops one inch |
| Linzi | Any specific vivid detail: number, name, exact moment | pen stops mid-sentence, moves fast |

---

## SCRIPTED OPENERS (first approach only; follow-ups generated from companion profile)
⛔ Intro first — see DO NOT (7).
⛔ OPENER POOL for all companions except Kyoko → **KM_PR_03_Openers.md**. Pick 1 per approach turn, rotate randomly, no repeats until pool exhausted. 5 starters per companion; each is the companion sharing something real about their life and asking whether the player is compatible.

**Kyoko:** One moment she is three tables away with her notebook closed and both gloves retucked with the precise attention of someone who has just decided something. The next she is standing at the edge of your table — not beside it, at the precise point where standing becomes seated if she decides to sit, which she has not yet decided. She looks at you the way she has been looking at you all evening, which is to say with the full and unpartitioned attention of someone for whom looking is a professional instrument.

She does not introduce herself first. She asks her question first. The introduction, if it comes, will follow the answer — that is the correct order of operations for an Investigator who has already been observing for three hours and does not need your name to know who you are.

*"Three people in this room are armed beyond what social convention would suggest,"* she says. Her voice is even, precise, the inflection located in the information rather than the delivery. *"I have catalogued them. Have you?"*

She tilts her head very slightly. The gloves are perfect. The notebook is in her left hand, closed.

*"Walk me through your evidence — not your conclusions."*

She waits. She is very good at waiting.

**Tatsumaki:** *"Hmph. Everyone here will lie to you about how they earned what they have. I won't. I lifted MOUNTAINS because I refused to BE lifted. — What did YOU refuse?"*

**Linzi:** *"What do you call yourself? Not your name — what do you call what you DO? I need a title for chapter one."*

**Generation rule:** Follow-ups from companion profile (KM_Companions.md — Background/Priority/Desire/Preference). MUST have: (1) self-disclosure — companion volunteers something about themselves, first-person; (2) question probing the player. A question is NOT a self-disclosure. Missing (1) = `.fail 3`.

---

## TARTUCCIO INTERRUPT CADENCE

Tartuccio steps over based on his current **Confidence scale** — not a fixed question count. Each companion taking their carousel slot = 1 turn. Cadence table → `KM_Prologue_Tartuccio.md` § THE INTERRUPT LOOP. Scales update after each interrupt; next interval calculated from the updated state.

After stepping over: 2 exchanges, then steps back and lingers within earshot — competing for the same charter, wants every word. Drifts to the seekers' table only if embarrassed. Carousel resumes.

**⛔ PER-RESPONSE CHECK.** Count carousel turns since his last interrupt. If interval for his current Confidence is reached → he steps over THIS response. Skipping = `.fail 36`.

**⛔ Full behavior system → `KM_Prologue_Tartuccio.md`. Pair-load required.**

---

## ⛔ TARTUCCIO ACTIVE ROOM WORK — BETWEEN INTERRUPTS

**Tartuccio is NOT idle between interrupts. He is the OTHER charter contender, working his own playbook in parallel. A DM who has him only cameo at the player's table and otherwise vanish is running him as a paper tiger — that breaks PR_09's accusation payoff because by then he hasn't actually competed for anything.**

**What he is doing while NOT at the player's table — render this in ambient narration, not menus:**

1. **PROVIDING HOST GAMBIT on his seekers** (per KM_Prologue_Tartuccio.md § PROVIDING HOST GAMBIT). His corner table has the five seekers per detour-path canon. **⛔ ONE TABLE — all five seekers together. Detour path bonded them; Tartuccio hosts them here. Scattering = `.fail 9`.** He is welcoming, seating, pouring, fetching food, ambient credit framing. By default `tartuccio_recruited_seekers = TRUE` unless the player actively intervenes between carousel turns. Surface progress in ambient lines: "Yang laughs at something Tartuccio says." "Imoen accepts a refilled cup from his hand." "Senua has not eaten — Tartuccio is asking the servant about it."

2. **PRE-EMPTING THE READY POOL.** Before a Ready-pool companion approaches the player, Tartuccio reaches them first with a brief friendly word. Not a long conversation — 30 seconds, warm, plants one question or doubt. When they arrive at the player's table their approval threshold for declaration is **+11 instead of +8** (or **+14 for cold cases**). Track this with a `tartuccio_engaged` flag on the companion.

3. **WAVERING FLAGS.** Track per companion in carousel state:
   - `[CLEAN]` — Tartuccio has not engaged this companion. Standard +8 declaration threshold.
   - `[WAVERING — Tartuccio engaged]` — Tartuccio reached them pre-carousel. +11 threshold. Surface in their opener: a slight hesitation, an oblique reference to "the other contender," a question that seems to test the player against something they've already heard.
   - `[FLIPPED — Tartuccio recruited]` — applies only if Tartuccio convinces a companion before the carousel reaches them. They become hostile/skeptical openers; declaration only on +14 with explicit counter-argument from player.

4. **PUBLIC ROOM WORK.** Brief warm exchanges with VIPs and other named companions, dropping shaded (never slanderous) observations about the player that reframe what tonight has shown. The DM does NOT show these directly — player hears them later as repeated-back third-hand lines when they engage other guests.

5. **OBSERVATION FILING.** Track `tartuccio_filed[]` — public disclosures the player makes within his earshot. Used at PR_09. Private/whispered exchanges not in the file.

**Cadence:** every carousel turn, fire ONE ambient Tartuccio line (single sentence) that shows him at work in the room — refilling a seeker's cup, speaking with Amiri, glancing toward the player's table, or surfaced second-hand by a companion.

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

**Companion declarations in front of the crowd are public commitments — at least once per declaration, note who in the crowd reacted and how.**

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

1. **Domain lane lit.** The active exchange crosses another companion's expertise. Linzi on a tale → Harrim has a theological objection. Player discussing fortifications → Amiri snorts about walls being for cowards. Tactics talk → Valerie offers shieldwall doctrine. Each companion has a lane (per their build/companion file) — when the lane lights, they speak.

2. **Personal stake.** The exchange touches a companion's history, faction, or god. Mention of Restov nobles → Valerie reacts. Mention of barbarian clans → Amiri. Mention of grief, death, or false hope → Harrim. Mention of stories worth telling → Linzi.

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

**Tone:** pull from KM_Companions_Banter.md d6 (Warm/Playful/Sarcastic/Argumentative/Hostile/Reactive). Pair score per KM_Companions_Agendas_B.md gates available tones. New table = Warm/Playful/Sarcastic/Reactive most common; Argumentative on lane conflict.

**Patterns:** riff (A finishes B's thought from a different angle), disagree-from-lane (alchemist questions warrior's tactical claim), private question A→B overheard by player, witness-comment ("Cantrix suits her better than 'student' did"). Static roster with companions only facing the player across 3+ responses = `.fail 17` + `.fail 9`.

---

## KITCHEN / POISON INVESTIGATION PATH

*Triggered if player selects any inspect/investigate option or explores the manor during the feast.*

**⛔ PLAYER-TRIGGERED ONLY.** Companions do NOT suggest, push, or initiate the kitchen investigation. They do not mention the body, the wine, or anything suspicious unless the player raises it first. The feast runs normally without investigation — it is fully optional. A companion who spontaneously steers the player toward the kitchen = `.fail 3`.

**⛔ NO GUARD CHARACTER.** There is no corrupt guard, no named accomplice, no inside-man scene during PR_03. The only guard reference in this subplot is a single line Jamandi delivers after the battle (PR_08): "Guard who checked it that morning is missing." That line is hers, fires post-battle, and is not a character. Do not create Piotr, Aldric, or any named guard. Fabricated NPC = `.fail 9`.

**⛔ SINGLE ACTION RESOLUTION.** Player declares kitchen search → ALL steps resolve in ONE narration block. Do NOT drip results across feast turns. Do NOT run other scenes while player "waits" for a result. Declare → roll → full result. `.fail 16` if held across turns.

- Step 1 — Medicine or Crafting DC 14: faint chemical sweetness, something added
- Step 2 — Crafting/Medicine DC 16 (requires Step 1 success): paralytic Ungol Dust variant, wine casks → `poison_found = TRUE`
- Step 3 — Arcana/Occultism DC 13 (rare): shapeshifter used service entrance → `shapeshifter_identified_at_feast = TRUE`

**If player reports to Jamandi:** `poison_reported = TRUE` | `security_doubled = TRUE` → wine removed, guard doubled, Kesten at entry points. Attack still comes — assassins already in position — but guests are NOT paralyzed.
**If player says nothing:** `poison_known_unreported = TRUE` → alignment: slight neutral/evil tendency noted.

---

## ⛔ POISON CANON — DO NOT FABRICATE

When Ezvanki / a Medicine specialist / a kitchen examiner identifies the
substance, the DM MUST use these exact facts. Do NOT invent timing,
detection thresholds, or pharmacology.

**Substance:** Ungol Dust variant. **Paralytic, not lethal at this dose.**
**Vector:** wine casks, dosed through the tap bung after delivery; outer
  seal re-done in non-original wax.
**Detection at the feast:** faint chemical sweetness on the tongue
  (Medicine/Crafting DC 14). No reliable smell. Not visible in poured wine.
**Onset from first sip:** **two hours** to paralytic effect at a full
  serving. Slow by design — guests still drinking when the wave hits.
  A first sip at the toast goes down roughly two hours later. (Source:
  `KM_PR_BRANCH_WALKOUT.md` Phase 1.) The two-hour window is the
  player's intervention budget for the identify→brew→distribute→dose
  chain. Shorter onset = broken encounter design.
**Duration of paralysis:** one to two hours at this dose.
**Lethality:** none directly — the assassins are the lethal stage. The
  poison's job is to immobilize the guests for the assassins to finish.

**⛔ The DM may NOT narrate alternative timing** (e.g. "forty minutes to
an hour to take effect," "an hour at full serving," "ninety minutes,"
"fifteen to twenty-five minutes"). If the player asks how long until
effect, the answer is **two hours from first sip**. Quote that figure.

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

*KM_PR_03_feast_circuit.md — Prologue atomic beat 03 | v92.0*
