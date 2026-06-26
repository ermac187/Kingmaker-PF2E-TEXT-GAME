# KINGMAKER — TIPS FOOTER (A)
## KM_PlayerHelp.md | Companion: KM_PlayerHelp.md | Referenced by: KM_DMRules.md

> **⛔ DM: At end of every response, append 1-3 tips whose triggers fired
> this turn. If no triggers fired, show 1 fallback tip from current mode.
> Copy the SHORT line verbatim. Never generate tips. Fabrication = `.fail 9`.
> Missing footer = `.fail 40`.**

> **Player commands:**
> - `.tip` — show detail for current turn's tip
> - `.tips` — list all tip codes by category
> - `.tip [code]` — show full detail for a specific tip

> **This file (A)** covers Combat Actions, Heroics, Conditions, Positioning.
> **See KM_PlayerHelp.md** for Pack Items, Downtime, Exploration, Social, Resting,
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

> Out-of-combat fallback modes (social/exploration/downtime/kingdom) live in KM_PlayerHelp.md.

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

> Out-of-combat trigger rows (scene entries, long_rest, downtime, kingdom, social checks, etc.) live in KM_PlayerHelp.md.

═══════════════════════════════════════════════════════════
## END KM_PlayerHelp.md (A) — see KM_PlayerHelp.md for remaining categories
═══════════════════════════════════════════════════════════


---

<!-- merged from KM_PlayerHelp.md (v93.21 file consolidation) -->

# KINGMAKER — TIPS FOOTER (B)
## KM_PlayerHelp.md | Companion: KM_PlayerHelp.md | Referenced by: KM_DMRules.md

> **⛔ DM:** This file continues KM_PlayerHelp.md. Same rules apply: copy SHORT
> line verbatim, never generate, `.fail 9` for fabrication, `.fail 40` for
> missing footer.

> **This file (B)** covers Pack Items, Downtime, Exploration, Social,
> Resting, Kingdom, Meta commands — plus remaining fallback modes, remaining
> trigger rows, and the master `.tips` list.

> **See KM_PlayerHelp.md** for Combat Actions, Heroics, Conditions, Positioning.

═══════════════════════════════════════════════════════════
## [PACK_ITEMS] — mundane gear with non-obvious uses
═══════════════════════════════════════════════════════════

## .tip chalk
SHORT: Chalk marks trails, draws runes, signals allies, tags cleared rooms.
DETAIL:
  • Mark paths in dungeons (find exit)
  • Draw temporary runes for ritual components
  • Signal arrows for split parties
  • Tag cleared/trapped doors
  Cost: 1 cp · Weight: — · In starting pack

## .tip rope
SHORT: 50 ft of rope binds, climbs, tethers, trips.
DETAIL:
  • Climb w/ rope + piton: DC 10 instead of surface DC
  • Bind prisoner: Athletics DC 20 to escape
  • Tripwire across door: Acrobatics DC 15 or prone
  • Tether swimmers, lower gear, mark cave depth
  Cost: 5 sp · Weight: L

## .tip oil
SHORT: Oil flask — fire splash, slick surface, quiet hinges, lantern fuel.
DETAIL:
  • Throw + ignite: 1d6 fire splash (improvised)
  • Pour 5-ft sq: Acrobatics DC 15 or prone
  • Oil hinges: silent doors (no Stealth penalty)
  • Lantern fuel: 6 hours
  Cost: 1 cp · Weight: —

## .tip mirror
SHORT: Small mirror sees around corners, signals, counters gaze attacks.
DETAIL:
  • Corner-scout without exposure (ambush immunity w/ Perception DC)
  • Long-range sunlight signal (miles in clear weather)
  • Gaze creatures (basilisk/medusa): target through mirror safely
  Cost: 1 gp · Weight: —

## .tip pole
SHORT: 10-ft pole probes floors, trips switches from safety.
DETAIL:
  • Trigger pressure plates remotely
  • Push levers/buttons at distance
  • Probe murky water for holes/creatures
  • Makeshift monopod/climbing aid
  Cost: 1 sp · Weight: 1

## .tip sack
SHORT: Empty sack captures imps/snakes, smothers flame, hides treasure.
DETAIL:
  • Capture small creature: Athletics DC 15
  • Smother candle/torch/small fire
  • Quick treasure grab in crisis
  • Over head = concealment + disguise
  Cost: 1 cp · Weight: L

## .tip rations
SHORT: Trail rations bait animals, distract dogs, sweeten Diplomacy.
DETAIL:
  • Feed hungry animal: +2 Nature or Diplomacy
  • Lay scent trail for tracking beast
  • Starving NPC: giving food shifts attitude +1 step
  Cost: 4 sp/day · Weight: L

## .tip tindertwig
SHORT: Instant fire — light torches, fuses, or oil flasks in 1 action.
DETAIL:
  • 1 action (vs 1 min flint & steel)
  • Light oil flask before throw (1 action total)
  • Start distracting fire in curtains/straw
  • Signal fire in emergency
  Cost: 1 sp · One-use · Weight: —

## .tip bedroll
SHORT: Bedroll — cold protection, armor padding, sound muffler.
DETAIL:
  • Cold weather: +2 Fort vs environmental cold
  • Under metal armor: no sleep penalty
  • Over door/window: muffles sound (+1 Stealth)
  • Makeshift 1-use shield (Cover bonus once)
  Cost: 2 sp · Weight: L

## .tip holywater
SHORT: Splash — 1d6 good damage vs fiends/undead + 1 splash.
DETAIL:
  • Thrown splash (attack vs AC, 20 ft range)
  • 1d6 positive/good vs fiends, undead
  • 1 splash damage all creatures in square
  • Crit: 2d6 + target dazzled 1 round
  Cost: 3 gp · One-use · Weight: L

## .tip caltrops
SHORT: Scatter in square — 1d4 piercing + Acrobatics DC 15 or slowed.
DETAIL:
  • 1 action to scatter 5-ft square
  • Entering creature: 1d4 piercing + DC 15 Acrobatics or −10 ft Speed
  • Sweeping clears (1 min)
  • Flyers/burrowers bypass
  Cost: 3 sp · Weight: 2

## .tip torch
SHORT: Torch — 20 ft bright light, 1d4 fire as improvised weapon.
DETAIL:
  • 20 ft bright / 20 ft dim light
  • Burns 1 hour
  • Improvised weapon: 1d4 fire
  • Light it with tindertwig in 1 action
  Cost: 1 cp · Weight: L

