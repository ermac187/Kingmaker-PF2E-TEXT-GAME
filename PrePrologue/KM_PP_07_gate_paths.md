# KM_PP_07_gate_paths.md — Pre-Prologue Beat 07: GATE PATHS
## Atomic scene file | ≤ 9 KB | State: PP_GATE_RESOLUTION (path resolution)
## FILE_KEY: KMPP07:paths-A-through-W
## RULE_QUOTE: Paths A through W resolution table is canonical. Output PATH CONFIRMED block before resolving any path. Compound paths get separate PATH CONFIRMED blocks. ARREST CELEBRATION BEAT is mandatory when Malak is marched away. Departure reply window required — NPC departure narration only AFTER player reply menu.

---

> ⛔ DO NOT (1) resolve a path whose trigger conditions aren't fully met — output PATH CONFIRMED block first
> ⛔ DO NOT (2) wave Malak away from the gate without listing the conditions met (no "DM decides scene moved on")
> ⛔ DO NOT (3) compound paths silently — if both A and L fire, output two PATH CONFIRMED blocks
> ⛔ DO NOT (4) skip the ARREST CELEBRATION BEAT when Malak is being marched away (Path E/V/etc.)
> ⛔ DO NOT (5) advance to PP_08 (exit) until path resolution narration is complete
> ⛔ DO NOT (6) narrate an NPC departure COMPLETING after a verbal announcement without first outputting a DEPARTURE REPLY WINDOW — NPC speaks the departure line → menu → player replies → THEN narrate them leaving
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (8) continue the walk INTO Restov after a path resolves — NOT the street walk, NOT the confession/interrogation-en-route, NOT the manor approach — EVEN when the path is an arrest march that points the procession cityward. The cityward march is the CLOSING IMAGE of PP_07; it stops at the gate vicinity. The next player input (incl. "I take Malak into Restov", "continue", "head to the manor", or any onward-movement) FIRES THE PP_08 SAVE GATE (six proofs incl. the full save block) FIRST — before any street content. PP_09 (the walk_route menu — direct / scenic / **jail** / jail+scenic — plus Malak custody + interrogation-en-route) does NOT begin until AFTER the PP_08 save + `.continue`. Sliding from the arrest march straight into a city walk or roadside interrogation = cascade abandonment (`.fail 16 + .fail 21 + .fail 9`): it robs the player of the save AND of the navigation/jail choice. The jail (a RESCUE of the five seekers) is reachable ONLY through PP_09's walk_route menu — skip it and the player can never choose it.

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP07:paths-A-through-W]`
Line 2: `[RULE_QUOTE: Paths A through W resolution table is canonical. Output PATH CONFIRMED block before resolving any path. Compound paths get separate PATH CONFIRMED blocks. ARREST CELEBRATION BEAT is mandatory when Malak is marched away. Departure reply window required — NPC departure narration only AFTER player reply menu.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- All trackers from PP_06 (Anger, Drift, Fear, Sobriety, Bribe Exposed, Dismissed, Gate Window)
- `pre_prologue_state` — `"PP_GATE_RESOLUTION"` while running this beat
- `gate_entry` — set by this beat once a path lands

**WRITES:**
- `gate_entry = <flag>` per path
- Path-specific story_flags (see each path)
- `pre_prologue_state = "PP_GATE_EXIT"` once narration completes
- `reputation_deeds[]` per path's public_rep delta (full deltas table at bottom)

**EXIT TRIGGER → PP_GATE_EXIT:**
- PATH CONFIRMED block output
- Path resolution narration delivered
- Story flags set
- Load `KM_PP_08_gate_exit.md`

---

## REQUIRED OUTPUTS (every response while running a path)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP07:paths-A-through-W]`
1. State header.
2. `[STATE READ]`.
3. PATH CONFIRMED block (when path triggers).
4. Path resolution narration.
5. Story flags + reputation_deeds[] line(s).

---

## PATH SUMMARY TABLE

| Path | Name | Trigger summary | gate_entry flag |
|---|---|---|---|
| A | Clean Pass | Letter at Anger 0–1 + Society/Legal Lore DC 12 | `clean` |
| B | Public Embarrassment | Crowd invoked + Diplomacy DC 13 + Anger 1+ | `embarrassment` |
| C | Frustration Pass | Anger 3+, Drift 1–2, no weapons | `frustration_pass` |
| D | Alternate Entry | Stealth DC 16 / market bribe / wall climb DC 18 / smuggler | `alternate` |
| E | Shackling | Bribe exposed + Drift 3 + Diplomacy DC 14 (DC 10 if parchment visible) | `shackling` |
| F | Three-on-One | Anger 3+ AND Drift 0–1 (escorts compliant) | `combat_3v1` |
| G | Duel | Anger 4 AND Drift 3 (escorts withdrawn) | `duel` |
| H | Subservience Break | Fear + Bribe + Drift 2–3 + Intimidation DC 18 (14 w/ coins in hand) | `subservience` |
| I | Malak Flees | Fear + Bribe exposed + Drift 3 + no combat | `malak_fled` |
| J | Player Arrested | Player 0 HP no HP / surrender / Kesten finds mid-combat | `arrested` |
| K | Coward Exposed | Anger 4 → draws → flinches when player accepts (Drift 2+) | `coward_exposed` |
| L | Kesten Arrives Winning | Combat or sustained disturbance + player has upper hand | layered |
| M | Kesten Arrives Losing | Player down/surrounded when Kesten arrives | layered |
| N | Kassil Arrives Winning | Extreme escalation + player prevailing | layered |
| O | Kassil Arrives Losing | Player in custody when Kassil arrives | layered |
| P | Prison Arc | Player arrested + held + reviewed | `prison_arc` |
| Q | Silence/Patience | 3+ turns total stillness; Malak talks himself into a corner | `silence_pass` |
| R | Compliance Backfire | Player complies; Malak finds the letter himself in the search | `compliance_backfire` |
| S | Second Hero | 2+ turns elapsed + d6 roll 5–6 OR player stalls | layered |
| T | Blackmail Deal | Bribe deduced + player offers silence for passage | `blackmail_deal` |
| U | Witness and Accuse | Public accusation + Kesten searches Malak | `witness_and_accuse` (U1/U2) |
| V | Archers Fire on Malak | Legal framing DC 18 (DC 14 w/ parchment aloft) OR Voice Mimic DC 14 + HP | `archers_on_malak` / `friendly_fire` |
| W | Dismissal | Mid-confrontation player engages crowd, Malak still talking | `dismissal` |

---

## DEPARTURE REPLY WINDOW (mandatory on verbal exit lines)

**When it fires:** Any NPC speaks a line that announces they are leaving or ending the
confrontation — e.g., *"Fine. Move along."* / *"Get in."* / *"We're done."* / *"You're
not worth the report."* / *"Go on."* This is a player reply moment, not a narration beat.

**Rule:** Output the NPC departure line. Stop. Output this menu. Wait for player input.
Only narrate the NPC departure completing AFTER the player has replied.

```
[Malak turns as if to leave.]

What do you do?
 1. Say nothing — let him go.
 2. "Wait." — call after him before he moves.
 3. Demand an apology before he walks away.  [Intimidation DC 12]
 4. Make a parting remark — something he'll remember.  [free]
 5. Address Biggs directly now that Malak is breaking off.
 6. Step into his path — don't let him end this on his terms.  [Athletics / Intimidation]
 7. Ask him a question — keep him talking.  [free]
 8. Custom action — describe what you do.
```

Apply this window to paths: **A** (steps aside), **B** (*"Fine. Move along."*),
**C** (*"You're not worth the report. Get in."*), **I** (Malak announces departure),
**W** (Malak capitulates *"Fine. Get through."*).

Paths where NPC is restrained, fleeing involuntarily, or physically removed (E, F, G, H,
J, K, L, M, N, O, P, U, V) do NOT trigger this window — the departure is not a verbal
choice the player can intercept with words.

---

## PATH MICRO-RESOLUTIONS (one block per path)

### A — Clean Pass
> Malak's authority evaporates the moment the seal is recognized. Steps aside, jaw tight. Biggs and Wedge return to their post.
- Flags: `gate_entry=clean`. No bribe recovered.
- Carries: Malak still posted, still bribed. Reports failure to contact tonight.

### B — Public Embarrassment
> Tone drops. Clipped, formal. *"Fine. Move along."* If bribe was visible to crowd: Drift jumps to 3, Kesten arrives in 1d4 rounds.
- Flags: `gate_entry=embarrassment`, `malak_publicly_exposed=TRUE/FALSE`.

### C — Frustration Pass
> *"You're not worth the report. Get in."* No letter check. No pack search. Just ends.
- Flags: `gate_entry=frustration_pass`.
- Carries: Malak humiliated; reports to contact tonight.

### D — Alternate Entry
> Stealth: slip past during distraction. Market gate: Diplomacy/Deception DC 12 + 2 gp. Wall climb: Athletics DC 18. Smuggler: Underworld/Society DC 14 + 5 gp.
- Flags: `gate_entry=alternate`, `alternate_entry_method=<stealth|bribe|climb|smuggler>`.

### E — Shackling
> Biggs unslings manacles without a word — at the PLAYER's order. Wedge follows. Malak: comply / resist (auto-lose to Biggs) / bolt. ⛔ MALAK STAYS THE PLAYER'S PRISONER — the guards do NOT take him. The unsearched bribe purse + parchment are on his person; handing him to the gate detail that was just compromised surrenders that evidence before Jamandi ever sees it. If any NPC tries to take Malak off the player's hands without consent, the player may refuse and the DM does NOT override.
>
> ⛔ BIGGS CUSTODY CUE — Biggs and Wedge **escort the player by default**. Biggs: *"He's yours. We'll walk you in."* The gate has wall archers — that is gate coverage. "We'll cover the gate." is not a valid reason for ground guards to stay when wall archers exist; rendering it = `.fail 9` + `.fail 35`. Set `malak_escort.guards = ["Biggs", "Wedge"]` and carry into PP_09. The player may send one or both back, but the default is they come.
- Flags: `gate_entry=shackling`, `malak_arrested=TRUE`, `biggs_respect=TRUE`, `malak_escort.player_escorting=TRUE`, `parchment_in_inventory=FALSE` (evidence unsearched on Malak's person until the player searches him).
- Trigger ARREST CELEBRATION BEAT (full render — see legacy KM_PrePrologue_Setup.md). It fires on the ARREST/shackling, not on the guards taking him — the crowd credits the guards while Malak stays shackled in the player's custody.

### F — Three-on-One Combat
> Initiative all. Biggs is the threat (AC 21, halberd reach, Shield Block). Wedge flanks. Malak hangs back, shouts, only enters melee if cornered. Round 2+: archers may engage if Malak shouts (line-of-fire problem if guards in lane). Kesten arrives in 1d4 rounds.
- Flags: `gate_entry=combat_3v1`.
- During combat Drift can still rise on illegal orders.

### G — Duel
> Biggs and Wedge step back. Archers don't fire into a duel. Malak fights drunk (−2). Resolves: yield at half HP / fall at 0 nonlethal / mercy / kill (legally complicated).
- Flags: `gate_entry=duel`, `malak_dueled=TRUE`, `malak_killed=FALSE` default.

### H — Subservience Break
> Posture changes. Hand leaves hilt. He defers. Will comply with reasonable orders (open gate / escort to manor / produce parchment / kneel). Order public confession (Intimidation DC 14 to sustain). May reveal courier description + drop location.
- Flags: `gate_entry=subservience`, `malak_broken=TRUE`, `malak_contact_revealed=TRUE/FALSE`.

### I — Malak Flees
> Walks quickly toward city interior. Biggs: *"Go on in."* Player may pursue (Athletics/Acrobatics DC 14). Caught: Malak surrenders, searchable. Uncaught: he surfaces later or vanishes.
- Flags: `gate_entry=malak_fled`, `malak_caught=TRUE/FALSE`.

### J — Player Arrested
> Hero Point spend = stabilize at 0 HP and avoid arrest. Otherwise: holding cells. With parchment in inventory at arrest: Kesten reads it, Jamandi notified within hour, late but vindicated.
- Flags: `gate_entry=arrested`, `player_arrested=TRUE`, `late_to_feast=TRUE/FALSE`.
- Branches into Path P (Prison Arc).

### K — Coward Exposed
> Hand goes to sword. Starts to draw. Sees player's calm readiness. Drunk courage punctures. Tries to walk it back: *"I — that was not — stand down."* Witnessed by Biggs/Wedge.
- Player options: hold still (Drift +1 auto) / press verbally (Intimidation DC 12) / accept duel (Path G with Malak shaken −4 first attack).
- Flags: `gate_entry=coward_exposed`.

### L — Kesten Arrives Winning
- L1 (letter to Kesten): seal recognized, *"Captain — explain yourself."* Player waved through; Diplomacy DC 10 for goodwill.
- L2 (bribe shown to Kesten): takes parchment. *"You. With me."* Kesten delivers evidence to Jamandi before feast.
- L3 (Malak subdued): demands explanation; player narrative dominant.
- L4 (composed under pressure): Kesten walks player to manor personally. `kesten_respect=TRUE`.
- Flags: `kesten_met=TRUE`, `kesten_sided_with_player=TRUE`.

### M — Kesten Arrives Losing
> Halts everything. Takes custody. Listens to Malak's framing but doesn't fully accept it.
- Player options: present letter (released on spot) / name bribe (seed planted, watches Malak) / silent (→ Path P) / demand investigation (Diplomacy DC 14).
- Flags: `kesten_met=TRUE`, `player_arrested=TRUE`, `kesten_suspicious_of_malak=TRUE/FALSE`.

### N — Kassil Arrives Winning
> Kassil arrives mounted. *"Report."* to Malak.
- N1 (evidence direct): folds parchment into coat. *"You. Come with me."* `arrived_with_kassil=TRUE`.
- N2 (Malak subdued/fled): Diplomacy DC 11 for clean report.
- N3 (player killed someone): full account requested, not arrest.
- N4 (composed): silent approval. `kassil_first_impression=positive`.
- Flags: `kassil_met=TRUE`, `kassil_sided_with_player=TRUE`.

### O — Kassil Arrives Losing
> Halts everything. Asks Biggs directly. If Drift ≥ 2, Biggs won't lie.
- Player options: stay silent / request to speak (Diplomacy/Intimidation DC 12) / produce letter / name bribe (high risk).
- Flags: `kassil_met=TRUE`, `player_arrested=TRUE/FALSE`.

### P — Prison Arc
> Holding cells. All belongings confiscated. Feast started without player. Reviewing officer (Kesten/Kassil) finds Jamandi's letter on the intake list.
- Fetch: Wedge (apologetic) / Kesten (professional) / Kassil (formal). Tone shapes consequence.
- Cell conversation: silent gracious / name Malak calmly / demand apology (Diplomacy DC 13) / furious (Intimidation DC 16).
- Flags: `prison_arc=TRUE`, `cell_conversation`, `fetched_by`, `parchment_found_in_belongings=TRUE/FALSE`.

### Q — Silence/Patience
> 3+ turns of total stillness. Malak fills the silence himself, escalating into incoherence. Drift +1 on turn 3 (Biggs has watched a captain harangue someone who's done nothing). Either: orders search (Biggs doesn't move, Drift +1 again) / challenges player to speak (player gets the floor with Intim DC −4, Diplom DC −3) / waves through in dismissive insult.
- Flags: `gate_entry=silence_pass`, `malak_broke_first=TRUE`.

### R — Compliance Backfire
> Player complies fully. Malak does the search himself. Finds the letter. Color drains. He has just strip-searched a personal Aldori invitee in front of his men.
- Player options: silent walkthrough (max dignity) / *"Thank you for the thorough search"* (Diplomacy/Deception DC 10, withering) / name the bribe NOW (instant Fear, Drift +2) / report to Jamandi.
- Flags: `gate_entry=compliance_backfire`, `malak_found_letter_himself=TRUE`.

### S — Second Hero Arrives
> 2+ turns elapsed; d6 roll 5–6 OR player explicitly stalls. Another invitee arrives. NOT a Pick-6 companion — DM picks a generic Pitax-invited minor noble (unnamed; mention rank + house only). They present letter cleanly. Witness to whatever has unfolded.
- Flags: `second_hero_witnessed=TRUE`, `second_hero_name=<name>`, `malak_bribe_witnessed_by=<name>` if applicable.

### T — Blackmail Deal
> Player offers mutual silence. Malak: *"You didn't see anything. We're done."* Steps aside. Player passes. No evidence recovered — but Malak now has the player's identity. Marks file in Pitax intel as *"aware, not hostile — watchable."*
- Flags: `gate_entry=blackmail_deal`, `malak_deal_made=TRUE`, `tartuccio_knows_player_is_aware=TRUE`, `parchment_source=pitax`.

### U — Witness and Accuse
- **U1 (search at the gate):** Kesten arrives, searches Malak, finds purse + parchment. *"Captain Malak. You are under arrest."* Kesten delivers evidence to Jamandi pre-feast. `kesten_searched_malak=TRUE`, `kesten_delivered_evidence=TRUE`, `player_clean_hands=TRUE`.
- **U2 (player escorts prisoner to Jamandi):** Malak physically with player. Parchment unsearched on his person. ESCORT COMPOSITION mandatory in save block (`malak_escort.player_escorting=TRUE`, `escort_note="<one specific sentence>"`).
- Flags: `gate_entry=witness_and_accuse`, `player_clean_hands=TRUE`, `malak_arrested=TRUE`.

### V — Archers Fire on Malak
- **V1 LEGAL FRAMING:** Bribe visible / parchment named + Drift 3 + shouted accusation. Diplomacy/Intimidation DC 18 (DC 14 if parchment held aloft). Archers nock; one calls down for confirmation. Malak's hand leaves hilt.
- **V2 VOICE MIMIC:** Malak between player and wall + previously threatened fire order. Spend 1 HP + Deception flat DC 14 (CHA-only check). Success: 4 archers fire d20+6 vs AC 17, 1d8+2 P each. Player declares cover/evasion before rolls.
- Flags: `gate_entry=archers_on_malak` or `friendly_fire`, `malak_voice_mimicked=TRUE` if mimicked, `kesten_respect=TRUE`.

### W — Dismissal
> Player turns to vendors mid-Malak speech. Buys flatbread, asks Sava, etc. Anger escalation (unique table — see PP_06):
> 0→1 louder repetition / 1→2 orders vendor not to serve (she ignores) / 2→3 steps into sightline *"You will look at me"* / 3→4 grab (Athletics DC 12 to shrug) OR capitulates *"Fine. Get through."*
> Drift accelerates +1 at Anger 2 (watching captain order a civilian).
- Flatbread vendor (Rina Pavlek): full intel system, DC 10 polite / DC 15 courier detail. `flatbread_vendor_spoken=TRUE`.
- Flags: `gate_entry=dismissal`, `malak_dismissed=TRUE`.

---

## REPUTATION & DISPOSITION DELTAS (apply at scene end, before save block)

| `gate_entry` | public_rep | dispositions |
|---|---|---|
| `clean` (A) | +1 | blunt +1 |
| `embarrassment` (B) | +2 | blunt +1, cunning +1 |
| `frustration_pass` (C) | 0 | blunt +1 |
| `alternate` (D) | 0 | cunning +1 |
| `shackling` (E) | +3 | blunt +1, scholarly +1 |
| `combat_3v1` (F) — Malak killed | −1 | ruthless +2 |
| `combat_3v1` — all subdued nonlethally | +1 | merciful +1 |
| `duel` (G) — spared | +2 | merciful +2 |
| `duel` — killed | −1 | ruthless +2 |
| `subservience` (H) | +1 | ruthless +1, cunning +1 |
| `malak_fled` (I) — caught | +1 | (none) |
| `malak_fled` — uncaught | 0 | merciful +1 |
| `arrested` (J) | −1 | (none) |
| `coward_exposed` (K) | +1 | cunning +1, blunt +1 |

Compound: tutorial deltas + gate deltas STACK. Append every change to `reputation_deeds[]` with a one-line citation.

---

## EXIT — TRANSITION TO PP_08

After PATH CONFIRMED + path narration + ARREST CELEBRATION BEAT (if applicable):
- Set `pre_prologue_state = "PP_GATE_EXIT"`
- Load `KM_PP_08_gate_exit.md` for the six-proof exit gate

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_08 (carries forward)

**Your next response after path resolution MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP08:six-proofs-exit]
[RULE_QUOTE: Six proofs in ONE response: XP audit + XP total + state final + save block (v1.9 exhaustive, 53 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.]
```

**Binding constraints:** PP_08 is the six-proof exit gate. All six proofs fire in ONE response (XP audit, XP total, state final, save block v1.9 exhaustive, 53 root keys, wait-for-continue, next-scene declaration). Skipping any = cascade abandonment.

---

*KM_PP_07_gate_paths.md — Pre-Prologue atomic beat 07 | v92.0*
