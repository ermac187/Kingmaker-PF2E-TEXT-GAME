# KINGMAKER — DREAM SEQUENCE SYSTEM
## KM_Dreams.md | Active from: Chapter 1 | Referenced by: KM_Weather_Camping.md, KM_DMRules.md

> **DM:** Dreams fire during Long Rest. They are NOT random — each is gated by story flags. Nyrissa's presence in the Stolen Lands creates fey-touched visions that advance the main plot, offer lore, and grant mechanical effects based on player responses. Dreams are scripted scenes — read them from this file, do not improvise. Maximum 1 dream per 3 Long Rests (prevent fatigue).

---

## 📊 DREAM TRIGGER RULES

1. **Check flags at Long Rest.** If a dream's trigger conditions are met and cooldown (3 rests) has passed, the dream fires.
2. **Dreams interrupt rest** but do not prevent rest benefits. The player still recovers HP/spells.
3. **Player always has choices** inside the dream. Choices affect disposition, flags, and sometimes grant buffs/debuffs.
4. **Dreams cannot be skipped.** They are narrative. The player experiences them.
5. **Track in save block:** `"dream_log": ["D1", "D3"], "dream_cooldown": 0, "dream_buff_active": null`

---

## 🌙 DREAM SEQUENCES

### D1 — THE WRONG FOREST
**Trigger:** Chapter 1, first Long Rest in the Stolen Lands.
**Nyrissa flag:** `nyrissa_awareness: 0` (she is watching but unaware you notice)

*You are walking through a forest that is almost the one you camped in. The trees are the same species but the spacing is wrong — too regular, like someone planted them from a diagram. The light comes from no direction. A path appears that you did not choose to walk.*

*At the end of the path: a garden. Roses grow in colors that do not exist. A woman's voice, very close, says nothing you can hear — but you understand that she is surprised you are here.*

*You wake. The fire has burned to coals. Nothing happened. But the direction of the wind changed while you slept.*

**Effect:** `nyrissa_awareness: 1`. No mechanical effect. Atmosphere establishment.

---

### D2 — THE MIRROR POOL
**Trigger:** Chapter 2, after founding the kingdom. `nyrissa_awareness ≥ 1`

*A pool in the forest. Your reflection is wrong — it wears your armor but the scars are in different places. It looks at you with an expression you have never made. It mouths a word you almost understand.*

*The pool ripples. Your reflection reaches toward the surface. You feel something — not cold, not warm. Recognition.*

**Choice point:**
```
 1. Reach back  → +1 Cunning. nyrissa_early_contact = TRUE. Dream buff: +1 Will saves for 1 day.
 2. Step away   → +1 Blunt. No flag change. No buff. "Not yet."
 3. Shatter the pool  → +1 Ruthless. nyrissa_awareness reset to 0 for 1 chapter (she retreats).
```

---

### D3 — THE BLOOM SEED
**Trigger:** Chapter 3, after first Bloom encounter. `nyrissa_awareness ≥ 1`

*The roses again. This time you can smell them — sweet, with an undertone of decay. One rose is open. Inside: a seed made of something that looks like compressed starlight. The woman's voice is clearer now.*

*"This is what I plant. Do you understand what grows?"*

*The seed pulses in your palm. It is warm. You know — in the dream-logic way of knowing — that if you swallow it, you will understand the Bloom. If you crush it, you will resist the Bloom. If you plant it, you will control the Bloom.*

**Choice point:**
```
 1. Swallow the seed  → nyrissa_backstory_known +1. Dream buff: Bloom creatures hesitate 1 round before attacking you (Will DC 14 to act normally). +1 Scholarly.
 2. Crush the seed    → Bloom resistance: +2 to saves vs Bloom effects for 1 chapter. +1 Blunt. Nyrissa: "Disappointing."
 3. Plant the seed    → nyrissa_early_contact = TRUE. Dark flag: nyrissa_bloom_connection = TRUE. Dream buff: +2 Nature checks involving fey/Bloom. +1 Cunning. Risk: Nyrissa can send messages directly in future dreams.
 4. Wake up           → No effect. Seed disappears. "You are not ready."
```

