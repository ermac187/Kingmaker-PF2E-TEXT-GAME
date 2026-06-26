# KINGMAKER — MARRIAGE SYSTEM
## KM_Marriage.md | Active from: Stage 5 Devoted Consort | Referenced by: KM_Romance.md, KM_Kingdom.md, KM_LoadRules_B.md

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
- love_scene_occurred = true (KM_Romance_C.md § Love Scene System)
- The player has built either:
    - A Capital Cathedral or Temple (KM_Buildings.md), OR
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
1. The DM sets a quiet, intentional setting per partner voice (Goldmoon at
   sunrise prayer, Tatsumaki on a windless rooftop, Olivier on the perimeter
   walk, Tika at the inn-bar she rebuilt, etc.).
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
| Goldmoon | *"Mishakal whispered something just now. I will not tell you what. ...Yes. Of course."* |
| Tika | *"Wait — really? — really? OK. OK. Yes. Yes — wait, ask me again, I want to hear it again."* |
| Ryuko | *"You serious? — yeah, you're serious. ...Yeah. I'm in. I'm IN. Don't make me say a speech."* |
| Morrigan | *"You have asked me to refuse one chain by accepting another. The arithmetic is absurd. ...And yes."* |
| Sucrose | *"Oh. Oh — I — I prepared a list of reasons you should — but — I think — yes. Yes. Yes please."* |
| Artoria | *"My liege. ...My — beloved. The oath I swore was for a kingdom that ended. The oath I would swear next is for one that is beginning. ...I accept."* |
| Olivier | *"Confirmed. ...Yes. The answer is yes. Logistics later."* |
| Yoko | *"...Holy shit. ...Yeah. YEAH. Get over here."* |
| Kyoko | *"Statistical analysis suggests this is the optimal outcome. ...That is — also — what I want. Yes."* |
| Tatsumaki | *"...You'll have to ask twice. Just so I'm sure. ...Once more. ...Yes. Don't make me say it AGAIN."* |

| Partner (QL) | Her Answer |
|---|---|
| Tristian | *"Sarenrae taught me to say yes to gifts I do not deserve. I am trying. Yes."* |
| Octavia | *"Don't make this a scene. ...Fine. It IS a scene. Yes. Of course yes. Now kiss me before I cry, you idiot."* |
| Kalikke | *"Both of us. Always. ...Yes."* — *"Yes."* (one voice, then the other) |
| Nok-Nok | *"NOK-NOK SAYS YES! NOK-NOK ALWAYS SAYS YES! HERO ASKED!"* |
| Jubilost | *"I prepared an acceptance speech. It is fourteen pages. I shall give the abridged version: yes."* |
| Ekundayo | *"Trkaa decided. So did I. Yes."* |

| Partner (legacy / WotR) | Her Answer |
|---|---|
| Valerie | *"...You know I will say yes. You knew before you asked. ...So ask anyway. I want to hear it."* |
| Arueshalae | *"I never thought I would be asked. I thought I would be — owned. You asked. ...Yes."* |
| Daeran | *"Gracious. — Yes. Obviously yes. Do not make me elaborate, I shall lose my composure."* |
| Ember | *"Yes. Yes yes yes. I have known for months. I was waiting."* |

> **Refusal is rare** — at Stage 5, a refusal is mechanical only. Reasons:
> - Partner is Artoria/Yoko/Tatsumaki/Ryuko AND the player has open
>   `love_triangle_active = true` flag → they refuse and exit romance.
> - Partner is Morrigan AND player has shown any "tame her" behavior
>   (ordered her, restricted her movement, asked her to abandon witchcraft)
>   → she refuses, exits romance permanently.
> - Otherwise, refusal at Stage 5 should NOT happen. If the DM is unsure,
>   the answer is yes — that's what Stage 5 means.

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
              deity to be reflected. Goldmoon, Tristian, Artoria, and
              certain others have a strong preference for this option.
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

**The kiss is a Bond Moment** (KM_Romance_P3.md § PHYSICAL INTERACTIONS).
Save block: `married: TRUE`, `spouse: "[Name]"`, `wedding_chapter: <N>`,
`wedding_type: "[scope]"`.

---

## 📜 VOWS — PARTNER LINES (active 11)

> **DM:** The DM speaks each partner's vow verbatim during the ceremony.
> The player either responds in template form (.vow) or freeform.

