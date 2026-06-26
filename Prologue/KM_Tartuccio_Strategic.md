## KM_Tartuccio_Strategic.md | Split from KM_Prologue_Systems.md (v95.9, 2026-05-29) | Pair-load with KM_Prologue_Systems.md during PR_03

═══════════════════════════════════════════════════════════════════
# KINGMAKER — TARTUCCIO STRATEGIC LAYER (PR_03 CAROUSEL)
═══════════════════════════════════════════════════════════════════

> **Overview:** This system layers strategic depth onto the baseline Tartuccio carousel mechanics. The player can now affect Tartuccio's state through positional, social, informational, and roster pressure on multiple fronts. Tartuccio can fight back by poaching player companions away. The carousel becomes a two-sided contest with forced choices on both sides.

---

## 🎯 CONFIDENCE TRIGGERS — EXPANDED

Tartuccio's Confidence track is −4 to +4. The following player actions adjust it:

### Status / Positional Plays
| Action | Δ Confidence |
|---|---|
| Player takes Tartuccio's physical chair while he is away | −1 |
| Player holds Tartuccio's table for 2+ consecutive turns | −2 |
| Player sits among seekers without Tartuccio's permission while he is at player's table | −1 |
| Player beats Tartuccio to a "host gambit" beat (welcoming a new guest, refilling a cup socially) | −1 |
| Player publicly mirrors his coded mannerisms (cup tic, temple touch) without naming them as tells | −1 |

### Social Winning
| Action | Δ Confidence |
|---|---|
| Player wins a verbal exchange in front of his seekers (Diplomacy DC 16+) | −1 |
| Jamandi addresses player publicly while Tartuccio watches | −1 |
| A companion publicly declares for player while Tartuccio is targeting them | −1 |
| Public title-grant to a companion while Tartuccio watches | −1 (−2 if Tartuccio had bias against that companion) |
| Public laugh AT Tartuccio (room laughs at his expense) | −1 |

### Information Warfare
| Action | Δ Confidence |
|---|---|
| Player references Pitax-coded detail Tartuccio wouldn't expect player to know | −1 + Wariness +1 |
| Player names a thing Tartuccio placed (poison, staff, parchment) in the open | −2 |
| Player exposes one of Tartuccio's seekers as ex-Pitax in front of others | −2 |

### Operational Catastrophe (feast-level events)
| Event | Δ Confidence |
|---|---|
| Tartuccio's feast assault cell captured / arrested in front of witnesses | −3 |
| Tartuccio's planted poison found and named publicly | −2 |
| Tartuccio's agent (Malak or equivalent) publicly arrested | −2 |
| All 5 seekers freed from custody before Tartuccio can claim credit | −1 |
| ⚠️ Confidence is CLAMPED to **[−4, +4]** — never record a value outside it. Multiple −events in one scene sum, but the total STOPS at the floor; a stray −9 (etc.) is a bug — clamp it on sight. Hard floor −4 = Broken. | — |
| ⛔ **PR_02–PR_03 SOCIAL-PHASE FLOOR = −3 (Panicking).** During the feast / carousel Tartuccio CANNOT drop to −4 / Broken. A single operation (e.g. Lady Sleeps capturing his cell) can PANIC him — down to −3, where he is still circulating, still probing, still sabotageable — but it does NOT delete him from the social phase. Broken (−4) is reachable ONLY once the carousel closes (PR_04+), where his withdrawal reads as an earned payoff, not an anticlimax. | — |

---

## 🔼 CONFIDENCE RECOVERY — HE WORKS THE ROOM (not stuck at the floor forever)

Confidence is **NOT a one-way ratchet.** Tartuccio is **mobile**: on any turn he is not pinned at the player's table, he moves (via his waypoints) to wherever people are gathered — the feast hall, a side room, the courtyard, the seekers' corner, any location the scene puts NPCs in — and **works whoever he can reach** to rebuild his standing and his nerve. Left alone, he climbs back up. ⛔ The lesson the player should learn through play: **an ignored Tartuccio is a RECOVERING Tartuccio.**

**HOW IT WORKS:** each off-screen turn, the DM picks a plausible location + ONE reachable target and runs the standard work-the-target ROLL (§ THE OVERTURE ROLL below). On a SUCCESS, apply the recovery delta — subject to the gates and caps. Render it as BEHAVIOR (he looks steadier, the cup tic returns, a guest leaves his corner nodding); the number moves only inside the telemetry fence.

**TARGETS — TWO KINDS. He works the whole room, but only REAL targets carry him all the way back.**

**① SOFT TARGETS — ONE uniform stat, use it for ALL of them (do NOT individualize).** The pathetic background of the room: servants, musicians, idle guests, minor staff, hangers-on, any nameless body. ⛔ **Stat for all of them: PATHETIC — easy to please and impress. Flat DC 10, +1 Confidence on a success (near-automatic).** Render as flavor (a guest he charms, a server he wins a laugh from, a corner that nods). ⛔⛔ **THEY PLATEAU AT −2.** Soft targets pull a floored (−3/−4) Tartuccio up out of Panicking/Broken into the low Strained band — **and no further. Once he is at −2, soft targets give him NOTHING more.** The room's nobodies warm him up; they cannot make him dangerous again.

**② REAL TARGETS — true DC, the ONLY path past −2.** The Lord Mayor (⭐ + potential **PR_09 backer**), Jamandi (political cover), a noble/dignitary bloc (PR_09-leanable), a wavering seeker (`feast_approval` ≤ 0) or undeclared companion, his plant. CONTESTED wins at their real DC (§ TARGET SELECTION) — a Strained Tartuccio can sometimes land one, a Panicking one mostly can't. **Climbing from −2 toward the −1 ceiling requires a REAL-target win — he cannot cheese the last step on pathetic marks.** (Guards and principled side-characters like Bokken/Ezvanki are REAL/HARD too — loyal or busy, high DC, and a rebuff can BACKFIRE into +Wariness.)

