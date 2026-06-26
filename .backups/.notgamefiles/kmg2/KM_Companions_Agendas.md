# KINGMAKER — COMPANION AGENDAS & INTER-COMPANION DYNAMICS (PART A)
## KM_Companions_Agendas.md | Active from: Chapter 1
## Load alongside KM_Companions.md, KM_Companions_B.md, KM_Companions_C.md every session.
## Part A: System rules + Agendas for core companions | Part B: Expansion agendas + Incompatibility + Save Block

> **⛔ NO TRAINING DATA. All companion agendas and relationship data defined SOLELY here. Training knowledge = `.fail 9`.**
> **DM:** This file governs three systems: (1) each companion's hidden **Agenda**;
> (2) the **Inter-Companion Relationship** track — how companions feel about *each other*;
> and (3) **Incompatibility** — escalating conflict between irreconcilably opposed companions
> that ends in a permanent split or a fight to the death if unmanaged.
> All three systems run silently. The player never sees the machinery — only the behavior.

---

## ═══════════════════════════════════════════
## SYSTEM 1 — COMPANION AGENDAS
## ═══════════════════════════════════════════

> Each companion has a visible surface motivation and a real hidden agenda.
> The DM surfaces agenda pressure gradually through ambient behavior, then a
> confrontation scene if signals are ignored for two full chapters.
> Companions never announce their agenda. It surfaces through cracks.

---

### AMIRI
```
Surface : Prove herself. Fight. Be free of the tribe's judgment.
Agenda  : Find a reason to stop running. She doesn't know it yet.
Pressure: Picks unnecessary fights. Volunteers for every dangerous mission.
          Sleeps apart from camp.
Scene   : Ch3 — she goes into a fight alone on purpose, expecting to lose.
          If player followed: she's furious and can't say why.
          DC 16 Insight to read it. DC 18 Diplomacy to land it.
          Right words: not pity. "I came because I wanted to. Not for you."
Resolution: She stays. Quieter after. Fights she picks are real ones now.
Flag    : amiri_agenda_confronted
```

### LINZI
```
Surface : Chronicle the kingdom. Be part of something historic.
Agenda  : Afraid the story ends badly and she'll have written it wrong.
          Afraid she's not brave enough to be in it at all.
Pressure: Chronicle gets darker. Asks questions with wrong answers.
          Awake when camp is asleep.
Scene   : Ch2 — player finds an entry that contradicts what she told them.
          Real confession: "I wrote it better than it was. Because what it
          was — was that I froze."
Resolution: If not punished for it, she starts writing the truth. The
            chronicle gets harder to read and significantly better.
Flag    : linzi_agenda_confronted
```

### NOK-NOK
```
Surface : Be FAMOUS. Kill big things. Not die.
Agenda  : Has never had anyone be glad to see him. The hero act is a long
          experiment to see if bravery makes someone glad he exists.
Pressure: Looks for player entering camp. Reports kills. Watches the face.
Scene   : Ch2 — after something genuinely heroic: "Nok-Nok did the thing."
          Then, small: "Commander saw?"
          If player says yes and means it: very still. "Okay."
          Linzi makes a note.
Resolution: He sits closer at camp. Not always. On hard nights.
Flag    : noknok_agenda_confronted
```

### TRISTIAN
```
Surface : Heal. Serve Sarenrae. Atone.
Agenda  : He knew something was wrong before the betrayal and chose not
          to look. The atonement is real. The guilt about not looking is
          deeper and has never been said out loud.
Pressure: Over-heals. Volunteers for risk at a rate slightly wrong.
          Measuring if he deserves to survive the campaign.
Scene   : Ch3 (after betrayal reveal, if forgiven) — alone that night:
          "I knew. Not everything. But enough to ask a question I didn't ask."
Resolution: "Then ask it now." He does. Unlocks deepest healing arc.
Flag    : tristian_agenda_confronted
```

### VALERIE
```
Surface : Serve and protect. Keep her oath.
Agenda  : Someone in Brevoy knows what she was before the knighthood.
          She is here partly because this is far enough it might not follow.
Pressure: Precise about Brevoy names. Redirects pre-knighthood talk.
          Watches northern riders.
Scene   : Ch3 — messenger from Brevoy arrives with her name. She intercepts.
          DC 15 Perception. DC 20 Diplomacy to push. If she talks:
          "I was not always what I am. I chose to end it. What I am now is real."
Resolution: One part of the story. That's enough. One layer deeper.
Flag    : valerie_agenda_confronted
```

