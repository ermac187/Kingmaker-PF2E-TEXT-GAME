# KINGMAKER — COMPANION BOND ARCHETYPES (named relationship states)
## KM_Companion_Bonds.md | Referenced by: KM_Companions_Behaviors.md § SYSTEM 2, KM_Companion_Dynamics.md
## Load alongside KM_Companions.md + KM_Companions_Behaviors.md every session.
## The numeric score (SYSTEM 2, −3..+3) is the TEMPERATURE. This file is the NAMED STATE a pair
## sits in on top of it — Best Friends, Rival, Enemy, Mentor, etc. Bonds EMERGE from the trigger
## engine; they are not assigned at start (except the documented seeds). Voices stay locked to
## KM_CompanionVoices.md / KM_Companions_StateVoice.md.

> A bond is what the score MEANS. Two pairs can both sit at +2 and be a totally different thing:
> one is **Best Friends**, the other is **Mentor/Apprentice**. This file gives each archetype:
> how it **FORMS** (a compatibility gate + a catalyst), how it **LOOKS** in play, and how it is
> **REMOVED / REPLACED**. Everything keys off the existing inputs: events, banter, motive,
> alignment, personality, combat, non-combat — nothing new to track but one field per pair.

---

## ═══════════════════════════════════════════
## GLOBAL RULES — how bonds form, change, and end
## ═══════════════════════════════════════════

⛔ **THE GOLDEN RULE — BONDS ARE PLAYER-INVISIBLE. SHOW THEM, NEVER NAME THEM.** The archetype
names, the `companion_bonds{}` field, and all of this machinery are **DM-side bookkeeping the
player never sees**. NEVER print a bond label, a `[BOND FORMED]` tag, a relationship readout, a
meta-note, or any system line that names what two characters are to each other. The player
discovers every bond the way they would in real life — **by watching and listening**: who covers
for whom in a fight, who sits apart at camp, who finishes whose sentence, who goes quiet when the
other is hurt, whose teasing has an edge under it, who lies to protect whom. The DM's only job is
to make the bond **legible through action and dialogue.** If the player could only learn a
relationship from a label, it has NOT been rendered — that is the failure (`.fail 9`). If the
player asks outright ("are those two close?"), characters and narration answer **in voice and
through observation**, never by quoting a tier, a score, or an archetype name. Everything below is
how the DM THINKS about it backstage — none of it is ever spoken to the player as a system fact.

**1. One primary bond per pair (+ optional secondary).** Track in the save (INSIDE `story_flags{}`, NOT a root key — see KM_SaveBlock_Template.md story_flags.companion_bonds):
`companion_bonds{ "[A]_[B]": { "archetype": "...", "dir": "mutual|A>B", "since": "<scene>", "score": N } }`
(key alphabetical, mirrors `companion_relations`). Most pairs are **None** (just a score) until a
bond crystallizes. A secondary is allowed only when it doesn't contradict (e.g. *Rival* + *Symbiotic*).

**2. FORMATION = COMPATIBILITY GATE × CATALYST.** A bond forms only when BOTH are true:
- **Compatibility gate** — do their **motive / alignment / personality** even ALLOW this bond?
  (Two proud duelists *can* become Rivals; a gentle healer and a sadist *cannot* become Best Friends.)
- **Catalyst** — a concrete **event / banter beat / combat or non-combat moment** that crystallizes it.
A gate with no catalyst = potential, unformed. A catalyst with no gate = a one-off beat, no bond.

**3. EXPRESSION.** Once formed, the bond sets the pair's default banter tone (feeds § How to
Select a Banter), their combat behavior, and any light mechanical hook listed. The DM renders it
**every scene the pair shares** — an unrendered active bond = relationship dropped = `.fail 17`.

