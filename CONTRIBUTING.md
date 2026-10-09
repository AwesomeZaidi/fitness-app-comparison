# Contributing

Thanks for helping. You don't need to be a developer: most contributions are a link and a sentence in an issue form.

**What happens to your contribution:** it's labelled within 3 days, decided within 14, and if it's accepted the change is credited to you in the pull request. Corrections to SPLYT's own cells are handled first. Before opening a pull request, run `npm run check`. Please read the [code of conduct](CODE_OF_CONDUCT.md).

Corrections are the main reason this repository is public. If a value is wrong, we want to know, and that includes values for SPLYT.

## The quick way: open an issue

- **[Correct a cell](../../issues/new?template=correction.yml).** Give the app, the feature, the value you propose, and a link to an allowed source with the sentence that supports it.
- **[Suggest a feature](../../issues/new?template=new-feature.yml).** Give a name and a definition precise enough that two people would mark the same app the same way.

Allowed sources are the app's App Store listing and release notes, its official website, help centre or docs, official blog, and Google Play listing. [METHODOLOGY.md](METHODOLOGY.md#sources) has the full rule.

## Editing the data yourself

You need Node 20 or newer. There is nothing to install.

### Correcting a matrix cell

Edit `data/matrix.json`. Each cell looks like this:

```json
"auto_rep_counting": {
  "gravl": {
    "value": "unknown",
    "source": null,
    "note": "Not mentioned in the watch help articles' lists of wrist features or in release notes.",
    "checkedAt": "2026-10-08",
    "basis": "public-source"
  }
}
```

1. Set `value` to `yes`, `partial`, `no` or `unknown`.
2. Set `source` to an https link on an allowed source. A `yes`, `partial` or `no` value needs one.
3. Put a short quote from the source, or a close paraphrase, in `note`. For `partial`, the note also says what is missing.
4. Set `checkedAt` to today's date.
5. Run `node scripts/validate.mjs`. It must pass.
6. Open a pull request with the source link in the description.

A `no` needs positive evidence: an explicit statement, or absence from a thorough official feature list. "I couldn't find it" means `unknown`.

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

- **A new feature** needs a cell for every app, each following the rules above.
- **A new app** needs an entry in `data/apps.json` (App Store id, official domains, `paceSource: "app-store"`) and a cell for every feature.

Running `node scripts/fetch-releases.mjs --app <id>` creates the app's release file.

## Scripts

| Script | What it does |
|---|---|
| `scripts/fetch-releases.mjs` | Reads each App Store page's version history and merges it into `data/releases/<app>.json`. It never deletes older entries. Options: `--app`, `--dry`. |
| `scripts/fetch-listings.mjs` | Snapshots each listing (description, version, release notes) from the iTunes Lookup API into `data/snapshots/<app>/<date>.json`, only when something changed. Options: `--app`, `--always`, `--dry`. |
| `scripts/compute-pace.mjs` | Builds `data/pace.json` from `data/releases/`. Options: `--from`, `--to`, `--stdout`. |
| `scripts/validate.mjs` | Checks the rules and exits non-zero on any error. `--strict` also fails on warnings. |
| `scripts/diff-report.mjs` | Writes a Markdown summary of what changed since the last commit, used as the weekly PR body. Options: `--out`, `--validation`. |

## For maintainers

- `.github/workflows/weekly.yml` runs every Monday and can be started by hand from the Actions tab.
  - It needs **Settings → Actions → General → "Allow GitHub Actions to create and approve pull requests"** turned on.
  - It never merges anything.
- `.github/workflows/validate.yml` runs the validator on every pull request.
- **Review weekly PRs like any other.**
  1. Classify the releases that need it.
  2. Check whether a listing change affects any cell. If it does, fix the cell in a separate correction with its source.
  3. Merge.

## Conduct

Be specific and cite sources. Disagreements are settled by evidence, not by who is asking. If you work for one of these apps, that's fine, but please say so.
