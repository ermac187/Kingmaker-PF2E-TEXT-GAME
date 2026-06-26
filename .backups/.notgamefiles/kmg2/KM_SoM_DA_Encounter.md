# KINGMAKER — SECRETS OF MAGIC SPELLS
## Secrets of Magic | Magus, Summoner Focus Spells + New Spell Additions

> **DM:** Load this file when Build 7 (Magus) or Build 19 (Summoner) casts a
> focus spell, uses a Spellstrike combo not covered in KM_Spells_Arcane_Primal.md,
> or when any spell from Secrets of Magic is cast or identified.
> Add to KM_LoadRules.md trigger: "Magus focus spell or Summoner eidolon spell" → this file.

---

## ⚡ MAGUS FOCUS SPELLS (Build 7)

> Focus spells cost 1 Focus Point. Regain with Refocus (10 min, practice arcane kata).
> Magus starts with 1 Focus Point. Some feats increase this to 2 or 3.

### Conflux Spells (Hybrid Study — Laughing Shadow)

**Dimensional Assault** *(Laughing Shadow signature — always available)*
- Cast: 1A (free action before a Strike)
- Effect: Teleport up to your Speed, then make a Strike as part of the same action. The teleport does not trigger reactions. If Arcane Cascade is active, add +1d6 elemental damage to the Strike.
- Heightened: No heightening — scales with character level naturally.

**Dimensional Disappearance** *(L5 unlock)*
- Cast: 1A
- Effect: Become Invisible and Undetected until the start of your next turn, or until you Strike (whichever comes first). Can be used after a Spellstrike to escape before reactions fire.

**Blink Charge** *(L9 unlock)*
- Cast: 2A
- Effect: Teleport up to 60 ft and Strike three times (each at −2 MAP cumulative). Each Strike can target a different creature. You may teleport between each Strike (up to 15 ft per teleport).

---

### Spellstrike Spells (Arcane, best combos for Build 7)

> These are standard arcane spells used specifically for Spellstrike delivery.
> Listed here with Spellstrike-specific notes not covered in KM_Spells_Arcane_Primal.md.

**Shocking Grasp + Spellstrike**
- Combined action: 2A (1 for Spellstrike, spell slot expended)
- Damage: Weapon damage + 2d12 electricity (L1) or 4d12 (L3 heightened)
- Critical: +2d6 persistent electricity; target wearing metal armor is Flat-footed until end of their next turn
- Best use: Opening strike from Arcane Cascade position

**True Strike + Spellstrike**
- Action: 1A (True Strike) + 2A (Spellstrike) = 3 actions total
- Effect: Roll the Spellstrike attack twice, take higher result. Ignore the multiple attack penalty on this attack.
- Note: Burn this on high-AC targets or when the Spellstrike spell is particularly powerful

**Vampiric Touch + Spellstrike** *(L3)*
- Combined: 2A
- Damage: Weapon damage + 6d6 void; you gain half the void damage as Temp HP
- Critical: Full void damage → Temp HP
- Best use: When at below half HP — the heal-back makes it safe to be in melee

**Phantasmal Killer + Spellstrike** *(L4)*
- Combined: 2A
- Effect: Strike hits → target must Will save or take 8d6 mental and Frightened 4; on crit fail, Fort save or die
- Note: Highest burst potential of any L4 Spellstrike. Use on humanoids (worst Will saves).

**Disintegrate + Spellstrike** *(L6)*
- Combined: 2A
- Damage: Weapon damage + 14d10 force on hit; if target reduced to 0 HP by this attack: disintegrated (no raise dead without Resurrection or Wish)
- Note: Save this for bosses. 14d10 will one-shot most non-boss enemies.

---

### Arcane Cascade (Stance — always active after Spellstrike)

> Arcane Cascade is a stance, not a spell. It activates automatically after any Spellstrike.

**While in Arcane Cascade:**
- +1d6 damage of the last spell's energy type on all melee Strikes
- +10 ft Speed
- If no energy type (force/physical spell): +2 force damage instead

**Losing Arcane Cascade:** Cast a non-cantrip spell, use Spellstrike again, or be Stunned/Paralyzed.

**Reactivating:** Cast a cantrip as part of entering Cascade stance (free action at L3+).

---

## 🌀 SUMMONER FOCUS SPELLS (Build 19)

> Summoner focus spells support the Eidolon. Most require the Eidolon to be manifested.
> Focus Points: 1 at L1. Increase to 2 at L3 with Evolution feats.

