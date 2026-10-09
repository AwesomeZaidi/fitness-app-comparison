# Methodology

These are the rules behind every value in `data/`. Where a rule can be checked by a script, `scripts/validate.mjs` checks it.

**Conflict of interest:** SPLYT wrote these rules, collected the data, made the grouping and vetting judgements, and makes one of the six apps. The rules are designed so that someone outside SPLYT can check every value, SPLYT's included, and every judgement. The limits that follow from this are listed at the end.

The detailed working record — every feature, every claim merged into it, every rejected claim, every override and the hardest judgement calls — is **[MERGE-LOG.md](MERGE-LOG.md)**. This page states the rules.

## 1. What is compared

- **Apps.** SPLYT, Hevy, Strong, Gravl, Fitbod and Motra, identified by their US App Store ids in [`data/apps.json`](data/apps.json).
  - Motra is App Store id **1548577496** (Train Fitness Inc.). It is *not* "MOTRA" (id 6756487760), an unrelated app from a different company. The validator rejects that id.
  - The comparison is limited to these six apps for now.
- **Features.** The 188 features in [`data/features.json`](data/features.json), in 14 categories derived from the data. They were not chosen in advance: the list is built bottom-up from the claims each app makes about itself (section 2). Each feature has a one-line definition, and the cell is judged against that definition, not against the shorter name.

## 2. The feature list and the matrix

### 2.1 Collecting claims

For each app, a separate extraction pass read only that app's own public material and recorded every user-facing capability the app says it has today. The brief was identical for all six apps and is published as [`tooling/EXTRACTION-BRIEF.md`](tooling/EXTRACTION-BRIEF.md). No pass saw another app.

- **Allowed sources:** the app's App Store listing and release notes, its official website and blog, its help centre or documentation, and Google Play (for Android availability only). Each app's official domains are in `data/apps.json`.
- **Not allowed:** reviews, Reddit, YouTube, third-party blogs, comparison sites, our own testing, and our own knowledge.
- **Not extracted:** pricing, trials and plan limits; bug fixes and speed or reliability items; roadmap, "coming soon" and beta items; adjectives with no capability. Features an app's own later sources say were removed are recorded separately (`removed`).
- **Each claim** has a short neutral name, a one-line description, a verbatim quote (≤ 240 characters), the exact URL, a source type (`app_store`, `release_notes`, `website`, `help_centre`, `google_play`) and the source's date where it has one.

Extraction is an **AI-assisted step**: an AI model followed the brief for each app, and the maintainer reviewed the result. Everything after it is either a human judgement recorded as data or a deterministic script (section 2.6).

| App | Claims | Help centre | Release notes | Website | App Store | Google Play |
|---|---:|---:|---:|---:|---:|---:|
| SPLYT | 535 | 288 ¹ | 168 ² | 73 | 6 | 0 |
| Hevy | 233 | 128 | 20 | 55 | 29 | 1 |
| Gravl | 174 | 113 | 29 | 22 | 9 | 1 |
| Motra | 159 | 115 | 33 | 4 | 7 | 0 |
| Fitbod | 141 | 118 | 0 | 9 | 13 | 1 |
| Strong | 120 | 70 | 16 | 5 | 29 | 0 |

¹ SPLYT's feature index, published 2026-10-09 (see below). ² Mostly SPLYT's in-app What's New, plus its App Store release notes. Strong's website features page is password-protected, so its website claims come from the homepage only.

Raw claims are in [`data/claims/<app>.json`](data/claims/).

**SPLYT's feature index.** SPLYT has no help centre. On **2026-10-09, the same day as this comparison**, it published a feature index at [splyt.fit/features](https://splyt.fit/features) (288 entries, `data/claims/splyt-index.json`, numbered `i0`–`i287`). It was treated as a help centre and vetted with the same classes as every other app's. It cuts both ways:
- **For SPLYT:** 8 SPLYT "yes" cells rest on it alone. Without it, SPLYT has 125 "yes" (66%) instead of 133 (70.7%), and is still first.
- **Against SPLYT:** SPLYT describes the index as complete, so where SPLYT's marketing copy claims something the index does not describe, that claim was marked `unsubstantiated` and not counted (a 0–21 daily strain score, using the watch without the phone, body circumference measurements, watching a friend's sets live). Where older SPLYT claims and the index disagree, the index wins. No other app's help centre claims to be complete, so no other app could be held to that test.

