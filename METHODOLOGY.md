# Methodology

These are the rules behind every value in `data/`. Where a rule can be checked by a script, `scripts/validate.mjs` checks it.

**Conflict of interest:** SPLYT wrote these rules, collected the data, and makes one of the six apps. The rules are designed so that someone outside SPLYT can check every competitor value. SPLYT's own column can't be checked that way, and the limits that follow from this are listed at the end.

## 1. What is compared

- **Apps.** SPLYT, Hevy, Strong, Gravl, Fitbod and Motra, identified by their US App Store ids in [`data/apps.json`](data/apps.json).
  - Motra is App Store id **1548577496** (Train Fitness Inc.). It is *not* "MOTRA" (id 6756487760), an unrelated app from a different company. The validator rejects that id.
  - The comparison is limited to these six apps for now.
- **Features.** The 52 features in [`data/features.json`](data/features.json), in eight categories. Each has a one-line definition, and the cell is judged against that definition, not against the shorter label.
  - SPLYT drew up the list. See [Known limitations](#5-known-limitations).

## 2. Feature cells

### Values

| Value | Meaning |
|---|---|
| `yes` | An allowed source shows the app does this, as defined. |
| `partial` | The app does part of it, or only in a narrower form. The note says which part. |
| `no` | An allowed source says the app does not do this, **or** the app's thorough official feature list leaves it out. |
| `unknown` | We couldn't establish it either way from allowed sources. |

### "No" needs evidence

Not finding something isn't evidence that it's missing. A competitor cell is only `no` when one of these is true:
- an official source says so (for example, "At this time Motra is available exclusively for the Apple Watch"), or
- the app publishes a thorough feature list, such as a full features page or a complete help centre, and the feature isn't in it.

Otherwise the cell is `unknown`.

### Sources

Each competitor cell with a `yes`, `partial` or `no` value has:
- `source`: an https link to one of the **allowed sources** below, and
- `note`: a quote from that source or a close paraphrase, saying where on the page to look when that helps.

The **allowed sources** are:
- the app's **App Store** listing and release notes
- the app's **official website**
- its **help centre or documentation**
- its **official blog**
- its **Google Play** listing

Each app's official domains are listed in `data/apps.json`. These don't count as sources: reviews, Reddit, YouTube, third-party blogs, comparison sites, and our own testing of a competitor's app. They can point us to an official source, but they can't replace one.

`unknown` cells may have a source and a note too, usually to record what was searched.

### SPLYT's column

SPLYT's cells have `"basis": "self-reported"`. They were checked against SPLYT's own source code on 2026-10-08. That code isn't public, so you can't check these cells the same way as the others. You can check them by using the app, and challenge any of them through the same correction process as everyone else.

Each `partial` value carries a note saying what is missing:
- **Works offline:** workouts log offline and sync later. Not everything works offline.
- **Strava:** activities arrive only through Apple Health. There is no direct connection.
- **Progression suggestions:** last time's weights are prefilled, but no increase is suggested.

### Counting

The headline number for each app is its count of **`yes` cells out of 52**.
- `partial`, `no` and `unknown` add nothing.
- Partial values aren't weighted, and features aren't weighted against each other.

Each cell has a `checkedAt` date. A value describes the app on that date.

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
  - The matrix is never changed automatically.
- **Corrections.** Anyone can propose a change through an issue or pull request, with a source.
  - A correction is accepted if the source is allowed and supports the change.
  - When a cell changes, its `checkedAt` is updated.
  - Corrections to SPLYT's column follow the same process.

## 5. Known limitations

- **SPLYT chose the features.** A company's list tends to include what that company has built. Suggestions for features SPLYT lacks are especially welcome.
- **Unknown is not no, but it still lowers the count.** SPLYT has no `unknown` cells, because its makers know their app. Competitors have 8 to 19 each. Apps that document less score lower partly for that reason. On most of the features where SPLYT is the only confirmed `yes`, the other apps are `unknown`, not `no`.
- **Garmin & other wearables.** The definition counts Wear OS support. Hevy and Fitbod are `yes` through their Wear OS apps only, and neither supports Garmin; their notes say so. Gravl supports both. If you only care about Garmin, read the notes.
- **Free vs paid.** A `yes` means the feature exists in some tier. The cells don't separate free from paid.
- **iOS and the US storefront.** Listings, release notes and dates come from the US App Store. Android-only features, such as Fitbod's photo import, are marked `partial` when they're missing on iOS.
- **Reddit and other user reports weren't used.** They aren't allowed sources. Also, during collection Reddit returned HTTP 403 for every request and the Internet Archive was temporarily offline, so they couldn't have been used to find leads either.
- **Release history coverage.**
  - Gravl's history is only covered from 2026-03-01. The live page reaches back only that far, and no archived copy of the page exists from before August 2026.
  - Some version numbers never appear in a store history, such as Gravl 1.53.2–1.53.3 and Fitbod 8.27–8.28. They were presumably never released, so this isn't a gap in the data.
- **The iTunes Lookup API can lag the store page.** On 2026-10-09 it briefly reported Strong 6.5.0 after the store page listed 6.5.1. Release history comes from the page, and listing snapshots come from the API.
- **Exceptions to the source rule, flagged for re-checking:**
  - Fitbod "Export your data" (`yes`) cites a third-party guide, because Fitbod's help centre has no article on it. The validator warns about this cell until it has an official source.
  - Two notes also mention third-party material as context only: a user review in Hevy "Works offline", and a blog claim in Strong "Garmin & other wearables". Neither value depends on it.
- **Conflicting official sources.** Gravl's App Store copy says the Watch works "without your phone", but its help centre says the phone still owns and saves the session. The cell is `partial` and the note quotes both.
- **Judgement calls exist.** Where one official source is thinner than another, cells that look similar can land differently. For example:
  - Hevy "Habits" and "Sleep" are `no` because they're absent from Hevy's 48-item feature list, but Hevy "Log by voice", with the same absence, is `unknown`.
  - Grip variants that exist only as separate library exercises are `partial` for Fitbod and Motra and `unknown` for Hevy.

  These are open to correction like anything else.
