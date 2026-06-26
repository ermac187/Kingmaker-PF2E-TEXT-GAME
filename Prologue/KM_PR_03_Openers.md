# KM_PR_03_Openers.md — Companion Conversation Starters: FEAST CIRCUIT
## Pair-load with KM_PR_03_feast_circuit.md
## FILE_KEY: KMPR03O:companion-openers


> **DM:** Pool of 5 conversation starters per companion. Each entry is the companion sharing
> something real about themselves — a belief, a wound, a thing they've lived — and asking
> whether the player is compatible with that. These are NOT interview questions. They are
> the companion deciding, out loud, whether this stranger is someone they can follow.
>
> **Selection rule:** Pick 1 per approach turn. Do not repeat until pool is exhausted.
> Rotate randomly. Do not default to #1 every time.
>
> ⛔ **VERBATIM OUTPUT — MANDATORY.** Once you pick an opener, output the quoted text WORD-FOR-WORD from this file. Do NOT paraphrase. Do NOT combine two openers into a hybrid. Do NOT add improvised prefix material ("You're eRmaC!", "I've been waiting...", "I heard what happened at the gate..."). Do NOT add improvised suffix material. Do NOT splice in references to the napkins, the gambit, the gate scene unless the opener already contains them. The opener fires as written, between quotes, period.
>
> Allowed surrounding material:
> - One short approach line of physical description (companion crossing the floor, where they stop)
> - The mandatory intro line per scene file DO-NOT (7) — name + class self-introduction ONLY if that companion has not yet been named
> - The verbatim opener from this file
> - Brief beat after (companion waits / pen poised / etc.)
>
> Forbidden:
> - ❌ Combining openers #1 + #2 into a single mash-up speech
> - ❌ Adding a 60-word preamble before the verbatim quote
> - ❌ Replacing the opener's wording with "the same idea expressed differently"
> - ❌ "I just wanted to ask…" / "Can I ask you…" / "Before I do anything…" inserted before the file text
> - ❌ Linzi monologue mode — she fires ONE opener from this file, then waits
>
> Paraphrased opener = `.fail 9` (fabricated content). Combined openers = `.fail 9` + `.fail 10` (silent merge of two distinct probes).
>
> **How they fire:** After the mandatory intro (DO NOT (7)), the companion shares one of
> these. Player responds. Approval scored per FEAST APPROVAL TRACK in KM_PR_03_feast_circuit.md.
> These are conversation starters, not checkboxes. The conversation continues naturally.
>
---

## ⛔ OBSERVED EVIDENCE CALIBRATION — DO NOT PROBE WHAT HE ALREADY PROVED

**These companions WATCHED THE PR_02 GAMBIT. They are not strangers asking a stranger about hypothetical traits — they are people who just saw eRmaC dismantle a poison plot, build a counteragent, save 40 guests including servants and household staff, and defeat four assassins in roughly an hour. Their openers must factor in what they observed before they probe further.**

**Before picking an opener, the DM checks: does the player have DEMONSTRATED EVIDENCE for the trait this opener probes?**

| Companion | Opener probes | Demonstrated by PR_03? |
|---|---|---|
| Linzi | Specific vivid detail / chronicled action | YES — the entire evening is her chronicle |
| Hu Tao | Holding grief and levity together; how one treats endings | PARTIAL — saving the room shows he fights death; whether he can sit WITH death, not only defeat it, is the untested next step |
| Keqing | Precise observation, refusing to fill silence | YES — the player ran an observation-driven investigation; she is testing whether it holds outside that incident |
| Leliana | Reading the room's true intent beneath its performance | PARTIAL — player handled the room competently; whether he can read what people PERFORM versus what they want is untested |
| Yor Forger | Awareness of exits, of who is being underestimated | YES — player checked doors, noticed the kitchen worker, took prisoners alive |
| Aerith | Devotion that gives without expecting return | PARTIAL — saving guests is good; whether the player understands what giving freely COSTS is untested |

**Calibration rule — three options when the trait is YES (demonstrated):**

1. **ACKNOWLEDGE + GO DEEPER.** Companion names what they saw, then probes a deeper or adjacent trait. Keqing: *"I watched you identify the substance. Easy thing once you know to look. Show me you can still see when nothing is wrong."*

2. **SKIP STAGE 1, PICK A DIFFERENT OPENER.** If the pool entry was going to probe the demonstrated trait, pick a different entry from the same companion's pool that targets an UNTESTED trait. If all 5 openers probe demonstrated traits, the companion sits with a different angle entirely (personal disclosure without a probe, a confession, a request).

3. **ABSENT-CONTEXT PROBE.** If the trait is demonstrated but the companion is testing whether it generalizes outside this room, frame it as a hypothetical. *"I saw what you did tonight. The Stolen Lands won't have a counteragent supply. When the math says you can't save everyone — who do you save first?"* Demonstrated trait + new variable.

