# KINGMAKER — BUILD AUDIT: BARBARIAN
## KM_BuildAudit_Barbarian.md | Source files: KM_Builds_B.md (1–6), KM_Builds_B2.md (7–10)
## Audit date: 2026-05-14 | Canon reference: PF2e Remaster Player Core / Player Core 2

> **Method:** Each build is audited at L1 (statblock math, feat-slot accounting) and across the L1–20 leveling map (feat-level legality, feat-name fabrication, class-feature placement). Deltas shown only — values not listed = correct or unverified.
>
> **PF2e Remaster Barbarian L1 proficiencies (canon reference):**
> Perception: Expert | Fort: Expert | Ref: Trained | Will: Trained | Class DC: Trained
> *(Note: some Player Core 2 sources boost Will to Expert at L1 — entries flagged with [†].)*
>
> **PF2e save formula:** `L + prof_bonus + ability_mod` where Trained = +2, Expert = +4, Master = +6, Legendary = +8.
> **PF2e Init = Perception** in standard play.
>
> **Barbarian class progression milestones (Remaster):**
> L3 Furious Footfalls (+5 Speed) | L5 Brutal Critical | L7 Juggernaut (Expert Fort, success→crit) + Weapon Spec
> L9 Lightning Reflexes (Expert Ref) | L11 Mighty Rage | L13 Greater Juggernaut (Master Fort)
> L15 Indomitable Will (Master Will) + Greater Weapon Spec | L17 Quick Rage | L19 Devastating Strike

---

## SYSTEMIC PATTERNS (apply to all 10 builds)

1. **Saves and Perception are L-short.** Files compute as `prof + mod` without adding character level. At L1 every Expert save/perception reads 1 lower than canon; every Trained reads correctly only by coincidence (some are also short).
2. **Init mis-stated.** Files use a DEX-like number; canon is Init = Perception bonus.
3. **Background skill feat omitted or wrong.** Warrior bg canonically grants Intimidating Glare; multiple builds list Powerful Leap as bg feat (not what Warrior grants).
4. **L1 standard class feat slot empty.** When Natural Ambition is taken, Sudden Charge (or equivalent) is labeled as the Natural Ambition grant — but the standard L1 class feat slot is left unfilled in the leveling map.
5. **Juggernaut placed at L3 (illegal).** Canon: L7. Affects all 10 builds.
6. **Master Fort at L9 (illegal).** Canon: Greater Juggernaut at L13.
7. **Greater Weapon Specialization at L10 (illegal).** Canon: L15.
8. **Indomitable Will at L15** — placement OK (canon L15) but it's a class feature, not a [PICK] feat — should not consume the class-feat slot.
9. **"Brutal Rage" at L5** — canonical name is **Brutal Critical** (extra die on crit). "Brutal Rage" is not a published class feature name.
10. **"Rage of Ruin" at L20** — not a canonical PF2e feat. Suspected fabrication or homebrew rename.

---

## BUILD 1 — TACTICAL REACH KING *(Human Versatile / Giant Instinct / Warrior)* ✅ LIVE
**File:** KM_Builds_B.md:31-104
**Status:** PASS — all audit findings resolved. Canon-compliant against PF2e Remaster (Player Core / Player Core 2).
**Last verified:** 2026-05-17

### Resolution summary
v93.12 mass sweep (2026-05-15) fixed: HP 24→23, Brutal Critical naming, Juggernaut placement L3→L7, Greater Juggernaut L9→L13, Greater Weapon Spec L10→L15, Gigantic Stature L13→L14, background skill feat to Intimidating Glare, removed Reactive Strike fabricated path, removed Rage of Ruin fabrication, removed Titan Mauler/Devastator/Improved Knockdown placement errors.

