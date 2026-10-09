// Exports the rankings published on https://splyt.fit/apps into
// data/rankings/<YYYY-MM-DD>.json, so any past list can be audited.
//
// Reads the same two public views the page reads (store_directory,
// store_history_span) with SPLYT's public anon key. The raw daily history
// behind them is not published — see RANKINGS.md.
//
//   SPLYT_SUPABASE_URL=… SPLYT_SUPABASE_ANON_KEY=… node scripts/export-rankings.mjs
import { mkdir, writeFile } from 'node:fs/promises';

const URL_ = process.env.SPLYT_SUPABASE_URL;
const KEY = process.env.SPLYT_SUPABASE_ANON_KEY;
if (!URL_ || !KEY) {
  console.log('export-rankings: SPLYT_SUPABASE_URL / SPLYT_SUPABASE_ANON_KEY not set — skipping.');
  process.exit(0);
}

const COLS = 'app_id,name,developer,kind,price,rating,rating_count,first_released,rank_free,rank_paid,rank_grossing,gained_7d,gained_30d,gained_365d';
const GYM = 'kind=eq.strength_gym';
const TRACKERS = 'kind=in.(strength_gym,general_workouts)';

async function get(path) {
  const res = await fetch(`${URL_}/rest/v1/${path}`, { headers: { apikey: KEY, Authorization: `Bearer ${KEY}` } });
  if (!res.ok) throw new Error(`${path}: HTTP ${res.status} ${await res.text()}`);
  return res.json();
}

const list = (filter, order, limit, extra = '') => get(`store_directory?select=${COLS}&${filter}${extra}&order=${order}&limit=${limit}`);

const [span] = await get('store_history_span?select=first_day,last_day,days');
const day = span.last_day;
const weekAgo = new Date(Date.parse(day) - 7 * 864e5).toISOString().slice(0, 10);

const out = {
  source: 'https://splyt.fit/apps',
  method: 'https://github.com/AwesomeZaidi/fitness-app-comparison/blob/main/RANKINGS.md',
  day,
  history: span,
  lists: {},
};
for (const [scope, filter] of [['gym_strength', GYM], ['all_trackers', TRACKERS]]) {
  out.lists[scope] = {
    today_free: await list(filter, 'rank_free.asc', 25, '&rank_free=not.is.null'),
    today_paid: await list(filter, 'rank_paid.asc', 25, '&rank_paid=not.is.null'),
    today_grossing: await list(filter, 'rank_grossing.asc', 25, '&rank_grossing=not.is.null'),
    all_time: await list(filter, 'rating_count.desc.nullslast', 50),
    week: span.days >= 8 ? await list(filter, 'gained_7d.desc.nullslast', 25, '&gained_7d=not.is.null') : null,
    month: span.days >= 31 ? await list(filter, 'gained_30d.desc.nullslast', 25, '&gained_30d=not.is.null') : null,
    year: span.days >= 366 ? await list(filter, 'gained_365d.desc.nullslast', 25, '&gained_365d=not.is.null') : null,
  };
}
out.new_this_week = await list(TRACKERS, 'first_released.desc', 100, `&first_released=gte.${weekAgo}`);

await mkdir('data/rankings', { recursive: true });
const file = `data/rankings/${day}.json`;
await writeFile(file, JSON.stringify(out, null, 2) + '\n');
console.log(`export-rankings: wrote ${file} (history ${span.days} day(s), ${out.new_this_week.length} new this week)`);