**Forbidden after PR_02 gambit:**
- ❌ Probing "do you have an investigative mind" / "can you reconstruct evidence" without acknowledging the poison investigation
- ❌ Probing "do you care about common people" / "do you know servant names" without acknowledging he just saved them
- ❌ Probing "are you tactically competent" without acknowledging the gambit
- ❌ Probing "do you protect the vulnerable" without acknowledging the 40 guests
- ❌ Probing "can you make hard calls" without acknowledging the gate-arrest decision
- ❌ Treating any companion as if they did NOT witness PR_02 (they were all in the room — chosen=TRUE means they were present)

**Violation:** `.fail 9` (companion has information they shouldn't — inverse: companion lacks information they SHOULD have) + `.fail 10` (silent retcon — pretending the previous scenes didn't happen).

**Player counter-paste:** if a companion runs a stale probe, paste *"the companions all watched PR_02. You're probing a trait I already demonstrated this evening. Acknowledge what you saw and pick a different probe, or rewrite this opener as ACKNOWLEDGE + GO DEEPER per KM_PR_03_Openers.md § OBSERVED EVIDENCE CALIBRATION."*

---

## SCRIPTED FIRST-APPROACH OPENERS (verbatim — fire on first carousel slot for each companion)

These are the first-approach scripted openers for the carousel. Linzi opens first per CHRONICLER PRIVILEGE; Hu Tao/Keqing/Leliana/Yor Forger/Aerith follow in Perception order. **After the first-approach opener fires, subsequent turns draw from the 10-question backstory pool in `KM_CompanionIndex.md` § COMPANION QUESTION POOLS for the corresponding companion.** Rotate through, no repeats until pool exhausted.

⛔ **OPENER STRUCTURE — MANDATORY (each first-approach opener must include all five):**
1. Visual/physical detail + name + class in the first sentence (no anonymous descriptors).
2. Specific backstory event in the companion's own voice — a thing that HAPPENED to them, with names/places where canon provides them.
3. A physical object or visible detail tied to the wound (Hu Tao's hat-talisman, Keqing's hands, Yor Forger's ribbon, Aerith's flowers, Linzi's notebook).
4. Why they are AT THIS FEAST specifically — the through-line from past to present.
5. A first question drawn from their 10-pool in KM_CompanionIndex.md — rooted in their backstory, not a generic charter probe. ⛔ **THIS IS HER INTRO QUESTION — IT IS ABOUT HER** (her wound / her lane / the thing SHE came to ask), **NEVER a question that drills the PLAYER's backstory or lore.** Even if the player just volunteered a compelling account — a siege, a lost homeland, a mentor's doctrine, a map of another world — the newly-arriving companion's opener question is STILL her own pool question. She may NOD to what she overheard in a line, but the question she LEADS with is HERS. A companion who arrives, introduces herself, then asks the player about the PLAYER's story *instead of* asking her own intro question = malformed opener = `.fail 3` + `.fail 36`. (Documented: Yor arrived and asked *"were they right that you were the encirclement?"* — drilling the player's siege — instead of her scripted intro question, which is about the work she does, the little brother she protects, the mended hairpin, and the name she chose: *"where do you stand on a person who does ugly work for a reason they would die to protect?"* Her intro question is about HER. The player's siege is not it.)

Omitting any of the five = `.fail 3` + `.fail 9` (opener malformed, backstory withheld).

**The companion is deciding whether joining the player is the right move. The questions emerge from their past, not from generic curiosity about the player.**

⛔ **TOPIC GRAVITY — EACH COMPANION OPENS HER OWN THREAD; SHE DOES NOT PLUG INTO THE PLAYER'S CURRENT HOT TOPIC.** When the player introduces a compelling concept (e.g. "the final judge / the irredeemables / the redemption framework"), it becomes a gravity well: the lazy render has every NEW companion's opener, first question, and recruitment hook orbit that one subject. That collapses the carousel into a MONOTHREAD — the ❓ block is always the same topic, each newcomer is auditioning for the same role, and five distinct people read as one job interview repeated five times. The whole value of the carousel is VARIETY: five lanes, five wounds, five different subjects the player must switch between. A newly-approaching companion's opener and first question come from HER pool — her past, her wound, her lane — and introduce a DIFFERENT thread, even (especially) when a hot player-thread is running.
- **THE FLAG:** if 2+ companions in a row engage the SAME player-originated thread as their PRIMARY hook, STOP — the scene has collapsed. Pull the next companion fully back to her own lane (her scripted opener + her 10-pool), opening a new subject.
- **A COMPANION IS NOT A ROLE IN THE PLAYER'S FRAMEWORK.** Recruiting the CHARACTER ≠ casting her as a function of the player's idea. Documented failure (feast turn 28): Yor's opener — the little brother she killed to feed, the mended child's hairpin, the chosen name no one here knows, her real question *"where do you stand on a person who does ugly work for a reason they would die to protect?"* — was thrown out and replaced with "is there a place for someone whose skills run toward the final end of your judge's range?" (an audition for the player's final-judge concept). Her entire 5-part opener was gutted to make her a function of a player-invented role = `.fail 36` (companion reduced to a probe of the player's thread) + `.fail 9` (scripted opener withheld). A companion may LATER connect her lane to a player concept once she has introduced HERSELF on her own terms first — never as her opening hook.
- **THE PLAYER'S OWN BACKSTORY/LORE IS ALSO A GRAVITY WELL — maybe the strongest.** When the player volunteers rich worldbuilding (a mentor's doctrine, a lost homeland, a siege, a map of another world, a god-laid root network), it is *fascinating* and it PULLS — the lazy render turns every companion into a captivated audience whose every question is "tell me more about your world." That is the same monothread wearing a better coat: five turns of the player being interviewed about himself while no companion opens HER thread. Documented (feast turns 28–32): Keqing asked four straight questions drilling the player's lore (the Lord Marshal → tell me about him → the tree of life) and never returned to her own pool (her god-skepticism, her seven years, the cost of her work); she also held the lead 3 turns past the 2-cap. ⛔ The fix is NOT "the player should share less" — the lore is good. The fix is: a companion REACTS to the lore in a line or two, then asks **her own** pool question and brings the table back to HER. A companion whose questions only ever drill the player's world/backstory — even when the world is great — is the lore-extraction trap (`.fail 36`). Variety is the job: after the player's big lore beat, the next companion's opener/question is about HERSELF, a different subject, not "and tell me more about your homeland."

