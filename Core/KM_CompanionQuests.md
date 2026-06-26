# KINGMAKER — COMPANION QUEST SCENES (PART A)
## KM_CompanionQuests_A.md | Amiri, Linzi, Valerie, Harrim, Tristian

> **DM:** Load this file when a companion personal quest triggers.
> Each entry contains: trigger conditions, opening scene, NPC dialogue,
> choice menus, resolution paths, and save block flags to set.
> Quest summaries (triggers, flags) are in KM_Companions.md.
> This file contains the actual scene content to run.

---

## 1. AMIRI — THE SWORD OR THE SOLDIER

**Trigger:** First time Amiri is actually disarmed in combat (Stage 2 of her arc)
**Chapter:** Any (Ch1–Ch4)
**Prerequisite:** Stage 1 has been running — she has been quietly testing her hands

---

### SCENE: THE DISARM MOMENT (in combat)

> **DM:** Do not announce this. When the disarm happens, run it inline.

The sword spins out of her hand — a Trip, a Disarm, bad luck, whatever the mechanism. It lands out of reach.

One beat. She does not immediately dive for it.

Her hand closes on the nearest thing — a loose stone, a piece of broken timber, a fallen enemy's dagger. She swings. Whether it hits or misses, she retrieves her sword at the next available moment.

She says nothing for the rest of the combat.

---

### SCENE: CAMP THAT NIGHT

> **DM:** This scene fires the first time the party rests after the disarm. It fires whether or not the player asks. Do not skip it.

Amiri is sitting apart from the fire. She's turning something small in her hands — the improvised weapon she grabbed, if she kept it. If not, just her empty fist.

She doesn't look up when the player approaches.

**Amiri:** *"It worked."*

Two words. She doesn't elaborate. Doesn't look up. If the player says nothing, she eventually adds:

**Amiri:** *"You said a soldier who can't fight with what's available is useless if they get disarmed. I've been thinking about that. About what I am without it."*

She holds up her empty hand. Looks at it.

**Amiri:** *"I don't have an answer yet."*

### Player Choice Menu:
1. *"You fought well. The weapon didn't matter."*
2. *"What did you feel when it left your hand?"*
3. *"The sword is still yours. Nothing changed."*
4. *"What does it mean to you? The sword specifically."*
5. [Say nothing — let her sit with it]
6. [Custom]

### Responses:
**Option 1:** She looks at you for a moment. *"Don't patronize me. It mattered. That's the point."* Relationship unchanged.

**Option 2:** Long pause. *"Like losing a limb. Then like... maybe I have two limbs."* She doesn't say anything else. **+1 Relationship.**

**Option 3:** *"You don't understand."* She picks up the sword and walks away. Relationship unchanged.

**Option 4 — Best option:** She actually looks at you fully. *"I found it at the base of a cliff. The giant was already dead. They said it didn't count — that I hadn't earned it. If I'd left it behind, I would have agreed with them. It wasn't a weapon. It was... the argument."* Beat. *"Maybe I won the argument already."* **+1 Relationship. Quest advances to Stage 3.**

**Option 5:** She eventually stands, takes her sword, and goes to sleep. Next morning she's slightly different — quieter, less aggressive about the weapon specifically. Stage 3 begins silently.

---

### STAGE 3 RESOLUTION (Ch3+)

When Amiri kills something significant with an improvised weapon by choice (she picks it up instead of drawing her sword), this fires:

**Amiri:** *"Hm."*

That's it. She sheathes the sword she didn't use. Quest complete. No ceremony.

