# CHAPTER 7 — THE FINAL ACT
# ═══════════════════════════════════════════

**Levels:** 18–20 | **Final chapter**
**Location:** House at the Edge of Time — Nyrissa's true domain

## Overview
The final dungeon. The Lantern King's curse is the root of everything. Five endings exist based on accumulated flags — see `KM_Mythic_Systems.md` for full requirements and scripted narration. The ending is NOT chosen from a menu — it emerges from play.

---

## The House at the Edge of Time

**Point of no return.** All companion quests must be resolved before entering.

> **DM:** Before the player enters, run the companion check:
> - List every companion's quest status
> - Warn: "Any incomplete quests mean that companion faces their Ch7 risk inside"
> - Ask: "Are you ready to proceed?"

```
ENTRY & LAYOUT (canon):
  You begin OUTSIDE the main gates. Companions who were with you temporarily VANISH — you re-recruit
  them room by room inside (Mercenaries, if used, stay with you). Personal Stash is UNAVAILABLE;
  no camping; all unfinished quests have already failed at the threshold.
  MAGIC WELLS move you between levels:
    Well at the gates       → First Floor.
    Well on the Second Floor → Basement.
  The end point is NYRISSA'S SANCTUARY (the final conversation begins there).

DUNGEON PROPERTIES:
  Time flows differently — past and present overlap in different rooms
  Some rooms show the kingdom's founding; others show its destruction
  Companions see visions of their personal fears (roleplay opportunities)
```

---

## Companion Fates Inside

```
RE-RECRUITMENT INSIDE THE HOUSE (canon room structure — companions are scattered, rescued one by one):
  NORTHEAST → THRONE ROOM: the chronicler (Linzi / Leliana) is held here, guarded by satyr archers and
    a fey horned guardian — a moderate fight to free them.
  SOUTHWEST → three rooms each holding a separated companion (canon: Harrim, Jubilost Narthropple,
    Nok-Nok — swap for the active roster).
  NORTHWEST exit → THE FROZEN BONEYARD: a companion waits in the NW corner (canon: Amiri). Recruit them,
    exit and re-enter the area, then return to the same spot to fight KEAN.
  Find/free the scattered companions before reaching Nyrissa's Sanctuary.
```

```
All quests complete → all companions present for the final fight

Incomplete quests trigger:
  Valerie → burning prison room — Perception 16 + Athletics 18 to save her
  Harrim  → wanders off, rejoins after Nyrissa fight
  Jaethal → Urgathoa influence — Diplomacy 20 each scene to keep her aligned
  Octavia + Regongar (one quest incomplete) → prison room, save one
  Octavia + Regongar (both incomplete) → both imprisoned, save one only
  Amiri (nilak_died) → present but leaves after Nyrissa is defeated (grief)
```

---

## Nyrissa — The True Fight

```
NYRISSA — see KM_Bestiary.md for full stat block (CR 20, HP 380, AC 43)

PHASE 1 (HP 380–190): Thorn Wall, Dominate (lowest Will), Wail of the Lost, Fey Step (teleport 60 ft).

PHASE 2 (below 190 — Lantern King intervenes):
  Heals Nyrissa to 190 HP. "Go on then. Finish her. That's what I've been waiting for."
  He wants you to kill her — that's part of the curse.

THE CHOICE (true ending gate):
  Kill Nyrissa (standard) → BAD ENDING
  [Requires: nyrissa_backstory_known = TRUE]:
    "I know what he did to you. I know what was taken."
    → Nyrissa pauses. She looks at the Lantern King.
    → Diplomacy DC 30 OR 2 Hero Points
    → SUCCESS: Break the curse. Confront the Lantern King. TRUE ENDING.
    → FAIL: Fight continues, bad ending.
```

---

## The First Crown & Shyka — Alternate Resolution

If the player carried **THE FIRST CROWN** out of Ch6, it changes how this ends:

```
RETURN THE CROWN TO NYRISSA (and spare her):
  SHYKA THE MANY (the time-fey lord of the First Crown) uses the Crown to undo Nyrissa — ending her
  threat and SKIPPING the final boss fight entirely. A clean, lore-true resolution and a best-ending route.
KEEP THE CROWN:
  The player may wield it against Nyrissa AND against the Lantern King in the fight above.
`first_crown_choice = [returned / kept]` decides which path is live.
```

