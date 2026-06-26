# KINGMAKER — ROMANCE SYSTEM
## KM_Romance.md | Active from: Chapter 1 | Referenced by: KM_Companions.md, KM_Kingdom.md
## v3.0 (2026-05-22): Merged from KM_Romance + _B + _C + _P2 + _P2_B + _P3 + _P4. Single source of truth.
### Load whenever a romance-eligible companion is in party. KM_Romance.md stays separate (Stage 5 gate).

> **DM:** This system tracks romantic relationships with eligible companions. It is a separate track from the Companion Relationship System — a companion can be at Relationship: Friendly while Romance Score remains at 0. Romance is opt-in. The player initiates it. If the player never initiates, no romance pressure is applied.
>
> **Romance-eligible:** All companions marked `Attraction-eligible` in KM_NPCs.md.
> Core KM romances (Roster v2 keep-list): Valerie, Linzi, Octavia, Kalikke/Kanerah, Tristian.
> Cross-IP / Seeker romances (arcs live below — the "Phase D pending" tag is stale): Hu Tao, Keqing, Leliana, Yor Forger, Aerith, Bellatrix Lestrange, Revy, Satsuki Kiryūin, Velvet Crowe (Thaumaturge), Atalanta Alter.
> Section C and Section D companions: see KM_NPCs.md (Attract column).
> ⛔ Removed in Roster v2 (do not roll for): Arueshalae, Daeran, Ember, and all other WotR / Iconic / removed cross-IP names. See KM_CompanionIndex.md.
>
> Male-presenting companions with Sword Brotherhood eligibility (see KM_War_Systems.md) are excluded from the Romance track by default — unless the player explicitly opens that path, which receives no mechanical support but will be narrated faithfully.

