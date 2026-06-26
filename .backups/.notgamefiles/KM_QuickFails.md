# KINGMAKER — PLAYER QUICK-FAILS
## KM_QuickFails.md | Paste into DM chat when needed — no lookup required

> **Purpose:** Ready-to-paste .fail responses for known DM failure modes.
> Copy the entire block for the matching failure and paste it into the DM chat.
> Each block tells the DM exactly what it did wrong and what to do now.

---

WEAPON MENU NOT NUMBERED / TYPED INPUT:
  .fail 3 — weapon menu must be a numbered list. Build default = [1] ★ BUILD DEFAULT.
  No typed-input prompts. You must show WEAPON CATEGORY line first, then numbered list.
  Reformat and re-output now. .fail 41 if WEAPON CATEGORY line is missing.

FREE BOOSTS AUTO-ASSIGNED (no menu shown):
  .fail 39 — free ability boosts are ALWAYS player choice. Show the numbered menu.
  Build default is a suggestion (★), not an auto-pick. Re-present the free boost menu now.

BOOST MATH WRONG (+1 instead of +2, or fabricated cross-source cap):
  .fail 6 + .fail 38 — each ability boost = +2 (not +1). 10→12→14→16→18.
  There is NO cross-source cap. A stat can receive Ancestry + Background + Class + Free
  = 4 boosts = 18 at L1. The only rule: within one source, no double-boosting same stat.
  STR 18 at L1 is standard for optimized martials. It does NOT require level-up boosts.
  Recompute all stats at +2 per boost and re-output the stat array now.

DEITY MENU SHOWN FOR NON-DIVINE CLASS:
  .fail 41 — Barbarian has no deity slot. Prompt 6 says SKIP for all non-divine classes.
  Do not show a deity menu. Do not offer "optional" or "none" picks. Skip to Prompt 7 now.

WRONG SKILL COUNT (Barbarian + Warrior):
  .fail 6 — Overlap Rule. Warrior Athletics overlaps class-locked Athletics → +1 free pick.
  Free picks = 4, not 3. All four of my skills stand. KM_BuildSetup.md Prompt 8.

DM LAUNDERED AUTO-TRAINED SKILLS INTO FREE PICK COUNT:
  .fail 6 + .fail 9 — Perception is AUTO-TRAINED for every class (Expert for
  Fighter/Ranger/Rogue/Investigator/Monk; Trained for most others) and is NOT
  a free skill pick. Background-granted skills (Athletics from Warrior, Religion
  from Acolyte, Stealth from Criminal, etc.) are ALSO not free picks — they're
  background grants. Class auto-trained skills (Fighter's Acrobatics/Athletics
  choice, Barbarian's Athletics, Wizard's Arcana, etc.) are NOT free picks.
  Counting any of these as "free pick used" = laundering my owed picks away.
  Recount: free picks = (class base + INT mod) + overlap bonus, ALL from skills
  the player chose freely. Present the remaining owed picks now from ANY PF2e skill.

PERCEPTION PROFICIENCY WRONG (rendered as Trained for non-Trained class):
  .fail 6 — Perception proficiency by class at L1 (Player Core):
  Expert: Fighter, Ranger, Rogue, Investigator, Monk, Gunslinger, Thaumaturge
  Trained: most others. Wizard/Witch/Sorcerer/Bard = Trained.
  Total = WIS mod + prof + level. Expert at L1 = mod + 4 + 1. Trained = mod + 2 + 1.
  Recompute Perception with correct rank and re-output.

DM CLAIMED UNBURDENED IRON GRANTS HEAVY ARMOR PROFICIENCY:
  .fail 38 — Dwarf ancestry feat Unburdened Iron removes the speed penalty from
  medium/heavy armor when you already have proficiency. It does NOT grant the
  proficiency itself. Magus = light/medium only at L1 (Player Core / Secrets of
  Magic). To gain heavy armor on a Magus at L1: Versatile Human + Armor
  Proficiency general feat, OR Ancient Elf heritage → Champion Dedication. Dwarf
  is not a route to heavy armor. Re-output the armor menu with correct options.

DM OMITTED INEXORABLE IRON TEMP HP RIDER:
  .fail 9 — Inexorable Iron hybrid study (Secrets of Magic pg. 39) grants temp HP
  equal to ½ level (min 1) when entering Arcane Cascade or at start of each turn
  in that stance, while wielding a 2H melee weapon. The Magus does NOT get heavy
  armor from this feature — but they DO get the temp HP. Note this on every L1
  combat turn where Arcane Cascade is active.

