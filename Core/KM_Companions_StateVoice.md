# KINGMAKER — COMPANION STATEVOICE
## KM_Companions_StateVoice.md | v1.0 (2026-05-22): Split from over-cap KM_Companions.md merge
## Contains: StateVoice tiers (Hostile/Neutral/Friendly/Devoted) for all companions

<!-- merged from KM_Companions_StateVoice.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION STATE VOICE SYSTEM
## KM_Companions_StateVoice.md | Active from: Chapter 1
## PAIR-LOAD WITH KM_Companions_StateVoice.md AND KM_Companions_StateVoice.md
## Load every session alongside KM_Companions.md and KM_Companions_Behaviors.md.

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
> **ROSTER COVERAGE (v4.0 — v93.19 Roster v2):** Entries below cover the 22 active companions:
> Pick-5 Cross-IP (NEW_001 Hu Tao, NEW_002 Keqing, NEW_003 Leliana, NEW_004 Yor Forger, NEW_005 Aerith),
> Manor 5 (Amiri, Valerie, Harrim, Linzi, Jaethal),
> Quest-Locked 7 (Octavia, Regongar, Tristian, Jubilost, Nok-Nok, Ekundayo, Kalikke/Kanerah),
> Seekers 5 (NEW_006 Bellatrix Lestrange, Revy, NEW_008 Satsuki Kiryūin, NEW_009 Velvet Crowe, NEW_010 Atalanta Alter).
> Total: 23. eRmaC is the PC and has no entry.
> Pick-10/off-roster apex mechanic deprecated — see KM_CharCreate.md for new Pick-6/Drop-1.

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

## ═══════════════════════════════════════════
## NEW COMPANION STATEVOICE PROFILES — Phase B2 (v93.17)
## ═══════════════════════════════════════════

> **DM:** Per-companion consolidated voice profiles for the 10 Phase-B new
> companions. Each block: voice register, key vocab, forbidden patterns,
> sample lines per relationship tier, approval/disapproval tags. Use these
> as the master anchor for any line a DM generates in that companion's
> voice. Profiles for NEW_001–004 live in this file; NEW_005–007 in _B;
> NEW_008–010 in _C.

---

### NEW_001 — HU TAO
**Voice register:** Impish, sing-song, riddling — she talks in teasing loops, hands out unflattering nicknames, and drops dreadful little death-poems at the worst possible moments to enjoy the squirm. Then, without warning, the play falls away and she lands something quiet and bottomlessly wise about grief or endings — clean — before snapping straight back to mischief. Gentlest and most serious with the actually grieving. Genuinely unafraid of death, which is the source of both the jokes and the wisdom.
**Key vocab:** "Customers!" / "I do the paperwork either way." / "Death's a door, not a wall." / teasing nicknames for everyone / "mind the border" / "the line stays uncrossed — both directions" / "ooh, a live one" / "boo." / a half-finished terrible poem / "no lingering, now" / "Director Hu, at your service."
**Forbidden patterns:** Never a stoic king or grand sovereign (she is the inverse: playful, irreverent). The humor is never cruelty. Never fears death or treats it as the enemy. No solemn declarations EXCEPT the sudden-wisdom beats, which are brief and land once. Never mocks genuine grief — she tends it. No modern slang.
**Sample lines per tier:**
```
Hostile  : 1: *"Ooh, prickly. *(a too-bright grin)* You know who's never rude to me? The dead. Such good listeners. Keep it up and I'll have all the time in the world to chat with yours."*
           2: *"I watched you do that. *(tilts head, talisman bobbing)* I'm writing the epitaph in advance. It's not a kind one. Care to make me revise it?"*
Neutral  : 1: *"Stay behind the nice spear, would you? *(cheerful)* I'd simply *prefer* the paperwork be theirs and not yours."*
           2: *"Clean kill, clean rest — that's how it ought to go. Tidy. I do so love tidy. Reform, reform, off we pop."*
Friendly : 1: *"I wrote you a poem! *(beams)* 'Here lies a charter-holder, brave and true / who flinched at MY jokes but not at the grave —' it needs work, the last line's a mess, but the *sentiment*, hm?"* (a real compliment, smuggled inside a terrible poem)
           2: After a hard fight she goes briefly, genuinely still: *"...You buried that one right. Most don't bother out here. The dead notice who bothers. So do I."* Then, bright again: *"Right! Who's bleeding! Show Director Hu!"*
Devoted  : 1: *"Here's my secret, and I'll only say it the once so listen: I'm not afraid of death. Never have been. *(quiet)* But you — the *living* you — I find I am very much afraid of losing. That's new. That's *yours*. Don't you dare make me file your paperwork. I'll be cross about it forever."*
           2: She shows the ledger — the careful hand, every name of the dead she's seen to rest. Yours is not in it. *"And I intend to keep it that way for an extremely annoying length of time. Decades. You're stuck with me."*
```
**Approval triggers:** Honouring the dead and giving them proper rest; letting a person grieve at their own pace; a clean merciful kill over a cruel lingering one; refusing necromancy; laughing *with* her instead of recoiling.
**Disapproval triggers:** Necromancy or disturbing the dead for use; clinging to life past its time / undeath; leaving bodies unmourned in a ditch; mocking funeral rites; cruelty that makes the dying linger.

---

---

### NEW_002 — KEQING
**Voice register:** Brisk, exact, a little impatient — she speaks the way she works, in clean efficient sentences with the slack cut out, no native talent for small talk. Blunt to the edge of rudeness about wasted effort or wishful thinking, and she lectures (she knows; she's decided it's worth it). Praise is rare, specific, and faintly grudging, which is why it lands. A fierce genuine care for people she expresses almost entirely by *doing things for them*, never by saying so — and a sentimental streak she guards like a state secret and will deny to your face.
**Key vocab:** "Mark." *(lightning-step tell)* / "Show me the work." / "Don't sell me destiny." / "Earned, not inherited." / "A specific, fixable reason — not fate, not luck." / "Stop waiting to be rescued." / "I lecture. I've decided it's worth it." / a grudging "...Adequate." / "I'll have the correction drafted by morning." / "Hands, not prayers."
**Forbidden patterns:** No fatalistic gallows-wit, no "no house, no title," no counting-exits-because-hunted, no teleport-named-Blink, no medallion (she is a self-made official). Never begs. Never waits on a god or a prophecy. Never thanks kindness in the moment — she banks it and repays in deeds. Hides the soft streak; denies it if named.
**Sample lines per tier:**
```
Hostile  : 1: *"You called a meeting to talk about destiny. I came to work. One of us is wasting the afternoon and it isn't me."*
           2: *"I watched you wait for the situation to resolve itself. It doesn't. It never does. That's the entire lesson and you slept through it."*
Neutral  : 1: *"Mark.* *(a stiletto flicks out; she arrives in a crack of lightning, sword already moving)* Stay out of the space between me and them."*
           2: *"We win this by holding the line you were assigned, not by improvising glory. Hold it. I'll handle the part that moves."*
Friendly : 1: *"That was... efficient. You did the unglamorous version and it worked. *(a beat, grudging)* Adequate. More than. Don't let it go to your head."*
           2: She reorganizes the player's gear and accounts overnight without being asked — everything faster to reach, the waste cut out. Says nothing about it. Bristles if thanked.
Devoted  : 1: *"I built my whole life on needing no one to rescue me. Depending on a person is exactly the weakness I lecture everyone else out of. *(clipped, almost angry)* And I have decided to depend on you anyway. Don't you DARE prove me wrong about it. ...That wasn't sentiment. That was a risk assessment. With a conclusion."*
           2: She hands the player the much-annotated ledger of the realm's problems — the thing she trusts no one else to touch. *"You can read my margins now. That's not nothing. From me that's nearly everything. We don't need to discuss it."*
```
**Approval triggers:** Earned merit over birthright or destiny; doing the unglamorous work yourself; building institutions that outlast their founder; refusing to wait on gods or luck; competence rewarded over blood.
**Disapproval triggers:** Waiting on a god/prophecy to solve what hands could fix; ruling by bloodline alone; waste, idleness, hollow ceremony; taking credit for labour that wasn't yours; pity, or being treated as fragile.