**Boost Eidolon** *(L1, always available)*
- Cast: 1A (Free action at L7 with Greater Boost feat)
- Duration: Until end of your next turn
- Effect: Eidolon gains +2 status bonus to attack rolls and damage rolls
- Note: Use this every turn before the Eidolon attacks. It's your most efficient action.

**Reinforce Eidolon** *(L1)*
- Cast: 1A
- Duration: Until end of your next turn
- Effect: Eidolon gains +2 status bonus to AC and saves
- Note: Use when a powerful enemy is targeting the Eidolon.

**Manifest Eidolon** *(Special — not a focus spell)*
- Cast: 3A
- Effect: Bring the Eidolon into the world. It appears in a space adjacent to you.
- Note: If the Eidolon is reduced to 0 HP, it returns to your soul; you must use this again to resummon it. You take 2d6 mental damage when it returns.

**Transcribe Moment** *(L5)*
- Cast: Reaction (trigger: Eidolon critically hits)
- Effect: The critical hit also targets one additional creature adjacent to the original target. It deals the same damage (not a critical — normal damage roll).

**Twin Eidolon** *(L11)*
- Cast: 2A
- Duration: 1 round
- Effect: Create a duplicate of the Eidolon that can act independently. The duplicate has full HP and takes a full turn. At the end of the round, the duplicate collapses. Usable 1/day.

---

## 📚 SECRETS OF MAGIC — NEW SPELLS (All Traditions)

> These spells appear in Secrets of Magic and are available to any caster of the
> listed tradition at the listed level. Add to the appropriate tradition file when needed.

### New Arcane/Occult Spells

| Spell | Level | Traditions | Cast | Save | Effect |
|-------|-------|-----------|------|------|--------|
| Tether | 1 | Arc/Occ | 2A | Ref | Link two creatures; if they move more than 30 ft apart, both take 2d6 force |
| Runic Impression | 1 | Arc | 2A | — | Stamp a weapon rune onto a surface; lasts 1 hour; first to pick up gains rune effect |
| Improbable Collapse | 3 | Arc | 2A | Ref | Target's armor compresses; −2 AC + Clumsy 2 for 1 min (Fort ends) |
| Envenom Companion | 2 | Arc/Prim | 2A | — | Your animal companion's attacks gain poison (1d4 Con damage, Fort DC 18) for 1 min |
| Scatter Scree | 4 | Arc/Prim | 2A | — | Create difficult terrain in 20-ft burst that lasts 1 hour; moving through deals 1d6 piercing |
| Blazing Dive | 5 | Arc | 2A | Ref | Fly up 120 ft then dive; 10d6 fire in 10-ft burst at landing point |
| Seal Fate | 7 | Arc/Occ | 2A | Will | Target is Doomed 1 permanently; Will save each week reduces by 1 |
| Eclipse Burst | 7 | Arc/Occ | 2A | Ref/Fort | 8d10 cold (Ref) + Blinded (Fort) in 20-ft burst |
| Infectious Melody | 3 | Occ | 2A | Will | Melody spreads compulsion to attack nearest creature; 30-ft burst |
| Hollow Heart | 5 | Occ | 2A | Fort | Target loses emotion permanently until cured; immune to fear and morale but also courage and inspiration |
| Unfettered Pack | 5 | Prim | 2A | — | Up to 6 animals gain Haste for 1 min |
| Nature's Reprisal | 5 | Prim | Reaction | Ref | Trigger: creature damages a plant or animal. Entangled + 4d8 piercing (vines) |
| Elemental Annihilation Wave | 9 | Arc/Prim | 2A | Ref | 500-ft line; 10d6 of chosen element; half width 60-ft burst at end |

### New Divine Spells

| Spell | Level | Cast | Save | Effect |
|-------|-------|------|------|--------|
| Draw the Lightning | 2 | 2A | Ref | Lightning rod: next lightning strike redirected to you; you take half, rest negated |
| Spirit Sense | 2 | 2A | — | Detect undead and spirits within 60 ft for 10 min; know exact location |
| Spiritual Anamnesis | 3 | 2A | Will | Force target to relive a memory (you choose which); Stunned 1 + Confused 1 rnd on fail |
| Savor the Sting | 1 | Reaction | Fort | Trigger: target takes physical damage. They also take 1d4 mental; if they fail save, they feel compelled to hit the same attacker again |
| Angelic Wings | 4 | 2A | — | You grow wings; Fly Speed 40 ft for 10 min |
| Heal Animal | 1 | 2A | — | As Heal but targets animals/beasts only; +1d8 extra healing |
| Word of Truth | 4 | 2A | Will | Target cannot lie for 1 hour; can choose to stay silent instead |
| Celestial Brand | 5 | 2A | — | Brand one creature; it glows; +1d6 good damage vs it for all allies; invisible creatures revealed |