---

## The Cursed King / Queen — The Ravaged Capital

After Nyrissa is dealt with — IF the player does not simply let her go — they are teleported to the
**RAVAGED CAPITAL** for the true final quest.

```
THE CURSED KING / QUEEN:
  Timer: 20 days to resolve (15 days if the Nyrissa attack counter reached 75+ during Ch6).
  The capital lies in ruins from the Bloom's assault. The player faces the last of the curse's fallout
  and seals the kingdom's final fate — which ending variant fires resolves here.
  Feeds directly into the 5 endings (see KM_Mythic_Systems.md).
```

`cursed_king_queen_resolved = TRUE`

---

## Default Ending (The Ruler's Ending)

Kill Nyrissa without meeting true ending requirements. Kingdom survives with reduced stats. No resolution to the Lantern King's curse. Full scripted narration in `KM_Mythic_Systems.md` — Ending 1.

**Other endings** (Conquest, Transcendence, Golden) fire based on accumulated flags. See `KM_Mythic_Systems.md` for all 5 ending variants and their flag checklists. DM checks eligibility at Ch6 opening.

---

## True Ending

> *Nyrissa stares at the Lantern King.*
> **Nyrissa:** *"You gave me a heart so you could take it. You cursed me to love what I destroy. For ten thousand years."*
>
> *The Lantern King is not laughing anymore.*
>
> *"You were supposed to kill her," he says to you. "That was the arrangement."*
>
> *The Lantern King waits for an answer. Present a choice menu — the player's response is their own.*

```
LANTERN KING — Eldest Fey (Trickster Divinity)
HP: 320 | AC: 30 | Cannot be permanently killed (he is a fundamental force)
His attacks deal Confused 1 (Will DC 26) on hit — trickery made manifest
His weakness: Honesty. The more directly the player speaks truth to him, the lower his DCs.

Each round: Player can attack OR speak truth:
  [Attack] → deals damage, no special effect
  [Truth] → Lore (Fey) DC 20 OR player identifies something real about him
    → His AC drops by 1 per truth told (cumulative, max −6)
    Examples: "You're afraid of what you created." (+1 AC reduction)
              "You've been alone since before this kingdom existed." (+1)
              "She loved something you made and you couldn't stand it." (+2)

At 0 HP: The Lantern King cannot die. He yields. For the first time in ten thousand years, someone made him yield.
He removes Nyrissa's curse. She is free.
```

> *Nyrissa kneels in the ruins of the House.*
> **Nyrissa:** *"I don't know what I am without the curse."*
> *She looks at you. And at the kingdom visible through the crumbling walls.*
> *"But I would like to find out."*

**True Ending outcomes:**
- Nyrissa can be offered a place in your kingdom (she becomes a permanent ally — unique advisor)
- Kingdom receives the Bloom's land back (all consumed hexes restored)
- `true_ending_achieved = TRUE`
- Linzi (if saved): writes the final chapter of the chronicle — the real one
- Leliana (if `leliana_chronicler_mode` + survived to here): performs the completed Verse as the final movement — the real ending, played rather than written. If the Verse was never finished, she plays it to where she got and lets the last note hang unresolved (intentional — do not "complete" it for her).

---

## Final XP & Epilogue

| Source | XP |
|--------|----|
| Ch7 dungeon encounters | ~4,800 |
| Nyrissa (boss) | 2,000 |
| Lantern King (true ending) | 1,600 |
| Companion saves | 400–800 depending |
| **Chapter 7 Total** | **~9,200–10,000** |

**Final Kingdom State:**
- True Ending: All stats restored, Bloom land reclaimed, Nyrissa as optional advisor
- Bad Ending: Kingdom survives, permanently reduced Culture and Loyalty, cursed undercurrent

---

## 🎭 EPILOGUE SCENES (Linzi's Questions)

Linzi (or her book, if she died) asks the player a final series of questions about their reign. Answers generate the epilogue narrative.

**If `leliana_chronicler_mode = true`:** Leliana runs this beat instead of Linzi — she asks the same reign questions between movements of the Verse (or, if she died, they surface as the untitled pieces in her Ballad Cycle / the final score page, and the player answers by choosing which get performed). Same epilogue-generation function, her register not Linzi's: less "what will the official account say" and more "what was this worth — was it worth finishing." The generated epilogue is delivered as the closing performance of the Verse rather than the closing page of the chronicle.