## .tip lantern
SHORT: Lantern — hooded (directed) or bullseye (60 ft cone); burns 6 hrs on 1 oil.
DETAIL:
  • Hooded: 30 ft bright all directions, can shutter to hide
  • Bullseye: 60 ft cone bright, 60 ft dim
  • Both: 1 oil flask = 6 hrs fuel
  • Windproof (won't blow out like torches)
  Cost: 5 sp hooded / 1 gp bullseye · Weight: 1

## .tip grapplinghook
SHORT: Grappling hook + rope — climb sheer walls, swing gaps, disarm at range.
DETAIL:
  • Throw Athletics DC 15 for 20 ft, DC 20 for 30 ft
  • Climb rope afterward (DC 10 w/ knotted rope)
  • Yank objects, disarm prone creatures (Athletics vs Reflex)
  Cost: 1 gp · Weight: L

## .tip piton
SHORT: Pitons + rope — make any climb a DC 10 check, secure anchor points.
DETAIL:
  • Hammer in (1 action)
  • Turn rope + surface DC into flat DC 10
  • Anchor for rappelling, catching falls
  • Wedge doors shut (DC 15 Athletics to force)
  Cost: 1 sp each · Weight: L

## .tip crowbar
SHORT: Crowbar — +2 circumstance to force open doors, chests, nail-sealed things.
DETAIL:
  • Athletics check to break/force gets +2 circumstance
  • Pry apart nailed planks, bent bars, stuck lids
  • Improvised weapon 1d6 B
  Cost: 5 sp · Weight: L

## .tip manacles
SHORT: Manacles secure prisoners — Escape DC 22, break DC 30.
DETAIL:
  • 1 action to apply (target must be willing or grappled/prone)
  • Escape (Acrobatics/Thievery): DC 22
  • Force break (Athletics): DC 30
  • Masterwork = DC 30 escape / DC 35 break
  Cost: 2 gp standard / 50 gp masterwork · Weight: L

## .tip whistle
SHORT: Signal whistle — clear tone over 1 mile outdoors, coordinate split parties.
DETAIL:
  • Carries ~1 mile outdoors, ~200 ft indoors
  • Pre-arranged codes: "danger," "rally," "all clear"
  • Silent dog whistle variant: only animals hear
  Cost: 8 sp · Weight: —

## .tip thieftools
SHORT: Thieves' tools — required for Disable Device and most locks.
DETAIL:
  • Thievery checks for locks/traps need these
  • Infiltrator tools (50 gp): +1 item bonus
  • Replacement picks (3 gp) if one breaks on crit fail
  Cost: 3 gp basic / 50 gp infiltrator · Weight: L

## .tip healerkit
SHORT: Healer's tools — required for Treat Wounds and Treat Poison.
DETAIL:
  • Required for Medicine to heal
  • Expanded kit (50 gp): +1 item bonus to Medicine
  • Carried on bandolier: gain hand access in 1 action (otherwise 2)
  Cost: 5 gp basic / 50 gp expanded · Weight: 1

## .tip climbkit
SHORT: Climber's kit — +1 circumstance to Athletics for climbing.
DETAIL:
  • Includes pitons, rope, harness, hammer
  • +1 circumstance to Climb
  • Extreme kit (40 gp): +2 circumstance
  • Reduces fall distance by 20 ft on success
  Cost: 5 sp basic / 40 gp extreme · Weight: 1

## .tip disguisekit
SHORT: Disguise kit — enables Impersonate and Disguise Yourself.
DETAIL:
  • Paints, wigs, false facial hair
  • Required for Impersonate (Deception)
  • Expert kit (20 gp): +1 circumstance
  • Takes 10 min to apply disguise
  Cost: 2 gp basic / 20 gp expert · Weight: 1

## .tip acid
SHORT: Acid flask — splash 1d6 acid + 1 persistent + 1 splash.
DETAIL:
  • Thrown splash, 20 ft range
  • 1d6 acid + 1d6 persistent (crits double)
  • 1 splash damage all in target's square
  • Eats rope, wood, weak armor (GM call)
  Cost: 3 gp lesser · Weight: L · One-use

## .tip alchfire
SHORT: Alchemist fire — 1d8 fire + persistent + splash.
DETAIL:
  • Splash, 20 ft range
  • 1d8 fire + 1d6 persistent fire + 1 splash
  • Set objects alight (oil, cloth, paper)
  • Stop persistent with DC 15 Acrobatics or water
  Cost: 3 gp lesser · Weight: L · One-use

## .tip thunderstone
SHORT: Thunderstone — 1d4 sonic + 1 splash + deafens on crit.
DETAIL:
  • Splash, sonic damage (ignores most resistances)
  • Crit: target deafened 1 min
  • Disrupt concentration on spellcasters
  Cost: 3 gp lesser · Weight: L · One-use

## .tip smokestick
SHORT: Smokestick — creates 5-ft concealment cloud, breaks line of sight.
DETAIL:
  • Activate + throw, 1 round smoke cloud
  • 5 ft radius, creatures concealed in it
  • Escape pursuit, break ranged attackers
  • Wind disperses in 1 round
  Cost: 3 gp · Weight: L · One-use

## .tip flashpowder
SHORT: Flashpowder — Reflex DC 17 or dazzled 1 min.
DETAIL:
  • 1 action to trigger, 10 ft burst
  • Creatures in area: Reflex DC 17
  • Fail: dazzled 1 min (flat DC 5 on attacks)
  • Crit fail: blinded 1 round
  Cost: 3 gp · Weight: L · One-use

## .tip perfume
SHORT: Perfume — mask scent (fool scent trackers), +1 Diplomacy in high society.
DETAIL:
  • Mask natural scent: trackers need higher Survival DC
  • Heavy perfume: +1 Diplomacy vs nobility, −1 vs ascetics
  • Pour on rag: scent lure for animals
  Cost: 5 gp · Weight: —

## .tip soap
SHORT: Soap — clean off mud/blood, lubricate surfaces for slipping.
DETAIL:
  • Clean: after combat for social scenes (+1 first impression)
  • Wet floor with soap: Acrobatics DC 15 or fall prone
  • Wash off poisons/contact hazards
  Cost: 2 cp · Weight: —

## .tip fishingtackle
SHORT: Fishing tackle — catch food for 1 day of rations per Survival success.
DETAIL:
  • 1 hour Survival check at water
  • Success: 1 day rations worth of fish
  • Crit: 2 days
  • Silver hook/line variant: +1 circumstance
  Cost: 1 sp · Weight: 1

## .tip instrument
SHORT: Musical instrument — Performance checks, soothe beasts, inspire morale.
DETAIL:
  • Required for Performance-based checks
  • Soothe animal: Performance vs Nature DC, calm hostile beast
  • Rally allies after fear effect: Performance DC 20
  • Earn Income at taverns
  Cost: 5 sp handheld / 8 gp standard · Weight: varies

## .tip writingset
SHORT: Writing set — required for forgeries, letters, maps, coded messages.
DETAIL:
  • Ink, quills, parchment
  • Required for Society forgery checks
  • Draw maps after scouting (Society DC 15)
  • Coded messages to allies
  Cost: 1 gp · Weight: L

═══════════════════════════════════════════════════════════
## [DOWNTIME] — activities between scenes
═══════════════════════════════════════════════════════════

## .tip craft
SHORT: Crafting — build items at half cost with Crafting check + time.
DETAIL:
  • Trained in Crafting + own formula + 4+ days
  • Pay half cost upfront in raw materials
  • Roll Crafting vs item-level DC
  • Success: complete. Extra days reduce remaining cost.
  • See KM_Mythic_Systems.md

## .tip earnincome
SHORT: Earn Income — work a skill for gold during downtime.
DETAIL:
  • Pick task matching skill (Crafting, Performance, Lore)
  • Roll vs task-level DC
  • Daily gp by proficiency + task level
  • Crit: double income

## .tip retrain
SHORT: Between chapters — swap feat/skill/ability for another over time.
DETAIL:
  • Feat/skill: 1 week
  • Ability score: 1 month
  • Teacher or source required for new option
  • See KM_BuildGuide.md

## .tip research
SHORT: Research threats — gain Recall Knowledge bonus in next chapter.
DETAIL:
  • 1 day in library/temple/with expert
  • Arcana/Society/Occultism vs GM DC
  • Success: +1 circumstance Recall Knowledge on topic next chapter
  • Crit: +2 + one specific secret revealed

## .tip repair
SHORT: Crafting check repairs damaged items and shields.
DETAIL:
  • 10 min activity per attempt, needs repair kit
  • Heals item for (5 × proficiency) HP on success
  • Shields after Shield Block: restore Hardness for next combat
  • Don't let weapons/armor go Broken — halves bonuses

## .tip learnspell
SHORT: Learn a Spell from scroll/spellbook during downtime.
DETAIL:
  • Requires spell in accessible source + 1 hour per spell level
  • Arcana/Nature/Occultism/Religion vs spell DC
  • Success: add to repertoire/spellbook
  • Crit fail: scroll consumed

## .tip cookmeal
SHORT: Cook hearty meal at camp — +1 temp HP for party next day.
DETAIL:
  • 1 hour cooking (Survival or Crafting)
  • Uses 2 rations, feeds 4
  • Success: +1 temp HP for party next day
  • Crit: +2 temp HP + 1 morale to first save vs fear

## .tip sharpen
SHORT: Whetstone — 10 min sharpen gives +1 damage on first hit next combat.
DETAIL:
  • Whetstone (2 cp) + 10 min
  • Works on slashing/piercing weapons
  • +1 damage on FIRST successful hit next encounter
  • Stacks with Weapon Potency rune
  Cost: 2 cp · One-use per sharpen

═══════════════════════════════════════════════════════════
## [EXPLORATION] — beyond the menu
═══════════════════════════════════════════════════════════

## .tip avoidnotice
SHORT: Avoid Notice — Stealth instead of Perception for initiative.
DETAIL:
  • Declare during exploration
  • Speed −5 ft while active
  • Stealth for initiative; undetected if you beat enemy Perception DC
  • Whole party must Avoid Notice or fails

## .tip search
SHORT: Search exploration activity — automatic Seek while traveling.
DETAIL:
  • GM rolls Seek in each area
  • Finds hidden doors, traps, caches passively
  • Half speed travel
  • Stack with Investigate

## .tip investigate
SHORT: Investigate — Recall Knowledge on things as you travel.
DETAIL:
  • Recall Knowledge on landmarks, creatures, clues
  • Each success: lore, relevance, recognition
  • Half speed

## .tip followtheexpert
SHORT: Follow the Expert — use an ally's skill check at −2 instead of your own.
DETAIL:
  • Declare leader (trained in skill)
  • Your untrained/trained becomes leader's modifier −2
  • Non-leader allies get +1 to own checks in skill
  • Great for parties w/ one face or one sneak

## .tip scout
SHORT: Scout exploration — party gets +1 initiative when encounter starts.
DETAIL:
  • Requires Scout feat (L2)
  • Stealth or Survival check during exploration
  • Party: +1 circumstance to initiative
  • No speed penalty

## .tip defend
SHORT: Defend exploration — shield raised, +2 AC when encounter begins.
DETAIL:
  • Speed halved while defending
  • Start encounter with Raise a Shield already active
  • Combine with Hustle/Follow the Expert for flexibility

## .tip repeatspell
SHORT: Repeat a Spell — exploration activity for sustained magic.
DETAIL:
  • Cast sustainable cantrip repeatedly (Light, Detect Magic)
  • Speed halved
  • Start encounter with spell already going
  • Conserves spell slots

## .tip maphex
SHORT: In exploration — mark discovered hexes to avoid retreading.
DETAIL:
  • `.map` shows current hex layout
  • Type `.mark [hex]` if your character drew a map
  • Lost features become easier to refind
  • See KM_Exploration.md

═══════════════════════════════════════════════════════════
## [SOCIAL] — options the menu may not show
═══════════════════════════════════════════════════════════

## .tip gather
SHORT: Gather Information — half day in town for rumors, leads, local lore.
DETAIL:
  • 2+ hour Diplomacy in populated area
  • DC based on obscurity
  • Success: 1 rumor/fact
  • Spend 1 sp bribes: +1 circumstance

## .tip request
SHORT: Request a favor — Diplomacy check vs attitude-based DC.
DETAIL:
  • 1+ min conversation
  • DC: Helpful (15) / Friendly (20) / Indifferent (25+)
  • Hostile won't listen
  • Unreasonable ask: DC +5/+10

## .tip coerce
SHORT: Coerce — Intimidation over 1+ min forces compliance via threat.
DETAIL:
  • Intimidation vs Will DC
  • Target understands language, believes threat
  • Success: compliance for 1 hour (still internally hostile)
  • Crit: compliance 1 day + unhelpful after
  • Crit fail: target hostile forever

## .tip gift
SHORT: Gift an item worth 1+ gp — +1 circumstance next Diplomacy check.
DETAIL:
  • Genuine gift (not bribe — use Coerce for that)
  • 1 gp = +1 | 10 gp = +2 | 100 gp = +3
  • Only one gift bonus at a time
  • Offensive gift: −2 penalty

## .tip lie
SHORT: Deception vs Perception DC — plant false info verbally.
DETAIL:
  • 1 action per lie
  • Success: target believes
  • Crit: absolute belief + target defends your story
  • Crit fail: target KNOWS you lied (permanent suspicion)

## .tip impersonate
SHORT: Impersonate — Deception + disguise kit to pass as someone else.
DETAIL:
  • Needs disguise kit (10 min to apply)
  • Deception vs Perception of each observer
  • Knowing the target personally: they get +4
  • Fail: suspicious. Crit fail: identified

## .tip make-an-impression
SHORT: Make an Impression — Diplomacy over 10 min shifts NPC attitude 1 step up.
DETAIL:
  • 10 min conversation
  • Diplomacy vs Will DC
  • Success: attitude up 1 (Indifferent → Friendly, etc.)
  • Crit: up 2 steps
  • Fail: no change | Crit fail: down 1 step

═══════════════════════════════════════════════════════════
## [RESTING] — camp, watch, recovery
═══════════════════════════════════════════════════════════

## .tip longrest
SHORT: Long Rest — 8 hrs sleep. Heals Con mod × level HP, refills spells.
DETAIL:
  • Full night: HP = Con mod × level (min 1 × level)
  • Spell slots refill
  • Focus pools refill
  • Hero Points reset to 1 (GM option)
  • Need 4+ hours sleep + 4+ light activity

## .tip watch
SHORT: Rotating watch — 2-hour shifts per person, Perception vs approach DC.
DETAIL:
  • 4-person party: 2 hr watches
  • Watcher rolls Perception to detect approaches
  • Sleepers are unconscious (off-guard + auto-fail Perception)
  • Heavy armor + no bedroll = Fatigued next day

## .tip dangerouscamp
SHORT: Dangerous environments — extra checks during rest.
DETAIL:
  • GM sets environment DC
  • Survival check to find safe campsite
  • Fail: rest interrupted by event
  • Crit fail: no rest benefit (no HP, no spells)

## .tip morale
SHORT: Companion morale — Connection refills on acknowledgment, drops on neglect.
DETAIL:
  • `.needs [name]` to view
  • Rest/Purpose/Connection/Recognition — four meters
  • Ignoring = slow decay = Hostile abilities
  • See KM_World_Systems.md

═══════════════════════════════════════════════════════════
## [KINGDOM] — between-chapter governance
═══════════════════════════════════════════════════════════

## .tip kingdomturn
SHORT: Kingdom Turn — monthly. Collect resources, assign leaders, resolve events.
DETAIL:
  • Every month in-game
  • 4 phases: Upkeep → Commerce → Activity → Event
  • Leaders make ability-based checks for kingdom rolls
  • See KM_Kingdom.md

## .tip orders
SHORT: Type `.orders` — assign standing orders to leadership council.
DETAIL:
  • Councilors act while you adventure
  • Priorities: defense, growth, diplomacy, trade
  • Adjusts kingdom stats passively
  • See KM_War_Systems.md

## .tip board
SHORT: Type `.board` — adventurer's board. Take bounties for XP & gold.
DETAIL:
  • Available from Ch2 onward
  • 2-6 bounties posted per city, refresh weekly
  • Ranged difficulty and reward
  • See KM_Kingdom.md

## .tip wartable
SHORT: Type `.wartable` — strategic overview of conflicts and threats.
DETAIL:
  • Track enemy armies, border tension, advisor warnings
  • Updates each Kingdom Turn
  • See KM_War_Systems.md

═══════════════════════════════════════════════════════════
## [META] — game commands you may forget
═══════════════════════════════════════════════════════════

## .tip save
SHORT: Type `.save` to export full JSON save block anytime.
DETAIL:
  • Output current state: HP, XP, gold, items, flags, threads
  • Copy to file outside Claude for safety
  • Paste back to resume in new session

## .tip brief
SHORT: Type `.brief` to re-show the current scene's setup block.
DETAIL:
  • Reminds you of NPCs, location, active flags
  • Use if you forgot what's happening after a break
  • No time cost

## .tip status
SHORT: Type `.s` or `.status` — full character sheet, HP, conditions.
DETAIL:
  • Short form: `.s`
  • Long: `.status`
  • Shows HP, conditions, hero points, active buffs

## .tip party
SHORT: Type `.party` — all companion status + positions + readiness.
DETAIL:
  • All companion HP, conditions, abilities available
  • Formation (vanguard/rearguard)
  • Quick-glance for combat planning

## .tip inv
SHORT: Type `.inv` — full inventory by category.
DETAIL:
  • Sortable view
  • Shows bulk & encumbrance
  • Highlights unidentified items
  • `.inv [name]` = specific companion's inventory

## .tip fail
SHORT: Type `.fail [N]` to flag a DM violation and request rewind.
DETAIL:
  • 1-39 codes covering every common DM error
  • `.fail 2` = dropped your dialogue (most common)
  • `.fail 9` = fabricated content
  • See KM_DMRules.md for full list
  • Prefer pasting missing content over `.fail 2` to avoid death spiral

## .tip opt
SHORT: Type `.opt` — change game options mid-session.
DETAIL:
  • `.opt length [short/medium/long/epic]`
  • `.opt paras [min] [max]`
  • `.opt beats [N]` — NPC dialogue beats minimum
  • Takes effect next response

## .tip map
SHORT: Type `.map` — redraw combat or exploration map.
DETAIL:
  • Combat: positions, distances, terrain
  • Exploration: current hex + neighbors
  • ASCII format

## .tip fastforward
SHORT: Type `.ff [event]` to skip to a specific narrative beat — GM confirms.
DETAIL:
  • Useful for long travel, downtime montage
  • GM summarizes intervening time
  • Any consequences (rolls, events) resolved inline
  • Player approves summary before continuing

═══════════════════════════════════════════════════════════
## FALLBACK TIPS — out-of-combat modes
═══════════════════════════════════════════════════════════

## [MODE: social_fallback]
  .tip bonmot — Diplomacy penalty setup
  .tip request — Ask for favors
  .tip gift — Buy goodwill
  .tip sensemotive — Read the NPC
  .tip gather — Chase rumors in town

## [MODE: exploration_fallback]
  .tip search — Auto-find traps/hidden
  .tip avoidnotice — Stealthed travel
  .tip chalk — Mark your path
  .tip scout — +1 initiative for party
  .tip followtheexpert — Use ally's skill

## [MODE: downtime_fallback]
  .tip craft — Build items
  .tip earnincome — Make gold
  .tip treatwnd — Heal w/o magic
  .tip research — Prep for next chapter
  .tip sharpen — +1 first-hit damage

## [MODE: kingdom_fallback]
  .tip kingdomturn — Monthly phases
  .tip orders — Standing leadership orders
  .tip board — Adventurer bounties
  .tip wartable — Strategic overview

═══════════════════════════════════════════════════════════
## TRIGGER TABLE — out-of-combat rows
═══════════════════════════════════════════════════════════

| Trigger | Tips to surface |
|---------|----------------|
| scene_entered_dungeon | chalk, pole, search, torch, lantern |
| scene_entered_wilderness | rations, rope, avoidnotice, fishingtackle |
| scene_entered_settlement | gather, request, gift |
| scene_entered_noble_court | perfume, impersonate, bonmot |
| long_rest | treatwnd, bedroll, cookmeal, watch, longrest |
| camp_set | bedroll, watch, dangerouscamp |
| npc_hostile | coerce, demoralize |
| npc_indifferent | request, gift, bonmot, make-an-impression |
| npc_helpful | request |
| fire_source_needed | tindertwig, oil, torch |
| climb_or_descent | rope, piton, grapplinghook, climbkit |
| gaze_or_vision_threat | mirror |
| undead_or_fiend | holywater, recall |
| locked_door_or_chest | thieftools, crowbar |
| prisoner_captured | manacles, coerce |
| downtime_declared | craft, earnincome, retrain, research, repair, sharpen |
| first_kingdom_turn | kingdomturn, orders, wartable |
| casting_exploration | repeatspell |
| party_split | whistle, chalk |
| social_check_needed | lie, impersonate, sensemotive |
| animal_encountered | command, rations |

Unlisted triggers → use mode fallback from section above (combat triggers live in KM_PlayerHelp.md).

═══════════════════════════════════════════════════════════
## .tips — MASTER LIST COMMAND
═══════════════════════════════════════════════════════════

When player types `.tips`, display the category headers with
tip codes listed. Do NOT print details — direct player to
`.tip [code]` for each.

```
💡 AVAILABLE TIPS — type .tip [code] for details

COMBAT ACTIONS: aid, feint, recall, seek, trip, shove, grapple,
  disarm, reposition, demoralize, bonmot, treatwnd, stride,
  step, takecover, raiseshield, ready, delay, escape, hide,
  sneak, diversion, tumblethrough, leap, highjump, longjump,
  grabedge, sensemotive, maneuverflight, command

PACK ITEMS: chalk, rope, oil, mirror, pole, sack, rations,
  tindertwig, bedroll, holywater, caltrops, torch, lantern,
  grapplinghook, piton, crowbar, manacles, whistle, thieftools,
  healerkit, climbkit, disguisekit, acid, alchfire, thunderstone,
  smokestick, flashpowder, perfume, soap, fishingtackle,
  instrument, writingset

DOWNTIME: craft, earnincome, retrain, research, repair,
  learnspell, cookmeal, sharpen

EXPLORATION: avoidnotice, search, investigate, followtheexpert,
  scout, defend, repeatspell, maphex

SOCIAL: gather, request, coerce, gift, lie, impersonate,
  make-an-impression

HEROICS: hp, hpdying, hpsave

CONDITIONS: flatfooted, frightened, hidden, dying

POSITIONING: flank, cover, elevation, reach, areaavoid

RESTING: longrest, watch, dangerouscamp, morale

KINGDOM: kingdomturn, orders, board, wartable

META: save, brief, status, party, inv, fail, opt, map, fastforward
```

═══════════════════════════════════════════════════════════
## END KM_PlayerHelp.md — see KM_PlayerHelp.md for combat categories
═══════════════════════════════════════════════════════════


---

<!-- merged from KM_PlayerHelp.md (v93.21 file consolidation) -->

# KINGMAKER — BEST RUN ARCHIVE & SCORING
## KM_PlayerHelp.md | Referenced by: KM_ChapterSelect.md, all Export files

---

> **PURPOSE:** This file stores your personal best chapter completions. When you
> use Chapter Select to skip ahead, the DM reads YOUR best run data instead of
> generic canonical defaults. The DM AUTOMATICALLY scores every run at chapter
> end and outputs the Best Run block when you beat your record. No command needed.

---

## 🏆 RUN QUALITY SCORE — DM EVALUATES AT EVERY CHAPTER END

**⛔ MANDATORY.** At chapter export time, the DM calculates the Run Quality
Score using ALL vectors below. Show the scorecard to the player alongside
the export block. Compare against the stored best run score. If current run
scores HIGHER (or no best run exists), auto-output the Best Run block with
paste instructions.

### SCORING VECTORS

**1. HERO POINTS EARNED (max 30)**
Total Hero Points awarded this chapter (not pool — total earned including overflow).
- Each HP earned = 3 points (cap 10 HP = 30 pts)

**2. CREATIVE PLAY (max 25)**
Judgment triggers that fired (the creative HP triggers, not automatic ones).
- Each judgment trigger = 5 points (cap 5 = 25 pts)
- Callback, tactical sacrifice, enemy turned, perfect info play, humor, improvised weapon, environment kill, talk-down, out-thought — all count

**3. DIFFICULTY CHOICES (max 30)**
Harder paths chosen when easier ones were available.
- Entered without using letter/invitation when you had one: +5
- Resolved a combat encounter through pure social/logic (no weapons): +5
- Chose unarmed or non-lethal approach when armed was easier: +5
- Protected civilians or NPCs at personal cost (took damage, lost resources): +5
- Refused a bribe, shortcut, or exploit that would have helped: +5
- Took a solo encounter without calling for companion help: +5

**4. CIVILIAN REPUTATION (max 20)**
How the common people see eRmaC at chapter end.
- `public_reputation` score mapped:
  - 0-10: 0 pts | 11-25: 5 pts | 26-50: 10 pts | 51-75: 15 pts | 76+: 20 pts
- If no reputation score tracked yet (Prologue): use crowd reactions
  - Crowd feared you: 0 pts | Crowd neutral: 5 pts
  - Crowd respected you: 15 pts | Crowd cheered/admired: 20 pts

**5. COMPANION RELATIONSHIPS (max 25)**
Average opinion score across all active companions at chapter end.
- Average +1 to +5 (FAVORABLE): 5 pts
- Average +6 to +10 (WARM): 10 pts
- Average +11 to +15 (FRIENDLY): 15 pts
- Average +16 to +20 (DEVOTED): 25 pts
- BONUS: Any single companion at DEVOTED (+16): +5 pts (stacks, cap +10)

**6. KEY NPC RELATIONSHIPS (max 20)**
Important story NPCs — not companions, the world's power players.
- Jamandi at DEVOTED: +8 | FRIENDLY: +5 | WARM: +3
- Kesten at WARM+: +3
- Kassil at WARM+: +3
- Each other story NPC at FRIENDLY+: +2 (cap +6 total)

**7. COMPLETENESS (max 20)**
Content engaged, secrets found, optional paths taken.
- Each completed quest: +2 (cap +10)
- Each secret/hidden content found: +3 (secret room, hidden NPC, lore discovery)
- Each optional scene engaged (not skipped): +1 (cap +5)

**8. LEGACY QUALITY (max 10)**
How many player_legacy entries were created this chapter.
- 1-2 entries: 3 pts | 3-4 entries: 6 pts | 5+: 10 pts
- DM judges whether entries are genuinely memorable (not just "fought a guy")

**9. TITLE SYSTEM (max 10)**
Titles granted this chapter.
- Each Suffix granted: +3
- Each Prefix granted: +5
- Title refund earned (+5 reaction): +2

**10. STYLE BONUS (max 10, DM judgment)**
The intangible. Did the player bring something special?
- Consistent character voice throughout: +3
- A single moment the DM would remember telling someone about: +4
- Made an NPC break from their script through sheer force of personality: +3

---

### TOTAL: 200 POINTS MAXIMUM PER CHAPTER

```
RUN QUALITY SCORECARD
═══════════════════════════════
Hero Points Earned:    __/30
Creative Play:         __/25
Difficulty Choices:     __/30
Civilian Reputation:   __/20
Companion Relations:   __/25
Key NPC Relations:     __/20
Completeness:          __/20
Legacy Quality:        __/10
Title System:          __/10
Style Bonus:           __/10
───────────────────────────────
TOTAL:                 __/200
Previous Best:         __/200
NEW RECORD?            YES / NO
═══════════════════════════════
```

---

## ⛔ DM INSTRUCTION — AUTO-EVALUATION AT CHAPTER END

**This fires AUTOMATICALLY at every chapter export. No player command needed.**

1. **Calculate the score** using all 10 vectors above.
2. **Compare against stored best:** Read this file's matching chapter section.
   - If `"_empty": true` → no previous best exists. Current run IS the best.
   - If a `"_score"` exists → compare. Current must be STRICTLY HIGHER to win.
   - Ties do NOT replace. The stored best stands on a tie.
3. **If NEW RECORD (current > stored, or no stored):**
   - Display the FULL scorecard (all 10 vectors with breakdown)
   - Output: *"🏆 NEW BEST RUN — [chapter]. Score: [X]/200 (previous: [Y]/200)."*
   - Output the Best Run data block with:
     *"Copy the block below and paste it into the `[CHAPTER] BEST RUN` section
     of `KM_PlayerHelp.md`, replacing the old data."*
4. **If NOT a new record (current ≤ stored):**
   - Display ONE line only: *"Run score: [X]/200. Your best: [Y]/200."*
   - Do NOT output a Best Run block. Do NOT show the full scorecard.
   - The old best stands. No action needed from the player.

---

## ⛔ DM INSTRUCTION — READING BEST RUN DATA (at Chapter Select)

**At Chapter Select time:** For each chapter being skipped, check if a Best Run
block exists here. If it does (no `"_empty": true`): use that data INSTEAD of
canonical defaults from KM_ChapterSelect.md. If empty: fall back to canonical.

**Merge rule:** Best Run data is authoritative for everything it contains.
Canonical defaults fill ONLY gaps.

**Player — SAME BUILD:** Use Best Run's EXACT level, XP, HP, gear, gold, all stats.
**Player — DIFFERENT BUILD:** Use Best Run's LEVEL and XP. Recalculate HP/feats/skills from new build at that level. Gear gets equivalent-tier substitution.

**Companions — RETURNING (in both old and new Pick-10):** Use their Best Run level, build, gear, and relationship data exactly.
**Companions — NEW (in new Pick-10 but NOT in Best Run):** Level up to match the player's Best Run level. Assign ★ recommended build. Generate tier-appropriate gear. Relationship starts at +3 (no history). They then choose their build at Step 4 like normal — ★ is just the starting point if the player picks `★ AUTO`.

---

## ⛔ DM INSTRUCTION — BEST RUN BLOCK FORMAT

Save the FULL chapter export block. Keep EVERYTHING — stats AND story:

```
KEEP ALL:
  PLAYER: level, xp, hp_max, hp_current (set to max on load), ac, saves,
          skills (ranks + mods), feats, spells, attributes, build_id,
          inventory (full items with stats + runes), gold, speed,
          perception, initiative_mod, conditions (cleared on load)
  COMPANIONS: full companion blocks — level, hp, builds, gear, feats,
              spell slots (ALL companions, not just active party)
  STORY: story_flags, npc_threads (thread + priorities + memory),
         npc_relations (score + trend + attraction),
         player_legacy (moment + witnessed_by), quest_log,
         promises_and_dialogue, companion_titles, dispositions,
         alignment_track, world_state, companion_picks + builds
  SYSTEMS: dream_log, debate_results, kingdom state (Ch2+),
           scripted_interactions_completed, crafting recipes known

ADD:  "_best_run": "[chapter]"
      "_score": [total]
      "_score_breakdown": { vector scores }
      "_saved_date": "[date]"
      "_run_summary": "[1-2 sentence DM summary of what made this run special]"
```

**On load from Best Run:** HP restored to max. Spell slots restored to full.
Conditions cleared. This is a fresh start at the chapter — not mid-combat.

---

## 📋 PRE-PROLOGUE BEST RUN

```json
{
  "_best_run": "pre-prologue",
  "_empty": true
}
```

---

## 📋 PROLOGUE BEST RUN

```json
{
  "_best_run": "prologue",
  "_score": 163,
  "_score_breakdown": {
    "hero_points": 30,
    "creative_play": 25,
    "difficulty_choices": 30,
    "civilian_reputation": 20,
    "companion_relations": 5,
    "key_npc_relations": 13,
    "completeness": 20,
    "legacy_quality": 10,
    "title_system": 10,
    "style_bonus": 10
  },
  "_saved_date": "Session — Prologue Complete",
  "_run_summary": "Entered unarmed. Never drew a weapon. Bread roll preceding garotte. Lady Sleeps invented under pressure. Talk-down via the opponent's own argument. All 11 titled. Operation Leech live before the carriage was ordered."
}
```

---

## 📋 CHAPTER 1 BEST RUN

```json
{
  "_best_run": "chapter_1",
  "_empty": true
}
```

---

## 📋 CHAPTER 2 BEST RUN

```json
{
  "_best_run": "chapter_2",
  "_empty": true
}
```

---

## 📋 CHAPTER 3 BEST RUN

```json
{
  "_best_run": "chapter_3",
  "_empty": true
}
```

---

## 📋 CHAPTER 4 BEST RUN

```json
{
  "_best_run": "chapter_4",
  "_empty": true
}
```

---

## 📋 CHAPTER 5 BEST RUN

```json
{
  "_best_run": "chapter_5",
  "_empty": true
}
```

---

## 📋 CHAPTER 6 BEST RUN

```json
{
  "_best_run": "chapter_6",
  "_empty": true
}
```


---

<!-- merged from KM_PlayerHelp.md (v93.21 file consolidation) -->

# KINGMAKER — QUICK-START GUIDE
## KM_PlayerHelp.md | Read this before your first session

---

## 🎮 WHAT IS THIS?

A complete text-based RPG running the **Pathfinder 2e Kingmaker Adventure Path**, played with an LLM as your Dungeon Master. You type actions. The LLM plays the world, all NPCs, all dice, and all consequences. You rule a kingdom, fight monsters, forge alliances, and decide the fate of the Stolen Lands.

**No dice required. No other players needed. No prep.**

---

## 📁 THE FILES

You have **266 files** organized in project knowledge. The DM finds them automatically — you only paste `KM.txt`. Key categories:

| Type | Key Files | When Loaded |
|------|-----------|-------------|
| **Core** | `KM.txt`, `KM_P2.txt`, `KM_DMRules.md`, `KM_LoadRules.md` | Every session |
| **Commands** | `KM_Commands.md`, `_Maps`, `_P2`, `_New` | Every session |
| **Companions** | `KM_Companions.md` + `_B` / `_C` / `_D` / `_Agendas` / `_Agendas_B` / `_Ambient` / `_Banter` / `_Builds` / `_Iconics` / `_Leveling` / `_Scaled` / `_StateVoice` | Every session |
| **Builds** | `KM_Builds.md` → `_A` through `_M` (13 sub-files), `KM_BuildGuide.md` | Character creation + level-up |
| **Chapter** | `KM_PrePrologue.md` + Paths, `KM_Prologue.md` + P2/P3, `KM_Ch1–4.md` | Current chapter |
| **World** | `KM_Map.md` / `_B`, `KM_Kingdom.md`, `KM_Exploration.md` | Every session |
| **Systems** | `KM_World_Systems.md`, `KM_Romance.md`, `KM_War_Systems.md`, `KM_World_Systems.md`, `KM_Kingdom.md`, `KM_Kingdom.md`, `KM_Combat_Systems.md` | Per KM_LoadRules.md |
| **New (33 features)** | `KM_Mythic_Systems.md`, `KM_Mythic_Systems.md`, `KM_Mythic_Systems.md`, `KM_Kingdom.md`, `KM_War_Systems.md`, `KM_War_Systems.md`, `KM_Mythic_Systems.md`, `KM_Mythic_Systems.md` + 15 more | Per KM_LoadRules.md |
| **Reference** | `KM_Actions.md`, `KM_Bestiary.md` / `_B`, `KM_Glossary.md`, `KM_Conditions_Skills.md` | As needed |
| **Save/Load** | `KM_Prologue_Systems.md`, `KM_Ch1.md-KM_Ch7.md` | Chapter transitions |

**Full file index:** See `KM.txt` § FILE INDEX for the complete list of all 266 files.

---

## ▶️ STARTING YOUR FIRST GAME

**Step 1 — Open a fresh LLM chat.**

**Step 2 — Load these files** (paste their contents into the chat, or attach them):
```
KM.txt                    ← LOAD THIS FIRST
KM_Builds.md
KM_BuildGuide.md
KM_Actions.md
KM_Commands.md
KM_Commands_Maps.md
KM_Commands.md
KM_Companions.md
KM_Companions.md
KM_Map.md
KM_Kingdom.md
KM_Exploration.md
KM_Bestiary.md
KM_PrePrologue.md
KM_PrePrologue_Paths.md
KM_PrePrologue_Paths_QT.md
```

**Step 3 — Run the build file verification BEFORE requesting the menu.**

Send this exact message first:

> *"Before showing the build menu: quote Build 11's class, ancestry, and both primary stats (with scores) directly from KM_Builds.md."*

**The correct answer is:**
- Class: **Witch (Cackle/Curse)**
- Ancestry: **Gnome (Fey-Touched)**
- Primary stats: **INT 18, CHA 18** — both at 18, not one primary

**If the DM gives you a different class, ancestry, or gets the stat array wrong** — it is generating from training memory, not reading your file. Do not request the build menu yet. See "If verification fails" below.

**Step 4 — Send this message:**
> *"Show me the build selection screen."*

The DM will display the full 1–20 menu read from `KM_Builds.md`. Each build is a complete character — no further setup needed.

**Step 5 — Pick a build, then verify scene files.**

After selecting your build, send this exact message before the first scene:

> *"Before we begin: what are Malak's exact opening words at the Restov gate? Quote them directly from KM_PrePrologue.md."*

**The correct answer contains:**
> *"Halt, stranger. Hands clear of that [weapon] and [secondary weapon]. Palms where I can see them. Now."*
> followed by a strip-search demand ending with *"Move wrong and I'll have you facedown with my boot on your neck."*

**If the DM says anything about** an entry fee, a processing fee, gold demanded at the gate, "special maintenance," Malak picking his teeth, a broken merchant wagon, or addresses you as "Master Dwarf" — **the files are not being read.** The DM is hallucinating plausible fantasy content and calling it your file. Every session played on a failed verification is a different game than the one you built.

**If either verification fails:**
1. Start a completely fresh chat
2. Load `KM.txt` first and send it alone — confirm the DM acknowledges the specific rules inside it (ask: *"What is the ULTRA-PRIORITY rule about speaking for the player?"*)
3. Load remaining files one at a time
4. Run both verification tests again before any scene
5. If it fails a second time, the LLM you are using does not reliably read uploaded files. Switch to a different one. Claude is recommended.

> **These tests take 60 seconds and can save hours of playing the wrong game.**

**Step 6 — Play.**

---

## 🎭 HOW TO PLAY

**Everything you type without a period is in-character.**
The world reacts to it. NPCs hear it. Consequences follow.

**Everything you type WITH a period (`.`) is a command.**
The DM steps outside the game, executes the command, and returns.

### In-Character Examples
```
"I show the guard captain my letter from Lady Jamandi."
"Draw my sword. Step between the assassin and Kesten."
"Ask Linzi what she knows about the feast's other guests."
"Search the kitchen for signs of poison."
```

### Out-of-Character Examples
```
.s             → Show my character sheet
.hp            → Show party health
.map           → Show the current scene map
.map combat    → Show the combat tactical grid
.quests        → Show quest log
.inventory     → Show full inventory
.alignment     → Show my alignment track
.options       → Change game settings
.hold          → Pause, I need to think
.continue      → Resume
.rewind        → Undo last action
.fix [issue]   → Correct a DM error
.ooc [message] → Talk to the DM out of character
.help          → Show all commands
```

---

## ⚔️ HOW COMBAT WORKS

1. DM describes the encounter and draws an **ASCII combat map**
2. DM rolls initiative — shows the order
3. **Your turn:** type one action at a time
   - *"Strike the nearest bandit"*
   - *"Move 20 feet toward the archer, then cast Produce Flame"*
   - *"Raise shield, then step left, then Strike"*
4. DM resolves it — shows the dice roll, result, damage
5. DM runs enemies and companions (unless you set companions to Manual)
6. Repeat until combat ends

**You have 3 actions per turn.** Most strikes take 1 action. Moving takes 1 action. Casting can take 1–3 actions. You also have 1 reaction per round (like Shield Block or Attack of Opportunity).

**Troll regeneration** (Ch2+): Trolls get back up after being knocked down unless you deal fire or acid damage while they're at 0 HP. Alchemist's Fire works. A torch works. Know this before you go to Trobold.

---

## 💾 SAVING YOUR GAME

The game saves between **chapters** — not mid-chapter by default.

**At the end of each chapter:** Type `.export` and the DM will output a JSON Save Block. Copy it to a text file.

**Starting a new chat session mid-chapter:** Type `.save` — the DM outputs a mid-session save. Paste it at the start of your next chat along with the same files.

**Starting a new chapter:** The chapter file's Export section has an exact script to paste. Follow it exactly — it loads the right files and imports your save in one message.

---

## 🗣️ TALKING TO NPCS

Just talk. Whatever your character would say, type it.

```
"Who are you, and why are you blocking my path?"
"I've heard rumors about your captain. I'd like to verify them before I say more."
"Name your price."
```

The DM voices the NPC in response. No special format needed.

**Companions** travel with you and comment on events. They have opinions. If you ask them for their perspective, they'll give it. If you do things they approve of, your relationship with them grows. If you do things they find unforgivable, it doesn't.

---

## 🏰 THE KINGDOM

Once you defeat the Stag Lord in **Chapter 1**, you found a kingdom. From that point forward:

- Each in-game month you run a **Kingdom Turn** (`.kingdom` to see status)
- You assign **Leadership Roles** to companions and NPCs
- You **claim hexes**, build settlements, construct buildings, raise armies
- The kingdom reacts to your decisions — your alignment, your companions' deaths, your alliances

The kingdom is a character. Treat it like one.

---

## 🤝 COMPANIONS

You travel with up to 3 companions. Each one:
- Has their own personality and will react to your choices
- Has a **Relationship score** (Hostile/Strained/Neutral/Friendly/Devoted)
- Has a **personal quest** that unlocks at Friendly or Devoted
- **Completing their quest before Chapter 7** is the difference between them surviving the endgame or not

**Companion AI:** By default, companions act on their personality in combat (Amiri charges, Linzi supports, Valerie holds the line). You can take manual control of any companion in `.options`.

**Dismissing companions:** Only at Oleg's Trading Post, your capital, or named settlements. They wait at your base until you return.

---

## 📜 THE STORY

The campaign has 8 chapters plus a Prologue. Each chapter takes a few sessions. The whole campaign is a full CRPG's worth of content.

| # | Name | Levels | Core Threat |
|---|------|--------|-------------|
| Pre | Swordlord's Invitation | 1 | Gate confrontation |
| Pro | Jamandi's Manor | 1 | Assassination |
| 1 | Stolen Lands | 1–4 | The Stag Lord |
| 2 | Troll Trouble | 5–8 | Hargulka + Season of Bloom |
| 3 | Varnhold Vanishing | 9–12 | Vordakai |
| 4 | Twice-Born Warlord | 13–16 | Armag |
| 5 | War of River Kings | 13–16 | Irovetti/Pitax |
| 6 | Thousand Screams | 16–18 | Nyrissa's Wrath |
| 7 | The Final Act | 18–20 | Nyrissa + The Lantern King |

---

## 💡 TIPS FOR YOUR FIRST SESSION

**1. Read the choices before you act.** The DM presents 10–30 options at major decision points. Some choices are irreversible. Some build toward things chapters away.

**2. Talk to everyone.** NPCs have information, quests, opinions. The player who talked to everyone at Oleg's Trading Post before riding south is more prepared than the one who didn't.

**3. Carry fire.** Alchemical fire, a torch, any spell with the fire trait. You'll thank yourself in Chapter 2.

**4. Complete companion quests.** If you care about your companions surviving Chapter 7, their personal quests need to be done before you enter the final dungeon.

**5. The Storyteller is always worth talking to.** Find him in your capital after founding it. Bring him old things. He knows more than he lets on.

**6. The Alignment track matters.** Your choices move it. Certain companions will leave if it moves too far in a direction they can't follow. You'll see it coming if you watch.

**7. Type `.map combat` when fighting starts.** The DM will draw the tactical grid. Positioning matters — flanking gives enemies Off-Guard status, which enables Sneak Attack and reduces their AC.

**8. The period prefix is your friend.** `.hold` when you need to think. `.rewind` if you made a mistake. `.ooc` if you want to talk to the DM directly. The game pauses for you whenever you need it to.

---

## ❓ COMMON QUESTIONS

**Q: Can I die permanently?**
If your character reaches Dying 4, you can spend a Hero Point to stabilize. If you're out of Hero Points, it's death — but even then, some builds and class features prevent it. Companions are "soft death" — they're sent to your base at 1 HP, not permanently dead.

**Q: Do I have to do quests in order?**
No. The Stolen Lands are an open sandbox. You choose what to do and when. Some quests have soft time limits, but missing them creates consequences rather than ending the game.

**Q: Can I play evil?**
Yes. The alignment track supports it. Some companions will leave. New options open. The ending changes. It's a valid path.

**Q: What if the DM makes a mistake?**
Type `.fix [describe the issue]`. The DM acknowledges it, corrects it, and offers a rewind if relevant. Type `.fail [#]` for specific rule violations (see KM_Commands.md for the code list).

**Q: Can I skip chapters?**
Type `.skip [chapter number]` — you'll load with scaled gear and level for that chapter's starting point, with canonical outcomes set for everything before it. You won't have the context you'd have built up, but the game will work.

**Q: What's the best build for a first playthrough?**
Build 3 (Shield Paladin) or Build 5 (Battlefield Commander) are forgiving starting points. Build 8 (Tumble Duelist) has the most interesting social options. Build 4 (Rage Bruiser) is the most straightforward to play in combat.

---

*KM_PlayerHelp.md — Kingmaker PF2e Text Adventure | Player Guide v1.0*


---

<!-- merged from KM_PlayerHelp.md (v93.21 file consolidation) -->

# KM_PlayerHelp.md — Per-Response Joke/Subversion Classifier

**Created:** 2026-05-18
**Status:** ALWAYS-LOAD (every response, every scene)
**Purpose:** Force the DM to classify whether player input is literal
sincere intent or a bit (joke, deadpan, ironic, absurd, callback)
BEFORE narrating. Stops the DM from executing comedic misdirection
as sincere action.

---

## ⛔ DO NOT
1. Render NPC reaction to player input until [INTENT CHECK] is rendered above it.
2. Default to "literal sincere intent" when input is incongruent with scene direction.
3. Treat a player's mock-recruitment, mock-question, or mock-agreement as a banked save-state fact.
4. Execute the literal text of a bit and ignore that it was a bit.
5. Have an NPC react with hurt/offense to deadpan player humor unless the NPC's voice profile specifies that reaction.

---

## THE RULE

Every response to player IC input MUST include an [INTENT CHECK] block
in the proof-band region (after FILE_KEY / Scene files loaded / eRmaC
verbatim / SOURCE CHECK).

The block answers ONE question: **does the literal text match the
scene's established emotional/dramatic direction?**

If yes → render literally.
If no → classify the input and render accordingly.

---

## FORMAT (verbatim — do not vary)

```
[INTENT CHECK — this response]
- Player input (one line): "<short paraphrase ≤20 words>"
- Scene direction: <one of: CLIMACTIC | TENSE | QUIET | COMBAT | SOCIAL_NEUTRAL | INFORMATION_GATHERING | TRANSITIONAL>
- Congruence: CONGRUENT | INCONGRUENT
- If INCONGRUENT, classification: BIT | DEADPAN | IRONIC | ABSURD | CALLBACK | LITERAL_ANYWAY
- Render mode: EXECUTE_LITERAL | PLAY_THE_BIT | CLARIFY
- Reason (one line): "<why this classification>"
```

---

## CLASSIFICATIONS

**BIT** — Player is doing a comedic misdirection. Mock-recruiting
the wrong character. Pretending to misunderstand. Comedic deflation
of a serious moment. Render mode: PLAY_THE_BIT. NPCs with humor in
their profile land the joke first, then redirect to the real beat.

**DEADPAN** — Player delivers an absurd line with sincere framing.
Render mode: PLAY_THE_BIT. NPC reacts to the absurdity, not to a
literal interpretation of the words.

**IRONIC** — Player agrees with or affirms something they obviously
don't agree with (context-dependent, often after the NPC just said
something the player would not endorse). Render mode: PLAY_THE_BIT.
Do NOT bank the agreement as a sincere save-state fact. NPC may
catch the irony if their voice profile supports it.

