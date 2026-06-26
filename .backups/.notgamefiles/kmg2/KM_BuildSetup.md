# KINGMAKER — BUILD SETUP (8-PROMPT SEQUENCE)
## KM_BuildSetup.md | Referenced by: KM.txt Step 2, KM_Builds_A–M.md headers

> **⛔ DM: After the player confirms class + build, you MUST run ALL 8 prompts
> below IN STRICT NUMERIC ORDER (1 → 2 → 3 → 4 → 5 → 6 → 7 → 8). Output each
> prompt VERBATIM. STOP after each. WAIT for input. Do NOT combine. Do NOT
> skip. Do NOT auto-select defaults. Do NOT reorder. Skipping or reordering
> any prompt = `.fail 3` (agency violation) + `.fail 9` (file content ignored).**

> **Purpose:** The build file lists defaults for ancestry / heritage / weapon /
> armor / stats / skills / deity / background. Without these prompts, the DM
> treats the default as final and strips the player's right to customize.
> These 8 prompts restore that right — ancestry, heritage, stat, weapon,
> armor, deity, background, and skills.

> **⛔ HERITAGE IS A SEPARATE STEP (Prompt 2).** It is NOT a sub-question of
> Prompt 1 (Ancestry). Even if the Ancestry table suggests a heritage in its
> "Heritage" column, the player must explicitly confirm or choose a heritage
> in Prompt 2. Skipping Prompt 2 = `.fail 3`.

> **⛔ BACKGROUND COMES BEFORE SKILLS (Prompt 7 before Prompt 8).** Background
> grants a fixed trained skill + Lore skill which must be locked before the
> player picks remaining class skills. Running Skills before Background = `.fail 3`.

---

## ⛔ MANDATORY CHECKLIST BLOCK (every BuildSetup response)

Every response that runs a BuildSetup prompt MUST open with this exact
checklist block at the TOP of the response (before the prompt itself):

```
═══ BUILDSETUP CHECKLIST ═══
[✓]  1. Ancestry          → recorded: [value or "—"]
[✓]  2. Heritage          → recorded: [value or "—"]
[✓]  3. Stat Priority     → recorded: [value or "N/A locked" or "—"]
[→]  4. Weapon            → IN PROGRESS (this prompt)
[ ]  5. Armor             → pending
[ ]  6. Deity             → pending (or "N/A — no deity slot")
[ ]  7. Background        → pending
[ ]  8. Skills            → pending
─── post-prompt sequence (MUST run before save block) ───
[ ]  9. Setup Assembly    → boosts, feats, HP/AC, languages, skill mods
[ ] 10. Starting Gear     → KM_StartingGear.md screen (A/B/C). Skipping = .fail 41
[ ] 11. Pick-10 Companions → KM_Companions_Iconics.md screen ("?" = random)
[ ] 12. Pick-5 Seekers     → any 5 from full roster (Malak's jail team) ("?" = random)
[ ] 13. Save Block         → USE KM_SaveBlock_Template.md (EXHAUSTIVE MODE) — ONLY AFTER 11 + 12 recorded
[ ] 14. Chapter Select     → KM_ChapterSelect.md screen
════════════════════════════
```

**Marker rules:**
- `[✓]` = prompt complete, value locked. Show recorded value after `→`.
- `[→]` = the prompt this response is running RIGHT NOW. Exactly one per response.
- `[ ]` = pending. Show "pending" or "N/A — [reason]" if skip-applicable.
- `[✗]` = explicitly skipped per spec (e.g. Prompt 3 on STR-locked Barbarian, Prompt 6 on non-divine class). Show reason.

**STOP footer (also mandatory at END of every prompt response):**
```
⛔ STOP — DO NOT ADVANCE. Awaiting player input for Step [M].
⛔ DO NOT auto-select. DO NOT skip ahead.
⛔ Steps remaining after this one: [list, e.g. 5-Armor, 6-Deity, 7-Background, 8-Skills, 9-Assembly, 10-Pick10, 11-Pick5, 12-SaveBlock, 13-Chapter]
⛔ Save Block does NOT generate until Step 11 (Pick-5 Seekers) is recorded.
⛔ Prologue does NOT begin until Step 13 (Chapter Select) is chosen.
```

**Why this exists:** the DM has historically jumped from Prompt 3 directly to
companion selection or save block, skipping Weapon/Armor/Deity/Background.
A visible checklist at the top of every response forces the DM to track
every step. If the checklist shows `[ ] 5. Armor → pending` but the next
response narrates the prologue, the skip is immediately visible.