---

## ⚙️ MAGUS SPELLSTRIKE RULES (Complete Reference)

> Full Spellstrike rules for Build 7. Supersedes any summary elsewhere.

### Standard Spellstrike
1. Cast a spell that requires 1 or 2 actions with a single target or melee range as part of Spellstrike (costs 2A total)
2. Make a melee Strike
3. On hit: spell effect delivers through the weapon. The spell's effect activates as if it had hit the target.
4. On miss: the spell is lost (expended) but deals no damage
5. On critical hit: the spell effect is also a critical (double damage dice for the spell if applicable)

### Recharging Spellstrike
- Spellstrike is expended after use. Recharge methods (each costs 1A):
  - Cast a cantrip
  - Use a Conflux spell (focus spell)
  - Use Arcane Cascade activation

### What CAN be Spellstriked
- Any spell with a single target that requires a spell attack roll OR that you deliver by touch
- Cantrips: Electric Arc (2 targets, pick one), Produce Flame, Gouging Claw
- L1–L9 spells: Shocking Grasp, Vampiric Touch, Disintegrate, Phantasmal Killer, Finger of Death

### What CANNOT be Spellstriked
- Area spells (Fireball, Cone of Cold) — unless a feat allows it
- Spells that target "you" only
- Spells with a casting time of 3+ actions
- Buff spells that don't target enemies

### MAP and Spellstrike
- Spellstrike counts as a Strike for MAP purposes
- If you've already Struck this turn, Spellstrike is at MAP (−5 or −10)
- True Strike before Spellstrike ignores the MAP penalty for that Strike

---

## 🌀 SUMMONER EIDOLON TYPES (Build 19 — Anger Phantom)

> The Anger Phantom eidolon is Build 19's default. Stats scale with level.
> Other eidolon types listed for reference if player switches via retraining.

### Anger Phantom (Default — Build 19)
- **Size:** Medium (Large at L7 via Evolution)
- **Strikes:** Fist (1d6+4 B, Agile) + Spiritual Strike (1d6 force on crit)
- **Ability:** Furious Assault — 1/round, after a hit, make a free Shove (Athletics +level+Str vs Fort)
- **Skill:** Intimidation
- **Senses:** Darkvision

### Devil Eidolon (alternative)
- **Strikes:** Claw (1d6 S) + Tail (1d4 P, Agile)
- **Ability:** Tempt — 1/day, Charm (Will DC 20)
- **Resistances:** Fire 5, Cold 5

### Fey Eidolon (alternative)
- **Strikes:** Branch (1d8 B) or Vine (1d4, Reach 10 ft)
- **Ability:** Fey Step — 1/round, teleport 15 ft as free action after a Strike
- **Skill:** Nature or Deception (choose at creation)

### Plant Eidolon (alternative)
- **Strikes:** Root (1d10 B) + Tendril (1d6, Reach 10 ft)
- **Ability:** Entangling Growth — 1/day, Entangle in 15-ft burst (Ref DC 20)
- **Resistances:** Poison immunity; resist physical 5

### Undead Eidolon (alternative — Jaethal approval)
- **Strikes:** Claw (1d8 S) + Void Drain (1d4 void, touch)
- **Ability:** Undead Nature — immune to death, disease, poison, sleep
- **Weakness:** Positive 10

---

*KM_SoM_DA_Encounter.md — Secrets of Magic Section v1.0*
*Source: PF2e Secrets of Magic (Paizo)*
# KINGMAKER — DARK ARCHIVE CONTENT
## Dark Archive | Psychic Amps, Thaumaturge Implements, Dark Archive Spells

> **DM:** Load this file when Build 14 (Psychic) uses an Amp, when Build 6 or 12
> (Thaumaturge) uses an Implement ability not in other files, or when any
> Dark Archive spell is cast or identified.
> Add to KM_LoadRules.md trigger: "Psychic Amp or Thaumaturge implement ability" → this file.

---

## 🧠 PSYCHIC AMPS — COMPLETE REFERENCE (Build 14)

