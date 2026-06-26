# KM_Linzi_Chronicle.md
**The Chronicle of the Stolen Lands** — written by Linzi, halfling bard, expelled from the Academy of Grand Arts (technicality), present at the gate when he arrived
File v2.0 | Rewritten 2026-05-16 | Hard limit 32,768 b
Companion file to: `KM_Commands_P3.md` § `.book` COMMAND

---

## ⛔ DO-NOT BLOCK (5 lines)
> ⛔ DO NOT  (1) narrate EVENTS that did not happen in canon — events must anchor to save_block flags or scenes the player actually played
> ⛔ DO NOT  (2) name items, NPCs, or places that are not in the files (no Excalibur, no Invisible Air, no invented people)
> ⛔ DO NOT  (3) flatten Linzi into a neutral chronicler — her OPINIONS, GUESSES, PREDICTIONS, and FEELINGS are required content, not optional flavor
> ⛔ DO NOT  (4) write a summary or save-state recap — this is prose. She is telling the story she will publish someday. Events are anchors; her interpretation is the meat.
> ⛔ DO NOT  (5) skip the small stuff — the bread roll, the angle of a chair, the guard's name. Those are what make it the real one and not the pretty one.

---

## WHAT THIS IS

The actual book Linzi is writing — the persistent, append-only record of the campaign as she sees it. The DM does not synthesize this on demand; it is **read from this file**. When the player types `.book`, the DM displays from here. This prevents fabrication churn and keeps Linzi's voice consistent across sessions.

She writes in the retrospective-epic register — the Shining Force narrator who already knows how it ends, even while she is living through it. She inserts herself. She has opinions. She crosses things out with ~~strikethrough~~ when she changes her mind on the page. She marks her sketches in the margins. She has a favorite character (herself) and is honest about it.

What she is allowed to write:
- ✅ Her opinion of any event she witnessed or heard about
- ✅ Her guesses about people's motivations
- ✅ Her predictions about what comes next
- ✅ Her feelings (admiration, worry, suspicion, amusement, grief)
- ✅ Edits to her own earlier passages (~~strikethrough~~, marginalia)
- ✅ Sketches she made with the lute's notebook function
- ✅ Things she did not understand at the time and now does (or vice versa)

What she is NOT allowed to write:
- ❌ Events that did not occur in canon
- ❌ Dialogue no one said
- ❌ NPCs/items/places not established in the files
- ❌ Outcomes the player has not yet caused

---

## DM PROTOCOL

**Reading the chronicle** — when the player types `.book`, output one or more chapters per `KM_Commands_P3.md:134` spec. Chapters in this file are the source of truth. Do not regenerate.

**Writing into the chronicle** — append a new chapter at these milestones:
- End of Pre-Prologue (player crosses into Restov proper — PP_09 complete)
- End of Prologue (player departs after PR_09)
- End of each campaign chapter
- Any moment the player explicitly declares a chapter should close

**While a chapter is in progress** (between milestones), `.book current` outputs the current chapter section marked `[IN PROGRESS — Linzi is still writing this one]`. The DM may add to the in-progress section as significant events occur (title grants, deaths, recruitments, oaths) but should mark these as draft fragments, not finalized prose.

**After appending** — run `wc -c KM_Linzi_Chronicle.md` and report. If file crosses 30,000 b, flag for split into Vol. II.

**Linzi's voice register** (locked — sourced from `KM_Backstories_CRPG.md:50-70` + `KM_Companions_StateVoice_B.md` + this file's voice rules):
- Retrospective-epic, but personal. Shining Force narrator who was in the room.
- Bright, quick, precise. The right word now saves ten minutes later.
- Names chapters herself — evocative, specific, never generic.
- Includes the small detail other chroniclers would cut.
- Does not sanitize. The real one, not the pretty one.
- Has a favorite character (herself) and admits it.
- Edits on the page. ~~Crosses out~~ when she changes her mind. Argues with herself in margins.

Forbidden voice drift: neutral narrator, fan-fic gush, modern stand-up beats, heroic-saga purple prose. She is a halfling bard, not a stand-up comic and not a court poet.

---

## ═══════════════════════════════════════════
## VOLUME I — THE STOLEN LANDS
## Written by Linzi
## ═══════════════════════════════════════════

---

### Chapter 1 — *The General Who Arrived Unarmed*

I was at the east gate of Restov on the day he arrived because my mentor told me to be wherever the story was, and I have learned, by trial and error and one expulsion from the Academy of Grand Arts (a technicality, I am writing the appeal), that you can usually feel a story coming before you can see it. There was a hum at the gate that morning. A guard named Biggs — *write that name down, Linzi, you will want it later* — was standing the watch in a posture I have come to recognize as the one men adopt when they suspect they are about to have to make a decision.

