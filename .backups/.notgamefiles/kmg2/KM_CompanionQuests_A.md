# KINGMAKER — COMPANION QUEST SCENES (PART A)
## KM_CompanionQuests_A.md | Amiri, Linzi, Valerie, Harrim, Tristian

> **DM:** Load this file when a companion personal quest triggers.
> Each entry contains: trigger conditions, opening scene, NPC dialogue,
> choice menus, resolution paths, and save block flags to set.
> Quest summaries (triggers, flags) are in KM_Companions_B.md.
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
