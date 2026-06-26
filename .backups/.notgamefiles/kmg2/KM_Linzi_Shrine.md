# KINGMAKER — THE SHRINE OF RETURNING
## KM_Linzi_Shrine.md | Active: Chapter 6 | Referenced by: KM_Ch4.md (Ch6 section)

---

> **DM:** Load this file during Chapter 6. The shrine quest becomes available the moment the player returns to the capital after Linzi's death in Thousandbreaths. This is a one-chance, one-god decision. The player chooses which shrine to build. That choice is permanent. Once a shrine is selected and construction begins, the other two gods will not hear prayers on this matter.
>
> **CRITICAL FLAGS:**
> - `linzi_dead = TRUE` — triggers this quest
> - `shrine_god_chosen` — set when player commits to a shrine (`shelyn` / `pharasma` / `urgathoa`)
> - `shrine_built = TRUE` — set when construction is complete
> - `linzi_resurrection_attempted = TRUE` — set when the ritual is performed
> - `linzi_returned = TRUE/FALSE` — outcome
> - `linzi_mark` — the permanent mark left on her (`shelyn_marked` / `pharasma_marked` / `urgathoa_marked`)

---

## 🕯️ QUEST TRIGGER — RETURN FROM THOUSANDBREATHS

> *Back at the capital. The throne room feels different without her in it.*
> *Her notebook is on the table. She left it there before you departed.*
> *The last entry is dated the morning you left for Thousandbreaths.*
> *"Chapter [X]: The Final Chapter. Working title. Obviously."*

Jhod Kavken approaches the player within 24 hours of return:

> **Jhod:** *"There are those who say death is not always final. I've spent my life in service to a god who healed the unhealable. I won't tell you it's possible. But I won't tell you it's impossible either."*
>
> *He sets three scrolls on the table.*
> *"These are the forms. Each one is a covenant with a different power. You should read all three before you decide. Once you begin construction — once the first stone is laid — the other two doors close. The gods do not share this kind of claim."*

**Player must read all three scrolls before choosing.** Each scroll describes the god's nature and the general shape of what they'll ask. DM presents the overview below — do not yet reveal the specific prices.

---

## 📜 THE THREE SCROLLS — OVERVIEW

> **SCROLL OF SHELYN** — *The Eternal Rose, Goddess of Love, Beauty, and Art*
> *"She governs what endures. What is made with love outlasts what is made for power. Her shrines are built in beauty. Her prices are paid in beauty. She has been known to return what was lost — but she will ask you to understand what you are asking for."*

> **SCROLL OF PHARASMA** — *The Lady of Graves, Goddess of Death, Fate, and Prophecy*
> *"She governs every soul that passes. The dead belong to her. To ask for one back is to ask her to undo her own work. She does not do this lightly, or cheaply, or without consequence. But she has done it. She is not cruel. She is absolute."*

> **SCROLL OF URGATHOA** — *The Pallid Princess, Goddess of Undeath, Gluttony, and Disease*
> *"She can return the dead. She returns them as they are — which is to say, changed. What she gives is real. What she takes is also real. Her shrines are not built in beauty. Her prices are not paid in beauty. But she delivers."*

**Player chooses one.** The other two scrolls turn to ash when the first shrine stone is laid.

---

## 🌸 PATH 1 — SHELYN'S SHRINE

### The Shrine

**Without existing temple:** Requires 8 RP and 30 days of construction. A freestanding marble structure with rose motifs. No prior religious infrastructure needed.

**With existing Temple of Shelyn (max tier):** Requires 4 RP and 14 days. The shrine is an extension of what already exists — the god is already present in your kingdom.

**Construction event:** As the shrine nears completion, roses begin growing around it — unseasonably, out of season. Local children bring flowers without being asked. `shelyn_shrine_attention = TRUE`

---

### Shelyn's Price — What She Asks

When the shrine is complete, a vision comes. Not a booming divine voice — a woman's voice, warm and tired, like someone who has seen everything and still chooses to love it.

