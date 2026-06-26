# KINGMAKER — COMPANION QUEST SCENES (PART C)
## KM_CompanionQuests_C.md | Companions: Seelah, Kyra, Merisiel, Valeros, Sajan

> **DM:** Load when any of these companions' personal quests trigger.
> Same format as KM_CompanionQuests_A.md and _B.md.
> Quest summaries (triggers, flags) are in KM_Companions_B.md.
> All quests: Trigger = Relationship ≥ Friendly unless noted.
> All reward: +2 Relationship on completion. Ch7 risk: incomplete = −2 to all checks.

---

## 13. SEELAH — THE STOLEN HELMET

**Trigger:** Relationship ≥ Friendly + Ch2
**Location:** Capital → Restov district

---

### SCENE: THE LETTER

A worn letter arrives for Seelah — no seal, no return address. She reads it and says nothing until the player asks.

**Seelah:** *"Someone found the family of the paladin whose helmet I stole. A daughter. She's eight. She wants to know what happened to her father."*

She folds the letter carefully.

**Seelah:** *"He died before I could return it. I've been carrying that."*

### Player Choice Menu:
1. *"Will you write back?"*
2. *"What do you want to do?"*
3. *"You were a child. It wasn't your fault."*
4. *"What would he have wanted?"*
5. [Custom]

**Option 2 — Best:** *"I want to go there. I want to look her in the face and tell her what her father did for me."* **+1 Relationship. Quest advances.**

**Option 3:** She shakes her head. *"That doesn't matter. What matters is what I do now."* Relationship unchanged.

---

### RESOLUTION SCENE

Seelah returns from Restov quieter than she left. She finds the player.

**Seelah:** *"She cried. I thought she'd be angry. She just... cried. And then she asked if I was a good paladin."*

Beat.

**Seelah:** *"I said I was trying to be."*

**Flag:** `seelah_quest = complete`
**Reward:** Seelah gains *Debt Carried Forward* — once per day, she may spend her Reaction to prevent a killing blow on any ally (reduces to 1 HP instead of 0).

---

## 14. KYRA — THE VILLAGE'S NAME

**Trigger:** Relationship ≥ Friendly + Ch2
**Location:** Capital shrine → Stolen Lands village

---

### SCENE: THE SHRINE

The player finds Kyra at the capital shrine late at night. She's not praying — she's staring.

**Kyra:** *"I've never said the name of my village out loud. Since the fire. It felt like... if I said it, something would end."*

She turns.

**Kyra:** *"A survivor found me. Someone from before. She wants to rebuild somewhere nearby. She wants to know if I'll come."*

### Player Choice Menu:
1. *"Will you go?"*
2. *"What's the village's name?"*
3. *"You don't have to go back."*
4. *"What does Sarenrae tell you?"*
5. [Custom]

**Option 2 — Best:** Long silence. Then she says it. One word. The DM uses the name naturally in scene description afterward. **+1 Relationship. Quest advances.**

---

### RESOLUTION SCENE

They travel together. The site is empty meadow. The survivor, an older woman named Sera, is already there with a cart.

Kyra kneels at the center of the meadow and presses her palm to the earth.

**Kyra:** *"We're going to build something here. Not the same thing. Something new."*

She stands and helps Sera unload the cart.

**Flag:** `kyra_quest = complete`
**Reward:** +1 Loyalty (kingdom) permanently. Kyra's Healing Font slots +1.

---

## 15. MERISIEL — THE PRICE OF TRUST

**Trigger:** Relationship ≥ Friendly + Ch2
**Location:** Narlmarches — a specific waypoint

---

### SCENE: SHE ASKS FIRST

Merisiel drops in next to the player on the road — from somewhere above.

**Merisiel:** *"Someone's been following us for three days. Not hostile. Waiting for something."*

She watches the player's face.

**Merisiel:** *"I know who it is. She's an old partner. I left a job unfinished. She's here to collect."*

### Player Choice Menu:
1. *"Do you want backup?"*
2. *"What was the job?"*
3. *"Should I be worried?"*
4. *"Do you trust her?"*
5. [Custom]

**Option 4 — Best:** *"I don't know. I used to."* She's quiet. *"That's the question, isn't it."* **+1 Relationship. Quest advances.**

---

### RESOLUTION SCENE