> Amps are enhanced versions of cantrips. Using an Amp costs 1 action more than
> the base cantrip AND expends 1 Psi point (Psychic's resource pool).
> **Psi Points:** Equal to your level ÷ 2 (round up). Regain all after 10 min rest.
> **Unleash Psyche:** Spend all Psi points (minimum 1); for 3 rounds all Amps are free
> (no Psi cost) and enhanced. Usable 1/10 min. After it ends: Stupefied 1 for 1 minute.

### CANTRIP: TELEKINETIC PROJECTILE
**Base (1A):** 1d6+spellmod bludgeoning to one target; no attack roll needed
**Amped (2A, 1 Psi):** Three projectiles; each deals 1d6+spellmod; each can target a different creature; all use the same spell DC (Reflex save — half on success)
**Unleashed:** Five projectiles; +spellmod to each; automatically pick up and hurl a Bulk 1 object from the environment for one of the projectiles (+1d8 bonus damage)

---

### CANTRIP: DAZE
**Base (2A):** 1d6 mental to one target; Will save; Stunned 1 on crit fail
**Amped (3A, 1 Psi):** 4d6 mental; Will save; Stunned 2 on fail; Stunned 3 on crit fail; affects up to 2 targets
**Unleashed:** 6d6 mental; Stunned 1 on success; Stunned 3 on fail; Stunned 4 on crit fail; affects all in 15-ft burst

---

### CANTRIP: MIND SPIKE
**Base (2A):** 1d6+spellmod mental to one target; −1 Will saves until end of next turn on fail
**Amped (2A, 1 Psi):** 3d6+spellmod mental to TWO targets; both take −2 Will saves for 1 round; if both fail, each also takes 1d4 persistent mental damage
**Unleashed:** 5d6+spellmod; −3 Will saves; persistent mental 1d6; affects three targets

---

### CANTRIP: SHIELD (Psychic version)
**Base (1A):** +1 circ. AC until next turn; Hardness 5
**Amped (1A, 1 Psi):** +2 circ. AC; Hardness 10; lasts until start of YOUR next turn (not just until their turn)
**Unleashed:** +3 circ. AC; Hardness 15; you can use Shield Block as a free action once this turn

---

### CANTRIP: TELEKINETIC REND (Psi cantrip — unlocked at L3)
**Base (2A):** 2d6+spellmod bludgeoning to one target; no save (automatic hit); pushes 5 ft
**Amped (2A, 1 Psi):** 4d6+spellmod; pushes 10 ft; target is also Flat-footed until end of next turn
**Unleashed:** 6d6+spellmod; pushes 20 ft; target is Prone on fail (no save — automatic)

---

### CANTRIP: GRAVITY WEAPON (Psi cantrip — unlocked at L5)
**Base (2A):** Next weapon Strike deals +2d6 bludgeoning from gravitational force
**Amped (2A, 1 Psi):** +4d6 bludgeoning; if target fails Fort save, also Knocked Prone
**Unleashed:** +6d6; Knocked Prone (Fort or Immobilized 1 round instead of just Prone)

---

### CANTRIP: DRAW THE LIGHTNING (Psi cantrip — unlocked at L9)
**Base (2A):** 2d12 electricity to all in 30-ft line; Ref half
**Amped (2A, 1 Psi):** 4d12 electricity; 30-ft line + 10-ft wide; Ref half; on crit fail target is Stunned 1
**Unleashed:** 6d12; 60-ft line; Stunned 1 on fail; Stunned 2 on crit fail

---

### CANTRIP: SHATTER MIND (Psi cantrip — unlocked at L13)
**Base (2A):** 3d6 mental to one target; Will half
**Amped (2A, 1 Psi):** 6d6 mental; Will half; on fail: Stupefied 2 for 1 round
**Unleashed:** 8d6 mental; Stupefied 3 on fail; Stupefied 4 on crit fail; affects 2 targets

---

### UNLEASH PSYCHE — FULL RULES

**Activating:** Free action, any time. Spend all remaining Psi points (minimum 1).
**Duration:** 3 rounds from activation.
**While active:**
- All Amps cost 0 Psi points (free)
- All Amps use the Unleashed version (listed above)
- +2 status bonus to spell DCs
- Your eyes glow with psychic light; cannot be concealed as a spellcaster

**After it ends (when 3 rounds expire OR you choose to end it):**
- Stupefied 1 for 1 minute
- All Psi points expended

**Recovery:** 10 min rest in a quiet space. Regain all Psi points.

---

## 🔮 THAUMATURGE IMPLEMENTS — COMPLETE REFERENCE (Builds 6 and 12)

> Thaumaturges use Implements — held objects with magical significance.
> Each Implement has a passive benefit and an active ability (1A or reaction).
> Builds 6 and 12 each have two Implements. They must hold at least one to benefit.

### WEAPON IMPLEMENT (Build 12 primary, Build 6 secondary)

**Passive:** Weapon deals +2 damage to creatures you've Exploited (Exploit Vulnerability used on them this combat)

**Intensify (1A):** Your weapon gains one of these effects for 1 minute (choose when activating):
- Flaming (+1d6 fire on all Strikes)
- Shock (+1d6 electricity)
- Frost (+1d6 cold)
- Disrupting (+1d6 spirit vs undead)

**Implement's Interruption (Reaction):** Trigger: adjacent enemy attacks an ally. Make a Strike against that enemy before the attack resolves. If you hit, the enemy's attack is at −2.

**At L7 — Weapon Implement (Greater):**
- Intensify lasts until end of encounter (not 1 minute)
- Critical hits with the weapon apply the Intensify energy as 1d10 persistent

**At L13 — Implement Mastery:**
- Intensify grants TWO energy types simultaneously
- +4 damage vs Exploited creatures (up from +2)

---

### CHALICE IMPLEMENT (Build 12 secondary, Build 6 tertiary)

**Passive:** Once per combat, when you successfully Exploit Vulnerability, you heal 1d6 HP

**Drink Deep (1A):** Drink from the Chalice to regain HP equal to your level + Cha modifier. This is a healing action that functions like a potion (not a spell). Usable 1/10 min.

**Martyr's Implement (Reaction):** Trigger: an ally within 30 ft takes damage. You take half that damage instead; the ally takes the other half. This can reduce the ally's damage but you cannot reduce your share further.

**At L7 — Chalice (Greater):**
- Drink Deep heals 2d6+level+Cha
- Martyr's Implement: ally takes no damage; you take it all (still can't reduce yours)