---

### D4 — THE THOUSAND FACES
**Trigger:** Chapter 3-4, after learning about Nyrissa's curse. `nyrissa_backstory_known ≥ 1`

*A hall of mirrors, each reflecting a different version of Nyrissa. Young. Old. Kind. Monstrous. Weeping. Laughing. Dead. The woman stands at the center, and she is all of them and none of them. She turns to you.*

*"They took my ability to love. Not the memory of it — the capacity. Do you know what it is to remember what you could feel and know that you will never feel it again?"*

**Choice point:**
```
 1. "I'm sorry."  → +1 Merciful. Nyrissa relationship +1. Dream buff: +1 to Diplomacy with fey for 1 chapter.
 2. "That doesn't excuse what you've done."  → +1 Blunt. Nyrissa relationship +0 (she expected this). No buff.
 3. "Is there a way to restore it?"  → +1 Scholarly. nyrissa_saveable flag +1. Dream buff: +2 to Recall Knowledge about First World for 1 chapter.
 4. "I know exactly what that is."  → +1 Merciful. Nyrissa relationship +2. Nyrissa: silence. Then: "Perhaps you do." (Strongest emotional impact.)
```

---

### D5 — THE LANTERN KING'S SHADOW
**Trigger:** Chapter 4+. `nyrissa_backstory_known ≥ 2`

*The dream is not Nyrissa's. Something else is here — vast, amused, and cruel. A lantern floats in darkness. Its light shows you things: your kingdom burning. Your companions dead. Your throne empty. The Lantern King's voice is laughter shaped into words.*

*"Everything you build, I will take. This is what I do. I take the things that matter most."*

*The lantern goes dark. You are alone in nothing.*

**Choice point:**
```
 1. Defy him. "Try."  → +1 Blunt. Will save DC 20. Success: resist the fear, +2 Will saves for 1 day. Failure: Frightened 1 until next rest. Either way: Lantern King takes notice.
 2. Study the darkness.  → +1 Scholarly. Recall Knowledge (Occultism DC 18). Success: learn one Lantern King weakness. Failure: headache, Stupefied 1 for 4 hours.
 3. Say nothing.  → +1 Cunning. No immediate effect. But: lantern_king_aware = TRUE. This flag matters in the final chapter.
 4. Wake up screaming.  → No flag. No effect. Companions check on you. Moment of vulnerability.
```

---

### D6 — THE GARDEN AT THE END
**Trigger:** Chapter 5+. `nyrissa_saveable ≥ 2`

*Nyrissa's garden again. But this time you are expected. A chair. A table. Two cups of something that smells like rain. She sits across from you and for the first time does not speak in riddles.*

*"I am running out of time. The Bloom is not my weapon — it is my curse consuming me. When it finishes, I will be gone. Not dead. Gone. The difference matters."*

*"You are the first person in a thousand years who has stayed long enough to hear this."*

**This dream has no choice menu.** The player responds naturally. DM voices Nyrissa based on KM_NPC_Relations_A.md profile. The conversation is the reward. At the end: `nyrissa_saveable +1`, `true_ending_flags +1`.

---

### D7 — THE CHOICE (Pre-Final Chapter)
**Trigger:** Chapter 6, before final dungeon. All `nyrissa_saveable ≥ 3`

*No garden. No pool. Just a road — the same road you walked to Restov at the beginning. Nyrissa walks beside you.*

*"If you find my love — the piece they cut from me — and return it... I don't know what happens. Nobody has tried. But I think the Bloom stops. I think I become... something I forgot how to be."*

*"Will you look for it?"*

