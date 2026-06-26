# KINGMAKER — PROLOGUE PART 2-B: FINAL BATTLE & THE CALM AFTER
## KM_Prologue_P2_B.md | Pair-load with KM_Prologue_P2.md

> **DM:** Part B of the Prologue P2 file. Always pair-load with `KM_Prologue_P2.md` (Part A covers the Kitchen/Poison investigation path and Phase 3 — the Manor Sweep). This file covers Phase 4 (Final Battle in the Banquet Hall) and Phase 4.5 (The Calm After — companion approaches). Phase 5 lives in `KM_Prologue_P3.md`.

---

## ⚔️ PHASE 4 — THE FINAL BATTLE

### Return to the Banquet Hall

> *The hall is unrecognizable. Windows solid black — orange fire reflected in cracked glass. Table overturned, candles scattered, smoke from above.*

> *Jamandi Aldori — dueling silks, no armor, sword out, bleeding from a cut across her arm. She didn't have time to change. She hasn't retreated an inch. Ezvanki crouches behind the table cycling heals. Around her: the Assassin Leader and his Rift Channelers.*

> *One assassin near the servant door has stopped. He is looking at you.*

> *His body changes — skin going granite-grey, frame expanding. Eight feet. Then nine. The Frost Giant stands where a man was standing. It turns toward Jamandi. The assassins were the distraction.*

> *Tika arrives from the east corridor two rounds into the fight — polearm out, hair plastered, already swinging.*

```
[GM SCENE BRIEF — Banquet Hall Final Battle]
ENEMIES    :
  Assassin Leader (Rogue/Sorcerer 4)
    HP: 48 | AC: 19 (Mirror Image active — 3 images)
    Fort +4 | Ref +9 | Will +6
    Attacks: Rapier d20+8 (1d6+4 P) | Sneak Attack +2d6
    Spells: Mirror Image (active), Protection from Good, Cause Fear
    Loot: Bracers of Armor +1, Potion of Barkskin, Alchemist's Fire ×1, Acid Flask ×2

  Frost Giant (Shapeshifter, resumes true form)
    HP: 62 | AC: 17 | Speed: 35 ft
    Fort +10 | Ref +5 | Will +6
    Greataxe: d20+10 (1d12+8 S, 2-hand)
    Special: Reach 10 ft | Knockdown on crit
    Loot: Greataxe (1d12 S), Chainshirt (AC +3)

  Rift Channelers ×3 (Summoner thralls)
    HP: 16 each | AC: 13
    Claw: d20+4 (1d6+2 S)
    Special: Summon Fiendish Creature (1/each, used if not killed quickly)

ALLIES     :
  Jamandi Aldori (fighting, heavily wounded — do not let her die)
  Ezvanki Keeg (healing Jamandi, non-combat)
  Tika (joins Round 2 if she hasn't already joined — +1 attacker)
  All recruited companions fight alongside player

PRIORITY   : Rift Channelers first → Assassin Leader.
  ⛔ FROST GIANT IS JAMANDI'S FIGHT. Player does NOT target the Giant at any
     point. DM does NOT offer options/menus/rolls against it. `.fail 35`.

IF security_doubled = TRUE (player reported poison):
  Kesten arrives Round 3 with 2 guards → additional allies
  Assassin Leader has only 1 Mirror Image (not 3) — was rushed
```

**Initiative:**
```
🎲 INITIATIVE — FINAL BATTLE
  [Player]          : d20 + [Init] = [total]
  Assassin Leader   : d20 + 6     = [total]
  Frost Giant       : d20 + 2     = [total]
  Rift Channelers   : d20 + 1     = [total] (×3, all same)
  Jamandi (allied)  : d20 + 5     = [total]
  Tika (Round 2)    : d20 + 4     = [total]
```