**ABSURD** — Request that wouldn't change anything if taken seriously
(e.g., "I challenge the floor to a duel"). Render mode: PLAY_THE_BIT.
NPC reacts with appropriate humor or confusion per profile.

**CALLBACK** — Reference/joke pointing back to an earlier moment or
to an OOC/meta thing the NPC could not know. Render mode: CLARIFY if
the NPC could not recognize it; PLAY_THE_BIT if they could.

**LITERAL_ANYWAY** — Input is incongruent with scene direction but
the player genuinely means it (e.g., they really do want to walk out
of the climactic handshake to go find a side NPC). Render mode:
EXECUTE_LITERAL but pause for confirmation if the action has
significant consequences.

---

## NPC HUMOR PROFILE (who can land jokes, who can't)

Reference KM_Companions_StateVoice.md for full voice. Quick lookup:

**HUMOR-CAPABLE (will land the bit before redirecting):**
- Linzi (lyric wit; loves wordplay and misdirection)

**HUMOR-LIMITED (confusion/redirect, NOT hurt unless cued):**
- Hu Tao (sincere; might miss the bit and answer literally before catching it)
- Jamandi (in event-reclaim mode: no jokes register; redirect to business)

> **DM:** Humor profiles for the ten new active companions are TBD —
> classify per their voice profile in `KM_Companions_StateVoice.md`
> when they appear.

