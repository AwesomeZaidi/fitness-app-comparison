#!/usr/bin/env node
// Check that data/ follows the rules in METHODOLOGY.md. Exits 1 on any error.
//
//   node scripts/validate.mjs
//   node scripts/validate.mjs --strict   # warnings count as errors too
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, readJson, readJsonIfExists, args } from './lib.mjs';
import { computePace } from './compute-pace.mjs';

const opt = args();
const errors = [];
const warnings = [];
const err = (m) => errors.push(m);
const warn = (m) => warnings.push(m);

const VALUES = ['yes', 'partial', 'no', 'unknown'];
const DATE = /^\d{4}-\d{2}-\d{2}$/;
const isDate = (s) => typeof s === 'string' && DATE.test(s) && !Number.isNaN(new Date(s).getTime());
// Wrong-app guard: "MOTRA" (6756487760) is a different company's app.
const FORBIDDEN_IDS = { '6756487760': 'MOTRA, an unrelated effort-points app — Motra is 1548577496' };

// ---- features.json
const fjson = readJson('data/features.json');
const catIds = new Set(fjson.categories.map((c) => c.id));
const featIds = new Set();
for (const f of fjson.features) {
  if (!/^[a-z][a-z0-9_]*$/.test(f.id)) err(`features: bad id "${f.id}"`);
  if (featIds.has(f.id)) err(`features: duplicate id "${f.id}"`);
  featIds.add(f.id);
  if (!catIds.has(f.category)) err(`features: ${f.id} has unknown category "${f.category}"`);
  if (!f.label?.trim()) err(`features: ${f.id} has no label`);
  if (!f.definition?.trim()) err(`features: ${f.id} has no definition`);
}

// ---- apps.json
const ajson = readJson('data/apps.json');
const apps = ajson.apps;
const appIds = new Set();
for (const a of apps) {
  if (appIds.has(a.id)) err(`apps: duplicate id "${a.id}"`);
  appIds.add(a.id);
  if (!/^\d+$/.test(a.appStoreId)) err(`apps: ${a.id} appStoreId must be digits`);
  if (FORBIDDEN_IDS[a.appStoreId]) err(`apps: ${a.id} uses App Store id ${a.appStoreId} (${FORBIDDEN_IDS[a.appStoreId]})`);
  if (!['app-store', 'in-app-whats-new'].includes(a.paceSource)) err(`apps: ${a.id} has unknown paceSource "${a.paceSource}"`);
  if (!Array.isArray(a.officialDomains) || !a.officialDomains.length) err(`apps: ${a.id} needs officialDomains`);
}
const publishers = apps.filter((a) => a.publisher);
if (publishers.length !== 1) err(`apps: exactly one app must be marked publisher (found ${publishers.length})`);

// ---- matrix.json
const m = readJson('data/matrix.json');
const officialFor = (app) => new Set([...(ajson.sharedOfficialDomains ?? []), ...app.officialDomains]);
for (const fid of Object.keys(m.cells)) if (!featIds.has(fid)) err(`matrix: unknown feature id "${fid}"`);
for (const fid of featIds) {
  const row = m.cells[fid];
  if (!row) { err(`matrix: feature "${fid}" is missing`); continue; }
  for (const k of Object.keys(row)) if (!appIds.has(k)) err(`matrix: ${fid} has unknown app "${k}"`);
  for (const app of apps) {
    const c = row[app.id];
    const at = `matrix: ${fid} / ${app.id}`;
    if (!c) { err(`${at} is missing`); continue; }
    if (!VALUES.includes(c.value)) err(`${at} value "${c.value}" not in ${VALUES.join('|')}`);
    if (!isDate(c.checkedAt)) err(`${at} checkedAt must be YYYY-MM-DD`);
    if (app.publisher) {
      if (c.basis !== 'self-reported') err(`${at} must have basis "self-reported"`);
      if (!c.note?.trim()) err(`${at} needs a note`);
      if (c.value === 'partial' && /^Self-reported: checked/.test(c.note)) err(`${at} is partial but its note does not say what is missing`);
      continue;
    }
    if (c.basis !== 'public-source') err(`${at} must have basis "public-source"`);
    if (c.value !== 'unknown') {
      if (!c.source) { err(`${at} is "${c.value}" but has no source URL`); continue; }
      let u;
      try { u = new URL(c.source); } catch { err(`${at} source is not a URL: ${c.source}`); continue; }
      if (u.protocol !== 'https:') err(`${at} source must be https: ${c.source}`);
      if (!c.note?.trim()) err(`${at} is "${c.value}" but has no quote or paraphrase in note`);
      const host = u.hostname;
      const ok = [...officialFor(app)].some((d) => host === d || host.endsWith(`.${d}`));
      if (!ok) warn(`${at} source is not on an official domain (${host}) — see METHODOLOGY.md, "Sources"`);
    } else if (c.source) {
      try { new URL(c.source); } catch { err(`${at} source is not a URL: ${c.source}`); }
    }
  }
}

