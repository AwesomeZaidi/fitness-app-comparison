#!/usr/bin/env node
// Summarise what the fetch scripts changed since the last commit, as Markdown
// for a pull-request body.
//
//   node scripts/diff-report.mjs                       # print to stdout
//   node scripts/diff-report.mjs --out report.md
//   node scripts/diff-report.mjs --validation v.txt    # append validate.mjs output
//
// "Before" is the committed version of each file (git HEAD). Snapshots are
// compared with the app's previous snapshot.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { ROOT, loadApps, readJsonIfExists, readJsonAtHead, args, today } from './lib.mjs';

const opt = args();
const apps = loadApps();
const out = [];
const p = (s = '') => out.push(s);
const quote = (s) => (s?.trim() ? s.trim().split('\n').map((l) => `> ${l}`).join('\n') : '> _(no notes)_');

function trackedAtHead(dir) {
  try {
    return new Set(execFileSync('git', ['ls-tree', '-r', '--name-only', 'HEAD', dir], { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).split('\n').filter(Boolean));
  } catch {
    return null;
  }
}

/** Minimal line diff (LCS). Returns lines prefixed with "+ ", "- " or "  ". */
function lineDiff(a, b) {
  const A = (a ?? '').split('\n'), B = (b ?? '').split('\n');
  const n = A.length, m = B.length;
  const L = Array.from({ length: n + 1 }, () => new Uint32Array(m + 1));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) L[i][j] = A[i] === B[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
  const res = [];
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (A[i] === B[j]) { res.push(`  ${A[i]}`); i++; j++; }
    else if (L[i + 1][j] >= L[i][j + 1]) res.push(`- ${A[i++]}`);
    else res.push(`+ ${B[j++]}`);
  }
  while (i < n) res.push(`- ${A[i++]}`);
  while (j < m) res.push(`+ ${B[j++]}`);
  return res.filter((l) => !l.startsWith('  ') || l.trim()); // keep context lines that have text
}

p(`# Weekly refresh — ${today()}`);
p();
p('Automated fetch of App Store release history and listings. **Nothing here changes the feature matrix.** A person reviews this PR, classifies any new releases, and decides whether any matrix cell needs a correction (with a source) before merging.');
p();

// ---- releases
let newCount = 0, pendingCount = 0;
const relSections = [];
for (const app of apps) {
  const now = readJsonIfExists(`data/releases/${app.id}.json`);
  if (!now) continue;
  const before = readJsonAtHead(`data/releases/${app.id}.json`);
  const had = new Map((before?.releases ?? []).map((r) => [r.version, r]));
  const added = now.releases.filter((r) => !had.has(r.version));
  const changed = now.releases.filter((r) => had.has(r.version) && had.get(r.version).notes !== r.notes);
  if (!added.length && !changed.length) continue;
  const lines = [`### ${app.name}`, ''];
  for (const r of added) {
    newCount++;
    let status;
    if (app.paceSource !== 'app-store') status = 'not classified (this app’s scoreboard uses its in-app What’s New)';
    else if (r.repeatsPreviousNotes) status = 'auto: repeats the previous release’s notes — adds nothing';
    else if (r.generic) status = 'auto: boilerplate — names nothing';
    else if (r.features === null) { status = '**needs review** — list named new features in `features`, fixes/speed-ups in `notCounted`'; pendingCount++; }
    else status = `${r.features.length} feature(s)`;
    lines.push(`**${r.version}** — ${r.date} — ${status}`, '', quote(r.notes), '');
  }
  for (const r of changed) {
    lines.push(`**${r.version}** — notes changed since last commit`, '', '```diff', ...lineDiff(had.get(r.version).notes, r.notes), '```', '');
  }
  relSections.push(...lines);
}
p('## New App Store releases');
p();
if (relSections.length) relSections.forEach((l) => p(l));
else p('None since the last commit.'), p();