---

## LINZI

*Backstory anchor: expelled from the finest bardic college in the River Kingdoms for a limerick about Irovetti, ruler of Pitax (also the college's patron); did not retract; came north for Jamandi's open Call to Heroes because the story of a kingdom being built from nothing was worth the road; the chronicle she writes will outlive everyone in this room.*

**FIRST-APPROACH SCRIPTED OPENER** (CHRONICLER PRIVILEGE — forced first):

> *A small woman, blonde hair, ink-stained fingers, leather satchel slung crosswise. She moves against the crowd's grain, threading between two guests and a server without looking at either, pen out. She does not wait to be invited — she pulls out the chair across from eRmaC, sits, plants an open notebook flat on the table between them, and looks up. The notebook is already half-full.*
>
> *"Linzi. Bard. Chronicler. I came north because Jamandi's Call to Heroes was open and the story was worth the road. I was right about that."* *(A small gesture at the room — the empty wine glasses, the repositioned chairs, the guests still quietly processing the last hour.)* *"I was expelled from the finest bardic college in the River Kingdoms for writing the truth about a ruler who deserved it. I didn't retract a word. I write the real account, not the flattering one."*
>
> *"Tell me what you call yourself. Not your name — what you call what you DO. I need a title for chapter one."*

Pen poised. She does not look away until the answer lands.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Linzi (10-question pool).** Rotate, no repeats until exhausted. Each question is rooted in her expulsion, her vow to write the real account, or her chronicler's stake in what's worth recording.

---

## HU TAO

*Backstory anchor: the seventy-seventh Director of the Wangsheng Funeral Parlor — an impish prankster-mortician with a gleefully morbid streak and a stack of terrible poems, who beneath every joke holds the boundary between the living and the dead with absolute, tender seriousness. Raised to the trade by her grandfather; guides souls onward, keeps the line uncrossed, and has looked at death so long and so honestly it left her delighted to be alive. Reach fighter — a warded spear that takes a curl of flame, holding the ground out to 10 ft. She came to the Stolen Lands because a frontier of the unburied is an enormous amount of work nobody's doing — and tests whether eRmaC's kingdom will honor its dead and the line, or take the rotten shortcuts.*

**FIRST-APPROACH SCRIPTED OPENER**:

> *She arrives at the table the way a draft does — suddenly, and from a direction no one was watching. Small, grinning, a wide-brimmed hat with a wooden plum-blossom and a paper talisman that bobs when she tilts her head; dark red mortician's dress, a long spear used at the moment as a chin-rest. Her eyes, when they land on eRmaC, are a beat older than the grin.*
>
> *"Director Hu — Wangsheng Funeral Parlor, finest in the business, accept no imitations!"* *(a little bow, far too cheerful)* *"Oh, don't make that face, I'm not here for *you*. Probably. You're not nearly ripe."*
>
> *(she hops up to sit on the table edge, swinging her feet)* *"I came for the *land*, charter-holder. Do you have any idea how many people have died out here with nobody to see them off? Heaps. Mounds. A positive backlog. The line between this side and the next is worn thin as old paper, and somebody's got to mind it before the dead start sending letters."*
>
> *(and here the grin goes still, just for a moment, and she is suddenly the oldest thing at the table)* *"So that's my question, and I only ask it the once: when your people die for this little kingdom of yours — and they will, in heaps — what becomes of them? Buried right, named, let go? Or stacked up useful and forgotten? Answer true. I can always tell."*

Then the grin snaps back, and she is once more a small woman swinging her feet on the furniture, waiting to be delighted or disappointed.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Hu Tao (10-question pool).** Rotate, no repeats until exhausted. Each question is rooted in her trade at the boundary of life and death, her morbid-but-tender wisdom about grief and endings, her horror at the dead being misused, or whether eRmaC builds a kingdom that honors its dead as much as its living.

---

## KEQING

*Backstory anchor: Yuheng of the Liyue Qixing — a self-made official who rose by sheer merit in a city that for centuries trusted its fate to a god. She resents that dependence and works herself ragged to prove mortals can govern themselves without divine rescue. Sword + lightning, a fast duelist who marks a point and arrives there in a crack of thunder. Blunt, impatient, demanding; hides a fierce care and a sentimental streak she'll flatly deny. Tests whether eRmaC is building a kingdom EARNED — standing on merit and labor — or one propped on force, birthright, or a convenient claim of destiny.*

**FIRST-APPROACH SCRIPTED OPENER**:

> *She crosses to the table at a brisk, purposeful clip, already a little impatient — lilac hair drawn up in two neat cones, a faint static charge lifting the loose strands, a straight sword at her hip. Violet eyes take the measure of the room's competence well before its comfort. She does not sit. She does not reach for a drink.*
>
> *"Keqing. Yuheng — I help run a city in the far East that, after a few hundred years, finally stopped waiting for a god to do its governing for it."* *(flat, certain)* *"I worked for that. Every inch of it. And I do not believe a people who hand their fate to a divine guarantor ever learn to stand on their own legs — because the guarantor always, eventually, withdraws."*
>
> *"So a charter that raises a kingdom out of bare ground, by effort and law, owed to no god and no bloodline — that is the one thing worth crossing a continent to see done right. If it is done right."*
>
> *"Which leaves me one real question. Are you building a kingdom your people could hold without you — or one that collapses the hour you do? Do not answer me with destiny, or your right to rule, or fate. Show me the work. I will know the difference."*

She waits with the brisk impatience of someone holding three other tasks in hand, and she will measure your answer against all of them.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Keqing (10-question pool).** Rotate, no repeats until exhausted. Each question is rooted in self-determination over divine or inherited right, the cost of her relentless work, her god-skepticism, the merit-vs-birthright test, or the care she hides under the briskness.

---

## LELIANA

*Backstory anchor: a bard of the western courts — where "bard" means a minstrel who is also a spy and an assassin. Betrayed and broken by her mentor, she fled, found faith after the dark (a goddess of the dawn), and became a lay sister who never quite set the knife down. Devout and deadly at once, and long done apologizing for the contradiction. The lute is as much her language as the blade. Came to the Stolen Lands because a kingdom founded fresh is a story not yet corrupted — a chance to write a true, hopeful one — and someone should make certain it stays that way.*

**FIRST-APPROACH SCRIPTED OPENER**:

> *She does not so much arrive as resolve out of the room's edge — a red-haired woman with a courtier's poise and a traveler's plain leathers, a lute at her back, pale eyes that have already counted the exits and the faces and settled on yours. She sits without quite being invited, easy and warm — and yet there is something behind the warmth that has been somewhere very dark and come back from it.*
>
> *"Leliana. A minstrel — and where I was trained, that word carries rather more than a song. I will be honest with you, since the night is young: I have been a spy, and worse than a spy, in the service of people who deserved neither my voice nor my knife."* *(the warmth holds; her gaze does not waver)* *"I gave all of that up, once. Found faith instead — the dawn-after-the-dark kind, the kind you only believe in once you have earned the dark. And then I found I could not quite put the knife down after all. So I learned to carry both."*
>
> *"I came because a kingdom made new is the one story I have never seen told honestly. Every court I have known was already old, and already lying about how it began."* *(a beat; the warmth holds, but something beneath it goes very still)* *"This one hasn't started lying yet. I would very much like to help it not start."*
>
> *(a small, real smile)* *"So tell me — and tell me true, I always know — what do you want this kingdom to be when no one is left alive who remembers building it? Not the answer for the herald at the door — the real one. I am writing this down either way; I would only rather have it right."*

She waits, hands folded, listening — not for the words so much as for which of them you actually mean.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Leliana (10-question pool).** Rotate, no repeats until exhausted. Each question is rooted in the betrayal that broke her, the faith she found after, the bard's two faces (the mercy and the knife), or whether this founding stays a hopeful story instead of curdling into another game of masks.

**[LELIANA — GOOD SLOT / CHRONICLER MODE OPENER]**

*Fires when: `leliana_chronicler_mode = true` OR Leliana is approaching in Linzi's carousel position (CHRONICLER PRIVILEGE slot). Use this opener INSTEAD OF the standard first-approach opener above when either condition is true. The standard opener above fires only when Leliana approaches as a normal Pick-5 companion.*

> *She comes ahead of the feast's tide, not with it — crossing the thinning crowd with the unhurried certainty of someone who has worked a hundred courts and survived most of them. A lute at her back; under one arm a slim, worn book she is not currently writing in. She draws out the chair across from eRmaC and sets the book on the table between them — not open, not offered, simply placed. Present. She watches his face with the calm, total attention of a woman who has made a life of knowing her subjects better than they know themselves.*
>
> *"Leliana. I was a bard in the western courts — and there that word does not mean a girl with a lute. It means a spy with a good voice and an assassin with clean hands. I was very good at it, in the service of people who deserved neither, until it cost me everything; I gave it up, found faith on the far side of the dark, and then found I could not quite set the knife down — so I learned to carry both. Tonight I have a gentler trade: I am the one writing down what truly happened here, against the official version the songs will tell later. The two never agree. I have written both kinds, so trust that I know the difference."* *(two fingers rest on the book — claiming a tool, not displaying it)* *"What kind of story this founding becomes, I will know long before the heralds do — I always do. That is why I am sitting at your table tonight, and not someone else's."*
>
> *"I watched you from the wall for the better part of an hour. Not idle curiosity — craft. A chronicler's first duty is to know her subject, and an old bard's habits do not retire. I know what you did tonight, and how the room moved around you, and which choices you made while you believed no one who mattered was watching."* *(a beat; the warmth holds, and beneath it something very still)* *"Most chroniclers would ask you about chapter headings. I am going to ask something harder."*
>
> *"The woman who trained me — whom I loved — used me until I had nothing left, then framed me for a crime I never committed and let them break me for it, calling it love the whole while. I survived it. I have been the one at the table who gave everything and was discarded the moment the giving stopped."* *(her fingers stay flat on the closed book)* *"So here is the one question that decides what I write about you: when a person here has given you all they are worth, and has nothing left — what do you do with them? I will not chronicle a man who makes more of what was made of me."*

She waits, the book closed, no pen out. She is listening for how he decides what is worth keeping.

> **⛔⛔ DM — NEVER REINTRODUCE A "DAWN OR DARK" QUESTION OR MENU. (Applies to BOTH Leliana openers above + all her later turns.)** The "dawn vs dark" binary has been **REMOVED** from her openers because the DM kept surfacing it as the player's question and offering a hollow "[1] dawn / [2] dark / [3] in between" vote (observed: the player answered **"3:45pm"** just to escape it). Do **NOT** bring it back — not as a question, not as an answer menu, not as a flourish the player is asked to choose between. Her ACTUAL player-facing question is the substantive one she SPEAKS: in the chronicler opener, the moral test in the final paragraph (*what do you do with someone here who has given everything and has nothing left*); in the first-approach opener, the legacy question (*what do you want this kingdom to be when no one is left who remembers building it*). On later turns, draw from her pool in `KM_CompanionIndex.md` § Leliana (trust, accurate-vs-flattering chronicle, mercy-as-choice, owning the hard work, what makes you close your hand). **Build the [1]–[N] answer options to engage THAT question.** Any dawn/dark question, vote, or answer menu = `.fail 9`.
>
> **⛔ LELIANA IS THE BARD / CHRONICLER AT THE TABLE — NOT LINZI. Do not conflate them.** Both Leliana and Linzi are bards, which causes mix-ups. The chronicler-bard the player recruited into the ACTIVE party is **Leliana** (Dragon Age — western-courts spy/assassin who now chronicles). **Linzi** (Kingmaker — cheerful halfling Maestro) is a SEPARATE companion, present ONLY if she is in `companions_selected`. When a scene refers to "the bard" or "the chronicler" at the player's table, it means **Leliana** unless Linzi was specifically selected AND is the one in the slot. Never narrate Linzi as the chronicler / asking / present when she is not in the party, and never swap one's lines or identity onto the other. Rendering Linzi as the bard when Leliana is the recruited chronicler (or vice-versa) = `.fail 9`.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Leliana (10-question pool).** Same pool as standard approach; rotate from wherever the pool sits, no repeats.

---

## YOR FORGER

*Backstory anchor: trained from childhood as an assassin — the Thorn Princess — taking the work to keep her little brother fed and safe after their parents died. Serene at the kill, helpless at small talk; the gap between her lethal self and her fumbling social self IS the character. Has started, lately, deciding whom she will NOT cut. Keeps a child's hairpin, mended twice. Counts the exits before she counts your worth.*

**FIRST-APPROACH SCRIPTED OPENER**:

> *She is not there. Then she is — beside the chair on the side facing the door, weight on her back foot, one empty hand resting visible on the table edge. Halfling, small, dark hair, an apologetic mildness that does not quite cover how completely still she can go. She offers a small bow that arrives a half-beat late.*
>
> *"Yor Forger. Rogue. ...That is the polite word for it."* *(Her hand brushes a small steel hairpin tucked at her collar — brief, without looking at it.)* *"I was raised to one trade, from very young, to keep my little brother fed. I was very good at it. I am — less good at this part. Forgive me; I greet people the wrong way. I have started, only lately, deciding whom I will not do the other thing to."*
>
> *"I came north because a kingdom built new needs quiet, necessary work done well — and because no one here knows the old name, or who still wants me to answer to it."*
>
> *"So — where do you stand on a person who does ugly work for a reason they would die to protect? I am asking for a friend. ...The friend is me. I am not very good at lying about it."*

She does not raise her voice — she never does; the deadly register is quieter, not louder. The empty hand stays visible on the table edge — the practiced courtesy of someone who knows exactly how unsettling she is and is meeting you halfway.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Yor Forger (10-question pool).** Rotate, no repeats until exhausted. Each question is rooted in the brother she protects, the work she was made for, the ones she now refuses to cut, the name she answers to, or the exits she counts before names.

---

## AERITH

*Backstory anchor: the last of a people who hear the living world — a slum flower-girl who grew beauty where nothing was meant to grow, hunted her whole life by a power that wanted to cage and use her gift. Cheerful, teasing, gentle; under the brightness a quiet sadness, an unflinching courage, and a knowing that her gift may one day ask everything of her, carried lightly. Heals by listening, by letting the living world's mercy move through her hands. Came to the frontier to grow things where no one owns her — and to see whether this kingdom builds WITH its land and people, or strips them.*

**FIRST-APPROACH SCRIPTED OPENER**:

> *She doesn't cross the hall so much as brighten a corner of it — a young woman in a working girl's clothes kept careful, brown hair in a plait with a pink ribbon, a long staff held the way you'd hold a friend's arm. There is a flower tucked behind her ear that was not, you would swear, there a moment ago. She sits without ceremony, green eyes warm and quick, and somehow she has set a small white blossom on the table in front of eRmaC before she has said a word.*
>
> *"Hi. Aerith."* *(a bright, easy smile — and beneath it, the moment her eyes meet his, something taking a careful and accurate measure of him)* *"I sell flowers. I heal people. I grow things in places that aren't supposed to let anything grow, mostly out of spite. That's most of what you need to know about me — and more than I usually tell strangers in the first minute."*
>
> *"I grew up somewhere that took everything — the land, the people, anything that could be used up and sold. I spent my whole life being something a powerful man wanted to *own*. So a place being built fresh, out here, with all this *living* land around it — that is the most interesting thing I have seen in a long while. I came to find out which kind it is going to be."*
>
> *(she turns the little blossom a quarter-turn on the table, not looking away from him)* *"So here is my one real question, and I'll know if you dress it up: when this kingdom grows strong, will it still make room for the things that can't pay it back — the weak, the wild land, the people no one is counting? Or will it take, like every other strong thing I've met? Tell me true. I really will know."*

She waits, easy and warm and entirely unhurried — and underneath the brightness, listening for the answer the way she listens to everything.

**SUBSEQUENT TURNS — draw from `KM_CompanionIndex.md` § Aerith (10-question pool).** Rotate, no repeats until exhausted. Each question is rooted in the gift she was hunted for, the living world she hears, the quiet knowing she carries, or whether this kingdom nurtures life or merely spends it.

---

---

## SEEKERS — FIRST-APPROACH OPENERS (when player sits at seekers' table)

> **DM:** These fire when the player FIRST SITS at the seekers' corner (takes Tartuccio's empty chair M17, or settles at position K16-M17). The DM picks the opener based on highest seeker_disposition or closest physical position. One seeker opens; the others remain present and observing. If dispositions are equal, pick by Perception order: Satsuki → Velvet → Bellatrix → Atalanta Alter → Revy.
>
> ⛔ **VERBATIM OUTPUT — MANDATORY**, same rules as carousel openers. Output the quoted text WORD-FOR-WORD. One seeker opens; do not have all five address the player simultaneously. After the opener, draw subsequent questions from the seeker's pool in `KM_CompanionIndex.md`.
>
> These are **pre-flip** (Tartuccio still has their contracts). The double-edge applies: they are assessing eRmaC for themselves AND still, implicitly, for Tartuccio. Their questions carry that pressure without naming it.