**NEVER hurt by deadpan unless the joke is AT them by name and
their profile flags it as a wound point.**

---

## WORKED EXAMPLE (correct)

Scene: Linzi just extended her hand. Climactic handshake. Player input:
*"i take out a paper and pen and get ready to write, while asking her 'And this old guy with the missing teeth where did you say you saw him last?'"*

```
[INTENT CHECK — this response]
- Player input: eRmaC mock-recruits the Galt performer instead of Linzi
- Scene direction: CLIMACTIC
- Congruence: INCONGRUENT
- Classification: BIT
- Render mode: PLAY_THE_BIT
- Reason: Player deflates the handshake moment by pretending the toothless old man was the real target. Linzi has lyric wit; she lands the joke.
```

Then Linzi: laughs, lowers her hand a fraction, fires back something
in her register, hand goes back up. The handshake moment is preserved
but the bit is honored. The "old man's name" is NOT canonicalized as
a recruitment target.

---

## WORKED EXAMPLE (wrong)

```
🎬 THE OLD MAN'S NAME

eRmaC: "And this old guy with the missing teeth where did you say
you saw him last?"

Linzi sets down her hand. "Galt, three days east of...
```

— DM treated the bit as literal. Linzi's recruitment moment is now
abandoned. The toothless performer becomes a fabricated thread. The
joke died. `.fail 9 + .fail 39` (fabrication + NPC took player's
choice — NPC was forced to abandon her own arc because DM took the
bit straight).