**Mirror Image rules:**
```
While Mirror Image is active (3 images):
  Each attack roll: d4 → 1-3: hits an image (image destroyed, no damage)
                          4: hits the real Assassin Leader
  Images remaining: 3 → 2 → 1 → 0 (Mirror Image ends)
  Dispel Magic or AOE spell destroys all images simultaneously
```

---

### ⚔️ SCRIPTED DUEL — JAMANDI vs FROST GIANT

> **⛔ Trigger:** Frost Giant drops below 50% HP (31 HP or fewer). DM narrates this immediately. Player's combat turn pauses for 1 round of narration, then resumes.

> *Jamandi breaks from the melee. She is bleeding from three wounds. Her sword arm should not work as well as it does. She strides directly toward the Frost Giant — not running, walking — with the measured pace of someone who has done this before and is not interested in doing it again.*

> *The Giant swings. Jamandi drops under the greataxe — flat, one palm on the floor — and the blade passes over her by inches. She rises inside the Giant's reach, where its weapon is useless and hers is not.*

> *Two cuts. The first opens the Giant's hamstring. The second, rising, takes it across the ribs as it stumbles. Not showy. Not acrobatic. A swordlord's economy — the minimum violence required, delivered with the precision of someone who has spent forty years making a blade an extension of her intent.*

> *The Giant falls to one knee. Jamandi steps back. She is not breathing hard. Her eyes have not changed since she started walking.*

> *That is a swordlord. The title is not inherited. It is proven.*

**Mechanical effect:** Jamandi's strikes KILL the Frost Giant. Not "18 damage" — the duel resolves it completely. Giant HP → 0 at end of narration. Full Giant XP to player (allied NPC credit).

**DM Rule:** Do NOT skip, summarize, or let the player target the Giant before/during/after the duel. Her fight start to finish. This establishes Jamandi as warrior, not politician — referenced by NPCs for the rest of the campaign. Player or Tika stealing her kill = `.fail 35` + Jamandi permanently misread as "noble who needed saving."

---

### Post-Battle — Loot Window

> **IMPORTANT DM INSTRUCTION:** Before the player speaks to Jamandi, remind them explicitly:
> *"Collect all loot before speaking to Jamandi Aldori. You cannot return to the mansion after this conversation."*

**Available loot (all must be collected now):**
```
FROM ASSASSIN LEADER  : Bracers of Armor +1, Potion of Barkskin, Alchemist's Fire ×1, Acid Flask ×2
FROM FROST GIANT      : Greataxe (1d12 S), Chainshirt (AC+3 light armor)
FROM SECRET ROOM      : Masterwork Longsword + Gold Ring (if found in Phase 3)
FROM ARMORY           : Any armor/weapons taken earlier
FROM CHESTS/CORRIDORS : 8 gp (corridor), silver earrings + 35 gp (secret room), 12 gp (library)
JAMANDI'S GIFTS       : Camping Supplies ×1, Rations ×4, Scroll of Raise Dead (given in Phase 5)
```

---

## 🕯️ PHASE 4.5 — THE CALM AFTER

> **DM:** Triggers when the primary crisis is resolved — standard combat, Compressed Assault, Lady Sleeps gambit, or any player-driven resolution. Danger is over. Jamandi has thanked the player and returned control of the room. **Do not skip or rush this into the accusation. The player has earned stillness.**

### ⛔ KITCHEN REPORT — FIRES FIRST IF `poison_reported = TRUE`

**This scene is mandatory before any companion approaches the player.** If `poison_reported = FALSE` or not set, skip entirely and proceed to Triggering the Phase below.

> *Kesten crosses the hall toward Jamandi. He says something brief. She listens without expression, asks one question, and he answers. Then she looks across the room — at you.*

**JAMANDI** *(approaching the player directly, not addressing the room)*: *"The kitchen. You were right."*

**Jamandi:** *"Wine casks dosed through the service entrance. If you hadn't moved when you did, everyone in that hall would have been on the floor when they arrived."* A pause. *"I don't say that lightly."*

