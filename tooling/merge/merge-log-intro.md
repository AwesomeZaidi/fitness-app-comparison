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
