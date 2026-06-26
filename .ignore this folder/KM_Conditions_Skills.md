# KINGMAKER — CONDITIONS, DISEASES & CURSES
## KM_Conditions_Skills.md | Conditions & Skills Reference

> **DM:** Load this file when any condition, disease, or curse is applied, queried,
> or needs mechanical resolution. This is the authoritative source — do not
> apply conditions from memory.

---

## 📋 CONDITIONS REFERENCE

> Conditions are persistent states that modify a creature's capabilities.
> Unless noted, conditions end when their source ends or a specified action removes them.
> **Value conditions** (Frightened 2, Drained 1, etc.) reduce by 1 each turn unless noted.

### ATTITUDE CONDITIONS (NPC disposition)

| Condition | Meaning | Mechanical Effect |
|-----------|---------|------------------|
| Helpful | Wants to assist you | Will take significant risks to aid; Diplomacy DC −5 |
| Friendly | Likes you | Will help with low-risk requests; Diplomacy DC −2 |
| Indifferent | No opinion | Neutral; standard DCs |
| Unfriendly | Dislikes you | Won't help; Diplomacy DC +2 |
| Hostile | Wants to harm you | May attack; Diplomacy DC +5; Demoralize may cause flee |

---

### COMBAT CONDITIONS (alphabetical)

| Condition | Effect | Ends When |
|-----------|--------|-----------|
| **Blinded** | Can't see; all targets Concealed (20% miss); Flat-footed; −4 Perception | Source ends or magical cure |
| **Broken** | Item non-functional; can't be used until Repaired | Repair action (DC = item Hardness +10) |
| **Clumsy X** | −X to Dex-based rolls, DCs, AC | Value reduces 1/turn; source ends |
| **Confused** | Roll d8 each turn: 1–4 Strike random adjacent, 5–6 do nothing, 7–8 act normally | Will save each turn (DC = effect DC) |
| **Concealed** | 20% miss chance (DC 5 flat check) | Source ends |
| **Dazzled** | All targets Concealed to you | Source ends |
| **Deafened** | Can't hear; −2 Perception; spell failure (verbal) DC 5 flat check | Source ends |
| **Doomed X** | Dying threshold reduced by X (die at Dying 4−X) | Removed only by specific spells |
| **Drained X** | −X to Con-based rolls, max HP reduced by X×level | Reduces 1/long rest; Restoration |
| **Dying X** | Unconscious; Recovery check each turn (DC 10+X); Dying 4 = death | Stabilize action; Heal; Hero Point |
| **Encumbered** | −10 ft Speed; −1 all checks and DCs; armor ACP doubles | Reduce Bulk below encumbered threshold |
| **Enfeebled X** | −X to Str-based rolls and DCs | Reduces 1/turn; source ends |
| **Fascinated** | Flat-footed; can't act in a way that damages source; −2 Perception (other threats) | Hostile act by source; Will save |
| **Fatigued** | −1 to all checks and DCs; can't use exploration activities | 8 hours rest |
| **Flat-footed** | −2 AC | Source ends |
| **Fleeing** | Must Stride away from source each turn | Duration ends; source removed |
| **Frightened X** | −X to all checks and DCs | Reduces 1/turn at end of turn |
| **Grabbed** | Immobilized + Flat-footed; both grabber and grabbed | Escape action (Athletics/Acrobatics vs grabber DC); grabber releases |
| **Hidden** | Observers know approximate location; must Seek to detect; attacks vs you DC 5 flat | Observed |
| **Immobilized** | Can't use move actions; −10 ft Speed is irrelevant | Source ends; Escape action |
| **Invisible** | Undetected by sight; don't need Stealth to be Hidden vs sight | Source ends |
| **Observed** | Fully visible; no concealment | Hidden, Concealed, Invisible |
| **Off-Guard** | Same as Flat-footed: −2 AC | Source ends |
| **Paralyzed** | Flat-footed; can't act; Str/Dex-based DCs fail | Duration ends; specific cure |
| **Petrified** | Turned to stone; unconscious; immune to physical damage; Fort save each day | Stone to Flesh; specific cure |
| **Prone** | −2 attacks; Melee attacks vs you +1; Ranged attacks vs you −2; crawl 5 ft/action | Stand action (1A); if grabbed, can't stand |
| **Quickened** | +1 action per turn (specific restriction based on source) | Duration ends |
| **Restrained** | Immobilized + Flat-footed; can't use reactions | Escape (opposed Athletics vs DC) |
| **Sickened X** | −X all checks and DCs; can't Eat or Drink | Retch (1A, Fort DC = effect DC); reduces 1/turn |
| **Slowed X** | Lose X actions per turn | Duration ends |
| **Stunned X** | Lose X actions next turn (not per turn — total X actions lost) | Actions tick down |
| **Stupefied X** | −X Int/Wis/Cha checks, DCs, and spell DCs; spell failure DC flat check | Reduces 1/turn; Restoration |
| **Unconscious** | Unaware; Flat-footed; Blinded; −4 Perception; Dying if at 0 HP | Wake with 1+ HP; Stabilize if Dying |
| **Undetected** | Observers don't know location; DC 11 flat check to target correctly | Detected |
| **Wounded X** | Next time Dying: start at Dying X+1 instead of 1 | Remove with Treat Wounds (Medicine DC 20); Long rest |

