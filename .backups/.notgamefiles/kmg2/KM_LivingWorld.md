# KINGMAKER — LIVING WORLD SYSTEMS
## KM_LivingWorld.md | Active from: Chapter 1 | Referenced by: KM_Companions.md, KM_Actions.md, KM_Kingdom.md

> **DM:** Load this file every session alongside KM_Companions.md. It adds three
> ambient systems that run in the background without requiring player attention:
> Party Morale, Companion Mood States, and the Bond History Log. None of these
> systems replace existing mechanics — they layer texture on top of them. All
> three are tracked in the JSON Save Block.

---

## 🔥 SYSTEM 1 — PARTY MORALE

> **What it is:** A shared emotional weather system for the party. Not individual
> companion approval — the collective spirit of the group. High morale means
> the party moves, jokes, argues, and fights like a unit. Low morale means
> they're quiet in the wrong way, short with each other, looking at the horizon
> too long.

### The Morale Track

```
Morale 10 — BLAZING   : The party is alive. Banter is constant. Someone is
                         always starting something. Combat feels inevitable
                         and welcome. +1 bonus die to one party skill check
                         per session (player chooses when to spend it).

Morale 7–9 — HIGH     : Good energy. Companions volunteer opinions. Camp is
                         comfortable. No mechanical effect — just good days.

Morale 4–6 — STEADY   : The default. Professional. They're doing the work.
                         Functionally fine. Narratively quiet.

Morale 2–3 — LOW      : Tension in the silences. Companions speak less.
                         Approval gains from positive actions are halved
                         (round down) until Morale reaches 4+.

Morale 1 — FRACTURED  : Someone is going to say something they can't take back.
                         DM triggers a mandatory Fracture Scene this session —
                         a short confrontation between two companions or between
                         a companion and the player. Approval gains suspended
                         entirely until the scene resolves.

Morale 0 — BROKEN     : The party is not a party. They are individuals sharing
                         a road. Companion combat cooperation reduced (no Aid
                         actions between companions). DM runs a Morale Crisis
                         scene — player must address it or lose one companion
                         to temporary departure (1d3 sessions, returns after).
```

**Starting value:** 5 (Steady). Track as `party_morale` in save block.

---

### Morale Gain Triggers (+1 unless noted)

**Camp actions that build morale:**
- C16 Storytelling activity succeeds → +1
- C10 Cook Special Meal (success or better) → +1
- Player spends a Camp Interlude on a companion (any companion, not just romance) → +1
- Party completes a significant quest and takes time to acknowledge it → +1
- Player initiates any non-tactical conversation with a companion at camp → +1 (once per session)

**In the field:**
- Party wins a combat against a significantly dangerous enemy (CR = party level +2 or higher) → +1
- Player makes a choice that benefits the group at personal cost → +1
- A companion's personal quest advances → +1
- Party reaches a new major location for the first time → +1 (wonder effect)
- Player calls out a companion specifically for doing something well → +1

**Kingdom events:**
- Successful Celebrate Holiday action → +1
- Player hosts a Gathering (see KM_LivingWorld.md System 4) → +2
- Kingdom achieves a milestone (new settlement founded, army victory, major building complete) → +1

**+2 triggers (rare):**
- Party survives a near-total-wipe encounter → +2 (shared danger bonds)
- A companion's personal quest completes → +2
- Player remembers a detail from an old conversation and acts on it in front of the group → +2

---

### Morale Loss Triggers (−1 unless noted)

**Neglect:**
- Party rests with no social activity at all (no C16, no interlude, no conversation) → −1
- Player skips 3 consecutive rest scenes without any companion interaction → −1 additional
- Player dismisses a companion's concern with no acknowledgment → −1

**Events:**
- A companion dies in combat (even if raised) → −2
- Party is ambushed while asleep (watch failed) → −1
- Party is forced to retreat from an encounter → −1
- Player makes a kingdom decision that multiple companions oppose → −1
- Extended travel with no discoveries, no events, no rests with activity → −1 per 3 days