// ---- snapshots
const tracked = trackedAtHead('data/snapshots');
const snapSections = [];
for (const app of apps) {
  const dir = path.join(ROOT, 'data/snapshots', app.id);
  if (!fs.existsSync(dir)) continue;
  const files = fs.readdirSync(dir).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort();
  const rel = (f) => `data/snapshots/${app.id}/${f}`;
  const fresh = files.filter((f) => (tracked ? !tracked.has(rel(f)) : f.startsWith(today())));
  for (const f of fresh) {
    const cur = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')).listing;
    const prevFile = files.filter((x) => x < f).at(-1);
    const prev = prevFile ? JSON.parse(fs.readFileSync(path.join(dir, prevFile), 'utf8')).listing : null;
    const lines = [`### ${app.name} — ${f.slice(0, 10)}${prev ? ` (vs ${prevFile.slice(0, 10)})` : ' (first snapshot)'}`, ''];
    if (!prev) { lines.push(`Version ${cur.version}, released ${cur.currentVersionReleaseDate?.slice(0, 10)}.`, ''); snapSections.push(...lines); continue; }
    for (const k of ['trackName', 'artistName', 'sellerUrl', 'version', 'currentVersionReleaseDate', 'formattedPrice', 'minimumOsVersion', 'contentAdvisoryRating']) {
      if (JSON.stringify(prev[k]) !== JSON.stringify(cur[k])) lines.push(`- **${k}**: ${prev[k] ?? '—'} → ${cur[k] ?? '—'}`);
    }
    if (JSON.stringify(prev.genres) !== JSON.stringify(cur.genres)) lines.push(`- **genres**: ${prev.genres?.join(', ')} → ${cur.genres?.join(', ')}`);
    if (prev.releaseNotes !== cur.releaseNotes) lines.push('', '**Release notes now:**', '', quote(cur.releaseNotes));
    if (prev.description !== cur.description) {
      lines.push('', '<details><summary><b>Description changed</b> — check whether any matrix cell cites it</summary>', '', '```diff', ...lineDiff(prev.description, cur.description), '```', '</details>');
    }
    lines.push('');
    snapSections.push(...lines);
  }
}
p('## App Store listing changes');
p();
if (snapSections.length) snapSections.forEach((l) => p(l));
else p('None since the last commit.'), p();

// ---- scoreboard
const paceNow = readJsonIfExists('data/pace.json');
const paceBefore = readJsonAtHead('data/pace.json');
if (paceNow) {
  p(`## Scoreboard (${paceNow.window.from} → ${paceNow.window.to})`);
  p();
  p('| App | Before | Now | Awaiting review | Basis |');
  p('|---|---:|---:|---:|---|');
  for (const r of paceNow.apps) {
    const b = paceBefore?.apps?.find((x) => x.app === r.app);
    p(`| ${r.name} | ${b ? b.newFeatures : '—'} | ${r.newFeatures} | ${r.pendingReview.length} | ${r.basis} |`);
  }
  p();
  if (paceBefore && paceBefore.window.to !== paceNow.window.to) p(`_Window end moved from ${paceBefore.window.to} to ${paceNow.window.to}._`), p();
}

// ---- validation
if (opt.validation && fs.existsSync(opt.validation)) {
  p('## Validation');
  p();
  p('```');
  p(fs.readFileSync(opt.validation, 'utf8').trim());
  p('```');
  p();
}

p('## Reviewer checklist');
p();
p(`- [ ] ${pendingCount ? `Classify the ${pendingCount} release(s) marked **needs review** (edit \`data/releases/<app>.json\`, set \`classifiedBy: "human"\`), then run \`node scripts/compute-pace.mjs\`.` : 'No releases need classifying.'}`);
p('- [ ] If a release or description adds or removes a compared feature, open a correction (with a source) rather than editing the matrix in this PR.');
p('- [ ] `node scripts/validate.mjs` passes.');
p();
p(`<sub>${newCount} new release(s), ${snapSections.length ? 'listing changes found' : 'no listing changes'}. Generated by scripts/diff-report.mjs.</sub>`);

const md = out.join('\n') + '\n';
if (opt.out) fs.writeFileSync(path.resolve(opt.out), md);
else process.stdout.write(md);