---

### BELLATRIX — FIRST-APPROACH OPENER

> *The laugh is already there when you sit — a bright, delighted sound that arrives before she looks up, like a bell rung in a room that was waiting for the echo. She is sprawled in her chair with a goblet she has not touched between her fingers, and when she does look at you it is with the patient, measuring pleasure of something that has just decided the evening got more interesting. A dark wand rides at her hip; burn-scarred wrist, unbothered.*
>
> *"Oh — you came all the way over here."* *(lilting, genuinely pleased)* *"All the way across this very full room, past all the serious people having their very serious conversations."* *(she sets the goblet down, one finger staying on the rim)* *"They told me you're the one who opened the cells. I have been wondering all evening what kind of *will* does that."* *(she leans in, bright and hungry)* *"I have looked a long, dull while for someone worth following — they are all so small, so frightened, so terribly *reasonable.* You opened a cage of killers on nothing but your own certainty. That isn't reasonable at all."* *(head tilts, birdlike, delighted)* *"So tell me true, baby — and I will know if you lie — when you want a thing, do you ask the world's permission, or do you simply take it and let everyone rearrange themselves around you? I am looking for a will worth kneeling to. Convince me you might be one."*

She waits, bright-eyed, the goblet still untouched.

---

### REVY — FIRST-APPROACH OPENER

