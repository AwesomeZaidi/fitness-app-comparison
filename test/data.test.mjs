import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { computePace } from '../scripts/compute-pace.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

test('the published data passes validation', () => {
  // Throws (and fails the test) on a non-zero exit.
  execFileSync(process.execPath, ['scripts/validate.mjs'], { cwd: ROOT, stdio: 'pipe' });
});

test('the pace scoreboard can be recomputed from the release files alone', () => {
  const pace = computePace({ from: '2026-08-24', to: '2026-10-08' });
  assert.ok(pace && typeof pace === 'object');
});