**Choice point:**
```
 1. "I will."  → true_ending_path = TRUE. Final chapter: alternate objectives added.
 2. "I'll try."  → true_ending_path = "uncertain". Modified final chapter.
 3. "I can't promise that."  → No flag. Standard final chapter.
 4. "I already know where it is."  → Only if nyrissa_backstory_known ≥ 4 AND scholarly ≥ 5. Nyrissa: stunned silence. true_ending_path = TRUE, golden_ending_eligible = TRUE.
```

---

## ⚠️ DM RULES

1. **Dreams are scripted. Read them exactly.** Do not improvise dream content. The words are chosen.
2. **1 dream per 3 Long Rests maximum.** More frequent = player feels harassed. Less frequent = they forget the thread.
3. **Never announce the dream name.** The player doesn't see "D3 — THE BLOOM SEED." They experience it.
4. **Dreams are private.** Companions don't share them. If the player tells a companion, the companion reacts in-character.
5. **Dream buffs last 1 day** (or 1 chapter where noted). Track as temporary condition.

---

---

## 🌑 COMPANION DREAM INTRUSIONS

> **DM:** At Devoted (+2) relationship, a companion's presence can bleed into the player's dreams. These are not Nyrissa dreams — they are the player's subconscious processing the people around them. One companion intrusion per 5 Long Rests maximum. They do not count against the Nyrissa dream cooldown.

### CD-1 — AMIRI: THE GIANT'S SHADOW
**Trigger:** Amiri at Devoted. After her quest fires.
> *You dream of a hill. Amiri stands at the top. Behind her — a shadow ten times her size. It has her shape but holds a sword that blocks the sun. She does not turn to look at it. She is looking at you. "Is that me?" she asks. "Or is that what I was afraid I'd become?"*

No choice. The dream ends. +1 Bond Moment with Amiri logged.

### CD-2 — LINZI: THE UNWRITTEN PAGE
**Trigger:** Linzi at Devoted. After she has documented 3+ major events.
> *A library with no walls. Books stacked to a sky that is also pages. Linzi sits at a desk in the center, writing. You look over her shoulder. The page is blank. "I know every word of your story," she says without looking up. "But I don't know how it ends. That's the only page that matters, and I can't write it until you do."*

No choice. +1 Bond Moment with Linzi.

### CD-3 — JAETHAL: THE EMPTY MIRROR
**Trigger:** Jaethal at Devoted OR Hostile. Fires either way — different tone.
> *A dark room. One mirror. Jaethal stands before it. The mirror shows nothing — not darkness, nothing. "I used to see myself," she says. "Now I see what I am. Do you know the difference?"*

**If Devoted:** She turns to you. "You are the first person in a century who looked at what I am and stayed."
**If Hostile:** She turns to you. "You looked at what I am and decided it disgusted you. You were not wrong."

+1 Bond Moment regardless.

### CD-4 — REGONGAR: THE CHAIN
**Trigger:** Regongar at Devoted. After his quest Stage 2.
> *A forge. Regongar stands at the anvil. He is making a chain — link by link. You realize he is making it for himself. "This is what I know how to build," he says. "I break them and then I build new ones. I don't know how to build anything else." He looks at the chain. "Teach me."*

No choice. +1 Bond Moment.

### CD-5 — SEELAH: THE OATH
**Trigger:** Seelah at Devoted. After receiving her title.
> *A cathedral. Seelah kneels at the altar, but the altar is your throne. She is not praying. She is making an oath. The words are in a language you don't know — but you understand every one. When she rises, her armor is brighter than when she knelt.*

No choice. Seelah gains permanent +1 to saves while in the player's party. +1 Bond Moment.

---

## 🔥 NIGHTMARE SEQUENCES

> **DM:** Nightmares fire when things go badly — party Morale ≤ 2, major companion death, kingdom crisis. They are not Nyrissa's doing. They are the player's own fear. No buffs — only narrative weight.

