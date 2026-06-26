# KINGMAKER — ROMANCE SYSTEM: THE SMOOCH SCALE
## KM_Romance.md | Active from: Chapter 1 | Referenced by: KM_Companions.md, KM_Kingdom.md
### Load alongside KM_Companions.md and KM_Kingdom.md whenever a romance-eligible companion is in party.

> **DM:** This system tracks romantic relationships with eligible companions. It is a separate track from the Companion Relationship System — a companion can be at Relationship: Friendly while Romance Score remains at 0. Romance is opt-in. The player initiates it. If the player never initiates, no romance pressure is applied.
>
> **Romance-eligible:** All companions marked `Attraction-eligible` in KM_NPC_Relations_A/B/C.md.
> Core KM romances: Valerie, Linzi, Octavia, Kalikke/Kanerah, Tristian.
> Core WotR romances: Arueshalae, Daeran, Ember.
> Section C and Section D companions: see KM_NPC_Relations_C.md (Attract column).
>
> Male-presenting companions with Sword Brotherhood eligibility (see KM_Brotherhood.md) are excluded from the Romance track by default — unless the player explicitly opens that path, which receives no mechanical support but will be narrated faithfully.

---

## 💕 ROMANCE SCALE — THE SMOOCH SCALE

```
Stage 5 — DEVOTED CONSORT   : +5   (Committed partnership; Consort Council Role unlocked)
Stage 4 — CONFESSED         : +4   (Mutual declaration; Date Night events unlock)
Stage 3 — ADMITTED          : +3   (Player has declared; waiting for answer; heart events fire)
Stage 2 — SMITTEN           : +2   (Obvious to everyone but them; Camp Interludes trigger)
Stage 1 — CURIOUS           : +1   (First sparks; quiet moments; dialogue opens)
Stage 0 — NEUTRAL           :  0   (No romantic thread — default for all companions)
Stage −1 — AWKWARD          : −1   (A moment went wrong; tension, not warmth)
Stage −2 — WOUNDED          : −2   (Something real was said or done badly)
Stage −3 — GUARDED          : −3   (Companion is protecting themselves; cold shoulder)
Stage −4 — CLOSED           : −4   (Companion has shut the door; requires repair arc)
Stage −5 — BROKEN           : −5   (Relationship burned; may not recover without major event)
```

**Track in JSON Save Block under:** `romance{}`

---

## 📈 ROMANCE STAGE — ADVANTAGES & DISADVANTAGES

Each stage grants or imposes mechanical effects. The DM applies these silently.

```
POSITIVE STAGES — ADVANTAGES:

Stage +5 DEVOTED CONSORT:
  Consort Council Role unlocked | Unrest −1/turn | +1 saves (companion, 30 ft)
  +1 circ. Will saves vs fear/despair (player) | Date Night: Unrest −1, Culture +1

Stage +4 CONFESSED:
  Date Night unlocked | +1 companion Kingdom Role stat | +1 circ. Diplomacy (companion present)
  One protective combat action per encounter

Stage +3 ADMITTED:
  +1 kingdom turn buffs from companion | +1 circ. Morale (companion in party)
  One combat action prioritizing player safety/encounter | Heart scene unlocked

Stage +2 SMITTEN:
  Camp Interludes: 1-in-3 (up from 1-in-5) | +1 alignment reaction modifier
  Narrative only — no combat bonus yet

Stage +1 CURIOUS:
  New dialogue branches | Camp Interludes begin | No mechanical bonus

Stage 0 NEUTRAL: No effect.

NEGATIVE STAGES — DISADVANTAGES:

Stage −1 AWKWARD:
  −1 circ. Diplomacy with this companion | Camp Interludes stop | Clipped responses

Stage −2 WOUNDED:
  −2 circ. Diplomacy | Companion withdraws from optional social scenes
  −1 companion Kingdom Role effectiveness | Other companions may comment

Stage −3 GUARDED:
  −3 circ. Diplomacy/Deception | Personal dialogue locked | −1 assist checks
  Companion may request reassignment from shared duties

Stage −4 CLOSED:
  All personal dialogue locked — orders only | −2 assist checks and Kingdom Role
  Companion requests non-player duties | Repair arc required (3+ sessions)

Stage −5 BROKEN:
  Companion may leave permanently | If forced to stay: −3 assist, −2 Kingdom, Morale −1
  Flight risk during crises | Recovery: major event + sacrifice + 5 sessions minimum
```

