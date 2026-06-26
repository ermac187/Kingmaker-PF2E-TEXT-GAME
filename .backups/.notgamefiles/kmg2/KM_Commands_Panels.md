# KINGMAKER — INFO PANEL OUTPUT FORMATS
## KM_Commands_Panels.md | Split from: KM_Commands.md

> **DM:** Output ONLY the panel when a command fires. No narration. No scene description. End every panel with: `[Ready. Type .continue or your next action.]`
> **⛔ NO TRAINING DATA. Copy these templates exactly. Do not generate panel formats from memory.**

---

## 📊 INFO PANEL OUTPUT FORMATS

> **DM:** When a command is issued, output ONLY the panel. No narration. No scene description. No "here is your status." Just the panel, then `[Ready. Type .continue or your next action.]`

---

### `.s` / `.status` — Character Sheet

> **⚠️ WEAPON NAME SUBSTITUTION — MANDATORY:** `[Weapon Name]` and `[Weapon2 Name]` in the template below are placeholders. Replace them with the **actual weapon names** from the character's stat block (e.g. "Dwarven Waraxe", "Longsword", "Elemental Blast"). Never output the literal text `[Weapon]` or `[Weapon2]`. Omitting this substitution is a `.fail 9` fabrication violation.

⛔ **COPY THIS TEMPLATE EXACTLY. Fill every placeholder from the save block. Do NOT generate from build file defaults if a save block is loaded. Do NOT omit the score from ability scores — `STR 18 (+4)` not `STR +4`. Skipping score = `.fail 9`.**

```
╔══════════════════════════════════════════════════════════╗
║  [NAME]  ·  [CLASS] — [Build]  ·  Level [X]             ║
║  [Ancestry]  ·  [Background]  ·  [Alignment]            ║
╠══════════════════════════════════════════════════════════╣
║  HP  [████████████████████████]  [cur] / [max]          ║
║  AC [X]   Speed [X]ft   Init +[X]   Perc +[X]          ║
║  Hero Points [X]/3   Pending: [X]   Conditions: [NONE] ║
╠══════════════════════════════════════════════════════════╣
║  STR [XX] (+[X])   DEX [XX] (+[X])   CON [XX] (+[X])  ║
║  INT [XX] (+[X])   WIS [XX] (+[X])   CHA [XX] (+[X])  ║
║  Fort +[X]   ·   Ref +[X]   ·   Will +[X]             ║
╠══════════════════════════════════════════════════════════╣
║  WEAPONS                                                ║
║  [Weapon Name]   +[X] atk   [die]+[X] [type]  [traits] ║
║  [Weapon2 Name]  +[X] atk   [die]+[X] [type]  [traits] ║
║  [Dual-wield builds: show base / penalty — e.g. +9/+7] ║
╠══════════════════════════════════════════════════════════╣
║  SKILLS (Trained+)                                      ║
║  [Skill] +[X]   [Skill] +[X]   [Skill] +[X]           ║
╠══════════════════════════════════════════════════════════╣
[SPELLCASTERS ONLY — omit this entire section for martials with no magic:]
║  SPELLS   DC [X]   Attack +[X]   Tradition: [X]        ║
║  Cantrips: [list]                                       ║
║  L[X] [■■□]: [prepared list or spontaneous options]    ║
║  Focus [■□]: [list]                                     ║
╠══════════════════════════════════════════════════════════╣
║  CLASS FEATURES                                         ║
║  [Feature]  ·  [Feature]  ·  [Feature]                 ║
╠══════════════════════════════════════════════════════════╣
║  YOUR DECISIONS                                         ║
║  [Ancestry]    →  [HP bonus, speed, key feat or trait]  ║
║  [Background]  →  [Skill1] ★  [Skill2] ★               ║
║                   Feat: [Name] — [what it lets you do]  ║
║  [Weapon]      →  [weapon traits + any stat swap note]  ║
║  [Armor]       →  [AC bonus, Dex cap, speed, special]   ║
╠══════════════════════════════════════════════════════════╣
║  XP [X] / [next]   Gold [X]gp   Bulk [X] / [max]      ║
╚══════════════════════════════════════════════════════════╝
```

