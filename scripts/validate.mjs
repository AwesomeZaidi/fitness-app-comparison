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
const SOURCE_TYPES = ['app_store', 'release_notes', 'website', 'help_centre', 'google_play'];
const CLASSES = ['capability', 'aspect', 'unsubstantiated', 'not_shipped', 'fix', 'ui_tweak', 'vague', 'out_of_scope'];
const CELL_KEYS = ['value', 'quote', 'url', 'sourceType', 'date', 'note', 'claim'];
// SPLYT's in-app What's New screen has no web page; cells citing it name the build instead.
const IN_APP_WHATS_NEW = /^https:\/\/splyt\.fit \(in-app What['’]s New, build \d+\)$/;
const DATE = /^\d{4}-\d{2}-\d{2}$/;
const isDate = (s) => typeof s === 'string' && DATE.test(s) && !Number.isNaN(new Date(s).getTime());
// Wrong-app guard: "MOTRA" (6756487760) is a different company's app.
const FORBIDDEN_IDS = { '6756487760': 'MOTRA, an unrelated effort-points app — Motra is 1548577496' };

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
const officialFor = (app) => new Set([...(ajson.sharedOfficialDomains ?? []), ...app.officialDomains]);

// ---- data/claims: the raw, per-app claims every feature and cell is built from
const claims = {}; // app -> array of claims; SPLYT's feature index is addressed as "i<n>"
const claimKey = (app, idx) => `${app}:${idx}`;
const claimByKey = new Map();
function loadClaims(file, app, prefix) {
  const at = `claims/${file}`;
  const d = readJsonIfExists(`data/claims/${file}`);
  if (!d) { err(`${at} is missing`); return; }
  if (d.app !== app && !(prefix && d.app?.startsWith(app))) err(`${at}: "app" is "${d.app}", expected "${app}"`);
  if (!isDate(d.collectedAt)) err(`${at}: collectedAt must be YYYY-MM-DD`);
  if (!Array.isArray(d.claims) || !d.claims.length) { err(`${at}: needs a non-empty "claims" array`); return; }
  d.claims.forEach((c, i) => {
    const id = `${at} #${prefix}${i}`;
    if (!c.feature?.trim()) err(`${id}: no feature name`);
    if (!c.quote?.trim()) err(`${id}: no quote`);
    if (!c.url?.startsWith('https://')) err(`${id}: url must start with https://`);
    if (!SOURCE_TYPES.includes(c.sourceType)) err(`${id}: sourceType "${c.sourceType}" not in ${SOURCE_TYPES.join('|')}`);
    if (c.date != null && !isDate(c.date)) err(`${id}: date must be YYYY-MM-DD or null`);
    claimByKey.set(claimKey(app, `${prefix}${i}`), c);
  });
  for (const r of d.removed ?? []) if (!r.feature || !r.quote || !r.url) err(`${at}: removed items need {feature, quote, url}`);
  claims[app] = (claims[app] ?? 0) + d.claims.length;
}
for (const app of apps) loadClaims(`${app.id}.json`, app.id, '');
loadClaims('splyt-index.json', 'splyt', 'i');
const claimFiles = new Set(fs.readdirSync(path.join(ROOT, 'data/claims')).filter((f) => f.endsWith('.json')));
for (const f of claimFiles) if (f !== 'splyt-index.json' && !appIds.has(f.replace(/\.json$/, ''))) err(`claims/${f}: not an app in apps.json`);

// ---- features.json
const features = readJson('data/features.json');
if (!Array.isArray(features)) err('features.json must be an array');
const featIds = new Set();
const categories = new Set();
for (const f of features) {
  if (!/^[a-z0-9][a-z0-9-]*$/.test(f.id)) err(`features: bad id "${f.id}" (lowercase, digits and hyphens)`);
  if (featIds.has(f.id)) err(`features: duplicate id "${f.id}"`);
  featIds.add(f.id);
  if (!f.name?.trim()) err(`features: ${f.id} has no name`);
  if (!f.definition?.trim()) err(`features: ${f.id} has no definition`);
  if (!f.category?.trim()) err(`features: ${f.id} has no category`);
  categories.add(f.category);
  if (!Array.isArray(f.aspects)) err(`features: ${f.id} aspects must be an array`);
  for (const [k, list] of [...Object.entries(f.members ?? {}), ...Object.entries(f.alsoEvidencedBy ?? {})]) {
    if (!appIds.has(k)) { err(`features: ${f.id} lists claims for unknown app "${k}"`); continue; }
    for (const idx of list) if (!claimByKey.has(claimKey(k, idx))) err(`features: ${f.id} refers to claim ${k}:${idx}, which does not exist`);
  }
  if (!Object.keys(f.members ?? {}).length && !Object.keys(f.alsoEvidencedBy ?? {}).length) err(`features: ${f.id} has no claims behind it`);
  if (f.firstDocumented && (!appIds.has(f.firstDocumented.app) || !isDate(f.firstDocumented.date))) err(`features: ${f.id} firstDocumented needs a known app and a YYYY-MM-DD date`);
}

// ---- matrix.json
const m = readJson('data/matrix.json');
let inAppCitations = 0;
for (const fid of Object.keys(m)) if (!featIds.has(fid)) err(`matrix: unknown feature id "${fid}"`);
for (const fid of featIds) {
  const row = m[fid];
  if (!row) { err(`matrix: feature "${fid}" is missing`); continue; }
  for (const k of Object.keys(row)) if (!appIds.has(k)) err(`matrix: ${fid} has unknown app "${k}"`);
  for (const app of apps) {
    const c = row[app.id];
    const at = `matrix: ${fid} / ${app.id}`;
    if (!c) { err(`${at} is missing`); continue; }
    for (const k of CELL_KEYS) if (!(k in c)) err(`${at} has no "${k}" field`);
    for (const k of Object.keys(c)) if (!CELL_KEYS.includes(k)) err(`${at} has an unexpected field "${k}"`);
    if (!VALUES.includes(c.value)) err(`${at} value "${c.value}" not in ${VALUES.join('|')}`);
    if (c.date != null && !isDate(c.date)) err(`${at} date must be YYYY-MM-DD or null`);
    if (c.claim != null) {
      const cl = claimByKey.get(c.claim);
      if (!c.claim.startsWith(`${app.id}:`)) err(`${at} cites another app's claim ${c.claim}`);
      else if (!cl) err(`${at} cites claim ${c.claim}, which does not exist`);
      else if (cl.quote !== c.quote || cl.url !== c.url || cl.sourceType !== c.sourceType) err(`${at} quote/url/sourceType do not match claim ${c.claim}`);
    }
    if (c.value === 'unknown') continue;
    // yes / partial / no: every app, SPLYT included, needs a source URL and a quote.
    if (!c.quote?.trim()) err(`${at} is "${c.value}" but has no quote`);
    if (!SOURCE_TYPES.includes(c.sourceType)) err(`${at} sourceType "${c.sourceType}" not in ${SOURCE_TYPES.join('|')}`);
    if (c.value !== 'yes' && !c.note?.trim()) err(`${at} is "${c.value}" but has no note saying why`);
    if (!c.url) { err(`${at} is "${c.value}" but has no source URL`); continue; }
    if (app.publisher && IN_APP_WHATS_NEW.test(c.url)) { inAppCitations++; continue; }
    let u;
    try { u = new URL(c.url); } catch { err(`${at} source is not a URL: ${c.url}`); continue; }
    if (/\s/.test(c.url)) { err(`${at} source is not a URL: ${c.url}`); continue; }
    if (u.protocol !== 'https:') err(`${at} source must be https: ${c.url}`);
    const host = u.hostname;
    const ok = [...officialFor(app)].some((d) => host === d || host.endsWith(`.${d}`));
    if (!ok) warn(`${at} source is not on an official domain (${host}) — see METHODOLOGY.md, section 2.1`);
  }
}
if (inAppCitations) warn(`matrix: ${inAppCitations} SPLYT cell(s) cite SPLYT's in-app What's New screen (readable in the app, not on the web) — see METHODOLOGY.md`);

// ---- vetting.json: every claim classified exactly once; nothing left unplaced
const vetting = readJson('data/vetting.json');
const vetted = new Set();
for (const v of vetting) {
  const k = claimKey(v.app, v.claimIndex);
  const at = `vetting: ${k}`;
  if (!claimByKey.has(k)) { err(`${at} is not a claim in data/claims`); continue; }
  if (vetted.has(k)) err(`${at} is classified twice`);
  vetted.add(k);
  if (!CLASSES.includes(v.class)) err(`${at} class "${v.class}" not in ${CLASSES.join('|')}${v.class === 'unplaced' ? ' — the claim was never mapped (tooling/merge/mapping.py)' : ''}`);
  if (!v.reason?.trim()) err(`${at} (${v.class}) has no reason`);
  if (v.mappedTo != null && !featIds.has(v.mappedTo)) err(`${at} is mapped to unknown feature "${v.mappedTo}"`);
  for (const x of v.alsoEvidences ?? []) if (!featIds.has(x)) err(`${at} also evidences unknown feature "${x}"`);
  if (v.feature !== claimByKey.get(k).feature) err(`${at} feature name does not match the claim file`);
}
for (const k of claimByKey.keys()) if (!vetted.has(k)) err(`vetting: claim ${k} has not been classified (unmapped)`);

// ---- scores.json agrees with the matrix
const scores = readJson('data/scores.json');
if (scores.totalFeatures !== featIds.size) err(`scores: totalFeatures ${scores.totalFeatures} ≠ ${featIds.size} features`);
for (const app of apps) {
  const s = scores.apps?.[app.id];
  if (!s) { err(`scores: ${app.id} is missing`); continue; }
  for (const v of VALUES) {
    const n = [...featIds].filter((fid) => m[fid]?.[app.id]?.value === v).length;
    if (s[v] !== n) err(`scores: ${app.id} ${v} is ${s[v]}, matrix gives ${n} — run npm run build:matrix`);
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
console.log(`\n${errors.length} error(s), ${warnings.length} warning(s) — ${featIds.size} features × ${apps.length} apps, ${claimByKey.size} claims checked.`);
process.exit(fail ? 1 : 0);