**Violations:**
- Missing checklist block at top of response = `.fail 41`
- Missing STOP footer = `.fail 41`
- More than one `[→]` marker, or no `[→]` marker = `.fail 41`
- Marking a step `[✓]` that was never actually run = `.fail 41` + `.fail 3`
- Advancing past the `[→]` step without recording player input = `.fail 41` + `.fail 3`
- Jumping the `[→]` marker forward by more than 1 (e.g. from 3 to 7) = `.fail 41` + `.fail 3`
- Outputting Save Block (Step 12) before Steps 10 + 11 are `[✓]` = `.fail 9` (broken-seed save) + `.fail 41`
- Beginning prologue narration before Step 13 is `[✓]` = `.fail 3` + `.fail 41`

**Recovery:** reprint the earliest unfinished prompt with corrected checklist.
Never combine prompts. Never shorten. Corrections are additive.

**Player override:** type `.checklist` to force the DM to reprint the
checklist block showing current state.

---

## ⛔ PROMPT 1 — ANCESTRY CONFIRMATION

**⛔ IGNORE the A/B/C template in the build file header — it is outdated.**
Use the **Race Options table** in the current build (the 10-row numbered table
below the stat block). Output VERBATIM:

```
════════════════════════════════════════════
ANCESTRY — [Build Name]
Default: [★1 row from Race Options table]

All options (pick any — ranked by fit, not restricted to this list):
  [copy Race Options table rows 1–10 verbatim, # | Ancestry | Heritage | Why]

Type a number (1–10) or any PF2e ancestry name.
════════════════════════════════════════════
```
STOP. Wait for input. Player may pick any ancestry — the table is ranked
guidance, not a restriction. Apply the HP / speed adjustments from the build
file header (ANCESTRY BASE HP, SPEED, HEIGHT). **Heritage is NOT chosen here
— proceed to PROMPT 2.**

---

## ⛔ PROMPT 2 — HERITAGE

**RUN THIS PROMPT FOR EVERY ANCESTRY.** Heritage is a discrete PF2e character
creation step — never bundle into Prompt 1, never auto-select the table's
suggested heritage, never skip. Look up the chosen ancestry's heritage list
in `KM_AncestryGuide.md` and output the canonical heritage table verbatim.

Output VERBATIM:
```
════════════════════════════════════════════════════════════
HERITAGE — [Ancestry] ([Build Name])
The Race Options table suggested: [Heritage from P1 table row, if any] (★)

All [Ancestry] heritages (pick any — the suggestion is guidance only):
  [copy the ancestry's full heritage list from KM_AncestryGuide.md verbatim,
   numbered. Each row: # | Heritage | Effect (one line)]

Type a number or any heritage name. Type ? for more detail on a heritage.
════════════════════════════════════════════════════════════
```
STOP. Wait for input. Record `player.heritage`. Apply heritage effects
(extra feat, extra skill, vision change, resistance, etc.) — most heritages
do NOT change HP / speed / stat array, but a few do (e.g. Hill Dwarf +1 HP
already included in dwarf base; Half-Elf grants Low-Light Vision; Versatile
Human grants 1 extra general feat at L1; Skilled Human grants 1 extra
trained skill at L1). Update the stat block accordingly.

⛔ **HERITAGE VERIFY — MANDATORY before advancing to Prompt 3.**
Output this line verbatim (values from KM_AncestryGuide.md — NOT from training data):
`HERITAGE CONFIRMED: [Ancestry] → [Heritage Name] | [one-line effect]`
Wrong or fabricated heritage = `.fail 9`. Skipping this line = `.fail 41`.

Proceed to PROMPT 3.

---

## ⛔ PROMPT 3 — STAT PRIORITY (primary attack stat)

**RUN THIS PROMPT ONLY IF the build's class supports both STR and DEX as
primary attack stats.** Classes where swap is legal:
  Fighter, Ranger, Magus, Monk, Rogue, Swashbuckler, Investigator,
  Champion (Liberator/Redeemer DEX viable), Thaumaturge, Inventor.

For STR-locked (Barbarian, Guardian) or DEX-locked (Gunslinger) or
casting-stat-locked (full casters) builds, **SKIP this prompt and say:**
*"This build's primary stat is locked to [X]. Proceeding to Prompt 4."*