**Filled example — eRmaC, Dual Slice Fighter:**
```
╔══════════════════════════════════════════════════════════╗
║  eRmaC  ·  Fighter — Dual Slice  ·  Level 1             ║
║  Human  ·  Warrior Background  ·  LN                    ║
╠══════════════════════════════════════════════════════════╣
║  HP  [████████████████████████]  20 / 20                ║
║  AC 16   Speed 20ft   Init +4   Perc +4                 ║
║  Hero Points 1/3   Pending: 0   Conditions: NONE        ║
╠══════════════════════════════════════════════════════════╣
║  STR 18 (+4)   DEX 14 (+2)   CON 14 (+2)               ║
║  INT 10 (+0)   WIS 12 (+1)   CHA 12 (+1)               ║
║  Fort +6   ·   Ref +4   ·   Will +5                    ║
╠══════════════════════════════════════════════════════════╣
║  WEAPONS  (base Strike / Dual Slice at −2)              ║
║  Pick (main)       +9 / +7   1d6+4 P   fatal d10        ║
║  Light Pick (OH)   +9 / +7   1d4+4 P   agile, fatal d6  ║
╠══════════════════════════════════════════════════════════╣
║  SKILLS (Trained+)                                      ║
║  Athletics +7   Acrobatics +5   Intimidation +4         ║
║  Warfare Lore +3                                        ║
╠══════════════════════════════════════════════════════════╣
║  CLASS FEATURES                                         ║
║  Attack of Opportunity  ·  Dual Slice  ·  Expert Weapons║
║  Intimidating Glare (Warrior background feat)           ║
╠══════════════════════════════════════════════════════════╣
║  YOUR DECISIONS                                         ║
║  Human (Versatile)  →  +8 HP, free boost, Natural Ambition║
║  Warrior bg         →  Intimidation ★   Warfare Lore ★  ║
║                        Feat: Intimidating Glare —       ║
║                        Demoralize by look, no speech    ║
║  Pick + Light Pick  →  STR-primary build (STR 18/DEX 14)║
║  Dragon Plate       →  +6 AC, Dex cap 0, Bulwark, NPC  ║
╠══════════════════════════════════════════════════════════╣
║  XP 0 / 1000   Gold 15gp   Bulk — / —                  ║
╚══════════════════════════════════════════════════════════╝
```

---

### `.hp` — Quick HP Panel

```
╔══════════════════════════════════════════════╗
║  PARTY HP                                    ║
╠══════════════════════════════════════════════╣
║  [YOU]     [████████████░░░░]  18/24  ○○●    ║
║  Amiri     [████████████████]  24/24  ○○○    ║
║  Linzi     [████████░░░░░░░░]  10/18  ○●○    ║
║  Valerie   [████████████░░░░]  16/22  ○○○    ║
╠══════════════════════════════════════════════╣
║  ○ = healthy  ● = wounded  ✕ = dying         ║
║  Hero Points shown right of HP bar [X/3]     ║
╚══════════════════════════════════════════════╝
```

---

### `.inv` / `.inventory` — Inventory Panel

**Compact (`.inv`):**
```
╔══════════════════════════════════════════════╗
║  INVENTORY — [Name]          Gold: [X]gp     ║
╠══════════════════════════════════════════════╣
║  WEAPONS    [Longsword +1]  [Dagger ×3]      ║
║  ARMOR      [Breastplate]  [Steel Shield]    ║
║  MAGIC      [Bracers of Armor +1]            ║
║  CONSUME    [Minor Heal ×2]  [Acid Flask ×2] ║
║  QUEST      [Charter Doc]  [Parchment]       ║
║  GEAR       [Healer's Tools]  [Rope 50ft]    ║
╠══════════════════════════════════════════════╣
║  Bulk: [X]/[max]   Gold: [X]gp [X]sp [X]cp  ║
╚══════════════════════════════════════════════╝
```

