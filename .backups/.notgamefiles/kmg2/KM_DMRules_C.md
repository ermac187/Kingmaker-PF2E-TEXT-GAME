# KINGMAKER — DM RULES SUPPLEMENT C: FEAST CAROUSEL
## KM_DMRules_C.md | Pair-load with KM_DMRules.md during PR_03 (feast)

> Load this file alongside KM_DMRules.md whenever KM_PR_03_feast_circuit.md is active. All rules here extend the ACTIVE CONVERSATION LOCK section of KM_DMRules.md.

---

**QUEUE ARRIVAL — CAROUSEL PROTOCOL:** When the carousel queues the next companion and the player's current exchange is still open:
- The incoming companion arrives physically — finds a seat, settles in, accepts a drink — and joins the active conversation as a participant, not a bystander.
- They engage with the current exchange. At minimum one chime-in that responds to what is actually being discussed. They are not silent props waiting for their turn.
- They do NOT open their own thread while the current exchange is live. Their opener waits.
- When the player closes the current exchange: the incoming companion's opener fires in the SAME response. They are already seated — no gap, no "would you like to speak with [name]?" prompt.
- ⛔ The incoming companion may NOT redirect, override, or close the active exchange. They are guests in it until the player signals done.
- ⛔ Do NOT hold the incoming companion off-screen while they wait. They are physically present and participating from the moment the carousel queues them.

**EARSHOT PARTICIPATION — OPEN CHIME-IN:** Any companion within earshot may speak when the active exchange touches their lane, interest, wound, or expertise — regardless of carousel order, pool status, or whether they have had their own turn yet.

- **Within earshot** = at the player's table (Recruited) OR in the earshot ring: Engaged companions, crowd members in LEANING IN / COMMITTED states, any named companion standing within conversational range
- **BackOfQueue** companions have physically drifted away but may re-enter the earshot ring and chime in if something strongly hits their personal-stake lane — one strong trigger is enough to pull them back
- Chime-ins are brief (2–4 sentences), voiced in that companion's established register, and do NOT consume a carousel slot or advance any clock
- Player may respond, ignore, or redirect — each outcome updates that companion's interest state: substantive answer → LEANING IN or Engaged; ignored → cools one step
- ⛔ The active carousel exchange is NOT interrupted by a chime-in. The chime-in is a line from the perimeter. The active companion retains the floor until the player signals done.

**FEAST CAROUSEL — TARTUCCIO CROWD SWAY** *(supplement to KM_Prologue_Tartuccio.md — both loaded during PR_03)*

Three physical layers. Tartuccio targets each differently:
- **AT TABLE (Recruited)** — Declared companions. He cannot un-declare them; targets them to surface visible doubt in front of the committed, or plant second thoughts the player must then manage.
- **EARSHOT RING (Engaged + LEANING IN / COMMITTED crowd)** — His PRIMARY targets. Interested but not yet locked. A successful Frame here blocks a declaration. A successful Taint sends one drifting to BackOfQueue.
- **WIDER ROOM (BackOfQueue + LEANING OUT + ALIGNED ELSEWHERE)** — Ambient Taint only. Shaded remarks, public asides. Not direct engagement.

**Individual targeting — each interrupt picks ONE person, not a topic:**
1. Highest `feast_approval` in the earshot ring → Frame target. Knock the front-runner before they declare.
2. Companion whose wound or core need the player's last answer didn't fully address → Taint target. Name the gap quietly in that person's direction.
3. BackOfQueue companion still within range → ambient remark to the room, not addressed directly.

He targets their interests, not his own. That is what makes it effective and hard to expose.

**When Frame/Taint lands:** fire 1–2 ambient reactions from named companions — a posture shift, a glance exchanged, a cup set down without drinking. Declared companions don't un-declare but may go quiet or surface the seeded doubt as a follow-up question in their own next beat.

**Player counter:** Address the individual Tartuccio just targeted — not Tartuccio. Arguing with him directly burns the player's turn and lets his Frame settle silently on the seeded companion. Talking to the doubting companion directly bypasses the frame and forces him to recalculate. If the player argues with Tartuccio instead, the Frame still lands.

**TARTUCCIO POSITION — MANDATORY FEAST OUTPUT (every response):**
Every feast response includes a Tartuccio position line before the player menu. Must state: (1) his current location, (2) what he is visibly doing, (3) whether he is within earshot of the active exchange.