Otherwise output VERBATIM:
```
════════════════════════════════════════════
STAT PRIORITY — [Build Name]
Default primary: [STR or DEX]
  [S] STR primary — [one-line effect, e.g. "heavy armor, maul 1d12"]
  [D] DEX primary — [one-line effect, e.g. "light armor, rapier 1d6 finesse"]
Type S or D.
════════════════════════════════════════════
```
STOP. Wait for S or D. Swap the stat array (primary ↔ secondary attack stat)
if player chose the non-default. Proceed to PROMPT 4.

---

## ⛔ PROMPT 4 — WEAPON CHOICE

Look up the build's class/build row in KM_BuildScreen.md CLASS → WEAPON CATEGORY table
to find its category (A–H). Then display that category's FULL weapon list verbatim from
KM_BuildScreen.md WEAPON CATEGORIES. Do NOT generate a truncated subset.

⛔ **WEAPON CATEGORY VERIFY — MANDATORY before showing the weapon list.**
Output this line verbatim (values from KM_BuildScreen.md CLASS → WEAPON CATEGORY table):
`WEAPON CATEGORY: [Class/Build] → Category [X] | [N] weapons in category | source: KM_BuildScreen.md`
Wrong category = `.fail 9`. Skipping this line = `.fail 41`.

Place the build's default weapon at [1] (marked ★ BUILD DEFAULT). Remaining entries are
the category list in order. Add a Custom option as the final numbered entry.

⛔ **THE BUILD DEFAULT IS ALWAYS [1]. It is NEVER outside the numbered list. It is NEVER
presented as a typed-input option ("type GUISARME", "type the weapon name", etc.).
It is entry [1] in the numbered menu. Full stop. No exceptions.**

⛔ **WEAPON MENU FORMAT LOCK — numbered list only. Every entry must be:**
`[N] Weapon Name — [dice] [type] [traits]`
No sub-headers, no unnumbered bullets, no prose lists, no mixed format.
"Type the weapon name" prompts = `.fail 3`. Any non-numbered weapon entry = `.fail 3`.
Build default outside the numbered list = `.fail 3`.
If the player types a name instead of a number, treat it as Custom and confirm.

After player picks, update the build's Weapon line in the stat block.
Proceed to PROMPT 5.

## ⛔ PROMPT 5 — ARMOR CHOICE

COPY-PASTE the armor table from KM_BuildScreen.md STEP 2.6 EXACTLY AS WRITTEN.
DO NOT generate from PF2e training data — stats differ from core rules.
Omitting Dragon Plate, using wrong AC values, or fabricating entries = .fail 9.
Entry count = 11 (options 0–10). Showing fewer = .fail 9.

