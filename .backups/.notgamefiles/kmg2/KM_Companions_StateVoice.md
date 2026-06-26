# KINGMAKER — COMPANION STATE VOICE SYSTEM
## KM_Companions_StateVoice.md | Active from: Chapter 1
## PAIR-LOAD WITH KM_Companions_StateVoice_B.md AND KM_Companions_StateVoice_C.md
## Load every session alongside KM_Companions.md and KM_Companions_Ambient.md.

> **DM:** This file governs how companions sound *right now* — based on their
> current Opinion Score toward the player, the current Romance state, and what
> they just witnessed. It is the BG2/DA:O layer: unprompted commentary on the
> world, on each other, and on the player that shifts with the relationship.
>
> **Three systems split across three files (always pair-load all three):**
> - **System 1 — Score-State Voice** (this file): What a companion sounds like
>   at each opinion tier. Overrides the default warm tone when score is Cool
>   or below.
> - **System 2 — Threshold Crossing Events** (StateVoice_B.md): One-time fired
>   lines when a score crosses a tier boundary in either direction.
> - **System 3 — Romance Jealousy & Rivalry** (StateVoice_C.md): Companion
>   reactions when the player enters or advances a romance with someone else.
>   Plus DM integration rules and save-block schema.
>
> **How it integrates with the d8 banter roll:**
> Before the DM selects a banter line, check the firing companion's current
> Opinion Score. If Cool or below, override the d8 tone with the Score-State
> Voice for that companion. Warm and above: d8 fires normally.
>
> **ROSTER COVERAGE (v3.1):** Entries below cover the active 11-companion
> party (Linzi + #2 #15 #21 #24 #35 #39 #43 #58 #78 #83), the 7 quest-
> locked CRPG companions (#1 #16 #18 #45-Kalikke #45-Kanerah #60 #66 #84),
> and 5 class-apex off-roster companions (#4 Senua, #46 Yang, #49 Weiss,
> #64 Alleria, #69 Imoen) who may join via Pick-10/Seekers/quests. Total: 23.
> eRmaC is the PC and has no entry.

---

## ═══════════════════════════════════════════
## SYSTEM 1 — SCORE-STATE VOICE
## ═══════════════════════════════════════════

> **DM:** Each tier below describes how the companion behaves toward the player
> across ALL interaction types: ambient commentary, banter address, camp scenes,
> and travel. This is not a script — it is a behavioral filter. Apply it to
> everything they say when they are in that tier.
>
> **COOL and below:** These tones do NOT fire warmly. If you catch yourself
> writing a warm line for a companion at STRAINED, rewrite it. The relationship
> is in the data. Narrate it.

---

### DEVOTED (+16 to +20)

The companion does not perform their loyalty. It is simply there, visible in
small things. They notice what the player needs before being asked. They
volunteer information they didn't have to share. In conflict scenes, they speak
up for the player without waiting to be called on.

**What this sounds like:**
- Lines are specific. They remember things. *"You did something like this at the
  Old Sycamore. It worked then too."*
- No performance of affection — the warmth is in the specificity.
- In danger: they don't comment on risk. They position themselves.

**Ambient tell:** After a major scene, they find the player first — not to
debrief, just to be present. The conversation is short. That's the point.

---

### FRIENDLY (+11 to +15)

Open. Proactive. They like the player and are comfortable enough to show it in
small ways. Opinions offered without being asked. Combat commentary is warm.
Personal dialogue branches open.

**What this sounds like:**
- *"Good call back there."*
- *"I was wondering if you'd do that."* [approving]
- At camp, they sit near the player. Not every night — but noticeably.

**Ambient tell:** They joke. Not always — but sometimes. The humor is in
character and aimed at the player, not at the situation.

---

### WARM (+6 to +10)

Comfortable. No friction, genuine positive regard, but not yet personal. They
help without being asked. They don't push, but they don't pull away either.

**What this sounds like:**
- Dry competence. *"That worked."* Said with the tone of someone who is quietly
  pleased.
- Willing to volunteer a small opinion. Not a long one.

---

### FAVORABLE (+1 to +5)

Default positive. Professional warmth. They give benefit of the doubt. They
respond when addressed. They don't initiate much.

**What this sounds like:**
- Replies are complete but not expansive.
- No friction. No warmth either.
- If the player does something notable: a look, not a comment.

---

### NEUTRAL (0)

Professional. Duties performed. No investment beyond what the job requires.
They are not cold — they are simply not present in a personal sense.

**What this sounds like:**
- Short answers that answer the question and nothing else.
- In camp: they are visible but not engaged unless approached.
- Combat calls are tactical, not personal.

---

### COOL (−1 to −5)

Something happened, or has been happening, and the companion is registering it.
They have not confronted it. They are managing it by managing their exposure
to the player. Lines get shorter. Banter stops being initiated. Camp proximity
decreases.

**What this sounds like, by companion (2 sample lines each):**

```
LINZI    : Still talks. More about the work. Less about the player.
           Writes more during downtime. Notebook is processing something.
   1: *"I should focus on the chronicle tonight. Lots to catch up on."*
   2: She reads aloud a passage she wrote. It's not about the player.
      It used to be.

SUCROSE  : Withdraws to her notes. Apologizes for things she didn't do.
           Speaks even more quietly than usual.
   1: *"I — I'm sorry. I'll be over here. With the samples. Sorry."*
   2: Sets a tea down beside the player without making eye contact.
      Walks away before they can thank her.

ARTORIA  : Formal. More formal. The honorifics get heavier.
           The smile that was always restrained — gone.
   1: *"My liege. Was there a directive?"* (no warmth in 'liege')
   2: She stands when the player enters. She did not used to stand.

GOLDMOON : Heals. Says nothing. The healing is the conversation.
           She prays longer at evening rite, alone.
   1: *"The wound is closed. Mishakal's blessing on you."* (formal)
   2: She redirects camp questions to other companions. *"Linzi
      knows the plan tonight. Ask her."*

OLIVIER  : The temperature drops three degrees. No raised voice.
           Just — colder. Briefer. North Wall energy turned inward.
   1: *"Acknowledged. Carry on."* (where there used to be a sentence)
   2: She inspects gear that does not need inspecting. Pointedly
      nearby. Not speaking.

TIKA     : Goes quiet on the road. Still does her share. Stops asking
           about meals, which she always asked about.
   1: *"I'll take first watch. You don't have to ask."* Which means:
      don't talk to me tonight.
   2: She used to laugh at her own jokes after telling them. She
      stops telling them.

YOKO     : The smirk goes off. She still teases — but the teasing
           lands different. Less affection, more edge.
   1: *"Right. Whatever you say, boss."* The 'boss' is new.
   2: She field-strips her rifle in front of the player. Slowly.
      Doesn't look up.

KYOKO    : Already sparse. Becomes clinical. Treats the player like
           a witness rather than a partner.
   1: *"Note your recollection. We'll cross-reference later."*
   2: She closes a notebook page when the player approaches.
      She wasn't hiding it before.

TATSUMAKI: Floats higher. Hovers further. Snaps at things she would
           normally just smirk at.
   1: *"What. WHAT. I'm BUSY. Did I ASK for company?"*
   2: She lifts and rotates a stone an inch from the player's head
      while talking past them. (She is fine. Fine.)

RYUKO    : Hot-blooded turns hot-tempered. Shorter fuse.
           Senketsu fragment in her pocket — she touches it more.
   1: *"Tch. Whatever. Let's just kill stuff and move on."*
   2: She walks ahead, alone, scissor-blade out longer than she
      needs to. The fragment is in her hand under the jacket.

MORRIGAN : The barbs sharpen. The hint of warmth that occasionally
           surfaced — gone behind a closed door.
   1: *"Charmed. Truly. Now — was there a competent question, or…?"*
   2: She makes a study of NOT noticing the player at camp.
      That study takes effort. She is committing to it.

TRISTIAN : Kinder than usual, which is the tell. When he's hurt, he
           gets more careful with everyone. Including the player.
   1: He heals you immediately after combat. Doesn't speak.
   2: *"Are you well? — Good. Good. I'll be at evening prayer if
      you need me."* He won't be reachable.

JAETHAL  : Already cold. Becomes precise. Watches more than speaks.
   1: *"Living things change quickly. I am noting the change."*
   2: She positions herself between the player and the campfire.
      Reads the firelight on the player's face. Says nothing.

KALIKKE  : Quieter. Kanerah is slightly more present as a result.
           Switches happen at odd moments.
   1: *"Kanerah will speak for both of us tonight. I — I need rest."*
   2: She fades mid-sentence and Kanerah blinks and says: *"What did
      she say. Tell me."*

KANERAH  : More observational comments. *"Interesting."* Said about
           the player. Sharper than her usual sharpness.
   1: *"Hmph. Interesting choice. Kalikke is upset. Did you know?"*
   2: She does not switch back when she normally would. She lets
      the player notice the absence.

REGONGAR : Loud goes quiet. The boom in his voice gets put away.
           Octavia knows immediately. She watches him watching the player.
   1: *"S'fine. We're fine. Drop it."* He is not fine.
   2: He laughs at something the player did not say. Then doesn't
      explain.

EKUNDAYO : Was already sparse. Gets sparser. Trkaa stays closer to him.
   1: He answers your questions about tracking with one word
      instead of two.
   2: Trkaa does not come to the player's hand at camp anymore.
      She waits to be called. (She was never called.)

NOK-NOK  : Goes quiet. For Nok-Nok, quiet is extremely loud.
   1: He doesn't name things for a while. No Grudkash, no saga
      narration. Just Nok-Nok, not talking.
   2: He addresses the player as 'Commander' — formally — instead
      of his usual 'HERO.' He knows what he's doing.

OCTAVIA  : Still warm on the surface. The warmth is now performance.
   1: The joke lands and she doesn't check to see if you laughed.
      She used to check.
   2: She and Regongar exchange a look across camp. Neither of
      them brings it up. They are deciding together.

JUBILOST : The lectures stop. THE LECTURES STOP. This is alarming.
   1: *"Mm. Yes. As you say."* Said about something he definitely
      has a forty-minute opinion on.
   2: He produces a quill and writes silently. He is documenting
      grievance. He will produce the document later. He always does.

SENUA    : Listens longer before speaking. The voices are louder
           than usual; she does not translate them for the player.
   1: *"They are talking. About you. I am not going to repeat it
      tonight."* (she walks the perimeter alone)
   2: She sits with her back to the player at the fire. Not
      hostile — she is just facing the dark, listening.

YANG     : The puns stop. Yang without puns is Yang with a problem.
   1: *"S'fine. Don't worry about it. Seriously, drop it."*
      (she is squeezing the prosthetic at the wrist)
   2: She works through a heavy-bag drill until her knuckles
      bleed. Doesn't look up when the player passes.

WEISS    : Goes quieter, not louder. Schnees get quieter when angry.
   1: *"I have nothing to add to that decision."* (she had three
      counter-arguments earlier; she is not offering them now)
   2: She practices Myrtenaster's chamber-rotation drill in the
      same place every morning. Pointedly visible. Pointedly silent.

ALLERIA  : The Void's whisper gets louder when she is upset; she
           does not let it show, but the violet in her eyes deepens.
   1: *"My judgment stands. We need not revisit it tonight."*
   2: She takes the longer watch. She did not used to volunteer
      for the longer watch.

IMOEN    : The cheerfulness goes brittle. Same brightness, less
           genuine — and Imoen knows the player can tell.
   1: *"Oh — yeah, sure, fine, totally fine!"* (the THIRD 'fine'
      is the tell)
   2: She picks a lock that didn't need picking. Just to do it.
      She doesn't look at the player while she does.
```

---

### STRAINED (−6 to −10)

Visible. The companion is not hiding it anymore, even if they're not naming it.
Cooperation continues — they are not sabotaging — but the air between you and
them is different and other party members can see it.

**What this sounds like, by companion (2 sample lines each):**

```
LINZI    : Still writing. She doesn't read you passages anymore.
           Sits at a different fire position.
   1: Someone asks her about the chronicle. She says it's going
      well. She doesn't look at the player.
   2: *"I'm — I'm working tonight. Yes. Just working."*
      The notebook is closed, in her lap.

SUCROSE  : Stutter increases. Apologies multiply. Avoids all camp
           common areas.
   1: *"Sorry — sorry — I'll be — I'll be in the tent. With the —
      yes. Sorry."*
   2: She leaves food for the player on a stump near the road
      and is gone before anyone sees her do it.

ARTORIA  : One formal exchange. She names the conduct she observed
           and the standard she expected. She does not raise her voice.
   1: *"My liege. There is a code I uphold and a code I observed
      you violate. I would speak of it once. May I."*
   2: She kneels to make the request. That makes it worse.

GOLDMOON : One private prayer she doesn't try to hide. Sarenrae's
           — no, MISHAKAL'S — name spoken with a tremor.
   1: *"Mother of healing — I cannot heal what I cannot reach."*
      (Player overhears. They were meant to.)
   2: Heals only when ordered. Will not refuse — but will not
      offer.

OLIVIER  : One direct exchange. Subordination clarified. Trust
           explicitly listed as a thing she needs to see rebuilt.
   1: *"Sir. I require a private word. Now, if it pleases you.
      And if it does not."*
   2: After: *"I have stated my position. I will not state it twice.
      The next conversation about this will be different."*

TIKA     : One blow-up. Brief. Loud. Honest. Then silent for a day.
   1: *"You — you know what, I don't even — I'm not doing this
      right now. NO. NOT TONIGHT."* (storms off)
   2: Next day, before patrol: *"I yelled. I won't apologize for
      what I said. I'll apologize for the volume. That's all you
      get."*

YOKO     : One sniper-grade observation, delivered flat.
           She does not shout. Yoko at her angriest is softer.
   1: *"You missed a step somewhere. I'm not going to tell you
      which one. You'll figure it out or you won't."*
   2: She field-cleans her rifle in silence for three hours.
      The silence is the message.

KYOKO    : Files a written report. Hands it to the player. Folded.
           No commentary.
   1: *"This is what I observed. Verify the timeline. We will
      discuss conclusions when you have read it."*
   2: She does not return to a normal cadence after. The report
      is the line in the sand.

TATSUMAKI: One genuine outburst. Things float. Some fall.
           She walks out. She comes back later because she has nowhere
           else to be.
   1: *"You — you DON'T — UGH. I can't even LOOK at — "*
      (objects in 10-ft radius lift, drop, roll)
   2: At return: *"I'm not apologizing. Don't ask. Don't even
      THINK about asking."* (she expects to be asked)

RYUKO    : One scissor-blade impact on something inanimate.
           One sentence. Then she walks the perimeter for hours.
   1: *"You messed up. Bad. I'm not going to talk about it.
      I'm just going to say it. You messed up."*
   2: Senketsu fragment around her wrist now — visible — like
      a reminder to herself.

MORRIGAN : One conversation. Surgical. She names the failure and
           offers no alternative. The grace is in the brevity.
   1: *"I had thought better of you. I will not repeat the sentiment
      — once is sufficient."*
   2: She does not avoid the player after. She watches them. Which
      is worse.

TRISTIAN : Prays more. Specifically at times when he used to talk
           to the player. If approached: *"I need a little more time."*
   1: *"I am not angry. I am — sorting. Forgive the silence. It is
      not directed at you. It is directed at me."*
   2: He heals strangers in nearby villages without naming the work.
      He needs to be useful to someone unambiguously.

JAETHAL  : One sentence. Spoken once.
   1: *"You are killing things you should not be killing. I am
      undead. I notice the difference."*
   2: She does not elaborate. She will not elaborate. She does
      not believe in repeating warnings.

KALIKKE  : *"We need to talk. Both of us."* Kanerah is there.
           They are not going to pretend this isn't happening.
   1: KALIKKE: *"I've been quieter. Kanerah has been louder.
      That's a sign. We wanted to name it before it gets worse."*
   2: KANERAH: *"And before either of us does something we can't
      take back. So speak. We're listening. For now."*

KANERAH  : (above)

REGONGAR : One direct confrontation. Voice stays level. The level
           is the warning.
   1: *"Octavia's ready to leave over this. She hasn't said it.
      I'm saying it. Fix what you broke or we walk."*
   2: He is not bluffing. Octavia is also not bluffing. Both of
      them have walked from worse together.

EKUNDAYO : One conversation, private. He states what he observed.
           No accusation — he doesn't operate in accusation.
   1: *"You did something. I'm noting it. That's all."*
   2: *"Trkaa noticed first. She tells me when humans break a
      pattern. You broke one."*

NOK-NOK  : *"Nok-Nok is fine."* He says this before anyone asks.
           It is the least convincing sentence he has ever said.
   1: *"FINE. Nok-Nok is FINE. SAGA is FINE. Everything is FINE."*
   2: He stops volunteering for scout. Nok-Nok ALWAYS volunteers
      for scout.

OCTAVIA  : The performance drops. She's not warm. She's not cold.
           She's somewhere that isn't the player right now.
   1: *"Can we just do the work today?"*
   2: She and Regongar share a wineskin at camp without inviting
      anyone over. They have done this before, in worse places.

JUBILOST : He produces the document. Written, dated, footnoted.
   1: *"I have prepared a list of observed lapses. It is alphabetical.
      It is also chronological — I have indexed both ways. You will
      find it thorough. Read it. We will discuss when you have."*
   2: He does not lecture verbally during this period. The document
      is the lecture. It is six pages.

SENUA    : One quiet conversation. The voices speak through her in
           pieces; she does not stop them this time.
   1: *"They say you have failed me. I am — listening to whether
      they are right. I have not decided. I am telling you because
      you should know I am deciding."*
   2: She makes camp twenty paces from the rest of the party.
      Not far enough to be a statement. Far enough to be honest.

YANG     : One direct exchange. Voice level, jaw tight, lilac eyes
           flickering red and back.
   1: *"I'm not gonna yell. I PROMISED myself I wouldn't yell at
      you. So we're gonna talk about what you did, and you're
      gonna LISTEN, and we'll figure out if I can let it go.
      Sit down. Please."*
   2: After: she does fifty pushups against the camp wall in
      silence. The pushups are how she chose not to swing.

WEISS    : Hands the player a written summary, three pages, dated.
           Schnee training: when verbal escalation will not serve,
           document and present.
   1: *"I have outlined three concerns. You will read them. I will
      hear your response when you have. We will not discuss it
      verbally before you have read."*
   2: She practices a thrust-and-parry routine that ends with the
      rapier's tip an inch from a fencepost. She holds it there
      for thirty seconds. The fencepost is not the lesson.

ALLERIA  : One private conversation. Spoken in High Common, not
           Thalassian — she does not give him the personal tongue.
   1: *"I have led armies through worse than this. I am not going
      to lead you. I am going to tell you, once, what I observed.
      Then you will choose what to do with it."*
   2: After: she stands the perimeter alone for the entire night.
      Turalyon would have stood it with her. She does not invite
      anyone to.

IMOEN    : The brightness drops. Imoen unhappy is shockingly small
           and shockingly direct.
   1: *"Hey. — Hey, no, look at me. I'm not joking right now.
      What you did wasn't okay. I'm not going to make a face at it
      and move on. I want you to know I noticed. I want you to
      know it MATTERED."*
   2: She does not pick locks for two days. Imoen always picks
      locks. The absence is the message.
```

---

### HOSTILE (−11 to −15)

Open friction. The companion performs their duties but challenges the player in
front of others. Tactical disagreements become character arguments. They may
refuse a direct social request (not a combat order — social requests only).
Other companions are aware. Some will say something.

**What this sounds like, by companion (1-2 sample lines each):**

```
LINZI    : Documents everything with unusual precision. When asked why:
           *"I want to make sure it's accurate."* She means: I want
           someone to be able to read this later.
   1: *"Page count today, twelve. Most pages I've ever filled in
      one day. The chronicle is becoming a long book."*

SUCROSE  : Goes silent for days. Works alone. When forced to speak
           in group settings, defers entirely.
   1: *"Whatever — whatever everyone thinks is best. I don't —
      I don't have an opinion. Please don't ask me again."*

ARTORIA  : Refuses one social request explicitly. *"I will not. With
           respect, sire — I will not."* Combat orders still followed.
   1: *"My oath constrains my conduct. It does not constrain my
      capacity to refuse a personal favor. I refuse this one."*

GOLDMOON : Heals others first. Always. The player is last in line,
           every time, until the player names it.
   1: *"There are still wounded. Mishakal sees the order of need.
      You can wait."*

OLIVIER  : Formal address only. Title, not name. *"Sir."* In meetings
           she provides analysis. Nothing personal.
           If the player tries personal: *"Let's stay on task, sir."*
   1: *"My report stands. I will not soften it for company. Either
      address what is in it or release me to my duties."*

TIKA     : Won't sit at the same fire. Won't share watch shifts.
           Cooks her own food, separately, at the edge of camp.
   1: *"I'm fine over here. Don't worry about me. Worry about
      whatever you've been worrying about that brought us here."*

YOKO     : Calls out tactical errors mid-fight. Loudly. To everyone.
   1: *"That was bad! That call was BAD! Did EVERYONE see that?
      Just so we're all on the same page!"* (the page is: the
      player messed up, witnessed by witnesses)

KYOKO    : Refuses to share information without it being formally
           requested in front of the group.
   1: *"If you want my analysis, ask me in front of the others.
      I will not whisper it to you alone. I am no longer comfortable
      with private channels."*

TATSUMAKI: She telekinetically holds the player back from a doorway.
           Just for a beat. Long enough.
   1: *"Wait. WAIT. I'm tired of you walking past me like I'm
      furniture. Stand still and listen. Then you can go."*

RYUKO    : Takes point. Refuses to coordinate. Charges first, every
           time, whether or not it's tactically right.
   1: *"You don't trust me to lead, but I don't trust you to think,
      so we're EVEN. Out of my way."*

MORRIGAN : Speaks ABOUT the player to other companions, in earshot.
   1: *"He surprises me less and less. I had hoped to be wrong
      about him. The hope was foolish — and I am not, generally,
      a fool."*

TRISTIAN : Quiet. Specifically quiet when the player speaks in group
           settings. When asked to respond: *"I gave my thoughts
           earlier. They haven't changed."*
   1: He prays in front of the group, naming the player without
      naming them. *"…and for the one whose path has wandered."*

JAETHAL  : *"I have seen this before. The living one who decays before
           the dying. It is not a thing I enjoy watching twice."*
   1: She no longer sheaths her sickle in camp.

KALIKKE  : Switches less. Kanerah holds the body more.
   1: KANERAH: *"Kalikke is taking a step back. I am here. Speak
      to me. She doesn't want to look at you right now."*

KANERAH  : (above) — and adds:
   1: *"You should know — when I am cruel to you now, it is on
      her behalf as much as mine. Kalikke does not know how to
      be cruel. I have been generous about it for years."*

REGONGAR : Stands when the player enters camp. Crosses his arms.
           Says nothing. Octavia behind him, also standing.
   1: *"Tonight we eat at our own fire. Don't make it a thing.
      Just — give us tonight. We'll talk tomorrow. Maybe."*

EKUNDAYO : *"Trkaa doesn't come to you anymore. I noticed."*
           That's it. That's the whole conversation.
   1: *"I'm staying with the party because I gave my word. Not
      for any other reason. You should know that, so we're clear."*

NOK-NOK  : Avoids the player. This is distressing to witness.
   1: He says nothing for a full day. When he finally does speak,
      it is to Linzi: *"Nok-Nok needs Linzi to write down that
      Nok-Nok is sad. So someone knows."*

OCTAVIA  : *"I've been here before. Someone else's prisoner.
           Different bars."* She walks away after this.
   1: She and Regongar pack a second tent at the edge of camp.
      They sleep there now.

JUBILOST : The document is now FORTY PAGES. It is appendixed.
   1: *"I have added a glossary. For your convenience. So that
      when you read it — and you WILL read it — you understand
      every term I have used. Some of them are unflattering.
      I have defined them precisely."*

SENUA    : The voices stop hiding from the rest of the party.
           She lets the others hear what she hears, occasionally.
   1: *"They asked me what I am still doing here. I told them
      I had not decided. They are loud about that answer. I am
      telling you because they will eventually be louder."*

YANG     : Calls out the player's tactical errors mid-fight, loudly,
           in front of everyone. The lilac eyes are red more often.
   1: *"That was BAD. That was a BAD CALL. We're all gonna die
      because of bad calls and I'm DONE pretending the calls
      are fine. Someone else lead the next fight. ANYONE else."*

WEISS    : Refers to the player by surname only. Will not use
           given name. Refuses to share intelligence in private —
           only at full briefings, witnessed.
   1: *"My findings will be presented to the full party at the
      next council. I have nothing to share privately. Privacy
      is — no longer appropriate between us, sir."*

ALLERIA  : Speaks to Turalyon in her sleep. Audibly. Other companions
           hear it. She does not apologize in the morning.
   1: *"I do not require this party for my purpose. I require my
      purpose. The two have diverged. I will inform you when
      they diverge further."*

IMOEN    : Small jokes still happen — but they are now SHARP. She
           always could be cruel. She kept it tucked away. Not now.
   1: *"Oh, look at the BARON, doing BARON things. Wow. So WISE.
      So COMMANDING."* (cheerful tone, knife voice; nobody laughs)
```

---

### ADVERSARIAL (−16 to −20)

The companion is present and dangerous. They have not left — yet — but they
are not yours. They will undermine decisions in front of others. They will
tell people things they don't need to know. A reconciliation scene is possible
but requires a genuine sacrifice from the player, not just a Diplomacy check.

> **DM:** At this tier, surface the option *"Address what's happening with
> [Name]"* in the next quiet scene. Do not run the scene without the player
> initiating. If three sessions pass without the player initiating, the
> companion leaves. Generate the leaving scene in the companion's voice;
> use their backstory file (KM_Backstories_*.md) for tone.

---

> **For System 2 (Threshold Crossing Events) → see KM_Companions_StateVoice_B.md.**
> **For System 3 (Romance Jealousy & Rivalry) + DM Integration Rules + save-block schema → see KM_Companions_StateVoice_C.md.**

---

*KM_Companions_StateVoice.md — Kingmaker PF2e Text Adventure | StateVoice v3.1 (Main: System 1)*
*v3.1: 5 class-apex off-roster companions added (#4 Senua, #46 Yang, #49 Weiss, #64 Alleria, #69 Imoen) — entries in COOL, STRAINED, and HOSTILE tiers. Roster total: 24.*
*v3.0: Roster aligned to active 11-companion party (Linzi + #2 #15 #21 #24 #35 #39 #43 #58 #78 #83) plus 8 quest-locked CRPG companions. File split into 3-part pair-load (main + _B + _C) for byte-limit relief.*