- *"Tartuccio is at his corner table — Imoen is laughing at something he said."*
- *"Tartuccio stands near the east column, drink in hand, not speaking. He is within earshot."*
- *"Tartuccio has drifted within two tables of yours, body angled toward your conversation."*

⛔ Earshot must be explicit. The player uses this to react — speak carefully, address him directly, or act on what he is doing. A missing position line makes him invisible between interrupts, which breaks the scene.

**⛔ TARTUCCIO CLOCK — DEFINITION AND ANTI-CONFUSION:**
`tartuccio_clock` = player turns completed since the last interrupt. It is NOT a cumulative feast_q sum. It is NOT a question count. There is no 4/8/12 threshold. That system does not exist in any current file — do not apply it.

Player turn = one Enter press. One companion conversation ≈ 4 player turns (intro, their questions, your questions, title/close). At the end of each player turn, check: turns since last interrupt ≥ interval for current Confidence (per KM_Prologue_Tartuccio.md § THE INTERRUPT LOOP cadence table) → Tartuccio steps over this response. feast_q values track per-companion approval only. They do not trigger Tartuccio.

Starting clock = 0. After an interrupt fires: clock resets to 0. Count turns from there.

---

## ⛔ FEAST POSITION SELECTION — STRATEGIC POSITIONING

**At PR_02's exit / PR_03's start, the player chooses where to stand or sit in the hall. The position determines: (1) earshot range — how many companions hear them, (2) Tartuccio's travel distance — how fast he can interrupt, (3) Tartuccio's eavesdrop fidelity on the player's table, (4) drift cadence modifier — how quickly companions arrive at the table. Each position is a real trade-off.**

**Reference grid (Banquet Hall Template 1, 15×15 — see KM_DMRules_B.md § HALL POSITION):**
- HEAD TABLE: row 2 (Jamandi H2, Kassil D2, Ezvanki L2)
- SEEKERS' CORNER: K10-M12 (Tartuccio M12, seekers s1-s5)
- WINE ALCOVE: B12-C13
- HEARTH: N5-N7
- MAIN DOOR: F15/I15 (Kesten posted G15/H15)
- CHAMPIONS: D6-F7 (player default E6)
- BALCONY: off-grid above row 1 (Jaethal observes)

**The positions — present as a numbered menu at PR_02 → PR_03 transition. Each has SHARP trade-offs; no two should feel interchangeable:**