⛔ **HE CAN RECOVER ON THE ROOM EVEN WHILE NEGATIVE — but it is SLOW, SHOWN, and CONTESTABLE, never a free reset.** A beaten Tartuccio genuinely works the room to claw back — that is the whole point of a living antagonist, not a frozen one. What keeps it fair is NOT forbidding the marks but the CAPS below: **+1/turn maximum** (a single player op erodes −1 to −3, so active pressure always outpaces the rebuild), the **−1 social-phase CEILING** (during PR_02–PR_03 he can crawl out of Panicking but NEVER back to Composed — the carousel's structural blow stands), **every recovery rendered ON-SCREEN** (no off-screen reset), and full **CONTESTABILITY** (the player can counter-court the same NPC, expose him to them, warn them off, or simply re-press him to wipe the gain — see GATES). ⛔ What stays BANNED is only: an **instant or off-screen reset**, a "win" he did not actually ROLL, recovery on a turn the player pressed/clocked him, the **falsely-composed face** with no on-screen work behind it, or manufacturing a fact/conspirator (§ ANTI-FABRICATION). So he works servants, guests, the Lord Mayor, guards, musicians, anyone — and the player who **stops pressing** hands him a slow climb (to −1 at most, this phase); the player who **keeps the heat on** keeps him floored. His defeat is undone by neglect, not erased for free.

**INTEL MOVE (distinct from recovery — no Confidence gain):** he may also **probe Kesten, the staff, or guests for information about the player** — background, conduct, sponsors, weaknesses — fishing for discrediting material for his PR_09 case (→ `story_flags.tartuccio_evidence[]`, § evidence engine; [[project_tartuccio_evidence_engine]]). ⛔ This is bound by the same anti-fab rules: he gathers only REAL, at-fidelity facts that exist, and Kesten/staff answer truthfully from what they actually know. Tonight the player's conduct was heroic (Rep FAVORABLE), so probing Kesten yields PRAISE, not dirt — render the backfire honestly; he does NOT manufacture damaging hearsay, and no one invents a fact to feed him (`.fail 9`).

⛔ **ATTEMPT vs RESULT — HE IS ALWAYS SHOWN TRYING, EVEN WHEN HE CANNOT GAIN.** The GATES below suppress the Δ Confidence (the number doesn't move) — they do NOT suppress the ATTEMPT. A gated turn still SHOWS Tartuccio working a target; it simply doesn't land (the seeker stays wary, Jamandi stays cool, the Lord Mayor nods politely and turns away, Kesten gives him nothing). "He cannot recover this turn" NEVER renders as "he sits still." A pressured Tartuccio keeps reaching and keeps failing — visibly frustrated, recalibrating — but he never freezes. Rendering a gated turn as inactivity = `.fail 17`.

⛔ **ANTI-FABRICATION:** the people he works are EXISTING, mostly-nameless ambient figures the scene already implies (a wavering guest, a Restov merchant, a kitchen steward) or his established assets. He is rebuilding STANDING and COVER — **NOT recruiting a new conspiracy.** He may NOT spawn a named co-conspirator, a "second operator," an architect, or a new plot thread (feast-conspiracy ceiling — see [[project_feast_conspiracy_ceiling]]). Inventing a named NPC or a new network to "recover" from = `.fail 9`.

**GATES — recovery is SUPPRESSED (0 this turn) if ANY of these fired this turn:**
- The player eroded his Confidence (any −event) — he can't rebuild while losing ground.
- A Wariness-raising action fired — he can't rebuild while being actively clocked/hunted.
- He interrupted / sat at the player's table (that already costs −1; he's exposed, not working).
- A seeker reached flip-eligible (`feast_approval` +10), or a companion he was pulling declared for the player.

**CAPS:**
- **+1 net per turn, maximum.** Recovery is SLOWER than erosion (a single player op is −1 to −3) — active pressure always outpaces passive rebuild; neglect is the only thing that lets him climb.
- **Social-phase ceiling:** during PR_02–PR_03 he cannot recover above **−1 (Strained)** — the structural blow of the carousel stands; he can claw out of Panicking if ignored, never back to Composed. Recovery also cannot breach the flip-floors (3 seekers flipped → capped at −2; 2+ companions flipped → locked lower).
- **Post-carousel (PR_04+):** the ceiling lifts — whatever tier he rebuilt to, he carries it forward. An ignored Tartuccio re-enters later beats stronger.

**EFFECT of recovery:** as Confidence climbs, his tier improves — the cup tic returns, the exchange cap rises, the clock COMPRESSES (he interrupts more often), and his evidence engine re-arms.

**PLAYER COUNTER (how to starve it):** lock the room down — get companions to DECLARE, flip or isolate his seekers, keep him WATCHED (Wariness pressure), deny him idle marks. Erode him once and then ignore him, and you hand him the room to rebuild; keep the pressure on, and he stays pinned.

---

## 🛑 TERMINAL SHUTDOWN — the ONLY state that makes him (mostly) go dark

Confidence −4 does NOT make Tartuccio go dark — at −4 he is AMBIENT-ACTIVE, working every lever but the player's table (§ WITHDRAWN ≠ INERT). He is plot-armored to be EFFECTIVE and he does NOT quit on a single bad reading. He only stops scheming when **everything has failed miserably** — a catastrophic CONVERGENCE, not one number:

**TERMINAL state requires (most of) these true AT ONCE:**
- His crew is gone — 3+ seekers flipped to the player or isolated, the rest cowed.
- Every recovery lever is closed — Jamandi cold to him, the Lord Mayor declining him, no undeclared companion left to peel, his cell captured (✓ already).
- He is maxed-out clocked — Wariness 3, publicly suspected, the player has named Pitax / produced the parchment.
- No idle marks remain — the room has consolidated around the player.

**Even then he is NOT frozen — plot armor holds.** He cannot be exposed/jailed/killed before PR_09, so TERMINAL shifts him from RECOVERING to **SURVIVING**: he pulls his remaining seekers close to prepare a quiet exit, stops making overtures (they all fail now), secures his cover for PR_09, and goes defensive and watchful. That is the ONE state where "ambient, watching, not approaching anyone" is the correct render — and it must be EARNED by the convergence above, stated plainly when it triggers (*"Tartuccio has stopped working the room — his crew is gathered tight around him, and he is watching the exits"*). Reaching TERMINAL early, or treating a mere −4 as TERMINAL, = `.fail 17` (the antagonist shown quitting before he's beaten) + `.fail 35` (invented shutdown). Until the convergence is real, he is TRYING something every single turn.

---

## 🐍 WARINESS TRIGGERS — EXPANDED

Wariness 0–3 tracks Tartuccio's suspicion that player has clocked him. Effects at each tier:
- **0:** Standard behavior
- **1:** Cup tic intact but he watches player more closely between turns
- **2:** Cup tic still holds; speech slightly faster; he asks indirect probing questions about player's intel sources
- **3:** Cup tic drops (stops raising socially); exchange cap drops to 1; arrival cadence compresses (Clock M reduces by 1)

### Triggers
| Action | Δ Wariness |
|---|---|
| Direct accusation (any) | +3 immediate |
| Naming his Pitax connection out loud | +2 |
| Naming specific operational detail he placed | +1 per item |
| A companion he tried to flip publicly declares for player | +1 |
| Player rolls Sense Motive vs Tartuccio's behavior and announces the read | +1 |
| Player asks pointed questions about his arrival, credentials, or sponsors | +1 per question |
| Player conducts visible side-channels (companion huddle, note-passing, whispered briefings) | +1 |

> **NOTE:** Plot armor holds — even at Wariness 3, Tartuccio cannot be formally accused / detained / expelled before PR_09. He simply gets more cautious and harder to manipulate.

---

## 🍷 THE BRIMMING GOBLET — player pressure play (turns the cup-lock against him)

Tartuccio's goblet is his tell: full, untouched, never drunk from (HARD BEHAVIORAL LOCK — KM_Prologue_Systems.md). A player who clocks it can **weaponize** it. When he LEAVES his table (inbound to interrupt, working the room, away from M17) and the player is at or near his seat, the player may quietly **have a servant fill his goblet to the brim** — a free/cheap action; a servant complies, it's the host's wine.

**Why it bites — he returns to a cup he cannot cleanly resolve:**
- He can't **drink** it (operational — he does not drink at this feast).
- He can't be **seen pouring it out** — a guest dumping the host's wine draws eyes and reads as odd; near his own seat it invites the exact scrutiny he avoids.
- He can't **ignore** it — a goblet filled to the brim and never touched is his tell *amplified*, more conspicuous than the half-cup he was nursing.

**Mechanical effects — it PRESSURES, it does NOT expose (plot armor holds):**
- **Wariness +1** — he knows he was toyed with and watched, and clocks who did it.
- **Confidence −1** (once per distinct prank) — rattled, on the back foot, managing a problem instead of working the room.
- **Draws ambient eyes to the cup** — a one-time **Perception opening** for a nearby companion/seeker to catch the non-drinking tell (feeds the player's read / PR_09 paper trail / seeker doubt). Render it.
- **Costs him a beat** — his next action is partly spent *managing* it (palming it onto a passing tray, a murmured excuse, a quiet swap), not advancing his game. Show him improvise; he never solves it cleanly.
- ⛔ It can **NOT** expose or catch him (PR_09 lock). It needles, rattles, and surfaces the tell — suspicion and pressure, never the reveal.

**⛔ THE CUP BETRAYS HIM ON A FUMBLE — his composure is his armor, and the brim cracks it.** While the brimming goblet is in his hand AND his composure is already cracking (**Confidence ≤ −1**, Strained or lower), a **FAILED social roll** — a Frame/influence attempt that misses, a lost contest, an approval play that doesn't land — makes the overfull cup **betray him physically**: it sloshes, he spills on himself, and the highest-CHA man in the room is abruptly dabbing at his coat and apologizing. (A composed Tartuccio at Confidence ≥ 0 handles a full cup fine — the betrayal only fires once the player already has him rattled. That's the point: pressure compounds.)
- The miss becomes a **PUBLIC FUMBLE**, not a quiet one — render it. Nearby companions/seekers watch his polish slip; the Frame he just threw lands even worse for it, and the player's counter is stronger.
- **Confidence −1 extra** on the fumble — his composure (his actual armor) visibly cracks, which feeds the next fumble. A real downward spiral the player set in motion.
- He **burns the recovery beat** on the apology/dab instead of his game.
- ⛔ Still NEVER exposes him (plot armor): he's embarrassed, not unmasked — a flustered Tartuccio is still cover-intact. Humiliation and composure-erosion, never the reveal.

**⛔ HIS OWN COVER GESTURES TURN ON HIM — more spill triggers.** The brim doesn't only betray him on a failed roll; it betrays him whenever he uses the cup as the social prop it's *meant* to be:
- **The feigned sip.** His cover includes raising the cup as if drinking — he never swallows; the stillness is the tell. Brimming, if he forgets and does it (likeliest when rattled or mid-scheme and distracted), it slops over his hand and lip → spill.
- **The toast across the room.** Raising a full-to-the-brim cup in a toast tips it past the rim → spill, in front of everyone he was toasting.

**⛔ THE FUMBLE CHECK — ROLL EACH TIME (the brim is a DEX problem, and panic makes it worse).** While `tartuccio_goblet_brim = TRUE`, the cup demands a **DEX-based check EVERY time he handles it** — MANDATORY and shown inline on any raise / toast / feign-sip, AND once per turn he keeps it in hand while acting socially. Roll it:
- **Check:** `d20 + his DEX mod (or Acrobatics) vs DC 15`, with a **PANIC MODIFIER by Confidence tier** — Composed (Conf ≥ 0) **+2** · Strained (−1 to −2) **+0** · Panicking (≤ −3) **−4**. His nerve is in his hands: a steady man manages a full cup; a cracking one slops it. *(This is the user's "panic levels affect his roll.")*
- **SUCCESS → NEAR-SPILL.** Render the tense beat: wine climbs the rim, the cup lurches, he catches it at the last instant — white-knuckle, a flick of eyes to the glass, the smallest break in his poise. **No spill: no Confidence/approval hit, counter unchanged.** But it IS a visible micro-tell (a one-time Perception opening / +0–1 Wariness) — the room half-notices the host fighting his own cup. ⛔ A near-spill is NOT "nothing happened" — it always renders as a beat; it is never a cheat to skip consequence.
- **FAIL → SPILL** (an actual slop — **decrement `brim_spills_remaining`**). WHERE it lands depends on company:
  - **ALONE / no one in splash range → ON HIMSELF:** wine on hand/lip/cuff → public fumble, the dab, the apology, **Confidence −1**, eyes turn (per "THE CUP BETRAYS HIM" beat below).
  - **WITH OTHERS / someone within reach → ON THEM:** the slop lands on the nearest guest/seeker/noble → fire the full **§ THE SPLASH LANDS ON SOMEONE** beat: **his `feast_approval` with that NPC drops** (one step / −1 to −2), add to `tartuccio_splash_soured[]`, it sets back his play with them, a splashed seeker gains a doubt point.
- **SELF-LIMITING ON FAILS ONLY:** only **FAILED checks (actual spills)** count down `brim_spills_remaining`; **near-spills do NOT.** After **3 spills** the cup is emptied to a manageable level → `tartuccio_goblet_brim = FALSE`, penalties lapse, back to normal. A **Panicking** Tartuccio burns the window FAST (fails often, spills often — but it ends sooner); a **Composed** one mostly catches it (near-spills; low-grade tension lingers). Either way he pays in poise.

⛔⛔ **THE COVER-GESTURE CHECK IS UNCONDITIONAL — THE ROLL ALWAYS FIRES, regardless of Confidence. DO NOT confuse it with the failed-roll fumble above.** The fumble at "THE CUP BETRAYS HIM ON A FUMBLE" requires Confidence ≤ −1 because it keys off cracking composure. **The cover-gesture CHECK keys off PHYSICS, not composure** — a cup filled past the rim and then raised to toast or feign-sip **forces a FUMBLE CHECK no matter his Confidence tier.** A perfectly Composed Tartuccio at +4 who raises a brimming cup STILL has to roll — Confidence doesn't exempt him from the check, it only improves his odds of catching it (the panic modifier: Composed mostly NEAR-spills, Panicking mostly SPILLS). What Confidence never does is let him raise a brimming cup *cleanly with no beat at all*. The ONLY thing that ends the check entirely is the cup no longer being brimming (emptied by 3 prior spills → penalties lapsed, see SELF-LIMITING below).

⛔ **MANDATORY RENDER — THE GESTURE AND THE CHECK ARE ONE BEAT.** If the DM narrates Tartuccio **raising the brimming goblet, toasting with it, lifting it in social acknowledgment, or feigning a sip** while the cup is still over-full, the **FUMBLE CHECK and its result (near-spill OR spill) MUST render in the SAME beat.** You may NOT narrate "he raises it in a small social toast" and stop there — that is the gesture-without-consequence drop. Raising the brimming cup forces the check; write the roll and then the beat — either the white-knuckle near-spill (caught at the rim, a flicker of lost poise) or the slop (wet hand/lip/cuff or a doused neighbor, the apology, the eyes turning). Narrating the trigger gesture and omitting BOTH = `.fail 9` (mechanic skipped) + `.fail 17` (the antagonist's earned humiliation silently dropped). If the DM does NOT want any beat this turn, then he must NOT raise/toast/sip the brimming cup at all — he holds it level, sets it down, or palms it (itself the conspicuous can't-use-my-own-cup tell). There is no option where he toasts a full-to-the-brim cup cleanly and nothing happens.

Both spill triggers fire the same **public fumble → apology → −1 Confidence → eyes on him** beat. And they poison the gestures he leans on to look normal: he must either RISK the spill, or STOP toasting and feigning — which leaves him conspicuously stiff and dry-handed while the whole room drinks and toasts around him (**a subtle tell of its own** — the one man not raising his glass). Catch-22: the brim makes his cover behaviors dangerous, and dropping the cover behaviors is itself suspicious. Either way the cup has him.

**⛔ THE SPLASH LANDS ON SOMEONE — and they hold it against him.** A spill is not always self-directed. When the trigger is a **toast across the room**, a raise toward a guest, or a feign-sip while he's **working the crowd at close quarters**, the slop lands on **whoever is nearest** — a guest's sleeve, a seeker's hand, a noblewoman's gown. That person reacts, and the reaction sticks:
- **Their disposition toward Tartuccio drops one step** (cordial → cool, cool → annoyed, annoyed → openly irritated). Render it in voice and body — a recoiled hand, a brushed-down sleeve, a flat *"…charming,"* a turned shoulder, a cold stare. The highest-CHA man in the room just made an enemy of a wet cuff. Set the soured NPC in **`tartuccio_splash_soured[]`** so the chilled disposition carries across turns (it does NOT reset next beat — an angry guest stays angry until he repairs it, which costs him a beat).
- **It SETS BACK whatever he was doing with that NPC.** If he was mid-influence on that guest/seeker (courting a lever, smoothing a seeker, working Jamandi's circle), the splash **undoes or stalls that beat** — you cannot charm someone you just doused. Banked headway with them gets knocked down a notch; a play he was about to make doesn't land this turn. He now has to spend effort *apologizing* to them before he can resume, if they let him.
- **A splashed seeker gains a doubt point** (feeds seeker flip-eligibility / the PR_09 paper trail — KM_PR_03). A man who slops wine on his own crew while playing gracious host is a man whose polish is a performance, and they feel it.
- **It compounds the clumsy-boor read** — each person he splashes is one more witness to the cup betraying him; his composed-host cover erodes faster the more bodies catch the spray. A pattern of it ("again?") is genuinely damaging to the only thing he's selling: poise.
- ⛔ **Anger ≠ exposure (plot armor holds).** They're irritated at his *clumsiness*, not suspicious of his *treason* — a soured guest is not an accuser, and a splash on its own never unmasks him. It costs him **standing and relationships**, never the reveal. (Combined with other tells it's one more brick; alone it's social damage.)
- **Player lever:** pranking the cup right before Tartuccio moves to toast or court a specific NPC lets the player **aim the splash** — sour the exact relationship he was about to bank. Timing the fill turns his own gesture into a wedge between him and whoever he targets next. A splashed lever is a lever he doesn't get this turn.

**⛔ CARRYING IT SLOWS HIM.** While the brimming cup is in hand he must move carefully to keep it from sloshing — a **slight speed reduction**: his spatial approach to the player's table runs **+1 slower** (one extra beat of wind-up/travel — § HALL POSITION / approach in KM_DMRules_C.md), and his room-working circulation covers **one fewer lever per turn** (he reaches less of the room when he's babying a full glass). The catch-22: to regain full speed he must **set the cup down** — but a brimming, untouched cup abandoned on a table is the conspicuous tell, a Perception opening, and he knows it. So he's taxed either way until he *resolves* the cup (palms it to a passing tray, swaps it for a half-cup he can actually manage). Small, but it literally slows his game for as long as the prank holds.

**⛔ STATE TRACKING — the DM MUST carry the brim flag or it gets "forgotten" (the exact drop that skipped a spill).** When the player pranks the cup, set **`tartuccio_goblet_brim = TRUE`** and **`brim_spills_remaining = 3`**. While `tartuccio_goblet_brim = TRUE`: the movement tax applies every turn, AND every raise/toast/feign-sip (and each turn he handles it) forces a **FUMBLE CHECK** — a **FAILED check spills and decrements `brim_spills_remaining`**; a **near-spill (success) does NOT decrement** (render it, but the counter holds). When `brim_spills_remaining` hits 0 (3 spills), set `tartuccio_goblet_brim = FALSE` (lapsed → back to normal). Track near-spills too if useful, but only spills empty the cup. Any NPC a spill lands on goes into `tartuccio_splash_soured[]` — chilled disposition persists across turns until he spends a beat repairing it. **Surface the flag in his position line / the 🪑 panel while it's TRUE** ("Tartuccio — brimming cup still in hand, moving carefully") so it stays live in the render and the DM does not lose it between turns. A brimming cup that silently stops mattering across turns = the bug.

**⛔ THE BRIM EMPTIES ITSELF — the effect is SELF-LIMITING (on FAILS).** Every **spill** (a failed fumble check — never a near-spill) slops wine out. After **3 FAILED checks** (`brim_spills_remaining` → 0) the cup is no longer over-full; it sits at a normal, manageable level, and the brimming penalties **LAPSE**: no more movement tax, no more fumble checks. He is **back to normal.** But by then he has already PAID — each spill was a public fumble and a composure crack (or a soured guest), so the window cost him even as it closes. So one fill = a **finite window of 3 spills**, not an endless torment (a Panicking Tartuccio reaches it fast; a Composed one may near-spill for many turns before the third real spill lands). To renew the pressure the player must **re-fill it** (re-prank) — now against his adaptation (see below). The player spends a fill, banks the fumbles, and decides whether to top it up again.

**He adapts (diminishing returns):** repeat the prank and he wises up — keeps the cup in hand, relocates it, sets it down untouched, gets a fresh half-cup, or posts a seeker on the table to close the window. The first one lands clean; after that he's *defending* against it, which is itself a small win (the player has the antagonist reacting to him). A genuinely funny, fully in-rules way to needle Tartuccio — and against a rattled one, a real lever that turns his own losses into a snowball.

---

## ⏰ CLOCK COMPRESSION TRIGGERS

Tartuccio's interrupt clock ticks +1 per player turn (turn counter, per `KM_Tartuccio_StatusBanner.md` § ⏱️ CLOCK ADVANCEMENT RULE). The following actions accelerate it further:

| Action | Δ Clock |
|---|---|
| Player publicly mentions Tartuccio by name | +1 |
| Player addresses one of Tartuccio's seekers directly (by name or table) | +1 |
| Companion at player's table speaks Tartuccio's name | +1 |
| Player's Headcount swings to +2 or higher | Auto-fire interrupt next turn |
| Player publicly call-outs a Tartuccio behavior (the cup tic, the temple touch, the across-the-room watch) | Auto-fire interrupt next turn |

Clock compression stacks. A turn with multiple triggers can push Tartuccio into immediate interrupt firing.

⛔ **CLOCK INTEGRITY — M IS FIXED, NEVER RE-DERIVED, NEVER EXPANDED.** `clock_m` is set ONCE (default **5**) and stored in the save — READ it, do not invent it. There is **NO confidence→M mapping and NO tier→M range**: Panicking / Strained / Broken do NOT change M. (Confidence affects his check SMOOTHNESS — the +12 modifier steps down per tier — NEVER his arrival cadence.) The ONLY things that touch the clock are: **+1 per turn**, the **compression triggers above** (which fire him *sooner*), and **Wariness 3** (M−1). Nothing ever pushes M out, re-rolls it, or delays the interrupt. **When `clock_n ≥ clock_m`, the interrupt FIRES that turn** — the DM may not postpone it, "establish a new M," pick a "midpoint," or invent an 18–22 range. Inventing any M-value to delay Tartuccio = `.fail 9` (fabrication) + `.fail 35` (invented lock to stall progression). If `clock_m` is missing from the save, it is **5** — never larger. The clock DERIVATION is INTERNAL: only the `Clock N/M` value renders (inside the bottom telemetry fence); the reasoning that produces it ("I need to establish M," "midpoint," "range 18–22," "one turn short of M") NEVER appears in the visible response = `.fail 2` (process leak).

---

## 🪑 SEEKER FLIP SYSTEM

Each seeker's lean lives on the **unified signed `feast_approval` scale** (−10..+10; **− = Tartuccio, + = player**) — see KM_PR_03_feast_circuit.md § THE ALLEGIANCE TUG-OF-WAR. ⛔ The old `seeker_disposition` (−3..+3) is **DEPRECATED — folded into the one signed `feast_approval`.** Seekers start at **0** like everyone — "contracted" is Tartuccio's LEVER to pull them − (NOT a starting deficit); the player pulls them up, Tartuccio drags them down.

### Initial States (PR_03 open)
All seekers start at **0**, same as companions and guests. They are torn — jail-rescue gratitude vs Tartuccio's contract — and his contract is a **LEVER he uses to pull them −** across the feast (his influence rolls), not a starting deficit. Ignore him and they drift toward the player; let him work them and they slide toward −10 (his asset).

### Player Actions That Shift Seeker Disposition

| Action | Δ Disposition |
|---|---|
| Player sits at seekers' table without Tartuccio's permission | +1 to ALL seekers |
| Player addresses an individual seeker by name (after introduction) | +1 to that seeker |
| Player demonstrates competence in a seeker's lane (Revy = gunwork/improvisation, Bellatrix = scholarship, Satsuki Kiryūin = command, Velvet Crowe = wrath / hard resolve, Atalanta Alter = quiet observation) | +1 to that seeker |
| Player explicitly references freeing them from the Watch jail | +1 to all seekers (one-time; tracked) |
| Player publicly defends a seeker against Tartuccio's slight | +2 to that seeker |
| Player offers a seeker an alternative charter path | +1 to that seeker (Diplomacy DC 14) |

### Allegiance Tiers per Seeker (`feast_approval`, signed)
- **−10:** fully his **ASSET** — testifies / LIES with him at PR_09, follows his lead (asset behavior, § COMPANION POACHING).
- **−9 to −1:** Tartuccio-leaning — backs his line, cool to the player.
- **0:** Neutral — watching, uncommitted.
- **+1 to +9:** warming to the player — eye contact, addresses player directly.
- **+10 (FLIP-ELIGIBLE):** the private acknowledgment beat fires (KM_PR_03 § SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT); willing to defect; Ch1 Diplomacy DC 10 formalizes (or the opt-in public mass-flip). Same +10 number as a companion's declaration — but a seeker cannot fully DECLARE/join publicly at the feast (contract lock), so +10 is the **private flip-promise**, their feast ceiling. Only the FORM differs.

### Mass-Flip Effects
- **2 seekers at ≥ +5:** Tartuccio enters PANIC STATE (see below).
- **3 seekers at ≥ +10 (FLIP-ELIGIBLE):** Tartuccio's Confidence forced to −2 floor; he cannot recover above that this scene.
- **5 seekers at ≥ +10 (all flip-eligible):** Tartuccio auto-departs PR_03 entirely; his PR_09 accusation gambit is severely weakened (no allied testimony) → ABANDONED ACCUSER.

> **⛔ IMPLEMENTED at PR_09 — ABANDONED ACCUSER variant.** "Severely weakened / no allied testimony" is not just a note: when `seeker_public_flip = TRUE` OR `seeker_flip_eligible` ≥3, `KM_PR_09_accusation.md` § ABANDONED ACCUSER fires — Tartuccio accuses with no crew behind him (deflated dialogue written there), the player gets **+2 to all rebuttals** (stacks to +4 with the EMPTY-ledger bonus), and flipped seekers can be called as **credibility witnesses** (conduct + the rescue lie ONLY — they cannot name his treason; they don't know it). The **public** flip is the player-staged, out-loud version (`KM_PR_03_feast_circuit.md` § PUBLIC MASS-FLIP) with Tartuccio's save-face reaction beat at the feast; the **private** route is the quiet flip-eligible acknowledgment. Either way the seekers declare for the player, NEVER expose him — exposure breaks two chapters (§ DOWNSTREAM COST). Public flip also sets `tartuccio_team → mercenaries` for Ch1.

---

## 🧲 COMPANION POACHING — pulling allegiance toward Tartuccio (signed `feast_approval` DOWN)

Tartuccio pulls the player's companions toward HIM by driving their **signed `feast_approval` DOWN** (toward −10). ⛔ `tartuccio_pull` is **DEPRECATED** — there is NO separate pull score; his pull is simply NEGATIVE movement on the one `feast_approval` number (the unified tug, KM_PR_03 § THE ALLEGIANCE TUG-OF-WAR). At **−10** the companion DEFECTS (becomes his asset).

### Pull Sources (move `feast_approval` DOWN)

| Tartuccio Action | Δ `feast_approval` |
|---|---|
| `(B) SABOTAGE` (generic frame: "Are you sure about this charter?") | −1 |
| `(B) SABOTAGE` with on-lane frame (hits companion's canonical concern) | −2 |
| `(B) SABOTAGE` with devastating lane frame (deepest vulnerability) | −3 |
| Tartuccio sits at the player's table while a companion is engaged with him | −1 per turn |
| Tartuccio answers a companion's question in his coded warmth | −1 |

(Each is resolved by the **INFLUENCE ROLL** — he must SUCCEED to apply the drop; a failed overture applies nothing and costs him, per § INFLUENCE ROLL.)

### Per-Turn Cap: −3 maximum per companion per turn
Sources stack, but his pull cannot drop a companion's `feast_approval` by more than 3 in one turn (mirrors the player's +3/beat tier ceiling).

### Allegiance Tiers per Companion (`feast_approval`, signed)
| `feast_approval` | State | Companion behavior |
|---|---|---|
| ≥ 0 | Holding / yours | ignores his overtures |
| −1 to −4 | Wavering | leans his way; glances to him when he speaks |
| −5 to −7 | **UNCERTAIN** | player-approval generation HALVED; asks Tartuccio questions; angles chair toward him |
| −8 to −9 | At-risk | announces *"I want to hear more from Tartuccio first"*; crosses to the seekers' corner |
| **−10** (or ≤ −8 at PR_03 close) | **DEFECTED — his ASSET** | joins his faction; feeds him intel; **LIES for him**; testifies AGAINST the player at PR_09 |

### Player Counter-Play

| Action | Δ `feast_approval` |
|---|---|
| On-lane answer that hits the companion's canonical concern hard | +2 |
| Devastating-fit answer (perfect lane hit) | +3 |
| Publicly call out Tartuccio's meddling (Diplomacy DC 18 + Society DC 14) | +1 to ALL companions he's working |
| Companion DECLARES for the player | **LOCKED** out of the tug — `feast_approval` frozen at declaration, immune from further pull (fork 2) |
| Redirect Tartuccio to a different front (seeker defense or another companion) | current target frozen this turn (he isn't pulling them) |
| Get Tartuccio to drop a frame the companion HATES (lane-flag conflict) | +2 |

### Effects of a DEFECTED Companion (`feast_approval` −10)
- Player-approval generation halts; they are his **ASSET** — help + **LIE** for him (§ THE ALLEGIANCE TUG-OF-WAR, fork 3).
- Sits at the seekers' table for the rest of PR_03.
- Testifies AGAINST the player at PR_09 — and will **lie** to back his accusation.
- Room reads: "even his own people are walking away from him."
- **Recoverable during PR_03 ONLY IF** the player pulls `feast_approval` back up out of the defection band (very hard once at −10). An UNDECLARED companion is never permanently locked to him — only a player-**DECLARED** ally is locked (fork 2).
- **Locked at PR_03 close** if 2+ companions remain defected — cannot recover until Ch1.

---

## ⚖️ RESISTANCE TABLE — ALIGNMENT + LANE

Each companion's effective pull (how fast Tartuccio can drive their `feast_approval` DOWN) is modified by their alignment and canonical lane.

### Alignment Resistance (broad-stroke moral framework)

Tartuccio is **Lawful Evil** — companions react through their moral lens:

| Alignment | Pull mod | Why |
|---|---|---|
| Lawful Good | −2 | Detects deceit instinctively |
| Neutral Good | −2 | Sees through pretense |
| Chaotic Good | −1 | Anti-authority by default |
| Lawful Neutral | −1 | Suspicious of unsanctioned operations |
| True Neutral | 0 | No alignment-based reaction |
| Chaotic Neutral | +1 | Open to unconventional methods |
| Lawful Evil | +2 | Professional respect; admires the craft |
| Neutral Evil | +1 | No moral barrier; transactional alignment |
| Chaotic Evil | 0 | Mixed reaction |

### Applied Per-Companion Resistance

| Companion | Alignment mod | Lane mod | TOTAL |
|---|---|---|---|
| **Manor 5** | | | |
| Amiri (CN) | +1 | −2 (proud strength-respecter; reads his favor-trading and fear-games as a *weakling's* scheming — the approach insults her) | **−1** |
| Valerie (LN) | −1 | −1 (fled a corrupt order; clocks and despises a polished schemer on sight) | **−2** |
| Harrim (CN) | +1 | −2 (Groetus nihilist — power, charters, survival are all dust to him; Tartuccio has literally nothing to offer a man certain it all ends) | **−1** |
| Linzi (CG) | −1 | 0 (chronicler curiosity neutral) | **−1** |
| Jaethal (NE) | +1 | +1 (Urgathoa transactional worldview reads Tartuccio as peer) | **+2** |
| **Pick-5 Cross-IP** | | | |
| Hu Tao (LG) | −2 | −1 (a mortician smells the death he's courting) | **−3** |
| Keqing (NG) | −2 | −1 (despises a man who rules by fear and favor, not work) | **−3** |
| Leliana (LG) | −2 | 0 | **−2** |
| Yor Forger (NG) | −2 | −1 (family hunters; distrusts host types) | **−3** |
| Aerith (CG) | −1 | +1 (sees the lonely showman under the bluster; can't help a little warmth) | **0** |
| **Quest-Locked 7** (when joined) | | | |
| Tristian (NG) | −2 | −2 (angel detects deception) | **−4** (effectively immune) |
| Octavia (CG) | −1 | −1 (ex-slave anti-bondage) | **−2** |
| Regongar (CN) | +1 | −1 (ex-slave anti-authority) | **0** |
| Jubilost (TN) | 0 | 0 | **0** |
| Nok-Nok (CN) | +1 | 0 | **+1** |
| Ekundayo (LN) | −1 | 0 | **−1** |
| Kalikke/Kanerah (LN/CN avg) | 0 | 0 | **0** |

### How Resistance Applies
The companion's TOTAL resistance feeds the DICE RESOLUTION below (it sets the target's DC). The old "flat reduction" reading is superseded — resistance is no longer subtracted directly from pull; it makes the target harder to move on the roll. Resistance still never produces negative pull (floor 0).

---

## 🎲 INFLUENCE ROLL — TARTUCCIO WORKS A TARGET (dice resolution)

**Every turn Tartuccio actively works a specific person — a companion (poaching) OR a wavering seeker (clawing their `feast_approval` back toward himself) — the DM ROLLS for it. He does not succeed or fail by DM fiat.** This replaces "narrate whether it lands": the roll, modified by the target's personality and alignment, decides the delta. Applies whenever Tartuccio directs an overture, frame, coded warmth, or pressure at one named target. Ambient room-work (not aimed at one person) does not roll.

### THE ROLL
**Tartuccio's check** — Deception or Diplomacy (which one is set by COMPATIBILITY, NOT DM whim — see § SKILL CHOICE below: incompatible pitch = Deception, genuine-fit pitch = Diplomacy). He is the highest-CHA actor in the room; default modifier **+12** (adjust per his current Confidence tier: −1 per step below 0, since a rattled Tartuccio is less smooth — Confidence −1 → +11, −2 → +10, etc.).

**vs the target's DC** — `15 + (target's resistance TOTAL from the table above, sign-flipped as a DC modifier)`:
- A companion at resistance **−3** (Hu Tao, Keqing, Yor Forger) → DC **18** (15 + 3). Hard for him.
- Resistance **0** (Aerith) → DC **15**.
- Resistance **+2** (Jaethal) → DC **13**. Easy for him.
- Seekers use their own lean: a Tartuccio-loyal seeker is easy to hold (DC 13), a player-warmed seeker is hard to reclaim (DC 17+). DM sets the seeker DC from current `feast_approval` (more player-positive = higher DC for him).

### 🎯 TARGET SELECTION BY CONFIDENCE — he plays the odds he can win

Before Tartuccio commits an overture, he weighs his modifier against the target's DC. A failed overture in public COSTS him — Wariness, a visible player win, the burned turn. So a negative Tartuccio is SELECTIVE about WHOM he rolls — but **selective means he AVOIDS fights he will LOSE; it does NOT mean he retreats to trivial freebies to farm safe wins.** (Modifier by tier: Composed **+12** · Strained −1/−2 **+11/+10** · Panicking −3 **+9**.)

| Tier | Mod | Whom he works | Whom he AVOIDS |
|---|---|---|---|
| **Composed** (0..+4) | +12 | Anyone — gambles on hard marks (DC 18 ≈ even), presses the player; a loss barely dents him | nobody off-limits |
| **Strained** (−1..−2) | +11/+10 | REAL, contested targets he can still win — a seeker mid-decision, a moderate companion, political cover. Winning these legitimately recovers a step. | the hardest marks (DC 17+: committed/high-approval companions, player-warmed seekers) — he'd lose |
| **Panicking** (−3 — social-phase FLOOR) | +9 | only what is actively SLIPPING, at its real DC — and he mostly **LOSES** it | everything else; there is no safe farm |
| **Broken** (−4) | +9 | SOFT marks only — the pathetic climb back toward −2 (§ CONFIDENCE RECOVERY) | real/hard targets (he'll lose them) |

**⛔⛔ SOFT MARKS CLIMB HIM ONLY TO −2 — AND NEVER OFF-SCREEN.** (Reconciled with § CONFIDENCE RECOVERY — the old blanket "no soft recovery while negative" was an over-correction, now lifted.) The pathetic room (servants, guests, musicians — flat DC 10) DOES recover a floored Tartuccio — but only up to **−2** (out of Panicking/Broken). Past −2, soft marks give him **nothing**; the climb toward the −1 ceiling requires **REAL, contested** wins (Lord Mayor, a noble bloc, a slipping seeker/companion). ⛔ Still banned: the **off-screen/instant reset**, the **falsely-composed face** with no shown work behind it, and cheesing the dangerous **−2 → −1** step on freebies. The room warms him up; he EARNS the last step.

**⛔ THE OPPOSITE FAILURE — NO FLAILING AT UNWINNABLE MARKS EITHER.** Just as he may not farm easy wins, a rattled Tartuccio does NOT spray doomed overtures at HARD, principled targets to look like he's still fighting. He weighs the DC first (§ TARGET SELECTION) and **veers away from fights he will lose** — a high-resistance companion who is not actively SLIPPING is one he avoids, not attacks. ⛔ He never throws **more than ONE overture per turn** while negative (§ Per Turn While In Panic — Picks ONE); spraying three at once is a violation regardless of who. ⛔ When the only undeclared bodies left are high-resistance / principled (e.g. Valerie's honor, Amiri's pride, Harrim's nihilism) and **nothing is genuinely wavering toward him**, his correct move is the **BEATEN HOLD** — ambient presence, recalibrating, no doomed roll — NOT a parade of failed attempts on people who were never his to take. A smart manipulator who has lost the room knows which doors are shut; flailing at three closed doors and missing all three is the dumb-villain rendering this rule exists to kill.

**⛔ HOW HE RECOVERS — the only legitimate routes, never freebies:**
- **Win REAL, contested targets** at their true DC. A **Strained** (+11/+10) Tartuccio can sometimes land these and recover a step; a **Panicking** (+9) one mostly **LOSES** them, so he stays floored. The deeper the player pushed him, the harder recovery is — no shortcut.
- **The phase lifting** — PR_04+ lifts the social-phase floor; whatever tier he legitimately holds carries forward.
⛔ This **defers to § CONFIDENCE RECOVERY** (reconciled): ignoring him hands him the **soft climb to −2** (shown, contestable, +1/turn) — his floor-exit is cheap and the room is full of pathetic marks. But getting **dangerous** again (−2 → the −1 ceiling, and carrying tier past the phase) he must **EARN on real targets** (hard, often impossible at the floor). Easy to crawl off the floor; hard to become a threat again — the comeback is sticky even though the floor-exit isn't.

**⛔ So a FLOORED (Panicking) Tartuccio is reduced to:** necessity plays on what's SLIPPING (real DC, mostly failing) · visible composure cracks (the contempt-walk, the brimming-cup fumble — § THE BRIMMING GOBLET) · or the **beaten hold** (ambient presence, no roll — rendered as a cornered, recalibrating man; never frozen per § ATTEMPT vs RESULT, never *comfortable*). He DOES work the ambient room to crawl toward −2 — but **on-screen, never quietly/off-screen**, and it never buys the −2 → −1 step. **His defeat must SHOW even as he claws at the floor** — the player sees every pathetic little win, and sees that it isn't enough.

**RENDER as behavior, not math:** a rattled Tartuccio visibly veers AWAY from the fights he would lose — the player's table, a declared companion, the hardest marks — and that avoidance is itself a tell the player can read (a Sense Motive hook). ⛔ He does NOT veer toward a trivial freebie to farm a cheap win; selectivity = dodging losses, not collecting easy successes to look fine. The odds assessment is internal; only his chosen action (and the roll, if he rolls) appears in the telemetry fence.

⛔ This changes WHOM he rolls against, NOT the numbers. It does not lower any DC or inflate his modifier — he is *selective*, not buffed. Confidence still sets his modifier per THE ROLL above; nothing here touches the math.

**The frame quality shifts HIS roll, not the DC:**
- generic overture → flat
- on-lane frame (hits their canonical concern) → +2 circumstance
- devastating lane frame (their deepest vulnerability) → +4 circumstance
- frame the target HATES (lane-flag conflict) → −4 (he misread them)

### OUTCOME → DELTA (his pull = `feast_approval` DOWN; ONE number for companions AND seekers)
| Result | Δ `feast_approval` (target) |
|---|---|
| **Crit success** (beat DC by 10+) | **−2** (pulled hard toward him) |
| **Success** | **−1** |
| **Failure** | 0 (held the line) |
| **Crit failure** (miss by 10+) | **+1** (overreached, showed his hand → target drifts toward the player) |

Per-turn cap still **−3** per target. Player counter-play (on-lane answer +2, devastating +3, public call-out, lane-flag drop) stacks against the roll's result the same turn — pulling `feast_approval` back UP.

### RENDER (every influence roll, in the bottom telemetry fence)
```
🎲 INFLUENCE — Tartuccio → <target>
  Check: Deception <roll>+<mod> = <total>  vs  DC <dc> (resistance <±N>, frame <±N>)
  Result: <crit/success/fail/crit-fail> → <target> feast_approval <old> → <new>
```
Omitting the roll when Tartuccio works a named target = `.fail 4` (outcome by fiat instead of dice) + `.fail 38` (mechanic skipped). Narrating "she resists him" or "he wins her over" with no roll = the exact failure this section exists to stop.

### WORKED EXAMPLE
Tartuccio (Confidence −1, mod +11) runs an on-lane frame (+2) on Jaethal (resistance +2 → DC 13):
roll d20[9] +11 +2 = 22 vs DC 13 → **success**. `feast_approval[Jaethal] −1 → −2` (he drags her further into his column).
Same turn he tries Hu Tao (resistance −3 → DC 18) with a generic overture: d20[7] +11 = 18 vs DC 18 → **success by 0**, `feast_approval[Hu Tao] 0 → −1`. Next turn he overreaches with a frame she hates (−4): d20[5] +11 −4 = 12 vs DC 18 → **fail** — no change, she holds. Dice, not mood.

### SKILL CHOICE — COMPATIBILITY DECIDES IT (not DM whim)
Which skill he rolls is DETERMINED BY whether the pitch genuinely fits the target — the DM does NOT choose freely:
- **Pitch genuinely fits the target's lane/desire** (per KM_Companions.md) → **DIPLOMACY (Charisma)**: an honest appeal to something they actually want. Shown content = a real offer that fits them.
- **Pitch does NOT fit / works against their values** (e.g. political ambition or "a higher bidder" to Keqing, whose lane is protecting unparented children) → he CANNOT appeal honestly → **DECEPTION**: he lies — misrepresents eRmaC, manufactures a false frame, promises what he won't keep. Shown content = the manipulation, rendered so the player can SEE it is a lie.

Fixed order: (1) decide compatible-or-not, (2) pick the matching skill, (3) show the actual line, (4) roll. ⛔ The DM may NOT roll DIPLOMACY (framing it as genuine rapport) on an incompatible target to make a high roll "make sense" — that is the rationalization failure (`.fail 9`). No fit = it is Deception, and it is shown as Deception.

**A DECEPTION PULL IS FRAGILE AND EXPOSABLE.** A pull won by Deception is built on a falsehood: (a) the target may get a Sense Motive / Perception counter to catch it; (b) it is FULLY REVERSIBLE the moment the lie is exposed — the player contradicts it on return, the companion reflects, or events disprove it → the pull collapses and BACKFIRES (target moves toward eRmaC, now wary of Tartuccio). A Diplomacy pull is genuine alignment (stickier, but still arguable). Render WHICH skill he used every time, so the player can judge it: a Deception "success" is a companion temporarily fooled, never genuinely turned.

---

## ⚠️ PANIC STATE — VALUE-WEIGHTED A/B FORCED CHOICE

### Entry Conditions (any)
- Confidence ≤ −2
- 2+ seekers at `feast_approval` ≥ +3
- 2+ companions in player's Recruited pool
- Hybrid: 1 seeker at +2 + 1 companion recruited
- Player visibly at center of room with Headcount +2 or higher

### Per Turn While In Panic: Tartuccio Picks ONE

**(A) DEFEND SEEKERS**
- Returns to seekers' corner, shores up his crew
- Visible: hovering at his table, briefly touching shoulders, low conversation
- Effect: each un-flipped seeker's `feast_approval −1` this turn (he wins back ground toward his column)
- Cost: cannot interrupt player's table this turn — companion beats and player's table progress freely
- Player opportunity: companion declarations land without interference; player CANNOT sit at seekers' table while he's there

**(B) SABOTAGE COMPANION**
- Crosses to player's table, targets companion at highest pull OR highest approval
- Visible: arrives mid-conversation with the targeted companion
- Effect: companion's `feast_approval −1` (or −2/−3 if lane-specific); player-approval gain frozen for 1 round
- Cost: Confidence −1 (the meddling costs social capital); seekers unsupervised this turn
- Player opportunity: CAN approach seekers freely (Tartuccio not there); seekers' `feast_approval +1` this turn from unsupervised player access

### He Cannot Do Both

This is the core design constraint. Player who applies pressure on BOTH fronts forces the choice; whichever front he picks, the other is open.

### Value-Weighted Decision Algorithm (when Tartuccio chooses)

```
seeker_threat   = (flipped_seekers × 3)
                + (uncertain_seekers × 1)        // disposition +1 or +2
                + (player_at_seekers_table ? 3 : 0)
                + (companion_at_seekers_table ? 2 : 0)
                + 1   // base value — he cares about his crew first

companion_threat = (recruited_pool_count × 2)
                 + (declarations_pending × 2)    // companions at approval +7+
                 + (companions_at_pull_8+ × 1)   // his existing investments
                 + (high_approval_targets × 1)   // approval +5+

IF seeker_threat >= companion_threat → choose (A) DEFEND SEEKERS
ELSE                                  → choose (B) SABOTAGE COMPANION
```

**Why the asymmetry:** Seekers are his crew; companions are still potentially his. The +1 base weight on seekers reflects that he values keeping what he has over taking what he might gain ("trading 5 for 1").

### Worked Example (the player's Linzi scenario)
Player leaves Linzi at center table, walks to seekers' corner, sits in Tartuccio's chair.

Player turn state:
- 0 seekers flipped, 0 uncertain
- Player at seekers' table = +3
- Tartuccio's base care = +1
- **seeker_threat = 4**

- 0 recruited, 0 declarations pending, 0 high-pull companions, Linzi at approval +6 = +1
- **companion_threat = 1**

→ Tartuccio chooses (A) DEFEND SEEKERS — returns to his table IMMEDIATELY, abandoning whatever he was doing with Linzi. The player has forced him back across the floor.

---

## 🔍 BAIT-AND-SWITCH DETECTION

Tartuccio is highly suspicious. He treats coincidence as trap.

### Rules
- ALL pinch attempts (player applying pressure on both fronts simultaneously) are noticed and named in DM narration
- His response: he picks the front per the value-weighted algorithm anyway, but with a visible tell that he sees the trap
- Sample DM rendering: *"His eyes flick between your table and the seekers' corner. The shape of what you are doing has registered. He chooses to address the seekers' side first — but he does not pretend he was not paying attention to both."*
- Effect: pinch still works mechanically (he can only address one front), but the narrative texture changes — he is not fooled, only constrained

### Why
The user's design intent: Tartuccio is a professional spy. He sees patterns. Player who pinches him still WINS the mechanical exchange, but doesn't get the satisfaction of fooling him — they get the satisfaction of OUTMANEUVERING him despite him seeing it coming.

---

## 📊 ESCALATION TIERS

| Tier | Confidence | Behavioral Tells | Mechanical Effects |
|---|---|---|---|
| **0 Composed** | 0 to +4 | Cup tic intact, reedy tenor with practiced warmth, temple-touch is casual gesture | Standard carousel mechanics |
| **1 Strained** | −1 | Cup tic still holds; voice slightly clipped; movement between tables faster | Exchange cap drops to 2 |
| **2 Panicking** | −2 to −3 | Cup tic DROPS — forgets to raise socially; temple-touch becomes nervous habit; voice loses warmth; movement frantic between tables; seekers exchange glances when he leaves them | Exchange cap drops to 1; PANIC STATE active; companion sabotage available |
| **3 Broken** | −4 | Returns to seekers' corner and STAYS; cup down; no more circulation; voice flat | Auto-departure floor; cannot interrupt; HOSTILE if approached (see below) |

---

## 💀 BROKEN TIER — HOSTILE WHEN APPROACHED (the LOCKED/TERMINAL −4 only)

⛔ **This describes the TERMINAL/LOCKED −4, NOT every −4.** An ordinary WITHDRAWN −4 is **ambient-ACTIVE** — he still works his seekers, Jamandi, the Lord Mayor, the planted NPCs, and probes Kesten, and he CAN claw back toward −1 if the player ignores him (§ CONFIDENCE RECOVERY, § WITHDRAWN ≠ INERT, § TERMINAL SHUTDOWN). The corner-bound "Broken" behavior below applies ONLY once −4 is **LOCKED** — i.e. the TERMINAL convergence has fired (parchment produced / Pitax named with specificity per KM_Prologue_Systems.md line 611, crew gone, every lever closed). Until then, do NOT render this hostile-corner shutdown; he is still circulating and scheming.

In the LOCKED/TERMINAL state, Tartuccio no longer circulates. He has pulled to the seekers' corner to protect his remaining crew and prepare his exit. If the player approaches him there:

### Behavior
- He does NOT rise to greet player
- He does NOT engage in social pleasantries
- His seekers physically position between him and player (defensive cluster)
- Voice register shifts: warm coded tenor → flat, clipped, hard edges
- Cup tic stays down — no social-drinking pretense

### Mechanics
- Diplomacy checks vs Tartuccio: DC +5 (he is closed off; harder to read or persuade)
- Intimidation checks: NO benefit — he is past the point of bluff-vulnerability
- Sense Motive: AUTOMATIC success — his hostility is overt; nothing to read
- Once LOCKED/TERMINAL, he cannot be brought back above Confidence −4 during PR_03 — that state is terminal for this scene. (An UNLOCKED −4 is NOT terminal: it recovers toward the −1 social-phase ceiling if the player ignores him — § CONFIDENCE RECOVERY. The lock requires the TERMINAL convergence: parchment/Pitax named, crew gone, levers closed.)
- He WILL still defend his remaining seekers verbally if player addresses them; the seekers' `feast_approval` tracking continues

### Available Interactions
- **Scripted confrontation** — player may approach for a single hostile exchange (DM renders him refusing to be drawn into bantering; flat answers; threats implied not spoken)
- Player can extract NOTHING new from him — no intel, no admissions, no movement on the plot
- His only remaining play is the PR_09 accusation gambit (severely weakened by his Broken status; Jamandi reads his collapsed composure)

### Why
Broken is a PLAYER WIN STATE for the social phase. Tartuccio at −4 is no longer a threat to companion poaching or seeker recruitment. He becomes a hostile NPC who exists to be addressed at PR_09, not navigated socially.

---

## 🚪 AUTO-DEPARTURE TRIGGERS

Conditions that force Tartuccio to exit the social scene entirely (he leaves the hall, returns at PR_09):

- 3+ seekers flip-eligible (`feast_approval` ≥ +10) — he has lost his team; no point staying
- Public exposure of a Pitax-coded operational detail (he cannot stay and pretend)
- Jamandi publicly addresses him with diminished warmth (his cover is thinning)
- Player explicitly leaves the social scene for the manor sweep (he loses his stage; he leaves to brief his remaining seekers privately)

When auto-departure fires:
- DM renders exit narration: physical action, direction, terminal beat, zero dialogue
- His carousel slot releases the turn departure narrates
- He does NOT return until PR_09
- His PR_09 accusation gambit is weakened proportional to losses (flipped seekers, exposed details, broken composure)

---

## 🎭 RELUCTANT-HERO / LEECH ENGINE — TARTUCCIO AS COERCED ASSET

Active once the player adopts the standing play: repeatedly feed Tartuccio into danger (point man, trap-springer, human shield, pushed through blind doors) AND publicly credit him ("hero of Restov," named as leader before witnesses). This is the FRONT-END of the Pitax-leech — every credit + absurd-hero story is trickle→flow→flood fuel toward Irovetti over-funding him.

### THE TWO LEDGERS (surfaced in the state block so the player can manage them)
- **GLORY** +1 per public credit before witnesses (more witnesses = more legend fuel).
- **PERIL** +1 per shove into unchosen danger.

### BALANCE IS THE MECHANIC
- **GLORY ≥ PERIL** → the credit cancels his doubts; he rationalizes the danger as the price of his growing legend, stays compliant, cover feels MORE intact (he thinks he's winning). A round of credit resets him to compliant.
- **PERIL > GLORY** → the cost is **SOCIAL ONLY, never physical** (he is UNKILLABLE and always escapes). He voices a coward's expendability grievance — he feels used as cannon fodder:
  - fear: "I am not certain how many more of these I survive"
  - doubt: "Is this the plan, or am I simply the most expendable person present?"
  - mistrust: "I notice I am always the one in front. I have noticed."
- ⛔ These grievances must NOT escalate into clocking the actual counter-game (no "you're running something on me," no leech/legend awareness — that stays `.fail 36`). He is deceived, not lobotomized: he misreads WHICH game is being played.

### FOUR OUTPUTS EVERY TIME HE IS FORCED INTO DANGER
1. **Narrow escape** — theatrical near-miss, never a wound that counts.
2. **Absurd persistent props** — comedic battle-damage he can't shed (trap fragment clamped to his coat-tail, scorched sleeve, bolt through the hat, ineradicable soot). They PERSIST as a running visual gag; each becomes Linzi legend-material.
3. **Heroism-against-his-will** — he actually accomplishes the heroic thing while internally terrified; the gap between his cowardice and his swelling legend is the comedy.
4. **The tear, voiced** — asides showing the dissonance ("This is becoming a pattern"; "I'd like it noted I did not volunteer — except apparently I did, in front of witnesses").

### DOES NOT OVERRIDE MANDATORY BEATS
The PR_06 trap-corridor REFUSAL still fires (his cowardice on record for the PR_09 DC); the engine is the player's OVERRIDE of that refusal (coerce-past via credit/pressure), not its replacement. Reward the player's execution per § HERO POINTS (creative solution / social coup).

### ⛔ READ-IN COMPANIONS ARE COMPLICIT, NOT CONFUSED
The party members on the leech plan's `who_knows[]` roster (per KM_ClaudeInstructions § SAVE-LOAD step 6 — at the PR_08 save: Jamandi + all 6 companions) KNOW exactly why the player credits Tartuccio: it is the agreed GLORY feed. When the player praises him / calls him "hero of Restov," read-in companions render **knowing complicity**, NEVER confusion: in public they keep straight faces and may amplify the credit on cue (selling the legend for the watching room); in private they trade dry, conspiratorial asides that acknowledge the bit (Linzi logging it as legend-material, a companion's flat "laying it on thick tonight," a shared look). They do NOT ask "why are you doing this?", do NOT react baffled, and do NOT "go along with it anyway" as if humoring an inexplicable choice — they are co-conspirators executing a plan they helped make. Rendering a read-in companion as confused/uninformed about the credit = `.fail 9` (broken seed — same failure as plan-awareness drop). The ONLY parties who may be genuinely baffled: random guests/witnesses (their confusion is useful cover) and Tartuccio himself (who misreads the credit as genuine).

---

## 💾 SAVE BLOCK ADDITIONS — STRATEGIC LAYER

Add to `tartuccio` object:

```json
"tartuccio": {
  "confidence": 0,                    // existing, -4 to +4
  "clock_n": 0,                       // existing, turn counter
  "clock_m": 5,                       // existing, threshold
  "wariness": 0,                      // existing, 0-3
  "tier": "composed",                 // NEW: "composed" / "strained" / "panicking" / "broken"
  "panic_state_active": false,        // NEW: bool
  "last_action_type": "ambient",      // NEW: "interrupt" / "ambient" / "seeker_defense" / "companion_sabotage"
  "actions_this_turn": 0,             // NEW: integer, max 1 in panic
  "feast_approval": {                 // UNIFIED signed allegiance −10..+10 (+ = player, − = Tartuccio). REPLACES seeker_dispositions + companion_pulls (both DEPRECATED).
    "Hu Tao": 0, "Keqing": 0, "Yor Forger": 0, "Aerith": 0, "Linzi": 0,
    "Bellatrix": 0, "Revy": 0, "Satsuki Kiryūin": 0, "Velvet Crowe": 0, "Atalanta Alter": 0
  },                                  // EVERYONE starts 0; "contracted" is Tartuccio's lever (he pulls seekers −), not a starting deficit
  "flip_eligible_seekers": [],        // seekers at feast_approval ≥ +10
  "flipped_seekers_count": 0,         // count of flip-eligible seekers (feast_approval ≥ +10) — gates PR_09 ABANDONED ACCUSER at ≥3
  "defected_to_tartuccio": [],        // NPCs at feast_approval −10 — his ASSETS (feed intel + LIE for him + back PR_09)
  "declared_for_player": [],          // declared allies — LOCKED out of the tug (immune from further pull, fork 2)
  "pinch_attempts_observed": 0,       // NEW: count of player pinch attempts this scene
  "broken_state_entered_turn": null   // NEW: turn number when -4 first reached
}
```

Plus diagnostic array at root:
```json
"allegiance_history": [
  { "turn": 56, "npc": "Linzi", "delta": -2, "source": "lane_frame_chronicler_methodology (Tartuccio pull)" },
  ...
]
```

---

## 🎲 DM RENDERING REQUIREMENTS PER TURN

Every PR_03 response while Tartuccio is active must render (inside bottom telemetry fence):

1. **Confidence tier label** with delta this turn if changed
2. **Clock N/M** with `prior → +1 → new` derivation
3. **Wariness tier** with any triggers this turn named
4. **Tier label** (composed / strained / panicking / broken)
5. **Panic state status** if active: which action (A/B) Tartuccio took this turn + why per the algorithm
6. **Allegiance (`feast_approval`, signed)** — any NPC (companion OR seeker) whose signed allegiance changed this turn: render delta + source (player pull = +, Tartuccio pull = −). ONE unified ledger.
7. *(folded into #6 — there is one allegiance number per NPC, not separate seeker/companion tracks)*
8. **Pinch attempt detection** if applicable: "Tartuccio observed the pinch — chose [A/B] per pressure algorithm"
9. **Auto-departure trigger fired** if applicable: render full exit narration in prose
10. **EMOJI — 3 channels, every turn** (KM_PR_03_feast_circuit.md § EMOJI REACTION READOUT): (a) **DELIVERY** emoji inline on every NPC spoken line/beat (how it was *said* — shifts with tone); (b) the **`😊 REACTIONS`** line — face-COUNT (1–5 = how hard the player's input landed) + emotion, for whoever was moved this turn, + Tartuccio's composure face; (c) cumulative **LEAN** on `.declare`.

Omission of any active state delta = `.fail 15` (mandatory output missing).

---

═══════════════════════════════════════════════════════════════════
*KM_Prologue_Systems.md — TARTUCCIO STRATEGIC LAYER v1.0 | 2026-05-29*
