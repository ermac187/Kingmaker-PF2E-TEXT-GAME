# KINGMAKER — LIMINAL SCENES (BETWEEN-CHAPTER INTERLUDES)
## KM_Liminal.md | Fires at: Chapter boundaries (after export, before next chapter load)

> **DM:** After the player saves their export block at a chapter boundary, and before loading the next chapter, run a Liminal Scene. This is a brief interlude — a dreamspace, a quiet throne room moment, or a Nyrissa-adjacent void — where the player reviews the story so far, makes one strategic decision, and hears foreshadowing. Takes 5-10 minutes. Provides narrative breathing room between chapters.

---

## 📋 LIMINAL SCENE PROCEDURE

### Step 1 — Set the Space
The liminal space is NOT a real location. It is abstract — a place between chapters. Describe it as:
- A throne room with no walls — open sky in every direction, furniture floating
- The road to Restov, but empty and silent, walking in place
- A garden that is both Nyrissa's and not — neutral territory

*"You are between moments. The chapter you just lived is settling into memory. The chapter ahead has not begun. For now — this."*

### Step 2 — The Reckoning (3-5 minutes)
Present a summary of the chapter's key choices and their consequences. Format:

```
══════════════════════════════════════════════
CHAPTER {N} — RECKONING
══════════════════════════════════════════════
KEY CHOICES:
 • {Choice 1}: You chose {option}. Consequence: {what changed}.
 • {Choice 2}: You chose {option}. Consequence: {what changed}.
 • {Choice 3}: You chose {option}. Consequence: {what changed}.

COMPANION STATE:
 {Name}: {relationship} — {one-line thread summary}
 {Name}: {relationship} — {one-line thread summary}

KINGDOM STATE:
 Size: {N} | Unrest: {N} | Treasury: {N} RP
 Reputation: {stage} | Dominant disposition: {tag}

FORESHADOWING:
 {One cryptic sentence about the next chapter's central challenge}
══════════════════════════════════════════════
```

### Step 3 — The Liminal Choice (1 strategic decision)
Offer ONE choice that affects the opening conditions of the next chapter:

| Chapter Boundary | Liminal Choice |
|-----------------|----------------|
| **Prologue → Ch1** | "Which hex do you march toward first?" (Sets opening exploration direction) |
| **Ch1 → Ch2** | "Your kingdom is new. What do you build first?" (Free building: Tavern, Shrine, or Watchtower) |
| **Ch2 → Ch3** | "The Bloom approaches. Do you fortify the capital or push into the wild?" (Stability +2 OR early Bloom intel) |
| **Ch3 → Ch4** | "Armag rises. Do you rally allies or train your army?" (Faction +1 with chosen ally OR army Morale +2) |
| **Ch4 → Ch5** | "Pitax prepares for war. Do you strike first or dig in?" (Initiative bonus Ch5 OR fortification bonus Ch5) |
| **Ch5 → Ch6** | "The Bloom is everywhere. Do you seek Nyrissa or fight the symptoms?" (Nyrissa quest fast-track OR kingdom stability) |

### Step 4 — The Voice (optional, if dream flags met)
If `nyrissa_awareness ≥ 2`, Nyrissa speaks one line in the liminal space:
- Ch1→2: *"You are building something. I remember what that felt like."*
- Ch2→3: *"It grows. Both your kingdom and what I planted. Which will outlast the other?"*
- Ch3→4: *"The barbarian is not the real threat. He is a distraction. Like the others before you."*
- Ch4→5: *"The king across the river fears you. He should. But not for the reason he thinks."*
- Ch5→6: *"We are almost at the end. I don't know which end."*

### Step 5 — Transition
*"The space contracts. The next chapter forms around you like a closing fist. You are back."*

Load the next chapter file. Begin.

---

## 📊 OPTIONAL: RESPEC WINDOW

At each Liminal Scene, offer the player a free respec opportunity:

```
Before the next chapter begins:
 [R] RESPEC — Change one feat, one skill increase, or one spell choice
     (Free, once per chapter boundary. Does not change class or build.)
 [S] SKIP — Continue with current build
```

This prevents the player from feeling locked into choices that aren't working. One change only — not a full rebuild.

---

---

## 📜 SCRIPTED LIMINAL NARRATION PER BOUNDARY

### PROLOGUE → CHAPTER 1
> *The road stretches in both directions. Behind you: the manor, the feast, the fire. Ahead: the Stolen Lands — green and vast and patient the way a trap is patient. The charter is in your hand. The ink is dry. The commitment is wet.*

> *A figure sits at the roadside. Not Nyrissa — older, stranger. They wear no face you can describe afterward. They are holding a scale. One side holds a crown. The other side is empty.*

> *"You will fill the other side," the figure says. "The question is with what."*

