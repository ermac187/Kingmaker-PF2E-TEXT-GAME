# KM_Leliana_Ballads.md — LELIANA BALLAD STYLE + EXEMPLARS
## Referenced by: KM_Companions_Titles.md § BALLAD CYCLE AUTO-FILL · KM_SaveBlock_Template.md § leliana_ballad_cycle (`ballad`)
## Load when Leliana is the active chronicler (leliana_chronicler_mode = true) or composes a BALLAD CYCLE entry.

Leliana is the BARD-CHRONICLER. Her `leliana_ballad_cycle` `ballad` field IS a
ballad she composed — actual sung LYRICS (the words), WRITTEN AS SONGS in this style, and they
MUST RHYME. The ballad is the WORDS she sings — NEVER a prose description of how the music
sounds (see Rule 1). This file is the canonical style guide; the three EXEMPLARS at the
bottom are the gold standard. Leliana's register is warm, plain, and old — the lyrics keep faith
with what happened; they do not perform. She underplays where a younger bard would flourish.

═══════════════════════════════════════════════════════════════════
⛔ HARD RULES (every Leliana ballad)
═══════════════════════════════════════════════════════════════════
0. ⛔ LYRICS, NOT A DESCRIPTION OF THE MUSIC. The ballad body is WORDS SHE SINGS — rhyming
   lyrics, like every exemplar below. It is NOT a prose description of the melody or the
   instrumentation. THESE ARE WRONG (the documented current failure):
     ✗ "two voices identical; by measure eight the lower voice begins to lag a half-beat…"
     ✗ "a grace note in measure seven that does not belong to the key; it does not resolve."
   That is describing the music, not writing it — a "ballad" with no sung words = `.fail 9`.
   The technical detail (key, time-signature, ONE brief melodic figure) may appear ONLY as a
   short `🎵` header line ABOVE the lyrics — never AS the song. The DIARY field already
   carries the prose account; the ballad/`ballad` field carries the LYRICS. RIGHT = the
   exemplars (verses you can actually sing). WRONG = a paragraph about what the music does.
1. IT RHYMES. Default to AABB couplets (a / a / b / b). The CHORUS is a fixed rhyming
   refrain that repeats. A Leliana "ballad" in free verse / non-rhyming lines = not a ballad =
   `.fail 9` (wrong medium). If a line doesn't have a rhyme partner, it isn't finished.
2. IT IS STRUCTURED with labelled sections in [brackets] — see THE STRUCTURE below.
3. IT CARRIES STAGE DIRECTIONS in (parentheses): instrumentation, who lifts a torch,
   dynamics (swells / drops / wall of sound), the action the music tracks.
4. ENSEMBLE ballads name a VOICE per part (the character singing) with a short voice
   descriptor in (parens) — "(cold and steady)", "(steel-clear)", "(bright)".
5. LELIANA'S INSTRUMENT IS THE DAWNSONG LUTE. Where an exemplar
   below shows Linzi + lute, that is the alternate-chronicler version — in a Leliana run the
   chronicler line and the lead instrumental are Leliana + lute. She sings the chronicler's verse,
   low and unhurried.
6. USE THE REAL PARTY. The exemplars' rosters are illustrative. Cast the verses with the
   companions actually present this run; the FLAME COUNT in the chorus/triumphant verse =
   the actual party size ("Seven flames", "Six seals", "Twelve flames" — match the count).
7. NO INVENTED EVENTS. Like all chronicle entries, a ballad may dramatize the FEEL but may
   not add an event not in the entry's `fact`/`diary` (§ leliana_ballad_cycle). It rhymes
   about what actually happened. Leliana, of all chroniclers, will not sing a thing that did not occur.

═══════════════════════════════════════════════════════════════════
SCALING — match the ballad to the beat
═══════════════════════════════════════════════════════════════════
- MINOR scene (a quiet beat, a single exchange): a SHORT ballad — Intro cue + one or two
  rhyming verses + a short refrain. Still rhymes, still in her voice, still has a stage
  direction or two. Keep the save lean.