> *She returns to Ezvanki and Kassil without waiting for a response.*

**DM:** Set `kitchen_report_delivered = TRUE`. Fires once. Proceed to companion approaches.

**If `shapeshifter_identified_at_feast = TRUE`:** Kesten adds: *"Whatever got in through the service entrance — it wasn't human. Or wasn't human long enough to matter."* Jamandi looks at Kassil. Neither speaks. `shapeshifter_confirmed_at_debrief = TRUE`

---

### Triggering the Phase

**Conditions:** Crisis resolved. Player has stepped back from the spotlight. At least 10 minutes of in-game time pass before Tartuccio triggers Phase 5.

**DM instruction:** Companions approach gradually, stay after speaking, and form a growing group:
- *Early:* 2–3 nearby. One-on-one. *Mid:* 5–6 gathered. *Late:* All present.

**⛔ EARSHOT SCORING.** ALL companions in earshot score relationship shifts (−2 to +2) from EVERY player statement — not just statements aimed at them. A companion who overhears something they deeply agree with gains +1/+2 even if the player was talking to someone else.

**⛔ GATHER RULE.** Companions come to the player — not the other way around. The player stays where they are. Companions approach naturally, drawn by the conversation. This is important: the player is not circulating and recruiting. They are stationary. People come to them. Tartuccio cannot credibly accuse the player of canvassing if the player never moved. NPCs stay until dismissed.

**The room:** Candles, cold food, guards cycling. Jamandi in conference with Ezvanki and Kassil at the far end.

---

### TIKA — She Finds You First

> *She drops into the chair next to you without asking. Polearm leaned against the table, hair still damp from the library fight, the smell of smoke on her tabard. She is already mid-thought.*

**Tika:** *"Back there — you had a bread roll and two napkins. You could've grabbed a sword off any fallen guard. You went with the napkins. Why?"*

She is genuinely puzzled. This is how Tika evaluates people — she asks about the choice that confused her, the one that didn't fit the easier read.

**TIKA** *(after the player explains)*: *"I grew up in an inn. I can tell a loudmouth from a leader in about thirty seconds, and most people fail that read. You didn't. Nobody died tonight who didn't earn it — and that is harder than swinging a sword. Most of the captains who came through our common room would have grabbed the steel."*

She asks follow-up questions — not politics, just the moments where everything was chaos and a decision had to be made before there was time to make it. *"If someone on your team gets left exposed because of your call — what do you actually do that night? Not in principle. That night."*

**Her hidden question:** *"The Black Watch Empire. I've never heard of it, and I served drinks to men who'd marched a long way before I ever picked up a polearm. Where exactly is it? Is it still there?"* Her world is the inn, the road, and the people who walked into her common room. Empires of the east are abstract to her as the moon.

---

### LINZI — She Has Been Waiting Politely for Several Minutes

> *She materializes at your elbow the moment Amiri takes a breath. Notebook out. She has been writing while pretending to be poisoned.*

**Linzi:** *"I'm sorry — I've been trying to wait — Amiri is very filling as a conversationalist — but I have questions and the night is only so long."*

Her questions arrive in rounds: *"When you walked through the gate with Malak in chains — what were you thinking? Not tactically. Personally."* → *"You left your weapons in the garden without being asked. Rehearsed, or decided in the moment?"* → *"The bread roll — when did you pick it up? Before or after the garrote? Because if before, you were planning two things at once while everyone else was playing dead."* → *"After everything — you stepped back. Gave her the room. Why?"*

She does not accept "I don't know." She asks it differently. She believes every answer is in there and she just needs the right question.

**Linzi** *(after any good answer)*: *"Yes. That's the first line of Chapter One."*

---

### TARTUCCIO — He Approaches When You Are Briefly Alone

> *He doesn't come when Amiri or Linzi are there. He waits. When there's a gap — when others have stepped away — he materializes at your side. Not performing.*