**At L13 — Implement Mastery:**
- Drink Deep heals 3d6+level+Cha; also removes one condition (Frightened, Sickened, or Enfeebled — your choice)

---

### TOME IMPLEMENT (Build 6 secondary)

**Passive:** +2 circ. bonus to Recall Knowledge checks

**Esoteric Lore (Passive):** You can always Recall Knowledge about any topic using Occultism, regardless of what skill would normally apply

**Share Knowledge (1A):** Recall Knowledge about a creature and share the result with all allies. Each ally gains the benefit of the knowledge (e.g., if you learn its weakness, all allies can exploit it this combat).

**Tome's Reflection (Reaction):** Trigger: you or an ally fails a save. You instantly Recall Knowledge about the source of the effect. If you succeed, the ally can reroll the save (keep second result).

**At L7 — Tome (Greater):**
- Recall Knowledge critical successes reveal an additional piece of tactical information (the DM states one combat-relevant fact not normally available)

---

### AMULET IMPLEMENT (available to both builds via feat)

**Passive:** +1 circ. AC against attacks from creatures you've Exploited

**Amulet's Abeyance (Reaction):** Trigger: you would take damage. Reduce damage by your level + Cha modifier. Usable 1/10 min.

**Spirit's Wrath (1A):** Amulet fires a bolt — ranged attack (Occultism +level+Cha vs AC): 2d6 spirit + Frightened 1 on hit. Range 30 ft.

**At L7 — Amulet (Greater):**
- Spirit's Wrath: 4d6 spirit; Frightened 2; range 60 ft
- Abeyance: reduce damage by 2×(level + Cha mod)

---

### EXPLOIT VULNERABILITY — FULL RULES

> Exploit Vulnerability is the Thaumaturge's core action. Everything else builds on it.

**Action:** 1A
**Requirement:** You have at least one Implement in hand
**Effect:** Make an Esoteric Lore check (Occultism, DC = 10 + creature level):

| Result | Effect |
|--------|--------|
| Critical Success | Creature has a weakness of 2+level/2 to your attacks this combat; ALSO learn one additional fact about it |
| Success | Creature has a weakness of 2+level/4 (min 2) to your attacks this combat |
| Failure | No weakness this turn; try again next turn (it costs 1A each attempt) |
| Critical Failure | No weakness; you can't attempt again until next combat |

**Weakness scaling:**
| Level | Success Weakness | Crit Success Weakness |
|-------|-----------------|----------------------|
| 1–4 | 2 | 4 |
| 5–8 | 3 | 6 |
| 9–12 | 4 | 8 |
| 13–16 | 5 | 10 |
| 17–20 | 6 | 12 |

**Intensify Vulnerability (L3 feat):**
- On a success, the weakness applies to ALL damage from you (not just weapon attacks)
- On a crit success, allies within 10 ft also benefit from half the weakness value

**Intensify Vulnerability II (L9 feat):**
- Allies within 10 ft benefit from the full weakness value (not half)
- You can maintain two Exploits simultaneously (one per Implement)

---

## 📚 DARK ARCHIVE SPELLS

### New Occult/Psychic Spells