// ---- releases
const relDir = path.join(ROOT, 'data/releases');
for (const f of fs.readdirSync(relDir).filter((f) => f.endsWith('.json'))) {
  const r = readJson(`data/releases/${f}`);
  const at = `releases/${f}`;
  if (!appIds.has(r.app)) { err(`${at}: unknown app "${r.app}"`); continue; }
  if (f.endsWith('-whats-new.json')) {
    if (r.basis !== 'self-reported') err(`${at}: basis must be "self-reported"`);
    for (const e of r.entries ?? []) {
      if (!isDate(e.date)) err(`${at}: entry ${e.build} has a bad date`);
      if (!Array.isArray(e.new)) err(`${at}: entry ${e.build} needs a "new" array`);
    }
    continue;
  }
  const app = apps.find((a) => a.id === r.app);
  if (f !== `${r.app}.json`) err(`${at}: file name should be ${r.app}.json`);
  if (r.appStoreId !== app.appStoreId) err(`${at}: appStoreId ${r.appStoreId} does not match apps.json (${app.appStoreId})`);
  if (!isDate(r.fetchedAt)) err(`${at}: fetchedAt must be YYYY-MM-DD`);
  const seen = new Set();
  let prevDate = '9999-12-31';
  for (const x of r.releases) {
    const id = `${at} ${x.version}`;
    if (seen.has(x.version)) err(`${id}: duplicate version`);
    seen.add(x.version);
    if (!isDate(x.date)) err(`${id}: bad date "${x.date}"`);
    if (x.date > prevDate) err(`${id}: releases must be sorted newest first`);
    prevDate = x.date;
    if (typeof x.notes !== 'string') err(`${id}: notes must be a string`);
    if (x.features !== null && !(Array.isArray(x.features) && x.features.every((s) => typeof s === 'string' && s.trim()))) err(`${id}: features must be null or an array of non-empty strings`);
    for (const n of x.notCounted ?? []) if (!n.item || !n.reason) err(`${id}: notCounted items need {item, reason}`);
    if (x.features?.length && (x.repeatsPreviousNotes || x.generic)) err(`${id}: repeated or boilerplate notes cannot carry features`);
    if (x.features !== null && !['human', 'auto'].includes(x.classifiedBy)) err(`${id}: a classified release needs classifiedBy "human" or "auto"`);
  }
}

// ---- pace.json is up to date
const pace = readJsonIfExists('data/pace.json');
if (!pace) err('pace.json is missing — run scripts/compute-pace.mjs');
else {
  const fresh = computePace(pace.window);
  for (const row of fresh.apps) {
    const old = pace.apps.find((a) => a.app === row.app);
    if (!old || old.newFeatures !== row.newFeatures || old.pendingReview.length !== row.pendingReview.length) {
      err(`pace.json is stale for ${row.app} (says ${old?.newFeatures}, data gives ${row.newFeatures}) — run scripts/compute-pace.mjs`);
    }
    if (row.pendingReview.length) warn(`pace: ${row.app} has ${row.pendingReview.length} release(s) in the window awaiting classification: ${row.pendingReview.map((p) => `${p.version} (${p.date})`).join(', ')}`);
  }
}

for (const w of warnings) console.log(`warning: ${w}`);
for (const e of errors) console.log(`ERROR:   ${e}`);
const fail = errors.length || (opt.strict && warnings.length);
console.log(`\n${errors.length} error(s), ${warnings.length} warning(s) — ${featIds.size} features × ${apps.length} apps checked.`);
process.exit(fail ? 1 : 0);