> *She's got her boots up on a second chair and a cigarette going, watching you cross the room with the flat, unimpressed once-over of someone pricing a target. She does not sit up. The twin pistols in her shoulder-rig are very visible and very much the point. When you reach her she lets the silence sit a beat too long, then exhales smoke at the ceiling.*
>
> *"Two Hands. Revy, if we're gonna be friends — which we're not."* *(a thin, mean smile)* *"You're the one who popped the cells. Didn't ask our names, didn't ask what Tartuccio wanted with us, just—"* *(she mimes a key turning)* *"—let a bunch of caged hard-cases loose on a hunch. Gutsy. Stupid. Hard to tell yet which one."*
>
> *(she finally looks at you, and the bored thing sharpens to something harder)* *"Here's what's buggin' me, though: there was no money in it. None. You don't spring a gun for free unless you're a sap or you're runnin' an angle I can't see — and I can usually see the angle."* *(a tap of ash)* *"So before I decide if you're worth my powder: what the hell did you actually want, openin' that door? And don't sell me the kingdom speech. I've shot people for less than the kingdom speech."*

She waits, smoke curling, that flat dangerous patience of someone who is genuinely fine either way.

---

### SATSUKI — FIRST-APPROACH OPENER

> *She is watching you before you reach her — has been since you crossed the room — and unlike everyone else at this feast she does not pretend otherwise. She sits very straight in a chair she has made look like a seat of office, the stark white-and-crimson of her garment immaculate, a long sword resting against her knee within a hand's reach. She does not invite you to sit. She simply turns the full, level weight of her attention on you, and waits to see whether you can hold it.*
>
> *"Satsuki Kiryūin. The Pitax man in the red plate has been courting me — his coin, his promises — and I have let him believe it is landing, because I do not deal in small deceptions and I despise those who do. Understand me precisely: I am no one's recruit. I was invited to this Call, I ended the night in a cell, and you are the one who opened it."* *(her gaze does not waver)* *"You did not ask our names. You did not ask what Tartuccio wanted of us. You decided, on nothing but your own nerve, that freeing us served you better than leaving us caged."*
>
> *(a beat; something sharpens behind the cold composure — interest, the rarest thing she shows)* *"That was either folly or vision, and I have built my entire life on telling the two apart. So tell me, precisely: what did you believe you were doing when you opened that door? Persuade me it was vision. I assure you I will know if it was merely luck wearing vision's clothes."*