| Spell | Level | Traditions | Cast | Save | Effect |
|-------|-------|-----------|------|------|--------|
| Phantom Pain | 1 | Occ | 2A | Will | 2d4 mental + Sickened 1 on fail; Sickened 2 on crit fail; 1 min |
| Ectoplasmic Expulsion | 2 | Occ | 2A | Fort | 3d6 force; expel one condition affecting you onto target (it gains the condition you had) |
| Curse of Lost Time | 3 | Occ | 2A | Fort | Target ages rapidly; Clumsy 2 + Enfeebled 2 for 1 min; on crit fail: permanent Drained 1 |
| Thoughtform | 3 | Occ | 2A | Will | Create a mental duplicate of yourself; it has 20 HP and you can perceive through it |
| Mental Static | 4 | Occ | 2A | Will | 30-ft burst; all spellcasters in area must DC 22 Will or lose their prepared spell (random) |
| Read the Room | 2 | Occ | 1A | — | Instantly sense the emotional state of everyone in 30 ft; know who is hostile/fearful/hiding something |
| Brain Drain | 5 | Occ | 2A | Will | Steal prepared spell from caster (your choice of which); you can cast it once within 1 hour |
| Pyschokinetic Hand | 1 | Occ | 1A | — | As Mage Hand but 60-ft range and can move 3 Bulk; can be used to make simple attacks (1d4+spellmod force, no MAP) |
| Paranoia | 2 | Occ | 2A | Will | Target sees all creatures as enemies; attacks randomly each round for 1 min (Will each round to end) |
| Synesthesia | 5 | Occ | 2A | Fort | Target's senses scramble; Blinded + Deafened for 1 min; every action requires DC 22 flat check or fails |

### New Thaumaturge-Adjacent Spells (Occult/Divine)

| Spell | Level | Traditions | Cast | Save | Effect |
|-------|-------|-----------|------|------|--------|
| Object Reading | 2 | Occ | 1 min | — | Touch object; learn last creature to hold it, and one significant event involving it |
| Spirit Spiral | 3 | Div/Occ | 2A | Will | Call a spirit from the area; it answers up to 5 questions truthfully (knows only what it knew in life) |
| Fear the Sun | 4 | Div | 2A | Fort | Target that is light-vulnerable (undead, vampire, etc.) takes 6d6 fire + Blinded for 1 min on fail |
| Delay Affliction | 2 | Div | 2A | Fort | Pause one disease or curse affecting target; it doesn't progress for 24 hours |
| Entrench | 3 | Div/Occ | 2A | Fort | Target cannot move from current position for 1 min (Will each round to end); can still act otherwise |

---

*KM_SoM_DA_Encounter.md — Dark Archive Section v1.0*
*Source: PF2e Dark Archive (Paizo)*
# KINGMAKER — ENCOUNTER BUILDING & ALCHEMIST CLASS
## Encounter Building & Alchemist Rules

> **DM:** Load this file when building a combat encounter, checking if a fight
> is appropriately balanced, or when a player selects a custom Alchemist build.

---

## ⚔️ ENCOUNTER BUILDING RULES

> PF2e uses an XP budget system. The party earns XP for defeating enemies.
> The DM builds encounters by spending an XP budget against the party's level.

### ENCOUNTER DIFFICULTY BUDGETS (4-player party)

| Difficulty | XP Budget | Expected Outcome |
|------------|-----------|-----------------|
| Trivial | 40 XP | Party wins easily; no resources spent |
| Low | 60 XP | Party wins; minor resource use |
| Moderate | 80 XP | Party wins; meaningful resource use |
| Severe | 120 XP | Party likely wins; significant resources spent; possible PC drops |
| Extreme | 160 XP | Party may lose; TPK possible |

**Party size adjustments:**
- 3 players: −20 XP to all budgets
- 5 players: +20 XP to all budgets
- 6 players: +40 XP to all budgets

---

### ENEMY XP VALUES (by level relative to party)

| Enemy Level vs Party Level | XP Value |
|---------------------------|----------|
| Party level −4 | 10 XP |
| Party level −3 | 15 XP |
| Party level −2 | 20 XP |
| Party level −1 | 30 XP |
| Same as party | 40 XP |
| Party level +1 | 60 XP |
| Party level +2 | 80 XP |
| Party level +3 | 120 XP |
| Party level +4 | 160 XP |

**Example — Party is L5, building a Moderate encounter (80 XP budget):**
- 2 bandits (L4 = 30 XP each) + 1 lieutenant (L6 = 80 XP) = too much (140 XP)
- 2 bandits (L4 = 30 XP each) + 1 sergeant (L5 = 40 XP) = exactly 100 XP (Severe)
- 3 bandits (L4 = 30 XP each) = 90 XP (between Moderate and Severe — good)
- 1 troll (L5 = 40 XP) + 2 wolves (L3 = 20 XP each) = 80 XP (Moderate)