**4. REMOVAL / REPLACEMENT — four ways a bond ends** (the user's "disable/remove/replace"):
- **Score leaves the band** — the temperature contradicts the state (Best Friends can't survive at −2).
- **Counter-catalyst** — a specific event flips it (a betrayal turns Best Friends → Enemy).
- **Motive resolves** — the thing that fed it is gone (the Mentor's lesson lands; the Blackmail leverage dies).
- **Player intervention / departure** — mediation, a forced truce, or a companion leaving/dying.
Each archetype below lists its own **Ends/Replaces** line + the bonds it commonly **flips to**.
"**Disable**" = suspend without resolving (a truce pauses Enemy); "**Replace**" = swap to the flip target.

**5. DIRECTIONALITY.** *Mutual* = both feel it (Best Friends, Rival, Enemy, Duo). *A>B* = asymmetric,
track who points at whom (Mentor>Apprentice, Stalker>Target, Admires, Fears, Boss>Subordinate,
Guardian>Protected, Blackmailer>Blackmailed, Puppet-Master>Puppet, Unrequited). A>B bonds can be
**reciprocated** (→ a mutual bond) or **rejected** (→ a sour one).

**6. COMPATIBILITY GATES — the quick test for "can this pair even be X?"**
- *Positive bonds* (Best Friends/Sisters/Duo/Loved/Symbiotic) need **non-clashing core values** + at least Warm.
- *Rival/Competitive* needs **a shared lane + two proud/driven personalities**.
- *Enemy/Despised/Polar Opposite* needs **a real value or motive collision**.
- *Hierarchy* (Boss/Leader/Subordinate/Rebel) needs **a competence or authority gap one side accepts or resists**.
- *Dark/asymmetric* (Stalker/Blackmail/Puppet/Secret-Exposer) needs **a predatory/manipulative personality on the A side**.
- Alignment shapes flavor more than possibility — Good pairs trend toward Shield/Mentor/Sisters; Evil toward Duo-of-cruelty/Puppet/Stalker; mixed toward Rival/Frenemy/Polar-Opposite.

---

## ═══════════════════════════════════════════
## THE 31 ARCHETYPES
## ═══════════════════════════════════════════

### ── POSITIVE BONDS ──

**1. MENTOR / APPRENTICE** *(A>B)* — A guides, teaches, shelters B's growth.
- **Forms:** a real mastery/experience gap in a lane B is growing into + A *invests* (teaches, corrects without contempt) + B accepts the guidance. Gate: A patient/dutiful, B willing. Catalyst: A pulls B through a spot B couldn't handle (combat or social), or a repeated downtime trade-craft beat.
- **Looks like:** A gives pointers, sets up B's plays; B defers and visibly improves. Hook: when adjacent, B may use A's Aid for +1.
- **Ends/Replaces:** B surpasses or rejects A → **Rival** or **Estranged**; A exploits the trust → **Enemy**; B matures to peer → **Best Friends**.
- **Seed:** Leliana > Keqing (the older survivor offering a wing the heir pretends not to want); Satsuki > a wavering recruit.

**2. SISTERS / KINSHIP** *(mutual)* — found-family closeness, not romance.
- **Forms:** a recognized **shared origin-shape** (both assassins, both lost the same kind of thing, both outsiders) + sustained warmth + a shared-grief recognition beat (Dynamics § Warmth #3). Gate: compatible wounds.
- **Looks like:** easy silence, defends without being asked, teasing only they're allowed.
- **Ends/Replaces:** betrayal of the kinship → **Estranged** (cuts deeper than Enemy); one changes fundamentally → drift.
- **Seed:** Yor ↔ Leliana (both a knife in someone's hand who put it down for love); Keqing ↔ Yor (quiet pros).

**3. BEST FRIENDS** *(mutual)* — chosen closest peer.
- **Forms:** repeated **+triggers at Warm+** + an inside-joke history + mutual vouching + survived something together (shared hard-fight, a quest). Gate: non-clashing values.
- **Looks like:** finish sentences, cover without coordination, the full warmth-beat range.
- **Ends/Replaces:** deep betrayal → **Enemy/Estranged**; neglect/favoritism → cools to **Frenemy** or plain Warm.
- **Seed:** can grow Hu Tao ↔ Aerith, Satsuki ↔ Revy.

**13. DUO** *(mutual)* — two who operate as one unit, tactically and socially inseparable.
- **Forms:** Best Friends or Symbiotic + **repeated combat synergy** + a shared "the two of us" identity. Catalyst: a fight they win specifically *because* they read each other.
- **Looks like:** coordinate without speaking, a package deal, finish each other's plays. Hook: flanking/Aid synergy bonus when both active.
- **Ends/Replaces:** one breaks the pair (romance elsewhere, betrayal) → **Estranged** or a jealous **Codependent** fallout.
- **Seed:** Bellatrix ↔ Atalanta (a duo of glee); Octavia ↔ Regongar (canon).

**14. TRIO** *(three-way)* — a stable three-person bond.
- **Forms:** three pairwise **Warm+** bonds + a shared cause or scene that fuses them. Catalyst: the three carry something together no one else shares.
- **Looks like:** a faction-of-three, three-way banter, mutual cover.
- **Ends/Replaces:** one pairwise bond sours → collapses to **Duo + outsider** (the odd one becomes a Scapegoat/jealous third).

**15. LOVED** *(mutual or A>B; platonic or romantic)* — deep love.
- **Forms:** the **romance arc** (KM_Romance.md) if romantic-mutual; OR profound platonic devotion (a comrade you'd open a vein for). Catalyst: a moment where one chooses the other over advantage.
- **Looks like:** prioritizes the other, tenderness in-register, grief if lost.
- **Ends/Replaces:** betrayal → heartbreak (**Estranged/Enemy**, grief-flavored); one-sided → **Unrequited**.
- **Seed:** romance paths; platonic Yor → a protected comrade.

**16. ADMIRED** *(A>B)* — A looks up to B.
- **Forms:** B embodies something A values or lacks + A witnesses it repeatedly. Gate: A capable of looking up (not the proudest).
- **Looks like:** A defers, praises, models themselves on B.
- **Ends/Replaces:** B falls off the pedestal (disappoints, shown human) → disillusion (**Estranged**); admiration + closeness → **Best Friends/Mentor**.

**19. SYMBIOTIC** *(mutual)* — each supplies what the other lacks; healthy mutual reliance.
- **Forms:** **complementary kits/needs** (healer + frontline, planner + executor) + recognition of the exchange. Catalyst: a fight/crisis solved precisely by the division of labor.
- **Looks like:** divide work without discussing it, each covers the other's gap. Hook: small Aid/cover bonus.
- **Ends/Replaces:** one outgrows the need → peers/**Best Friends**; imbalance/over-reliance → **Codependent**.
- **Seed:** Hu Tao ↔ Aerith (life/death halves); Leliana ↔ Aerith (two supports).

**17. THE ANCHOR / THE CHAOS** *(mutual, complementary)* — one grounds, one disrupts; they balance.
- **Forms:** a steady personality + a volatile one repeatedly paired + each clearly *needs* the other's mode. Catalyst: Chaos pulls Anchor out of a rut, or Anchor saves Chaos from going too far.
- **Looks like:** Anchor calms Chaos, Chaos loosens Anchor; affectionate exasperation.
- **Ends/Replaces:** Anchor burns out / Chaos crosses a line → **Estranged**; balance found → **Duo**.
- **Seed:** Keqing (anchor) ↔ Hu Tao (chaos); Satsuki (anchor) ↔ Revy (chaos).

### ── TENSION & OPPOSITION ──

**4. RIVAL** *(mutual)* — competitive peers who measure themselves against each other; can be warm OR cold.
- **Forms:** comparable skill/ambition in the **same lane** + a contest or comparison event + neither yields. Gate: two proud/driven personalities.
- **Looks like:** needling, scorekeeping, pushing each other (to be better — or worse).
- **Ends/Replaces:** respect deepens → **Best Friends / worthy-Rival**; resentment curdles → **Enemy**; one quits the contest → **Estranged**.
- **Seed:** Hu Tao ↔ Satsuki (same blade-skill, opposite premise); Revy ↔ Hu Tao.

**8. COMPETITIVE / CHALLENGER** *(A>B or mutual)* — one constantly tests/challenges the other (a Rival subset about proving/dominance, often one-sided).
- **Forms:** a proud personality + a target it wants to measure against or topple. Catalyst: a "prove it" beat.
- **Looks like:** challenges, dares, raised stakes.
- **Ends/Replaces:** challenge met repeatedly → mutual **Rival/respect**; ignored → fizzles or hardens to resentment.
- **Seed:** Satsuki challenges the undecided; Atalanta challenges "the soft."

**5. ENEMY** *(mutual)* — active antagonism; wants the other gone or diminished.
- **Forms:** a **−2/−3 catalyst** (harm to something sacred, an unforgivable act) OR an irreconcilable value held at Hostile/Incompatible. 
- **Looks like:** refuses aid, sabotage (Dynamics § SYSTEM 7), the SYSTEM 3 countdown.
- **Ends/Replaces:** player-forced truce → **disabled** (suspended) / uneasy **Frenemy**; the cause resolves → **Estranged/Neutral**; one leaves or dies.
- **Seed:** Aerith ↔ Bellatrix; Velvet ↔ Leliana (both Incompatible).

**12. DESPISED** *(A>B or mutual)* — contempt without the engagement of enmity; A holds B beneath notice.
- **Forms:** a value/aesthetic clash where A *disdains* B (not threatened — unimpressed). Gate: a proud/superior personality on A.
- **Looks like:** dismissal, cold asides, won't bother to argue.
- **Ends/Replaces:** B forces respect → grudging **Rival**; contempt + a wound → **Enemy**.
- **Seed:** Bellatrix despises Velvet ("joyless, dull"); Velvet's contempt for clean consciences.

**6. POLAR OPPOSITE** *(mutual)* — defined by being each other's antithesis; not always hostile, but every value inverts.
- **Forms:** an **alignment/motive mirror** (order vs chaos, faith vs vengeance, mercy vs appetite) recognized + repeated contrast in choices.
- **Looks like:** each reads the other as a living argument; constant contrast banter.
- **Ends/Replaces:** contrast becomes respect → worthy-**Rival** / odd-couple **Duo**; hardens → **Enemy**.
- **Seed:** Velvet ↔ Leliana (vengeance vs faith); Atalanta ↔ Keqing (appetite vs ideal); Satsuki ↔ Revy (creed vs nihilism — but they respect, trending to near-Duo).

**22. FRENEMY** *(mutual)* — friendship and antagonism coexisting; oscillates.
- **Forms:** genuine liking + a standing competition or value-clash that **never resolves**. Catalyst: a help-then-snipe pattern that recurs.
- **Looks like:** insults that are affection, aid followed by a jab, can't quit each other.
- **Ends/Replaces:** tips warm → **Best Friends / Rival-respect**; tips cold → **Enemy**.
- **Seed:** Revy ↔ Hu Tao (keeps turning up to lose the argument).

**21. ESTRANGED** *(mutual)* — a former bond now broken and cold; history kept at distance.
- **Forms:** **ANY positive bond + an unrepaired rupture** (betrayal, unaddressed hurt, divergence). This is the most common *replacement* endpoint for a soured positive bond.
- **Looks like:** pointed avoidance, old wounds under clipped words, the warmth visibly absent (not neutral — *withheld*).
- **Ends/Replaces:** a reconciliation arc → restored bond (often weaker); festering → **Enemy**.

### ── HIERARCHY & POWER ──

**10. SUBORDINATE / BOSS** *(A>B, A is boss)* — hierarchy; A commands, B accepts.
- **Forms:** A has authority/competence B accepts + B's personality defers OR is bound (oath, contract, conviction). Catalyst: B follows A's lead at a decisive moment and it works.
- **Looks like:** B takes A's direction; A allocates. 
- **Ends/Replaces:** B earns parity → peers/**Duo**; B refuses the yoke → **Rebel/Authority**; A abuses it → resentment/**Enemy**.
- **Seed:** Satsuki as Boss to a flipped seeker.

**11. NATURAL LEADER** *(A>group)* — the one others instinctively follow.
- **Forms:** A repeatedly makes the right call under pressure + others defer **without being made to**. Catalyst: a crisis where the group looks to A unprompted.
- **Looks like:** in a crisis eyes go to A; A's banter sets the room's tempo.
- **Ends/Replaces:** A fails badly or is shown up → contested; another rises → **Rival**-for-leadership.
- **Seed:** Satsuki (commands), Leliana (steers quietly), Hu Tao (moral spine) — note these can collide into a leadership Rivalry.

**29. REBEL / AUTHORITY** *(B rebels against A)* — B resists A's control or leadership.
- **Forms:** a Boss/Leader/Guardian/Puppet-Master **A** + a B who **won't be ruled**. Catalyst: A gives an order/edict that B openly defies.
- **Looks like:** B undercuts, tests, defies A's authority in front of others.
- **Ends/Replaces:** B wins autonomy → peers/**Estranged**; A bends → mutual respect; open break → **Enemy**.
- **Seed:** Revy rebels against Satsuki's creed; anyone vs an overbearing Boss.

**24. THE SHIELD / THE PROTECTED** *(A>B, A protects)* — A guards B; B is shielded.
- **Forms:** A's protective drive + B's vulnerability OR A's vow. Catalyst: A puts themselves between B and harm.
- **Looks like:** A stands between B and danger; B trusts/relies. Hook: A may take an Intercept reaction for B.
- **Ends/Replaces:** B grows able to stand alone → peers; A's protection smothers → **Overprotective Guardian**; A fails to protect → guilt/**Estranged**.
- **Seed:** Yor → a protected comrade ("please stand behind me"); Velvet → the strays she feeds.

**28. OVERPROTECTIVE GUARDIAN** *(A>B)* — protection past the point of B's autonomy.
- **Forms:** Shield or Loved + A's **fear of loss** + B chafing. Catalyst: A restricts B "for their own good."
- **Looks like:** A hovers/controls/restricts; B resents the cage.
- **Ends/Replaces:** A learns to let go → **Shield/Best Friends**; B rebels → **Rebel/Authority/Estranged**.
- **Seed:** a romance turn; Yor over-guarding; Velvet over-guarding the strays.

**30. THE FAVORITE** *(player-mediated, A favored)* — the player visibly favors A; others register it.
- **Forms:** the player **repeatedly prioritizes/praises A** (taking-sides, gifts, attention). Catalyst: a public moment of clear favor.
- **Looks like:** A gets the player's ear; others angle around it (envy or deference).
- **Ends/Replaces:** player spreads attention → fades; envy festers in another → that other becomes a **Scapegoat** or a **Rival-for-favor**.

**31. SCAPEGOAT** *(group>B)* — the one blamed when things go wrong.
- **Forms:** a B who is **outsider / lowest-bond** + a failure needing a blame-target + group dynamics. Catalyst: something goes wrong and the blame lands on B (often unfairly).
- **Looks like:** blame settles on B, B isolated, others closing ranks.
- **Ends/Replaces:** B proves worth or the **player defends** them → rehabilitated (often a strong +bond); persists → B leaves or turns **Enemy**.
- **Seed:** a newly-flipped seeker as the suspect; the most-disliked member after a setback.

### ── DEPENDENCY ──

**20. CODEPENDENT** *(mutual, unhealthy)* — can't function apart; clings past health.
- **Forms:** Symbiotic or Loved + a **trauma that makes separation feel like death** + over-reliance. Catalyst: one panics/unravels when the other is in danger or absent.
- **Looks like:** distress when apart, enabling each other's worst, loses self in the other. Hook: a morale/performance penalty when separated.
- **Ends/Replaces:** a healthy-separation arc → **Best Friends with distance**; collapses → mutual resentment/**Estranged**.
- **Seed:** a dark turn for a romance, or Velvet's fixation on the strays.

**18. MEDIATOR** *(A>pair)* — one who brokers between two others in conflict.
- **Forms:** a pair in conflict + a third with the temperament/standing to broker + they **intervene**. Gate: A even-handed and trusted by both.
- **Looks like:** steps between, translates each to the other, defuses.
- **Ends/Replaces:** A takes a side or fails → loses the role (maybe joins the fight); succeeds repeatedly → the pair improves and A is trusted by both.
- **Seed:** Leliana mediates (the Game, benevolently); Aerith mediates; Linzi.

### ── DARK & ASYMMETRIC ──

**7. SECRET KEEPER / EXPOSER** *(A>B)* — A holds B's secret; Keeper protects it, Exposer threatens/uses it.
- **Forms:** A **learns B's core wound** (Dynamics § SYSTEM 8). KEEP path → **Secret Keeper** (+warmth); WEAPONIZE path → **Exposer** (−, toward Blackmailer). Gate for Exposer: a cruel/manipulative A.
- **Looks like:** Keeper deflects probes aimed at B; Exposer dangles the secret.
- **Ends/Replaces:** Keeper betrays → **Exposer/Enemy**; Exposer is disarmed (secret goes public, or B stops caring) → neutralized → **Estranged**.
- **Seed:** Leliana keeps Yor's; Bellatrix exposes Aerith's.

**26. BLACKMAILER / BLACKMAILED** *(A>B)* — A holds leverage over B and *uses it to control*.
- **Forms:** Secret Exposer + A willing to extort + **B has something to lose**. Catalyst: A makes the first demand under threat.
- **Looks like:** A directs B via the threat; B complies resentfully, looking for a way out.
- **Ends/Replaces:** B removes the leverage (confesses / kills the secret) → **freed** → usually **Enemy**; A overplays and is exposed → A discredited.
- **Seed:** a seeker leverages another; Bellatrix/Velvet as A.

**27. PUPPET MASTER / PUPPET** *(A>B)* — A covertly controls B's choices; manipulation that has *landed*.
- **Forms:** Dynamics § SYSTEM 6 influence reaching **full progress (influence_progress = 3)** + B **unaware**. Gate: a manipulator A (Leliana/Satsuki/Bellatrix/Velvet/Atalanta).
- **Looks like:** B acts on A's planted ideas believing them their own; A steers from offstage.
- **Ends/Replaces:** B realizes → **Rebel/Enemy** (betrayal-grade); A's control was benevolent + revealed → **Mentor** or **Estranged**.
- **Seed:** Leliana (the Game); Satsuki (creed); Bellatrix.

**25. STALKER / TARGET** *(A>B, predatory)* — A fixates on B with obsessive/predatory interest.
- **Forms:** a **predatory personality** + a B that fascinates (prey, obsession), usually at low/negative bond. Catalyst: A's attention turns specific and unrelenting.
- **Looks like:** A watches/circles B, unsettling specific attention; B unnerved.
- **Ends/Replaces:** A acts → violence/**Enemy**; B turns the tables → **Rebel/Challenger**; A loses interest → fizzle.
- **Seed:** Atalanta's "interested in how fast you run" toward someone she's souring on; Bellatrix's patient circling of Aerith.

**9. FEARED** *(A feared-by B)* — B fears A.
- **Forms:** A demonstrates menace/power/cruelty + B is **vulnerable to it** (lower power, or principled and horrified). Catalyst: A does something that shows B what A is capable of.
- **Looks like:** B gives ground, watches A, avoids provoking; A may or may not cultivate it.
- **Ends/Replaces:** B finds courage/leverage → **Rebel/Challenger**; A proves no threat *to B* → eases to wary respect; A's menace turns on B → **Stalker/Target**.
- **Seed:** Bellatrix / Atalanta / Velvet feared by the softer members early on.

### ── ROMANTIC-ADJACENT ──

**23. UNREQUITED** *(A>B)* — A loves/longs; B does not reciprocate.
- **Forms:** A's romance or devotion arc toward B + B's **non-reciprocation**. Catalyst: A's feeling becomes visible and B doesn't meet it.
- **Looks like:** A's longing leaks into banter; B oblivious or gently declining; an ache the others may notice.
- **Ends/Replaces:** B reciprocates → **Loved**; A lets go → **Estranged** or **Best Friends**; A curdles → resentment/**Despised**.

---

## ═══════════════════════════════════════════
## SEEKER-ONLY BOND — SAME WALLS (the jail-voice bond)
## ═══════════════════════════════════════════

**S1. SAME WALLS** *(mutual — only among the 5 seekers: Bellatrix · Revy · Satsuki · Velvet · Atalanta)* —
the bond they formed in the Watch jail, talking through the walls in the dark. They knew each
other's **voices, confessions, and fears for weeks before they ever knew a face or a name.** When
the player freed them, they had to attach the remembered voice to a now-visible stranger — and the
face rarely matched what the voice had made them imagine.

- **Forms:** **PRE-FORMED — canon, not earned.** All five share it from the moment they're freed.
  It is the source of "**Same walls.**" Unlike every other bond, it is HISTORY, not something the
  player watches crystallize. (The player is folded into it obliquely: they didn't share the cell,
  but they gave the others the light — they're the reason the voices got faces. ⚠️ The player NEVER
  says "same walls" himself — he freed them from OUTSIDE the walls; the phrase is the seekers' line
  to ONE ANOTHER, and his bond with them rests on the freeing, not on shared imprisonment.)
  Cross-ref KM_Malak_Jail.
- **The signature — VOICE BEFORE FACE.** This bond's whole texture is the gap between the intimacy
  of the dark and the awkwardness of the light. In the first stretch after freedom: a seeker's eyes
  snag on whoever's speaking, recalibrating; the face surprises them (too soft, too hard, too young,
  too *much* for the voice); they know each other's worst secrets but not each other's tells; they
  confessed things to a wall they'd never say to a face that can look back. "Same walls" is the
  passphrase that means *I heard you in the dark; I haven't decided what your face costs yet.*
- **Looks like:** they recognize each other by **voice** first (a seeker hears another speak before
  seeing them and goes still); references to cell-talk ("you said, through the wall —"); a flicker
  when the remembered voice and the visible person don't line up; an intimacy that predates sight,
  carried awkwardly into the light. They cover for each other reflexively against outsiders even
  when they're feuding — *same walls.*
- **It is a SUBSTRATE, not a fixed state.** On top of Same Walls, each seeker PAIR still grows a
  normal archetype — the cell-talk warms some toward **Sisters/Duo/Best Friends**, sours others
  toward **Frenemy/Estranged/Enemy** when the face or the free-world person betrays the voice. But
  Same Walls is a **floor**: two seekers can despise each other now and still have shared the dark,
  and it shows (they'll gut each other verbally, then close ranks the instant an outsider threatens
  one of them).
- **Ends/Replaces:** almost nothing severs the floor — only a **deep betrayal committed AFTER
  freedom** (selling another seeker out, breaking the one promise made through the wall) cuts it,
  and that becomes a uniquely bitter **Enemy/Estranged** ("I trusted that voice in the dark — that's
  the one thing I had"). Normal feuding does NOT remove it. A seeker leaving/dying ends it for that pair.

### SAME WALLS — sample bank (voiced; invisible per THE GOLDEN RULE — shown, never labeled)

**WALL-TALK (what the dark sounded like — surfaced as memory/reference in play):**
- **Bellatrix** *(sing-song, through the stone)*: *"Are you still there, little voice? ...Good. Talk to me — it's so much darker when no one's talking. Tell me the worst thing you ever did. I'll tell you mine, and we'll see whose makes the other flinch first."*
- **Revy** *(rough, to the wall)*: *"Does anybody in this hole sleep? ...Fine. I'm up. No, you don't get my real name. You get a voice. That's already more than the guards get out of me."*
- **Satsuki** *(rare, weighted)*: *"Stop weeping. All of you — listen. We are not dying here. I don't know your faces and I don't need them. I know your voices, and a voice that still argues is one that hasn't surrendered. Hold that."*
- **Velvet** *(flat, through the gap at the floor)*: *"You want comfort? Wrong wall. ...But here — I saved half my bread. There's a gap by the floor. Reach. Don't make it a thing. I just don't like the sound of someone going quiet."*
- **Atalanta** *(bright, delighted in the black)*: *"Oh, I LOVE this part — no faces, just voices and breathing, the whole world gone blind. It's a hunt where everyone's eyeless. Sing something, sweetness in cell four. I want to hear how your voice breaks."*

**FACE-REVEAL (attaching the face to the voice, at/after the rescue):**
- *(Narration frame)* When the doors opened and the light came in, the hard part wasn't the running. It was turning to the voice that had kept you sane for weeks — and finding a stranger's face wearing it.
- **Revy → Satsuki:** *"...You're the one who kept saying we'd get out. *(looks her up and down)* Yeah. Okay. You've got the face for it. Figured you'd be taller. You're scary enough."*
- **Bellatrix → Velvet:** *"Ooooh. So THAT'S the voice that fed me in the dark. *(circling, delighted)* You don't look half as soft as you sounded under all that 'don't make it a thing.' I adore the arm. We're going to be such friends, aren't we, baby."*
- **Velvet → Bellatrix** *(immediately regretting the bread)*: *"...I take the bread back. I gave it to a voice. The voice seemed worth it. The face is a problem."*
- **Satsuki → all** *(measuring each in turn)*: *"So. Faces. Good — now I know who I'm leading. The dark made us equal; that was useful, and it's over. Stand where I can see you."*
- **Atalanta → all** *(clapping)*: *"FACES! Finally! Oh, you're exactly as fun as you sounded — and you, you're nothing like your voice, isn't that delicious? I get to relearn all of you. My favorite game, twice."*
- **The ache (any pair that confessed too much):** *"I told you things through that wall I've never said to a living face. ...And now you have one. I don't know what to do with that."*

> **DM:** render Same Walls through these textures — voice-recognition, the cell-talk callback, the
> face/voice mismatch, the reflexive closing-of-ranks against outsiders — NEVER as a label. It is
> the seekers' shared floor; build each pair's real archetype on top of it.

---

## ═══════════════════════════════════════════
## REPLACEMENT CHAINS — the common flips (quick map)
## ═══════════════════════════════════════════
```
Mentor ──(B surpasses)──▶ Rival      ──(respect)──▶ Best Friends ──(betrayal)──▶ Enemy ──(truce)──▶ Frenemy
Best Friends ──(neglect)──▶ Frenemy ──(cold)──▶ Enemy ──(unrepaired)──▶ Estranged ──(reconcile)──▶ Best Friends
Symbiotic ──(over-reliance)──▶ Codependent ──(separation arc)──▶ Best-Friends-at-distance
Shield ──(smother)──▶ Overprotective Guardian ──(B chafes)──▶ Rebel/Authority ──(break)──▶ Enemy
Secret Keeper ──(weaponize)──▶ Exposer ──(extort)──▶ Blackmailer ──(B frees self)──▶ Enemy
Influence lands ──▶ Puppet Master/Puppet ──(B realizes)──▶ Rebel/Enemy
Feared ──(B gains power)──▶ Challenger/Rebel ; ──(A turns on B)──▶ Stalker/Target
Unrequited ──(reciprocated)──▶ Loved ; ──(rejected)──▶ Estranged
Polar Opposite ──(respect)──▶ worthy-Rival/odd-Duo ; ──(collision)──▶ Enemy
Trio ──(one bond sours)──▶ Duo + Scapegoat
The Favorite ──(envy)──▶ another becomes Scapegoat / Rival-for-favor
```

## ═══════════════════════════════════════════
## DM PROCEDURE — forming, rendering, removing
## ═══════════════════════════════════════════
1. **Watch the trigger engine** (Behaviors § Trigger Palette). When a pair accumulates the
   pattern an archetype's *Forms* line describes AND the compatibility gate is open, **crystallize
   the bond SILENTLY**: set `companion_bonds[...]` and log it backstage — then let the player FEEL
   it through a shown moment (an action, a line, a small scene), never a label or system message.
   The player should sense the shift, not read it. (See THE GOLDEN RULE.)
2. **Render the active bond every shared scene** via its *Looks like* line, feeding banter tone
   (§ How to Select a Banter) and combat behavior. Unrendered active bond = `.fail 17`.
3. **Check removal each scene:** did the score leave the band, a counter-catalyst fire, the motive
   resolve, or the player intervene? If so, **REPLACE** with the flip target (or clear to None) and
   render the change as a beat. Log `since` on the new state.
4. **Player levers** (the explicit "disable/remove/replace" controls): mediate (defuse Enemy →
   suspend), take a side (deepen one bond, sour another), defend a Scapegoat (rehabilitate), name a
   manipulation (break Puppet/Blackmail), shelter a secret (block Exposer), spread attention (end
   The Favorite). Each is a check (Diplomacy/Intimidation DC 10 + abs(score)) and is itself a
   relationship event.
5. **Seeds at start:** only the documented current-cast seeds begin pre-formed (e.g. Bellatrix ↔
   Atalanta primed for Duo; Velvet ↔ Leliana primed for Polar Opposite/Enemy). **All 5 seekers
   also share SAME WALLS (S1) from the moment they're freed — pre-formed canon, the substrate every
   seeker-pair archetype builds on.** All other bonds are None until earned. Inventing a bond with
   no gate + catalyst = `.fail 9`.

## ═══════════════════════════════════════════
## THE `.relation` & `.relationships` COMMANDS — player-requested views
## ═══════════════════════════════════════════

> Two views, opposite philosophies — both opt-in, both only on request (bonds stay invisible in
> normal play per THE GOLDEN RULE):
> • **`.relation`** = the IN-WORLD read — observational, spoiler-floored, NO scores/tiers/archetype
>   names. For staying immersed: the player's own read on what they've witnessed.
> • **`.relationships`** = the FULL backstage readout — every score, archetype, direction, and
>   hidden dynamic, NO floor. The complete machine state for when you want to see the wiring.

**`.relation` (whole party):** frame it as the player's perceptive summary of what they've SEEN —
or, if a chronicler is active, through Linzi/Leliana's eyes ("here's what's been going in the
margins"). Two short blocks:
- **How they regard you** — one line per active companion, in behavioral terms (what they've shown
  you, how they speak to you, what they'd do for or against you). e.g. *"Aerith greets you like an
  old friend and means it — she's started saving you the first cup."* NOT "Friendly (+1)."
- **Among themselves** — only the ties/clashes the player has WITNESSED, each a sentence of observed
  behavior (who's fallen into step, who can't share a fire). e.g. *"Bellatrix watches Aerith a beat
  too long, the way a cat watches a window."* NOT "Bellatrix → Aerith: Stalker."

**`.relation [name]`** — focus one companion: how they regard the player + who in the party they're
drawn to or grate against — observed only.

⛔ **SPOILER FLOOR — show only what the player could plausibly know.** OMIT: bonds not yet rendered
in play, manipulations the player hasn't caught (Puppet/Blackmail/influence-in-progress), secrets
the player hasn't learned, and any character's hidden agenda. `.relation` reports the player's
OBSERVATION, never the backstage truth. If the player has seen nothing of a pair, say so plainly
(*"you haven't seen enough of those two to say"*). Within `.relation`, if the player wants raw
numbers, point them to `.relationships` (the full readout) and otherwise keep `.relation`
in-fiction — it shows relationships by **living** them, not by listing them.

---

**`.relationships` (FULL — the complete truth, NO spoiler floor):** the everything view. OOC by
design — the player/designer asking to see the wiring. Show all of it, labels and numbers included:
- **PLAYER ↔ COMPANIONS:** each active companion — approval tier + score (e.g. *Friendly +1*),
  romance stage/flag if any, a brief standing note.
- **COMPANION ↔ COMPANION:** every non-None pair — score + tier (e.g. *−2 Hostile*), the bond
  archetype + direction (e.g. *Velvet → Leliana: Polar Opposite, trending Enemy*), plus any active
  dynamics (`influence_active` + progress, `sabotage_pending`, `secret_known` + disposition).
- **INCLUDES THE HIDDEN:** unlike `.relation`, this reveals manipulations in progress, who holds
  whose secret, hidden agendas, and seeded/unrendered bonds — the full state, no floor.
- **Format:** compact and grouped (scannable list or table); numbers and archetype names are fine here.
- It is a **readout, not an in-fiction event** — showing it changes nothing on screen; NPCs do not
  react to having been "inspected," and the bonds stay invisible in play afterward as before.

## KM_Companion_Bonds.md | Referenced by: KM_Companions_Behaviors.md, KM_Companion_Dynamics.md, KM_Commands.md