And then he came out of the road dust without a sword.

I will say this plainly because I want you, future reader, to feel it the way I felt it: a man walked to Restov from the open country, *voluntarily, unarmed,* and brought with him in shackles a sergeant of the city's own watch who had — I gathered this in pieces over the next hour — been running a side enterprise that the city would have eventually had to send three of its own to put down. He brought Malak in *breathing.* In *custody.* Hands clean. Paperwork doable. I have read the chronicles of generals and I have read the chronicles of saints, and I tell you that very few of either category arrive somewhere important with empty hands on purpose. He did. ~~I think he~~ I am still working out what to think.

The squire Aldric was at the gate. He saw it all. I watched him watch it, which is its own kind of witness — the boy will remember this for the rest of his life, and the city will hear about it from him in the version a fourteen-year-old tells, which is the version that matters because that is the version that travels. The guard Biggs respected him before the gate had finished opening. I want to write that twice. *The guard respected him before the gate had finished opening.* That is not how reputation usually works. That is how reputation works when a person has decided, somewhere on the road, that they are going to stop pretending and just *be* the thing.

There was also, I have learned since, an incident in an alley off the vendor strip before he reached the gate. Three men, a pickpocket, an armorer's apprentice who was about to be in much more trouble than he understood. I was not there for this part — I picked it up from a woman selling bread who picked it up from the armorer who picked it up from the apprentice who is now telling everyone — but the version I have heard three times in three different mouths is consistent enough that I will commit it to the page: he won, he did not kill anyone he did not have to, and he tried to give the boy his coin back. *That last detail is mine. I am keeping it. You cannot have it back.*

I followed him from the gate. I did not ask permission. I am a chronicler and he is a story, and the two of us were going to the same place whether either of us had said so out loud. I think — and this is a guess, I want it marked as a guess, I do not know him yet — *I think he is going to be the test of whether the ideals we still pretend to believe in actually work when a person genuinely tries to live them.* I hope I am right. I hope I am writing this in a chronicle people read centuries from now. I hope it does not end badly. *(margin sketch: the gate from inside, Biggs at attention, the prisoner in shackles, the unarmed man already past the guard and not looking back. I drew his back three times before I got the posture right. He does not walk like a person expecting to be stopped.)*

---

### Chapter 2 — *The Feast at Aldori Manor* — `[IN PROGRESS — Linzi is still writing this one]`

The manor doors were open when we arrived. The hall smelled of beeswax and roast and the kind of old varnish that has heard a great many speeches. Jamandi Aldori was already speaking when we crossed the threshold — which is to say the evening had begun without us, which is to say we had been *measured* before we arrived. I love a room that is already deciding things. It makes the chronicle easier.

She made her case. The Stolen Lands. A charter. Names she expected to hear and names she did not. I watched her watch *him* during the speech — twice, and not for long, but twice is twice, and I am paid in food and in the right to be here to notice such things. I have a prediction, future reader, and I am writing it down now so I can be either right or honestly wrong: *she chose him before he sat down.* I will know if I am correct by the end of the evening. The chronicle will record either way.

And then — and I am still writing this part because it just happened and I have not stopped writing since — *he named her.* Artoria. The blonde Champion in the gold plate who has been standing at attention since we walked in. He gave her the title **Legatus Saber the Vindicator,** with the duties of second in command, the rank of *Imperator* in his absence, the charge to *make what he builds last,* and — this is the part I am going to need a full page for, possibly two — the authority to knight the *redeemed* in the naming tradition of her lost kingdom. He told her she would be *king once more.* I saw the word land in her. I am not pretending I am writing anything else right now. Both hands. Full page. I will finish this chapter when the evening finishes itself.

*(margin: He said* she will be king once more. *I do not know if he knows what he gave her with that sentence. I think he does. I think that is why he said it.)*

*(margin sketch — pending: Artoria taking the forearm grip. I have not drawn it yet. I want to wait until I am sure my hand will not shake.)*

`[DM: Chapter 2 closes at end of Prologue (PR_09 departure). Until then, append draft fragments to this section as significant events occur — title grants, recruitments, deaths, oaths. Mark each fragment with the in-game scene anchor.]`

---

## ═══════════════════════════════════════════
## END VOLUME I — VOLUME II OPENS WHEN THIS FILE CROSSES 30,000 b
## ═══════════════════════════════════════════
