// Shared helpers for the scripts in this folder. Node 20+, no dependencies.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const DATA = path.join(ROOT, 'data');

export function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, rel), 'utf8'));
}

export function readJsonIfExists(rel) {
  const p = path.join(ROOT, rel);
  return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, 'utf8')) : null;
}

export function writeJson(rel, obj) {
  const p = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(obj, null, 2) + '\n');
}

/** The file as it was in the last commit, or null (not committed / not a git checkout). */
export function readJsonAtHead(rel) {
  try {
    const out = execFileSync('git', ['show', `HEAD:${rel}`], { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], maxBuffer: 64 * 1024 * 1024 });
    return JSON.parse(out);
  } catch {
    return null;
  }
}

/** Today's date as YYYY-MM-DD in UTC (all dates in this repo are UTC). */
export function today() {
  return new Date().toISOString().slice(0, 10);
}

export function loadApps() {
  return readJson('data/apps.json').apps;
}

/** Parse `--key value` and `--flag` arguments. */
export function args(argv = process.argv.slice(2)) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith('--')) continue;
    const key = a.slice(2);
    const next = argv[i + 1];
    if (next === undefined || next.startsWith('--')) out[key] = true;
    else { out[key] = next; i++; }
  }
  return out;
}

/** Restrict an app list with --app hevy,strong when given. */
export function selectApps(apps, opt) {
  if (!opt.app) return apps;
  const want = String(opt.app).split(',');
  const unknown = want.filter((w) => !apps.some((a) => a.id === w));
  if (unknown.length) throw new Error(`unknown app id(s): ${unknown.join(', ')}`);
  return apps.filter((a) => want.includes(a.id));
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/** GET with a browser-like UA, a timeout and a few retries. Returns the body text. */
export async function get(url, { tries = 3, timeoutMs = 30000 } = {}) {
  let last;
  for (let i = 1; i <= tries; i++) {
    try {
      const res = await fetch(url, {
        headers: {
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
          'accept-language': 'en-US,en;q=0.9',
        },
        redirect: 'follow',
        signal: AbortSignal.timeout(timeoutMs),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
      return await res.text();
    } catch (e) {
      last = e;
      if (i < tries) await sleep(1500 * i);
    }
  }
  throw last;
}

export const pause = sleep;

/** Release notes that name nothing: only boilerplate like "Bug fixes and improvements". */
export function isGeneric(notes) {
  if (!notes || !notes.trim()) return true;
  const text = notes
    .toLowerCase()
    .replace(/release notes for [\d.]+/g, ' ')
    .replace(/version [\d.]+/g, ' ')
    .replace(/what's new in this update:?/g, ' ')
    .replace(/as always, if you have any feedback or issues please let us know:?\s*\S+@\S+/g, ' ')
    .replace(/[^a-z\s]/g, ' ');
  const BOILERPLATE = new Set(
    ('a an and the to of on in for with our we us this that it is are has have been be ' +
      'bug bugs fix fixes fixed minor small general various other additional ' +
      'performance improvement improvements improve improved enhancement enhancements stability stable ' +
      'latest versions version ios watchos ipados update updates updated contains internal backend ' +
      'help page load speed speeds tweaks polish squashed boost got were app experience thanks using')
      .split(' '),
  );
  const words = text.split(/\s+/).filter(Boolean);
  return words.length > 0 && words.every((w) => BOILERPLATE.has(w));
}

export function normalizeNotes(s) {
  return String(s || '').replace(/\r\n/g, '\n').trim();
}