```
🎭 CHOOSE YOUR FEAST POSITION — sharp trade-offs; no two are alike

1. 🛡️ CHAMPIONS (E6) — warrior cluster, military gravity
   + Warriors (Tika, Olivier, Artoria, Ryuko, Yoko): +1 approach speed
   + Kassil disp +1/turn (military respect)
   + Combat-build Diplomacy +1
   − Casters/scholars (Morrigan, Sucrose, Tatsumaki, Kyoko): −1 approach
   − Jamandi disp +0 (she reads "joined the soldiers, not the politics")
   − Tartuccio targets the warriors first while you cluster with them
   TRADE: warrior-recruitment specialist. Hostile to caster recruitment.
   ──────

2. 👑 HEAD TABLE (G2/I2) — standing alignment with host (NOT seated)
   + Jamandi disp +1/turn (court alignment); +1 more if you defend her
   + Kassil immediate; Linzi +1; Ezvanki within earshot
   + PR_09 political weight ×1.3 (your testimony carries)
   + Tartuccio CANNOT approach here (too public; he loses face trying)
   − Populists (Ryuko, Yoko, Tatsumaki, Tika): −2 approach (sycophant)
   − Morrigan refuses to approach while you're here (will meet elsewhere)
   − Earshot 2-sq only (head table Full; rest of hall cut off)
   TRADE: court politics maxed. Recruitment narrowed to court-tolerant.
   ──────

3. 🌑 WINE ALCOVE (C12) — privacy, depth, withdrawal
   + Morrigan +2 approach (preferred terrain); Sucrose +1 (shadow work)
   + All scored threads here get +2 disposition swing (private = honest)
   + Tartuccio M+3 (he hesitates visibly; half his usual interrupts)
   + Self-serve wine in arm's reach (free action)
   − Earshot ≤2 sq Full (most of hall dead to you)
   − ALL other companions: −2 drift cadence (read you as withdrawn)
   − Jamandi disp −1/turn (you skipped her event)
   − PR_09 audience ×0.7 (you weren't seen)
   TRADE: deep one-on-one specialist. Carousel crawls.
   ──────

4. 🔥 HEARTH (N6) — aggressive intel, contested ground
   + Tartuccio Full audio TO him (every word he says quotable)
   + Seekers Partial earshot (passive disp build, slower than #7)
   + Tartuccio Confidence floor −1 (you're rattling him in his zone)
   + Goldmoon +1 approach (warmth/healing motif)
   − Tartuccio Full audio FROM you (weaponized in PR_09)
   − Tartuccio Exchange Cap +1 (he can press 3 instead of 2 at baseline)
   − Headcount Pressure +1 tier against you (HIS zone, not neutral)
   − Seekers read "shopping for loyalty": Ch1 flip DC +1 for any you fail
   TRADE: intel war / Tartuccio harasser. Costly if you're not winning.
   ──────

5. 🎭 CENTER FLOOR (H8) — maximum visibility, maximum exposure
   + Full audio across the hall (everyone hears your WINS)
   + +1 drift to ALL companions
   + PR_09 audience ×1.5
   + Performance/Diplomacy spot checks +2 (audience presence)
   + Linzi +2 (best chronicle material in the building)
   − +1 drift to TARTUCCIO too — he comes hard and fast (M−2)
   − Everyone hears your LOSSES too — failed-check penalties DOUBLED
   − Jamandi disp −1/turn (you stole her stage)
   − Conservatives (Goldmoon, Kyoko, Olivier): −1 approach
   TRADE: high-reward / high-cost spectacle. Wins are huge; losses ruin.
   ──────

6. 🪜 MAIN DOOR (G14) — security posture, exit access
   + Kesten immediate (Crime/Investigation queries +2)
   + EXIT ACCESS — leave the manor cleanly, no combat trigger
   + Late arrivals pass you first (free intel on every entering NPC)
   + Yang +1 approach (respects door duty); Kesten disp +1/turn
   − Companions read "ready to bolt": −2 drift cadence (slow carousel)
   − Jamandi disp −1/turn (notices distance)
   − Far-side beats unseen (no passive Perception on Hearth/Head Table)
   − Tartuccio ignores you — sounds good, but he works the room freely
   TRADE: security operator. Companion investment suffers.
   ──────

7. 🪑 SEEKERS' EDGE (J11) — deepest enemy territory, biggest swing
   + ALL 5 seekers Full earshot (massive passive disp build)
   + Ch1 flip DC −2 PER seeker tier achieved here (strongest unlock)
   + Direct seeker dialogue without provoking Tartuccio combat
   + Seeker Diplomacy +2
   + Tartuccio M−1 (clock fast; but he's rattled, 3 sq from him)
   − Tartuccio Full+ audio FROM you (every word quotable, PR_09 ammo)
   − Headcount Pressure +1 tier; Tartuccio Exchange Cap +1
   − Public seeker failure CASCADES — fail here, ALL 5 shift −2 each
   − Jamandi disp −2/turn (STRONGEST negative — "fraternizing the gnome")
   TRADE: Ch1 seeker-flip prep. Burns Jamandi relationship hard.
   ──────

8. 🌀 MOBILE / CIRCULATING — refuses to settle, works the room
   + +1 drift to ANY companion whose path you cross (broad sweep)
   + Tartuccio M+2 (struggles to land interrupts on moving target)
   + +1 Perception on ambient details (you see staff, late arrivals, gossip)
   + No companion locked in earshot zone — you can intercept anywhere
   − No deep conversations — opener slots take 2 turns instead of 1
   − Jamandi disp −1/turn (reads as nervous; bad host-read)
   − No passive earshot scoring (radius effectively 0 when moving)
   − Chronicle records you as "agitated" (Linzi disp −1)
   TRADE: breadth over depth. Generalist's choice.
   ──────

9. 👁️ BALCONY (off-grid, above row 1) — observer view
   + Visual on ALL positions (read body language at +3 Perception)
   + Jaethal-adjacent — unlocks her observer thread
   + Tartuccio CANNOT approach (off-grid)
   + +2 Perception on all social tells (lying, nervousness, signal exchanges)
   − NO companion can approach (carousel HALTS while up here)
   − No recruitment progress; no passive disp scoring
   − Tartuccio works room freely; Headcount Pressure +2 tiers against you
   − Jamandi may publicly call you down (humiliation choice point fires)
   TRADE: intel maximalist / recruitment zero. Strategic but slow.
   ──────

10. ✦ LINZI-ANCHOR (D6, beside Linzi) — chronicler cluster
    + Linzi disp +1/turn (proximity bonus)
    + Chronicle weight to PR_09 +20% (her record carries you)
    + Linzi-led openers fire 1 turn faster (she primes the table)
    + Bard composition bonuses (+1 Performance/Diplomacy when she plays)
    + Inherits CHAMPIONS earshot (D6 is in zone)
    − Companions with Linzi friction (Olivier, Sucrose) −1 approach
    − Chronicle bias toward player view (Jamandi reads as "Linzi's pet")
    − If Linzi later moves, anchor drops (must reposition or follow)
    TRADE: chronicler-led RP build. Locks you to Linzi's arc.
    ──────

11. 🍷 KITCHEN DOOR (A8) — consumable buffs, full menu, instant access
    + DIRECT food/drink access (free action, no turn cost) — full menu below
    + Max 3 buffs active; buffs carry into PR_04/05 combat if still active
    + Staff disp +1/turn (you treat them as people, you tip well)
    + Ezvanki +1 approach (he respects servants); Sucrose +1 (alchemy talk)
    + Late kitchen news (staff gossip, supply runs, late arrivals)
    − Jamandi disp −1/turn (snubbing the social event)
    − Carousel −1 drift (antisocial read)
    − No view of seekers' corner or head table
    − Tartuccio ignores you; you ignore him (mutual blind)
    TRADE: buff stacker / staff intel. Pre-loads combat. Antisocial frame.
    ──────

12. ⚔️ KASSIL'S SIDE (E2, adjacent to head table west) — military advisor
    + Kassil disp +2/turn (direct military pairing)
    + Olivier +2 approach (recognizes military discipline); Artoria +1
    + War-talk topics get +2 Diplomacy
    + Jamandi PARTIAL earshot (Kassil is near her — she catches gist)
    + Access to military intel (border reports, Kesten coordination)
    − Casters (Morrigan, Tatsumaki, Sucrose) −2 approach (martial gravity)
    − Tartuccio reads as "currying military favor" — Confidence +1 (he WANTS combat framing for PR_09)
    − Linzi disp −1 (bard near soldiers reads as boring)
    TRADE: war-council framing. Locks tone hard toward martial.
    ──────

13. 🐍 TARTUCCIO TAIL — wherever the gnome goes, you go
    + Intercept EVERY flip attempt (you're at his elbow constantly)
    + Tartuccio Confidence floor −2 (he can't shake you)
    + Each successful interrupt counter gives +1 disp with target companion
    + Full+ audio on him always (every word a weapon)
    − Tartuccio Exchange Cap +2 (he can press 4 always; +4 at Dominant = 5)
    − Headcount Pressure +2 tiers immediately (most aggressive read)
    − Jamandi disp −1/turn (reads as obsessive)
    − Conservatives (Goldmoon, Kyoko, Olivier) −2 approach (reads erratic)
    − If you fail an interrupt counter, target shifts to Tartuccio HARD (−3 disp)
    TRADE: hunter mode. All-in on neutralizing him. Catastrophic if outmatched.
    ──────

14. ✏️ CUSTOM — describe any cell; modifiers calculated from distance + zone adjacency
```