> **Shelyn:** *"She wrote everything down. Do you know how rare that is? Most lives are lived and lost and no one thought to make them permanent."*
>
> *A pause.*
>
> **Shelyn:** *"I will bring her back. But you have to give me something that matters. Not gold. Not blood. Something you made — that you put yourself into — that you would keep if you could."*

**THE PRICE — The Chronicle:**
Shelyn asks for the original manuscript of Linzi's chronicle. Every page. Every word Linzi wrote.

The chronicle is the record of your entire campaign — every battle, every companion, every choice. It is the only copy. If you give it:
- Linzi returns
- The chronicle goes to Shelyn's domain
- Linzi remembers everything she wrote but has no physical record of it
- She will have to write it again from memory — and the new version will be different

```
PLAYER MUST CHOOSE:
A. Give the chronicle → Shelyn accepts. Ritual begins.
B. "I can't give this away — it's her life's work" → Shelyn:
   "Then perhaps you understand why I asked for it. She would want you to keep it.
    Give me something else — something you made that matters to you personally."
   → Alternative: Player must create something (Crafting DC 22 + 3 days + 100 gp)
     A piece of art, a monument design, a composition — made BY the player, not bought.
     On success: Shelyn accepts the alternative.
     On failure: The offering is insufficient. Shelyn does not respond.
     One attempt only.
C. "Is there anything else?" → "No. I ask for what is real."
```

**If the chronicle is given OR the alternative succeeds:**

> *The shrine glows softly. Not dramatically — the way sunlight looks through leaves.*
> *Linzi's notebook opens on the table. The pages turn on their own.*
> *Then she is there. Standing in the shrine garden.*
> *She looks at her hands. Then at you.*
>
> **Linzi:** *"...I had the strangest dream. I was somewhere very bright and someone was asking me to sing and I kept saying I wasn't ready yet."*
> *She looks around. The capital. The shrine. Roses.*
> *"...Did you build this for me?"*

---

### Shelyn's Mark

`linzi_mark = shelyn_marked`

Linzi returns fully herself — warm, enthusiastic, notebook always in hand. But Shelyn's touch remains:

- Her new chronicle glows faintly when she reads passages aloud
- Flowers grow slightly faster near wherever she camps
- Once per long rest: she can cast *Soothe* (2d10+8 healing) without components — she hums it into existence without knowing she's doing it
- **Permanent:** Her writing is subtly, indefinably better. Even she notices it. She cannot explain it.

**Companion reactions:**
- Amiri: *"Hm. You came back. Good. It was quiet."* (She is relieved. She will not say so.)
- Tristian: Weeps quietly in the shrine garden. Says nothing for a while. Then: *"Thank you."*
- Valerie: Formally acknowledges her return. Notes that Shelyn's blessing on a bard is *"fitting, if sentimental."*
- Jaethal: *"Interesting. She looks alive. Almost entirely."* (Means this as a compliment.)

---

## ⚖️ PATH 2 — PHARASMA'S SHRINE

### The Shrine

**Without existing temple:** Requires 10 RP and 45 days. A stark stone structure — no ornamentation, no flowers, no warmth. Just clean edges and a scale motif carved above the entrance. The locals find it unsettling. Unrest +1 during construction.

**With existing Temple of Pharasma (max tier):** Requires 5 RP and 20 days. Unrest +0 (the temple's presence has already normalized Pharasma's aesthetic in your kingdom).

**Construction event:** A psychopomp — a hooded figure with a pale mask — appears at the construction site on the third day. It says nothing. It observes. It leaves. `pharasma_shrine_noticed = TRUE`

---

### Pharasma's Price — What She Asks

The vision comes at midnight, exactly. The shrine is cold even in summer. A voice like stone sliding against stone.

> **Pharasma:** *"You want her back."*
> *Not a question.*
>
> **Pharasma:** *"You understand that I have processed ten thousand souls today. That each of them had someone who wanted them back. That I made no exceptions."*
>
> *A pause that lasts longer than it should.*
>
> **Pharasma:** *"But you are not ten thousand somebodies. You are the ruler of a kingdom that sits on land I have particular interest in. And she is — I will admit — not finished yet. There is more chronicle in her. I can see it."*
>
> **Pharasma:** *"My price is this: something that should not exist, ends. You will know it when you find it. Bring me the proof, and she comes home."*