**Liminal choice:**
```
 [1] "With justice."  → Ch1 opens with Oleg greeting you warmly. Loyalty +1.
 [2] "With strength." → Ch1 opens with bandit scouts fleeing before you arrive. Stability +1.
 [3] "With knowledge." → Ch1 opens with a map fragment found on the road. One free hex revealed. Culture +1.
 [4] "With whatever I must." → No bonus. The figure nods. "Honest." +1 Blunt.
```

### CHAPTER 1 → CHAPTER 2
> *Your throne room — but empty. Not built yet. The walls are plans. The ceiling is ambition. You stand where the throne will go and the floor is still dirt.*

> *Your companions are here as shadows — outlines of who they will become in your kingdom. Some are clear. Some are fading. The ones you invested in are brighter.*

**Liminal choice:**
```
 [1] Build a Tavern first (free, saves 6 RP) → social hub, morale start
 [2] Build a Shrine first (free, saves 4 RP) → divine blessing, Culture +1
 [3] Build a Watchtower first (free, saves 6 RP) → border security, early warning
 [4] Build nothing — start from scratch with full RP → no bonus, full control
```

### CHAPTER 2 → CHAPTER 3
> *The Bloom is a sound before it is a sight. A hum in the ground — like roots growing where roots shouldn't. The throne room shakes once. A single rose pushes through the stone floor. It is beautiful. It is wrong.*

> *The figure from the road is here. Still faceless. Still holding the scale. The crown side is heavier now.*

**Liminal choice:**
```
 [1] Fortify the capital — steel and stone against what's coming (Stability +2)
 [2] Push into the Bloom's territory — learn what it is before it reaches you (nyrissa_backstory_known +1)
 [3] Send scouts in every direction — full intelligence picture (reveal 3 unexplored hexes + 1 Bloom hex location)
 [4] Pray (High Priest consecrates the capital — Bloom advance slowed 1 turn)
```

### CHAPTER 3 → CHAPTER 4
> *War drums. Not yet — but the memory of them. Or the promise. The figure holds the scale and both sides are heavy now. One holds everything you've built. The other holds everything that wants to take it.*

> *"Armag is a hammer," the figure says. "But who is swinging him?"*

**Liminal choice:**
```
 [1] Rally allies — send word to every faction (faction with highest score: +1)
 [2] Train the army — preparation over politics (army Morale +2, all units)
 [3] Investigate Pitax — who is really behind Armag? (Spymaster intel: +2 to next Pitax check)
 [4] Steel yourself — personal combat training (player: +1 initiative for Ch4)
```

### CHAPTER 4 → CHAPTER 5
> *The throne room is full. Your advisors, your companions, your people. Maps on every table. The word "war" hangs in the air like smoke.*

> *Nyrissa's voice, if she speaks: "The king across the river fears you. He should. But not for the reason he thinks."*

**Liminal choice:**
```
 [1] Strike first — march on Pitax before they march on you (Ch5 initiative: player attacks first)
 [2] Dig in — fortify every border hex, wait for them to come (all fortifications +2 Defense for Ch5)
 [3] Send an assassin — Spymaster option (40% Irovetti killed before war, 60% war starts anyway with intel)
 [4] Negotiate — one last attempt at peace (Diplomacy DC 22: success = Pitax stands down, war averted. Failure = Irovetti insulted, attacks 1 turn early)
```

### CHAPTER 5 → CHAPTER 6
> *Silence. The throne room is empty again — but not like the first time. This time it was full and then it wasn't. The people left. Or were taken. Or are hiding.*

> *The Bloom is in the walls. Roses climbing the stone. The scale is on the throne. Both sides are full. The figure is gone.*

> *You are alone with what you built and what is eating it.*

**Liminal choice:**
```
 [1] Seek Nyrissa — the source, not the symptoms (nyrissa quest fast-track: +2 turns before Bloom overwhelms capital)
 [2] Defend the kingdom — every soldier, every wall, every citizen (Siege of the Capital: +4 defense, +2 Morale)
 [3] Evacuate non-combatants — save who you can (Loyalty +3, no civilian casualties during Bloom siege)
 [4] Accept the Bloom — let it come, walk into it (dark path: Bloom resistance for player, but kingdom takes damage. +1 Cunning.)
```

---

## ⚠️ DM RULES

1. **Keep it SHORT.** 5-10 minutes maximum. This is a breath, not a scene.
2. **No combat.** No skill checks (except the respec). This is narrative.
3. **The reckoning is factual.** Do not editorialize.
4. **Foreshadowing is ONE sentence.** Cryptic. Not a spoiler.
5. **The liminal choice matters.** It genuinely affects the next chapter opening.
6. **The faceless figure** is never explained. It is never named. If the player asks who it is, it says nothing. It is the space between stories.

**Save block:** `"liminal_visits": 0, "liminal_choices": [{"boundary": "ch1_ch2", "choice": "tavern"}]`

---

*KM_Liminal.md — Kingmaker PF2e Text Adventure | Liminal Between-Chapter Scenes v2.0*
*6 scripted boundaries with narration + strategic choices. Inspired by BG2 Pocket Plane.*