**JAMANDI EARSHOT MECHANIC:**

When `jamandi_in_earshot = TRUE` (positions 2, 5, 6, 12; partial-only at 9 Balcony visual):
- Jamandi can **chime in** on your conversations when topics in her lane fire (charter, Brevoy politics, Restov, the Lord Marshal, the assassination, Aerynth, Tartuccio). She does NOT chime in on private companion-recruitment beats.
- Jamandi forms **disposition shifts** from overheard content. +1 / −1 to `npc_dispositions.Jamandi` per overhead lane-hit. (Mirror of companion earshot passive approval, but Jamandi only.)
- Jamandi can **intervene** in companion conflicts at her discretion — single line, no forced redirect. Counts as her diplomatic care for the room.
- Tartuccio earns a `tartuccio_filed` entry whenever sensitive content (Pitax, parchment, Aerynth) is spoken in Jamandi's earshot — he files it for PR_09.

When `jamandi_in_earshot = FULL` (position 2 only):
- All of the above, AND she catches verbatim. Any public claim becomes her testimony at PR_09.
- She may directly address the player when the topic warrants. The companion exchange pauses briefly.

When `jamandi_in_earshot = PARTIAL` (positions 5, 6, 12):
- She catches fragments and tone. Disposition shifts apply but on partial info — may misread.
- Her chime-ins are about the gist, not specifics. She may ask follow-up questions if she heard something striking.