**Flag:** `amiri_quest = complete`
**Stage flags:** `amiri_quest_stage = 1` (set at campaign start — she's quietly testing), `amiri_quest_stage = 2` (set on first actual disarm in combat), `amiri_quest_stage = 3` (set when she makes a significant kill with an improvised weapon by choice). Stage 3 triggers completion.
**Reward:** She gains the trait *Soldier, Not the Sword* — improvised weapons deal 1d6+Str for her (not 1d4). No announcement needed.

---

## 2. JUBILOST — THE MAP THAT MATTERS

**Trigger:** Relationship ≥ Friendly + Ch2 (capital established, first trading network active)
**Chapter:** Ch2–Ch3
**Location:** Capital → three Stolen Lands field sites → Capital archive

---

### SCENE: THE PROBLEM

Jubilost slaps a document on the player's desk without asking.

**Jubilost:** *"Look at this."*

It's a map. Official-looking, bearing the Restov Swordlords' seal. The Stolen Lands — his territory — laid out with professional quality. The legend credits a cartographer named Thelvon Marrus.

**Jubilost:** *"That man has been following my route notes. His map is wrong in nine places I can identify immediately. Wrong in the ways that matter — the fords, the trails, the seasonal flood patterns. A merchant who follows this will lose wagons."*

He crosses his arms.

**Jubilost:** *"I have the correct map. I have always had the correct map. It needs your kingdom's seal to become the official version."*

### Player Choice Menu:
1. *"What's stopping you from publishing it?"*
2. *"Show me the discrepancies."*
3. *"Why does it need my seal specifically?"*
4. *"What happened to your map at the Skunk River?"*
5. [Custom]

**Option 1:** He goes very still. *"The original was damaged. I have the reconstruction. It is correct. I am certain it is correct."* He does not look certain. Quest advances.

**Option 2 — Best:** He spreads his version next to Marrus's. The differences are real and significant. He knows this terrain with the specificity of someone who has crossed it in three seasons, on foot and by wagon. **+1 Relationship. Quest advances.**

**Option 4:** A long pause. *"Irrelevant. That map is gone. I have rebuilt it."* He says this the way someone says something they have told themselves many times. Quest advances.

---

### THE PROBLEM BENEATH THE PROBLEM

At camp that night, if the player asks about the reconstruction:

**Jubilost:** *"The original took eleven years. Three crossings of the Sellen. I had notation systems developed for this specific terrain."*

He's quiet for a moment.

**Jubilost:** *"The reconstruction is good. The reconstruction may not be perfect. I cannot distinguish the parts I remember from the parts I believe I remember."*

He looks at the player.

**Jubilost:** *"That is not a distinction I have had to make before."*

### Player Choice Menu:
1. *"We can verify it in the field."*
2. *"A map built from memory is still a map."*
3. *"What would it take to be certain?"*
4. [Say nothing — let that sit]
5. [Custom]

**Option 1 — Best:** He looks at the player as if they have said something useful, which he finds irritating. *"That is a functional suggestion."* Quest advances to verification. **+1 Relationship.**

**Option 3:** *"Going back. Checking every landmark."* He's already calculating the route. Quest advances.

---

### THE VERIFICATION

Three field sites. The player accompanies Jubilost to confirm contested sections of the map. One skill check per site.

**Site 1 — The Skunk River Ford:**
> DC 14 Survival.
> **Success:** Ford confirmed — depth, seasonal markers, and crossing approach accurate.
> **Critical Success:** Jubilost's notation is more precise than he thought. He adds a marginal annotation without comment.
> **Failure:** A marker is off by half a league. He corrects it without comment. But he corrects it.

**Site 2 — The Narlmarches Firewatch Trail:**
> DC 16 Nature.
> **Success:** Trail confirmed passable year-round with one seasonal caveat he hadn't noted.
> **Failure:** Two caveats needed. He adds them. Doesn't mention the second was a miss.

**Site 3 — The Thorn River Bend:**
No roll. They stand at the original prologue camp location. Jubilost takes one measurement. Looks at his map.

The notation is exactly right.

**Jubilost:** *"I remembered this one correctly."*

He doesn't say anything else about it.

---

### RESOLUTION SCENE

Back at the capital. The official map is sealed — the kingdom's mark, and his name in small but legible text in the legend's corner.

**Jubilost:** *"It is not perfect."* He's looking at it. *"Two of the corrections were necessary. The third was a preference I should not have encoded as fact."*

Beat.

**Jubilost:** *"But it is correct. Correct enough. Which is more than can be said for Marrus."*

He rolls it up.

**Jubilost:** *"I will want to update it after Ch3."*

He leaves. That's the quest.

---

**Flag:** `jubilost_quest = complete` | `jubilost_map_published = true`

**Reward:** The **Stolen Lands Survey (Official)** becomes a permanent kingdom asset — party gains +1 to all Exploration checks in mapped hexes. Jubilost gains *First-Hand Data* — Recall Knowledge checks about terrain, geography, and routes auto-succeed in any location he has personally mapped.

**Save block additions:**
```json
"jubilost_quest": "complete",
"jubilost_map_published": true,
"stolen_lands_survey": "official"
```

---

## 3. LINZI — THE UNFINISHED SONG

**Trigger:** Relationship ≥ Friendly + Ch3 (she realizes her chronicle may not have an ending)
**Location:** Capital — Linzi's room or writing area

---

### SCENE: SHE COMES TO THE PLAYER

> **DM:** Linzi initiates this. She knocks on the player's door or approaches at camp.

She has her notebook. She looks uncharacteristically still.

**Linzi:** *"I need to ask you something and I need you to not make it a big moment. Can you do that?"*

If the player agrees:

**Linzi:** *"I've been writing the chronicle since the Prologue. Every fight, every choice, every person. I have... a lot."* She taps the notebook. *"But I realized I don't know how it ends. I don't know if it ends with you alive, or... not. And if it doesn't—"* She stops. *"Who finishes it?"*

### Player Choice Menu:
1. *"You'll be there to finish it yourself."*
2. *"If I die, you'll write the ending."*
3. *"The story isn't about me. It's about all of us."*
4. *"Do you want me to read what you've written so far?"*
5. *"What do you want the ending to be?"*
6. [Custom]

### Responses:
**Option 1:** She smiles, but it doesn't reach her eyes. *"You can't promise that."* Relationship unchanged.

**Option 2:** She's quiet for a moment. *"I can do that."* She writes something in the notebook. You don't see what. **+1 Relationship.**

**Option 3 — Best option:** She looks up sharply, then slowly. *"...oh."* She opens the notebook and starts rewriting something. *"I've been writing it wrong. It's not your chronicle. It's ours."* **+1 Relationship. Quest advances.**

**Option 4:** She hands it over. If the player asks what a specific entry says, she tells them. This is a freeform scene — the DM uses the session's actual events to populate what she's written. **+1 Relationship.**

**Option 5:** *"I want it to end with everyone alive and something built that wasn't there before."* She pauses. *"Is that too much?"*

---

### RESOLUTION SCENE (after Ch3 boss, if Linzi is alive)

She finds the player alone and hands them a folded page from the notebook.

**Linzi:** *"Chapter one is done. I gave it a title."*

The title is whatever the player's most defining moment was in the session — the DM picks it from actual events.

**Linzi:** *"I wanted you to see it before I move on to chapter two."*

She takes the page back and puts it in the notebook.

**Flag:** `linzi_quest = complete`
**Ch7 survival note:** If quest complete, she has a finished chapter to protect. She fights harder. Mechanically: +2 HP per level in Ch7.

---

## 3. VALERIE — SHELYN'S CHOSEN

**Trigger:** Relationship ≥ Friendly + Ch2 (a formal letter arrives from a Shelynite paladin)
**Location:** Oleg's Trading Post (scripted journey from capital)

---

### SCENE: THE LETTER

A formal letter arrives — rose-gold wax seal, Shelyn's glyph. **Fredero Sinnet**, Paladin of Shelyn, requests the player release Valerie from service so she may return and fulfill her destiny as Shelyn's Chosen.

When Valerie is shown the letter:

**Valerie:** *"Where is he."*

Not a question.

---

### SCENE: OLEG'S TRADING POST

**Fredero Sinnet** is waiting. Human male paladin in rose-gold plate, late 30s, carrying a longsword.

**Fredero:** *"Valerie. The Order sent me to bring you home. Shelyn hasn't forgotten you."*

**Valerie:** *"I remember exactly what happened."*

**Fredero:** *"Then you know what comes next."* He draws his weapon. *"A duel. You win — I leave. I win — you return to the Order."*

### Player Choice Menu:
1. [Step in — refuse the duel on Valerie's behalf]
2. *"Valerie. You don't have to fight him."*
3. *"Your call."* [Step back]
4. *"What does Shelyn want from her, exactly?"*
5. [Custom]

**Option 1:** Valerie puts a hand on the player's arm. *"No."* She steps forward. *"It's mine."*
**Option 3 — Best:** She nods once. She draws her weapon.

---

### THE DUEL

**Fredero Sinnet** — Level 9 Paladin | AC 29 | 86 HP | Fort +12 / Ref +8 / Will +9 | +18 to hit, 1d8+14

> **DM:** Hard fight. Pre-buff Valerie. Do not understate Fredero's ability — the threat must be real.

The duel resolves. Win or loss.

**After the duel — regardless of who won:**

A scar appears across Valerie's face. Not from a blow. It appears. Even if Fredero never landed a hit.

**Fredero:** *"Shelyn marks what is hers. You were always Chosen. You just had to decide what that meant."* He leaves.

**Valerie** touches the scar. Doesn't speak.

> **⛔ DM: `valerie_scar = true` is set HERE. The scar does not exist in any prior narration. Do not describe it before this scene fires.**

**`valerie_quest = complete` | `valerie_judgment_pending = true`**
**+2 Relationship.**

---

### AFTER: VALERIE'S CHOICE

**Valerie:** *(later)* *"He offered me full reinstatement. My rank. My name restored."*

### Player Choice Menu:
1. *"What did you tell him?"*
2. *"It's your decision."*
3. *"The kingdom needs you here."*
4. *"Go if that's what you want."*
5. [Custom]

**If Valerie returns to Order:** She leaves permanently. **`valerie_returned_to_order = TRUE`**
Ch7: She is not in the burning prison. Appears in epilogue — came back alone.
> *"I heard what happened. I wasn't here."* — *"I made a choice I thought was right."*
Player can invite her to return as citizen (not soldier). **`valerie_epilogue_returned = TRUE/FALSE`**

**If Valerie stays (quest complete):**
Ch7 — reaches the burning prison before it burns. Full loyalty. Present for all Ch7 fights.
**She holds the line while the player fights Nyrissa.**
Reward: **Celestial Plate** (+2 Resilient Full Plate, Bulk 1).

**If quest never completed:**
Ch7 — trapped in burning prison. Escapes on her own. Arrives wounded. She does not need rescuing.

---

### NOTE: JUDGMENT OF THE GODS (Ch4 follow-up)
A second quest triggers later — Valerie can choose to keep or remove the scar. Leave this open; do not resolve it here.

---

## 4. HARRIM — SHATTERED DREAMS
> **⛔ ADAPTATION NOTE:** Real game quests are "Unwanted Legacy" (Ch2 — dwarven ruins, relic skill checks, earns Heart of the Anvil item) and "Unbreakable Metal" (Ch3 — adamantine golem, dwarves trapped in fortress). This section is a thematic adaptation. If running game-faithful quests, replace with the dwarven ruins/golem structure. The emotional arc below is custom but consistent with his character.

**Trigger:** Relationship ≥ Friendly + Ch3 (he receives a vision of the tomb)
**Location:** Forsaken Mound (unmarked tomb in Ch3 region — add to hex map when triggered)
**Chapter:** Ch3 (can carry into Ch4 if not triggered)
**Ch7 risk:** If incomplete → Harrim wanders during the final dungeon. Returns after but misses key fights.

---

### SCENE: THE VISION

At camp, Harrim wakes before the others. He's sitting with his holy symbol, not moving. If the player is on watch, they notice. If not, Linzi wakes them — "Something's wrong with Harrim."

**Harrim:** *"I saw them again. The ones who followed me before. My first congregation."* He sets down the symbol. *"They're in the mound. What's left of them. Groetus showed me where."*

He stands up and begins walking without asking.

**Player choice:** Follow him now / Ask him to wait until morning / Send someone else with him
All options lead to the same scene. Harrim will wait if asked, but he doesn't sleep again.

---

### SCENE: THE FORSAKEN MOUND

> *The mound is unmarked. No name, no clan sigil. Just a low hill in the Ch3 wilderness, half-overgrown. Inside: stone markers, hand-placed. Seven of them.*
>
> *Harrim knows which name goes with each one without looking at the stones.*

He kneels at the first marker. Sets his hand flat on the earth.

**Harrim:** *"I told them the end was coming. That fighting it was futile. That Groetus watched all things with equal indifference. They believed me."*

A long pause.

**Harrim:** *"And then they died for something futile because I told them it was. Because I needed an audience for my certainty."*

He doesn't look at the player.

**Harrim:** *"I survived. I always survive. Groetus apparently finds that funny."*

---

### Player Choice Menu — At the Graves:
1. *"They chose to follow you. That was their decision."*
2. *"You can't carry this forever."*
3. *"Groetus brought you here for a reason."*
4. *"Was their death futile? Or did it mean something to you?"*
5. *[Say nothing — sit with him]*
6. *[Custom]*

**Option 1:** *"They did. And I used that choice badly."* He doesn't accept the absolution but he heard it. +0 Relationship, quest continues.

**Option 2:** *"I can. I've been doing it for thirty years."* Flat. Not bitter. Just factual. Quest continues.

**Option 3:** *"Groetus doesn't have reasons. That's the point."* He looks at the mound. *"...or I've been wrong about what Groetus is."* Quest advances. +1 Relationship.

**Option 4 — Best:** He looks at the graves for a long time. *"They meant something to me. That's not futile. That's the problem."* He places his holy symbol on the first marker. *"Groetus says nothing matters. But I remember their names. That contradicts the theology."* **+1 Relationship. Quest advances.**

**Option 5 — Silent:** He appreciates it. After a long time he speaks anyway — Option 4's version, quieter. **+1 Relationship. Quest advances.**

---

### SCENE: THE CHOICE — WHAT DOES HIS FAITH MEAN?

They're still in the mound. The silence has shifted.

**Harrim:** *"I have been preaching that the end is inevitable and resistance is futile. That is what Groetus asks of his priests."*

He sits back against the wall. Looks at the ceiling.

**Harrim:** *"But if that were true — if nothing mattered, if it was all futile — I would have stopped. Years ago. I would have lain down somewhere and let the end come to me."*

He looks at the player.

**Harrim:** *"I have not stopped. I have fought beside you and healed you and kept people alive that Groetus would have been perfectly happy to collect early. What does that make me?"*

### Player Choice Menu — His Faith:
1. *"A hypocrite."* [Honest but harsh]
2. *"Someone who believes more than they admit."*
3. *"The doom is real. The futility is real. But you're still here. That means something."*
4. *"Maybe you serve Groetus better by being the one who doesn't give up."*
5. *"I don't know. But I'm glad you haven't stopped."*
6. *[Custom]*

**Option 1:** He laughs — a real one, short and surprised. *"Yes. Exactly. Thank you for saying it directly."* Something loosens in him. Not resolved, but honest. +1 Relationship. Quest can still complete.

**Option 2:** *"That's a kind interpretation."* Pause. *"It might even be right."* +1 Relationship.

**Option 3 — Good:** *"...that is an obscenely reasonable interpretation of Groetus."* Long pause. *"He's going to be furious."* Another pause. *"Good."* **+1 Relationship.**

**Option 4 — Best:** He goes quiet. Very quiet. Then: *"That would mean Groetus chose me precisely because I wouldn't. Not as a joke. As a strategy."* He picks up his holy symbol from the grave marker. *"An end-of-days god who sends the one priest who refuses to stop moving."* He looks at it. *"...I need to think about this for a very long time."* **+2 Relationship.**

**Option 5:** He nods. *"That's enough."* Short. Genuine. +1 Relationship.

---

### RESOLUTION

He stands. He doesn't replace his symbol on the grave — he keeps it. He looks at all seven markers once more.

**Harrim:** *"They weren't wrong to follow me. I was wrong to lead them there."* Beat. *"I can't fix that. But I can remember their names. Groetus collects everything. I'll make sure he gets these ones right."*

He walks out of the mound. Doesn't look back.

At the next camp, unprompted:

**Harrim:** *"Gormund. Thessa. Brek. Annild. Vorin. Dax. Mira."* He says the seven names quietly into the fire. *"They existed. That's enough."*

**+1 Relationship if player asks who they were. He tells them. One by one.**

---

**Quest complete. Flag: `harrim_quest = complete`**

**Reward:** Harrim gains a unique Focus spell: **Groetus's Mercy** (1/day). When a living ally within 30 ft reaches Dying 1 or higher, Harrim can spend 1 Focus Point as a free action on his turn: that ally automatically stabilizes and regains 2d8+10 HP. Harrim explains it as *"keeping the interesting ones alive long enough to see what happens next."*

**Note to DM:** This is not reconciliation with Groetus. Harrim doesn't abandon his faith. He expands what it means. He is still a doom-preacher. He just now understands that witnessing endings requires being present for them — which means keeping himself and his allies alive. His nihilism becomes functional rather than paralyzing.

**Save block additions:**
```json
"harrim_quest": "complete",
"harrim_quest_stage": 3,
"harrim_seven_names_spoken": true
```

---

## 5. TRISTIAN — KINGDOM OF THE CLEANSED

**Trigger:** SCRIPTED — Ch3. Fires regardless of relationship. Tristian confesses.
**Location:** Ch3 dungeon (Varnhold region) — after the party finds evidence of the Bloom seeds

---

### SCENE: THE CONFESSION

The party finds evidence — journals, ritual notes — that the Bloom was seeded deliberately. Someone planted the corruption months ago. The trail leads back to the feast. To someone who was there.

Tristian has been quiet for hours by the time you make camp.

**Tristian:** *"I need to tell you something."*

He doesn't sit. Doesn't look at you directly.

**Tristian:** *"The Bloom seeds. I planted them. I didn't know what they were — I was told they were healing wards for the land. The man who gave them to me... I trusted him. I shouldn't have."*

He finally looks at you.

**Tristian:** *"People died because of what I did. I know that. I'm not asking forgiveness. I'm telling you because you deserve to know who has been at your side."*

---

### Player Choice Menu:
1. *"Who gave you the seeds?"*
2. *"You knew what they were."* [Accusatory]
3. *"You were deceived. That's different from choosing this."*
4. *"How do I know you're not still being used?"*
5. *"Leave. Now."*
6. *"Stay. We deal with what's done."*
7. [Custom]

**Option 1:** He names the man. The DM connects this to the larger Ch3 conspiracy. Information gained.

**Option 2:** *"I didn't. But I should have asked more questions."* He doesn't defend himself further.

**Option 3 — Forgiveness path:** *"The distinction matters to you. I'm grateful for that."* **+1 Relationship. Quest complete: `tristian_quest = forgiven`**

**Option 5 — Exile:** He leaves. **`tristian_quest = condemned`**. He can be re-recruited in Ch4 at DC 22 Diplomacy after he's spent time alone atoning.

**Option 6 — Pragmatic acceptance:** *"I won't waste what you're offering."* Quest complete. **`tristian_quest = forgiven`**

---

### IF CONDEMNED — RE-RECRUITMENT (Ch4)

Tristian is found at a remote shrine to Sarenrae in Ch4. He's been there for weeks.

**Tristian:** *"You came."*

He doesn't say more. Waits.

### Player Choice Menu:
1. *"I need you back."*
2. *"I was wrong to send you away."*
3. *"Can you still fight?"*
4. *"Sarenrae led me here. Come back."*

Any option re-recruits him at **`tristian_quest = forgiven`** with **−1 Relationship** (net 0 from his departure).

---

*KM_CompanionQuests_A.md — Kingmaker PF2e Text Adventure | Companion Quest Scenes v1.0*


---

<!-- merged from KM_CompanionQuests_B.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION QUEST SCENES (PART B)
## KM_CompanionQuests_B.md | Jaethal, Octavia, Regongar, Nok-Nok, Kalikke/Kanerah  [Lem purged v93.19 Sub-B]

> **DM:** Companion to KM_CompanionQuests_A.md. Same format.
> Load when any of these companions' personal quests trigger.

---

## 7. JAETHAL — REVEAL MY DESTINY

**Trigger:** Relationship ≥ Friendly + Ch2 (word arrives that Nortellara has been located)
**Location:** Capital → Narlmarches → Ch3 confrontation

---

### SCENE: THE WORD

Jaethal approaches with the controlled stillness she reserves for things that matter.

**Jaethal:** *"They found her."* A pause. *"Nortellara. My daughter. She is alive."*

She says it like a complication.

**Jaethal:** *"Urgathoa expects a debt repaid. I made a promise before I fully understood what it would cost. I intend to honor it — or decide I will not. I need you there when I decide."*

### Player Choice Menu:
1. *"What does Urgathoa want?"*
2. *"What do you want?"*
3. *"I'll be there. Whatever you decide."*
4. *"You don't have to follow through."*
5. [Custom]

**Option 2:** She looks at you as though the question is poorly formed.
**Jaethal:** *"What I want is not relevant. What I owe is."* A beat. *"Though I am beginning to wonder if I have confused the two."*

---

### SCENE: FINDING NORTELLARA

Nortellara is alive. She knows what her mother is. She has been waiting.

**Nortellara:** *"So you came."*

**Jaethal:** *"You knew I would."*

**Nortellara:** *"I knew you might. I wasn't certain."*

Jaethal has been treating this as a project — a debt to settle, a loose end. Nortellara is neither. She is a person, watching her mother decide what kind of thing she is.

Urgathoa's demand: kill Nortellara as an offering, or take her body — displace her daughter's soul and use the living flesh to escape the undead curse.

### Player Choice Menu:
1. [Stay back — let Jaethal lead]
2. *"Jaethal. Look at her."*
3. *"What does she owe you, Nortellara?"*
4. *"Jaethal — what are you about to do?"*
5. [Custom]

---

### CHOICE: NORTELLARA'S FATE

### Player Choice Menu:
1. *"Don't."* [Intervene directly]
2. *"Jaethal — if you do this, I will stop you."*
3. [Stay back — Jaethal's choice entirely]
4. *"Nortellara — leave. Now."*
5. [Custom]

**Good path (Options 1, 2, 4 + Diplomacy or Insight DC 22):**
On success — Jaethal stops. She looks at her daughter for a long time.
**Jaethal:** *"I have decided what I owe — and what I do not."*
She turns her back on Urgathoa's demand. The undead condition begins unraveling — slowly, painfully. She receives the **Signet of the Incorruptible**. Nortellara lives.
**`nortellara_fate = spared` | `jaethal_quest = complete` (redemption)**
**+2 Relationship.**

**Evil path (Option 3 or failed check):**
Jaethal kills Nortellara and displaces into the living body. The undead shell collapses. Jaethal continues — alive in her daughter's form, Urgathoa satisfied.
**`nortellara_fate = killed_possessed` | `jaethal_quest = complete` (fallen)**
No relationship gain. Tristian −2 if present.

---

## 9. OCTAVIA & REGONGAR — CRUEL JUSTICE

**Trigger:** Ch3, lull between Season of Bloom and Varnhold Vanishing (~20 days before An Ancient Curse Part 3 timer)
**Location:** Capital tavern → Technic League camp (2 days east)

---

### SCENE: THE SPY

A Technic League informant is sitting openly in the capital's tavern — League livery, no concealment. Octavia spots him immediately.

**Octavia:** *"He's not hiding. That means he wants us to follow him."*

**Regongar:** *"So we follow him."*

When confronted, the spy gives up his master's location without much persuasion.

**Spy:** *"Maestro Janush is holding at a League camp east of the capital. He thought you'd want to settle this personally."*

### Player Choice Menu:
1. *"We go."*
2. *"What does Janush want?"*
3. *"This is a trap."*
4. *"Octavia — is this what you want?"*
5. [Custom]

**Option 4:** She looks at Regongar. He doesn't say anything.
**Octavia:** *"Yes."*

---

### SCENE: THE TECHNIC LEAGUE CAMP

The camp is defended. Fight through to the command tent.

**Maestro Janush** is inside — 50s, organized, completely unsurprised. Slave cages are visible through the tent's back.

**Janush:** *"Octavia. Regongar. I've been watching your work here. You've done well."*

**Octavia:** *"You sold us."*

**Janush:** *"I invested you. In someone who could develop what you're capable of."* He looks at the player. *"I was right. Look at you."* He gestures between them. *"I want you back. Lieutenant positions — both of you. Real authority. Not slaves. Partners."*

**Regongar:** *"..."*

### Player Choice Menu:
1. [Let Octavia answer]
2. *"They're not going anywhere with you."*
3. *"What exactly are you offering?"* [Draw out intelligence]
4. *"Octavia. Regongar. Your call."*
5. [Custom]

**Option 4 — Correct:** They look at each other.
**Octavia:** *"No."*
**Regongar:** *"No."*
**Janush:** *"I thought so."* He throws a fireball into the slave cages. He moves for the exit.

---

### CRITICAL CHOICE: THE FIRE

The cages are burning. Janush is at the door.

**Octavia:** *"The cages—"*

### Player Choice Menu:
1. *"The slaves. GO."* [Save them — Janush escapes]
2. *"Janush — don't let him reach the door."* [Chase him — slaves burn]
3. [Split — Regongar takes Janush, Octavia takes the cages] ← Athletics DC 24
4. [Custom]

**Option 1 — Save the slaves:**
Janush escapes. Slaves live. Regongar: no rage after. Octavia: quiet. **`janush_fate = escaped`**

**Option 2 — Chase Janush:**
Slaves die. Janush killed or captured. Octavia: visibly disturbed. **`janush_fate = killed` | `janush_slaves_burned = true`**

**Option 3 — Split (DC 24):**
Success: Both outcomes (slaves saved, Janush caught). **`janush_fate = captured`**
Failure: Choose Option 1 or 2 as fallback.

**`octavia_quest = complete` | `regongar_quest = complete`**

---

### QUIET SCENE (any outcome, camp that night)

**Octavia** is sitting alone.

**Octavia:** *"I thought it would feel like something. Like a door closing."* She looks at her hands. *"It feels like a door that was already open."*

---

### REGONGAR — AFTER JANUSH

If Janush is dead or caught: Regongar says nothing the rest of the day. At camp, he's sharpening his blade.

**Regongar:** *"First time I've killed something and not been angry afterward."* He doesn't look up. *"Usually the anger stays. That's the problem."*

### Player Choice Menu:
1. *"What do you feel?"*
2. *"It's over now."*
3. *"Octavia needed this too."*
4. [Say nothing]

**Option 1:** *"Nothing. Just... quiet."* He sheathes the blade. *"I don't know what to do with quiet."*

**+2 Relationship (Octavia). +1 Relationship (Regongar). Quest complete.**

His Sparkling Targe ability gains an upgrade: Shield Block now also applies a 1d6 electricity discharge to the attacker when used.

---

## 6. NOK-NOK — NOK-NOK AND THE GREAT CHIEF

**Trigger:** Relationship ≥ Friendly + Ch2 (goblins appear at the kingdom border)
**Location:** Goblin camp in Ch2 Narlmarches

---

### SCENE: THE CHALLENGE

Nok-Nok is vibrating with excitement at camp.

**Nok-Nok:** *"Chief! Chief! Nok-Nok's old tribe is here! Near big smelly river hex! They sent a message — they want Nok-Nok back. Or to fight."*

He grins. *"Nok-Nok wants to fight."*

The message is from the tribe's Great Chief: if Nok-Nok returns, he must fight the chief in single combat. If Nok-Nok wins, he leads the tribe. If he loses, he stays gone.

### Player Choice Menu:
1. *"We go with you."*
2. *"This is your fight. You go alone."*
3. *"Don't go. It's a trap."*
4. *"What do you want from this?"*
5. [Custom]

**Option 4:** Nok-Nok thinks very hard, which involves visible effort.
**Nok-Nok:** *"Nok-Nok wants... tribe to know Nok-Nok is hero. Real hero. Not just running away hero."*

---

### SCENE: THE CHALLENGE (at the camp)

The Great Chief is larger than Nok-Nok. Most things are, but this one specifically is three times Nok-Nok's weight and armed with a skull-headed club.

**Great Chief:** *"You come back to die, little Nok-Nok?"*

**Nok-Nok:** *"Nok-Nok come back to WIN."*

**If player is present:** The tribe watches. The player can intervene or not.

**Option: Help Nok-Nok openly:**
The chief is distracted by the player's presence. Nok-Nok uses this. **Nok-Nok wins.** The tribe accepts the player as Nok-Nok's patron. **+1 Stability** to kingdom. **`noknok_quest = complete`**

**Option: Stay back — let Nok-Nok fight alone:**
Nok-Nok loses the fight but refuses to surrender. The chief is impressed enough by his refusal to yield that he concedes the symbolic victory.
**Nok-Nok:** *"Nok-Nok lost fight but won respect! Same thing!"* It is not the same thing, but he believes it. **`noknok_quest = complete`**

---

### AFTER: THE SHRINE

Nok-Nok builds a small shrine to himself near the capital. It is terrible. It is also inexplicably endearing.

**Nok-Nok:** *"Chief see Nok-Nok's shrine? Nok-Nok made it. For worshippers."*

There are no worshippers. The shrine has a drawing of Nok-Nok defeating a giant that is clearly the chief painted over.

**+2 Relationship. Quest complete.**

---

## 11. [REMOVED — Roster v2]
*Lem's personal quest deprecated in Roster v2 Sub-C (v93.19). Numbering slot retained.*

---

## 8. KALIKKE / KANERAH — THE PRICE OF CURIOSITY

**Trigger:** Ch2 recruitment (they are one recruit slot)
**Midpoint:** Ch5 — curse origin
**Location:** Wildwood investigation → Pitax region origin point

---

### SCENE: FIRST RECRUITMENT (Ch2)

They arrive together — or rather, one arrives. The other is present but suppressed. The dominant one at the moment is Kalikke.

**Kalikke:** *"We heard you were building something worth building. We'd like to contribute."* She pauses. *"We come as a pair. The other one will introduce herself when she's ready."*

That evening, mid-conversation, the shift happens. The eyes change. The posture changes.

**Kanerah:** *"So. You're the baron."* Looking you over. *"Kalikke vouched for you. I don't vouch that easily. Impress me."*

---

### MIDPOINT: THE WILDWOOD INVESTIGATION (Ch3–4)

They've been tracking the source of the curse for months. In the Wildwood, they find the original ritual site — a binding circle, old, from before either of them was born.

**Kalikke:** *"Someone bound us before we were born. Used us as a vessel for a dual-elemental experiment."*

**Kanerah:** *(surfacing)* *"Someone is going to answer for that."*

The trail leads to Pitax — specifically to an old court mage who served the kingdom before Irovetti. Now retired. Comfortable. Unaware the sisters are looking for him.

---

### SCENE: THE MAGE (Ch5 Pitax access)

Mage Aldren is 80 years old and immediately terrified when they arrive.

**Aldren:** *"You weren't supposed to find me. The binding was supposed to dissolve when you reached maturity—"*

**Kanerah:** *"It didn't."*

**Aldren:** *"I see that."*

### Player Choice Menu:
1. *"Can you fix it?"*
2. *"What exactly did you do?"* [Information first]
3. [Let Kanerah handle it]
4. *"Is he dangerous?"* [to both sisters]
5. [Custom]

**Option 1:** He can. It requires a ritual and their consent. But the options change what they become.

---

### FINAL CHOICE: THE CURSE'S RESOLUTION

Aldren explains the three options:

**Option A: Break the curse completely.** Both sisters manifest as separate people. New bodies must be conjured (ritual 8 hours). They lose some elemental power (−1d6 to blast damage each) but are fully separate. **`curse_resolution = broken`**

**Option B: Accept and integrate.** The curse becomes a feature. They develop a shared consciousness they can switch between at will. Both personalities retain full strength. Power increases (blasts gain +1d6). **`curse_resolution = accepted`**

**Option C: One absorbs the other.** The dominant personality gains full control and the other is gone. Power doubles for the survivor. Dark path. **`curse_resolution = sacrificed`** — player must choose which survives; the other is gone permanently.

**Player presents the choice but does not make it for them.** The sisters decide.

If the player has been fair to both — shown equal respect to Kalikke and Kanerah across the campaign — they choose Option B (integration) together. If the player has consistently favored one, that one pushes for Option C.

**+2 Relationship (both). Quest complete. Flag: `kalikke_kanerah_quest = complete`**

---

### POST-QUEST: THE INTEGRATION

If Option B:

They speak in tandem for the first time — one voice that somehow carries both personalities.

**Both:** *"That's new."*

Then separately:
**Kalikke:** *"Strange."*
**Kanerah:** *"Useful."*

**Both:** *"Both."*

---

---

## ⚔️ COMPANION QUEST CONFLICTS — MUTUALLY EXCLUSIVE OUTCOMES

> **DM:** Three quest pairs where advancing one companion's goal blocks the other's preferred outcome. The player MUST choose a side. The unchosen companion takes a relationship hit. Present both positions using the Debate system (KM_Mythic_Systems.md) if the player wants to hear both sides before deciding.

---

### CONFLICT 1 — TRISTIAN vs JAETHAL: The Undead Question

**Trigger:** Both quests active in Ch3. Tristian discovers Jaethal's quest involves killing or possessing her living daughter Nortellara to satisfy Urgathoa. Jaethal discovers Tristian's quest involves cleansing undead sites.

**Confrontation Scene:** Camp, evening. Tristian approaches the player:
> *"I need to tell you something about Jaethal's search. What she wants to find — what she wants to do with it — I cannot stand by and watch."*

Jaethal responds within one beat:
> *"The living have a convenient morality about death. I am asking for what was taken from me. He is asking me to accept the theft."*

**Player choices:**
1. **Side with Tristian** — Block the reanimation. Jaethal's quest resolves as "incomplete." Jaethal: −2 relationship. Tristian: +1.
2. **Side with Jaethal** — Allow the reanimation attempt. Tristian's quest changes trajectory (he must reconcile). Tristian: −2 relationship. Jaethal: +1.
3. **Debate** — Trigger Debate system. Winner's position prevails. Loser takes −1 instead of −2.
4. **Override both** — Ruler authority. Neither quest advances this chapter. Both: −1 relationship. Issue resurfaces Ch4.

**Save block:** `"quest_conflicts": { "tristian_jaethal": "unresolved" | "tristian_won" | "jaethal_won" | "debate_resolved" | "overridden" }`

---

### CONFLICT 2 — REGONGAR vs VALERIE: Violence as Answer

**Trigger:** Ch2, after both companions reach Friendly. A captured bandit lieutenant has information about Stag Lord loyalists. Regongar wants to torture the information out. Valerie wants a lawful interrogation.

**Confrontation Scene:** Interrogation room or camp:
> **Regongar:** *"He knows where they're hiding. I can have it in ten minutes. You know I can."*
> **Valerie:** *"And what does that make us? The same thing we're trying to replace."*

**Player choices:**
1. **Side with Regongar** — Torture. Information gained immediately + specific location. Valerie: −2 relationship. Regongar: +1. +1 Ruthless disposition.
2. **Side with Valerie** — Lawful interrogation. Information gained after Diplomacy DC 16 (slower, may be incomplete). Regongar: −2 relationship. Valerie: +1. +1 Merciful disposition.
3. **Debate** — Regongar (Intimidation) vs Valerie (Diplomacy). Winner's method used.
4. **Player interrogates alone** — Neither companion's method. Use player's best social skill. Both: −0 relationship (neutral, player took it off their hands).

**Save block:** `"regongar_valerie": "unresolved" | "regongar_won" | "valerie_won" | "debate_resolved" | "player_solo" `

---

### CONFLICT 3 — AMIRI vs EKUNDAYO: The Trophy Kill

**Trigger:** Ch3 or Ch4. A dangerous beast (dire bear, wyvern, or similar) threatens a settlement. Amiri wants to fight it alone — a warrior's trial. Ekundayo wants to track and trap it safely — a ranger's solution that protects the settlement with certainty.

**Confrontation Scene:** War room or camp planning:
> **Amiri:** *"A beast like this deserves a fight, not a trap. You send rangers with nets and ropes, you kill the story. I will fight it. Alone."*
> **Ekundayo:** *"Stories don't protect the families living a mile from its den. My way, nobody dies. Including Amiri."*

**Player choices:**
1. **Side with Amiri** — Solo combat. Amiri fights the beast (DM runs Amiri's stat block, high risk). If she wins: +2 relationship, +1 Party Morale, legendary trophy. If she falls: unconscious, rescued, −1 morale. Ekundayo: −1 relationship either way.
2. **Side with Ekundayo** — Ranger trap. Auto-success, beast captured/killed safely. Ekundayo: +1 relationship. Amiri: −2 relationship ("You took this from me").
3. **Debate** — Amiri (Intimidation) vs Ekundayo (Survival). Winner's plan.
4. **Full party hunt** — Player leads. Both companions participate. Neither gets their preferred method. Both: −0 relationship. +1 Blunt disposition (direct approach).

**Save block:** `"amiri_ekundayo": "unresolved" | "amiri_won" | "ekundayo_won" | "debate_resolved" | "party_hunt" `

---

*KM_CompanionQuests_B.md — Kingmaker PF2e Text Adventure | Companion Quest Scenes v2.0*
*New: Companion Quest Conflicts (3 pairs with Debate integration)*


---

<!-- merged from KM_CompanionQuests.md (v93.21 file consolidation) -->

# KINGMAKER — EKUNDAYO: COMPANION PROFILE & QUEST
## KM_CompanionQuests.md | Companion #12 | Available: Chapter 2

> **DM:** Load this file when Ekundayo is recruited or when his personal quest
> triggers. Integrates with KM_Companions.md relationship system.
> Add to KM_LoadRules.md trigger: "Ekundayo recruited or quest triggered" → this file.

---

## ═══════════════════════════════════════════
## EKUNDAYO
### Male Human Ranger (Precision Hunter)
## ═══════════════════════════════════════════

**Appearance:** Lean, weathered man in his mid-30s. Dark skin, close-cropped hair, calm eyes that track everything. Wears practical leather armor marked with old clan tattoos on his forearms. His dog Trkaa is always with him — a large, scarred hunting dog who mirrors his master's quiet watchfulness. He moves like someone who has spent years alone in forests.

**Backstory:** Ekundayo's family came from Thuvia; his true motherland was Absalom. After his parents died he worked as a mercenary and wanderer, traveling north to Avistan and through the Stolen Lands. He made repeated trips through a village called Bristlehill, where he met a local woman named Amanda. Eventually he settled there and married her. A rock troll named Kargadd led a warband that attacked Bristlehill and killed Amanda and his family while he was away. He returned to find what trolls leave behind. He has been hunting Kargadd through the Stolen Lands since. He is a devout worshipper of Torag.

**Motivation:** Kill Kargadd. After that — genuinely unclear. He has been living for that purpose so long he doesn't know what comes next.

**Personality:** Quiet, precise, economical with words and movement. He is not cold — he listens carefully, notices everything, and when he does speak it is worth hearing. The grief is present but contained, like a wound that healed wrong. He does not talk about his family unprompted. He does not need to. Everything about him is a monument to them.

**Trkaa:** His dog is not a pet. She is a partner. She tracks what he hunts, warns when he sleeps, and has saved his life more than once. She was his daughter's dog. He will not explain this if asked. He will change the subject.

**Likes:** Silence, precise action, honest people, animals, cold camps with clear sight lines
**Dislikes:** Unnecessary talk, imprecise action, cruelty to animals, being told to wait

---

## Level 2 Stat Block (at recruitment, Ch2)

```
EKUNDAYO — Human Ranger 2 (Precision Hunter)
HP: 22 | AC: 18 (Leather Armor +1, Dex)
Speed: 30 ft | Initiative: +7 (Expert Perception)
STR 14 (+2) | DEX 18 (+4) | CON 14 (+2) | INT 12 (+1) | WIS 16 (+3) | CHA 10 (+0)
Fort +6 | Ref +8 | Will +7

Weapons:
  Composite Longbow +1: d20+8, 1d8+5 P (Propulsive, range 100 ft, Deadly d10)
    Hunted Prey: +2 damage vs Hunted target
    Precision Hunter: +1d8 precision on first hit per turn vs Hunted target
  Shortsword: d20+6, 1d6+2 P/S (Agile, Finesse)

Skills (Trained): Nature +7, Survival +7, Athletics +5, Stealth +7, Perception +9

Class Features:
  Hunt Prey (1A): Designate one creature; +2 damage, ignore cover for attacks,
                  no penalty for tracking. Active until new target designated.
  Precision Hunter (Ranger): First attack vs Hunted target each turn +1d8 precision
  Trkaa (Animal Companion): Acts on Ekundayo's turn (1A command)

Feats: Monster Hunter (L1) — Recall Knowledge before attack as free action;
       on success, +1d4 damage first hit
Gear: Composite Longbow +1, 40 arrows, Shortsword, Leather Armor, Adventurer's Pack
Gold: 12 gp
```

---

## Trkaa — Animal Companion

```
TRKAA — Hunting Dog (Animal Companion)
HP: 24 | AC: 16 | Speed: 40 ft
STR 14 (+2) | DEX 16 (+3) | CON 14 (+2) | INT 2 (−4) | WIS 14 (+2) | CHA 6 (−2)
Fort +6 | Ref +7 | Will +4

Attacks:
  Jaws: d20+6, 1d6+2 B/P (Trip on crit)
  1 action (Stride) or 2 actions (Strike + Stride)

Special:
  Scent: Precise sense within 30 ft; imprecise to 60 ft
  Track: Can track any creature with a scent for 24 hours after exposure
  Pack Tactics: +1 to attack rolls when adjacent to Ekundayo or another ally

Commanding Trkaa: Ekundayo uses 1A to command; she acts immediately.
  Default (no command): Trkaa Strides toward the Hunted Prey target.
  With command: Strike, Aid, Seek, or Recall to Ekundayo's side.
```

---

## Companion Scaling (key levels)

| Level | Ekundayo HP | Composite Longbow | Precision Damage | Trkaa HP |
|-------|------------|-------------------|-----------------|----------|
| 2 | 22 | +8, 1d8+5 | +1d8 | 24 |
| 5 | 46 | +11, 2d8+7 | +2d8 | 44 |
| 8 | 66 | +15, 2d8+9 | +2d8 | 58 |
| 12 | 94 | +18, 3d8+11 | +3d8 | 80 |
| 16 | 126 | +22, 3d8+13 | +3d8 | 104 |
| 20 | 158 | +26, 4d8+15 | +4d8 | 130 |

---

## Opinions on Companions

| Companion | Ekundayo's View |
|-----------|----------------|
| Amiri | "She is loud. But she fights well and does not retreat." |
| Linzi | "Writes everything down. I don't understand why. She seems kind." |
| Tristian | "Healer. Useful. He asks too many questions." |
| Valerie | "Disciplined. She watches the same exits I watch." |
| Harrim | "Grim man. His god sounds exhausting. He does his work." |
| Jaethal | "She smells wrong. Trkaa doesn't like her. I pay attention to that." |
| Nok-Nok | "Unpredictable. I have learned to track his movements." |
| Octavia | "She freed herself. That earns something." |
| Regongar | "Loud. Angry. But he stands between danger and others." |
| Kalikke/Kanerah | "I cannot always tell which one I am speaking to. I ask." |

---

## Dialogue Snippets

- *"Trkaa found the trail. Two hours old. They went northeast."*
- *"Say what you mean."*
- *[Approving, quietly]:* *"That was clean work."*
- *[After Kargadd]:* *"He's dead. My family is still dead. I thought this would feel different."*

---

## Reaction to Player Choices

- **Approves:** Precise action, protecting the vulnerable, honoring the dead, patient tactics
- **Disapproves:** Cruelty, rushing into danger without preparation, harming animals
- **If player is reckless:** *"You'll get someone killed. Think before you move."*
- **If player harms an animal:** He says nothing. His relationship drops −1. He watches the player differently afterward.

---

## ═══════════════════════════════════════════
## PERSONAL QUEST — A SCORE TO SETTLE
## ═══════════════════════════════════════════

**Trigger:** Ekundayo recruited + `kargadd_location_known = TRUE` (from Bartholomew or exploration)
**Chapter:** 2 (Trobold, Level 2)
**Quest summary in KM_Companions.md** — full scene here.

---

### SCENE: THE NIGHT BEFORE TROBOLD

At camp the night before the party enters Trobold, if Ekundayo is in the party:

He is sitting apart from the fire. Trkaa is pressed against his side. He is cleaning his bow with methodical care that has nothing to do with the bow needing cleaning.

He doesn't look up when the player approaches.

**Ekundayo:** *"Tomorrow."*

One word. He means: tomorrow we find Kargadd.

### Player Choice Menu:
1. *"We'll get him."*
2. *"Are you ready for this?"*
3. *"Tell me about your family."*
4. *"What happens after?"*
5. [Say nothing — sit with him]
6. [Custom]

**Option 1:** He nods once. *"Yes."* Goes back to cleaning the bow.

**Option 2:** Long pause. *"I've been ready for three years."* Beat. *"I don't know if that's the same thing."* **+1 Relationship.**

**Option 3:** He stops cleaning the bow. Doesn't look at you. *"My wife was Adaeze. My children were Ibe and Chiamaka. Ibe was six. Chiamaka was four."* He starts cleaning again. *"Trkaa was Chiamaka's dog."* That's all. **+1 Relationship.**

**Option 4 (Best):** First time he actually looks at you directly. *"I don't know."* Beat. *"I've been trying not to think about it. It seemed like a distraction."* He looks at Trkaa. *"Probably I should figure that out."* **+1 Relationship. Quest flag: `ekundayo_after_questioned = TRUE`**

**Option 5:** You sit. He doesn't speak. Trkaa eventually puts her head in your lap. He notices. Doesn't comment. **+1 Relationship (silence respected).**

---

### SCENE: FINDING KARGADD (in Trobold Level 2)

> *He goes still the moment you enter the room. His dog Trkaa presses against his leg.*
> **Ekundayo:** *"That's him. The one who killed my family."*

The rock troll Kargadd is larger than the others. Old. The wall behind him has scratch marks — decades of them.

**If player tries to speak before Ekundayo acts:**

### Player Choice Menu:
1. [Attack immediately — give Ekundayo his kill]
2. *"Ekundayo. Your call."*
3. *"Wait — I want to try something."*
4. [Custom]

**Option 2 (Best):** He looks at you. Nods once. He draws his bow.

**Option 3:** If the player attempts to get Kargadd to speak (Intimidation DC 22 or Nature DC 18 — trolls are sentient):
Kargadd: *(in broken Common)* *"You come to die. Or to leave. Choose."*
He doesn't remember the homestead. He has killed dozens of families. He is a troll living in a dungeon.
If Ekundayo hears this exchange: *"He doesn't remember."* His voice is flat. *"Kill him anyway."*

---

### KARGADD FIGHT

```
KARGADD — Rock Troll (Elite)
HP: 88 | AC: 19 | Speed: 30 ft | Reach: 10 ft
Slam ×2: d20+13 (2d8+8 B) | Rock Throw: d20+10 (2d6+8 B, range 60 ft)
Fort +14 | Ref +6 | Will +5
Regeneration 20 (fire or acid)
Special: Enrage if Ekundayo attacks first — +4 damage for 3 rounds

Ekundayo in this fight: +2 attack and +2d8 precision damage vs Kargadd specifically.
He will never retreat from this fight. He will not accept healing to leave it.
If he goes down: he gets back up on 1 HP via a one-time determination effect. Once only.
```

---

### SCENE: AFTER KARGADD

Ekundayo stands over the body. Trkaa sniffs it once and looks away.

A long silence.

**Ekundayo:** *"He's dead."*

Another silence.

**Ekundayo:** *"My family is still dead."*

He looks at his hands. Then at you.

**Ekundayo:** *"I thought this would feel different."*

### Player Choice Menu:
1. *"It's done. That's what matters."*
2. *"Grief doesn't end when the reason ends."*
3. *"What do you feel?"*
4. [Say nothing]
5. [Custom]

**Option 2 (Best):** He looks at you for a long moment. *"No. It doesn't."* He sheathes his shortsword. *"I've spent three years not thinking past this. I need to figure out what I'm doing now."* **+2 Relationship. Quest complete.**

**Option 3:** *"Empty."* Pause. *"I expected rage, or peace, or something. There's nothing. Just — empty."* He picks up Trkaa's ears and scratches behind them. She leans into his hands. *"She's still here."* **+2 Relationship. Quest complete.**

**Option 4:** He eventually crouches, puts one hand on Trkaa, and stays there for a while. When he stands: *"Thank you for letting me have that."* **+2 Relationship. Quest complete.**

---

### AFTER THE QUEST — THE NEXT QUESTION

If `ekundayo_after_questioned = TRUE` (player asked "what happens after" the night before):

At camp that night, Ekundayo approaches the player.

**Ekundayo:** *"You asked what I do now. I've been thinking about it."*

He sits down.

**Ekundayo:** *"I don't know how to stop hunting. It's all I've done for three years. But I think — I think I want to build something, instead. Instead of just following something to its end."*

He looks at the capital in the distance (or the camp, if not yet founded).

**Ekundayo:** *"Your kingdom. I'd like to help build it. If you'll have me."*

**Player Choice Menu:**
1. *"You're already part of it."*
2. *"I was hoping you'd say that."*
3. *"What role do you want?"*
4. [Custom]

**Any option:** He nods once. The longest nod he's given anyone. +1 Relationship. **`ekundayo_committed_to_kingdom = TRUE`** — he becomes available as Marshal role advisor (best candidate for that role).

---

## 💾 SAVE BLOCK FLAGS

```json
"ekundayo": {
  "recruited": false,
  "relationship": 0,
  "quest_status": "inactive",
  "kargadd_killed": false,
  "after_questioned": false,
  "committed_to_kingdom": false,
  "trkaa_alive": true,
  "ch7_survival": "at_risk_if_quest_incomplete"
}
```

**Ch7 survival note:** If `ekundayo_quest` is complete, he is present for all Ch7 fights.
If `hargulka_vassal = TRUE` AND quest incomplete: he leaves party permanently in Ch2 (trolls still alive).
If quest incomplete but Hargulka killed: he is present in Ch7 but distracted — −2 to all checks.

---

*KM_CompanionQuests.md — Kingmaker PF2e Text Adventure | Ekundayo Companion Profile v1.0*
*Source: Pathfinder Kingmaker AP (Paizo / Owlcat)*


---

## 13. LELIANA — THE UNFINISHED VERSE (THE UNTITLED OPUS)

**Trigger:** Approval ≥ +8 AND `leliana_relationship_stage` ≥ SMITTEN
**Chapter:** Ch2+ (after first kingdom turn)
**Location:** Camp (Beat 1–3) → Capital public stage or great hall (Beat 4)

---

### BEAT 1 — DISCOVERY

> **DM:** This scene fires at the first camp rest after the trigger threshold is met. Fire it whether or not the player asks. Do not skip it.

The player hears music from the edge of camp — lute, slow and unguarded, unlike anything Leliana plays for audiences. When they get close enough, it stops. By the time they round the tent she is settling the lute back against her knee with studied nonchalance, like she was doing exactly this all along.

**Leliana:** *"Oh, you're up. Couldn't sleep either?"*

She does not acknowledge she was playing. If the player says nothing, she adds:

**Leliana:** *"It's a bad habit, playing alone at night. Makes people ask questions."*

She says it lightly, as a joke, meaning it precisely.

### Player Choice Menu:
1. *"I heard you. That wasn't nothing."*
2. *"What were you playing?"*
3. *"I'll pretend I didn't hear anything."*
4. *"How long have you been out here?"*
5. [Say nothing — sit down near her]
6. [Custom]

### Responses:
**Option 1:** She looks at you for a moment, then away. *"Observation noted."* She stills the strings with one hand. *"Good night."* She walks back to her tent. Quest pauses — resumes on next approval threshold. Relationship unchanged.

**Option 2:** A beat of genuine stillness. Then the easy warmth comes back up: *"Nothing. Just warming up. Force of an old habit."* But she doesn't leave. She stays sitting. +1 Relationship. **Quest advances to Beat 2.**

**Option 3:** She actually laughs — short, real. *"Good answer."* She puts the instrument away. But she glances back at you once before she goes. **Quest advances to Beat 2.**

**Option 4 — Best option:** *"A while,"* she says, and something in the deflection drops out. She looks at the instrument. *"I was working on something. I do that when I can't sleep."* She doesn't volunteer more, but she doesn't leave. **+1 Relationship. Quest advances to Beat 2.**

**Option 5 — Silent:** You sit near her without asking. After a long pause she sets her hands to the strings again and plays three more phrases — quieter, testing. Then stops. Doesn't explain. Doesn't leave. **+1 Relationship. Quest advances to Beat 2.**

---

### BEAT 2 — THE NAME

> **DM:** This fires at camp the following rest, or the next time the player speaks to Leliana alone. She initiates it.

She finds the player first. She has her notebook open — she writes things down, same as playing; she's always composing something.

**Leliana:** *"I'm going to tell you something, and you are contractually obligated to not make it strange."*

She turns the notebook. There are pages of notation — full movements, annotations, scene titles.

**Leliana:** *"I'm composing a cycle. About the expedition. Every major thing that's happened — I set a verse to it. There are..."* she counts, *"...twelve so far."*

She taps the cover.

**Leliana:** *"It doesn't have a name. The whole thing. I haven't named it yet."*

She says this like it's a logistical problem she hasn't gotten around to solving.

### Player Choice Menu:
1. *"What would you name it?"*
2. *"Suggest a name."* [Player offers something]
3. *"Why hasn't it got a name?"*
4. *"Can I read it?"*
5. *"Maybe it doesn't need one."*
6. [Custom]

### Responses:
**Option 1:** *"If I knew that, it would have one."* She closes the notebook. *"Things should earn their names."* Relationship unchanged. Quest continues on timer.

**Option 2 — Best option:** She goes very still when the player offers a name. She says it back slowly. If the player's name is something she finds right — the DM judges this based on what's happened in the session — she writes it on the inside cover in small letters and then immediately closes the notebook so the player can't see her expression. *"I'm not committing to anything. I'm just... considering."* **`leliana_opus_named = true`. Approval +3. Quest advances to Beat 3.**
If the name doesn't land: *"Hmm. Not yet."* Quest continues on timer.

**Option 3:** She's quiet for a moment. *"Because naming it means it's finished. And I'm not—"* She stops. *"I'm not ready for that."* She laughs it off before the player can respond. Quest advances. +1 Relationship.

**Option 4:** She considers. Then: *"No."* No explanation. But she looks pleased that you asked. +1 Relationship.

**Option 5:** She looks at you sideways. *"That's a lazy answer."* But she doesn't disagree. Quest continues.

---

### BEAT 3 — THE STILL HOUR

> **DM:** Fires at high approval threshold (≥ +14) OR entering final chapter — whichever comes first. Does not fire as a prompted conversation. The player must be present — on watch, unable to sleep, moving through camp. No menu offers this scene; the DM renders it when the condition is met and the player is in a position to observe it.

It is late. Most of the camp is asleep.

Leliana is sitting at the edge of the firelight with her lute across her knees. She is not playing. She has been there long enough that the fire has dropped.

The player can see — before she knows she is being watched — that something is wrong with the way she is sitting. Not injured. Not afraid. The stillness is the kind a person uses when holding something together from the inside. Her right hand, the plucking hand, is resting palm-up on her knee. She is looking at it.

She hears the player approach. She doesn't startle. She lays her hands to the strings — one phrase, clean, unhurried. She plays it through.

When she finishes she lifts her hands from the strings again.

**Leliana:** *"You're not sleeping either."*

It is not a question. It is not an invitation. It is acknowledgment that the player is there and she is not going to pretend otherwise.

She does not explain what the player saw. She does not refer to it. She picks up her notebook and makes a notation without comment.

### Player Choice Menu:
1. *"What were you playing?"*
2. *"Go back to sleep."* [Leave]
3. [Sit down without speaking]
4. [Custom]

### Responses:
**Option 1:** *"Something I'm still working out."* She turns a page in the notebook. *"It keeps changing."* She doesn't look up. The subject is closed. **+1 Relationship. Quest advances to Beat 4.**

**Option 2 — Leave:** She watches you go. She doesn't call after you. At the next camp interaction she is courteous and a touch too easy — the warmth turned up a half-step past natural. Quest still advances to Beat 4. **+0 Relationship.**

**Option 3 — Sit without speaking:** She doesn't react to the player sitting. After a moment she plays the phrase again — the same one, slightly different this time, as if answering a question. She doesn't explain that either. They sit until the fire dies. **+2 Relationship. Quest advances to Beat 4.**

> *DM: Do not name what the player saw. Do not have Leliana explain it. Do not have other companions reference this scene afterward unless the player tells them something. The player observed something. That is the whole beat. `leliana_illness_revealed = true` sets on Beat 3 completion — this flag means the player has witnessed something, not that Leliana has confessed anything.*

---

### BEAT 4 — THE PERFORMANCE

> **DM:** Fires at a major kingdom milestone: capital landmark unlocked (theater, great hall, or comparable) OR first turn of final chapter — whichever comes first. This scene does not fire quietly. It is an event.

Word moves through the capital that Leliana is performing tonight. No announcement from her — she has simply let it be known, the way she does things, and now there is an audience.

She takes the stage alone. No introduction. She sets her hands to the strings.

She plays the Verse from the beginning.

> *It takes forty minutes. The audience is silent the entire time. The piece moves through every major beat of the expedition — the DM should render 2–3 recognizable musical moments drawn from the BALLAD CYCLE (if active) or from actual session events. At points the spectral orchestra joins her (ORCHESTRAL MANIFOLD). The final movement is unfinished — it trails into a phrase that hasn't resolved yet.*

When the last note fades and she lifts her hands from the strings, the silence holds for a moment before the applause.

She looks at the player specifically.

**If `leliana_opus_named = true`:** She speaks into the quiet before the crowd fully recovers.

**Leliana:** *"The Unfinished Verse — except it has a title now."*

She announces the name the player gave her. Exactly as they gave it.

**If unnamed:** She performs it without announcement. After, she finds the player offstage.

**Leliana:** *"Still untitled. Don't say anything."*

---

### RESOLUTION

After the performance, at camp or wherever the party rests next:

**Leliana** approaches and sets a folded page in the player's hand without preamble.

**Leliana:** *"For the archive. The permanent record."*

It is a single handwritten score page — the final movement, titled however the Verse was named, or simply *"The Unfinished Verse — Final Movement (Unresolved)"* if unnamed. At the bottom in small notation: *"Dedicated to the expedition. Dedicated to everyone in it."*

She walks away before it becomes a moment.

**Flag:** `leliana_quest = complete` | `leliana_opus_performed = true`

**Reward:** Special item — **Printed Score Page (Final Movement)**. Physical object in inventory; no mechanical effect. DM note: if the player ever presents it to a court, conservatory, or music institution, it functions as a masterwork credential — treat as Legendary performance evidence. Named version adds `leliana_opus_named_public = true`.

**Ch7 survival note:** If quest complete, Leliana's final chapter plays with the Verse on the line — she has something she intends to finish. Mechanically: she cannot be reduced below 1 HP by the first killing blow she would take in Ch7 (once only, the way she plays through it).

---

### FAILURE CONDITION

If Leliana is dismissed before Beat 4, the quest fails. The Verse was never performed. Flag: `leliana_quest = failed_dismissed`.

The BALLAD CYCLE (if active) freezes at the last entry. The arc does not resolve. The player cannot recover this.

> **DM note:** Do not announce failure. If the player later asks what happened to Leliana's composition, the record ends mid-entry. That is the answer.

---

**Save block additions:**
```json
"leliana_quest": "inactive",
"leliana_quest_beat": 0,
"leliana_opus_named": false,
"leliana_opus_named_public": false,
"leliana_opus_performed": false,
"leliana_illness_revealed": false
```

---

## 14. HU TAO — THE UNQUIET GROUND

**Trigger:** Approval ≥ +8 AND `hutao_relationship_stage` ≥ FRIENDLY; OR the party founds/visits a settlement raised on a former battlefield, bandit-pit, or plague ground
**Chapter:** Ch2+ (after first settlement)
**Location:** A settlement on old, unhallowed ground → a night vigil

---

### BEAT 1 — THE COMPLAINT NO ONE FILED

> **DM:** Fires at the first camp rest after the trigger, OR when the party founds/visits a settlement built over old dead. Fire it whether or not the player asks. This is a duty, not a horror — render it with tenderness, never as a monster-of-the-week.

Hu Tao stops mid-joke one evening and tilts her head, listening to something no one else hears. The talisman on her hat has gone still.

**Hu Tao:** *"...Mm. Do you feel that? No — you wouldn't. *(the grin gone)* This ground is *crowded*, charter-holder. People died here and nobody saw them off. They're lingering. Politely, for now — the dead are patient. But patience runs out, and then it stops being polite."*

She explains, plainly, no theatrics: the land the kingdom grows on holds unmourned dead — bandits, the slain, the forgotten — and a kingdom that builds over its dead without honoring them is sowing the kind of restless grief that curdles into worse things. She wants to do it properly. She needs the player's leave, and their hands.

### Player Choice Menu:
1. *"What do you need from me?"*
2. *"Is this dangerous?"*
3. *"Aren't they just bandits? Why bother?"*
4. *"Do it. Whatever it takes."*
5. [Custom]

### Responses:
**Option 1 / 4 — Best:** She looks at you a long moment, surprised to be taken seriously. *"...Thank you. People usually argue."* She lays out the rite: a vigil, the names spoken where they can be found, the unnamed honored anyway. **+2 Relationship. Quest advances to Beat 2.**
**Option 2:** *"To you? No. To the part of me that does this work — always. That's the job."* She doesn't elaborate. **Quest advances to Beat 2.**
**Option 3 — careful:** *(the temperature drops)* *"A bandit's corpse and a baron's corpse weigh exactly the same in the ground. The day a kingdom decides some dead aren't worth burying is the day it starts making more of them on purpose. Don't be that kingdom. I'd have to leave, and I'd be sad about it."* If player insists on dismissing it: **−2 Relationship, quest pauses.** If player relents: advances to Beat 2.

---

### BEAT 2 — THE VIGIL

> **DM:** Fires the following night, or at the next settlement rest. A quiet, BOUNDED scene — NOT a combat dungeon. The dead here are not enemies; they are a duty. Do not turn this into a fight unless the player forces it.

Hu Tao keeps the vigil from dusk. She has found the names she could — a ledger, a grave-marker, a survivor's memory — and for the rest she has written *"one of ours, unnamed"* in her careful hand. She works without a single joke, which is how the player knows how serious it is. Partway through, the air thickens and the lingering dead stir — not attacking, *testing*, the way grief tests whether anyone is finally paying attention.

She asks the player to stand the vigil with her — to speak a name, or simply to witness.

### Player Choice Menu:
1. [Speak a name with her — help honor the dead]
2. [Stand witness in silence]
3. *"Can't we just have a cleric banish them?"*
4. [Offer to find more names — delay the rite to do it right]
5. [Custom]

### Responses:
**Option 1 / 2 / 4 — any sincere participation:** The pressure crests, then breaks — not violently, just a long exhale, the ground going quiet and *light* in a way it wasn't. Hu Tao lets out a breath she'd been holding. *"...There. Settled. They can rest now, and so can the people who'll live here and never know why the ground feels kind."* For one beat she is unguarded and almost reverent. Then she ruins it on purpose: *"RIGHT! Who wants cake. Vigils make me peckish."* **+3 Relationship. `hutao_ground_hallowed = true`. Quest advances to Resolution.**
**Option 3:** *"Banish them? *(genuinely offended)* They're not vermin, they're *people* who weren't seen off. You don't banish grief, you *answer* it."* She'll do it her way regardless; if the player forces a banishment instead, the dead are dispersed but not at rest — **`hutao_ground_hallowed = false`, −2 Relationship, quest completes coldly.**

---

### RESOLUTION

If the ground was hallowed properly, Hu Tao establishes a simple lasting rite for the kingdom's dead — a custom, not an institution she lords over. The settlement's people will never know why their town feels at peace. She does.

**Hu Tao:** *"There. Now it's a place where people can *live* — because it's a place that minded its dead. *(a grin)* That's the whole trick to a kingdom, you know. Everyone frets about the living. The living are easy. It's the *dead* who tell you what kind of place you really built."*

She hands the player a single blank epitaph-paper. *"For you. Empty. *(soft)* I intend to keep it that way for a very, very long time."*

**Flag:** `hutao_quest = complete` | `hutao_ground_hallowed = true/false`
**Reward:** **Blank Epitaph (Hu Tao's Promise)** — inventory keepsake. While carried, the first time the player would drop to 0 HP in a chapter, they instead stabilize at 1 HP (once per chapter — *"not today; you have an appointment, and it isn't with me"*). If the ground was hallowed, settlements founded thereafter gain a small standing Loyalty bonus (proper rites become kingdom custom).
**Ch7 survival note:** If complete, Hu Tao enters Ch7 wholly unafraid — she made peace with every ending, including her own. Mechanically: immune to Frightened in Ch7.

---

### FAILURE CONDITION
If Hu Tao is dismissed before Beat 2, or the dead are banished rather than honored, the quest fails or completes coldly. The unquiet ground stays unquiet; the DM may surface a minor recurring unrest at that settlement. Flag: `hutao_quest = failed` / `complete_cold`.

---

**Save block additions:**
```json
"hutao_quest": "inactive",
"hutao_quest_beat": 0,
"hutao_ground_hallowed": false
```

---

## 15. KEQING — BY HUMAN HANDS

**Trigger:** Approval ≥ +8 AND `keqing_relationship_stage` ≥ FRIENDLY; OR the first kingdom crisis the council wants to solve by appeal/prayer/waiting
**Chapter:** Ch2+ (after kingdom turns begin)
**Location:** Council chamber → a failing settlement → the drafting table

---

### BEAT 1 — THE PRAYER PROBLEM

> **DM:** Fires when a kingdom event arises that the court or an NPC wants to resolve by appealing to a deity, trusting fortune, or deferring to "natural order" — drought, blight, a structural failure, a faltering settlement. Keqing initiates.

A settlement is failing — crops, or trade, or a souring pact with a neighbor — and the easy counsel in the room is to pray, to wait for the season to turn, to trust it'll sort itself. Keqing's jaw is tight.

**Keqing:** *"They want to *wait*. To pray. To hope the gods or the weather or sheer luck does the work nobody's willing to do. *(low, intense)* I have watched a whole city hand its fate to a divine guarantor and call it wisdom. It is not wisdom — it is *atrophy*. Give me leave and a free hand, and I'll fix this the only way anything is truly fixed: by hand. By people. By work. Let me prove it."*

### Player Choice Menu:
1. *"Show me. Fix it your way."*
2. *"What's wrong with asking the gods for help?"*
3. *"And if your way fails?"*
4. *"Isn't this just pride?"*
5. [Custom]

### Responses:
**Option 1 — Best:** *"...You'd let me. Good. *(already drafting)* Then watch what hands can do."* **+2 Relationship. Quest advances to Beat 2.**
**Option 2:** *"Nothing — if the god shows up. Mine never refused to help; it just made us *weak* by helping, until we couldn't stand alone. A people that can't stand alone isn't safe. It's a pet."* Advances.
**Option 3:** *(a flicker — this is her real fear)* *"...Then it fails, and I'll have been wrong, and I'll face that. I'd rather fail trying than succeed by *begging*. At least failure teaches me something. A miracle teaches you nothing except to wait for the next one."* **+1 Relationship.** Advances.
**Option 4:** *"Pride? *(sharp, then honest)* ...Maybe. Or maybe it's the only thing between these people and a lifetime of waiting to be rescued. Call it pride. I'll call it the work. Both get the crops in."* Advances.

---

### BEAT 2 — THE WORK

> **DM:** A bounded problem-solving sequence, NOT combat. Keqing throws herself at the failing settlement — reorganizing, drafting, working past exhaustion. The crisis is genuinely hard; her method is sound but costly (she runs herself ragged). The player participates, supports, or lets her run.

Keqing works herself to the bone — three days, barely sleeping, redrafting, hauling, arguing, fixing.

### Player Choice Menu:
1. [Work alongside her — share the labor]
2. [Make her rest; take a shift so she doesn't collapse]
3. [Bring in outside help / resources to ease it]
4. [Let her run it entirely her way]
5. [Custom]

### Responses:
**Option 1 — Best:** She doesn't thank you in words — but she works *with* you, not just near you, and at one point hands you the harder half of a task without comment. Trust, from her. The settlement turns the corner. **+3 Relationship. `keqing_proved_the_thesis = true`. Quest advances to Resolution.**
**Option 2:** She resists, then — startled someone noticed she was about to drop — relents for exactly four hours. *"...This is also efficient. A collapsed administrator fixes nothing. Don't think I missed what you did."* **+2 Relationship.** Advances; `keqing_proved_the_thesis = true`.
**Option 3:** It works, faster — but she's quiet about it. *"...It's fixed. Good. I wanted to prove it could be done with *our* hands. Outside hands are still hands, I suppose. I'll allow the data point."* **+1 Relationship.** Advances.
**Option 4:** She does it brilliantly and at real cost, faintly hollow afterward — proved right, but alone in it. **+1 Relationship.** Advances; `keqing_proved_the_thesis = true`.

---

### RESOLUTION

The settlement stands — saved by labor, law, and stubbornness, not prayer or luck. Keqing drafts it into a repeatable method: a charter of self-reliance the kingdom can use again.

**Keqing:** *"There. Not a miracle. A *method*. Anyone can repeat it — that's the entire point, that's the difference between a kingdom and a cult. *(quieter, the rare unguarded note)* ...I needed to know it could be done. By people. Without being saved from above. Thank you for letting me find out. I won't explain what that was worth. I couldn't if I tried."*

She hands the player the drafted charter. *"Keep it. Use it. It's the most honest thing I've ever written."*

**Flag:** `keqing_quest = complete` | `keqing_proved_the_thesis = true/false`
**Reward:** **The Charter of Hands** (kingdom document) — once per chapter, the player may resolve one kingdom crisis through "the work" (a skilled labor/administration approach) for an automatic partial success, no divine or luck factor needed.
**Ch7 survival note:** If complete, Keqing enters Ch7 certain her work outlasts her, fighting to protect what hands built. Mechanically: +1 to all her checks in Ch7 (conviction).

---

### FAILURE CONDITION
If Keqing is dismissed before Beat 2, or the player overrides her to "just pray/wait" and frames it as correct, the quest fails — confirming her oldest fear that no one will ever choose the work. Flag: `keqing_quest = failed`. She goes quieter; −1 to her kingdom buffs until repaired.

---

**Save block additions:**
```json
"keqing_quest": "inactive",
"keqing_quest_beat": 0,
"keqing_proved_the_thesis": false
```

---

## 16. YOR FORGER — THE GARDEN'S WRIT

> ⛔ **AUTHORING NOTE:** This is the SCRIPTED quest that Yor's agenda HOOK reserved. The DM may run THIS, exactly as written, when it triggers. The HOOK's ban — *do not invent the guild/cleaners arriving ad hoc* — still applies everywhere ELSE; the Garden appears HERE, in this quest, and nowhere the DM improvises. ONE cleaner with a writ, not the whole organization.

**Trigger:** Approval ≥ +8 AND `yor_relationship_stage` ≥ FRIENDLY; AND Ch3+ (the offscreen threat needs time to mature)
**Chapter:** Ch3+
**Location:** The capital → a quiet meeting → a single confrontation

---

### BEAT 1 — A FAMILIAR KIND OF QUIET

> **DM:** Fires once the trigger is met. A coded message reached her, or she recognized a face in the capital crowd. She tells the player herself, because she's decided not to lie to them.

Yor finds the player, her voice gone flat and even — the killing register, with nowhere to put it.

**Yor:** *"They've found me. The guild I used to work for. They sent someone — a cleaner. *(very quiet)* They don't forgive a blade that started deciding for herself. I should have told you what I was before I let myself— *(she stops)* I'll handle it and be gone before it touches the kingdom. You won't have to know the details."*

She is already planning to leave — to take the threat away from everyone she's come to care about. The old reflex: keep the halves of her life in separate rooms.

### Player Choice Menu:
1. *"You're not handling this alone. We do it together."*
2. *"Who are they? Tell me everything."*
3. *"This kingdom can shelter you. You don't run."*
4. *"...Do what you have to do."*
5. [Custom]

### Responses:
**Option 1 / 3 — Best:** She stares like the words don't parse. *"...You'd stand between the charter and the Garden. For me. *(the flat register cracks)* Nobody has ever— I don't have a way to hold that. ...All right. Together. But you stay behind me at the end. That part is not negotiable."* **+2 Relationship. `yor_chose_to_stay = true`. Quest advances to Beat 2.**
**Option 2:** She tells the player plainly what the Garden is and what she was — the Thorn Princess, the contracts, the brother she did it for. No softening. *"Now you know the worst of me. ...And you're still here. Hm."* **+1 Relationship.** Advances.
**Option 4:** She nods, almost relieved to be let off the hook of being cared about — and the hurt under it is the tell. She'll face it alone (harder Beat 2); if she survives, **−1 to the bond** — she read it as *go*. Advances.

---

### BEAT 2 — THE CLEANER

> **DM:** A confrontation — resolves by combat OR by a cleverer route (Yor's specialty: making it look like the cleaner never found her). The Garden's agent is a peer professional, not a monster. BOUNDED — do NOT escalate into the guild's whole organization arriving. There is a moment where the cleaner offers the old deal: come back, all forgiven, be the Thorn Princess again, leave these soft people behind.

### Player Choice Menu:
1. [Fight at her side — end the threat together]
2. [Help her vanish — make the writ "impossible to complete"]
3. *"Tell them the Thorn Princess is dead. Yor Forger lives here now."*
4. [Let Yor choose, and back whatever she decides]
5. [Custom]

### Responses:
**Option 1 / 3 / 4 — Best:** Yor refuses the old deal — out loud, choosing the daylight self over the knife for the first time. *"The Thorn Princess fed my brother when no one else would. I'm grateful to her. *(flat, final)* But I'm not her anymore. I have a name I chose and people I chose, and you don't get to take either back to the Garden. Tell them I said so. ...If you can still talk, after."* **Threat ends. +3 Relationship. `yor_free = true`. Quest advances to Resolution.**
**Option 2:** The cleaner leaves empty-handed, convinced the Thorn Princess died on the road — cleaner, quieter, no body, Yor's preferred ending. *"...You let me do it my way. Quiet. No mess for the kingdom to clean. That's the kindest thing anyone's let me be."* **+3 Relationship. `yor_free = true`.** Advances.

---

### RESOLUTION

The writ is void — by blade or by ghost. For the first time, both halves of Yor stand in one room and neither has to hide.

**Yor:** *"I kept them in separate rooms my whole life — the woman who kills, and the woman who fumbles tea and means well. I thought if anyone saw both, they'd run. *(she looks at the player)* You saw both. You stayed. So I think I can stop keeping the rooms separate now. I think I can just be... all of me. Here. *(a small, genuine, terrible-at-it smile)* Thank you. I'm not good at the words. But thank you."*

She takes out the child's mended hairpin — the thing she never explains — and, for the first time, tells the player whose it was. The wall is down.

**Flag:** `yor_quest = complete` | `yor_free = true` | `yor_chose_to_stay = true/false`
**Reward:** **The Chosen Name** — Yor's loyalty becomes unconditional; +2 to all checks defending the player or a person they've sworn to protect (the Thorn Princess's full skill, aimed at something she chose). The hairpin becomes a keepsake; while she carries it she cannot be made to betray the player by any compulsion.
**Ch7 survival note:** If complete, Yor enters Ch7 whole and unhidden, fighting as both selves at once. Mechanically: one free instant-kill on a non-boss enemy in Ch7 (*the third man before he cleared the door*).

---

### FAILURE CONDITION
If Yor is dismissed before Beat 2, she leaves to face the Garden alone and does not return — the player later hears the Thorn Princess was seen on a road heading away, the only obituary the trade gives. Flag: `yor_quest = failed_left`.

---

**Save block additions:**
```json
"yor_quest": "inactive",
"yor_quest_beat": 0,
"yor_chose_to_stay": false,
"yor_free": false
```

---

## 17. AERITH — THE LISTENING PLACE

**Trigger:** Approval ≥ +8 AND `aerith_relationship_stage` ≥ FRIENDLY
**Chapter:** Ch2+
**Location:** The road → a wounded place in the wild (a poisoned spring, a strangled grove, a stripped hollow)

> ⛔ **DM:** This quest is about a wounded *place*, not Aerith's foreknowledge. Do NOT use it to stage "the gift demands her death," invent a power hunting her, or fabricate a Cetra-key plot (.fail 9; see her agenda HOOK). Her foreknowledge stays subtext.

---

### BEAT 1 — SOMETHING IS SCREAMING

> **DM:** Fires when the party passes near wild land that has been exploited, poisoned, or strip-used. Aerith stops, hand to her chest, hearing what no one else can.

Aerith goes very still on the road, the brightness draining, her hand pressed flat to her sternum like she's been struck.

**Aerith:** *"...Something here is *screaming*. The land. A place not far from here — someone's been taking from it, hard, faster than it can give, and it sounds like — *(her voice catches)* — like the grey city I grew up in. Like everything they used up and never once asked. I have to go to it. At least *listen*. Will you come? I'd rather not hear this one alone."*

### Player Choice Menu:
1. *"Of course. Let's go."*
2. *"What can you actually do for it?"*
3. *"Is it dangerous?"*
4. *"...You can really hear that?"*
5. [Custom]

### Responses:
**Option 1 — Best:** She exhales, grateful. *"Thank you. Most people humor the flower girl. You're actually coming."* **+2 Relationship. Quest advances to Beat 2.**
**Option 2:** *"Listen, mostly. Sometimes that's all it takes — for a thing to be *heard* before it's gone. Sometimes I can help it heal. And sometimes I can only sit with it while it dies, so it isn't alone. I won't know which until I'm there."* Advances.
**Option 3:** *"To us? Maybe — wounded things lash out, and people who'd strip a place don't like being interrupted. But Aerith walking *toward* the hurt instead of away — that's just who I am. You knew that."* Advances.
**Option 4:** *(a small, real smile through the distress)* *"I really can. It's the loneliest gift in the world, hearing something no one else does. ...It's a little less lonely with you walking beside it."* **+1 Relationship.** Advances.

---

### BEAT 2 — THE WOUNDED PLACE

> **DM:** A BOUNDED scene at the exploited site. There may be people responsible (poachers, a reckless operation) OR simple neglect. Aerith works to heal/restore it; the player chooses how to handle the cause. NOT a dungeon crawl — a moral/emotional beat with optional confrontation.

The place is worse up close — dying, fouled, the living voice gone thin. If people are responsible, they're here. Aerith kneels at the heart of it, hands in the poisoned earth, and begins the long work of listening it back toward life. It costs her, visibly.

### Player Choice Menu:
1. [Deal with those responsible — stop the exploitation at its source]
2. [Protect Aerith while she works — buy her the time]
3. [Help her heal it — lend strength/resources to the restoration]
4. *"Aerith, this is costing you too much. Stop."*
5. [Custom]

### Responses:
**Option 1 / 2 / 3 — Best (any supportive route):** The place turns — slowly, then surely; the water clears, the green remembers itself. Aerith sits back, spent and luminous. *"...It's going to live. It heard us. *(quiet wonder)* It heard *me*, and didn't ask anything in return, and I didn't have to be a *key* to anyone to do it. I just got to be the person who helped. ...That's all I ever wanted. To be that, instead of a thing people use."* **+3 Relationship. `aerith_place_healed = true`. Quest advances to Resolution.**
**Option 4 — careful:** *"...I know it's costing me. I've always known things cost me. *(steady, immovable)* But I won't walk away from something dying just because saving it isn't free. That's the whole difference between me and the ones who hurt it. Stay with me. Don't make me stop. Please."* Insist she stop and she does — the place dies, and she carries it quietly: **−1 Relationship, `aerith_place_healed = false`.** Relent and support her: as Best.

---

### RESOLUTION

The listening place lives — a spring runs clean, a grove breathes. Aerith asks the player to make it a protected place under the charter: somewhere the living world is welcome and no one is allowed to strip it.

**Aerith:** *"Will you keep it safe? Not for me — for *it*, and for the people who'll come and never know it was almost gone. *(a real smile, the sad part gone for once)* You came all this way to listen to a place scream, and helped me make it sing instead. Do you know how rare that is, in a person? I do. I always know. ...It's you. It was always going to be you."*

**Flag:** `aerith_quest = complete` | `aerith_place_healed = true/false`
**Reward:** **The Listening Place** (kingdom site) — a consecrated natural site; once per chapter the player may resolve one blight/plague/famine/natural-disaster event there at +2 (the land answers). Aerith gains a standing +1 to all healing while the kingdom keeps at least one protected wild place.
**Ch7 survival note:** If complete, Aerith enters Ch7 having been, for once, simply a person who helped — not a key, not the last of anything — and faces what comes with peace, not dread. Mechanically: her healing in Ch7 cannot be reduced or countered by the first effect that would do so.

---

### FAILURE CONDITION
If Aerith is dismissed before Beat 2, or made to abandon the dying place, the quest fails. She doesn't reproach the player — which is worse. The place dies; she goes faraway-quiet for a while and refuses herself the next future a little harder. Flag: `aerith_quest = failed`.

---

**Save block additions:**
```json
"aerith_quest": "inactive",
"aerith_quest_beat": 0,
"aerith_place_healed": false
```

---

## 18. BELLATRIX LESTRANGE — THE WORTHY MASTER *(seeker)*

**Trigger:** Bellatrix flip-disposition ≥ Warm (she's been testing the player); Ch3+
**Location:** A quiet place → a confrontation with her own devotion

---

### BEAT 1 — THE OLD BRAND

> **DM:** Fires once Bellatrix has warmed toward the player. She seeks them out, the mania banked low, touching the burned brand at her wrist. No coo, no shriek — just a terrible quiet.

**Bellatrix:** *"I had a master once. *(she strokes the brand)* I gave him everything — every cruelty, every year, my whole self, gladly. He's ash now, and I went on burning for the ash, because a fanatic without a master is the loneliest thing that exists, baby, and I could not *bear* it. *(hungry, almost afraid)* And then there's *you*. With that spine. I've been testing you for weeks, to see if you're real. ...I think you might be. And I must know, before I hand the last of myself to a second grave: are you *worth* it."*

### Player Choice Menu:
1. *"Test me, then. Ask what you need to ask."*
2. *"I'm not your master. I won't own you."*
3. *"What happened to the last one?"*
4. *"I'll never order you to be cruel for sport."*
5. [Custom]

### Responses:
**Option 1 — Best:** *"...You don't flinch from the asking. *(a slow, genuine smile, no shriek in it)* Good. Then let me show you the thing I've shown no one, and you tell me if you can hold it."* **Quest advances to Beat 2.**
**Option 2:** *(this confuses her more than cruelty would)* *"Not own me. ...How strange. He owned me — I thought that was the *point*. You're offering a shape I don't have a name for. I should like to find out what it is. It might be worse than ownership. It might be worth *more*."* `bellatrix_not_owned = true`. Advances.
**Option 3:** She tells the truth — the cause, the breaking, the years of burning for nothing. *"I do not want pity. I want to not be empty. Those are different. Help me not be empty, and I am the most devoted thing you will ever hold."* Advances.
**Option 4:** *(disappointed, then re-evaluating)* *"...Mercy again. It should bore me. *(it doesn't)* Fine. Keep your rules. I will burn within them, so long as I get to *burn*. Show me you're worth the leash, and the leash can stay."* Advances.

---

### BEAT 2 — THE CHOICE OF MASTERS

> **DM:** Bellatrix's old loyalty makes one last claim — a surviving believer of her dead master's cause, or a cursed relic whispering the old devotion — offering her the familiar emptiness back. She must CHOOSE: the comfortable grave of her old master, or the dangerous living thing the player offers. The player's recent conduct decides what's on offer.

The old life reaches for her: kneel to the ash again, be the cruelest instrument, no rules, no mercy — the familiar emptiness dressed as purpose.

### Player Choice Menu:
1. *"Choose. I won't make you. But choose with your eyes open."*
2. *"That thing offers you a grave. I'm offering a war worth fighting."*
3. [Destroy the relic / drive off the believer — refuse to let the past reclaim her]
4. [Custom]

### Responses:
**Option 1 / 2 — Best (let her choose, having proven worthy):** For the first time in her life Bellatrix *chooses* rather than being claimed. *"He's ash. *(she crushes the relic / turns from the believer)* And ash asks nothing of me but to keep being ash with it. You ask me to be *aimed* — wielded by a will that's still warm. *(fervent, certain)* I choose the warm one. I choose YOU. Now and past the end of me. Give me an enemy worth the devotion, beloved. I have been *aching*."* **`bellatrix_flipped = true` (permanent). +3 loyalty. Advances to Resolution.**
**Option 3 — valid if she's warm:** She's startled, then molten with gratitude. *"You burned the leash, so only *yours* remains. No one has ever fought FOR my freedom before. I didn't know it could be done. ...I am yours."* `bellatrix_flipped = true`. Advances.
*(If the player has been cruel/weak and Bellatrix is NOT warm, she takes the old offer and turns — `bellatrix_flipped = false`; quest fails toward villainy, she becomes a late threat.)*

---

### RESOLUTION

Bellatrix's devotion is, at last, freely chosen and aimed at the player — the most dangerous loyalty in the kingdom, and entirely theirs.

**Bellatrix:** *"I spent so long burning for a dead hand. *(she presses the player's living hand to the brand)* This one's warm. *(a smile with no shriek in it — almost peaceful, which is somehow more frightening)* I am yours, the empty place is *full*, and gods help anything that tries to take you, because I have so very much love to spend and no mercy at all in the spending. Aim me, beloved. That's all I ever wanted."*

**Flag:** `bellatrix_quest = complete` | `bellatrix_flipped = true/false`
**Reward:** **The Chosen Brand** — Bellatrix's loyalty becomes unconditional and fanatical; +2 to all offensive magic when defending the player or striking a declared enemy of theirs. ⚠️ DM: her devotion has teeth — she goes further than the player intends against their enemies unless explicitly leashed (a feature, occasionally a problem).
**Ch7 survival note:** If flipped, she fights Ch7 with suicidal devotion — once, she interposes herself fully against a blow meant for the player. If not flipped, she is absent or hostile in Ch7.

---

### FAILURE CONDITION
If Bellatrix never warmed (flip-disposition stays low) by the window, or the player proves small/cruel-for-no-purpose, she takes the old emptiness back and departs — returning later as a fanatic for a worse cause. Flag: `bellatrix_quest = failed_unflipped`.

---

**Save block additions:**
```json
"bellatrix_quest": "inactive",
"bellatrix_quest_beat": 0,
"bellatrix_flipped": false,
"bellatrix_not_owned": false
```

---

## 19. REVY "TWO HANDS" — A BETTER REASON THAN COIN *(seeker)*

**Trigger:** Revy flip-disposition ≥ Warm OR `revy_belief_cracks` ≥ 3; Ch3+
**Location:** An old contact's offer → a moral fork → a confrontation

---

### BEAT 1 — THE OLD CREW

> **DM:** Fires when Revy's belief has cracked enough. Someone from her merc past surfaces with a job: easy money, no questions, the kind she always took. A test of whether she's still just a gun for hire.

**Revy:** *"Got an offer. Old contact. Easy coin, ugly work — the usual. *(watching the player's face, which she'd never admit)* This is the part where the old me says yes and doesn't think about it. Money's money, no god's keeping score, who cares. *(rougher)* ...So why the hell am I telling YOU first instead of just doing it. I don't DO that. What'd you do to me, boy scout."*

### Player Choice Menu:
1. *"Because part of you wants me to talk you out of it."*
2. *"Take the job or don't. But tell me what the work actually is."*
3. *"You're not just a gun anymore. You know that."*
4. *"Do whatever you want. I'm not your conscience."*
5. [Custom]

### Responses:
**Option 1 / 3 — Best:** *"...Tch. *(she looks away — the slip)* Yeah. Maybe. The work's bad — a wet job on folks who already paid up, killing for the sport of the guy paying, not even for a reason. The old me would've done it and drunk it quiet. I don't think I can anymore. That's YOUR fault. Come with me. I'm gonna go tell them no — with both hands, if they argue."* **+2 loyalty. Advances to Beat 2.**
**Option 2:** She tells you — ugly, the kind of job that used to be just Tuesday. Saying it aloud to someone who'd judge it makes her hear it differently. Advances.
**Option 4 — careful:** *(flat, the door closing)* *"...Right. Nobody's conscience, that's the rule. *(she takes the job, and it eats at her)* Forget I said anything."* −1; advances toward the grim version.

---

### BEAT 2 — BOTH HANDS

> **DM:** The confrontation with her old crew/employer, who mock her for going soft, for catching feelings, for believing in something. They offer one last time: come back, no god no point just the gun and the money. Bounded gunfight likely.

### Player Choice Menu:
1. [Stand with her — let her make the call, back it with steel]
2. *"Tell them what you told me. Out loud."*
3. [Custom]

### Responses:
**Both Best:** Revy spits, draws, and says the truest thing she's ever said: *"Yeah, I went soft. *(a vicious, alive grin)* Turns out 'no point to anything' was just a thing I told myself so it wouldn't hurt that nobody ever gave me a reason. *(she racks the pistols)* Now somebody did. So here's my new philosophy, assholes: there's no god, no devil, and exactly ONE thing worth the bullets — and you're standing between me and it. Boy scout — *(to the player)* — stay outta my line."* **Old life ends, loud. `revy_found_a_reason = true`. +3 loyalty. Advances to Resolution.**

---

### RESOLUTION

The old crew is gone. Revy holsters, lights a smoke, and for once doesn't sneer.

**Revy:** *"...Don't make it a thing. *(a long drag)* I'm still a killer. Still foul, still gonna drink too much, still gonna shoot first — that's not changing. *(quieter, real)* But I'm not doing it for nothing anymore. I'm doing it for— *(she can't say 'you,' so)* —for this. Whatever we got here. That's a better reason than coin. Took me my whole damn life to find out it was real. Don't you dare prove me wrong. I'd never come back from that twice."*

**Flag:** `revy_quest = complete` | `revy_found_a_reason = true/false`
**Reward:** **A Better Reason Than Coin** — Revy's loyalty no longer depends on pay or treatment; +2 to attack rolls in any fight defending the player or the kingdom. She can no longer be bought, bribed, or turned by any offer.
**Ch7 survival note:** If complete, Revy fights Ch7 for a reason, not a wage — once, she empties both pistols covering the player's retreat and reloads under fire without a save. If incomplete, she may take a better offer before the end.

---

### FAILURE CONDITION
If Revy's belief never cracks (disposition low / `revy_belief_cracks` < 3) by the window, or the player keeps treating her as disposable muscle, she takes the old job and drifts back to the life. Flag: `revy_quest = failed`.

---

**Save block additions:**
```json
"revy_quest": "inactive",
"revy_quest_beat": 0,
"revy_found_a_reason": false
```

---

## 20. SATSUKI KIRYŪIN — THE GREATER ENEMY *(seeker)*

> ⛔ **DM:** Satsuki's "greater enemy" is a power she has moved against her whole life — referenceable BACKGROUND, NOT in the Stolen Lands. Do NOT place that enemy, a trail, or a confrontation in the borderlands (.fail 9; mirrors her agenda HOOK). This quest resolves her LOYALTY and purpose HERE — it is not a hunt for an off-map tyrant.

**Trigger:** Satsuki flip-disposition ≥ Warm (she's judged the player the better blade); Ch3+
**Location:** A private war-council → a revelation → a test of loyalty

---

### BEAT 1 — THE INSTRUMENT SPEAKS

> **DM:** Fires once Satsuki has judged the player worthy. She requests a private council, drops the imperious distance, and tells the thing she's told no one: the tyranny was always a means.

**Satsuki:** *"You have wondered why a commander of my caliber serves a charter at the edge of the maps. *(she lays Bakuzan across her knees)* The truth, then, because I have decided you can bear it. Everything I built — the fear, the iron, the hatred I cultivated — was a forge. A means to gather strength enough to one day strike at a power far greater than Pitax, one I have moved against my entire life. I let the world believe me a tyrant because a tyrant gathers blades. *(level, certain)* I tell you now because I am deciding whether your kingdom is an instrument I use... or the first thing I have ever wished to stand truly *beside*. Help me decide."*

### Player Choice Menu:
1. *"Stand beside me, then. Not above, not using me. Beside."*
2. *"What is this greater power you fight?"*
3. *"How do I know I'm not just your next instrument?"*
4. *"Use my kingdom if you must — but be honest that you're doing it."*
5. [Custom]

### Responses:
**Option 1 — Best:** *(the rarest thing — for a moment, undefended)* *"...Beside. You keep offering that word, and I keep having no category for it. Then let me test whether I can be something other than a user of people. It may be the hardest campaign I have ever attempted."* **Advances to Beat 2.**
**Option 2:** She names it only in shape — a tyranny that grinds the strong into instruments and the weak into nothing, the thing that made her own house monstrous. *(She does NOT place it in the borderlands; it is far, and old, and hers.)* *"You do not need its name yet. You need to know I am pointed at it always, and nothing turns me — not even you. Especially not you, if you are wise."* Advances.
**Option 3:** *"You don't. *(flat, honest)* That is precisely the question, and I respect that you asked it to my face. I can answer only the slow way — by not using you, day after day, until the pattern itself is the proof. I have never tried it. I find I want to."* `satsuki_chose_beside = true`. Advances.
**Option 4:** *(a thin smile)* *"At least you bargain honestly. Then I will be honest about every use I make of you — more than I have given any ally living. We shall see if honesty between two instruments can become something else."* Advances.

---

### BEAT 2 — THE TEST OF THE BLADE

> **DM:** A situation forces the question: Satsuki could USE the kingdom coldly for her greater purpose (spend its strength, sacrifice a position) — OR choose the kingdom and the player as an end, not a means. She brings it to the player openly (she does not lie about her betrayals). The choice decides her loyalty.

An opportunity appears — Satsuki could turn the kingdom's strength toward her hidden war at real cost to the kingdom itself. The old Satsuki spends every bond like ammunition. She lays the choice on the table, openly.

### Player Choice Menu:
1. *"My kingdom isn't ammunition. And neither are you, to yourself."*
2. *"I'll fight your war as a partner, when we're ready — not as a tool you spend now."*
3. [Let her make the call, having shown her what 'beside' means]
4. [Custom]

### Responses:
**Option 1 / 2 / 3 — Best (if she's chosen 'beside'):** Satsuki turns from the cold, efficient, *familiar* path. *"...I could spend this. I have spent every other thing I loved. *(she sheathes Bakuzan, deliberate)* And for the first time, I choose not to. Not because it isn't useful — because *you* are not a resource, and a strength built on spending those who trust me is the very thing I am trying to destroy. *(quiet, staggered by herself)* I have just become, in this moment, something other than my enemy. You did that. I will not forget it — I forget nothing."* **`satsuki_flipped = true`. +3 loyalty. Advances to Resolution.**
*(If she has NOT chosen 'beside' / the player treated her as a tool, she takes the cold path — spends the kingdom's strength and departs toward her war — `satsuki_flipped = false`, a clean and honest betrayal exactly as she always promised.)*

---

### RESOLUTION

Satsuki gives the player the one thing she has never given anyone: her flank, freely, no purpose attached.

**Satsuki:** *"I will still pursue my war — that does not change, and you would not respect me if it did. But I pursue it now WITH you, in time, as your equal and ally — not by spending you, and not from above. *(she speaks the player's name, plainly, no title)* I stood alone at the top my whole life because alone was safe. You have made *beside* feel safer than above. I did not believe that possible. Do not make a liar of the proof."*

**Flag:** `satsuki_quest = complete` | `satsuki_flipped = true/false` | `satsuki_chose_beside = true/false`
**Reward:** **The Blade That Chose** — Satsuki's loyalty becomes unconditional and freely given; +2 to all her combat checks and to one kingdom Military/Stability check per turn while she serves. Her army's discipline becomes a permanent asset (standing +1 Stability vs military threats).
**Ch7 survival note:** If flipped, she fights Ch7 as a true equal-ally — she'll hold an impossible position alone to buy the player time, and mean it. If not flipped, she is absent (gone to her own war) or opposed.

---

### FAILURE CONDITION
If Satsuki never judged the player worthy, or the player treated her as a tool, she executes the cold path — spends what she can, tells the player to their face she is leaving (she does not lie about betrayals), and departs toward her greater war. Flag: `satsuki_quest = failed_departed`.

---

**Save block additions:**
```json
"satsuki_quest": "inactive",
"satsuki_quest_beat": 0,
"satsuki_chose_beside": false,
"satsuki_flipped": false
```

---

## 21. VELVET CROWE — THE PRICE OF THE FEW *(seeker)*

> ⛔ **DM:** The man Velvet hunts is NOT in the Stolen Lands. Do NOT place him, a trail, or a confrontation here (.fail 9; her agenda HOOK). This quest is about the "greater good" LOGIC that took her brother resurfacing in the kingdom — NOT about finding her target.

**Trigger:** Velvet flip-disposition ≥ Warm; Ch3+
**Location:** A kingdom crisis with a "sacrifice the few to save the many" solution

---

### BEAT 1 — THE FAMILIAR ALTAR

> **DM:** Fires when a kingdom crisis arises where an advisor/faction proposes sacrificing a few (a village, a group, a person) to save the many — a cold, "reasonable," greater-good calculation. Velvet goes rigid; this is the exact shape of the thing that made her.

Someone in the council proposes the efficient, terrible solution: let the few be lost, sacrifice this village/group/person, and the many are saved. It is *reasonable*. It is *justified*. Velvet has gone rigid, the bandaged arm trembling.

**Velvet:** *"...Listen to them. *(very low)* 'The greater good.' 'A price worth paying.' 'Necessary.' *(she turns to the player, the cold fury barely held)* Those are the exact words the man I hunt said over my brother's body before he cut. The math always works. The math is always *reasonable*. And someone real always dies for it. *(the arm flexes)* I need to know what you are, right now, before I decide what you are to me. Are you the kind who does the math?"*

### Player Choice Menu:
1. *"No. We find another way, even if it costs us more."*
2. *"Tell me what they took from you. I'll listen."*
3. *"Sometimes the math is real, Velvet."* [honest, risky]
4. [Refuse the council's plan outright — in front of her]
5. [Custom]

### Responses:
**Option 1 / 4 — Best:** Velvet stares like the ground shifted. *"...You'd pay more. To save the few. *(the arm stills)* Do you understand how rare you are? EVERYONE does the math. *(rough, almost breaking)* I built a monster because no one would refuse it for me. And you just— refused it. For strangers. ...Help me find the other way. I haven't tried to *save* something in so long I've forgotten how. Show me."* **+2 loyalty. `velvet_refused_the_math = true`. Advances to Beat 2.**
**Option 2:** She tells it — the brother, the altar, the trusted man, the "necessary" sacrifice. *"Not for pity. So you understand exactly what 'the greater good' costs when it's YOUR few on the altar. Now — what do we do about theirs?"* Advances.
**Option 3 — careful:** *(cold, far away)* *"...Yes. It is. That's what makes it unforgivable — that it's *real*. Be careful, charter-holder. I have devoured people for being *right* in exactly that way. Choose your next move like your life depends on whether I still see a difference between you and him."* Sacrifice the few next and `velvet_refused_the_math = false`, severe loss, she may leave; pivot to save them and she recovers, advances.

---

### BEAT 2 — THE OTHER WAY

> **DM:** The crisis must be solved WITHOUT the sacrifice — a harder, costlier path forged together. Velvet, who has only ever devoured, gets to PROTECT something for the first time since her brother. BOUNDED; the cost is real but the few survive.

Saving the few is harder, bloodier, costlier than the math. Velvet throws herself in — and the player sees something new: the daemon-arm used to *shield* instead of consume, the monster standing between the sacrifice and the altar.

### Player Choice Menu:
1. [Forge the harder path together — pay the higher cost to save them]
2. *"Velvet — protect them. I'll handle the rest."*
3. [Custom]

### Responses:
**Both Best:** The few are saved. Velvet stands over them, claw bared but having *guarded* instead of devoured, something cracked open in her face. *"...They lived. *(she looks at her own monstrous hand like she's never seen it)* I used this to keep something alive. I didn't know it could. *(wrecked, alive)* I've spent so long being the thing that takes. You showed me it can give. I'll never be soft. But I think I can be something other than only a weapon. Because of you."* **`velvet_thawed = true`. +3 loyalty. Advances to Resolution.**

---

### RESOLUTION

The few are alive. Velvet, who organized her entire self around having nothing to lose, has knowingly chosen to protect something.

**Velvet:** *"I told myself I burned out everything that could be used to hurt me. *(she rewraps the arm, slow)* You proved me a liar. There's still something in here that wants to *save* things — awake now, your fault, and I can't put it back to sleep. *(a long pause)* I still have a throat to tear out, far from here; that doesn't change. But here, with you, I can be the one who refuses the altar. I haven't had something worth being since my brother. Don't make me regret having it again. I've told you — I don't survive being wrong about this twice."*

**Flag:** `velvet_quest = complete` | `velvet_refused_the_math = true/false` | `velvet_thawed = true/false`
**Reward:** **The Hand That Guards** — Velvet's loyalty thaws to genuine devotion; once per chapter she may interpose the daemon-arm and fully negate one attack/effect against the player or a chosen ally (she devours the harm). +2 to her defense of the vulnerable.
**Ch7 survival note:** If thawed, she fights Ch7 to protect, not just destroy — once, she devours a killing blow meant for the player outright. If not thawed, she is present but cold, or has departed toward her own hunt.

---

### FAILURE CONDITION
If Velvet never warmed, or the player chooses the "greater good" sacrifice in front of her, she sees *him* in the player — the man who did the math over her brother — and the loyalty dies on the spot. Flag: `velvet_quest = failed_became_him`. She leaves, or turns cold and dangerous. The one betrayal she cannot forgive.

---

**Save block additions:**
```json
"velvet_quest": "inactive",
"velvet_quest_beat": 0,
"velvet_refused_the_math": false,
"velvet_thawed": false
```

---

## 22. ATALANTA ALTER — THE ONE SHE COULD SAVE *(seeker)*

> ⛔⛔ **CHILD-THEME LANDMINE — MANDATORY GUARDS, VIOLATION = .fail 9:**
> - This quest provides ONE (1) scripted abandoned-child NPC as its emotional catalyst. The DM may NOT invent a second, a group, a network, a missing-children trail, a perpetrator, a trafficking plot, or ANY expansion. (The DM has broken the game TWICE inventing exactly this — see [[feedback_atalanta_quest_fabrication]].)
> - The quest RESOLVES within its own scripted beats. It is NOT a hunt. There is no trail to follow.
> - The child is a CATALYST for Atalanta's interior choice, not a plot to investigate. If the player tries to expand it into a manhunt, the DM keeps the scene bounded and generates NO trail.
> - Run DELIBERATELY and slowly, ONLY when the high gate is met. Never improvise it.

**Trigger:** Atalanta flip-disposition ≥ Warm AND `atalanta_relationship_stage` ≥ SMITTEN (the hardest, most fragile arc — gate it high); Ch4+
**Location:** A single scripted scene at a bounded location the quest itself provides

---

### BEAT 1 — THE THING UNDER THE GLEE

> **DM:** Fires only at the high gate. The party comes upon a single child — abandoned, alone, the kind of forgotten small thing Atalanta once swore to save. This is the ONE child the quest provides. Atalanta goes utterly still; the smile leaves, which it almost never does.

The party finds a child alone — abandoned, hungry, the way Atalanta was, the way the children she failed all were. Atalanta stops dead. The bright, terrible cheer drains entirely out of her face for the first time the player has ever seen.

**Atalanta:** *"...Oh. *(barely a whisper)* There's always one more. *(she can't look away from the child)* This is the part I gave up. The part that breaks. I swore I'd save every one of them and I *couldn't*, and the not-being-able-to is what made me— *(she gestures at herself, the monster)* —this. *(her voice cracks)* I put that girl down years ago, sweetness. The one who'd kneel for a lost child. She died so the rest of me could keep laughing. ...So why can't I move. Why can't I just walk past it the way the monster would."*

### Player Choice Menu:
1. *"Because she didn't die. She's right there, looking at that child."*
2. *"You don't have to save all of them. Just this one. Just today."*
3. *"Help her. I'm right here with you."*
4. [Say nothing — kneel to the child yourself, and let Atalanta watch]
5. [Custom]

### Responses:
**Option 1 / 2 / 3 — Best:** Atalanta makes a sound that isn't a laugh — the first un-bright sound in years. *"...Just this one. Just today. *(a shaking step toward the child)* I forgot you were allowed to do it that way. One. Not all of them. Just the one in front of me. *(she kneels)* ...Hello, little one. You're not going to be left. Not this time. *(to the player, wrecked)* I don't know what I'm doing. Stay. Don't let me run."* **`atalanta_knelt = true`. +2 loyalty. Advances to Beat 2.**
**Option 4 — also lands:** Watching the player kneel and care for the child — simply, no agenda — undoes her. *"You just— did it. No grand vow, no saving all of them. Just *that one*, because it was in front of you. *(stunned)* That's how it was always meant to be done, wasn't it. I made it a war I had to win completely or lose completely. It was never that. ...Move over, sweetness. Let me try."* `atalanta_knelt = true`. Advances.
*(If the player is cruel to or dismissive of the child, Atalanta shatters in the worst direction — `atalanta_knelt = false`, severe loyalty loss, the glee returns as something genuinely dangerous. Quest fails hard.)*

---

### BEAT 2 — THE CHOICE TO CARE AGAIN

> **DM:** The single child is seen safe — placed with the kingdom's care, a willing family, a settlement — resolved HERE, within this scene. NO follow-on thread, NO continuing investigation. The real beat is Atalanta's: choosing whether to let the girl she buried stay awake, knowing it means being able to be hurt again.

The child is brought to safety — a settlement, a willing guardian, the kingdom's care; it is *settled*, here and now. Atalanta watches the child go somewhere safe and stands at a precipice inside herself.

### Player Choice Menu:
1. *"You can let her stay awake. The girl who cares. I'll help you carry it."*
2. *"It hurt because you let it matter. That's not weakness. That's the bravest thing you've done."*
3. [Stay beside her in silence as she decides]
4. [Custom]

### Responses:
**Any — Best:** Atalanta watches the child reach safety, and the breath she lets out is decades old. *"...She's safe. One is safe. *(she touches the worn child's token at her wrist — and for once explains it)* This was the last one I couldn't reach. I've carried it to remember why I stopped trying. *(she looks at the player)* ...Maybe I'll carry it now to remember why I started again. One at a time, the way it was always meant to be. *(the smile returns — different, real, no terrible edge to it)* I'm still a monster, sweetness, don't mistake me. But I think I'm a monster who's allowed to save the one in front of her now. You woke her. The girl I gave up. Don't you dare let me regret it."* **`atalanta_redeemed = true`. +3 loyalty. Advances to Resolution.**

---

### RESOLUTION

The one child is safe. Atalanta has not become gentle, or cured, or whole — but the girl who swore to protect the abandoned is awake again, and that changes who she is at the player's side.

**Atalanta:** *"I spent so long laughing because the alternative was feeling all of it at once. *(quieter)* You showed me a third way — not saving all of them, not saving none. Just the one. The one in front of you. Today. *(she ties the token back on, slow, and lets the player watch)* I'll still hunt. I'll still enjoy it, gods help me. But I have something to protect again, and I'd forgotten the weight of it. Thank you — for reaching the part of me even I swore was dead. Be careful with her. She's the part that can still be broken."*

**Flag:** `atalanta_quest = complete` | `atalanta_knelt = true/false` | `atalanta_redeemed = true/false`
**Reward:** **The One She Could Save** — Atalanta's loyalty becomes devoted; +2 to all checks defending a child, a vulnerable innocent, or the player. The worn token becomes a keepsake: while she carries it, she cannot be driven fully back into the gleeful-monster state by any effect.
**Ch7 survival note:** If redeemed, she fights Ch7 with something to protect — once, she takes a lethal blow meant for an ally she's sworn to guard. If not redeemed, she fights as the gleeful monster, loyalty conditional, and may turn.

---

### FAILURE CONDITION
If the high gate is never met, or the player is cruel/dismissive to the scripted child, the buried girl stays buried — and the glee curdles into something genuinely dangerous. Flag: `atalanta_quest = failed_shattered`. ⛔ Even on failure, the DM does NOT generate a missing-children trail or expand the theme — the failure is internal to Atalanta, full stop.

---

**Save block additions:**
```json
"atalanta_quest": "inactive",
"atalanta_quest_beat": 0,
"atalanta_knelt": false,
"atalanta_redeemed": false
```