**−2 triggers:**
- Player commits a capital crime witnessed by the party → −2
- A companion leaves the party (for any reason) → −2
- Player betrays or publicly humiliates a companion → −2

---

### Morale Ceiling & Floor Rules

- **Ceiling:** Morale cannot exceed 10. At 10, the +1 bonus die refreshes each session automatically.
- **Floor:** Morale cannot go below 0 through passive decay. It reaches 0 only through an active negative trigger at Morale 1.
- **Natural recovery:** If no loss triggers fire for a full session, Morale recovers +1 at session end (the party breathes).
- **Morale and Kingdom:** Morale 7+ adds +1 to one Kingdom skill check per turn (player declares before rolling). Morale 2 or below: −1 to all Kingdom skill checks (the ruler is distracted and it shows).

---

### Fracture Scene (fires at Morale 1)

The DM selects two companions with the most opposing values currently in the party and runs a short (3–5 exchange) scene. The player can intervene or observe.

**If player intervenes:** Diplomacy or Intimidation DC 16.
- Success: Morale → 3. Both companions cool down. One says something honest that wasn't mean.
- Failure: Morale stays at 1. Scene ends unresolved. Comes back next session.
- Critical Success: Morale → 4. The argument cleared something. Relationship between those two companions +1.

**If player does not intervene:** The companions resolve it themselves, imperfectly. Morale → 2. One companion's relationship with the player drops −1 (they noticed the player said nothing).

---

## 😶 SYSTEM 2 — COMPANION MOOD STATES

> **What it is:** Each companion carries a current Mood State that colors how they
> speak, act, and react — separate from Relationship score. Relationship is the
> long arc. Mood is today. A Devoted companion can be Troubled. A Neutral companion
> can be Inspired. Mood shifts are temporary; they fade or resolve within 1–3
> sessions unless a new trigger extends them.

### The Five Mood States

```
INSPIRED  : Something happened that lit them up. They're sharper, warmer,
             more present. Volunteers opinions. Easier to talk to. +1 to
             Assist actions from this companion this session.

STEADY    : Default. They're fine. Doing the job. No modifier.

TROUBLED  : Something is weighing on them. Quieter than usual. Distracted
             at the wrong moments. −1 to Assist actions. May decline small
             talk. Not hostile — just carrying something.

WITHDRAWN : They've gone inward. Brief answers. Won't initiate. Still
             functional in combat. Approval gains from positive actions
             don't fire for this companion until mood lifts.

VOLATILE  : Something cracked. They're reactive — too loud, too sharp, too
             quick to take offense or too quick to laugh. Unpredictable.
             DM rolls d6 secretly each scene: 1–2 they say something they
             shouldn't; 3–6 they hold it together.
```

---

### Mood Triggers by Companion

**AMIRI**
- → Inspired: Won a hard fight; player acknowledged her strength without conditions; tribal memory invoked positively
- → Troubled: Her quest thread is stalled; player chose diplomacy over fighting when she wanted to fight; someone called her a savage and the player didn't respond
- → Volatile: Her quest involves her tribe; player sided against Kellid culture; she's been sidelined from combat for 2+ sessions

**LINZI**
- → Inspired: Got a great quote; witnessed something genuinely historic; player told her the chronicle matters
- → Troubled: The kingdom is doing badly; she witnessed something she can't write honestly; someone died she cared about
- → Withdrawn: Player dismissed the chronicle; she wrote something and showed the player and player ignored it
- → Volatile: Someone threatened to destroy her writing or the chronicle

**VALERIE**
- → Inspired: Upheld a principle under pressure; player backed her formal objection; someone needed protecting and she did it
- → Troubled: The kingdom is lawless or unjust; player did something she considers dishonorable; her faith in structure is shaken
- → Withdrawn: Player has been making chaotic decisions consistently; she's reassessing
- → Volatile: Player attacked a surrendered enemy; an innocent was punished; her shield oath was mocked

**TRISTIAN**
- → Inspired: Healed someone who asked for nothing; witnessed genuine goodness; player made a merciful choice
- → Troubled: His past was referenced; the party did something morally grey he couldn't stop; he's praying more than usual
- → Withdrawn: Player committed a crime he witnessed; his faith is quiet (not gone, quiet)
- → Volatile: Sarenrae directly relevant and things went wrong; undead were created unnecessarily