v93.13 targeted edits (2026-05-17) fixed:
| Issue | Resolution |
|-------|-----------|
| AC 13 (Unarmored) contradicted Full Plate L1 premise | → AC 19 (10 + 6 Full Plate + 3 Trained Heavy, DEX cap 0) |
| Intimidation +1 (labelled Trained, used Untrained math) | → +3 (Trained + CHA 0 + L1) |
| Warfare Lore +1 (same bug) | → +3 (Trained + INT 0 + L1) |
| L3 Furious Footfalls note had outdated "light/no armor" conditional | → "flat +5 status to Speed, unconditional; +10 while raging" |
| L12 Combat Grab (Fighter-only class feat placed in skill slot) | → Battle Medicine (legal skill feat, fits Medicine +5 third-action pattern) |
| L19 "Armor of Will" (Champion-only feature) | Deleted; L19 is Devastating Strike only |
| L20 "Apex Predator" (fabricated name) | Deleted; L20 is Ability Boost ×4 + Rampage |

### Legality verified
- L1 statline: HP 23, AC 19, Init +7, Perception +7, Fort +8, Ref +3, Will +7, all skill bonuses match prof + ability + L1
- L1 feat slots: Heritage general feat (Armor Prof Heavy — legal because Barb starts Trained Medium), Ancestry (Natural Ambition → bonus class feat Sudden Charge), Class (Raging Intimidation), Skill (Intimidating Glare via Warrior bg)
- L1-20 leveling map: every class feature at canon level, every class feat legal at its slot, every skill feat legal, Sentinel archetype chain (L2 Ded → L7 Expert Heavy → L15 Master Heavy) intact
- L18 Unstoppable Juggernaut confirmed canon (Barb L18 class feat — resistance + Con mod + 1 HP stay-alive reaction)

### Live status
This is the live build for the current playthrough character (eRmaC, per save state). Active in `KM_Builds_B.md`. Available on `KM_BuildScreen.md` Barbarian menu as option [1]. Ready for play.

---

## BUILD 2 — FURY FLURRY *(Human Natural Ambition / Fury Instinct / Warrior)*
**File:** KM_Builds_B.md:108-167

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 24 | 23 | **+1** unexplained |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** (Trained: 1+2+2 = +5) |
| Will | +5 | +5 (Trained) / +7 (Expert) | ✓ or **−2** |
| Perception | +4 | +7 | **−3** |
| Init | +2 | +7 | **−5** |
| Athletics | +6 | +7 | **−1** |
| Acrobatics +4 | — | +5 | **−1** |

### L1 feat-slot issues
- **Double Slice picked as L1 Natural Ambition class feat — ILLEGAL.** Double Slice is a L1 **Fighter** class feat. Natural Ambition grants a 1st-level **class feat from your own class**. Barbarians do not have Double Slice in their feat list. **Critical fabrication.**
- Background skill feat: Warrior → Intimidating Glare. Not listed; only "Double Slice" appears at L1.
- L1 standard class feat slot: empty (same pattern).

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal at L3.** |
| 3 | Raging Athlete | L7 class feat. **Illegal at L3.** |
| 4 | Two-Weapon Flurry | **Fighter** L8 feat. Barbarian cannot pick directly. Needs Fighter Dedication chain. **Illegal/fabricated.** |
| 5 | Brutal Rage | Likely Brutal Critical rename. |
| 5 | Power Attack | L1 class feat — legal at L5 but wasted slot. |
| 6 | Improved Knockdown | L8 class feat. **Illegal at L6.** |
| 7 | Knockback Strike | Not canonical PF2e Barbarian feat. **Suspected fabrication.** |
| 8 | Brutal Bully | L6 class feat. Legal at L8 ✓ |
| 9 | Devastator | See Build 1 — likely fabrication. |
| 9 | Master Fort | Should be L13 (Greater Juggernaut). |
| 10 | Greater Weapon Specialization | L15. **Illegal at L10.** |
| 13 | Furious Sprint | L8 class feat. Legal at L13 ✓ |

**Count:** 7 stat deltas, 3 L1 feat issues (1 critical fabrication), 8 leveling issues.

---