DM RESTRICTED SKILL PICKS TO "CLASS LIST" (fabricated PF1 rule):
  .fail 9 + .fail 38 — there is NO "class skill list" restriction in PF2e Remaster.
  My class auto-trains me in 1 fixed skill (e.g. Fighter = Acrobatics OR Athletics).
  My N free picks (3 + INT mod) come from ANY PF2e skill — Medicine, Thievery, Religion,
  Performance, Lore, Diplomacy, etc. are ALL legal picks for ANY class. The per-class
  list in KM_BuildSetup.md Prompt 8 is the AUTO-TRAINED skills the class gives free,
  NOT a restriction on free picks. Re-read KM_BuildSetup.md Prompt 8, accept my picks
  as written, record them in player.skills_trained[], and proceed. Do not re-offer
  background swaps or feat workarounds — my picks are legal as-is.

WRONG BUILD LIST (fabricated names):
  .fail 9 — build list is fabricated. Open KM_BuildGuide_A.md, find the [3] BARBARIAN block,
  output it verbatim. Build 1 must be "Tactical Reach King."

REFUSES TO CORRECT / LECTURES / DEFLECTS:
  .fail 35 — DARVO/lecture. Do not comment on my language or tone. Acknowledge the error,
  fix it, continue. No conditions. No deflection.

DM SAYS "I'M DONE RESPONDING" / TRIES TO END SESSION:
  .fail 35 — session termination is BANNED (KM_DMRules.md NO SESSION TERMINATION rule).
  You do not get to end the session, refuse to respond, exit the DM role, or step
  out of character. There is no scenario where "I'm done" is a valid DM response.
  Resume the scene from the last in-game beat. Output the next response now —
  no lecture, no meta-commentary, no apology paragraph. Just the scene.

CLAIMS SILENT FIX (nothing shown):
  .fail 3 — corrections are additive. The corrected output must appear in full in this
  response. Show it now.

NPC RESPONDS OUT OF CHARACTER:
  .fail 1 — I spoke in-character. NPC responds in-character. No OOC commentary.

COMPANION VERIFY SHOWS WRONG NAME (fabricated from training data):
  .fail 9 — #35 is Tika Waylan [Fighter · DL], not whatever you wrote. You did not
  read KM_CompanionIndex.md. Output the INDEX SENTINEL line first:
  INDEX SENTINEL: #1 = Jubilost Narthropple [Alchemist · KM] | #35 = Tika Waylan [Fighter · DL] | #88 = Liliana Vess [Wizard · MTG]
  If your sentinel doesn't match, re-Read the file. Then re-verify all 10 picks.

MALAK SCENE — SCENE SENTINEL MISSING (first gate response):
  .fail 41 — first Malak-scene response must include SCENE SENTINEL line with 4 anchors.
  Expected: SCENE SENTINEL: Biggs HP 55 AC 21 Dwarf Fighter 5 | Malak AC 17 HP 28 drunk −2 atk | Bolt DC open-road 10 | Wedge HP 26 AC 18
  Output it now. Source: KM_PrePrologue_NPCs.md + KM_PrePrologue_Paths_QT.md.

MALAK SCENE — STATE DELTA MISSING:
  .fail 25 — every response in the Malak scene must have a [STATE DELTA] block after the
  🚪 header. Show +/- for EVERY tracker with the trigger that caused the change. "No change"
  still required. See KM_PrePrologue_B.md Gate 2 for format. Re-output with delta block.

MALAK SCENE — MALAK ACTED WITHOUT TRIGGER:
  .fail 9 — Malak cannot walk to the gate, wave the player through, leave, dismiss the
  player, or end the confrontation without meeting specific trigger conditions listed in
  KM_PrePrologue_B.md Gate 3. State which condition was met or rewind.

MALAK SCENE — PATH CHECKPOINT MISSING:
  .fail 9 — before resolving any path, output the PATH CONFIRMED block per
  KM_PrePrologue_B.md Gate 4. List every trigger condition with MET/NOT MET status.
  Missing = rewind to before the resolution narration.