```
1. What was your kingdom known for? (Culture / Economy / Military / Justice)
2. What happened to [key NPC]? (For each major NPC — outcomes based on flags)
3. Did you rule with the sword or the word? (Alignment-based)
4. What came next? (Open-ended — player describes what happens after)
```

---

*KM_Ch7.md — Kingmaker PF2e Text Adventure | Chapter 7: The Final Act*
*Source: Pathfinder Kingmaker AP (Paizo) + Owlcat Games | PF2e rules: 2e.aonprd.com*


---

<!-- merged from KM_Linzi_Shrine.md (v93.21 file consolidation) -->

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

## 🏛️ MUTUAL EXCLUSION — CHRONICLER KINGDOM BUILDINGS

**Condition gate (set at LINZI-REPLACEMENT GATE or Linzi dismissal):**

| Flag state | Available building |
|---|---|
| `linzi_primary_chronicler = TRUE` (default) | Linzi Shrine of Returning (above) |
| `leliana_chronicler_mode = TRUE` | Hall of the Unfinished Verse (below) |

Both are Tier 2+ kingdom structures, and since Linzi and Leliana are **never both in a run** (NEVER-BOTH invariant, KM_Companions_Behaviors.md § LINZI-REPLACEMENT GATE), only ONE is ever built.

⛔ **UPDATED — supersedes the old "by choice, not by grief" framing.** Per the MASTER TRANSFORMATION RULE, when Leliana holds the chronicler-bard slot she INHERITS Linzi's full death arc: it is **Leliana** whom Nyrissa takes in Thousandbreaths (Linzi is not in the run), and the **Hall of the Unfinished Verse is her RESURRECTION shrine — by grief, triggered by her Ch6 death**, derived from the Linzi Shrine of Returning by swapping words→music. Same death trigger, same 4 save conditions (her 10 ballad verses / the Unfinished Verse replace the Storyteller fragments), same three gods (Shelyn/Pharasma/Urgathoa), same prices, same outcomes, same epilogue role. If Leliana is SAVED (4 conditions + interpose), she lives and the shrine is skipped — exactly as for Linzi. Use the Linzi Shrine mechanics below, re-skinned to music.

---

<!-- LELIANA CONCERT HALL — parallel to Linzi Shrine kingdom building -->

# KINGMAKER — THE HALL OF THE UNTITLED OPUS
## KM_Leliana_Hall (inline) | Active: Ch2+ (Realm Tier 2) | Condition: leliana_chronicler_mode = TRUE

---

> **DM:** This section activates when `leliana_chronicler_mode = TRUE` AND `leliana_opus_named = TRUE` AND the kingdom has reached Realm Tier 2. The Hall is a voluntary construction — the player proposes it, the kingdom builds it. It is not triggered by a death. It is triggered by a performance.
>
> **CRITICAL FLAGS:**
> - `leliana_chronicler_mode = TRUE` — prerequisite (Leliana holds the chronicler role)
> - `leliana_opus_named = TRUE` — prerequisite (player gave the opus its name in Beat 2)
> - `hall_proposed = TRUE` — set when player initiates construction
> - `hall_built = TRUE` — set when construction completes
> - `leliana_opus_performed = TRUE` — set at companion quest Beat 4; activates landmark tier
> - `hall_landmark = TRUE` — set after first foreign dignitary visit post-performance
> - `linzi_primary_chronicler = FALSE` — must be false; mutual exclusion with Linzi Shrine

---

## 🎵 QUEST TRIGGER — THE PERFORMANCE PROPOSAL

Unlike the Linzi Shrine, the Hall is not born from loss. It is born from the moment the expedition becomes something worth commemorating in stone.

