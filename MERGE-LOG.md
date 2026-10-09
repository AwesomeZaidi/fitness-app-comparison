# How the feature list and scores were built

This is the working record behind a public comparison of six iOS workout trackers: **SPLYT, Hevy, Strong, Gravl, Fitbod and Motra**. SPLYT made this comparison, and SPLYT is one of the six apps. Every rule below was written to apply to all six in the same way, and where a rule cuts against SPLYT, the record says so.

## 1. Inputs

- **Claims.** For each app, a separate extraction pass read only that app's own public material: its App Store listing, release notes, website, help centre or FAQ, and Google Play for Android availability. Each pass followed the same brief and saw no other app. Each claim carries a verbatim quote, a URL, a source type and a date. In total: SPLYT 247 + 288 (see below), Hevy 233, Strong 120, Gravl 174, Fitbod 141, Motra 159.
- **SPLYT feature index.** SPLYT has no help centre. On **2026-10-09, the same day as this comparison**, it published a feature index at https://splyt.fit/features (288 entries). Readers should bear that date in mind. Its entries were treated as help-centre claims, vetted with the same classes and strictness as every other app's help centre, and numbered `i0`–`i287` in this log. Where SPLYT's older claims and the index disagree, the index won, and the older claim was marked `unsubstantiated`. SPLYT also describes the index as a complete feature list. So where SPLYT's own marketing copy claims something the index does not describe, that claim was also marked `unsubstantiated`: the 0–21 daily strain score, phone-free watch use, body circumference measurements, and watching a friend's sets live. No other app's help centre claims to be complete, so no other app could be held to this test. It is stricter on SPLYT than on anyone else.
- **Store listings, checked the same way for all six (2026-10-09).** The App Store product page's Compatibility and Languages sections, and the store record's `iosUniversal` flag, were read for every app. Google Play was searched for SPLYT and Motra, the two apps whose claim files had no Android evidence either way.

## 2. Building canonical features

- A canonical feature is something a typical lifter would recognise as a distinct thing to look for in an app. Settings and small variants of one capability were merged into it as **aspects**. Aspects are shown but not scored. For example, rest-timer sounds and ±15 s buttons are aspects of "Rest timer". Generator settings such as goal, experience, split type, session length and variety are aspects of "Generated training program" or "Generated single workout".
- **The same granularity was applied to every app.** When one app listed many small items and another listed one sentence, both mapped to the same parent:
  - SPLYT's 13 separate voice claims (logging, corrections, superset grouping, building templates and splits by voice, voice on the watch…) became one feature, "Voice logging".
  - SPLYT's competition details (3D race worlds, custom characters, character library, stakes, awards, race chat) are aspects of "Competitions and challenges".
  - SPLYT's split-builder details (rotating cycles, varied weeks, pause, rerun…) are aspects of "Custom split builder".
  - Hevy's widget list, Fitbod's and Gravl's programming settings, and Motra's auto-detection settings are aspects too.
- Related but different capabilities stay separate:
  - auto rep counting ≠ auto exercise detection
  - Garmin ≠ Wear OS
  - Garmin watch app ≠ Garmin Connect sync
  - AI coach chat ≠ generated program
  - ChatGPT/MCP integration ≠ in-app AI chat
  - warm-up set tagging ≠ automatic warm-up sets
  - body weight log ≠ body measurements
  - Apple Health export ≠ Apple Health import
- "Generated training program" counts any app that builds a personalised program from your goals, schedule and equipment, whether or not the app calls it AI. Hevy says its Trainer is algorithmic and "does not rely on AI". It still counts, because the feature is what the user gets.
- A feature exists only if some app currently claims it. Removed features that no app still offers did not create rows. They are listed under "Removed features" at the end of this log.
- After a first pass, three features that only SPLYT had were folded into broader parents, following the rule "when in doubt, choose the grouping fairest to the other apps":
  - Recovery activities (sauna, cold plunge…) became an aspect of "Non-lifting activity types".
  - SPLYT's combined daily ring became an aspect of "Habit and daily-goal tracking".
  - AI goal setting became an aspect of "AI coach chat".
- The daily strain score row was dropped. Its only claim (SPLYT, website) was vetted as unsubstantiated, and a row exists only if some app has counted evidence for it.
- That leaves 188 canonical features in 14 categories. The categories were derived from the data.

## 3. Scoring rules (identical for all six)

| Value | Meaning |
|---|---|
| **yes** | At least one counted claim from the app's own sources whose quote shows the capability. The strongest is attached as evidence. The order of preference is: core claim over aspect over "also"; then help centre > release notes > website > App Store > Google Play. |
| **partial** | The app's own evidence states a limitation that makes it materially less than the definition: rolling out or public beta, only on Android when the feature is general, rest timer only, support-assisted only, live indicator only. |
| **no** | Explicit evidence of absence or removal from the app's own sources, or from its store listing (App Store compatibility, no Google Play listing). Each one is cited. |
| **unknown** | Everything else. **Unknown is not no.** It means the app's own material, as extracted, does not show the capability. |

## 4. Vetting every claim

Every claim was classified before scoring (`data/vetting.json`). The classes are the same for every app:

| Class | Counts? | Meaning |
|---|---|---|
| `capability` | yes | A concrete capability, described by its quote. |
| `aspect` | yes, under its parent only | A setting or variant of a parent feature. |
| `unsubstantiated` | no (never above unknown on its own) | Marketing-only, and contradicted by, or absent from, the app's more detailed own sources. |
| `not_shipped` | partial at most | Rolling out to some users, or a public beta. |
| `fix` | no | A bug fix or speed/reliability improvement. |
| `ui_tweak` | no | Layout, redesign or copy change. |
| `vague` | no | A name with no description of what it does. |
| `out_of_scope` | no | Pricing or plan limits (excluded by the brief). |

Interpretations applied to every app:

- A bare name in a marketing list counts only when the name itself fully states the user-facing capability: "Dark Mode", "Siri Shortcuts", "Fully featured iPad app".
- Names that do not say what they do were rejected: Motra "Challenges", Motra "Guide Mode", Strong "3rd Party Integrations" (which was never extracted).
- A store claim contradicted by the app's own help centre loses. Gravl's App Store says its watch app is "standalone", but its help says "Keep the iPhone within reach". Strong's homepage lists "Workout Scheduling", but its help lists scheduling as still being built.
- A fix-only release note does not prove the underlying feature. Strong's "Faster Apple Health workout imports" and Gravl's "Improvements on bodyweight sync" therefore leave those cells unknown.

## 5. The hardest judgement calls

1. **SPLYT's same-day feature index.** It is accepted as help-centre evidence, but it also makes four SPLYT website claims `unsubstantiated` (section 1). No other app could be held to this test.
2. **Watch without the phone.**
   - Gravl: **no**. Its help says the phone owns the session.
   - Fitbod: **no**. Its help says "companion app, not a standalone experience".
   - Strong: **yes**. The App Store says "with or without your iPhone". Its help's "will be able to work independently" refers to pairing, not to logging away from the phone.
   - Hevy: **yes**. Its website says "leave your phone in the locker room", and the App Store says the watch saves workouts offline.
   - SPLYT: **unknown**. Its website claim is not backed by its index.
3. **AI and algorithmic program generation are one feature.** Generated programs and generated single workouts are two separate features. SPLYT's AI split drafts count as a generated program. SPLYT has no claim of automatic progressive overload, so that cell is unknown.
4. **Collapsing SPLYT's many small claims** (voice, competitions, splits, watch screens) into parents, and doing the same to every other app's settings lists.
5. **Platform rows come from App Store compatibility, read the same way for all six.**
   - iPad means a native iPad build, so only universal apps count: SPLYT and Hevy.
   - Vision Pro and Mac mean "listed as compatible". Vision compatibility is largely automatic for iPhone/iPad apps, so the Vision row is weak evidence of any real effort.
6. **Android = no for SPLYT and Motra**, because Google Play search found no listing. A "MOTRA" app (com.motra.app) exists, but it is from a different developer (motraapp.com).
7. **Strong's scheduling (no) and muscle heat map (unknown).** Both appear only in one variant of the homepage feature strip.
8. **Garmin.**
   - Gravl: yes for both the watch app and Connect sync.
   - Hevy: **no**, because its help says Garmin integration "is not possible at this time".
   - Fitbod: unknown. Only its website FAQ lists Garmin, and its help documents Garmin only as a Bluetooth heart-rate source on Android.
9. **Rolling out and beta.**
   - Motra's AI coach: **partial**. It was announced as a staged rollout and is not documented in help.
   - Fitbod's live heart rate, AirPods heart rate and Bluetooth monitors: **partial**. They are "gradually rolling out", and Bluetooth monitors are Android-only.
   - Gravl's voice workout creation: **partial**. It is a public beta, cited from its help centre. It was not in Gravl's extracted claims, because the brief excluded beta items.
   - Fitbod Clubs leaderboards: **unknown**. They are a closed beta "at select gym locations".
10. **Narrow evidence beats broad evidence.**
    - SPLYT's "Workouts from Apple Fitness, Strava and gym treadmills land in your history" counts for Apple Health import but **not** as a Strava integration, because SPLYT's index says imports come through Apple Health.
    - SPLYT's "body weight and measurements" counts as a weight log only.
    - Motra's single help-centre sentence naming "tempo" was accepted as tempo tracking. It describes something the user can do from the watch, but it is the thinnest "yes" in the matrix.

## 6. Limits a reader should know

- **This list measures what each app documents about itself, not what it can do.** An app that writes more release notes and help articles gets more cells marked yes. Strong has the thinnest documentation (120 claims, and its features page is password-protected), so many Strong cells are unknown rather than no. SPLYT's index was published the day of the comparison and adds 288 entries, and this inflates SPLYT's documented surface. Compare percentages with that in mind.
- Fitbod's release notes are boilerplate, so none of its claims are dated.
- Each claim was read once, by an extraction pass that worked on one app at a time. Help centres were not re-read exhaustively for every cell, so some unknowns may be capabilities an app has but did not describe in the pages that were read.
- **How much the same-day SPLYT index matters.** Eight SPLYT "yes" cells rest only on the index: timed exercises, keep screen awake, repeat or save a past workout as a template, workout reminders, training streaks, body data synced with Apple Health, starting templates on the watch, and privacy controls. Without the index, SPLYT would have 125 yes (66%) instead of 133 (71%). The index also removed or weakened five SPLYT cells that older SPLYT claims would have scored yes: daily strain was dropped, body measurements, watch-only use and Strava import became unknown, and live friend-following became partial. Its net effect is therefore smaller than its 288 entries suggest.


## Every canonical feature and what was merged into it

Format: app — `claim-index` original claim name (role). Roles: core = scored member; aspect = a setting or variant shown under the feature; also = the claim belongs to another feature but its quote also proves this one. SPLYT indices starting with `i` come from the 2026-10-09 feature index. Claims marked ✗ were not counted (class in brackets).


### Workout logging

#### Strength set logging (`set-logging`)
Log weight and reps for each set of a lift during a live workout.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `0` Strength set logging (core) ✗ [unsubstantiated]; `2` Custom lifting keypad (aspect); `27` Default sets and reps (aspect); `i24` Lifting keypad (core); `i3` Workout defaults (aspect); `i31` Duplicate or remove a set (aspect)
- **Hevy**: `0` Strength workout logging (core); `80` Eight exercise types (aspect)
- **Strong**: `12` Warm-up set tag (also); `85` RPE logging (also); `12` Warm-up set tag (also); `85` RPE logging (also)
- **Gravl**: `58` One-tap prefilled set logging (core)
- **Fitbod**: `57` Add or delete sets mid-workout (core); `66` Per-side unilateral labelling (aspect)
- **Motra**: `33` Phone-only workout logging (core) ✗ [fix]; `47` Previous performance display (also); `46` Smart set auto-update (aspect); `47` Previous performance display (also)

#### Start an empty workout (`empty-workout`)
Start an unplanned workout and add exercises as you go.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `4` Previous weights prefilled (also); `i63` Quick start (core); `4` Previous weights prefilled (also)
- **Hevy**: `1` Start empty workout (core)
- **Strong**: `100` Empty workout start (core)
- **Gravl**: `74` Manual empty workout (core)
- **Fitbod**: `51` Build workout from scratch (core)
- **Motra**: `34` Freeform empty workouts (core)

#### Previous performance shown or pre-filled (`previous-performance`)
While logging, each set shows or pre-fills what you lifted last time on that exercise.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `4` Previous weights prefilled (core); `22` Copy sets from a past session (aspect); `23` Copy numbers between movements (aspect); `i32` Last-time values (core); `i33` Pre-fill last weight (core); `i8` Use these sets (aspect)
- **Hevy**: `23` Auto-fill from last session (core); `24` Previous performance column (core); `25` Previous values per routine (aspect); `26` Tap previous value to fill (aspect)
- **Gravl**: `58` One-tap prefilled set logging (also); `58` One-tap prefilled set logging (also)
- **Motra**: `47` Previous performance display (core); `48` Weight memory (core)

#### Live comparison during a workout (`live-workout-stats`)
During a workout, running totals or a live comparison against previous sessions are shown.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `37` Live activity comparison gauge (core); `39` Recent sessions mid-workout (aspect); `i59` Live comparison with your history (core)
- **Hevy**: `45` Live volume and set counter (core)
- **Strong**: `107` Focus metric per exercise (core); `108` Volume change vs last session (aspect)

#### Effort per set (RPE / RIR) (`rpe-rir`)
Record perceived exertion or reps in reserve for a set or exercise.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `15` Reps in reserve logging (core); `i27` RIR / effort per set (core)
- **Hevy**: `27` RPE logging (core); `28` RPE auto-checks set (aspect)
- **Strong**: `85` RPE logging (core)
- **Gravl**: `3` Per-exercise effort rating (core)
- **Fitbod**: `62` Reps in reserve logging (core); `63` Edit effort rating later (aspect)
- **Motra**: `39` Per-set RPE logging (core)

#### Whole-workout effort rating (`workout-effort-rating`)
Rate how hard an entire session felt.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `16` Workout effort rating (core); `i16` Rate workout effort (core)
- **Motra**: `40` Workout perceived effort rating (core)

#### Lifting tempo tracking (`tempo-tracking`)
Record the tempo of a set.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **Motra**: `41` Tempo tracking (also); `41` Tempo tracking (also)
- _Decision — Motra = yes:_ Named in a help-centre sentence listing what can be tracked from the watch; no further detail. Source: https://help.motra.com/en/articles/9888453-about-motra

#### Complete planned sets without entering each (`quick-complete`)
Mark a planned workout, group or all remaining sets as done as prescribed instead of entering every set.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `28` Follow-along mode (core); `29` Simple mode strength session (aspect); `i50` Follow along (core); `i49` Simple mode (aspect)
- **Fitbod**: `45` Log a whole superset at once (core)
- **Motra**: `61` Log all unlogged sets on finish (core)

#### Workout name and notes (`workout-notes`)
Give a workout a name and attach a free-text note or description.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `26` Rename workout mid-session (core); `31` Auto-named strength workouts (aspect)
- **Hevy**: `33` Workout title and description (core)
- **Strong**: `32` Workout notes (core)
- **Motra**: `63` Workout photos and captions (core)

#### Photos or video on a workout (`workout-media`)
Attach photos or video to a logged workout.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra yes

- **Hevy**: `171` Workout photos and video (core)
- **Strong**: `33` Progress photos (also); `33` Progress photos (also)
- **Motra**: `63` Workout photos and captions (also); `63` Workout photos and captions (also)

