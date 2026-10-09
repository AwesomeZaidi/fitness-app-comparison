#!/usr/bin/env node
// Snapshot each app's App Store listing via Apple's public iTunes Lookup API
// into data/snapshots/<app>/<YYYY-MM-DD>.json.
//
//   node scripts/fetch-listings.mjs              # every app
//   node scripts/fetch-listings.mjs --app gravl  # one app
//   node scripts/fetch-listings.mjs --always     # write even if nothing changed
//   node scripts/fetch-listings.mjs --dry        # print, write nothing
//
// A snapshot is only written when something in it differs from the app's
// previous snapshot, so the folder records changes rather than every week.
// The lookup API can lag the store page by a day or so (e.g. on 2026-10-09 it
// briefly still reported Strong 6.5.0 after the page listed 6.5.1); release history
// comes from fetch-releases.mjs, not from here.
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, loadApps, writeJson, get, pause, args, selectApps, today } from './lib.mjs';

const opt = args();
const FIELDS = ['trackId', 'trackName', 'artistName', 'sellerUrl', 'version', 'currentVersionReleaseDate', 'releaseNotes', 'description', 'price', 'formattedPrice', 'currency', 'genres', 'minimumOsVersion', 'contentAdvisoryRating'];

function latestSnapshot(appId, upTo) {
  const dir = path.join(ROOT, 'data/snapshots', appId);
  if (!fs.existsSync(dir)) return null;
  const files = fs.readdirSync(dir).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f) && f.slice(0, 10) <= upTo).sort();
  if (!files.length) return null;
  return JSON.parse(fs.readFileSync(path.join(dir, files.at(-1)), 'utf8'));
}

const comparable = (s) => JSON.stringify(FIELDS.map((k) => s?.listing?.[k] ?? null));

let failed = 0;
const stamp = today();
for (const [i, app] of selectApps(loadApps(), opt).entries()) {
  if (i) await pause(1000);
  try {
    const url = `https://itunes.apple.com/lookup?id=${app.appStoreId}&country=us`;
    const body = JSON.parse(await get(url));
    const r = body.results?.[0];
    if (!r || String(r.trackId) !== String(app.appStoreId)) throw new Error(`lookup returned no result for id ${app.appStoreId}`);
    const listing = Object.fromEntries(FIELDS.map((k) => [k, r[k] ?? null]));
    const snap = { app: app.id, source: url, fetchedAt: new Date().toISOString(), listing };
    const prev = latestSnapshot(app.id, stamp);
    const same = prev && comparable(prev) === comparable(snap);
    const rel = `data/snapshots/${app.id}/${stamp}.json`;
    if (same && !opt.always) {
      console.log(`${app.id.padEnd(7)} unchanged since ${prev.fetchedAt.slice(0, 10)} (v${listing.version})`);
      continue;
    }
    console.log(`${app.id.padEnd(7)} v${listing.version} (${listing.currentVersionReleaseDate?.slice(0, 10)}) → ${prev ? 'changed' : 'first snapshot'}: ${rel}`);
    if (!opt.dry) writeJson(rel, snap);
  } catch (e) {
    failed++;
    console.error(`${app.id.padEnd(7)} FAILED: ${e.message}`);
  }
}
if (failed) process.exit(1);