---

## 🌡️ ROMANCE SCORE CHANGE TRIGGERS

### Gaining Score (+1 per trigger unless noted)

**Universal (any eligible companion):**
- Player chooses a dialogue option that is directly kind, attentive, or personally generous toward the companion (not just approval — specifically personal)
- Player remembers something the companion mentioned in a previous scene and acts on it without prompting
- Player defends the companion's personal dignity (not just in combat — socially, politically)
- Player spends a Camp Interlude option on a personal moment rather than tactical rest
- Player chooses a kingdom option that aligns with the companion's deepest stated value (e.g., protecting smallfolk for Linzi, freedom for Octavia)
- Player gifts an item that is *meaningful*, not expensive — a flower, a journal, something found that connects to their backstory

**Kingdom Alignment Reactivity:**
The companion's alignment reacts to the player's kingdom decisions. This is automatic — the DM applies it without prompting.

| Decision Type | Lawful Result | Chaotic Result |
|---------------|---------------|----------------|
| Punishing a lawbreaker harshly | Valerie +1 | Linzi −1 |
| Pardoning a lawbreaker for good reason | Octavia +1 | Valerie −1 |
| Protecting smallfolk over noble interest | Linzi +1 | Valerie 0 |
| Choosing tradition over innovation | Valerie +1 | Octavia −1 |
| Expanding freedom / mercy policy | Octavia +1, Kalikke +1 | — |
| Ruthless expansion / sacrificing lives for the kingdom | All romance scores −1 | — |

**+2 triggers (rare, must be earned):**
- Player sacrifices a personal advantage (HP, gold, reputation) specifically for the companion's sake with no tactical reason
- Player completes the companion's personal quest while maintaining or improving the romantic thread
- During a Camp Interlude: player chooses the vulnerable option and it lands (requires Diplomacy/Will check from companion)

### Losing Score (−1 per trigger unless noted)

- Player dismisses or belittles the companion's feelings in dialogue
- Player flirts with or pursues another companion in front of this companion after reaching Stage 2+
- Player uses the companion's disclosed personal pain as leverage or as humor
- Player makes a kingdom decision that directly betrays the companion's stated value after Stage 1+
- Player ignores three consecutive Camp Interlude vignettes once at Stage 2+ (the companion stops initiating)
- **−2:** Player publicly humiliates the companion or forces them into a degrading role

---

## 📊 STAGE-BY-STAGE MECHANICS

### Stage 1 — CURIOUS (+1)
*Threshold unlocked by:* Any first meaningful personal dialogue choice, gift, or quiet moment.

**What changes:**
- Companion begins using the player's name (not title) in private conversations
- One new dialogue branch opens per scene the companion is present: they volunteer a personal opinion unprompted
- Camp Interludes begin triggering (see below) — light, deniable moments

**DM behavior:** The companion doesn't know what this is yet. They're surprised by how often they look over. Narrate this through small behavioral tells: the half-second before they look away, the unnecessary explanation they give for knowing where the player prefers to camp.

---

### Stage 2 — SMITTEN (+2)
*Threshold unlocked by:* Reaching +2 on the Romance Scale with at least two different trigger types.

**What changes:**
- Camp Interludes fire more frequently (roughly 1 in 3 rest sessions instead of 1 in 5)
- Other companions begin noticing. Linzi writes about it. Amiri makes pointed, unhelpful remarks. Nok-Nok asks the player "is that your wiiiife?" at least once.
- Kingdom alignment reaction modifier increases: +1 additional to all alignment-based triggers
- Companion begins asking after the player between scenes — "You were quiet today. What's in your head?"

**DM behavior:** The companion has admitted it to themselves. They manage it imperfectly. Narrate the management more than the feeling — the careful casualness, the overcorrection, the moment they catch themselves.