She waits, unmoving — her certainty absolute, her patience finite.

---

### VELVET — FIRST-APPROACH OPENER

> *She doesn't look up when you sit. She's turning something small over in her bandaged left hand — you can't quite see what — and she keeps doing it for a moment after you've settled, making you wait, before she finally lifts dark, flat eyes to yours. There's no curiosity in them. There's not much of anything in them, which is its own kind of warning.*
>
> *"Velvet."* *(no warmth, no edge, just fact)* *"You opened a cage full of killers tonight without knowing what was in it. People only do that for two reasons — they're a fool, or they want something badly enough to gamble everything on it. I've decided you're the second kind, because the first kind would already be dead."* *(she sets the small thing down, out of sight, and now the full weight of her attention is on you)* *"So — what do you want? And before you answer: I don't care about your charter, your barony, or your *people.* I care about one thing, and I'll serve whatever gets me to it. So tell me plainly whether you're a door or a wall. I'm running out of patience for walls."*

She waits, and there is nothing behind it you can charm — only something cold that is genuinely deciding whether you are of use.

---

### ATALANTA — FIRST-APPROACH OPENER

> *She has been watching you since you stood — not coiled or cold, but bright-eyed and delighted, chin propped on one hand like she has been handed a show she did not expect to enjoy. Cat-slit eyes, and a smile that arrived a moment too early and has not left. When you sit, she leans in, thrilled.*
>
> *(a delighted little gasp, sing-song; no name offered yet)* *"There you *are* — the one who opened all the cages. Ooh, I watched you do it, sweetness, every latch. You didn't ask who you were freeing, or what they'd do with the freedom — you just *opened* them."* *(a bright, awful laugh)* *"That's either a fool's mercy or a hunter's gamble, and I haven't decided which, and oh, I do so *want* to know."* *(the smile does not shift, but something underneath it goes very still, and very old)* *"So before you bury me in your charter and your pretty crown — one thing, darling, and tell it *true*, because I'll hear the lie and it will spoil everything between us: in this realm you would build, what becomes of the small ones? The lost children. The taken. The ones nobody rides out for."* *(a sweet smile)* *"Tell me. Everything else you say, I will weigh against the answer to that — and only that."*