#### Add and reorder exercises mid-workout (`edit-live-workout`)
Add exercises to, or drag to reorder exercises within, a workout in progress.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `24` Reorder exercises (core); `i40` Reorder movements (core)
- **Hevy**: `22` Reorder and replace exercises (core)
- **Strong**: `101` Drag-and-drop exercise reordering (core)
- **Gravl**: `72` Reorder exercises (core); `73` Add exercises mid-workout (core)
- **Fitbod**: `55` Add, replace, delete, reorder exercises (core)

#### Exercise swap with suggested alternatives (`exercise-swap`)
Replace an exercise mid-workout, with the app suggesting suitable alternatives.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `20` Exercise swap with ranked alternatives (core); `i37` Switch exercise (core); `i38` Machine taken? alternatives (aspect)
- **Hevy**: `94` Suggested exercise alternatives (core); `95` One-off or permanent swap (aspect); `22` Reorder and replace exercises (also); `22` Reorder and replace exercises (also)
- **Gravl**: `42` Same-muscle exercise swap (core)
- **Fitbod**: `56` Smart exercise replacement (core)
- **Motra**: `56` Exercise swap (core); `57` AI exercise swap suggestions (aspect)

#### Exercise notes (`exercise-notes`)
Attach a note to an exercise, kept with the session or shown next time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `21` Exercise notes (core); `i36` Exercise notes (core)
- **Hevy**: `30` Exercise notes in routines (core); `31` Clickable links in notes (aspect); `32` Per-workout exercise notes (aspect)
- **Strong**: `34` Exercise notes (core); `35` Pinned exercise notes (aspect)
- **Gravl**: `82` Exercise notes (core)
- **Fitbod**: `64` Exercise notes (core)
- **Motra**: `24` Exercise notes on watch (also); `24` Exercise notes on watch (also)

#### Grip and attachment tracking (`grip-tracking`)
Record the grip, handle or attachment used, with history kept per grip.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `18` Grip and handle selection (core); `19` Per-grip history and weights (aspect); `i34` Grips and handles (core); `i233` Filter history by grip (aspect)
- **Motra**: `4` Automatic set start/end detection (also); `5` Grip and variation recognition (also); `4` Automatic set start/end detection (also); `5` Grip and variation recognition (also)

#### Bodyweight, weighted and assisted exercises (`bodyweight-exercises`)
Exercises that use body weight, including added load or assistance, are logged and counted correctly.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `30` Bodyweight exercise volume (core)
- **Hevy**: `10` Bodyweight exercise logging (core); `11` Assisted bodyweight exercises (core); `12` Weighted bodyweight exercises (core); `13` Update bodyweight mid-workout (aspect)
- **Strong**: `10` Assisted bodyweight exercises (core)
- **Fitbod**: `68` Added weight on bodyweight exercises (core)
- **Motra**: `49` Assisted exercises with negative weight (core)

#### Timed exercises (`timed-exercises`)
Log time-based exercises (e.g. planks) by duration, with a timer.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `i35` Track by time, reps or weight (core)
- **Hevy**: `8` Duration-based exercise logging (core); `57` Inline stopwatch for timed sets (aspect); `58` In-workout countdown timer (aspect)
- **Strong**: `11` Duration-based exercises (core)
- **Gravl**: `76` Timed exercise logging (core)
- **Fitbod**: `70` Timed exercise tracking (core)
- **Motra**: `52` Timed exercise timer (core); `51` Reps, distance or time measurement (aspect)

#### Pause, resume or discard a workout (`pause-discard`)
Pause the workout clock and resume later, or throw away a workout in progress.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `124` Siri workout control (also); `i47` Pause and resume (core); `124` Siri workout control (also)
- **Hevy**: `36` Discard workout (core); `37` Pause workout timer (core)
- **Gravl**: `71` Pause and resume workout (core)
- **Fitbod**: `60` Pause a workout (core); `61` Discard a workout (core)

#### Edit or delete past workouts (`edit-past-workouts`)
Change or delete a workout after it has been saved.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `32` Edit past workouts (core); `i18` Edit a past workout (core); `i19` Delete a workout or one activity (aspect)
- **Hevy**: `40` Edit saved workouts (core); `41` Delete workouts and sets (core); `38` Edit workout duration (aspect)
- **Strong**: `94` Edit past workouts (core)
- **Gravl**: `80` Edit finished workouts (core); `81` Delete workouts (core)
- **Fitbod**: `58` Edit logged workouts (core); `59` Delete logged workouts (core)
- **Motra**: `62` Edit past workouts (core)

#### Log a workout after the fact (`log-past-workout`)
Record a workout you did earlier, on its real date and time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `33` Manual activity logging (core); `i0` Log an activity manually (core); `i1` Log a missed workout late (aspect)
- **Hevy**: `39` Backdate workouts (core); `44` Multiple workouts per day (aspect)
- **Strong**: `93` Log past workouts (core)
- **Gravl**: `79` Log past workouts (core)
- **Fitbod**: `54` Log workout for a past date (core)

#### Search workout history (`history-search`)
Search or filter the list of past workouts.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `181` Workout history search (core); `i20` Workout history (core)

#### Forgotten-workout reminder (`inactivity-reminder`)
Prompts you when a workout appears abandoned (inactivity or leaving the location).

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `43` Inactivity workout check (core); `i61` Forgotten-workout check (core); `i268` 'Still working out?' check (aspect)
- **Motra**: `59` Inactivity save reminder (core); `60` Location-based save reminder (core)

#### Offline logging (`offline-logging`)
Workouts can be logged and saved without a connection and sync later.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `34` Offline workout saving (core); `i2` Finish workouts offline (core)
- **Hevy**: `196` Watch offline auto-save (core)
- **Fitbod**: `77` Offline workout generation and logging (core)
- **Motra**: `27` Offline watch workout storage (core); `28` Interrupted workout recovery (aspect)

#### Kilograms and pounds (`kg-lb`)
Choose kilograms or pounds as the weight unit.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `36` Kilograms and pounds (core); `i4` Pounds or kilograms (core)
- **Hevy**: `66` Kg and lb units (core)
- **Strong**: `30` Pounds and kilograms (core)
- **Gravl**: `102` kg and lb units (core)
- **Fitbod**: `75` Weight units lb/kg (core)
- **Motra**: `54` Weight unit setting (core); `55` Distance unit setting (aspect)

#### Per-exercise weight units (`per-exercise-units`)
Use a different weight unit for an individual exercise or piece of equipment.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `67` Per-exercise weight unit (core)
- **Strong**: `31` Mixed weight units (core)
- **Gravl**: `103` Per-gym weight unit (core)
- **Fitbod**: `76` Per-exercise unit override (core)
- **Motra**: `53` Per-exercise weight units (core)

#### Keep screen awake during workouts (`keep-screen-awake`)
Option to stop the phone locking during a workout.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `i60` Keep screen awake (core)
- **Hevy**: `59` Keep screen awake (core)
- **Motra**: `58` Keep screen awake during workouts (core)


### Sets, supersets & loading

#### Rest timer (`rest-timer`)
A countdown (or count-up) between sets, typically starting when a set is completed.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `44` Rest timer (core); `47` Adjustable rest by drag (aspect); `50` Manual rest start (aspect); `i42` Rest timer (core); `i45` Manual rest for any activity (aspect)
- **Hevy**: `50` Automatic rest timer (core); `52` Default rest timer (aspect); `53` Adjust rest timer in 15s steps (aspect)
- **Strong**: `9` Automatic rest timer (core); `86` Full-screen rest timer (aspect); `87` Adjust or skip rest timer (aspect); `88` Manual rest timer start (aspect)
- **Gravl**: `59` Rest timer (core)
- **Fitbod**: `71` Rest timer (core)
- **Motra**: `42` Automatic rest timer (core)

#### Custom rest per exercise or set (`custom-rest`)
Set different rest durations per exercise or per set, remembered next time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `45` Per-movement rest times (core); `46` Per-set custom rest times (core); `51` Rest after warm-up option (aspect); `i43` Per-movement rest time (core); `i44` Per-set rest override (core)
- **Hevy**: `51` Per-exercise rest timers (core)
- **Strong**: `89` Per-exercise rest timer duration (core); `90` Separate warm-up rest duration (aspect)
- **Gravl**: `60` Per-exercise rest timer (core)
- **Fitbod**: `72` Exercise-specific recommended rest (core)
- **Motra**: `44` Per-set rest times (core)

#### Rest-end alerts (`rest-alerts`)
A sound, vibration, voice cue or notification when rest is over.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `48` Rest end chime and vibration (core); `i46` Rest-end alert (core)
- **Hevy**: `56` Rest timer notification (core); `54` Rest timer sounds (aspect); `55` Set-complete sound volume (aspect)
- **Strong**: `91` Rest timer sound choice (aspect); `92` Rest timer notifications (core) ✗ [fix]
- **Gravl**: `61` Rest timer sound (core) ✗ [fix]; `121` Watch haptic rest timer (also); `121` Watch haptic rest timer (also)
- **Fitbod**: `73` Rest timer notifications (core)
- **Motra**: `43` Rest alarm (core); `45` Spoken rest audio prompts (aspect)

#### Warm-up set tagging (`warmup-sets`)
Mark sets as warm-ups (kept separate from working sets).

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `10` Warm-up sets (core); `i28` Set types (also); `i28` Set types (also)
- **Hevy**: `15` Warm-up set type (core); `64` Exclude warm-ups from stats (aspect)
- **Strong**: `12` Warm-up set tag (core)
- **Gravl**: `65` Warm-up sets (also); `65` Warm-up sets (also)
- **Fitbod**: `37` Automatic warm-up sets (also); `37` Automatic warm-up sets (also)
- **Motra**: `35` Warm-up and cool-down sets (core)

#### Automatic warm-up sets (`warmup-calculator`)
The app inserts warm-up sets with calculated weights before working sets.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **Hevy**: `63` Warm-up set calculator (core)
- **Strong**: `26` Warm-up calculator (core); `27` Customizable warm-up formulas (aspect)
- **Gravl**: `65` Warm-up sets (core)
- **Fitbod**: `37` Automatic warm-up sets (core)

#### Drop sets (`drop-sets`)
Log a set as a drop set with reduced-weight follow-on efforts.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `8` Drop sets (core); `9` Default drop-set reduction (aspect); `i29` Drop sets (core)
- **Hevy**: `16` Drop set type (core); `18` Rest timer skipped before drop sets (aspect)
- **Strong**: `14` Drop set tag (core)
- **Gravl**: `64` Drop sets (core)
- **Motra**: `36` Drop sets (core)

#### Failure sets (`failure-sets`)
Mark a set as taken to failure.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `11` Failure sets (core); `i28` Set types (core)
- **Hevy**: `17` Failure set type (core)
- **Strong**: `13` Failure set tag (core)

#### Additional set types (top set, partials, cool-down) (`other-set-types`)
Set-type tags beyond warm-up, drop and failure, such as top sets, partial reps or cool-down sets.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `12` Top sets (core); `13` Partial reps logging (core); `i30` Partials (core)
- **Motra**: `35` Warm-up and cool-down sets (also); `35` Warm-up and cool-down sets (also)

#### Supersets (`supersets`)
Group two exercises to be performed back-to-back.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `5` Supersets (core); `i39` Supersets and giant sets (core)
- **Hevy**: `19` Supersets (core); `21` Smart superset scrolling (aspect)
- **Strong**: `15` Supersets (core); `17` Superset-aware next-set navigation (aspect)
- **Gravl**: `62` Supersets (core)
- **Fitbod**: `43` Manual superset/circuit builder (core); `44` Normalize weights across superset (aspect)
- **Motra**: `37` Manual supersets (core)

#### Giant sets and circuits (`giant-sets-circuits`)
Group three or more exercises together as a giant set or circuit.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `6` Giant sets (core); `i39` Supersets and giant sets (also); `i39` Supersets and giant sets (also)
- **Hevy**: `20` Giant sets and circuits (core)
- **Strong**: `16` Circuits (core)
- **Gravl**: `63` Circuits (core)
- **Fitbod**: `43` Manual superset/circuit builder (also); `43` Manual superset/circuit builder (also)
- **Motra**: `38` Circuits (core)

#### Per-set rep targets and pyramids (`set-targets`)
Templates can hold rep ranges or different targets per set (pyramids, reverse pyramids).

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `14` Per-set rep targets (core)
- **Hevy**: `7` Rep range targets (core)
- **Gravl**: `32` Pyramid sets (core); `33` Reverse pyramid sets (core); `31` Straight sets progression style (aspect)

#### Plate calculator (`plate-calculator`)
Shows which plates to load for a target weight.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `17` Plate calculator (core); `i26` Plate calculator (core); `i25` Load the bar (aspect)
- **Hevy**: `60` Plate calculator (core); `61` Custom bars and plates (aspect); `62` Plate calculator for Smith machine (aspect)
- **Strong**: `28` Plate calculator (core); `29` Bar type selection (aspect)
- **Gravl**: `68` Plate calculator (core); `69` Plate loading modes (aspect); `70` Plate inventory (aspect)
- **Fitbod**: `74` Plate calculator (core); `67` Bar-plus-plates vs plates-only weight (aspect)


### Templates, plans & calendar

#### Saved workout templates (`templates`)
Save reusable workouts and start a session from one.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `75` Saved workout templates (core); `40` Search workout picker (aspect); `78` Set types in templates (aspect); `i136` Workout templates (core)
- **Hevy**: `2` Reusable workout routines (core); `4` Duplicate routine (aspect)
- **Strong**: `3` Custom routines / templates (core); `49` Template search (aspect)
- **Gravl**: `77` Saved workout templates (core)
- **Fitbod**: `52` Saved workouts (core)
- **Motra**: `73` Workout templates (core); `71` Sort custom exercises and templates (aspect); `76` Template search and muscle filter (aspect); `82` Muscle map for templates (aspect)

#### Template folders or tags (`template-organisation`)
Organise templates into folders or tags.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `76` Template folders (core); `i139` Template folders (core)
- **Hevy**: `3` Routine folders (core)
- **Strong**: `97` Template folders (core); `98` Archive templates (aspect)
- **Motra**: `75` Template tags (core)

#### Repeat a past workout or save it as a template (`save-as-template`)
Turn a completed workout into a template, or start a new session copied from it.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `i23` Repeat a past workout (core); `i138` Save a workout as template (core)
- **Hevy**: `43` Save workout as routine (core); `42` Copy a past workout (aspect)
- **Strong**: `95` Save workout as template (core)
- **Fitbod**: `52` Saved workouts (also); `52` Saved workouts (also)
- **Motra**: `74` Save workout as template (core)

#### Update template from a workout (`update-template`)
After a workout that changed, choose to write the changes back into its template.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra yes

- **Hevy**: `5` Update routine from workout (core); `6` Auto-update routine weights and reps (aspect)
- **Strong**: `96` Update template from workout (core)
- **Motra**: `77` Update template from workout (core)

#### Per-template progress (`template-history`)
A template shows its past runs or a progress trend.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `95` Template trend graph (core)
- **Motra**: `81` Template volume progression chart (core); `83` Template last-performed date (aspect)

#### Ready-made single workouts (`prebuilt-workouts`)
A library of pre-built single sessions to start from.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra yes

- **Hevy**: `82` Pre-built routine categories (core); `83` Save routines from blog (aspect)
- **Strong**: `99` Example templates (core)
- **Fitbod**: `48` Pre-built on-demand workouts (core)
- **Motra**: `80` Pre-made template library (core)

#### Ready-made programs and splits (`prebuilt-programs`)
A library of pre-built multi-day programs or weekly splits.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `79` Proven split library (core); `80` Auto-fill split with exercises (aspect); `i110` Proven split library (core); `i119` Fill a split with exercises (aspect)
- **Hevy**: `81` Pre-built program library (core)
- **Gravl**: `13` Preset training splits (core); `15` Split recommendation helper (aspect)