**THE PRICE — Destroy an Abomination Against Death:**

Pharasma requires the player to end something that violates the natural order of death. Three valid targets exist — player must complete one:

```
OPTION A: A LICH'S PHYLACTERY
  Any active lich in the Stolen Lands region whose phylactery has not been destroyed.
  If Vordakai's Oculus was destroyed in Ch3: this option is already fulfilled.
    → `vordakai_phylactery_destroyed = TRUE` from Ch3 carries here
    → Present the Oculus fragments at the shrine. Pharasma accepts immediately.
    → This is the "easy" path — players who finished Ch3 thoroughly get rewarded.
  If Vordakai was recruited [evil path]: this option is NOT available.
  Alternative phylactery: A minor lich in the Narlmarches (new encounter, Level 14).
    → HP: 140 | AC: 26 | Spells: 8th level | Phylactery: stone box in a hidden tomb
    → +1,800 XP

OPTION B: SEAL A PORTAL TO THE NEGATIVE PLANE
  A rift has been leaking negative energy into a Narlmarches hex.
  Location: revealed by the psychopomp if player asks it (Diplomacy DC 18 to communicate)
  The seal: Occultism DC 28 + 3 castings of Consecrate (requires a cleric in party)
           Or: sacrifice a Level 5+ magic item into the rift (consumed, gone)
  Time: 2 days on-site
  → +1,200 XP

OPTION C: DESTROY THE UNDEAD ARMY
  If any undead NPC was recruited as an advisor (Vordakai, or certain evil path choices)
  Pharasma will not accept Linzi's return while a warlord of undeath advises the ruler.
  This option requires the player to dismiss and destroy the undead advisor.
  A steep price for players who took the evil path.
```

**When the price is paid:** Return to the shrine with proof (phylactery fragments / sealed rift / dismissal record).

> *The shrine's scale tilts. Slightly. Then levels.*
>
> *Pharasma's voice, once:*
> **Pharasma:** *"The scales are balanced. A wrong against death is corrected. A right against death is permitted."*
>
> *Linzi walks out of the shrine door. She looks dazed. Like someone who fell asleep mid-sentence and woke up in a different room.*
>
> **Linzi:** *"...It was very organized there. Very — orderly. There was a queue. I was number [X]. I never found out what [X] meant."*
> *She blinks. Looks at you.*
> *"You balanced the scales for me, didn't you."*

---

### Pharasma's Mark

`linzi_mark = pharasma_marked`

Linzi returns fully herself — but she has stood in Pharasma's hall and remembers it, dimly, the way one remembers a dream that meant something.

- She no longer fears death in the abstract. She has seen the process. It's orderly.
- Once per session: when any party member reaches 0 HP, Linzi can call out a number — their number from the queue — and they automatically stabilize (no recovery check needed). She doesn't fully understand how she knows. She just does.
- Her chronicle entries about death — of enemies, of companions, of moments — are now written with uncommon precision. She does not flinch from them.
- **Permanent:** Pharasma's psychopomps leave her alone. Undead creatures treat her as one degree less hostile by default (they sense she has stood in that hall and returned with permission).

**Companion reactions:**
- Harrim: *"You've seen the Gray Lady's hall. I have dreamed of it my entire life."* He sits with her for an hour. Neither speaks much. It is the most at peace he has seemed.
- Jaethal: Studies her with genuine interest. *"What was it like? Tell me everything."*
- Tristian: Troubled. *"The Lady of Graves gave her back. That doesn't happen. What did we trade for that?"*
- Amiri: *"The dead stay dead. Except when they don't. Fine."*

---

## 💀 PATH 3 — URGATHOA'S SHRINE

### The Shrine