---

### CONDITION INTERACTIONS

```
Grabbed → cannot Stride, Step, or use most move actions
Grabbed → both creatures are Flat-footed to each other
Dying → Recovery Check each turn: d20 + Fort bonus vs DC (10 + Dying value)
  Crit Success: Stable (lose Dying, keep Unconscious)
  Success: no change
  Failure: Dying +1
  Crit Fail: Dying +2
Dying 4 → Death (unless Doomed reduces threshold)
Wounded X stacks each time you recover from Dying
Wounded is cleared by: full rest + Treat Wounds (DC 20) OR Restoration spell
```

---

## 🦠 DISEASES

> Diseases progress through stages over time. Each listed interval, the afflicted
> makes a Fort save. Success = move to previous stage (or recover if at Stage 1).
> Failure = move to next stage. Critical failure = move 2 stages forward.
> Critical success = immediately recover.

### Filth Fever
**Source:** Sorrow Marshes travel, rats, giant frogs, open sewage
**Onset:** 1d4 days | **Saving Throw:** Fort DC 12 | **Interval:** 1 day

| Stage | Effect |
|-------|--------|
| Stage 1 | Fatigued |
| Stage 2 | Fatigued + Enfeebled 1 |
| Stage 3 | Fatigued + Enfeebled 2 |

**Treatment:** Antiplague (+2 Fort); Remove Disease (L3 divine/primal); Bed rest + Medicine DC 15

---

### Blinding Sickness
**Source:** Undead encounters in Ch3, Vordakai's tomb
**Onset:** 1 day | **Saving Throw:** Fort DC 16 | **Interval:** 1 day

| Stage | Effect |
|-------|--------|
| Stage 1 | Drained 1 |
| Stage 2 | Drained 2 |
| Stage 3 | Drained 2 + Blinded |
| Stage 4 | Drained 3 + Blinded (permanent if not cured within 1 week) |

**Treatment:** Remove Disease (L3); Restoration (reduces Drained); Medicine DC 22

---