#### Programs from named coaches (`creator-programs`)
Structured plans authored by named coaches or creators, with their own content.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **Gravl**: `16` Creator training plans (core)

#### Custom split builder (`split-builder`)
Build your own multi-day split or weekly plan by hand.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `82` Manual split builder (core); `81` Rotating splits (aspect); `i112` Build a split by hand (core); `i109` Splits hub (aspect); `i111` Rotating split cycles (aspect); `i113` Start from a split shape (aspect); `i114` Drag to reorder a split (aspect); `i115` Vary weeks in a split (aspect); `i116` Split length and start date (aspect); `i117` Preview before adding (aspect); `i120` Split progress page (aspect); `i121` Edit a split (aspect); `i122` Pause a split (aspect); `i123` Run a split again (aspect); `i124` Delete a split (aspect); `i213` Split progress card (aspect)
- **Gravl**: `14` Custom split builder (core)

#### Planning calendar (`training-calendar`)
Schedule workouts on future dates in a calendar, and see planned against completed.

_Result:_ SPLYT yes · Hevy no · Strong no · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `83` Training calendar (core); `84` Monthly ring calendar (aspect); `85` Drag to reschedule (aspect); `86` Copy a planned day (aspect); `87` Scheduled workout times (aspect); `88` Usual training time hint (aspect); `89` Missed workout tracking (aspect); `90` Recurring planned sessions (aspect); `65` Rest day logging (aspect); `i126` Training calendar (core); `i128` Plan a future day (core); `i127` Month view (aspect); `i129` Repeat a planned day (aspect); `i130` Drag to reschedule (aspect); `i131` Copy a training day (aspect); `i132` Rest days (aspect); `i133` Remove planned workouts (aspect)
- **Strong**: `57` Workout scheduling (core) ✗ [unsubstantiated]
- _Decision — Hevy = no:_ Hevy's calendar shows past workouts only. Source: https://help.hevyapp.com/hc/en-us/articles/35380117933207-Track-Your-Workout-Consistency-with-the-Calendar-and-Streak-Features
- _Decision — Strong = no:_ The homepage strip lists 'Workout Scheduling', but Strong's help says it is still being built. Source: https://help.strongapp.io/article/242-future-features

#### Workout history calendar (`history-calendar`)
A calendar or grid view of days you trained.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `i214` Workout calendar heatmap (core); `83` Training calendar (also); `83` Training calendar (also)
- **Hevy**: `134` Workout calendar (core); `135` Year and multi-year calendar (aspect)
- **Strong**: `44` Calendar home screen widget (also); `44` Calendar home screen widget (also)
- **Gravl**: `150` Activity calendar (core)
- **Motra**: `120` Workout calendar (core)

#### Workout reminders (`workout-reminders`)
Notifications reminding you to train (scheduled or after inactivity).

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `i267` Inactivity nudge (core); `i269` Next-activity reminder (aspect)
- **Fitbod**: `49` Workout preview notifications (core)
- **Motra**: `123` Workout reminders (core)

#### Apple Calendar sync (`apple-calendar-sync`)
Planned workouts appear in the system calendar.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `91` Apple Calendar sync (core); `i135` Apple Calendar sync (core)


### Automatic programming

#### Generated training program (`plan-generation`)
The app builds a personalised multi-day program from your goals, schedule and equipment.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `103` AI-generated splits (core); `104` AI programs with set types (aspect); `105` AI split editing (aspect); `109` AI confirm before changes (aspect); `i107` AI split generator (core); `i95` Plans and splits from chat (aspect)
- **Hevy**: `84` Generated personalized program (core); `91` Full program view (aspect); `92` Next-workout preview (aspect); `93` Modify generated workouts (aspect); `98` Program variety setting (aspect); `101` Focus muscle group (aspect); `102` Target workout duration (aspect); `103` Program rest timer length (aspect); `104` Cardio in generated workouts (aspect); `105` Split type selection (aspect); `106` Training goal selection (aspect); `107` Experience level setting (aspect); `108` Weekly frequency setting (aspect); `109` Female program templates (aspect); `110` Reorder program workouts (aspect); `111` Restart program (aspect); `112` In-program workout tips (aspect); `113` Program science explainer (aspect)
- **Gravl**: `10` AI workout generation (core); `11` Weekly plan generation (aspect); `20` Skip planned workout (aspect); `21` Start any workout of the week (aspect); `22` Upcoming workouts view (aspect); `24` Workout duration setting (aspect); `25` Fitness goal selection (aspect); `26` Weekly training frequency goal (aspect); `27` Experience level setting (aspect); `28` Exercise variety level (aspect); `29` Configurable sets per exercise (aspect); `30` Configurable rep ranges (aspect); `35` Muscle focus (aspect); `83` Per-exercise advanced settings (aspect)
- **Fitbod**: `0` AI-generated personalized workouts (also); `11` Training split selection (also); `7` Experience levels (aspect); `8` Fitness goal selection (aspect); `9` Powerlifting-focused programming (aspect); `10` Olympic weightlifting programming (aspect); `11` Training split selection (aspect); `12` Workouts-per-week schedule (aspect); `13` Adjustable workout duration (aspect); `14` Exercise variability setting (aspect); `0` AI-generated personalized workouts (also); `11` Training split selection (also)

