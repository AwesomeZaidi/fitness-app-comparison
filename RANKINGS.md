# How the App Store rankings are made

This explains every list on **[splyt.fit/apps](https://splyt.fit/apps)**: what goes in, how apps are labelled, and how each list is ordered. You should be able to rebuild any list from Apple's public data using only this page.

SPLYT makes the page, and SPLYT is one of the apps listed. It gets the same row and the same rules as every other app. Nothing on the page is hand-ordered.

## Where the numbers come from

Everything comes from Apple's public, unauthenticated endpoints for the **US** App Store. The collection started on **2026-10-09** and runs every day at 10:00 UTC.

| What | Source |
|---|---|
| Chart positions | Health & Fitness (genre 6013) top free, top paid and top grossing feeds: `https://itunes.apple.com/us/rss/top{free,paid,grossing}applications/limit=200/genre=6013/json`. Apple returns about 100 entries per chart. |
| Finding apps | The App Store search API (`https://itunes.apple.com/search?entity=software&country=us`) run daily for the 30 terms below, plus every app on the three charts. |
| Rating, rating count, price, version, release and update dates | The lookup API (`https://itunes.apple.com/lookup?id=…&country=us`), refreshed daily for every app found so far. |

**Search terms:** workout tracker, workout log, gym tracker, gym log, weightlifting, weight lifting log, strength training, lifting tracker, progressive overload, hypertrophy, powerlifting, bodybuilding, workout planner, workout app, home workout, calisthenics, crossfit, hiit workout, rep counter, ai personal trainer, fitness planner, gym workout plan, apple watch workout, exercise log, training log, running plan, kettlebell, resistance band workout, personal trainer app, fitness tracker.

An app becomes "new" on the page from its `releaseDate`, which is its first release on the App Store, not the date we found it.

## Which apps count as workout trackers

The Health & Fitness category also holds period trackers, calorie counters and gym-chain apps. To keep the lists comparable, each app is labelled once, when it's first found, by a language model (`gpt-4.1-mini`, temperature 0). The model sees only the app's name, developer, primary genre and the first 1,500 characters of its App Store description. These are the exact instructions:

```
You classify iOS App Store apps for a directory of workout-tracking apps.
For each app, pick exactly one kind:
- strength_gym: logging, tracking or planning gym / strength / weight training (workout loggers, lifting trackers, AI gym planners, powerlifting/bodybuilding programs centred on lifting)
- general_workouts: guided workout programs — home workouts, HIIT, calisthenics, yoga-for-fitness, follow-along video classes, 7-minute workouts, wall pilates
- cardio_gps: running, cycling, walking, swimming or other GPS / cardio activity tracking and plans
- nutrition: calorie counting, macros, diet, fasting, meal planning, weight-loss food logging
- gym_membership: the app of one gym chain, box, studio or club — membership, check-in, class booking or that facility's own WODs (Planet Fitness, Crunch, Orangetheory, SugarWOD-style box apps, any "<Name> CrossFit" or "<Name> Fitness" club app), even if it also logs workouts
- wellness_other: health/fitness-adjacent but not the above — sleep, meditation, cycle/period tracking, steps-for-rewards, heart rate monitors, activity rings, medical, posture, habit trackers
- not_fitness: not a health or fitness app
```

| Label | Shown on the page as | Included in lists |
|---|---|---|
| `strength_gym` | Gym & strength | Yes. This is the default ranking scope. |
| `general_workouts` | Guided workouts | Yes, under "All workout apps" and in the directory |
| `cardio_gps` | Running & cardio | Directory only, behind a filter |
| `nutrition`, `gym_membership`, `wellness_other`, `not_fitness` | — | No |

Labels can be wrong, because a model reads marketing copy. If an app is mislabelled, [open an issue](../../issues/new) with the App Store link. A correction is applied by hand and noted in the issue.

## How each list is ordered

Every list states its rule in one line on the page. These are those rules in full:

| List | Order | Notes |
|---|---|---|
| **Today** | The app's position in Apple's US Health & Fitness chart (free, paid or grossing) on the latest collection day | Only apps in scope are shown, keeping Apple's own rank number, so gaps are normal: #13, #35, #36… |
| **This week / This month / This year** | Ratings gained: today's total rating count minus the count 7, 30 or 365 days earlier | Until our own record covers the window, the start count comes from an Internet Archive copy of the app's page (see "History from before we started"), and the page marks the gain ≈ with the copy's date. |
| **All time** | Total App Store rating count, among **active** apps | Ratings, not downloads. Apple doesn't publish download numbers. The page's Active · Inactive · All switch changes this. |
| **New this week** | First App Store release in the last 7 days, newest first | Directory scope (gym & strength plus guided workouts) |
| **Directory (every sort)** | Active apps by default; Inactive and All are one tap away | See "Active and inactive apps" below. |
| **Directory: Top rated** | Average star rating, among apps with **at least 100 ratings**; ties broken by rating count | The floor stops a single 5★ review from winning. |
| **Directory: Most reviews / Newest / Today's chart** | Rating count / first release date / chart position | |

## History from before we started

Our own daily record began on 2026-10-09, so on their own the week, month and year lists would stay empty for 7, 30 and 365 days. To fill that gap, we read old copies of each app's US App Store page from the [Internet Archive](https://web.archive.org/). Each copy has Apple's **exact** rating count in its structured data (`aggregateRating.reviewCount`).

For each window, the start count is taken as follows:

1. **Our own row** for exactly 7, 30 or 365 days ago, when we have one. This is exact.
2. Otherwise, **the archive copy closest to that day**, within 3 days for the week, 10 days for the month and 60 days for the year. The gain is scaled to the window's length: `(today − then) × window ÷ days between`. The page shows these gains as "≈ +N" with the date of the copy.
3. Otherwise, **no entry**. Apps with no archive copy near the start are left out of that list instead of being guessed.

Each archive point links to the copy it came from (`source_url`). Once our own record covers a window (week on 2026-10-16, month on 2026-11-08, year on 2027-10-09), it takes over automatically and the ≈ marks go away. Each app's page also charts its rating count over time, using archive copies (hollow dots) and our daily record (solid dots).

## Community upvotes and notes

The page also has a **community** chart, kept apart from Apple's numbers. These numbers never change any ranking based on Apple's data.

- **Who can vote.** Anyone signed in, with Google or an emailed link. An account is a SPLYT account, and you don't need the app.
- **Votes.** One upvote per person per app, removable. The chart counts upvotes cast in the last 24 hours, 7 days, 30 days or 365 days, plus all time.
- **Notes.** One note per person per app, and you can edit it. A note records how you know the app (use it now / used to / tried it), for how long, what you pay, which app you switched from and why, and what the app is good and not great at. Writing a comment is optional. The structured answers are added up into each app's summary.
- **What we hold ourselves to.**
  - SPLYT's team **can't upvote SPLYT**. The database enforces this, not the page.
  - Anything the team writes carries a "SPLYT team" badge.
  - Notes can't contain links.
  - Votes and posts are rate-limited.
  - There is no paid placement and there are no sponsored rows.
- **What's public.** Display names, votes and notes. Emails and account ids are never shown.
- **Moderation.** People can report a note. Reported notes are reviewed by hand: hidden, deleted, or left up.

## Active and inactive apps

An app is **inactive** if its last App Store update (the lookup API's `currentVersionReleaseDate`) is more than **365 days** old. Many once-popular apps still hold large rating counts years after their last release, so the all-time list and the directory hide inactive apps by default. The Active · Inactive · All switch shows just the inactive ones or everything, and an inactive app's row says "No update since <date>". Lists based on today's chart or on recent rating gains aren't filtered: an app has to be in active use to show up there.

## What is published, and what isn't

- **Published:**
  - Every list as shown, exported weekly to [`data/rankings/`](data/rankings/) by `scripts/export-rankings.mjs`. Any past list can be checked against what the page said.
  - This method.
  - The labelling instructions above.
- **Not published:**
  - The raw daily snapshot tables behind the lists.
  - The questions visitors type into the site's recommender, which are private.

The lists are built from Apple's public data, so anyone can start their own daily collection and check ours going forward.

## Limits

- **US App Store, iPhone only.**
- **Ratings aren't downloads or quality.** Older apps have had longer to collect them.
- **Apple's charts are opaque.** Apple doesn't publish how chart positions are computed, and a chart position reflects recent downloads, not how good an app is.
- **Search can miss apps.** An app that matches none of the 30 terms and never charts won't appear. Suggest a term or an app via an issue.