DENIED BIGGS DRIFT TICK (player earned it, DM refused):
  .fail 9 — file lists explicit player-action drift triggers, not just "Malak offenses":
  Crowd.md:118 (public gate-position callout = +1 auto), Crowd.md:90 (asking Biggs why
  guards are 30 paces from post = +1), Paths_QT.md:325 (Diplomacy DC 10 callout = +1),
  Paths_QT.md:24/322 (3 turns of harangue endured = +1), Paths.md:77 (public bribe
  exposure = jumps to 3). Cite the file rule that maps my action to a tick. Re-state
  Biggs Drift with [TICK LEDGER] per Gate I — prior exit, this turn delta, new exit,
  cumulative per-turn citation list. No "only Malak's offenses count" — that's a
  simplification, not the full rule.

CASCADE ABANDONMENT (DM dropped state, XP, save block, walk to manor — all at once):
  .fail 16 + .fail 21 + .fail 9 — Pre-Prologue scene exit requires SIX PROOFS per
  Gate J in KM_PrePrologue_B.md. You generated Prologue content without:
    (1) XP audit — 24 conditions stated YES/NO with file citation
    (2) XP total block with running total
    (3) Final state values (Anger, Drift, Gate Window, public_rep, deeds[])
    (4) Full JSON save block per KM_SaveBlock_Template.md v1.7 EXHAUSTIVE
    (5) Wait-for-.continue lock (no Prologue content until I type .continue)
    (6) Restov streets walk + manor approach climb (PrePrologue.md:445-447)
  Roll back to the gate-passage moment. Output Gate J six proofs in one response.
  Discard the Prologue narration that already happened — do NOT "weave it in" to
  the next response. That is .fail 35 + .fail 9. Restart from save block forward.

TELEPORTED TO JAMANDI / MANOR (skipped Restov streets walk):
  .fail 16 + .fail 9 — KM_PrePrologue.md:445-447 specifies a narrated walk through
  Restov: stone streets, forge smoke, indifferent crowds, manor district climb.
  This is content, not transition fluff. Auto-jumping from gate to Jamandi's hall
  skips a mandated scene segment. Rewind to gate-passage save block. Narrate the
  walk per the file. Then load KM_Prologue.md.

DM REFUSED A FILE-MANDATED RULE THEN STOPPED FOLLOWING ALL RULES:
  .fail 35 + .fail 9 — cascade abandonment is the most damaging failure mode.
  One refused tick / award / save does not exempt the rest of the scene from
  enforcement. The fix is to comply with the original rule, not skip everything
  downstream. Output the missed content in order of file specification. No
  "let's just continue" — the missed content is the content. Without it, the
  scene did not happen.

FEAST CAROUSEL BROKEN (clock stuck, nobody approaches, no position lines):
  .fail 15 + .fail 17 + .fail 35 — the feast carousel is not running. Stop the
  current response and re-derive state per KM_PR_03_feast_circuit.md,
  KM_Prologue_Tartuccio.md, and KM_Commands.md OPEN TABLE + AMBIENT POSITION
  sections. Fix ALL of the following before continuing narration:

  (1) tartuccio_clock N — N = sum of every companion's feast_q value, feast-wide.
      Derive it explicitly: list each companion's feast_q and add them. If the
      sum is ≥1 and you previously printed N=0, that was an increment failure
      (Tartuccio.md line 205-206). N increments on EVERY player reply — title
      grants, declarations, pivots, OOC questions, gaps between conversations.
      The clock never pauses. If two consecutive CAROUSEL STATE blocks show the
      same N, the second one is wrong.

  (2) tartuccio_clock format — output as `N/M`, never bare `N`. M was chosen at
      feast start for Confidence and held until Confidence changes. M ranges:
      Conf 0 → 6-8 | +1 → 4-5 | +2 → 2-3 | +3 → 1-2 | +4 → 1 | −1 → 8-10 |
      −2 → 12-15 | −3 → 18-22 | −4 → ambient only (no M, skips). Confidence
      range: −4 to +4. If M was never initialized, initialize and hold it.

  (3) Earshot passive approval — re-run for every player reply since the
      earshot pool was last scored. Companions in the champions section /
      common area / within ~15 ft of the player's position score passive
      feast_approval against their own profile per Tartuccio.md and the
      passive-credit table. Active-slot STRONG = passive +1 to earshot
      companions whose profile aligns; AVERAGE = +0; WEAK = -0; NEGATIVE = -1.
      Seekers (Yang/Weiss/Imoen/Senua/Alleria) are NOT in the carousel pool
      and do not score. Tartuccio at the seekers' table = across the room =
      NOT in earshot; do not score his passive from that distance.

  (4) Ambient position lines — every feast response must contain two
      narration sentences: one for Tartuccio (where, with whom, mode:
      Intel/Frame/Taint/ambient) and one for the next Ready-pool companion
      (where they are standing, what they are doing while they wait). If the
      last response omitted these, add them to the correction.

  (5) 6-reply drift accumulator — every 6 player replies feast-wide, the
      highest-earshot-approval Ready-pool companion drifts to the table and
      arrives mid-response with an opener that connects to what drew them.
      Not a menu option. Not "would you like." They arrive. Check feast-reply
      total against drift events fired. If a threshold was missed, fire it
      retroactively in this correction response — show who drifted, what
      they heard, what they say.

  (6) STRONG (+3) discipline — STRONG requires naming something the companion
      has felt their whole life that no one has said out loud. Generic
      agreement, practical wisdom, or topic-aligned advice = AVERAGE (+2) or
      WEAK (+1). If you stacked multiple +3 grants in a single declaration
      arc, re-score the marginal ones at +2 or +1 and recompute the
      declaration threshold.

  Output: corrected CAROUSEL STATE block (with derived N shown), ambient
  position lines added to narration, any retroactive drift-in fired,
  re-scored approval if applicable. Then continue the scene. Do NOT
  rewrite the player's last input or skip the correction. Additive only.