- MAJOR / CEREMONIAL beat (kingdom founding, the charter signing, a feast triumph, a great
  victory, a roster coming together): the FULL ENSEMBLE ANTHEM — the complete structure
  below, every present companion getting a line. The three exemplars are this scale.
The bigger the moment, the bigger the ballad.

═══════════════════════════════════════════════════════════════════
THE STRUCTURE (full ensemble anthem)
═══════════════════════════════════════════════════════════════════
[Intro]            — instrumental atmosphere (Leliana's lute lifts the melody); set the mood.
[Verse 1]          — the chronicler/lead opens (Leliana, or the player). Establishes the journey.
[Verse 2: The Build] — two companions harmonize; a second instrument joins. Their lanes.
[Chorus]           — the FIXED RHYMING REFRAIN (the hook). Drums + strings drive in.
[Verse 3: Triumphant] — more companions, each a rhymed line; the music swells ("Siege of Trust").
                     Ends naming the FLAME/SEAL COUNT = party size ("Seven flames that shall not yield!").
[Bridge: The Roll Call] — staccato; the torch passes hand to hand; EACH companion ONE line,
                     voice descriptor in (parens). One beat per voice.
[Climax: The Leader's Decree] — music drops to a pulse; eRmaC steps forward with the
                     Wax-Sealed Charter and delivers a longer rhymed stanza (4 lines, the
                     Shrike / spark-in-darkness / crane-on-the-wax / clear-the-tracks motifs).
[Final Chorus]     — the refrain again, maximum volume, "Together we'll reclaim what's known!"
[Outro: Grand Finale] — "Raise the torch! Raise the seal! ..." the closing rallying couplets.
[Ending]           — instrumental close + one diegetic sound (the gate-bar lifting, a final lute note fading).

═══════════════════════════════════════════════════════════════════
MOTIF VOCABULARY (recurring, draw from these)
═══════════════════════════════════════════════════════════════════
- TORCH & FLAME: torches catching down the line; each companion a flame; "Raise the torch!"
- SEAL & CHARTER: the wax seal, the crane upon the wax, the Aldori charter "signed and sealed".
- KEEPING FAITH & THE BLANK PAGE (Leliana's own): the page not yet written, the vow that is not an elegy,
  the dead carried in the dawn hour, "I keep faith." Use sparingly, where the beat earns the weight.
- THE FIXED CHORUS (adapt last line per beat):
    Open your gates, we ask with song,
    Not force of arms — where we belong.
    By flame and seal our truth is shown,
    These River Lands we'll call our own!   (final chorus: "Together we'll reclaim what's known!")
- THE FIXED OUTRO couplets:
    Raise the torch! Raise the seal!
    Let the iron meet the wheel!
    From the mountains to the fen,
    Bring the light to life again!
    By the Charter in our hand,
    We are keepers of the land!
- THE DECREE opener (eRmaC): "In the shadow of the Shrike, where the wild briars grow, /
    A spark begins in darkness, a seed begins to sow! / I hold the seal of Aldori, the
    crane upon the wax — / [a fourth line that rhymes with -ax, naming the beat's action]."
- FLAME COUNT = party size (Six / Seven / Twelve "flames"/"seals").

═══════════════════════════════════════════════════════════════════
EXEMPLARS (the gold standard — match this rhyme + structure + motifs)
═══════════════════════════════════════════════════════════════════

───── EXEMPLAR A — "The Gates of Oleg" (Linzi's lute version shown; in a Leliana run her lute leads, she sings Verse 1) ─────

[Intro]
(Leliana's Dawnsong Lute lifts a low, silver line over the snow — clear, unhurried, welcoming. The note hangs a half-beat in the cold air after her hand has left the strings.)

[Verse 1: Leliana]
(Solo, low and warm. She raises a torch and the Aldori invitation.)
Through frozen roads we've travelled far,
Beneath the same cold northern star.
No bandits we — but faith and seal,
A keeping-true of what is real.

[Verse 2: The Build — Aerith & Keqing]
(Aerith touches her torch to Keqing's. A second voice, then a woodwind, joins in harmony.)
Aerith: Let mercy bless and torches rise —
A goddess walks beneath your skies.
Keqing: I've tracked these woods since I could stand;
No thief stays hidden in this land.

[Chorus: Powerful Harmony — Hu Tao leads, all join]
(Driving drums and rhythmic strings. Torches catch flame down the line.)
Open your gates, we ask with song,
Not force of arms — where we belong.
By flame and seal our truth is shown,
These River Lands we'll call our own!

[Verse 3: Triumphant — Hu Tao & Yor]
(The music swells into a "Siege of Trust." Each raises an invitation.)
Hu Tao: By shield and blade I hold the line —
The helpless saved, that vow is mine.
Yor: No lock, no gate I cannot read;
I wear no name but one I freed.
(Together, rising) See here the charter, signed and sealed —
Seven flames that shall not yield!

[Bridge: The Roll Call]
(Staccato drums. The torch passes hand to hand; each voice a single beat.)
Jaethal: (cold and steady) Beyond the grave, my vigil stays.
Hu Tao: (steel-clear) I've shielded children — I'll shield this gate.
Aerith: (bright) By mercy's grace, your sick I'll mend.
Keqing: (low) The wild raised me; I miss no track.
Yor: (soft, certain) No chain, no crown — I chose this road.
Leliana: (low, unhurried) By lute and faith, the truth I'll bear.

[Climax: The Leader's Decree — General eRmaC]
(The music drops to a rhythmic pulse. eRmaC steps forward, raising the Wax-Sealed Charter.)
eRmaC: In the shadow of the Shrike, where the wild briars grow,
A spark begins in darkness, a seed begins to sow!
I hold the seal of Aldori, the crane upon the wax —
Oleg, the road you've guarded, we'll clear of bandit tracks!

[Final Chorus: Full Ensemble — Soaring]
(Maximum volume. The lute rings triumphantly beneath the voices. A total wall of sound.)
Open your gates, we ask with song,
Not force of arms — where we belong.
By flame and seal our truth is shown,
Together we'll reclaim what's known!

[Outro: Full Ensemble — Grand Finale]
Raise the torch! Raise the seal!
Let the iron meet the wheel!
From the mountains to the fen,
Bring the light to life again!
By the Charter in our hand,
We are keepers of the land!

[Ending]
(The drums stop abruptly. Only a fading lute remains — one low note held past the rest. Then — the heavy wooden bar of Oleg's gate lifting.)

───── EXEMPLAR B — "By Iron and Blood" (full CRPG-roster founding anthem) ─────

[Intro: Quiet Lute and Flute]
[Atmospheric, solemn]

[Verse 1]
[Male Vocal] (eRmaC)
I raise the first flame in the heart of the night,
A dwarven shield raised to stand for the light.
We claim this dark land where the ancient ones hide,
Stand behind me! Let the mountain break the tide!

[Verse 2]
[Female Vocal] (Linzi)
(Torch catches flame)
The story begins, and I'm writing it down!
From the untamed wilds to a glorious crown!
I hold up the seal, let the enemies see,
The heroes have come to set the lands free!

[Verse 3]
[Male Vocal] (Tristian)
(Torch catches flame)
By Sarenrae's grace, watch the shadows recede,
A healing light for the Stolen Lands' need.

[Verse 4]
[Female Vocal] (Jaethal)
(Torch catches flame)
Through shadows we walk, let the weak ones complain,
Death is no obstacle, only our gain.

[Pre-Chorus]
[Male Vocal] (Nok-Nok)
Nok-Nok is here! The most hero of all!
[Female Vocal] (Valerie)
Hold fast the formation, we answer the call!

[Chorus]
[Choir - Mixed Male and Female Vocals]
[Heavy War Drums and Strings]
Raise up the torch, let the river kings see!
We banish the dark and we claim destiny!
With the flame and the steel and the blood in the mud,
We forge a new home by iron and blood!

[Verse 5]
[Male Vocal] (Lem)
(Torch catches flame)
A confident tune and a nimble quick wit,
We'll solve any problem, just wait for it!

[Female Vocal] (Kalikke / Kanerah)
With the calm of the water, the wrath of the flame,
Two souls intertwined carving out our new name.

[Verse 6]
[Male Vocal] (Harrim)
(Torch catches flame)
It all ends in ruin, to dust we'll divide...
But until the world breaks, I will march by your side.

[Female Vocal] (Octavia)
Oh, lighten up Harrim! The future's in bloom!
A little bright magic to banish the gloom!

[Pre-Chorus]
[Female Vocal] (Amiri)
My big blade is thirsty! Who's first to bleed?!
[Male Vocal] (Regongar)
Point me at the carnage, let lightning succeed!

[Bridge]
[Tempo slows down, solemn and epic]
[Male Vocal] (eRmaC)
The charter is drawn. The kingdom is born.
Through the fangs of the wild, through the teeth of the storm.

[Guitar and Orchestral Crescendo]
[Massive Build Up]

[Chorus]
[Massive Choir - All Voices United]
Raise up the torch, let the river kings see!
We banish the dark and we claim destiny!
Six seals of honor against the long night,
Six torches blazing, holding the light!

[Outro]
[Male Vocal] (eRmaC)
We hold the Stolen Lands.
The darkness is done.
[Choir - A Capella]
The ceremony ends.
The kingdom is one.
[Fade out with a final drum hit]

───── EXEMPLAR C — "These River Lands" (flute version, full CRPG roster) ─────

[Intro]
(A solo, silver flute melody pierces the winter air, high and clear. Peaceful and welcoming.)

[Verse 1: Linzi]
(Solo voice, gentle. Linzi raises her torch and her Aldori invitation.)
Through frozen roads we've traveled far
Beneath the fading northern star
No bandits we, but rightful souls
With charter, seal, and worthy goals

[Verse 2: Build - Tristian & Nok-Nok]
(Tristian touches his torch to Nok-Nok's. A second woodwind joins in harmony.)
Let torches burn and voices rise
No deception in our eyes
By Aldori's hand we're called to serve
This stolen land we'll help preserve

[Chorus: Powerful Harmony - Valerie, Kalikke, Kanerah, Lem]
(Driving drums and rhythmic strings join. Torches catch flame down the line.)
Open your gates, we ask with song
Not force of arms, where we belong
By flame and seal our truth is shown
These River Lands we'll call our own!

[Verse 3: Triumphant - Octavia, Harrim, Amiri, Regongar]
(The music swells into a "Siege of Trust." Each hero raises their invitation.)
Octavia: My magic weaves through winter's bite
Harrim: In Groetus' shadow, I find the light
Amiri: My blade is giant, my spirit free
Regongar: Through storm and blood, our destiny!
See here the charter, signed and sealed
Twelve flames that shall not yield!

[Bridge: The Roll Call]
(Staccato drum beats. Each character speaks/sings their line as the torch passes.)
Jaethal: (Cold and steady) Beyond the grave, my vigil stays.
Valerie: (Resonant) By shield and scar, I guard these ways.
Kalikke/Kanerah: (Duality) From water's depth to fire's breath.
Lem: (Cheerful) My song shall defy the sting of death.
Tristian: (Kind) For Sarenrae, the sun shall rise.
Nok-Nok: (Raspy) The goblin hero kills the lies!

[Climax: The Leader's Decree - General eRmaC]
(The music drops to a rhythmic pulse. eRmaC steps forward, raising the Wax-Sealed Charter.)
eRmaC: In the shadow of the Shrike, where the wild briars grow
A spark begins in darkness, a seed begins to sow!
I hold the seal of Aldori, the crane upon the wax
To carve a path of justice through the forest and the tracks!

[Final Chorus: Full Ensemble - Soaring]
(Maximum volume. Flute trills triumphantly. Total wall of sound.)
Open your gates, we ask with song
Not force of arms, where we belong
By flame and seal our truth is shown
Together we'll reclaim what's known!

[Outro: Full Ensemble - Grand Finale]
Raise the torch! Raise the seal!
Let the iron meet the wheel!
From the mountains to the fen,
Bring the light to life again!
By the Charter in our hand,
We are keepers of the land!

[Ending]
(The drums stop abruptly. Only a fading flute remains. The sound of a heavy wooden bar lifting.)
