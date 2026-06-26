# KINGMAKER — TIPS FOOTER (A)
## KM_Tips.md | Companion: KM_Tips_B.md | Referenced by: KM_DMRules.md

> **⛔ DM: At end of every response, append 1-3 tips whose triggers fired
> this turn. If no triggers fired, show 1 fallback tip from current mode.
> Copy the SHORT line verbatim. Never generate tips. Fabrication = `.fail 9`.
> Missing footer = `.fail 40`.**

> **Player commands:**
> - `.tip` — show detail for current turn's tip
> - `.tips` — list all tip codes by category
> - `.tip [code]` — show full detail for a specific tip

> **This file (A)** covers Combat Actions, Heroics, Conditions, Positioning.
> **See KM_Tips_B.md** for Pack Items, Downtime, Exploration, Social, Resting,
> Kingdom, Meta — plus the master `.tips` list and full trigger table.

---

## FOOTER FORMAT (print at end of every response)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 TIP: [SHORT line]. Type `.tip [code]` for details.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Pick UP TO 3 tips. One is usually enough. Prefer trigger-matched over fallback.

═══════════════════════════════════════════════════════════
## [COMBAT_ACTIONS] — PF2e actions the choice menu may miss
═══════════════════════════════════════════════════════════

## .tip aid
SHORT: Spend an action to help an ally's next check (+1, or +2/+3/+4 on crit).
DETAIL:
  • 1 action + ready; ally rolls on their turn
  • Roll DC 15 (or GM-set) matching ally's action
  • Success: +1 | Crit: +2 expert / +3 master / +4 legendary
  • Works on attacks, skills, saves — anything with a check
  • Declare BEFORE the ally rolls

## .tip feint
SHORT: Deception vs Perception DC to make target off-guard to your next attack.
DETAIL:
  • 1 action, trained Deception required, target within 30 ft sees you
  • Success: target off-guard (−2 AC) to YOUR next melee attack this turn
  • Crit: off-guard to all melee attackers until your next turn
  • Crit fail: YOU off-guard to target until your next turn

## .tip recall
SHORT: Recall Knowledge to learn an enemy's weaknesses, resistances, or lore.
DETAIL:
  • 1 action, skill based on creature type:
    - Arcana: constructs, dragons, magical beasts
    - Nature: animals, beasts, fey, plants
    - Religion: undead, celestials, fiends, divine
    - Occultism: aberrations, spirits, mental
    - Society: humanoids, civilized cultures
  • Success: 1 useful fact | Crit: 2 facts + specific numbers
  • DC scales with creature level + rarity
  • Can try again but GM raises DC each time

## .tip seek
SHORT: Seek action reveals hidden enemies, traps, concealed objects.
DETAIL:
  • 1 action, specify area or creature
  • Perception vs creature Stealth DC or trap DC
  • Success: hidden → observed, or undetected → hidden
  • In exploration, Searching uses Seek automatically

## .tip trip
SHORT: Athletics vs Reflex DC knocks enemy prone.
DETAIL:
  • 1 action, target within reach, 2+ legs needed
  • Success: prone (−2 attack, off-guard, 1 action to stand)
  • Crit: prone + 1d6 bludgeoning
  • Set up allies' attacks — prone = off-guard to melee

## .tip shove
SHORT: Athletics vs Fortitude DC pushes enemy 5 ft (10 on crit).
DETAIL:
  • 1 action, hand free or shield raised
  • Success: target 5 ft away | Crit: 10 ft + prone
  • Shove into hazards, cliffs, out of flanks
  • Can shove off ledges (falling damage applies)

