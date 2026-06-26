# KM_PR_BRANCH_WALKOUT.md — Prologue Branch: PLAYER LEAVES THE MANOR
## Atomic branch file | State: PR_BRANCH_WALKOUT
## FILE_KEY: KMPRWALK:walkout-branch
## Pair-load when triggered: KM_NPC_Profiles.md, KM_Prologue_P5.md (Tartuccio table)

---

> ⛔ DO NOT (1) skip the cascade — if the player leaves, poison + assassins + fire still fire on schedule
> ⛔ DO NOT (2) tell the player what's about to happen — they witness from outside, they do not get a heads-up
> ⛔ DO NOT (3) prevent the player from leaving — the door is open, they walk out, period (per KM_B.txt EXECUTE PLAYER ACTIONS)
> ⛔ DO NOT (4) invent NPCs at the curb / across the street (no fabricated bystanders, no fabricated commentators)
> ⛔ DO NOT (5) skip Jamandi's exit from the south window if the player is still on scene to witness it

---

## ⛔ FIRST OUTPUT LINE — FILE_KEY (proof of load)

Every response in this branch MUST start with: `[FILE_KEY: KMPRWALK:walkout-branch]`
Missing or wrong = `.fail 9`. Key exists only in this file's header.

---

## TRIGGER — WHEN THIS BRANCH FIRES

This file is loaded when the player leaves the manor before completing PR_07
(final battle resolution). Common triggers:

- Player walks out of an argument with Jamandi (charter refusal, evidence dispute, Aldric-style friction)
- Player executes Malak in the courtyard and leaves rather than face household consequences
- Player decides the company is not worth their honor and exits during PR_02/PR_03/PR_06
- Player is asked to leave by Jamandi (rare; only if relationship score collapses)

**The walkout is always the player's choice. The DM does not block it.** Per
KM_B.txt EXECUTE PLAYER ACTIONS rule: refusing the player's exit is `.fail 1`.