| Partner | Her Vow |
|---|---|
| Linzi | *"I will write you accurately, even when I love you. I will edit no kindness out and no flaw in. I will keep you. The chronicle ends here. The story keeps going."* |
| Goldmoon | *"By Mishakal's hand and by mine — I will hold you in light when light is hard. I will pray for you, and beside you, and as long as my voice lasts. You are mine."* |
| Tika | *"I learned my own name working a tavern that didn't survive. I'm going to learn it again, working THIS — with you. Forever. Don't make me say more, I'm already crying."* |
| Ryuko | *"I came here looking for who killed my dad. I found out something else. I found YOU. I am DONE running at the wrong things. I run at THIS now. Forever."* |
| Morrigan | *"I refuse every chain. I have built this one. I will wear it. I will not let you break it without my hand on the saw beside yours. That is the vow. It is more than I have given anyone."* |
| Sucrose | *"I made — I made a vow. It was thirty pages. I'm going to read three lines: I am not pretending. I am not performing. I am here. ...That's it. That's the vow. Please be kind to it."* |
| Artoria | *"I, Artoria of Britain, who once held a kingdom that ended — I bind my oath to you, who hold one beginning. You are my liege and you are my beloved. Both, equally. Witness it."* |
| Olivier | *"I do not say things I do not mean. I do not retract things I have said. I have said yes. I am saying it again now, in front of the kingdom and the gods. Yes."* |
| Yoko | *"I aim. I don't miss. I'm not missing this one. You're it. You're the one. I'm done looking. ...That's the vow. Don't make me redo it."* |
| Kyoko | *"My investigation is closed. The conclusion: you. The evidence: every interaction I have catalogued since we met. The verdict: love. I rest my case on this hand."* |
| Tatsumaki | *"...Hmph. ...Fine. ...You. You and only you. ...There. Said it. Don't ASK me to say it again. ...Unless you want me to. ...I would."* |

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
  (see KM_StrongholdEvents.md for triggers).

Save block: `heir_declared: TRUE`, `heir_source: "[born/adopted/ward/successor]"`,
`heir_name: "[…]"`, `heir_age_narrative: <N>`.

---

## 💔 DIVORCE & SEPARATION

> **DM:** Marriages can fail. The player may initiate a separation. The
> partner may also leave under specific extreme conditions. This is rare
> and intentional — not a casual mechanic.

**Player-initiated separation (`.separate`):**
- Available only after a Tier 3+ jealousy event OR a major relationship
  rupture (see KM_Romance_B.md § TIER 4).
- Confirmation prompt — DM asks twice.
- On confirmation: `separated: TRUE`, Consort role ends, kingdom buffs
  end. Partner exits party and returns to a meaningful location (their
  home region, their faction, their order). Public_reputation −5
  kingdom-wide. Unrest +2 for 1 chapter.
- Recovery path: long, voluntary, and requires partner consent. Treat as
  a Tier 4 Rupture repair arc (KM_Romance_B.md), 5+ sessions minimum.