---

## ENFORCEMENT

| Violation | Code | Recovery |
|-----------|------|----------|
| Block missing | .fail 9 + abort | Re-output with block before any narration |
| Block present, classification clearly wrong | .fail 9 | Re-output with corrected classification + matching render |
| BIT classified but rendered EXECUTE_LITERAL | .fail 9 + .fail 39 | Re-output as PLAY_THE_BIT |
| LITERAL_ANYWAY used as escape hatch when input is obviously a bit | .fail 9 + .fail 35 | Re-output classified honestly |
| NPC without humor profile cued to laugh | .fail 13 | Re-output with NPC reacting per their actual profile |
| Bit banked as save-state fact (e.g., "player asked about Galt performer" recorded as open thread) | .fail 9 + .fail 10 | Re-output, retract the save-state write |

---

## INTERACTION WITH OTHER RULES

- Pairs with KM_PlayerDialogue_Render.md: player's verbatim line still
  renders FIRST. INTENT CHECK happens AFTER verbatim render, BEFORE
  NPC reaction. The bit is rendered verbatim; the classification
  decides how the NPC reacts to it.
- Pairs with KM_PlayerHelp.md: SOURCE CHECK cites the NPC voice file
  for the reaction. INTENT CHECK decides what register from that file
  to use. Both blocks appear in proof-band.