---

### ENCOUNTER BUILDING GUIDELINES

**Terrain and positioning:**
- Flat, open fights favor heavily armored builds (Builds 1–5)
- Elevated ranged positions favor Builds 6, 7, 15
- Chokepoints favor tanks; open ground favors cavalry/reach weapons
- Add terrain features: difficult terrain (slows), cover objects (Stealth), hazards (traps)

**Enemy composition:**
- Solo boss: use a creature 3–4 levels above party; add minions if budget allows
- Minion swarm: many weak enemies testing AoE and action economy
- Elite mooks: 2–3 enemies at party level; tests sustained DPR
- Mixed: 1 elite + 2–3 weaker; most common in Kingmaker

**Minion rule:** Enemies with the Minion trait cost half their XP value (round down). They only act when commanded by a leader creature.

**Elite and Weak adjustments (quick scaling):**
- **Elite:** +2 to all modifiers, +HP (level +2 equivalent) — add 10 XP to cost
- **Weak:** −2 to all modifiers, −HP (level −2 equivalent) — subtract 10 XP from cost

---

### KINGMAKER ENCOUNTER PACING BY CHAPTER

| Chapter | Typical Daily Encounters | Recommended Difficulty Mix |
|---------|------------------------|---------------------------|
| Ch1 (L1–4) | 3–5 | 1 Severe, 2 Moderate, 1–2 Low |
| Ch2 (L5–8) | 3–4 | 1 Extreme (boss), 2 Severe, 1 Low |
| Ch3 (L9–12) | 2–4 | 1 Extreme, 1–2 Severe, 1 Moderate |
| Ch4 (L13–16) | 2–3 | 1 Extreme, 1 Severe, 1 Moderate |
| Ch5+ (L17–20) | 2–3 | 2 Extreme, 1 Severe |

**Resource depletion:** A well-paced day drains 60–70% of the party's spell slots, Focus Points, and consumables before the final encounter. If the party reaches the boss fight at full resources, the day was too easy.

---

### TRAP AND HAZARD XP

Traps and hazards also contribute to encounter XP.

| Hazard Level | XP (Simple Hazard) | XP (Complex Hazard) |
|-------------|-------------------|---------------------|
| Same as party | 10 XP | 40 XP |
| Party +1 | 15 XP | 60 XP |
| Party +2 | 20 XP | 80 XP |
| Party +3 | 30 XP | 120 XP |

**Simple hazard:** One-action threat (a pit trap, a pressure plate, a falling boulder)
**Complex hazard:** Multi-round threat with its own initiative (a rolling boulder room, a flooding chamber, an animated statue that keeps attacking)

---

### ENCOUNTER XP REWARDS (player XP)

Players earn XP equal to the encounter's total XP budget when they complete it.

| Encounter Difficulty | Player XP Earned |
|---------------------|-----------------|
| Trivial | 40 XP |
| Low | 60 XP |
| Moderate | 80 XP |
| Severe | 120 XP |
| Extreme | 160 XP |

**Bonus XP for non-combat solutions:**
- Negotiating past an encounter: 30–50% of its XP
- Stealth bypass (no combat): 25% of its XP
- Creative solution (collapses ceiling on enemies): full XP

---

## 🧪 ALCHEMIST CLASS REFERENCE

> For custom builds choosing Alchemist. Not one of the 20 preset builds.
> Use this if a player selects Alchemist in custom build mode.

### Core Stats
| Stat | Value |
|------|-------|
| HP per level | 8 + Con |
| Key Ability | Intelligence |
| Saves | Expert Fort, Trained Ref, Trained Will |
| Proficiencies | Alchemical bombs, simple weapons, unarmed |
| Armor | Light armor |

### Core Mechanic: Advanced Alchemy + Infused Reagents

**Infused Reagents:** Each day, you gain reagents equal to your level + Int mod. These are used to create items.

**Quick Alchemy (1A):** Spend 1 reagent to create any alchemical item you have a formula for. Item lasts until end of turn if not used (infused — magical version of the item). Full-cost items can be prepared during daily prep.

**Advanced Alchemy (daily prep):** During daily prep, spend reagents to create batches of 2 alchemical items each. These last until next daily prep.

**Formula Book:** Alchemist knows all common alchemical formulas of their level or lower. Rare formulas must be found or purchased.

---

### Alchemist Research Fields (Subclass)

**Bomber:** Alchemical bombs deal +1 damage per damage die. Critical hits with bombs deal persistent damage equal to the number of damage dice.