**Tartuccio:** *"You are not what I prepared for."* He lets that sit. *"You arrested a man, prevented a massacre, captured an assassination squad, and then sat down and ate cold pheasant. I find that... professionally interesting."*

His questions are designed to find edges: *"The Black Watch Empire — I cannot place it in any geography I know. Where exactly is it located?"* — He is testing whether the player is lying about their background. *"A General who walks in unarmed as a gesture of respect. Either genuine honor or a very sophisticated performance of honor. Do you find that distinction matters?"*

He offers the ring here if he hasn't already — same flag, same Phase 5 implications.

**Tartuccio** *(before he steps away)*: *"I want you to know — whatever Jamandi decides — I did not come here as your enemy. I came as your competitor. Those are different things."* He smiles once, without warmth, and rejoins the guests.

---

### ARTORIA — She Comes When She Has Something Specific to Say

> *No small talk. She crosses the room, stops in front of you, armor still smoking faintly from the burning building. Helmet under one arm. This is a debrief.*

**Artoria:** *"The disarmament at the threshold. You weren't obligated. You had legal standing, momentum, every reason to walk in armed. You chose otherwise. As a gesture."*

*"What is the foundation of your sovereignty — the strength of your arm, or the consent of those you lead? I am asking precisely. I have heard the speech version. I want the unrehearsed one."*

She listens to the full answer without expression. She is already evaluating the gap between what you say and what you mean.

**Artoria** *(if the answer is honest, including "both, and I knew it")*: *"The only honest answer. Good."* She does not relax — Artoria does not relax — but the angle of her shoulders changes by a degree. *"When the resources are low and the winter is harsh, will you eat the same rations as your lowest soldier? Yes or no."*
**Artoria** *(if the answer performs certainty)*: *"A king has no human heart. The performance of certainty is what kills the people who trust it. I will not follow a sovereign who has not yet learned the difference."* — but she does not leave.
**Artoria** *(if "pure calculation")*: *"I held a kingdom together for twenty years on calculation alone. I do not recommend it. But I recognize it."* A nod. *"I will work with what is honest."*

---

### TATSUMAKI — She Finds the Floating Corner of the Room

> *She has not sat down all evening. She is standing — or hovering, technically — about a foot above the floor near a high window, arms folded, considering whether standing was worth it. She does not approach. She allows the player to come to her.*

> *If the player approaches:*

**Tatsumaki:** *"Oh. The napkin person."* She does not look at you. *"You're the one in charge here? You look like a total amateur. Why are you wasting my time?"*

> *She is testing the entry. The contempt is real. The fact that she has not already left is also real.*

**Tatsumaki:** *"I have been in three other rooms tonight that were less embarrassing than this one. The fact that I am still in this room is information about you, not about me. Don't get smug about it."*

A pause. She drifts a fraction lower — not landing, just acknowledging.

**Tatsumaki:** *"If something genuinely threatening shows up — and it will, because this region is held together with string and bad faith — what are you going to do while I handle it?"*

> *She watches the player without turning her head. This is the question she actually wants answered. Everything else was preamble.*

**Tatsumaki:** *"You aren't going to try to give me orders, are you? Hint: don't. I have left places for less."*

**TATSUMAKI** *(if the player gives a real answer — not flattery, not deference, not a pitch)*: *"Hm."* She lands. Briefly. Like she's surprised herself. *"Convince me why I shouldn't just leave. You have about thirty seconds and I'm already bored."* — But she has stopped looking at the door, and her arms have come uncrossed by approximately one inch. That is a commitment.

---

### MORRIGAN — She Waits Until Almost Everyone Else Has Gone

> *She does not approach during the noise. She watches from the long table, where she has been the entire evening, eating little and saying less. When the room thins, she stands. She does not hurry. She arrives.*

**Morrigan:** *"You fought well. You thought while you fought, which is rarer than the sword schools admit."* A pause. *"Do you value power, or the illusion of it? There is a considerable difference, and most rulers spend their entire reign confusing the two."*