The trigger fires after `leliana_opus_performed = TRUE` (companion quest Beat 4 — Leliana's first public performance of the Verse). Within one kingdom turn of that event:

> *The throne room feels different after the concert. Not quieter — fuller. As if the air retained the last chord.*
> *Leliana is at the far end of the room, running her hands along the lute strings, re-tuning by ear. She does not look up when you approach.*
>
> **Leliana:** *"You know what the trouble with a performance is, child? It ends. The moment ends. The piece ends. The room forgets it by morning — and I have outlived more rooms than you'd credit."*
>
> *She finally looks up. The easy warmth has gone quiet and serious — the way it does when she means a thing all the way down.*
>
> **Leliana:** *"I'm not asking for anything. I just think — if a kingdom is going to keep a chronicle, it should have a place where the chronicle lives. Somewhere the music doesn't end just because the hand leaves the strings."*
>
> *A beat.*
>
> **Leliana:** *"That's all. That's the whole thought."*

**Player may respond:**
- "I'll have it built." → `hall_proposed = TRUE`; construction begins
- "What would you want it to be called?" → She: *"Whatever you want. I named the piece. The building is yours."* → player may name it (stored as `hall_name`; defaults to `"Hall of the [leliana_opus_name]"`)
- "Not right now." → quest waits; she nods and says nothing more; trigger re-fires at next major kingdom milestone

---

## 🏛️ THE HALL — CONSTRUCTION

**Requirement:** Realm Tier 2+, `leliana_chronicler_mode = TRUE`, `leliana_opus_named = TRUE`

**Without existing Bardic College or Conservatory:** 10 RP and 40 days. A dedicated concert hall with a Ballad Vault beneath it — shelved archives of composed works, performances recorded in notation. Designed for the living chronicle, not religious purpose.

**With existing Bardic College (max tier):** 6 RP and 20 days. The Hall becomes an attached wing of the College — the archive and the academy share a building. Leliana finds this deeply appropriate. She does not say so.

**Construction event:** Three days before completion, musicians from the capital begin arriving at the construction site uninvited. They play outside. Nobody organized this. Nobody asked them to. By the final day there are eleven of them. `hall_spontaneous_musicians = TRUE`

> *When the last stone is set, Leliana walks in alone. She stays for twenty minutes. She comes out and says:*
> **Leliana:** *"The acoustics are perfect. I don't know how. They're just perfect."*

---

## 🎼 THE SCORE VAULT — WHAT LIVES INSIDE

The Hall has two levels:

**Upper level — The Performance Hall:**
Open to the public. Concerts occur here monthly (automatic Culture event). The Verse is performed on the first of each month if Leliana is present in the kingdom. If Leliana is on expedition, the Hall's resident musicians perform an arrangement from the Ballad Cycle.

**Lower level — The Ballad Vault:**
The full Ballad Cycle in physical form. Each entry from `leliana_ballad_cycle` corresponds to a bound score on the shelves. Pages glow faintly with harmonic residue — anyone who reads a score hears a ghost of the original performance (ambient, 10 seconds, non-magical).

The Vault is accessible to scholars, visiting diplomats, and — eventually — to the player in a special menu:

```
.vault command (when player is at the Hall):
Output: Ballad Vault contents (same as .score, plus building notes)
Each entry: [N] "[title]" — [scene description] — [date, if known]
Example:
  [1] "Overture for a House on Fire" — the night of Jamandi's banquet — Day 1
  [2] "First Movement: Stolen Land" — the party's first hex claimed — Day 14
  ...
```

---

## 🌟 HALL EFFECTS — KINGDOM MECHANICS

**Passive (always active while Hall stands):**

| Effect | Value | Notes |
|---|---|---|
| Culture per turn | +2 | Living chronicle reputation |
| Stability per turn | +1 | Cultural anchor; citizens know the story |
| Loyalty per turn | +1 | The chronicle is *about them*; they recognize themselves in it |
| All Stability/Culture events | +1 bonus | "Living chronicle" reputation modifier applies to all such rolls |

**Note:** The +1 bonus to all Stability/Culture events represents the kingdom's reputation as a place with a living historical witness. Diplomats and merchants give more credit to a kingdom whose chronicle is ongoing, not archived.

**Active (once per kingdom arc, player-triggered):**

**"THE CHRONICLE SPEAKS"** — Leliana performs a new composition at the Hall publicly before a specific negotiation, crisis, or court event.
- Roll Performance DC 18 (Leliana's modifier applies)
- Success: the target event's DC is reduced by 4 (the chronicle shifts perception — foreign parties arrive already sympathetic to your story)
- Critical success: DC reduced by 8; the opposing party asks to hear more. Leliana's approval +1.
- Failure: no effect; normal DC
- Costs: one kingdom turn (Leliana is occupied composing and performing)

---

## 🏆 LANDMARK TIER — AFTER leliana_opus_performed = TRUE

When the companion quest Beat 4 is complete AND the Hall is built, the Hall becomes a **kingdom landmark** within one turn:

> *A delegation from the Rostland Court arrives. Their herald asks, with evident rehearsal:*
> **Herald:** *"We heard there is a bard here whose work chronicles the founding of a kingdom in real time. The Sword Lords wish to hear it."*

`hall_landmark = TRUE`

**Landmark effects (permanent additions to passive):**

| Effect | Value |
|---|---|
| Fame per turn | +1 |
| Diplomatic relations | All River Kingdom factions +1 disposition on first contact |
| Foreign dignitary visits | 1d4 visiting nobles per 6 turns (Economy +1 per visit, automatic) |
| Rival kingdoms | Pitax/Brevoy may attempt to commission Leliana directly — player can allow or refuse |

**If a rival kingdom attempts to commission Leliana:**
```
PLAYER CHOICE:
  Allow → Leliana composes one piece for them. She makes it complimentary but not flattering.
           Rival faction disposition +1; Leliana approval −1 (she didn't want to; she did it anyway)
  Refuse → Leliana: "Good. I don't write on commission." Approval +1.
  "Ask Leliana" → She: "Whatever you think is right." [defers to player; no approval change]
```

---

## 💾 THE HALL AND THE OPUS — SAVE BLOCK FLAGS

Add to SaveBlock_Template.md:

```json
"leliana_hall": {
  "hall_proposed": false,
  "hall_built": false,
  "hall_name": "",
  "hall_landmark": false,
  "hall_spontaneous_musicians": false,
  "vault_accessible": false,
  "chronicle_speaks_used": false,
  "rival_commission_attempted": false,
  "rival_commission_accepted": false
},
"leliana_opus": {
  "opus_named": false,
  "opus_name": "",
  "opus_performed": false,
  "opus_print_item": false
}
```

**Mutual exclusion flag (set at gate):**
```json
"chronicler_building": {
  "linzi_shrine_available": true,
  "leliana_hall_available": false,
  "linzi_shrine_built": false,
  "leliana_hall_built": false
}
```

If `leliana_chronicler_mode` becomes true mid-playthrough (Linzi dismissed): `linzi_shrine_available` flips to `false`, `leliana_hall_available` flips to `true`. If Linzi Shrine was already built: it remains but the Hall cannot be built. If neither was built: mutual exclusion applies.

---

## 📊 COMPARISON TABLE — LINZI SHRINE VS LELIANA HALL

| | Linzi Shrine of Returning | Hall of the Unfinished Verse |
|---|---|---|
| **Trigger** | Linzi's death (Ch6) | Leliana's death (Ch6) — she inherits Linzi's death arc, medium-swapped (the old "first public performance" trigger is SUPERSEDED) |
| **Availability** | `linzi_primary_chronicler = TRUE` | `leliana_chronicler_mode = TRUE` |
| **Tone** | Grief and resurrection | Grief and resurrection (same as Linzi, re-skinned to music) |
| **Cost (no existing temple/college)** | 6–10 RP / 21–45 days (varies by god) | 10 RP / 40 days |
| **Cost (max existing building)** | 3–5 RP / 10–20 days (varies by god) | 6 RP / 20 days |
| **Alignment resonance** | Good / Neutral / Evil (player's choice of god) | Neutral (no alignment requirement) |
| **Passive kingdom bonus** | Varies by god; shrine-specific | +2 Culture, +1 Stability, +1 Loyalty, +1 all Stability/Culture events |
| **Active power** | Varies by god; resurrection-focused | "The Chronicle Speaks" — reduce event DC by 4–8 |
| **Landmark tier** | N/A | Yes — fires after `leliana_opus_performed = TRUE` |
| **Landmark effects** | N/A | +1 Fame/turn, foreign dignitary visits, diplomatic +1 |
| **Can fail?** | Yes (price-dependent) | Only if player never triggers Beat 4 of Leliana's quest |
| **Mutual exclusion** | Yes — cannot build if `leliana_chronicler_mode = TRUE` | Yes — cannot build if `linzi_primary_chronicler = TRUE` |

---

*KM_Leliana_Hall (inline) — Kingmaker PF2e Text Adventure | Leliana Concert Hall / Ballad Vault v1.0*