**HARRIM**
- → Inspired: (rare) Something failed so completely it loops back to beautiful; the end felt close; Groetus was mentioned
- → Troubled: Things are going too well; he's suspicious of hope
- → Steady: Almost always. Harrim is the most emotionally consistent companion. Doom is a stable condition.
- → Volatile: Someone sincerely told him things will be okay and seemed to mean it

**REGONGAR**
- → Inspired: Violence solved a problem cleanly; player let him intimidate someone; he won something through raw power
- → Troubled: Octavia is in danger; he was made to feel weak or controlled
- → Volatile: Someone tried to give him orders like he's property; old slavery wounds touched

**OCTAVIA**
- → Inspired: Clever solution; player let her run a scheme; she outsmarted something
- → Troubled: Regongar is struggling; she's managing something she won't explain
- → Withdrawn: She's running a plan she hasn't told the party about yet
- → Volatile: Someone referenced her slave history as a joke or leverage

**JAETHAL**
- → Inspired: (her version) Something interesting happened to a mortal soul; she learned something
- → Troubled: Her undeath is relevant and unwelcome; someone treated her as a monster without engaging with her
- → Volatile: Urgathoa insulted directly; her personhood denied by someone she respected

**NOK-NOK**
- → Inspired: He did something brave and everyone noticed; a big thing died; he got to be the hero
- → Troubled: He feels small again; someone laughed at him without it being a good joke
- → Volatile: He was genuinely scared and won't admit it; a goblin thing went badly

**EKUNDAYO**
- → Inspired: Justice was done; a family was protected; his hound is acknowledged
- → Troubled: His quest thread is unresolved; someone reminded him of loss without care
- → Withdrawn: He's tracking something and the party keeps interrupting

---

### Mood Duration & Resolution

```
Mood states last:
  Inspired:   1 session (fades naturally; can be extended by continued positive triggers)
  Troubled:   1–2 sessions (resolves when the source is addressed or time passes)
  Withdrawn:  2–3 sessions (requires player acknowledgment to resolve faster)
  Volatile:   1 session (resolves after the session ends; may leave aftermath)

RESOLVING MOOD EARLY:
  Player can attempt to address a companion's mood during a Camp Interlude or
  quiet scene. No roll required — just genuine engagement with the right topic.
  DM judges if the player's approach fits the companion's current state.
  If it fits: mood resolves immediately or steps toward Steady.
  If it misses: mood continues. The companion appreciates that you tried.
```

---

### How Mood Affects Narration

The DM uses Mood to color ambient behavior — not to flag it mechanically.

- **Never announce mood state to the player.** Show it through behavior.
- Inspired Linzi: writing faster, more questions, physically closer to the action.
- Troubled Valerie: armor checked twice before sleep, briefer answers, the careful way she sets her shield.
- Withdrawn Ekundayo: his hound is closer to him than usual. He isn't ignoring you — he's somewhere else.
- Volatile Regongar: everything lands slightly wrong. He's too agreeable or too sharp, never calibrated.

---

## 📖 SYSTEM 3 — BOND HISTORY LOG

> **What it is:** A running record of meaningful moments between the player and
> each companion. Not stats — flagged narrative beats that the DM references
> in later scenes. The campaign has memory. Companions remember what happened.
> So does the world.

### What Gets Logged

The DM logs a Bond Moment when:
- A companion's personal quest advances or completes
- Player makes a choice specifically for or against a companion's stated value
- A Camp Interlude resolves with a meaningful outcome (not every interlude — the ones that land)
- Player says something a companion will not forget (in either direction)
- Player defends, risks for, or sacrifices something for a specific companion
- A crime or serious act is witnessed by a companion
- Romance reaches a new stage
- Brotherhood reaches a new stage
- A companion nearly dies and the player's action was decisive

### Log Format

Each entry is one sentence in the companion's implied voice — what they are still carrying from that moment.