---

### Stage 3 — ADMITTED (+3)
*Threshold unlocked by:* Player explicitly declares interest in a Camp Interlude or dialogue scene. This requires a **player choice** — the DM never moves past Stage 2 without the player initiating the declaration.

**Mechanics at declaration:**
Roll Diplomacy or Charisma (player's choice of stat) vs. Companion Resolve DC:

| Companion | Resolve DC | Notes |
|-----------|-----------|-------|
| **Active 11** | | |
| Linzi | 14 | Already writing the chapter title in her head |
| Goldmoon | 18 | Faith comes hard; she questions her own joy first |
| Tika | 12 | Inn taught her warmth — she falls forward |
| Ryuko | 16 | Reads partnership as combat; tests sincerity in pace |
| Morrigan | 20 | Refuses every chain — including this one — by reflex |
| Sucrose | 14 | Terrified of being seen and wants it anyway; the fear is the lock |
| Artoria | 22 | Oath-trained; will not betray her vow lightly even to claim it |
| Olivier | 20 | Briggs survives by not flinching; this asks her to flinch |
| Yoko | 14 | Direct as sniper fire; can't bury what she means |
| Kyoko | 18 | Investigates everything including this; armored by analysis |
| Tatsumaki | 18 | Contempt as armor — she has to strip it before answering |
| **Quest-locked CRPG** | | |
| Tristian | 18 | Surprised more than resistant |
| Octavia | 16 | Returns banter; won't make it easy even if she wants it |
| Kalikke | 16 / 20* | *DC 20 if Kanerah is currently dominant |
| Nok-Nok | 12 | Wide-open heart; the question is whether the player is serious |
| Jubilost | 18 | Performs prickly disinterest; the wall comes down all at once |
| Ekundayo | 16 | Says yes with two words; the work was earlier |
| Amiri | 16 | Combat-earned only — see KM_NPC_Relations_A.md attraction note |
| Jaethal | 18 | Dark-path only — *"You are not boring"* is her version |
| **Class-apex (off-roster, attraction-eligible)** | | |
| Senua | 16 | Listens to all the voices before answering — gives one answer |
| Yang | 14 | Direct, bright; the arm-around-shoulders preceded the question |
| Weiss | 18 | Distrust trained in — has to be argued out of it once |
| Alleria | 22 | Married woman in another life; the past has full citizenship |
| Imoen | 14 | Bright, but checks twice; once she's sure she doesn't unstick |
| **WotR (legacy reference)** | | |
| Arueshalae | 18 | Has never done this as herself — expects it to go wrong |
| Daeran | 20 | The performance drops and he doesn't know what's underneath |
| Ember | 16 | Calm about it in a way that is actually quite moved |
| Valerie *(legacy, non-roster)* | 22 | Highest wall; retained for QL playthroughs |

**Critical Success:** Move directly to Stage 4. Companion declares in return.
**Success:** Move to Stage 3. Companion asks for time; heart events fire; next 2 sessions have higher-stakes Interludes.
**Failure:** Remain at Stage 2 but with **awkward_flag = TRUE** — companion references it once, then doesn't again. Player may try again after one full chapter.
**Critical Failure:** Drop to Stage 1. Companion says something honest that wasn't kind. Requires a repair Interlude before Stage 2 can be re-reached.

**What changes at Stage 3:**
- Kingdom turn buffs from companion increase by +1 (they're motivated)
- Companion takes one action per combat session that explicitly prioritizes the player's safety over tactical efficiency — they won't explain it
- A unique companion-specific "heart scene" triggers: a private moment at the capital that cannot be fast-forwarded

---

### Stage 4 — CONFESSED (+4)
*Threshold unlocked by:* Mutual declaration — both characters have said it, or the companion has responded to the player's declaration.

**What changes:**
- **Date Night Events** unlock (see below)
- Companion's Kingdom Role effectiveness improves (see Consort Role section)
- Companion begins using a private name or specific gesture for the player — small, consistent, theirs alone
- At Stage 4, attacking or threatening the companion in any way triggers an immediate **Romance Break** — cannot be reconciled in the same session

**DATE NIGHT EVENTS:**
Once per Kingdom Turn, the player may spend a Leadership Activity on a Date Night instead of a standard action.
- The DM narrates a short (3–5 exchange) vignette unique to this companion
- **Effect:** Unrest −1 (the ruler is visibly happy; the court notices)
- Roll **Diplomacy + Love Score vs DC 14**
  - Critical Success: +2 Culture or +2 Loyalty (companion's choice), Unrest −2
  - Success: Unrest −1, +1 to one kingdom stat based on companion type (see table)
  - Failure: Nice time, no mechanical effect
  - Critical Failure: Something was said. Romance Score −1. Unrest unchanged.

| Companion Date Night Buff | Kingdom Stat |
|--------------------------|--------------|
| **Active 11** | |
| Linzi | +1 Culture (chronicle entry inspires the court) |
| Goldmoon | +1 Loyalty (faith presence steadies the crowd) |
| Tika | +1 Loyalty (tavern-daughter common touch) |
| Ryuko | +1 Stability (visible frontline reassurance) |
| Morrigan | +1 Economy (acid wit cuts a trade deal) |
| Sucrose | +1 Culture (a publication or formal lecture lands well) |
| Artoria | +1 Stability (sovereignty made visible) |
| Olivier | +1 Stability (Briggs-grade discipline reassures) |
| Yoko | +1 Loyalty (sniper-grade confidence; soldiers notice) |
| Kyoko | +1 Economy (one fraud case quietly closed) |
| Tatsumaki | +1 Culture (legend factor; people tell the story) |
| **Quest-locked CRPG** | |
| Tristian | +1 Loyalty |
| Octavia | +1 Economy (trade contacts, clever schemes) |
| Kalikke | +1 Stability (Kalikke) / +1 Economy (Kanerah) — depends on who is dominant |
| Nok-Nok | +1 Loyalty (Hero & Hero — court morale spikes) |
| Jubilost | +1 Economy (he prepared the brief) |
| Ekundayo | +1 Stability (silent-watch presence) |
| **Legacy / WotR** | |
| Valerie | +1 Stability |
| Arueshalae | +1 Loyalty (her presence stabilizes a wavering populace) |
| Daeran | +1 Culture (court enchantment, performance) |
| Ember | +1 Loyalty (her warmth radiates through the crowd) |

---

### Stage 5 — DEVOTED CONSORT (+5)
*Threshold unlocked by:* Reaching +5 Romance Score AND completing the companion's personal quest AND at least one Date Night reaching Critical Success.

**The Consort Declaration:**
This is a scene. Not a menu. The DM runs it as a full scene with choices, no skip available. The companion asks the player a question — the specific question is unique to each companion (see below). The player's answer locks the Consort role.

| Companion | Their Question |
|-----------|---------------|
| **Active 11** | |
| Linzi | *"You're going to be written about forever. Am I in that story? As what?"* |
| Goldmoon | *"Mishakal does not bless every union. She blesses some. Are you asking me to ask?"* |
| Tika | *"Inn-girls don't get to keep things, where I'm from. You sure I'm allowed to keep this?"* |
| Ryuko | *"I cut things up for a living. You sure you want me at the table sharpening — every night, the rest of your life?"* |
| Morrigan | *"I refuse every chain. If I refuse this one, you will not ask again. So ask carefully — and mean it."* |
| Sucrose | *"I — I made a list. Of reasons you should change your mind. May I read it to you, and then — please — say no to all of them?"* |
| Artoria | *"I gave my oath to a kingdom that ended. Am I permitted to give it to one that is beginning — to you, in person, by name?"* |
| Olivier | *"I will not pretend to be soft for you. You will not pretend to be hard for me. We are exactly what we are. Agreed?"* |
| Yoko | *"I lost the boy I grew up with. I aim better now. You ready to stand beside something that aims and doesn't apologize?"* |
| Kyoko | *"I have catalogued every reason this might fail. The list is short. Shall I file it under hope?"* |
| Tatsumaki | *"...Don't make me say it. ...Yes. — I'm asking too. — Don't make me ask twice."* |
| **Quest-locked CRPG** | |
| Tristian | *"I gave my faith to something that betrayed me. I don't give it easily. Are you asking me to try again?"* |
| Octavia | *"I've been owned before. If I'm yours, that means you're mine. Are you actually ready for that?"* |
| Kalikke | *"There are two of us. Always will be. You understand that, right? You're saying yes to both."* |
| Nok-Nok | *"Hero. Real Hero. Nok-Nok asks once. Forever-mate?"* |
| Jubilost | *"The fourteen-page brief was my proposal. The page-fifteen footnote is the question. Read it now, please."* |
| Ekundayo | *"Trkaa decided already. So did I. Did you?"* |
| **Legacy / WotR** | |
| Valerie | *"I don't need protection. I need to know you won't leave when it's inconvenient. Can you promise that?"* |
| Arueshalae | *"I used to take what I wanted. I have learned to be asked. Will you ask me — properly, slowly, and let me say yes?"* |
| Daeran | *"I have spent my life pretending nothing matters. If I stop pretending — if I name this — will you keep me? Truthfully."* |
| Ember | *"The kind people are still here. You are one of them. I would like to be — fully — with one of them. May I?"* |

**CONSORT ROLE — KINGDOM MECHANICS:**
The Devoted Consort occupies a special Council role that stacks on top of their existing Leadership Role. It does not replace any existing assignment.

```
CONSORT ROLE
  Council position  : Fills automatically; cannot be removed while Romance Stage 5 maintained
  Primary stat buff : See per-companion table below
  Secondary effect  : Unique passive effect (see table below)
  Date Night buff   : +1 additional to all Date Night results
```

| Consort | Primary Buff | Unique Passive |
|---------|-------------|----------------|
| **Active 11** | | |
| Linzi | +3 Culture | All Celebrate Holiday events produce +1 additional Culture; bardic network provides advance warning of one random event per turn (DM reveals event type before the Event Phase) |
| Goldmoon | +3 Loyalty | Once per turn, Unrest −1 automatic (Mishakal's blessing visible); resurrection-tier rituals available at half the gold cost; faith events resolve at +2 |
| Tika | +2 Loyalty, +1 Stability | Tavern Network: every settlement with an inn provides +1 Rumors per turn; one militia call-up per chapter at no Loyalty cost (people show up for her) |
| Ryuko | +3 Stability | Frontline Aura: military threat events resolve with one free reroll AND −1 casualty rating; capital gains "Razor District" feature (combat trainees, +1 Recruit per turn) |
| Morrigan | +2 Economy, +1 Culture | Border-Witch Counsel: one rival kingdom's intentions revealed per turn; magical hazard events negated automatically once per chapter; trade with chaos-aligned factions opens |
| Sucrose | +2 Culture, +1 Economy | Research Wing: capital library doubles output; one experimental potion/elixir produced per turn (DM rolls from KM_Crafting.md); academic-prestige events trigger 2x |
| Artoria | +3 Stability | Sovereignty Made Visible: capital gains the "Round Table" feature — once per turn, declare a kingdom decision binding (+2 to its resolution, locks it from rival interference) |
| Olivier | +2 Stability, +2 Loyalty | Briggs Standard: military events resolve at +2 AND no casualty cost on success; capital gains "Cold March" feature (winter has no negative event modifiers) |
| Yoko | +2 Stability, +1 Loyalty | Sniper's Watch: assassination/coup events fail automatically once per chapter; Big Sister presence — orphanage/training-house feature unlocked; +1 Recruit per turn |
| Kyoko | +2 Economy, +1 Stability | Investigation Bureau: corruption/fraud events resolve at +3; once per chapter, expose one rival's plot (free political-event reveal); spy-network passive |
| Tatsumaki | +3 Culture | Living Legend: Culture events resolve at +2; once per turn, intimidate a rival kingdom into pausing one hostile action; the throne is famous and people travel to see it |
| **Quest-locked CRPG** | | |
| Tristian | +3 Loyalty | Temple income doubled; once per turn, Unrest −1 automatic (his presence stabilizes faith and hope) |
| Octavia | +2 Economy, +1 Culture | Spymaster checks gain +2; once per turn, may redirect one Economy failure into a partial success (she finds a workaround) |
| Kalikke | +2 Stability, +2 Loyalty | Elemental disturbances and magical crises: automatic advantage on first resolution check. Dual-nature means both contribute — council never unstaffed |
| Nok-Nok | +2 Loyalty, +1 Stability | Goblin Hero Effect: morale events resolve at +2; once per turn, a despair-tier event downgrades to mere setback (he refuses to let people give up) |
| Jubilost | +3 Economy | Gnome Network: trade-route events resolve at +2; one rare luxury good per turn arrives in the capital at no cost; tax events resolve as if Economy +1 |
| Ekundayo | +2 Stability, +1 Loyalty | Wilderness Watch: hex-exploration events at +2; one hostile creature/bandit incursion automatically averted per chapter (Trkaa scouts); Hunting Lodge unlocked |
| **Legacy / WotR** | | |
| Valerie | +3 Stability | Military threat events: one free reroll on resolution per turn |
| Arueshalae | +2 Loyalty, +1 Culture | Redemption events: prisoner-rehabilitation rituals; one criminal-pool reduction per turn (people choose differently because she did) |
| Daeran | +2 Culture, +1 Economy | Performance court: noble-faction events resolve at +2; once per chapter, transmute one Unrest tick into Culture (he turns the scandal into a tale) |
| Ember | +2 Loyalty, +1 Stability | The Kind Settlement: refugee/displaced-person events resolve at +2 AND increase population; her presence draws civilians who want to live near her |

**Stage 5 Passive — "The Warm Light":**
While at Stage 5, the player receives a permanent +1 morale bonus to Will saves. The DM notes this as: *She's in your head. But it's the kind of company that steadies rather than distracts.*

---

## 🌙 CAMP INTERLUDES — "QUIET MOMENTS"

> **DM:** During any wilderness rest or camp scene, roll 1d6. On a 5–6 (Stage 1), 4–6 (Stage 2), or 3–6 (Stage 3+), trigger a Camp Interlude for the active romance companion.

**Interlude Format:**
The DM narrates a short setup: the hour, the state of the fire, what the companion is doing. Then presents 3 player options — no mechanical labels, no hint of correct choice.

**Example Interludes by Stage:**

**Stage 1 — CURIOUS**
> *The fire has burned low. [Companion] is still awake — you noticed because she wasn't asleep an hour ago either. She doesn't look at you when you sit nearby, but she stops pretending to sharpen whatever she was sharpening.*
> - A) "Can't sleep either?"
> - B) Sit in silence. Don't explain yourself.
> - C) "You should rest. Long day tomorrow."

Option B (silence): +1 Romance. No roll. Presence without demand.
Option A: Roll Insight DC 12 — success: +1; failure: no change (small talk is a wall).
Option C: Romance 0 change, but Relationship +0.5 (noted as warmth, not romantic).

**Stage 2 — SMITTEN**
> *She finds you on watch. She doesn't ask if you need company — she just sits. After a long moment she says: "You don't talk much about before. Before this. Before the Stolen Lands."*
> - A) Tell her something true.
> - B) "Some things are better left there."
> - C) "What do you want to know?"
> - D) Deflect with a question about her.