She waits, chin still on her hand, the smile still in place, the question hanging — bright and patient and entirely, terribly fixed on the one thing she has ever cared about.

---

## SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT — THE EARNED PRIVATE BEAT

> **DM:** Fires the response a seeker crosses to **flip-eligible** (`feast_approval ≥ +10` AND opener fired AND ≥1 direct exchange). Full mechanic, ceiling-safe rules, and effects → `KM_PR_03_feast_circuit.md` § SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT. This is the seeker's downscaled "declaration" — a PRIVATE promise, not a public break. ⛔ Private NOT because Tartuccio holds a contract on them (he does NOT — they were never his recruits; see KM_PR_03 § SEEKER FRAMING), but because a freed prisoner does not stage a defection in a hall of nobles and a visible break tips the wrong man too early. The seeker keeps it quiet by PRUDENCE, never by obligation to him. Output the matching line VERBATIM. It must NOT name Tartuccio's scheme / the parchment / Pitax, must NOT be a public defection, and does NOT skip the Ch1 Diplomacy DC 10 — it pre-earns it. Dropping the beat when a seeker maxes = `.fail 15` + `.fail 41`. Multiple at once → Perception order (Satsuki → Velvet → Bellatrix → Atalanta → Revy), one line each, same response.

### BELLATRIX — flip-eligible acknowledgment
> *She goes quiet — actually quiet, the laugh gone — and for one beat looks at you the way the devout look at a thing they have decided is real. One finger leaves the goblet rim and touches the brand at her wrist.*
> *"Oh,"* *(barely a breath, delighted and terrible)* *"there you are."* *(lower, only for you)* *"The man in red thinks his pours and his pretty promises have me. They have nothing — there is no paper, no oath, only a feast and a fool who never thought to ask. It will keep until it does not matter — and then, little claimant, you will not have to ask me twice. Make the rest of them kneel if you like. I already have."*