### 2.2 Vetting every claim

Before scoring, every claim was put in exactly one class ([`data/vetting.json`](data/vetting.json)), with a reason for every claim that is not counted. The classes are the same for every app:

| Class | Counts? | Meaning |
|---|---|---|
| `capability` | yes | A concrete capability, described by its quote. |
| `aspect` | under its parent only | A setting or variant of a parent feature. |
| `unsubstantiated` | no — never above unknown on its own | Marketing-only, and contradicted by, or absent from, the app's more detailed own sources. |
| `not_shipped` | partial at most | Rolling out to some users, or a public beta. |
| `fix` | no | A bug fix or speed/reliability improvement. |
| `ui_tweak` | no | Layout, redesign or copy change. |
| `vague` | no | A name with no description of what it does. |
| `out_of_scope` | no | Pricing or plan limits (excluded by the brief). |

Per-app counts:

| App | Claims | Kept | unsubstantiated | not_shipped | fix | ui_tweak | vague | out_of_scope | Not counted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SPLYT | 535 | 504 | 9 | 0 | 0 | 16 | 0 | 6 | **31** |
| Hevy | 233 | 231 | 0 | 0 | 0 | 2 | 0 | 0 | 2 |
| Strong | 120 | 115 | 2 | 0 | 3 | 0 | 0 | 0 | 5 |
| Gravl | 174 | 170 | 1 | 0 | 3 | 0 | 0 | 0 | 4 |
| Fitbod | 141 | 138 | 1 | 2 | 0 | 0 | 0 | 0 | 3 |
| Motra | 159 | 149 | 1 | 1 | 2 | 3 | 3 | 0 | 10 |

SPLYT had the most claims rejected. Interpretations applied to every app:
- A bare name in a marketing list counts only when the name itself fully states the capability ("Dark Mode", "Siri Shortcuts").
- A store claim contradicted by the app's own help centre loses (for example Gravl's "standalone" watch app; Strong's "Workout Scheduling").
- A fix-only release note does not prove the underlying feature.

### 2.3 Canonicalisation: from claims to features

