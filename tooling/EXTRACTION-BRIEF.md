# Feature-claim extraction brief (identical for every app)

Goal: an objective, bottom-up feature list for a public comparison of iOS workout
trackers. The master list will be the UNION of every feature any app claims about
itself. You extract ONE app's claims. Every app gets this same brief, SPLYT included —
no app gets special treatment, and you must not consider any other app while working.

## What to extract
Every distinct user-facing capability the app SAYS it has, today:
- Logging, programming/plans, AI, Apple Watch / wearables, health integrations,
  social/competition, stats/analytics, platform availability (Android, web, iPad),
  integrations (Strava, Garmin, Apple Health…), widgets/Live Activities, import/export,
  content (exercise library size, videos), personalization, accessibility, units, etc.
- Be exhaustive and granular: if the app names it, capture it, even minor things
  ("plate calculator", "RPE logging", "dark mode", "rest timer sounds").
- Each claim = one capability. Split lists ("supersets, drop sets and circuits" → 3).

## What NOT to extract
- Pricing, trials, subscriptions, promos, referral programs, company news.
- Bug fixes, speed/reliability improvements, redesigns with no new capability.
- Roadmap / "coming soon" / beta-only / region-limited-and-not-US (note if US unavailable).
- Marketing adjectives with no capability ("the best app", "beautiful design").
- Features the app's own later sources say were REMOVED or replaced (record them in
  `removed` instead, with the source).

## Sources — ONLY the app's own public material
1. Current App Store listing: `https://itunes.apple.com/lookup?id=<ID>&country=us`
   (description) and the product page https://apps.apple.com/us/app/id<ID>.
2. Its release notes / version history: already collected at
   `/private/tmp/claude-501/-Users-asimzaidi-code-techmade-tempo5-tempo/e66187b6-9560-4cdc-801a-82d725c53bec/scratchpad/fac-repo/data/releases/<app>.json`
   (read all of it; older notes count if not later removed).
3. Its official website feature pages and blog announcements.
4. Its official help centre / docs / FAQ (feature lists, "how to" articles prove a
   feature exists). Zendesk help centres expose `/api/v2/help_center/en-us/articles.json`
   (paginate) — use it when the site blocks scraping.
5. Google Play listing only for Android-availability facts.
Not allowed: review sites, Reddit, YouTube, third-party blogs, your own knowledge.

## Output
Write JSON to `/private/tmp/claude-501/-Users-asimzaidi-code-techmade-tempo5-tempo/e66187b6-9560-4cdc-801a-82d725c53bec/scratchpad/fl/claims-<app>.json`:
```
{ "app": "<app>", "collectedAt": "2026-10-09",
  "sourcesRead": [{"url","type","what"}],
  "claims": [
    { "feature": "short neutral name, 2-6 words, no brand words",
      "detail": "one line: what it does, in neutral terms",
      "quote": "verbatim words from the source (≤ 240 chars)",
      "url": "exact source URL",
      "sourceType": "app_store|release_notes|website|help_centre|google_play",
      "date": "YYYY-MM-DD if the source is dated (release date), else null" } ],
  "removed": [ {"feature","quote","url","date"} ],
  "notes": "anything ambiguous" }
```
Use neutral feature names (e.g. "Automatic rep counting", not "AutoReps™").
One claim per capability; if several sources prove it, keep the strongest one (prefer
App Store/help centre over blog) and add others to a `"alsoAt": [url…]` field.
Accuracy over volume: never invent; every claim must have a real quote and URL you saw.
Reply with: number of claims, the 15 most distinctive ones, anything you couldn't reach.