#### Generated single workout (`workout-generation`)
The app generates a personalised workout on demand (today's session).

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `102` AI-generated workout templates (core); `107` AI fills live workout (core); `i106` AI workout generator (core); `i94` Workouts built in chat (aspect)
- **Hevy**: `92` Next-workout preview (also); `92` Next-workout preview (also)
- **Gravl**: `18` AI one-off custom workout (core); `23` Per-session duration override (aspect)
- **Fitbod**: `0` AI-generated personalized workouts (core); `1` Learns from user edits (aspect); `16` Per-session workout modifiers (aspect); `17` Change today's muscle focus (aspect); `18` Swap day within training split (aspect); `41` Cardio added to strength workouts (aspect)
- **Motra**: `86` AI workout generation (core); `88` Generation duration and intensity (aspect); `89` Target muscle group selection (aspect); `90` One-off generation instructions (aspect); `91` Saved generation instructions (aspect); `93` Exercise variety preference (aspect); `102` Experience level and goals profile (aspect)

#### Automatic progressive overload (`progressive-overload`)
The app recommends when and how much to increase weight or reps based on your performance.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `85` Progressive overload suggestions (core); `86` Progression for reps-only exercises (aspect); `87` Suggested starting weights (aspect); `88` Stall reminders (aspect)
- **Gravl**: `0` Automatic progressive overload (core); `1` Rep-then-weight double progression (aspect); `43` Weight explanation insights (aspect); `46` Global recommended-weight reduction (aspect); `47` Exercise-order fatigue adjustment (aspect); `48` Cross-exercise progress transfer (aspect); `49` Time-off weight easing (aspect); `50` Per-lift learned progression thresholds (aspect); `51` Bodyweight exercise progression (aspect)
- **Fitbod**: `3` Automatic progressive overload (core); `4` Auto-recommended sets, reps and weight (aspect); `5` Conservative starting estimates for new users (aspect); `6` Return-from-break load reduction (aspect)
- **Motra**: `96` AI weight and rep recommendations (core); `97` Auto-progression levels (aspect); `99` Wellness-based progression (aspect)

#### Progression on repeated templates (`template-progression`)
Saved workouts can be re-run with automatically progressed sets, reps or weights.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `78` Saved workout progression modes (core)
- **Fitbod**: `53` Saved workout re-progression (core)
- **Motra**: `98` Progression for custom templates (core)

#### Recovery-driven workout selection (`recovery-planning`)
The next workout's muscles are chosen from estimated per-muscle recovery.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `12` Recovery-based adaptive split (core); `111` Rest day recommendation (aspect)
- **Fitbod**: `11` Training split selection (also); `17` Change today's muscle focus (also); `20` Workout auto-refresh on new data (aspect); `11` Training split selection (also); `17` Change today's muscle focus (also)
- **Motra**: `87` Readiness-aware generation (core); `84` Template recovery match (aspect)

#### Automatically generated supersets (`auto-supersets`)
Generated workouts can group exercises into supersets or circuits automatically.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `62` Supersets (also); `62` Supersets (also)
- **Fitbod**: `42` Automatic supersets and circuits (core)
- **Motra**: `94` Generated warm-ups, cool-downs and supersets (core)

#### Exercise exclusions and preferences (`exercise-preferences`)
Exclude exercises (or muscles) from recommendations, or ask for some more often.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `96` Excluded exercises list (core)
- **Gravl**: `37` Exercise exclusion (core); `38` Favorite exercises prioritized (core); `36` Muscle group exclusion (aspect); `39` Exercise queue (aspect)
- **Fitbod**: `22` Exercise preference controls (core)
- **Motra**: `92` Excluded exercises (core)

#### Injury-aware programming (`injury-aware`)
Record injuries or painful movements and recommendations avoid or substitute aggravating exercises.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `106` AI injury-aware planning (core)
- **Hevy**: `97` Injury-aware programming (core)
- **Gravl**: `40` Injury-aware programming (core); `41` Injury check-ins (aspect)
- **Fitbod**: `23` Injury and limitation adjustments (core)
- **Motra**: `103` Injury-aware exercise selection (core)

#### Gym equipment profiles (`equipment-profiles`)
Saved gym/equipment profiles restrict recommended exercises to what you have.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `99` Program equipment profiles (core)
- **Gravl**: `6` Equipment-aware workout generation (core); `98` Multiple gym profiles (core); `94` Custom equipment (aspect); `95` AI equipment recognition from photo (aspect); `96` Machine weight ranges from photo (aspect); `99` Gym search and equipment preload (aspect)
- **Fitbod**: `32` Equipment-based workout filtering (core); `34` Multiple gym locations (core); `30` Bodyweight-only mode (aspect); `31` Home training without equipment (aspect); `35` Share gym equipment setup (aspect)
- **Motra**: `100` Gym equipment profiles (core)

#### Available weights and increments (`owned-weights`)
Tell the app which dumbbells, plates or machine increments you have so suggestions are loadable.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `100` Available dumbbell and plate weights (core)
- **Gravl**: `2` Weights snapped to owned equipment (core); `97` Per-machine weight increments (core); `100` Equipment configuration (aspect)
- **Fitbod**: `33` Custom weight increments (core); `36` Resistance band collection (aspect)
- **Motra**: `101` Custom weight increments (core)

#### Periodization (deloads, phases, test days) (`periodization`)
Planned variation over weeks: deload periods, phased progressions or max-effort test days.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **Gravl**: `34` Scheduled deload periods (core)
- **Fitbod**: `2` Non-linear periodization (core); `15` Focus lifts with 4-week phased progression (core); `21` Max effort test days (core)

#### Regenerate today's workout (`workout-regeneration`)
Ask for a new version of a generated workout.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `19` Workout regeneration (core)
- **Fitbod**: `19` Regenerate workout on demand (core)
- **Motra**: `95` Regenerate with feedback (core)

#### Weekly set targets per muscle (`weekly-set-targets`)
Recommended weekly working-set ranges per muscle, with progress against them.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **Hevy**: `90` Recommended weekly sets range (core); `89` Program progress report (aspect)
- **Gravl**: `142` Weekly set volume trends (also); `142` Weekly set volume trends (also)
- **Fitbod**: `24` Weekly set targets per muscle (core)


### AI & voice

#### AI coach chat (`ai-coach-chat`)
A conversational AI coach inside the app that answers using your own training data.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra partial

- **SPLYT**: `96` AI coach chat (core); `97` AI long-term memory (aspect); `98` AI charts in chat (aspect); `99` AI web search (aspect); `100` AI photo understanding (aspect); `101` Searchable AI chat history (aspect); `113` AI exercise cards in chat (aspect); `i93` Splyt AI chat (core); `i96` Habits managed in chat (aspect); `i97` Log sleep, weight and notes (aspect); `i99` Answers from your history (aspect); `i100` Web answers with sources (aspect); `i101` Photos in AI chat (aspect); `i102` Chat history and search (aspect); `i103` Coach memory (aspect); `i104` Coach style (aspect); `i272` AI coach nudges (aspect); `108` AI goal setting and coaching (aspect); `i98` Goal suggestions (aspect)
- **Motra**: `104` AI coach chat (core) ✗ [not_shipped]; `105` Video upload to AI coach (aspect); `106` Save coach-suggested templates (aspect)
- _Decision — Motra = partial:_ Announced in release 6.3.0 (2026-05-22) as a staged rollout 'in the coming week'; no help article documents it, so availability to all users is unconfirmed. Source: https://apps.apple.com/us/app/id1548577496

#### AI-written training summaries (`ai-summaries`)
AI-written plain-language summaries of a workout or a training week.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `110` Weekly AI insights (core); `111` Weekly plain-language recap (aspect); `112` Insight history (aspect); `i105` Weekly coach notes (core); `i224` Coach's read in recaps (aspect); `i271` Weekly AI insight (aspect)
- **Gravl**: `52` Weekly AI score explanation (core); `53` AI workout summaries (core)

#### Form analysis from video (`ai-form-analysis`)
Record or upload a video of a set and get a form score or feedback.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **Gravl**: `54` AI form analysis (core); `55` Form score history and friend leaderboard (aspect)

#### AI progress-photo analysis (`ai-physique-analysis`)
AI commentary on progress photos.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `114` AI progress photo analysis (core); `i108` Progress photo analysis (core)

#### AI-filled custom exercises (`ai-custom-exercise`)
AI fills in a custom exercise's details from its name or a video link.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `71` AI-filled custom exercise details (core); `i10` AI fill for custom exercises (core)
- **Gravl**: `92` AI-filled custom exercise by name (core); `91` Custom exercise from video link (aspect)

#### ChatGPT / Claude / MCP integration (`external-ai`)
Connect external AI assistants (ChatGPT, Claude, MCP clients) to your training data.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **Hevy**: `114` ChatGPT app integration (core); `115` AI-generated plan import (aspect); `116` Send workout to AI assistants (aspect)
- **Gravl**: `168` MCP server for AI assistants (core)
- **Motra**: `107` Connect to external AI assistants (core); `108` Create templates via AI assistant (aspect)

#### Voice logging (`voice-logging`)
Log sets, workouts or plans by speaking.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl partial · Fitbod unknown · Motra unknown

- **SPLYT**: `116` Voice set logging (core); `117` Voice correction of logged sets (aspect); `118` Voice superset grouping (aspect); `119` Voice workout commands (aspect); `120` Voice template builder (aspect); `121` Voice split builder (aspect); `122` Voice quick-log after the fact (aspect); `123` Voice grip setting (aspect); `66` Voice day logging (aspect); `133` Watch voice start (aspect); `134` Watch voice logging (aspect); `i90` Voice set logging (core); `i91` Log past workouts by voice (aspect); `i92` Build a template by talking (aspect); `i118` Describe your split aloud (aspect); `i66` Start a workout by voice (aspect); `i74` Voice logging on the watch (aspect)
- _Decision — Gravl = partial:_ Gravl's help says workouts can be described out loud, but the feature is labelled Beta (publicly offered in the app). Not in the extracted claims because the brief excluded beta items; added here as partial. Source: https://gravl.ai/help/create-a-one-time-custom-workout

#### Head-gesture logging (`head-gesture-logging`)
Log sets hands-free with head gestures through headphones.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra unknown

- **Fitbod**: `119` Head-gesture set logging (core)


### Exercise library & content

#### Built-in exercise library (`exercise-library`)
A built-in catalogue of exercises (size as stated by the app).

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `67` Exercise library size (core); `i6` Exercise library (core)
- **Hevy**: `74` Exercise library 400+ (core); `14` Hybrid/HYROX functional exercises (aspect)
- **Strong**: `106` Exercise library (200+) (core)
- **Gravl**: `7` Exercise video library (also); `7` Exercise video library (also)
- **Fitbod**: `78` Exercise library 1,000+ (1,600+) (core); `83` Pregnancy-safe exercise category (aspect); `84` Cardio exercises (aspect); `85` Mobility exercises (aspect); `86` Partner exercises (aspect); `87` Olympic lift progressions (aspect); `88` Plyometric exercises (aspect); `89` Exercise effectiveness score (aspect)
- **Motra**: `64` 1,000+ exercise library expansion (core); `68` Exercise difficulty levels (aspect)

#### Exercise demonstration videos or animations (`exercise-demos`)
Each exercise has a video or animated demonstration.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `68` Animated exercise demos (core); `i7` Exercise how-to (core)
- **Hevy**: `75` Exercise demo videos (core)
- **Strong**: `5` Exercise demonstration videos (core)
- **Gravl**: `7` Exercise video library (core)
- **Fitbod**: `79` Multi-angle HD exercise videos (core)

#### Written exercise instructions (`exercise-instructions`)
Step-by-step written instructions for exercises.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `68` Animated exercise demos (also); `i7` Exercise how-to (also); `68` Animated exercise demos (also); `i7` Exercise how-to (also)
- **Hevy**: `76` Step-by-step exercise instructions (core); `47` Exercise how-to in workout (aspect)
- **Strong**: `4` Exercise instructions (core)
- **Gravl**: `9` Exercise instructions (core)
- **Fitbod**: `80` Written exercise instructions (core)
- **Motra**: `66` Exercise detail pages (core)

#### Target muscles per exercise (`exercise-muscle-map`)
Shows the primary and secondary muscles an exercise works.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `69` Exercise muscle map (core)
- **Fitbod**: `81` Target muscle breakdown per exercise (core)
- **Motra**: `66` Exercise detail pages (also); `66` Exercise detail pages (also)

#### Exercise search and filters (`exercise-search`)
Search the exercise library and filter it by muscle or equipment.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `73` Browse exercise library outside workout (core); `i5` Exercise picker (core)
- **Hevy**: `74` Exercise library 400+ (also); `74` Exercise library 400+ (also)
- **Strong**: `48` Exercise search (core)
- **Gravl**: `88` Exercise library search and filters (core); `89` Last-trained date per exercise (aspect)
- **Fitbod**: `82` Exercise search and filters (core)
- **Motra**: `67` Exercise search tab (core)

#### Custom exercises (`custom-exercises`)
Create your own exercises.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `70` Custom exercises (core); `72` Share custom exercises (aspect); `i9` Custom exercises (core)
- **Hevy**: `77` Custom exercises (core); `78` Custom exercise media (aspect); `79` Duplicate exercise (aspect)
- **Strong**: `0` Custom exercise creation (core); `59` Rename custom exercises (aspect)
- **Gravl**: `90` Custom exercises (core); `93` Custom exercises in generated workouts (aspect)
- **Fitbod**: `65` Custom exercises (core)
- **Motra**: `69` Custom exercises (core); `70` Custom exercise photos (aspect)

#### Hide, merge or reset exercise data (`library-management`)
Hide unwanted library exercises, merge one exercise's history into another, or reset history from a date.

_Result:_ SPLYT unknown · Hevy unknown · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **Strong**: `104` Merge exercise data (core); `105` Hide exercises (core); `61` Start history from date (core)

#### Offline exercise videos (`offline-videos`)
Download exercise videos to watch without a connection.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod no · Motra unknown

- **Gravl**: `8` Offline exercise video downloads (core)
- _Decision — Fitbod = no:_ Fitbod's help says offline video is unavailable. Source: https://help.fitbod.me/hc/en-us/articles/30721437384215-How-to-Navigate-the-Exercise-Details-Screen

#### Warm-up, stretching and mobility routines (`warmup-routines`)
Stretching, mobility or warm-up exercise routines added before or after workouts.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `66` Warm-up exercise routines (core); `67` Stretching cool-down routines (core)
- **Fitbod**: `38` Warm-up and cool-down stretching (core); `39` Foam-rolling soft-tissue work (aspect); `40` Muscle primer activation drills (aspect)
- **Motra**: `65` Stretches and warm-up exercises (core)

#### In-app tutorials and guided setup (`app-tutorials`)
Built-in or official how-to guidance for using the app.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `246` Interactive logging tutorial (core); `i276` Guided setup (aspect)
- **Motra**: `72` Video tutorial guide (core)


### Stats & progress

#### Personal records (`personal-records`)
Personal records are detected automatically, ideally flagged as they happen.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `35` Personal record celebrations (core); `74` Exercise history and 1RM (also); `i231` Exercise personal records (core); `i219` Top personal records list (aspect); `i236` Live PR detection (aspect); `i237` PRs on workout summary (aspect); `74` Exercise history and 1RM (also)
- **Hevy**: `120` Personal records tracking (core); `122` Live PR notifications (aspect); `123` PR medals on workouts (aspect)
- **Strong**: `6` Personal records tracking (core)
- **Gravl**: `84` Automatic PR detection (core); `85` PR and workout celebrations (aspect); `101` Per-gym records and 1RMs (aspect)
- **Fitbod**: `94` Personal records (core)
- **Motra**: `117` Automatic PR detection (core)

#### Records by rep count (`rep-max-table`)
A table of best (and predicted) weights for each rep count.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra yes

- **Hevy**: `121` Set records table (core)
- **Strong**: `62` Records screen (core); `63` Projected rep-max table (core)
- **Motra**: `113` Rep-range PR table (core)

#### Estimated one-rep max (`estimated-1rm`)
Estimated 1RM calculated from logged sets.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `74` Exercise history and 1RM (also); `i230` Estimated 1RM (core); `74` Exercise history and 1RM (also)
- **Hevy**: `65` Estimated one-rep max (core)
- **Strong**: `7` Estimated one-rep max (core)
- **Gravl**: `44` Estimated 1RM tracking (core); `45` Manual 1RM override (aspect)
- **Fitbod**: `90` Estimated one-rep max (core)
- **Motra**: `112` Estimated one-rep max (core)

#### Per-exercise progress charts (`exercise-charts`)
Charts of an exercise's weight, 1RM, volume or reps over time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `74` Exercise history and 1RM (core); `i229` Exercise progress chart (core)
- **Hevy**: `117` Exercise progress charts (core); `118` Cardio pace and distance charts (aspect)
- **Strong**: `18` Volume progression chart (core); `19` 1RM progression chart (core); `103` Per-exercise charts (core)
- **Gravl**: `136` Exercise analytics (core)
- **Fitbod**: `95` Exercise history charts (core)
- **Motra**: `114` Exercise trends (core)

#### Per-exercise history (`exercise-history`)
A list of every past session of a given exercise.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `74` Exercise history and 1RM (also); `i232` Exercise history (core); `74` Exercise history and 1RM (also)
- **Hevy**: `119` Exercise history (core)
- **Strong**: `102` Exercise history view (core)
- **Gravl**: `137` Exercise history (core)
- **Motra**: `114` Exercise trends (also); `114` Exercise trends (also)

#### Training volume tracking (`volume-tracking`)
Total volume (weight x reps) calculated per workout and over time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `173` Volume and cardio trends (core); `i218` Workout stats and weekly volume (core); `i220` Volume and cardio trends (aspect)
- **Hevy**: `133` Profile dashboard trends (also); `133` Profile dashboard trends (also)
- **Strong**: `8` Total weight lifted (core); `110` Count dumbbells twice option (aspect)
- **Fitbod**: `96` Volume tracking (core)
- **Motra**: `111` Total volume lifted (core)

#### Workout frequency and duration trends (`training-trends`)
Charts of how often and how long you train over time.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `171` Training time charts (core); `172` Workout frequency chart (core); `177` Session vs history card (aspect); `i215` Activity per week chart (core); `i212` Against your history (aspect); `i216` Time-of-day chart (aspect); `i217` Activity category filter (aspect); `i210` Stats overview numbers (aspect)
- **Hevy**: `133` Profile dashboard trends (core); `130` Most-logged exercises (aspect)

#### Sets or volume per muscle group (`muscle-breakdown`)
Stats breaking training down by muscle group.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `169` Volume by body part (core); `i220` Volume and cardio trends (also); `i211` Muscle load map (also); `i220` Volume and cardio trends (also); `i211` Muscle load map (also)
- **Hevy**: `125` Muscle group graphs (core); `127` Sets per muscle group chart (core); `128` Muscle distribution chart (core); `129` Weekly muscle body diagram (core)
- **Gravl**: `142` Weekly set volume trends (core)
- **Fitbod**: `24` Weekly set targets per muscle (also); `24` Weekly set targets per muscle (also)
- **Motra**: `126` Muscle set-distribution widget (also); `126` Muscle set-distribution widget (also)

#### Muscle heatmap (`muscle-heatmap`)
A body diagram shading the muscles trained in a workout or period.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `180` Rich workout summary (also); `i13` Muscle heatmap per workout (core); `i211` Muscle load map (core); `180` Rich workout summary (also)
- **Hevy**: `126` 7-day body heatmap (core); `46` Live muscle heatmap while logging (aspect); `71` Female body model (aspect)
- **Strong**: `56` Muscle heat map (core) ✗ [unsubstantiated]
- **Fitbod**: `29` Post-workout muscle impact map (core)
- **Motra**: `82` Muscle map for templates (also); `82` Muscle map for templates (also)
- _Decision — Strong = unknown:_ Named only in one variant of the homepage feature strip; not described anywhere else. Source: https://strong.app/

#### Strength score or level (`strength-score`)
A score or level rating your strength against standards or other users.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **Hevy**: `124` Strength level percentile (core)
- **Gravl**: `5` Strength score (core); `138` Strength score levels (aspect); `139` Strength score weekly summary (aspect); `140` Strength score expiry alerts (aspect); `141` Exclude muscles from strength score (aspect)
- **Fitbod**: `91` Per-muscle strength score (core); `92` Overall strength score (core); `93` Benchmark lift tracking (aspect); `97` Exercise percentile ranking (aspect) ✗ [not_shipped]

#### Weekly, monthly or yearly recaps (`workout-recaps`)
Periodic recap reports of your training.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `178` Weekly and monthly recaps (core); `183` Weekly score (aspect); `i222` Weekly recap (core); `i223` Monthly recap (core); `i270` Weekly summary push (aspect)
- **Hevy**: `131` Monthly report (core); `132` Year in review (core)
- **Gravl**: `143` Monthly review (core); `144` Monthly review stories (aspect)
- **Fitbod**: `98` Weekly and monthly workout reports (core); `99` Custom date-range reporting (aspect); `100` Year-in-review recap (aspect)

#### Customisable dashboard (`stats-dashboard`)
Choose which stats, charts or cards appear on a dashboard or home screen.

_Result:_ SPLYT yes · Hevy unknown · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `235` Home view customization (core); `i208` Customize Home (core); `i207` Daily overview stats (aspect)
- **Strong**: `70` Customizable profile dashboard (core); `72` Pin exercise charts to dashboard (core)

#### Post-workout summary (`workout-summary`)
A summary screen of the finished workout's stats.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra unknown

- **SPLYT**: `180` Rich workout summary (core); `i11` Workout summary (core); `i15` Per-activity breakdown (aspect)
- **Fitbod**: `29` Post-workout muscle impact map (also); `29` Post-workout muscle impact map (also)

#### Real-world volume comparisons (`volume-comparison`)
Total weight lifted expressed as a real-world comparison.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `218` Volume receipt share (core)
- **Hevy**: `140` Volume comparisons (core)

#### Training streaks (`training-streak`)
A streak of consecutive days or weeks of training (or of meeting a weekly goal).

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `i170` Workout streak (core)
- **Hevy**: `136` Weekly streak (core); `137` Streak recovery by backfilling (aspect); `138` Rest days counter (aspect)
- **Strong**: `45` Weekly workout streaks (core); `71` Weekly workout goal (aspect)
- **Gravl**: `157` Weekly goal streaks (core); `158` Streak freezes (aspect)
- **Fitbod**: `102` Weekly workout goal and streaks (core)
- **Motra**: `118` Custom weekly streak goal (core); `119` External workouts count toward streak (aspect); `122` Streak reminder notifications (aspect)

#### Achievements, badges and levels (`achievements`)
Badges, milestones or levels earned for training.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `139` Workout count milestones (core)
- **Gravl**: `159` Achievement badges (core); `160` XP and levels (aspect)
- **Fitbod**: `101` Milestone badges (core)
- **Motra**: `116` Achievements (core)

#### Calories burned (`calories-burned`)
Active calories recorded or estimated for workouts.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `126` Apple Watch app (also); `i78` Live heart rate and calories (also); `126` Apple Watch app (also); `i78` Live heart rate and calories (also)
- **Hevy**: `141` Watch heart rate and calories on workouts (also); `220` Active calories to Apple Health (also); `141` Watch heart rate and calories on workouts (also); `220` Active calories to Apple Health (also)
- **Strong**: `75` Calories burned tracking on watch (core)
- **Gravl**: `122` Watch heart rate and calories (also); `122` Watch heart rate and calories (also)
- **Fitbod**: `103` Calorie estimation (core)
- **Motra**: `31` Calorie tracking (core); `32` Manual calorie editing (aspect)


### Health, body & recovery

#### Workouts written to Apple Health (`apple-health-write`)
Finished workouts are saved to Apple Health.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `150` Apple Health two-way sync (core); `i160` Workouts saved to Health (core)
- **Hevy**: `219` Apple Health workout export (core); `220` Active calories to Apple Health (aspect); `222` Per-workout sync toggles (aspect)
- **Strong**: `65` Write workouts to Apple Health (core)
- **Gravl**: `113` Apple Health sync (core)
- **Fitbod**: `107` Apple Health workout export (core); `110` Per-workout health sync toggle (aspect)
- **Motra**: `131` Apple Health workout sync (core)

#### Import workouts from Apple Health (`apple-health-import`)
Workouts recorded by other apps are brought in from Apple Health.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `151` Auto-import external workouts (core); `i159` Apple Health workout import (core)
- **Strong**: `64` Import workouts from Apple Health (core) ✗ [fix]
- **Gravl**: `114` External workout import (core)
- **Fitbod**: `108` Apple Health workout import (core)
- **Motra**: `132` Import workouts from Apple Health (core)

#### Body data synced with Apple Health (`health-body-data`)
Body weight or composition is read from or written to Apple Health.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `i165` Weight sync with Health (core)
- **Hevy**: `144` Lean body mass (core)
- **Strong**: `66` Read body metrics from Apple Health (core)
- **Gravl**: `116` Bodyweight sync from Apple Health (core) ✗ [fix]
- **Fitbod**: `109` Apple Health body data sync (core); `106` Smart scale data via health platforms (aspect)
- **Motra**: `133` Body metrics from Apple Health (core)

#### Body weight log (`bodyweight-tracking`)
Log body weight over time with a trend.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `i238` Body weight log (core); `174` Weight trend (aspect); `i221` Body metrics trends (aspect)
- **Hevy**: `142` Body measurements (also); `142` Body measurements (also)
- **Strong**: `22` Body weight tracking (core)
- **Gravl**: `146` Body metrics dashboard (also); `146` Body metrics dashboard (also)
- **Fitbod**: `104` Body composition tracking (core); `105` Manual body metric entry (core)

#### Body measurements (circumferences, body fat) (`body-measurements`)
Log body measurements beyond weight, such as circumferences or body-fat %.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **SPLYT**: `154` Body weight and measurements (core) ✗ [unsubstantiated]
- **Hevy**: `142` Body measurements (core); `143` Left/right limb measurements (aspect); `148` Backdated measurements (aspect)
- **Strong**: `21` Body measurement tracker (core); `23` Body fat percentage tracking (core); `24` Body part circumference measurements (core)
- **Gravl**: `145` Body measurements logging (core); `146` Body metrics dashboard (aspect); `147` Measurement trends (aspect)
- **Fitbod**: `104` Body composition tracking (also); `104` Body composition tracking (also)
- _Decision — SPLYT = unknown:_ Website says 'body weight and measurements', but the feature index describes a body weight log only. Source: https://splyt.fit/roadmap

#### Progress photos (`progress-photos`)
Store private progress photos over time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `158` Progress photos (core); `i239` Progress photos (core); `i240` Photo alignment guides (aspect); `i241` Side-by-side photo compare (aspect); `i242` Edit progress photos (aspect); `i243` Progress photo reminders (aspect)
- **Hevy**: `145` Progress photos (core); `146` Progress photo overlay (aspect); `147` Progress photo comparison (aspect)
- **Strong**: `33` Progress photos (core)
- **Gravl**: `148` Progress photos (core); `149` Before/after photo comparison (aspect)

#### Calorie and macro logging (`nutrition-logging`)
Log food calories or macronutrients.

_Result:_ SPLYT no · Hevy unknown · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **Strong**: `25` Calorie intake logging (core); `67` Nutrition sync via Apple Health (core); `68` Macronutrient tracking with goals (core); `69` Daily calorie goal (core)
- _Decision — SPLYT = no:_ Removed in build 374. Source: https://splyt.fit (in-app What's New, build 374)

#### Sleep tracking (`sleep-tracking`)
View sleep (e.g. from Apple Health) or log it.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `152` Sleep tracking with stages (core); `153` Manual sleep logging (aspect); `i162` Sleep from Apple Health (core); `i163` Add sleep manually (aspect)

#### Steps tracking (`steps-tracking`)
Steps history in the app.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `155` Steps tracking (core); `i164` Step pace (core)

#### Activity rings in the app (`activity-rings`)
Move/Exercise/Stand rings shown inside the app.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `156` Activity rings in app (core); `157` Activity rings detail view (aspect); `i161` Activity rings detail (core); `i169` Activity goals (aspect)

#### Habit and daily-goal tracking (`habit-tracking`)
Track daily habits or a combined daily goal, with streaks and reminders.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `160` Habit tracking (core); `161` Auto-completing habits (aspect); `162` Weekly habit targets (aspect); `163` Habit reminders and privacy (aspect); `164` Habit streak calendar (aspect); `i154` Create habits (core); `i155` Habits that tick themselves (aspect); `i156` Habit options (aspect); `i157` Habit calendar and streaks (aspect); `i266` Habit reminders (aspect); `165` Daily combined ring (aspect); `166` Customizable ring pillars (aspect); `167` Ring closed notification (aspect); `168` Perfect-day nudge (aspect); `234` Ring color themes (aspect) ✗ [unsubstantiated]; `i166` Splyt Ring (aspect); `i167` Customise the Splyt Ring (aspect); `i84` Rings page (aspect); `i265` Ring reminder (aspect)

#### Muscle recovery tracking (`muscle-recovery`)
Per-muscle recovery or fatigue estimates.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `109` Muscle recovery tracking (core); `110` Manual recovery adjustment (aspect); `112` External cardio counts toward recovery (aspect)
- **Fitbod**: `25` Muscle recovery tracking (core); `26` Recovery body heat map (aspect); `27` Manual recovery override (aspect); `28` Outside activity counts toward recovery (aspect)
- **Motra**: `109` Muscle recovery tracking (core); `110` Recovery body map (aspect)

#### Heart rate during workouts (`heart-rate`)
Heart rate recorded and shown during or after a workout.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `38` Live heart-rate graph vs last time (core); `i58` Live heart rate on iPhone (core); `i78` Live heart rate and calories (aspect)
- **Hevy**: `194` Heart rate during workout (core); `141` Watch heart rate and calories on workouts (aspect)
- **Strong**: `74` Heart rate tracking on watch (core)
- **Gravl**: `122` Watch heart rate and calories (core)
- **Fitbod**: `124` Watch live heart rate (core); `116` Live heart rate during workouts (aspect) ✗ [not_shipped]
- **Motra**: `29` Heart rate tracking (core)

#### Heart-rate zones (`hr-zones`)
Time in heart-rate zones for a workout.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `159` Heart rate zones (core); `i12` Heart-rate chart and zones (core)
- **Motra**: `30` Customizable heart rate zones (core)


### Cardio, sports & other activities

#### Cardio exercise logging (`cardio-logging`)
Log cardio with distance and/or time.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `64` Machine console photo scan (also); `64` Machine console photo scan (also)
- **Hevy**: `9` Distance and cardio exercise logging (core)
- **Strong**: `1` Cardio exercise logging (core); `109` Distance-based exercises (core)
- **Gravl**: `75` Cardio workout logging (core)
- **Fitbod**: `69` Distance, time and machine-setting logging (core)
- **Motra**: `51` Reps, distance or time measurement (also); `51` Reps, distance or time measurement (also)

#### Non-lifting activity types (`activity-types`)
Track many activity types beyond lifting (sports, yoga, classes, recovery sessions such as sauna).

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `52` 90+ activity types (core); `54` Sports activity tracking (core); `57` Core training workout type (aspect); `i21` Start any of 93 activities (core); `i52` Timer view for sports and classes (core); `i22` Custom-named activity (aspect); `63` Recovery activity logging (aspect); `175` Recovery stats chart (aspect); `i53` Recovery activities (aspect)

#### Multi-activity sessions (`multi-activity-session`)
Chain several activities into one saved session.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `53` Multi-activity sessions (core); `i51` Multi-activity sessions (core); `i77` Add an activity to a session (aspect)

#### GPS outdoor tracking (`gps-tracking`)
Track outdoor runs, walks or rides with GPS distance and pace.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `58` Phone-only GPS outdoor tracking (core); `60` Elevation gain (aspect); `i54` Phone GPS for outdoor workouts (core); `i79` GPS distance workouts (aspect)

#### Route maps (`route-maps`)
Outdoor workouts show a route map.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `59` Route maps (core); `i14` Route, elevation and weather (core)
- **Gravl**: `115` Route maps for imported workouts (core)

#### Swim tracking (`swim-tracking`)
Pool laps or open-water swims tracked.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `61` Pool swim lap counting (core); `62` Open water swim stroke count (aspect); `146` Watch pool length setting (aspect); `i80` Pool and open-water swims (core); `i57` Pool length for swims (aspect)

#### Interval and round timers (`interval-timers`)
Timed intervals for HIIT, Tabata, circuits or boxing rounds.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra unknown

- **SPLYT**: `7` Circuits (core); `55` Boxing round timer (core); `56` HIIT and Tabata timers (core); `i55` Round timer for combat sports (core); `i56` Timed circuit builder (core)
- **Fitbod**: `46` Timed interval (HIIT) workouts (core); `47` Hands-free interval auto-play (aspect)

#### Read a cardio machine screen by photo (`machine-photo-scan`)
Photograph a cardio machine's display to import its numbers.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `64` Machine console photo scan (core); `i17` Scan a cardio machine screen (core)


### Apple Watch & wearables

#### Apple Watch app (`watch-app`)
An Apple Watch app for logging strength workouts.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `126` Apple Watch app (core); `132` Watch Digital Crown entry (aspect); `136` Watch rest screen with heart rate (aspect); `137` Watch next-set preview (aspect); `138` Watch music controls (aspect); `141` Watch rest timer button (aspect); `142` Watch workout summary HR chart (aspect); `143` Watch notifications (aspect); `242` Watch-routed notifications (aspect); `i67` Log sets on the wrist (core); `i62` Start workouts from the watch (aspect); `i75` Rest timer on the watch (aspect); `i76` Workout controls (aspect); `i81` Music controls mid-workout (aspect); `i82` Rate your effort (aspect); `i83` Watch workout summary (aspect); `i88` Reply to friends from the watch (aspect); `i89` Rich watch notifications (aspect)
- **Hevy**: `187` Apple Watch app (core); `190` Watch set logging (aspect); `195` Watch duration timers (aspect)
- **Strong**: `2` Standalone Apple Watch logging (also); `47` Watch button repeat setting (aspect); `58` Watch exercise details (aspect); `77` Digital Crown value entry (aspect); `78` Adjust rest timer on watch (aspect); `80` Exercise history and notes on watch (aspect); `84` Warm-up sets and timers on watch (aspect); `2` Standalone Apple Watch logging (also)
- **Gravl**: `120` Apple Watch set logging (core); `121` Watch haptic rest timer (aspect); `123` Watch PR celebration (aspect)
- **Fitbod**: `120` Apple Watch app (core); `121` Log sets on Apple Watch (aspect); `123` Watch rest timer with haptics (aspect)
- **Motra**: `19` Apple Watch app (core); `23` Customizable watch workout display (aspect)

#### Watch logging without the phone (`watch-standalone`)
Log a whole workout on the watch without the iPhone nearby.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl no · Fitbod no · Motra yes

- **SPLYT**: `149` Watch-only gym use (core) ✗ [unsubstantiated]
- **Hevy**: `187` Apple Watch app (also); `196` Watch offline auto-save (also); `187` Apple Watch app (also); `196` Watch offline auto-save (also)
- **Strong**: `2` Standalone Apple Watch logging (core)
- **Gravl**: `4` Standalone Apple Watch app (core) ✗ [unsubstantiated]
- **Motra**: `27` Offline watch workout storage (also); `27` Offline watch workout storage (also)
- _Decision — SPLYT = unknown:_ The website says no phone is needed; SPLYT's detailed feature index says only that the watch starts recording 'without touching your phone'. Not enough to confirm logging with the phone away. Source: https://splyt.fit/
- _Decision — Gravl = no:_ App Store copy calls the watch app standalone, but Gravl's help says the phone must be within reach. Source: https://gravl.ai/help/gravl-on-your-apple-watch
- _Decision — Fitbod = no:_ Fitbod's help says the watch app is a companion. Source: https://help.fitbod.me/hc/en-us/articles/360006499194-Apple-Watch

#### Start templates or plans on the watch (`watch-templates`)
Start a saved template, routine or today's planned workout from the watch.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod no · Motra yes

- **SPLYT**: `i64` Saved templates on the watch (core); `i65` Today's plan on the watch (aspect)
- **Hevy**: `189` Routines on watch (core); `197` Generated workout on watch (aspect)
- **Gravl**: `126` Start workout from watch (core)
- **Motra**: `22` Sync templates to watch (core); `20` Start workouts on the watch (aspect)
- _Decision — Fitbod = no:_ Workouts must be started on the iPhone. Source: https://help.fitbod.me/hc/en-us/articles/360006499194-Apple-Watch

#### Live phone-watch sync (`watch-phone-sync`)
The same workout is mirrored live on phone and watch.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `135` Watch auto-start from phone (core); `i85` Phone and watch in sync (core)
- **Hevy**: `188` Watch-phone live sync (core)
- **Strong**: `73` Phone-watch live sync (core); `76` Handoff between watch and phone (aspect)
- **Gravl**: `125` Live phone-watch sync (core)
- **Fitbod**: `121` Log sets on Apple Watch (also); `121` Log sets on Apple Watch (also)
- **Motra**: `21` Phone-watch workout mirroring (core)

#### Edit workout structure on the watch (`watch-workout-editing`)
Add or delete sets, or add, swap or reorder exercises, from the watch.

_Result:_ SPLYT yes · Hevy unknown · Strong yes · Gravl unknown · Fitbod partial · Motra yes

- **SPLYT**: `130` Watch set editing (core); `131` Watch exercise swap (aspect); `139` Watch supersets (aspect); `i70` Add an exercise mid-workout (core); `i69` Supersets on the watch (aspect); `i71` Switch exercise on the watch (aspect); `i72` Grip picker on the watch (aspect)
- **Strong**: `83` Add and delete sets on watch (core); `60` Replace exercise on watch (aspect); `81` Supersets on watch (aspect); `82` Reorder exercises on watch (aspect)
- **Fitbod**: `122` Edit sets on Apple Watch (core)
- **Motra**: `21` Phone-watch workout mirroring (also); `24` Exercise notes on watch (aspect); `21` Phone-watch workout mirroring (also)
- _Decision — Fitbod = partial:_ Sets can be added or removed on the watch, but swapping or adding exercises requires the iPhone. Source: https://help.fitbod.me/hc/en-us/articles/360006499194-Apple-Watch

#### Set types and effort on the watch (`watch-set-types`)
Tag set types or rate effort from the watch.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `140` Watch set type tagging (core); `i68` Warm-up, drop and failure sets (core)
- **Hevy**: `191` Watch set types (core)
- **Strong**: `79` Set type and RPE on watch (core)
- **Gravl**: `124` Watch effort rating (core)
- **Fitbod**: `125` Effort rating on Apple Watch (core)
- **Motra**: `41` Tempo tracking (core)

#### Watch complications (`watch-complications`)
App complications or widgets on the watch face.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `144` Watch complications (core); `i86` Splyt ring complication (core); `i87` Activity rings complication (aspect)
- **Hevy**: `192` Watch complications (core)
- **Gravl**: `128` Apple Watch complication (core)
- **Motra**: `26` Watch streak complications (core)

#### Custom watch faces (`watch-faces`)
App-provided Apple Watch faces.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `145` Ring watch face via Photos (core)
- **Hevy**: `193` Custom watch faces (core)

#### Automatic rep counting (`auto-rep-counting`)
The watch counts reps automatically from motion.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `127` Automatic rep counting (core); `128` On-device offline rep counting (aspect) ✗ [unsubstantiated]; `129` Full-screen phone rep count (aspect); `i73` Auto Reps (core)
- **Motra**: `1` Automatic rep counting (core); `11` Adjustable minimum rep threshold (aspect); `18` Unilateral rep counting (aspect)

#### Automatic exercise detection (`auto-exercise-detection`)
The watch identifies which exercise you are doing (and when sets start and end) from motion alone.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **Motra**: `0` Automatic exercise detection (core); `2` 470+ auto-detectable exercises (aspect); `3` No camera or video required (aspect); `4` Automatic set start/end detection (aspect); `5` Grip and variation recognition (aspect); `6` Detects free-weight, cable, machine and bodyweight exercises (aspect); `7` Automatic superset detection (aspect); `8` Personalized detection learning (aspect); `9` Detection learning toggle (aspect); `10` Reset detection learning (aspect); `12` Pause auto-detection mid-workout (aspect); `13` Manual-mode default for watch workouts (aspect); `14` Higher-accuracy detection model tier (aspect); `15` Auto-detection of custom exercises in templates (aspect)

#### Heart rate from AirPods (`airpods-heart-rate`)
Read heart rate from AirPods Pro during workouts.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod partial · Motra unknown

- **Hevy**: `198` AirPods heart rate (core)
- **Gravl**: `119` Heart rate from AirPods (core)
- **Fitbod**: `117` AirPods Pro heart rate (core)
- _Decision — Fitbod = partial:_ Live heart rate (including AirPods Pro 3) is 'gradually rolling out' per Fitbod's own help article. Source: https://help.fitbod.me/hc/en-us/articles/360056464934-Apple-AirPod-Pros

#### Bluetooth heart-rate monitors (`bluetooth-hr`)
Connect Bluetooth chest straps or other BLE heart-rate monitors.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod partial · Motra unknown

- **Fitbod**: `118` Bluetooth heart rate monitors (core)
- _Decision — Fitbod = partial:_ Android only, and part of live heart rate, which is still 'gradually rolling out'. Not available on iPhone. Source: https://help.fitbod.me/hc/en-us/articles/39224086573207-Live-Heart-Rate-Tracking

#### Garmin watch app (`garmin-watch-app`)
An app that runs on Garmin watches to log workouts.

_Result:_ SPLYT unknown · Hevy no · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **Gravl**: `129` Garmin watch app (core)
- _Decision — Hevy = no:_ Hevy's help centre says Garmin integration is not possible. Source: https://help.hevyapp.com/hc/en-us/articles/35361029194647-Hevy-and-Garmin-Integration-Update-Why-It-s-Not-Possible-Yet

#### Garmin Connect sync (`garmin-connect`)
Workouts appear in Garmin Connect.

_Result:_ SPLYT unknown · Hevy no · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **Gravl**: `130` Garmin Connect activity recording (core)
- **Fitbod**: `115` Garmin sync (core) ✗ [unsubstantiated]
- _Decision — Hevy = no:_ Hevy's help centre says Garmin integration is not possible. Source: https://help.hevyapp.com/hc/en-us/articles/35361029194647-Hevy-and-Garmin-Integration-Update-Why-It-s-Not-Possible-Yet
- _Decision — Fitbod = unknown:_ Only the website FAQ quick-stats list Garmin under 'Wearable Sync'; the help centre documents Garmin only as a Bluetooth heart-rate broadcaster on Android. Treated as unsubstantiated. Source: https://fitbod.me/faqs/

#### Wear OS app (`wear-os-app`)
An app for Wear OS watches.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **Hevy**: `199` Wear OS app (core); `200` Wear OS tile (aspect)
- **Gravl**: `131` Wear OS watch app (core); `132` Wear OS tiles (aspect)
- **Fitbod**: `126` Wear OS app (core); `127` Watch auto-advance to next exercise (aspect)

#### Fitbit integration (`fitbit`)
Workouts exchanged with Fitbit.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod partial · Motra unknown

- **Fitbod**: `114` Fitbit integration (core)
- _Decision — Fitbod = partial:_ Fitbod can still post workouts to Fitbit and import Fitbit cardio (iOS only), but Fitbit no longer auto-syncs Fitbod workouts into Fitbit activities. Source: https://help.fitbod.me/hc/en-us/articles/360026522774-Connecting-Fitbit-to-Fitbod-iOS-Only


### Social & competition

#### Friends or followers (`friends`)
Add friends or follow other users.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `184` Friends (core); `190` Contact friend finder (aspect); `191` Friends of friends (aspect); `i171` Friend requests (core); `i172` Find friends from contacts (aspect); `i173` Invite links (aspect); `i178` Friend's friends list (aspect)
- **Hevy**: `149` Follow other users (core); `151` Suggested athletes (aspect); `152` Search users (aspect); `153` Contacts friend finder (aspect); `154` Invite friends (aspect); `160` Hide suggested users (aspect); `165` Mutual followers shown (aspect)
- **Gravl**: `151` Friends (core)
- **Motra**: `140` Follow users (core); `141` User search (aspect); `142` Suggested people (aspect); `154` Remove followers (aspect)

#### Activity feed (`activity-feed`)
A feed of the workouts of people you follow or are friends with.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `185` Private friends activity feed (core); `i174` Friends activity feed (core)
- **Hevy**: `149` Follow other users (also); `149` Follow other users (also)
- **Gravl**: `152` Social activity feed (core)
- **Motra**: `139` Social activity feed (core)

#### Community or discover feed (`discover-feed`)
A feed or community space beyond your own friends.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `193` Community space (core); `194` PR spotlight (aspect); `i187` Splyt Community (core)
- **Hevy**: `150` Discover feed (core)

#### Likes and comments (`likes-comments`)
React to and comment on others' workouts.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `186` Reactions and comments (core); `i180` Comments (core); `i181` Quick replies to highlights (aspect)
- **Hevy**: `155` Likes on workouts (core); `156` Comments and replies (core); `34` Tag users in workout description (aspect); `157` Comment mentions (aspect); `158` Delete comments on own posts (aspect)
- **Gravl**: `153` Claps and comments (core)
- **Motra**: `143` Likes (core); `144` Comments and mentions (core)

#### Customisable profile (`user-profile`)
A user profile with name, photo or bio.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `237` Custom display name (core); `238` Profile avatars (aspect); `239` Profile photo from contacts or library (aspect); `i279` Edit your name (core)
- **Hevy**: `163` Public user profiles (core); `164` Profile bio and link (core); `180` Share profile (aspect)

#### Privacy controls (`privacy-controls`)
Control who can see your activity (private account, per-workout or per-item visibility, hiding from public feeds).

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `i188` Community incognito (core); `i156` Habit options (also); `i156` Habit options (also)
- **Hevy**: `159` Private profile (core); `48` Per-workout privacy (aspect); `49` Default workout visibility (aspect)
- **Motra**: `149` Private account (core); `150` Per-workout visibility (core); `151` Workout location privacy (aspect)

#### Block and report (`block-report`)
Block users and report users or content.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `198` Report and block (core); `i189` Block and report (core)
- **Hevy**: `161` Block and report users (core)
- **Motra**: `152` Block users (core); `153` Report users and workouts (core)

#### Follow a friend's workout live (`live-follow`)
See a friend's workout as it happens.

_Result:_ SPLYT partial · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `187` Follow a friend live (core) ✗ [unsubstantiated]; `210` Live training on competition map (aspect); `i175` Training-now indicator (core)
- _Decision — SPLYT = partial:_ SPLYT's feature index describes a live 'training now' dot only; the website's claim that you can watch a friend's sets land live is not in the index. Source: https://splyt.fit/features#friends

#### Browse a friend's training (`view-friend-history`)
Browse a friend's workout history or schedule.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `192` Friend history viewing (core); `93` View friend's training week (aspect); `i177` Friend workout history (core); `i134` View a friend's calendar (aspect); `i176` Friend profiles (aspect); `i225` Friends' recaps (aspect)
- **Hevy**: `163` Public user profiles (also); `163` Public user profiles (also)

#### Compare with a friend (`friend-compare`)
Compare your stats or lifts side by side with a specific friend.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `176` Compare progress with friends (core); `i179` Compare with a friend (core); `i226` You vs a friend (aspect); `i234` Compare lifts with friends (aspect)
- **Hevy**: `168` Compare stats with a user (core); `169` Exercise comparison with a user (core)
- **Gravl**: `155` Per-exercise friend comparison (core)

#### Leaderboards (`leaderboards`)
Rankings among friends or group members.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `197` Group leaderboard stats (core); `i186` Group leaderboards (core)
- **Hevy**: `170` Friends leaderboards (core)
- **Gravl**: `154` Strength score friend leaderboard (core); `156` Streak and workout leaderboards (core)
- _Decision — Fitbod = unknown:_ Fitbod 'Clubs' (gym leaderboards) is 'currently in beta at select gym locations' and was excluded at extraction.

#### Groups (`groups`)
Private groups of friends with shared activity.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `188` Groups (core); `189` Group chat (aspect); `195` Group check-in challenges (aspect); `196` Nudge friends (aspect); `i182` Groups (core); `i184` Group activity view (aspect); `i185` Group schedule (aspect)

#### Competitions and challenges (`competitions`)
Head-to-head or group competitions over a period.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `200` Friend competitions (core); `201` Twelve competition metrics (aspect); `202` Distance-based competitions (aspect); `203` 3D race visualization (aspect); `204` Custom race characters (aspect); `205` Character library (aspect); `206` Competition stakes (aspect); `207` Competition invites (aspect); `208` Competition history (aspect); `209` End-of-race awards (aspect); `i190` Create a competition (core); `i191` Competition types (aspect); `i193` Stakes (aspect); `i194` Who-owes-whom ledger (aspect); `i195` Animated race worlds (aspect); `i196` Race map strip (aspect); `i197` Standings and daily winners (aspect); `i198` Head-to-head view (aspect); `i199` Competition chat (aspect); `i200` Check-ins and nudges (aspect); `i201` Pick your racer (aspect); `i202` Create a custom character (aspect); `i203` Manage a competition (aspect); `i204` Competitions list (aspect); `i205` Results and rematch (aspect); `i206` Past group competitions (aspect); `i261` Competition alerts (aspect); `i262` Answer invites from a notification (aspect)
- **Motra**: `148` Challenges (core) ✗ [vague]
- _Decision — Motra = unknown:_ 'Challenges' appear only as a notification-settings category; no Motra source describes the feature. Source: https://help.motra.com/en/articles/14076034-managing-notifications

#### Friend activity notifications (`friend-notifications`)
Notifications when friends work out.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `143` Watch notifications (also); `i260` Friend activity alerts (core); `143` Watch notifications (also)
- **Hevy**: `162` Per-user workout notifications (core)
- **Motra**: `147` Friend activity notifications (core)

#### Tag a workout's gym or location (`gym-tagging`)
Attach the gym or location to a workout.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **Hevy**: `35` Gym tagging (core)
- **Motra**: `151` Workout location privacy (also); `151` Workout location privacy (also)

#### Connect your personal trainer (`trainer-platform`)
Link to your own personal trainer, who assigns programs and sees your data.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **Hevy**: `182` Coach connection (core); `183` Coach-assigned programs (aspect); `184` Chat with coach (aspect); `185` Auto-share data with coach (aspect); `186` Coach logs for you (aspect)


### Sharing, import/export & integrations

#### Shareable workout images (`share-cards`)
Generate shareable image cards of workouts or stats.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `211` Workout share cards (core); `213` Route share card (aspect); `216` Share day (aspect); `i146` Workout share images (core); `i227` Recap share images (aspect); `i235` Share exercise records (aspect)
- **Hevy**: `172` Social share cards (core); `174` Share exercise summary (aspect); `175` Share stats charts (aspect); `176` Share calendar (aspect)
- **Gravl**: `162` Workout share card editor (core)
- **Fitbod**: `137` Workout summary share cards (core)
- **Motra**: `145` Workout share cards (core)

#### Share to Instagram Stories (`instagram-stories`)
Post a workout card directly to Instagram Stories.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `212` Instagram Story sharing (core); `i146` Workout share images (also); `i146` Workout share images (also)
- **Hevy**: `173` Instagram story sharing (core)
- **Gravl**: `163` Instagram Story sharing (core)
- **Motra**: `146` Share to Instagram Stories (core)

#### Workout web links (`web-workout-links`)
Share a workout as a web link viewable without the app.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod yes · Motra unknown

- **SPLYT**: `214` Web workout links (core); `i147` Workout link (core); `i284` Shared workout page (aspect)
- **Hevy**: `177` Share workout link (core)
- **Fitbod**: `137` Workout summary share cards (also); `137` Workout summary share cards (also)

#### Share workouts or templates with others (`share-templates`)
Send a template, routine, split or workout to someone who can save and do it.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `215` Share templates by link (core); `77` Share template folders (aspect); `94` Share splits with friends (aspect); `217` Share workout to a friend (aspect); `i142` Template link (core); `i125` Share a split with a friend (aspect); `i140` Share a template folder (aspect); `i141` Send a template to a friend (aspect); `i143` Save a shared workout (aspect); `i144` Request a workout (aspect); `i145` Shared-with-friends history (aspect); `i285` Shared template page (aspect)
- **Hevy**: `178` Share routines (core); `166` Save others' routines (aspect); `167` Copy friends' workouts (aspect); `179` Share routine folders (aspect)
- **Strong**: `36` Share workouts and routines (core); `37` Import shared workout via link (aspect)
- **Gravl**: `161` Send workout to a friend (core)
- **Fitbod**: `136` Shareable adaptive workout links (core)
- **Motra**: `78` Public templates and sharing (core); `79` Duplicate templates (aspect)

#### Import history from another app (`import-history`)
Import your workout history from another tracker's export.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl partial · Fitbod unknown · Motra yes

- **SPLYT**: `219` Import from Strong and Hevy (core); `220` Undo an import (aspect); `i148` Import from Strong or Hevy (core); `i149` Share a file into Splyt (aspect); `i150` Undo an import (aspect)
- **Hevy**: `225` Import from Strong (core); `226` Revert data import (aspect)
- **Gravl**: `165` History import via support (core)
- **Motra**: `136` Workout history import (core)
- _Decision — Gravl = partial:_ Only by emailing Gravl support, who import it for you; there is no self-serve importer. Source: https://gravl.ai/blog/gravl-vs-fitbod

#### Import a workout from photos, files or links (`import-plan-from-media`)
Turn screenshots, documents, spreadsheets or social-video links into trackable workouts with AI.

_Result:_ SPLYT yes · Hevy unknown · Strong unknown · Gravl yes · Fitbod partial · Motra unknown

- **SPLYT**: `92` Import plan from screenshots (core); `221` Import from notes, photos, CSV, Sheets (core); `222` Import from social video links (core) ✗ [unsubstantiated]; `i151` Import workouts from notes or files (core); `i152` Import from TikTok or YouTube (core)
- **Gravl**: `17` AI import of workouts and programs (core)
- _Decision — Fitbod = partial:_ Fitbod can import a workout from a photo or screenshot on Android only; not on iPhone. Source: https://help.fitbod.me/hc/en-us/articles/38318585683991-Customizing-Today-s-Workout

#### Data export (`data-export`)
Export your workout data to a file.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `223` Data export (core); `179` Trainer report export (aspect); `i153` Export your data (core); `i228` Send recap to a trainer (aspect); `i286` Recap report page (aspect)
- **Hevy**: `227` Export workouts CSV (core); `228` Export measurements (aspect)
- **Strong**: `38` CSV data export (core); `39` Export options for timers and notes (aspect); `40` Measurements CSV export (aspect)
- **Gravl**: `164` Workout history export (core)
- **Motra**: `137` CSV data export (core); `138` Export by date range (aspect)

#### Cloud account sync (`cloud-sync`)
Data is stored in an account and synced across devices.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra unknown

- **SPLYT**: `34` Offline workout saving (also); `34` Offline workout saving (also)
- **Hevy**: `218` Cloud account sync (core)
- **Strong**: `20` Cloud sync and backup (core); `114` Cross-platform sync (iOS and Android) (aspect); `115` Manual force sync (aspect)
- **Fitbod**: `131` Cross-platform account sync (core)

#### Strava export (`strava-export`)
Push finished workouts to Strava.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `223` Strava sync (core); `224` Detailed Strava workout data (aspect)
- **Gravl**: `118` Strava export (core)
- **Fitbod**: `112` Strava workout export (core)
- **Motra**: `135` Strava sync (core)

#### Strava import (`strava-import`)
Import activities from Strava directly.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod yes · Motra unknown

- **Fitbod**: `113` Strava activity import (core)

#### Health Connect (Android) (`health-connect`)
Sync with Android Health Connect.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra unknown

- **Hevy**: `221` Health Connect sync (core)
- **Strong**: `117` Health Connect integration (Android) (core)
- **Gravl**: `117` Health Connect sync (core)
- **Fitbod**: `111` Health Connect integration (core)

#### Public developer API (`developer-api`)
A documented API for your own data.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **Gravl**: `167` Public developer API (core)


### Platforms, widgets & system

#### Android app (`android-app`)
Available on Android via Google Play.

_Result:_ SPLYT no · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra no

- **Hevy**: `216` Android app (core)
- **Strong**: `116` Android app (core)
- **Gravl**: `169` Android app (core)
- **Fitbod**: `130` Android app (core)
- _Decision — SPLYT = no:_ No Google Play listing: a Google Play search for 'splyt' and 'splyt fitness' (2026-10-09) returns no SPLYT app. Source: https://play.google.com/store/search?q=splyt&c=apps&hl=en_US&gl=US
- _Decision — Motra = no:_ No Google Play listing for Motra (motra.com). The only 'MOTRA' result (com.motra.app) is a different developer (motraapp.com). Motra's own help describes iPhone and Apple Watch only. Source: https://play.google.com/store/search?q=train%20fitness%20motra&c=apps&hl=en_US&gl=US

#### Native iPad app (`ipad-app`)
A native iPad build (universal app listed for iPad on the App Store).

_Result:_ SPLYT yes · Hevy yes · Strong no · Gravl no · Fitbod no · Motra no

- **Hevy**: `215` iPad app (core)
- _Decision — SPLYT = yes:_ App Store product page lists iPad and the store record marks the app universal (iosUniversal). Source: https://apps.apple.com/us/app/id6755893717
- _Decision — Hevy = yes:_ App Store product page lists iPad and the store record marks the app universal (iosUniversal). Source: https://apps.apple.com/us/app/id1458862350
- _Decision — Strong = no:_ App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version. Source: https://apps.apple.com/us/app/id464254577
- _Decision — Gravl = no:_ App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version. Source: https://apps.apple.com/us/app/id6450921637
- _Decision — Fitbod = no:_ App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version. Fitbod's help centre also says: 'We don't currently support iPad.' Source: https://apps.apple.com/us/app/id1041517543
- _Decision — Motra = no:_ App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version. Source: https://apps.apple.com/us/app/id1548577496

#### Web app or dashboard (`web-app`)
Use your account's training data in a web browser.

_Result:_ SPLYT unknown · Hevy yes · Strong no · Gravl yes · Fitbod partial · Motra unknown

- **Hevy**: `217` Web app (core)
- **Gravl**: `166` Web dashboard (core)
- **Fitbod**: `133` Web workout generator (core)
- _Decision — Strong = no:_ Strong's help lists a web app as in development. Source: https://help.strongapp.io/article/242-future-features
- _Decision — Fitbod = partial:_ Fitbod's website offers a public workout generator, but its own FAQ says the web platform is for onboarding only; you cannot use your training data there. Source: https://fitbod.me/faqs/

#### Apple Vision Pro compatibility (`vision-pro`)
Listed as compatible with Apple Vision on the App Store.

_Result:_ SPLYT yes · Hevy yes · Strong no · Gravl yes · Fitbod yes · Motra yes

- **Gravl**: `170` Apple Vision Pro support (core)
- **Fitbod**: `132` Mac and Vision Pro compatibility (core)
- **Motra**: `158` Apple Vision Pro compatibility (core)
- _Decision — SPLYT = yes:_ App Store compatibility lists Apple Vision. Source: https://apps.apple.com/us/app/id6755893717
- _Decision — Hevy = yes:_ App Store compatibility lists Apple Vision. Source: https://apps.apple.com/us/app/id1458862350
- _Decision — Strong = no:_ App Store compatibility does not list Apple Vision. Source: https://apps.apple.com/us/app/id464254577
- _Decision — Gravl = yes:_ App Store compatibility lists Apple Vision. Source: https://apps.apple.com/us/app/id6450921637
- _Decision — Fitbod = yes:_ App Store compatibility lists Apple Vision. Source: https://apps.apple.com/us/app/id1041517543
- _Decision — Motra = yes:_ App Store compatibility lists Apple Vision. Source: https://apps.apple.com/us/app/id1548577496

#### Mac (Apple silicon) availability (`mac`)
Listed as available on Mac on the App Store.

_Result:_ SPLYT no · Hevy no · Strong no · Gravl no · Fitbod yes · Motra no

- **Fitbod**: `132` Mac and Vision Pro compatibility (also); `132` Mac and Vision Pro compatibility (also)
- _Decision — SPLYT = no:_ App Store compatibility does not list Mac. Source: https://apps.apple.com/us/app/id6755893717
- _Decision — Hevy = no:_ App Store compatibility does not list Mac. Source: https://apps.apple.com/us/app/id1458862350
- _Decision — Strong = no:_ App Store compatibility does not list Mac. Source: https://apps.apple.com/us/app/id464254577
- _Decision — Gravl = no:_ App Store compatibility does not list Mac. Source: https://apps.apple.com/us/app/id6450921637
- _Decision — Fitbod = yes:_ App Store compatibility lists Mac (Apple silicon). Source: https://apps.apple.com/us/app/id1041517543
- _Decision — Motra = no:_ App Store compatibility does not list Mac. Source: https://apps.apple.com/us/app/id1548577496

#### Languages other than English (`languages`)
The app is localised into languages other than English.

_Result:_ SPLYT no · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **Hevy**: `72` Multiple languages (core)
- **Strong**: `119` Multiple languages (core)
- **Gravl**: `171` Eight languages (core)
- **Fitbod**: `134` Multiple languages (core)
- **Motra**: `157` Localized in 18 languages (core)
- _Decision — SPLYT = no:_ App Store lists English as the only language. Source: https://apps.apple.com/us/app/id6755893717

#### Home and Lock Screen widgets (`home-widgets`)
iPhone Home Screen or Lock Screen widgets.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `224` Home and lock screen widgets (core); `225` Training calendar widget (aspect); `226` Interactive habit widget (aspect); `227` Competition widget (aspect); `228` Start workout lock screen widget (aspect) ✗ [unsubstantiated]; `229` Widget color tint (aspect); `i247` Workout widget (core); `i246` Training calendar widget (aspect); `i248` Single habit widget (aspect); `i249` Habits widget (aspect); `i250` Competition widget (aspect); `i251` Splyt ring Lock Screen widget (aspect); `i252` Activity rings Lock Screen widget (aspect)
- **Hevy**: `205` Home screen widgets (core); `206` Stats widget (aspect); `207` Calendar widget (aspect); `208` Weekly comparison widget (aspect); `209` Routine of the day widget (aspect); `210` Quick access widget (aspect); `211` Routines widget (aspect); `212` Streak widget (aspect); `213` Rest days widget (aspect); `214` Last week workouts widget (aspect)
- **Strong**: `43` Workouts-per-week home screen widget (core); `44` Calendar home screen widget (core); `46` Activity home screen widget (core); `51` Quick-add measurement from widgets (aspect)
- **Gravl**: `133` Home Screen activity widget (core)
- **Fitbod**: `128` Home screen widget (core)
- **Motra**: `125` Home Screen widgets (core); `126` Muscle set-distribution widget (aspect); `127` Lock Screen widgets (aspect)

#### Live Activity and Dynamic Island (`live-activity`)
The live workout appears on the Lock Screen and in the Dynamic Island.

_Result:_ SPLYT yes · Hevy yes · Strong partial · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `230` Live Activity and Dynamic Island (core); `i244` Workout Live Activity (core)
- **Hevy**: `201` Live Activity (core); `202` Dynamic Island (core)
- **Strong**: `41` Rest timer Live Activity (core); `42` Rest timer in Dynamic Island (core)
- **Gravl**: `134` Live Activity during workouts (core); `135` Android ongoing workout notification (aspect)
- **Fitbod**: `129` Live Activities and Dynamic Island (core)
- **Motra**: `129` Live Activity and Dynamic Island (core)
- _Decision — Strong = partial:_ Strong's Live Activity and Dynamic Island show the rest timer only, not the live workout. Source: https://apps.apple.com/us/app/id464254577

#### Log sets from the Lock Screen (`lock-screen-logging`)
Complete sets from the Live Activity without unlocking.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra yes

- **SPLYT**: `231` Log sets from lock screen (core); `i245` Live Activity buttons (core)
- **Hevy**: `203` Complete sets from lock screen (core); `204` Rest timer controls on lock screen (aspect)
- **Gravl**: `134` Live Activity during workouts (also); `134` Live Activity during workouts (also)
- **Motra**: `130` Log sets from Live Activity (core)

#### Siri and Shortcuts (`siri`)
Control the app with Siri or the Shortcuts app.

_Result:_ SPLYT yes · Hevy unknown · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **SPLYT**: `124` Siri workout control (core); `125` Siri on locked phone (aspect); `i253` Start a workout with Siri (core); `i254` End, pause or resume with Siri (core); `i255` Add an activity with Siri (aspect)
- **Strong**: `55` Siri Shortcuts (core)

#### Control Center control (`control-center`)
A Control Center button for the app.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **Motra**: `128` Control Center control (core)

#### iMessage stickers (`imessage-stickers`)
A sticker pack for Messages.

_Result:_ SPLYT unknown · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra unknown

- **Hevy**: `181` iMessage stickers (core)

#### Distraction blocking during workouts (`app-blocking`)
Block chosen apps while a workout runs.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **Gravl**: `86` Workout Focus app blocking (core); `87` App unblock during rest (aspect)

#### No advertising (`no-ads`)
The app shows no ads.

_Result:_ SPLYT unknown · Hevy yes · Strong yes · Gravl unknown · Fitbod unknown · Motra unknown

- **Hevy**: `73` No ads (core)
- **Strong**: `118` Ad-free (core)


### Personalisation, account & support

#### Dark mode (`dark-mode`)
A dark appearance.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `232` Dark and light mode (core); `i281` Colour themes and dark mode (core)
- **Hevy**: `69` Dark mode (core); `70` Haptic feedback (also) ✗ [ui_tweak]; `70` Haptic feedback (also) ✗ [ui_tweak]
- **Strong**: `54` Dark mode (core)
- **Gravl**: `105` Dark mode (core)

#### Colour themes and accent colours (`themes`)
Choose colour themes or an accent colour.

_Result:_ SPLYT yes · Hevy unknown · Strong yes · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `233` Custom accent color (core); `i281` Colour themes and dark mode (also); `i282` Apple Fitness look (aspect); `i281` Colour themes and dark mode (also)
- **Strong**: `52` Color themes (core)
- **Gravl**: `106` Color themes (core); `107` Accent color choice (core)

#### Alternate app icons (`app-icons`)
Choose an alternate app icon.

_Result:_ SPLYT unknown · Hevy unknown · Strong yes · Gravl yes · Fitbod unknown · Motra unknown

- **Strong**: `53` Custom app icons (core)
- **Gravl**: `108` Alternate app icons (core)

#### First day of week setting (`week-start`)
Choose the day the week starts.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `240` Week start day setting (core); `i283` Start of week (core)
- **Hevy**: `68` First day of week setting (core)
- **Gravl**: `104` Configurable first day of week (core)
- **Fitbod**: `50` Start-of-week day setting (core)
- **Motra**: `121` Configurable week start day (core)

#### Notification controls and inbox (`notification-settings`)
Per-type notification toggles, or an in-app notification inbox.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl unknown · Fitbod unknown · Motra yes

- **SPLYT**: `241` Notification history (core); `i257` Notification inbox (core); `i258` Per-type notification switches (core); `i259` Watch or phone delivery (aspect); `i263` Mute from a notification (aspect); `i264` Record and streak alerts (aspect)
- **Hevy**: `231` Granular notification settings (core)
- **Motra**: `124` Granular notification controls (core)

#### Sign in with Apple or Google (`sign-in-options`)
Sign in with Apple or Google accounts.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl yes · Fitbod yes · Motra yes

- **SPLYT**: `243` Apple and Google sign-in (core); `i275` Sign in options (core)
- **Hevy**: `229` Sign in with Apple or Google (core)
- **Strong**: `111` Sign in with Apple (core); `112` Facebook login (aspect)
- **Gravl**: `173` Apple and Google sign-in (core)
- **Fitbod**: `135` Social sign-in options (core)
- **Motra**: `155` Apple, Google or email sign-in (core)

#### In-app account deletion (`account-deletion`)
Delete your account and data from inside the app.

_Result:_ SPLYT yes · Hevy yes · Strong yes · Gravl unknown · Fitbod yes · Motra yes

- **SPLYT**: `244` In-app account deletion (core); `i280` Delete account (core)
- **Hevy**: `230` In-app account deletion (core)
- **Strong**: `113` In-app account deletion (core)
- **Fitbod**: `140` In-app account deletion (core)
- **Motra**: `156` Delete your data (core)

#### In-app support and feedback (`in-app-support`)
Contact the team, report bugs or request features from inside the app.

_Result:_ SPLYT yes · Hevy yes · Strong unknown · Gravl yes · Fitbod unknown · Motra unknown

- **SPLYT**: `115` AI support chat (core); `199` Founders direct chat (aspect); `245` Feedback with screenshots (aspect); `i273` Talk to the team (core); `i274` Send feedback (core)
- **Hevy**: `232` In-app feature requests (core)
- **Gravl**: `172` In-app feature request board (core); `57` In-app AI support assistant (also); `57` In-app AI support assistant (also)

#### AI support assistant (`ai-support-assistant`)
An AI assistant answers support questions.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **Gravl**: `57` In-app AI support assistant (core)
- **Fitbod**: `139` AI support assistant (core)

#### Advice from human coaches (`trainer-advice`)
Ask certified trainers or coaches employed by the app for workout advice.

_Result:_ SPLYT unknown · Hevy unknown · Strong unknown · Gravl yes · Fitbod yes · Motra unknown

- **Gravl**: `56` Human coach chat (core)
- **Fitbod**: `138` Email a certified trainer (core)


## Claims we didn't count

Every claim was classified (full list in `data/vetting.json`). Only `capability` and `aspect` claims can make a cell 'yes'. `not_shipped` can make it 'partial'. `unsubstantiated` never scores above 'unknown' unless other evidence exists, and `fix`, `ui_tweak`, `vague` and `out_of_scope` (pricing/tier limits) never count.

### SPLYT
535 claims; kept 504; not counted 31 — unsubstantiated: 9, ui_tweak: 16, out_of_scope: 6

- `0` Strength set logging — **unsubstantiated**: App Store line still advertises food logging, which SPLYT's own What's New (build 374) and feature index say was removed; set logging is evidenced by other claims instead.
- `1` Large-number set entry — **ui_tweak**: Describes the size of the numbers on screen, not a capability.
- `3` One movement open at a time — **ui_tweak**: Layout behaviour (one card expanded at a time).
- `25` Collapsible exercise cards — **ui_tweak**: Collapsing a card is a layout control.
- `41` Live workout resume banner — **ui_tweak**: A banner to return to an open workout is navigation.
- `42` Get-ready countdown — **ui_tweak**: A 3-2-1 start animation.
- `49` Rest shown between sets — **ui_tweak**: Draws rest as a line between rows: display option.
- `128` On-device offline rep counting — **unsubstantiated**: On-device/offline rep counting is stated on the website only; the 2026-10-09 feature index does not describe it. Kept as an aspect note only.
- `147` Watch accent color sync — **ui_tweak**: Watch accent colour following the phone.
- `148` Watch centisecond clock — **ui_tweak**: Clock shows centiseconds.
- `149` Watch-only gym use — **unsubstantiated**: Website says no phone is needed on the gym floor; SPLYT's own detailed feature index only says the watch starts recording 'without touching your phone', which is not the same as working without it nearby.
- `154` Body weight and measurements — **unsubstantiated**: Website says 'body weight and measurements'; SPLYT's feature index describes only a body weight log (and weight/steps/sleep trends), no circumference or body-fat logging.
- `170` Daily strain score — **unsubstantiated**: The 0-21 daily strain score appears on the website only; the feature index lists every Stats view in detail and none is a strain score.
- `182` Interactive charts — **ui_tweak**: Press-and-hold on charts is an interaction refinement.
- `187` Follow a friend live — **unsubstantiated**: Website says you can watch a friend's sets land live; the feature index describes only a 'training now' live dot. Scored partial on the index.
- `222` Import from social video links — **unsubstantiated**: Release note includes Instagram links; the feature index lists TikTok and YouTube only (Instagram links are rejected). The capability is still evidenced by the index for TikTok/YouTube.
- `228` Start workout lock screen widget — **unsubstantiated**: Release note describes a lock-screen widget that starts a workout; the feature index's lock-screen widgets only show rings and open the app.
- `234` Ring color themes — **unsubstantiated**: App Store mention of 'dozens of ring colorways' is not described in the feature index; kept as an aspect only.
- `236` Tab bar glass intensity — **ui_tweak**: Tab bar frosting level.
- `i41` One movement at a time — **ui_tweak**: One-movement-at-a-time is layout.
- `i48` Minimise the workout — **ui_tweak**: Minimising the workout to a mini bar is navigation.
- `i137` Unlimited templates — **out_of_scope**: Pro tier limit (pricing), excluded by the brief.
- `i158` Unlimited habits — **out_of_scope**: Pro tier limit (pricing), excluded by the brief.
- `i168` Ring fill on finish — **ui_tweak**: Ring fill animation.
- `i183` Bigger and more groups — **out_of_scope**: Free vs Pro group limits (pricing).
- `i192` Join competitions free — **out_of_scope**: Free participation in competitions is a pricing statement.
- `i209` Roast me mode — **ui_tweak**: Alternative copy ('roast me') with no new capability.
- `i256` Links open in the app — **ui_tweak**: Universal links opening the app is plumbing, not a user capability.
- `i277` Manage subscription — **out_of_scope**: Subscription management (pricing).
- `i278` Pro plans with free trial — **out_of_scope**: Pro plans and trial (pricing).
- `i287` Invite pages — **ui_tweak**: Invite landing pages are plumbing for friend invites.

### Hevy
233 claims; kept 231; not counted 2 — ui_tweak: 2

- `29` RPE colour scale — **ui_tweak**: 'Redesigned the Set Row UI ... an RPE color scale' is a redesign.
- `70` Haptic feedback — **ui_tweak**: 'more haptic feedback, a smoother dark mode experience' is polish.

### Strong
120 claims; kept 115; not counted 5 — unsubstantiated: 2, fix: 3

- `50` Show Borders accessibility support — **fix**: 'Improved support for the Show Borders accessibility feature' is an improvement to an OS setting.
- `56` Muscle heat map — **unsubstantiated**: 'Muscle Heat Map' appears as a bare name in one of two variants of the homepage feature strip; no help article or release note describes it.
- `57` Workout scheduling — **unsubstantiated**: Homepage strip lists 'Workout Scheduling', but Strong's help article 'On Future Features' says scheduling is still being worked on.
- `64` Import workouts from Apple Health — **fix**: 'Faster Apple Health workout imports' is a performance fix; no Strong source describes the import itself.
- `92` Rest timer notifications — **fix**: 'Fix: Timer notifications may not include next set details' is a fix.

### Gravl
174 claims; kept 170; not counted 4 — unsubstantiated: 1, fix: 3

- `4` Standalone Apple Watch app — **unsubstantiated**: App Store calls the watch app standalone; Gravl's help article says 'Keep the iPhone within reach: the app on the phone is still what owns and saves the session.'
- `61` Rest timer sound — **fix**: 'Fixed Apple Music pausing on rest timer sound' is a fix.
- `116` Bodyweight sync from Apple Health — **fix**: 'Improvements on bodyweight sync from Apple Health' is an improvement; no Gravl source describes the sync itself.
- `127` Simplified watch logging view — **fix**: 'Rebuilt Apple Watch experience: better synchronization... more reliable rest timers' is a rebuild/fix.

### Fitbod
141 claims; kept 138; not counted 3 — unsubstantiated: 1, not_shipped: 2

- `97` Exercise percentile ranking — **not_shipped**: Help says percentile ranking is rolling out gradually; kept as an aspect.
- `115` Garmin sync — **unsubstantiated**: Website FAQ 'Wearable Sync: ... Garmin' only; the help centre documents Garmin only as a Bluetooth heart-rate broadcaster on Android.
- `116` Live heart rate during workouts — **not_shipped**: 'Now gradually rolling out on Android and iOS.'

### Motra
159 claims; kept 149; not counted 10 — unsubstantiated: 1, not_shipped: 1, fix: 2, ui_tweak: 3, vague: 3

- `16` Detection remembers corrections — **fix**: 'Improvements to auto-detection memory' is an improvement.
- `17` Form feedback — **unsubstantiated**: 'provide form-feedback' appears once on a marketing page; no help article describes any form feedback.
- `25` Collapse exercises on watch — **ui_tweak**: Expand/collapse exercises on the watch is layout.
- `33` Phone-only workout logging — **fix**: 'we've made some improvements to the phone-only workout' is an improvement note.
- `50` Non-weighted exercise logging — **ui_tweak**: Hiding weight fields for non-weighted exercises is a display change.
- `85` Guided template mode — **vague**: 'Guide Mode assists with the next set' does not say what it does.
- `104` AI coach chat — **not_shipped**: Release 6.3.0 announced the AI Coach as a staged rollout; no help article documents it.
- `115` Advanced metrics history — **vague**: 'Track your progress in detail, compare performance over time' describes no specific capability.
- `134` Health sync status banner — **ui_tweak**: A banner showing Health sync status.
- `148` Challenges — **vague**: 'Challenges' appear only as a notification category; no Motra source describes the feature.


## Where vetting changed a value compared with a naive mapping

A naive mapping marks an app 'yes' whenever any claim of its maps to the feature. These cells differ:

- Planning calendar — Hevy: naive unknown → **no**. Hevy's calendar shows past workouts only.
- Planning calendar — Strong: naive yes → **no**. The homepage strip lists 'Workout Scheduling', but Strong's help says it is still being built.
- AI coach chat — Motra: naive yes → **partial**. Announced in release 6.3.0 (2026-05-22) as a staged rollout 'in the coming week'; no help article documents it, so availability to all users is unconfirmed.
- Voice logging — Gravl: naive unknown → **partial**. Gravl's help says workouts can be described out loud, but the feature is labelled Beta (publicly offered in the app). Not in the extracted claims because the brief excluded beta items; added here as partial.
- Offline exercise videos — Fitbod: naive unknown → **no**. Fitbod's help says offline video is unavailable.
- Muscle heatmap — Strong: naive yes → **unknown**. Named only in one variant of the homepage feature strip; not described anywhere else.
- Import workouts from Apple Health — Strong: naive yes → **unknown**. Only claim was rejected as fix: 'Faster Apple Health workout imports' is a performance fix; no Strong source describes the import itself.
- Body data synced with Apple Health — Gravl: naive yes → **unknown**. Only claim was rejected as fix: 'Improvements on bodyweight sync from Apple Health' is an improvement; no Gravl source describes the sync itself.
- Body measurements (circumferences, body fat) — SPLYT: naive yes → **unknown**. Website says 'body weight and measurements', but the feature index describes a body weight log only.
- Calorie and macro logging — SPLYT: naive unknown → **no**. Removed in build 374.
- Watch logging without the phone — SPLYT: naive yes → **unknown**. The website says no phone is needed; SPLYT's detailed feature index says only that the watch starts recording 'without touching your phone'. Not enough to confirm logging with the phone away.
- Watch logging without the phone — Gravl: naive yes → **no**. App Store copy calls the watch app standalone, but Gravl's help says the phone must be within reach.
- Watch logging without the phone — Fitbod: naive unknown → **no**. Fitbod's help says the watch app is a companion.
- Start templates or plans on the watch — Fitbod: naive unknown → **no**. Workouts must be started on the iPhone.
- Edit workout structure on the watch — Fitbod: naive yes → **partial**. Sets can be added or removed on the watch, but swapping or adding exercises requires the iPhone.
- Heart rate from AirPods — Fitbod: naive yes → **partial**. Live heart rate (including AirPods Pro 3) is 'gradually rolling out' per Fitbod's own help article.
- Bluetooth heart-rate monitors — Fitbod: naive yes → **partial**. Android only, and part of live heart rate, which is still 'gradually rolling out'. Not available on iPhone.
- Garmin watch app — Hevy: naive unknown → **no**. Hevy's help centre says Garmin integration is not possible.
- Garmin Connect sync — Hevy: naive unknown → **no**. Hevy's help centre says Garmin integration is not possible.
- Garmin Connect sync — Fitbod: naive yes → **unknown**. Only the website FAQ quick-stats list Garmin under 'Wearable Sync'; the help centre documents Garmin only as a Bluetooth heart-rate broadcaster on Android. Treated as unsubstantiated.
- Fitbit integration — Fitbod: naive yes → **partial**. Fitbod can still post workouts to Fitbit and import Fitbit cardio (iOS only), but Fitbit no longer auto-syncs Fitbod workouts into Fitbit activities.
- Follow a friend's workout live — SPLYT: naive yes → **partial**. SPLYT's feature index describes a live 'training now' dot only; the website's claim that you can watch a friend's sets land live is not in the index.
- Competitions and challenges — Motra: naive yes → **unknown**. 'Challenges' appear only as a notification-settings category; no Motra source describes the feature.
- Import history from another app — Gravl: naive yes → **partial**. Only by emailing Gravl support, who import it for you; there is no self-serve importer.
- Import a workout from photos, files or links — Fitbod: naive unknown → **partial**. Fitbod can import a workout from a photo or screenshot on Android only; not on iPhone.
- Android app — SPLYT: naive unknown → **no**. No Google Play listing: a Google Play search for 'splyt' and 'splyt fitness' (2026-10-09) returns no SPLYT app.
- Android app — Motra: naive unknown → **no**. No Google Play listing for Motra (motra.com). The only 'MOTRA' result (com.motra.app) is a different developer (motraapp.com). Motra's own help describes iPhone and Apple Watch only.
- Native iPad app — SPLYT: naive unknown → **yes**. App Store product page lists iPad and the store record marks the app universal (iosUniversal).
- Native iPad app — Strong: naive unknown → **no**. App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version.
- Native iPad app — Gravl: naive unknown → **no**. App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version.
- Native iPad app — Fitbod: naive unknown → **no**. App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version. Fitbod's help centre also says: 'We don't currently support iPad.'
- Native iPad app — Motra: naive unknown → **no**. App Store product page lists iPad nowhere and the store record is not universal: there is no native iPad version.
- Web app or dashboard — Strong: naive unknown → **no**. Strong's help lists a web app as in development.
- Web app or dashboard — Fitbod: naive yes → **partial**. Fitbod's website offers a public workout generator, but its own FAQ says the web platform is for onboarding only; you cannot use your training data there.
- Apple Vision Pro compatibility — SPLYT: naive unknown → **yes**. App Store compatibility lists Apple Vision.
- Apple Vision Pro compatibility — Hevy: naive unknown → **yes**. App Store compatibility lists Apple Vision.
- Apple Vision Pro compatibility — Strong: naive unknown → **no**. App Store compatibility does not list Apple Vision.
- Mac (Apple silicon) availability — SPLYT: naive unknown → **no**. App Store compatibility does not list Mac.
- Mac (Apple silicon) availability — Hevy: naive unknown → **no**. App Store compatibility does not list Mac.
- Mac (Apple silicon) availability — Strong: naive unknown → **no**. App Store compatibility does not list Mac.
- Mac (Apple silicon) availability — Gravl: naive unknown → **no**. App Store compatibility does not list Mac.
- Mac (Apple silicon) availability — Motra: naive unknown → **no**. App Store compatibility does not list Mac.
- Languages other than English — SPLYT: naive unknown → **no**. App Store lists English as the only language.
- Live Activity and Dynamic Island — Strong: naive yes → **partial**. Strong's Live Activity and Dynamic Island show the rest timer only, not the live workout.

## Removed features

- **SPLYT** — Food and calorie logging (meal logging, quick meal log, barcode scanner, calories/macros cards): "Food and calorie logging has been removed. Splyt is focused on training, sleep and recovery." (https://splyt.fit (in-app What’s New, build 374), 2026-08-15)
- **SPLYT** — Bluetooth gym-machine pairing (FTMS treadmills, bikes, rowers, ellipticals, stair climbers): "Removed the confusing “connect machine / searching” spinner on the watch during indoor cardio — Splyt tracks straight from the watch." (https://splyt.fit (in-app What’s New, build 342), 2026-07-18)
- **SPLYT** — AI voice 'vibes' / persona lineup (Calm … Drill Sergeant, Noir Detective) and coach styles: "Voice mode is simpler and smoother: a focused set of four natural-sounding voices, and more lifelike, less robotic delivery." (https://splyt.fit (in-app What’s New, build 342), 2026-07-18)
- **SPLYT** — Hands-free AI voice chat (talking orb): "Talk to your coach
Ask SPLYT anything out loud, mid-set, and hear the answer back." (https://splyt.fit/roadmap)
- **SPLYT** — Demo mode (try the app with sample data before sign-up): "Try Splyt before you sign up — tap “Demo mode” on the welcome screen to explore the whole app with sample data" (https://splyt.fit (in-app What’s New, build 347), 2026-07-22)
- **SPLYT** — Apple Watch first-run tutorial / Replay Watch Tutorial: "The Apple Watch app opens straight to your workouts — the first-run tutorial has been removed." (https://splyt.fit (in-app What’s New, build 235), 2026-05-21)
- **Hevy** — Custom GPT chat (HevyGPT): "this also means we're sunsetting the old HevyGPT now that the new Hevy app for ChatGPT is available." (https://help.hevyapp.com/hc/en-us/articles/43652076665239-What-is-the-Hevy-App-on-ChatGPT)
- **Hevy** — Facebook sign-in: "we no longer support Facebook Sign-In" (https://help.hevyapp.com/hc/en-us/articles/34895051242903-Forgot-my-password-How-to-recover-or-change-a-password)
- **Hevy** — Direct Google Fit connection: "We previously connected directly to Google Fit, but Google has removed this option." (https://help.hevyapp.com/hc/en-us/articles/34204824335255-How-to-Connect-Hevy-to-Google-Fit-Using-Health-Connect)
- **Strong** — Direct MyFitnessPal integration: "Strong is no longer supporting direct MyFitnessPal integration. Please use our Apple Health for iPhone integration instead" (https://help.strongapp.io/article/146-myfitnesspal)
- **Strong** — Google Fit integration (Android): "As a result of Google's deprecation of the Google Fit API, Strong 2.X is no longer able to support Google Fit Integration." (https://help.strongapp.io/article/254-google-fit-health-connect-integration)
- **Gravl** — Reset all recommended weights: "Reset all recommended weights has been removed; percentage adjustments and individual exercise one-rep-max edits remain available." (https://gravl.ai/developers/release-notes/1.53.3)
- **Gravl** — Free-form colour picker: "Theme presets replace the free-form colour picker." (https://gravl.ai/developers/release-notes/1.53.3)
- **Fitbod** — Animated GIF exercise demos: "GIFs were removed in a recent update, and offline video support is currently unavailable." (https://help.fitbod.me/hc/en-us/articles/30721437384215-How-to-Navigate-the-Exercise-Details-Screen)
- **Fitbod** — Per-session fitness goal / difficulty / variability override: "Settings like Fitness Goal and Variability are now part of My Plan so they stay consistent across workouts instead of unintentionally resetting each day." (https://help.fitbod.me/hc/en-us/articles/38318585683991-Customizing-Today-s-Workout)
- **Fitbod** — Automatic posting of workouts into Fitbit activities: "Fitbit no longer auto-syncs Fitbod workouts to Fitbit activities. You will need to manually add your Fitbod activities to Fitbit." (https://help.fitbod.me/hc/en-us/articles/360026522774-Connecting-Fitbit-to-Fitbod-iOS-Only)

How they were used: SPLYT food logging → `nutrition-logging` = no. Fitbod offline video → `offline-videos` = no (GIF removal does not affect `exercise-demos`, which Fitbod still has as video). Fitbod Fitbit auto-posting → `fitbit` = partial. Removals of things no app still claims (SPLYT Bluetooth machine pairing, voice personas, hands-free voice chat, demo mode, watch tutorial; Hevy HevyGPT, Facebook sign-in, direct Google Fit; Strong direct MyFitnessPal, Google Fit; Gravl reset-all-weights, free colour picker; Fitbod per-session goal override) did not create features, because a feature only exists in this list if some app currently claims it.