The partner (Ivara) meets them at a crossroads. The job was theft — a document that implicated a Chelish lord. Merisiel never delivered it. Ivara wants it still.

Merisiel produces the document from inside her vest.

**Merisiel:** *"I kept it because I didn't trust the client. I still don't."*

She gives it to the player instead.

**Merisiel:** *(to Ivara)* *"The job's done. Just differently."*

The resolution depends on what the player does with the document (evidence, leverage, destroy). Ivara leaves either way — not happy, not hostile.

**Flag:** `merisiel_quest = complete` | `merisiel_document = [player_choice]`
**Reward:** Merisiel gains *Old Habit* — once per encounter, she may Sneak as a free action on her first turn.

---

## 16. VALEROS — THE WRONG SIDE OF A DEBT

**Trigger:** Relationship ≥ Friendly + Ch2
**Location:** Capital → Brevoy road

---

### SCENE: THE VISITOR

A mercenary captain named Garvin arrives at the capital asking for Valeros. He's owed money. A lot. From a job three years ago that went wrong.

Valeros doesn't deny it.

**Valeros:** *"I was on the wrong side of that one. I knew it halfway through and finished it anyway."* He looks at the player. *"That's the one I can't talk myself out of."*

### Player Choice Menu:
1. *"How much does he want?"*
2. *"What happened on the job?"*
3. *"Do you want to handle this yourself?"*
4. *"What does the wrong side mean to you?"*
5. [Custom]

**Option 4 — Best:** He's quiet for longer than usual. *"It means I knew. That's worse than not knowing."* **+1 Relationship. Quest advances.**

---

### RESOLUTION SCENE

Valeros tracks down Garvin privately. The player can follow or not.

If they follow: Valeros pays what he can, admits the rest, and offers his sword arm for one future job to make the balance. Garvin accepts.

Afterward, to the player:

**Valeros:** *"He didn't have to take it. I wouldn't have."* He refills his cup. *"Decent man. I owe him a good fight someday."*

**Flag:** `valeros_quest = complete`
**Reward:** +1 Economy (kingdom) — Garvin's mercenary network opens trade connections. Valeros gains *Earned Blade* — +1 to attack rolls when fighting alongside someone he's saved.

---

## 29. SAJAN — THE TWIN'S TRAIL

**Trigger:** Relationship ≥ Friendly + Ch3 (after sajan_agenda_confronted)
**Location:** A temple or shrine in the Stolen Lands

---

### SCENE: THE LEAD

After his agenda confrontation, this fires when a specific piece of intelligence arrives — a record matching his sister's description in a temple registry from the Stolen Lands region.

Sajan holds the copy of the record. He's very still.

**Sajan:** *"She was here. Three years ago."*

He looks up.

**Sajan:** *"She may still be."*

### Player Choice Menu:
1. *"We find her."*
2. *"Tell me what you know about her."*
3. *"Three years is a long time. Are you prepared for what we might find?"*
4. *"What does she look like?"*
5. [Custom]

**Option 3 — Best:** *"Yes."* One word. Then: *"I've been preparing for twelve years."* He folds the record carefully. **+1 Relationship. Quest advances.**

---

### RESOLUTION SCENE

The trail leads to a monastery in the eastern Stolen Lands. His sister — Sajni — is there. She's been there for two years. She's safe.

They see each other across a courtyard.

Neither runs. They walk. They meet in the middle.

The DM does not narrate what they say. The player watches from a distance.

When Sajan returns, his expression is different. The search has ended.

**Sajan:** *"She chose to stay. She is well."* He bows once to the player. *"You brought me here. I will not forget that."*

**Flag:** `sajan_quest = complete` | `sajni_found = TRUE` | `sajni_status = safe`
**Reward:** Sajan gains *Resolved Search* — his Ki pool increases by 1. His movement speed increases by 5 ft (the constant searching tension is gone).

---

*KM_CompanionQuests_C.md — Kingmaker PF2e Text Adventure | Companion Quest Scenes Part C v2.0*
*v2.0: Culled companions removed (Fumbus, Feiya, Quinn, Jirelle, Yoon, Korakai, Nhalmika, Nahoa, Samo, Crowe). Valid entries: Seelah, Kyra, Merisiel, Valeros, Sajan.*
