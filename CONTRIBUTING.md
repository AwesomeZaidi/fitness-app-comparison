# Contributing

Thanks for helping. You don't need to be a developer: most contributions are a link and a sentence in an issue form.

**What happens to your contribution:** it's labelled within 3 days, decided within 14, and if it's accepted the change is credited to you in the pull request. Corrections to SPLYT's own cells are handled first. Before opening a pull request, run `npm run check`. Please read the [code of conduct](CODE_OF_CONDUCT.md).

Corrections are the main reason this repository is public. If a value is wrong, we want to know, and that includes values for SPLYT.

## The quick way: open an issue

- **[Correct a cell](../../issues/new?template=correction.yml).** Give the app, the feature, the value you propose, and a link to an allowed source with the sentence that supports it.
- **[Suggest a feature](../../issues/new?template=new-feature.yml).** The list is built from what apps document, so a new feature needs an app's own source that documents it. Give a name, a definition precise enough that two people would mark the same app the same way, and that source.
- **Challenge a judgement.** If two features should be merged or split, or a claim was classified wrongly (see [MERGE-LOG.md](MERGE-LOG.md)), open a correction and name the feature id or claim, for example `hevy:94`.

Allowed sources are the app's App Store listing and release notes, its official website, help centre or docs, official blog, and Google Play listing. [METHODOLOGY.md](METHODOLOGY.md#21-collecting-claims) has the full rule.

## Editing the data yourself

You need Node 20 or newer, and Python 3 to rebuild the matrix. There is nothing to install.

### Correcting a matrix cell

`data/matrix.json`, `data/features.json`, `data/scores.json`, `data/vetting.json` and `MERGE-LOG.md` are **generated**. Don't edit them by hand: the Check workflow rebuilds them and fails if they differ. Each cell looks like this:

```json
"auto-rep-counting": {
  "motra": {
    "value": "yes",
    "quote": "tracking reps for over 470 unique exercise types – completely hands free!",
    "url": "https://apps.apple.com/us/app/id1548577496",
    "sourceType": "app_store",
    "date": "2026-08-10",
    "note": null,
    "claim": "motra:1"
  }
}
```

`claim` is the raw claim the cell was built from: index 1 in `data/claims/motra.json`. To change a cell, change what it is built from:

1. **A missing claim** (the app documents the feature, but the cell is `unknown`): add a claim to the end of `data/claims/<app>.json` with `feature`, `detail`, a verbatim `quote` (≤ 240 characters), the exact `url`, its `sourceType` (`app_store`, `release_notes`, `website`, `help_centre` or `google_play`) and `date` (or null). Then add its index to the feature's entry for that app in `tooling/merge/mapping.py` (for example `m="1 a11 a18 159"`). Never renumber existing claims.
2. **A misclassified claim** (counted when it shouldn't be, or the reverse): add, change or remove its line in `VET` in `tooling/merge/mapping.py`, with the class and a reason.
3. **Evidence that isn't a claim of a feature** (for example evidence of absence for a `no`): add an entry to `OVERRIDES` in `tooling/merge/mapping.py` with the value, a note, and the quote, url, sourceType and date.

Then:

```sh
npm run build:matrix   # rebuilds the generated files
npm run check          # must pass
```

Open a pull request with the source link in the description. A `no` needs positive evidence: an explicit statement, or a store listing that shows the absence. "I couldn't find it" means `unknown`.

### Classifying a new release (scoreboard)

The weekly job adds new App Store releases to `data/releases/<app>.json`. If a release's notes aren't just a repeat of the previous release or boilerplate, it arrives with `"features": null`, which means it needs review. To classify it:

```json
{
  "version": "1.54",
  "date": "2026-10-12",
  "notes": "…",
  "features": ["Named new feature A", "Named new feature B"],
  "notCounted": [{ "item": "Fix: something", "reason": "fix" },
                 { "item": "Faster sync", "reason": "speed or reliability" }],
  "classifiedBy": "human"
}
```

- List each new feature the notes **name**, in the notes' own words, shortened if needed.
- Put fixes, speed-ups and reliability items in `notCounted`.
- If an item could be either new or improved, count it as new.

Then run:

```sh
node scripts/compute-pace.mjs   # rewrites data/pace.json
node scripts/validate.mjs
```

### Adding a feature or an app

This changes what is being compared, so open an issue first.

- **A new feature** needs at least one app's counted claim behind it: add the claim(s) to `data/claims/`, then an `F(...)` entry in `tooling/merge/mapping.py` with an id, name, category and definition, and the claim indices for each app. Check every other app's claims for the same capability, and keep to the granularity rules in [METHODOLOGY.md](METHODOLOGY.md#23-canonicalisation-from-claims-to-features).
- **A new app** needs an entry in `data/apps.json` (App Store id, official domains, `paceSource: "app-store"`), a `data/claims/<app>.json` extracted with [`tooling/EXTRACTION-BRIEF.md`](tooling/EXTRACTION-BRIEF.md), every claim placed in `tooling/merge/mapping.py`, and the app added to `APPS` in `tooling/merge/build.py`.

Running `node scripts/fetch-releases.mjs --app <id>` creates the app's release file.

## Scripts

| Script | What it does |
|---|---|
| `scripts/fetch-releases.mjs` | Reads each App Store page's version history and merges it into `data/releases/<app>.json`. It never deletes older entries. Options: `--app`, `--dry`. |
| `scripts/fetch-listings.mjs` | Snapshots each listing (description, version, release notes) from the iTunes Lookup API into `data/snapshots/<app>/<date>.json`, only when something changed. Options: `--app`, `--always`, `--dry`. |
| `scripts/compute-pace.mjs` | Builds `data/pace.json` from `data/releases/`. Options: `--from`, `--to`, `--stdout`. |
| `tooling/merge/build.py` | `npm run build:matrix`. Rebuilds features, matrix, scores, vetting and MERGE-LOG.md from `data/claims/` and `tooling/merge/mapping.py`. Fails on unplaced or double-mapped claims. Python 3, no dependencies. |
| `scripts/validate.mjs` | Checks the rules and exits non-zero on any error. `--strict` also fails on warnings. |
| `scripts/diff-report.mjs` | Writes a Markdown summary of what changed since the last commit, used as the weekly PR body. Options: `--out`, `--validation`. |

## For maintainers

- `.github/workflows/weekly.yml` runs every Monday and can be started by hand from the Actions tab.
  - It needs **Settings → Actions → General → "Allow GitHub Actions to create and approve pull requests"** turned on.
  - It never merges anything.
- `.github/workflows/validate.yml` runs on every pull request: it rebuilds the matrix (failing if the committed data differs), validates, and runs the tests.
- **Review weekly PRs like any other.**
  1. Classify the releases that need it.
  2. Check whether a listing change affects any cell. If it does, fix the claim or mapping in a separate correction with its source.
  3. Merge.

## Conduct

Be specific and cite sources. Disagreements are settled by evidence, not by who is asking. If you work for one of these apps, that's fine, but please say so.
