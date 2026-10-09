import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';
import { computePace } from '../scripts/compute-pace.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = (rel) => JSON.parse(fs.readFileSync(path.join(ROOT, rel), 'utf8'));
const apps = read('data/apps.json').apps.map((a) => a.id);
const features = read('data/features.json');
const matrix = read('data/matrix.json');
const vetting = read('data/vetting.json');
const scores = read('data/scores.json');

test('the published data passes validation', () => {
  // Throws (and fails the test) on a non-zero exit.
  execFileSync(process.execPath, ['scripts/validate.mjs'], { cwd: ROOT, stdio: 'pipe' });
});

test('every feature has a cell for every app, and every cell has the full schema', () => {
  const keys = ['value', 'quote', 'url', 'sourceType', 'date', 'note', 'claim'].sort();
  assert.deepEqual(Object.keys(matrix).sort(), features.map((f) => f.id).sort());
  for (const f of features) {
    assert.deepEqual(Object.keys(matrix[f.id]).sort(), [...apps].sort(), f.id);
    for (const a of apps) assert.deepEqual(Object.keys(matrix[f.id][a]).sort(), keys, `${f.id}/${a}`);
  }
});

test('every yes/partial/no, SPLYT included, carries a source URL and a quote', () => {
  for (const [fid, row] of Object.entries(matrix)) {
    for (const [a, c] of Object.entries(row)) {
      if (c.value === 'unknown') continue;
      assert.ok(c.url?.startsWith('https://'), `${fid}/${a} has no https source`);
      assert.ok(c.quote?.trim(), `${fid}/${a} has no quote`);
    }
  }
});

test('every claim is classified once, and every claim not counted says why', () => {
  const counted = new Set(['capability', 'aspect']);
  const n = apps.reduce((s, a) => s + read(`data/claims/${a}.json`).claims.length, 0) + read('data/claims/splyt-index.json').claims.length;
  assert.equal(vetting.length, n);
  assert.equal(new Set(vetting.map((v) => `${v.app}:${v.claimIndex}`)).size, n);
  for (const v of vetting) {
    assert.notEqual(v.class, 'unplaced', `${v.app}:${v.claimIndex} is unmapped`);
    if (!counted.has(v.class)) assert.ok(v.reason?.trim(), `${v.app}:${v.claimIndex} (${v.class}) has no reason`);
  }
});

test('scores.json matches the matrix', () => {
  assert.equal(scores.totalFeatures, features.length);
  for (const a of apps) {
    const yes = Object.values(matrix).filter((row) => row[a].value === 'yes').length;
    assert.equal(scores.apps[a].yes, yes, a);
    assert.equal(scores.apps[a].yesPct, Math.round((1000 * yes) / features.length) / 10, a);
  }
});

test('the pace scoreboard can be recomputed from the release files alone', () => {
  const pace = computePace({ from: '2026-08-24', to: '2026-10-08' });
  assert.ok(pace && typeof pace === 'object');
});