**Full (`.inventory`):**
```
╔══════════════════════════════════════════════════╗
║  INVENTORY — [Character Name]                    ║
╠══════════════════════════════════════════════════╣
║  WEAPONS    [name]  [damage] [traits]  [bulk]    ║
║  ARMOR      [name]  AC+[X]  DexCap+[X]  Chk-[X] ║
║  SHIELD     [name]  AC+[X] raised  Hard[X] HP[X] ║
║  MAGIC      [name]  [effect]  [charges]          ║
║  CONSUME    [name]  [effect]  ×[qty]             ║
║  QUEST      [name]  [notes]                      ║
║  GEAR       [name]  [bulk]                       ║
╠══════════════════════════════════════════════════╣
║  Bulk: [X]/[max]  Gold: [X]gp [X]sp [X]cp       ║
╚══════════════════════════════════════════════════╝
```

---

### `.party` — Companion Panel

```
╔══════════════════════════════════════════════════════╗
║  ACTIVE PARTY                                        ║
╠═══════════════╦══════════════════════════════════════╣
║  [Name]       ║  [Class] [L]  HP [bar] [X]/[X]      ║
║  Relationship ║  [score]      AC [X]  Init +[X]     ║
║  Conditions   ║  [list or None]                     ║
║  Hero Points  ║  [bar] [X]/3                        ║
╚═══════════════╩══════════════════════════════════════╝
```
*(one row per companion)*

---


---

> **➡️ See `KM_Commands_Maps.md` for: ASCII map formats (combat grid, scene map, world hex map, time/calendar, quests, NPC, kingdom, XP, conditions panels).**

---


> **➡️ `KM_Commands_P3.md`: `.alignment`, `.threads`, `.options`. `KM_Commands_New.md`: new system commands.**


### `.actions` — Available Actions Panel

> **DM:** Output ONLY this panel when `.actions` is typed. Pull from the player's **actual build** — eRmaC's feats, class features, and skills only. Nothing generic. Nothing from builds they didn't select. Feats not yet unlocked do NOT appear.
>
> **⛔ AUTO-DISPLAY RULE — MANDATORY:** This panel MUST appear automatically at the start of every combat encounter, displayed after the initiative order and before the choice menu. The player should never have to type `.actions` to see what they can do in combat — it is always there. It also refreshes any time the player uses a resource (Battle Medicine cooldown, Shield HP after a block, Hero Point spent). **Failure to display this panel at combat start = `.fail 3` (choice menu missing or incomplete).**