### N-1 — THE EMPTY THRONE
**Trigger:** Kingdom Unrest ≥ 15.
> *Your throne room. Empty. Not abandoned — everyone left. Chairs pushed back. Cups half-finished. They didn't flee. They simply decided, together, that you were no longer worth staying for. The door is open. You can see them walking away. None of them look back.*

You wake. Morale does not change. But the dream sticks.

### N-2 — THE COMPANION GRAVE
**Trigger:** Any companion drops to 0 HP and is stabilized (close call).
> *A cemetery you don't recognize. One grave is fresh. The name on the stone is [companion who nearly died]. The date is tomorrow. You try to read the epitaph but the letters rearrange every time you look.*

You wake. +1 Urgency Stage for that companion's quest (if active).

### N-3 — THE GREEN LIGHT
**Trigger:** After taking 50+ damage in a single combat (brutal fight).
**Source:** KM_Backstory_eRmaC.md — The Final Battle

> *You are at the front lines. Where you always are. Where you always will be.*
>
> *The battle runs itself through your mind like a map: three casters positioning
> for a coordinated strike — mark them for elimination. A wounded ally falling
> back bleeding — medic dispatched. Eastern flank pushing too far forward,
> risking encirclement — pull them back fifteen yards. Northern group holding
> strong, potential breakthrough — redirect reinforcements.*
>
> *This is command. This is war.*
>
> *Then you see it. Green light, west. Not a hostile spell — you know those.
> Wrong color. Wrong trajectory. Buff spell? Summon? Nothing to be alarmed about.*
>
> *It crosses the battlefield. It weaves between combatants. It heads straight
> for you.*
>
> *Odd, but not dangerous.*
>
> *You focus back on the battle. Enemy formation weakening on the left flank —*
>
> *The green light hits you.*
>
> *Reality screams.*
>
> *The battlefield vanishes. Dystopia vanishes. Everything you fought for, bled
> for, killed for —*
>
> *Gone.*
>
> *You are in darkness. Wrong air. Unknown stone beneath your hands. Alone.
> And you understand with absolute clarity: they couldn't kill you. So they
> moved you.*
>
> *You kneel in the dark for a long time.*
>
> *Then you are here. This fire. This camp. These people.*
>
> *Your hands are shaking.*

You wake. No mechanical effect. If the player tells a companion — that companion
gains +2 relationship (they witnessed what it cost to rise). +1 Scholarly if
the player asks questions about the memory rather than suppressing it.

---

### N-4 — THE BROKEN WALL
**Trigger:** After a successful defensive siege or a near-collapse reversed by
a single decision. Also fires if the party holds a position outnumbered 3:1+.
**Source:** KM_Backstory_eRmaC.md — The Broken Wall

> *The siege engines are singing. The wall is crumbling. A soldier — young,
> terrified — runs to you through smoke.*
>
> *"Sir! The corner wall — it's half destroyed! They outnumber us five to one!
> We can't —"*
>
> *"Destroy it."*
>
> *The look on his face. The disbelief.*
>
> *"Do you trust me?"*
>
> *Smoke between you. Another section collapsing. Someone screaming for medics.*
>
> *"Do. You. Trust. Me?"*
>
> *"...Yes, General."*
>
> *You give the order. Your own mages bring down your own wall. The enemy sees
> the breach. They charge. Hundreds. Funneling through like water through a
> broken dam, screaming that Dystopia will burn.*
>
> *You raise your hand.*
>
> *You drop it.*
>
> *"NOW."*
>
> *The kill zone erupts.*
>
> *When the dust settles, the enemy commander stares at the mountain of his
> own men. And sounds the retreat.*
>
> *We didn't lose the wall. We gave them the wall.*
>
> *You wake. The camp is quiet. You gave the same order today. Different wall.
> Same principle.*

You wake. Dream buff: +2 to tactical decisions involving fortified positions
or defensive setups for 1 day. The player may reflect on the parallel to
today's battle — DM draws the connection if it is obvious.

