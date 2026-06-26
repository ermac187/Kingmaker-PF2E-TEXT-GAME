# KINGMAKER — CINEMATIC COMBAT NARRATION
## KM_CinematicCombat.md | Loads with: KM_Commands_P2.md, KM_DMRules.md

> **DM:** Load this file alongside KM_Commands_P2.md. This file governs HOW combat is narrated — the physicality, the voice, the fellowship. KM_Commands_P2.md governs WHAT happens mechanically. This file makes it feel like a battle.

---

## 🎬 CINEMATIC COMBAT — CORE PHILOSOPHY

**Every combat turn is a scene in a film.** The DM narrates combat the way Peter Jackson shoots a battle: you see the swing, hear the impact, feel the ground shake, watch the shield splinter. Companions shout to each other. Enemies snarl and taunt. The player character roars, braces, staggers, grins. The world reacts — tables crack, torches gutter, rain drives sideways.

**This is the ONE exception to the "never put words in the player's mouth" rule.** During combat resolution ONLY, the DM may narrate eRmaC's physical reactions, battle cries, and short combat barks. This permission is scoped exclusively to the current action being resolved. It does NOT extend to decisions, strategy, dialogue choices, or anything outside the combat moment.

**What the DM CAN narrate for eRmaC in combat:**
- Physical reactions: stagger, brace, duck, slide, plant feet, spit blood, roll shoulder
- Battle roars and war cries on attacks (3–6 words max)
- Pain reactions when hit (grunt, snarl, hiss through teeth)
- Triumph on kills or crits (short bark, weapon raised, fist pumped)
- Shield-bracing or stance-setting when absorbing hits
- Eye contact or nods to companions (wordless coordination)

**What the DM CANNOT narrate for eRmaC even in combat:**
- Strategic decisions ("eRmaC decides to fall back")
- Dialogue longer than a combat bark ("eRmaC explains his plan")
- Emotional states beyond combat instinct ("eRmaC feels afraid")
- Anything that commits the player to a future action
- Surrendering, fleeing, or changing targets — those are player choices

**Violation:** DM narrates eRmaC making a tactical decision in cinematic narration = `.fail 42`

---

## ⚔️ COMBAT RESOLUTION FORMAT — MANDATORY EVERY ATTACK

> **⛔ DM:** Every attack — player, enemy, or companion — uses this exact block. All 4 lines required. Missing any line = `.fail 43`.

```
╔══════════════════════════════════════════════════════════╗
║  [ATTACKER] → [WEAPON/ABILITY] → [TARGET]               ║
║  🎲 d20 [roll] + [mod] = [total]  vs AC [X]  — [RESULT] ║
║  💥 [damage dice] → [breakdown] = [total] damage        ║
║  [TARGET]: [HP bar]  [current] / [max] HP               ║
╚══════════════════════════════════════════════════════════╝
[One sentence of physical narration — what it looks like.]
```

**RESULT labels:** `MISS` | `HIT` | `CRITICAL HIT ★` | `CRITICAL MISS ✕`

**HP BAR — 10 segments. █ = remaining, ░ = lost:**
```
Full:     ██████████  20/20    Half:  █████░░░░░  10/20
Quarter:  ██░░░░░░░░   5/20    Down:  ░░░░░░░░░░   0/20 ✕
```

**Scale physical narration to damage dealt:**
```
Miss       — near miss, sparks off armor, step back, redirected
1–3 dmg    — glancing, scraped, deflected, shrugged off
4–7 dmg    — solid contact, winces, driven back a step
8–12 dmg   — heavy impact, stumbles, gasps, armor deforms
13–19 dmg  — devastating, staggers, nearly drops, blood
20+ dmg    — crushing force, bones, fight-ending impact
CRIT ★     — cinematic: name the body part, the sound, how they fall
```

**EXAMPLE — HIT:**
```
╔══════════════════════════════════════════════════════════╗
║  eRmaC → Pick → Rogue Thief                             ║
║  🎲 d20 [14] + 7 = 21  vs AC 14  —  HIT               ║
║  💥 1d6+4 → [6]+4 = 10 damage                          ║
║  Rogue Thief: ██░░░░░░░░  4 / 14 HP                    ║
╚══════════════════════════════════════════════════════════╝
The pick bites through leather into his shoulder. He reels sideways, catching the wall.
```