**Partner-initiated departure:**
- Triggers automatically if:
  - Player two-times AFTER marriage (any Romance Score ≥ +2 with a non-
    spouse companion). Strain meter tracks this escalation; departure
    fires at Strain 7. See § MARRIAGE STRAIN METER below.
  - Player commits an act fundamentally incompatible with spouse's core
    value. Examples: ordering Goldmoon to bless an execution; destroying
    Sucrose's research wing; ordering Olivier's Briggs guard executed;
    breaking Artoria's oath terms.
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
| Goldmoon | *"You slept. Mishakal says sleep is prayer by another name."* | *"I watched you dream. I should not admit that. I do not retract it."* | *"The kingdom can wait one hour. Eat with me first."* |
| Tika | *"Morning. Mug's ready. Know how you take it. Always have."* | *"You did that thing in your sleep again. Stop it — I can't wake up laughing every morning."* | *"They'll knock soon. Five more minutes."* |
| Ryuko | *"Didn't hear you come in. Good. ...Mornin'."* | *"Stop looking at me like that. ...Okay. You can look."* | *"How bad today? Scale of one to 'all going to die.' Mug first."* |
| Morrigan | *"You wake as if the sun requires an audience. Sit."* | *"I have decided I do not hate mornings. Revised opinion. New evidence."* | *"The court requires performance. Reserve something for me first."* |
| Sucrose | *"Oh — you're up! I — here. Eat."* | *"You are the most remarkable variable I — good morning. That should have come first."* | *"Whatever is wrong today — I checked the numbers. We've handled worse. Together."* |
| Artoria | *"My liege. A new day for the realm. ...And for us."* | *"You reach out in your sleep. I have stopped moving away from it."* | *"The kingdom stands because its ruler rises. I am here. That is everything."* |
| Olivier | *"Six-hundred-hours report: all quiet. ...Good morning."* | *"I do not make a habit of lingering. Noted exception."* | *"Busy day. Breakfast first. Non-negotiable."* |
| Yoko | *"Finally up. Been awake an hour. Perimeter's clear."* | *"Don't get used to me being this soft. ...Get a little used to it."* | *"Dispatch stack looks ugly. Ten minutes. I'll keep the door."* |
| Kyoko | *"Sleep: six hours forty-two minutes. Sufficient. You look better than the data suggests."* | *"I notice things I don't annotate. You fall in a separate file."* | *"Cases never end. Neither do we. That is today's relevant data."* |
| Tatsumaki | *"...You're loud when you wake up. I was already awake."* | *"Don't say anything. I'm letting you sit next to me. That counts."* | *"The kingdom doesn't get mornings. Those are mine. ...Ours. Tell them to wait."* |

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

**Goldmoon:** Sunrise prayers, private chapel.
*"I asked Mishakal what I should say. She said: say what is true. What is true is I am not the same. I am better. ...You did that. Thank you."*
Effect: Morale +1. Loyalty +1 if player joins the prayer.

**Tika:** Kitchen, early morning. She made something impractical.
*"One year. I — I made your favorite. Slightly burned the — it's fine. One YEAR, though. That's — that's a lot. ...Yeah. It's a lot."*
Effect: Morale +1. Opinion +1 if player eats without comment.

**Ryuko:** Rooftop, evening.
*"I don't do sentimental. ...I looked up when we actually met — it's been longer than one year. The wedding's the part we wrote down."* Pause. *"Good year."*
Effect: Morale +1.

**Morrigan:** Her study. She hands you a book, then takes it back.
*"I compiled what it means to be married to a ruler. The first sincere thing I have written in years. I will not give you the book. One line: 'I was incorrect about what I needed.'"*
Effect: Morale +1. Opinion +1 if player asks what she needed.

**Sucrose:** Lab, late evening. She forgot the date and clearly rushed.
*"Oh! Oh no — I — I knew it was today — I made you something. It lacks a ribbon but that's purely aesthetic — here."* [Something small and handmade.] *"Happy anniversary. I planned this better in my head."*
Effect: Morale +1. Opinion +1 if player says it's perfect.

**Artoria:** The great hall, empty.
*"In Camelot, anniversaries were kingdom events. Here they are private first. I believe that is better. ...I have kept one year's oath. I intend to keep the next. Is that what you wished to hear?"*
Effect: Morale +1.

**Olivier:** Evening perimeter walk.
*"One year since the ceremony. Eighteen months since I decided."* Pause. *"Both dates matter. ...The second one more."*
Effect: Morale +1. Opinion +1 if player asks about the earlier date.

**Yoko:** Campfire, late.
*"I had five drafts of a speech. Burned them — embarrassing."* Pause. *"What I actually think: I'm glad you asked. I'm glad I said yes. I'd do it again. ...That's the speech."*
Effect: Morale +1.

**Kyoko:** Quiet library corner.
*"I reviewed the year. Seventy-three shared meals. One hundred forty-two above-average conversations. Four disagreements, all resolved. Summary: strongly positive."* Pause. *"...Interpret that however is most meaningful."*
Effect: Morale +1. Opinion +1 if player says "I love you."

**Tatsumaki:** High ledge, evening wind.
*"You came up here. Good."* Long pause. *"One year."* Longer pause. *"...It was a good one."*
Effect: Morale +1.

### Anniversary 2 (8 Kingdom Turns after wedding)
*Tone: Settled. The wonder has deepened into something quieter.*

**Linzi:** *"I finished the chronicle. Volume One. ...I kept changing the ending. Then I realized: it doesn't end. That's the whole point."* She doesn't give it to you. *"You'll read it when we're old."* | Morale +1, Culture +1.