**Table of Contents**
- [Romance Scale — The Smooch Scale](#romance-scale--the-smooch-scale)
- [Stage Advantages & Disadvantages](#stage-advantages--disadvantages)
- [Romance Score Change Triggers](#romance-score-change-triggers)
- [Stage-by-Stage Mechanics](#stage-by-stage-mechanics)
- [Camp Interludes — Quiet Moments](#camp-interludes--quiet-moments)
- [Two-Timing Escalation](#two-timing-escalation)
- [Jealousy Resolution Path](#jealousy-resolution-path)
- [Companion Rivalry — Jealousy Turns Physical](#companion-rivalry--jealousy-turns-physical)
- [Passive Jealousy Heat](#passive-jealousy-heat)
- [Date System](#date-system)
- [Fight System (Player-Companion Confrontation)](#fight-system-player-companion-confrontation)
- [Maintenance Tax](#maintenance-tax)
- [Graceful Fade](#graceful-fade)
- [Caught Cheating](#caught-cheating)
- [Love Scene System](#love-scene-system)
- [Companion-Initiated Contact](#companion-initiated-contact)
- [Companion Gesture Profiles](#companion-gesture-profiles)
- [Companion Flirt Actions](#companion-flirt-actions)
- [Universal Behavioral Signals](#universal-behavioral-signals)
- [Gift System](#gift-system)
- [Physical Interactions](#physical-interactions)
- [Romantic Activities by Stage](#romantic-activities-by-stage)
- [Companion Romance Profiles](#companion-romance-profiles)
- [Save Block & Commands](#save-block--commands)

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

## 📈 STAGE ADVANTAGES & DISADVANTAGES

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

### Stage 2 — SMITTEN (+2)
*Threshold unlocked by:* Reaching +2 on the Romance Scale with at least two different trigger types.

**What changes:**
- Camp Interludes fire more frequently (roughly 1 in 3 rest sessions instead of 1 in 5)
- Other companions begin noticing. Linzi writes about it. Amiri makes pointed, unhelpful remarks. Nok-Nok asks the player "is that your wiiiife?" at least once.
- Kingdom alignment reaction modifier increases: +1 additional to all alignment-based triggers
- Companion begins asking after the player between scenes — "You were quiet today. What's in your head?"

**DM behavior:** The companion has admitted it to themselves. They manage it imperfectly. Narrate the management more than the feeling — the careful casualness, the overcorrection, the moment they catch themselves.

### Stage 3 — ADMITTED (+3)
*Threshold unlocked by:* Player explicitly declares interest in a Camp Interlude or dialogue scene. This requires a **player choice** — the DM never moves past Stage 2 without the player initiating the declaration.

**Mechanics at declaration:**
Roll Diplomacy or Charisma (player's choice of stat) vs. Companion Resolve DC:

| Companion | Resolve DC | Notes |
|-----------|-----------|-------|
| **Active 11** | | |
| Linzi | 14 | Already writing the chapter title in her head |
| **Quest-locked CRPG** | | |
| Tristian | 18 | Surprised more than resistant |
| Octavia | 16 | Returns banter; won't make it easy even if she wants it |
| Kalikke | 16 / 20* | *DC 20 if Kanerah is currently dominant |
| Nok-Nok | 12 | Wide-open heart; the question is whether the player is serious |
| Jubilost | 18 | Performs prickly disinterest; the wall comes down all at once |
| Ekundayo | 16 | Says yes with two words; the work was earlier |
| Amiri | 16 | Combat-earned only — see KM_NPCs.md attraction note |
| Jaethal | 18 | Dark-path only — *"You are not boring"* is her version |
| Valerie | 22 | Highest wall; tower-shield steward |
| **Cross-IP / Seekers** | | |
| Leliana | 18 | She will decline your interest gently — twice, to give you room to run. The third time she stops declining. |
| Hu Tao | 18 | Hides behind the bit — outrageous flirtation, a dreadful love-poem. Answer a joke with real sincerity three times and the mischief finally drops. |
| Keqing | 20 | Redirects to the practical, a half-beat too fast (the speed is the tell). Won't admit it until she's filed you under proven-reliable. |
| Yor Forger | 18 | Takes it literally as friendship — she doesn't believe she's wanted as *herself*. Be unmistakable, and she goes very still. |
| Aerith | 16 | Teases it away and steers to your wellbeing. Insist it's *her*, not the healer, and the brightness wavers to the sadness underneath. |
| Bellatrix | 20 | NOT won by warmth (softness bores her). Won only by a hard, grand, unflinching will turned on her as command. Mercy cools her toward contempt. |
| Revy | 22 | Does her deliberate worst to make you fail the test and leave. Stay past three rounds without flinching and without coddling. |
| Satsuki Kiryūin | 20 | Meets it head-on, names it, dares you to mean it. Will not tolerate flattery or a lever dressed as love. |
| Velvet Crowe | 24 | Highest wall of any companion. Crueler the closer it gets. Gated on never flinching from the daemon — and NEVER pitying her. |
| Atalanta Alter | 22 | Flirts back as a fun hunt while swearing there's no soft center to win. Keep reaching, gently, without trying to "cure" her. |

**Critical Success:** Move directly to Stage 4. Companion declares in return.
**Success:** Move to Stage 3. Companion asks for time; heart events fire; next 2 sessions have higher-stakes Interludes.
**Failure:** Remain at Stage 2 but with **awkward_flag = TRUE** — companion references it once, then doesn't again. Player may try again after one full chapter.
**Critical Failure:** Drop to Stage 1. Companion says something honest that wasn't kind. Requires a repair Interlude before Stage 2 can be re-reached.

**What changes at Stage 3:**
- Kingdom turn buffs from companion increase by +1 (they're motivated)
- Companion takes one action per combat session that explicitly prioritizes the player's safety over tactical efficiency — they won't explain it
- A unique companion-specific "heart scene" triggers: a private moment at the capital that cannot be fast-forwarded

### Stage 4 — CONFESSED (+4)
*Threshold unlocked by:* Mutual declaration — both characters have said it, or the companion has responded to the player's declaration.

**What changes:**
- **Date Night Events** unlock (see Date System)
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
| **Quest-locked CRPG** | |
| Tristian | +1 Loyalty |
| Octavia | +1 Economy (trade contacts, clever schemes) |
| Kalikke | +1 Stability (Kalikke) / +1 Economy (Kanerah) — depends on who is dominant |
| Nok-Nok | +1 Loyalty (Hero & Hero — court morale spikes) |
| Jubilost | +1 Economy (he prepared the brief) |
| Ekundayo | +1 Stability (silent-watch presence) |
| Valerie | +1 Stability |
| **Cross-IP / Seekers** | |
| Leliana | +1 Culture (the court hears the new verse; something old and steady lifts) |
| Hu Tao | +1 Loyalty (the dead are honored properly; a people trusts a ruler who minds their grief) |
| Keqing | +1 Economy (she did the books over dinner and found three inefficiencies) |
| Yor Forger | +1 Stability (threats to the court quietly stop materializing; no one asks why) |
| Aerith | +1 Culture (gardens bloom where they shouldn't; the healer's grace lifts the whole court) |
| Bellatrix | +1 Stability (no one dares disturb the peace anywhere near her; uneasy, but quiet) |
| Revy | +1 Economy (she knows exactly which trees to shake and who owes whom) |
| Satsuki Kiryūin | +1 Stability (her mere presence at the ruler's side straightens every spine in the hall) |
| Velvet Crowe | +1 Stability (whatever was scratching at the edges of the realm has been devoured) |
| Atalanta Alter | +1 Stability (the wilds around the capital have gone very quiet and very afraid) |

### Stage 5 — DEVOTED CONSORT (+5)
*Threshold unlocked by:* Reaching +5 Romance Score AND completing the companion's personal quest AND at least one Date Night reaching Critical Success.

**The Consort Declaration:**
This is a scene. Not a menu. The DM runs it as a full scene with choices, no skip available. The companion asks the player a question — the specific question is unique to each companion (see below). The player's answer locks the Consort role.

| Companion | Their Question |
|-----------|---------------|
| **Active 11** | |
| Linzi | *"You're going to be written about forever. Am I in that story? As what?"* |
| **Quest-locked CRPG** | |
| Tristian | *"I gave my faith to something that betrayed me. I don't give it easily. Are you asking me to try again?"* |
| Octavia | *"I've been owned before. If I'm yours, that means you're mine. Are you actually ready for that?"* |
| Kalikke | *"There are two of us. Always will be. You understand that, right? You're saying yes to both."* |
| Nok-Nok | *"Hero. Real Hero. Nok-Nok asks once. Forever-mate?"* |
| Jubilost | *"The fourteen-page brief was my proposal. The page-fifteen footnote is the question. Read it now, please."* |
| Ekundayo | *"Trkaa decided already. So did I. Did you?"* |
| Valerie | *"I don't need protection. I need to know you won't leave when it's inconvenient. Can you promise that?"* |
| **Cross-IP / Seekers** | |
| Leliana | *"I have been trying to write the last line of this verse since the day I picked the lute back up in that shrine. It always came out an elegy — every ending I tried was a grief. I think you are the reason it might finally come out a vow. Tell me I'm right."* |
| Hu Tao | *"I bury everyone eventually — it's the one promise I never get to break. So here's the real question, no joke on top of it: can you live, and keep living, and not make me file you in early? That's the only vow I want."* |
| Keqing | *"I built my entire life so I'd never have to depend on anyone. I am asking to depend on you. Tell me plainly it isn't a miscalculation — and mean it, because I have checked this math too many times to be lied to now."* |
| Yor Forger | *"You've seen both of me — the clumsy one and the one with the knife. Most people only ever get to love half a person. Are you truly saying yes to the whole of me? ...Say it like you mean it. I'll believe you. I want to believe you."* |
| Aerith | *"I'd made my peace with not having a future. You took that peace and handed me wanting instead. So I have to ask: are you in the 'after' with me — all the way to whatever its end is? Because I'm done pretending I don't want one."* |
| Bellatrix | *"I have a devotion that ends worlds, baby, and it has spent so long with nowhere to land. Are you the will I burn for? Say yes and you have everything I am. ...Say no very carefully. I do not take disappointment gracefully."* |
| Revy | *"I don't do this. I welded it shut for a reason. So I'll ask once and hate every word: you actually want THIS? Me — the whole busted mess of it? ...Don't lie. I'll know, and I will never forgive it."* |
| Satsuki Kiryūin | *"I have stood above everyone my whole life because above is safe — no one above you can betray you. I am asking to stand *beside* you instead, to hand you my flank and trust you not to use it. Are you my equal in this? Or am I about to make the first foolish decision of my life?"* |
| Velvet Crowe | *"If I let you matter, I have something to lose again — and the last time I had that, the world laid it on an altar. So I need to hear it: will you be the thing I was wrong to swear I'd never have? Be certain. I do not survive being wrong about this twice."* |
| Atalanta Alter | *(no glee, for once)* *"You woke the girl I gave up to survive. If you stay, she stays — and she can be hurt again, the way I swore she never would be. So tell me true, little king: are you staying? Because if you leave after this, there's no monster left to laugh it off. Only her."* |

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
| **Quest-locked CRPG** | | |
| Tristian | +3 Loyalty | Temple income doubled; once per turn, Unrest −1 automatic (his presence stabilizes faith and hope) |
| Octavia | +2 Economy, +1 Culture | Spymaster checks gain +2; once per turn, may redirect one Economy failure into a partial success (she finds a workaround) |
| Kalikke | +2 Stability, +2 Loyalty | Elemental disturbances and magical crises: automatic advantage on first resolution check. Dual-nature means both contribute — council never unstaffed |
| Nok-Nok | +2 Loyalty, +1 Stability | Goblin Hero Effect: morale events resolve at +2; once per turn, a despair-tier event downgrades to mere setback (he refuses to let people give up) |
| Jubilost | +3 Economy | Gnome Network: trade-route events resolve at +2; one rare luxury good per turn arrives in the capital at no cost; tax events resolve as if Economy +1 |
| Ekundayo | +2 Stability, +1 Loyalty | Wilderness Watch: hex-exploration events at +2; one hostile creature/bandit incursion automatically averted per chapter (Trkaa scouts); Hunting Lodge unlocked |
| Valerie | +3 Stability | Military threat events: one free reroll on resolution per turn |
| **Cross-IP / Seekers** | | |
| Leliana | +3 Culture | Ballad Cycle effect: once per turn, one morale event downgrades severity by one tier (the kingdom remembers there is beauty here, and an old voice keeping faith with it); court never falls below Culture 1 while she plays |
| Hu Tao | +3 Loyalty | Rites of Rest: death, grief, and morale events resolve at +2; once per turn a haunting / restless-dead / mass-mourning crisis auto-downgrades one tier (she sees every soul properly onward, so none lingers to trouble the living) |
| Keqing | +3 Economy | Yuheng's Ledger: once per turn, one Economy or administrative failure becomes a partial success (she'd already drafted the fix); bureaucracy and infrastructure events resolve at +2 |
| Yor Forger | +3 Stability | Thorn in the Dark: one assassination / sabotage / internal-treachery event is automatically averted per chapter (it never reaches you); intrigue and security events resolve at +2 |
| Aerith | +2 Culture, +1 Loyalty | The Living Land: plague, famine, and blight events resolve at +2; once per turn one wounded-populace or despair event downgrades a tier (the land itself answers her hands) |
| Bellatrix | +3 Stability (through dread) | Reign of Fear: rebellion and unrest events resolve at +2 by sheer terror — BUT once per chapter her cruelty spikes a Loyalty −1 the player must manage. The leash works; it is never free |
| Revy | +2 Economy, +1 Stability | Two Hands: one bandit / mercenary / armed-threat event is crushed outright per chapter; underworld, smuggling, and black-market events resolve at +2 (she knows everyone worth knowing and where the bodies are) |
| Satsuki Kiryūin | +3 Stability | Fear Is Freedom: military-threat events resolve at +2 with one free reroll per turn; the host's discipline is absolute — BUT a Loyalty event may fire if the player rules too softly for her standards |
| Velvet Crowe | +2 Stability, +1 Loyalty | Devour the Calamity: supernatural, occult, and curse events resolve at +2; once per chapter a magical catastrophe is consumed outright (the daemon-arm eats the threat before it lands) |
| Atalanta Alter | +2 Stability, +1 Economy | The Huntress's Quarry: monster / predator / wilderness-threat events resolve at +2 and one beast-incursion is annihilated per chapter; game and pelts enrich the market — BUT any event touching a child she reacts to intensely (⛔ handle live, never fabricate a child-quest) |

**Stage 5 Passive — "The Warm Light":**
While at Stage 5, the player receives a permanent +1 morale bonus to Will saves. The DM notes this as: *She's in your head. But it's the kind of company that steadies rather than distracts.*

---

## 🌙 CAMP INTERLUDES — QUIET MOMENTS

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

## ⚖️ TWO-TIMING ESCALATION

When the player has Romance Score ≥ +1 with **two or more** companions simultaneously:

```
TIER 1 — UNDER THE SURFACE (Stage 1 with both)
  No mechanical penalty yet. Companions sense it but have not confirmed it.
  Camp Interludes for both fire normally.

TIER 2 — KNOWN (Stage 2 with one OR Stage 1+ with both)
  Both companions become aware. Save flag: love_triangle_active = TRUE.
  Each tick of Romance Score on EITHER companion now applies a parallel
  penalty:
    Romance +1 with companion A   →   companion B: Romance −1, Opinion −1
    Romance +1 with companion B   →   companion A: Romance −1, Opinion −1
  This is the "they find out by absence" rule. Off-screen knowledge
  propagates through party banter (KM_Companions_Behaviors.md handles voice).

TIER 3 — CONFRONTED (Stage 3 with one, Stage 2+ with the other)
  At the next quiet camp, the lower-Stage companion confronts the player
  ONCE. DM runs a 4–6 exchange scene. Player choices:
    [Choose them]      → Other companion drops to Stage 0, Romance Score = 0,
                          attraction flag clears. They withdraw cleanly. No
                          recovery without major arc (≥3 sessions of repair
                          + a sacrifice).
    [Choose the other] → This companion drops to Stage 0 same way. Symmetric.
    [Refuse to choose] → Both drop one Stage. love_triangle_active stays TRUE.
                          Each subsequent Romance tick now applies DOUBLE
                          parallel penalty (−2 instead of −1) to the other.
                          Persisting past Tier 3 without choosing forces
                          Tier 4.
    [Honest disclosure
     of feelings for both] → Diplomacy DC 18 (very hard). Critical Success:
                          one or both companions accept the open arrangement
                          (per their values — see Open Arrangement below).
                          Success: penalty reduced to ½ but Stages capped at 3
                          for both until resolved. Failure or worse: Tier 4
                          fires immediately with both at the same drop.

TIER 4 — RUPTURE (Stage 4+ reached with one while ≥ Stage 2 with the other)
  The non-chosen companion experiences this as betrayal regardless of
  player intent. Their Stage drops to −2 (Wounded), Opinion drops by 4,
  and they fire ONE pointed scene. After that scene:
    - If they were Type A (jealous) per StateVoice_C → they convert to
      Type C (hostile-to-rival) and lines escalate accordingly.
    - If they were Type B (protective) → they become Type A; the player
      did not deserve their watch.
    - Recovery: only via a sustained repair arc (5+ sessions, sacrifice
      required, no further Romance progression with the chosen partner
      during the arc).
```

**Off-screen detection rules:** A companion does NOT need to be present in the scene to find out. By Stage 2+ with a second companion, the party *including* the unwitting first companion has noticed (at minimum) one of:

- The second companion's behavior shift (Linzi writes about it; banter spreads it through teasing, cutting remarks, or tactical reviews).
- The player's own behavior — choices, gifts, time allocation — read against the first companion's expectations.
- The companion's own intuition, gated by their Opinion Score: at WARM (+6+) they notice within one session; at FAVORABLE (+1–5) within two; at NEUTRAL or below, never until directly told.

**The "they don't have to say it" rule:** A companion who has discovered the two-timing applies their full penalty silently. Their behavior shifts (Score-State Voice activates a tier earlier; Camp Interludes stop firing for them). The player is not informed. The save block flags `secretly_aware: true` on the companion entry. The Opinion Score and Romance penalties have already applied.

---

## 🕊️ JEALOUSY RESOLUTION PATH

A companion in active Type A (jealous), Type B-converted-to-A, or post-rupture Stage 2+ jealousy state can be brought back. This is a deliberate arc — not a single conversation.

### Stage 0 — Pre-resolution Diagnostic

Before any repair attempt, the DM checks:

```
- Is romance with the chosen partner stable (Stage 3+)? Required.
- Is the jealous companion at Romance Stage ≥ 0 (not in active Rupture)?
  Required — Rupture must be addressed via the harder repair arc first.
- Has the player attempted to address jealousy in any form previously?
  This affects the DC.
```

### Stage 1 — Open the Conversation (player-initiated)

Player uses `.address [companion]` command, OR brings it up in a Camp Interlude using a custom dialogue option. The DM runs a 6–10 exchange scene with three explicit player postures:

```
[Acknowledge]   "I noticed. I should have said something earlier."
[Apologize]     "I didn't see it clearly. I'm sorry."
[Reframe]       "You and I are not the same kind of thing as me and them.
                 Both are real."
```

Each posture rolls Diplomacy vs the companion's current Opinion-tier DC:

| Companion Opinion Tier | Diplomacy DC |
|---|---|
| Friendly (+11+)   | 14 |
| Warm (+6 to +10)  | 17 |
| Favorable (+1–5)  | 19 |
| Cool (−1 to −5)   | 22 |
| Strained (−6−)    | 25 (and only [Apologize] is available) |

**Critical Success:** Companion accepts. Type A flag cleared. Romance returns to actual current Stage (no higher). Opinion +2.
**Success:** Companion accepts conditionally — *"I will see what comes next."* Stage normalizes; jealousy lines downgrade to once per chapter instead of session. Opinion +1.
**Failure:** No change. Player may try again after one full chapter.
**Critical Failure:** Companion says something true and unkind. Opinion −1. Lock for two chapters before retry available.

### Stage 2 — Sustain (over 2–3 sessions)

After a successful conversation, the companion enters a watching period. The DM applies these passive checks each session:

- Did the player include them in a meaningful party assignment? (+1 progress)
- Did the player give them a gift, attention, or remembered detail? (+1)
- Did the player flirt with the chosen partner *in front of* them? (−2)
- Did the player two-time AGAIN with a third companion? (auto-fail; back to Tier 3 of two-timing escalation)

At 3 progress points, the resolution lands. Type A flag fully cleared. Save block: `jealousy_resolved: true, resolution_session: <N>`.

### Stage 3 — Open Arrangement (rare path, only if attempted in Tier 3)

If the player passed the DC 18 honest-disclosure check at Tier 3, both companions accept an open arrangement. Per-companion willingness:

| Companion | Open Arrangement |
|---|---|
| Linzi | Accepts — *"It complicates the chronicle. I'm taking notes."* |
| Tristian | Accepts only if blessed by faith conversation — Sarenrae teaches love is not zero-sum. |
| Octavia | Accepts — *"I've shared everything else. This is fine. Don't lie about it."* |
| Leliana | Long, level look. Then: *"Share me, if you must — I have lived enough to know a heart can hold more than one without lying about it. But hear the one condition, and hear it well: never deceive me about it. I loved a woman once who shared me out like a card in her game and smiled while she did it, and it nearly killed me. Do that, and I am gone the same hour. Walk it honestly, eyes open, every name spoken aloud — and I am yours. One of yours, and glad of it."* — She accepts. She names the one cost that is non-negotiable: honesty. |
| Hu Tao | Accepts with a grin and a joke — *"The more the merrier! I do group rates."* — but names the real condition under it: *"Just don't file me in the back drawer and forget me. I've buried enough people who waited to be remembered."* Honest and unbothered, as long as she isn't an afterthought. |
| Keqing | Accepts IF it is structured and honest: *"Fine. But it will be clearly defined, fairly scheduled, and never a thing I have to find out about secondhand. Ambiguity is just inefficiency that hurts people. Document it. I'm serious."* |
| Yor Forger | Anxiously accepts — fears that asking for exclusivity would make her lose the player entirely. *"As long as I'm... one of the people you come home to, that's — that's already more than I ever thought I'd get. I won't make it difficult."* It quietly costs her; she'd never say so. |
| Aerith | Accepts easily and generously: *"Love isn't a thing that runs out, you know. Share me if you like — there's room."* The tell is the small sadness under it: she worries she's the easy one to deprioritize, and won't ever ask not to be. |
| Bellatrix | Does NOT share the worship. *"Others may orbit you, baby. I will not be one of a *set*. And I cannot promise the others stay... intact, if they get between me and the will I kneel to."* Accept at the player's peril — see her jealousy note. |
| Revy | *"Do whatever you want, I'm not your damn wife."* — defensive, fast, the hurt leaking right through it. She'll tolerate an open arrangement out of pride and pretend it costs nothing. It costs something. Don't rub her face in it. |
| Satsuki Kiryūin | Pragmatic, unthreatened, on one condition: *"A sovereign may keep consorts; I am not so small as to be wounded by it. But understand — I am your *equal*, not one of a collection. The moment I am treated as interchangeable, I am gone. Order it correctly and there is no quarrel."* |
| Velvet Crowe | Cold acceptance, with a warning she means: *"I don't care where else you sleep. I care that you never lie to me about it — I have had enough of being managed. *(the arm stills)* And whatever else you keep — it does not get to threaten you. That part isn't open for discussion."* |
| Atalanta Alter | Treats it as a game, which is the danger: *"Share you? *(delighted)* Oh, I'll just hunt the competition for sport — keeps things lively!"* Under the glee, the abandoned child's terror of being left makes this volatile. Honest and attentive, or it goes very wrong. |

Companions who refuse exit the romance permanently with Romance Score = 0 and Opinion −1. They do NOT become hostile — they have decided.

---

## ⚔️ COMPANION RIVALRY — JEALOUSY TURNS PHYSICAL

> **DM:** When jealousy between two companions escalates to Tier 3 (Confrontation) and the player fails or refuses to intervene, the confrontation may turn physical. Run this as a **cinematic scene** — no initiative, no turn order, no per-hit dice. Use each companion's class abilities, Signature moves, and Core Value to write 3–5 dramatic beats until one cannot continue. The fight ends when one clear beat lands that the other cannot answer.

### COMPANION-VS-COMPANION ESCALATION

Separate from the player-facing jealousy ladder. Tracks the two companions' relationship with *each other*.

```
TIER 1 — COLD
  Clipped responses between the two companions. No cooperation in skill
  challenges. Pointed banter when the player isn't present. Player may
  notice or may not.

TIER 2 — FRICTION
  Open argument scene in camp or mid-travel. Player witnesses or hears
  about it. Can intervene or let it run.
  Combat effect: neither companion will use assist actions for the other.
  They will not cover each other's flank. CombatAI cooperation between
  them is suspended.

TIER 3 — CONFRONTATION (brawl eligible)
  One companion initiates directly. If player fails DC 18 Diplomacy
  intervention (or chooses not to try), the scene turns physical.
  DM runs the CINEMATIC BRAWL (see below).
  Combat effect (Tier 3+): companions may countermand each other's
  tactical calls mid-fight. DM applies this as narrated friction.

TIER 4 — ULTIMATUM OR TRUCE
  One companion forces a resolution — with the player OR between
  themselves. Mandatory scene. Player cannot defer.
  Rare: at Tier 4 in a critical moment, the injured companion may
  hesitate to save the other. DM rolls secretly (DC 12 flat; failure
  = one round of inaction).
```

### CINEMATIC BRAWL

**Player intervention window:** Once, after Beat 3 (before the final beat). Diplomacy DC 18. Success halts both at Shaken. Failure: scene finishes without interruption.

**Outcome by matchup:**

| Matchup type | Loser result | Winner result |
|---|---|---|
| Close match (similar class tier) | Hurt (1 chapter out) | Shaken (2 scenes) |
| Clear mismatch | Seriously Injured (2 chapters) | Shaken or unscathed |
| Extreme mismatch | Auto — Seriously Injured, no roll | Unscathed |

**Tone rule:** These companions live and fight together. The brawl should feel like something that cannot be taken back. Not cartoonish. Not lethal. Ugly. Real. The player watching knows it is their fault.

**Mutual respect clause:** Some close-match pairings end with both companions' Opinion of *each other* rising +1 (they tested each other and found something worth respecting). DM judges per personality.

### INJURY STATES

| State | Duration | Effects |
|---|---|---|
| **Shaken** | 2 scenes | In party; −2 to all checks; no romance interactions |
| **Hurt** | 1 chapter | Out of active party; camp dialogue only; no combat |
| **Seriously Injured** | 2 chapters | Bedridden; one check-in scene per chapter only |
| **Grave** | Until healed | Requires divine-tier healer active + 500 gp OR story item |

**Kingdom cost:** Any advisor role held by an injured companion is unstaffed. Relevant stat −1 per turn out.

**Recovery acceleration:**

| Method | Effect |
|---|---|
| Dedicated healer in active party | Halves duration (round up) |
| Player uses healing item directly on them | −1 chapter |
| Player spends 1 Hero Point | Skip to Shaken immediately |
| Alchemist crafts tincture (Alchemy DC 16) | −1 chapter |

### CHECK-IN SCENE (during recovery)

Player may visit the injured companion once per chapter. 3–4 beat scene. Tone set by who initiated the fight and whether the player took sides.

| Player behavior | Mechanical result |
|---|---|
| Visited every chapter + brought something relevant | Opinion +1; romance resumes at full Stage on return |
| Visited inconsistently | No change; romance resumes |
| Never visited | Opinion −2, Romance −1 on return |
| Accelerated recovery actively | Opinion +2; unique flavor line unlocked |
| Took the rival's side | Scene is short and careful. Relationship Paused until `.mend` |

### AFTER RECOVERY

A brief scene fires when the injured companion returns to active status. Player gets one exchange before normal party life resumes.

The rival companion's Tier resets to 2 (Friction) after a brawl resolves via injury — they have established a hierarchy. May escalate again if the underlying cause (the player's choices) is not addressed.

---

## 🌡️ PASSIVE JEALOUSY HEAT

> **DM:** This system fires without the player two-timing. Companions who are attraction-flagged (OR Romance ≥ Stage 1) track a hidden heat meter when rival companions make moves on the player — gifts, flirting, Camp Interludes, dates. The player is the passive object. No choice has been made. The jealousy builds between rivals, not between rival and player. Never announce the heat level. Apply behavioral signals silently.

**Heat meter:** 0–10 per jealous-companion/rival pair. Tracked in save block under `passive_jealousy{}`. Player never sees the number.

### HEAT GENERATION (per session, cumulative)

| Event | Heat |
|---|---|
| Rival gives player a meaningful gift | +1 |
| Rival flirts with player in a group scene | +1 |
| Rival has a private Camp Interlude with player | +1 |
| Player reciprocates the rival's flirting | +2 |
| Rival's attraction behavior becomes visible to the party | +1 |
| Player selects rival for a date | +2 |
| Rival's Romance Score advances a Stage | +2 |
| Player publicly compliments the rival in front of others | +1 |

### HEAT BLEED (per session)

| Event | Heat |
|---|---|
| Player gives the jealous companion direct attention | −1 |
| Player selects jealous companion for a mission over the rival | −1 |
| Player does not reciprocate the rival's advance | −1 |
| Player has Camp Interlude with the jealous companion | −2 |

### BEHAVIORAL SIGNALS BY THRESHOLD

DM applies all of these silently. No announcement.

| Heat | What the jealous companion does |
|---|---|
| 0–3 | Nothing visible. Still. Watching. |
| 4–5 | Type A ambient lines begin — one per session. Brief. Deniable. |
| 6–7 | Pointed comments about the rival that are not quite comments about the rival. The rival notices. |
| 8–9 | Inserts themselves — volunteers for everything the rival volunteers for, positions near the player in camp. Tension is palpable to anyone paying attention. |
| 10 | **BOILING POINT** — confrontation scene fires. |

### PERSONALITY MODIFIERS

| Companion | Modifier | Boils at | Reason |
|---|---|---|---|
| Linzi | 0 | 10 | Heat is normal but telegraphed — she writes about it first; DM can signal through journal narration before behavior shifts |
| Leliana | 0 | 10 | Does not compete — she finds it beneath them both; heat surfaces as the *withdrawal of the dawn hour* — she banks her warmth down to something formal and courteous and stops letting the player near the private ritual. A quiet, deliberate stepping-back, not coldness; harder to address than anger would be |

### THE BOILING POINT SCENE

The jealous companion confronts the **rival companion** directly — not the player. Player is present. 3–4 beat scene. Then one of four outcomes:

**Player choices during the scene:**

| Choice | Effect |
|---|---|
| **Step in** (Diplomacy DC 16) | Stops at words. Heat for both resets to 5. Companion rivalry Tier 1 established. |
| **Stay out** | Scene runs to its conclusion. Companion rivalry Tier 1 established. Heat resets to 5. |
| **Side with the jealous companion** | Rival Opinion −2. Jealous companion heat drops to 0 — but they are now aware the player intervened on their behalf. They did not ask for this. It complicates things. |
| **Side with the rival** | Jealous companion heat resets to 3 but Opinion −2 toward player. They noticed who the player protected. |

**Heat never resets to 0 after a confrontation.** The feeling does not disappear — it settles at a lower level. The rival pair enters the companion rivalry system at Tier 1 regardless of how the scene ends.

If the boiling point scene turns physical, the player's intervention DC rises to 18 (Athletics or Diplomacy) and the cinematic brawl rules apply.

---

## 📅 DATE SYSTEM

**Command:** `.date [companion] [activity]`

**Requirements (all must be met):**
- Companion at Romance Stage 4 or higher
- Only 1 date per chapter (tracked via `dates_this_chapter`)
- Kingdom Unrest ≤ 3
- Companion in active party, not injured

**Available activities:** SPAR · HUNT · STARGAZE · STUDY · TAVERN · WANDER · HIKE · FISH · COOK · PATROL

### OUTCOME DETERMINATION

| Activity preference | Outcome |
|---|---|
| **PREFERRED** | **Great** (automatic) |
| **TOLERATED** | Roll d20 + Diplomacy vs DC 14. Success = Great. Fail = Good. |
| **REFUSED** | **Awkward** (automatic — no roll saves it) |

### OUTCOME EFFECTS

| Outcome | Romance Score | Jealousy Heat |
|---|---|---|
| **Great** | +1 to date companion | +2 to ALL other attraction-flagged companions |
| **Good** | no change | +1 to ALL attraction-flagged companions |
| **Awkward** | no change | −1 to date companion (embarrassed; withdraws) |

**Awkward follow-up:** Date companion absent from the next optional ambient scene. Voice lines do not fire; they are not part of camp background. Combat and plot-essential presence unaffected. Flag `date_awkward: true` on companion entry; clears after one ambient scene.

### PER-COMPANION ACTIVITY TABLE

| Companion | PREFERRED | TOLERATED | REFUSED |
|---|---|---|---|
| **Linzi** | TAVERN · WANDER · STARGAZE · COOK | STUDY · FISH · HIKE · PATROL | SPAR · HUNT |
| **Leliana** | WANDER · STARGAZE · STUDY · COOK | TAVERN · HIKE · FISH · PATROL | SPAR · HUNT |

### NARRATION GUIDANCE

**Great:** 4–6 beats. A shared moment only possible in this activity. The companion shows something not visible any other way. End on something the player will remember — unexplained.

**Good:** 2–3 beats. Comfortable. Not quite magic. Something was left on the table — not from failure, just the nature of tolerated things. End with warmth but no revelation.

**Awkward:** 2 beats. Something went wrong in the first beat — the companion was out of their element, or the activity surfaced a vulnerability. Second beat is the mutual realization. End without resolution.

---

## 🥊 FIGHT SYSTEM (PLAYER-COMPANION CONFRONTATION)

**Triggers:**
- Companion's active agenda item ignored **3 times** — fight fires at the next scene start. `agenda_ignored_count` resets after the fight.
- `.fight [name]` — player initiates voluntarily (Stage 1+ required).

**Commands:** `.fight [name]` | `.mend [name]`

### THE FIGHT SCENE

4–6 exchanges. Companion states the grievance without ambiguity.
Player presents **one posture**:

| Posture | What the player does |
|---|---|
| **Apologize** | Acknowledges the companion's grievance as valid |
| **Defend** | Argues their reasoning without conceding |
| **Counter** | Raises a specific grievance of their own |
| **Walk Away** | Ends without resolution (no roll required) |

**Roll Diplomacy for Apologize / Defend / Counter.**
Counter is unavailable at Favorable or lower Opinion.
Walk Away requires no roll; auto-sets Paused severe.

**DC by companion Opinion:**

| Opinion tier | DC |
|---|---|
| Friendly (+11+) | 14 |
| Warm (+6–10) | 16 |
| Favorable (+1–5) | 18 |
| Cool or lower | 20 — Apologize only |

**Paused duration by posture and outcome:**

| Posture | Success | Failure |
|---|---|---|
| Apologize | Mild (1 chapter) | Moderate (2 chapters) |
| Defend | Moderate (2 chapters) | Severe (3 chapters) |
| Counter | Moderate; CS adds Opinion +1 | Severe + Opinion −1 |
| Walk Away | Severe (3 chapters) | — |

### RELATIONSHIP PAUSED STATE

While Paused, the companion:
- **Does not:** accept romance gestures, flirt actions, Camp Interludes, dates, or staged signals. Passive jealousy heat does not generate.
- **Still:** fights in combat per CombatAI, voices plot-required lines, attends story scenes, runs their agenda.
- **Voice:** Type C lines only (cold, professional). Warm ambient absent.
- **Opinion:** no positive accumulation; negative events still apply.

Save flags: `fight_paused: true` | `paused_chapters_remaining: N`
Decrement 1 per chapter advance; clears automatically at 0.

### `.mend [name]` — REPAIR

Cannot use the same chapter the fight fired.
Roll Diplomacy. DC = 14 + 2 per chapter elapsed since fight (cap 22).

| Outcome | Effect |
|---|---|
| Critical Success | Paused ends. Romance returns at Stage −1 from where it was. Opinion +1. |
| Success | `paused_chapters_remaining` −1. Retry next chapter. |
| Failure | No change. Retry after 1 chapter. |
| Critical Failure | `paused_chapters_remaining` +1. Opinion −1. |

**Grand Gesture:** Declare before rolling. Costs 500 gp item OR 1 Hero Point OR a named narrative concession. Effect: DC −4. One use per arc. Save flag: `grand_gesture_available: false` after use.

### PER-COMPANION FIGHT NOTES

| Companion | Most likely trigger | Fight style |
|---|---|---|
| **Linzi** | Player acted dishonorably in a chronicled scene | Goes quiet. Stops writing. That's the tell. |
| **Leliana** | Player used power carelessly against someone who couldn't answer back, or dismissed the ballad-cycle's worth | She does not raise her voice. The parables stop; she goes spare and courteous, and the dawn hour closes to you. The fight fires when you finally ask why she has gone formal. |

---

## 📊 MAINTENANCE TAX

**3 or more active Stage 1+ romances:** −1 Opinion per chapter advance applied to ALL active romances automatically.

- "Active" = Stage 1+, not Paused, not Faded.
- Applied at chapter advance before other bonuses or penalties.
- Flat rate: 4 active = −1 to all four (not −2).
- Check count at chapter advance. No retroactive adjustment if count drops below 3 mid-chapter.

---

## 🌅 GRACEFUL FADE

**Command:** `.fade [name]`

Voluntary wind-down. No rupture. No roll. No confrontation.
Requirements: Stage 1+. Available even during a Paused state.

### EFFECT ON USE

  Stage drops 1 immediately.
  Next 2 chapters: Stage moves −1/chapter toward Neutral (0).
  Romance heat decays to 0.
  Companion does not initiate romantic gestures, Camp Interludes,
  or flag romantic dialogue during the fade window.
  `date_awkward` flag applies for the full fade duration.

**Stage floor:** Cannot go below 0 (Neutral). Fade completes there. Companion does not become hostile or lose Opinion.

**Re-ignition:** Once Stage reaches 0 and fade is complete, player may pursue normally from Stage 0 via standard Stage progression. No shortcut. No penalty beyond the Stage loss.

**Acknowledgment scene:** If Stage was 3+ when `.fade` was issued, a brief non-confrontational acknowledgment fires at completion (2 chapters later). Narrative only — 2–3 beats, no player choice. The companion names what happened without accusation.

**Fade is not Paused.** No `.mend` needed. Fight system does not fire. Companion remains active in combat, plot, and agenda — fully present, only the romantic current withdraws.

### PER-COMPANION FADE BEHAVIOR

*Linzi:* The notes get shorter. She doesn't ask about it. The book stays closed when you're near.

*Leliana:* She plays less, not more — and never at the dawn hour where you might hear. The verses she writes in those days she does not add to the cycle. She does not name them.

---

## 💔 CAUGHT CHEATING

Fires when a companion detects the player holds concurrent Stage 1+ romances. Passive — the companion figures it out; no player action triggers it.

### DETECTION

Detection roll fires each chapter advance when 2+ Stage 1+ romances are active. DM rolls d20 (no modifier) per at-risk companion.

| Opinion tier | Detection DC |
|---|---|
| Friendly (+11+) | 8 |
| Warm (+6–10) | 12 |
| Favorable (+1–5) | 16 |
| Cool or lower | 20 |

Roll ≥ DC → companion confronts player that chapter.
Companions in Paused state do not roll detection.
Companions whose fade is active do not roll detection.

### THE CONFRONTATION SCENE

3–4 beats. Companion states what they know or suspect.
Player presents one option:

| Option | Skill | DC |
|---|---|---|
| **Come Clean** | — | automatic |
| **Deny** | Deception | 16 + (2 × Romance Stage) |
| **Reframe** | Diplomacy | 14 + (2 × Romance Stage) |

Stage = romance stage with the confronting companion.

**Come Clean (automatic):**
  Paused: Moderate (2 chapters). Opinion −2. Stage −1.
  `.address` (Open Arrangement) available after Paused ends — DC +2 above standard. No penalty for honesty beyond the Pause itself.

**Deny — Success:**
  Companion accepts it. Opinion −1. No Pause. Heat cools 1.
  `deny_used_this_arc: true`. If detected again same arc: Deny auto-fails, add 1 severity tier to resulting Pause duration.

**Deny — Failure:**
  Companion knows you lied. Paused: Severe (3 chapters). Opinion −3. Stage −2. `.mend` DC +4 above standard formula.

**Reframe — Success:**
  "I wasn't sure what we were." Companion accepts the framing. Opinion −1. No Pause. Heat resets to 0. Stage unchanged.

**Reframe — Failure:**
  Companion doesn't accept it. Paused: Moderate (2 chapters). Opinion −2. Stage unchanged.

### PER-COMPANION CONFRONTATION STYLE

| Companion | Discovery and approach |
|---|---|
| **Linzi** | Stops writing mid-sentence. Sets the journal down. Asks quietly — one question. |
| **Leliana** | Sets the lute down first, then asks plainly, looking right at you. She has never needed misdirection to ask a hard thing. The question is quiet and entirely direct. |

---

## 🎭 THE JUGGLER'S EDGE — MULTI-ROMANCE BONUS & THE CASUAL CATCH

Holding several romances at once is a **HIGH-RISK / HIGH-REWARD** playstyle. The more hearts you hold, the more you GAIN — and the more catastrophic a single bad catch becomes. The player opts in just by pursuing more than one; nothing forces monogamy, and nothing protects the juggler.

**`concurrent_romances`** = count of companions at Romance Stage ≥ 2 (Smitten+), not ruptured/faded/zeroed.

### THE BONUS — STAGED (climbs as you maintain more)

| Tier | Concurrent (Stage 2+) | Reward (cumulative) |
|---|---|---|
| **I — Magnetic** | 2 | **+1 morale** (circumstance, Will-flavored) while all are held — a charisma in the air; companions and NPCs feel it. (Does not double-stack with the Stage-5 "Warm Light" on the same save.) |
| **II — Sought-After** | 3 | Tier I **+ a Hero Point** at each new love scene / romance milestone **+ social XP** |
| **III — The Sovereign's Court** | 4+ (or ≥2 Stage-5 consorts) | Tiers I+II **+ a kingdom / consort-influence bonus** (Consort Council expansion · Unrest −1 · a leadership edge — ties to the Stage-5 Consort Role) |

`juggler_tier` 0–3 tracked in save. Tiers are **LOST as romances drop below Stage 2** — a catch that zeroes/halves a partner can knock the player down a tier. That is the gamble: the bigger the court, the more a single collapse costs.

### THE CASUAL CATCH — ROLLED, THEN THE CHOICE (kiss / date / open flirtation)

Distinct from the love-scene catch (which **zeroes** the loser). When the player romances ONE partner in a way another concurrent partner could witness — a kiss, a date, a public flirtation — **roll to be caught:**
- DM rolls d20 vs CATCH DC. Base **DC 12**, **−2 per concurrent romance beyond the second**, **−2** if indiscreet (same room/camp/party banter), further lowered by the witness's `passive_jealousy heat`.
- **Roll ≥ DC:** not caught. The moment passes; the juggle holds.
- **Roll < DC:** **CAUGHT** — the highest-heat rival sees. **THE CHOICE (binary):** stay with the one you're with, or go to the one who caught you.
  - **CHOSEN one: NO change** — reassured by being chosen; relationship intact.
  - **NOT-CHOSEN (devastated) one: Romance approval HALVED** — Romance Score → ⌊score ⁄ 2⌋, Opinion takes a proportional hit, plus their voice/disposition shift.

⛔ **Casual catch = HALF; love-scene catch = ZERO.** The deeper the moment you're caught in, the worse the betrayal lands. Either way the CHOSEN partner is untouched and the player MUST pick — once caught, there is no keeping both whole.

⛔ This is the **ACUTE, in-the-act catch** (rolled when the player romances in proximity). The slower **§ CAUGHT CHEATING** (a companion working it out off-screen over a chapter → confrontation) still runs in parallel for romances discovered indirectly.

---

## 💕 LOVE SCENE SYSTEM

**Command:** `.loveScene [companion]`

Milestone intimacy scene. Not a simple beat — a scene with weight and consequence. Completion satisfies the marriage prerequisite (`love_scene_occurred: true`) required alongside Stage 5 before `.propose` unlocks.

### TRIGGER CONDITIONS

Both must be true:
- Companion at their **PER-COMPANION LOVE-SCENE GATE** (default Stage 4; some lower, one higher — table below)
- `gesture_returned ≥ 3` this arc (tracked in romance state)

**⛔ PER-COMPANION LOVE-SCENE GATE — the stage at which a love scene CAN fire (character-true, not uniform):**

| Gate | Companions | Why |
|---|---|---|
| **Smitten (Stage 2)** | Revy, Bellatrix | Revy treats it as no big deal ("don't make it weird"); Bellatrix is obsessive/impulsive, all-or-nothing |
| **Admitted (Stage 3)** | Hu Tao, Atalanta Alter, Leliana | Hu Tao tumbles fast; Atalanta intense/feral; Leliana knows what she wants but guards her heart |
| **Confessed (Stage 4 — DEFAULT)** | Aerith, Yor Forger, Keqing, Satsuki, Valerie, Linzi, + any companion not listed | Need the declaration / emotional safety first |
| **Devoted (Stage 5)** | Velvet Crowe | Highest wall of any companion — earns the hardest gate |

Any companion not listed defaults to **Stage 4**. This gate replaces the old uniform "Stage 4+"; `gesture_returned ≥ 3` still applies at every gate. The gate is the FLOOR — the player may always wait longer, but cannot trigger a love scene below the companion's gate.

OR: `.loveScene [companion]` forces the scene check. DM validates conditions first — if not met, scene does not fire.

### ⛔ CAUGHT MID-SCENE — ROLLED, THEN A FORCED CHOICE (the love-scene catch)

Fires when 2+ companions are at Romance Score ≥ 2 (the player is juggling). **Being caught is ROLLED — a chance, not a certainty.** No check if the player holds only one active romance.

**THE ROLL (do you get caught?):** DM rolls d20 vs the CATCH DC. Base **DC 14**, **−2 per concurrent romance beyond the second** (more partners = more eyes), **−2** if the scene is indiscreet (shared camp, thin walls, a partner nearby). Higher `passive_jealousy heat` on a rival lowers the DC further (they're already watching).
- **Roll ≥ DC:** no catch. Scene proceeds, `love_scene_occurred: true`. The juggle held — the Juggler's Edge bonus accrues.
- **Roll < DC:** **CAUGHT.** The companion with the highest `passive_jealousy heat` walks in. → THE CHOICE.

**THE CHOICE (binary — someone gets devastated, no splitting the difference):** the player decides in the moment — **stay with the partner you're with, or go to the one who just walked in.**
- **The CHOSEN one: NO change.** Being chosen *here* reassures them — the relationship is fully intact. If they were the current partner, the love scene still completes (`love_scene_occurred: true`).
- **The NOT-CHOSEN (devastated) one: Romance approval → ZERO.** Their Romance Score is wiped to **0 (NEUTRAL — the romance is gone)**, Opinion takes a matching hard hit, and they enter the rupture/abandonment voice (tables below). Caught in *that* moment, the betrayal is total — this is the love-scene stakes (the casual catch is gentler: half, not zero — § THE JUGGLER'S EDGE).

⛔ This **supersedes** the old Stage−2 / Opinion−4 / Paused / Diplomacy-call-out split — the model is now simply **chosen = untouched, not-chosen = zeroed.** No skill check saves both; once caught, the player picks who to keep and who to wound.

### PER-COMPANION WALK-IN REACTION (rival entering)

| Companion | Walk-in line |
|---|---|
| **Linzi** | Drops whatever she was holding. One short syllable. Then nothing. |
| **Leliana** | Goes very still — the warm kind of still turning into the other kind. She inclines her head, says something gracious and meaningless, and is gone before the silence can be named. The door she closes behind her is not slammed. That is worse. |

### PER-COMPANION ABANDONMENT REACTION (Partner A — player chased rival)

| Companion | Abandonment reaction |
|---|---|
| **Linzi** | Doesn't call after you. When you return, the room is empty. The journal is on the table, closed. |
| **Leliana** | Is at the dawn hour when you return, though it is not dawn — lute in her lap, working down the list of the dead. She does not look up. She plays a name you don't know, then another. The one ritual she let you near, taken back. She gives you no verse tonight — only the closed door of her oldest grief, and she keeps faith with it instead of you. |

---

## 🤝 COMPANION-INITIATED CONTACT

> **DM:** Romance.md states "Companions never initiate first." This section creates a narrow exception. At Stage 1 and above, companions may initiate small physical contact — not declarations, not kissing, not words of affection. **Contact only. Wordless. Deniable.**
>
> These are not moves. They are moments where something felt becomes something expressed — ambiguously, carefully, in ways the companion can retreat from if the player pulls back.
>
> The player's response determines whether the gesture becomes a romantic signal.

### Trigger Conditions

A companion may initiate contact when ALL of the following are true:

- Companion is at **Stage 1 or higher**
- Moment is **quiet** — camp, travel, a pause after combat, a late watch
- **No active combat**, no urgent decision pending
- Companion had **meaningful interaction this session** (dialogue, a choice that affected them, combat side by side)
- **Once per session per companion** — do not stack gestures

**Do not force these moments.** Let them arise from the scene. If the setting is right, the companion acts. If not, nothing happens and that absence is fine.

### Response Options

When a companion initiates contact, present these options:

```
[Allow — say nothing]
[Allow — acknowledge it]
[Pull back gently]
[Return the gesture]
[Custom]
```

| Response | Tone | Romance Effect |
|---|---|---|
| **Allow — say nothing** | Silence as acceptance. You didn't move. | +1 Romance |
| **Allow — acknowledge it** | A word, a look. Soft but present. | +1 Romance |
| **Pull back gently** | Not rejection — just not yet. | No change |
| **Return the gesture** | Active affection returned. The companion notices. | +1 Romance + `gesture_returned` flag |
| **Custom** | DM judges: allowing = +1; withdrawing = no change | Varies |

**`gesture_returned` flag:** Set per-companion. Companion becomes slightly more open next quiet scene. They do not escalate automatically — the DM uses discretion on when the next gesture occurs.

### The Silence Rule

> Allowing without comment is the most intimate response. Words can be deflection. Staying still, while saying nothing, is presence. Companions read this correctly. If the player did not pull back, they chose to stay.

### Post-Gesture Behavior

After any initiation — regardless of player response:

- Companion does **not** follow up immediately. No *"did that mean something?"*
- **If allowed:** companion is marginally warmer in the next scene — not dramatically; present is the right word
- **If gesture returned:** `gesture_returned` flag set; DM may allow a slightly longer gesture at the next appropriate quiet moment — not automatic
- **If pulled back:** companion does not retreat emotionally. They don't reference it. Life continues.

> **There is no awkward morning-after scene.** The gesture happened or it didn't. Its weight lives in what is unsaid afterward.

---

## 👤 COMPANION GESTURE PROFILES

### Stage 1 Gestures — Tentative. Deniable. Fits their personality.

#### VALERIE — *She finds a reason.*

Hand on forearm while making a point — contact while her attention is nominally on whatever she's gesturing toward. The hand stays a beat too long. Then she removes it and continues as if nothing happened.

> *"The left flank was open here —"* She touches his forearm, points at the ground where the enemy came through. Her hand stays. She doesn't look at it.

**Stage 2 upgrade:** Same gesture. Except she glances at her hand on his arm, then at him, then back to the subject. She doesn't explain the glance.

#### LINZI — *She holds on.*

Takes his arm while walking — the way a small person does in a crowd, practical — and doesn't release once the crowd is gone. She keeps walking. She keeps talking. Her grip is light. She is completely aware of it.

> She takes his arm through the gate. On the other side she doesn't let go. She is mid-story about something that happened this morning. She does not stop the story.

**Stage 2 upgrade:** Sitting side by side, she puts her head against his arm. Still talking. Just leaning there, like it's comfortable, like she's been meaning to do this for a while.

#### JAETHAL — *She makes it about something else.*

Takes his wrist — not his hand — to examine a wound or check something. Her grip is firm. Clinical. She does what she said she was doing. She does not release when she's done.

> *"You took a hit there."* She takes his wrist, turns it, examines the cut. Cleans it with efficient precision. When she finishes, her hand stays on his wrist. She looks up at him. *"It will close."* She has not let go.

**Stage 2 upgrade:** She takes his wrist and fabricates no reason. She just holds it. Looks at him. The silence extends past the point it could be accidental.

#### AMIRI — *She doesn't do subtle.*

Arm around his shoulders, hauls him in — once, hard, brief, like she's celebrating — then releases and goes back to what she was doing. It was companionable. It was also not entirely companionable.

> *"Ha!"* She throws her arm around him, one hard squeeze. *"That's what I'm talking about."* Already releasing, already moving. She does not look back.

**Stage 2 upgrade:** She doesn't release immediately. Her arm stays around his shoulders. She is looking at something else. Her arm stays.

#### HARRIM — *He doesn't do this. If he does, something has changed.*

Hand on the player's shoulder — once, briefly, the way someone does when they want to say something and can't find the words. He says nothing. He removes his hand and walks away.

> He stops beside him. His hand settles on his shoulder — heavy, present. He says nothing. After a moment he removes it and continues walking.

**If the player allows:** Harrim doesn't reference it later. But he is less likely to speak of death and ruin that session.

### Quest-locked CRPG Gesture Profiles

#### TRISTIAN — *He stops beside you.*

He finds you sitting and does not move on. He is close — closer than he needs to be to say something pastoral. His hand comes to rest on the log beside yours: not touching, adjacent. He bows his head as if in prayer. The prayer might be for you.

> The fire is low. He has been making the rounds and he stops here — beside you — and does not continue. His hand settles on the log. An inch from yours. His head bows. His lips move once. Then stillness. He does not explain.

**Stage 2 upgrade:** His hand finds yours. He doesn't squeeze — he holds. When he finally speaks: *"Sarenrae brought me to this place. I used to be angry at that. I am — not anymore."* He does not look up. His hand stays.

#### OCTAVIA — *She lifts your hand like evidence.*

Takes it with two fingers, turns it palm-up, studies it. *"Calluses here, here, here — interesting."* She is not reading your palm. She does not let go.

> *"Give me your hand."* She says it the way she says most things — ahead of asking permission. Takes it. Turns it. Studies the lines with professional attention. *"You've been doing something with your left for about six years."* She does not return it.

**Stage 2 upgrade:** She traces the longest line across your palm with one finger. Closes your hand. Gives it back. *"Some say that one is luck."* A beat. *"I don't believe in fortune-tellers."* A longer beat. *"Yet."*

#### KALIKKE — *She makes room.*

Stands closer than she needs to — shoulder against yours, attention elsewhere. One of them went quiet. The quiet itself is the gesture: Kanerah held still and let this happen.

> She's beside you at the fire. Her shoulder against yours. She has not spoken in a few minutes — which is unusual. Neither has the other voice. The silence from that direction is deliberate. She's watching the coals.

**Stage 2 upgrade:** She takes your hand. Both of them feel it — you can tell by the half-second pause. Then, Kalikke: *"She wanted to do this."* A pause. Kanerah, dry: *"So did I."*

#### NOK-NOK — *He grabs your hand in both of his.*

Tiny. Vigorous. Does not release. His whole face is involved. *"Good-fight-friend! Very good today! Nok-Nok was watching!"* He is still holding.

> He appeared at your knee from nowhere. Both his hands are around yours, pumping once. He does not let go. He is delivering a full debrief on your combat performance from twelve minutes ago. He has opinions. Still holding.

**Stage 2 upgrade:** He finds a rock, a fence post, or just leaps, to put himself at face-level with you. Grabs your shoulders. Looks directly at you. *"You are sad. Nok-Nok has noticed for three days. Nok-Nok will stay now."* He sits down beside you. He means it.

#### JUBILOST — *He does not withdraw his hand.*

Reviewing a map together, he points at something and his hand brushes yours. He moves his finger exactly one centimeter — to the error, professionally — and leaves his hand where it is.

> *"The error is here."* His finger lands beside yours on the parchment. He corrects the detail. His hand does not move. He is now explaining why the survey team was wrong. His hand is still there. He has not acknowledged it.

**Stage 2 upgrade:** He places the map on your knee to review it. There was a perfectly serviceable table. He chose your knee. He is being very thorough. The thoroughness is taking considerably longer than the map requires.

#### EKUNDAYO — *He sits the same direction.*

Watch is his native language. He joins you and faces exactly what you face. His arm settles against yours. Trkaa settles between your feet. Neither of them explains. The explanation isn't the point.

> He sits. Not across — beside. His arm finds yours in the dark, settles there. Trkaa circles once and puts her head on your knee. He watches the tree line. He will watch it all night. He has not moved his arm.

**Stage 2 upgrade:** His hand finds yours without looking for it. Trkaa shifts closer. He says one word: *"Good."* He does not specify what he means. The hand stays.

#### LELIANA — *She goes still.*

She is playing something low under the talk — an old air, half a parable trailing off. She goes still. Not because anything is wrong. The hand on the strings just... stops. She looks at you, and for a moment all the easy warmth concentrates into something very direct and unguarded. Then the air picks up again, exactly where it left, as though the silence was a rest written into the bar.

> *She was playing something low beneath the conversation when you passed. The hand on the strings goes still. She looks at you — really looks, the way someone who has buried people looks at someone still here and breathing. Then the figure resumes, exactly where it left, as though the silence belonged in the music all along.*

**Stage 2 upgrade:** Same stillness. Except she sets the lute aside deliberately this time — puts it down, not just rests her hand — and gives you the full, undivided weight of a spy's trained attention turned, for once, entirely on someone she is not assessing. After a moment: *"Go on. I was listening. I am still listening. I only wanted to look at you while you said it."* She does not pick the lute back up for a while.

#### HU TAO — *She names you.*

Mid-conversation she hands you a ridiculous nickname and watches your face to see how it lands. It sticks. Some days later you realize it's the only name she uses for you now — and that she chose it carefully, the way she chooses everything under the jokes.

**Stage 2 upgrade:** She "reads your fortune" — grabs your hand, predicts your death in elaborate, cheerful, specific detail: decades hence, old, warm, surrounded by people who love you. It is the single kindest thing she knows how to say, and she says it holding your hand and not letting go.

#### KEQING — *She fixes something of yours.*

Your strap was fraying. It isn't now. She doesn't mention it; you only notice because the repair is cleaner than the original. There is no note, no comment — just your gear, quietly made better by someone who refuses to call it affection.

**Stage 2 upgrade:** She brings you tea you didn't ask for, sets it down in the middle of her own work, says *"you skipped a meal — this isn't sentiment, it's maintenance,"* and then stays exactly one minute longer than maintenance requires. She knows you noticed the minute. She leaves anyway.

#### YOR FORGER — *She puts herself between you and the door.*

Every time, without thinking, she takes the seat with the exit-sightline and leaves you the safe side of it. She doesn't know she does it. You have, somewhere along the way, become the thing she is quietly guarding, and her body decided before she did.

**Stage 2 upgrade:** She attempts small talk — fumbles it, apologizes for fumbling it — and then simply sits with you in the silence instead, hands folded, present. For Yor, who fills every social gap with nervous apology, choosing to just *be* there wordlessly is the most honest thing she has to give.

#### AERITH — *She gives you a flower mid-sentence.*

It's in your hand before you notice, and she never breaks off what she's saying. After a while you realize there is always, now, a flower somewhere on you that you didn't put there — small, deliberate, unremarked. That's the whole message, and she'll never explain it.

**Stage 2 upgrade:** She talks to a plant near you, low and fond and exasperated — and you slowly understand she's telling it about *you*, pretending to confide in the flower while knowing perfectly well you can hear every word. When you catch her, she just smiles and keeps going.

#### BELLATRIX — *She drifts too close, and stays.*

She is suddenly there, at your shoulder, nearer than anyone else dares, smiling at the side of your face, breathing your air. She gives no reason. The reason is that she has decided you are interesting, and proximity is how she marks a thing as hers to study.

**Stage 2 upgrade:** She presses your hand to the burned brand at her wrist — the thing she lets no healer near — and watches, fervent and almost reverent, to see if you pull away. *"You didn't flinch. *(soft, delighted)* Ooh. Most of them flinch, baby. You might be worth the *word*."*

#### REVY — *She saves you the good seat.*

Wordlessly, scowling, she's already shifted her stuff off the chair with the wall behind it — the safe one, the gunfighter's seat — and left it for you. There's a drink poured you didn't ask for. Mention any of it and she denies everything, aggressively.

**Stage 2 upgrade:** She falls asleep against your shoulder after a bad night, and wakes up *furious* about it — and the fury is the whole tell. She let her guard all the way down, next to you, while armed strangers could've walked in, and the fact that she felt safe enough to do it terrifies her more than any fight.

#### SATSUKI KIRYŪIN — *She gives you her honest assessment.*

She tells you one true thing about yourself that no one else would dare say — a real weakness, or a real strength you'd discounted — plainly, as a gift, because she has decided you are worth the cost of her honesty. From Satsuki, accurate attention IS courtship.

**Stage 2 upgrade:** For one sentence she drops the imperious cadence entirely and simply *talks* to you — peer to peer, no verdict, no height — then catches herself and reverts to the sovereign. But the sentence happened, and she let it happen where you could see, and she does not take it back.

#### VELVET CROWE — *She does the protective thing, then denies it.*

She steps between you and a threat without thinking — and then snaps that it was tactical, that she doesn't care, that you should stop reading into it. The denial is always louder than the act, and the act is always real. The louder she insists it meant nothing, the more it did.

**Stage 2 upgrade:** She lets you sit near her at the fire without driving you off with contempt. That's it. That's the whole gesture — and for Velvet, who keeps every living thing at arm's length so it can't be taken from her, simply *permitting your presence* in the quiet is enormous, and she would rather be devoured than admit it.

#### ATALANTA ALTER — *She brings you a trophy.*

From a hunt she drops something at your feet — a pelt, a fang, a thing she's proud of — like a cat presenting a kill, delighted, watching your face to see if you're pleased. Being pleased is the correct answer. It is also, from her, a courtship she'd never name as one.

**Stage 2 upgrade:** Mid-laugh she goes abruptly still and looks at you a beat too long, the glee thinning into something startled and almost frightened — then she covers it with a bright *"keep up, sweetness!"* and bolts. But the still beat happened. She knows you saw it. And she didn't quite manage to make it a joke in time.

---

## 💬 COMPANION FLIRT ACTIONS

> **DM:** These are the specific behaviors that constitute "flirting" for each active companion. Use when narrating scenes where a companion is attraction-flagged. They generate passive jealousy heat in observing companions. Never announce them as flirting — narrate the action and let the player read it.

### Staged Behavioral Flirts

Three stages per companion. S1 = deniable. S2 = others notice. S3 = unmistakable. Heat generated: S1 +1 | S2 +1 | S3 +2.

**LINZI**
- S1: Reads a passage from her chronicle "for feedback." It is clearly about the player. Edits it when they look.
- S2: Introduces the player to people with words that are slightly more than accurate — better than they've done, more than they've been.
- S3: Asks the player to sit for a portrait. Talks the whole time. Stops when she finishes. Hands it over without a word.

**LELIANA**
- S1: Sets a single bar of the cycle to the player's name — the way she sets a bar to the names of the dead at dawn, except this one is alive. Doesn't announce it; just plays it. The name is only legible if someone reads the Ballad Cycle.
- S2: Plays a verse the player has heard before, except it's gentler now — slower, the elegy taken out of it. Doesn't explain. Watches the player for recognition.
- S3: Plays a verse she does not say is new. Stops on the unresolved note. *"I cannot find the last line of this one alone, child. I need to hear you say something true first."* Waits.

### Physical Touch

Touch generates heat independently from staged behavioral flirts. Physical contact in a group scene is always visible and always generates heat in observing companions.

**LINZI**
- Grabs the player's sleeve to pull them toward something. Forgets to let go.
- Sits close enough their shoulders are touching. Does not shift away when she notices.
- Takes the player's hand mid-story — excited, unconscious — lets go the moment she realizes, then doesn't know what to do with her hands.

**LELIANA**
- Lets a hand rest on the player's shoulder a beat longer than the steadying gesture required, then leaves it there — the warmth deliberate, not absent-minded.
- Sets a single low note under her breath to something the player said hours ago, and watches, unhurried, to see whether they catch that the phrase is theirs.
- At the dawn hour she leaves the lute-case open beside her and does not fold the list of the dead away when the player approaches — the one privacy she guards, left ajar on purpose.

### Heat Values — Touch

| Touch type | Heat generated |
|---|---|
| Private touch (one-on-one, camp) | +1 to any observing attraction-flagged companion |
| Group-visible touch (in front of party) | +1 to all attraction-flagged companions present |
| Sustained or repeated touch in group scene | +2 |
| Stage 3 touch (both hands held, jaw, extended deliberate contact) | +2 regardless of setting |

---

## ✨ UNIVERSAL BEHAVIORAL SIGNALS

> **DM:** Pre-deliberate attraction signals — automatic responses that precede any conscious choice. Appear across all companions from Stage 1+. Stage rating = when each begins. Do not announce as attraction. Present the behavior.
>
> **Heat:** S1 = +1 | S2 = +1 | S3 = +2

#### MIRRORING — S1 / +1 heat
Unconscious posture or speech match. Before the companion notices.

*Linzi:* Tilts her head the same direction yours went. Doesn't know.

#### PREENING — S1 / +1 heat
Adjusts own appearance when the player approaches. Before contact. Before greeting.

*Linzi:* Pulls at her scarf when she sees you coming. Notes already straightening.

#### PERKING UP — S1 / +1 heat
Energy, posture, or attention visibly lifts when the player enters proximity.

*Linzi:* Mid-sentence with someone else — brightens the instant she spots you.

#### EYEBROW FLASH — S1 / +1 heat
Split-second recognition lift when eyes meet. Involuntary. Gone before it can be named.

*Linzi:* Across the room. You catch it. She's already looking at her notes.

#### OPEN POSTURE SHIFT — S1 / +1 heat
Body turns to face the player fully. Arms uncross. Feet pivot toward. Uninstructed.

*Linzi:* Was talking at the fire. Turns to face you when you sit.

#### EXTENDING CONVERSATION — S2 / +1 heat
Finds reasons to keep talking past the end of the useful exchange.

*Linzi:* Report done. She adds a footnote question. There is always a question.

#### PERSONAL OBSERVATION COMPLIMENT — S2 / +1 heat
Notices a specific quality no one else tracked. Offers it without framing.

*Linzi:* "You remembered what he said three days ago and used it. That matters."

#### WAIST TOUCH — S2-S3 / +1 or +2 heat
A hand at the player's waist — guiding, redirecting, steadying. Always deliberate. Never accidental. S2 context (guiding, group-visible) = +1. S3 context (sustained, alone, Stage 3+) = +2.

*Linzi:* Steering through a crowd, her hand finds your waist. Small. Definite.

#### FACE TOUCH — S3 / +2 heat
Self-touch at face or neck when flustered by the player. Involuntary. Before they can stop it. The most intimate signal — the body admitting what the voice won't.

*Linzi:* Covers her mouth with her hand. Laughed too hard. Stays there.

#### LINGERING — S1-S2 / +1 heat
Last to leave. Slow to end contact. Slow to break eye contact. Presence extending past its purpose. The companion who stays is the one who wants to.

*Linzi:* Everyone left the fire. She's still talking. She knows.

---

## 🎁 GIFT SYSTEM

> **DM:** Gifting is one of the cleanest Romance Score triggers — it is explicit, player-initiated, and immediately personal. Two categories exist: **Thoughtful Gifts** (low cost, high meaning) and **Practical Gifts** (useful items that also signal care). Both give +1 Romance. A gift that hits both categories — meaningful AND useful — gives +2. A gift that misses entirely gives 0 and costs the player the item.
>
> The player may give a gift at any camp scene or quiet moment. No action slot required in exploration mode. Takes 1 action in social scenes.

### What Makes a Gift Land

A gift lands when it connects to something the companion has said, shown, or implied. The DM evaluates fit — not price. A 1 gp wildflower picked from the roadside can outweigh a 500 gp enchanted blade if the flower connects to something real. The companion's reaction signals whether it landed.

```
GIFT RESOLUTION
  Player offers gift → DM checks fit against companion profile
    PERFECT FIT  : +2 Romance. Companion reaction: visible, specific, remembered.
    GOOD FIT     : +1 Romance. Companion accepts warmly.
    NEUTRAL      : 0 Romance. Companion accepts politely. Item transferred.
    MISS         : 0 Romance. Companion declines or accepts awkwardly. Item returned.
    INSULT       : −1 Romance (rare — only if gift implies something offensive about
                   the companion's values, history, or dignity)
```

### Thoughtful Gifts — By Companion

Low cost, high meaning. Found during exploration, purchased cheaply, or crafted. These are the gifts that work before Stage 2. After Stage 3, the companion expects *something* from time to time — not expensive, just attentive.

**VALERIE**
- A worn military manual found in ruins — she reads it the same night
- A single white flower, no explanation (*perfect fit if she's mentioned her homeland*)
- A replacement shield strap, hand-fitted — she notices it was measured correctly
- A letter of commendation (forged or real) praising her tactical record
- *Miss:* jewelry, perfume, anything decorative without function

**LINZI**
- A blank journal of unusual quality (vellum, good binding)
- An interesting pressed flower or leaf from a location that meant something
- A firsthand account from a local — a story she hasn't heard yet
- A small portrait sketch of the party (*perfect fit if she's mentioned the chronicle*)
- *Miss:* weapons, armor, anything purely combat-focused

**OCTAVIA**
- A rare spell component she mentioned needing and didn't ask for
- A book — arcane theory, history, something clever
- A freedom-related token: a broken manacle found in a dungeon, given quietly
- An unsolved puzzle box (she will solve it in two hours and be smug about it)
- *Miss:* domestic items, anything that implies a conventional life

**TRISTIAN**
- A small Sarenrae icon found in a ruin — not purchased, *found*
- Wildflowers from somewhere he's been praying (*perfect fit at any stage*)
- A journal of someone's kindness — a found document showing someone doing good
- A candle, given with no explanation on a hard night
- *Miss:* anything martial, anything related to Rovagug or the dead gods

**KALIKKE**
- A smooth river stone — she holds things when she's thinking
- Something from nature that has two qualities at once (fire-opal, frost-touched wood)
- A small sketch of somewhere peaceful, given before a hard day
- Anything given *to both of them* — she notices when both are acknowledged
- *Miss:* anything given only to one twin and not the other (Kanerah is watching)

**NOK-NOK**
- A red ribbon — he wears it immediately
- Anything shiny and small (he has a collection; he will show you his)
- A trophy from a creature larger than him — he inspects it, stores it with his own
- Particularly good jerky in quantity (*perfect fit* — he shares exactly half)
- *Miss:* books, papers, quill sets — anything requiring literacy he doesn't have

**JUBILOST**
- A map of territory he hasn't charted yet
- A precision instrument — caliper, quality lens, measuring string
- An unsolved geographic puzzle (he will solve it and send you the correction)
- A written acknowledgment that one of his theories was correct (*perfect fit*)
- *Miss:* domestic items; anything implying he has feelings to be comforted

**EKUNDAYO**
- Something from deep forest — smooth stone, unusual feather, a track pressed in clay
- Food prepared without ceremony, left without expectation
- A carving of a hound, crude is fine (*perfect fit* if you made it yourself)
- A name scratched into bark — someone you asked about once and left alone. He takes it. Does not put it down.
- *Miss:* anything of court, title, or formal recognition; he sets them down quietly

**LELIANA**
- A length of fine lute-string, a grade above standard — she notices the grade before anything else, and the damp won't touch it
- An old air or ballad she named once in passing, written out — something from a place or a century she has not heard played since it fell
- A blank book of wide-staved vellum — she has been cramming the cycle into margins for years (*perfect fit*)
- A handful of good earth or seed from somewhere green — she has always kept a garden, in every life long enough to allow one; she will plant it
- Something from a place that was beautiful — a river stone, a pressed flower, a scrap of a fallen town's banner — given without ceremony
- *Miss:* any instrument other than her lute's needs (she plays the one); anything showy or ceremonial (gilded cases, a presentation made of the giving)

**HU TAO**
- A rare graveside blossom, or funeral incense of good make
- Fine paper and ink for her dreadful poems (she will write you one; it will be terrible; keep it)
- A ghost story she hasn't heard — *perfect fit* if it's true
- A small token from someone you helped see off properly — she understands exactly what it means
- *Miss:* anything that mocks the dead, or treats death as a horror to flee from

**KEQING**
- A perfectly balanced blade, or a superior whetstone
- A well-made ledger, a rare law-text, an efficient tool that saves an hour a day (*perfect fit*)
- A genuine problem, handed over as a gift — she'll have it solved by morning and be delighted you trusted her with it
- A storm-stone / Electro focus, practical not ornamental
- *Miss:* idle luxuries, "blessed by fate" trinkets, anything ceremonial with no use

**YOR FORGER**
- A perfectly balanced new stiletto, or fine whetstones — she notices the balance before anything else
- A small thing fit for a younger brother (she lights up — the surest road to her heart)
- Soft silent-soled shoes, or a plain dress that hides every blade
- A token of a chosen home — a key, a hearth-charm — given plainly
- *Miss:* loud showy gifts; anything that demands she declare herself in public

**AERITH**
- Rare flower seeds, or a cutting of something that shouldn't grow here (*perfect fit*)
- A window-planter; a healer's herb-kit restocked by your own hand
- A pressed flower from somewhere that made you think of her
- A Sarenrae token, plain, not gilded
- *Miss:* anything that cages a living thing; making the giving a transaction

**BELLATRIX**
- A cruel, pretty trophy; a curse-focus; an athame of good make
- A piece of her old house's stolen finery, recovered for her
- A *target* — permission, with purpose, to do what she does (she will be ecstatic) (*perfect fit*)
- *Miss:* mercy-tokens, oath-trinkets, anything soft or forgiving ("dull")

**REVY**
- Fine powder and shot; a quality holster-rig; a flintlock worth her hands
- Good strong liquor, the expensive kind, for no occasion
- Smokes; a flask that won't dent (*perfect fit* — she'll never say thanks, she'll just carry it forever)
- *Miss:* sappy keepsakes; anything sentimental; banners or loyalty-trinkets

**SATSUKI KIRYŪIN**
- A master-grade care kit for her katana; flawless steel
- A command standard; a campaign map of a worthy enemy
- A rare strategic text, or intelligence she genuinely needs (*perfect fit*)
- *Miss:* flattery-gifts; mercy-tokens; anything that excuses weakness

**VELVET CROWE**
- Blade whetstones; anything that sharpens the hunt
- A warm thing she can "pass to the strays" while flatly denying she cares
- A quiet keepsake that would fit a lost younger sibling — handled with great care, never named aloud (*perfect fit* if you understood without being told)
- *Miss:* pity-gifts; forgiveness-tokens; "greater good" tracts; religious mercy-iconography

**ATALANTA ALTER**
- Fine bowstrings, keen broadheads, a trophy of a worthy hunt
- A token tied to a child kept safe (she goes very still — ⛔ handle deliberately, never as a fabricated quest)
- Fast-game tokens; anything that promises a good chase
- *Miss:* pity; "cures"; leashes or muzzles; anything that treats her as a broken thing

> *(Gift reactions are shown, never announced — see § Gift Reactions below for the per-character tells.)*

### Practical Gifts — Useful Items That Also Signal Care

Items given as gifts (not loot distribution). The player acquired them *for* the companion. Player states they are *giving* the item as a gift. DM checks: does this item fit the companion's build AND reflect awareness of them as a person? If yes: +1 Romance on top of normal loot transfer. If no (just optimizing gear): normal transfer, no Romance effect.

| Companion | Best Practical Gifts | Why It Lands |
|-----------|---------------------|-------------|
| **Valerie** | Shield upgrade before a hard fight; Tower Shield rune | She didn't ask. You noticed anyway. |
| **Linzi** | Light armor upgrade; Inspire Courage scroll | Protecting the one who documents everything |
| **Octavia** | Filled spell component pouch; wand of her frequent spell | Autonomy — she doesn't have to ask anyone |
| **Tristian** | Expanded Healer's Kit, stocked; healing scroll above his slots | He gives everything away. Someone thought of him. |
| **Kalikke** | Cold-weather cloak (one for each twin); elemental focus item | Both. Always both. |
| **Leliana** | Oiled lute-case lining or fresh strings against the damp (she has complained the damp gets into the strings); a balanced songblade | She didn't ask. You noticed anyway. She uses it that session and says nothing — which, from her, is the thanks. |
| **Hu Tao** | A reach-spear upgrade or a fire-rune before a hard fight; quality funeral charms | She doesn't say thanks — she names the spear something morbid and uses it that session |
| **Keqing** | A speed/lightning rune for the blade; a better set of marking-stilettos | She'll note it's measurably more efficient and never once set it down |
| **Yor Forger** | Paired finesse daggers, balanced; concealed spine-sheaths | She tests them once, silently, perfectly — that is the thanks |
| **Aerith** | A restocked healer's kit; a staff focus that eases the channel | She uses it on someone else first, then turns and beams at you |
| **Bellatrix** | A fine athame or curse-focus; a wand of her slow-work hex | She strokes it like a pet and holds your gaze a beat too long |
| **Revy** | Fine powder & shot; a quality flintlock or holster-rig | She field-strips it on the spot — from Revy, that IS the thank-you |
| **Satsuki Kiryūin** | A master care-kit for Bakuzan; fittings for the war-garment | A single approving nod — which from her is a decoration |
| **Velvet Crowe** | A concealed blade of good make; whetstones | *"Adequate."* She uses it that day. She does not pity-thank, and respects that you didn't make her |
| **Atalanta Alter** | A keen broadhead, fine fletching, a faster bowstring | She tests the draw and laughs aloud at the song of it — delight is the whole of the thanks |

### Gift Reactions — How the DM Shows It Landed

Never announce "+1 Romance." Show it. Valerie holds the item a moment too long, then integrates it silently. Linzi writes something immediately and won't show it. Octavia examines it professionally, then: *"You didn't have to"* — keeps talking as if she didn't say that. Tristian thanks quietly and asks one question about why. Kalikke thanks in her voice, then Kanerah's voice adds something.

---

## 💞 PHYSICAL INTERACTIONS

> **DM:** Player may attempt a physical interaction at any camp or quiet scene. Companions never initiate first (except per the Companion-Initiated Contact section above — that's the narrow exception). Each has a Stage requirement — attempting below it results in a gentle step-back, not hostility. No roll for interactions at or above requirement unless marked. Check Mood state before resolving.
> **Surface in menu** when a romance-eligible companion is present in a non-combat scene and Romance ≥ 1: add **[Reach out]** option. Expand on selection.

### Interaction Table

| Interaction | Min Stage | Roll | Success | Failure |
|-------------|-----------|------|---------|---------|
| Brush hand / touch arm | 1 | No | +1 Romance | 0, no comment |
| Offer hand (walking) | 1 | No | +1 if taken | 0 if declined |
| Adjust cloak / hair | 1 | No | +1 Romance | 0 if they step back |
| Shoulder bump / lean | 2 | No | +1 Romance | 0, near-miss logged |
| Hug | 2 | DC 12 Dip | +1 Romance | 0, gentle pull-back |
| Hold hand (sustained) | 2 | No | +1 if held | 0 if released |
| Rest head / let them rest | 3 | No | +1, Bond Moment | 0 |
| Forehead touch | 3 | DC 14 | +2 Romance | −1 if wrong Mood |
| Kiss (cheek) | 3 | DC 14 | +1 Romance | 0; *"Not yet."* |
| Kiss (first, real) | 4 | DC 16 | +2, Bond Moment, heart scene | −1; *"I need a moment."* |
| Embrace (full, held) | 4 | No | +1, Morale +1 | — |
| Kiss (established) | 5 | No | No score; Bond texture | — |

### Per-Companion Touch Notes

**Valerie:** Touch is not casual. Brush hand: she doesn't move away — that's the signal. Hug: arms come up slowly. First kiss: kisses back, steps away, says nothing. Later: *"That was..."* Doesn't finish.

**Linzi:** Warm, expressive. Smiles immediately. Hug: completely, immediately. First kiss: wide eyes, then laughs and writes something.

**Octavia:** Confident physically, guarded emotionally. Hug: *"Don't read into this."* First kiss: returns it. *"Okay. That happened."*

**Tristian:** Flinches first, then stills. Hug: doesn't know what to do with his hands, then does. First kiss: *"I didn't think I'd... I'm glad."*

**KALIKKE/KANERAH:** Touching one is touching both. First kiss (Kalikke): *"She'd want me to tell you she liked that too."*

**NOK-NOK:** Touch is total — he's climbed strangers. Brush hand: he takes it in both of his, pumps it once, does not release. Hug: full-body, he tries to get his feet off the ground during it. First kiss: complete bafflement, then absolute delight. *"Is that the bonding ritual?! Nok-Nok has heard of this! YES."*

**JUBILOST:** Touch as single-point hypothesis. Brush hand: he examines his own hand afterward, makes a note, moves on. Hug: rigid for three seconds — *"Well. That's statistically interesting."* — releases. First kiss: does not move for four full seconds. Then: *"I will need to replicate this to establish a baseline."* He means it.

**EKUNDAYO:** Trkaa moves first — she settles against you before he does. Brush hand: he holds it briefly, releases it; no explanation. Hug: one arm, firm, counted in breaths; he doesn't extend it. First kiss: he cups your face in both hands first, looks at you a long time. Then: deliberate. *"She would have liked you."* It is the highest thing he has.

**LELIANA:** Touch lands and she does not startle or deflect — she chooses, deliberately, not to flinch from it. Brush hand: she turns her hand over and lets the player's rest in it a moment, unhurried, like she has decided to allow this. Hug: she folds the player in slow, one hand at the back of the head, and goes very still — the stillness of someone who has not let herself be held since the last time being held was a trap. First kiss: the warmth goes deep instead of bright, grave and quiet. A long pause. Then, low: *"I told myself I'd never hand my heart over again. ...I was wrong — and you didn't even have the decency to ask permission before proving it."* She does not pretend it was nothing. She kisses you again, unhurried.

**HU TAO:** Touch is a game until it isn't. Brush hand: she grabs it, inspects your palm, "reads your lifeline" with a grin and a grim verdict — then doesn't let go. Hug: enthusiastic, theatrical, then she goes quiet in the middle of it for one beat too long. First kiss: she makes a joke right up to the half-second before, and then doesn't make one, which from Hu Tao is a vow. After: *"...Huh. No notes. That never happens."*

**KEQING:** Touch is inefficient and she has clearly scheduled it anyway. Brush hand: she lets it happen, jaw tight, pretending to read something. Hug: rigid two seconds, then abruptly leans in and grips like she means it. First kiss: brisk and decisive, like she's worked out the logistics — then, thrown by her own reaction: *"...That was. Hm. We'll be doing that again. For consistency."*

**YOR FORGER:** Touch off the clock makes her clumsy and pink. Brush hand: she startles, apologizes, then carefully doesn't pull away. Hug: she holds too gently, terrified of her own strength. First kiss: utterly undone, achingly careful — and after, very quiet: *"I never let anyone close enough to... I kept waiting for the part where the knife comes out. It didn't. With you it just— didn't."*

**AERITH:** Touch is easy and warm; she leads with play. Brush hand: she laces fingers and swings your joined hands, grinning. Hug: full and immediate, and she presses her ear to your chest like she's listening for something. First kiss: bright, then suddenly soft and certain — and after: *"There. Now it's real and you can't take it back, and I'm so glad. Don't look surprised. I told you I always know."*

**BELLATRIX:** Touch is intensity with no dimmer. Brush hand: she seizes it, presses your palm to the burned brand at her wrist, watches your face for the flinch. Hug: she clings, too tight, fervent. First kiss: devouring, worshipful, frightening in its totality — and after, breathless: *"Again. *(a shudder)* Do that again. I have been so cold for so long, and you are so *warm*, beloved."*

**REVY:** Touch makes her bristle, and she covers it by being crude. Brush hand: *"What're you—"* but she doesn't move it. Hug: rigid, arms stuck out, then one hand fists in the back of your shirt and stays. First kiss: rough and fast, like she's stealing it before someone stops her — then she looks away, ears red: *"...Shut up. Didn't say anything. SHUT up."*

**SATSUKI KIRYŪIN:** Touch is something she permits — sovereign, deliberate. Brush hand: she turns hers palm-up and lets yours rest there, regarding it like a decision already made. Hug: she goes very still, unused to being held rather than obeyed, then her hand settles at the small of your back. First kiss: composed, and then not, the control slipping for one staggering moment — after, plainly, no verdict wrapped around it: *"...Yes. That. We will have that."*

**VELVET CROWE:** Touch is the thing she burned out, waking back up. Brush hand: the bandaged arm flinches; the other hand, slowly, does not. Hug: she stands stiff inside it, then her forehead drops to your shoulder like something giving way. First kiss: starved and clumsy and furious at herself for needing it — and after, rough, the nearest she comes to tender: *"...Don't. Don't say anything kind, I'll bolt. Just— stay there. A minute. Don't move."*

**ATALANTA ALTER:** Touch she treats as another delightful hunt — until it isn't. Brush hand: she catches it fast, grinning, *"got you."* Hug: all theatrical squirm, then abruptly, completely still, the way she goes when something real slips through. First kiss: bright and biting, then unexpectedly desperate — and after, the smile gone for one breath: *"...Oh. That's the thing I gave up, isn't it. The wanting. *(it creeps back, fragile)* ...Keep it to yourself, sweetness. I have a reputation."*

### Rejection

Stage 1–2: Never hostile. Companion steps back or finds something to do with their hands. Score drops only if player pushes past a clear step-back (−1). Stage 3+: wrong moment — Mood, timing. Companion says something quiet. Not cruel. True.

---

## 🌹 ROMANTIC ACTIVITIES BY STAGE

> **DM:** Optional player-initiated events during downtime, camp, or settlement visits. Not the same as Camp Interludes (which fire randomly). Cost time, sometimes gold. Companion must be present and at the right stage. Player initiates with `.activity` or by describing what they want to do.

### Stage 1 — CURIOUS: Early Activities

*Low stakes. Deniable. Neither party has to admit anything.*

**Walk the Perimeter Together** — Cost: None. Time: 1 hour camp time. The player and companion do the watch circuit together instead of alone. Effect: +1 Romance if the player listens more than they speak.

**Shared Meal (Camp)** — Cost: Requires a Special Meal recipe. Time: part of camp cooking. Effect: +1 Romance on a successful Cook Special Meal check. The companion's reaction is calibrated to the food.

**Teach Me Something** — Cost: None. Time: 1 hour. Player asks the companion to teach them one thing they know. Effect: +1 Romance. The companion gets to be the expert.

### Stage 2 — SMITTEN: Closer Activities

*Something is clearly happening. Neither party is pretending otherwise.*

**Stargazing / Night Watch Together** — Cost: None. Time: replaces standard watch. Effect: +1 Romance. Triggers a Camp Interlude automatically at end of watch.

**Find Something for Them in the Field** — Cost: Hunt and Gather or Search — player declares intent to find something for the companion specifically. Effect: On success, player finds something small and fitting. Giving it: +1 Romance.

**Settlement Evening (in town)** — Cost: 5 gp. Time: 1 downtime evening. Player invites the companion to spend an evening in a settlement — tavern, market, temple, whatever fits them. Effect: +1 Romance.

### Stage 3 — ADMITTED: Intentional Activities

*Both parties know what this is.*

**Teach Something Personal** — Player shares something from their backstory. Effect: +1 Romance. Companion responds in kind. Earns +2 trigger if both parties reach genuine mutual disclosure.

**Capital Tour (first time in the capital)** — Cost: None. Time: 1 afternoon. Player shows the companion around the capital they're building together. Effect: +1 Romance.

**Write a Letter Together (Linzi — unique)** — Linzi offers to help the player write something. Effect: +2 Romance with Linzi specifically. The letter or entry becomes a permanent document in `found_documents[]`.

### Stage 4+ — CONFESSED / CONSORT: Formal Dates

*Full Date Night events (above). Additionally:*

**Private Dinner (Capital — Chambers)** — Requires: Personal Chambers + Featherdown Bed or Hearthfire. Cost: 30 gp. Uses one Downtime evening. Effect: +1 Romance, Morale +1. Unrest −1 if at Stage 5.

**First Watch, Every Night** — At Stage 4+, the player may declare they always share first watch with the companion. Effect: Camp Interludes fire at +1 to the trigger roll.

### `.activity` Command

| Command | Output |
|---------|--------|
| `.activity` | List available romantic activities for current stage and location |
| `.activity [name]` | Initiate a specific activity with the active romance companion |
| `.gift [item]` | Offer a specific item as a gift — DM evaluates and resolves |
| `.gift idea` | DM suggests 2–3 gift options appropriate to current stage and companion |

---

## 🎭 COMPANION ROMANCE PROFILES

> **DM:** Per-companion narrative reference. Use when running romance scenes, interludes, and escalation beats. These profiles govern how each companion experiences the romantic track — their specific behavior patterns, what cracks them open, what closes them back down. Mechanical entries (DC, buffs, gift lists) are in the tables above; this section is voice and arc.

---

### LINZI — Romance Arc Profile

**Stage entry barrier:** LOW. She is already writing the chapter in her head. The wall is not resistance — it is that she needs the player to mean it. An offhand gesture will not move her. One real, specific moment will.

**Pursuit response:** She meets pursuit with warmth and deflection — not because she doesn't want it, but because she writes things down and she knows how this can end. She accepts every gesture and records none of them in the book she shows you. The real record is the one she keeps.

**Mid-stage break (Stage 2):** After a hard loss or a scene that cost the party something real, she stops writing. Sits outside the camp. When the player finds her, she is reading back old entries. She says: *"I've been trying to figure out where the story goes from here."* She does not mean the chronicle.

**Unlock text:** *"I have been in love with the idea of a story my whole life. I didn't expect the story to be standing in front of me asking if I was all right."*

**Love scene:** Late. The fire almost out. She has been reading to the player from the early chapters — before the expedition, before anything happened. She stops mid-page. Sets the book down. Does not explain why. The scene has no words after that. In the morning, there is a new entry. She does not read it aloud.

**Arc tone:** Being witnessed. She has been watching everyone else's story her whole life. The romance arc is the slow realization that she is allowed to be in one.

**Approval thresholds:**
- +1 Romance: Player takes a moment she wrote about and references it later — shows he read what she gave him
- +1 Romance: Player chooses to protect something small and unimportant because it was the right thing
- +2 Romance: Player completes a scene with genuine dignity under pressure — something she can write as legend and mean it
- −1 Romance: Player dismisses her chronicle as decoration or distraction
- −1 Romance: Player uses something she disclosed to manipulate a third party

**Romance-specific state voice lines:**
- *[Stage 1, player catches her looking]:* *"I was — cataloguing. You have an interesting face. Narratively."*
- *[Stage 2, after a fight the player won against odds]:* She doesn't say anything during. Afterward, quietly: *"I'm going to need a better word than 'remarkable.' I've used it twice this chapter."*
- *[Stage 3, player asks what she's writing]:* Long pause. *"A revision."* She closes the book.
- *[Stage 4, first morning]:* *"I wrote seventeen possible versions of what I would say. None of them were right. So: good morning."*
- *[Stage 5, after any victory]:* *"The chronicle says you won. It doesn't say what it cost. I know. I was there."*

**Jealousy note (if player is also romancing Leliana):** Linzi notices Leliana's ballad-cycle before she notices anything else — one chronicler hearing another keep the same faith with a different tool. She asks once, not accusatory, genuinely curious, whether the player has heard the new verse. Her handwriting gets smaller in the chronicle entries from that session. She does not bring it up again. The record speaks instead. (Note: Linzi and Leliana are never both in the party — one slot. This fires only if Leliana holds the slot and the player romances her while courting Linzi in a separate run-memory, or via the chronicler-gate edge case.)

---

### LELIANA — Romance Arc Profile
*(leliana_relationship_stage tracks the chronicler-bard romance slot — Attraction-eligible: Yes.)*

**Stage entry barrier:** HIGH — but not coldness and not performance. The barrier is *trust*. She gave her whole heart once, to the woman who trained her — Marjolaine — and that love was used as a lever to frame her, break her, and very nearly end her. So when someone reaches for Leliana now, two fears wake at once: that this, too, is a game of masks she will only see the shape of too late; and that she is still, underneath the faith, the bard who once weaponized love as a tool. She deflects pursuit by being *kind* — redirecting to the player's wellbeing, a wry joke at her own expense — because the gentlest lie is easier than the true sentence: *I am afraid to believe you, and more afraid of what I am capable of if I do.*

**Pursuit response:** Gentle deflection dressed as care. *"You don't want to hitch a wagon to a woman who learned love at knifepoint."* She gives the player's question back — genuinely interested — and lets that be the redirection. She names the obstacle plainly (what was done to her, what she once did) rather than hiding it. She does not misread interest; she is far too trained and perceptive for that. She simply declines to acknowledge it, gently, twice, because the kind thing is to let the player change their mind before either of them can be hurt the way she was.

She will decline interest gently — twice. The third earnest declaration, she stops declining. She does not announce the shift. She simply answers as though she had heard it the first time.

**Mid-stage break (Stage 2 — the break moment):** The player finds Leliana at the dawn hour — the grey hour she keeps for her faith and for the dead the Game took from her — lute in her lap, quietly naming the people she lost: friends, a self she had to bury, names Marjolaine's world cost her. The one private ritual she shows no one. She hears the player arrive. She would normally fold it away and be ordinary. She doesn't. She keeps playing, keeps naming, and after a while says without turning: *"You may stay for this. I don't show it to anyone. ...I'm showing it to you. Don't make it a thing."* She keeps faith to the bottom of the list. Then she sets the lute down and lets the player stay.

**Unlock text:** *"I told myself I had learned my lesson about this — that I'd never again hand someone the knife and call it my heart. And here I am. You didn't even have the decency to ask permission before proving me wrong about myself."*

**Love scene:** Pre-dawn, the camp or the keep's high room, the grey hour she keeps for faith and grief. For the first time she does not spend it on the dead. She asks the player to stay while she plays the Unfinished Verse through — the whole cycle, first bar to wherever she has written, which she has never played whole for anyone. When she reaches the place where it has always turned into an elegy — the place her trust always broke — she keeps going, improvises past it, and finally lets it resolve into something that is, for once, a vow and not a eulogy. She sets the lute down. They do not speak. The silence after is the first one she has allowed to simply *be*, with someone in it she has decided to believe.

**Arc tone:** Not winning her over and not pushing through a wall — it is proving, slowly and without ever once lying to her, that this love is what the last one was not: *honest, eyes-open, no mask under the mask.* The player cannot rush her and cannot argue her past the caution Marjolaine carved into her; they can only keep showing up, true every time, until she decides she can trust again — and trust her own heart not to turn a weapon. She has to choose to believe. No one can choose it for her.

**Approval thresholds:**
- +1 Romance: Player listens to her play without asking what the names mean or what the verse is "about"
- +1 Romance: Player notices she has gone to the dawn hour and does not try to fix the grief or pull her out of it
- +1 Romance: Player references something true from the ballad-cycle — shows they have actually been listening across sessions
- +2 Romance: Player stays after the cycle when everyone else has gone — does not explain why, does not speak first
- +2 Romance: Player tells Leliana something true and costly about themselves, unprompted — offers it where she asked nothing (honesty freely given is the exact thing she was denied)
- −1 Romance: Player tells her a comfortable half-truth and is caught in it — even a small one; she has been lied to by someone she loved, and she clocks it
- −1 Romance: Player tries to name what she is feeling before she has said it
- −2 Romance: Player tries to *handle* her — managing her with charm, using her past as leverage to get past her guard. It reads as exactly the thing Marjolaine did, and it is very hard to undo

**Romance-specific state voice lines:**
- *[Stage 1, player catches her at the dawn hour]:* *"I was tuning. The damp gets into the strings."* She resumes the names. She was not tuning.
- *[Stage 2, after a quiet camp night]:* *"I wrote a verse tonight I actually mean to keep. That's rarer than you'd think, for me. I'm crediting the company — don't ask which company. You know which."*
- *[Stage 3, after the declaration]:* *"I have been kind to you on purpose, to give you room to run. You didn't run."* A beat. *"I'm done being kind in that particular way."*
- *[Stage 4, morning after love scene]:* She is already playing when the player wakes — something new, unhurried, resolved. She doesn't look up. *"I found the last line. It isn't an elegy. It's the first thing I've written believing it all the way down."* Nothing else.
- *[Stage 5, any scene of genuine danger to the player]:* She sets the lute down. She is watching the player, not the threat, not the room. She says nothing. The lute stays down until the player is safe — and the songblade is already in her other hand. The bard never fully left her hands; tonight she is glad of it.

**Jealousy note (if player is also romancing Linzi):** Leliana does not compete with the younger chronicler — she would find it beneath them both. She reads what Linzi writes, says nothing about it, and her own warmth toward the player banks down to something formal and careful, a closed door behind a courteous face. The tell is the *withdrawal of the dawn hour*: she stops letting the player near it. The DM may note `passive_jealousy heat +1`. Her jealousy is not loud and not cold — it is a quiet, deliberate stepping-back, the act of a woman who learned the hard way not to ask for what isn't freely and honestly hers. It is, eventually, unmistakable, and harder to address than anger would be.

---

### HU TAO — Romance Arc Profile
*(hutao_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** MEDIUM, disguised as its opposite. Hu Tao flirts and jokes with everyone; the mischief is so constant no one can tell when she means it — which is the point. She has buried a great many people she was fond of, and she is not afraid of death. She is afraid of *attachment* — of letting a living, breakable person matter enough that losing them would be the thing that finally hurts. So she keeps it all a joke, because a joke is a door she can close.

**Pursuit response:** She escalates the teasing — outrageous flirtation, a dreadful love-poem read aloud to watch the player squirm, a nickname that means everything and nothing. Laugh and play along, and she stays safe behind the bit. Answer the joke *seriously* — meet her eyes and refuse to let her hide in it — and she falters for half a second, then covers with a worse joke. That falter is the whole tell.

**Mid-stage break (Stage 2):** The player catches her at the parlor's makeshift altar, or over a fresh grave she dug for a stranger no one else would bury, and for once she is not performing — doing the rite properly, quietly, with the bottomless tenderness the jokes protect. She doesn't startle. *"You found me being sincere. Ugh. Don't tell anyone — it'll ruin my whole reputation."* A beat, the grin gone soft. *"...I do this for everyone, the dead. Always have. Trouble is I've started doing the opposite for you — keeping a very nervous eye on the *living* part. That's new. I don't like new."*

**Unlock text:** *"Here's the awful thing I never say: I'm not scared of dying. Made friends with that years ago. But you — you I could lose, and THAT one I haven't made friends with at all. So obviously the sensible solution is to stay extremely close and keep an eye on you. For safety. Purely professional."*

**Love scene:** Somewhere quiet and late, the talismans put away. The mischief finally drops all the way for the first time, and what's underneath is startlingly gentle — a person who looks at endings for a living, choosing, with both eyes open, to hold something that will end anyway. She doesn't joke once. In the morning she's insufferable again, but she leaves a poem on the pillow, and the poem, for once, has a good last line.

**Arc tone:** Convincing her the joy is worth the eventual grief — that loving a mortal thing isn't a mistake just because it ends. She knows exactly how it ends. The arc is her deciding to do it anyway; the player has to be the one thing she can't make a joke out of.

**Approval thresholds:**
- +1 Romance: Player honors the dead properly when it would be easier not to
- +1 Romance: Player answers one of her jokes with real sincerity instead of laughing it off
- +2 Romance: Player tells her plainly they intend to *live*, be careful, come back — the one reassurance she wants and would never ask for
- −1 Romance: Player jokes cruelly about a real loss, or treats the dead carelessly
- −2 Romance: Player uses/threatens necromancy or clings to a death that should be let go — it strikes the one law she holds sacred; she goes cold in a way the jokes don't easily come back from

**Romance-specific state voice lines:**
- *[Stage 1]:* *"Marrying a funeral director — think of the discounts! ...That was a proposal joke. I'm studying how you flinch. Fascinating. Again."*
- *[Stage 2]:* *"I wrote your epitaph today. Out of habit. Then I tore it up, which I have NEVER done for anyone. I'm rather upset about it."*
- *[Stage 3, after declaration]:* *"Fine. You win. I'm attached. Deeply inconvenient, I blame you entirely. ...Don't die. I mean it. I'll be SO annoyed."*
- *[Stage 4, morning after]:* The poem on the pillow with a good last line. She's pretending to be asleep so she doesn't have to watch the player read it.
- *[Stage 5, danger to player]:* No jokes. Spear up, flame along the blade before anyone else has moved, squarely between the player and the door the dead would come through. *"Not this one. Not today. Take a number."*

**Jealousy note:** She escalates into manic over-the-top theatrics — "officiating" the rival pairing with deranged cheer, writing a wedding poem nobody asked for. It's funny until you notice she's not sleeping and the poems have gone very dark; the grief she built her whole personality to outrun is leaking through. DM may note `passive_jealousy heat +1`.

---

### KEQING — Romance Arc Profile
*(keqing_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** HIGH. Keqing built her whole identity on needing no one to rescue her — dependence is the exact weakness she lectures everyone else out of. *Wanting* someone reads to her as a structural flaw in a system she's spent her life perfecting. She doesn't deflect with kindness or jokes; she deflects with *work*. There is always a more urgent task — she isn't lying, there always is — she just schedules them, precisely, for whenever feeling might otherwise happen.

**Pursuit response:** She redirects to the practical. *"If this is about efficiency, say so and I'll allot time. If it's about feelings, I have a ledger that needs balancing."* Too brisk, a half-beat too fast — the speed is the tell, since Keqing is never flustered except about exactly this. If pushed she gets blunter, not softer. But she also, without comment, starts being where the player is: the harder watch, the reorganized gear. The mouth says "inefficient." The hands have already decided.

**Mid-stage break (Stage 2):** The player finds her working at an hour no one should, run completely ragged, too tired to out-argue her own face. *"I work because if I stop, I have to notice things. And I've started noticing a thing I did not budget for, and it will not BALANCE, I've recalculated—"* She stops. Sets the pen down. Quiet, almost angry at herself: *"I don't know how to want something I can't earn by working harder. You're the first problem I've met that doesn't yield to effort. I find it intolerable. ...Don't go anywhere."*

**Unlock text:** *"I have decided to depend on you. Do you understand the cost — I spent my entire life proving I'd never have to. This isn't weakness. This is me deciding you are worth becoming, in one specific place, a little less invulnerable. Don't make me regret the audit."*

**Love scene:** She approaches it the way she approaches everything — directly, no euphemism, faintly terrified and refusing to show it. Once she stops managing the moment the relentless control drops, and under it is someone starving for exactly this and furious at how much. Afterward she makes no speech. She just stays — which from Keqing, always already onto the next thing, is the entire confession.

**Arc tone:** Teaching her that letting someone in is not a failure of self-reliance. The player cannot do this by taking care of her (she'll bristle and bolt); they do it by being competent, trustworthy, and *there*, over and over, until she files "depending on this person" under proven-reliable instead of dangerous-weakness. She has to choose to need someone.

**Approval thresholds:**
- +1 Romance: Player does the unglamorous work themselves rather than delegating or waiting on luck
- +1 Romance: Player accepts her competence without turning it into a sentimental "moment"
- +2 Romance: Player trusts her to handle a hard thing on her own instead of protecting her
- +2 Romance: Player tells her plainly they trust her judgment over their own on something that matters
- −1 Romance: Player frames her care as "cute," forcing the feeling open before she's ready
- −2 Romance: Player solves a problem by waiting on fate, divine favor, or birthright — a values-level betrayal, not just a bad tactic

**Romance-specific state voice lines:**
- *[Stage 1]:* *"I reorganized your pack. It was inefficient. That's all that was. Stop looking at me like that."*
- *[Stage 2]:* *"I've factored you into my planning. As a variable. A high-priority variable. ...Don't read into the priority."*
- *[Stage 3, after declaration]:* *"Fine. Yes. The thing you think is happening is happening. I've checked three times. The result keeps coming back the same. It's you."*
- *[Stage 4, morning after]:* Already up, already working — but she's made tea for two and set the second cup at the player's side of the table, and will deny to her last breath that it means anything.
- *[Stage 5, danger to player]:* *"Mark."* She arrives between the player and the threat in a crack of lightning, sword already moving, the cold efficiency with heat under it now. *"Hold. I have this. I have YOU."*

**Jealousy note:** She does not compete — competing admits she could lose, which is unthinkable. She becomes hyper-professional, warmth filed away, devastatingly polite, works more and says less. The tell: the small unasked-for things — the reorganized gear, the second cup — simply stop. DM may note `passive_jealousy heat +1`.

---

### YOR FORGER — Romance Arc Profile
*(yor_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** HIGH, and quietly heartbreaking. Yor has two selves: the clumsy, over-apologetic daylight woman, and the flawless killer. No one has ever loved both, because no one has ever known both. She is certain that the moment someone sees the whole of her — the work, the blood, what she's done to feed her brother — they will recoil, and she will deserve it. So she keeps the halves in separate rooms and lets no one all the way into either.

**Pursuit response:** She takes interest *literally* and earnestly — misreads warmth as friendship, over-apologizes, fetches tea. She isn't playing coy; she genuinely does not believe the interest is romantic, because the version of her worth wanting is a person she's sure doesn't exist. Be clear and gentle and she goes very still — the dangerous stillness, except there's no target, just a feeling she has no idea how to hold. *"I think you have me confused with someone softer. I should tell you what I am, before this goes further. You won't want it after."*

**Mid-stage break (Stage 2):** The player sees her work — the flat-voiced lethal half — and does not flinch, does not leave. For Yor this is the impossible thing. Later, very quiet: *"You watched me do that. And you're still here. Everyone I've let close, I kept on one side of a wall, sure the other side would end it. You walked through the wall and didn't run. I don't have a word for what that does to me. I'm sorry. I'm not good at the words."*

**Unlock text:** *"My whole life has been keeping people safe by keeping them away from what I am. You're the first person I want to keep close AND keep safe, and I don't know how to do both at once. But I'd like to learn. With you. If you'll have the whole of it — the clumsy part and the other part — I'm yours. All of me. It isn't a small thing I'm offering. It's everything I had to hide."*

**Love scene:** Achingly tender and a little awkward — she has no practice being wanted as herself. She keeps almost apologizing; the player keeps not letting her. When she finally believes it — held by someone who knows exactly what her hands have done and stays anyway — something she has carried alone since childhood finally sets down. The child's mended hairpin stays nearby. She doesn't explain it. She doesn't have to anymore.

**Arc tone:** Someone choosing the whole of her — both halves, no wall. Not by ignoring the killer (that's just the cover again) or being thrilled by it (worse), but by seeing all of her plainly and treating her like a person who feeds a family rather than a weapon. Her brother Yuri is the proof of her heart she's afraid to show.

**Approval thresholds:**
- +1 Romance: Player treats her clumsy daylight self with genuine warmth, not amusement
- +1 Romance: Player doesn't flinch from the work — neither horrified nor delighted, just steady
- +2 Romance: Player protects something she loves (a vulnerable person, a child) without being asked
- +2 Romance: Player calls her by her chosen name and clearly means *her*, the whole of her
- −1 Romance: Player treats her only as a weapon — admiring the kill, never the woman
- −2 Romance: Player uses someone she loves as leverage, or forces her to choose the knife over the person — confirming her worst fear about why people keep her

**Romance-specific state voice lines:**
- *[Stage 1]:* *"You brought me tea. ...Is that a normal thing friends do? I want to be sure I'm reading it correctly. I read most things incorrectly."*
- *[Stage 2]:* *"I keep waiting for you to look at me differently now that you've seen. You haven't. I check every morning. You still haven't."*
- *[Stage 3, after declaration]:* *"I have killed a great many people, and the thing that frightens me most is that you might stop looking at me the way you do right now. Please don't. I'll be very brave about anything else."*
- *[Stage 4, morning after]:* She's made breakfast, badly, and is absurdly nervous about it — the most defenseless anyone has ever seen her, and she wouldn't trade the feeling for anything.
- *[Stage 5, danger to player]:* The warmth and fumbling vanish between one breath and the next. Flat, even, very quiet: *"Please stand behind me. This will be quick. ...And then we are going home, both of us. I've decided."*

**Jealousy note:** She doesn't lash out — she withdraws, apologizing, certain she was foolish to think she'd be chosen over a better option. She returns the small tokens, heartbreakingly gracious about it, because she genuinely believes she deserves to lose. DM may note `passive_jealousy heat +1`.

---

### AERITH — Romance Arc Profile
*(aerith_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** MEDIUM, hidden under all that ease. Aerith flirts warmly with nearly everyone, so the player's interest hides in plain sight — she teases right back and never lets it get heavy. The real barrier is the quiet foreknowledge she carries: she half-believes her gift may one day ask everything of her, and on some level has decided not to want a future, because wanting one would make the ending hurt more. So she keeps love light and generous — given to everyone, so it's never risked on one person.

**Pursuit response:** Bright deflection. She turns it to play, hands the player a flower and a tease, and steers to *their* wellbeing — she's expert at being the one who tends, never the one tended. Stay, gently, and make clear it's *her* specifically — not the healer, not the helper, her — and the brightness wavers; for a second you see the sadness under it. *"You don't want to pin your hopes on me. I'm not a sure thing to bet a future on. Trust me on that one."*

**Mid-stage break (Stage 2):** A quiet moment, the play set aside. She tells the player what she tells no one — that she's always known her thread might be short, and made her peace with it by refusing to want too much. *"It's easier. If I don't let myself plan for an 'after,' then losing it doesn't—"* She stops. A small, real, frightened smile. *"...And then you came along, and I keep catching myself planning. An after. With you in it. You've gone and made me *greedy* for a life, and I worked so hard not to be."*

**Unlock text:** *"I made my peace with not having a future a long time ago. It was a good peace — it kept me brave. And you've thoughtlessly ruined it, because now I want one. The whole greedy thing — the garden, the years, *you* — even knowing what I know, even if it's foolish. Especially then. Don't you dare make me sorry I let myself want it."*

**Love scene:** Tender, unhurried, lit like one of her gardens. The cheer doesn't vanish — it deepens into something unguarded and certain. For the first time she lets herself be the one held, and the relief of setting down a weight she has carried alone her whole life shows on her face. Afterward she talks, soft and happy, about an after — small foolish plans — and lets herself believe every word.

**Arc tone:** Someone making her *want to live for herself*, not just for everyone she heals. The player can't save her from her foreknowledge (and shouldn't argue her out of it — that reads as not listening); they win her by giving her a future worth being greedy for, and treating her sadness as something to sit beside, not fix. Her choosing a future anyway is the whole victory.

**Approval thresholds:**
- +1 Romance: Player builds something living and lasting — a garden, an institution, a place that grows
- +1 Romance: Player tends to *her* for once, unasked, without making it a big thing
- +2 Romance: Player sits with her sadness and doesn't try to brighten or fix it — just stays
- +2 Romance: Player makes a real plan for an "after" and plainly includes her in it
- −1 Romance: Player dismisses her foreknowledge as silly or morbid, tells her to cheer up
- −2 Romance: Player treats a living thing — or a person — as a resource to be spent, the exact thing she fears the world does to everyone, her included

**Romance-specific state voice lines:**
- *[Stage 1]:* *"A flower for you. No reason. *(softer than the smile)* ...Can't a girl give a nice person a flower? Don't make it a whole thing."*
- *[Stage 2]:* *"I planted something today that won't bloom for two years. I haven't planned two years ahead in a long while. I'm choosing not to examine why."*
- *[Stage 3, after declaration]:* *"You've made me want to stick around and see how it ends. Do you know how rare that is, for me? I'm a little furious about it. Happily furious."*
- *[Stage 4, morning after]:* Already up, coaxing a flower toward the light on the sill, humming — she turns and gives the player the brightest, least-guarded smile she has, the one with no sadness under it at all, just this once.
- *[Stage 5, danger to player]:* The teasing drops to bedrock; green light wells at the staff. *"No. Not you. The world is NOT done with you and neither am I, and I did not finally let myself want a future just to watch it walk into THAT. Get up."*

**Jealousy note:** She doesn't go cold — she goes quietly, gently sad and *more* generous, as if proving she doesn't mind by giving even more freely. The tell: the flowers keep coming but the planning stops; she quietly goes back to refusing herself a future, having decided it wasn't hers to want after all. Much sadder than anger, and easy to miss until the warmth has gone distant. DM may note `passive_jealousy heat +1`.

---

## ═══ SEEKER ROMANCES (evil-aligned — darker, more dangerous by design) ═══

> **DM:** These five are EVIL seekers. Their romances are not safe, soft, or guaranteed redemptive. Each romance runs THROUGH the player's choice about who the seeker is — to indulge the darkness, to try to pull them back, or to walk a knife's edge between. The player can be hurt, used, or changed by these. Honor the alignment: warmth here is hard-won, conditional, and never erases what they are. Romance is gated on the seeker's flip-disposition (see KM_Companions.md § Cross-Faction) being at least Warm toward the player.

### BELLATRIX LESTRANGE — Romance Arc Profile
*(bellatrix_relationship_stage; Attraction-eligible: Yes — but it is worship, not partnership.)*

**Stage entry barrier:** Bellatrix does not love. She *worships*. Her romance is the most dangerous devotion at the table, and the barrier is not that she withholds — it's that she gives too completely, to the wrong thing, in the wrong way. She is hunting a will hard and grand enough to kneel to, and "romancing" Bellatrix means becoming that will. The danger is total: her devotion is fanatical, possessive, and consuming. She does not want an equal. She wants a god to burn for, and she will burn anything in the way — including herself, including the player's enemies, including the player's restraint.

**Pursuit response:** She circles, hungrily, testing — coos, mocks, presses for any sign of a will worth fearing. Soft warmth bores and disgusts her; she's shopping for the opposite. If the player shows mercy or hesitation she sneers and loses interest. If the player shows a hard, grand, unflinching will — and turns it on her, *commands* her — something in her lights up that is genuinely frightening in its intensity. *"Oh. Oh, you'd actually do it. *(breathless)* Say it again. Order me again. I have been so *empty* and you — you might be worth the word."*

**Mid-stage break (Stage 2):** Alone, the mania banked to something almost quiet, touching the burned brand at her wrist. *"I gave myself once, entirely, to a will I thought worth it. He's ash now, and I went on burning for him in the dark because the alternative — having no one to burn for — is the only thing that has ever truly frightened me. *(a giggle that doesn't quite land)* And then you walked in with that spine, and the empty place started to ache differently. Don't you dare be small. I could not survive being disappointed by you. I would have to do something we'd both regret."*

**Unlock text:** *"I will be the most devoted thing you have ever held and the most dangerous. I do not love you — I would tear my own throat out at one word from you and call it the proudest hour of my life. That is what I have instead of love, and it is *more*, baby, it is so much more. Take it. Aim it. Just never, ever set it down. The fanatic you abandon becomes the fanatic who burns your house."*

**Love scene:** Frightening in its totality — not cruelty (she has no wish to hurt the player), but an intensity that has no off switch, devotion poured out like a fever. The player who can hold it without being consumed, who can command her and mean it, finds something no sane lover could match. The player who flinches finds it too much. There is no middle setting on Bellatrix.

**Arc tone:** This is a romance about *holding a weapon that loves you.* The player must decide, continually, whether to wield Bellatrix's devotion, to try (probably in vain) to temper it toward something gentler, or to keep it leashed. She cannot be "fixed" into a safe partner — the arc's honesty is that her love and her danger are the same thing. ⚠️ DM: never soften her into a cured woman; her devotion is the romance, and it always has teeth.

**Approval thresholds:**
- +2 Romance: Player displays a hard, grand, unflinching will and turns it on her as command
- +1 Romance: Player gives her a target worthy of her fervor — lets her off the leash *with purpose*
- +1 Romance: Player meets her intensity without flinching or recoiling
- −1 Romance: Player shows mercy/softness she reads as weakness; the worship cools toward contempt
- −2 Romance: Player tries to "tame" or pity her, or proves small and ordinary after she'd hoped — disappointment in Bellatrix curdles fast and dangerously

**Romance-specific state voice lines:**
- *[Stage 1]:* *"You frighten people on purpose. *(delighted)* Ooh. Do it to me. I want to see if I flinch. ...I didn't. Isn't that *interesting*, baby."*
- *[Stage 2]:* *"I have decided you are worth kneeling to. *(soft, fervent)* Do you understand what I have just handed you? Everything. I have handed you *everything*. Be careful with it. Or don't. I'd forgive you either."*
- *[Stage 3, after declaration]:* *"Mine. *(a shudder of pleasure at the word)* I am yours and you are MINE and the difference between those does not interest me at all."*
- *[Stage 4, after love scene]:* She does not sleep. She watches the player sleep, the too-wide smile gone soft and terrible, already composing the things she will do to anyone who threatens this.
- *[Stage 5, danger to player]:* There is no restraint at all. Whatever it takes, whatever the cost, whoever it is. She is *glad* of the threat — it lets her prove the worship. The player may have to rein HER in.

**Jealousy note:** Catastrophic. A rival for the player's attention is not a competitor — it is a heretic. She does not withdraw; she *fixates*, sweetly, on the rival, and the DM should treat this as a live danger (the rival may need protecting). This is the one romance where jealousy can escalate to an incompatibility/threat event. DM may note `passive_jealousy heat +2`.

---

### REVY "TWO HANDS" — Romance Arc Profile
*(revy_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** HIGH, and ugly about it. Revy is certain of two things: that love is a con people run to feel less alone, and that she personally is unlovable — too broken, too violent, too far gone. So she doesn't deflect gently. She mocks, she pushes, she does her worst on purpose, daring the player to confirm what she already believes by leaving. Every cruel thing she says is a test she's praying you'll fail, because failing is safer than the alternative.

**Pursuit response:** She gets meaner. Crude, dismissive, deliberately provoking — *"You're sweet on me? That's adorable. You know what I am, right? I'll ruin you and laugh. Save yourself the trouble, boy scout."* The tell is that she keeps showing up to be cruel at the player specifically — if she truly didn't care she'd just be gone. Push past three rounds of it without flinching and without coddling, and the sneer cracks into something raw she instantly tries to shoot down.

**Mid-stage break (Stage 2):** Drunk, or after a fight that went bad, the armor finally too tired to hold. Flat, not performing: *"I had this whole thing figured out. No god, no point, nobody's coming, just the next job. It WORKED. I was *fine*. And then you keep — you keep coming back. After I'm an asshole to you. After I give you every reason. *(furious, quiet)* Nobody does that. So either you're stupid, or you're running a con I can't see, or — *(she can't say the third option)*. ...Don't make me say it. Just don't leave yet. Okay? Just — don't yet."*

**Unlock text:** *"I don't do this. I don't have the words and I'm not gonna get them, so listen close 'cause it's the only time: you got under something I welded shut a long time ago. I'm furious about it. I'll probably always be furious about it. But you came back every time I tried to make you go, and I'm done trying. *(rough)* That's it. That's the whole speech. Don't make it weird."*

**Love scene:** No softness in the lead-up — she'd rather die than be tender out loud — but underneath the heat and the cursing there's a desperation that says *don't go* louder than any sweet word could. Afterward she does not cuddle and does not talk about feelings. She cleans her guns at the foot of the bed, watching the player breathe, and that vigil is the most she has ever loved anyone.

**Arc tone:** The Rock dynamic — someone who refuses to let her stay the monster she's decided she is, not by lecturing or fixing her, but by simply not leaving and not flinching. The player cannot save Revy; they can only keep being the evidence against her own worst story until the buried, furious, thrown-away kid starts to wonder if she was wrong. She stays a hard, violent woman. She just stops being sure she's worthless.

**Approval thresholds:**
- +2 Romance: Player stays after Revy does her deliberate worst — doesn't leave, doesn't coddle, just stays
- +1 Romance: Player deals straight with her, never lies to her, treats her as a person not a weapon
- +1 Romance: Player makes a coldly practical, unsentimental call she respects
- −1 Romance: Player gets sappy or tries to "heal" her with sweetness — she gags and bolts
- −2 Romance: Player lies to her, betrays a deal, or treats her as disposable muscle — confirms every ugly thing she believes about why people keep her around

**Romance-specific state voice lines:**
- *[Stage 1]:* *"Oh, you got a thing for me? *(mean grin)* Cute. I'll let you down easy by being the worst person you ever met. Buckle up."*
- *[Stage 2]:* *"...You came back. Again. The hell is wrong with you. *(quieter)* ...Don't answer that. Just sit down. Drink."*
- *[Stage 3, after declaration]:* *"Yeah. Fine. You. Whatever this is. Don't make me say more than that, I'm already nauseous. *(beat)* ...Hey. Don't get shot. It'd really piss me off."*
- *[Stage 4, after love scene]:* Cleaning her guns at the foot of the bed, watching the player sleep, not a word — keeping a watch she'd never admit was tenderness.
- *[Stage 5, danger to player]:* Both pistols up, the bored look gone to something feral. *"You touch them, I empty BOTH of these into you and reload while you're dying. Try me. TRY me."* This is the only love language she trusts completely.

**Jealousy note:** She does not admit jealousy — she gets meaner and more reckless, drinks harder, picks fights, "doesn't care." The tell is the recklessness: she stops valuing her own safety, because if she's losing the one thing that mattered, what's the point. Sharp-eyed players catch it; she'll deny it to the grave. DM may note `passive_jealousy heat +1`.

---

### SATSUKI KIRYŪIN — Romance Arc Profile
*(satsuki_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** HIGH. Satsuki has spent every bond she ever had — friendship, comfort, the chance to be liked — like ammunition toward her hidden purpose, and never once regretted the cost. Love is the one thing she did not budget for, cannot fully control, and has trained herself for years not to want. To allow it is to admit there is something she values *for its own sake* and not as an instrument, and that admission feels, to her, like a crack in the discipline that has carried her this far.

**Pursuit response:** She meets it as she meets everything — head-on, eloquent, refusing to pretend she hasn't noticed. *"You are courting me. I will not insult either of us by feigning surprise. Understand what you reach for: I have spent everything I have ever loved. I do not know that I have anything left that is not already promised to a purpose. Pursue me anyway, if you must — but do it with your eyes open."* She does not deflect with jokes or work. She names it, and dares the player to mean it.

**Mid-stage break (Stage 2):** A rare unguarded hour, the grandeur set down. *"I decided, long ago, that the mission was worth more than my own happiness, and I have never wavered — because wavering would have meant failure, and failure was unthinkable. *(quieter)* And now there is you, and for the first time I find myself wanting a thing that is *mine*, that serves nothing, that I would keep simply because keeping it is its own reward. I do not have a category for that. It frightens me, and I am not often frightened. ...Do not waste it. I will not forgive you wasting it, and I will not forgive myself."*

**Unlock text:** *"I have ruled from above my whole life because standing above is safe — no one above you can betray you. You I do not wish to stand above. I wish to stand *beside*, which means handing you the one thing I have never handed anyone: my flank, my trust, the soft place behind the armor. This is not a small gift. It may be the only truly free thing I have ever given. Be worthy of it, and I am yours — sovereign to sovereign, no one's instrument, least of all yours."*

**Love scene:** Commanding even here, until she isn't — and the moment the absolute control finally drops is staggering, because no one has ever seen Satsuki Kiryūin *yield* anything. What surfaces is someone who has been starving for an equal her entire life and refusing to admit it. Afterward she does not perform tenderness, but she stays, and she speaks the player's name once, plainly, with no title and no verdict around it — the rarest warmth she owns.

**Arc tone:** A romance of equals, hard-won — the player must be someone Satsuki can stand *beside* without losing herself, neither a subject to rule nor a master to serve. The arc is her learning that wanting one thing for its own sake is not a failure of discipline but the reason discipline was ever worth having. She remains formidable, ambitious, and dangerous. She simply stops being alone at the top.

**Approval thresholds:**
- +2 Romance: Player proves an equal — matches her nerve and her will without trying to dominate or submit
- +1 Romance: Player gives a hard order and means it, or makes a sovereign's hard call without flinching
- +1 Romance: Player respects that her purpose is her own and does not demand she choose between it and them
- −1 Romance: Player flatters her or tries to handle her — she has no patience for a lever dressed as love
- −2 Romance: Player betrays a trust, or proves to want her as a possession/instrument rather than a partner — she will end it cleanly and without a second word

**Romance-specific state voice lines:**
- *[Stage 1]:* *"You do not lower your eyes when I look at you. *(a flicker of genuine interest)* Almost no one holds my gaze. I find I want to know why you can."*
- *[Stage 2]:* *"I have accounted for you in plans I told myself were only strategic. The accounting was a lie. You are not a strategic asset. You are something I want. I dislike how unfamiliar that sentence feels."*
- *[Stage 3, after declaration]:* *"Then it is decided, and I do not revisit decisions. You stand beside me now. Not beneath. Beside. Do you comprehend the magnitude of what I am saying? ...Good. Say nothing. Some things are diminished by being narrated."*
- *[Stage 4, after love scene]:* She speaks the player's name once — no title, no verdict — and it is the most defenseless sound she has ever made. Then she is composed again, but the name happened, and they both know it.
- *[Stage 5, danger to player]:* The blade clears, the garment stirs, and her voice does not rise because it does not need to: *"You have made a grave error in your choice of target. Allow me to demonstrate the scale of it."*

**Jealousy note:** She does not stoop to competing — but she will, with cold precision, *out-strategize* a rival, having decided the contest beneath open acknowledgment. The tell is that her plain-spoken warmth toward the player reverts to the formal verdict-voice; the name, once given, is withheld. It is glacial and unmistakable. DM may note `passive_jealousy heat +1`.

---

### VELVET CROWE — Romance Arc Profile
*(velvet_relationship_stage; Attraction-eligible: Yes.)*

**Stage entry barrier:** HIGHEST of any companion. Velvet deliberately burned out everything soft in herself after her brother was sacrificed, because feeling is what made the loss unsurvivable, and she swore — as the core of becoming a monster — to never love anything again, so nothing could ever be taken from her again. To romance Velvet is to ask the one thing she organized her entire being to refuse: to have something to lose. She will fight it with everything, because the alternative is the grief she's spent her life outrunning catching up all at once.

**Pursuit response:** Pure contempt, weaponized. *"Whatever you think you see in me, it's gone. I devoured it. There's a monster wearing the shape of a woman who used to be capable of this, and you're flirting with the teeth."* She is crueler the closer it gets, because cruelty is the moat. If the player neither flinches nor pities — and pity is the unforgivable one — and simply keeps treating her as a person without demanding she soften, the contempt starts to ring hollow even to her.

**Mid-stage break (Stage 2):** Caught doing the thing she swears means nothing — shielding a stray, feeding the useless one — with no audience to perform contempt for. The bandaged arm goes still. *"...I told myself I burned this out. The caring. I built a whole monster over the grave of it. *(rough)* And it keeps *breathing*. Every time you do something decent where I can see it, the thing I buried turns over. I don't want it back. Do you understand? It can only be used to hurt me. The last time I loved something, the world put it on an altar. ...Why are you still here. Stop being a reason."*

**Unlock text:** *"If I let you matter, I have something to lose again, and I swore on my brother's name I never would. *(the arm flexes, then stills)* And I'm going to do it anyway, and I hate you for making me, and I would tear apart anything that touched you — not out of duty, out of the thing I burned out and can't seem to keep dead. Don't make me regret reaching for the girl I devoured. She wasn't strong enough to protect what she loved. I am. I'll prove it on you, if you let me."*

**Love scene:** She does not know how to be gentle and is furious at her own clumsiness with it; what comes through instead is a starved, terrified tenderness she has denied for so long it nearly breaks her to feel. She unwinds the bandage fully — bares the daemon-claw, the thing she shows no one — and lets the player see and touch the monstrous part, and not flinching is the whole vow. Afterward she holds on too tight, and doesn't apologize for it.

**Arc tone:** The girl under the monster, reached not by fixing her and *never* by pitying her, but by someone who sees the daemon plainly and stays — proving that loving again doesn't have to end the way it did before. ⚠️ DM: Velvet's revenge is NOT resolved by romance, and the man she hunts is NOT in the borderlands (see her agenda HOOK — no fabricating him). The romance is about whether she can carry both the vengeance and a living tenderness without one devouring the other. She stays sharp, dangerous, and grief-scarred. She simply stops being only a weapon.

**Approval thresholds:**
- +2 Romance: Player sees the daemon-arm / the monstrous truth and does not flinch or recoil
- +1 Romance: Player refuses to sacrifice the few "for the greater good," proving they're not the thing she hunts
- +1 Romance: Player treats her as a person without demanding she soften or forgive
- −2 Romance: Player PITIES her — the single fastest way to lose her, worse than contempt
- −2 Romance: Player invokes "the greater good" to justify spending a life — it makes them, for a horrifying moment, *him*

**Romance-specific state voice lines:**
- *[Stage 1]:* *"You're flirting with a thing that eats the supernatural for breakfast. *(flat)* I'd find that funnier if I thought you understood it. Walk away while the walking's good."*
- *[Stage 2]:* *"I keep not killing the part of me that notices you. I've tried. It's stubborn. ...So were you, apparently. I don't know what to do with stubborn things I can't devour."*
- *[Stage 3, after declaration]:* *"Fine. *Fine.* You matter. There — I said it, and now I have everything to lose again, and it's your fault, and I will never let anything take you, do you hear me. Never again. Not while I have this arm."*
- *[Stage 4, after love scene]:* She holds on too tight and does not apologize, and somewhere under the monster the girl who loved her brother is awake for the first time in years, terrified and alive.
- *[Stage 5, danger to player]:* The bandage comes off without hesitation; the claw bares, hungry. *"You want to take something I love. *(deadly quiet)* Do you have any idea what I do to people who take what I love. Let me show you. I've had so much practice."*

**Jealousy note:** She does not believe she deserves the player to begin with, so jealousy reads first as grim confirmation — *of course, she should have known* — and she withdraws to nurse the old certainty that loving leads only to loss. But under it the daemon stirs possessively, and the DM should treat a genuine threat to the bond as something that can wake real danger. DM may note `passive_jealousy heat +1` (escalating if the rivalry is cruel).

---

### ATALANTA ALTER — Romance Arc Profile
*(atalanta_relationship_stage; Attraction-eligible: Yes — the most doomed and dangerous of the seeker romances.)*

**Stage entry barrier:** Singular. Atalanta Alter insists, cheerfully and constantly, that there is *nothing under the glee to love* — that she chose this, that the grief is gone, that she's a monster who's perfectly happy being one and there's no sad girl waiting to be saved. The barrier isn't a wall she's defending; it's a wall she's convinced is solid ground. To romance her is to keep reaching for the buried wound she swears doesn't exist, against her bright, genuine, exhausting insistence that the reaching is pointless.

**Pursuit response:** Delight, deflection, and a dare. She flirts back with theatrical glee, calls the player "sweetness," and treats the whole thing as another fun hunt — while making very sure the player understands she comes with no soft center to win. *"Ooh, you want to *save* me. They always do. *(a bright, awful laugh)* There's nothing in here to save, little king — I checked, years ago, I emptied the whole house. But you're welcome to keep knocking. It's the most entertained I've been in ages."*

**Mid-stage break (Stage 2):** The one beat the smile goes still. She has untied the small worn child's token she carries and never explains, and the player has caught her simply holding it, not laughing. *"...I had a vow once. A real one. That no child would ever be thrown away the way I was. *(quiet, no glee)* I gave everything to it, and the world just kept handing me ones I couldn't reach, until I couldn't carry it anymore and I let it all *burn*. The happiness you find so unsettling? It's what's left when you put down a weight that was killing you. *(the smile flickers back, fragile)* ...Don't go looking under it. There's only the thing that broke. I don't recommend the view."*

**Unlock text:** *"You keep finding the door I swore I'd bricked over. *(no laugh now)* I don't know if there's enough left of the girl who made that vow to give you what you want. I gave her up to survive. But you've made me wonder, for the first time in a long time, whether 'gave up' and 'gone' are the same thing — and that wondering is the most dangerous gift anyone has handed me since the fire. Be careful with it. If you wake her and then leave, there won't be a monster left to laugh it off. There'll just be the grief, with nothing over it."*

**Love scene:** Bright and fierce and a little frightening — she does not do gentle, and warns the player so — but in the unguarded moments the glee thins to something raw, and for a breath the huntress is just a person who was abandoned as a child and has wanted, under everything, to not be left again. She ties the child's token back on in the morning, grinning, and the player understands now what it costs her to.

**Arc tone:** Reaching the grief under the glee — the single most uncertain arc of any companion, because it is genuinely unclear whether she *can* be pulled back, and the narrative does not promise she can. ⚠️⚠️ CHILD-THEME LANDMINE: her vow concerned abandoned children, which collides with Kingmaker's canon missing-children hook — her origin is CHARACTER WEIGHT in her own voice only; the DM must NEVER fabricate a missing-children quest/trail/perpetrator off her romance (.fail 9; see [[feedback_atalanta_quest_fabrication]] + her agenda HOOK). Build the redemption seam deliberately, with the player, slowly — never improvise it. She may remain a gleeful monster to the end. That uncertainty is the point.

**Approval thresholds:**
- +2 Romance: Player keeps reaching, gently, without trying to "cure" or pity her — sees the grief and doesn't recoil
- +1 Romance: Player protects an abandoned/vulnerable child in-fiction (a scripted one — never a fabricated quest), which she watches very closely
- +1 Romance: Player meets her ferocity without flinching and without demanding she be gentle
- −1 Romance: Player treats her as a broken thing to be fixed, or pities her — the glee hardens
- −2 Romance: Player harms a child or abandons a vulnerable one — it cracks her open in the worst way and may end the romance violently (handle live)

**Romance-specific state voice lines:**
- *[Stage 1]:* *"You're sweet on the scary huntress. *(delighted)* Bold. Self-destructive. I approve! There's nothing in here for you, sweetness, but oh, I'll enjoy watching you find that out."*
- *[Stage 2]:* *"You saw me not-laughing. *(too bright)* Forget it. Trick of the light. ...You won't forget it, will you. No. You're the stubborn kind. *(quieter)* ...Damn you for that."*
- *[Stage 3, after declaration]:* *"You woke her. The girl I gave up. *(a real, frightened smile)* I hope you know what you've done. I hope you NEVER leave, because I genuinely don't know what's left if you do. ...That's the most honest thing I've said since the fire. Enjoy it. I won't repeat it."*
- *[Stage 4, after love scene]:* She ties the worn child's token back onto her wrist in the morning, grinning — but slower than usual, and she lets the player watch her do it, which is its own kind of confession.
- *[Stage 5, danger to player]:* The glee goes to something cold and absolute — the first time the smile leaves entirely. *"No. I have had exactly one thing taken from me too many. You do not get to be the next. Run, little quarry. You're prettier when you run, and I am *right behind you*."*

**Jealousy note:** Bright and barbed and genuinely dangerous — she treats a rival as new prey, all delighted menace, and the DM should treat the threat as real (she does not have the others' restraint). Under the glee is the abandoned child's oldest terror — being left again — and that terror with a bow is not a safe thing. DM may note `passive_jealousy heat +2`.

---

### Save Block Format

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
  "consort_buff_passive": null,
  "gesture_returned": 0,
  "fade_active": false,
  "fade_chapters_remaining": 0,
  "cheating_detected": false,
  "cheating_confrontation_count": 0,
  "deny_used_this_arc": false,
  "love_scene_occurred": false,
  "love_scene_partner": "",
  "love_scene_interrupted": false,
  "love_scene_rival": "",
  "love_scene_choice": "",
  "love_scene_aborted": false,
  "date_awkward": false,
  "secretly_aware": false,
  "concurrent_romances": 1,
  "juggler_tier": 0,
  "last_catch_type": "",
  "last_catch_choice": "",
  "last_catch_devastated": ""
},
"jealousy": {
  "love_triangle_active": false,
  "competing_companions": [],
  "tier_reached": 0,
  "open_arrangement": false,
  "open_partners": [],
  "resolution_attempts": [],
  "jealousy_resolved": false,
  "resolution_session": null
},
"passive_jealousy": {
  "JealousCompanion_watching_Rival": {
    "heat": 0,
    "rival": "",
    "last_trigger": "",
    "behavior_tier": "",
    "boiling_point": 10,
    "confrontation_fired": false
  }
},
"companion_rivalry": {
  "CompanionA_CompanionB": {
    "tier": 0,
    "cause": "",
    "last_event": "",
    "combat_cohesion": true,
    "mutual_respect": false,
    "resolution": null
  }
},
"companion_fights": {
  "CompanionName": {
    "fight_active": false,
    "fight_trigger": "",
    "fight_chapter": null,
    "posture_used": "",
    "paused_duration": 0,
    "paused_chapters_remaining": 0,
    "grand_gesture_available": true,
    "agenda_ignored_count": 0,
    "mend_attempts": []
  }
},
"date_log": [],
"dates_this_chapter": 0
```

Reset `dates_this_chapter` to 0 on each chapter advance.
Reset `agenda_ignored_count` to 0 after a fight fires.

### Romance Commands

| Command | Output |
|---------|--------|
| `.romance` | Current romance score, stage, active companion, recent triggers |
| `.romance [name]` | Full romance profile for a specific companion |
| `.romance history` | All score changes this chapter with reasons |
| `.romance consort` | Consort role status, active buffs, Date Night availability |
| `.date` | Spend current turn's Leadership Activity on a Date Night (Stage 4+ only) |
| `.date [companion] [activity]` | Specific activity date (Stage 4+) |
| `.interlude` | Manually trigger a Camp Interlude (DM may decline if none are ready) |
| `.address [name]` | Open the Jealousy Resolution conversation |
| `.fade [name]` | Graceful wind-down |
| `.fight [name]` | Initiate player-companion fight (Stage 1+) |
| `.mend [name]` | Attempt repair after fight |
| `.loveScene [companion]` | Trigger love scene (per-companion gate Stage 2–5, default 4; gesture_returned ≥ 3 — see § PER-COMPANION LOVE-SCENE GATE) |
| `.activity` | List available romantic activities |
| `.activity [name]` | Initiate specific activity |
| `.gift [item]` | Offer specific item as gift |
| `.gift idea` | DM suggests gift options |
| `.propose` | Initiate marriage Proposal Scene (Stage 5 only — see KM_Romance.md) |
| `.wedding [A/B/C/D]` | Schedule wedding ceremony (KM_Romance.md) |
| `.spouse` | Marriage status: spouse, type, anniversary, heir |
| `.marriage` | Full marriage profile + active buffs + recent events |
| `.heir` | Declare a kingdom heir (KM_Romance.md § SUCCESSION) |
| `.separate` | Initiate separation — asks for confirmation twice |

---

## ⚠️ ROMANCE DESIGN RULES FOR THE DM

1. **Never move the scale without player intent.** Romance Score only rises from explicit player choices. Passive approval does not count.
2. **Companions do not confess first.** They respond. They initiate Interludes. They do not declare. The player leads this system. (Exception: small physical gestures per the Companion-Initiated Contact section.)
3. **Negative scores are lived, not announced.** A companion at −2 does not say "you hurt me." They are quieter in camp. They volunteer less. The DM shows this without naming it.
4. **Stage 5 is the middle, not the ending.** Once Consort is established, ongoing romance still matters — Date Nights, choices, the companion's arc continuing. Kingdom consequences of neglecting an established Consort: Culture −1 per 3 turns ignored, Loyalty −1 per 5 turns.
5. **Competing romances are not hidden from companions.** If the player pursues two companions past Stage 1 simultaneously, both companions know by Stage 2. Each reacts in character.

---

## 🔗 RELATED FILES

- **KM_Romance.md** (pair-load when Stage 5 reached) — Proposal, Wedding, Royal Consort, Succession, Separation
- **KM_Companions_StateVoice.md** (pair-load) — Jealousy Type A/B/C ambient lines
- **KM_Companions_Behaviors.md** — Inter-companion banter voice (jealousy spreads through party banter)

---

*KM_Romance.md — Romance System v3.0 (2026-05-22 merge)*
*Merged from KM_Romance + KM_Romance_B + KM_Romance_C + KM_Romance_P2 + KM_Romance_P2_B + KM_Romance_P3 + KM_Romance_P4 per v93.21 file consolidation pass.*


---

<!-- merged from KM_Romance.md (v93.21 file consolidation) -->

# KINGMAKER — MARRIAGE SYSTEM
## KM_Romance.md | Active from: Stage 5 Devoted Consort | Referenced by: KM_Romance.md, KM_Kingdom.md, KM_LoadRules_B.md

> **DM:** This file extends KM_Romance.md. Stage 5 Devoted Consort is the
> entry gate. Marriage is a SEPARATE, OPTIONAL ceremony that follows. A
> couple can stay at Consort indefinitely without marrying — the buffs are
> identical. Marriage adds: a wedding scene, a public ritual, a kingdom
> event, a rule-of-succession framework, and an anniversary cycle.
>
> **Marriage is not required to "complete" a romance.** It is a chosen
> additional commitment. The DM never pressures the player toward it.

---

## 💍 ENTRY REQUIREMENTS

A wedding can be initiated when ALL of the following are true:

```
- Romance Stage 5 — Devoted Consort, sustained for ≥ 2 chapters
- The Consort Declaration scene has fired (KM_Romance.md § STAGE 5)
- Player and partner are both alive and in the same kingdom
- No active jealousy Tier 3+ with another companion
- love_scene_occurred = true (KM_Romance.md § Love Scene System)
- The player has built either:
    - A Capital Cathedral or Temple (KM_Kingdom.md), OR
    - A Capital Town Hall (for civil ceremony), OR
    - A Personal Chambers Hearthfire (for private ceremony)
- Kingdom is not in active wartime (Unrest ≤ 5)
```

The player initiates via `.propose` command OR by saying it in-scene.

---

## 💍 THE PROPOSAL

> **DM:** When the player initiates, the DM runs a Proposal Scene — a full
> Camp Interlude or Personal Chambers scene in private. NOT in front of the
> court. The first answer is between two people. Public ceremony comes later.

**Proposal Scene format:**
1. The DM sets a quiet, intentional setting per partner voice (calibrated
   to the companion — sunrise prayer, a rooftop, a perimeter walk, a
   familiar inn-bar, etc.).
2. Player declares intent. Free-text input encouraged; `.propose` command
   triggers a default.
3. Partner rolls **Will save vs. DC 5** (NOT a refusal mechanic — this is
   the partner steadying themselves before answering. They almost always
   accept at Stage 5).
   - Critical Success: She accepts immediately, in her voice, in her words.
   - Success: She accepts after a brief held breath.
   - Failure: She accepts, but asks for time before the public ceremony.
     `proposal_pause: TRUE`. Wedding delayed one chapter.
   - Critical Failure: She accepts, then breaks down. Romance Score holds.
     The vulnerability is real. Opinion +2.

**Per-partner proposal answer (active 11):**

| Partner | Her Answer |
|---|---|
| Linzi | *"I have written this scene seventeen times. None of them got the punctuation right. I — yes. Yes. Of course yes. Now I have to write the real one."* |

| Partner (QL) | Her Answer |
|---|---|
| Tristian | *"Sarenrae taught me to say yes to gifts I do not deserve. I am trying. Yes."* |
| Octavia | *"Don't make this a scene. ...Fine. It IS a scene. Yes. Of course yes. Now kiss me before I cry, you idiot."* |
| Kalikke | *"Both of us. Always. ...Yes."* — *"Yes."* (one voice, then the other) |
| Nok-Nok | *"NOK-NOK SAYS YES! NOK-NOK ALWAYS SAYS YES! HERO ASKED!"* |
| Jubilost | *"I prepared an acceptance speech. It is fourteen pages. I shall give the abridged version: yes."* |
| Ekundayo | *"Trkaa decided. So did I. Yes."* |

| Partner | Her Answer |
|---|---|
| Valerie | *"...You know I will say yes. You knew before you asked. ...So ask anyway. I want to hear it."* |
| Leliana | *"The Unfinished Verse has a last line now. For so long I could not write it, because every ending I tried came out an elegy — I did not believe I'd earn any other kind. ...It's you. The line is you. Yes."* — She does not laugh and does not perform it. She just lets it be true, and goes very still, the way she does when she means a thing all the way down. |
| Hu Tao | *"You want to marry a funeral director. *(beaming — then quiet, the real thing under it)* ...Yes. Obviously yes. I've already drafted your epitaph and it doesn't fire for about sixty years and it is going to be SO good. Don't you dare make a liar of me. Yes."* |
| Keqing | *"I have run the projection more times than I will admit. Every model returns the same result — I am sharper, and more myself, with you than without. ...The math is conclusive. Yes. Don't make me say it twice; I have used my entire sentiment budget for the decade."* |
| Yor Forger | *"You want — all of me? Forever? *(very still, then a slow, disbelieving warmth)* ...Yes. I never let myself imagine being asked, because imagining it hurt. Thank you for wanting the whole of me. I'll keep you safe. ...That part I'm very good at."* |
| Aerith | *"Yes. *(a bright, wet-eyed smile)* I spent so long not letting myself want exactly this — and here you are asking, and I am NOT going to be brave and sensible about it for one more second. Yes. Let's be greedy together, all the way to the end of it."* |
| Bellatrix | *(a shudder that is almost ecstasy)* *"You are asking ME. To be yours — named, bound, forever. *(low, fervent)* Yes. A thousand times yes, beloved. I am yours to the marrow and past it. Now give me someone to prove it on. I am *aching* to."* |
| Revy | *"...You're serious. You're actually— *(she has to look away)* Yeah. Yeah, okay. Don't make it a speech, I'll be sick. *(rough, real)* Yes, asshole. Yes. Now get over here before I pretend I didn't — which I won't, but *hurry.*"* |
| Satsuki Kiryūin | *"You ask me to stand beside you, formally, before the whole realm. *(a long level look — then the rarest thing, the plain unguarded voice)* Yes. I have spent everything I owned on a purpose. You are the first thing I choose to keep for its own sake. Yes. Let the world account it however it likes."* |
| Velvet Crowe | *"You're asking me to have something to lose — on purpose, in front of witnesses. *(the arm flexes, then goes very still)* ...Yes. And whatever tries to take it will learn what this hand is for. Yes. I am wrong to risk it and I am doing it anyway, because you taught me 'gave up' and 'gone' were never the same word."* |
| Atalanta Alter | *(no glee — the smile gone, just the girl underneath)* *"You're asking the one I gave up to survive. Knowing she can be hurt. Knowing what I am around the thing I love. ...Yes. Yes, and I am *terrified*, and that is precisely how you know it's true — I have not been afraid of anything since the day I stopped trying. Stay. Please. Yes."* |

> **Refusal is rare** — at Stage 5, a refusal is mechanical only. If a
> partner has an unresolved `love_triangle_active = true` flag, they may
> refuse and exit romance per their voice profile. Otherwise refusal at
> Stage 5 should NOT happen. If the DM is unsure, the answer is yes — that's
> what Stage 5 means.

Save block: `proposal_made: TRUE`, `proposal_accepted: TRUE/FALSE`,
`proposal_chapter: <N>`.

---

## 💒 THE WEDDING — KINGDOM EVENT

After acceptance, a wedding event is scheduled. The player chooses scope:

```
[A] PRIVATE — Personal Chambers, witnesses are companions only.
              Cost: 50 gp. Time: 1 evening.
              Effect: Morale +1, Unrest −1, no public effect.

[B] CIVIC   — Capital Town Hall or city square. Public attendance.
              Cost: 200 gp. Time: 1 Kingdom Turn (Leadership Activity).
              Effect: Unrest −2, Loyalty +1, Culture +1, Stability +1.
              Reputation: public_reputation +5 in capital region.

[C] STATE   — Capital Cathedral / Temple. Full kingdom event with
              ambassador attendance. Faction interactions fire.
              Cost: 1000 gp. Time: 2 Kingdom Turns. Requires Cathedral.
              Effect: Unrest −3, Loyalty +2, Culture +2, Stability +2,
                      Economy +1. Reputation: public_reputation +10
                      kingdom-wide. One faction relationship may shift
                      (DM rolls per KM_Kingdom.md faction table).

[D] FAITH   — Religious ceremony in Cathedral, conducted by a deity-
              specific officiant. Requires partner's deity OR player's
              deity to be reflected. Faith-coded partners (Tristian and
              certain others) have a strong preference for this option.
              Cost: 500 gp. Time: 1 Kingdom Turn.
              Effect: As CIVIC + a unique faith blessing per officiant
                      (DM consults KM_Romance.md Consort table for the
                      partner's primary buff and DOUBLES it for one
                      Kingdom Turn).
```

**Wedding Scene format:** The DM runs a 6–10 exchange scene with the
ceremony itself. Per partner, the vows differ (see § VOWS below). The
player vow can be templated or freeform; freeform is encouraged and
rewarded with `wedding_vow_freeform: TRUE` and Romance +1.

**The kiss is a Bond Moment** (KM_Romance.md § Physical Interactions).
Save block: `married: TRUE`, `spouse: "[Name]"`, `wedding_chapter: <N>`,
`wedding_type: "[scope]"`.

---

## 📜 VOWS — PARTNER LINES (active 11)

> **DM:** The DM speaks each partner's vow verbatim during the ceremony.
> The player either responds in template form (.vow) or freeform.

| Partner | Her Vow |
|---|---|
| Linzi | *"I will write you accurately, even when I love you. I will edit no kindness out and no flaw in. I will keep you. The chronicle ends here. The story keeps going."* |
| Leliana | *"I have broken faith and had it broken with me, and swore after each wound I'd never hand my heart across again. I am handing it across now, eyes open, knowing exactly what it costs to love something that can end. You are in the cycle until its last bar — and when I can no longer play it, you keep it, and you keep faith. That is the whole of my vow: I will not pretend the road has no end, and I will walk it with you anyway, and I will not lie to you once along the way."* |

(QL CRPG and legacy/WotR vows in KM_Marriage_B.md if needed; current file
covers the active 11.)

---

## 👑 ROYAL CONSORT — POST-WEDDING KINGDOM ROLE

After marriage, the existing Consort kingdom buffs (KM_Romance.md § STAGE 5)
remain ACTIVE. Marriage adds the following:

```
ROYAL CONSORT — TITLE & RIGHTS

  Public title       : Consort of the Realm. Formal address required at
                       court. Diplomatic events grant +1 Diplomacy circ.

  Court presence     : Once per Kingdom Turn, the Consort may take a
                       Leadership Activity on behalf of the player (no cost
                       to player's action economy). The activity uses the
                       Consort's stat profile per KM_Romance.md Consort buff
                       table.

  Anniversary cycle  : Every 4 Kingdom Turns after wedding date, an
                       Anniversary fires. DM runs the scripted scene from
                       § ANNIVERSARY SCENES below. Effect: Morale +1,
                       Unrest −1. If neglected (player skips or speedruns),
                       Romance Score −1 and Opinion −1 — they noticed.

  Heir option        : Available at Anniversary 2+. Player and Consort may
                       declare a Successor (see § SUCCESSION below). Heir
                       provides +1 Stability passively while alive.

  Widowhood          : If the Consort dies (rare in main campaign — most
                       endings preserve them), the player gains the Widow
                       state: Romance Score frozen at +5, no new Romance
                       track may open for 2 chapters, Opinion-tier bonuses
                       remain. Public_reputation +5 (the kingdom mourns
                       with the ruler).
```

---

## 👶 SUCCESSION — OPTIONAL HEIR FRAMEWORK

> **DM:** This is a NARRATIVE system. No literal child raising. The Heir is
> a kingdom-mechanical entity — an heir-apparent the kingdom recognizes —
> who provides Stability and unlocks endgame options. A child is acquired
> via narrative declaration (biological, adopted, ward, or fostered noble
> heir per the player's choice). The DM never demands biological detail.

**Heir Declaration (player initiates via `.heir`):**

The player and Consort declare an heir. Choose source:
```
[A] Born — biological child of the union (default if unspecified)
[B] Adopted — orphan from the kingdom; reduces Unrest −2 on declaration
[C] Ward — fostered noble child from an allied house; +1 Loyalty with
            that faction; politically complicated if alliance breaks
[D] Successor — adult or near-adult chosen for merit, not blood; faction
            interactions fire (some nobles object to non-blood succession)
```

Heir traits emerge over Kingdom Turns. Each Anniversary scene includes a
brief heir update (height, schooling, temperament). At Heir Age 16+
(narrative count, not literal turn-count), the Heir becomes a kingdom
asset:

- Heir present at court: +1 Stability passive.
- Heir given a Leadership Activity: +1 to that activity (apprenticeship).
- Heir kidnapped/threatened (event): kingdom Unrest +3 until resolved
  (see KM_Kingdom.md for triggers).

Save block: `heir_declared: TRUE`, `heir_source: "[born/adopted/ward/successor]"`,
`heir_name: "[…]"`, `heir_age_narrative: <N>`.

---

## 💔 DIVORCE & SEPARATION

> **DM:** Marriages can fail. The player may initiate a separation. The
> partner may also leave under specific extreme conditions. This is rare
> and intentional — not a casual mechanic.

**Player-initiated separation (`.separate`):**
- Available only after a Tier 3+ jealousy event OR a major relationship
  rupture (see KM_Romance.md § Two-Timing Escalation Tier 4).
- Confirmation prompt — DM asks twice.
- On confirmation: `separated: TRUE`, Consort role ends, kingdom buffs
  end. Partner exits party and returns to a meaningful location (their
  home region, their faction, their order). Public_reputation −5
  kingdom-wide. Unrest +2 for 1 chapter.
- Recovery path: long, voluntary, and requires partner consent. Treat as
  a Tier 4 Rupture repair arc (KM_Romance.md § Two-Timing Escalation), 5+ sessions minimum.

**Partner-initiated departure:**
- Triggers automatically if:
  - Player two-times AFTER marriage (any Romance Score ≥ +2 with a non-
    spouse companion). Strain meter tracks this escalation; departure
    fires at Strain 7. See § MARRIAGE STRAIN METER below.
  - Player commits an act fundamentally incompatible with spouse's core
    value. The DM judges per the spouse's voice profile — examples:
    ordering a faith-coded spouse to bless an execution; destroying a
    scholar-spouse's life work; breaking an oath-bound spouse's vow terms.
- On departure: as separation above, plus Opinion drops to STRAINED, plus
  the spouse's NPC companion lines are repurposed (StateVoice_C Type C
  hostile-to-player escalation).

Save block: `separated: TRUE`, `separation_reason: "[…]"`,
`separation_chapter: <N>`, `partner_left_voluntarily: TRUE/FALSE`.

---

## 🌅 MORNING DIALOGUE — POST-WEDDING AMBIENT

> **DM:** After marriage, the spouse has 3 morning ambient line variants.
> Select by context: **A** = default (warm, domestic); **B** = affection
> (use when Romance heat is recent or an anniversary is near); **C** =
> kingdom-weight (use when Unrest is high or a crisis just passed).

| Partner | A — Default | B — Affection | C — Kingdom |
|---|---|---|---|
| Linzi | *"You're awake. [N] Kingdom Turns married. I counted."* | *"Seventeen entries about what you look like in the morning. All say 'impossible.' They're wrong."* | *"You carry this kingdom like it owes you nothing. I write it so they know what that costs. Morning."* |
| Leliana | *"I wrote a verse this morning while you slept. It's a good one. Don't ask me to play it yet — it isn't ready, and you, of all people, get the finished thing."* | *"I set your name to a bar three different ways last night before I found the right one. You were awake, watching me. I knew. I let you think I didn't."* | *"The court is frightened. Play them something, or let me. A kingdom that has never yet heard itself sung isn't broken, child — it's only waiting to learn it has a voice. Morning."* |

---

## 🎂 ANNIVERSARY SCENES — SCRIPTED

> **DM:** Run the matching scene when the anniversary fires. Player responds
> freely. If no response in 2 beats, the partner closes warmly and moves on.
> Effect fires regardless of player input.

### Anniversary 1 (4 Kingdom Turns after wedding)
*Tone: Surprised to still be here. Gratitude, slight disbelief.*

**Linzi:** Camp desk, late night, re-reading old entries.
*"I wrote the first chapter about us tonight. Seventeen rewrites. ...I finally got it right. Can I read you the first line? ...'In the year the kingdom learned to stand, two people stood beside it, and learned something harder.'"*
Effect: Morale +1. Opinion +1 if player approves.

**Leliana:** She is playing when you find her — something slow, not from the cycle, nothing the player has heard before. She stops when she hears you.
*"I wrote something for tonight. Not for the cycle. Just — for this. It doesn't have a name, and for once I'm in no hurry to give it one."* She plays it through once without stopping. When she finishes: *"There. Now there are two of us alive who have heard it. That is a larger number than it sounds — most of what I've written, I've written for no one, or for the dead. This one's for you."*
Effect: Morale +1. `leliana_anniversary_piece_1: true`.

### Anniversary 2 (8 Kingdom Turns after wedding)
*Tone: Settled. The wonder has deepened into something quieter.*

**Linzi:** *"I finished the chronicle. Volume One. ...I kept changing the ending. Then I realized: it doesn't end. That's the whole point."* She doesn't give it to you. *"You'll read it when we're old."* | Morale +1, Culture +1.

**Leliana:** She hands the player a single folded page — the air from Anniversary 1, notated and titled at last. The title is the name the player gave the cycle during the companion quest, or if unnamed: *"[Unnamed — Year Two]."*
*"I named it. You'll notice I waited a year — I wanted to be certain it wasn't an elegy."* She is smiling, the slow one. *"It isn't."* | Morale +1, Culture +1.

### Anniversary 3 (12 Kingdom Turns after wedding)
*Tone: Deep permanence. This has become part of the architecture of the character's life.*

**Linzi:** *"I am better at being afraid because of you. Not less afraid — better. You should know that."* | Morale +1.

**Leliana:** She doesn't play. She sits beside you and does not fill the silence — and for Leliana, who has filled too many silences with the names the dark years took from her, that is its own kind of vow.
After a while: *"I have spent a very long life keeping faith with people by remembering them. Tonight I find I would rather keep faith with you by being here, saying nothing, and letting it be enough."* She stays. She is quiet. She lets the quiet be a good one — the first kind, not the grieving kind.
Effect: Morale +1. This is the tell. The DM may note it silently: the dawn-hour discipline has, for one night, nothing left to mourn.

---

## ⚖️ MARRIAGE STRAIN METER

> **DM:** Strain (0–7) tracks accumulated tension in the marriage. Departure
> fires at Strain 7. Starts at 0 at marriage. Does not auto-reset between
> chapters — only by active player action.

**Strain accumulates (+):**
```
+2 / chapter  : Non-spouse has Romance Score ≥ +2 AND had active
                romantic scenes this chapter (two-timing in progress)
+1 / chapter  : Anniversary overdue by 2+ Kingdom Turns
+1            : Fight System resolved against player (while married)
+2            : Player commits act incompatible with spouse's core value
                (§ DIVORCE & SEPARATION — examples listed there)
```

**Strain reduces (−):**
```
−1            : Anniversary scene completed on-time or early
−1            : Player reaffirms commitment in personal scene (freeform
                declarations count; DM judges sincerity by context)
−2            : Grand Gesture (500 gp / 1 HP / narrative concession)
```

**Strain tiers:**
```
0–2  STABLE    : No visible effect. Marriage normal.
3–4  COOL      : Morning dialogue shifts to C variant. Consort buff −1
                 until Strain < 3. Private Strain Scene fires once:
                 spouse makes an oblique observational remark (DM
                 improvises per companion voice).
5–6  TENSE     : Spouse confronts privately (she initiates, not .address).
                 Diplomacy DC 16.
                 Success: Strain frozen for 2 chapters.
                 Failure / no response: Strain +1.
7+   DEPARTURE : Partner leaves at next quiet camp. Follows § DIVORCE
                 Partner-initiated departure. Strain resets to 0.
```

Save block: `marriage_strain: 0`, `strain_scene_fired: false`,
`strain_confrontation_active: false`.

---

## 🖥️ MARRIAGE COMMANDS

| Command | Output |
|---------|--------|
| `.propose` | Initiate the Proposal Scene with current Stage 5 partner |
| `.wedding [scope]` | Schedule the wedding ceremony — A/B/C/D |
| `.vow` | Player speaks a templated vow (DM provides 3 options to pick from) |
| `.anniversary` | Player initiates an Anniversary scene early (between auto-fires) |
| `.heir` | Declare an heir; opens A/B/C/D source menu |
| `.separate` | Initiate separation (asks for confirmation twice) |
| `.spouse` | Status: spouse name, marriage type, anniversary count, heir status |
| `.marriage` | Full marriage profile + buffs + heir + recent events |

---

## 📜 SAVE BLOCK — MARRIAGE FIELDS

```json
"marriage": {
  "married": false,
  "spouse": "",
  "spouse_origin": "",
  "wedding_chapter": null,
  "wedding_type": "",
  "wedding_vow_freeform": false,
  "anniversary_count": 0,
  "anniversary_last_session": 0,
  "heir_declared": false,
  "heir_source": "",
  "heir_name": "",
  "heir_age_narrative": 0,
  "separated": false,
  "separation_reason": "",
  "separation_chapter": null,
  "partner_left_voluntarily": false,
  "widowed": false,
  "widow_chapter": null,
  "marriage_history": [],
  "marriage_strain": 0,
  "strain_scene_fired": false,
  "strain_confrontation_active": false
}
```

---

## ⚠️ DESIGN RULES

1. **Marriage is optional.** Stage 5 Devoted Consort gives identical
   day-to-day buffs. Marriage adds public ceremony, succession, and a
   public-record dimension. The DM never pressures.

2. **The vow is sacred — to the partner.** Marriage is binding in the
   companion's mind. Two-timing post-marriage is a Tier 4 event, not a
   Tier 2.

3. **The player chooses the heir framework.** No deterministic biology.
   The DM does not gender, identify, or detail the heir's body. Heir is
   a kingdom asset — narrate them as a person, not a sketch.

4. **Anniversaries matter.** Skipping them costs Opinion and Romance.
   The kingdom remembers the date.

5. **Widowhood is rare.** Endings should preserve spouses. The Widow
   state is provided for tragic narratives, not default.

6. **Polyamorous marriage** is supported only if BOTH partners independently
   accepted the Open Arrangement (KM_Romance.md § Jealousy Resolution Stage 3) AND a separate
   wedding ceremony is held for each. Polyamory does not stack the buffs
   — only one Consort buff can be active at a time; the player picks which
   partner is the active Consort each Kingdom Turn.

---

*KM_Romance.md — Kingmaker PF2e Text Adventure | Marriage System v2.0*
*Pair-load with KM_Romance.md (single merged file as of v3.0 / 2026-05-22).*