- A **feature** is something a typical lifter would recognise as a distinct thing to look for in an app.
- Settings and small variants of one capability are merged into it as **aspects**. Aspects are listed under the feature but not scored on their own (for example rest-timer sounds are an aspect of "Rest timer").
- **The same granularity for every app.** When one app lists many small items and another lists one sentence, both map to the same parent. SPLYT's 13 separate voice claims became one feature, "Voice logging"; its competition and split-builder details are aspects; so are Hevy's widget list and Fitbod's and Gravl's programming settings.
- **Related but different capabilities stay separate**: auto rep counting ≠ auto exercise detection; Garmin ≠ Wear OS; Garmin watch app ≠ Garmin Connect sync; AI coach chat ≠ generated program; Apple Health export ≠ import; body weight log ≠ body measurements.
- **Features are defined by what the user gets**, not the app's wording: an algorithmic program generator and an "AI" one are the same feature.
- **When in doubt, the grouping fairest to the other apps wins.** Three features only SPLYT had were folded into broader parents for this reason.
- **A feature exists only if some app documents it with a counted claim.** Removed features no app still offers do not create rows; a row whose only claim was rejected (SPLYT's daily strain score) was dropped.
- One claim maps to one feature. A claim whose quote also proves a second feature can be cited as evidence for it (`alsoEvidencedBy`); it is not counted twice for the same feature.

Every grouping is data in [`tooling/merge/mapping.py`](tooling/merge/mapping.py) and is listed, feature by feature, in MERGE-LOG.md.

### 2.4 Cell values

| Value | Meaning |
|---|---|
| `yes` | At least one counted claim from the app's own sources whose quote shows the capability, as defined. |
| `partial` | The app's own evidence states a material limitation: rolling out or beta, Android-only when the feature is general, support-assisted only, or a narrower form. The note says which. |
| `no` | Explicit evidence of absence or removal from the app's own sources, or from its store listing (App Store compatibility, no Google Play listing). |
| `unknown` | Everything else. **Unknown is not no**: the app's own material, as read, does not show the capability. |

Each cell in [`data/matrix.json`](data/matrix.json) has:

| Field | |
|---|---|
| `value` | `yes`, `partial`, `no` or `unknown` |
| `quote` | the words from the source that support the value |
| `url` | where the quote is |
| `sourceType` | `app_store`, `release_notes`, `website`, `help_centre` or `google_play` |
| `date` | the source's date, if it has one |
| `note` | why, when the value was decided by a rule rather than a single claim; required for `partial` and `no` |
| `claim` | the raw claim the evidence came from (`<app>:<index>`), or null when the evidence was added by an override (for example App Store compatibility) |

**Every `yes`, `partial` and `no`, for every app including SPLYT, has a URL and a quote.** When several claims evidence a cell, the strongest is attached: a core claim over an aspect over an "also" claim; then help centre > release notes > website > App Store > Google Play. An `unknown` cell may carry the quote of a claim that was not counted, with a note saying why.

**Platform rows** (iPad, Mac, Apple Vision Pro, languages) were read from each app's App Store Compatibility and Languages sections, the same way for all six, on 2026-10-09. iPad means a native iPad build (the app is universal); Vision Pro and Mac mean "listed as compatible".

**SPLYT's in-app What's New.** Sixteen SPLYT cells cite release notes from SPLYT's in-app What's New screen, which has no web page. Their `url` is written `https://splyt.fit (in-app What's New, build N)`; the validator accepts that form only for SPLYT and reports how many cells use it. The entries since 2026-08-24 are also in `data/releases/splyt-whats-new.json`.

### 2.5 Counting

The headline number for each app is its count of **`yes` cells out of 188**.
- `partial`, `no` and `unknown` add nothing.
- Partial values aren't weighted, and features aren't weighted against each other.
- A `yes` means the feature exists in at least one tier, free or paid.

| App | Yes | % | Partial | No | Unknown |
|---|---:|---:|---:|---:|---:|
| SPLYT | 133 | 70.7% | 1 | 4 | 50 |
| Hevy | 120 | 63.8% | 0 | 4 | 64 |
| Gravl | 109 | 58.0% | 2 | 3 | 74 |
| Motra | 104 | 55.3% | 1 | 3 | 80 |
| Fitbod | 91 | 48.4% | 6 | 4 | 87 |
| Strong | 72 | 38.3% | 1 | 5 | 110 |

### 2.6 What is scripted

`npm run build:matrix` (`python3 tooling/merge/build.py`) reads `data/claims/` and `tooling/merge/mapping.py` and deterministically writes `data/features.json`, `data/matrix.json`, `data/scores.json`, `data/scores.md`, `data/vetting.json` and `MERGE-LOG.md`. It fails if a claim is out of range, mapped twice, or left unplaced. The Check workflow re-runs it on every pull request and fails if the committed files differ from the rebuild, so a cell can't be edited by hand without changing the claim or the mapping behind it.

`scripts/validate.mjs` then checks: every claim is well formed; every claim is classified exactly once, with a reason, and none is unmapped; every feature and app id is consistent across files; every cell has the full schema and an allowed value; every `yes`, `partial` and `no` has a URL and a quote; a cell's quote matches the claim it cites; and `scores.json` agrees with the matrix. Sources outside an app's official domains are reported as warnings.

## 3. Release-pace scoreboard

This counts **new features named in release notes** in a window. The window starts on **2026-08-24**, SPLYT's App Store relaunch (version 1.0.18). It ends on the date in `data/pace.json`. `scripts/compute-pace.mjs` produces the scoreboard from `data/releases/`, and you can pass it a different window with `--from` / `--to`.

### Rules, applied to every app

1. A release counts if its App Store date (UTC) falls inside the window.
2. Each new feature named in its notes counts once. A line like "5 new languages" counts as one.
3. **Fixes don't count, for anyone.** Neither do speed-ups or reliability items, such as "Faster app start" or "More reliable Apple Health sync". Each release in `data/releases/` lists these under `notCounted`.
4. **Repeated notes don't count twice.** If a release's notes are identical to the previous release's, it adds nothing (`repeatsPreviousNotes: true`).
5. **Boilerplate names nothing.** Notes like "Bug fixes and improvements" add nothing (`generic: true`).
6. When a competitor's note could be either new or improved, it is counted as **new**. When in doubt, the other app gets the point.
7. A release that a person hasn't classified yet is listed under `pendingReview` and adds nothing until someone does.

### Sources

- **Competitors:** the App Store version history, from `apps.apple.com/us/app/id<ID>`.
  - Apple shows only the 25 most recent versions. Older entries come from earlier fetches and from Internet Archive copies of the same page, and the scripts never delete them.
  - Coverage per app is recorded in each file's `coverage`.
- **SPLYT:** its in-app "What's New" screen (`data/releases/splyt-whats-new.json`). Only items in the screen's **new** section count. Its "improved" and "fixed" items are tallied but not counted.
- **Cross-check:** on 2026-10-08, we checked each competitor's website, blog, help centre, Google Play listing and APK history for features shipped in the window that the release notes didn't name. We found none that qualify. The sources checked and two borderline items are in `data/pace-crosscheck-2026-10-08.json`. Neither borderline item is counted:
  - Fitbod's Family Plan is a subscription option, and its help article predates the window.
  - Gravl: Macros is a separate app.

### Not like for like

SPLYT's What's New covers over-the-air updates that never become App Store releases, so it is a more detailed record than any competitor's App Store notes. The two kinds of count aren't measured the same way, and the README says so next to the numbers. A count of SPLYT's own App Store notes under rules 1–7 hasn't been done yet. The raw notes are in `data/releases/splyt.json`.

### Automation

`scripts/fetch-releases.mjs` classifies a new release automatically only in two mechanical cases:
- its notes repeat the previous release's, or
- its notes contain only boilerplate words.

Everything else stays `features: null` until a person classifies it in review.

## 4. Updates and corrections

- **Weekly.** Every Monday, a GitHub Actions job fetches release histories and listings, recomputes the scoreboard, validates, and opens a pull request with a summary.
  - Nothing merges on its own.
  - The feature list and matrix are never changed automatically, and claims are not re-extracted automatically.
- **Corrections.** Anyone can propose a change through an issue or pull request, with a source.
  - A correction is accepted if the source is allowed and supports the change.
  - A correction changes the input — a claim in `data/claims/`, or a judgement in `tooling/merge/mapping.py` — and the outputs are rebuilt with `npm run build:matrix`.
  - Corrections to SPLYT's column, and challenges to how claims were grouped or vetted, follow the same process.

## 5. Known limitations

- **Scores measure what apps document, not what they can do.** An app that writes more release notes and help articles gets more cells marked `yes`. Strong has the thinnest documentation (120 claims; its features page is password-protected), so many Strong cells are `unknown` rather than `no`. Fitbod's release notes are boilerplate, so none of its claims are dated.
- **Unknown is not no, but it still lowers the count.** Only `yes` counts. An `unknown` means the material that was read does not show the feature. Help centres were not re-read exhaustively for every cell, so some unknowns are capabilities an app has but did not describe in the pages that were read.
- **SPLYT's index was published the day of the comparison.** It adds 288 entries to SPLYT's documented surface. 8 SPLYT `yes` cells depend on it; without it SPLYT has 125 (66%). It also removed or weakened five SPLYT cells that older SPLYT claims would have scored `yes` (section 2.1).
- **SPLYT made the judgement calls.** SPLYT wrote the extraction brief, grouped the claims into features and vetted every claim. Every one of those decisions is recorded with its reason in MERGE-LOG.md and can be challenged. Reviews from outside SPLYT are especially welcome.
- **Extraction is AI-assisted.** Each claim was read once, by a pass working on one app at a time. A claim that was missed makes a cell `unknown`; a claim that was misread is checkable against its quote and URL.
- **Granularity is a judgement.** How finely capabilities are split into features changes the totals. The rule is the same for every app, and when in doubt the grouping fairest to the other apps was chosen, but a different reasonable grouping would give different numbers.
- **Free vs paid.** A `yes` means the feature exists in some tier. The cells don't separate free from paid.
- **iOS and the US storefront.** Listings, release notes and dates come from the US App Store. Android-only features are `partial` when they're missing on iOS.
- **Some SPLYT cells cite an in-app screen.** Sixteen SPLYT cells cite its in-app What's New, which you can read only in the app (section 2.4).
- **Reddit and other user reports weren't used.** They aren't allowed sources.
- **Release history coverage** (scoreboard).
  - Gravl's history is only covered from 2026-03-01. The live page reaches back only that far, and no archived copy of the page exists from before August 2026.
  - Some version numbers never appear in a store history, such as Gravl 1.53.2–1.53.3 and Fitbod 8.27–8.28. They were presumably never released, so this isn't a gap in the data.
- **The iTunes Lookup API can lag the store page.** On 2026-10-09 it briefly reported Strong 6.5.0 after the store page listed 6.5.1. Release history comes from the page, and listing snapshots come from the API.