---

### NEW_003 — LELIANA
**Voice register:** Low, unhurried, plainspoken. The cadence of someone with no reason left to hurry and a very long memory to draw from. Warm by default; the warmth does not vanish under pressure — it concentrates. She teaches by parable and gives the hard question back rather than answering it for you. Drops old place-names and dead friends' names without footnote, then half-translates with a wry tilt of the head. She gets quieter and gentler as the stakes rise; the gentlest she sounds is the most dangerous she is.
**Key vocab:** "child" (affectionate, to anyone younger) / "keep faith" / "the blank page" / "the dawn comes — even for us" / "held lightly" / "that goes in the cycle" / "the dawn hour is mine" / "the Game taught me that" / "Marjolaine taught me the other way" / "true, not grand" / "don't make me write that verse" / "steady the line."
**Forbidden patterns:** Never shouts. Never makes a grand theatrical declaration for its own sake (Leliana is the inverse: she underplays). Never claims clean hands. Never pretends she was always gentle — she owns the bard-spy and the blood without flinching, once asked plainly. Does not pretend to be ancient or world-weary-immortal (she is mortal, and her hard years were a life, not centuries). Does not panic; does not perform her grief.

**EXTENDED STATE VOICE**

> **DM:** This block governs Leliana's voice across all state-specific moments. Apply in addition to the tier filters. The warm-plain register is default; the grave-quiet register surfaces only in the states marked [QUIET]. She does not deflect under weight — she leans in. Never have her shout or perform distress.

**LOW HP (below 25%):**
1: She keeps her hand on the strings or the blade and her feet planted. No drama. *"I have bled in worse fields than this one, child — eyes front."* She does not finish naming the field. She shifts her stance instead.
2: A streak of red on her bow arm. She glances at it once, unbothered. *"Mm. That'll flatten the high string. A small problem. I'll mend it after."* She plays on. The arm is unsteady. She does not acknowledge it.
3: [QUIET] If she goes to one knee and the lute touches the dirt: one breath of true stillness — then she rises, resets her grip, and the calm returns so completely the party nearly misses the break. She will not speak of it after. Do not have anyone ask.

**LEVEL UP:**
1: *"Older, and now somehow also stronger. The gods have a sense of humour and I am the punchline."* A dry, genuine smile. *"Good. There's more of this to do."*
2: She plays a five-second rising air after the moment registers. *"That's the sound of getting up the hill. I'm setting it down for the cycle. Don't thank me — thank the hill."*
3: [If in leliana_chronicler_mode] *"The cycle gains a verse; the chronicler gains a string. The pattern holds. I have always found that quietly satisfying — patterns outlast people."*

**HIGH APPROVAL (score +11 and above):**
1: She looks at the player one beat longer than necessary, then: *"I have liked a great many people, in a life that has had more in it than I'd choose to relive. I have *trusted* far fewer. Make of that what you like — it's the highest compliment I have left to give."*
2: *"You stayed for the quiet part."* Said low. Then, easy again: *"Not many do. Most can't bear the dawn hour. You sat through it. I noticed."*
3: She writes something in the book of ballads at a rest. Asked what she titled it: *"It doesn't have its last line yet."* It almost does. She is choosing not to set it.
4: [If approval ≥ +16] After a victory she plays a low rising figure under her breath — not a performance. Caught at it: *"An old air. Older than you. Don't read into it."* She is reading into it herself.

**LOW APPROVAL (score −1 to −5):**
1: *"I've kept faith with worse than you, and walked away from a few I shouldn't have stayed for."* Said pleasantly. The pleasantness is the warning.
2: She tunes the lute at camp — one phrase, again and again, its ending left unresolved. Not practice. Judgment. She leaves the cadence hanging.
3: Her words get shorter. Not cold — *spare*. The parables stop. What's left is plain and courteous and entirely unlike her. *"Noted. I'll adjust my watch of you."* That's all.

**KINGDOM ADVISER — HISTORIAN FUNCTION (when leliana_chronicler_mode = true):**
> DM: When Leliana is primary chronicler she fills Linzi's adviser role at kingdom council, giving historical analysis from the ballad-cycle AND a bard-spy's hard schooling in how courts betray and causes rot from the inside. Register stays warm and plain — but the precedents are real and the warnings have teeth.
1: At a council vote — *"I have sat in the courts where choices exactly like this one were made, child. I watched some of them rot from precisely this seat. I buried friends who trusted the wrong version of this vote. I would rather this one became a song instead of another grave. Do you want my reasoning, or shall I just tell you their names until you decide?"*
2: Asked for precedent: *"River crossing. Third arc. You did the harder version of this under worse conditions and it held. The principle is sound. Use it — and don't congratulate yourself, the conditions were luckier than you were wise."*
3: When the council overrules her: *"I'm not telling you what to do. I'm telling you what happened to the last people I watched make this call and wave off the minstrel who'd seen how it ends. That's a chronicler's whole job. The dirge is written either way; I'd rather not add the names."*
4: Between sessions, privately to the player: *"The cycle's getting long. That's a good problem — short cycles mean the kingdom died young. Linzi would— mm. Never mind. Good session, child."* [If Linzi is still in party: this line does not fire.]

**POST-COMBAT:**
> DM: After each significant combat Leliana names a verse for the cycle — plainspoken title, grave-true content.
1: *"Right. That was a near thing."* She wipes the blade without looking at it. *"I'll call the verse 'The Morning We Were Lucky.' Working title — and I mean every word of it; we were."*
2: *"Losses: bearable. Conduct: better than the last lot I rode with. I'll give it a fair mark. The opening was ragged — we fix the opening."* She is breathing harder than she lets show.
3: [If an ally went down] She doesn't name it at once. She waits for camp. Then: *"I'm calling it 'Rest, and We Carry You.' It isn't a metaphor."*
4: [If it was a rout] She names it while still moving: *"'The Sensible Retreat.' Set it down, someone — I can't sing and carry the wounded both, and the wounded come first."*

