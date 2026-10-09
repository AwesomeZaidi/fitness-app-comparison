import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseVersionHistory } from '../scripts/fetch-releases.mjs';

const page = (data) => `<html><body><script type="application/json" id="serialized-server-data">${JSON.stringify(data)}</script></body></html>`;

test('reads the 2026 App Store page structure (TitledParagraph items)', () => {
  const html = page({
    data: [
      {
        shelf: 'versionHistory',
        items: [
          { $kind: 'TitledParagraph', text: 'New: Workout Focus.\nFixed a crash.', primarySubtitle: '1.53', secondarySubtitle: 'Sat Sep 26 2026 10:00:00 GMT+0000' },
          { $kind: 'TitledParagraph', text: 'Bug fixes', primarySubtitle: 'Version 1.52.1', secondarySubtitle: 'Fri Aug 28 2026 10:00:00 GMT+0000' },
        ],
      },
    ],
  });
  const rel = parseVersionHistory(html);
  const byVersion = Object.fromEntries(rel.map((r) => [r.version, r]));
  assert.equal(byVersion['1.53'].date, '2026-09-26');
  assert.match(byVersion['1.53'].notes, /Workout Focus/);
  assert.equal(byVersion['1.52.1'].date, '2026-08-28', 'the "Version " prefix is stripped');
});

test('falls back to the older versionDisplay / releaseDate fields', () => {
  const html = page({ versionHistory: [{ versionDisplay: '6.5.1', releaseDate: '2026-10-08T07:00:00Z', releaseNotes: 'Fix: sign-in' }] });
  const [r] = parseVersionHistory(html);
  assert.deepEqual([r.version, r.date], ['6.5.1', '2026-10-08']);
});

test('ignores entries without a parseable date', () => {
  const html = page({ versionHistory: [{ versionDisplay: '1.0', releaseDate: 'not a date', releaseNotes: 'x' }] });
  assert.equal(parseVersionHistory(html).length, 0);
});