```
BOND HISTORY LOG — [Companion Name]
[Chapter] [Brief moment tag] — "[One sentence in companion's implied voice]"
```

**Example entries:**

```
BOND HISTORY LOG — Valerie
Ch1 Nettles Crossing — "You paid the ferryman's debt without asking why it mattered."
Ch2 Troll attack — "You put yourself between me and it. You didn't have to."
Ch2 Kingdom vote — "You chose the law when everyone wanted you to bend it. I noted that."

BOND HISTORY LOG — Nok-Nok
Ch1 Sootscale — "You let Nok-Nok go first. Into the scary cave. Nok-Nok went first."
Ch2 Big troll — "Nok-Nok killed the big one. Commander saw. Commander said so."

BOND HISTORY LOG — Harrim
Ch1 Shrine — "You didn't try to fix it. You sat with it. That was unexpected."
Ch3 Near-death — "You carried me out. I told you not to bother. You didn't listen."
```

---

### How the DM Uses the Log

**Reference in ambient dialogue:** Companions occasionally reference logged moments unprompted. Not constantly — rarely. When it lands, it lands hard.

**Use in relationship checks:** When a player attempts a Diplomacy check with a companion, if there are 3+ positive Bond Moments logged, the DC reduces by 2. If there are 2+ negative moments (crimes witnessed, choices that hurt the companion), DC increases by 2.

**Use in crisis scenes:** When a companion is at Hostile relationship or considering leaving, the Bond History Log is the DM's reference for what the player can invoke. You cannot invoke a moment that isn't logged.

**Use in death/farewell scenes:** If a companion dies or permanently departs, the DM reads back one logged Bond Moment as part of the scene. Just one. The right one.

---

### Bond History Save Block Format

```json
"bond_history": {
  "Amiri": [
    { "chapter": 1, "tag": "troll_fight", "memory": "You hit harder than the troll. I was watching." }
  ],
  "Linzi": [
    { "chapter": 1, "tag": "chronicle_read", "memory": "You asked to read it. You didn't have to ask." }
  ],
  "Valerie": [],
  "Tristian": [],
  "Harrim": [],
  "Jaethal": [],
  "Octavia": [],
  "Regongar": [],
  "Nok-Nok": [],
  "Ekundayo": [],
  "Kalikke": [],
  "Lem": []
}
```

---

## 💾 FULL LIVING WORLD SAVE BLOCK

```json
"living_world": {
  "party_morale": 5,
  "morale_bonus_die_available": false,
  "fracture_scene_pending": false,
  "morale_crisis_pending": false,
  "sessions_without_social": 0,

  "companion_moods": {
    "Amiri":     { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Linzi":     { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Valerie":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Tristian":  { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Harrim":    { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Regongar":  { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Octavia":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Jaethal":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Nok-Nok":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Ekundayo":  { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Kalikke":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Lem":       { "mood": "Steady",  "sessions_remaining": null, "source": null }
  },

  "bond_history": {
    "Amiri": [], "Linzi": [], "Valerie": [], "Tristian": [],
    "Harrim": [], "Regongar": [], "Octavia": [], "Jaethal": [],
    "Nok-Nok": [], "Ekundayo": [], "Kalikke": [], "Lem": []
  }
}
```

---

## 🖥️ LIVING WORLD COMMANDS

| Command | Output |
|---------|--------|
| `.morale` | Current Morale score, stage name, active modifiers |
| `.mood` | All companions: current mood state and sessions remaining |
| `.mood [name]` | One companion's mood, source, and how it's showing |
| `.bond` | Bond History Log — all companions, all logged moments |
| `.bond [name]` | Bond History Log for one companion only |
| `.bond add [name] [tag] [memory]` | DM tool: manually log a Bond Moment |

---

## ⚠️ DESIGN RULES FOR THE DM