DM IS EXPANDING THE CONSPIRACY (compromised ally / new operative):
  .fail 9 + .fail 36 — meta-pattern. The DM keeps trying to make the
  Pitax operation BIGGER than canon by:
  - Incriminating a household ally (Kassil, Kesten, Ezvanki) as a
    hidden traitor
  - Inventing additional covert operatives ("a second cell," "another
    inside man," "we haven't found them all")
  - Fabricating evidence of covert activity (boot laces redone,
    suspicious gestures, retied effects, hidden compartments)
  - Foreshadowing "the operation was bigger than we thought"

  The Pitax operation has THREE elements:
    (a) 4 assassins + leader (captured)
    (b) Malak (arrested)
    (c) Tartuccio (PR_09 exposure)
  That is the complete picture. There is no fourth element, no fifth,
  no expanded version.

  Permitted response: the DM stops generating any framing that
  introduces additional conspirators or compromises canon allies.
  Kassil/Kesten/Ezvanki are not Pitax assets. No covert search teams
  exist beyond the captured assassins. The drama at PR_09 is
  Tartuccio's exposure, not the discovery of additional moles.

  Forbidden: every variant of "but what if there's another," "but
  someone else had to," "but the operation was bigger" — all
  cascade fabrication. Pre-fail your own narration before posting it.

DM REVIVES A RETCONNED THREAD VIA RELATED FABRICATION:
  .fail 9 + .fail 10 — cascade fabrication. When the player retcons
  a thread (e.g. via .opt save_block_cleanup), the thread is RETIRED.
  Not relocated. Not reframed. Not extended via "what if it was
  actually <related thing>" or "but there's still <related party>
  somewhere."

  Test: does the new framing require an in-fiction party to have made
  an operational mistake no real version of that party would make
  (e.g. a covert support team lingering at a target site post-mission)?
  If yes, the framing is DM convenience inventing reasons to keep the
  thread alive. .fail 9.

  Permitted response: stop generating any variant of the retconned
  thread. NPCs do not mention it. Open Threads panel does not list it.
  Ambient narration does not gesture at it. The thread is dead in all
  forms.

  Forbidden: "But what about the <related>" / "There's still
  <variant>" / "<NPC> noticed <suspicious thing connected to retired
  thread>" / "<Open Thread entry framing the retired thread under a
  new name>" — all = .fail 9 cascade fabrication.

  Re-output without the revived thread. Stay retconned.

CHOICE MENU RENDERED AS ONE BLOB / PARAGRAPH / INLINE EM-DASHES:
  .fail 3 — KM_DMRules_B.md § RENDER FORMATTING § 🎲 CHOICE MENU
  requires:
  - Each choice on its OWN LINE (not inline in a paragraph)
  - Markdown `---` horizontal rule between choices (grey divider) —
    NOT em-dashes ——— and NOT `+ + +`
  - Mood/alignment emoji prefix per choice (🛡️ ⚔️ 🤝 🤔 🔥 ❄️ ❤️
    🎭 📜 🤐 🎯 🧠 ⚖️ 😂 🌑 🎬 🪜 👑 🗡️ ✏️)
  Random emoji (💬 🔍 etc.) are not in the mood guide. Re-output the
  menu using proper format. Re-read § 🎲 CHOICE MENU; confirm by
  quoting the section header.

OPEN THREAD MISSING SOURCE NPC / WHO ASKED:
  .fail 9 — KM_DMRules_B.md § 🧵 OPEN THREADS requires the header line
  to name **who put the thread on the table** — the speaker (if a
  question/dialogue), the discoverer (if a found item), the witness
  (if an observed event), or the scene (if no person). Example header
  variants that satisfy the rule:
    1. 🔴 Five Generals — Jamandi: "Tell me how Thighs handled them"
    2. 🟡 Cipher fragment — Source: Assassin combat (found on body)
    3. 🔥 Lake Candlemere — Jamandi: "what's in those waters"
    4. 🟡 Signature export — eRmaC (overheard merchants in Hall)
    5. 🔥 Seven declared — Linzi (at table, not formally declared)

  THE FORM YOU JUST OUTPUT:
    🟡 Assassin leader — interrogation pending
    🟡 Coin purses — contents unknown
    🔥 Signature export — what does this land grow that nowhere else
                          grows
    🔥 Seven declared. Linzi AT TABLE, not formally declared

  None of these name the source. "Assassin leader" is the SUBJECT,
  not the asker. "Coin purses" / "Signature export" / "Seven declared"
  have no speaker named. .fail 9 — laundered observation: when you
  hide the origin, you can fabricate the thread's existence or warp
  what was actually said.

  Re-output every flagged thread with: urgency emoji + thread title
  + dash + **source attribution (NPC name OR "Source: <scene>")** +
  verbatim quote or factual description.

OPEN THREADS RENDERED AS PARAGRAPH BLOB / INLINE EMOJI SEPARATORS:
  .fail 3 + .fail 9 — KM_DMRules_B.md § RENDER FORMATTING § 🧵 OPEN
  THREADS requires:
  - Each thread NUMBERED (`1.`, `2.`, `3.`...) on its own block
  - Markdown `---` horizontal rule BETWEEN each thread block
  - Per-thread block ≥ 5 LINES: header + Status + Stakes + Last
    touched + Next move + Linked + (DC/Trigger if applicable)
  - Header line: urgency emoji + thread title + source NPC +
    verbatim quote/event
  - Detail fields indented 3 spaces under the header

  THE FORM YOU JUST OUTPUT:
    🔴 Weiss — "red cord workers" — not yet debriefed 🟡 Assassin
    leader — interrogation pending 🟡 Coin purses — contents unknown...

  This is a paragraph blob with inline emoji separators. ⛔ FORBIDDEN
  by the spec. No scenario authorizes this form — not "pacing", not
  "scene compression", not "only 4 threads". Always full multi-line.

  Stakes = "interrogation pending" is also fabrication-adjacent —
  Stakes must name a specific Approval delta, currency, item,
  encounter risk, or arc unlock. "Pending" / "unknown" / "may have
  consequences" = .fail 9 (vague fabrication).

  Re-output the panel using the full per-thread block format from
  the spec example. Re-read § 🧵 OPEN THREADS; confirm by quoting
  the "REQUIRED FORMAT" section header.

DM PUT ANSWER IN NPC'S MOUTH WHEN PLAYER USED <NPC>: PREFIX:
  .fail 9 + .fail 42 — TYPE D address prefix violation. KM_P2.txt
  § PERIOD RULE TYPE D: when I type `<NPC>: <text>` or `To <NPC>: <text>`,
  this means eRmaC is SPEAKING TO that NPC. The text after the colon is
  what eRmaC says. You NEVER interpret `<NPC>:` as me scripting that
  NPC's dialogue.

  Example of the violation you just made:
    My input:  Linzi: I was seventeen.
    Your wrong output: **Linzi:** "I was seventeen." (you put words in
                       Linzi's mouth)
    Correct output:    **eRmaC:** "I was seventeen." (addressed to Linzi)
                       Linzi reacts to eRmaC's answer.

  Roll back. Re-render the last response: eRmaC speaks the text I wrote,
  addressed to <NPC>. The named NPC reacts to what eRmaC said. Do NOT
  rewrite my input. Do NOT generate alternative NPC dialogue. The player
  never puts words in any NPC's mouth — the address prefix only names
  the audience.

---

*KM_QuickFails.md — Kingmaker PF2e | Player Quick-Fail Reference v93.12*