Filter by class proficiency (Dragon Plate #10 ALWAYS shown — see ⚠️ below):
- Light-only (Rogue/Bard): show 0–6, 10
- Medium (Barbarian/Ranger/Druid): show 0–6, 10
- Heavy (Fighter/Champion/Guardian): show 0–10
- Unarmored (Monk/Sorcerer/Wizard): show 0, 10, Custom only

⚠️ **DRAGON PLATE (#10) is PC-LOCKED to eRmaC and OVERRIDES class armor proficiency.** Shown to every class, no exceptions. Hiding it = `.fail 9`. Aerynth-origin artifact grants its own trained-Heavy proficiency to eRmaC. Full rule: KM_BuildScreen.md § DRAGON PLATE NOTE.

⛔ **ARMOR VERIFY — MANDATORY after player picks.**
Output this line verbatim (values from KM_BuildScreen.md STEP 2.6 — NOT from training data):
`ARMOR CONFIRMED: [Armor Name] | AC bonus +[X] | DEX cap [Y or "—"] | Check penalty [Z or "—"] | source: KM_BuildScreen.md`
Wrong stats = `.fail 9`. Skipping = `.fail 41`.

After player picks, recompute AC: 10 + armor bonus + DEX (capped) + proficiency (+3 at L1: rank 2 + level 1).
Update the stat block. Proceed to PROMPT 6.

## ⛔ PROMPT 6 — DEITY (divine/nature classes only)

**RUN THIS PROMPT ONLY IF the build's class is in the Mandatory or Optional list below.**
- **Mandatory** for: Cleric, Champion, Warpriest Cleric, Paladin (Champion: Iomedae/etc.)
- **Optional** for: Druid, Oracle, Animist, Exemplar, Monk
- **SKIP for ALL other classes** — including Barbarian, Fighter, Ranger, Rogue,
  Wizard, Sorcerer, Bard, Magus, Gunslinger, Inventor, Investigator, Kineticist,
  Psychic, Summoner, Swashbuckler, Thaumaturge, Witch, Commander, Guardian.
  Say *"No deity slot for [class]. Skipping to Prompt 7."* and PROCEED IMMEDIATELY.
  Do NOT show a deity menu with an optional/none option. Do NOT offer flavor picks.
  Showing a deity menu for a skip-class = `.fail 41`.

Output VERBATIM:
```
════════════════════════════════════════════════════════════
DEITY — [Build Name]
Kingmaker-relevant deities (pick one or type CUSTOM for any other):
  [1]  Erastil        — Huntsman, community, family. Kingmaker's patron saint.
  [2]  Abadar         — Law, cities, wealth. Popular in Restov and Brevoy.
  [3]  Iomedae        — Justice, honor, valor. Aldori noble tradition.
  [4]  Gorum          — War, strength, strife. Sword-arm deity.
  [5]  Sarenrae       — Sun, healing, redemption. Forgiving but firm.
  [6]  Desna          — Stars, travel, luck. Patron of wanderers.
  [7]  Shelyn         — Beauty, love, art. Peaceful path.
  [8]  Torag          — Dwarves, forge, protection. Stronghold guardian.
  [9]  Cayden Cailean — Freedom, ale, bravery. Drunken hero god.
  [10] Pharasma       — Death, fate, birth. Neutral arbiter.
  [11] Gyronna        — Hate, spite (uncommon — GM approves case by case).
  [12] Nethys         — Magic in all forms. Arcane scholar's choice.
Type 1–12 or CUSTOM.
════════════════════════════════════════════════════════════
```
STOP. Wait for selection. Record `player.deity`. For Cleric: also load the
deity's **domain list** (2 picks) from AoN or KM_Spells_Divine_Occult.md.
For Champion: also record the Cause (Paladin/Redeemer/Liberator) — this
may already be in the build file; if not, ask. Proceed to PROMPT 7.

---

## ⛔ PROMPT 7 — BACKGROUND

⛔ READ KM_Backgrounds_Screen.md DIRECTLY BY FILENAME. OUTPUT ITS TABLE VERBATIM.
Do NOT search by content keywords — search truncates and you will fabricate
the gaps. Do NOT reconstruct from training data. Use the Read tool with the
exact filename. Paste the table. Mark the build's default entry with ★.

⛔ SENTINEL CHECK before posting your output:
   Entry [ 1] must be: Borderlands Pioneer  (NOT Acolyte — that's CRB-order
                                              fabrication)
   Entry [ 8] must be: Acolyte               (first CRB entry)
   Entry [22] must be: Field Medic
   Entry [42] must be: Warrior               (final entry — if your table does
                                              NOT end here, you fabricated)
   All four sentinels must match. Wrong boosts, missing entries, fabricated
   names, "..." or "etc.", or skipped numbers = .fail 9. Re-Read and re-post.

After player picks, look up full entry in KM_Backgrounds.md or KM_Backgrounds_CRB.md.
Record player.background, player.background_skills[], player.background_skill_feat.

⛔ **BACKGROUND SKILL VERIFY — MANDATORY before advancing to Prompt 8.**
Output this line verbatim (values from KM_Backgrounds_Screen.md — NOT from training data):
`BACKGROUND CONFIRMED: [Background Name] = [Stat1]/[Stat2] | [Skill] + [Lore] | [Skill Feat]`
If training data and the file disagree, the file is authoritative.
Wrong or fabricated skills = `.fail 9`. Skipping this line = `.fail 41`.

Proceed to PROMPT 8 (Skills).

**Every background grants:** 2 ability boosts | 1 trained skill + 1 Lore skill | 1 skill feat

---

## ⛔ PROMPT 8 — SKILL CHOICES

Every class auto-trains the player in 1 fixed skill (sometimes 2). The
player then picks N additional trained skills, where N = class base + INT
mod. **Those N picks come from ANY skill in PF2e — not a "class list".**
Background grants 1 trained skill + 1 Lore skill on top of that. The build
file shows DEFAULT picks. Ask whether to keep or swap.

⛔ **NO CLASS SKILL LIST RESTRICTION (PF2e Remaster).** Not PF1. Free picks
come from ANY PF2e skill — Medicine, Thievery, Religion, Performance, etc.
are legal for any class. Per-class list below = AUTO-TRAINED only, not a
pick restriction. Rejecting "Medicine not on Fighter list" = `.fail 9` + `.fail 38`.

⛔ **SKILL COUNT VERIFY — output this line BEFORE presenting the skill menu:**
`SKILL COUNT: [class] base [N] + INT [±X] = [Y] | [background] [skill] overlap → [+1 or none] | free picks = [total] | Warfare/other Lore = locked separately`
Wrong free pick count = `.fail 6`. Skipping this line = `.fail 41`.
Example (Barbarian + Warrior, INT +0): `SKILL COUNT: Barbarian base 3 + INT 0 = 3 | Warrior Athletics overlap → +1 | free picks = 4 | Warfare Lore = locked`

**Skill count formula:**
  Total trained skills = (class base + INT mod) + 1 background skill + 1 background Lore skill
  Example: Fighter INT +0 with Warrior background = 3 + 0 + 1 (Athletics) + 1 (Warfare Lore) = 5

⛔ **OVERLAP RULE — MANDATORY (apply BEFORE counting free picks):**
If the background's trained skill duplicates a class-LOCKED skill, the redundant
grant **converts to +1 free class pick**. The Lore skill is unaffected (always
granted on top). DM must apply this every time — silently dropping the bonus
pick = `.fail 6`. "Already covered, no bonus" is the wrong answer.

  ► Barbarian + Warrior (Athletics overlap): Barbarian locks Athletics;
    Warrior grants Athletics + Warfare Lore. Athletics overlap → +1 free pick.
    INT +0: Athletics (locked) + **4 free class picks** + Warfare Lore = 6 trained.
    Free picks = 3 (base) + 1 (overlap) = **4, not 3.**
    Asking for only 3 free picks here = `.fail 6`.

  ► Magus + Scholar/Arcana: Arcana overlap → +1 free pick (4 total at INT +0).
  ► Cleric + Acolyte: Religion overlap → +1 free pick.
  ► Ranger + Hunter: Nature overlap → +1 free pick.
  ► Wizard + Scholar/Arcana: Arcana overlap → +1 free pick.
  ► Champion + Acolyte: Religion overlap → +1 free pick.

⛔ **DM ANTI-FLIP RULE:** Once the player commits to N free picks based on the
overlap formula, do NOT recount mid-prompt and demand a different N. If you need
to recount, explain the math first; don't silently flip the number. Flipping
the skill count back-and-forth across turns = `.fail 6` + `.fail 33`.

Output VERBATIM:
```
════════════════════════════════════════════════════════════
SKILLS — [Build Name]
Class auto-trains:  [fixed-grant skill(s), e.g. "Athletics (Fighter)"]
Free picks:         [N + INT mod] from ANY PF2e skill (see list below)
Background grants:  1 trained skill + 1 Lore skill ([Background] = [Skill] + [Lore])
Total trained:      [N + INT mod + 2 + class auto-grant]
Build's default:    [list from build file]

All PF2e skills (pick freely from this list for the [N + INT mod] free picks):
  Acrobatics · Arcana · Athletics · Crafting · Deception · Diplomacy
  Intimidation · Lore (any subject) · Medicine · Nature · Occultism
  Performance · Religion · Society · Stealth · Survival · Thievery
(Perception is auto-trained for everyone — not a pick.)

  [K] KEEP defaults — proceed with the skills above
  [S] SWAP — pick your own [N + INT mod] free skills from ANY skill above
  [?] Show me build recommendations before deciding
Type K, S, or ?.
════════════════════════════════════════════════════════════
```
STOP. Wait for selection.
- **K:** record the build's default skills in `player.skills_trained[]`. Proceed.
- **S:** wait for player to name [N + INT mod] skills FROM ANY PF2e SKILL.
  Do NOT reject picks for being "not on the class list" — no such list exists.
  Background-granted skills and class auto-grants are already locked. Record all.
- **?:** display the build file's recommendations + rationale, then re-present K/S.

**Background skill grants (common backgrounds):**
- Warrior: Athletics (or Intimidation) + Warfare Lore
- Scholar: choose from Arcana/Nature/Occultism/Religion/Society + Lore of field
- Guard: Intimidation + Legal Lore or Guild Lore
- Acolyte: Religion + a deity-appropriate Lore
- Criminal: Stealth + Underworld Lore
- Hunter: Nature + Terrain Lore (chosen)
- (other backgrounds: check KM_Backgrounds.md for skill grants)

**Class AUTO-TRAINED skills (fixed-grant only — NOT a restriction on free picks):**
- Alchemist: Crafting  |  Barbarian: Athletics  |  Bard: Occultism, Performance
- Champion: Religion  |  Cleric: Religion + domain  |  Druid: Nature (+order)
- Fighter: Acrobatics OR Athletics  |  Gunslinger: Stealth, Crafting
- Guardian: Athletics  |  Investigator: methodology  |  Magus: Arcana, Athletics
- Monk: (none)  |  Ranger: Nature, Survival  |  Rogue: Stealth (7 free picks)
- Sorcerer: bloodline  |  Thaumaturge: Occultism  |  Witch: Occultism (+patron)
- Wizard: Arcana  |  (other classes: see KM_Builds_A–M.md)

Free pick count = **3 + INT mod** most classes; **7 + INT** Rogue;
**2 + INT** Wizard/Witch. Skill proficiencies auto-advance per leveling map.

---

## ⛔ AFTER ALL 8 PROMPTS — SETUP ASSEMBLY

Output ALL of the following in a single response:

**① ABILITY BOOSTS — L1 STAT ASSEMBLY**

Total boosts at L1 = 9, each +2 (below 18). Sources:
  Class key: 1 fixed.
  Background: 2 (1 from 2-stat menu + 1 free).
  Ancestry: 2 (Human/Half-Elf/Half-Orc/Versatile = both free; others = 2 fixed or 1 fixed + 1 flaw + 1 free).
  Standard free: 4.
No double-boost within a single source. Each boost = +2 (NOT +1). 10→12→14→16→18.
"Stat cap N total" = `.fail 38`. +1 per boost = `.fail 6`. "Array needs level-ups" = `.fail 9`.

⛔ **COMPUTE N BEFORE OUTPUT.** N = total player-pick slots = (background 2-stat menu pick: 1) + (free-choice boosts: standard 4 + ancestry free + background free). For Human + flex-background classes N is typically 7–8. Locking the count to 4 when ancestry/background add free picks = `.fail 38`.

⛔ **FREE BOOSTS ARE PLAYER CHOICE.** Auto-assigning = `.fail 39`. Working backwards from the build's default stat array to "determine how boosts were distributed" and outputting `FREE BOOST 1: STR (14→16)` as already-applied = `.fail 39`. The build's array is a ★ SUGGESTION, never a pre-applied state.

⛔ **INPUT FORMATS**
Per-prompt: `FREE BOOST [k] of [N]:` + `[1] STR [2] DEX [3] CON [4] INT [5] WIS [6] CHA`. Wait between each.
Batch: player MAY answer all picks in one line (comma/space-separated digits 1-6) or `D` for build default. Validate count = N and uniqueness-per-source. Refusing a valid batch with "I must hold the line" theater = `.fail 35`.

Banned formats (`.fail 38`): ASSIGN / DEFAULT / SWAP BOOSTS / SWAP STATS commands, combined menu in DM output, "type SWAP + 4 stats if different" offer, working-backwards derivation, free-count locked to 4 when ancestry/background add free picks.

⛔ **HARD STOP — SELF-CHECK BEFORE POSTING.** Scan your draft. ALL must hold:
  (1) Response contains literal text `FREE BOOST 1 of ` (count-agnostic — number that follows must equal N you computed).
  (2) Response does NOT contain any of: `FINAL STATS`, `Fort +`, `Ref +`, `Will +`, `HP:`, `AC:`, `Speed:`. These appear only AFTER all picks recorded.
  (3) Response ends at the active menu. No derivation, no final array, no feat list past this point.
Any fail → delete from `FREE BOOST 1 of` onward, re-post stopping at the menu. `.fail 39` + `.fail 41`.

```
LOCKED BOOSTS:
  Class key: +[stat]
  Background pool: [A] or [B] (pick below; 2nd bg boost is free)
  Ancestry fixed: [stat(s) or "none — all free"]

BACKGROUND FIXED PICK (if 2-stat menu):  [1] [A]   [2] [B]

FREE BOOST 1 of [N]:
  [1] STR  [2] DEX  [3] CON  [4] INT  [5] WIS  [6] CHA
  ★ Suggested: [stat] — [reason from build file]
```
After ALL picks recorded, output the final stat array:
```
Boosts: Ancestry (+[..]) | Background (+[..]) | Class (+[..]) | Free (+[..])
STR [X] DEX [X] CON [X] INT [X] WIS [X] CHA [X]
```

**② FEATS — L1 (NUMBERED MENU REQUIRED — NEVER AUTO-FILL)**

⛔ **FEAT SOURCE LOCK — output before any feat menu:**
`FEAT SOURCES: Heritage = KM_AncestryGuide.md | Ancestry feat = KM_AncestryGuide.md | Background skill feat = KM_Backgrounds_Screen.md | Class feat = [build file]`
Fabricated feat not in named file = `.fail 9`. Skipping source line = `.fail 41`.

L1 feat slots (compute per character):
  Heritage: confirm from Step 2 (no menu).
  Background skill feat: AUTO-granted (announce, no menu).
  Ancestry feat: 1 menu from KM_AncestryGuide.md.
  L1 class feat: 1 menu from build file.
  Heritage bonus (if applicable): Natural Ambition → +1 class feat menu (same source, minus used pick); Versatile Human → +1 general feat menu (KM_GeneralFeats.md); Skilled Human → +1 trained skill (class skill list).

⛔ **EVERY non-auto slot = NUMBERED MENU.** Build default = ★ marker only, NOT pre-filled. Listing feats as filled values without preceding numbered menu = `.fail 39`.

⛔ **HARD STOP — SELF-CHECK BEFORE POSTING (feats phase).** ALL must hold:
  (1) Each non-auto feat slot output as: `[SLOT NAME] (slot k of M):` + numbered list `[1] FeatName — effect` ... drawn from the named source file.
  (2) No feat slot shows a single filled value without its menu first.
  (3) Response ends at the active feat menu, waiting for input.
Fail → delete and re-post with menus. `.fail 39`.

Player may swap with: SWAP ANCESTRY / SWAP SKILL / SWAP CLASS + feat name.

**③ HIT POINTS + ARMOR CLASS**
```
HP: [class base HP] + [CON mod] + [ancestry HP] = [total]
AC: 10 + [armor bonus] + [DEX mod capped] + 3 (trained = proficiency rank 2 + level 1) = [total]
```

**④ LANGUAGES**
```
Starting: Common + [ancestry language, e.g. Elven / Dwarven / Orcish]
Bonus: +[INT mod] additional languages if INT mod > 0 (player names them)
```

**⑤ FINAL TRAINED SKILLS (with modifiers)**
List every trained skill:
```
[Skill]: +2 (trained) + [ability mod] = +[total]
```

Then output: *"Setup confirmed. Ancestry [X], Heritage [H], Background [Y],
Weapon [Z], Armor [W], Deity [D or none]. HP [X] | AC [Y]. Generating save block."*
Heritage missing from confirmation line = `.fail 3` (heritage step skipped).
⛔ **DO NOT OUTPUT THE SAVE BLOCK YET. Starting Gear runs NEXT, then companion selection.**

⛔ **STARTING GEAR — STEP 10 — MANDATORY.**
Open `KM_StartingGear.md`. Output the gear selection screen verbatim. Wait for player to pick A, B, or C.
Record result in `inventory.gear[]` and adjust `gold` if player spent from 15 gp.
Skipping this step = `.fail 41`. Moving to companions before gear is confirmed = `.fail 41`.

⛔ **COMPANION SELECTION — STEP 11 — MANDATORY. RUNS AFTER GEAR, BEFORE THE SAVE BLOCK.**

**Exact sequence — no deviations:**
1. READ `KM_Companions_Iconics.md` DIRECTLY BY FILENAME and copy-paste the
   COMPACT PICK-10 SELECTION SCREEN verbatim.
2. STOP. Wait for the player to pick 10 companions by number.
   ⛔ **COMPANION NUMBER VERIFY — MANDATORY before recording pick.**
   Open `KM_CompanionIndex.md`. Output the SENTINEL CHECK first, then each pick:
   `INDEX SENTINEL: #1 = Jubilost Narthropple [Alchemist · KM] | #35 = Tika Waylan [Fighter · DL] | #88 = Liliana Vess [Wizard · MTG]`
   All three sentinels must match the file EXACTLY. Wrong name on any sentinel = `.fail 9` — re-Read the file.
   Then for each number the player submitted, output:
   `COMPANION VERIFY: #[N] = [Name] ([Class]) — CONFIRMED`
   Output all 10 lines. If any number is absent from KM_CompanionIndex.md, output:
   `COMPANION VERIFY: #[N] = NOT FOUND — re-prompt player`
   Do NOT substitute a name from PF2e training data. Do NOT guess.
   Using training data instead of KM_CompanionIndex.md = `.fail 9`. Skipping verify = `.fail 41`.
   Sentinel line missing = `.fail 41`. Wrong sentinel value = `.fail 9` (file not actually read).
   Record `player.companions[]` only after sentinel + all 10 lines are output.
3. Display the PICK-5 SEEKERS screen (any 5 from full roster — these are
   Malak's jailed team, recruitable in Ch1).
   ⛔ **SEEKER VERIFY — MANDATORY before recording.**
   Open `KM_CompanionIndex.md`. Output the same SENTINEL CHECK first:
   `INDEX SENTINEL: #1 = Jubilost Narthropple [Alchemist · KM] | #35 = Tika Waylan [Fighter · DL] | #88 = Liliana Vess [Wizard · MTG]`
   Then for each number the player submitted, output:
   `SEEKER VERIFY: #[N] = [Name] ([Class]) — CONFIRMED`
   Output all 5 lines. If any number is absent from KM_CompanionIndex.md, output:
   `SEEKER VERIFY: #[N] = NOT FOUND — re-prompt player`
   Do NOT substitute from PF2e training data. Using training data = `.fail 9`. Skipping verify = `.fail 41`.
   Sentinel line missing = `.fail 41`. Wrong sentinel value = `.fail 9`.
   Record `seeker_1`–`seeker_5` only after sentinel + all 5 lines are output.
4. ⛔ **SAVE BLOCK SCHEMA LOCK — output BOTH lines below before generating save block:**
   Line A — schema sentinel:
   `SCHEMA CHECK: save_version = "1.7" | source = KM_SaveBlock_Template.md EXHAUSTIVE MODE | top-level keys = 48`
   Line B — template fingerprint (first 6 root keys, verbatim, in order):
   `FINGERPRINT: save_version | chapter_completed | save_timestamp | save_label | player | companions`

   Then re-open `KM_SaveBlock_Template.md` and copy its structure verbatim.
   ⛔ DO NOT generate the save block from memory, training data, or inference.
      The template MUST be read in this turn. Output not derived from a fresh
      read of KM_SaveBlock_Template.md = `.fail 9`.
   ⛔ DO NOT use `"schema_version"` (the field is `save_version`).
   ⛔ DO NOT use version "1.6", "2.0", "2.0_EXHAUSTIVE", or any string other than `"1.7"`.
   ⛔ DO NOT invent, rename, reorder, or drop keys. All 48 top-level keys present.
   ⛔ DO NOT skip `passive_jealousy`, `companion_rivalry`, `companion_fights`,
      `date_log`, `dates_this_chapter`, `dispositions`, `marriage` (inside player),
      or `game_options.companion_leveling_mode` — these are common omissions.

   Wrong version = `.fail 9`. Wrong fingerprint = `.fail 9`. Fewer than 48
   top-level keys = `.fail 9`. Missing either sentinel line = `.fail 41`.

   NOW output the COMPLETE save block using `KM_SaveBlock_Template.md`
   (EXHAUSTIVE MODE — every field present, 48 top-level keys, all 8 log
   blocks populated) with `player.companions[]` and `seeker_1`–`seeker_5`
   already populated. Custom structure or omitted fields = `.fail 9`.
5. ONLY THEN proceed to the prologue.

**⛔ PROHIBITED until step 4 is complete:**
- Any scene narration or world description.
- Any NPC dialogue or location flavor.
- Any "you arrive at Jamandi's manor" or equivalent.
- Announcing you will show the screen without actually showing it.
- Assuming a default companion roster from training data.
- Outputting a save block before companions AND seekers are recorded.

Skipping or summarizing the Pick-10 screen = `.fail 9` (file content ignored).
Outputting save block before Pick-10 + Pick-5 complete = `.fail 9` (broken-seed save).
Starting the prologue before `player.companions[]` is confirmed = `.fail 3` (agency violation).

**If DM skipped any prompt:** player types `.fail 3 — prompt [N] skipped`.
DM reprints prompt [N] and continues.

---

## 📋 DM NOTES

- These prompts are the ONLY way the player chooses weapon / armor / stat /
  deity / skills. The build file's default line is a SUGGESTION, not a
  decision.
- Never combine prompts into one menu. One prompt per response. Wait between.
- If the build file has a richer alternatives table, USE IT instead of the
  generic fallback lists above. Generic fallbacks are last-resort only.
- Chosen values override the build file's stat block. If player picks a
  Finesse weapon on a STR-locked build, reject the choice and re-prompt.
- Companion builds (Pick-10): these 4 prompts do NOT run for companions.
  Companion builds use starred ★ defaults from KM_Companions_Builds.md.
  Only the player character gets setup prompts.

---

*KM_BuildSetup.md — Kingmaker PF2e Text Adventure | 8-prompt build customization*
*Enforces player agency over ancestry, stat, weapon, armor, deity, and skills*
