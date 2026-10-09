import { test } from 'node:test';
import assert from 'node:assert/strict';
import { isGeneric, normalizeNotes } from '../scripts/lib.mjs';

test('boilerplate release notes are recognised as naming nothing', () => {
  assert.equal(isGeneric('Bug fixes and improvements'), true);
  assert.equal(isGeneric('Bug fixes and performance improvements.'), true);
  assert.equal(isGeneric('New: Injuries — adapt your workouts based on training limitations.'), false);
});

test('notes are normalised without losing content', () => {
  const n = normalizeNotes('  Line one\r\n\r\n\r\nLine two  ');
  assert.match(n, /Line one/);
  assert.match(n, /Line two/);
  assert.doesNotMatch(n, /\r/);
});