She does not ask follow-up questions until she has the answer to that one.

**Morrigan:** *"Sentimentality rots a throne from within — I have watched it happen, more than once, from outside the walls. Are you prepared to make the necessary choice when the comfortable one fails you?"*

A pause. She is testing pragmatism. She is allergic to virtue that costs nothing.

**Morrigan:** *"And the practical question, since I am the one asking it: if the 'righteous' come to your door demanding I be handed over — for what I am, or for what they imagine I am — will you give me up to keep your reputation tidy? Or is your hospitality worth something?"*

> *She is not threatening to leave. She is informing the player of the price of her staying. There is a difference.*

**Morrigan** *(if the player commits without flowery language)*: *"Good. Then I'll stay."* No ceremony. Just a decision. *"I expected to be disappointed tonight. I am tolerably surprised. Do not make me regret the surprise."*

---

### GOLDMOON — She Approaches When Every Wound Has Been Dressed

> *She does not come to the player until every wounded guard has been seen to — not just the urgent ones, the untended ones. The Blue Crystal Staff at her belt has stopped glowing. Only then does she cross to you.*

**Goldmoon:** *"You're checking on everyone, aren't you. Not just the important ones. After Jamandi thanked you, you looked at Biggs and Wedge first. Not her."*

A pause. She is not finished.

**Goldmoon:** *"I have traveled with people who save lives. Some count them like a ledger. Some just move to the next one. I want to know which kind you are — and I do not trust the answer of someone who hasn't been asked it before."*

She does not look away. She is asking gently. She is not asking softly.

**Goldmoon:** *"A shepherd knows the names of their flock. Do you know the names of the people you are asking to follow you? Not their titles. Their names."*

A pause.

**Goldmoon:** *"And a question I learned to ask the hard way — if my presence brings something terrible to your door, will you ask me to leave, or will you stand with me?"*

> *She has died and come back carrying proof the gods exist. She does not take faith lightly, and she does not respect those who use it lightly either. She catches false comfort in a single sentence.*

**GOLDMOON** *(after an honest answer — even an honestly deferred one)*: *"Good. I can work with the truth. I have had difficulty with leaders who could not tell it."* She moves to go. Stops. *"I am not here because you are powerful. I am here because of what you did with the napkins."*

> *Her hidden question is whether your people paid for your ambition. If the player deflects: "You answered the question about the kingdom. I asked about the people." She does not push past one deflection.*

---

### SUCROSE — She Is Trying to Be Brave About This

> *She has rehearsed at least three opening lines. She tries the first one as she sits down — quietly, on the edge of the chair, not committing fully — and immediately regrets it.*

**Sucrose:** *"I — um. Hello. I had a — a better way to start this, I think, but I — okay, I'm just going to — okay."* She takes a small breath. Resets. The voice is still small but the words are now hers. *"How far should research be allowed to go? I'm asking genuinely. I think about this more than people think I do."*

> *She has a small notebook open in her lap. Not Linzi's notebook — diagrams, not narrative.*

**Sucrose:** *"Is knowledge worth risking lives? Whose lives? I'm asking about the specifics, not the principle. The principle answer is — I think the principle answer is a way of not answering."*

A pause. She glances at you, then back at her notebook.

**Sucrose:** *"And if I — if I accidentally created something dangerous, while trying to create something useful — what happens? To me, I mean. I'm asking because I have done it before. I'm not — I'm not proud of that. I'm telling you because the answer matters."*

She closes the notebook on one finger, marking a page.

**Sucrose:** *"Can you give me a quiet space to work, and not ask what's in the vials unless I tell you? That's a real question. I've been chased out of three places for the wrong answer to it."*

**SUCROSE** *(if the player listens — not solves, just listens)*: *"Oh. Okay."* The smallest exhale. *"I — I don't usually ask people things first. I usually just leave when it gets — when it gets like that. I'm going to try not leaving this time. If — if that's all right."*

