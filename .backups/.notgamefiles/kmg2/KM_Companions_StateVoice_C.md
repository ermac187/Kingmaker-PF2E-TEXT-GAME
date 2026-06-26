# KINGMAKER — COMPANION STATE VOICE: SYSTEM 3 (ROMANCE JEALOUSY & RIVALRY)
## KM_Companions_StateVoice_C.md | PAIR-LOAD WITH KM_Companions_StateVoice.md AND _B
## Continuation file. Always load alongside StateVoice main + StateVoice_B.

> **This file contains System 3 + DM integration rules + save-block schema.**
> See StateVoice main for System 1 (Score-State Voice) and StateVoice_B for
> System 2 (Threshold Crossing Events).
>
> Roster coverage matches main: active 11 (Linzi + #2 #15 #21 #24 #35 #39
> #43 #58 #78 #83) + 7 quest-locked CRPG companions (#1 #16 #18 #45-Kalikke
> #45-Kanerah #60 #66 #84) + 5 class-apex off-roster (#4 Senua, #46 Yang,
> #49 Weiss, #64 Alleria, #69 Imoen). Total: 23.

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
LINZI [if player romances Goldmoon, Tika, Sucrose, or Octavia]:
  Writes more. Reads you less. When you're in a scene together with
  the romance companion: *"I should let you two talk."* She wasn't
  in the way.

ARTORIA [if player romances anyone other than her]:
  *"My liege deserves joy. I am — pleased — for you both."* The
  hesitation is the entire content.

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

ARTORIA [to player, in private]:
  *"My king. — Sire. I will say this once. The oath I swore was
  not contingent on… anything. It is not contingent now. I needed
  you to know it has not changed. I will not raise it again."*

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

ARTORIA [accepted]:
  *"Sire. I believe in your choice. The oath stands sharper than
  before — duty unblunted by hope is the cleaner blade."*

ARTORIA [not accepted — rare]:
  Requests transfer to a different patrol rotation. Returns when
  asked. Will not revisit the topic.
```

---

### TYPE B — PROTECTIVE (cares about player; has opinions about the target)

> These companions are not jealous. They're watching the target and deciding
> if they trust them with the player. They may like the target fine in other
> contexts. In this context, they are assessing. They will say something if
> they don't like what they see.

**Stage 2 — watching:**
```
OLIVIER [most romances]:
  Reviews the romance target's combat performance with the player,
  unsolicited. *"[Name]'s positioning was crisp today. They held
  flank. That is a quality I value."* (verdict in progress)

GOLDMOON [most romances]:
  *"I have asked Mishakal about [Name]. The answer was — kind. I
  share it because you should know I asked."*

EKUNDAYO [most romances]:
  *"Trkaa watches [Name] more than usual."* If asked what that
  means: *"I don't know yet. She usually knows before I do."*

KYOKO [most romances]:
  *"I have catalogued [Name]'s known weaknesses and their last
  twelve combat decisions. The pattern is — acceptable. I shall
  inform you if it changes."*

JUBILOST [most romances]:
  *"I have prepared a brief — only fourteen pages — on the romance
  candidate's known associates, family lineages, and asset history.
  You should READ it. Romance is not exempt from due diligence."*
```

**Stage 3 — forming a verdict:**
```
OLIVIER [if she approves]:
  *"[Name] would die for you in a defensible posture. I find the
  prospect acceptable. Do not press them to."*

OLIVIER [if she doesn't approve]:
  *"[Name] makes decisions that suggest a private agenda. That
  agenda is now adjacent to YOU. Address it. Or I will."*

GOLDMOON [if she approves]:
  *"Mishakal does not bless every union. She blesses this one.
  I pass it along."*

GOLDMOON [if she doesn't approve]:
  *"I have prayed about this. The answer is — wait. Wait, and
  look more carefully. I have said what I was given."*

EKUNDAYO [if he approves]:
  *"Trkaa decided."* He nods toward the romance companion.
  *"That's enough for me."*

EKUNDAYO [if he doesn't approve]:
  *"I've been watching [Name] for two chapters. There's something
  they're not saying."* He looks at you. *"You probably know
  already. I just wanted you to know I know."*

KYOKO [if she approves]:
  *"My analysis is concluded. [Name] is — and I do not give this
  often — trustworthy. I have evidence. I will share it on request."*

KYOKO [if she doesn't approve]:
  *"My analysis flags three behavioral patterns inconsistent with
  the affection [Name] presents. I am providing the data. The
  interpretation is yours."*
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
> in current roster: Morrigan vs. anyone "naive" (Sucrose, Tika); Tatsumaki
> vs. anyone "weak" (Sucrose); Kanerah vs. romance targets she perceives as
> taking Kalikke's attention.

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
ARTORIA  : *"She illuminates rooms. You are fortunate. Treat the
            light gently."*
GOLDMOON : *"Her chronicle will outlive both of you. Make it a good
            chapter."*
YOKO     : *"Bardgirl, huh. She'll write you up when you snore.
            Hope you're flattered."*
NOK-NOK  : *"LINZI! Linzi is BEST! Nok-Nok approves! Hero good!"*
TRISTIAN : *"She finds light in everything."* Quietly. *"Hold onto
            that."*
OCTAVIA  : *"She'll surprise you. Pay attention when she does."*
```

**If player romances GOLDMOON:**
```
LINZI    : *"She prays for everyone. I am writing what it means
            that she now prays for you specifically."*
ARTORIA  : *"She is a healer who carries a war-chant. Match her
            in both. Or do not pretend."*
TIKA     : *"She kept me upright after a bad fight once. You should
            know that. She'll do the same for you."*
TRISTIAN : *"Mishakal is — different from Sarenrae. The answer is
            still the same. Be gentle with her."*
```

**If player romances ARTORIA:**
```
GOLDMOON : *"She binds her grief tightly. Do not pull threads
            you cannot retie."*
LINZI    : [writing furiously] *"This is the chapter people will
            read first. I want it accurate. Don't make me edit."*
OLIVIER  : *"She is a soldier. Treat her as a soldier first, a
            partner second. She will know the difference."*
MORRIGAN : *"Knights are tedious. Yours is less tedious than most.
            That is — a compliment."*
```

**If player romances OLIVIER:**
```
ARTORIA  : *"Major General Armstrong is a peer. Treat her as a
            peer. Your title does not raise you above her."*
TIKA     : *"She'll outlast you in arguments and outdrink you at
            camp. You know what you signed up for, right?"*
KYOKO    : *"Her history shows three failed unions. The pattern
            is informative. Read it."*
TATSUMAKI: *"Hmph. The COLD one. Suits you. You're both cold."*
```

**If player romances TIKA:**
```
LINZI    : *"She laughs harder than anyone in the chronicle.
            Don't stop making her laugh."*
ARTORIA  : *"She is a tavern's daughter who learned the spear.
            The combination is rare. Honor it."*
GOLDMOON : *"She gave me her last bandage at Old Sycamore. She
            gives. Make sure she also receives."*
RYUKO    : *"Tika's solid. Like — actually solid. Don't break
            that. I'll know."*
```

**If player romances RYUKO:**
```
TIKA     : *"She fights like a thunderstorm. You ready for the
            quiet after?"*
YOKO     : *"Hot-blood with a kamui fragment. You'd better keep
            up. She doesn't slow down for anyone."*
MORRIGAN : *"She runs at problems. Make sure she's running at
            the right ones."*
KANERAH  : *"Loud girl. Loud feelings. You can survive that. Or
            you can't. Don't pretend to."*
```

**If player romances MORRIGAN:**
```
LINZI    : *"She will say cruel things to your face and saved
            your life seven times in three sessions. Read both
            columns of the ledger."*
ARTORIA  : *"The witch is unblunted. Mind that what is sharp
            cuts both directions."*
SUCROSE  : *"She — she's been kind to me. In her way. Don't —
            don't hurt her. She would not show it if you did."*
TRISTIAN : *"Sarenrae has taught me to love what is difficult to
            love. I see why she sent her your way."*
```

**If player romances SUCROSE:**
```
LINZI    : *"She apologizes for existing. Make sure she stops.
            The chronicle deserves a Sucrose who knows she is
            seen."*
GOLDMOON : *"Be patient. She has been frightened a long time."*
YOKO     : *"Be GENTLE. I'm saying it once. She's small. You're
            not. Behave."*
TATSUMAKI: *"…The TIMID one. Hmph. Don't break her. Or — fine,
            just don't break her."*
```

**If player romances YOKO:**
```
TIKA     : *"She'll outshoot you and pretend she didn't. Don't
            let her pretend."*
RYUKO    : *"Yoko's the real deal. You'd better be too."*
LINZI    : *"She's written more poems in her head than she'd
            ever admit. Ask. She might tell."*
ARTORIA  : *"Markswomen love precisely. Be precise in return."*
```

**If player romances KYOKO:**
```
LINZI    : *"She files everything. She's filing this. You should
            know."*
JUBILOST : *"An investigator! Finally — someone of TASTE. I
            approve. I have prepared a small commemorative
            footnote. Do not lose it."*
OLIVIER  : *"Detectives evaluate. You will be evaluated. Be
            evaluable."*
TATSUMAKI: *"She thinks too much. You don't think enough. Maybe
            it works. Hmph."*
```

**If player romances TATSUMAKI:**
```
RYUKO    : *"BIG energy. You're either keeping up or crater.
            Good luck."*
MORRIGAN : *"The girl who lifts mountains has chosen the man who
            lifts swords. The arithmetic is — interesting."*
KYOKO    : *"Three documented outbursts this week. Plan accordingly."*
SUCROSE  : *"She's — she's louder than I am quiet. We balance,
            sometimes. You'll have to learn the rhythm."*
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
GOLDMOON : *"Sarenrae and Mishakal are not the same. They are
            sisters. We will manage. Be gentle with him."*
ARTORIA  : *"He prays for you nightly. I have heard it. I tell
            you because you should know what is given to you."*
NOK-NOK  : *"Tristian is HEALY-MAN. Tristian is GENTLE-MAN. You
            be gentle TOO! Or Nok-Nok WORDS-AT-YOU!"*
OCTAVIA  : *"Be careful. He gives himself. Don't take more than
            you can give back."*
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
YOKO     : *"I — okay. Okay. Sure. He's Nok-Nok. Yeah. He's a
            HERO. Don't hurt him. I'd actually be pissed."*
ARTORIA  : *"His heart is the size of a citadel. Treat the
            citadel as one would treat a city."*
TIKA     : *"Goblin Hero. Tavern's full of stories about goblin
            heroes. He's going to be the new ones."*
```

**If player romances EKUNDAYO:**
```
TRISTIAN : *"He has lost much. Sarenrae and Erastil both watch
            him. So shall I."*
OLIVIER  : *"Hunters love quietly. Match the volume. Do not
            speak over the silence."*
LINZI    : *"He says less than anyone in the chronicle. The pages
            about him are still the longest. That is a clue."*
```

**If player romances JUBILOST:**
```
LINZI    : *"He has given me TWO unsolicited drafts of his
            wedding-vow speech. The man is — invested."*
KYOKO    : *"His monologues are statistically correlated with
            heart-rate elevation. He is in love. The data is
            unambiguous."*
ARTORIA  : *"The gnome is unexpectedly tender. Honor that. He
            performs hardness. The performance is thin."*
```

**If player romances JAETHAL:**
```
GOLDMOON : *"She is dead. She is also — present. Mishakal does
            not forbid this. Mishakal asks: are you certain?"*
TRISTIAN : *"The undead are not outside Sarenrae's love. I will
            include both of you in my prayers."*
MORRIGAN : *"Charmed. The dead one. Of COURSE. You delight me,
            you know. You are an ongoing experiment."*
```

**If player romances REGONGAR:**
```
OCTAVIA  : *"You make him laugh. I noticed before he did. Don't
            stop."* [beat] *"Don't make me regret saying that."*
TIKA     : *"Big laugh. Big swing. Big heart. Don't break ANY
            of those, you hear me?"*
LINZI    : *"He is going to write me a letter about you, badly,
            and ask me to fix it. I am ready. I have a quill."*
```

**If player romances SENUA:**
```
GOLDMOON : *"She hears what others cannot. Mishakal honors that
            kind of listener. Be still around her. Stillness is
            half of love."*
LINZI    : *"She speaks in fragments because the voices speak
            in fragments. Listen to ALL of what she says. The
            chronicle is going to be hard to write fairly. I'll
            try."*
ARTORIA  : *"She has walked through her own underworld. Treat
            her as the warrior who returned, not as the wound
            that sent her."*
MORRIGAN : *"The Pict-girl. Marked. Touched. Listening. — I
            approve. Try not to disappoint her. The voices
            keep records longer than I do."*
TRISTIAN : *"Sarenrae teaches that what is broken can be loved
            without being repaired. Senua is not broken. But
            she is changed. Love what she IS."*
```

**If player romances YANG:**
```
RYUKO    : *"Yang's the real deal. You hit hard, she hits
            harder, you both hit fair. I respect it. Don't
            screw it up."*
TIKA     : *"She loses an arm and gets up swinging. You're
            going to see the strong days. Be there for the
            quiet ones too."*
LINZI    : *"She makes terrible puns. Write them down anyway.
            They are LOAD-BEARING. The chronicle has a JOKES
            appendix now. It is HER fault."*
ARTORIA  : *"A brawler who protects rather than dominates is
            rare. Honor the distinction. She made the choice
            consciously."*
MORRIGAN : *"The blonde girl who PUNCHES things. Of course.
            You delight me. Try not to die in a fashion she
            cannot lift you up from."*
```

**If player romances WEISS:**
```
ARTORIA  : *"The Schnee heir. She has unmade her family's name
            in her own hand. Honor that work. It is not finished."*
OLIVIER  : *"Heiress turned soldier. I respect the conversion.
            Treat her as a peer in both directions — title AND
            rank. She has earned both."*
KYOKO    : *"Her family records show three patterns of manipulation
            she has survived. She will recognize them in YOU
            instantly. Be careful what you pretend at."*
LINZI    : *"She filed her family crest off her sword herself.
            That is the chapter title I'm writing. Make sure I
            get to write a sequel."*
TATSUMAKI: *"Cold girl, sharp sword, COLD eyes. Hmph. Match.
            You picked a HARD one. Good."*
```

**If player romances ALLERIA:**
```
TRISTIAN : *"She walks with the Void at her shoulder and chooses
            otherwise daily. Sarenrae sees that choice. So shall I.
            Be the steady ground beneath her feet."*
ARTORIA  : *"A Ranger-General. A married woman in another life.
            Treat the past with the dignity she has earned for it.
            Do not attempt to replace it."*
MORRIGAN : *"The Void-touched elf. Excellent. Truly. You have
            chosen the most COMPLICATED person in the room. I am
            beginning to detect a pattern in your taste."*
GOLDMOON : *"Her grief is not a thing to be healed away. It is
            a thing to be honored. Honor it without naming it
            constantly. She'll know."*
KYOKO    : *"Her decision-tree is unusual: she has held a doomed
            position for a decade twice. She will hold YOU. Be
            worth holding."*
```

**If player romances IMOEN:**
```
LINZI    : *"She's pretending the bright is the whole story. It
            isn't. The chronicle has a 'beneath the smile' chapter
            and it is LONG. Don't be the reason it gets longer."*
TIKA     : *"She's been through worse than most of us. Don't make
            her teach you what 'worse' means. Just believe her."*
ARTORIA  : *"The pink-haired one. She is older than she looks
            and YOUNGER than she has had to be. Let her be the
            young one again. That is the gift."*
TRISTIAN : *"She survived Irenicus. Whatever I have to give her,
            it is small next to what she gave herself. Be that
            also — small in your demands, large in your patience."*
MORRIGAN : *"The Bhaalspawn rogue. Charmed. You collect them, do
            you. Very well — I shall watch with interest. Try not
            to break what surviving has already cracked."*
```

---

## ═══════════════════════════════════════════
## DM INTEGRATION RULES
## ═══════════════════════════════════════════

### Before every ambient line fires — check order:
```
1. What is this companion's current Opinion Score toward the player?
2. If COOL or below → use Score-State Voice filter (System 1, main file),
   not the warm default from KM_Companions_Ambient.md
3. Is there a pending Threshold Crossing Event for this companion
   (System 2, _B file)? If yes → fire it now instead of a regular
   ambient line.
4. Is the player at Romance Stage 2+ with anyone?
   If yes → check if this companion has a pending Jealousy/Rivalry
   line (System 3, this file). Fire one if none have fired this
   session.
5. None of the above → fire normal ambient line per
   KM_Companions_Ambient.md
```

### Frequency cap:
- One Score-State line per companion per session
- One Threshold Crossing Event per companion (fires once, never again)
- One Jealousy/Rivalry line per companion per session while romance
  is Stage 2+
- Normal ambient lines: per trigger rules in KM_Companions_Ambient.md

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
> **For System 2 (Threshold Crossing Events) → see KM_Companions_StateVoice_B.md.**

---

*KM_Companions_StateVoice_C.md — Kingmaker PF2e Text Adventure | StateVoice v3.1 (Sidecar C: System 3 + DM rules)*
*v3.1: 5 class-apex off-roster romance-target sections added (Senua, Yang, Weiss, Alleria, Imoen). Pair-load with main + _B. Same roster scope as main file.*