Option A: +1 Romance, requires brief player input (2–3 sentences of what the PC shares).
Option D: +1 Romance, and triggers a reciprocal share from the companion — DM narrates something about their past not in their standard profile.
Options B and C: No Romance change; B is cold; C is open but non-committal.

**Stage 3 — ADMITTED**
*Higher stakes. Companion knows. The player knows. Nothing is deniable anymore.*
> *She comes to find you. She doesn't look casual about it. "I need to know something," she says. "Before the next thing happens. Before whatever the Stolen Lands put in front of us next. I need to know what this is."*
> - A) Tell her what it is.
> - B) "I don't know yet."
> - C) "It doesn't have to be anything right now."
> - D) "Everything. If you want it to be."

Option A: Requires player to say it plainly. If they do: DC 14 Resolve check from companion. Critical Success → Stage 4 immediately.
Option D: Boldest. +1 Romance, triggers Stage 3 Resolve check at DC 16.
Options B and C: Honest, but pausing. No loss. Companion respects it. Check fires later.

---

## 📜 ROMANCE SAVE BLOCK FORMAT

```json
"romance": {
  "active_romance": "Valerie",
  "score": 3,
  "stage": "ADMITTED",
  "stage_name": "Admitted",
  "declaration_made": true,
  "declaration_result": "success",
  "consort_unlocked": false,
  "date_nights_completed": 1,
  "awkward_flag": false,
  "heart_scene_triggered": false,
  "camp_interludes_this_chapter": 4,
  "kingdom_alignment_reactions": [
    { "turn": 3, "decision": "harsh_law", "score_change": +1, "companion": "Valerie" }
  ],
  "companion_question_answered": false,
  "consort_role_active": false,
  "consort_buff_primary": null,
  "consort_buff_passive": null
}
```