**Without existing temple:** Requires 6 RP and 21 days. Faster and cheaper than the others — Urgathoa is not particular about aesthetics. The shrine is functional, dark-stoned, with a bone motif. Unrest +2 during construction and permanently while it stands. Citizens avoid the street it's on.

**With existing Temple of Urgathoa (max tier):** Requires 3 RP and 10 days. The temple's presence already marks your kingdom as darkness-touched. No additional unrest.

**Construction event:** The night the shrine is completed, something dies near it. An old dog. A tree. Nothing dramatic. Just — something. `urgathoa_shrine_fed = TRUE`

---

### Urgathoa's Price — What She Asks

The vision comes during a feast. Urgathoa appreciates irony.

> *The food tastes different suddenly. Richer. Too rich. Overwhelming.*
>
> **Urgathoa:** *"Oh, I like you. You built me a shrine. In your nice clean capital."*
> *A laugh — it sounds like something eating.*
>
> **Urgathoa:** *"I'll bring your little bard back. She'll be exactly herself. Mostly. There's just one thing."*
>
> **Urgathoa:** *"I'm hungry. I'm always hungry. Your kingdom is going to feed me — just a little, just an ongoing contribution — and your bard is going to carry my mark whether she likes it or not. And she will not like it."*
>
> *"The question is: does she get to decide? Or do you?"*

**THE PRICE — Three Components:**

```
COMPONENT 1: The Feast of Urgathoa (immediate)
  A feast must be held in the shrine. Not symbolic — a real feast, with real food,
  and at least one living person must eat until they are genuinely ill.
  The player must participate (or order it). Alignment: [Evil] flag.
  Duration: one evening. Cost: 200 gp in food and wine.

COMPONENT 2: The Ongoing Tithe
  Every kingdom turn: −1 to one of the following (player's choice each turn):
    Economy, Culture, or Loyalty
  This represents Urgathoa's ongoing appetite from your kingdom.
  Cannot be removed while the shrine stands.
  Removing the shrine: Urgathoa's mark on Linzi intensifies for 30 days (she is Sickened 1
  until a Remove Curse DC 25 is performed). After that: the tithe ends and the mark
  fades to its permanent baseline.

COMPONENT 3: Linzi's Consent (the real price)
  Urgathoa adds one condition: "She has to agree. I don't take what isn't offered."
  (She is lying about why she requires consent — she doesn't require it. She enjoys
  the moment when Linzi finds out and has to choose.)
  When Linzi returns: she is undead, functional, herself.
  She will be told immediately what happened.
  She will have one conversation with the player.
  She must then decide: accept Urgathoa's mark and live on as she is, or refuse
  it, which means returning to death.
```

**LINZI'S RETURN — The Conversation:**

> *She walks out of the shrine. She stops. She puts her hand to her chest.*
> *No heartbeat.*
>
> **Linzi:** *"...Oh."*
> *She looks at her hand. Holds it up to the light.*
> *"...I'm dead, aren't I. I mean — I'm here. But I'm dead."*
>
> *She turns to you. Her expression is complicated.*
> **Linzi:** *"You built a shrine to Urgathoa. For me."*
> *A long pause.*
> *"Tell me the price. All of it. Don't soften it."*

**Player must tell her. The DM presents the three components.**

```
LINZI'S DECISION:
  "I accept it."
    → She closes her notebook. Opens it again.
    → "Well. This will make for a very interesting chapter."
    → `linzi_accepted_urgathoa = TRUE`
    → She stays. Undead but herself.

  "I don't accept it."
    → She exhales — a habit, since she doesn't need to breathe anymore.
    → "Then I think... I think I have to go back."
    → She reaches out and touches your hand.
    → "Write the ending yourself. You know how the story goes."
    → She fades.
    → `linzi_refused_urgathoa = TRUE` — she returns to death
    → The shrine remains. The tithe begins regardless.
    → This is the worst outcome. Urgathoa got her feast and her tithe
      and the player has nothing.
    → Urgathoa: (distant, amused) "I did say she had to agree."
```

**If Linzi accepts:**

She stays. But the Urgathoa path has a redemption arc built in:

```
SECONDARY QUEST — Linzi's Cure (optional, available any time after Ch6):
  Jaethal knows a way to remove Urgathoa's mark — she had it done to herself
  once, partially. Reverse-engineer the process.
  Requires: Jaethal's quest complete + Occultism DC 28 + Remove Curse DC 25
  + A cleric of Sarenrae or Pharasma performing the rite (Tristian, Jhod)
  + 500 gp in ritual components
  On success: Mark removed. Linzi becomes fully alive again.
  The ongoing tithe ends.
  The shrine still stands (and still generates unrest) but is now inert.

  LINZI after cure: "I keep expecting the heartbeat to feel wrong. It doesn't."
  She is quiet for a moment. "Thank you. Both times."
```

---

### Urgathoa's Mark (if uncured)

`linzi_mark = urgathoa_marked`

Linzi is undead. She is herself — her humor, her writing, her warmth — but she is cold to the touch and has no heartbeat. She knows it. She writes about it with the same directness she writes about everything.

- She does not need food, water, or sleep (she still eats and sleeps by habit — she finds it comforting)
- She is immune to poison, disease, and sleep effects
- She is harmed by positive energy healing (heals for 0, or use Harm instead)
- Once per day: she can cast *Feast of Ashes* on a target (Fortitude DC 19 or Starving — no healing for 24 hours)
- **Permanent:** NPCs who can sense undead react poorly to her (−2 to her Diplomacy in formal settings). Urgathoa's mark glows faintly at the base of her throat when she writes at night.

**Companion reactions:**
- Jaethal: Sits beside her immediately. *"I understand what you are now better than any of them. Ask me anything."* Relationship +1.
- Harrim: *"The Pallid Princess claims another. And yet you persist. Curious."* He is not dismissive. He is genuinely observing.
- Tristian: Cannot look at her directly for three days. On the fourth day he sits across from her at breakfast. *"I'm sorry. I'm working on it."* She: *"I know. Take your time."*
- Amiri: *"You smell different."* Pause. *"You're still annoying. Good."*
- Valerie: Treats her with complete formal normality. Does not mention it once. This is, strangely, the kindest response.

---

## 📊 SUMMARY TABLE

| | Shelyn | Pharasma | Urgathoa |
|---|---|---|---|
| **Alignment** | Good | Neutral | Evil |
| **Cost (no temple)** | 8 RP / 30 days | 10 RP / 45 days | 6 RP / 21 days |
| **Cost (max temple)** | 4 RP / 14 days | 5 RP / 20 days | 3 RP / 10 days |
| **Price** | Something you made that matters | Destroy an abomination against death | A feast + ongoing kingdom tithe + Linzi's consent |
| **Difficulty** | Medium (can fail craft check) | Easy if Ch3 complete, harder otherwise | Low (Linzi may refuse) |
| **Linzi returns as** | Fully alive, Shelyn-touched | Fully alive, death-aware | Undead (curable) |
| **Permanent mark** | Faint glow, passive *Soothe* | Stabilize any ally 1/session, undead neutral | Undead traits, *Feast of Ashes* |
| **Unrest during build** | 0 | +1 | +2 |
| **Kingdom ongoing cost** | None | None | −1 stat per turn |
| **Can fail?** | Yes (craft check fails) | Rare (if Vordakai recruited) | Yes (Linzi refuses) |

---

## 💾 FLAGS TO CARRY IN SAVE BLOCK

```json
"linzi_shrine": {
  "triggered": true,
  "god_chosen": "",
  "shrine_built": false,
  "price_paid": false,
  "resurrection_attempted": false,
  "linzi_returned": false,
  "linzi_mark": "",
  "linzi_accepted_urgathoa": false,
  "linzi_refused_urgathoa": false,
  "linzi_cured_urgathoa": false,
  "chronicle_given_to_shelyn": false,
  "vordakai_phylactery_used": false,
  "ongoing_tithe_active": false
}
```

---

*KM_Linzi_Shrine.md — Kingmaker PF2e Text Adventure | Linzi Resurrection Quest v1.0*