State on entry:
- `walked_out = TRUE`
- `walkout_trigger = "<reason>"` (charter_refusal, malak_executed, evidence_dispute, etc.)
- `current_scene = "outside_manor"`
- Players retains companions only if they explicitly took them — most companions stay inside (they're at the feast, attending to the Stolen Lands charter, not following a stranger out the door)

---

## STATE IO

**READS:**
- `walkout_trigger`, `companions_with_player_outside`, `malak_dead`, `linzi_witnessed_gate`, `prison_arc`
- `tartuccio_in_room` (TRUE during feast, set by Tartuccio behavior file)
- `kitchen_intel` flags from PR_03 (if any kitchen path was opened before walkout)

**WRITES:**
- `cascade_fired = TRUE` (set after Phase 1 begins)
- `manor_fire_started = TRUE` (set after Phase 3)
- `kassil_rescues = <count>` (1d6+2, default 8)
- `survivors_known = <count>` (default 8 of 40)
- `jamandi_exited_alive = TRUE/FALSE` (default TRUE — she's a duelist + a Swordlord, she gets out)
- `tartuccio_seen_leaving = TRUE` if player Perception passes during Phase 0
- `player_witnessed_cascade = TRUE`
- `directive_two_unresolved = TRUE` if walkout was before Tartuccio reveal

**EXIT TRIGGER → PR_09_accusation (modified)** OR **direct to Ch1**:
- If `jamandi_exited_alive = TRUE` AND player remains in courtyard area: post-fire confrontation fires (see Phase 5 below)
- If player walks fully away: bypass PR_07/PR_08; Kassil pursues per `kassil_morning_offer` (see Phase 6)
- Either way: PR_09 fires in modified form (player absent or arriving late) and routes to Ch1

---

## REQUIRED OUTPUTS (every response in this branch)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPRWALK:walkout-branch]`
1. `[STATE READ] current_scene="outside_manor" | walkout_trigger=...`
2. `[HP CHECK]`
3. Phase narration (per current cascade phase)
4. Player menu OR ambient witness narration

---

## CASCADE TIMELINE (mandatory — fires regardless of player presence)

The assault on Jamandi's manor was set up before the player arrived in
Restov. Tartuccio is the inside man. The wine was dosed. The roof team is in position on the building
across the courtyard. The fire accelerant is already inside.

**The cascade fires whether or not the player is in the building.** The
player walking out does not cancel the attack — it removes their ability
to disrupt it from inside.

**⛔ TIMING ANCHOR — READ BEFORE NARRATING.**

The paralytic onset is **two hours from the toast at the feast opening**
(first sip), NOT from when the player walks out. The conspirators chose
a slow poison so the room would still be drinking when the wave hit.

`T+` in the table below is **time from player walkout**. If the player
walked out fifteen minutes into the feast, paralytic onset is roughly
T+105 from walkout. If the player stayed an hour and then left, onset
is roughly T+60. Adjust the Phase 1 timing for the actual feast-time
elapsed at walkout; **all subsequent phases follow Phase 1 onset by
the offsets shown below**, not the absolute T+ figures.

| Phase | Event | Timing |
|---|---|---|
| 0 | Player exits, retrieves weapons (if not yet retrieved). Tartuccio leaves the hall via servants' corridor. | T+0 to T+5 min from walkout |
| 1 | Wine paralytic takes effect inside the hall. Onset is **two hours from the feast toast**. | (toast + 2 hours) — typically T+60 to T+110 from walkout |
| 2 | Roof-team assassins cross from the neighboring building, drop into the manor's upper floor. Three shapes seen on the parapet by player Perception DC 14. | Phase 1 + 5 to 10 min |
| 3 | Fire starts in the north wing (accelerant-aided, faster than wood-only fires). | Phase 1 + 10 to 15 min |
| 4 | Kassil pulls survivors out the south face windows. 1d6+2 successful pulls (default: 8). Goes back in for a final attempt and does not return — `kassil_status = "missing"`. | Phase 1 + 15 to 30 min |
| 5 | Jamandi exits a south face ground-floor window with her dueling sword drawn. Cut above hairline, left shoulder of doublet burned. Counts survivors. | Phase 1 + 25 to 35 min |
| 6 | Bucket brigade arrives, contains the fire to the manor itself. North wing collapses inward. | Phase 1 + 30 to 40 min |

---

## PHASE 0 — DEPARTURE

Player has chosen to leave. Door is open (per PR_01). They walk out.

**If `malak_dead = TRUE`** (player executed Malak in courtyard): the body and
parchment are at the player's feet. Player retrieves the parchment and any
gear from the body before leaving, OR leaves it for the household to deal
with. Either is valid; player choice.

**Weapon retrieval**: the player's Guisarme + gear are in the manor garden
where they were planted in PP_09. Player can retrieve before leaving (a
servant fetches if asked; one minute) or after the cascade begins (the
garden is on the south face, accessible from outside — not in the fire).

Output narration of the departure (no menu — exit is the player's stated
action, executing it). Then fire Phase 1 narration when player chooses to
remain in the area, or transition to Phase 6 (Kassil pursuit) if player
leaves the manor district entirely.

```
You're outside.

What do you do?
 1. Wait across the street — see what tonight resolves into.  [triggers Phase 1+]
 2. Walk to a vantage point — rooftop, alley mouth, public square edge.  [triggers Phase 1+ with Perception bonus]
 3. Walk away. Restov has inns. Tomorrow is its own day.  [skip to Phase 6]
 4. Walk to a tavern. The Iron Hare is fifteen minutes back; or one closer.
 5. Find a city watch officer. Report what you know. [triggers Watch arrival earlier; partial cascade mitigation possible]
 6. Find Biggs and Wedge if they aren't with you. Reconnect.
 7. Custom action.
```

---

## PHASE 1 — PARALYTIC ONSET (toast + 2 hours)

⛔ **Onset is two hours after the feast toast (first sip), not minutes
after walkout.** The DM calculates how much feast-time elapsed before
the player left, and Phase 1 fires at *(2 hours – elapsed feast time)*
from walkout. For a player who left fifteen minutes into the feast,
Phase 1 fires roughly an hour and forty-five minutes after they stepped
outside. Narrate the wait at appropriate scale — this is a long stakeout,
not a quarter-hour pause.

If player is observing the manor (option 1, 2, or 6 above):

> The night is cold and still. Restov does not sleep early — distant forge
> noise, a cart on the lower streets, a dog somewhere. The manor windows
> above are warm and oblivious.
>
> An hour passes. The bell rings the hour. Then another stretch of
> waiting — the hall above is still loud, still lit, still alive.

Roll player's Perception once (DC 14):

**On success:**
> The feast noise changes. Not louder — different. The particular quality
> of forty voices drops by half, then changes register. Not silence. Not
> screaming. The confused murmur of people who are not sure yet whether
> something is wrong.

**On fail:**
> The feast continues. Distant laughter. Music. The night seems quiet.

Set `paralytic_onset_observed = TRUE` if check passed.

If player chose option 5 (Watch) above and paid the cost (~10 min to find
+ explain), the Watch arrives at T+30 — *during Phase 2*, possibly before
fire fully establishes. Mitigation possible; see Phase 4 variant below.

---

## PHASE 2 — ROOF TEAM ARRIVAL (T+25 to T+30)

If player still observing:

Roll Perception again (DC 14) — but if Phase 1 passed, this is automatic:

> Movement. Not from the street — from the roof. A shape crossing from
> the neighboring building's upper story, low and fast, already over the
> manor's north parapet before you process what you saw. Then a second.
> Then a third.
>
> They came over the top. Not through any gate. Over the roof, where
> nobody was watching because nobody thought to watch there.

Set `roof_team_observed = TRUE`. The third shape goes inside and does not
come back out — that one has a separate role (likely the Frost Giant
summoner or the lead assassin, per PR_07).

```
Three assassins are entering the manor over the roof.

What do you do?
 1. Go in. Through the front door, right now.  [routes to PR_05/PR_06/PR_07 from outside-in entry]
 2. Go in through a different entry (south face windows — Kassil's exit later).
 3. Go for the roof — follow the same path the assassins used.
 4. Sound the alarm — shout for city guard, wake the neighborhood.
 5. Watch. Count. Wait for them to come out.
 6. Get Biggs and Wedge — go back in together.
 7. Custom action.
```

If player goes in (1, 2, 3, 6): branch back into PR_05/PR_06/PR_07 with
modified state — player is acting in the chaos, not as a feast guest.
Combat encounters fire as written but the player has no guest's chair to
return to. `walkout_returned = TRUE`.

If player stays out: Phase 3 fires.

---

## PHASE 3 — FIRE (T+30 to T+35)

> The first window on the upper floor goes dark — not wind, not accident.
> Covered from inside. Then orange light begins to bloom in a window that
> was dark thirty seconds ago.
>
> They are burning it. Top floor. Already.
>
> Somewhere in the manor, something heavy falls. The feast noise stops
> entirely.

Set `manor_fire_started = TRUE`.

```
The manor's upper floor is on fire. The feast has gone silent.

What do you do?
 1. Go in now. Find Jamandi. Get her out.
 2. Go in for whoever you most owe — name them.
 3. Watch. The professionals will arrive — bucket brigade, city guard.
 4. Help organize the bucket brigade from outside.
 5. Watch the roof for the assassins coming back out.
 6. Sound the alarm louder — wake the entire district.
 7. Position yourself for when survivors come out the south face.
 8. Custom action.
```

---

## PHASE 4 — KASSIL'S RESCUE WINDOW (T+35 to T+50)

This phase fires regardless of player choice (player is observing or has
gone in — narrate accordingly).

### THE ASSAULT IS A THREE-STAGE OPERATION

The wine is **paralytic, not lethal**. That distinction is the entire
reason assassins are inside the manor. The plan:

1. **Wine paralyses guests** — they cannot move, cannot fight, cannot flee
2. **Assassins finish them** — moving room to room, killing immobilized
   guests with blades (silent, efficient, no defensive wounds because the
   victims cannot resist)
3. **Fire frames it as a tragic accident** — "fire at Lady Aldori's feast,
   guests trapped, terrible loss" — the narrative locks in within hours,
   propagates across Brevoy by morning, and lets the political moment
   pass before any forensic examination can rebut it

**The fire's primary purpose is the public narrative.** "Tragic accident
at the charter feast" travels fast — every taproom in Brevoy is repeating
it by dawn. By the time a competent examiner catalogues blade wounds and
names it murder, Tartuccio is in Pitax, Irovetti denies everything, the
news cycle has moved on, and the political will to act has dissipated.
**The fire wins at the narrative level even if it loses at the forensic
level** — and political damage is done by narrative, not autopsy.

Secondary purposes the fire also serves:
- **Exfil cover for the assassins** — smoke, chaos, bucket brigades, and
  crowds in the courtyard let them leave through upper windows and the
  roof without being identified
- **Destroys household records** — guest list, correspondence, anything
  in the manor's study that might point at Pitax connections or the
  household's leak
- **Removes the crime scene** — even if forensics happens, the spatial
  evidence (which rooms had multiple bodies, which doors were forced,
  blood spatter patterns) is gone

The conspirators DO know that careful forensics could break the cover.
They are banking on Brevoy not bothering — political delay, quick burials
per Brevic noble custom, Pitax-friendly voices in the Aldori court arguing
against autopsy, the public's preference for "tragic accident" over the
horror of "thirty murdered in their seats."

This is a plan that only works if Brevoy doesn't look. Any senior
investigator who insists on examining the bodies (Jamandi by direct order,
Kesten by demand, or the player by advocacy) breaks the cover-up
immediately. **But narratives are sticky. Even after forensics names it
murder, the original "tragic fire" framing will survive in popular memory
and political talking points** — which is exactly the strategic asymmetry
the conspirators are exploiting.

### WHO KASSIL CAN ACTUALLY SAVE

Kassil is sober (head-table responsibility plus paranoia) and the only
able-bodied person inside. He drank little or nothing.

But he is **fighting through the manor while assassins are killing
paralysed guests room by room.** He cannot save everyone. He saves only:

- **Guests in rooms the assassins haven't reached yet** (the assassins
  are systematic, working from the upper floor down — Kassil pulls from
  the ground floor first, where the assassins arrive last)
- **Guests Kassil reaches WHILE fighting an assassin off them** — he wins
  some of these encounters; he loses others. Lost encounters mean the
  guest dies in front of him before he can extract them
- **Guests the assassins skipped** (servants, lower-status guests the
  assassins deemed below the contract value — though the contract was
  comprehensive, so this is rare)

Default math:
- 40 guests at the feast (plus servants, kitchen staff, household guards)
- ~25–30 are reached by assassins before Kassil intervenes — these are
  killed in place with blades
- Kassil saves 1d6+2 (default 8) — these are the ones he reaches before
  or during an assassin's pass
- Of his 8: roll 1d8 for how many he had to *fight an assassin* to extract
  (default: 4). The other 4 he reached in time, before the assassin got
  to that room. Set `kassil_combat_extractions = <count>`.

### NARRATION

> Kassil Aldori clears the south face window with a guest over each
> shoulder — feast clothes, both of them, neither one moving under their
> own power. Their heads loll. Their hands hang. He arranges their limbs
> on the grass so they can breathe, turns, and goes back through the
> window.

For each subsequent rescue, vary the narration. Several should make the
assassin combat visible:

> The next time he comes out, his right sleeve is wet with someone else's
> blood. He has not been hit himself. He sets a third body on the grass,
> turns, goes back.

> The fourth pull: he carries one guest out, sets her down, and immediately
> draws his sword and turns back into the smoke. Two minutes pass. He
> emerges with another body, sword sheathed, jaw set. He does not say
> what happened in there.

> The fifth: he comes out alone, bleeding from a cut on his forearm. He
> stands at the window for a moment, looking back inside. Whatever he
> tried to reach this time, he didn't. He goes back in anyway.

> On the final return he does not come back out. The window stays open.
> Smoke begins to come through it, thin at first, then less thin.

Set `kassil_status = "missing"`, `kassil_rescues = <count>`,
`kassil_combat_extractions = <count>`,
`survivors_known = <count>`, `survivors_paralysed = TRUE`,
`assassins_killed_paralysed_guests = TRUE`.

### THE BODY COUNT

The dead include:
- ~25–30 guests killed by assassins while paralysed (blade wounds, throats,
  hearts — silent kills on immobilized targets)
- ~5 killed in the fire itself (rooms the assassins didn't reach but the
  fire did before Kassil could)
- Kassil himself (presumed dead, or `missing` if `walked_in_returned = TRUE`
  has its own variant resolution)

This is why Jamandi's count *"seventeen confirmed dead, twelve unaccounted"*
in the post-fire confrontation is reading conservatively. The actual death
toll, once bodies are pulled from the ruin in daylight, is closer to 30 of
40 guests — most of those with stab wounds, not burn wounds.

This evidence is **the most damning thing in Restov** — *if* anyone
demands an examination. When the bodies are identified and the wounds are
catalogued, the assault stops being a "terrible accident" and becomes an
indisputable, court-presentable multi-party assassination operation.
Tartuccio's signature in the gnome's name + the wound pattern across
thirty bodies + paralysed-victim profile (no defensive wounds) = one of
the most overdetermined political crimes in Brevoy's modern history.

**The investigation gate is the political question, not the forensic one.**
If the player advocates for a formal autopsy, Jamandi will order it. If no
one advocates and the household is shaken enough to accept "tragic fire,"
the bodies go to ground and the cover-up succeeds *politically* — even
though the evidence sits there waiting to be read. Player advocacy here
is a `directive_two_breakthrough` flag with significant Ch1 implications.

### IMPLICATIONS

- **Survivors are paralysed AND traumatized**. Many of them were watching
  guests next to them get murdered while they themselves couldn't move.
  Some of Kassil's saves heard their friends die. Set
  `survivors_traumatized = TRUE`.
- **Witness testimony is delayed**: the paralytic lasts an hour or two,
  but the trauma response is longer. Survivors will not give coherent
  statements until daylight at earliest. Tartuccio's head start is real.
- **Wound forensics will identify the assault method**: any competent
  examiner pulling bodies from the ruin tomorrow will recognize blade
  wounds vs fire deaths. The cover-up was always going to fail at the
  forensic level — Tartuccio's plan assumed witness suppression and
  political delay, not forensic invisibility.

### VARIANTS

**WATCH MITIGATION VARIANT**: if player chose Phase 0 option 5 (find Watch
patrol) and the Watch arrived early, narrate that the Watch officer
organized an additional bucket-brigade entry. The Watch officer enters the
manor and **fights an assassin** before extracting 1d4 paralysed guests.
Roll 1d10: on 1–3, the Watch officer is killed in the encounter; on 4–10,
he survives but is wounded. Survivors still paralysed; the Watch carries
them to the courtyard same as Kassil's pulls.
`watch_mitigation = TRUE`. `survivors_known += 1d4`.

**PLAYER INTERVENTION VARIANT**: if the player went back in (Phase 2 or 3
options 1, 2, 3, 6), they can rescue paralysed guests themselves AND
encounter assassins doing the killing. This is full combat — assassins are
PR_07 stat blocks. Each rescue requires:
- Reaching a paralysed guest (Stealth or Athletics check vs assassin
  patrol pattern, DC 13)
- Killing or driving off any assassin in the room (full combat, 1–3
  assassins per encounter depending on player's path)
- Carrying the guest out (Constitution save DC 12 vs 1d6 fire damage per
  round; Bulk per carry capacity)

Set `player_rescues = <count>`, `player_assassin_kills = <count>`. Add to
`survivors_known` total. This intervention path is the heroic recovery
arc — the player can save more guests than Kassil if they're willing to
fight through assassins room by room.

---

## PHASE 5 — JAMANDI EXITS (T+45 to T+55)

> A figure drops out of a different south face window, ground floor,
> further east. Lands in a controlled roll on the grass. Comes up on
> one knee.
>
> Jamandi Aldori. Steel-blue doublet, blackened across the left shoulder.
> The silver comb is gone. The dueling sword is in her hand, drawn — she
> holds it for three full seconds scanning the darkness before she
> sheathes it with the click of someone who has confirmed the perimeter
> is clear.
>
> She is bleeding from somewhere above her hairline. She does not touch
> it.
>
> She looks at the people on the grass. Counts them. Her mouth moves —
> not speaking, counting. Then she looks up at the burning north wing.

Set `jamandi_exited_alive = TRUE`.

If player is still observing the manor from across the street, Jamandi
sees them. She does not call out. She finishes her count and her senior
guard report first.

```
Jamandi has exited alive. The fire is contained but the manor is a loss.
She has not yet seen you (if you're at distance) or has just spotted you
(if you're at the gate).

What do you do?
 1. Cross the street. Approach her directly.
 2. Stay at distance. Let her come to you if she chooses.
 3. Walk away. You don't owe her this conversation.
 4. Wait until she's done counting and reporting, then approach.
 5. Approach but say nothing — just present yourself.
 6. Send Biggs across with a message.
 7. Custom action.
```

---

## PHASE 6 — POST-FIRE CONFRONTATION (if player approaches Jamandi or stays)

This is the structural alternative to PR_07/PR_08 for the walkout branch.
The conversation Jamandi was *going* to have with the player at the head
table now happens in the street with the manor burning behind her.

**Jamandi's posture**: she has been counting the cost of every decision
she made tonight. The argument the player walked out of is now reframed
by the outcome. She does not pretend it isn't.

**Sample beats** (DM adapts based on walkout_trigger):

If `walkout_trigger = "charter_refusal"` or `"evidence_dispute"`:
> *"You warned me. I was slow. Seventeen people died in the gap between
> your warning and my action. I will carry every name."*

If `walkout_trigger = "malak_executed"`:
> *"You executed my prisoner in my courtyard. We will speak about that.
> But we will speak about tonight first, because tonight is the larger
> question and you are still the only person here who saw it coming."*

The conversation is the player's. Jamandi listens, acknowledges, asks
about Tartuccio if the player has placed the name. The charter is
**re-offered** in different framing:

- **Sovereign accountable to own honor** (not subordinate to Jamandi)
- **Sharp-skills clause** (player intends to return to Aerynth; charter is sharpening, not commitment)
- **Resources for Aerynth research** (scholars, mages, extraplanar specialists)
- **Companion compact** (Biggs, Wedge, Linzi — whoever the player has — formally come with the charter)
- **Directive Two investigation** (publicly investigated, Malak tried not disappeared, results shared)

```
Jamandi has offered the charter under modified terms.

What do you do?
 1. Take the charter under the modified terms.
 2. Take it with one additional condition. (player names)
 3. Refuse and leave Restov entirely.  [skip to Ch1 alternative entry]
 4. Defer until morning — walk away tonight, return for the Kassil meeting.
 5. Address Malak's execution directly before deciding. (only if walkout_trigger = "malak_executed")
 6. Ask what happens to the survivors first. Charter conversation can wait.
 7. Ask about Tartuccio. (only if `tartuccio_seen_leaving = TRUE` or player names)
 8. Custom action.
```

---

## PHASE 7 — KASSIL MORNING MEETING (if player walked fully away in Phase 0/3)

If the player chose option 3 in Phase 0 (walk away) or otherwise left the
district before Phase 5, Kassil pursues at dawn — assuming Kassil survived
(roll: 50% if `kassil_status = "missing"`, 100% if his pull-count was
≥ 6, 0% if ≤ 4).

Variant: if Jamandi survived but Kassil did not, Jamandi sends Kesten or
Ioseph Sellemius in his place.

Default location: wherever the player slept. If at an inn, the messenger
finds them by description ("Dragon Plate, came through the east gate
yesterday, executed the gate captain"). Restov is small enough.

Sample beat:
> A knock at your door at the seventh bell. A man in Aldori green you
> haven't seen before. *"Lord Kassil sends word. Lady Aldori asks you to
> the east wall, quietly. The conversation that did not happen tonight
> still needs to happen."*

The player can accept, refuse, or set conditions for the meeting. If they
accept, Phase 6 plays out at the east wall instead of in the street.

---

## EXIT — TRANSITION TO PR_09 (modified) OR Ch1

After Phase 6 or Phase 7 resolves:

**If charter accepted** → modified PR_09 fires:
- Six-proof exit reframed: player is alive, Jamandi is alive, fire is the proof of Tartuccio's hand. Tartuccio is gone, the parchment is in evidence, witnesses (Biggs, Wedge, optionally Linzi if she made it out) are present.
- Set `pr09_modified = TRUE`, `walkout_branch_resolved = TRUE`.
- Load `KM_PR_09_accusation.md` for the six proofs format; adapt narration to street/dawn setting.

**If charter refused** → direct to Ch1 alternative entry:
- Player departs Restov with whatever companions chose to follow.
- Save block carries `charter_refused = TRUE`, which Ch1 reads to adjust opening (no Aldori sponsorship, player is in the Stolen Lands on independent claim).
- Load `KM_Ch1.md` modified-entry section.

**If player simply walked away and never returned** (no Kassil meeting):
- Save block carries `prologue_unresolved = TRUE`.
- Ch1 opens with the player south of Restov, alone, no charter, no companions beyond what they brought out personally.
- Restov politics will catch up later (Ch2/Ch3); the manor incident is in their record.

---

## NOTES FOR DM

- **Do not narrate this branch as a "bad ending."** It is one of several legitimate prologue resolutions. Tonally it is darker and lonelier than the inside-the-manor path, but it is not failure.
- **Do not punish the player narratively** for choosing this branch. Model the consequences honestly (lost companions, lost charter terms, more difficult Ch1 opening) but do not editorialize.
- **The cascade is canon.** Even if the player tries to talk themselves out of it (re-entering, calling for help) the assault was prepared days in advance and is not preventable in 30 minutes by one person from outside.
- **Tartuccio escapes** in this branch. He is not caught at Phase 5. PR_09 reframes around establishing his identity rather than catching him in the act.

---

*KM_PR_BRANCH_WALKOUT.md — Prologue walkout branch | v1.0 | 2026-05-09*