**Goldmoon:** *"Prayer taught me to keep asking for the same things. Not weakness — honesty."* She takes your hand. *"I am still asking for this. I expect I will for the rest of my life."* | Morale +1, Unrest −1.

**Tika:** *"Two years. You know what I stopped doing? Checking if you'll still be there. Not because I stopped caring — because I stopped needing to."* She refills your cup unprompted. | Morale +1.

**Ryuko:** *"I was looking for someone worth everything. Kept aiming wrong."* She tilts her chin at you. *"Two years. You're it."* | Morale +1.

**Morrigan:** *"Marriage changes what your nature grows toward. Tested this on myself. My data: I was growing toward this regardless. You accelerated the outcome."* | Morale +1.

**Sucrose:** The greenhouse she started after the wedding, two-year growth cycle.
*"I wanted something we grew together. Even if you didn't know."* She finally looks at you. *"...Is that strange?"* | Morale +1, Culture +1.

**Artoria:** *"Camelot lasted years before it ended. The differences are not circumstantial."* She faces you directly. *"The difference is you. I believe this one will stand."* | Morale +1, Stability +1.

**Olivier:** *"Two years of data. No meaningful negative impact on command effectiveness. Seventeen instances of improved judgment attributed to this."* She taps the table, not the map. *"Confirmed effective."* | Morale +1.

**Yoko:** *"I see it from up here. What we built."* Not talking about the kingdom. *"Needed the right aim."* | Morale +1.

**Kyoko:** *"Year two outperforms year one. Year one I was studying the system. Year two I stopped treating it as one."* Pause. *"My notes are different now. Less analysis. More record."* | Morale +1.

**Tatsumaki:** Same ledge, same ritual. She makes room before you ask.
*"Two years."* Pause. *"I know."* Pause. *"...Keep showing up."* | Morale +1.

### Anniversary 3 (12 Kingdom Turns after wedding)
*Tone: Deep permanence. This has become part of the architecture of the character's life.*

**Linzi:** *"I am better at being afraid because of you. Not less afraid — better. You should know that."* | Morale +1.

**Goldmoon:** *"In Que-Shu, the third year is the iron year — when a bond stops being new and starts being inevitable. ...I feel it. Don't you?"* | Morale +1, Loyalty +1.

**Tika:** *"I stopped counting every morning around month nine. That's when I knew — you were just the fact of things. I stopped reassuring myself you were real."* | Morale +1.

**Ryuko:** *"I thought about leaving. First year — still had the habit. One night, when things were hard."* Pause. *"I'm telling you now because I stayed. Every day since. It was never an accident."* | Morale +1.

**Morrigan:** *"I shall say what I would not have admitted three years ago: I am afraid of losing this. I have not feared loss in thirty years. ...That is your fault."* | Morale +1.

**Sucrose:** *"The perfectly perfect days were fewer than predicted. The ones still worth it — far more than predicted. ...I think that is what 'happy' means. More good days than the model suggested."* | Morale +1.

**Artoria:** *"I have no current projection for this kingdom's end. My previous models did not account for this variable."* She looks at you. *"I stopped calculating. I am simply here."* | Morale +1, Stability +1.

**Olivier:** She produces a folded letter. *"Not a report. An account of what this has been."* She offers it. *"Read it when I'm not looking."* | Morale +1.

**Yoko:** *"I thought home was a place you went back to. I went back to a lot of places. None of them were home."* She looks at you. *"Three years. I finally figured it out."* | Morale +1.

**Kyoko:** *"I have closed the investigation permanently. The conclusion is final. The conclusion is: yes. This. Always."* | Morale +1.

**Tatsumaki:** *"Three years."* Pause. *"...You never got easier to be around."* Pause. *"I mean that as the best possible thing. You just — are. And I am."* Pause. *"That's it."* | Morale +1.

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
   accepted the Open Arrangement (KM_Romance_B.md § STAGE 3) AND a separate
   wedding ceremony is held for each. Polyamory does not stack the buffs
   — only one Consort buff can be active at a time; the player picks which
   partner is the active Consort each Kingdom Turn.

---

*KM_Marriage.md — Kingmaker PF2e Text Adventure | Marriage System v2.0*
*Pair-load with KM_Romance.md, KM_Romance_B.md.*