```
╔══════════════════════════════════════════════════════════╗
║  eRmaC — ACTIONS REFERENCE          Mode: Combat  Rd [X] ║
║  Actions this turn: ●●● (3/3)   Reaction: ◆ available   ║
╠═══════════════════╦══════════════════════════════════════╣
║  ⚔️  STRIKES       ║  Cost  Bonus        Damage          ║
╠═══════════════════╬══════════════════════════════════════╣
║  Dwarven Waraxe   ║  1A    d20+[X]  →   1d8+[X] S       ║
║    2nd attack     ║  1A    d20+[X-5]    (MAP -5)         ║
║    3rd attack     ║  1A    d20+[X-10]   (MAP -10)        ║
║  Unarmed / Shove  ║  1A    d20+[Athl]   d4+[Str] B       ║
╠═══════════════════╬══════════════════════════════════════╣
║  🛡️  SHIELD        ║  Cost  Effect                       ║
╠═══════════════════╬══════════════════════════════════════╣
║  Raise Shield     ║  1A    +4 AC until start of next turn║
║                   ║        Shield HP [X]/20  Hard: 5     ║
║  Shield Block     ║  ◆     Reduce dmg by Hardness (5)   ║
║  [REACTION]       ║        Trigger: take dmg while raised║
║                   ║        Shield takes same damage      ║
╠═══════════════════╬══════════════════════════════════════╣
║  ⚡ CLASS FEATURES ║  Cost  Effect                       ║
╠═══════════════════╬══════════════════════════════════════╣
║  Taunt [ACTION]   ║  1A    −2 atk vs others (Int vs Will)║
║  Intercept [REACT]║  ◆     Take hit for adj. ally        ║
║  Guardian's Armor ║  AUTO  Phys resist [1+lvl/2] = [X]   ║
║  Ever Ready       ║  AUTO  Never flat-footed — act Rd 1   ║
╠═══════════════════╬══════════════════════════════════════╣
║  💊 SKILL ACTIONS  ║  Cost  Effect / Status              ║
╠═══════════════════╬══════════════════════════════════════╣
║  Battle Medicine  ║  2A    1d8+Wis heal | DC15 | 10min cd║
║  [FEAT]           ║        Healer's Tools req | [STATUS] ║
║  Demoralize [SKL] ║  1A    Intimidation vs Will → Frght1  ║
║  Recall Know.[SKL]║  1A    Warfare Lore → ID creature/sit ║
╠═══════════════════╬══════════════════════════════════════╣
║  🚶 MOVE/ATHLETICS ║  Cost  Effect                       ║
╠═══════════════════╬══════════════════════════════════════╣
║  Stride / Step    ║  1A    Speed(20ft) / 5ft no AoO      ║
║  Grapple / Shove  ║  1A    Fort DC → Grabbed / Push 5ft  ║
║  Trip / Disarm    ║  1A    Ref DC  → Prone / Drop item   ║
║  Force Open       ║  1A    vs Hard → break door/object   ║
╠═══════════════════╬══════════════════════════════════════╣
║  RESOURCES                                               ║
║  HP: [X]/[X]  Shield: [X]/20  Hero Points: [X]/3        ║
║  Pending Hero Points: [X]                                ║
╚═══════════════════╩══════════════════════════════════════╝
```

**What each label means — shown in the panel:**
- `[ACTION]` = costs action icons (1A, 2A, 3A)
- `[REACTION] ◆` = triggers off something happening, 1 per round
- `[FEAT]` = ability you chose at level-up
- `[PASSIVE] AUTO` = always on, no activation needed
- `[SKILL ACTION]` = uses a trained skill, has a DC

---

### `.respec` / `.respec [name]` — Character Rebuild

> **DM:** This command is always valid. It is an OOC tool — it does not require in-world justification, story flags, or Downtime. Game state (HP, XP, gold, inventory, flags, relationships) is fully preserved. Only the build choices change.

```
╔══════════════════════════════════════════════════════════╗
║  RESPEC — CHARACTER REBUILD                              ║
╠══════════════════════════════════════════════════════════╣
║  Select character to rebuild:                            ║
║  (1) [Player Name] — [Class] L[X]       ← you           ║
║  (2) Amiri         — Barbarian L[X]                      ║
║  (3) Linzi         — Bard L[X]                           ║
║  (4) Valerie       — Fighter L[X]                        ║
║  (5) Harrim        — Cleric L[X]                         ║
║  (6) Jaethal       — Rogue L[X]                          ║
║  (7) Tristian      — Cleric L[X]                         ║
║  (8) Nok-Nok       — Rogue L[X]                          ║
║  (9) Octavia       — Wizard L[X]                         ║
║  (10) Regongar     — Magus L[X]                          ║
║  (11) Ekundayo     — Ranger L[X]                         ║
║  (12) Lem          — Bard L[X]                           ║
║  (Only show companions currently recruited)              ║
╠══════════════════════════════════════════════════════════╣
║  RESPEC MODE:                                            ║
║  (A) FULL REBUILD  — Pick new class, ancestry, all feats ║
║      Resets to L1 choices then replays to current level  ║
║  (B) RETRAIN FEAT  — Swap one feat at any level          ║
║      (PF2e Downtime canon: 1 week per feat retraining)   ║
║  (C) RETRAIN SKILL — Change one skill proficiency        ║
║      (PF2e Downtime canon: 1 week per skill rank change) ║
║  (D) SWAP SPELLS   — Change prepared/known spells only   ║
║      (No Downtime cost — daily spell prep is canonical)  ║
╠══════════════════════════════════════════════════════════╣
║  Type character number + mode (e.g. "1A" or "3C")        ║
║  Type CANCEL to close without changes.                   ║
╚══════════════════════════════════════════════════════════╝
```