## BUILD 3 — ANIMAL INSTINCT MUTAGEN *(Orc Hold-Scarred / Animal Instinct / Herbalist)*
**File:** KM_Builds_B.md:171-230

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 28 | 28 | ✓ (10 Orc + 12 Barb + 4 CON = 26; **off by +2** unless Diehard/Hold-Scarred adds — Hold-Scarred Heritage doesn't add HP at L1, just Diehard. **Δ +2 unexplained**) |
| Fort | +8 | +9 | **−1** (1 + 4 + 4 = 9) |
| Ref | +7 | +6 | **+1** (Trained: 1+2+3 = +6) |
| Will | +5 | +5 (T) / +7 (E) | ✓ or **−2** |
| Perception | +4 | +7 | **−3** |
| Init | +3 | +7 | **−4** |
| Athletics | +6 | +7 | **−1** |
| Crafting +4, Survival +3, Nature +3 | — | +5/+4/+4 | **−1 each** |

### L1 feat-slot issues
- **"Hold-Scarred + Animal Skin"** at L1 — Hold-Scarred is a **heritage**, not a feat slot. Animal Skin is the L1 class feat. The pairing in "Key Feats: L1 Hold-Scarred + Animal Skin" is mislabeled but mechanically OK: heritage + L1 class feat.
- However the leveling map L1 PICK column lists "Hold-Scarred + Animal Skin" — Hold-Scarred is heritage, not a [PICK]. Confused slot labeling.
- L1 ancestry feat: not listed. Orc gets an L1 ancestry feat — missing from the build.
- Herbalist bg skill feat: should grant Natural Medicine. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Raging Athlete | L7. **Illegal at L3.** |
| 4 | Predator's Pounce | L8 class feat. **Illegal at L4.** |
| 5 | Greater Animalistic Attacks | **Not canonical.** Animal Instinct upgrades happen via auto-scale (Specialization Ability at L7). Suspected fabrication. |
| 7 | Vicious Evisceration | L8 class feat. Legal at L7? Edition-check. |
| 9 | Devastator | Fabrication (see Build 1). |
| 10 | Greater Weapon Spec | L15. **Illegal at L10.** |
| 11 | Apex Predator | Not canonical PF2e feat. **Suspected fabrication.** |
| 13 | Furious Sprint | L8 class feat. Legal at L13 ✓ |

**Count:** 7 stat deltas, 3 L1 feat issues, 7 leveling issues (2 suspected fabrications).

---

## BUILD 4 — SPIRIT INSTINCT FORCE DAMAGE *(Human Natural Ambition / Spirit Instinct / Acolyte)*
**File:** KM_Builds_B.md:234-293

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 24 | 23 | **+1** unexplained |
| Fort | +7 | +8 | **−1** |
| Ref | +5 | +4 | **+1** (1+2+1 = 4) |
| Will | +6 | +6 (T) / +8 (E if Remaster) | ✓ or **−2** |
| Perception | +5 | +7 | **−2** |
| Init | +1 | +7 | **−6** |
| Skills | various −1 each | | |

### L1 feat-slot issues
- **"Spirit's Wrath" at L1** — canonical name is **Spirit Rage** (Spirit Instinct's base feature) or **Furious Howl/Howl of Heavens**. "Spirit's Wrath" is not a PF2e feat. **Suspected fabrication.**
- Acolyte bg skill feat: canon = Student of the Canon. Not listed.
- L1 standard class feat slot empty.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Swipe | L4 Barbarian feat. **Illegal at L3.** |
| 4 | Spirit's Vengeance | Not canonical. **Suspected fabrication.** |
| 5 | Basic Oracle Spells | Archetype feat from Oracle Dedication. Legal at L5 if Oracle Ded taken L2 ✓ |
| 6 | Improved Spirit's Vengeance | Built on a fabricated base — fabrication. |
| 11 | Spirit Incarnation | Not canonical. **Suspected fabrication.** |
| Others | Same pattern as builds 1-3 (Juggernaut, Master Fort, GWS placements) | |

**Count:** 6 stat deltas, 2 L1 issues (1 fabrication), 6 leveling issues (3 fabrications).

---

## BUILD 5 — DRAGON INSTINCT ELEMENTAL BLASTER *(Half-Orc Orc Ferocity / Dragon Instinct / Hunter)*
**File:** KM_Builds_B.md:297-356

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 26 | 25 | **+1** (10 Half-Orc + 12 + 3 = 25) |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +5 | +5/+7 | ✓ or **−2** |
| Perception | +4 | +7 | **−3** |
| Init | +2 | +7 | **−5** |
| Skills | −1 each | | |

### L1 feat-slot issues
- **Dragon Roar at L1** — canonical name is **Intimidating Strike** or **Demoralize** + Dragon Instinct flavor. "Dragon Roar" might refer to the **Dragon Instinct anathema/feature**. Not a feat per se. Suspected misclassification.
- Hunter bg skill feat: canon = Survey Wildlife. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Swipe | L4 feat. **Illegal at L3.** |
| 4 | Draconic Arrogance | Not canonical PF2e feat (sounds like APG/Legacy). **Verify.** |
| 6 | Basic Bloodline Spell "Fireball equiv" | Generic — depends on Sorcerer Ded prereqs. Fireball is a 3rd-rank spell; "Basic Bloodline Spell" archetype feat grants 1st-rank bloodline spells only. **Wrong rank claim.** |
| 8 | Improved Dragon Breath | Not canonical Barbarian feat. **Suspected fabrication.** |
| 11 | Dragon Transformation | Sorcerer Draconic Bloodline focus spell at L18 (Form of the Dragon analog). As Barb-archetype access requires very high archetype investment. **Illegal at L11.** |
| Others | Standard Juggernaut/MasterFort/GWS errors | |

**Count:** 6 stat deltas, 2 L1 issues, 6 leveling issues (3 fabrications/wrong).

---

## BUILD 6 — SUPERSTITION ANTI-MAGIC *(Dwarf Stonegate / Superstition Instinct / Warrior)*
**File:** KM_Builds_B.md:360-419

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 26 | 26 | ✓ (10 Dwarf + 12 + 4 = 26) |
| Fort | +8 | +9 | **−1** |
| Ref | +5 | +4 | **+1** |
| Will | +6 | +6/+8 | ✓ or **−2** |
| Perception | +5 | +7 | **−2** |
| Init | +1 | +7 | **−6** |
| Athletics | +8 | +7 | **+1** (1+2+4 = +7) |

### L1 feat-slot issues
- **"Stone Walk" at L1** — Dwarf has **Stonemason's Eye**, **Stonegate** Heritage gives sense, but "Stone Walk" as ancestry feat name is non-canonical. Likely refers to **Stonewalker** L1 ancestry feat. Name mismatch.
- "Superstition Instinct" as L1 [PICK] feat — Superstition Instinct is the chosen Instinct (class feature), not a feat. **Slot mislabel.**
- Warrior bg skill feat (Intimidating Glare): not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 4 | Warded Mind | L12 class feat. **Illegal at L4.** Major error — this is sold as the "L4 identity feature" in build summary. |
| 5 | Terrifying Howl | L8 class feat. **Illegal at L5.** |
| 6 | Spell Sunder | Not a canonical PF2e Barbarian feat. Closest is **Sunder Spell** (Cleric) or **Counter Magic**. **Suspected fabrication.** |
| 11 | "Spell Sunder: Greater" | Built on fabricated base. |
| Others | Standard Juggernaut/MasterFort/GWS errors | |

**Count:** 6 stat deltas, 3 L1 issues, 5 leveling issues (2 fabrications, 1 major level mismatch).

---

## BUILD 7 — TITAN MAULER *(Human Versatile / Giant Instinct / Warrior)*
**File:** KM_Builds_B2.md:19-78

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 22 | 22 | ✓ (8 Human + 12 + 2 = 22) |
| Fort | +6 | +7 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +4 | +4/+6 | ✓ or **−2** |
| Perception | +3 | +5 | **−2** |
| Init | +2 | +5 | **−3** |
| Athletics | +6 | +7 | **−1** |

### L1 feat-slot issues
- **"Large Bastard Sword (2d12+4)" at L1** — Bastard Sword 1d8, Large weapon increases damage die size to 1d10 (one step up). **2d12 claim wrong.** Giant Instinct allows Large weapons but die scaling is +1 step, not double dice.
- "Raging Intimidation (free Demoralize on every hit while raging)" L1 — **Free Demoralize on every hit is NOT the canonical effect.** Raging Intimidation (L1 Barbarian feat) lets you Demoralize without spending action AND lets you use Intimidating Glare/Scare to Death while raging. It does NOT give free Demoralize on hit. **Mechanic fabricated.**
- Versatile Human "free general feat at L1" used for Raging Intimidation — Raging Intimidation is a CLASS feat, not a general feat. Versatile Human gives a general feat slot. **Slot type mismatch.** Would need to be the standard L1 class feat slot.
- Warrior bg skill feat (Intimidating Glare): listed at L2 as a [PICK]. But Intimidating Glare should be granted **automatically by Warrior background** at L1, not picked at L2.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 2 | Intimidating Glare | Should be auto-granted by Warrior bg at L1 (free) — not a L2 pick. |
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Swipe | L4. **Illegal at L3.** |
| 5 | Terrifying Howl | L8. **Illegal at L5.** |
| 6 | Giant's Stature | L6 ✓ — first correct placement |
| 8 | Come and Get Me | L12 class feat. **Illegal at L8.** |
| 11 | Collateral Thrash | L10 ✓ (legal at L11) |
| 12 | Predator's Pounce | L8 ✓ (legal at L12) but wasted slot |
| 16 | Scare to Death | L7 skill feat (Master Intimidation prereq, available ~L7). Skill feat slot consumed. Class feat slot at L16 = wasted? |
| Others | Standard errors | |

**Count:** 7 stat deltas, 4 L1 issues (1 mechanic fabrication, 1 weapon-math error), 7 leveling issues.

---

## BUILD 8 — ELEMENTAL RAGE *(Half-Orc Orc Ferocity / Fury Instinct / Farmhand)*
**File:** KM_Builds_B2.md:82-141

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 26 | 25 | **+1** |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +5 | +5/+7 | ✓ or **−2** |
| Perception | +4 | +6 | **−2** |
| Init | +2 | +6 | **−4** |

### L1 feat-slot issues
- "Orc Ferocity" labeled as L1 [PICK] — Orc Ferocity is a **Half-Orc ancestry feat (L1)** ✓ but slot label conflates ancestry feat with class feat in some entries.
- "Raging Intimidation" — mechanic fabrication carried over from Build 7 if used in same flavor.
- Farmhand bg skill feat: canon = Assurance (skill of choice) or Survey Wildlife. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 2 | Kineticist Dedication (elemental blast) | **Kineticist Dedication has Kineticist-specific prereqs (an element + impulse junction). Available L2 if rules support multiclass. Verify Player Core 2 compatibility.** |
| 3 | Juggernaut + Swipe | Both illegal placements. |
| 4 | Basic Kinesis | Archetype feat L4 (Basic Kineticist), legal ✓ |
| 6 | Elemental Blast upgrade (2d6) | Damage die progression for Kineticist scales with class level. Multiclass archetype Kineticist scales slower. **Verify die size.** |
| Others | Standard errors | |

**Count:** 6 stat deltas, 1-2 L1 issues, 5 leveling issues + archetype-scaling verify.

---

## BUILD 9 — RAGING FLURRY STRIKES *(Human Natural Ambition / Fury Instinct / Street Urchin)*
**File:** KM_Builds_B2.md:145-204

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 24 | 23 | **+1** |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +6 | +5/+7 | ✓ |
| Perception | +5 | +7 | **−2** |
| Init | +2 | +7 | **−5** |

### L1 feat-slot issues
- "Toughness" at L1 via Natural Ambition — Natural Ambition grants a **class feat**, not a general feat. Toughness is a **general feat**. **Slot type mismatch — illegal.**
- Street Urchin bg skill feat: canon = Pickpocket. Not listed.
- L1 standard class feat slot: empty.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 2 | Monk Dedication (Flurry of Blows, Powerful Fist 1d6) | Monk Dedication archetype feat ✓ L2. **Flurry of Blows is a Monk class feature, NOT granted by Monk Dedication.** Monk Dedication gives Trained in martial weapons + 8 HP + access to Monk archetype feats. Flurry of Blows specifically requires Basic Monk Spellcasting OR the **Monastic Weaponry** chain. **"Flurry of Blows from Monk Ded L2" is fabricated mechanic.** |
| 4 | Basic Unarmed Strike "Monk agile chain upgrades" | Not a canonical archetype feat name. Closest: Basic Kata. **Suspected fabrication.** |
| 6 | Savage Critical | Not canonical PF2e Barbarian feat. **Suspected fabrication.** |
| 3,9,10,15 | Standard errors | |

**Count:** 6 stat deltas, 2 L1 issues (1 illegal slot), 5 leveling issues (2 mechanism fabrications).

---

## BUILD 10 — PURE RAGE SUPPORT *(Human Natural Ambition / Fury Instinct / Street Performer)*
**File:** KM_Builds_B2.md:208-267

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 22 | 22 | ✓ |
| AC | 17 | 18 | **−1** (Hide armor at L1 Trained: 10+2+1+2+3 = 18; file 17 is short) |
| Fort | +6 | +7 | **−1** |
| Ref | +5 | +4 | **+1** |
| Will | +5 | +4/+6 | varies |
| Perception | +4 | +5 | **−1** |
| Init | +1 | +5 | **−4** |
| Performance +5 | — | +6 | **−1** (1+2+3 CHA = +6) |

### L1 feat-slot issues
- "Raging Intimidation" — mechanic fabrication if represented as free-Demoralize-on-hit (see Build 7).
- Street Performer bg skill feat: canon = Fascinating Performance. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut + Swipe | Both illegal at L3. |
| 5 | Terrifying Howl | L8. **Illegal at L5.** |
| 8 | Come and Get Me | L12. **Illegal at L8.** |
| 12 | Dragon Transformation | Sorcerer focus spell. Not legally accessible to this build (no Sorcerer Ded). **Illegal.** |
| Others | Standard errors | |

**Count:** 7 stat deltas, 1 L1 issue, 6 leveling issues.

---

## CONSOLIDATED FINDINGS

| Build | Stat deltas | L1 issues | Leveling issues | Critical fabrications |
|---|---|---|---|---|
| 1 Tactical Reach King | 6 | 3 | 10 | Titan Mauler-as-feat, Devastator, Rage of Ruin, Reactive Strike path |
| 2 Fury Flurry | 7 | 3 | 8 | **Double Slice illegal for Barb**, Knockback Strike, Devastator |
| 3 Animal Mutagen | 7 | 3 | 7 | Greater Animalistic Attacks, Apex Predator, Devastator |
| 4 Spirit Force | 6 | 2 | 6 | Spirit's Wrath, Spirit's Vengeance, Spirit Incarnation |
| 5 Dragon Blaster | 6 | 2 | 6 | Improved Dragon Breath, Dragon Transformation @ L11, Draconic Arrogance |
| 6 Superstition | 6 | 3 | 5 | Spell Sunder, Warded Mind @ L4 (huge error) |
| 7 Titan Mauler | 7 | 4 | 7 | **Raging Intimidation mechanic fabricated**, 2d12 weapon math |
| 8 Elemental Rage | 6 | 2 | 5 | Kineticist scaling verify |
| 9 Raging Flurry | 6 | 2 | 5 | **Flurry-from-Monk-Ded fabricated**, Savage Critical |
| 10 Pure Rage Support | 7 | 1 | 6 | Dragon Transformation @ L12 illegal |

**Totals across 10 Barbarian builds:**
- 64 L1 statblock math deltas
- 25 L1 feat-slot issues
- 65 L1-20 leveling-map errors
- ~25 distinct fabricated feat names or fabricated mechanics

**Top systemic fixes (one edit pattern, applies to all 10 builds):**
1. Add `L + ` to every save/perception/skill bonus calculation
2. Set `Init = Perception` (or note "see Perception")
3. Move **Juggernaut** from L3 → L7 (auto class feature)
4. Move **Master Fort** from L9 → L13 (Greater Juggernaut)
5. Move **Greater Weapon Specialization** from L10 → L15
6. Rename **Brutal Rage** → **Brutal Critical**
7. Replace or remove **Rage of Ruin** (L20) with a canonical capstone
8. Add **Lightning Reflexes** L9, **Mighty Rage** L11, **Quick Rage** L17, **Devastating Strike** L19 as auto class features
9. Auto-grant **background skill feat** at L1 per background canon (Intimidating Glare for Warrior, etc.) instead of consuming the L1 [PICK]
10. Document each Instinct's L1 anathema/special feature so it's not confused with a feat

---

*KM_BuildAudit_Barbarian.md — Audit v1.0 | 2026-05-14*