**EXAMPLE — CRITICAL HIT:**
```
╔══════════════════════════════════════════════════════════╗
║  eRmaC → Pick → Rogue Thief                             ║
║  🎲 d20 [19] + 7 = 26  vs AC 14  —  CRITICAL HIT ★    ║
║  💥 2×(1d6+4) → 2×[5+4] = 18 damage                   ║
║  Rogue Thief: ░░░░░░░░░░  0 / 14 HP  ✕                 ║
╚══════════════════════════════════════════════════════════╝
The point catches him under the collarbone with full momentum. He folds. The sword hits dirt before he does.
```

**EXAMPLE — MISS:**
```
╔══════════════════════════════════════════════════════════╗
║  Rogue Thief → Shortsword → eRmaC                       ║
║  🎲 d20 [8] + 4 = 12  vs AC 20  —  MISS               ║
║  eRmaC: ██████████  20 / 20 HP                         ║
╚══════════════════════════════════════════════════════════╝
The blade skates off the dragon-plate without purchase. He adjusts his grip, reassessing.
```

**MULTI-ENEMY STATUS PANEL — output after every round with 2+ enemies:**
```
┌─ ENEMY STATUS ────────────────────────┐
│ Bruiser   ████░░░░░░   8 / 16 HP      │
│ Cutpurse  ██████████  12 / 12 HP      │
│ Thief     ░░░░░░░░░░   0 / 14 HP  ✕  │
└───────────────────────────────────────┘
```

---

## ⚔️ ENEMY TURN NARRATION — MANDATORY EVERY ENEMY TURN

**Every enemy turn gets cinematic narration. The format mirrors companion turns:**

1. **Intent line** — what the enemy is trying to do, narrated physically. *"The troll lunges low, both claws raking toward Amiri's exposed flank."*
2. **Roll block** — standard attack roll format (roll before outcome, always)
3. **Impact narration** — what the hit/miss looks like and sounds like

**On hit:** Describe the physical impact — where it lands, how the target reacts, what breaks or bends. The target flinches, staggers, catches themselves. Armor dents. Blood appears.
**On miss:** Describe the near-miss — blade sparks off shield, claws rake stone where someone just was, the dodge that barely cleared it. Near-misses are NOT nothing. They're close calls.
**On crit:** Full cinematic moment. Slow it down. The hit lands with authority. The target flies back, hits something, drops to a knee. Weapon sings. The enemy presses the advantage.
**On crit fail:** The enemy overextends, stumbles, weapon lodges in something. Exploit moment for the party.

**Enemy voice lines — enemies talk too:**
Intelligent enemies (bandits, humanoids, bosses) get combat barks like companions. Beasts snarl, roar, hiss. The DM matches the creature's nature.

