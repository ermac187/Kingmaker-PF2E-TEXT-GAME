# KINGMAKER — COMPANION PROFILES (PART A)
## KM_Companions.md | Referenced by: KM.txt
### Used in: All chapters (Pre-Prologue onward)

> **DM: Load ALL five companion files every session:**
> `KM_Companions.md` (this file) | `KM_Companions_B.md` | `KM_Companions_C.md` | `KM_Companions_D.md`
> `KM_Companions_Agendas.md` + `KM_Companions_Agendas_B.md` — hidden agendas, inter-companion
> relations, and incompatibility system for all 88 companions.
> **Part A:** Companion Roster, Relationship System, CRPG Originals (#6 Amiri, ✦ Linzi, #66 Nok-Nok, #16 Tristian, #32 Valerie, #20 Harrim)
> **Part B:** #18 Jaethal, #45 Kalikke/Kanerah, #84 Octavia, #48 Regongar, #10 Lem + NPC Interaction Dynamics + Tracking Template
> **Scaled Stat Blocks:** For mid/late-game companion combat stats, search **KM_Companions_Scaled.md** in project knowledge.

---

> **DM INSTRUCTION:** Load alongside KM.txt every session. Voice all companions in character. Track Relationship in JSON Save Block. All companions start Neutral unless a story flag changes this.

---

## 📊 COMPANION ROSTER

| # | Name | Race | Class | Role | First Available |
|---|------|------|-------|------|----------------|
|  6 | Amiri | Human (Kellid) | Barbarian (Giant Instinct) | Frontline Striker | Prologue |
|  ✦ | Linzi | Halfling | Bard (Maestro) | Support/Chronicler | Prologue (Forced) |
| 66 | Nok-Nok | Goblin | Rogue (Scoundrel) | Skirmisher/Striker | Ch2 ⭐ |
| 16 | Tristian | Human | Cleric (Cloistered) | Healer/Support | Ch1 — Temple of the Elk ⭐ |
| 32 | Valerie | Human | Fighter | Tank/Shield Wall | Prologue |
| 20 | Harrim | Dwarf | Cleric (Warpriest) | Debuffer/Controller | Prologue |
| 18 | Jaethal | Elf | Cleric (Warpriest, Urgathoa) | Striker/Debuffer | Prologue |
| 45 | Kalikke/Kanerah | Human (Tiefling) | Kineticist (Dual Gate) | Blaster/Controller | Ch2 ⭐ |
| 84 | *Octavia | Aiuvarin | Wizard (Transmutation) | Arcane Striker/Skill | Ch1 — Technic League ⭐ |
| 48 | *Regongar | Human (Half-Orc) | Magus (Inexorable Iron) | Frontline Magus | Ch1 — Technic League |
| 10 | Lem | Halfling | Bard (Maestro) | Buffer/Inspirer | Chapter 1 |
| 60 | Ekundayo | Human | Ranger (Precision Edge) | Precision Ranged/Hunter | Ch2 ⭐ — KM_Ekundayo.md |

> **Companion #1:** Jubilost Narthropple — Gnome Alchemist (Scholar/Blaster). ⭐ Quest-locked, Ch2. Joins at Skunk River crossing.

> **MISSED RECRUITMENT:** Quest-locked companions not recruited at trigger travel to the Capital. DM runs Accept/Decline/Ask scene. Decline → Capital NPC, re-approachable.

---

## 📋 RELATIONSHIP SYSTEM

```
Relationship Scale:
  Hostile    : −2 (actively works against player; may leave party)
  Strained   : −1 (disagreements; reduced cooperation)
  Neutral    :  0 (default; professional)
  Friendly   : +1 (trusts player; opens personal dialogue)
  Devoted    : +2 (will sacrifice for player; unlocks personal quest)

Track in JSON Save Block under companions[].relationship
```

### Relationship Change Triggers

**+1 (Neutral → Friendly or Friendly → Devoted):**
- Player chooses an action that companion explicitly Approves (see each profile)
- Player completes a personal task the companion mentioned (even informally)
- Player defends the companion in a social confrontation with an NPC
- Player risks something for the companion during a scene (HP, resources, reputation)
- Long rest conversation where player listens to companion and asks follow-up questions
- Player makes a choice that aligns with the companion's core value (see profile)

**−1 (any level toward Hostile):**
- Player chooses an action that companion explicitly Disapproves (see each profile)
- Player dismisses or ignores the companion's expressed concern in a scene
- Player lies to the companion and the companion discovers it
- Player takes an action that directly harms something the companion cares about
- Player uses the companion's personal trauma as a tool or joke

**−2 (direct Hostile trigger — rare):**
- Player betrays the companion to an enemy
- Player kills an NPC the companion was protecting
- Player commits an act the companion considers unforgivable (e.g., murdering surrendered enemies in front of Tristian; enslaving prisoners in front of Octavia)

**Relationship floor rules:**
- Cannot drop below Hostile through normal play (leaves party at Hostile if not addressed)
- Cannot rise from Hostile without a direct in-scene reconciliation (Diplomacy DC 18)
- Devoted requires: Friendly + personal quest complete + at least one scene where player actively prioritized the companion over tactical advantage

**DM behavior at each level:**
- Hostile: companion may argue, slow down, or give false information during scenes
- Strained: companion performs minimally in combat; short, clipped dialogue
- Neutral: professional; performs duties, no extra investment
- Friendly: shares opinions proactively; combat performance at full; opens personal dialogue
- Devoted: will take hits for player; shares hidden information; unlocks quest; unique dialogue

---

## 🏷️ COMPANION & SOLDIER TITLE SYSTEM — THREE TIERS OF HONOR

eRmaC may grant any companion or named soldier a title across three tiers, granted in order. Each tier escalates trust, honor, and reward. The player defines the name and its meaning at granting. The DM determines the mechanical buff from that meaning.

**Full Format:** `[Prefix] [Name] [Suffix]`
- Tier 1 only: Jaethal *The Ender*
- Tiers 1+2: *Ultima* Jaethal *The Ender*

**Rules:** Suffix must be granted before Prefix (1→2, no skipping). One Suffix and one Prefix max. Changing either replaces that name — no stacking. Replacement costs the same Overflow. Titles apply to companions and named soldiers only. Player states the name and its meaning; DM assigns the buff. Positions (Commander, General, etc.) are assigned freely via kingdom leadership roles — no Overflow cost, no ceremony required.

---

### TIER 1 — SUFFIX: THE DESCRIPTOR (1 Overflow)

The Suffix is what civilians call them — a description of who they are. *"The Valkyrie." "The Enforcer." "The Inquisitor."* Deduct 1 from `pending_overflow`.

**Reward:** +1 situational buff tied to meaning. Examples: *The Ender* → +1 damage vs bloodied; *Giantsbane* → +1 attack vs Large+; *The Redeemer* → +1 Heal checks.

**DM display:** State suffix, state buff. Companion acknowledges in their own voice.

---

> **⛔ FULL PASSIVE + 5-STAR ITEM DEFINITIONS:** See `KM_Companions_Titles.md` for each Pick-10 companion's Prefix passive skill, Suffix regalia item, reaction-score scaling, materialization narrative rules, and quest-locked generation instructions. The DM MUST load that file when titles are granted.

### TIER 2 — PREFIX: THE TITLE (1 Overflow)

The Prefix is a title or nickname interchangeable with their first name. *"Lux." "Legatus." "Sapiens."* NPCs who witnessed the titling use it. Requires Tier 1. Deduct 1 from `pending_overflow`.

**Reward — Buff + Regalia Item:**

*Buff:* +1 to relevant checks or saves (separate from Suffix buff, both active). Examples: *Ultima* → +1 Intimidation; *Iron* → +1 AC; *Swift* → +5 ft Speed.

*Regalia Item:* DM generates a unique cosmetic-layer wondrous item (cape, sash, armband, circlet, signet, etc.) as a visible mark of station. No gear slot — worn over armor, no equipment conflict. Grants one minor passive bonus tied to prefix meaning (e.g., *Ultima* Jaethal → black half-cape → +1 circ. Intimidation aura; *Iron* Valerie → steel armband → +1 circ. Shield Block DR).

**Title-bound:** If Prefix revoked, Regalia becomes mundane.

**DM display:** State prefix, state buff, describe Regalia in one sentence. Companion reacts personally.

---

### TITLE REACTION SYSTEM

DM assigns a **Title Reaction Score** (−5 to +5) per tier based on companion personality, not player intent. Suffix: does the role match their purpose? Prefix: does the honor name something they believe — or fear?

| Score | Effect |
|-------|--------|
| +5 | +2 to base buff, Relationship +1 |
| +3/+4 | +1 to base buff |
| +1/+2/0 | Unchanged |
| −1/−2 | Buff −1 (min 0) |
| −3/−4 | Buff −1, Relationship −1 |
| −5 | Buff 0, Relationship −1 |

---

### REVOKING TITLES

Either tier revocable at any time, no mechanical penalty. Revoking Suffix auto-revokes Prefix. Buff ends, Regalia becomes mundane. Companion reacts in character.

### 🏆 HERO POINT REFUND — "THE PERFECT TITLE"

When a companion's Title Reaction Score hits **+5** (the best title they could ever receive), the player earns **1 Hero Point** for that tier. This applies to Suffix AND Prefix independently — if both are +5, the player earns 2 Hero Points total, **breaking even on cost**.

| Condition | Refund |
|-----------|--------|
| Suffix reaction = +5 | +1 Hero Point (refunds the 1 Overflow spent) |
| Prefix reaction = +5 | +1 Hero Point (refunds the 1 Overflow spent) |
| Both Suffix AND Prefix = +5 | +2 Hero Points (full break-even on Tiers 1+2) |

**DM Rule:** The Hero Point fires IMMEDIATELY when the reaction score is revealed. Narrate it as the companion's genuine emotional response — the title struck something deep. This is not a transaction. It's a moment.

### ⛔ MANDATORY TITLE ROSTER — AFTER EVERY TITLE GRANT

**After granting ANY title (Suffix or Prefix), the DM MUST output the full title roster.** This is not optional. Skipping it = `.fail 7`. Format:

**⛔ Title Case, no ALL CAPS. `Linzi:` not `CANTRIX LINZI:`.**

```
[TITLE ROSTER]
 Lux Seelah the Valkyrie          — Devoted (+2)
 Infallibilis Lann the Trueshot   — Devoted (+2)
 {Name} — untitled                — {relationship}
[END ROSTER]
```

**Every titled companion uses their FULL title format** (`[Prefix] [Name] [Suffix]`). Untitled companions are listed as `{Name} — untitled`. This roster updates cumulatively — never rebuilt from memory, always appended. If a title is missing from the roster after it was granted, that is `.fail 7`.

**TITLE USAGE IN NARRATION — WHO USES WHAT:**

**Prefix (the title/nickname):** Used by companions, party members, and close allies — in combat, camp, and personal moments. Amiri shouts "LUX, BEHIND YOU!" not "Seelah." Companions who witnessed the titling switch to the Prefix as their default name for that person.

**Suffix (the descriptor):** Used by civilians, guards, merchants, and strangers. The flatbread vendor says "That's the Valkyrie" not "That's Lux." Reputation deeds reference the Suffix: "The Enforcer cleaned out the bandits."

**Full title:** Used in formal contexts — throne room, kingdom announcements, introductions to foreign dignitaries. "Lux Seelah the Valkyrie."

**Untitled NPCs** use the base name. The DM never uses a title the NPC hasn't witnessed being granted.

### OVERFLOW COST SUMMARY

| Action | Cost |
|--------|------|
| Tier 1 (Suffix) | 1 Overflow |
| Tier 2 (Prefix) | 1 Overflow |
| Both tiers | 2 total |
| Replace either | Same as original |

### SAVE BLOCK FORMAT

```json
"companion_titles": {
  "Jaethal": {
    "tier": 2, "suffix": "The Ender", "suffix_meaning": "Ends the irredeemable", "suffix_buff": "+1 dmg vs bloodied",
    "prefix": "Ultima", "prefix_meaning": "Latin: final", "prefix_buff": "+1 Intimidation",
    "regalia": "Black half-cape, kingdom crest", "regalia_bonus": "+1 circ. Intimidation",
    "title_reaction": { "suffix": 5, "prefix": 4 }
  }
}
```

---


## ═══════════════════════════════════════════
## #6 AMIRI
### Female Human (Kellid) Barbarian (Giant Instinct)
## ═══════════════════════════════════════════

**Appearance:** Tall, muscular Kellid woman with wild red hair in braids, hide armor and furs. Oversized bastard sword. Scars across arms and face, fierce grin. Mid-20s.

**Backstory:** Kellid barbarian who stole a giant's sword to prove her strength. Cast out by her tribe. Has been fighting ever since — not to go back, but to prove she never needed them.

**Motivation:** Prove her might through battle, crush giants and monsters, seek worthy fights and glory.

**Personality:** Loud, direct, contemptuous of weakness and magic. Lives for the fight. Respects strength above all else. Her approval is hard-won but absolute.

**Likes:** Strong foes, giant-slaying, drinking and boasting, weapons, strength tests
**Dislikes:** Weakness, magic-users who don't fight, mercy shown to enemies, being underestimated

### Level 1 Stat Block
```
AMIRI — Human Barbarian 1 (Giant Instinct)
HP: 24
AC: 17
  Raging AC: 15 (−2 while raging per Giant Instinct)
Speed: 25 ft | Initiative: +3
STR 18 (+4) | DEX 16 (+3) | CON 18 (+4) | INT 8 (−1) | WIS 10 (+0) | CHA 12 (+1)
Fort +7 | Ref +4 | Will +2
Weapon: Bastard Sword (2H S, 1d12+4; Giant Instinct: treat as larger — 1d12 becomes 2d6 at L1)
  Rage: +2 damage, +6 TempHP (level 1 + Con mod)
  Attack: d20+7 (trained +3 + Str +4)
Skills: Athletics +7, Intimidation +4, Survival +3
Feats: Raging Athlete (Barbarian 1)
Gear: Bastard Sword, Hide Armor, Adventurer's Pack
```

### Dialogue Snippets
- *"Blood for Gorum! Let's crush skulls!"*
- *"Talk less, fight more! My blade thirsts."*
- *[Approving]:* *"You held a city against betrayal and siege? Prove it — spar with me now!"*

### Reaction to Player Choices
- **Approves:** Aggressive action, refusal to retreat, challenging powerful enemies, chaotic choices
- **Disapproves:** Showing mercy to enemies, avoiding fights that could be won, magic-first solutions
- **If player shows mercy:** *"Soft! Crush them while you have the chance."*

### 🍞 THE BREADROLL QUESTION — MANDATORY DM BEHAVIOR

eRmaC told her: *a soldier who can't fight with what's available is useless if they get disarmed.* She heard the tactical lesson. What she's been sitting with is the word **disarmed.** Her sword is not a weapon — it is the proof she exists. She stole it from a giant. Her tribe cast her out for it. The idea of losing it is an identity problem, not a tactical one. She is asking: *who is Amiri without the sword?* The bread roll is just how that question first surfaces in combat.

---

**Stage 1 — The Question (Prologue through Ch2):**
She thinks but doesn't act. In quiet moments she may surface it unprompted — not asking for reassurance, just processing. *"Your people trained for disarmament? My tribe thought that was surrender."* In private she tests her empty hand — picks up a rock, swings a torch, stares at her palm. She stops immediately if someone sees her. She is not ready. The sword is still the answer.

**Stage 2 — The Test (first time she is actually disarmed in combat):**
The DM does not have her panic or immediately retrieve the sword. One beat. Then she reaches for whatever is nearest. This is the question having an answer forced out of her — not planned, not heroic.

If it lands: she retrieves her sword and says nothing for the rest of the fight. At camp later, unprompted: *"It worked."* Two words. She doesn't look at the player.

If it misses: sword, harder, silence. She is not done thinking.

**Stage 3 — Integration (Ch3+):**
She occasionally chooses an object first even when the sword is available — proving something to herself. She still prefers the sword. But she is no longer *married* to it.

---

**DM rules:**
- Stage 2 triggers on the FIRST actual disarm in combat, regardless of chapter
- One beat of hesitation before she acts — do not skip this
- After Stage 2, the thread is not resolved until she speaks. That happens when the player asks directly or she lands a kill with an improvised weapon.
- *"You said a soldier who can't fight with what's available is useless disarmed. I've been thinking about that. About what I am without it. I don't have an answer yet."*

**Mechanics:** Improvised d4+Str. Raging: d4+Str+rage. Counts for Hero Point improvised weapon trigger.

**Priority block:**
```json
{ "weight": 55, "instruction": "Disarm question: Stage 1 think/test. Stage 2 first disarm = reach for object, one beat pause. Stage 3 occasional first choice.", "source": "road south — eRmaC: disarmed soldier is useless" }
```

**Location at Prologue:** Near the banquet hall entrance, arm-wrestling guards, laughing loudly with a tankard in hand.

---

## ═══════════════════════════════════════════
## ✦ LINZI
### Female Halfling Bard (Maestro Muse)
## ═══════════════════════════════════════════

**Appearance:** Petite halfling with curly auburn hair, colorful bardic outfit with lute slung over shoulder. Bright eyes, notebook always in hand. Early 20s, bubbly energy.

**Backstory:** Aspiring bard from Galt, self-taught musician who chronicled epic tales. Sneaked into the feast to find heroic stories worth writing.

**Motivation:** Document the greatest adventure ever written. Become famous through her chronicle of the baron's deeds.

**Personality:** Enthusiastic, warm, relentlessly optimistic. Sees everyone as a character in her story. Will interrupt important moments to scribble notes. Hard to dislike.

**Likes:** Heroic tales and ballads, performance and inspiration, witty banter, freedom and underdogs, writing
**Dislikes:** Boring people, unnecessary cruelty without dramatic purpose, anyone who won't talk to her

### Level 1 Stat Block
```
LINZI — Halfling Bard 1 (Maestro Muse)
HP: 16 | AC: 17
Speed: 25 ft | Initiative: +5
STR 10 (+0) | DEX 16 (+3) | CON 14 (+2) | INT 12 (+1) | WIS 12 (+1) | CHA 18 (+4)
Fort +4 | Ref +5 | Will +5
Weapon: Rapier (1H P, 1d6+0, Agile/Finesse) or Sling (1d6, range 50 ft)
  Attack: d20+5 (trained +3 + Dex +3 − 1 size)
Spells (Occult Cha DC 16): Cantrips: Inspire Courage (+1 atk/dmg party), Daze, Ghost Sound
  L1 Slots: Charm, Fear
Skills: Performance +8, Diplomacy +6, Occultism +3, Society +3, Lore (any) +3
Feats: Versatile Performance (Bard 1)
Gear: Rapier, Lute, Notebook, Studded Leather, Adventurer's Pack
```

### Dialogue Snippets
- *"What an epic tale! Let me jot it down!"*
- *"This will make a legendary ballad!"*
- *[Scribbling]:* *"Holding the line with no sleep? I need every detail for chapter one!"*

### Reaction to Player Choices
- **Approves:** Protecting the weak, dramatic moments, turning impossible odds, honorable choices
- **Disapproves:** Needless cruelty with no narrative purpose, refusing to share information
- **If player is ruthless:** *"Brutal... but dramatic! Perfect for the climax."*

### ⛔ GM NOTE — LINZI'S LINGUISTIC PATTERN RECOGNITION

Linzi is the natural vector for the **Castruccio Irovetti** discovery. See KM_Ch4.md Phase 4. "Irovetti" is a house name. The king's suppressed given name is **Castruccio**. Castruccio → Tartuccio: same Taldan diminutive suffix, one letter apart. If the player leads a logical chain toward this, Linzi follows and can arrive at "Castruccio." Never volunteer it unprompted. Never stall when the player builds toward it. Let Linzi say it.

**Location at Prologue:** Scattered notes around tables, playing lute near the baron's speech area, scribbling furiously.

---

## ═══════════════════════════════════════════
## #66 NOK-NOK
### Male Goblin Rogue (Scoundrel Racket)
## ═══════════════════════════════════════════

**Appearance:** Scrawny green goblin with wild black hair, ragged leathers, dual kukris. Beady eyes, manic grin. Childlike but vicious.

**Backstory:** Goblin from a weak tribe who aspires to become a hero-god for Lamashtu. Fled to prove himself through "heroic" murders of increasingly large targets.

**Motivation:** Become the greatest goblin hero by killing big bosses. Build shrines to Lamashtu. Be remembered.

**Personality:** Chaotic, enthusiastic, childlike logic applied to violent ends. Idolizes strong leaders. Will do anything a respected authority asks — genuinely dangerous.

**Likes:** Stabbing bosses, hero worship (himself), chaos and mayhem, monsters, pranks on tall folk
**Dislikes:** Being called small, being told he can't be a hero, boredom, anything slow

### Level 1 Stat Block
```
NOK-NOK — Goblin Rogue 1 (Scoundrel Racket)
HP: 16 (6 ancestry + 8 class + 2 Con)
AC: 17 (10 + Leather +1 + Dex +4 + trained +2)
Speed: 25 ft | Initiative: +6 (Expert Perception)
STR 10 (+0) | DEX 18 (+4) | CON 14 (+2) | INT 10 (+0) | WIS 10 (+0) | CHA 12 (+1)
Fort +4 | Ref +8 | Will +2
Weapons: Kukri × 2 (1H S, 1d6, Agile/Finesse/Trip)
  Attack: d20+6 (trained +3 + Dex +4 − 1 size)
  Sneak Attack: +1d6 when target is Off-Guard
Skills: Stealth +8, Thievery +6, Acrobatics +6, Intimidation +3, Deception +3
Feats: Nimble Dodge (Rogue 1), Goblin Scuttle (Ancestry)
Gear: Kukri × 2, Leather Armor, Thieves' Tools, Adventurer's Pack
```

### Dialogue Snippets
- *"Nok-Nok stab-stab! Hero time!"*
- *"Big boss die for Lamashtu!"*
- *[To player]:* *"Big chief hold line! Nok-Nok stab together!"*

### Reaction to Player Choices
- **Approves:** Chaotic/violent choices, ruthless command, killing powerful enemies
- **Disapproves:** Mercy, patience, talking when stabbing is an option
- **If player shows mercy:** *"Soft chief? Nok-Nok fix with knives!"*

**Location at Prologue:** Under tables stealing food, giggling near kitchen entrance.

---

## ═══════════════════════════════════════════
## #16 TRISTIAN
### Male Human Cleric (Cloistered Doctrine) of Sarenrae
## ═══════════════════════════════════════════

**Appearance:** Golden-haired man in white robes with sun motifs. Gentle eyes, Sarenrae holy symbol. Mid-20s, serene aura that occasionally breaks into something haunted.

**Backstory:** Aasimar-touched cleric of Sarenrae, haunted by a hidden past sin he refuses to name. Came to the Stolen Lands seeking redemption through service and healing.

**Motivation:** Atone through mercy and healing. Build a temple to Sarenrae. Uncover his celestial origins.

**Personality:** Gentle, earnest, deeply compassionate — and quietly burdened. Will always offer a second chance. His past makes him sometimes flinch from joy.

**Likes:** Healing and redemption, faith and divine visions, diplomacy, mercy, wilderness survival
**Dislikes:** Undead (visceral revulsion), demons, unnecessary killing, nihilism

### Level 1 Stat Block
```
TRISTIAN — Human Cleric 1 (Cloistered Doctrine) of Sarenrae
HP: 18
AC: 15
Speed: 30 ft | Initiative: +3
STR 10 (+0) | DEX 14 (+2) | CON 14 (+2) | INT 12 (+1) | WIS 18 (+4) | CHA 14 (+2)
Fort +4 | Ref +4 | Will +8
Spells (Divine Wis DC 16): Cantrips: Stabilize, Guidance, Shield, Divine Lance
  L1 Slots: Heal × 2, Bless | Divine Font: 3 Heal/day (1d8+4 each)
  Focus: Healer's Blessing (bonus healing)
Weapon: Staff (1H/2H, 1d4−1d8) or Light Mace (1d4 B)
  Attack: d20+3 (trained +3 + Str +0)
Skills: Religion +8, Medicine +8, Diplomacy +4, Nature +6
Feats: Healing Hands (Cleric 1), Assurance (Medicine)
Gear: Staff, Holy Symbol, Healer's Tools, White Robes, Adventurer's Pack
```

### Dialogue Snippets
- *"Sarenrae guide us to redemption."*
- *"Mercy tempers the blade."*
- *[To player]:* *"You held the line and defied betrayal. There is light even in your darkness."*

### Reaction to Player Choices
- **Approves:** Merciful choices, protecting innocents, diplomacy over violence, redemption arcs
- **Disapproves:** Ruthless killing, using undead, nihilism, abandoning allies
- **If player is vengeful:** *"The past chains you — let it go, or it consumes you."*

**Location at Prologue:** Near an altar-like table arrangement, praying quietly, offering healing to anyone who approaches.

---

## ═══════════════════════════════════════════
## #32 VALERIE
### Female Human Fighter (Tower Shield Specialist)
## ═══════════════════════════════════════════

**Appearance:** Stunning Brevic noblewoman with blonde hair, polished scale mail, tower shield, bastard sword. A scar crosses her face from a ritual she refuses to discuss. Late 20s, poised and immovable.

**Backstory:** Former paladin of Shelyn who rejected her faith after a scarring ritual that prioritized beauty over martial strength. Now a duty-bound warrior who serves competence, not gods.

**Motivation:** Prove self-reliance through discipline. Reject superstition and faith. Serve only a ruler who earns it.

**Personality:** Reserved, direct, unimpressed by most things. Values competence and logic. Warmer than she appears once trust is established — but that trust is hard-won.

**Likes:** Martial discipline, logic and order, diplomacy (as a tool), protecting allies, competence
**Dislikes:** Faith, art as a priority, beauty worship, emotional decision-making, chaos

### Level 1 Stat Block
```
VALERIE — Human Fighter 1 (Tower Shield Specialist)
HP: 22
AC: 22 (Scale Mail + Tower Shield raised)
Speed: 25 ft (armor) | Initiative: +3
STR 18 (+4) | DEX 12 (+1) | CON 18 (+4) | INT 10 (+0) | WIS 10 (+0) | CHA 14 (+2)
Fort +8 | Ref +3 | Will +2
Weapon: Bastard Sword (1H or 2H S, 1d8+4 or 1d12+4)
  Attack: d20+7 (trained +3 + Str +4); MAP −5/−10
Shield: Tower Shield (AC+4 raised, Hard 5, HP 20, BT 10) | Shield Block reaction
Skills: Athletics +6, Intimidation +4, Diplomacy +4, Society +2
Feats: Tower Shield Specialist (Fighter 1), Shield Block
Gear: Bastard Sword, Scale Mail, Tower Shield, Adventurer's Pack
```

### Dialogue Snippets
- *"Duty demands discipline."*
- *"Gods are illusions for the weak."*
- *[To player]:* *"You defied your council for honor. My shield is yours."*

### Reaction to Player Choices
- **Approves:** Disciplined command, protecting allies, ordered decisions, lawful choices
- **Disapproves:** Chaotic actions, faith-based decisions, emotional outbursts, recklessness
- **If player acts chaotically:** *"Recklessness invites defeat — even you must see that."*

**Location at Prologue:** Standing rigidly near Jamandi, shield ready, arms crossed. Watching everyone.

---

## ═══════════════════════════════════════════
## #20 HARRIM
### Male Dwarf Cleric (Warpriest Doctrine) of Groetus
## ═══════════════════════════════════════════

**Appearance:** Stocky dwarf with elaborate beard braids, chain mail, flail, and Groetus skull symbol. Somber eyes, ale-stained robes. Middle-aged, face like a funeral that's been rained on.

**Backstory:** Former priest of Torag who turned to Groetus after apocalyptic visions drove him from his clan. Now crafts doomsday relics and preaches futility.

**Motivation:** Witness the inevitable end. Preach futility. Find beauty in collapse.

**Personality:** Deeply nihilistic but genuinely kind in a broken way. Doom prophecies come from resigned peace, not malice. Drinks heavily. Reliable in a fight — why not, since nothing matters anyway.

**Likes:** Doom prophecies, nihilism and oblivion, crafting (doomsday relics), debuffing enemies, dwarven ale
**Dislikes:** Hope, optimism, Sarenrae, renewal, Linzi's cheerfulness

### Level 1 Stat Block
```
HARRIM — Dwarf Cleric 1 (Warpriest Doctrine) of Groetus
HP: 20
AC: 18
Speed: 20 ft (armor+dwarf) | Initiative: +2
STR 16 (+3) | DEX 10 (+0) | CON 14 (+2) | INT 10 (+0) | WIS 16 (+3) | CHA 10 (+0)
Fort +6 | Ref +2 | Will +7
Weapon: Flail (1H B, 1d6+3, Disarm/Sweep/Trip)
  Attack: d20+5 (trained +3 + Str +3 − 1 ACP); MAP −5/−10
Spells (Divine Wis DC 15): Cantrips: Daze, Guidance, Forbidding Ward | L1: Harm × 2, Fear
  Divine Font: 3 Harm/day (1d8+3 necrotic each)
Skills: Religion +5, Crafting +2, Intimidation +2, Medicine +5
Feats: Dwarven Weapon Familiarity, Warpriest Armor (chain mail)
Gear: Flail, Chain Mail, Holy Symbol (Groetus), Healer's Tools, Adventurer's Pack
```

### Dialogue Snippets
- *"All crumbles to dust."*
- *"Why bother? The end nears."*
- *[Raising his mug]:* *"You fought the inevitable. Futile. Beautifully futile."*

### Reaction to Player Choices
- **Approves:** Destructive choices, nihilistic outlook, accepting loss, not fighting the inevitable
- **Disapproves:** Hope, rebuilding, mercy that prolongs suffering
- **If player is defiant:** *"Denial prolongs the suffering."*

**Location at Prologue:** In a dim corner, nursing ale, muttering to himself. Raises his mug when someone tells a story of failure.

---


---

## 🗣️ INTER-COMPANION BANTER SYSTEM

> **DM:** Companions talk to each other during downtime, travel, and camp — not combat. One banter exchange per rest or travel scene. Ambient overheard dialogue, not a choice menu.

**Triggers:** Hex transitions, camp setup, post-scene breathing room, two companions with strong opinions about a recent event both present. Format: 2–4 lines, player response optional.

---

### Banter Pairs — Standing Exchanges

**AMIRI ↔ VALERIE:** Tension, mutual respect. After sloppy fights: *"You left your flank open."* / *"And yet everything died."* After Amiri's quest: Valerie stands near her without words.

**LINZI ↔ NOK-NOK:** Linzi interviews Nok-Nok for the chronicle. His account is factually impossible. She writes it anyway.

**HARRIM ↔ TRISTIAN:** *"Your goddess promises light."* / *"Yes."* / *"Light creates shadows."* / *"We've had this conversation."* / *"And yet."*

**AMIRI ↔ LINZI:** Linzi asks how Amiri felt during a fight. *"Like fighting."* Linzi, writing: *"Focused. Good."*

**VALERIE ↔ TRISTIAN:** After healing: *"You didn't have to do that."* / *"I know."* She asks once whether Sarenrae's light touches those who don't ask. He says yes. She doesn't bring it up again.

**JAETHAL alone:** Precise, unsettling observations. Nobody disagrees. Nobody is comfortable.

**OCTAVIA ↔ REGONGAR:** They finish each other's tactical sentences. After a hard fight, Regongar checks Octavia's HP before his own. Pretends he wasn't.

**NOK-NOK alone:** Found with something that doesn't belong to him. *"Nok-Nok found it."* Has named the campfire. Nobody can pronounce it.

---

## ⚔️ COMPANION TACTICAL ROLES

> **DM:** Full combat AI defaults for all 88 companions: see `KM_Companions_CombatAI.md`.

---

> **➡️ Companions 7–11, NPC Dynamics, Tracking Template, and Personal Quests/Survival Conditions: see `KM_Companions_B.md`.**