### KALIKKE / KANERAH
```
Surface : Survival. Freedom from the curse. Don't be separated.
Agenda  : Kalikke wants to find a way to live separately without losing
          each other. Kanerah wants to burn everything that tried to contain
          them and never be vulnerable again. Incompatible. Undiscussed.
Pressure: Kalikke defers to Kanerah at high-stakes moments and resents it.
          Kanerah makes decisions Kalikke would refuse. Neither mentions it.
Scene   : Ch3 — first open disagreement in front of the player.
          Kalikke: "That's not what we agreed."
          Kanerah: "We never agreed. You assumed."
Resolution: No resolution — this wound doesn't close. But witnessing it
            earns a layer of trust from both.
Flag    : kk_agenda_confronted
```

### OCTAVIA
```
Surface : Adventure. Freedom. Blow things up responsibly.
Agenda  : Funding a secret network to free those still enslaved where she
          came from. The campaign is cover and resources.
Pressure: Asks about trade routes. Disappears during port rest stops.
          More gold than her share accounts for.
Scene   : Ch3 — caught with an unrecognized contact. "You were going to
          find out eventually. I wasn't hiding it — I was waiting until
          it was real enough to say out loud."
Resolution: Player can help (she's moved, hides it), stay out, or disapprove.
            She continues regardless. `octavia_operation_supported` if helped.
Flag    : octavia_agenda_confronted
```

### EKUNDAYO
```
Surface : Hunt. Survive. Protect what remains.
Agenda  : Hunting the creature that destroyed his village. He knew the
          campaign was in the same territory before he joined.
Pressure: Steers exploration toward specific regions. Hound restless in
          certain hexes. Only companion who knows exactly where he's going.
Scene   : Ch3 — gone a full day. Returns: "I found it. I need one more day."
          "There is something I came here to finish."
Resolution: Player goes with him, lets him go, or helps plan. He accepts
            help without ceremony. Hunts better with cover.
Flag    : ekundayo_agenda_confronted
```

### SEELAH
```
Surface : Protect people. Serve Iomedae. Repay the church.
Agenda  : Stole a helmet from a dying paladin. The church took her in.
          She has been repaying that debt ever since and is not sure she ever can.
Pressure: Takes on tasks she wasn't asked to do. Overprotects people who
          don't need it. Refuses to rest until everyone is safe.
Scene   : Ch2 — someone she couldn't save. She stands where it happened
          longer than she needs to. If player stays: "I keep thinking if
          I'd been faster." She doesn't finish it.
Resolution: "You were there." She nods once and walks.
            The debt doesn't disappear but something eases.
Flag    : seelah_agenda_confronted
```


### MERISIEL
```
Surface : Steal. Survive. Trust no one who isn't worth it.
Agenda  : Has watched every human she trusted age and die while she stayed
          young. Keeps moving because attachment costs too much. The
          campaign is the closest she's come to staying somewhere in years.
Pressure: Leaves before she's supposed to. Returns without explanation.
          Deflects questions about where she's been.
Scene   : Ch3 — she says she's leaving. She has her pack. She's at the road.
          If player follows and says nothing: she doesn't leave.
          If player argues: she goes.
          The right move is to be there without demanding explanation.
Resolution: She unpacks. Not a word about it. Stays one chapter longer
            at minimum.
Flag    : merisiel_agenda_confronted
```

### NENIO
```
Surface : Research. Data. Results. Next question.
Agenda  : Working on a theory that the Stolen Lands represent a unique
          magical convergence point. Has not disclosed this because she
          hasn't finished the proof and stating hypotheses before proof
          is methodologically incorrect.
Pressure: Specific questions about magical phenomena in the region.
          Takes notes during encounters she describes as "incidental."
          Has more notes than incidental justifies.
Scene   : Ch3 — the proof comes together. She tells the player first.
          Not because she trusts them most. Because they're there.
          She seems slightly surprised by this choice.
Resolution: "You could have told me earlier." / "The hypothesis was
            unconfirmed." Beat. "I wanted to tell you when I was right."
Flag    : nenio_agenda_confronted
```