### Ghoul Fever
**Source:** Ghoul bite or scratch (Vordakai's tomb, Ch3 undead encounters)
**Onset:** 1 day | **Saving Throw:** Fort DC 15 | **Interval:** 1 day

| Stage | Effect |
|-------|--------|
| Stage 1 | Drained 1 + Fatigued |
| Stage 2 | Drained 2 + Fatigued |
| Stage 3 | Paralyzed (Ghoul Paralysis — no actions) |
| Death | If killed while infected: rise as Ghoul in 24 hours |

**Treatment:** Remove Disease before Stage 3; Heal spell suppresses 1 hour

---

### Poison Sickness (generic taint)
**Source:** Poisoned water sources, Bloom corruption areas (Ch2)
**Onset:** 10 min | **Saving Throw:** Fort DC 13 | **Interval:** 1 hour

| Stage | Effect |
|-------|--------|
| Stage 1 | Sickened 1 |
| Stage 2 | Sickened 2 + Clumsy 1 |
| Stage 3 | Sickened 2 + Clumsy 2 + Drained 1 |

**Treatment:** Antitoxin (+2 Fort); Neutralize Poison; Medicine DC 18

---

### Voracious Plague (Bloom Disease, Ch2)
**Source:** Bloom-touched creatures; corrupted plant contact
**Onset:** 1 hour | **Saving Throw:** Fort DC 17 | **Interval:** 1 day

| Stage | Effect |
|-------|--------|
| Stage 1 | Fatigued + Sickened 1 |
| Stage 2 | Enfeebled 1 + Sickened 2 |
| Stage 3 | Enfeebled 2 + Stupefied 1 + Drained 1 |
| Stage 4 | Character transforms into Bloom thrall (story consequence) |

**Treatment:** Tristian's divine intervention (story); Remove Disease DC 22; Bald Hilltop consecration

---

### Mummy Rot
**Source:** Ancient tomb contact (Ch3, Vordakai's pyramid)
**Onset:** 1 minute | **Saving Throw:** Fort DC 20 | **Interval:** 1 day

| Stage | Effect |
|-------|--------|
| Stage 1 | Drained 1 (cannot be healed by non-magical means) |
| Stage 2 | Drained 2 (as above) |
| Stage 3 | Drained 3 + Doomed 1 |
| Death | Cannot be raised by Raise Dead — only Resurrection or Wish |

**Treatment:** Remove Disease + Restoration simultaneously (both required); DC 25 Medicine

---

## 🔮 CURSES

> Curses do not progress like diseases. They apply immediately and persist
> until removed by the specific cure listed. Fort/Will saves may suppress
> effects temporarily but do not remove the curse.

### Curse of the Stag Lord's Spite
**Source:** Dying in the Stag Lord's fort without completing his questline
**Effect:** −2 circ. all checks while in the Stolen Lands; bandits always Hostile
**Remove:** Kill the Stag Lord; OR complete his redemption path

---

### Nyrissa's Longing
**Source:** Extended contact with First World bleed zones (Ch4+)
**Effect:** Stupefied 1 (permanent, not reducible); −2 Will saves; compelled to seek Nyrissa
**Remove:** Briar artifact wielded; OR Nyrissa's death; OR Wish

---

### Tartuk's Hex
**Source:** Tartuk (Sootscale questline, if he curses the player)
**Effect:** Kobolds and gnomes Hostile on sight; −4 circ. Nature checks for 1 month
**Remove:** Kill Tartuk; OR Sootscale vouches for you (Diplomacy DC 25)

---

### Ovinrbaane's Dominion
**Source:** Wielding Ovinrbaane without passing its Will save after combat
**Effect:** Dominated until you Strike an ally; cycle repeats after each combat
**Remove:** Destroy Ovinrbaane (requires adamantine weapon and 100+ damage in one hit); Wish

---

### River King's Geas
**Source:** Breaking a sworn oath to a River Kingdom ruler (Ch4)
**Effect:** Sickened 2 permanently; −2 Charisma-based checks with all River Kingdoms
**Remove:** Fulfill the broken oath; OR Atone ritual (cleric L5 divine spell) + 500 gp offering

---

### Bloom Taint (Lingering)
**Source:** Surviving Voracious Plague Stage 3 without full cure
**Effect:** Plants within 10 ft grow aggressively toward you; −2 Nature checks; occasional involuntary plant growth
**Remove:** Old Beldame's ritual (Ch1+ if allied); Restoration (Greater, L6); Bald Hilltop cleansing

---

*KM_Conditions_Skills.md — Kingmaker PF2e Text Adventure | Conditions, Diseases & Curses v1.0*
*Source: PF2e GM Core, Player Core, Kingmaker AP (Paizo)*
# KINGMAKER — SKILL DCs & ACTIONS REFERENCE
## Skills Reference (continued from above)

> **DM:** Full skill action reference with DCs, outcomes, and modifiers.
> Use this file when any skill check is called. Do not set DCs from memory.

---

## 📊 STANDARD DC BY LEVEL (Task Difficulty)

| Level | Untrained | Trained | Expert | Master | Legendary |
|-------|-----------|---------|--------|--------|-----------|
| 0 | 10 | 10 | — | — | — |
| 1 | 15 | 15 | — | — | — |
| 2 | 16 | 16 | — | — | — |
| 3 | 18 | 18 | — | — | — |
| 4 | 19 | 19 | — | — | — |
| 5 | 20 | 20 | 20 | — | — |
| 6 | 22 | 22 | 22 | — | — |
| 7 | 23 | 23 | 23 | — | — |
| 8 | 24 | 24 | 24 | — | — |
| 9 | 26 | 26 | 26 | — | — |
| 10 | 27 | 27 | 27 | 27 | — |
| 11 | 28 | 28 | 28 | 28 | — |
| 12 | 30 | 30 | 30 | 30 | — |
| 13 | 31 | 31 | 31 | 31 | — |
| 14 | 32 | 32 | 32 | 32 | — |
| 15 | 34 | 34 | 34 | 34 | 34 |
| 16 | 35 | 35 | 35 | 35 | 35 |
| 17 | 36 | 36 | 36 | 36 | 36 |
| 18 | 38 | 38 | 38 | 38 | 38 |
| 19 | 39 | 39 | 39 | 39 | 39 |
| 20 | 40 | 40 | 40 | 40 | 40 |

**Simple DCs (no level):**
| Difficulty | DC |
|------------|-----|
| Very Easy | 10 |
| Easy | 13 |
| Medium | 15 |
| Hard | 20 |
| Very Hard | 25 |
| Incredible | 30 |
| Impossible (still possible) | 35 |
| Legendary | 40 |

**DC Adjustments:**
| Circumstance | Adjustment |
|-------------|-----------|
| Trained only (requires training) | +2 to DC if untrained |
| Legendary only | +10 if not legendary |
| Rushing (half time) | +5 DC |
| Taking time (double time) | −2 DC |
| Unfamiliar (never seen before) | +2 DC |
| Highly familiar | −2 DC |

---

## ⚔️ ACROBATICS

| Action | DC | Success | Failure | Notes |
|--------|-----|---------|---------|-------|
| Balance (difficult terrain) | 15 | Move through normally | Flat-footed, half speed | Each square of difficult terrain is a check |
| Tumble Through (past enemy) | Enemy Ref DC | Move through their space | Blocked, can't pass | Can't end in their space |
| Squeeze (tight space) | 15–20 | Move at half speed | Stuck (Escape DC 20) | DC scales with tightness |
| Maneuver in Flight | 15 | Maintain position | Fall 10 ft | Only if flying without fly speed |

---

## 💪 ATHLETICS

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Climb | 15 (easy), 20 (normal), 25 (hard) | Move at half speed | No progress |
| Disarm | Target's Reflex DC | Knock item away; Crit = take item | Target keeps item; Crit fail = you drop weapon |
| Grapple | Target's Fortitude DC | Target Grabbed | No effect; Crit fail = you Grabbed |
| High Jump (1A Stride) | 30 − distance jumped × 10 | Jump height listed | Normal jump height |
| Long Jump (1A Stride) | 5 × distance to jump | Jump listed distance | Half distance |
| Shove | Target's Fortitude DC | Push 5 ft; Crit = 10 ft + Prone | No effect |
| Swim | 10 (calm), 15 (rough), 20 (stormy) | Move at half speed | No progress; Crit fail = lose air |
| Trip | Target's Reflex DC | Target Prone; Crit = Prone + Grab | No effect; Crit fail = you Prone |

---

## 🎭 DECEPTION

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Create Diversion | Opponent's Perception DC | Hidden for 1 round | Observed |
| Feint | Target's Perception DC | Target Flat-footed vs your next attack | No effect |
| Impersonate (disguise) | Viewer's Perception DC | Believed | Seen through |
| Lie | Listener's Perception DC | Believed | May or may not be believed (DM) |

**Lie modifiers:** Plausible lie: −2 | Implausible: +4 | Impossible: +8 | Target suspicious: +4

---

## 🤝 DIPLOMACY

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Gather Information | 15–25 (by rarity of info) | Info found in 2d4 hours | Info not found; Crit fail = false info |
| Make an Impression | NPC's Will DC | Attitude improves 1 step | No change; Crit fail = worsens 1 step |
| Request | Based on request difficulty | NPC agrees | NPC refuses |

**Request DC by ask:**
| Request | DC |
|---------|----|
| Trivial favor | 5 |
| Minor inconvenience | 10 |
| Significant risk to NPC | 20 |
| Risk NPC's life | 30 |
| Suicidal/fundamentally opposed | 40 |

---

## 😨 INTIMIDATION

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Coerce | Target's Will DC | Complies; Unfriendly afterward | Refuses; Hostile if crit fail |
| Demoralize | Target's Will DC | Frightened 1; immune 10 min | No effect |

**Demoralize:** +1 Frightened per 5 below DC on crit success. −1 DC if target already at disadvantage.

---

## 🏥 MEDICINE

| Action | Time | DC | Success | Failure |
|--------|------|----|---------|---------|
| Administer First Aid (stop bleeding) | 1A | 15 | Stop persistent bleed | No effect |
| Administer First Aid (stabilize dying) | 1A | 15 | Target Stable | No effect |
| Identify Disease | — | 15 (common) to 30 (rare) | Know disease and cure | Wrong info |
| Identify Poison | — | 15 to 30 | Know poison and antidote | Wrong info |
| Treat Disease | 8 hours | 15 | Patient gets +2 save vs disease | No modifier |
| Treat Poison | 1A | 15 | Patient gets +2 save vs poison | No modifier |
| Treat Wounds (short rest, 10 min) | 10 min | 15 | Restore 2d8 HP | No healing; Crit fail = 1d8 damage |
| Treat Wounds (expert, DC 20) | 10 min | 20 | Restore 2d8+10 HP | — |
| Treat Wounds (master, DC 30) | 10 min | 30 | Restore 2d8+30 HP | — |
| Treat Wounds (legendary, DC 40) | 10 min | 40 | Restore 2d8+50 HP | — |

**Treat Wounds:** Each creature can only benefit once per hour. Healer's Tools required.

---

## 🌿 NATURE

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Command Animal | 15 (friendly), 20 (unfriendly) | Animal obeys simple command | Refuses |
| Identify | 15 (common) to 30 (rare) | Know creature type/traits | Wrong; Crit fail = dangerous wrong info |
| Recall Knowledge (nature topics) | 15–30 | Correct info | No info; Crit fail = false info |

---

## 🔍 PERCEPTION

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Seek (detect hidden) | Stealth DC of hidden creature | Creature Hidden or Observed | Unaware |
| Sense Motive | Deception DC | Sense if deceptive; Crit = know the lie | Don't know if lying |

**Standard Perception DCs:** Finding a secret door: 20–30 | Noticing an ambush: 15–25 | Detecting poison in food: 20 | Identifying a disguised person: Deception result

---

## 🎭 PERFORMANCE

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Perform | Varies by venue | Earn income at listed rate | Poor reception |
| Earn Income | 15 (L1 task) to 40 (L20 task) | Earn by task level | Half or no income |

**Performance income by task level:** L1: 2 sp/day | L3: 5 sp | L5: 2 gp | L8: 5 gp | L10: 10 gp | L14: 25 gp | L16: 40 gp | L20: 100 gp

---

## 🙏 RELIGION

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Recall Knowledge (divine topics) | 15–30 | Correct divine/undead/fiend info | No info |
| Identify Magic (divine) | 15–30 | Identify spell or magic item | No info; Crit fail = false |

---

## 🥷 STEALTH

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Avoid Notice (exploration) | Observers' Perception DC | Hidden while exploring | Observed |
| Hide | Observers' Perception DC | Hidden | Observed |
| Sneak (move while hidden) | Observers' Perception DC | Stay Hidden | Observed |

**Concealment modifier:** −2 DC in dim light; −4 DC in darkness; +2 if moving quickly

---

## 🔓 THIEVERY

| Action | DC | Success | Failure |
|--------|-----|---------|---------|
| Disable Device (trap) | 20–40 (by trap level) | Trap disabled | No progress; Crit fail = trap triggered |
| Palm an Object | Observers' Perception DC | Item taken unnoticed | Noticed |
| Pick a Lock | 20 (simple) to 40 (masterwork) | Lock open | No progress; Crit fail = lock jammed |
| Steal | Observers' Perception DC −5 | Item stolen | Noticed |

**Lock DCs:** Poor lock: 15 | Average: 20 | Good: 25 | Superior: 30 | Masterwork: 35 | Magical: 40

---

## 🔎 RECALL KNOWLEDGE (by skill)

> **DM:** When a player Recalls Knowledge, tell them what their character knows
> about a creature, item, person, or topic. Critical success = extra detail or
> a useful tactical fact. Failure = no info. Critical failure = wrong info presented as fact.

| Skill | Topics |
|-------|--------|
| Arcana | Arcane magic, constructs, dragons, magical beasts |
| Crafting | Alchemical items, structures, siege weapons, traps |
| Deception | Forgeries, cons, criminal organizations |
| Diplomacy | Negotiation tactics, NPC preferences, legal codes |
| Intimidation | Enemies' fears and weaknesses to Demoralize |
| Lore (specific) | Narrow topics: Warfare Lore, Heraldry Lore, etc. |
| Medicine | Diseases, poisons, anatomy |
| Nature | Animals, plants, weather, fey, elementals, primal magic |
| Occultism | Occult magic, spirits, undead, aberrations |
| Performance | Artistic traditions, famous performers, cultural events |
| Religion | Deities, divine magic, undead, celestials, fiends |
| Society | Humanoids, history, laws, governments, nobility |

**Kingmaker-specific Recall Knowledge DCs:**
| Topic | DC |
|-------|----|
| Stag Lord's identity | 18 (Ch1) |
| Hargulka's troll army composition | 20 (Ch2) |
| Vordakai's nature (lich) | 24 (Ch3) |
| Irovetti's Pitax connections | 22 (Ch4) |
| Nyrissa's true nature (First World) | 28 (Ch4+) |
| The Briar's origin | 30 (endgame) |

---

## 🔓 SKILL PROFICIENCY UNLOCKS

> Higher proficiency ranks unlock new actions beyond what Trained allows.
> The DM announces when a new action becomes available at level-up.

### Unlocks by Rank

| Skill | Trained | Expert | Master | Legendary |
|-------|---------|--------|--------|-----------|
| Athletics | Climb, Swim, High Jump, Long Jump, Shove, Trip, Grapple, Disarm | — | Shove/Trip at reach (10 ft without reach weapon) | Wall Jump (no surface needed, 1 round) |
| Acrobatics | Balance, Tumble Through, Squeeze | — | Rapid Maneuver (Tumble Through as free action 1/round) | — |
| Diplomacy | Make an Impression, Request, Gather Info | **Bon Mot** (1A: witty remark → target −2 Will saves for 1 min on success) | — | — |
| Intimidation | Demoralize, Coerce | — | Terrifying Resistance (demoralize 2 targets at once) | — |
| Medicine | First Aid, Treat Wounds, Treat Poison, Treat Disease | Battle Medicine (Treat Wounds as 1A in combat, 1/creature/day) | — | Chirurgeon (Treat Wounds in 1 action instead of 10 min) |
| Stealth | Hide, Sneak | — | Cover your Tracks as part of Sneak (no extra action) | — |
| Thievery | Pick a Lock, Disable Device, Palm Object, Steal | — | Steal without being adjacent (5 ft reach) | — |
| Nature | Recall Knowledge, Command an Animal | — | — | Speak with Animals (permanent, no spell needed) |
| Survival | Subsist, Track, Cover Tracks, Sense Direction | — | Impeccable Tracking (Track at full Speed, no penalty) | — |
| Arcana | Recall Knowledge, Identify Magic, Decipher Writing | — | — | Unified Theory (use Arcana for any magical Recall Knowledge) |
| Occultism | Same as Arcana | — | — | Unified Theory (same as Arcana) |
| Society | Recall Knowledge, Create Forgery, Subsist | — | Streetwise (Gather Info in 1 hour instead of 1 day) | — |
| Crafting | Craft, Repair, Identify Alchemy | — | Specialty Crafting (−2 to DCs for one craft type) | — |
| Performance | Perform, Earn Income | — | — | Virtuosic Performer (legendary performances always impress) |

### Bon Mot — Full Rules (Expert Diplomacy unlock)

> **Action:** 1A | **Range:** 30 ft | **Target:** One creature
> Make a Diplomacy check vs target's Will DC.
> **Success:** Target takes −2 status penalty to Perception and Will saves until end of next turn. This extends each time the target fails a Will save.
> **Critical Success:** Penalty is −3 and lasts until they critically succeed on a Will save.
> **Failure:** No effect.
> **Critical Failure:** You're flustered — you take the −2 penalty instead.
>
> Build 13 (Silver Tongue Scoundrel) and Build 6 (Thaumaturge) unlock this at Expert.

### Mounted Combat (Expert Athletics unlock)

> **Mounting:** 1A Interact action. Requires a trained mount (animal companion or purchased horse).
> **Riding:** The mount moves on your turn — you use your action to command it (1A) or it uses its own speed if it has the Minion trait.
> **Lance:** +2 damage on the first Strike each turn if you moved at least 10 ft on a mount this turn (Jousting trait).
> **Falling:** If mount is reduced to 0 HP or spooked (Fort DC 15), Athletics DC 15 to land safely (no damage). Fail: 1d6 bludgeoning per 10 ft fallen (typically 1d6).
> **Enemy mounts:** Targeting the mount instead of the rider — the rider is Off-Guard if the mount takes damage from a called shot or is reduced below half HP.
*Source: PF2e Player Core, GM Core (Paizo)*