## .tip grapple
SHORT: Athletics vs Fortitude DC restrains an enemy.
DETAIL:
  • Success: target grabbed (off-guard, can't move)
  • Crit: restrained (needs 1 action to Escape)
  • Grappled target can only Escape or counter-grapple
  • Maintains until you release, move, or attack other target

## .tip disarm
SHORT: Athletics vs class DC to weaken grip (−2 attacks) or take weapon on crit.
DETAIL:
  • Success: −2 to target's attacks w/ that weapon until next turn
  • Crit: weapon falls to ground (or in your free hand)
  • Works on held weapons AND shields

## .tip reposition
SHORT: Athletics vs Fortitude to force enemy to move 5 ft ANY direction you choose.
DETAIL:
  • Unlike Shove: YOU pick direction (behind you, into ally reach, etc.)
  • Success: 5 ft any direction | Crit: 10 ft
  • Target can't be moved through paths it couldn't normally enter

## .tip demoralize
SHORT: Intimidation vs Will DC — target frightened 1 (or 2 on crit).
DETAIL:
  • 1 action, no language needed with visual threat
  • Frightened = penalty to all checks equal to value
  • Reduces by 1 each turn — stack before big fights
  • Crit fail: target immune to YOUR Demoralize for 24 hrs

## .tip bonmot
SHORT: Diplomacy feat — witty insult: −2 Perception & Will for 1 min.
DETAIL:
  • Requires Bon Mot feat (Diplomacy)
  • 1 action, within 30 ft, shared language
  • Success: target −2 Perception & Will for 1 min
  • Great before enemy Will-save spell or Seek

## .tip treatwnd
SHORT: Medicine heals HP out of combat (10 min per attempt).
DETAIL:
  • 10 min activity, DC 15 trained (or higher for bonus)
  • Success: 2d8 (+10/+20/+30 for expert/master/legendary)
  • Crit: 4d8 | Fail: 1d8 damage | Crit fail: 1d8 damage
  • 1 hour cooldown (Continual Recovery feat removes)

## .tip stride
SHORT: Stride moves up to your full Speed; you can Stride twice in a turn.
DETAIL:
  • 1 action per Stride
  • Double-Stride: close gaps fast
  • Triggers reactions like Attack of Opportunity — Step to avoid
  • Difficult terrain halves Speed; greater difficult quarters it

## .tip step
SHORT: Step 5 ft without triggering reactions — safe retreat or close.
DETAIL:
  • 1 action, 5 ft only
  • Does NOT trigger Attack of Opportunity
  • Can't Step in difficult terrain
  • Use to disengage, slip past, or adjust position safely

## .tip takecover
SHORT: Take Cover action — standard cover becomes greater cover (+4 AC/Reflex).
DETAIL:
  • 1 action while behind something
  • Standard cover (+2) → greater cover (+4 AC + Reflex + Stealth)
  • Must actively crouch/duck — lost if you attack
  • Works with allies (ally = lesser cover) or terrain

## .tip raiseshield
SHORT: Raise a Shield grants +2 AC and lets you Shield Block reaction.
DETAIL:
  • 1 action, held shield
  • +2 Circumstance AC until start of your next turn
  • Enables Shield Block reaction: reduce damage by shield Hardness
  • Sturdy shields can Block bigger hits without breaking

## .tip ready
SHORT: Ready an action with a trigger — fires when condition met before your next turn.
DETAIL:
  • 2 actions to Ready; only 1 action can be Readied
  • Trigger: "when X happens, I do Y"
  • Used action doesn't refund if trigger doesn't fire
  • Classic: "Ready to shoot if they charge" / "Ready to cast if wizard does"

## .tip delay
SHORT: Delay your turn to act later in initiative order (free reaction).
DETAIL:
  • Happens at start of your turn, before anything else
  • You take no turn now; can re-enter between any two turns later
  • New initiative position becomes permanent
  • Can't delay into a dead round (can lose your turn)

## .tip escape
SHORT: Break free from grappled/restrained — Athletics, Acrobatics, or unarmed attack.
DETAIL:
  • 1 action, pick your best: Athletics, Acrobatics, or attack bonus
  • vs grabber's Athletics DC or spell DC
  • Success: escape condition | Crit: escape + target off-guard to you
  • Crit fail: no action refund, still stuck

## .tip hide
SHORT: Hide with Stealth to become hidden from enemies that can't see you.
DETAIL:
  • Needs cover or concealment
  • Stealth vs enemy Perception DC
  • Success: hidden (enemies know square but attacks have flat DC 11)
  • Broken if you attack, speak loudly, or lose cover
  • Prereq to Sneak (move while hidden)

## .tip sneak
SHORT: Sneak to move while staying hidden — Stealth vs each observer's Perception.
DETAIL:
  • 1 action, 5 ft per Sneak
  • Must start hidden
  • Stealth vs each enemy's Perception DC; fail vs any = you're observed
  • Great for scouting, assassinations, escapes

## .tip diversion
SHORT: Create a Diversion (Deception) to become hidden mid-combat.
DETAIL:
  • 1 action, Deception vs each enemy's Perception DC
  • Trick: point & shout, feint stumble, throw rock
  • Success vs enemy: you're hidden from that enemy until end of next turn
  • Fail: enemy immune to same trick for 1 hour

## .tip tumblethrough
SHORT: Acrobatics vs Reflex to move through enemy's square.
DETAIL:
  • 1 action (counts as part of Stride)
  • Success: pass through enemy space
  • Fail: stop before entering
  • Great flanking setup when allies can't reach

## .tip leap
SHORT: Horizontal 10 ft jump without Athletics check (15 ft with high Str or feat).
DETAIL:
  • 1 action, free with standing still
  • Horizontal: 10 ft standard | 15 ft with Powerful Leap / high Athletics
  • Vertical: 3 ft (5 with Quick Jump)
  • Longer jumps use High Jump / Long Jump activities

## .tip highjump
SHORT: Athletics DC 30 for big vertical leap — 8 ft on success, 5 ft fail.
DETAIL:
  • 2 actions; Stride first as bonus
  • DC 30 Athletics: 8 ft vertical, crit: 15 ft
  • Fail: 5 ft (still ok)
  • Crit fail: fall prone after 5 ft

## .tip longjump
SHORT: Athletics check for long horizontal jump — distance = your Speed on crit success.
DETAIL:
  • 2 actions, must Stride 10+ ft first
  • DC = jump distance in feet
  • Success: jump the distance
  • Crit: jump up to your Speed
  • Fail: land in water/prone if gap not cleared

## .tip grabedge
SHORT: Reflex save when falling next to ledge — catch the edge, avoid fall damage.
DETAIL:
  • Triggered when you'd fall past a ledge/surface to grab
  • Reflex vs GM DC (usually 15-20)
  • Success: grab, dangling, use actions to Climb up
  • Fail: fall normally

## .tip sensemotive
SHORT: Perception check to read an NPC's emotional state, truthfulness, or intent.
DETAIL:
  • 1 action; opposed Perception vs Deception DC
  • Success: sense lie, fear, hidden agenda
  • Crit: specific detail (what they're hiding, who they fear)
  • Fail: no info
  • Crit fail: false reading (they fool you)

## .tip maneuverflight
SHORT: Acrobatics for tricky flight — dodge, dive, evasive maneuver.
DETAIL:
  • Required for flying creatures in tight spaces/bad weather
  • DC based on conditions (GM set, usually 15-25)
  • Success: maintain altitude, execute maneuver
  • Fail: lose altitude or go prone in air
  • Feat required if not natural flier

## .tip command
SHORT: Command an Animal — Nature check to direct your mount/companion/pet.
DETAIL:
  • 1 action, Nature vs level-based DC
  • Success: animal obeys 1 action
  • Animal Companions usually 2 actions on success
  • Crit: 3 actions | Fail: 1 action
  • Untrained animal = higher DC

═══════════════════════════════════════════════════════════
## [HEROICS] — Hero Point tactics
═══════════════════════════════════════════════════════════

## .tip hp
SHORT: Hero Points reroll any d20 — take new result even if worse.
DETAIL:
  • Spend 1 HP: reroll any d20 you JUST rolled
  • Take new result (even if worse) — no take-higher
  • Earned: nat 20s, dramatic moments, GM award
  • Max 3 at any time
  • See KM_P2.txt § Hero Point System

## .tip hpdying
SHORT: Spend ALL Hero Points when dying — avoid death, stabilize at 1 HP.
DETAIL:
  • Spend ALL current HP (minimum 1)
  • Immediately stabilize at 1 HP
  • Not "heal" — you are at 1 HP, still in danger
  • Can only do this once per dying occurrence

## .tip hpsave
SHORT: Save Hero Points for critical rolls — final save, boss hit, or lethal crit.
DETAIL:
  • Early-fight rerolls rarely worth it
  • Save for: killing blow, death save, plot-critical check
  • HP reset each session/long rest (varies by table)
  • Ask GM for session HP policy

═══════════════════════════════════════════════════════════
## [CONDITIONS] — status effect reminders
═══════════════════════════════════════════════════════════

## .tip flatfooted
SHORT: Off-guard = −2 AC. Stacks with every other penalty.
DETAIL:
  • Prone = off-guard to melee
  • Flanked (ally on opposite side) = off-guard
  • Grabbed/restrained = off-guard
  • Hidden attacker's target = off-guard to them
  • Stack off-guard with demoralize/feint for huge hits

## .tip frightened
SHORT: Frightened N = −N to all checks & DCs. Reduces by 1 each turn.
DETAIL:
  • Applied by Demoralize, spells, fear sources
  • Penalty to EVERYTHING: attacks, damage, AC, saves, skills
  • Decreases by 1 at end of each turn
  • Stacks — Demoralize + Fear spell = Frightened 3

## .tip hidden
SHORT: Hidden attackers: target flat DC 11 instead of AC.
DETAIL:
  • Hidden = enemies know square but can't see you
  • Attacks use flat DC 11 check first; fail = miss regardless of roll
  • Enemies off-guard to hidden attackers
  • Break hidden by attacking, loud action, or Seek

## .tip dying
SHORT: Dying = lose consciousness at 0 HP. Fort save each turn or die at 4.
DETAIL:
  • 0 HP: Dying 1 (or 2 if crit hit reduced you)
  • Each turn while dying: Recovery check DC 11 + dying value
  • Crit success: dying −2 | Success: dying −1 | Fail: dying +1 | Crit fail: +2
  • Dying 4 = dead. Healed above 0 = wounded condition

═══════════════════════════════════════════════════════════
## [COMBAT_POSITIONING] — tactical awareness
═══════════════════════════════════════════════════════════

## .tip flank
SHORT: Flanking — ally on opposite side of enemy makes them off-guard to melee.
DETAIL:
  • Draw imaginary line between you and ally through enemy
  • If line passes through opposite edges = flanking
  • Both of you: enemy is off-guard (−2 AC) to melee
  • Reach weapons extend flanking range

## .tip cover
SHORT: Cover grants +2 AC/Reflex (lesser) to +4 (standard) — Take Cover for greater.
DETAIL:
  • Lesser cover: corner of wall, ally = +1 AC
  • Standard cover: low wall, behind creature = +2 AC/Reflex
  • Greater cover: arrow slit, heavy = +4 AC/Reflex
  • Take Cover action: upgrade standard → greater (+4)

## .tip elevation
SHORT: Higher ground = +1 circumstance to attack (5+ ft elevation diff).
DETAIL:
  • 5+ ft higher than target: +1 attack
  • Flying attackers vs grounded melee: attackers get +1 too
  • Doesn't stack (one direction only)
  • Ranged attacks: better line of sight from high ground

## .tip reach
SHORT: Reach weapons (polearms, whips) hit at 10 ft, deny Steps around you.
DETAIL:
  • Glaives, halberds, whips, longspears = 10 ft reach
  • Denies enemy Stride past you (Step still works)
  • Flanking extends to 10 ft with reach weapons
  • Attack of Opportunity (if you have it) triggers at 10 ft

## .tip areaavoid
SHORT: Area spells hit everyone — spread the party before AoE enemies cast.
DETAIL:
  • 15-ft bursts (fireball size): spread party 20+ ft apart
  • Line spells: don't stand in a line
  • Cone spells: don't cluster in front
  • Watch for spellcaster somatic components (hands) = incoming AoE

═══════════════════════════════════════════════════════════
## FALLBACK TIPS — combat modes
═══════════════════════════════════════════════════════════

## [MODE: combat_fallback]
  .tip aid — Help ally's next check
  .tip recall — Learn enemy weakness
  .tip demoralize — Frighten for penalty
  .tip flank — Off-guard via positioning
  .tip takecover — Upgrade cover for +4 AC

> Out-of-combat fallback modes (social/exploration/downtime/kingdom) live in KM_Tips_B.md.

═══════════════════════════════════════════════════════════
## TRIGGER TABLE — combat & tactical rows
═══════════════════════════════════════════════════════════

| Trigger | Tips to surface |
|---------|----------------|
| first_combat_round | aid, recall, seek, flank |
| enemy_prone_off_guard | feint, trip, reposition |
| unknown_enemy_type | recall, sensemotive |
| hidden_or_concealed | seek, hide, takecover |
| skill_check_failed | hp |
| nat_20_rolled | hp |
| dying_condition | hpdying, treatwnd |
| flanking_opportunity | flank, reach |
| elevated_terrain | elevation |
| frightened_applied | frightened |
| off_guard_applied | flatfooted |
| stealth_possible | hide, sneak, avoidnotice |
| area_spell_incoming | areaavoid |
| animal_encountered | command |

> Out-of-combat trigger rows (scene entries, long_rest, downtime, kingdom, social checks, etc.) live in KM_Tips_B.md.

═══════════════════════════════════════════════════════════
## END KM_Tips.md (A) — see KM_Tips_B.md for remaining categories
═══════════════════════════════════════════════════════════