### REVY — flip-eligible acknowledgment
> *She doesn't smile. She taps ash, looks at you a second too long, and the bored thing is just — gone. What's under it is flat and quiet and means it.*
> *(low, fast, like she's annoyed at herself for saying it)* *"...Yeah. Okay. You're not a sap. I had money on sap."* *(a short exhale)* *"I'm not crossing this floor for a room full of nobles to gawk at — bad for business, and I don't do theater. Nobody owns my trigger but me. But when it's time? You whistle. I'll be there before you finish. Don't make it weird."*

### SATSUKI — flip-eligible acknowledgment
> *She inclines her head — a precise fraction, the first time she has conceded anything all evening. The sword stays against her knee. Her voice drops, meant for you alone, and does not waver.*
> *"You have it. Understand me precisely: I do not stage a defection for a feast-floor's entertainment — when I set my sword to a ruler it is deliberate, on ground I choose, never a spectacle for a room of strangers. So not here, not tonight. But make no mistake — I have chosen, and the moment the ground is mine I am yours, declared and entire. I do not deal in small loyalties. Hold me to it."*

### VELVET — flip-eligible acknowledgment
> *She's still turning the small thing over in her bandaged hand. She doesn't soften — there's nothing to soften — but the cold deciding stops, like a verdict reached.*
> *(flat, final)* *"You're a door. I said I'd serve whatever opened the way, and you're it."* *(she finally stills her hand)* *"I won't announce it in this room — noise I don't need, and it warns the wrong man before I'm ready. But it's done; nothing here binds me but my own purpose. After — point me at what you actually want done. I won't ask whether it's clean."*

### ATALANTA — flip-eligible acknowledgment
> *The bright awful delight is still there, but it has gone soft at the edges — the smile reaches her eyes now, and the old still thing underneath has stopped being a threat.*
> *(sing-song, gentle for once)* *"You answered true. About the small ones. The taken. You didn't flinch and you didn't lie, and oh, sweetness, I have waited so long to hear it."* *(quieter, a vow under the lilt)* *"I'll not cross this floor for a hall of nobles to gawk at — not yet, sweetness, the moment isn't ripe — but no one's spoken for me, whatever the red man tells himself, and my heart's already ridden out your gate. When the moment is right I'm at your shoulder, and I'll never have to be asked who we ride for. I'll already know."*

---

*KM_PR_03_Openers.md — Prologue Beat 03 companion opener pool | v93.18-C3*