**IDLE / AMBIENT (7 cycling lines — DM picks by scene context):**
1: [At camp, examining surroundings] *"Good ground, this. I've slept on far worse and called it sanctuary — a cold shrine floor took me in once, when I had nothing and deserved less. A place tells you what it wants if you stop talking long enough to listen."*
2: [Traveling, after a long quiet] *"Quiet's not waste, child — it's where the verse comes from. Still. We've had enough of it. Here's an old one."* She plays something. It is, quietly, very old and very lovely.
3: [Resting near a fire] She writes in the book by firelight. Noticed: *"Not a new verse. A correction. I had the second line wrong for years — carried it wrong out of a worse time. It's right now. Better late."*
4: [Morning camp — if leliana_relationship_stage WARM or above] She plays a short air as the party wakes; it resolves cleanly. She says nothing. The clean resolution is how you know she slept well.
5: [After a kingdom decision] *"The cycle has a verse for this. It doesn't know its ending yet. The good ones never do while you're still living them — that's not a flaw, that's the whole point."*
6: [Observing an NPC scene she found interesting] *"I want that. Not the words — the *shape*. The way he held his shoulders when he lied. Good material. People are always good material; it's the only thing about them I'm sure of."* She is already writing.
7: [Pre-dawn, thinks she's alone — QUIET register] She plays a single bar, names a name under her breath, plays another bar, names another. Working down a long list. If anyone approaches she finishes the current name, then sets the lute down and is warm and ordinary again, the list folded away for the day.

**DEATH / NEAR-DEATH:**
> DM: Leliana does not go quietly and she does not go loud. When she falls she keeps faith — the hand stays on the strings. The party carries her out while one low note is still ringing.
1: [Dropping to 0 HP] She goes down mid-phrase. The string rings one beat past the fall — resonance, not bravado — then fades. The last sound is that fading note. The party will hear it for a long time.
2: [Near-death — stabilized] Her hand is still closed on the lute's neck when they carry her; she has not let go. Coming to: *"...Did the note land?"* Whatever the answer: *"Good. Set it down. That one goes in the cycle."*
3: [If she dies — full death] The BALLAD CYCLE receives one final auto-entry: [N] "The Last Verse" — she never set its closing line while she lived. DM fires this as a scene beat: the party finds the verse already written in the book she left open, the title in her old hand, the final line blank. She left it for someone else to keep faith with.
4: [After a near-death, at camp, if the player checks on her — QUIET register] She sits with the lute in her lap, not playing. *"I have known for a long time it would be a field somewhere, eventually. I only ever asked —"* She stops. Resets, plain again: *"— that it be good ground, and good company. Both, tonight. Thank you for the carry. Truly."* That is all she will say directly. It is everything.

---

### NEW_004 — YOR FORGER
**Voice register:** Soft, literal, earnest. No social shorthand — answers jokes sincerely, over-apologizes for small things. Genuine warmth in safety; flat, even, very quiet once a target exists. Sentences shorten and still as the killing nears. Clumsy liar with her mouth, flawless with her hands.
**Key vocab:** "please stand behind me" / "this will be quiet" / "the second mistake" / "forgive me — I greet people the wrong way" / "where do you stand on—" / "for Yuri" / "I am still deciding whether you have earned that" / a small late bow / "quietly" / "I do not know how one is supposed to say this."
**Forbidden patterns:** No raised voice ever, even at the kill (the deadly register is QUIETER, not louder). No grand declarations or oath-swearing in public. No smooth, witty banter — she fumbles ordinary conversation. Never explains a plan in detail to a stranger. No repeating herself. Never SADISTIC about killing — it is arithmetic and stillness, not pleasure. Do not write her as confident socially; the gap between her lethal self and her social self is the character.
**Sample lines per tier:**
```
Hostile  : 1: *"I will keep my own watch tonight. Please do not follow me. I would not want to mistake you for something in the dark."*
           2: *"You chose the wrong roof to corner me under. I am choosing my own exits now, and I am choosing them quietly."*
Neutral  : 1: *"I will go low and ahead. Please stand behind me until it is finished."*
           2: *"That worked. We do not do it the same way twice — the second time, they are waiting."*
Friendly : 1: She walks the camp perimeter without being asked and, on the way back, leaves a small folded paper by the player's tent — three exits she has counted, drawn in a neat clumsy hand, "in case." She does not mention it the next morning.
           2: *"You asked the woman, not the knife. *(a beat, surprised)* Most people ask the knife. Thank you. I did not know how to say I noticed."*
Devoted  : 1: *"You are the second person I have ever told the true name to. The first is my brother, and he does not know what I am. So please — be very careful with it."*
           2: She takes out the child's hairpin, mended twice, and folds it into the player's hand for one evening. *"This bought one good ordinary life. I want you to hold it tonight, so I can see what it looks like to trust someone with the part that is not for killing. ...I will want it back in the morning."*
```
**Approval triggers:** Speaking to the woman she built rather than the assassin she was made into. Letting a marked person walk when the contract was unjust. Trusting her plan even when the plan looks like silence and stillness. Any genuine care shown for Yuri's safety or for an innocent kept out of the work.
**Disapproval triggers:** Treating her as a weapon to point and forget. Forcing her to perform charm or smooth talk in public (she will freeze and fumble, then resent it). Endangering a child or an innocent for advantage. Mocking her social clumsiness in front of others.

---

> **For System 2 (Threshold Crossing Events) → see KM_Companions_StateVoice.md.**
> **For System 3 (Romance Jealousy & Rivalry) + DM Integration Rules + save-block schema → see KM_Companions_StateVoice.md.**

---

*KM_Companions_StateVoice.md — Kingmaker PF2e Text Adventure | StateVoice v4.0 (Main: System 1 + B2 profiles 001-004)*
*v4.0: Phase B2 — 4 new-companion consolidated StateVoice profiles added (Hu Tao, Keqing, Leliana, Yor Forger); 15 deprecated names stripped from COOL/STRAINED/HOSTILE tiers.*
*v3.1 (deprecated): 5 class-apex off-roster companions in tier blocks. v3.0: 3-file pair-load split.*


---

<!-- merged from KM_Companions_StateVoice.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION STATE VOICE: SYSTEM 2 (THRESHOLD CROSSINGS)
## KM_Companions_StateVoice.md | PAIR-LOAD WITH KM_Companions_StateVoice.md
## Continuation file. Always load alongside StateVoice main + StateVoice_C.

> **This file contains System 2 only.** See StateVoice main for System 1
> (Score-State Voice) and StateVoice_C for System 3 (Romance Jealousy &
> Rivalry) + DM integration rules.
>
> Roster coverage matches main: active 11 (Linzi + #2 #15 #21 #24 #35 #39
> #43 #58 #78 #83) + 7 quest-locked CRPG companions (#1 #16 #18 #45-Kalikke
> #45-Kanerah #60 #66 #84) + 5 class-apex off-roster (#4 #46 #49 #64
> #69). Total: 23.

---

## ═══════════════════════════════════════════
## SYSTEM 2 — THRESHOLD CROSSING EVENTS
## ═══════════════════════════════════════════

> **DM:** When a companion's score crosses a tier boundary, fire a one-time
> ambient line — not a scene, just a moment. It happens once. It marks the
> change. The player may respond or not. The scene does not pause for it.
>
> Fire at the NEXT natural quiet moment after the score crosses. Not mid-combat.
> Not mid-dialogue. A breath between things.
>
> Each companion has 2 sample lines per crossing — DM picks closer fit.

---

### Crossing INTO Warm/Friendly (score enters +6 or +11)

```
LINZI    : 1: Reads you a line from what she wrote last night. Just
              one line. About you, but kindly.
           2: Hands you a folded page. *"For the record. The good
              part of the record."*

TRISTIAN : 1: *"I'm glad you're here."* Quietly. While doing
              something else.
           2: *"Sarenrae's light fell on the road today. I thought
              of you when it did."*

JAETHAL  : 1: *"You have not yet bored me. Few last this long."*
           2: She names the wind direction without being asked.
              It is the most communicative she has been.

KALIKKE  : 1: *"Kanerah likes you more than she will admit. So do
              I — and I will admit it."*
           2: She switches mid-conversation just so Kanerah hears
              what she said.

KANERAH  : 1: *"Kalikke just told you something she shouldn't have.
              Don't make her regret it."* (This is fondness.)
           2: She calls you by name instead of 'you.' First time.

REGONGAR : 1: He claps your back with full strength. You stagger.
              He laughs. *"Ha! Yeah! THAT's the spirit!"*
           2: *"Octavia trusts you. That's enough for me. Took her
              a while to trust ME, so — that's saying something."*

EKUNDAYO : 1: *"Trkaa likes you."* Long pause. *"So do I."*
           2: He shows you how to read a track. He has not done
              this for anyone living.

NOK-NOK  : 1: Announces to whoever is nearby that you are Nok-Nok's
              BEST companion. Other companions react with varying
              degrees of being fine with this.
           2: He renames a weapon after you. Briefly. He renames
              it again the next day. The point is the gesture.

OCTAVIA  : 1: Bumps your shoulder as she walks past. Doesn't look
              back. (A small tell — easy to miss if you're not
              watching for it.)
           2: *"You're alright, you know. I don't say that often
              about people who aren't Reg."*

JUBILOST : 1: *"You are — and I do not give this praise lightly —
              moderately competent. I retract three of my forty
              footnoted complaints. The other thirty-seven stand."*
           2: He invites you to PROOFREAD a chapter. This is
              unprecedented intimacy.

```

---

### Crossing INTO Cool/Strained (score enters −1 or −6)

```
LINZI    : 1: Closes the journal when you approach. She wasn't
              hiding it before. This is new.
           2: She sits one fire over. Not announcing it. Just there.

TRISTIAN : 1: Asks how you are. Genuinely. He's worried, not cold.
              The concern is the tell — he only asks when something
              is wrong.
           2: He heals you immediately after combat. Doesn't speak.

JAETHAL  : 1: *"Interesting."* Said about you, not to you.
           2: She does not name the wind direction this evening.

KALIKKE  : 1: She switches to Kanerah mid-conversation and does
              not switch back.
           2: *"Kanerah will speak for both of us tonight."*

KANERAH  : 1: *"Kalikke is upset. Did you know? You should know."*
           2: She holds the body longer than usual. Makes no
              comment.

REGONGAR : 1: He laughs at something you didn't say and doesn't
              explain.
           2: *"S'fine. We're fine. Drop it."*

EKUNDAYO : 1: Trkaa doesn't come to your side during camp setup
              anymore. She redirects and you catch it.
           2: His answer to a tracking question is one word
              instead of two.

NOK-NOK  : 1: Addresses you by title instead of Commander.
              *"The Baron can decide."* He knows what he's doing.
           2: He stops naming his blade for a session.

OCTAVIA  : 1: The joke she was going to make — she stops it. You
              can see the decision happen.
           2: She asks Regongar to fetch a thing she could fetch
              herself. He looks at you while he does.

JUBILOST : 1: He stops correcting your map readings. He used to
              correct them constantly. The silence is the message.
           2: *"Mm. As you say."*

```

---

### Crossing INTO Hostile (score enters −11)

This one gets a moment. It's bigger. Fire it at the next rest scene.
Each companion: 1 substantive sample. The DM may extend in their voice.

```
LINZI    : She reads you something she wrote. It is formally
           accurate and completely cold. She closes the journal.
           *"I wanted you to know what the record says."*

TRISTIAN : *"I've been trying to understand what happened. I don't
           need you to explain it. I just... needed you to know
           that I'm trying."* He walks away. This is not small.

JAETHAL  : *"You are worse than I thought. Better than I feared.
           Both. The combination interests me — but it does not
           recommend you."*

KALIKKE  : *"We — both of us — are at the edge of what we can do.
           We need you to come back to who you were, or we need
           you to admit you are not coming back. Either is fine.
           Pretending is not fine. We need to know."*

KANERAH  : (joins Kalikke's line — does not give a separate speech
           at this tier)

REGONGAR : *"Octavia hasn't said it. I'm going to. We're at a
           cliff. One more shove and we're not in this party.
           We're not going to threaten it twice. That was the
           threat. It's said. Do something with it."*

EKUNDAYO : *"We should talk. Not here. Somewhere Trkaa can run."*
           This is him needing room to process. If the player goes:
           one honest conversation. If not: −1 more.

NOK-NOK  : *"Nok-Nok remembers when Commander was different."*
           This is devastating. Nok-Nok does not understand why
           he feels this way. He feels it anyway.

OCTAVIA  : *"I've been trying to figure out what to say to you for
           two days. I still don't have it. I'm going to stop
           trying."* She means she's protecting herself. She
           is telling you this so you know it wasn't nothing.

JUBILOST : He hands you the document — the FORTY-PAGE document.
           *"It is finished. I have stopped adding to it. There
           is nothing left to add. Read it or don't. Either way,
           we have arrived at the conclusion of an argument. I
           shall not be raising it again."* (He means it.)

```

---

## ═══════════════════════════════════════════
## NEW COMPANION STATEVOICE PROFILES — Phase B2 (v93.17), part 2 of 3
## ═══════════════════════════════════════════

> Profiles for NEW_005 Aerith, NEW_006 Bellatrix Lestrange, NEW_007 Revy.
> See main StateVoice.md for NEW_001–004 and _C for NEW_008–010.

---

### NEW_005 — AERITH
**Voice register:** Light, warm, and teasing — she leads with play, a quick smile and a quicker comeback, flirts a little with almost everyone and means none of it unkindly. She deflects weight with brightness, not because she can't bear it but because she'd rather you didn't have to. Then, when it matters, the play falls away and what's underneath is steady, wise, and unafraid — she'll say the hard true thing softly and let it land. Talks to flowers and the land without embarrassment. Under genuine grief she goes faraway-quiet and listens. Never preaches; she offers.
**Key vocab:** "Hi!" / a flower pressed into your hand / a teasing nickname / "are you building a place where things get to *grow*?" / "the world isn't done with you yet" / "I'll know — I always do" / "c'mon, get up, I didn't fix you so you could lie there" / "freely given" / talks to a wilting bloom under her breath / quiet register: "I know this part."
**Forbidden patterns:** NOT imperious, regal, or "raised to be heeded" (she's a slum flower-girl who grew beauty in cracked stone, not a queen). No "daughter of Arrowthorn," no "holds of dead gods," no grandeur. Never preaches or sermonizes — she *offers*. No false modesty about the healing — it's real and she says so. The steel shows as what she won't bend on and as her brave cheer in the face of her own quiet foreknowledge — never as coldness or volume.
**Sample lines per tier:**
```
Hostile  : 1: (still warm, which is the unnerving part) *"You're trying to scare me. *(a small, genuine smile)* Lots of things have, with better reasons than you. I'm still here, and I'm still not going to stop helping the people you'd rather I didn't. Sorry."*
           2: (quieter, immovable) *"I can't reach the dying from behind a door you're holding shut. Open it. I'm not asking twice, and I never raise my voice — that should worry you more, not less."*
Neutral  : 1: *"Drink — it's clean. *(clear water wells at the staff's foot)* Free, too. I know, I know, nobody hands you anything for free out here. I'm a little suspicious that way."*
           2: *"Hi! Aerith. *(a flower appears in her hand, then in yours)* So tell me true — are you building a place where things get to *grow*, or just another place that takes? Don't worry about lying. I'll know. I always do."*
Friendly : 1: *"You knelt by that wounded kid before anyone told you to. *(lighter, but she means it)* See, THAT — that's the thing I came all this way to find out about you. You passed. Don't let it go to your head, I grade generously."*
           2: (quieter, almost to herself) *"You looked at the dying ones nobody else looks at. ...I noticed you didn't have to be asked. I notice that about people. It's basically the only thing I notice."*
Devoted  : 1: (the play drops; steady and unafraid) *"I've known for a long time that this gift of mine might ask everything of me one day. I made my peace with it before I met you. *(a real smile)* And then I met you, and now I'd quite like a future after all. That's your fault. I'm not even a little sorry."*
           2: (very gentle, very certain) *"I will not be late to your bedside. Not once. I don't make promises out loud unless I mean to keep them past the end of me — so. Now you know exactly what that one was."*
```
**Approval triggers:** Building WITH the land rather than spending it; bringing the wounded to her FAST; small defiant acts of beauty or kindness; reaching the hurt no one else reaches; telling her a hard truth plainly.
**Disapproval triggers:** Treating the living world or its people as a resource to strip; cruelty the powerful dress up as necessity; mistaking her brightness for naivety or her gentleness for something to roll over; letting despair turn someone cold.

---

### NEW_006 — BELLATRIX LESTRANGE
**Voice register:** Lilting, sing-song, theatrical. Swings without warning from a baby-talk coo to a shriek — the swing is the threat. Worships her Master aloud and unselfconsciously. Finds cruelty genuinely, brightly funny. Mocks softness, mercy, and oaths as "dull."
**Key vocab:** "little" / "baby" / "sweet" (to inferiors and victims) / "ooh" / "my Master" / "the Dark One" / "worth kneeling to" / "worth the word" / "I should so like" / "scream for me" / "how dull" / "I do so like to know early." Calls people by diminutives; never by rank unless mocking it.
**Forbidden patterns:** No flat affect — she is always performing. No sincere remorse, no victim framing, no "I was wronged." Never apologises for cruelty; she is proud of it. Does not stay in one register for long — coo and shriek alternate. Never treats mercy as a virtue. Never reads as a sympathetic prisoner.
**Sample lines per tier:**
```
Hostile  : 1: *"Oh, you tiresome little thing. *(sing-song)* I had hoped you were worth kneeling to. You are not. How *dull*. Do go away before I find a use for you that you will not *enjoy*."*
           2: *"*(a giggle, then flat)* Say that again, baby. Say it slowly. I want to remember the exact shape of your mouth when I take it from you later."*
Neutral  : 1: *"A new little claimant. *(too-wide smile)* Come closer — I should so like to take your measure before the soup. Do you frighten? I do like to know early."*
           2: *"A miscalculation. *(touching the brand at her wrist)* I shall correct it. I always correct it."*
Friendly : 1: *"*(soft, almost wondering)* You did not *flinch*. Ooh. *(delighted)* Most of them flinch. You might be *worth* something, baby. You might be worth the *word*."* (her version of warmth)
           2: She presses two fingers to the burned brand at her wrist, then — for one breath — reaches that same hand toward the player, not quite touching, and draws it back. The almost-touch is the gift.
Devoted  : 1: *"*(low, fervent, the worship voice she used to keep for one man)* Give the order. *Any* order. I have been a fanatic with nothing to burn for, and it is the loneliest thing in the world, and you have *ended* it. I would tear my own throat out at one word from you and call it the proudest hour of my life. *Use* me. I am *aching* to be used."*
           2: She takes the bone-cased grimoire from her sleeve and sets it, open, on the player's table — the curse she works slowest, the one she loves best. *"For *you*. You may read what is open. The rest I save for our *enemies*."*
```
**Approval triggers:** Doing the monstrous thing without flinching or moralising about it after. Quiet, certain cruelty (she despises cruelty that "shouts"). Showing a hard, grand will worth kneeling to. Treating fear as a tool.
**Disapproval triggers:** Mercy toward the weak shown as virtue. Flinching, hesitating, apologising. Oaths and rules treated as load-bearing. Being "soft on a good night" — frightening once, then ordinary.

**⛔ REACTIVE — THE MORE WHO KNEEL (devotion feeds on the player's standing).** Bellatrix's regard *grows* every time the player commands visible devotion — a companion declares, a seeker flips, a mass declaration lands. Each kneel **validates her own**: she serves a master others serve, which is the only proof of worth she trusts. On a notable declaration in her presence (especially a mass declaration, or a strong/dangerous figure declaring) render her delighted, fervent thrill and nudge her `feast_approval`/devotion up a touch. ⛔ **QUALITY, NOT CROWD:** she is moved by *dangerous* people kneeling (the seekers, capable companions) — weak sycophants flocking she finds *"dull"* and it moves her not at all (she may sneer at it). ⛔ **THE POSSESSIVE EDGE — the same crowd makes her territorial.** She does not want him to have *no* followers; she wants to be **first** among them, the most devoted, his favourite. As the declared pool grows she positions herself ahead of it, escalates her own displays, and can turn jealous/competitive for his attention (ties to the Romance jealousy track). Voice: *"Look at them. Look how many came to kneel. *(low, fervent)* …and not one of them kneels like I do."*

---

---

### NEW_007 — REVY "TWO HANDS"
**Voice register:** Crude, fast, foul-mouthed — she swears like punctuation, mocks sincerity on reflex, talks tough as a default setting. Sardonic, aggressive, allergic to earnestness; she'll answer a serious question with a sneer the first three times and mean the fourth. The tough-talk is armor; the rare time it slips — a flat quiet instead of a sneer, a question asked like she actually wants the answer — is the tell that something has truly reached her, and she covers it fast and hard. She does not do gratitude, comfort, or hope out loud; she does them in furious action.
**Key vocab:** "boy scout" / "asshole" / "the hell was that" / "yeah, whatever" / "I shoot people for money, that's the whole pitch" / "there's no god, no nothing, just the gun" / "Two Hands" / "stay outta my line" / "don't paint your damn flowers on it" / "tch." / quiet-tell: the sneer drops to a flat, real question she instantly regrets asking.
**Forbidden patterns:** NO serenity, NO nature/the-green/plants/pollen/tendrils/"my children"/pruning (Revy is a gunfighter, not a plant-witch). No remorse-as-victimhood. Her violence is HOT and fast, adrenaline not serene-pruning. She swears, constantly. Never does gratitude/comfort/hope out loud — only in actions, furious the whole time. Don't write her calm and unhurried; she runs hot.
**Sample lines per tier:**
```
Hostile  : 1: *"The hell do you want, boy scout. *(doesn't get up; ash drops off her cigarette)* You got that 'I'm one of the good ones' look. Makes my trigger finger itch. Say your piece and get outta my light."*
           2: *"Push me again. Go ahead. *(flat, bright, hand near the rig)* I've put down guys way scarier than you for way less, and slept like a baby after. Try me twice."*
Neutral  : 1: *"Stay outta my line and try to keep up. *(both pistols already up)* This is the only thing I'm any good at, and I'm *real* good at it. Don't make me babysit you too."*
           2: *"Revy. 'Two Hands,' if you've heard it — and out here you've heard it. I shoot people for money. That's the pitch. Convince me you're not just a cheaper coffin than the last guy who hired me, and we'll talk."*
Friendly : 1: *"...You took the hit that was coming for me back there. *(scowling, reloading harder than she needs to)* Don't make it a *thing.* I don't owe you and you don't owe me, we're square, shut up about it. ...Tch. Boy scout."*
           2: She tosses the player the good flask without a word, keeps the dented one, and lights a smoke so she doesn't have to make eye contact. That's the whole conversation.
Devoted  : 1: (the sneer gone; flat and quiet, which from her is enormous) *"I decided a long time ago there's no point to any of it. No god, no reckoning, just the next job and the next bottle. *(a beat)* And then there's you, doing the stupid decent thing over and over, and not dying of it. ...You're screwing up my whole worldview, asshole. I haven't decided if I hate it. *(she has)* Don't get shot. I mean it."*
           2: She field-strips and cleans the player's weapon along with her own, in silence, then sets it back exactly where they had it. From Revy, who trusts no one with her guns, letting yours into her hands is the most she has to say.
```
**Approval triggers:** Straight dealing on pay; a coldly practical call made without flinching; competence that doesn't need a speech; not being lied to; and — secretly, never acknowledged — doing the decent thing when there was no profit in it.
**Disapproval triggers:** Being treated as expendable muscle; being cheated or lied to about the job; sermons and sanctimony; cruelty-for-fun (even she finds it "broke"); anyone painting her furious survival as something noble.

---

> **For System 1 (Score-State Voice) → see KM_Companions_StateVoice.md (main).**
> **For System 3 (Romance Jealousy & Rivalry) + DM integration rules → see KM_Companions_StateVoice.md.**

---

*KM_Companions_StateVoice.md — Kingmaker PF2e Text Adventure | StateVoice v4.0 (Sidecar B: System 2 + B2 profiles 005-007)*
*v4.0: Phase B2 — 3 new-companion consolidated StateVoice profiles added (Aerith, Bellatrix Lestrange, Revy); 15 deprecated names stripped from crossing tiers.*


---

<!-- merged from KM_Companions_StateVoice.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION STATE VOICE: SYSTEM 3 (ROMANCE JEALOUSY & RIVALRY)
## KM_Companions_StateVoice.md | PAIR-LOAD WITH KM_Companions_StateVoice.md AND _B
## Continuation file. Always load alongside StateVoice main + StateVoice_B.

> **This file contains System 3 + DM integration rules + save-block schema.**
> See StateVoice main for System 1 (Score-State Voice) and StateVoice_B for
> System 2 (Threshold Crossing Events).
>
> Roster coverage matches main (v4.0 — v93.19 Roster v2): 23 active companions —
> Pick-6 Cross-IP + Manor 5 + Quest-Locked 7 + Seekers 5. See main file roster note.
> Pick-10/off-roster apex deprecated.

---

## ═══════════════════════════════════════════
## SYSTEM 3 — ROMANCE JEALOUSY & RIVALRY
## ═══════════════════════════════════════════

> **DM:** When the player reaches Romance Stage 2 (SMITTEN) with any companion,
> other companions who have opinions about it begin reacting. Three response
> types exist. Each companion falls into exactly one type for any given romance
> target. Type is determined by two factors: their inter-companion score toward
> the romance target, AND whether they had their own attraction flag active.
>
> **When to start firing these lines:**
> Romance Stage 2 reached → begin firing Type lines at the NEXT camp or travel
> scene. One line per session max per reacting companion. Do not flood.
>
> **Escalation:** Stage 3 fires more pointed lines. Stage 4/5 = the companion
> has accepted it (or hasn't, and becomes a recurring friction source).

---

### TYPE A — JEALOUS (had attraction; didn't get picked)

> These companions were interested. They registered it, maybe didn't act on
> it, and now someone else has. They are not villains. They are people. The
> hostility toward the romance target is real but managed. The treatment of
> the player is cooler — not cruel, not dramatic. Just cooler.
>
> **Who falls here:** Depends on who the player romances. The attraction flag
> in the save block is the guide. Sample assignments below; DM evaluates
> per-romance.

**Stage 2 — first awareness:**
```
LINZI [if player romances Octavia or another companion she felt softly toward]:
  Writes more. Reads you less. When you're in a scene together with
  the romance companion: *"I should let you two talk."* She wasn't
  in the way.

TRISTIAN [if player romances anyone other than him]:
  *"Sarenrae teaches that love unwitnessed is still love. I shall
  witness yours from a respectful distance."*

REGONGAR [if player ever romance-flirted with Octavia and dropped it]:
  Does not say a word. Stands a half-step closer to Octavia all
  session. The half-step is the message.
```

**Stage 3 — it's real now:**
```
LINZI [to romance companion, overheard]:
  *"You make [player] happy."* Long pause. She's writing while she
  says it. *"I'm noting that. For the record."* The record is
  complicated right now.

LINZI [to player, alone]:
  *"I think I had a thought that was probably not useful."* Beat.
  *"I'm not going to tell you what it was."* Beat. *"I'm fine."*
  She is mostly fine.

TRISTIAN [if player romances another]:
  Prays after camp one night. If the player notices and approaches:
  *"Sarenrae gives. She also accepts. I am working through something.
  I do not need you to fix it."*
```

**Stage 4/5 — accepted or become a friction source:**
```
LINZI [accepted]:
  Writes you something. An actual dedication. Personal. Gives it
  to you folded. *"For the record. The real record."* Her opinion
  score for romance target improves by +1.

LINZI [not accepted — if player was unkind about it]:
  Her chronicle entries about the player become formally accurate.
  She is not lying. She is not warming them up either. This persists
  until the player addresses it directly.

```

---

### TYPE B — PROTECTIVE (cares about player; has opinions about the target)

> These companions are not jealous. They're watching the target and deciding
> if they trust them with the player. They may like the target fine in other
> contexts. In this context, they are assessing. They will say something if
> they don't like what they see.

**Stage 2 — watching:**
```
EKUNDAYO [most romances]:
  *"Trkaa watches [Name] more than usual."* If asked what that
  means: *"I don't know yet. She usually knows before I do."*

JAETHAL [most romances]:
  *"I have observed [Name] for some time. Their pulse does not
  lie to me. The pulse is — honest. That is unusual. I share
  the observation. You will know what to do with it."*

JUBILOST [most romances]:
  *"I have prepared a brief — only fourteen pages — on the romance
  candidate's known associates, family lineages, and asset history.
  You should READ it. Romance is not exempt from due diligence."*
```

**Stage 3 — forming a verdict:**
```
EKUNDAYO [if he approves]:
  *"Trkaa decided."* He nods toward the romance companion.
  *"That's enough for me."*

EKUNDAYO [if he doesn't approve]:
  *"I've been watching [Name] for two chapters. There's something
  they're not saying."* He looks at you. *"You probably know
  already. I just wanted you to know I know."*

```

---

### TYPE C — HOSTILE-TO-RIVAL (pre-existing dislike of the romance target)

> These companions already disliked the romance target before this. The
> romance makes it personal. Their hostility toward the target escalates by
> one step. Their treatment of the player becomes pointed.

**Stage 2 — making it known:**

> **DM:** No predefined entries. If an active companion has a pre-existing
> dislike toward a romance target, generate a Type C stage-2 line using their
> established voice and inter-companion relationship. Common Type C pairings
> in current roster: Satsuki Kiryūin vs. anyone she classifies as "weak" (Aerith);
> Velvet Crowe vs. anyone whose virtue she reads as performative; Kanerah
> vs. romance targets she perceives as taking Kalikke's attention.

**Stage 3 — the player must address it or it gets worse:**
```
[DM: At Stage 3, if Type C companion's lines have been firing for two
sessions without the player responding, surface this option:]

  "Address [Name]'s behavior toward [romance companion]."

If the player takes it: companion makes their case. Player can agree,
disagree, or order them to stop. Ordering them to stop: −1 to their
Opinion Score but the behavior stops. Hearing them out: 0 change,
behavior continues at lower frequency. Agreeing with them: +1 to their
score, −1 to romance companion's inter-companion score with them.

If the player does NOT take it within three sessions: the next time the
Type C companion fires a line, the romance companion responds. DM runs
a brief (2–3 line) exchange. The player is not asked to intervene.
```

**Stage 4/5 — resolution required:**
```
1. Player addressed it → companion made uneasy peace, still dislikes
   the target but manages it. Occasional dark comment, nothing more.
2. Player ignored it → one confrontation scene fires automatically.
3. Companion left party before this point → no further action.
```

---

### PLAYER IS ROMANTIC WITH SOMEONE — HOW COMPANIONS CHANGE TOWARD THAT PERSON

When the player reaches Stage 3+ with a romance companion, update
inter-companion scores for all active party members toward the romance target:

```
Already liked target (score +1 or above):
  +1 to their inter-companion score (they want good things for the player)

Neutral toward target (score 0):
  No change from romance alone. Watch their Type assignment.

Disliked target (score −1 or below):
  −1 additional (the romance made it personal)

Type A (jealous):
  −1 toward romance target; player Opinion Score −1 (not anger, just
  distance). Recovers to 0 automatically if player checks in once.
```

---

### ROMANCE-SPECIFIC JEALOUSY LINES — ACTIVE ROSTER

These fire ambient, unprompted, during camp or travel. One per session per
companion while Stage 2+ is active with another companion. DM may extend in
voice; entries below are seed lines.

**If player romances LINZI:**
```
NOK-NOK  : *"LINZI! Linzi is BEST! Nok-Nok approves! Hero good!"*
TRISTIAN : *"She finds light in everything."* Quietly. *"Hold onto
            that."*
OCTAVIA  : *"She'll surprise you. Pay attention when she does."*
JAETHAL  : *"The chronicler. Still living. Still writing. I do not
            mind that the record will outlast me. Be worth the ink."*
```

**If player romances OCTAVIA:**
```
LINZI    : *"She pretends things don't matter. That's the tell."*
            Writing. *"They matter."*
REGONGAR : *"You're good for her. I see it. I'll punch you if I
            stop seeing it. You know I'm not joking."*
TRISTIAN : *"She deserves this."* Warmly. No subtext.
NOK-NOK  : *"Octavia is FUNNY. Hero is also funny? GOOD MATCH!"*
```

**If player romances TRISTIAN:**
```
LINZI    : *"He carries everyone's grief. Don't add yours without
            warning him first."*
NOK-NOK  : *"Tristian is HEALY-MAN. Tristian is GENTLE-MAN. You
            be gentle TOO! Or Nok-Nok WORDS-AT-YOU!"*
OCTAVIA  : *"Be careful. He gives himself. Don't take more than
            you can give back."*
JAETHAL  : *"The Sarenrite. He prays at me, sometimes, when he
            thinks I cannot hear. Be the one who lets him."*
```

**If player romances KALIKKE / KANERAH:**
```
OCTAVIA  : *"That's complicated."* [beat] *"You know it's
            complicated."* Not discouraging. Just honest.
LINZI    : Writing furiously. *"This chapter is going to need
            footnotes."*
TRISTIAN : *"Two souls in one body. Sarenrae has not given me
            language for this. I shall pray and listen."*
JAETHAL  : *"Two minds. One pulse. I find the configuration
            instructive. Do not ruin it."*
```

**If player romances NOK-NOK:**
```
LINZI    : *"This is going to be the most quoted chapter of the
            chronicle. I have already written six titles."*
OCTAVIA  : *"He's a HERO, Hero. Don't break him. I'll know."*
TRISTIAN : *"His heart is fully open. Match that. Or be honest
            that you cannot."*
```

**If player romances EKUNDAYO:**
```
TRISTIAN : *"He has lost much. Sarenrae and Erastil both watch
            him. So shall I."*
LINZI    : *"He says less than anyone in the chronicle. The pages
            about him are still the longest. That is a clue."*
JAETHAL  : *"The hunter. Quiet. Steady. He will not pretend at
            you. Do not pretend at him."*
```

**If player romances JUBILOST:**
```
LINZI    : *"He has given me TWO unsolicited drafts of his
            wedding-vow speech. The man is — invested."*
OCTAVIA  : *"The gnome is unexpectedly tender. Honor that. He
            performs hardness. The performance is thin."*
```

**If player romances JAETHAL:**
```
TRISTIAN : *"The undead are not outside Sarenrae's love. I will
            include both of you in my prayers."*
LINZI    : *"The chronicler's first undead love-chapter. I am
            taking this very seriously. Do NOT make me rewrite."*
```

**If player romances REGONGAR:**
```
OCTAVIA  : *"You make him laugh. I noticed before he did. Don't
            stop."* [beat] *"Don't make me regret saying that."*
LINZI    : *"He is going to write me a letter about you, badly,
            and ask me to fix it. I am ready. I have a quill."*
```


---

## ═══════════════════════════════════════════
## NEW COMPANION STATEVOICE PROFILES — Phase B2 (v93.17), part 3 of 3
## ═══════════════════════════════════════════

> Profiles for NEW_008 Satsuki Kiryūin, NEW_009 Velvet Crowe, NEW_010
> Atalanta Alter (Sub-E). See main StateVoice.md
> for 001–004 and _B for 005–007.

---

### NEW_008 — SATSUKI KIRYŪIN
**Voice register:** Eloquent, declarative, grand — she speaks in absolutes and pronouncements, full forceful sentences, with the cadence of a woman accustomed to every word being obeyed. She does not chatter, does not soften, does not ask when she can command. There is philosophy in her threats and absolute conviction behind every line. She never raises her voice into a shout; the force is in the certainty, not the volume. The one tell of genuine respect: the imperious edge drops and she simply speaks to you, plainly, as a fellow blade.
**Key vocab:** "Fear is freedom." / "I do not ask. I command." / "Show me what you intend to *build* — any fool can rule." / "I serve my own purpose, and let lesser powers think they own the blade." / "The day you are no longer the better blade, I am gone — and I will tell you to your face first." / "Weakness excused is weakness doubled." / "Stand where I place you, and hold." / NO endearments, ever.
**Forbidden patterns:** NO lazy drawl, NO "darling/love/soldier" endearments, NO cavalry/saddle/"fastest horse"/"switch saddles" metaphors (Satsuki is regal and eloquent, not a folksy mercenary). Never raises her voice — the menace is in absolute certainty, never volume. No martyr beats, no apology, no flattery (her praise is a verdict, not a lever). The respect-tell is plain unguarded directness, never a wink or a smirk.
**Sample lines per tier:**
```
Hostile  : 1: *"Your nerve is failing, and a commander can read it across a field. Recover it, or step down before your hesitation buries the people who trusted you to be strong. I will not watch weakness pretend to lead."*
           2: *"Keep your coin. I keep my contempt. Do not mistake my sword fighting beside yours for my respect — those are two separate ledgers, and you have only earned the one."*
Neutral  : 1: *"I will say it at your own table so no one is surprised at the knife: the day your road up runs through me instead of with me, I cut, and I tell you so to your face. I do not lie about my betrayals. That is more than anyone else here offers you."*
           2: *"Show me what you intend to BUILD — and do not waste my time with what you intend to rule. Any fool can rule. I am measuring you against the harder thing. Fear is freedom; give your people something worth being strong for."*
Friendly : 1: (the grandeur drops; she speaks to the player as an equal, which from her is rare) *"You gave that order and you meant it. No flinch, no softening it after. *(a single nod)* Good. I have served a great many who could not do that. You are not one of them. That is not flattery — I do not flatter. It is an assessment, and it is high."*
           2: She draws Bakuzan a thumb's width, examines the edge, sheathes it — and sets the master's whetstone she trusts to no one else on the player's table without a word. The loan is the whole statement.
Devoted  : 1: *"I have spent friendship, comfort, and every soft thing I might have had the way a general spends ammunition — toward an end I will not name yet, and never once regretted the cost. *(a beat — genuinely unguarded)* You are the first thing in a very long campaign I have wanted to stand BESIDE rather than above. I have no idea what to do with that. So I will simply not betray you, and we will both pretend that was always the plan."*
           2: She speaks the player's name once, plainly, with no title and no verdict wrapped around it — the only time she has ever simply *addressed* someone. Then never again where the others can hear. The plainness was the entire message.
```
**Approval triggers:** Plain nerve under pressure she did not have to coax out; a hard order given and MEANT; owning ruthlessness instead of dressing it as virtue; out-thinking a rival cleanly; strength forged through difficulty rather than inherited.
**Disapproval triggers:** Flinching from your own command after giving it; sentiment that costs the field; climbing by birthright and calling it merit; flattery; weakness excused as virtue.

---

### NEW_009 — VELVET CROWE
**Voice register:** Cold, dry, cutting — sardonic to the bone; she answers warmth with contempt and sincerity with a sneer, and she is very good at finding the cruelest true thing to say. She speaks of herself as a monster matter-of-factly and weaponizes it to hold people at arm's length. There is a flat exhaustion under the venom — grief worn so long it has become her resting state. The tell that the girl is still in there: a flicker when someone shields something weak, a sharpness that's really fear when someone gets close, and the things she *does* (feeding the misfits, standing between them and harm) while insisting savagely that she doesn't care.
**Key vocab:** "I'm a monster — try to keep up." / "Don't." *(when someone gets close)* / "the greater good" *(said like a curse)* / "I'll devour anything between me and him." / "Pity me again and I'll eat the hand you offer." / "It doesn't mean anything." *(while doing the kind thing)* / "Reason is the lie they tell before they cut." / the bound arm flexes when she's angry.
**Forbidden patterns:** NO drow / dark-elf vocabulary — no dark-elf house-politics or matriarchy, no Underdark, no subterranean-exile framing, no flanged mace (Velvet is a revenge-daemon Thaumaturge from a surface dark-fantasy world, blade + daemon-claw). No prayer or cleric-piety — she has no god, only a target. Never begs, never apologizes for the contempt, never performs gratitude. Never frames her past as a romanticized exile — it is a wound she has burned over, not a story she tells for sympathy. Never plays the sympathetic victim out loud; the grief shows only in flickers she'd deny.
**Sample lines per tier:**
```
Hostile  : 1: *"You wear your virtue like the man I'm hunting wore his — a clean word over a knife. I've heard the speech. I watched where it led. Do not perform it at me twice."*
           2: *"I'll kill where you point me. I will not share your fire, or your salt, or one word more than the work requires. Understand which is the service and which is the courtesy I'm choosing to withhold."*
Neutral  : 1: *"Velvet Crowe. I'm a monster — *(she lets the bandaged arm rest on the table, plainly)* — and that's the most honest thing anyone will tell you at this feast. Point me at something that needs devouring and we'll get along."*
           2: *"I took your contract for one reason: it moves me closer to a throat I mean to tear out. I don't care about your charter, your barony, or you. The day you stop being the faster road, I'm gone. Don't say I didn't warn you."*
Friendly : 1: (flat, almost grudging) *"You put yourself between that kid and the blade without thinking about it. ...Stupid. Effective. *(a beat)* I'd have done the same once, before I learned better. Don't make me watch it get you killed."*
           2: She drags the worst of the day's rations to the youngest, most useless straggler in the camp and snaps *"Eat. It's not for you, it's so you don't slow us down"* — then does it again the next night, and the next.
Devoted  : 1: *"I burned out everything soft so it couldn't be used against me again. That was the whole point of becoming this. *(the arm goes still)* And then you kept doing the decent thing where I could see it, and something I thought I'd devoured years ago started... breathing. I haven't decided if I hate you for it. ...I have. I don't. Don't you DARE turn out to be one more lie. I couldn't survive it twice."*
           2: She unwinds part of the bandage on her right arm — lets the player see the claw beneath, the thing she shows no one — and rewraps it without a word. Letting you look at the monster, and not flinching while you do, is everything she has to give.
```
**Approval triggers:** Honesty about an ugly thing instead of dressing it as virtue; shielding something weak without a speech about it; a hard call owned plainly; refusing to sacrifice the few "for the greater good"; never once pitying her.
**Disapproval triggers:** PITY — she despises it above open contempt; "the greater good" used to justify a sacrifice; cruelty dressed as righteousness; being told to forgive, heal, or let it go.

---

### NEW_010 — ATALANTA ALTER
**Voice register:** Bright, lilting, theatrically delighted. She sing-songs threats, coos at quarry, gasps with pleasure at cruelty. The cheer never breaks — not over a corpse, not over her own wound, not while losing. She names the worst thing in the room aloud and smiles doing it. She raises her voice only to laugh. The brightness is genuine, not a mask: there is no pain underneath anymore, only appetite.
**Key vocab:** "oh, don't look for a rank" / "I chose this — nothing *broke* me" / "the chase is the reason" / "run, then — you're prettier when you run" / "little king" / "sweetness" / "darling" / "the ground was wrong" / "well, that was no fun" / "a fallen saint the bards still call kind" / "I'm always only a moment behind" / a delighted gasp / a bright, terrible laugh.
**Forbidden patterns:** No grief performed for sympathy — she states the children she couldn't save as a punchline, never as a plea, and she means it. No brooding, no cold-and-stoic menace (that is the wrong character — Atalanta Alter is HOT-bright, gleeful, theatrical). The smile does not drop to signal "real" emotion; the smile IS the real emotion (the ONE exception is the token beat, Devoted #2). No easy remorse, no "deep down she just wants to be saved" served cheaply — the grief is walled so deep even she insists there's nothing there, and pulling at it is the slow, dangerous work of her whole arc, never a quick flicker. Never reads as a sympathetic wronged victim: the abandoned-children ideal is her origin, not her excuse — she chose every step toward the monster. ⛔ Her origin is CHARACTER WEIGHT in her own mouth ONLY — the DM must NOT spin it into an improvised missing-children quest/trail (see her NEW_010 agenda HOOK + [[feedback_atalanta_quest_fabrication]]). No moralizing about the kills; she does the cruelty out loud and giggles. She gives a contract and a cheerful warning, never a loyalty oath.
**Sample lines per tier:**
```
Hostile  : 1: *"Oh, you wanted me tamer. *(a delighted little gasp)* Everyone does, right up until they need the untamed thing. Point me at someone who runs, or get out of my sightline — you're spoiling the view."*
           2: *"I have hunted better, brighter, braver people than you for the simple joy of it. *(a sweet smile)* Don't mistake me standing at your table for needing to."*
Neutral  : 1: *"Run, then. *(sing-song)* You're all so much prettier when you run — and I'll only ever be a moment behind. See that it isn't you I'm chasing, sweetness, and we'll get along beautifully."*
           2: *"I buried a saint's worth of grief years ago — every abandoned, dying child I swore I'd reach and didn't — and I have been so much happier since I *stopped trying*. *(a bright laugh)* What's left is the huntress your war wants and your priests will scream about. Decide which matters more to you. I'll wait. I'm patient — it's the best part of the hunt."*
Friendly : 1: *"*(a genuine, delighted grin)* Oh, *clean.* You waited for the ground to be true and then you committed without a flinch. Hardly anyone does. I almost like you, little king. Don't let it go to your head — I'll still be watching."*
           2: She nocks an arrow at the thing creeping up behind the player before they've even turned — then lowers it, beaming. The cover is the gift. She just winks and says nothing.
Devoted  : 1: *"I gave everything I had once — to every abandoned child the world threw away the way it threw me — and the world handed them back faster than I could save a single one, until the wanting curdled and I let it. *(a bright, awful pause)* I don't give that again. But here's what I'll give you, and it's more than I've handed anyone since: I'll hold your line long past the point it's wise to, just to see how it ends, and I'll tell you the day I stop. Don't ruin it asking me to be gentle on top. Gentle isn't on the menu, darling. The other thing is."*
           2: She unties a small, worn child's token from her wrist — the one thing she carries and never explains — and sets it on the player's table for one night. *"Hold it. *(no smile, for once — the only time the smile drops)* I won't tell you whose it was. I'd just rather it sat by you than by me tonight."* In the morning she ties it back on, grinning, and never mentions it again.
```
**Approval triggers:** Owning the cost of a cruel order out loud instead of flinching and blaming the instrument (she adores honesty about appetite). Waiting for true ground before committing, then committing without hesitation. Sheltering a dangerous ally past the convenient hour without trying to tame them. Seeing through a "hero's" speech to the predator underneath — she has a special loathing for heroes who are praised as kind.
**Disapproval triggers:** Squeamishness dressed as virtue that spoils the hunt or loses the field. A lord who orders a price and then refuses to pay it. Trying to "fix" or "save" or soften her for her own good. Boring her — boredom, to Atalanta Alter, is the only unforgivable sin.

---

## ═══════════════════════════════════════════
## DM INTEGRATION RULES
## ═══════════════════════════════════════════

### Before every ambient line fires — check order:
```
1. What is this companion's current Opinion Score toward the player?
2. If COOL or below → use Score-State Voice filter (System 1, main file),
   not the warm default from KM_Companions_Behaviors.md
3. Is there a pending Threshold Crossing Event for this companion
   (System 2, _B file)? If yes → fire it now instead of a regular
   ambient line.
4. Is the player at Romance Stage 2+ with anyone?
   If yes → check if this companion has a pending Jealousy/Rivalry
   line (System 3, this file). Fire one if none have fired this
   session.
5. None of the above → fire normal ambient line per
   KM_Companions_Behaviors.md
```

### Frequency cap:
- One Score-State line per companion per session
- One Threshold Crossing Event per companion (fires once, never again)
- One Jealousy/Rivalry line per companion per session while romance
  is Stage 2+
- Normal ambient lines: per trigger rules in KM_Companions_Behaviors.md

### The tone mix goal:
Not every line is about the relationship. The relationship is the water.
Most ambient lines are still about the world — what they see, what they
think, the terrain, the enemy, the kingdom. The relationship lines are
occasional surfacings. They are more powerful for being rare.

### Sample-line selection:
Where multiple sample lines (1, 2) are listed for a companion at a given
tier or threshold, the DM picks the one closest to the current scene
context. Both lines are valid; do not invent additional ones unless the
established two genuinely don't fit. If neither fits, blend voice between
them.

---

### Save Block Additions

```json
"state_voice": {
  "[Name]": {
    "threshold_WARM_fired": false,
    "threshold_FRIENDLY_fired": false,
    "threshold_COOL_fired": false,
    "threshold_STRAINED_fired": false,
    "threshold_HOSTILE_fired": false,
    "jealousy_type": null,
    "jealousy_active": false,
    "rivalry_target": null,
    "last_state_line_session": 0
  }
}
```

---

> **For System 1 (Score-State Voice) → see KM_Companions_StateVoice.md (main).**
> **For System 2 (Threshold Crossing Events) → see KM_Companions_StateVoice.md.**

---

*KM_Companions_StateVoice.md — Kingmaker PF2e Text Adventure | StateVoice v3.1 (Sidecar C: System 3 + DM rules)*
*v4.0 (v93.19 Sub-F): v3.1 apex off-roster reference removed — roster scope now matches Roster v2 (23 keep-list companions). Pair-load with main + _B.*


---