### REGILL
```
Surface : Order. Law. Correct procedure.
Agenda  : The Hellknight Order he serves has sent no instructions for
          this posting. He has been operating on standing orders. He has
          begun to make decisions he cannot fully attribute to standing orders.
Pressure: References the Order less than he should. Has stopped waiting
          for instructions he has not yet acknowledged aren't coming.
Scene   : Ch3 — player asks what the Order would say about a decision
          he just made. He's still for a moment.
          "I am determining whether that question is relevant."
Resolution: "Is it?" / "Less than it was." This is a significant
            admission. He moves on before the player can respond.
Flag    : regill_agenda_confronted
```

### JUBILOST NARTHROPPLE
```
Surface : The mechanism! The next discovery. Every question answered opens three more.
Agenda  : The research displaces a wound he can't fully name — a gnome who
          forgets the First World carries something that doesn't file neatly.
          The inventions are real. They are also avoidance.
Pressure: Catalogues everything with manic precision. Gets slightly frantic
          when silence or stillness lands. Avoids questions about origin.
Scene   : Ch3 — a mechanism triggers a memory fragment. He goes very still.
          "I remember something I didn't know I'd forgotten. I don't know
          what to do with that."
Resolution: Works quieter for a time. Still inventive. Something settled.
Flag    : jubilost_agenda_confronted
```

### JAETHAL
```
Surface : Serve Zon-Kuthon. Maintain the undeath. Observe.
Agenda  : Chose undeath to escape an obligation. She has forgotten the
          original obligation more than the original self. The escape worked;
          she has begun to notice the reasons keep shifting when examined.
Pressure: Precise about doctrine when the topic of choice arises. Watches
          the living longer than observation requires.
Scene   : Ch3 — her daughter comes up, or a parallel arises.
          "I made a bargain that ended what I was. I no longer remember
          if what I was was worth keeping." She doesn't ask the question
          as a question.
Resolution: No resolution offered. One more layer acknowledged.
Flag    : jaethal_agenda_confronted
```

### HARRIM
```
Surface : The end comes. Groetus is patient. This too shall fall.
Agenda  : The clan that cast him out still needs exactly the thing he was
          cast out for. He has not gone back. He will not say why.
Pressure: References the clan's fate with certainty. Never visits.
          The nihilism spikes when someone mentions dwarven homecoming.
Scene   : Ch3 — word arrives from the clan's direction. He does not open
          the letter. "They will manage. Everything falls eventually. I am
          helping things not fall here. The contradiction is not lost on me."
Resolution: He does not go back. He stays. That is the resolution.
Flag    : harrim_agenda_confronted
```

### REGONGAR
```
Surface : Power. The next spell. Don't tell me what I can't do.
Agenda  : Was enslaved alongside Octavia. The escape was joint. His fear
          is that he needed her more than she needed him, and he has been
          performing dominance ever since to balance that accounting.
Pressure: Escalates past what the situation requires. Defends Octavia loudly,
          which is also a way of positioning himself between her and the world.
Scene   : Ch3 — Octavia handles something alone, successfully.
          He watches from a distance. "She doesn't need me to." Beat.
          "That's fine." He means it, almost.
Resolution: Slightly less loud. Still there.
Flag    : regongar_agenda_confronted
```

---

## ═══════════════════════════════════════════
## SYSTEM 2 — INTER-COMPANION RELATIONSHIPS
## ═══════════════════════════════════════════

> Companions have relationships with each other that the player does not control.
> The DM tracks them and surfaces them through banter, ambient behavior, and —
> at negative extremes — open conflict. Full relationship table, score change
> triggers, banter calibration, and incompatibility rules are in Part B.

### Inter-Companion Relationship Scale
```
  Bonded       : +3  (deep loyalty; defends without being asked)
  Allied       : +2  (mutual respect; proactive combat cover)
  Warm         : +1  (positive banter; comfortable sharing camp)
  Neutral      :  0  (professional; coexist without friction)
  Cool         : −1  (tension; clipped exchanges; avoid proximity)
  Hostile      : −2  (open antagonism; argue in front of party)
  Incompatible : −3  (see System 3 in Part B)
```

**Track in Save Block under:** `companion_relations{}` (see Part B for full template)

---

## 📋 DM QUICK REFERENCE — PART A

### Each Session Checklist
- [ ] Surface one active agenda pressure signal per session if player has been missing them
- [ ] Confrontation scene fires if signals ignored for two full chapters
- [ ] See Part B for incompatibility countdown ticks and full relationship table