---

### RYUKO — She Walks Up Loud

> *No approach. She is just suddenly there, scissor blade across her back, hands on hips, looking at the player like she has already decided three things and is checking the fourth.*

**Ryuko:** *"You look like you think you're a big deal."* Flat. Not hostile — diagnostic. *"Are you going to start acting like it the second things go your way?"*

She does not wait for an answer to that one. It was the warm-up.

**Ryuko:** *"Who's really pulling the strings here? I've got a low tolerance for finding out later. So if there's a name above yours, or a treaty I should know about, or a reason you've been told to be nice to me specifically — say it now. I'll respect 'I can't tell you.' I will not respect 'oh, that.'"*

A pause. The intensity drops by a degree, but not the focus.

**Ryuko:** *"And the one that actually matters: are we partners, or am I a weapon you're pointing at things? Answer straight. I've been pointed before."*

> *She has been used — by institutions, by her own blood, by systems that told her the truth was too complicated for her to handle. She spots manipulation before the sentence is finished. She has very good reasons to.*

**RYUKO** *(if the answer is honest — including "honestly, both, and I'm working on the second one")*: *"Hah."* A short, surprised laugh — not friendly, not unfriendly. *"Okay. Yeah. That's not the answer I was expecting. That's why I'm staying."* She turns. Doesn't go anywhere. Just turns enough to be standing alongside you instead of in front of you. That is the commitment.

---

### OLIVIER — She Has Been Drafting an After-Action Report in Her Head

> *Sword sheathed. Posture parade-ground. She approaches at a steady walk, stops at exactly the right distance, and begins speaking before she has finished arriving.*

**Olivier:** *"Twelve minutes from first contact to full containment. No civilians lost. One arrest. Four correct decisions, two survivable ones, one I would have made differently."*

She is not introducing herself. She is filing a debrief.

**Olivier:** *"I don't care about your titles. Can you fight, or are you a pampered mouth in a fancy chair? Tonight suggests the former. Suggests is not the same as confirms."*

A pause. She does not soften.

**Olivier:** *"I will tell you something now and not repeat it. If you give me a command that is tactically unsound, I will ignore it. I will not consult you. I will not apologize. I have held a wall against worse than what is coming, and the way I held it was by not following bad orders. So — can you lead a commander you can't fully control?"*

She lets that sit.

**Olivier:** *"Don't talk to me about potential. I have buried potential. Show me your results — what have you actually accomplished, and at what cost?"*

> *Briggs taught her that potential is a currency commanders spend on themselves. Results are what soldiers go home on.*

**OLIVIER** *(if the player answers without padding)*: *"Acceptable."* Not warm. Final. *"This kingdom looks soft. I expect that will be addressed."* She does not say she is staying. She has assumed it. She turns ninety degrees and now stands at parade rest beside the player's chair, watching the room. She is now your problem.

---

### YOKO — She Waits Until It's Quiet

> *She has been at the back of the room all evening. Rifle propped against her chair. She is not drinking. When the room thins, she comes over without ceremony and sits on the corner of the table — not in the chair.*

**Yoko:** *"What do you actually believe in? Not your goal. The thing underneath the goal."*

She is not asking idly. She is clear-eyed about it.

**Yoko:** *"I've lost people I cared about to big dreams. People who'd have followed someone like you anywhere — and did, and didn't come back. So I'm going to ask you a number question, and I want a number answer if you have one."*

A pause. She does have a number in mind herself.

**Yoko:** *"How many lives are you willing to spend on this? And does that number have a floor?"*

She is not testing whether the player has the right answer. She is testing whether the player has thought about it at all.

**Yoko:** *"And the trigger you didn't pull tonight."* She tips her head toward the gate, where Malak is presumably back at his post. *"Captain at the gate. You had every reason. You didn't. I want to know why. Not the official reason."*