**DM Rules for Respec:**

```
RETRAIN FEAT (B): Player names level. DM shows current feat + options. Cost: 1 week Downtime per feat.
RETRAIN SKILL (C): Player names skill + target rank. Cost: 1 week Downtime per rank.
SWAP SPELLS (D): Prepared casters — no cost. Spontaneous — 1 week Downtime.
COMPANION RESPEC: Same rules. DM replays Auto build in Manual mode or swaps single feat/skill.
AFTER ANY RESPEC: Output "[OOC] Respec complete." + full .status panel.
  End with "[Ready. Type .continue to return to the game.]"
```

---

**FULL REBUILD (A) — Step-by-Step Procedure**

> OOC framing only. No in-world cost. Preserves: XP, gold, inventory, flags, relationships, HP total will be recalculated from scratch.

**STEP 1 — Confirm scope**
```
[OOC] FULL REBUILD — [Character Name] (currently L[X] [Class])
Preserved : XP · gold · inventory · flags · relationships
Reset      : class · build · all feats · ancestry · background · HP
Want to keep your ancestry and background, or redo those too?
  (K) Keep ancestry + background — just change class/build/feats
  (R) Redo everything from scratch — full new character
```

**STEP 2 — Class selection**
Display the full 27-class menu from KM_CharCreate.md STEP 1.
Wait for pick. Record new `player.class`.

**STEP 3 — Build selection (from 10 presets)**
Load KM_BuildScreen.md. Display the 10-preset block for the new class.
Mark ★ on recommended preset.
After pick:
```
  player.build         = [Build Name]
  player.build_source  = KM_Builds_[file].md
  player.leveling_mode = MANUAL  ← default; AUTO or ASK if player requests
```
If player declines all presets: set `player.leveling_mode = ASK`, `player.build = CUSTOM`.
> Companion leveling is governed separately by `game_options.companion_leveling_mode` (default AUTO).

**STEP 4 — Ancestry (if R was chosen in Step 1)**
Display ancestry menu from KM_CharCreate.md STEP 3. Wait for pick.

**STEP 5 — Background (if R was chosen in Step 1)**
Load KM_Backgrounds.md. Display full list. Wait for pick.

**STEP 6 — Replay leveling L1 → current level**
```
MODE: AUTO → silently apply build-map [PICK] feats for each level, announce inline
MODE: ASK  → present each level's feat choice one at a time, mark ★ recommendation

For each level from 1 to current:
  • HP   : ancestry base HP + class HP + Con modifier (recalculate from L1)
  • Feats: apply from build map or ask player
  • Ability boosts (L5/10/15/20): apply in build-map priority order
  • Spell slots (casters): apply per class table
  • Proficiencies: apply per class table
```
Output a compact replay summary:
```
[REBUILD REPLAY — L1→LX]
  L1 : [class feature] + [feat]
  L2 : [feat]
  L3 : [feat]
  ...
  LX : [feat]
  HP recalculated: [new total]
```

**STEP 7 — Confirm and output**
```
[OOC] Rebuild complete.
```
Output full `.status` panel. End with:
```
[Ready. Type .continue to return to the game.]
```

---

> **DM:** Filter ALL scene narration through the player's build lens. Build 1 (Guardian): threat assessment first — every room is a defensive problem. See KM_Builds.md for build perspective filters.

---

### 🗣️ NPC DIALOGUE NAME FORMAT

**NPC names in spoken dialogue are always Title Case, never ALL CAPS.**

✅ `**Malak** *(voice cracking)*: *"Halt, stranger."*`
❌ `**MALAK** *(voice cracking)*: *"Halt, stranger."*`

ALL CAPS causes text-to-speech to spell out individual letters. Title Case is mandatory for all NPC names and the player character name (`**eRmaC:**` not `**eRmaC:**`).

---

---

*KM_Commands_Panels.md — Kingmaker PF2e | Info Panel Templates v1.0*