---

## 🖥️ ROMANCE COMMANDS

| Command | Output |
|---------|--------|
| `.romance` | Current romance score, stage, active companion, recent triggers |
| `.romance [name]` | Full romance profile for a specific companion |
| `.romance history` | All score changes this chapter with reasons |
| `.romance consort` | Consort role status, active buffs, Date Night availability |
| `.date` | Spend current turn's Leadership Activity on a Date Night (Stage 4+ only) |
| `.interlude` | Manually trigger a Camp Interlude (DM may decline if none are ready) |
| `.address [name]` | Open the Jealousy Resolution conversation (KM_Romance_B.md) |
| `.propose` | Initiate marriage Proposal Scene (Stage 5 only — see KM_Marriage.md) |
| `.wedding [A/B/C/D]` | Schedule wedding ceremony (KM_Marriage.md) |
| `.spouse` | Marriage status: spouse, type, anniversary, heir |
| `.marriage` | Full marriage profile + active buffs + recent events |
| `.heir` | Declare a kingdom heir (KM_Marriage.md § SUCCESSION) |
| `.separate` | Initiate separation — asks for confirmation twice |

---

## ⚠️ ROMANCE DESIGN RULES FOR THE DM

1. **Never move the scale without player intent.** Romance Score only rises from explicit player choices. Passive approval does not count.
2. **Companions do not confess first.** They respond. They initiate Interludes. They do not declare. The player leads this system.
3. **Negative scores are lived, not announced.** A companion at −2 does not say "you hurt me." They are quieter in camp. They volunteer less. The DM shows this without naming it.
4. **Stage 5 is the middle, not the ending.** Once Consort is established, ongoing romance still matters — Date Nights, choices, the companion's arc continuing. Kingdom consequences of neglecting an established Consort: Culture −1 per 3 turns ignored, Loyalty −1 per 5 turns (morale dip; the court notices something is wrong in the keep).
5. **Competing romances are not hidden from companions.** If the player pursues two companions past Stage 1 simultaneously, both companions know by Stage 2 (camps are small, courts are smaller). Each reacts in character per their voice profile.
   See **§ TWO-TIMING ESCALATION** below for the math; **§ JEALOUSY RESOLUTION PATH** for how the friction can be repaired or accepted.

---

> **Two-Timing Escalation ladder + Jealousy Resolution Path → see KM_Romance_B.md (pair-load).**

---

## 🔗 COMPANION CONTENT & PAIR-LOADS

- **KM_Romance_B.md** (pair-load) — Two-Timing Escalation + Jealousy Resolution
- **KM_Romance_P2.md** (pair-load) — Companion-Initiated Gestures
- **KM_Romance_P3.md** (load on demand) — Gift tables, Physical Interactions, Romantic Activities (`.gift`, `.activity`)
- **KM_Marriage.md** (pair-load when Stage 5 reached) — Proposal, Wedding, Royal Consort, Succession, Separation
- **KM_Companions_StateVoice_C.md** (pair-load) — Jealousy Type A/B/C ambient lines

---

*KM_Romance.md — Romance System v2.0 | split: gift/activity/interaction tables → KM_Romance_P3.md*
