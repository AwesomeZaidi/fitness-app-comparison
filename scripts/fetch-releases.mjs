#!/usr/bin/env node
// Fetch each app's App Store version history and merge it into
// data/releases/<app>.json.
//
//   node scripts/fetch-releases.mjs                 # every app
//   node scripts/fetch-releases.mjs --app hevy      # one app (comma-separate for more)
//   node scripts/fetch-releases.mjs --dry           # print, write nothing
//
// apps.apple.com serves the 25 most recent versions inside a JSON blob in the
// page (<script id="serialized-server-data">). Older entries already in the
// file are never deleted. A new entry is classified automatically only when
// that is mechanical (notes identical to the previous release, or boilerplate
// like "Bug fixes and improvements"); otherwise `features` is null and a
// person fills it in during review. See CONTRIBUTING.md.
import { loadApps, readJsonIfExists, writeJson, get, pause, args, selectApps, today, isGeneric, normalizeNotes } from './lib.mjs';

const opt = args();

/** Pull every {version, date, notes} out of an apps.apple.com product page. */
function parseVersionHistory(html) {
  const blobs = [];
  const tagged = html.match(/<script[^>]*id="?serialized-server-data"?[^>]*>([\s\S]*?)<\/script>/);
  if (tagged) blobs.push(tagged[1]);
  // Fallback: any other inline JSON script that mentions a version history.
  for (const m of html.matchAll(/<script[^>]*type="application\/(?:ld\+)?json"[^>]*>([\s\S]*?)<\/script>/g)) {
    if (m[1] !== tagged?.[1] && /versionHistory|versionDisplay/.test(m[1])) blobs.push(m[1]);
  }
  const found = new Map();
  const add = (version, rawDate, notes) => {
    version = String(version || '').replace(/^Version\s+/i, '').trim();
    const d = new Date(rawDate);
    if (!version || Number.isNaN(d.getTime())) return;
    const rel = { version, date: d.toISOString().slice(0, 10), notes: normalizeNotes(notes) };
    const prev = found.get(version);
    if (!prev || rel.notes.length > prev.notes.length) found.set(version, rel);
  };
  const walk = (o) => {
    if (Array.isArray(o)) return o.forEach(walk);
    if (!o || typeof o !== 'object') return;
    // Current page structure (2026): TitledParagraph items, version in
    // primarySubtitle ("6.5.1" or "Version 6.5.1"), date in secondarySubtitle.
    if (o.$kind === 'TitledParagraph' && o.primarySubtitle && o.secondarySubtitle) add(o.primarySubtitle, o.secondarySubtitle, o.text);
    // Older structure: { versionDisplay, releaseDate, releaseNotes }.
    if (o.versionDisplay && o.releaseDate) add(o.versionDisplay, o.releaseDate, o.releaseNotes);
    for (const v of Object.values(o)) walk(v);
  };
  for (const b of blobs) {
    try { walk(JSON.parse(b)); } catch { /* not JSON; ignore */ }
  }
  return [...found.values()];
}

const cmpRelease = (a, b) => (a.date === b.date ? b.version.localeCompare(a.version, 'en', { numeric: true }) : b.date.localeCompare(a.date));

function merge(file, app, fetched, stamp) {
  const out = file ?? {
    app: app.id,
    appStoreId: app.appStoreId,
    source: app.appStoreUrl,
    history: 'Built by scripts/fetch-releases.mjs from the live App Store page.',
    coverage: { from: null, to: null, note: '' },
    fetchedAt: null,
    releases: [],
  };
  const byVersion = new Map(out.releases.map((r) => [r.version, r]));
  const added = [], changed = [];
  for (const f of fetched) {
    const have = byVersion.get(f.version);
    if (!have) {
      const r = { version: f.version, date: f.date, notes: f.notes, generic: null, repeatsPreviousNotes: null, features: null, notCounted: [], classifiedBy: null, firstSeen: stamp };
      out.releases.push(r);
      byVersion.set(f.version, r);
      added.push(r);
    } else if (normalizeNotes(have.notes) !== f.notes) {
      have.previousNotes = have.notes;
      have.notes = f.notes;
      have.notesChangedSeen = stamp;
      changed.push(have);
    }
  }
  out.releases.sort(cmpRelease);
  // Classify the new ones only where it is mechanical.
  for (const r of added) {
    const i = out.releases.indexOf(r);
    const older = out.releases[i + 1];
    r.repeatsPreviousNotes = !!older && normalizeNotes(older.notes) === normalizeNotes(r.notes);
    r.generic = isGeneric(r.notes);
    if (r.repeatsPreviousNotes || r.generic) { r.features = []; r.classifiedBy = 'auto'; }
  }
  const dates = out.releases.map((r) => r.date).sort();
  if (dates.length && (!out.coverage.from || dates[0] < out.coverage.from)) out.coverage.from = dates[0];
  out.coverage.to = dates.at(-1) ?? out.coverage.to;
  out.fetchedAt = stamp;
  return { file: out, added, changed };
}

async function main() {
  const apps = selectApps(loadApps(), opt);
  const stamp = today();
  let failed = 0;
  for (const [i, app] of apps.entries()) {
    if (i) await pause(1500);
    try {
      const html = await get(app.appStoreUrl);
      const fetched = parseVersionHistory(html);
      if (!fetched.length) throw new Error('no version history found in the page (structure changed?)');
      const rel = `data/releases/${app.id}.json`;
      const { file, added, changed } = merge(readJsonIfExists(rel), app, fetched, stamp);
      if (app.paceSource !== 'app-store') {
        file.paceNote = `${app.name}'s scoreboard count does not use these App Store entries (paceSource: ${app.paceSource}); they are kept for reference and left unclassified.`;
      }
      const pending = added.filter((r) => r.features === null).length;
      console.log(`${app.id.padEnd(7)} ${String(fetched.length).padStart(2)} on page, ${added.length} new (${pending} need review), ${changed.length} with changed notes; newest ${fetched.map((r) => r.date).sort().at(-1)}`);
      if (!opt.dry) writeJson(rel, file);
    } catch (e) {
      failed++;
      console.error(`${app.id.padEnd(7)} FAILED: ${e.message}`);
    }
  }
  if (failed) process.exit(1);
}

await main();
