# KINGMAKER — COMPANION QUEST SCENES (PART B)
## KM_CompanionQuests_B.md | Jaethal, Octavia, Regongar, Nok-Nok, Lem, Kalikke/Kanerah

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

## 11. LEM — A BARD'S CALLING

**Trigger:** Relationship ≥ Friendly + Ch3 (news from Pitax)
**Location:** Capital → Pitax region (Ch5 access or side expedition)

---

### SCENE: THE NEWS

Lem is playing quietly when he stops mid-note. He's been handed a letter.

**Lem:** *"The Academy of Grand Arts. Irovetti has started arresting students for 'subversive performance.'"* He sets the lute down. *"My classmates are still there."*

He looks at you.

**Lem:** *"I know what you're going to say. It's a political situation. It's Pitax. We're not ready."*

**Player Choice Menu:**
1. *"Tell me who they are. We'll get them out."*
2. *"What would getting them out require?"*
3. *"Is this worth a diplomatic incident?"*
4. *"Write something. A protest. Send it through channels."*
5. [Custom]

---

### PATH A: EXTRACTION (Stealth or Diplomacy)

Requires accessing Pitax — either during Ch5 or via a risky side expedition.

**Stealth path:** Sneak into the Academy quarter. Stealth DC 22 (Pitax guards). Each student found = one Stealth check. 1d4+2 students total.

**Diplomacy path:** Negotiate with a Pitax cultural attaché. Diplomacy DC 24. Success = the students are quietly transferred. Failure = Irovetti hears about the attempt (−1 to all Pitax Diplomacy for 1 chapter).

**On success:**
Lem greets the students at the capital. He's performing for them that night.

**Lem:** *(to the player, quietly)* *"They said they kept performing. Even when they knew they might be arrested for it. They kept performing."*

He doesn't say anything else. He doesn't need to.

**`lem_quest = complete`.** Students add **+1 Culture per kingdom turn permanently.**

---

### PATH B: THE POLITICAL COMPOSITION

Lem writes. For three days, you barely see him. What he produces is a piece of music — a ballad that travels through merchants and travelers to Brevoy and the River Kingdoms. Within a month, enough political pressure lands on Pitax that the students are quietly released.

Slower. Safer. Lem is proud of it, but:

**Lem:** *"I wrote a song about courage. And then waited for other people to be courageous. That's not quite the same thing, is it."*

**`lem_quest = complete`** (political path — no Culture bonus, but **+1 Loyalty** for the ballad's reach).

**+2 Relationship either path.**

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

> **DM:** Three quest pairs where advancing one companion's goal blocks the other's preferred outcome. The player MUST choose a side. The unchosen companion takes a relationship hit. Present both positions using the Debate system (KM_Debates.md) if the player wants to hear both sides before deciding.

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