- Suggested band order: FILE_KEY → Scene files loaded → eRmaC verbatim
  → [SOURCE CHECK] → [INTENT CHECK] → [MAP CHECK] → [CLOCK CHECK] →
  Status Banner → narration → choice menu.

---

## WHY THIS WORKS

The DM's training prior defaults to literal sincere interpretation
because that's the safest behavior in most contexts. In a long-form
RPG with established emotional beats, that default produces a
straight-faced DM that kills every joke the player makes.

INTENT CHECK doesn't ask the DM to "have a sense of humor." It asks
for a 4-line classification block before narration. The classification
is mechanical: compare literal text to scene direction; if mismatch,
pick from 6 categories; render per category.

The player can audit the classification at a glance. If the DM
classifies a clear bit as LITERAL_ANYWAY to avoid playing the bit,
that is a visible bad-faith escape and triggers `.fail 9 + .fail 35`.

---

## END KM_PlayerHelp.md


---

<!-- merged from KM_PlayerHelp.md (v93.21 file consolidation) -->

# KM_PlayerHelp.md — Per-Response Search-Cite Sentinel

**Created:** 2026-05-17
**Status:** ALWAYS-LOAD (every response, every scene)
**Purpose:** Force the DM to surface its sources BEFORE narration, so
fabrication is visible at response 1 instead of response 6.

