# KINGMAKER — NEWER SYSTEMS (CONSOLIDATED)
## KM_Mythic_Systems.md | v1.0 (2026-05-22): Merged from 13 newer-system files. Single source of truth.

> **DM:** Database file. Each section preserves the source file's original structure. Query by topic name.

**Table of Contents**
- [Dispositions](#dispositions)
- [Examination](#examination)
- [Debates](#debates)
- [Influence](#influence)
- [Ultimatums](#ultimatums)
- [Dreams](#dreams)
- [Liminal](#liminal)
- [Scripted Interactions](#scripted-interactions)
- [Crafting](#crafting)
- [Dungeon Puzzles](#dungeon-puzzles)
- [Mobile Base](#mobile-base)
- [Mythic Paths](#mythic-paths)
- [Endings](#endings)



---

<!-- merged from KM_Dispositions.md (v93.21 file consolidation) -->

# KINGMAKER — DISPOSITION TAG SYSTEM
## KM_Dispositions.md | Referenced by: KM_Kingdom.md, KM_NPCs.md, KM_World_Systems.md

> **DM:** This file contains full NPC reaction tables for each of the 5 disposition tags. Load when the player's dominant tag reaches 3+ (tracked in KM_Kingdom.md). NPCs reference the player's dominant tag in dialogue — not by name, but through behavioral cues, offers, and assumptions. Disposition is NOT alignment. A Lawful Good ruler can be Ruthless. A Chaotic Neutral ruler can be Scholarly.

---

## 📊 DISPOSITION GAIN REFERENCE

### Merciful (+1 per instance)
- Spare a defeated enemy when execution was available
- Heal or tend a prisoner
- Offer a second chance after betrayal
- Choose negotiation over combat when combat was clearly easier
- Forgive a debt or fine
- **Bonus +2:** Spare a named villain who harmed you personally

### Ruthless (+1 per instance)
- Execute a prisoner or defeated enemy
- Choose lethal force when nonlethal was available
- Intimidation check that causes lasting fear (Frightened 3+)
- Order a companion to do something cruel
- Destroy something valuable to make a point
- **Bonus +2:** Execute a named NPC the party had a relationship with

### Cunning (+1 per instance)
- Succeed on a Deception check in a meaningful social scene
- Spot a trap, lie, or hidden motive before it triggers (Perception/Sense Motive)
- Outmaneuver an NPC in negotiation (achieve better terms than offered)
- Use information gathered earlier to leverage a current situation
- Set a trap or ambush that works
- **Bonus +2:** Solve a major plot problem through manipulation rather than force

### Blunt (+1 per instance)
- Directly state an uncomfortable truth to an NPC's face
- Refuse a bribe, shortcut, or convenient lie
- Confront authority publicly
- Choose the straightforward plan over the clever plan
- Tell an ally they're wrong when diplomacy would be easier
- **Bonus +2:** Publicly accuse a powerful NPC of wrongdoing with evidence

### Scholarly (+1 per instance)
- Succeed on a Recall Knowledge check in exploration
- Examine an object, document, or scene detail (`.examine` or equivalent)
- Ask a follow-up question about lore or history in dialogue
- Read a found document fully (not skimming)
- Choose to investigate before acting
- **Bonus +2:** Solve a puzzle without hints or skill checks

---

## 🗣️ NPC REACTION TABLES BY TAG

### MERCIFUL (dominant tag 3+)

| NPC Type | Reaction |
|----------|----------|
| **Guards/Soldiers** | Defer more readily. Lower threat assessment. "The ruler who spares is the ruler who can afford to." Some respect it. Veterans find it naive. |
| **Merchants/Vendors** | Slightly higher initial prices — mercy reads as softness to traders. +5% markup until reputation overrides. |
| **Prisoners/Criminals** | Surrender more quickly. Word spreads in underworld: "This one lets you live." Crime system: +10% surrender rate on apprehension. |
| **Nobles/Diplomats** | Leverage it. "Your reputation for mercy precedes you — surely you can extend that courtesy to our border dispute." Diplomacy DCs from nobles: −1 (they expect to win concessions). |
| **Commoners** | Warm. Gift frequency +1 per chapter. Children approach without fear. Mothers name sons after you (ambience). |
| **Clergy** | Favorable. Good-aligned clergy seek audience. Evil-aligned clergy test boundaries. "A merciful ruler is a challenge." |
| **Companions** | Good-aligned companions: +1 Opinion over time. Evil-aligned companions: occasional dialogue questioning whether mercy is weakness. |

### RUTHLESS (dominant tag 3+)

| NPC Type | Reaction |
|----------|----------|
| **Guards/Soldiers** | Snap to attention faster. Obey without hesitation. Fear-based compliance — efficient but brittle. Morale checks under pressure: −1 (they fear failure more than the enemy). |
| **Merchants/Vendors** | Lower prices unprompted. −5% on all purchases. They don't want trouble. |
| **Prisoners/Criminals** | Fight harder when cornered — surrender means death. Crime system: −10% surrender rate. But crime rate drops −15% (deterrence). |
| **Nobles/Diplomats** | Cautious. Fewer demands. Diplomacy DCs: +1 (they don't want to provoke you but also don't trust you). Offers come pre-sweetened. |
| **Commoners** | Quiet. Streets clear faster when you walk. Gift frequency −1 per chapter. Nobody makes eye contact. Efficient governance, cold streets. |
| **Clergy** | Good-aligned clergy: concerned dialogue. Evil-aligned clergy: approach with partnership offers. "Strength recognizes strength." |
| **Companions** | Evil-aligned companions: +1 Opinion. Good-aligned companions: occasional pushback. Morale −1 if Ruthless 7+ (companions afraid too). |

> ⛔ **BATTLEFIELD EXTENSION — ADVERSARY MORALE & QUARTER (KM_Combat_Systems.md).** The Prisoners/Criminals surrender effect above is NOT only for the Crime system — it governs **combat morale too.** `mercy_standing = Merciful − Ruthless` is the enemy-facing "Mercy Standing": Merciful pulls broken enemies toward **surrender**, Ruthless toward **flee or fight-to-the-death** (surrender = death to a known butcher). Leaders/captains/bosses comment on it and behave differently. ⛔ **It's a CURVE, not a slope — both extremes cost you:** too merciful → enemies stop fearing you (Intimidation/coercion fail; surrenders may be faked); too savage → enemies refuse capture (no live prisoners → intel lost). The firm middle takes the most usable prisoners. Run the full system at an enemy's break point — see KM_Combat_Systems.md § ADVERSARY MORALE & QUARTER. Word only spreads from survivors (annihilation teaches no one).

### CUNNING (dominant tag 3+)

| NPC Type | Reaction |
|----------|----------|
| **Guards/Soldiers** | Slightly paranoid around you. Double-check their own reports before presenting them. "If the ruler already knows, why is she asking?" |
| **Merchants/Vendors** | Harder to cheat. They assume you know the real price. Deception DCs against you: +2 (from their perspective). No price modifier — they respect the game. |
| **Prisoners/Criminals** | Talk more carefully. Provide less information voluntarily but respond well to specific questions. Interrogation quality improves: +1 to question yield. |
| **Nobles/Diplomats** | Respect but guard themselves. Fewer casual offers. More formal proposals with contingencies. "This ruler reads the contract." Diplomacy: neutral DCs, but they offer better initial terms. |
| **Commoners** | Wary admiration. "Clever ruler" is a compliment with reservations. Trust takes longer. Once earned, deeper. |
| **Rogues/Spies** | Approach first with information for sale. Spymaster's network expands faster: −1 turn to recruit new agents. |
| **Companions** | Int/Wis-based companions: +1 Opinion. Cha-based companions: neutral. Cunning companions offer tactical observations more often. |

### BLUNT (dominant tag 3+)

| NPC Type | Reaction |
|----------|----------|
| **Guards/Soldiers** | Respect. Strongly. "Knows what to say and says it." Morale +1 in combat when ruler is present (certainty is reassuring). |
| **Merchants/Vendors** | No haggling attempts. They give you the real price first. Saves time. No price modifier — straightforward dealing. |
| **Prisoners/Criminals** | Confess faster. Blunt interrogation breaks pretense. Interrogation time: −1 question to reach truth. |
| **Nobles/Diplomats** | Some offended, some refreshed. Diplomacy DCs: +1 with formal courts (no protocol). −1 with frontier leaders (they prefer plain speech). |
| **Commoners** | Trust quickly. "At least with this one, you know." Gift frequency neutral. Petition frequency +1 (they feel they can approach). |
| **Clergy** | Mixed. Forthright clergy appreciate it. Political clergy find it inconvenient. |
| **Companions** | Martial companions: +1 Opinion. Social/diplomatic companions: occasional friction. Amiri: +2 Opinion. |

### SCHOLARLY (dominant tag 3+)

| NPC Type | Reaction |
|----------|----------|
| **Guards/Soldiers** | Mild confusion. Respect the title but don't understand the approach. "The ruler was reading during the siege briefing." |
| **Merchants/Vendors** | Offer rare books, maps, scrolls first. Scholarly items appear in merchant inventory +1 per chapter. |
| **Prisoners/Criminals** | Provide more contextual information — they sense the ruler wants the full picture, not just a confession. |
| **Nobles/Diplomats** | Bring advisors. Come prepared with documentation. Diplomacy DCs: −1 (they can't bluff when you've read the treaty). |
| **Commoners** | Send their children to ask questions. Sages and tutors seek positions at court. +1 Culture per kingdom turn (soft bonus, not cumulative past +3). |
| **Wizards/Scholars** | Approach unprompted with research problems, ancient texts, translation requests. These become side quest hooks. |
| **Companions** | Int-based companions: +1 Opinion. Wis-based: neutral. Cha-based: mild teasing ("Are you going to read about the monster or fight it?"). |

---

## 📊 CROSS-TAG INTERACTIONS

When two tags are both at 5+, NPCs reference the combination:

| Combination | NPC Shorthand |
|-------------|---------------|
| Merciful + Scholarly | "The philosopher-king" — sages and clergy seek audience first |
| Merciful + Blunt | "Honest and fair" — commoners trust deeply, criminals take advantage |
| Ruthless + Cunning | "The spider" — everyone is afraid and no one knows why |
| Ruthless + Blunt | "The executioner" — feared but never ambushed. No one is confused about consequences |
| Cunning + Scholarly | "The mastermind" — spies and sages compete for attention |
| Blunt + Scholarly | "The professor" — lectures enemies before defeating them |

---

## ⚠️ DM RULES

1. **Never announce tag changes.** The player does not see "+1 Merciful." They see NPCs reacting differently over time.
2. **Reference dominant tag within 2 NPC interactions** of entering a new settlement. Not every NPC — but the first merchant or guard should color their greeting.
3. **Tags do not decay.** Once earned, permanent. The player's history follows them.
4. **Conflicting tags are fine.** Merciful 6, Ruthless 4 = a ruler who is usually merciful but has a hard edge. NPCs notice both.
5. **Track via `.disposition` command** — displays all 5 tags and current values. Player-facing, not NPC-facing.

---

*KM_Dispositions.md — Kingmaker PF2e Text Adventure | Disposition Tag System v1.0*
*Core rules in KM_Kingdom.md. This file: NPC reaction tables and DM guidance.*


---

<!-- merged from KM_Examination.md (v93.21 file consolidation) -->

# KINGMAKER — OBJECT EXAMINATION SYSTEM
## KM_Examination.md | Referenced by: KM_Commands.md, KM_DMRules.md

> **DM:** When the player uses `.examine [object]` or describes examining something specific in the scene, this system governs the response. Object examination rewards curiosity with lore, hidden items, and Codex entries. It feeds the Scholarly disposition tag (KM_Dispositions.md).

---

## 📋 COMMAND

`.examine [object]` — Examine a specific object, surface, or detail in the current scene.

**Aliases:** `.look at [object]`, `.inspect [object]`, or natural language ("I examine the bookshelf", "I look at the stain on the floor")

---

## 🔍 EXAMINATION PROCEDURE

### Step 1 — Is the object in the scene?
- If the object was described in the Scene Brief, narration, or is a reasonable inference from the location: proceed.
- If the object was NOT described and is NOT a reasonable inference: "You don't see [object] here."
- **Do NOT invent objects.** If the player asks to examine something the files don't mention, it's not there.

### Step 2 — Determine examination tier

| Tier | DC | What It Reveals | Example |
|------|-----|----------------|---------|
| **Surface** | None (free) | Physical description: size, material, condition, visible markings | "The bookshelf is old oak, warped from damp. Three shelves. The bottom shelf is empty." |
| **Detail** | Perception DC 12 | Hidden features: scratches, stains, wear patterns, maker's marks | "The bottom shelf has drag marks — something heavy was moved recently." |
| **Lore** | Recall Knowledge DC 14 (relevant skill) | Historical, magical, or cultural significance | "The maker's mark is Aldori — this shelf was looted from a swordlord's estate." |
| **Secret** | Perception DC 18 or specific knowledge | Hidden compartments, concealed items, trapped mechanisms | "Behind a false panel: a folded map with three locations circled in red ink." |

### Step 3 — Output format
```
[EXAMINE — {Object Name}]
{Surface description — always shown}
{Detail — only if Perception check succeeds}
{Lore — only if Knowledge check succeeds}
{Secret — only if high Perception or player names the right spot}
```

### Step 4 — Tag and reward
- **+1 Scholarly** if the examination reveals Detail or Lore tier (not Surface alone)
- **Found Document:** If the object contains a readable document, add to `found_documents[]` in save block
- **Codex Entry:** If the lore is significant, add to player's Codex (KM_Glossary.md)
- **Hidden Item:** If Secret tier reveals an item, add to `pending_loot` — player must `.loot` to claim

---

## 🏠 SCENE OBJECT CATEGORIES

### Objects That Should Always Be Examinable

| Location Type | Default Examinable Objects |
|---------------|--------------------------|
| **Throne Room** | Throne, tapestries, windows, advisory table, floor stones, fireplace |
| **Tavern/Inn** | Bar counter, notice board, fireplace, kegs, patron belongings (if visible) |
| **Dungeon** | Walls (for moisture/carvings), doors (for mechanisms), floor (for tracks), ceiling (for drips/creatures) |
| **Camp** | Campfire (coals, fuel type), bedrolls (arrangement), perimeter (tracks, disturbances), sky (weather signs) |
| **Market** | Stalls (specific wares), carts (origins), vendor equipment (quality tells) |
| **Wilderness** | Trees (age, carvings), rocks (mineral type), water (clarity, flow), animal signs (tracks, scat) |
| **Battle Aftermath** | Bodies (equipment, insignia, wounds), ground (blood patterns, footprints), dropped items |

### Objects That Should NEVER Be Examinable (Fabrication Risk)
- Objects the player names that are not in the scene files
- NPC body parts or intimate details (redirect to Perception check for tells)
- Items inside locked/sealed containers the player hasn't opened
- Anything that would reveal DM-only information without a check

---

## 📖 LORE QUALITY STANDARDS

**Good examination lore:**
- Connects to something the player has seen or will see
- Reveals one specific fact, not a summary
- Creates a question the player might follow up on
- Is short: 1-3 sentences maximum

**Bad examination lore:**
- Generic flavor with no game connection ("It's an old bookshelf")
- Dumps paragraphs of history unprompted
- Reveals answers to active mysteries without a check
- Tells the player what to do with the information

---

## ⚠️ DM RULES

1. **Examination is free action in Exploration mode.** No action cost. The player is curious — reward it.
2. **In Combat:** Examining an object costs 1 action (Seek action variant). Perception check applies.
3. **Repeat examinations:** If the player examines the same object twice, give them the same info. Do NOT invent new details to fill the second look.
4. **Companion assist:** If a companion has a relevant skill (Medicine for wounds, Crafting for weapons, Religion for holy symbols), they can assist — use their modifier instead if higher.
5. **Chain examinations:** If examining object A reveals object B, the player can examine B immediately. This is how multi-step discovery works.
6. **Scene files override this file.** If a chapter file specifies what examining a specific object reveals, use that text, not generated content.

---

## 📋 CHAPTER-SPECIFIC EXAMINABLE OBJECTS WITH LORE PAYOFFS

### PROLOGUE — Jamandi's Manor

| Object | Location | Surface (free) | Detail (Perc DC 12) | Lore (Know DC 14) | Secret (Perc DC 18) |
|--------|----------|----------------|---------------------|--------------------|--------------------|
| Jamandi's sword | Banquet hall, on display | Aldori dueling blade, well-used | The edge has been resharpened hundreds of times — this is not ceremonial | Aldori Swordlords train from age 7. This blade has 40+ years of muscle memory in its wear | Hidden inscription on the pommel: a name. Not Jamandi's. |
| The feast wine | Any table | Red, Rostland vintage, served in silver | Faint residue on the rim — slightly cloudy | Paralytic agent. Tasteless. Takes 10 minutes to take effect. | The serving staff didn't pour from the same casks — kitchen staff used a different barrel. |
| Tartuccio's ring | If given to player | Gold, ornate, warm to the touch | Faint arcane aura. Not dangerous — but not simple jewelry | Tracking enchantment. Low-power. Someone wants to know where the wearer goes. | The maker's mark is Pitaxian. Tiny, inside the band. |
| Manor walls | Any corridor | Thick stone. Old construction. Aldori banners. | Scratches on the floor — furniture has been moved recently to create choke points | The manor was built as a fortress first. The feast hall was an armory. | Behind one banner: a sealed passage (leads to secret room). |

### CHAPTER 1 — The Stolen Lands

| Object | Location | Surface | Detail (DC 12) | Lore (DC 14) | Secret (DC 18) |
|--------|----------|---------|----------------|-------------|----------------|
| Oleg's palisade | Oleg's Trading Post | Wooden walls, recently reinforced | The reinforcement is amateur — Oleg did this himself | This was originally a Brevic border checkpoint. The foundation stones have garrison markings. | A buried cache under the south wall: 50 gp + a map fragment (hex reveal). |
| Stag Lord's helmet | Stag Lord's Fort | Antlered helm, crude | The antlers are real — grafted onto a metal frame | Pre-dates the Stag Lord by centuries. This was a religious artifact repurposed as armor. | Fey-touched. Detect Magic: faint transmutation. The antlers grow 1mm per year. |
| Old Sycamore tree | Old Sycamore hex | Massive, ancient, hollow | The trunk has been carved — tunnels inside are shaped, not natural | First World thin spot. The tree exists partially in both planes. | At midnight, the tree hums. Nature DC 16: it's communicating with something underground. |
| Tartuccio's journal | Old Sycamore, after defeat | Leather-bound, coded entries | The code is simple substitution cipher. Decryptable with Linguistics DC 12 or 10 minutes. | Contents: payment records, contact descriptions, references to "P." (Pitax) | A page torn out. The torn edge has blood on it. Not Tartuccio's blood type. |

### CHAPTER 2-3 — Kingdom Building

| Object | Location | Surface | Detail (DC 14) | Lore (DC 16) | Secret (DC 20) |
|--------|----------|---------|----------------|-------------|----------------|
| Throne (when built) | Capital throne room | Whatever materials the player chose | The craftsmanship reflects who built it — dwarven joints, elven filigree, or rough frontier carpentry | A throne is a symbol before it's furniture. The first ruler to sit in it defines what it means. | If eRmaC's Aerynth armor contacts the throne: faint resonance. The materials recognize each other across worlds. |
| Bloom roses | Any Bloom hex | Beautiful. Wrong colors. Sweet smell with decay undertone | The petals are warm. Plants shouldn't be warm. | First World corruption. Not natural growth — forced manifestation. Something is pushing reality aside. | The roots go deeper than any plant's should. They're not feeding on soil. They're feeding on the boundary between planes. |
| Kingdom banner | Capital or army | Whatever the player designed | The fabric is mundane. The symbol is not — people react to it before they read it. | Symbols acquire power through association. This one is acquiring it fast. | Merchants from other kingdoms have started copying the design. Imitation is the first stage of cultural influence. |

---

## ⚠️ DM RULES

1. **Examination is free action in Exploration.** In Combat: 1 action (Seek).
2. **Repeat examinations:** Same info. Do NOT invent new details.
3. **Companion assist:** Use their modifier if higher.
4. **Chain examinations:** Examining A reveals B → player can examine B immediately.
5. **Scene files override this file.**
6. **These tables are EXAMPLES.** DM generates examination results for objects not listed here using the same tier system (Surface/Detail/Lore/Secret).

**Save block:** Examination discoveries feed into `found_documents[]` and Codex entries.

---

*KM_Examination.md — Kingmaker PF2e Text Adventure | Object Examination System v2.0*
*Rules + chapter-specific examination tables with lore payoffs.*


---

<!-- merged from KM_Debates.md (v93.21 file consolidation) -->

# KINGMAKER — PERSUASION DEBATE SYSTEM
## KM_Debates.md | Referenced by: KM_DMRules.md, KM_Commands.md

> **DM:** When two characters have a fundamental disagreement that cannot be resolved by a single check or player fiat, use the Debate system. This is a structured social contest — best of 3 opposed checks. It replaces "DM decides" with a mechanical resolution that feels earned.

---

## ⚔️ WHEN TO USE DEBATES

**Use a Debate when:**
- Two companions disagree on a course of action and the player wants to settle it fairly
- The player is negotiating with a stubborn NPC who won't yield to a single Diplomacy check
- A kingdom advisor proposes something another advisor opposes (KM_Kingdom.md)
- The player wants to convince a companion to change their mind on a deeply held belief

**Do NOT use a Debate when:**
- A simple skill check would resolve it (use the normal roll)
- The disagreement is trivial or one-sided
- Combat is imminent (switch to Initiative)
- The NPC is mindless, fanatical, or magically compelled (no debate possible)

---

## 📋 DEBATE PROCEDURE

### Step 1 — Frame the Debate
DM announces the debate, the stakes, and the two positions:
```
[DEBATE — {Topic}]
POSITION A: {Character A's stance} — championed by {Name}
POSITION B: {Character B's stance} — championed by {Name}
Stakes: {What happens if A wins / What happens if B wins}
Best of 3 rounds. Each round: opposed skill check.
```

### Step 2 — Three Rounds of Opposed Checks
Each round, both sides choose a social approach:

| Round | Approach Options | Skill Used |
|-------|-----------------|-----------|
| **Round 1 — Opening** | Argue (Diplomacy), Provoke (Intimidation), or Mislead (Deception) | Chosen skill vs. opponent's Will DC |
| **Round 2 — Rebuttal** | Any approach. Cannot repeat Round 1's exact skill. | Same mechanic |
| **Round 3 — Closing** | Any approach. Free choice — repetition allowed. | Same mechanic |

**Resolution per round:**
```
Roll: d20 + [skill mod] vs DC [10 + opponent's Will save bonus]
Success      = Win this round (+1 point)
Crit Success = Win this round (+2 points) — devastating argument
Failure      = Lose this round (opponent +1 point)
Crit Failure = Lose badly (opponent +2 points) — humiliating concession
```

### Step 3 — Determine Winner
- **First to 3 points wins.** (Can end early on Round 2 if someone scores crit success both rounds.)
- **Tie after 3 rounds:** Deadlock. Neither side concedes. DM presents compromise or player makes final call (relationship consequence for the loser).

### Step 4 — Consequences

| Outcome | Effect |
|---------|--------|
| **Player wins** | NPC/companion yields on the specific issue. No relationship penalty for graceful loss. +1 Cunning or Blunt disposition (DM choice based on approach used). |
| **Player wins by 3+ point margin** | Decisive victory. NPC/companion deeply reconsiders. +1 relationship with any witness who agreed with the player's position. |
| **Player loses** | NPC/companion's position prevails this time. Player can override (ruler authority) but takes −1 relationship with the companion AND −1 with any witness. |
| **Player loses by 3+ point margin** | Humbling defeat. −1 relationship with companion. +1 relationship with opponent (they respect you fought). Disposition tag gain: +1 Blunt (you tried). |
| **Deadlock** | Unresolved tension. Companion mood shifts to Troubled (KM_Kingdom.md). Issue resurfaces in 1d4 sessions. |

---

## 🎯 VOLLEY MODE — BACK-AND-FORTH CONVERSATION

> **DM:** Use Volley Mode for any high-stakes conversation, argument, interrogation, or confrontation where the normal flow (NPC delivers full speech → player replies to all of it) would break the scene. One beat at a time. No walls of text.

---

### What It Is

**Normal mode:** NPC delivers a full speech → player reads it → player replies to everything at once.

**Volley Mode:** NPC speaks 1–3 sentences → stops → player responds → NPC reacts (1–3 sentences) → repeat. Each exchange is one beat. The conversation builds naturally and the player can react in the moment.

---

### How to Enter

- Player types `.volley` — DM enters Volley Mode for the current conversation
- Player types `.end` to exit at any time
- DM should suggest it for: heated arguments, tense negotiations, Tartuccio confrontations, Phase 4.5 companion scenes, accusations, any conversation where pacing matters

**Phase 4.5 companion scenes default to Volley pacing.** Short beats. Player responds to each. Not speeches.

---

### Rules

1. **NPC maximum: 3 sentences per beat** — then stop and wait
2. **The NPC reacts to what the player actually said** — not what it expected
3. **Inline mechanical notes — one line max after each beat:** `[Tartuccio: credibility −1]` / `[Amiri: +1 relationship]`
4. **Player responds freely** — no choice menu required (optional). Say anything, go silent, stand up, leave
5. **No assumptions about what the player will say next** — the NPC does not pre-load a response to an answer it hasn't received

---

### Automatic Triggers

- Phase 4.5 companion scenes
- Tartuccio's Phase 4.5 slot (his one exchange per clock cycle = one volley)
- Any direct challenge from the player (`"You were standing there the whole time"` → volley)
- Any formal accusation or confrontation scene

---

### Example Rhythm

```
NPC: [1–3 sentences]
[pause — waiting]

> player says something

NPC: [reacts to what was actually said — 1–3 sentences]
[pause — waiting]

> player says something
```

No monologues. No walls. The scene builds one exchange at a time.

---

### Relationship to the Interrupt System

Volley Mode supersedes the interrupt system for conversational contexts. When the NPC only speaks 3 sentences before pausing, the player naturally responds before the next assumption lands — no mid-speech break mechanics needed. The interrupt fail codes remain active for cases where the DM delivers a full speech outside Volley Mode.

---

## 🤝 COMPANION ASSIST

If a third party wants to support one side:
- **Second:** One companion can "second" a debater. The debater gains +2 circumstance bonus to ONE round (declared before the roll).
- **Cost:** The seconding companion stakes their own reputation. If the side they support loses, −1 relationship with the winning side's champion.
- **Limit:** One second per side per debate.

---

## 📊 NPC DEBATE MODIFIERS

| NPC Type | Modifier | Reason |
|----------|----------|--------|
| **Nobles / Diplomats** | +2 to Diplomacy rounds | Professional arguers |
| **Barbarians / Warriors** | +2 to Intimidation rounds, −2 to Deception | Direct, honest, threatening |
| **Rogues / Spies** | +2 to Deception rounds | Trained liars |
| **Scholars / Clergy** | +2 to Diplomacy, −2 to Intimidation | Reason over force |
| **Merchants** | +2 to Deception, +1 to Diplomacy | Salespeople |

---

## 🎯 EXAMPLE DEBATES

### Companion Disagreement
```
[DEBATE — Prisoner Fate]
POSITION A: Execute the bandit leader — championed by Amiri
POSITION B: Imprison and interrogate — championed by Tristian
Stakes: A wins = execution, +1 Ruthless. B wins = prisoner lives, +1 Merciful.
```

### Kingdom Advisor Conflict
```
[DEBATE — Tax Policy]
POSITION A: Raise taxes to fund the army — championed by Treasurer
POSITION B: Keep taxes low to maintain loyalty — championed by Councilor
Stakes: A wins = Economy +2, Loyalty −1. B wins = Loyalty +1, Economy −1.
```

### NPC Negotiation
```
[DEBATE — Trade Agreement]
POSITION A: Favorable terms for our kingdom — championed by Player (eRmaC)
POSITION B: Favorable terms for Pitax — championed by Irovetti's Envoy
Stakes: A wins = +3 Economy for 2 turns. B wins = +1 Economy but Pitax spy network installed.
```

---

## ⚠️ DM RULES

1. **Debates are NOT combat.** They are social encounters. Choice menu rules still apply after the debate resolves (10-30 options for what to do next).
2. **Show all math.** Every roll is displayed with full breakdown, same as combat.
3. **NPCs argue back.** Between rounds, the DM narrates the NPC's counter-argument. This is not just rolling dice — it's a scene. The arguments should be in character.
4. **Player can forfeit.** At any point, the player can concede the debate. Same as losing, but no crit failure penalty.
5. **Debate frequency:** No more than 1 debate per session unless the player initiates additional ones. Overuse dilutes impact.
6. **Companion-vs-companion debates** (player not participating): Player watches and chooses which side to support via the Second mechanic, or stays neutral.

---

## 📋 CHAPTER-SPECIFIC SCRIPTED DEBATES

### DB-1: The Bandit Captain's Fate (Ch1)
```
[DEBATE — What to do with a captured bandit leader]
POSITION A: Execute — championed by Amiri
  "Dead bandits don't recruit. Dead bandits don't escape."
POSITION B: Imprison and interrogate — championed by Tristian
  "A dead man tells no tales. A living one tells everything."
Stakes: A = +1 Ruthless, bandit intel lost | B = +1 Merciful, intel gained
```

### DB-2: The Troll Treaty (Ch2-3)
```
[DEBATE — Negotiate with trolls or exterminate]
POSITION A: Negotiate territory — championed by Grand Diplomat
  "Every war we avoid is gold we keep and soldiers who live."
POSITION B: Exterminate — championed by General
  "Trolls don't honor treaties. They honor fire."
Stakes: A = Loyalty +1, Stability +1, risk of troll betrayal | B = Stability +2, Culture −1
```

### DB-3: The Coronation Speech (Ch4)
```
[DEBATE — What kind of ruler to declare yourself]
POSITION A: Servant of the people — championed by Councilor
  "A ruler who serves earns loyalty no crown can buy."
POSITION B: Sovereign by right of conquest — championed by General
  "You took these lands with blood and will. Own it."
Stakes: A = Loyalty +3, +1 Merciful | B = Stability +3, +1 Ruthless
```

### DB-4: The Spy's Fate (Ch3-4)
```
[DEBATE — What to do with a captured Pitax agent]
POSITION A: Turn them — championed by Spymaster
  "A spy you control is worth ten you kill."
POSITION B: Public execution — championed by Marshal
  "A dead spy sends a message. A turned spy sends doubt."
Stakes: A = +1 Cunning, Spymaster network +1, 20% double-agent risk | B = +1 Blunt, Pitax faction −1, deterrence
```

### DB-5: The Alliance Price (Ch4-5)
```
[DEBATE — Accept Aldori military aid with strings attached]
POSITION A: Accept — championed by Grand Diplomat
  "We need their swords more than we need our pride."
POSITION B: Refuse — championed by Ruler (player argues against themselves)
  "Their swords come with chains. We fight alone or not at all."
Stakes: A = Aldori army unit joins, Aldori faction +2, kingdom owes a future favor | B = No allies, +2 Morale (independence), +1 Blunt
NOTE: Player can champion either side or delegate.
```

### DB-6: The Mercy Question (Ch5, during war)
```
[DEBATE — Spare surrendered Pitax soldiers]
POSITION A: Spare and recruit — championed by Tristian
  "They fought for a tyrant. Now the tyrant is gone. Give them a choice."
POSITION B: Prisoner camp — championed by Valerie
  "Mercy to the enemy is cruelty to our dead. Contain them."
Stakes: A = +1 army unit (Pitax Defectors, low morale), +1 Merciful | B = Stability +2, no risk, +1 Ruthless
```

### DB-7: The Nyrissa Debate (Ch6, if nyrissa_backstory_known ≥ 2)
```
[DEBATE — Can Nyrissa be saved?]
POSITION A: Save her — championed by Tristian or player
  "She was cursed. She did not choose this. If there is a way to undo it, we must try."
POSITION B: Destroy her — championed by Jaethal or General
  "A thousand years of murder. The Bloom ate kingdoms. Sympathy does not resurrect the dead."
Stakes: A = True Ending path confirmed, +1 Merciful | B = Standard ending, +1 Blunt
NOTE: This is the most important debate in the game. The DM narrates it with full weight.
```

### DB-8: The Legacy Debate (Ch6, pre-finale)
```
[DEBATE — What happens to the kingdom if you don't come back]
POSITION A: Succession plan — championed by Councilor
  "Name an heir. Write a charter of succession. The kingdom survives you."
POSITION B: No plan — championed by Amiri
  "If you die, you die. The kingdom figures it out. That's what kingdoms do."
Stakes: A = Kingdom stability post-game, Councilor +1 | B = Nothing changes. +1 Blunt. Amiri: "Finally, someone who doesn't plan for their own funeral."
```

---

*KM_Debates.md — Kingmaker PF2e Text Adventure | Persuasion Debate System v2.0*
*Rules + 11 scripted debates. Inspired by Divinity: Original Sin.*


---

<!-- merged from KM_Influence.md (v93.21 file consolidation) -->

# KINGMAKER — INFLUENCE-GATED COMPANION ABILITIES
## KM_Influence.md | Referenced by: KM_Companions.md, KM_Companions_Behaviors.md, KM_DMRules.md

> **DM:** Load this file from Ch2 onward. Each companion has two hidden abilities locked behind relationship extremes. At **Devoted (+2)** they unlock a positive passive. At **Hostile (−2)** they unlock a dark ability — the companion is still useful but working against the player's interests in subtle mechanical ways. Announce the unlock inline when the relationship crosses the threshold. The ability persists until the relationship changes.

---

## 📊 UNLOCK RULES

| Relationship | Threshold | Effect |
|-------------|-----------|--------|
| **Devoted** (+2) | Companion trusts completely | Unlock **Devoted Passive** — a permanent beneficial ability |
| **Friendly** (+1) | Normal positive | No special ability |
| **Neutral** (0) | Default | No special ability |
| **Strained** (−1) | Tension | No special ability, but companion occasionally questions orders |
| **Hostile** (−2) | Active resentment | Unlock **Dark Ability** — companion subtly undermines the player |

### Rules
- **Announcement:** When relationship crosses +2 or −2, DM narrates a scene (2-3 sentences) where the ability manifests for the first time. Not a popup — a character moment.
- **Persistence:** Ability stays active as long as relationship stays at that threshold. If relationship moves from +2 to +1, Devoted Passive deactivates (DM narrates the withdrawal).
- **One per companion.** A companion cannot have both abilities active simultaneously.
- **Dark abilities are HIDDEN from the player.** The player sees the consequences but the DM does not announce "Dark Ability activated." The player must figure out why things keep going wrong.

---

## 🟢 DEVOTED PASSIVES (Relationship +2)

| Companion | Devoted Passive | Mechanic |
|-----------|----------------|----------|
| **Amiri** | **Blood Fury** — Amiri enters a controlled rage when the player drops below 25% HP | Amiri gains +2 attack, +4 damage for 3 rounds. Fires once per combat, auto. |
| **Linzi** | **Chronicler's Insight** — Linzi notices things the player missed | Once per exploration scene, Linzi auto-succeeds on a Perception check the player failed (DM reveals the missed detail as Linzi's observation). |
| **Valerie** | **Shield Sister** — Valerie positions to cover the player instinctively | When player is critically hit, Valerie can use her reaction to Shield Block for the player if adjacent. Reduces damage by her shield's Hardness. |
| **Harrim** | **Fatalist's Clarity** — Harrim's nihilism becomes tactical precision | +1 circumstance bonus to party Will saves when Harrim is in the active party. "Nothing matters. Which means nothing can frighten us." |
| **Jaethal** | **Undying Sentinel** — Jaethal ignores the first instance of dying per day | When Jaethal drops to 0 HP, she instead drops to 1 HP once per long rest. "Death and I have an arrangement." |
| **Tristian** | **Mercy's Touch** — Tristian's heals carry emotional weight | Tristian's Heal spells restore +2 HP per spell rank. "He means it. You can feel the difference." |
| **Octavia** | **Arcane Harmony** — Octavia links her casting to the player's rhythm | When the player casts a spell, Octavia can cast a cantrip as a free action on the same target (once per combat). |
| **Regongar** | **Rage Bond** — Regongar fights harder near the player | +1 attack when adjacent to the player. "He's not protecting you. He's competing." |
| **Nok-Nok** | **Goblin Instinct** — Nok-Nok senses ambushes | Party cannot be surprised while Nok-Nok is in active party. "Nok-Nok smelled them first." |
| **Ekundayo** | **Hunter's Mark Shared** — Ekundayo's prey becomes the party's prey | When Ekundayo uses Hunt Prey, all party members gain +1 circumstance to attack that target. |
| **Jubilost** | **Alchemical Surplus** — Jubilost produces extra consumables | At each long rest, Jubilost creates 1 free alchemical item (bomb, elixir, or antidote) from his supplies. |

---

## 🔴 DARK ABILITIES (Relationship −2) — DM EYES ONLY

> **⛔ Do NOT reveal these to the player.** The player experiences the effects. They must figure out the cause. If confronted, the companion denies it (Deception vs. player's Perception).

| Companion | Dark Ability | Hidden Mechanic |
|-----------|-------------|-----------------|
| **Amiri** | **Reckless Spite** — Amiri takes unnecessary risks in combat | Amiri attacks the most dangerous enemy regardless of tactics. Ignores player formation orders 30% of the time. |
| **Linzi** | **Edited Chronicle** — Linzi records events with a slant | Reputation gains from witnessed deeds are −1 (Linzi's version is less flattering). Player may notice NPC reactions don't match expectations. |
| **Valerie** | **Cold Shoulder** — Valerie withholds Shield Block | Valerie does not use Shield Block reaction for the player. Uses it for other companions only. |
| **Harrim** | **Doom Whisper** — Harrim's pessimism becomes contagious | −1 to party Morale gain triggers (morale increases by 1 less). Harrim's camp dialogue is noticeably darker. |
| **Jaethal** | **Shadow Drain** — Jaethal siphons from healing | When an area Heal is cast, Jaethal absorbs 2 HP from the player's share. Undetectable without Medicine DC 18. |
| **Tristian** | **Withheld Grace** — Tristian's heals are less effective | Tristian's Heal spells on the player restore −2 HP per spell rank. On others, normal. |
| **Octavia** | **Spell Interference** — Octavia's magic creates static | Player's spell DCs are −1 when Octavia is in the party. Subtle arcane interference. Arcana DC 20 to detect. |
| **Regongar** | **Friendly Fire** — Regongar's AoE "accidents" | Regongar's AoE spells have a 15% chance to include the player in the area. "Sorry. Got carried away." |
| **Nok-Nok** | **Sticky Fingers** — Nok-Nok pockets loot before the player sees it | 10% of coin loot from encounters is silently reduced. Nok-Nok's personal gold increases. Perception DC 16 to notice discrepancy. |
| **Ekundayo** | **Withdrawn Support** — Ekundayo stops sharing tactical information | Ekundayo no longer warns of ambushes or tracks for the party. Player loses any ranger Perception bonuses from Ekundayo. |
| **Jubilost** | **Sabotaged Supplies** — Jubilost's alchemy is slightly off | Alchemical items used by the player have a 20% chance of reduced effect (half damage, half duration). Jubilost blames "field conditions." |

---

## 📋 DETECTION AND CONFRONTATION

If the player suspects a Dark Ability and confronts the companion:

1. **Companion denies** — Deception check vs. player's Perception
2. **If caught** — Companion admits resentment. Player gets 3 options:
   - **Address the grievance** — Start a repair path. If player resolves the underlying issue, relationship can climb back to −1 and Dark Ability deactivates.
   - **Threaten** — Intimidation DC 16. Dark Ability pauses for 1 chapter. Relationship stays at −2.
   - **Dismiss from party** — Companion leaves. Quest content for that companion locked.
3. **If not caught** — Dark Ability continues. Companion is more careful (detection DCs increase by +2).

---

## ⚠️ DM RULES

1. **Dark Abilities are storytelling tools, not punishment.** They exist to make hostile relationships feel consequential and give the player a reason to manage relationships.
2. **Never stack Dark Abilities.** If multiple companions are at −2, only activate 2 maximum per session. Choose the most dramatically relevant.
3. **Devoted Passives fire automatically.** Do not ask the player. Narrate the companion acting.
4. **Track in save block per companion:** `"influence_ability": "none" | "devoted_passive" | "dark_ability"`

---

*KM_Influence.md — Kingmaker PF2e Text Adventure | Influence-Gated Companion Abilities v1.0*
*Inspired by NWN2 influence system. Devoted = reward. Hostile = consequence.*


---

<!-- merged from KM_Ultimatums.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION URGENCY & ULTIMATUM SYSTEM
## KM_Ultimatums.md | Referenced by: KM_Companions_Behaviors.md, KM_CompanionQuests_A–D.md

> **DM:** Load from Ch2 onward. This system adds visible urgency to companion quest deadlines and incompatibility countdowns (KM_Companions_Behaviors.md). The player sees behavioral cues escalate — never a number, always narrative — until the companion delivers an ultimatum. If the player ignores the ultimatum, the companion acts on their own (leaves, fights, or forces the issue).

---

## 📊 URGENCY STAGES

Each companion quest deadline and incompatibility countdown has an urgency stage tracked silently:

| Stage | Name | Behavioral Cues (DM narrates these) |
|-------|------|-------------------------------------|
| 0 | **Hidden** | No visible urgency. Companion mentions the issue casually. Normal camp behavior. |
| 1 | **Subtle** | Companion brings up the topic unprompted once per rest. Slightly distracted in combat (no mechanical effect). Eats less at camp. |
| 2 | **Visible** | Companion paces at camp. Refuses one camp activity per rest ("Not tonight"). Conversation threads circle back to the issue. Other companions notice and comment. |
| 3 | **Ultimatum** | Companion confronts the player directly. Scripted dialogue. Clear deadline stated in-character. The companion WILL act at the end of the stated deadline if the player does not. |
| 4 | **Action** | The companion acts. Departure, solo mission (may die), forced confrontation, or betrayal depending on the quest. This is NOT a bluff. |

### Escalation Timing
- **Stage 0 → 1:** Fires when the quest/countdown has consumed 50% of its time or trigger count
- **Stage 1 → 2:** Fires at 75%
- **Stage 2 → 3:** Fires at 90%
- **Stage 3 → 4:** Fires when the deadline expires or the countdown reaches max

---

## 🗣️ URGENCY DIALOGUE BY COMPANION

### Stage 1 — Subtle Mentions

| Companion | Stage 1 Line |
|-----------|-------------|
| **Amiri** | *"I've been thinking about [quest topic]. Don't worry about it."* (She's worrying about it.) |
| **Linzi** | *"I should write about [quest topic] before I forget the details."* (She hasn't forgotten.) |
| **Tristian** | *"I prayed about [quest topic] last night. I didn't get an answer."* (He's afraid of the answer.) |
| **Jaethal** | *"Time means less to me than to you. But even I notice it passing."* |
| **Valerie** | *"There's something I need to handle. When you have a moment."* (She won't ask twice at this stage.) |
| **Regongar** | *"We should do that thing. The thing I mentioned. Soon."* |
| **Harrim** | *"Delay is just slow refusal. I should know — I've practiced both."* |
| **Ekundayo** | Says nothing. Sharpens arrows more than usual. Dog watches the road. |
| **Nok-Nok** | *"Nok-Nok is PATIENT. Nok-Nok can wait. Nok-Nok is VERY patient."* (He cannot.) |
| **Octavia** | *"Remember when I asked about [quest topic]? I'm still asking."* |

### Stage 2 — Visible Distress

| Companion | Stage 2 Behavior |
|-----------|-----------------|
| **Amiri** | Breaks something at camp (not valuable — a stick, a clay mug). Apologizes poorly. |
| **Linzi** | Stops writing for an entire rest period. When asked: *"Some stories don't wait for the chronicler."* |
| **Tristian** | Heals less efficiently (−1 per spell rank — narrative, not mechanical yet). Prays audibly. |
| **Jaethal** | Disappears from camp for 1-2 hours. Returns without explanation. Other companions noticed. |
| **Valerie** | Armor polish becomes aggressive. Conversation is clipped. Drills alone. |
| **Regongar** | Picks a fight with another companion over nothing. Apologizes with *"I'm just — we need to go."* |

### Stage 3 — Ultimatum (Scripted Confrontation)

**Format:** Companion approaches the player at camp or during a quiet moment. Not interruptible. Other companions go quiet.

**Template:**
> **[Companion]:** *"[Personal statement about why this matters]. I have waited because I trusted you. I am telling you now: if we do not [specific action] before [deadline in narrative terms], I will [specific consequence]. This is not a threat. This is what I am going to do."*

**Player response options (always these 4):**
```
1. Agree — commit to the quest now  [Quest activates immediately]
2. Ask for more time  [Deadline extends by 1 kingdom turn — ONCE only]
3. Refuse  [Companion relationship −2, Stage 4 fires immediately]
4. Debate it  [Trigger Debate system — KM_Debates.md]
```

### Stage 4 — Action (Consequences)

| Companion | Action If Ignored |
|-----------|------------------|
| **Amiri** | Leaves the party. Goes to fight [quest target] alone. Player can find her wounded at the quest location (50% chance) or find her body (50%). |
| **Linzi** | Doesn't leave. But her chronicle becomes public — she publishes what she has, including unflattering details. Reputation −2 in capital. |
| **Tristian** | Confesses his secret early (if relevant) or departs for a pilgrimage. Returns in 2 chapters, changed. |
| **Jaethal** | Pursues her quest alone. Succeeds, but the method damages the party's reputation. Crime system: +1 Infamy. |
| **Valerie** | Returns to the Order. Gone permanently unless player pursues within 1 kingdom turn. |
| **Regongar** | Violent outburst at camp. Combat may trigger (Regongar vs. player, nonlethal). Resolved: he apologizes and relationship resets to −1. Unresolved: he leaves with Octavia. |

---

## 📋 INCOMPATIBILITY COUNTDOWN INTEGRATION

The existing Incompatibility Countdown system (KM_Companions_Behaviors.md) already tracks count/max/stage. This file adds the VISIBLE LAYER:

- **Countdown at 50%:** Stage 1 urgency for BOTH companions in the pair
- **Countdown at 75%:** Stage 2 urgency for both
- **Countdown at 90%:** Stage 3 — but for incompatibility, BOTH companions deliver ultimatums. Player must choose a side or mediate (Debate system).
- **Countdown at max:** Stage 4 — the incompatibility resolves violently or with departure. See KM_Companions_Behaviors.md § System 3 for outcomes.

---

---

## 🗣️ STAGE 3 — FULL ULTIMATUM SCRIPTS

### Amiri — "The Sword Asks"
> *"I came here because I thought you were someone who does things. Not plans things. Not schedules things. Does them. My sword has been on my back for [X] days and the thing I came to do is still undone. I am telling you: before the next moon, we go. Or I go alone. I've done alone before. I'm good at it."*

### Linzi — "The Unfinished Chapter"
> *"I've been patient. I've been so patient you probably forgot I asked. But the story I came to write — the one I told you mattered — it's slipping away. The details are fading. The people involved are moving on. If we don't go now, there won't be a story. There'll be a footnote. I don't write footnotes."*

### Valerie — "The Order's Shadow"
> *"I asked you once. I explained what was at stake. You said 'soon.' That was [X] days ago. The Order is not waiting. They are deciding without me. If I am not there to answer for myself, they will answer for me. And their answer will be permanent."*

### Harrim — "The Grave Won't Wait"
> *"I told you about the graves. I told you what I needed to see before the end. You nodded. That was kind. But kindness without action is just the sound of someone being polite while the world closes. The graves are being disturbed. The dead don't wait for the living to be ready."*

### Tristian — "The Light Fades"
> *"I have tried not to burden you with this. But the truth I carry — the thing I did — it is not getting lighter with time. It is getting heavier. Every day I don't confess, every day I don't make right what I made wrong, I become more of what I was trying to stop being. Please. Before I can't come back from it."*

### Jaethal — "The Dead Don't Bargain"
> *"I have been more patient than any living person would credit. I have waited because you asked. But what I seek is not patient. It decays. It fades. The dead do not hold their shape forever — even the ones who want to. If we do not go before the season turns, there will be nothing left to find."*

### Octavia — "The Network Burns"
> *"The people I'm trying to help don't have the luxury of your schedule. Every week we delay, someone else is sold. Someone else disappears. I know the kingdom matters. I know your war matters. But this is MY war, and I've been waiting for you to notice it's on fire."*

### Nok-Nok — "Nok-Nok Is Not Patient"
> *"Nok-Nok has been VERY patient. VERY VERY patient. Nok-Nok waited like you said. But the thing Nok-Nok needs to do? It is not waiting. It is HAPPENING. And if Nok-Nok does not go NOW, the thing Nok-Nok was trying to prove — that Nok-Nok is more than what the tribe said — that proof goes away. And then Nok-Nok is just... Nok-Nok. Please."*

### Ekundayo — "The Trail Goes Cold"
> He doesn't say much. He puts his bow on the table in front of you. Looks at it. Looks at you.
> *"The trail. It's going cold. Another week and I lose them forever. I am asking — not demanding. I don't demand. But I am telling you that if we don't move, I will. And I would rather move with you than without you."*

---

## 💀 STAGE 4 — FULL CONSEQUENCE TABLE

| Companion | Stage 4 Action | Recovery Possible? |
|-----------|---------------|-------------------|
| **Amiri** | Leaves. Goes to fight alone. 50% found wounded at quest site, 50% found dead. | If wounded: recruitable at quest site. If dead: permanent. |
| **Linzi** | Publishes incomplete chronicle with unflattering details. Rep −2. Stays in party but relationship locked at −1. | Relationship unlocks after player completes a quest she cares about. |
| **Valerie** | Returns to the Order. Gone 2 chapters. Returns changed — colder, more formal. Relationship resets to 0. | Can rebuild, but she never fully trusts the player's timing again. |
| **Harrim** | Goes to the graves alone. Returns 1 chapter later having found what he needed — but without the player's help, the meaning is diminished. Quest = incomplete. | No recovery for the quest. Relationship −1 permanent. |
| **Tristian** | Confesses publicly at the worst possible moment (mid-diplomatic scene or mid-combat). Chaos. | Forgiveness path still available but the damage is done — Loyalty −2, public trust shaken. |
| **Jaethal** | Pursues her quest alone. Succeeds via dark methods. Crime system: +2 Infamy. Returns with what she wanted but won't explain how. | She's back. But something is different. Companion mood: permanently Withdrawn unless directly addressed. |
| **Octavia** | Leaves with Regongar (if both in party) or alone. Gone 1 chapter. Returns having freed people — but burned bridges with a faction the player needed. Faction −2. | Recruitable when she returns. Relationship −1 but she doesn't regret it. |
| **Regongar** | Violent outburst. Attacks the nearest object (wall, table, training dummy). If no outlet: attacks a companion. Nonlethal but frightening. | Apologizes within 1 day. Relationship −1 but self-aware about it. If he hurt a companion: THAT companion's relationship with Regongar −2. |
| **Nok-Nok** | Disappears. Literally. Gone from camp one morning. Found 1d4 sessions later in an absurd situation (trapped in a cave, accidentally king of a goblin village, hiding in a barrel). | Always recoverable. Nok-Nok cannot permanently leave — he just gets lost in increasingly ridiculous ways. |
| **Ekundayo** | Leaves silently. His dog stays. Ekundayo is found 1 chapter later having tracked his target alone — succeeded but badly wounded. Dog led the party to him. | Recruitable. Dog never left the party. Ekundayo: "He knew where I'd be." Relationship −1 but +1 with the dog. |

---

## ⚠️ DM RULES

1. **Never show numbers.** The player sees behavior, not stages.
2. **Stage 3 is a real scene.** Block 2-3 minutes. Don't rush it.
3. **Stage 4 is irreversible** unless noted otherwise. Consequences are real.
4. **Track:** `"urgency_stage": 0` per companion quest/countdown.
5. **Max 2 active urgencies at Stage 2+** per session. Queue others.

---

*KM_Ultimatums.md — Kingmaker PF2e Text Adventure | Companion Urgency & Ultimatum System v2.0*
*Full scripts for all 10 companions. Inspired by BG2 departure timers.*


---

<!-- merged from KM_Dreams.md (v93.21 file consolidation) -->

# KINGMAKER — DREAM SEQUENCE SYSTEM
## KM_Dreams.md | Active from: Chapter 1 | Referenced by: KM_Kingdom.md, KM_DMRules.md

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

**This dream has no choice menu.** The player responds naturally. DM voices Nyrissa based on KM_NPCs.md profile. The conversation is the reward. At the end: `nyrissa_saveable +1`, `true_ending_flags +1`.

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

### CD-5 — VALERIE: THE OATH
**Trigger:** Valerie at Devoted. After receiving her title.
> *A duelist's circle. Valerie stands across from you, blade lowered, not in challenge. She speaks an Aldori oath you don't know — but you understand every word. When she sheathes the sword, the cut on her face from a fight three sessions ago is gone.*

No choice. Valerie gains permanent +1 to saves while in the player's party. +1 Bond Moment.

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
If shared with Valerie: she says nothing. She nods once. +1 relationship.

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


---

<!-- merged from KM_Liminal.md (v93.21 file consolidation) -->

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


---

<!-- merged from KM_ScriptedInteractions.md (v93.21 file consolidation) -->

# KINGMAKER — SCRIPTED INTERACTIONS
## KM_ScriptedInteractions.md | Referenced by: KM_Exploration.md, KM_Ch1–4.md

> **DM:** Scripted Interactions are multi-step choose-your-own-adventure vignettes triggered during exploration. Unlike normal scenes, they are self-contained — 3-5 decision points, each gated by different skills, companions present, or player resources. They handle non-combat encounters: crossing a bridge, negotiating with a spirit, navigating a trapped corridor. Present as text with numbered choices at each node.

---

## 📋 SCRIPTED INTERACTION FORMAT

```
═══════════════════════════════════════
SCRIPTED INTERACTION — {Title}
═══════════════════════════════════════
{Opening description — 2-3 sentences}

NODE 1:
 1. {Option — skill gated}  [Skill DC X]
 2. {Option — companion gated}  [Requires: {Companion}]
 3. {Option — resource gated}  [Costs: {item/gold/spell}]
 4. {Option — universal}  [No requirement]

→ Each option leads to NODE 2a, 2b, 2c, or 2d
═══════════════════════════════════════
```

### Rules
1. **3-5 nodes per interaction.** Not longer — these are vignettes, not dungeons.
2. **Every node has 3-4 options.** At least 1 universal (no requirement).
3. **Companion-gated options** require that companion in the active party AND at relationship Friendly+.
4. **Skill-gated options** use the standard PF2e check. Show the roll.
5. **Failure is not death.** Failed checks lead to harder paths or reduced rewards, not game over.
6. **XP at the end.** Award encounter XP based on the highest DC overcome.

---

## 🌉 SI-1: THE BROKEN BRIDGE (Ch1-2, Exploration)

**Trigger:** Party reaches a river crossing where the bridge has collapsed.

```
The bridge over the Shrike River is down — half the span
hangs into the water, timbers split and swollen. The river
runs fast here. Crossing on foot means waist-deep current.
The far bank has what you came for.

NODE 1 — THE CROSSING:
 1. Swim across  [Athletics DC 14] — Brute force
 2. Find another crossing point  [Survival DC 12] — Takes 4 hours extra
 3. Repair the bridge  [Crafting DC 16 + 2 hours + Lumber ×1] — Permanent fix
 4. Send a companion to scout  [Requires: Ranger or Rogue in party]
```

**Node 1 Results:**
- **Swim (Success):** Across but Wet condition. Equipment check: 10% chance one item soaked (DM rolls).
- **Swim (Failure):** Swept downstream. Takes 1d6 bludgeoning, washes up 1 hex south. Must backtrack.
- **Find crossing (Success):** Shallow ford found. Safe crossing, no penalties. +1 Scholarly.
- **Repair bridge:** Bridge permanently fixed. Future crossings instant. Kingdom map updated. +1 to trade routes using this hex.
- **Scout:** Companion finds a fallen tree crossing 200 ft upstream. DC 10 Acrobatics to cross. Safe.

```
NODE 2 — THE FAR BANK:
 1. Examine the ruins  [Perception DC 14]
 2. Search for tracks  [Survival DC 12]
 3. Set up camp and observe  [2 hours, auto-success]
 4. Push forward immediately  [No check]
```

**Node 2 Results:**
- **Examine ruins (Success):** Find carved rune. Recall Knowledge (Arcana DC 16) identifies it as a ward marker. +10 XP (Minor milestone).
- **Tracks (Success):** Recent humanoid tracks — bandits passed 1 day ago. Direction learned.
- **Camp and observe:** See smoke from a camp 2 hexes away. Intelligence: learn enemy count (3-5).
- **Push forward:** No information gathered. Normal exploration continues.

```
NODE 3 — THE CAMPFIRE (only if Node 2 revealed camp):
 1. Approach openly  [Diplomacy DC 14]
 2. Sneak closer  [Stealth DC 16]
 3. Circle around and ambush  [Stealth DC 14 + Survival DC 12]
 4. Ignore and continue  [No check]
```

**XP Award:** 60 XP (moderate encounter equivalent).

---

## 🗿 SI-2: THE STONE GUARDIAN (Ch2-3, Dungeon Entrance)

**Trigger:** Party finds a sealed tomb/ruin entrance with a stone construct blocking the door.

```
A figure carved from granite stands before the entrance.
Its eyes are empty but oriented toward you. A voice — not
from the stone, from the air around it — speaks in Hallit:

"Name the three rivers that feed the Stolen Lands."

NODE 1 — THE RIDDLE:
 1. Answer correctly  [Recall Knowledge: Geography DC 14]
 2. Bluff an answer  [Deception DC 18]
 3. Search for the answer carved nearby  [Perception DC 12]
 4. Attack the guardian  [Combat: Stone Golem level 6]

NODE 2 — (if riddle passed):
"Name the king who lost these lands."
 1. Answer correctly  [Recall Knowledge: History DC 16]
 2. "There is no king. I am the ruler now."  [Intimidation DC 16]
 3. Ask Linzi  [Requires: Linzi in party, auto-success — she knows]
 4. Examine the guardian for clues  [Perception DC 14]

NODE 3 — (if both riddles passed):
The guardian steps aside. The door opens.
"You may pass. But what you seek inside will ask
harder questions than I did."
 → Dungeon entrance unlocked. +30 XP (Moderate milestone). +1 Scholarly.

(If combat chosen at any point: guardian fights.
Victory opens the door but no riddle XP.)
```

---

## 🌿 SI-3: THE FEY NEGOTIATION (Ch3+, Exploration near First World thin spots)

**Trigger:** Party enters a hex with active fey presence (Nyrissa connection).

```
A circle of mushrooms. Inside: a satyr sitting on a
stump, drinking from a cup that refills itself. He sees
you and grins. "Ah. The mortal who thinks they own the
Stolen Lands. How delightful. Sit."

NODE 1 — THE OFFER:
"I can tell you something about the woman in the garden.
The one who plants roses that eat worlds. But I require
payment. Not gold. Something interesting."
 1. Offer a story  [Performance DC 14 — satyrs love entertainment]
 2. Offer a secret  [Player must reveal a genuine secret from their backstory]
 3. Offer a drink from your supplies  [Requires: wine, mead, or specialty alcohol]
 4. Refuse to bargain with fey  [No check — satyr shrugs, disappears]

NODE 2 — THE INFORMATION (if payment accepted):
The satyr tells you ONE thing about Nyrissa (DM selects
based on current nyrissa_backstory_known level):
 - Known 0: "She was not always what she is. Someone made her this way."
 - Known 1: "The Lantern King took something from her. Not her power. Worse."
 - Known 2: "She cannot love. Not 'will not.' Cannot. The capacity was cut from her like a limb."
 - Known 3: "The piece he cut still exists. Somewhere in the First World. She's been looking for a thousand years."

nyrissa_backstory_known +1. +30 XP (Moderate milestone).

NODE 3 — THE PARTING GIFT:
"One more thing, free of charge."
The satyr tosses you a seed.
 1. Catch it  [Free item: Fey Seed — plant in kingdom hex for +1 Culture]
 2. Let it fall  [Seed grows into a mushroom circle on the spot — mark on map]
 3. Crush it  [+1 Ruthless. Satyr: "Interesting." Disappears faster.]
```

---

## 🏚️ SI-4: THE ABANDONED MILL (Ch2, Settlement Hex)

**Trigger:** Party explores a hex with a ruined mill marked on the map.

```
A water mill, abandoned. The wheel still turns — slowly,
grinding nothing. The door hangs open. Inside: flour dust
on every surface, undisturbed. Someone left in a hurry.

NODE 1 — THE ENTRANCE:
 1. Search the main floor  [Perception DC 12]
 2. Check the millstone mechanism  [Crafting DC 14]
 3. Go upstairs to the living quarters  [No check]
 4. Examine the flour dust for tracks  [Survival DC 12]
```

**Node 1 Results:**
- **Search (Success):** Ledger under the counter. Last entry: "They come at night. Three nights now. We leave tomorrow." Date: 2 months ago.
- **Mechanism (Success):** Mill is functional. Repair would take 1 day + 2 Lumber. Could become a kingdom building (free Mill, saves 6 RP). +1 Scholarly.
- **Upstairs:** Beds overturned. Personal belongings left behind. A child's toy on the floor.
- **Tracks (Success):** Clawed prints, not animal. Humanoid but wrong. Lead to the cellar door.

```
NODE 2 — THE CELLAR (if tracks found or player investigates):
 1. Open the cellar door cautiously  [Stealth DC 14]
 2. Call down  [No check — alerts whatever is there]
 3. Barricade the door and leave  [No check — safe exit]
 4. Send a companion down  [Requires: martial companion]

NODE 3 — BELOW:
 1. Fight the mites (3 Mite Warriors, CR 1 each)  [Combat]
 2. Offer food to drive them out  [Survival DC 12]
 3. Intimidate them into fleeing  [Intimidation DC 14]
```

**Resolution:** Mill cleared. Can be claimed as kingdom building. If mites driven out peacefully: Reputation +1. Families may return (Loyalty +1 in this hex if player posts notice at capital).

**XP:** 80 XP. +1 Scholarly if ledger found.

---

## ⛏️ SI-5: THE COLLAPSED MINE (Ch2-3, Mountain/Hill Hex)

**Trigger:** Party finds a mine entrance partially blocked by rockfall.

```
The mine entrance is half-buried. Timber supports visible
but cracked. Air from inside is cold and stale. Pick marks
on the rock face are old — decades, not years.

NODE 1 — ENTRY:
 1. Clear the rubble  [Athletics DC 16, 2 hours]
 2. Find a side entrance  [Survival DC 14, 1 hour]
 3. Examine the rock face  [Recall Knowledge: Mining/Geology DC 14]
 4. Leave it  [No check]

NODE 2 — INSIDE (dark, Darkvision or light needed):
 1. Follow the main shaft  [No check — leads to NODE 3]
 2. Examine the support timbers  [Crafting DC 12]
 3. Check for ore veins  [Perception DC 14]
 4. Listen carefully  [Perception DC 16]

NODE 3 — THE DEEP CHAMBER:
 1. Investigate the glowing mineral  [Arcana DC 16]
 2. Mine it  [Athletics DC 14 + Crafting DC 14]
 3. Touch it  [Fort DC 14 — cold damage if failed]
 4. Ask Harrim about the stone  [Requires: Harrim in party — auto-success]
```

**Resolution:** Mine contains a deposit of rare mineral (Arcane Dust ×3 or Gemstones ×2). If support timbers repaired (Crafting DC 12): mine becomes kingdom resource node (+1 Ore/turn). Harrim: "This stone is older than the mountain. It was here before the rock formed around it."

**XP:** 100 XP. +1 Scholarly if mineral identified.

---

## 🌳 SI-6: THE TALKING TREE (Ch3, Deep Forest Hex)

**Trigger:** Party enters a hex with an ancient oak marked as "First World Thin Spot."

```
The tree is enormous — twenty people could not circle its trunk.
Its bark has patterns that almost look like a face. As you
approach, the patterns move. The tree is looking at you.

"You are not from here." Its voice is the sound of roots
growing through stone. "Neither am I. Sit. I have time."

NODE 1 — THE CONVERSATION:
 1. Sit and listen  [10 minutes, auto — tree shares lore]
 2. Ask about Nyrissa  [Diplomacy DC 14]
 3. Ask about the Stolen Lands' history  [No check — free lore]
 4. Ask about your armor  [The tree has never seen Aerynth material]
```

**Node 1 Results:**
- **Listen:** Tree tells a story about the First World bleeding into Golarion. nyrissa_backstory_known +1 if below 3.
- **Nyrissa (Success):** "She was planted here by something that wanted to see what would grow. The Lantern King gardens with cruelty." nyrissa_backstory_known +1.
- **History:** The Stolen Lands were a fey border march. The "theft" was mortals building where the fey had not finished building.
- **Armor:** The tree goes still. "I have seen wood from ten thousand forests and metal from every mountain. I have not seen this. Where did you come from?" No answer satisfies the tree. It remembers the question.

```
NODE 2 — THE REQUEST:
"Something is wrong with my roots. The Bloom — it poisons
the deep water. I cannot move. I cannot fight. Will you
go to the spring, three hills east, and cleanse it?"

 1. Accept the quest  [Side quest added: Cleanse the Spring]
 2. Ask what's in it for you  [Diplomacy DC 12]
 3. Offer to try right here  [Nature DC 18 — partial fix only]
 4. Decline  [Tree understands — "Mortals have their own roots to tend."]
```

**Resolution:** Quest "Cleanse the Spring" added if accepted. Completing it later: tree grants a gift (Bonewood Staff — +1 Nature, +1 to healing spells in forests). If declined: tree is fine with it. Can return later and accept.

**XP:** 60 XP (conversation) + 120 XP (quest completion).

---

## 🏰 SI-7: THE RUINED WATCHTOWER (Ch3-4, Border Hex)

**Trigger:** Party explores hex containing a crumbling stone watchtower.

```
Four floors. The top two are open to the sky. The first floor
is intact but the door is barred from inside. Something scratched
"LEAVE" into the stone above the lintel. The scratching is recent.

NODE 1 — APPROACH:
 1. Call out  [No check — whoever is inside hears]
 2. Break down the door  [Athletics DC 16]
 3. Climb to the second floor  [Athletics DC 14]
 4. Circle the tower for another entrance  [Perception DC 12]

NODE 2 — INSIDE:
 A deserter from Pitax's army. Armed, scared, alone. He fled
 rather than participate in Irovetti's plans. He has intelligence.

 1. Reassure him — you're not Pitax  [Diplomacy DC 12]
 2. Threaten him out  [Intimidation DC 14]
 3. Offer asylum in your kingdom  [No check — automatic]
 4. Ask Valerie to talk to him  [Requires: Valerie — soldier to soldier]

NODE 3 — THE INTELLIGENCE:
 1. Ask about Pitax army strength  [He knows: 3 units, positions, general]
 2. Ask about Irovetti's plan  [He knows: timeline, invasion route]
 3. Ask about other deserters  [He knows: 4 more hiding in the Narlmarches]
 4. Ask all three  [Takes 2 hours, all intelligence gained]
```

**Resolution:** Full Pitax army intelligence if all questions asked (+2 to next army engagement). If asylum offered: deserter becomes minor NPC at capital (potential Spymaster agent). If other deserters found: 4 additional recruits (1 free militia unit).

**XP:** 80 XP. +1 Cunning if intelligence extracted. +1 Merciful if asylum granted.

---

## 💀 SI-8: THE BONE CAIRN (Ch4, Kamelands Hex)

**Trigger:** Party discovers a burial mound with recent disturbance.

```
Stones stacked in the old Kellid way. But the earth around
the base is freshly turned. Something dug in — or out.
The air smells of wet soil and something older.

NODE 1:
 1. Examine the disturbance  [Perception DC 14]
 2. Check for undead presence  [Religion DC 14]
 3. Dig  [Athletics DC 12, 1 hour]
 4. Leave it undisturbed  [No check — respectful exit]

NODE 2 — THE BURIAL CHAMBER:
 1. Examine the sarcophagus  [Perception DC 16]
 2. Read the Kellid inscriptions  [Society DC 14 or Linguistics DC 12]
 3. Open the sarcophagus  [Athletics DC 14 — releases occupant]
 4. Ask Harrim about the runes  [Requires: Harrim — auto-read, provides context]

NODE 3 — THE REVENANT:
 Not hostile. Not yet. A Kellid warrior, dead 200 years,
 disturbed by the Bloom's corruption of the earth. He asks
 one question: "Is my line ended?"
 1. Answer honestly  [Research or Recall Knowledge DC 16]
 2. Lie — "Your descendants live"  [Deception DC 18]
 3. Offer to find out  [Side quest: research Kellid genealogy]
 4. Destroy the undead  [Combat: Revenant CR 6]
```

**Resolution:** If answered truthfully or quest completed: Revenant rests peacefully. Grave goods: ancient Kellid weapon (+1 cold iron greataxe, historical significance). If lied to and caught (Revenant has +8 Perception): combat. If destroyed: weapon drops but Kellid faction −1. +1 Scholarly if inscriptions read. +1 Merciful if revenant laid to rest peacefully.

**XP:** 120 XP.

---

## ⚠️ DM RULES

1. **Scripted Interactions are self-contained.** Start to finish in one scene. No saving mid-interaction.
2. **Show all rolls.** Even in a narrative vignette, the dice are visible.
3. **Companion-gated options should feel valuable.** The player should think "I'm glad I brought Linzi."
4. **Create new ones for chapter-specific content.** This file provides the template and 8 examples. Chapter files can reference additional interactions using this format.
5. **1-2 per exploration session.** Don't overuse. These are special encounters, not the default.

**Save block:** `"scripted_interactions_completed": ["SI-1", "SI-3"]`

---

*KM_ScriptedInteractions.md — Kingmaker PF2e Text Adventure | Scripted Interactions v1.0*
*Inspired by Pillars of Eternity scripted interactions.*


---

<!-- merged from KM_Crafting.md (v93.21 file consolidation) -->

# KINGMAKER — CRAFTING SYSTEM
## KM_Crafting.md | Active from: Chapter 1 | Referenced by: KM_Actions.md, KM_Kingdom.md

> **DM:** Recipes are found as loot during exploration (on bodies, in chests, purchased from merchants, or discovered via `.examine`). The player crafts items during Downtime using materials + a Crafting check. Recipes are permanent once learned. Materials are consumable. The Mobile Base (KM_MobileBase.md) provides a crafting bench bonus when available.

---

## 📋 COMMANDS

`.craft` — Display known recipes, available materials, and start a crafting attempt.
`.recipes` — List all known recipes with material requirements.

---

## 📊 CRAFTING PROCEDURE

### Step 1 — Choose a Recipe
Player selects from known recipes (`.recipes`).

### Step 2 — Check Materials
Recipe lists required materials. Player must have all in inventory.

### Step 3 — Crafting Check
```
Roll: d20 + Crafting modifier vs Recipe DC
Crit Success: Item crafted + bonus property (DM generates — extra charge, improved quality)
Success:      Item crafted as described
Failure:      Materials consumed, item not created. 50% of material cost refunded as scrap.
Crit Failure: Materials consumed, item not created. Crafting mishap: 1d6 fire/acid damage.
```

### Step 4 — Time Cost
- **Simple recipes:** 1 Downtime day
- **Moderate recipes:** 2 Downtime days
- **Complex recipes:** 4 Downtime days
- **Crafting bench bonus** (Mobile Base upgrade): −1 day (min 1)

---

## 📦 MATERIAL TYPES

| Material | Found In | Common Sources |
|----------|---------|---------------|
| **Iron Ore** | Mining hexes, cave loot | Purchased from smiths (2 gp) |
| **Rare Wood** | Forest hexes, lumber camps | Old Sycamore, Narlmarches |
| **Monster Parts** | Combat loot (beasts, magical creatures) | Troll blood, wyvern scales, dire bear hide |
| **Alchemical Reagents** | Purchased, found in labs, herb gathering | Bokken, Jubilost, apothecaries |
| **Arcane Dust** | Disenchanting magic items, magical locations | Spell-touched ruins, ley line hexes |
| **Rare Herbs** | Herb gathering (Nature DC 14), specific hexes | Fangberry bushes, moon radish patches |
| **Gemstones** | Mining, treasure hoards, purchased | Diamond, ruby, sapphire (for enchantments) |
| **Exotic Hide** | Combat loot (specific creatures) | Wyrmskin, troll hide, basilisk scales |

---

## 📜 RECIPE LIST

### WEAPONS — TIER 1 (Ch1-2, Crafting DC 14-16)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Cold Iron Blade** | Iron Ore ×3 | 16 | 2 days | Cold Iron weapon (bypass DR/cold iron) |
| **Flaming Weapon Oil** | Alchemical Reagents ×2, Arcane Dust ×1 | 18 | 1 day | Apply: +1d6 fire for 1 hour |
| **Troll-Bane Arrow (×10)** | Iron Ore ×1, Alchemical Reagents ×1 | 14 | 1 day | Acid-coated, prevent troll regen 1 round |
| **Silversheen Coating** | Iron Ore ×1, Gemstones ×1 | 16 | 1 day | Apply: counts as silver for 1 hour |
| **Weighted Throwing Hammer (×3)** | Iron Ore ×2 | 14 | 1 day | Returning thrown weapon, 1d6+Str B, range 20 ft |

### WEAPONS — TIER 2 (Ch3-4, Crafting DC 18-20)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Wyvern Venom Blade** | Monster Parts (wyvern) ×2, Alchemical Reagents ×1 | 20 | 2 days | Poison: Fort DC 18 or Enfeebled 1 + Clumsy 1 |
| **Frost-Forged Weapon** | Iron Ore ×2, Rare Herbs ×1, Arcane Dust ×1 | 18 | 2 days | +1d6 cold. Creatures hit: Slowed 1 on crit |
| **Giant-Bane Oil** | Monster Parts (giant) ×2, Alchemical Reagents ×2 | 18 | 1 day | Apply: +2d6 damage vs Large+ creatures, 1 hour |
| **Thunderstone Arrow (×5)** | Iron Ore ×1, Arcane Dust ×1, Gemstones ×1 | 18 | 1 day | On hit: Fort DC 18 or Deafened 1 round + 1d6 sonic |
| **Barbed Net** | Iron Ore ×1, Exotic Hide ×1 | 16 | 1 day | Thrown: Immobilized (Escape DC 18), 1d4 piercing/round |

### WEAPONS — TIER 3 (Ch5+, Crafting DC 22+)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Bloom-Warded Blade** | Arcane Dust ×3, Rare Herbs ×2, Gemstones ×1 | 22 | 4 days | +2d6 vs fey/Bloom creatures. Immune to Bloom weapon corrosion |
| **Siege Bolt (×3)** | Iron Ore ×3, Alchemical Reagents ×2 | 20 | 2 days | Crossbow bolt that deals damage to structures/walls (2d12 to objects) |
| **Vorpal Oil** | Arcane Dust ×4, Gemstones ×2, Monster Parts ×2 | 24 | 4 days | Apply: on nat 20, Fort DC 22 or decapitated (kill). 1 use. |

### ARMOR & SHIELDS (Crafting DC 16-22)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Reinforced Shield** | Iron Ore ×2, Rare Wood ×1 | 18 | 2 days | Shield Hardness +2 |
| **Fire-Resistant Cloak** | Exotic Hide ×1, Alchemical Reagents ×1 | 16 | 1 day | Fire Resistance 5 for 1 day |
| **Troll-Hide Armor Patch** | Monster Parts (troll) ×2 | 18 | 2 days | Fast Healing 1 (wearer) for 1 combat/day |
| **Spell-Deflecting Buckler** | Iron Ore ×2, Arcane Dust ×2 | 20 | 3 days | Shield Block absorbs spell damage (not just physical) |
| **Camouflage Cloak** | Exotic Hide ×2, Rare Herbs ×1 | 16 | 2 days | +2 Stealth in wilderness hexes. Advantage on ambush checks |
| **Bloom-Ward Armor Oil** | Alchemical Reagents ×3, Rare Herbs ×2 | 22 | 2 days | Apply: Resist 5 to Bloom damage for 1 day |

### CONSUMABLES — TIER 1 (Ch1-2, Crafting DC 12-16)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Healing Salve (×3)** | Rare Herbs ×2 | 12 | 1 day | Heal 2d8+4 HP (applied, not spell) |
| **Antidote (×3)** | Rare Herbs ×1, Alchemical Reagents ×1 | 14 | 1 day | Counteract poison (counteract +10) |
| **Blast Bomb** | Alchemical Reagents ×3 | 16 | 1 day | Thrown: 4d6 fire, 10-ft burst, Ref DC 16 half |
| **Smoke Bomb (×3)** | Alchemical Reagents ×1 | 12 | 1 day | 10-ft concealment cloud, 3 rounds |
| **Darkvision Elixir** | Rare Herbs ×1, Arcane Dust ×1 | 14 | 1 day | Darkvision 1 hour |
| **Alchemist's Kindness (×5)** | Rare Herbs ×1 | 12 | 1 day | Remove Sickened, nausea, hangover. Popular at feasts |
| **Tanglefoot Bag (×3)** | Alchemical Reagents ×2 | 14 | 1 day | Thrown: Immobilized 1 round, Ref DC 14 half |

### CONSUMABLES — TIER 2 (Ch3-4, Crafting DC 16-20)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Greater Healing Salve (×3)** | Rare Herbs ×3, Alchemical Reagents ×1 | 18 | 2 days | Heal 4d8+8 HP |
| **Elixir of Life** | Rare Herbs ×2, Gemstones ×1, Arcane Dust ×1 | 20 | 2 days | Heal 5d8+12 HP + remove 1 condition |
| **Frost Bomb** | Alchemical Reagents ×3, Rare Herbs ×1 | 18 | 1 day | Thrown: 4d6 cold, 10-ft burst, Slowed 1 on fail |
| **Invisibility Potion** | Arcane Dust ×2, Alchemical Reagents ×1 | 18 | 2 days | Invisible 10 min (breaks on attack) |
| **Thunderstone (×3)** | Iron Ore ×1, Alchemical Reagents ×2 | 16 | 1 day | 15-ft burst: Fort DC 16 or Deafened + Stunned 1 |

### CONSUMABLES — TIER 3 (Ch5+, Crafting DC 20+)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Breath of Life Scroll** | Arcane Dust ×4, Gemstones ×2 | 24 | 4 days | As Breath of Life spell (reaction, prevent death) |
| **War Paint of the Kellid** | Monster Parts ×2, Rare Herbs ×2 | 20 | 2 days | +2 Intimidation, +1 attack for 1 combat. Kellid tradition |
| **Philosopher's Stone Fragment** | Gemstones ×4, Arcane Dust ×3 | 26 | 4 days | Convert 1 base metal item to gold equivalent (100 gp value) |

### UTILITY (Crafting DC 14-22)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Trap Kit** | Iron Ore ×1, Rare Wood ×1 | 14 | 1 day | 2d6 piercing, DC 16 Perception/Ref |
| **Signal Arrow (×5)** | Rare Wood ×1 | 12 | 1 day | Visible flare 500 ft. Army signals |
| **Feather Token (Tree)** | Rare Wood ×1, Arcane Dust ×2 | 18 | 2 days | Instant tree. Cover, climbing, bridge |
| **Expedition Tent** | Exotic Hide ×2, Rare Wood ×1 | 16 | 4 days | +2 to camp Survival checks |
| **Hex Ward Marker** | Arcane Dust ×2, Gemstones ×1 | 20 | 4 days | −25% random encounter rate in hex, permanent |
| **Portable Bridge** | Rare Wood ×3, Iron Ore ×2 | 18 | 4 days | Spans 30-ft gap. Reusable. 500 lb capacity |
| **Underwater Breathing Helm** | Iron Ore ×2, Arcane Dust ×2 | 20 | 3 days | Breathe underwater 8 hours. Reusable |
| **Compass of True North** | Iron Ore ×1, Gemstones ×1, Arcane Dust ×1 | 16 | 2 days | Never get lost. Navigation Survival DCs: auto-pass |
| **Kingdom Banner** | Rare Wood ×1, Exotic Hide ×1 | 14 | 2 days | Plant in hex: kingdom claim visible. Army Morale +1 if visible during battle |

---

## 📋 RECIPE DISCOVERY

Recipes are NOT automatically known. They must be found:

| Source | How |
|--------|-----|
| **Loot** | Found on bodies, in chests, or in dungeon rooms. DM adds to treasure as appropriate. |
| **Merchants** | Purchased from specialist vendors. Bokken sells alchemical recipes. Smiths sell weapon recipes. |
| **Examination** | Using `.examine` on a crafting bench, smith's tools, or alchemical lab may reveal a recipe (Perception DC 14). |
| **Companion gift** | At Devoted relationship, some companions share a personal recipe (Jubilost: Blast Bomb, Octavia: Darkvision Elixir). |
| **Kingdom event** | Some stronghold events (KM_Kingdom.md) reward recipes. |
| **Quest reward** | Side quests may award unique recipes not available elsewhere. |

---

## ⚠️ DM RULES

1. **Don't flood recipes.** 1-2 per chapter is the right pace. The player should feel each discovery.
2. **Materials are loot.** Add them to treasure tables alongside gold and gear. 1-2 materials per significant encounter.
3. **Crafting is Downtime.** Cannot craft during travel, combat, or active scenes. Requires camp or settlement.
4. **Companion assist:** If a companion has Crafting proficiency, they can Aid (+1 to +4 based on proficiency).
5. **No infinite loops.** Crafted items cannot be disenchanted for more materials than they cost.

**Save block:** `"crafting": { "known_recipes": ["healing_salve", "cold_iron_blade"], "materials": {"iron_ore": 3, "rare_herbs": 2}, "crafting_queue": [] }`

---

*KM_Crafting.md — Kingmaker PF2e Text Adventure | Crafting System v1.0*
*Inspired by NWN2 crafting bench system. Recipes found, not known.*


---

<!-- merged from KM_DungeonPuzzles.md (v93.21 file consolidation) -->

# KINGMAKER — MULTI-ROOM DUNGEON PUZZLES
## KM_DungeonPuzzles.md | Referenced by: KM_Ch1.md-KM_Ch7.md, KM_Game_Subsystems.md

> **DM:** These are multi-room puzzles that span 3+ connected rooms. The player must track information across rooms (rune sequences, lever states, key fragments). Use the ASCII map to show room connections and puzzle state. Standard puzzle rules apply (KM_Game_Subsystems.md): player solves, not skill checks. One hint per puzzle. Skill check bypass after 3 failed attempts.

---

## 🗺️ DUNGEON PUZZLE 1: THE RUNE GATE (Ch2, Old Sycamore Deep)

**Setup:** 4 rooms connected in a square. Central locked door requires 4 runes activated in correct sequence.

```
MAP:
  [A]———[B]
   |     |
  [D]———[C]
      ↓
   [GATE]
```

**Room A — The Scholar's Chamber:**
- Wall inscription: "First comes the star that guides / Then the wave that carries"
- Rune pedestal with STAR symbol. Pressing it: pedestal glows blue. Records: Rune 1 = STAR.
- Bookshelf: `.examine bookshelf` reveals faded text: "The order is written in the walls, not the books."

**Room B — The Warrior's Chamber:**
- Wall inscription: "Third stands the mountain, unmoved / Last falls the flame, consuming what remains"
- Rune pedestal with FLAME symbol. If pressed now: electric shock (2d6 lightning). Must be pressed FOURTH.
- Weapon rack: `.examine weapons` — ornamental, not real. Maker's mark matches Room A books.

**Room C — The Priest's Chamber:**
- Rune pedestal with MOUNTAIN symbol. Must be pressed THIRD.
- Altar: `.examine altar` — offerings of stone chips. Recall Knowledge (Religion DC 14): "Mountain before flame — the order of creation in Sarkorian theology."

**Room D — The Thief's Chamber:**
- Rune pedestal with WAVE symbol. Must be pressed SECOND.
- Hidden panel (Perception DC 16): Contains the sequence written plainly: ★ 🌊 ⛰️ 🔥

**Solution:** Press pedestals in order: A (Star) → D (Wave) → C (Mountain) → B (Flame)

**Correct:** Central GATE opens. +30 XP (Moderate milestone). +1 Scholarly disposition.
**Wrong order:** All pedestals reset. 1d6 force damage to player. "The runes reject your offering."
**Skill bypass (after 3 failures):** Recall Knowledge (Arcana DC 18) — DM reveals the sequence.

---

## 🗺️ DUNGEON PUZZLE 2: THE PRESSURE PLATE MAZE (Ch3, Ancient Tomb)

**Setup:** A 5×5 grid room. Some tiles are pressure plates. Walking on the wrong plate = dart trap (2d4 piercing). The safe path is encoded on a mosaic in the previous room.

```
MAP:
  [ENTRY] → [MOSAIC ROOM] → [GRID ROOM] → [TREASURE]

GRID ROOM (5×5):
  [ ][ ][ ][ ][ ]   ← Row 1 (far wall)
  [ ][ ][ ][ ][ ]   ← Row 2
  [ ][ ][ ][ ][ ]   ← Row 3
  [ ][ ][ ][ ][ ]   ← Row 4
  [E][ ][ ][ ][ ]   ← Row 5 (entry side)

  E = Entry point (bottom-left)
  T = Target (top-right, Row 1 Col 5)
```

**Mosaic Room:**
A floor mosaic shows a serpent winding through a grid. The serpent's path = safe tiles.
- `.examine mosaic` — DM describes the serpent's path clearly
- The path: E(5,1) → (4,1) → (4,2) → (3,2) → (3,3) → (2,3) → (2,4) → (1,4) → (1,5) = T

**Grid Room:**
- Player states which tile they step on: "I move to row 4, column 1"
- **Safe tile:** DM narrates: "The stone holds. No sound."
- **Trap tile:** Dart trap: 2d4 piercing, Ref DC 14 half. Player returns to last safe tile.
- **Companion warning:** If a companion with Perception +8 or higher is present, they shout a warning on the FIRST trap tile only ("STOP!"). Free retry. Not subsequent traps.

**Solution:** Follow the serpent path exactly.
**Alternative:** Fly over (if available). Acrobatics DC 20 to jump tile-to-tile (3 checks, 1 per row traversed).
**Brute force:** Take the traps. Max 4 trap tiles on a random path. 8d4 piercing total (expensive but survivable).

---

## 🗺️ DUNGEON PUZZLE 3: THE ELEMENTAL LOCKS (Ch4, Armag's Tomb Antechamber)

**Setup:** 3 rooms, each with an elemental lock. All 3 must be solved to open the inner tomb. Locks can be solved in any order. Each lock requires combining two elements using the Surface Combo system (KM_Combat_Systems.md).

```
MAP:
  [FIRE LOCK]  [WATER LOCK]  [EARTH LOCK]
       \           |           /
        \          |          /
         [INNER TOMB DOOR]
```

**Fire Lock Room:**
- A frozen brazier. The fire is encased in ice. Mundane fire doesn't melt it — magical cold.
- **Solution:** Cast a fire spell ON the ice (Fire + Frozen surface = thaw, then brazier lights)
- **Alternative:** Kineticist fire impulse, alchemist fire, or torch + bellows (Crafting DC 16)
- **Lock opens:** Brazier lights. First seal broken.

**Water Lock Room:**
- A dry fountain. The water channel leads to a sealed pipe. Above: a rain-catcher on the ceiling filled with stagnant water.
- **Solution:** Break the rain-catcher (Athletics DC 14 or ranged attack). Water flows to fountain. Fountain activates mechanism.
- **Alternative:** Create Water spell. Hydraulic Push into the channel.
- **Lock opens:** Fountain flows. Second seal broken.

**Earth Lock Room:**
- A stone column with a crack. The column must be broken to open the path — but hitting it triggers a cave-in (4d6 bludgeoning in 15 ft).
- **Solution:** Earthquake effect, Earth Kineticist blast, or place an explosive at the base and retreat (Crafting DC 16 to rig, 3 rounds to retreat).
- **Alternative:** Tunnel around it (2 hours, Athletics DC 16, partner assists).
- **Caution solution:** Examine the crack first (Perception DC 14). Reveals structural weakness — targeted strike at the weak point: no cave-in.
- **Lock opens:** Column splits. Third seal broken.

**Inner Tomb Door:** All 3 seals broken → door opens. +80 XP (Major milestone). +1 Scholarly.

---

## 📋 PUZZLE STATE TRACKING

DM tracks puzzle state on the grid/map using symbols:

| Symbol | Meaning |
|--------|---------|
| ✓ | Rune/lock solved |
| ✗ | Rune/lock failed attempt |
| → | Player's current position |
| ! | Trap (revealed after trigger) |
| ? | Unexamined room |

**Save block (during dungeon):** `"dungeon_state": { "dungeon_id": "rune_gate", "rooms_cleared": ["A", "D"], "puzzle_state": {"star": "activated", "wave": "activated", "mountain": "inactive", "flame": "inactive"}, "attempts": 1 }`

---

## ⚠️ DM RULES

1. **Player solves. Not skill checks.** The puzzle is the game. Skill checks are bypass only.
2. **Show the map at each step.** Update ASCII grid with current state after every player action.
3. **One hint per puzzle.** Genuine clue, not the answer. "The mosaic in the previous room showed a path."
4. **Companion contributions are flavor, not solutions.** A companion can comment ("This reminds me of Sarkorian theology") but cannot solve it for the player.
5. **Track state in save block during dungeon.** If session ends mid-puzzle, state persists.
6. **Multiple attempts allowed.** Resetting costs time (and sometimes HP from traps). The player is never permanently locked out.

---

## 🗺️ DUNGEON PUZZLE 4: THE WEIGHT BRIDGE (Ch4, Armag's Tomb Approach)

**Setup:** A bridge over a chasm. Weight sensors embedded in the stones. Too much weight = collapse. Too little = doors won't open.

```
MAP:
  [ENTRANCE] → [BRIDGE — 15 tiles, 3 wide] → [DOOR]

BRIDGE RULES:
  Total weight on bridge must be EXACTLY 4 (measured in "stones")
  Player = 2 stones. Companion = 1 stone each. Equipment = varies.
  Door opens only when bridge reads exactly 4.
  Bridge collapses at 6+.
```

**Clue (previous room):** A mural showing four figures crossing a bridge. One is large (2), three are small (1 each). But only three figures reach the other side — one stepped off midway. Total on bridge at the door: 2 + 1 + 1 = 4.

**Solutions:**
- Player (2) + 2 companions (1+1) = 4 ✓. Two companions stay behind.
- Player (2) + 1 companion (1) + drop 1 stone of equipment on the bridge = 4 ✓
- Player removes armor (drops to 1) + 3 companions = 4 ✓ (creative, risky)
- Fly/levitate across (no weight) and open door from the other side — bypasses entirely

**Wrong:** Player + 3 companions = 5 → bridge groans, warning. Player + 4 = 6 → collapse (4d6 fall damage, Ref DC 18 to grab edge).

**XP:** 100 XP. +1 Scholarly if mural clue used.

---

## 🗺️ DUNGEON PUZZLE 5: THE MIRROR MAZE (Ch5, Pitax Palace Basement)

**Setup:** A 4×4 grid of rooms. Each room has a mirror on one wall. Mirrors can be rotated. A beam of light enters from the top-left. The beam must reach the bottom-right to open the vault.

```
MAP (4×4, beam enters A1, must exit D4):
  [A1→]  [A2]  [A3]  [A4]
  [B1]   [B2]  [B3]  [B4]
  [C1]   [C2]  [C3]  [C4]
  [D1]   [D2]  [D3]  [D4→EXIT]

Mirrors: each room has 1 mirror, angled / or \
Rotate mirror: player specifies room + angle
Beam travels in straight line, bounces off mirrors
```

**Starting mirror positions (DM tracks):**
- A1: \ (redirects beam down to B1)
- B1: / (redirects beam right to B2)
- B2: empty (beam passes through)
- B3: \ (redirects beam down to C3)
- All others: random angles

**Solution:** Multiple valid paths. Player must trace the beam through rotations. DM describes: "The beam hits the mirror in B3 and redirects downward. It passes through C3 (no mirror) and hits D3. The mirror in D3 is angled \ — the beam goes right, into D4. The vault clicks."

**Hint:** A diagram of the grid scratched into the wall of A1 with the beam drawn — but the mirrors have been moved since the diagram was made. One mirror is correct, the rest need adjusting.

**XP:** 120 XP. +1 Scholarly.

---

## 🗺️ DUNGEON PUZZLE 6: THE BLOOD OATH DOORS (Ch5-6, Nyrissa's Approach)

**Setup:** Three doors. Each requires a sacrifice — not HP, but something the player has earned. The doors test what the player values.

```
MAP:
  [HALL] → [DOOR 1] → [DOOR 2] → [DOOR 3] → [INNER SANCTUM]

Each door has an inscription. Each demands a price.
All three must be opened. The order doesn't matter.
```

**DOOR 1 — THE DOOR OF TITLES:**
*"Give a name you gave. One who carries your honor must return it."*
- **Price:** Revoke one companion title. The companion loses their Suffix and Prefix. Relationship −1. The title burns away on the door.
- **Alternative (Arcana DC 22):** Create a false title — an illusion of sacrifice. Door accepts it. No companion loses anything. +1 Cunning.
- **Refusal:** Door remains shut. Must find another way (Athletics DC 24 to force, or Thievery DC 22 to pick the magical lock).

**DOOR 2 — THE DOOR OF MEMORY:**
*"Give a moment that made you. One that you would relive if you could."*
- **Price:** The player names a Bond Moment from the Bond History Log. That moment is consumed — the companion and player both forget it happened. Remove from save block.
- **Alternative (Diplomacy DC 22):** Argue that all moments are equal. Door: "Interesting. Pass." No sacrifice.
- **Refusal:** Same as Door 1.

**DOOR 3 — THE DOOR OF POWER:**
*"Give what makes you strong. One ability you earned must be unearned."*
- **Price:** Lose one Prestige Upgrade ability (L10 or L15). Ability deactivates permanently.
- **Alternative (Will DC 24):** Resist the door's demand through sheer willpower. "I earned this. You cannot take what I chose to become."
- **Refusal:** Same forcing options.

**Design intent:** The Alternatives exist so the player never HAS to sacrifice. But the sacrifices are real — and Nyrissa, watching from beyond the door, judges what the player chose. If the player sacrificed all three: `nyrissa_saveable +2` (she saw someone give up what they valued). If zero sacrifices: +0, but +1 Cunning or +1 Blunt.

**XP:** 150 XP. +1 Scholarly if alternatives found.

---

## ⚠️ DM RULES

1. **Player solves. Not skill checks.** Skill checks are bypass only.
2. **Show the map at each step.** Update ASCII grid with current state.
3. **One hint per puzzle.** Genuine clue, not the answer.
4. **Companion contributions are flavor, not solutions.**
5. **Track state in save block during dungeon.**
6. **Multiple attempts allowed.** Resetting costs time (and sometimes HP).

---

*KM_DungeonPuzzles.md — Kingmaker PF2e Text Adventure | Multi-Room Dungeon Puzzles v2.0*
*6 dungeons across Ch2-6. Inspired by Icewind Dale.*


---

<!-- merged from KM_MobileBase.md (v93.21 file consolidation) -->

# KINGMAKER — MOBILE BASE (CARAVAN / RIVER BARGE)
## KM_MobileBase.md | Active from: Chapter 2 (unlocked via Kingdom investment) | Referenced by: KM_Exploration.md, KM_Kingdom.md

> **DM:** The Mobile Base is a kingdom-funded caravan or river barge that serves as a mobile camp with upgradeable features. It makes wilderness exploration more strategic by providing persistent bonuses, storage, and facilities. Unlocked mid-Ch2 via kingdom investment (10 RP). The player chooses caravan (land) or barge (river) — each has different terrain advantages.

---

## 🚀 ACQUISITION

**Kingdom Activity:** Commission Mobile Base (10 RP, 1 kingdom turn build time)
```
[KINGDOM ACTIVITY — Commission Mobile Base]
Your kingdom is large enough to support a permanent expedition force.
Choose your mobile base type:

 [C] CARAVAN — Wagon train with draft horses. Travels all land hexes.
     Advantage: No terrain restriction on land. Carries more supplies.
     Disadvantage: Slower on roads (land speed). Cannot cross deep water.

 [B] RIVER BARGE — Flat-bottomed vessel for Stolen Lands waterways.
     Advantage: Fastest travel on river hexes (−1 day per river hex).
     Disadvantage: Cannot leave river network. Must dock to explore inland.
```

---

## 📊 BASE STATS

| Stat | Caravan | Barge |
|------|---------|-------|
| **Speed** | 2 hexes/day (road), 1 hex/day (off-road) | 3 hexes/day (river), N/A (land) |
| **Cargo Capacity** | 50 Bulk | 80 Bulk |
| **Ration Storage** | 30 days | 45 days |
| **Defense** | AC 15, HP 60 | AC 12, HP 80 |
| **Crew** | 2 drivers + guards | 4 crew + guards |
| **Camp bonus** | +2 to Prepare Campsite | +2 to Prepare Campsite, no ground hazards |

---

## 🔧 UPGRADES

Purchased with RP during Kingdom Turns. Each upgrade takes 1 turn to install.

| Upgrade | RP Cost | Effect |
|---------|---------|--------|
| **Crafting Bench** | 6 RP | Craft items during travel (KM_Crafting.md). −1 day crafting time. |
| **War Room** | 8 RP | `.wartable` accessible during travel. +1 to army command checks. |
| **Companion Quarters** | 4 RP | Companions in reserve gain +1 to next combat check (rested). Camp morale events fire more frequently. |
| **Expanded Storage** | 4 RP | Cargo +20 Bulk. Ration storage +15 days. |
| **Armored Hull** | 6 RP | Defense: AC +3, HP +20. Resists ambush damage. |
| **Cooking Station** | 4 RP | Special Meal recipes available during travel (KM_Kingdom.md). +1 to meal quality. |
| **Medical Bay** | 6 RP | Treat Wounds during travel (no downtime needed). +2 to Medicine checks on the base. |
| **Signal Tower** (Caravan) | 4 RP | Visual signal to nearest watchtower. Early warning system extends 1 hex. |
| **Sail Rig** (Barge) | 6 RP | Speed +1 hex/day on river when wind is favorable (50% of days). |

---

## 🗺️ TRAVEL WITH MOBILE BASE

### Movement
- **Caravan:** Follows road network at 2 hexes/day. Off-road: 1 hex/day. Cannot enter mountain or deep water hexes.
- **Barge:** Follows river hexes at 3 hexes/day. Must dock at river-adjacent land hexes to explore inland. Docking = free action.

### Encounters While Traveling
- Mobile Base **does not prevent** random encounters. Encounter chance as normal.
- If attacked: party fights from/near the base. Base provides cover (+2 AC while behind it).
- **Ambush protection** (if Armored Hull): Perception DC to detect ambush reduced by 2 (easier to spot).

### Camping in the Mobile Base
- All camp activities available. +2 circumstance bonus to Prepare Campsite (built-in shelter).
- Night attacks: base provides walls. Attackers must breach (Athletics DC 14 for caravan, DC 12 for barge).
- **Weather protection:** Moderate weather hazards (rain, wind) negated while in the base. Severe (storm, tornado) still apply.

---

## 💥 MOBILE BASE DAMAGE

The base can be damaged by combat, environmental hazards, or story events.

| HP Remaining | Status | Effect |
|-------------|--------|--------|
| 100–61% | Intact | All bonuses active |
| 60–31% | Damaged | Speed −1 hex/day. One upgrade offline (DM picks least critical). |
| 30–1% | Critical | Speed halved. Two upgrades offline. Camp bonus lost. |
| 0 | Destroyed | Base lost. Must commission new one (full RP cost). Cargo dumped in current hex. |

**Repair:** 2 RP per 25% HP restored. Takes 1 kingdom turn. Cannot repair while traveling — must be at a settlement.

---

## 📋 DISPLAY FORMAT

```
══════════════════════════════════════════════
MOBILE BASE — {Caravan/Barge} "{Name}"
══════════════════════════════════════════════
HP: {current}/{max} | Status: {Intact/Damaged/Critical}
Speed: {X} hexes/day | Cargo: {used}/{max} Bulk
Rations: {current}/{max} days
Upgrades: {list of installed upgrades}
Current Location: Hex [{x,y}] — {description}
══════════════════════════════════════════════
```

**Save block:** `"mobile_base": { "type": "caravan", "name": "The Iron Road", "hp": 60, "hp_max": 60, "upgrades": ["crafting_bench", "companion_quarters"], "cargo_used": 12, "rations": 30, "location": [4,7] }`

---

## ⚠️ DM RULES

1. **The base is a home.** Companions comment on it. They decorate their quarters. It's not just a stat block — it's a place.
2. **Name it.** The player names their caravan/barge. Use the name in narration.
3. **Upgrades are visible.** When the crafting bench is installed, describe the tools bolted to the wagon bed. When the war room is added, describe the map table.
4. **Destruction is dramatic.** If the base is destroyed, it's a scene — cargo scattered, upgrades lost, companions salvaging what they can.
5. **One base at a time.** Cannot have both caravan and barge. Can switch by commissioning a new one (old one decommissioned, upgrades do not transfer).

---

## 🎲 MOBILE BASE EVENTS (d8, roll per 3 hexes traveled)

| d8 | Event | Resolution |
|----|-------|-----------|
| 1 | **Wheel breaks** (caravan) / **Hull scrapes** (barge) | Crafting DC 14 to repair (1 hour). No repair: Speed −1 until settlement. |
| 2 | **Ambush on the road/river** | Combat encounter. Base provides cover (+2 AC). If Armored Hull: attackers take 1d6 approaching. |
| 3 | **Merchant encounter** | Traveling merchant offers 3 random items at 120% price. Rare materials available (1 per encounter). |
| 4 | **Refugee request** | Family asks for a ride to the capital. Accept: Loyalty +1, 1 day slower. Refuse: no penalty. |
| 5 | **Weather damage** | Severe weather hits the base. Fort DC 14 or base takes 10 HP damage. Expedition Tent negates. |
| 6 | **Companion moment** | Random companion has a scene triggered by the travel. Bond Moment opportunity. +1 if engaged. |
| 7 | **Discovery** | Warden spots something from the base: hidden trail, animal den, mineral deposit. Free hex intel. |
| 8 | **Nothing** | Quiet travel. Good time to craft, rest, or talk. |

### Named Caravan Events (story-specific)

**"The Painted Wagon" (Ch2):** A traveling theater troupe asks to join your caravan for protection. Accept: they perform at your next settlement (Culture +1, Loyalty +1). Refuse: they're attacked 1 hex later (guilt moment — player can rescue).

**"The River Ghost" (Ch3, barge only):** At night on the river, something bumps the hull. Perception DC 16: a body, face-down. Investigation reveals a murdered Pitax courier carrying intelligence. Free intel + quest hook.

**"The Broken Axle" (Ch4):** The caravan master reports the axle was sabotaged — cut partway through. Someone in the caravan or a recent visitor did this. Investigation scene (KM_Examination.md format). Spymaster: auto-detect if present.

**"The Bloom on the Water" (Ch6, barge only):** Roses growing on the river surface. The barge can push through (hull takes 2d6 damage) or detour (adds 1 day). Nature DC 18: the roses part if you play music. Hakon or Linzi: auto-success.

### Upgrade Narration

When an upgrade is installed, the DM describes it in one sentence:

| Upgrade | Installation Narration |
|---------|----------------------|
| Crafting Bench | *"A heavy wooden bench bolted to the wagon bed, tools hanging from pegs. It smells of iron filings and possibility."* |
| War Room | *"A map table that folds out from the wall. Pins and string. The kingdom's borders drawn in charcoal. It makes the caravan feel like a command post."* |
| Companion Quarters | *"Curtained sections. Not privacy — the illusion of it. Enough for people who've been sleeping on the ground to remember what a personal space feels like."* |
| Medical Bay | *"Clean cloth, boiled instruments, a folding cot. Tristian called it 'adequate.' From him, that's a compliment."* |
| Cooking Station | *"A proper fire pit with a wind shield and hanging pots. The first meal cooked here makes the caravan smell like a home."* |

**Save block:** `"mobile_base": { "type": "caravan", "name": "The Iron Road", "hp": 60, "hp_max": 60, "upgrades": ["crafting_bench"], "cargo_used": 12, "rations": 30, "location": [4,7] }`

---

*KM_MobileBase.md — Kingmaker PF2e Text Adventure | Mobile Base System v2.0*
*Travel events + named story events + upgrade narration.*


---

<!-- merged from KM_MythicPaths.md (v93.21 file consolidation) -->

# KINGMAKER — MYTHIC PATHS (POWER SOURCE CHOICE)
## KM_MythicPaths.md | Active from: Chapter 5 | Referenced by: KM_Ch5.md, KM_Endings.md

> **DM:** At a pivotal moment in Chapter 5, the player chooses a Power Source that defines their late-game identity and unlocks 3 abilities + 1 ultimate. This choice alters the final chapter structure and enables specific endings. The choice is narratively framed — not a menu, but a scene where the power source chooses the player as much as the player chooses it.

---

## 🔮 THE FOUR PATHS

### PATH 1 — FEY CHAMPION (Nyrissa's Power)
*The Stolen Lands are saturated with First World energy. Nyrissa offers a fragment of her power — not as a gift, but as a bridge.*

**Requirement:** `nyrissa_awareness ≥ 3` AND `nyrissa_early_contact = TRUE`

**Scene:** Nyrissa appears in the Bloom's heart. "I cannot fight what is happening to me. But you can carry what I was. Will you?"

**Abilities:**
| Level | Ability | Effect |
|-------|---------|--------|
| 1 | **Fey Step** | 1/combat, teleport 30 ft as a free action. Leave a rose where you stood. |
| 2 | **Bloom Ward** | Immune to Bloom damage and Bloom creature fear auras. Bloom creatures hesitate 1 round. |
| 3 | **First World Sight** | Permanent True Seeing vs fey illusions. +2 to saves vs enchantment. |
| Ultimate | **Nyrissa's Garden** | 1/day, create a 30-ft zone of First World terrain for 1 minute. Allies: +2 AC, fast healing 5. Enemies: difficult terrain, Fascinated (Will DC 22). |

**Ending unlock:** True Ending eligible. Nyrissa can be saved.

---

### PATH 2 — SWORD SAINT (Martial Transcendence)
*Power from mastery, not magic. The blade has been your answer since Aerynth. Here, it becomes something more.*

**Requirement:** Player build is martial (Fighter, Guardian, Barbarian, Monk, Rogue, Ranger, Champion, Swashbuckler, Thaumaturge) AND `prestige.l10_choice` is military-aligned

**Scene:** During a moment of perfect clarity in combat — time stops. Your weapon speaks. Not words. Understanding.

**Abilities:**
| Level | Ability | Effect |
|-------|---------|--------|
| 1 | **Perfect Strike** | 1/combat, treat an attack roll as a natural 20 (auto-crit). |
| 2 | **Unbreakable** | When dropped to 0 HP, remain at 1 HP instead. 1/day. |
| 3 | **Speed of Thought** | +1 action on the first round of every combat (Quickened). |
| Ultimate | **Mythic Blade** | Weapon permanently gains +2 to attack and damage. On a critical hit: target must make Fort DC 24 or be Stunned 2. |

**Ending unlock:** Conquest ending. The kingdom survives by force of will.

---

### PATH 3 — FIRST WORLD SOVEREIGN (Nature's Crown)
*The land itself recognizes you. Not as owner — as steward. The Stolen Lands stop being stolen.*

**Requirement:** `scholarly ≥ 5` OR Druid/Ranger/Kineticist build AND kingdom Culture ≥ 60

**Scene:** The oldest tree in the Narlmarches bends toward you. The earth trembles once — not an earthquake, a greeting.

**Abilities:**
| Level | Ability | Effect |
|-------|---------|--------|
| 1 | **Land's Blessing** | All kingdom hexes: +1 to all checks within your territory. Random encounter rate −10%. |
| 2 | **Verdant Shield** | 1/combat, summon a wall of living wood (Wall of Thorns, free action). |
| 3 | **Sovereign's Call** | 1/day, summon a Treant ally (level = player level −2) for 1 encounter. |
| Ultimate | **Crown of Roots** | The kingdom's land fights invaders. During sieges: +4 Defense to all fortifications. Enemy armies in your territory: −2 Morale per turn. |

**Ending unlock:** Golden Ending eligible. The Stolen Lands become a permanent haven.

---

### PATH 4 — SHADOW WALKER (Void Between Worlds)
*You came from Aerynth. You walk between planes. The space between worlds is not empty — it remembers you.*

**Requirement:** Player's gear is from Aerynth (all builds) AND `cunning ≥ 5` OR `ruthless ≥ 5`

**Scene:** During a moment between sleep and waking, the void opens. Not Nyrissa's garden. The space you crossed to get here. It offers to take you further.

**Abilities:**
| Level | Ability | Effect |
|-------|---------|--------|
| 1 | **Planar Shift** | 1/day, phase through solid matter (walls, doors, barriers) for 1 round. |
| 2 | **Void Armor** | Resistance 5 to all damage types. Your Aerynth armor resonates. |
| 3 | **Between Worlds** | 1/combat, become incorporeal for 1 round. Immune to physical damage. Can still attack. |
| Ultimate | **The Bridge** | Open a permanent portal between two locations in your kingdom. Travel between them is instant. During final battle: call reinforcements from any portal location. |

**Ending unlock:** Transcendence ending. eRmaC understands why they crossed worlds.

---

## 📋 PATH SELECTION SCENE

```
══════════════════════════════════════════════
MYTHIC CHOICE — THE POWER SOURCE
══════════════════════════════════════════════
Something has changed. The battles, the kingdom, the Bloom
— they have opened something in you. Four paths forward.
Only one is yours.

 [1] Fey Champion — Accept Nyrissa's fragment
 [2] Sword Saint — Trust the blade that brought you here
 [3] First World Sovereign — Let the land choose you
 [4] Shadow Walker — Step into the space between

Some paths may be unavailable based on your choices.
This decision is permanent.
══════════════════════════════════════════════
```

---

## 📊 ABILITY UNLOCK TIMING

| Mythic Level | When | How |
|-------------|------|-----|
| 1 | Path chosen (Ch5) | Immediate |
| 2 | Mid-Ch5 (after first major victory) | Narrative unlock |
| 3 | Ch6 (before final dungeon) | Narrative unlock |
| Ultimate | Final chapter (climax) | Fires automatically at dramatic peak |

---

## 📜 UNLOCK NARRATION — SCRIPTED SCENES

### Fey Champion — Unlock Scene
> *The Bloom's heart is not a place — it's a wound. You stand at the center of it. Roses the color of infection climb the walls of a space that shouldn't exist. And she is there.*

> *Nyrissa does not look like a villain. She looks like someone standing at the edge of a very long fall.*

> *"I cannot fight what is happening to me," she says. "But you — you carry something I don't have anymore. Will. Purpose. The ability to choose." She extends her hand. A single rose, glowing. "This is what I was. Carry it. Use it. Before there is nothing left of me to give."*

> *The rose dissolves into your palm. The First World breathes into your bones.*

### Sword Saint — Unlock Scene
> *It happens in the middle of a fight. Not the hardest fight — not a boss, not a siege. Just combat. Blade against blade. And then — time stops.*

> *Not magically. Not a spell. The moment stretches because your body has reached a state your mind hasn't caught up with. Every angle is visible. Every outcome is calculated. The blade in your hand is not a weapon. It is a thought you are having.*

> *Your weapon speaks. Not words. Understanding. A language of edge and intent that Aerynth's forges built into the metal and Golarion's wars finally woke up.*

> *"Perfect Strike" is not a technique. It's the moment when there is no difference between what you intend and what happens.*

### First World Sovereign — Unlock Scene
> *You are walking through your kingdom. Alone — no companions, no guards. Just the land. And the land is... aware of you.*

> *A tree bends. Not in wind — toward you. The grass under your feet grows an inch as you step. A stream changes course — slightly, barely — to flow toward the path you're walking.*

> *The oldest tree in the Narlmarches has been waiting. It bends its crown — a gesture that takes a tree a decade to make, offered in a second.*

> *"You are not the first to rule here," the land says — not in words, in growing. "But you are the first the land chose back."*

### Shadow Walker — Unlock Scene
> *Between sleep and waking. The space you crossed to get here — from Aerynth to Golarion — opens like a door you forgot was there.*

> *It is not empty. It never was. The void between worlds is full of the residue of every crossing — memories that fell off in transit, intentions that didn't survive the translation. Your armor hums. Your weapon resonates. They remember this place.*

> *"You came through here once," the void says — not a voice, a pressure. "You thought it was an accident. It wasn't. I've been waiting for you to come back."*

> *You don't go back. Not yet. But the door stays open. And you can feel the other worlds on the other side — close enough to touch.*

---

## 🗣️ NPC REACTIONS TO MYTHIC PATHS

| Path | Companion Reactions | NPC Reactions |
|------|-------------------|-------------|
| **Fey Champion** | Tristian: awed. Jaethal: suspicious. Amiri: uncomfortable. Linzi: documenting frantically. | Druids sense the change. Merchants feel uneasy. Fey creatures bow. |
| **Sword Saint** | Valerie: envious-respectful. Amiri: inspired. Harrim: "Even perfection ends." | Soldiers stop sparring when you walk by. Smiths want to study your blade. Aldori Swordlords request an audience. |
| **First World Sovereign** | Linzi: peaceful. Ekundayo: his dog sits at your feet without being called. Nok-Nok: terrified then delighted. | Animals follow you. Plants grow where you stand. Farmers bring offerings. Children aren't afraid. |
| **Shadow Walker** | Jubilost: overwhelmed with questions. Jaethal: "Finally someone as strange as I am." Octavia: worried. | Mages detect nothing and that scares them. Your shadow moves wrong in torchlight. People step aside before they decide to. |

### Mythic Path + Kingdom Interaction

| Path | Kingdom Bonus (passive) |
|------|----------------------|
| **Fey Champion** | Bloom advance slowed 1 hex/turn permanently. Fey encounters: 50% friendly. |
| **Sword Saint** | Army Offense +1 globally (your legend inspires). Personal combat: +1 to all attack rolls. |
| **First World Sovereign** | Food commodity +2/turn (land yields more). Random encounter rate −15% in all hexes. |
| **Shadow Walker** | Spymaster operations: +2 to all rolls. Portal network: instant travel between 2 kingdom settlements. |

**Save block:** `"mythic_path": { "chosen": "shadow_walker", "abilities": ["planar_shift", "void_armor"], "power_level": 2 }`

---

*KM_MythicPaths.md — Kingmaker PF2e Text Adventure | Mythic Paths v2.0*
*4 paths + unlock narration + NPC reactions + kingdom bonuses.*


---

---

## SECRET & ALTERNATE ENDINGS — MOVED (v95.9)
> The endings catalog was split to **KM_Endings.md** for file-size compliance. Load it at the campaign finale.