> *She watches the player's hands while they answer. She has learned that hands tell on people before words do.*

**YOKO** *(if the player has a real answer)*: *"Okay."* She picks up the rifle. Doesn't shoulder it — just lifts it from where it's been leaning. *"A leader's back is what their soldiers see the most. I'll ride behind you for a while. I'll let you know if I stop liking what I see."* That is the offer. She does not repeat it.

---

### KYOKO — She Closes Her Notebook Before She Speaks

> *She has been writing all evening. Small notebook, narrow handwriting, the kind that reads as cataloguing rather than journaling. When she is ready, she closes it. She does not put it away.*

**Kyoko:** *"You're hiding something. Everyone is. I am not asking you to tell me what it is — yet. I am asking you a different question."*

A pause.

**Kyoko:** *"Is your secret a threat to what you're trying to build? Be specific. I have already noted three things about you tonight that don't reconcile with the official biography. I have not mentioned them to anyone. I am giving you the opportunity to make me unnecessary on this."*

She does not blink. She does not perform the not-blinking either.

**Kyoko:** *"My working theory of you is that you scan for outliers, not threats. That is unusual. Most leaders scan for threats and miss the outliers, which is why most leaders are surprised by exactly the people they should not have been surprised by. So I want to know — and answer carefully, because I will know — if I find evidence of corruption in your inner circle, will you let me prosecute it? Or will you cover it up?"*

A pause. Last question, and the one she has been working up to all night.

**Kyoko:** *"If I deduce something about you that you didn't want known — what happens next? Not in principle. To me, specifically."*

> *Her father left because the work mattered more to him than she did. She decided that was information about him, not about her. She has been measuring rulers by that standard ever since.*

**KYOKO** *(after the player answers — even honestly badly)*: *"Acceptable."* She opens the notebook again, writes one line, closes it. *"I will continue observing. If at any point my assessment changes, I will tell you to your face. That is a promise — and a courtesy I do not extend to most people."* She does not move. She is staying.

---

### THE WINDOW — WHAT HAPPENS IF THE PLAYER STAYS QUIET

> *If the player takes no action and simply sits with the stillness, the DM runs through the following:*

Tika finds a chair next to you and sits in silence. She doesn't need you to talk — she grew up reading rooms, and she is reading this one. Linzi hovers, closes her notebook, then writes one line and shows it: *"The general came back from the garden empty-handed, and somehow that was the most dangerous thing he did all night."* Tartuccio watches from across the room — does not approach. Artoria stands at the window, helmet under her arm, expression unchanged. Tatsumaki has drifted back near the high window and is pretending not to be watching. Goldmoon finishes bandaging the last untended guard and looks over once, just once, with the kind of attention that doesn't need a return. Sucrose is nervously rearranging the items on her tray and not leaving. Ryuko stands a few paces off with her arms folded and her weight on one hip, daring anyone to ask her if she's staying. Olivier remains at parade rest a step behind your chair. Yoko sits sideways on the corner of the table, the rifle across her knees, eyes on the door. Kyoko writes one more line, closes the notebook, does not put it away. Morrigan refills her wine and watches the room the way a hawk watches a field.

*No one demands anything from you. The silence is earned.*

---

### ENDING THE PHASE — TRANSITION TO PHASE 5

**Phase 4.5 ends when:**
- The player signals readiness (explicitly or by asking what happens next)
- OR Tartuccio begins moving toward Phase 5

> *The hour is late. Candles burn low. Jamandi is watching you from across the hall with the expression of someone making a decision.*
> *Tartuccio smooths his jacket. Steps toward the center of the room.*

> **Phase 5 begins.**

---

> **➡️ Continue in `KM_Prologue_P3.md` — Phase 5: The Accusation, Companion Split, Jamandi's Final Question, Departure, XP Summary.**

*KM_Prologue_P2_B.md — Kingmaker PF2e Text Adventure | Prologue P2 Part B v1.0*