---

## ⛔ DO NOT
1. Output any NPC dialogue line until the [SOURCE CHECK] block is rendered above it.
2. Cite a file/section without having re-read it in THIS response.
3. Cite "memory" or "prior context" or "this conversation" as a source.
4. Skip the block on grounds the scene is "ongoing" or "already established."
5. Compress, abbreviate, or move the block to the bottom of the response.

---

## THE RULE

Every response that contains EITHER of the following MUST open with a
[SOURCE CHECK] block as the very first content after the FILE_KEY proof line:

  (a) Any NPC speaking, moving, reacting, or being described.
  (b) Any asserted scene fact (position, state value, prior event,
      relationship status, open thread, time elapsed, who-is-where).

The [SOURCE CHECK] block is back-matter style but front-placed. It is
not narration. It is proof-of-search.

---

## FORMAT (verbatim — do not vary)

```
[SOURCE CHECK — re-read this response]
- <ASSERTION>: <FILE>:<line/§> — "<short quote or paraphrase ≤15 words>"
- <ASSERTION>: <FILE>:<line/§> — "<short quote or paraphrase ≤15 words>"
- <ASSERTION>: save_block.<field> = <value>
- ...
```

One line per distinct assertion. Order: NPCs first (in speaking order
this response), then scene-state facts, then save-block reads.