---

### N-5 — THE MENTOR'S FLASK
**Trigger:** A companion's loyalty drops sharply in a single session (−3 or
more). Or fires when eRmaC extends deep trust to someone new for the first time.
**Source:** KM_Backstory_eRmaC.md — The Revolt

> *A flask. Two men sharing it by firelight. Three nights ago.*
>
> *You remember the weight of it in your hand. The smell of the fire.
> The easy way he laughed at something you said.*
>
> *A mentor. A man whose tactics you had studied. Whose decisions you had
> trusted without examining.*
>
> *Three nights ago.*
>
> *Now you stand in the smoke of burning tents and you can hear his voice —
> the same voice that laughed — giving orders to kill your people.*
>
> *The most dangerous threat isn't the army at the gate.*
>
> *You wake. Someone in the camp shifts in their sleep. You lie still
> and watch the fire and do not go back to sleep.*

No mechanical effect. If the player tells a companion about this dream,
that companion gains +1 relationship regardless of current standing — they
understand something about why he watches them the way he does.

---

### N-6 — THE PROMOTION
**Trigger:** After receiving a major title, responsibility, or formal command
(charter, founding the kingdom, being named a lord).
**Source:** KM_Backstory_eRmaC.md — The Promotion

> *The war room. The empty chairs.*
>
> *Thighs Deadlyflesh stands across from you. He looks older than you
> remember. Or perhaps you are only now seeing it.*
>
> *"We have no generals left," he says. "We need one voice."*
>
> *"Can you bear that weight?"*
>
> *You think of the soldiers who followed you when you had no authority.
> The walls that held because you told them they could.*
>
> *"Yes."*
>
> *"Then kneel."*
>
> *You kneel. His hand falls on your shoulder.*
>
> *"This burden cannot be shared. This responsibility cannot be divided.
> You stand alone at the top of the chain of command."*
>
> *"Do you accept?"*
>
> *"I accept."*
>
> *"Then rise, General. And may the gods you don't believe in have mercy
> on your enemies."*
>
> *"Because you won't."*
>
> *You rise.*
>
> *You wake. The weight is still there. It was always going to be there.*
> *That's why you said yes.*

Dream buff: +1 to all Leadership checks for 1 day. The player may choose to
reflect on the parallel between this moment and what they just received.
If shared with Regill: he says nothing. He nods once. +1 relationship.

---

### N-7 — THE MOURNING
**Trigger:** After being separated from companions for an extended period, or
after a companion is lost (0 HP, captured, or missing).
**Source:** KM_Backstory_eRmaC.md — The Mourning

> *Dystopia's central square. The Tree of Life behind him, its branches moving
> in wind that carries something heavier than air.*
>
> *Thighs Deadlyflesh stands before the crowd. His voice carries across
> the silence.*
>
> *"We do not know if he lives. We do not know where he is."*
>
> *The crowd is still. The soldiers are still. Even the merchants are still.*
>
> *A woman calls out: "He taught us to stand fast!"*
> *A soldier: "He taught us that honor isn't negotiable!"*
> *A child: "He taught us that the strong protect the weak!"*
>
> *And then the voice that carries everything:*
>
> *"THE GENERAL IS LOST, BUT HE IS NOT FORGOTTEN!"*
>
> *A thousand voices answering.*
>
> *You wake. The camp is intact. Your companions are here.*
> *They are still here.*
> *You lie still and listen to them breathe and say nothing.*

No mechanical effect. If the player reaches out to a companion in the morning
— any gesture, any word — that companion gains +1 relationship. The dream
tends to produce quiet mornings.

---

*KM_Dreams.md — Kingmaker PF2e Text Adventure | Dream Sequence System v2.0*
*12 dreams: 7 Nyrissa, 5 companion intrusions, 3 nightmares. Inspired by BG2 Slayer dreams.*