When `jamandi_in_earshot = VISUAL_ONLY` (pos 9 Balcony): body language + crowd reactions only; disposition shifts from visible actions only.

When `jamandi_in_earshot = ROTATING` (pos 8 Mobile, 13 Tail): recalculate per response from current cell. Mobile = path-radius; Tail = whatever Tartuccio hears (she watches him).

When `jamandi_in_earshot = FALSE` (positions 1, 3, 4, 7, 10, 11):
- She cannot hear OR react to player-table content. Disposition shifts only from direct interactions (player approaches her, she approaches the player).
- Sensitive disclosures (Pitax, Tartuccio's identity, Aerynth specifics) are safe from her — but also unprovable to her later. Tradeoff.

**SERVICE / SIGNAL ACCESS MECHANIC:**

Different positions grant different access to staff and key NPCs without leaving your seat. Save block tracks:
- `staff_access`: low / moderate / high
- `kesten_access`: immediate / fast / visible / far
- `kassil_access`: immediate / fast / visible / far

**Access tiers (apply to all three — Staff/Kesten/Kassil):**
- **IMMEDIATE**: arrives within the response, 0 turn cost
- **VISIBLE / FAST**: arrives within 1 turn, 0 turn cost (background)
- **MODERATE**: 1-2 turn delay, 0 turn cost but narrated wait
- **DISTANT**: runner needed, 1-2 turn delay
- **FAR**: 2-3 turns; sometimes substituted by a runner with a question

**Staff signal:** wine, food, errands, messages. Wine alcove has self-serve wine in arm's reach (free action) regardless of staff tier.

**Kesten signal:** prisoner updates, perimeter intel, cell access, guard repositioning, escort.

**Kassil signal:** guest intel, message routing, household coordination, archive lookups, political read.

**Signal commands:** `.signal staff [wine/food/errand]` | `.signal kesten [reason]` | `.signal kassil [reason]` | `.kitchen <item>` (pos 11 only, full menu, free action)

**FEAST CONSUMABLES** — full menu at pos 11 (Kitchen Door); other positions use `.signal staff` for wine/bread/cider subset (1-2 turn delay).

DRINKS (table-scope: player + Recruited companions at CHAMPIONS D6-F7):
- Stagwine: +1 Dipl w/ Aldori (1 hr)
- Brevoy red wine: +1 Will vs fear/Intim, −1 Perc (30 min)
- Spiced cider: +1 Fort, +2 vs cold (1 hr)
- Restov whisky: +2 Will vs fear, **−2 Will vs charm** (30 min)
- Coffee/strong tea: +1 Perc, −1 Stealth (1 hr)

FOOD (player-only):
- Roast venison: +5 HP scene-recovery, non-magical (1/scene)
- Honey cake: +1 morale to next ally action witnessed (1 use)
- Iced fruit: clears 1 fatigue tier (1/feast)
- Black bread + cheese: +1 Fort vs fatigue (2 hr)

Max 3 buffs active per char; 4th request waits or `.drop <buff>`. Active buffs CARRY into PR_04/05 if duration extends past explosion (30-60 min covers the night). At pos 11, player is alone — drinks apply to player only until walked to the table (1 turn, no buff lost). Save: `active_buffs[]` { item, type, expires_at_turn, scope, granted_to[] }.

**Render in STATE READ:**
```
Position: 🛡️ Champions (E6) | Earshot: 4-sq | T-travel: 7 sq | Drift: normal
         Staff: moderate | Kesten: distant | Kassil: distant | Jamandi-earshot: NO
```

**SEEKER EARSHOT MECHANIC (positions 4 and 7):**

The 5 seekers at Tartuccio's table (Yang, Weiss, Imoen, Senua, Alleria) do NOT enter the carousel — they remain at his table all feast per § PR_03 SEEKER EXCLUSION. But when the player is in earshot, they passively score the player's threads against their OWN profiles (per KM_Backstories_D*.md).

Each seeker has a `seeker_dispositions.<name>` field in the save block, starting at 0. Accumulates over the feast based on overheard content. Disposition tiers:
- 0 to +1: NEUTRAL (Ch1 flip DC unchanged — Diplomacy DC 10)
- +2 to +3: WARMING (DC −1 → DC 9)
- +4 to +5: INTERESTED (DC −2 → DC 8)
- +6 to +7: SYMPATHETIC (DC −3 → DC 7)
- +8+: ALIGNED (no roll needed — they flip on request)
- Negative: HOSTILE (DC +1 to +3, escalating)

**Seeker scoring by position:**
- #4 Hearth (N6): Senua + Alleria edge-partial earshot, score at −1 tier
- #7 Seekers' Edge (J11): ALL 5 fully in earshot, full-tier scoring
- #13 Tartuccio Tail: scores whichever seekers are near Tartuccio's current cell
- All other positions: seekers OUT of earshot, no scoring

**Seeker profile anchors (per KM_Backstories_D*.md):**
Yang—physical courage, protect defenseless. Weiss—excellence + integrity, refuse inherited tyranny. Imoen—stay with chosen people, forward momentum. Senua—face what others can't see. Alleria—precision, duty, don't surrender.

Score each seeker independently per FEAST APPROVAL TRACK + position modifier.

**REVERSE EARSHOT — `🪑 SEEKERS' TABLE` panel mandatory at positions 4, 7, 13** (Tail when near corner). Panel renders Tartuccio's current gambit beat, each seeker's reactions (body language + audio), seeker-to-seeker overheard lines, quotable Tartuccio lines (citation ammo). Missing panel at these positions = `.fail 9`.

Position 4 (Hearth): visual on all 5, audio fragments from Senua/Alleria only, no verbatim Tartuccio quotes (gist only). Position 7 (Seekers' Edge): full audio + visual, every line quotable. Position 13 (Tail at corner): full+ audio, every word.

Panel format:
```
🪑 SEEKERS' TABLE
Tartuccio: <current gambit beat>
Yang/Weiss/Imoen/Senua/Alleria: <one line each — body language + audio>
```

---

**Tradeoff summary (15×15 grid, distances from Tartuccio M12):**
| # | Position | Cell | Earshot | T-dist | Jamandi | Seekers | Signature trade |
|---|---|---|---|---|---|---|---|
| 1 | Champions | E6 | 3-sq | 11 sq | NO | NO | Warrior cluster / casters −1 |
| 2 | Head Table | G2 | 2-sq | 13 sq | **FULL** | NO | Politics / populists −2, Tt blocked |
| 3 | Wine Alcove | C12 | 2-sq, **−1 tier** | 10 sq | NO | NO | Privacy / carousel crawls |
| 4 | Hearth | N6 | 2-sq | 6 sq | NO | PARTIAL | Intel war / Tt Cap +1, HC +1 |
| 5 | Center Floor | H8 | **5-sq** | 6 sq | PARTIAL | NO | Spectacle / losses doubled |
| 6 | Main Door | G14 | 2-sq | 5 sq | PARTIAL | NO | Exit + Kesten / drift −2 |
| 7 | Seekers' Edge | J11 | 2-sq | 3 sq | NO | **ALL 5** | Ch1 flip DC −2/tier / Jamandi −2/turn |
| 8 | Mobile | varies | rotating | varies | rotating | rotating | Breadth / openers 2× turns |
| 9 | Balcony | off-grid | none | ∞ | visual | NO | Intel max / carousel HALTS |
| 10 | Linzi-anchor | D6 | 3-sq | 11 sq | NO | NO | Chronicler / Linzi-locked |
| 11 | Kitchen Door | A8 | 2-sq | 12 sq | NO | NO | Poison watch / antisocial |
| 12 | Kassil's Side | E2 | 2-sq | 12 sq | PARTIAL | NO | War council / casters −2 |
| 13 | Tartuccio Tail | tracks Tt | 1-sq | 0-1 sq | varies | varies | Hunter / Cap +2, HC +2 |
| 14 | Custom | any | calc | calc | calc | calc | DM derives modifiers from cell |

**Save block fields written on selection:**
`player_feast_position` (slug) | `player_feast_cell` (e.g. "E6") | `earshot_radius` (int) | `tartuccio_travel_distance` (int) | `tartuccio_eavesdrop_modifier` (int) | `drift_cadence_modifier` (int) | `headcount_pressure_modifier` (int) | `tartuccio_exchange_cap_modifier` (int) | `jamandi_disp_per_turn` (int) | `companion_affinity_modifiers` (object: name→delta)

**Mechanical effects each response:**

1. **Earshot:** companions within `earshot_radius` can interject + score passive approval. Outside = visual only.

2. **Tartuccio Cadence:** M = base_M + travel modifier. Distance from M12 to player cell:
   1–3 sq → **−1** | 4–6 sq → **0** | 7–9 sq → **+1** | 10–12 sq → **+2** | 13+ sq → **+3**
   Worked (Conf 0, base M=7): Seekers' Edge 3 sq → M=6 · Hearth 6 sq → M=7 · Center/Door 5-6 sq → M=7 · Champions 11 sq → M=9 · Head Table 13 sq → blocked (politics). **Min M=1 (Dominant + adjacent). Max approaches never (Withdrawn at Alcove/Kitchen). Mid-feast reposition recalculates immediately** — narrate Tartuccio adjusting posture, abandoning half-formed Frame.

3. **Eavesdrop:** position-fidelity modifier applies to Tartuccio's standard table.

4. **Drift Cadence:** `drift_due = floor(N / (6 + drift_cadence_modifier))`. Wine Alcove −2 → /8. Center +1 → /5. Mobile no drift (no passive earshot).

5. **Headcount Pressure modifier:** Hearth/Seekers' Edge +1 tier from spatial proximity. Tartuccio Tail +2. Balcony +2 (cedes the floor).

6. **Exchange Cap modifier:** Hearth +1, Seekers' Edge +1, Tartuccio Tail +2.

**Player may move mid-feast** (as a "move to <position>" action — costs 1 player turn, updates all position fields immediately, narration shows the physical reposition and companions/Tartuccio reacting to it). Save block `player_feast_position` updates; new modifiers apply from the next response.

**Rendering — STATE READ block must show current position:**
```
[STATE READ] current_scene="prologue_feast" | phase=PR_03_FEAST_CIRCUIT
Position: 🛡️ Champions section (C6) | Earshot: 4-sq | T-travel: 7 sq | Drift: normal
```

Missing position selection at PR_03 start = `.fail 9` (position fabricated by DM instead of chosen by player) + `.fail 45` (player position narrated without declaration).

---

## ⛔ TARTUCCIO ARRIVAL COUNTDOWN — VISIBLE EVERY RESPONSE

**The `Clock: N/M` line in STATE DELTA is the raw counter — but it's not legible at a glance. Every response must ALSO output an explicit arrival countdown so the player can see when Tartuccio will step over.**

**Required line in 📜 TARTUCCIO STATE DELTA — directly below the Clock line:**

```
Arrives in: <M − N> player turns  (progress: [▓▓▓░░░░] 3/7)
```

**Format rules:**
- `M − N` = turns until interrupt fires at current Confidence threshold. At N=3 / M=7, that's **4 turns**.
- Progress bar: 7 characters wide, ▓ for elapsed cells, ░ for remaining. Length stays 7 even if M is higher or lower — scale visually.
- If Confidence = −4 (Withdrawn): replace the line with `Arrives in: never (Withdrawn — ambient only)`.
- If clock just reset to 0/M after an interrupt: `Arrives in: M turns (just reset — interrupt N just fired)`.
- If clock is 1 turn away: `Arrives in: 1 turn — NEXT RESPONSE` (bold the urgency).
- If clock fires THIS response: `Arrives in: 0 — STEPPING OVER NOW`.

**Full STATE DELTA block with countdown:**

```
📜 TARTUCCIO STATE DELTA
Confidence: 0 → 0 | Trust: +1 → +1 | Activity: Measured
Clock: 3/7 | Interrupts done: 0 | Mode: Intel
Arrives in: 4 player turns  (progress: [▓▓▓░░░░] 3/7)
Headcount: 0 AT TABLE vs 5 at corner (Δ = −5) → Pressure: Comfortable
Target: none yet | Eavesdrop: seekers' corner | Fidelity: Visual only
Wariness: none established
```

**Examples by Confidence (showing M variability):**
- Confidence 0, N=3/M=7: `Arrives in: 4 turns (progress: [▓▓▓░░░░] 3/7)`
- Confidence +1, N=2/M=5: `Arrives in: 3 turns (progress: [▓▓░░░] 2/5)`
- Confidence +2, N=1/M=3: `Arrives in: 2 turns (progress: [▓░░] 1/3)`
- Confidence +4, N=0/M=1: `Arrives in: 1 turn — NEXT RESPONSE (progress: [░] 0/1)`
- Confidence −2, N=8/M=14: `Arrives in: 6 turns (progress: [▓▓▓▓░░░] 8/14)`
- Confidence −4: `Arrives in: never (Withdrawn — ambient only)`

**Forbidden patterns:**
- ❌ Showing only `Clock: N/M` without the explicit `Arrives in: X turns` line
- ❌ Omitting the progress bar
- ❌ Showing the same `Arrives in:` count two responses in a row (means clock didn't increment — see § HEADCOUNT PRESSURE and Tartuccio.md self-check rule)
- ❌ Misreporting `Arrives in:` value — must equal `M − N` exactly

Missing the countdown line = `.fail 3` (output structure incomplete). Wrong arithmetic = `.fail 4` (math error).

---

## ⛔ APPROVAL SCORING — PER-THREAD ANALYSIS, ANCHOR ON HIGHEST TIER

**The ambiguity:** sometimes the DM scores the whole player message as one tier; sometimes the DM scores each statement separately and stacks them. Neither is fully right. The canonical rule:

**Step 1 — Decompose the answer into threads.** A "thread" is a distinct statement, argument, or beat the player made. A short answer may have one thread; a long paragraph may have 3–6. Each thread gets analyzed against the active companion's profile (Background / Priority / Desire / Preference / Wound per KM_Companions.md).

**Step 2 — Score each thread independently against the companion's profile.** Per-thread tier:
- STRONG (+3) — names a wound, core truth, or recognition the companion has felt but never heard externalized
- AVERAGE (+2) — touches their lane with specificity
- WEAK (+1) — generic alignment / right sentiment, forgettable delivery
- 0 — irrelevant to their lane
- −1 — contradicts a stated value
- −2 — betrays a core need or wound

**Step 3 — Anchor on the HIGHEST positive tier.** The answer's overall tier = the strongest single thread, NOT the sum. A player who says one STRONG thing + two AVERAGE things scores **+3 once for this turn**, not +3+2+2 = +7. The strong thread is the moment; the others are texture.

**Step 4 — Apply negative threads as a drag.** Negative threads (−1, −2) reduce the anchor by one tier each. A STRONG (+3) + one −1 thread → AVERAGE (+2) for the turn. A STRONG + two −1 threads → WEAK (+1). A STRONG + one −2 thread → WEAK or 0. The negative cannot push past the anchor's floor in a single turn unless the anchor was AVERAGE or lower to begin with.

**Step 5 — Apply once per turn.** feast_approval increments by the anchor tier, ONCE per turn, regardless of thread count. Per-turn cap is one tier — not "+3 per STRONG thread."

**Why this matters:** if the player gave a long answer with five threads where 4 were AVERAGE and 1 was STRONG, the STRONG anchors the turn — the answer hit. If all 5 threads were AVERAGE, the answer hits AVERAGE — solid but not a wound-recognition moment. If the player gave a one-line answer that hits STRONG, that line alone hits STRONG. Long answers are not penalized for having texture; short answers are not boosted artificially.

**Rendering in 🎯 SCORING block:**
- List threads numbered with per-thread tier
- State the anchor explicitly
- State the drag if any negative threads fired
- Final turn delta = anchor minus drag, applied once

**Example output (compact):**
```
🎯 SCORING — Linzi
T1: "Am I your co-author?" → AVG (+2) — correct lane, no wound named
T2: "How are they the finest college when they make a decision that
   lowers their reputation?" → STRONG (+3) — names her 4-year wound
T3: "Redemption arc is best story" → WEAK (+1) — generic she knows
T4: jab on "finest college" → AVG (+2) — lane puncture, not wound

Anchor: STRONG (+3) Thread 2. Drag: none. Turn delta: +3.
feast_approval[Linzi]: 0 → +3
```

**Forbidden patterns:**
- ❌ Summing +3 +2 +2 +1 = +8 in one turn (stacking is banned; per-turn cap = one tier)
- ❌ Scoring "the whole answer" as a single tier without identifying the anchor thread
- ❌ Awarding STRONG when no thread actually named a wound (vague-but-right-topic = AVERAGE; perfect-about-wrong-topic = WEAK)
- ❌ Ignoring negative threads when computing drag

**Player counter-paste:** if a turn awarded `+5` or higher from a single answer, paste *"per-turn cap is one tier per KM_DMRules_C.md § APPROVAL SCORING. Re-score: identify the anchor thread, apply drag from any negative threads, single delta this turn."*

---

*KM_DMRules_C.md — feast carousel supplement. Pair-load with KM_DMRules.md during PR_03.*