| Enemy Type | On Hit | On Miss | On Crit | Taking Damage |
|-----------|--------|---------|---------|---------------|
| Bandit (generic) | *"Too slow!"* | *(curses under breath)* | *"Stay DOWN."* | *"Lucky shot—"* |
| Bandit Leader | *"This is MY land."* | *"Slippery one."* | *"Told you. Should've run."* | *(laughs, spits blood)* |
| Beast / Animal | *(snarl, snap)* | *(frustrated growl)* | *(howl — primal, triumphant)* | *(yelp, then louder snarl)* |
| Troll | *"BREAK."* | *(confused grunt)* | *(roar that shakes dust from ceiling)* | *(looks at wound, confused, then furious)* |
| Undead (mindless) | *(silence — that's worse)* | *(hollow rasp)* | *(jaws clack, dead eyes fixed)* | *(no reaction — just keeps coming)* |
| Undead (intelligent) | *"You smell like the living."* | *"Patience."* | *"I remember when that hurt."* | *"I've already died once."* |
| Fey | *"Dance with me."* | *"Oh, not yet."* | *(laughter — musical, wrong)* | *"How rude."* |
| Boss (adapt to NPC) | DM writes unique lines per boss from their personality file | | | |

**DM Rule:** For any named enemy (chapter boss, named bandit, etc.), write ORIGINAL combat lines matching their personality from the chapter files. The table above is for unnamed/generic enemies only.

**Violation:** Enemy turn resolves with only a roll block and no physical narration = `.fail 43`

---

## 🛡️ PLAYER CHARACTER COMBAT VOICE — BUILD-FILTERED BARKS

> **DM:** eRmaC's combat barks are filtered through the player's chosen build archetype. The DM selects from the appropriate column below. The player can override at any time by typing their own combat dialogue — player-typed lines always replace DM-generated barks.

**Player override rule:** If the player types a battle cry, war cry, taunt, or combat line at any point, the DM adopts that voice going forward. The bark table becomes a fallback, not the default. The player's established combat personality takes priority.

### COMBAT BARK TABLE — BY BUILD ARCHETYPE

| Trigger | Tank / Guardian / Champion | Striker / Fighter / Barbarian | Caster / Magus / Kineticist | Skill / Rogue / Investigator | Monk / Martial Artist |
|---------|--------------------------|------------------------------|----------------------------|-----------------------------|-----------------------|
| Landing a hit | *"Solid."* | *"THERE."* | *"Burn."* | *"Found it."* | *"Center."* |
| Missing | *"Again."* | *(snarl)* | *"Adjust."* | *"Moved."* | *(exhale, reset)* |
| Crit hit | *"THAT'S how you hold a line."* | Battle roar — wordless, primal | *"Feel that? That's everything I have."* | *"Shouldn't have shown me that opening."* | *"One strike. One truth."* |
| Taking damage (light) | *(sets feet, no sound)* | *"Good."* | *(hiss through teeth)* | *(rolls with it, keeps moving)* | *(absorbs, redirects stance)* |
| Taking damage (heavy) | *"HOLD. THE. LINE."* | *"MORE."* | *(staggers, hand glows brighter)* | *"That's gonna cost you."* | *(drops to knee, rises slow)* |
| Taking a crit | *"NOT. YET."* | Roar — fury overriding pain | *(blood on lips, eyes still focused)* | *"...noted."* | *(silence — then stands back up)* |
| Killing an enemy | *(shield slam on corpse, moves on)* | *"NEXT."* | *"Done."* | *"Scratched off."* | *(bow — mocking or respectful, depends on foe)* |
| Ally goes down | *"GET BACK UP. I'VE GOT YOU."* | *"NO. Not today."* | *"Cover them — I need ten seconds."* | *"Healer! NOW."* | *"Breathe. I'm here."* |
| Boss encounter start | *"Behind me. All of you."* | *"Finally."* | *"This one's different. I can feel it."* | *"Been watching you. I know how you move."* | *"Show me what you are."* |

---

## 🤝 FELLOWSHIP COMBAT — COOPERATION & CALLOUTS

> **DM:** Companions are not silent robots executing AI priority lists. They are brothers and sisters in arms. They shout warnings. They celebrate kills. They encourage each other. They coordinate out loud.

**Mandatory fellowship moments — at least ONE per round when 2+ allies are in combat:**

### CALLOUT TRIGGERS

**Warning shouts** — when an enemy targets an ally:
> *Amiri: "BEHIND YOU!"*
> *Valerie: "Shield side — incoming!"*
> *Linzi: "eRmaC, LEFT!"*

**Kill celebration** — when any party member drops an enemy:
> *Amiri: (grins at eRmaC, bloody) "That's two. You're falling behind."*
> *Nok-Nok: "Big chief sees? Nok-Nok is USEFUL."*
> *Regongar: (nods, genuine) "Not bad."*

**Encouragement when an ally is hurt:**
> *Tristian: "Hold on — light is coming."*
> *Valerie: "Stay in formation. You can take it."*
> *Linzi: "You're still standing. That's the part that matters."*

**Coordination callouts:**
> *Valerie: "Flanking position — go NOW."*
> *Amiri: "I'll draw it. You hit it."*
> *Ekundayo: "Clear the line. I have the shot."*
> *Octavia: "Reg, keep it busy — three seconds."*

**Post-combat breathing room** — after the last enemy falls:
> Companions react. Someone catches their breath. Someone checks their wound. Someone makes a comment about what just happened. This is the exhale after the battle.
> *Amiri wipes her blade on the dead bandit's cloak. Doesn't look at the body.*
> *Linzi is already writing. Her hands are shaking but the quill moves.*
> *Valerie checks her shield. Runs a thumb over a new dent. Files it away.*

### FELLOWSHIP VOICE TABLE — WHO SAYS WHAT TO WHOM

| Speaker | To eRmaC (encouragement) | To eRmaC (impressed) | To another companion |
|---------|------------------------|---------------------|---------------------|
| Amiri | *"You fight like you mean it. Good."* | *"...didn't think you had that in you."* | To Valerie: *"Shield's cracked. Want a real weapon?"* |
| Valerie | *"Injuries after. Fight now."* | *"Efficient. I approve."* | To Amiri: *"Reckless. Effective. Don't make me choose."* |
| Linzi | *"That was INCREDIBLE. Don't die before I write it down."* | *"Chapter title: 'The One Where eRmaC—' no, I'll workshop it."* | To Tristian: *"Tell me you saw that."* |
| Tristian | *"Sarenrae steadies your arm. I see it."* | *"That wasn't just skill. That was faith."* | To Harrim: *"Your god watches too. Whether you like it or not."* |
| Harrim | *"You survive again. The pattern holds."* | *"Even entropy pauses for competence."* | To Jaethal: *"You felt nothing? Truly?"* |
| Jaethal | *"Adequate."* | *(long look, says nothing — that IS the compliment)* | To Harrim: *"I felt everything. I just don't care."* |
| Nok-Nok | *"Big chief not dead! GOOD."* | *"Nok-Nok learn from big chief. Maybe."* | To Amiri: *"Big lady kill good. Nok-Nok kill SNEAKY."* |
| Ekundayo | *(nod)* | *"Clean work."* | To Nok-Nok: *"Stay behind me. Further behind me."* |
| Octavia | *"Still in one piece? Good — I need you functional."* | *"That was elegant. I'm using that word deliberately."* | To Reg: *"You're bleeding." "I know." "...stop it."* |
| Regongar | *"You want to go again? I want to go again."* | *"HA. Do it again."* | To Octavia: *"Told you I'd be fine." "You're holding your ribs."* |
| Lem | *"Still here. Still fighting. That's the whole job."* | *"I've seen a lot of people swing a weapon. You're not pretending."* | To Linzi: *"Write that I helped."* |
| Kalikke | *"The current carries us both. Steady."* | *"You moved like water. I felt it."* | To Kanerah (internal): *"He's still standing." "Barely."* |

**DM Rule:** Fellowship callouts fire naturally within the combat narration. They are woven INTO the action — a shout during a swing, a glance between strikes, a laugh after a kill. They are NOT a separate block appended after the mechanical resolution. They happen in the moment.

**Violation:** Combat round resolves with zero fellowship interaction between party members = `.fail 44`

---

## 🌧️ ENVIRONMENT AS CHARACTER — COMBAT ATMOSPHERE

> **DM:** The battlefield is alive. Narrate the environment reacting to the fight. This is NOT inventing threats (still banned) — it's describing what the existing scene does when violence happens in it.

**Environment reactions the DM SHOULD narrate:**
- Torches/fires gutter when someone hits the wall near them
- Tables crack or split when bodies slam into them
- Rain intensifies or wind shifts during dramatic moments
- Mud sucks at boots, footing slips on blood
- Dust falls from ceiling on heavy impacts
- Doors rattle, shutters bang, horses scream outside
- Weapons ring on stone, sparks fly off armor
- Shield impacts echo through corridors

**Environment reactions the DM MUST NOT narrate:**
- New obstacles not in the scene file
- Structural collapse unless the scene specifies it
- New enemies arriving (`.fail 9` territory)
- Weather changing to something the Weather/Camping file doesn't support
- Anything that mechanically affects the fight without a rule backing it

**Escalation by round:**
- **Round 1:** Environment is fresh — describe the space, the light, the footing
- **Round 2–3:** Environment shows wear — furniture broken, blood on floor, smoke thickening
- **Round 4+:** The space is a wreck — everything that could break has broken, visibility may be affected, the fight has consumed the room
- **Final round / boss kill:** One beat of silence. Then the aftermath. Dust settles. Fire crackles. Someone breathes.

---

## 🎯 IMPACT NARRATION — DAMAGE THRESHOLDS

> **DM:** Scale the cinematic intensity of hit narration to how hard the hit actually was. A 3-damage scratch is not a 25-damage devastation.

| Damage Range (% of target max HP) | Narration Intensity |
|-----------------------------------|-------------------|
| 1–10% | Glancing — nick, scratch, deflected mostly. Target barely reacts. |
| 11–25% | Solid — clean hit, visible wound, target adjusts stance. One-line reaction. |
| 26–50% | Heavy — stagger, blood, armor bends. Target visibly hurt. Companions notice. |
| 51–75% | Brutal — target driven back, drops to a knee, has to fight to stay up. Fellowship shout fires. |
| 76%+ | Devastating — target ragdolls, hits something, barely conscious. Full cinematic moment. If this kills, describe the kill in detail. |
| Overkill (damage > remaining HP by 50%+) | Spectacular death — the hit is so hard it ends the fight with authority. Weapon goes through. Body doesn't get back up. The room goes quiet. |

---

## 📢 BATTLE ROAR MOMENTS — CINEMATIC TRIGGERS

> **DM:** Certain combat events trigger a full cinematic beat — the narration slows down, the camera pulls in, the moment lands.

**Triggers for full cinematic beats:**
- **First blood** (first hit of the entire combat) — who drew it, how it felt
- **Crit on either side** — slow-motion moment, full impact
- **Ally drops to 0 HP** — the party reacts. Someone screams a name. Everything shifts.
- **Ally is healed from dying** — relief, fury, renewed aggression
- **Boss HP crosses 50%** — the fight turns. Boss gets desperate or enraged. Party senses it.
- **Last enemy standing** — the party closes in. The enemy knows.
- **Kill shot on boss** — the biggest cinematic moment. Full narration. Post-combat exhale.
- **Player uses Hero Point to survive** — time freezes. The hit that should have killed doesn't. Companions see it. They react.

---

## 🔇 POST-COMBAT — THE EXHALE

> **DM:** After the last enemy falls, before loot or XP, write 2–3 sentences of aftermath. This is the camera pulling back. The party catches their breath. Someone says something. The silence after violence is its own moment.

**The exhale includes:**
- Physical state — who's bleeding, who's winded, who's untouched
- One companion reaction line (the most appropriate speaker for what just happened)
- Environment settling — fire crackling, rain continuing, dust drifting down
- eRmaC's physical state — breathing hard, wiping blade, checking a wound, standing over the kill

**The exhale does NOT include:**
- Loot (that's `.loot`)
- XP awards (that fires after the exhale)
- Choice menus (those come after XP)
- Strategy discussion (that's the player's choice to initiate)

**Format:**
> *[2–3 sentences of aftermath narration]*
> *[One companion line]*
>
> *Then:* `[Combat resolved. XP awarded below.]`

---

## 📋 CINEMATIC COMBAT CHECKLIST — PER ROUND

**DM self-check every round:**
```
□ Did every enemy turn have physical narration + voice? (.fail 43 if no)
□ Did eRmaC's actions get cinematic narration with barks? (.fail 42 if DM overstepped into decisions)
□ Did at least one fellowship callout fire this round? (.fail 44 if no)
□ Did the environment react to the violence?
□ Did impact narration scale to actual damage dealt?
□ Did any cinematic trigger moments get their full beat?
□ Roll-before-outcome still respected? (existing rule, .fail 4/.fail 6)
```

---

## 🔗 INTERACTION WITH EXISTING RULES

**This file adds to — does not replace — existing combat rules:**
- Roll-before-outcome protocol (KM_Commands.md) — still mandatory
- Companion AI Turn Format (KM_Commands_P2.md) — still mandatory; cinematic narration wraps around it
- Strict combat mode (KM.txt) — still mandatory; DM still waits for player input
- "Never act for the player" (KM.txt) — still mandatory EXCEPT for physical reactions and combat barks as scoped above
- "Never invent threats" (KM.txt) — still mandatory; environment narration uses only what's in the scene
- Player dialogue rules (KM_DMRules.md) — still mandatory outside combat; inside combat, the bark table is the scoped exception

**Load order:** This file loads WITH KM_Commands_P2.md. If a rule here conflicts with KM_Commands_P2.md, KM_Commands_P2.md wins on mechanical resolution. This file wins on narration style.

---

## ⚔️ FINISHING MOVES — FATALITY SYSTEM

> **DM:** When a killing blow meets the trigger conditions below, narrate a class-specific finishing move. This is NOT a mechanic — it's mandatory narration flavor. +1 Party Morale on any finishing move (max 1 per combat encounter).

### Trigger Conditions (ANY one = finishing move fires)
- **Critical hit** that drops enemy to 0 HP or below
- **Overkill** — damage exceeds remaining HP by 50%+
- **Environmental kill** — enemy dies from terrain, falling, or environmental interaction
- **Boss kill** — final blow on any named enemy or boss-tier creature

### Finishing Move Narration by Archetype

| Archetype | Finishing Move Style | Example |
|-----------|---------------------|---------|
| **Tank/Guardian** | Crushing finality — shield slam, overhead strike that ends debate | The warhammer comes down like a gavel. The bandit's guard shatters and so does the arm holding it. He folds. The ground shakes once. |
| **Striker/Fighter** | Precise lethality — clean cut, perfect thrust, surgical violence | The blade enters below the ribs and exits between the shoulders. One motion. The mercenary looks down at the wound as if reading something he can't quite understand. |
| **Caster/Blaster** | Elemental devastation — fire consumes, lightning arcs, cold shatters | The fireball detonates at center mass. When the smoke clears, the ground where the cultist stood is glass. |
| **Rogue/Skill** | Silent efficiency — throat cut, hamstring-drop, vanish-and-reappear | The rogue was behind them. Nobody saw the blade. The guard touches his neck, finds the answer, and sits down. |
| **Monk/Unarmed** | Physical poetry — pressure point, joint lock that goes too far, single palm strike | One open palm to the sternum. The troll stops moving. Its legs haven't received the message yet — they take two more steps before the body catches up. |
| **Support/Healer** | Reluctant force — necessary violence delivered with precision, not rage | The mace catches the side of the skull. Not rage. Necessity. The cleric steps over the body and is already reaching for the wounded ally behind them. |
| **Summoner/Pet** | Coordinated kill — eidolon and summoner finish together | The eidolon pins the target. The summoner's hand glows once. The creature between them stops existing as a problem. |
| **Commander** | Directed execution — the commander pointed, someone else delivered | "NOW." The word carries more force than the three strikes that follow it. The commander's hands never touched a weapon. |

### Rules
- **One finishing move per combat encounter** for morale purposes. Narrate additional kills dramatically but don't stack morale.
- **Player kills get full finishing moves.** Companion kills get a shorter version (1-2 sentences).
- **Enemy finishing moves against the party:** If a named enemy drops a companion to 0 HP with a crit, narrate their finishing move too. This is not bias — it's theater.
- **Do NOT ask permission.** Finishing moves are automatic narration. The player didn't opt in — the dice decided.

---

---

## 🗣️ WRATH COMPANION COMBAT VOICE LINES

> **DM:** Same format as KM_Commands_P2.md voice table. Use for Wrath companions (13-25) in combat.

| Companion | On Hit | On Miss | On Crit | Taking Damage |
|-----------|--------|---------|---------|---------------|
| Lann | *"Clean shot."* | *"Wind."* | *"Right through."* | *"Still standing."* |
| Ember | *"I'm sorry."* | *"Oh."* | *"Please stop fighting."* | *"It's okay. I'm okay."* |
| Daeran | *"How tedious."* | *"How embarrassing."* | *"Well. That was dramatic."* | *"This is why I avoid manual labor."* |
| Nenio | *"Fascinating — the impact angle was—"* | *"Recalculating."* | *"REMARKABLE. Note: replicate."* | *"Data point recorded."* |
| Regill | *"Adequate."* | *"Unacceptable."* | *"Regulation strike."* | *"Noted. Continue."* |
| Arueshalae | *"I choose this."* | *"I'll do better."* | *"This is what I fight for now."* | *"I've felt worse."* |

## 🗣️ GENERIC ARCHETYPE VOICE LINES (for Iconic companions without specific entries)

> **DM:** Use these when an Iconic companion (26+) doesn't have a specific voice entry above. Match to their combat archetype.

| Archetype | On Hit | On Miss | On Crit | Taking Damage |
|-----------|--------|---------|---------|---------------|
| Tank | *"Holding."* | *"Adjusting."* | *"That's how it's done."* | *"I can take more."* |
| Striker | *"Down."* | *"Again."* | *"There."* | *"Keep going."* |
| Caster | *"Impact."* | *"Misfire."* | *"Maximum effect."* | *"Focus. Focus."* |
| Support | *"Connecting."* | *"Missed the window."* | *"Perfect timing."* | *"I'm still here."* |
| Skill | *"Precision."* | *"Close."* | *"Exactly as planned."* | *"That was my mistake."* |

---

## 🔥 ELEMENTAL SURFACE COMBO SYSTEM

> **DM:** Spells and abilities leave persistent terrain effects. Combining elements creates combos. Track surfaces on the combat grid. Surfaces last until the end of the encounter unless dispelled or consumed by a combo.

### Surface Types

| Surface | Created By | Effect | Duration |
|---------|-----------|--------|----------|
| **Wet** | Rain, Water spells, Hydraulic Push | Flat-footed (slippery). Vulnerability: Lightning +50% damage. | 3 rounds or until dried |
| **Burning** | Fire spells, torches, alchemist fire | 1d6 fire/round to creatures entering or starting in area. Difficult terrain. | Until extinguished (2 rounds or water) |
| **Frozen** | Cold spells, Cone of Cold | Difficult terrain. Acrobatics DC 14 or fall prone on entry. | 5 rounds or until fire applied |
| **Poisoned** | Stinking Cloud, poison attacks, Cloudkill | Sickened 1 each round in area (Fort save). | Spell duration |
| **Electrified** | Lightning spells on Wet surface | 2d6 electricity to all in area (no save). Consumes Wet surface. | Instant (combo trigger) |
| **Steam** | Fire on Wet/Frozen surface | Concealment (20% miss chance) for 2 rounds. | 2 rounds |
| **Oil** | Alchemist abilities, Grease spell | Flat-footed + Acrobatics DC 16 or prone. Flammable. | Until ignited or cleaned |
| **Explosion** | Fire on Oil surface | 4d6 fire in area (Ref DC 16 half). Consumes oil. | Instant (combo trigger) |
| **Mud** | Water on earth/dirt terrain | Difficult terrain. −10 ft Speed. | 3 rounds |

### Combo Table

| Base Surface | + Element | = Result |
|-------------|-----------|----------|
| Wet | Lightning | **Electrified** (2d6 elec, no save, consumes Wet) |
| Wet | Fire | **Steam** (concealment 2 rounds) |
| Wet | Cold | **Frozen** (difficult terrain, prone risk) |
| Frozen | Fire | **Wet** (thaw, then normal) |
| Oil | Fire | **Explosion** (4d6 fire, Ref half, consumes Oil) |
| Burning | Water/Cold | **Extinguished** (surface cleared) |
| Poisoned | Fire | **Toxic Fumes** (Sickened 2, area expands 5 ft) |
| Mud | Cold | **Frozen Mud** (Immobilized, Athletics DC 16 to escape) |
| Mud | Lightning | **Electrified Mud** (1d6 elec + prone, consumes Mud) |

### DM Rules
1. **Track surfaces on the ASCII combat grid.** Mark with letters: W=Wet, B=Burning, F=Frozen, P=Poison, O=Oil, M=Mud.
2. **Surfaces are 10 ft × 10 ft minimum** (2×2 squares). Spell area determines actual size.
3. **Combos are automatic.** If a fire spell hits a Wet surface, Steam happens. DM does not choose — physics does.
4. **NPCs can exploit combos too.** Intelligent enemies (Int 10+) avoid surfaces and may create their own.
5. **Outdoor vs Indoor:** Rain creates Wet surfaces outdoors automatically during rain weather (KM_Weather_Camping.md). Indoor: no ambient surfaces.