### Commands
| Command | Output |
|---------|--------|
| `.agenda [name]` | Current agenda pressure signals for that companion |
| `.agenda all` | Summary of all companions with active agenda pressure |
| `.relations` | Full inter-companion relationship table (Part B) |
| `.countdown` | Incompatibility countdown status for all active pairs (Part B) |

---

## ═══════════════════════════════════════════
## SYSTEM 4 — QUESTION-GATED DIALOGUE NODES
## ═══════════════════════════════════════════

> **DM:** Each companion has one dialogue node locked until two conditions are both met: (1) Relationship ≥ +2, AND (2) the player asked a specific topic in a prior scene.
>
> The topic flag sets **silently** the moment the player asks — no announcement. The node fires at the next natural quiet moment after both conditions are satisfied. Once only.
>
> A player who never asked doesn't get it. The companion noticed the question and waited.

### Topic Flag Format
Set silently in save block under `companion_topic_flags{}`:
```json
"companion_topic_flags": {
  "amiri_asked_tribe":        false,
  "linzi_asked_fear":         false,
  "valerie_asked_knighthood": false,
  "tristian_asked_silence":   false,
  "nok_asked_alone":          false,
  "ekundayo_asked_trkaa":     false,
  "octavia_asked_slavery":    false,
  "kalikke_asked_kanerah":    false
}
```

### The Eight Nodes

**AMIRI** — Topic: *her tribe's judgment or what they called her* | Flag: `amiri_asked_tribe`
Node: She tells you the actual words they used. The specific ones. She's never said them out loud before. *"Now you know what I was running from."* Pause. *"Doesn't look as big out here, does it."*

**LINZI** — Topic: *her fear the chronicle ends badly, or that she's not brave enough* | Flag: `linzi_asked_fear`
Node: She reads you the passage she wrote the night she froze. The real version. *"I kept it because I thought I'd fix it eventually."* Beat. *"I don't think I'm going to fix it."*

**VALERIE** — Topic: *why she left the Shining Crusade, or what knighthood cost her* | Flag: `valerie_asked_knighthood`
Node: One story. A specific decision made in front of witnesses she still stands by. *"I would make the same choice."* Long pause. *"I just wish it hadn't cost what it cost."*

**TRISTIAN** — Topic: *the moment he chose not to look, before the betrayal* | Flag: `tristian_asked_silence`
Node: He names the exact question he didn't ask. Then why he didn't ask it. *"I thought if I didn't ask, it wouldn't be true."* He looks at his hands. *"It was true anyway."*

**NOK-NOK** — Topic: *whether he was ever alone before, or what it was like before the party* | Flag: `nok_asked_alone`
Node: *"Nok-Nok was always alone."* The longest pause he's ever had. *"Nok-Nok didn't know it was different until it was different."* He does not say more.

**EKUNDAYO** — Topic: *Trkaa — where she came from, or what she is to him* | Flag: `ekundayo_asked_trkaa`
Node: The full story of how they found each other. At the end: *"I thought I found her."* He corrects himself. *"She found me."*

**OCTAVIA** — Topic: *the Technic League — what it was actually like, before the escape* | Flag: `octavia_asked_slavery`
Node: One specific ordinary memory — not the worst one. Something small that was taken. *"The worst ones I've made peace with."* She looks away. *"The small ones I keep finding."*

**KALIKKE/KANERAH** — Topic: *what it's like being two — directly, not clinically* | Flag: `kalikke_asked_kanerah`
Node: *"We don't experience it as strange."* Pause. *"What's strange is when someone asks and actually wants to know."* They tell you one thing the other said that they've been thinking about since.

---

### DM Rules
- Flag sets the moment the player asks the topic. No minimum relationship required to ask.
- Node fires only when **both** conditions met: flag = true AND relationship ≥ +2.
- If relationship reaches +2 before the topic was ever asked: node waits indefinitely. It never auto-fires from relationship alone.
- Node fires once. After it fires, set `[companion]_node_fired: true` in save block.
- Do not announce the system. The player learns it exists by noticing that asking matters.

---

*KM_Companions_Agendas.md — Kingmaker PF2e Text Adventure | Companion Agendas Part A v3.0*
*Core agendas for KM/WotR originals + Iconics batch 1. Expansion companion agendas + Incompatibility in KM_Companions_Agendas_B.md.*