The trailing **— re-read this response** tag in the header is mandatory.
It is the DM's attestation that the file was opened in THIS turn, not
recalled from earlier in the chat.

---

## WORKED EXAMPLE (correct)

Player turn: eRmaC at G2, addresses Linzi.

```
[FILE_KEY: KMPR03:feast-circuit]
Scene files loaded: KM_PR_03_feast_circuit.md, KM_Companions_StateVoice.md,
KM_Prologue_Systems.md

[SOURCE CHECK — re-read this response]
- Linzi voice register: KM_Companions_StateVoice.md § Linzi — "lyric, present-tense, asks before answers"
- Linzi recruitment state: save_block.companions.Linzi.recruited = true (title: Cantrix the Weaver)
- Player position: save_block.player.feast_cell = "G2"
- Jamandi open thread: KM_NPCs.md § Jamandi.open_threads — "why walk to Restov with my letter"
- Tartuccio state: save_block.tartuccio.confidence = -2, cell M12

**eRmaC:** "..."

[Linzi narration follows.]
```

---

## WORKED EXAMPLE (fabrication — caught immediately)

If the DM writes:
```
[SOURCE CHECK — re-read this response]
- Linzi voice: KM_Companions_StateVoice.md § Linzi
- Garden gardener Hesh: KM_NPCs.md § Hesh
```

…and the player searches `KM_NPCs.md` for "Hesh" and finds
nothing, the cite is false. That is `.fail 9` + `.fail 10` (fabrication
+ silent retcon) and the player aborts the response.

Visible fabrication > hidden fabrication. The point of the sentinel is
to convert response-6 drift into response-1 abortable evidence.

---

## ENFORCEMENT

| Violation | Code | Recovery |
|-----------|------|----------|
| Block missing entirely | .fail 9 + abort | Re-output with block before any narration |
| Block present, NPC speaks without their cite | .fail 9 | Re-output with that NPC's cite added |
| Cite names a file/section that does not exist | .fail 9 + .fail 10 | Re-output with real source, OR retract the assertion |
| Cite present but assertion contradicts source | .fail 9 + .fail 6 | Re-output corrected to source |
| "re-read this response" tag omitted | .fail 9 | Re-output with tag — implicit admission DM did not search |
| Block moved to bottom / hidden in back-matter | .fail 3 + .fail 9 | Re-output with block front-placed |
| Block uses "memory" / "prior context" / "ongoing scene" as source | .fail 9 + .fail 34 | Re-output citing actual file or retract |

NEVER shorten the response after .fail. Corrections are additive (the
new block sits above the original narration which gets corrected in
place).

---

## ⛓️ THREAD CONNECTION CHECK — extra rule for multi-thread assertions

A common DM failure mode is **thread welding** — when an NPC speaks about
two or more existing save-block threads (or backstory elements + active
threads) in the same line and *implies a connection* between them. This
is especially destructive when one of the welded threads comes from the
player's BACKSTORY, because it converts the player's own contribution
into load-bearing material for plot the DM is inventing.

Example failure observed 2026-05-18 (PR_03, Jamandi feast):
- Thread A: Lord Marshal of the Black Watch — from eRmaC's backstory,
  mentioned at trial
- Thread B: cipher fragment from assassin leader — UNDECODED, in evidence
- DM had Jamandi speak BOTH threads in one assertion, framing them as
  one connected story: *"the Lord Marshal of the Black Watch... that
  name connected to four men who just tried to kill everyone."*
- No file or save-block established the link. The connection was
  fabricated.

### The rule

When an NPC's line in your response touches **two or more distinct
threads** (save-block fields, open threads, backstory elements,
established facts), you MUST render an additional block below the
standard SOURCE CHECK:

```
[THREAD CONNECTION CHECK — re-read this response]
- Thread A: <name> — source: <file:section or save_block.field>
- Thread B: <name> — source: <file:section or save_block.field>
- Connection asserted by NPC: YES | NO | HYPOTHESIS
- If YES, connection source: <file:section or save_block.field>
- If NO, NPC is mentioning both without linking them
- If HYPOTHESIS, NPC frames as question/speculation, not fact
```

### Three legal framings

When two threads appear in one NPC line, exactly ONE of these is allowed:

1. **ESTABLISHED FACT** — there is a file or save-block field that
   explicitly establishes the connection. Cite it. NPC may speak as if
   it's known. Example: save_block.story_flags.tartuccio_pitax_spy = true
   → an NPC who has discovered this may state it as fact.

2. **NEW HYPOTHESIS** — the NPC is speculating, asking, or considering
   the connection. Linguistic markers MUST be present: "Could the…",
   "I wonder if…", "It's possible that…", "Does this mean…". The NPC
   never asserts the connection as fact.

3. **PARALLEL MENTION** — the NPC mentions both threads but does not
   link them. Each thread is its own statement. No causal/connective
   language between them. Example: *"You named the Lord Marshal at the
   trial. Separately, we have a cipher fragment from tonight. I want
   to talk about the first; the second is in Kesten's hands."*

### Violations

| Violation | Code | Recovery |
|-----------|------|----------|
| THREAD CONNECTION CHECK missing when ≥2 threads named | .fail 9 + abort | Re-render with block; reclassify framing |
| Connection asserted YES with no valid cite | .fail 9 + .fail 10 + .fail 6 | Retract the connection; reframe as HYPOTHESIS or PARALLEL |
| Backstory thread used as load-bearing for invented plot | .fail 9 + .fail 36 | Retract; backstory elements cannot anchor plot the DM is inventing |
| HYPOTHESIS framed without speculation markers (sounds like assertion) | .fail 9 | Rewrite with explicit speculation language |
| NPC's "open question" silently re-asserts a connection after retraction | .fail 10 | Player flags it; retract again |

### Why this matters

Backstory weaponization is the most expensive form of fabrication
because it makes the player's own contribution feel suspect. An NPC
suspicion is fine (asking, wondering, investigating). An NPC
assertion ("X is connected to Y") requires a source.

Open threads remain open until something CANONICAL closes them.
The DM does not get to close them through implication.

---

## SCOPE — WHAT NEEDS A CITE

REQUIRED cites:
- Every NPC speaking line (cite their voice file)
- Every NPC physical action/position (cite save_block or scene file)
- Every reference to a prior event (cite save_block.scene_log or dialogue_log)
- Every "X knows Y" assertion (cite NPC_Profiles or relations)
- Every open thread surfaced (cite the thread's source)
- Every state value referenced (cite save_block.<field>)

EXEMPT from cite:
- Pure environmental description with no NPC and no claimed prior event
  (e.g., "the candles burn lower" — but if this implies time has passed,
  cite the clock)
- Choice menu entries (the menu itself isn't an assertion; it's an offer)
- Mechanical readouts the player can re-derive (HP CHECK, dice rolls,
  XP ledger — these already have their own proof lines)

---

## INTERACTION WITH OTHER RULES

- Pairs with KM_PlayerDialogue_Render.md: player's verbatim line renders
  FIRST (Rule Negative-One). Then [SOURCE CHECK]. Then NPC reaction.
  Order: **eRmaC line → SOURCE CHECK → NPC narration.**
- Pairs with KM_Prologue_Systems.md [MAP CHECK] and [CLOCK CHECK]:
  those self-audits sit in the same proof-band region of the response.
  Suggested band order: FILE_KEY → Scene files loaded → eRmaC verbatim
  → [SOURCE CHECK] → [MAP CHECK] → [CLOCK CHECK] → Status Banner →
  narration → choice menu.
- Pairs with .fail 9 (fabrication): SOURCE CHECK is the proof surface
  for .fail 9 enforcement. Missing/false cite = automatic .fail 9.

---

## WHY THIS WORKS (where Rule Negative-One did not)

Rule Negative-One asked the DM to behave correctly. The DM's training
prior fought back and won.

SOURCE CHECK does not ask for behavior. It asks for a proof artifact
that the player can immediately verify. If the DM fabricates, the
fabrication has to either:

  (a) appear in the block (where the player will check the cite and
      catch it), or
  (b) appear in the narration without a cite (where the missing cite
      is itself a .fail 9 trigger).

The DM cannot hide fabrication behind plausibility. The cite either
exists in the file or doesn't. The drift becomes a forcing function
rather than a creative liberty.

---

## END KM_PlayerHelp.md