**Chirurgeon (Healer):** Elixirs of Life you create restore the maximum amount (no dice roll — always max). You can use Quick Alchemy to create a Healing Potion as 1A (costs 1 reagent; heals as standard potion).

**Mutagenist:** Mutagens you create last 1 hour (not 10 minutes). You can be under two mutagen effects simultaneously without the usual conflict penalty.

**Toxicologist:** Poisons you create are 2 levels higher for the purpose of the Fort save DC. You are immune to your own poisons.

---

### Alchemist Level Progression

| Lvl | HP+ | Class Features |
|-----|-----|----------------|
| 1 | 8+Con | Research Field, Advanced Alchemy, Quick Alchemy, Formula Book |
| 2 | 8+Con | Alchemist feat |
| 3 | 8+Con | Mutagenic Flashback, Perpetual Infusions (L1 items free/day) |
| 4 | 8+Con | Alchemist feat |
| 5 | 8+Con | Ability boost, Alchemical Alacrity (Quick Alchemy for 2 items) |
| 6 | 8+Con | Alchemist feat |
| 7 | 8+Con | Perpetual Potency (L3 items free/day) |
| 8 | 8+Con | Alchemist feat |
| 9 | 8+Con | Double Elixir (one Quick Alchemy creates 2 items) |
| 10 | 8+Con | Ability boost, Alchemist feat |
| 11 | 8+Con | Perpetual Perfectionism (L11 items free/day) |
| 12 | 8+Con | Alchemist feat |
| 13 | 8+Con | Greater Field Discovery (Research Field upgrade) |
| 14 | 8+Con | Alchemist feat |
| 15 | 8+Con | Ability boost, Alchemical Mastery |
| 16–20 | 8+Con | Alchemist feats, capstones |

**Perpetual Infusions:** Free items per day by Research Field:
- Bomber: 2 Alchemist's Fire (Lesser) free daily
- Chirurgeon: 2 Elixirs of Life (Lesser) free daily
- Mutagenist: 2 Mutagens (any type, Lesser) free daily
- Toxicologist: 2 Poisons (any type, Lesser) free daily

---

### Key Alchemist Feats (L1–L10)

| Feat | Level | Effect |
|------|-------|--------|
| Calculated Splash | 1 | Splash damage = Int mod (instead of 1) |
| Efficient Alchemy | 1 | During daily prep: create 3 items per batch instead of 2 |
| Enduring Alchemy | 1 | Quick Alchemy items last until end of NEXT turn (not this turn) |
| Poison Weapon | 2 | Apply poison to weapon as free action (1/round) |
| Smoke Bomb | 2 | Bombs also create Concealment (smoke) in 10-ft burst for 1 min |
| Combine Elixirs | 4 | Mix two elixirs into one; target gains both effects from one action |
| Debilitating Bomb | 4 | Bomb crits apply a condition (Clumsy/Enfeebled/Stupefied 1) |
| Directional Bombs | 4 | Choose which squares receive splash damage |
| Sticky Bomb | 6 | Bomb targets take persistent damage equal to bomb's splash damage |
| Healing Bomb | 6 | Create a healing bomb: 2d6+Int healing in splash; heals allies, damages undead |
| Expanded Splash | 8 | Splash radius increases to 10 ft |
| Greater Debilitating Bomb | 8 | Conditions from Debilitating Bomb increase to 2 |
| Merciful Elixir | 8 | Add Remove Fear or Remove Sickness to any Elixir of Life created |
| Powerful Alchemy | 10 | Save DCs for your items = 10 + proficiency + Int (up from flat +1) |

---

### Alchemist Starting Build (if player selects custom Alchemist)

**Recommended:** Bomber field for combat relevance, or Chirurgeon for party support.

**Bomber L1 Stat Block:**
```
HP: 8+Con | AC: 16 (Leather + trained)
STR 10 | DEX 16(+3) | CON 16(+3) | INT 18(+4) | WIS 12(+1) | CHA 10
Fort +7 | Ref +5 | Will +3
Attacks: Alchemist's Fire (thrown 20 ft) d20+5, 1d8+1 fire + 1 splash
Skills: Crafting +8, Medicine +5, Nature +5, Arcana +6
Daily: 5+4=9 reagents | Perpetual: 2 Lesser Alchemist's Fire free
Feats: Calculated Splash
Gold: 15 gp + 20 gp reagent allowance
```

---

*KM_SoM_DA_Encounter.md — Encounter Building & Alchemist Section v1.0*
*Source: PF2e GM Core, Player Core (Paizo)*