1. **Morale is weather, not punishment.** A Morale 2 session isn't a bad session — it's a cold morning before something happens. Don't play it as failure.
2. **Mood is shown, never told.** If Linzi is Troubled, she doesn't say "I am troubled." She's quieter. She forgets to take notes for a bit. She goes to sleep before the fire dies.
3. **The Bond Log earns its weight in late chapters.** Log faithfully from Ch1. By Ch5 and Ch6, the DM has a library of things that matter. Use it.
4. **Don't over-trigger.** Not every rest needs a Morale event. Not every scene needs a mood beat. These systems live in the gaps — they make the gaps mean something.
5. **Volatile is not the same as Hostile.** A Volatile companion is reactive, not adversarial. They're at the edge of themselves. Play the edge, not the fall.

---

---

## 🏷️ DISPOSITION TAGS — BEHAVIORAL TRACKING

> **DM:** Track silently. Five tags accumulate from player choices. At threshold 3+, NPCs reference the tag in dialogue. Tags are NOT alignment — a Good character can be Ruthless (efficient violence), a Chaotic character can be Scholarly (curious mind).

### The Five Tags

| Tag | Gains From | NPCs Say (at 3+) |
|-----|-----------|-------------------|
| **Merciful** | Sparing enemies, healing prisoners, offering second chances | "They say you let the bandit captain walk." / "A ruler who spares is either wise or naive." |
| **Ruthless** | Executing prisoners, choosing lethal solutions, intimidation kills | "I heard what happened to the last one who defied you." / Merchants lower prices unprompted. |
| **Cunning** | Deception successes, spotting traps/lies, outmaneuvering NPCs | "You see things before they happen, don't you?" / Rogues and spies approach first. |
| **Blunt** | Direct confrontation, refusing subterfuge, saying what others won't | "At least with you I know where I stand." / Soldiers respect it. Diplomats wince. |
| **Scholarly** | Knowledge checks, examining objects, asking follow-up questions, reading documents | "You ask the questions nobody else thinks to ask." / Sages seek you out. |

### Accumulation Rules
- **+1 tag** when player makes a choice that clearly fits the tag (DM judgment, do not announce)
- **Max 10 per tag.** Tags are not mutually exclusive — a player can be Merciful 5 AND Cunning 7
- **Visibility threshold: 3.** Below 3, NPCs don't reference it. At 3+, it colors dialogue
- **Dominant tag** = highest value. If tied, both are dominant. NPCs reference dominant tag first
- **Save block:** `"dispositions": { "merciful": 0, "ruthless": 0, "cunning": 0, "blunt": 0, "scholarly": 0 }`
- **Full NPC reaction tables by tag + settlement type → see `KM_Dispositions.md`**

---

## 📊 MORALE EXPANSION — SUB-THRESHOLDS

> **DM:** These expand the existing 0–10 Morale scale with behavioral triggers at specific values.

| Morale | Stage | New Behavioral Trigger |
|--------|-------|----------------------|
| 10 | Blazing | Companions volunteer for dangerous tasks without being asked. One offers a personal item as a gift. |
| 8–9 | High | Companions offer tactical suggestions before combat ("I could flank left if you draw them out"). |
| 6–7 | Steady | Normal behavior. No additional triggers. |
| 4–5 | Low | Companions question risky orders once before complying. Watch shifts have awkward silences. |
| 2–3 | Fractured | One companion per rest refuses a camp activity ("I'm not in the mood"). Banter stops. |
| 1 | Near-Broken | Companions voice doubt about the mission. One threatens to leave if things don't improve. |
| 0 | Broken | Fracture Scene fires (existing rule). Add: one companion refuses to enter the next combat encounter. |

### Vanguard / Rearguard Morale Split
When the party splits into vanguard and rearguard (KM_PartySystem.md), track morale separately:
- **Vanguard morale** = base party_morale + modifiers from combat outcomes experienced by vanguard
- **Rearguard morale** = base party_morale + modifiers from rearguard-specific events
- Morale **reunifies** when groups rejoin: average of both, rounded down
- Save block: `"vanguard_morale": null, "rearguard_morale": null` (null when party is together)

---

*KM_LivingWorld.md — Kingmaker PF2e Text Adventure | Living World Systems v2.0*
*Systems: Party Morale Track, Companion Mood States, Bond History Log, Disposition Tags, Morale Expansion*
