#!/usr/bin/env python3
"""Deterministic build of the canonical feature list, scoring matrix, vetting and logs.

Inputs : data/claims/<app>.json, data/claims/splyt-index.json, tooling/merge/mapping.py (hand judgements)
Outputs: data/{features,matrix,scores,vetting}.json, data/scores.md, MERGE-LOG.md
Run    : python3 tooling/merge/build.py   (from anywhere; paths are relative to the repository root)
         npm run build:matrix              (same thing)

Exits non-zero if the mapping has errors (out-of-range or double-mapped claims) or any claim is left
unplaced. The Check workflow re-runs this and fails if the committed outputs differ from the rebuild.
"""
import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True  # keep tooling/merge free of __pycache__
sys.path.insert(0, HERE)
import mapping as M  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
CLAIMS = os.path.join(ROOT, "data", "claims")
OUT = os.path.join(ROOT, "data")
APPS = ["splyt", "hevy", "strong", "gravl", "fitbod", "motra"]
NAMES = dict(splyt="SPLYT", hevy="Hevy", strong="Strong", gravl="Gravl", fitbod="Fitbod", motra="Motra")
SPLYT_OFFSET = 247
COUNTED = {"capability", "aspect"}
SRC_RANK = {"help_centre": 0, "release_notes": 1, "website": 2, "app_store": 3, "google_play": 4}

# ------------------------------------------------------------------ load claims
claims, removed = {}, {}
for a in APPS:
    d = json.load(open(os.path.join(CLAIMS, f"{a}.json"), encoding="utf-8"))
    cl = d["claims"]
    if a == "splyt":
        assert len(cl) == SPLYT_OFFSET, len(cl)
        idx = json.load(open(os.path.join(CLAIMS, "splyt-index.json"), encoding="utf-8"))["claims"]
        cl = cl + idx
    claims[a] = cl
    removed[a] = d.get("removed", [])


def key(tok):
    """'i12' -> 259 for SPLYT index; '12' -> 12."""
    return SPLYT_OFFSET + int(tok[1:]) if tok.startswith("i") else int(tok)


def label(a, i):
    if a == "splyt" and i >= SPLYT_OFFSET:
        return f"i{i - SPLYT_OFFSET}"
    return str(i)


# ------------------------------------------------------------------ parse mapping
primary = {a: {} for a in APPS}     # claim -> (featureId, role core|aspect)
also = {a: collections.defaultdict(list) for a in APPS}
members = {}
errors = []
for f in M.FEATURES:
    mem = {}
    for a in APPS:
        lst = []
        for tok in f["tok"][a].split():
            role = "core"
            if tok[0] == "a":
                role, tok = "aspect", tok[1:]
            elif tok[0] == "x":
                role, tok = "also", tok[1:]
            i = key(tok)
            if i >= len(claims[a]):
                errors.append(f"{a}:{tok} out of range in {f['id']}")
                continue
            if role == "also":
                also[a][i].append(f["id"])
            else:
                if i in primary[a]:
                    errors.append(f"{a}:{tok} mapped twice: {primary[a][i][0]} and {f['id']}")
                primary[a][i] = (f["id"], role)
            lst.append((i, role))
        mem[a] = lst
    members[f["id"]] = mem

vet_over = {}
for a, tok, cls, why in M.VET:
    vet_over[(a, key(tok))] = (cls, why)
unattached = {a: {key(t) for t in M.UNATTACHED.get(a, [])} for a in APPS}

# ------------------------------------------------------------------ vetting
vetting, unmapped = [], []
for a in APPS:
    for i, c in enumerate(claims[a]):
        role = primary[a].get(i, (None, None))[1]
        fid = primary[a].get(i, (None, None))[0]
        if (a, i) in vet_over:
            cls, why = vet_over[(a, i)]
        elif role == "core":
            cls, why = "capability", "Quote describes the capability."
        elif role == "aspect":
            cls, why = "aspect", f"A setting or variant of '{fid}'; shown as an aspect, not scored on its own."
        elif i in also[a]:
            cls, why = "capability", "Evidence for: " + ", ".join(also[a][i])
        else:
            cls, why = None, None
        if fid is None and not also[a].get(i) and i not in unattached[a]:
            unmapped.append(dict(app=a, claimIndex=label(a, i), feature=c["feature"], why="not placed"))
        if cls is None:
            cls, why = "unplaced", "not placed"
        src = "data/claims/splyt-index.json" if (a == "splyt" and i >= SPLYT_OFFSET) else f"data/claims/{a}.json"
        vetting.append(dict(app=a, claimIndex=label(a, i), sourceFile=src, feature=c["feature"],
                            mappedTo=fid, alsoEvidences=also[a].get(i, []), role=role, **{"class": cls}, reason=why))
cls_of = {(v["app"], v["claimIndex"]): v["class"] for v in vetting}


def claim_cls(a, i):
    return cls_of[(a, label(a, i))]


# ------------------------------------------------------------------ scoring
def evidence(a, i):
    c = claims[a][i]
    return dict(quote=c["quote"], url=c["url"], sourceType=c["sourceType"], date=c.get("date"),
                claim=f"{a}:{label(a, i)}")


def candidates(fid, a):
    out = []
    for i, role in members[fid][a]:
        out.append((i, role))
    for i, fl in also[a].items():
        if fid in fl:
            out.append((i, "also"))
    return out


ROLE_RANK = {"core": 0, "aspect": 1, "also": 2}


def best(cands):
    return sorted(cands, key=lambda t: (ROLE_RANK[t[1]], SRC_RANK.get(claims[t[2]][t[0]]["sourceType"], 9),
                                        -len(claims[t[2]][t[0]]["quote"])))[0]


matrix, cellnotes = {}, []
for f in M.FEATURES:
    fid = f["id"]
    matrix[fid] = {}
    for a in APPS:
        cands = [(i, r, a) for i, r in candidates(fid, a)]
        counted = [t for t in cands if claim_cls(a, t[0]) in COUNTED]
        ns = [t for t in cands if claim_cls(a, t[0]) == "not_shipped"]
        uns = [t for t in cands if claim_cls(a, t[0]) == "unsubstantiated"]
        rej = [t for t in cands if claim_cls(a, t[0]) in ("fix", "ui_tweak", "vague", "out_of_scope")]
        cell = dict(value="unknown", quote=None, url=None, sourceType=None, date=None, note=None, claim=None)
        if counted:
            b = best(counted)
            cell.update(value="yes", **evidence(a, b[0]))
            if b[1] != "core":
                cell["note"] = ("Evidenced by a claim mapped as an aspect of this feature." if b[1] == "aspect"
                                else f"Evidenced by a claim mapped primarily to '{primary[a].get(b[0], ('?',))[0]}'.")
        elif ns:
            b = best(ns)
            cell.update(value="partial", **evidence(a, b[0]))
            cell["note"] = "Not fully shipped: " + vet_over.get((a, b[0]), ("", ""))[1]
        elif uns:
            b = best(uns)
            cell.update(value="unknown", **evidence(a, b[0]))
            cell["note"] = "Claim not counted (unsubstantiated): " + vet_over.get((a, b[0]), ("", ""))[1]
        elif rej:
            b = best(rej)
            cell.update(value="unknown", **evidence(a, b[0]))
            cell["note"] = f"Only claim was rejected as {claim_cls(a, b[0])}: " + vet_over.get((a, b[0]), ("", ""))[1]
        naive = "yes" if cands else "unknown"
        if (fid, a) in M.OVERRIDES:
            v, note, ev = M.OVERRIDES[(fid, a)]
            cell["value"], cell["note"] = v, note
            if ev:
                cell.update(ev); cell["claim"] = None
            cellnotes.append((fid, a, v, note))
        cell["naive"] = naive
        matrix[fid][a] = cell

# ------------------------------------------------------------------ features.json
features_out = []
for f in M.FEATURES:
    fid = f["id"]
    aspects, dated = [], []
    for a in APPS:
        for i, role in candidates(fid, a):
            c = claims[a][i]
            if claim_cls(a, i) not in COUNTED:
                continue
            if role == "aspect":
                aspects.append(c["feature"])
            if c.get("date"):
                dated.append((c["date"], a, c["url"]))
    seen, asp = set(), []
    for x in aspects:
        if x.lower() not in seen:
            seen.add(x.lower()); asp.append(x)
    fd = min(dated) if dated else None
    features_out.append(dict(
        id=fid, name=f["name"], definition=f["definition"], category=M.CATEGORIES[f["cat"]],
        aspects=asp,
        firstDocumented=dict(app=fd[1], date=fd[0], url=fd[2]) if fd else None,
        members={a: [label(a, i) for i, r in members[fid][a]] for a in APPS if members[fid][a]},
        alsoEvidencedBy={a: list(dict.fromkeys(label(a, i) for i, r in candidates(fid, a) if r == "also")) for a in APPS
                         if any(r == "also" for _, r in candidates(fid, a))},
    ))

# ------------------------------------------------------------------ scores
cats = list(dict.fromkeys(M.CATEGORIES[f["cat"]] for f in M.FEATURES))
total = len(M.FEATURES)
scores = {"totalFeatures": total, "apps": {}, "categories": {}}
for a in APPS:
    vals = collections.Counter(matrix[f["id"]][a]["value"] for f in M.FEATURES)
    only, lacks = [], []
    for f in M.FEATURES:
        row = matrix[f["id"]]
        others = [row[o]["value"] for o in APPS if o != a]
        if row[a]["value"] == "yes" and all(v in ("no", "unknown") for v in others):
            only.append(f["id"])
        if row[a]["value"] in ("no", "unknown") and all(v == "yes" for v in others):
            lacks.append(f["id"])
    scores["apps"][a] = dict(yes=vals["yes"], yesPct=round(100 * vals["yes"] / total, 1), partial=vals["partial"],
                             no=vals["no"], unknown=vals["unknown"], onlyThisApp=only, onlyThisAppLacks=lacks)
for c in cats:
    fs = [f for f in M.FEATURES if M.CATEGORIES[f["cat"]] == c]
    scores["categories"][c] = dict(features=len(fs), yes={a: sum(matrix[f["id"]][a]["value"] == "yes" for f in fs) for a in APPS},
                                   partial={a: sum(matrix[f["id"]][a]["value"] == "partial" for f in fs) for a in APPS})
# vetting summary
vs = {}
for a in APPS:
    cnt = collections.Counter(v["class"] for v in vetting if v["app"] == a)
    vs[a] = dict(total=sum(cnt.values()), kept=cnt["capability"] + cnt["aspect"], **cnt)
scores["vetting"] = vs
# naive vs vetted differences
diffs = []
for f in M.FEATURES:
    for a in APPS:
        c = matrix[f["id"]][a]
        if c["naive"] != c["value"]:
            diffs.append(dict(feature=f["id"], app=a, naive=c["naive"], vetted=c["value"], note=c["note"]))
scores["vettingChangedValues"] = diffs

# ------------------------------------------------------------------ write json
for c in matrix.values():
    for cell in c.values():
        cell.pop("naive", None)
json.dump(features_out, open(os.path.join(OUT, "features.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(matrix, open(os.path.join(OUT, "matrix.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(scores, open(os.path.join(OUT, "scores.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(vetting, open(os.path.join(OUT, "vetting.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ scores.md
L = []
L.append(f"# Scores\n\n{total} canonical features. 'Yes' needs at least one counted claim from the app's own sources; "
         "'no' needs explicit own-source or store-listing evidence of absence; everything else is 'unknown' (unknown is not no).\n")
L.append("| App | Yes | % of all | Partial | No | Unknown |\n|---|---|---|---|---|---|")
for a in APPS:
    s = scores["apps"][a]
    L.append(f"| {NAMES[a]} | {s['yes']} | {s['yesPct']}% | {s['partial']} | {s['no']} | {s['unknown']} |")
L.append("\n## Yes count by category\n")
L.append("| Category | Features | " + " | ".join(NAMES[a] for a in APPS) + " |\n|---|---|" + "---|" * len(APPS))
for c in cats:
    s = scores["categories"][c]
    L.append(f"| {c} | {s['features']} | " + " | ".join(str(s["yes"][a]) + (f" (+{s['partial'][a]}p)" if s["partial"][a] else "") for a in APPS) + " |")
fname = {f["id"]: f["name"] for f in M.FEATURES}
L.append("\n## Features only one app has (yes for it; no/unknown for every other app)\n")
for a in APPS:
    s = scores["apps"][a]
    L.append(f"**{NAMES[a]}** ({len(s['onlyThisApp'])}): " + (", ".join(fname[x] for x in s["onlyThisApp"]) or "none"))
    L.append("")
L.append("\n## Features every other app has but this one does not (no/unknown here; yes for all five others)\n")
for a in APPS:
    s = scores["apps"][a]
    L.append(f"**{NAMES[a]}** ({len(s['onlyThisAppLacks'])}): " + (", ".join(fname[x] for x in s["onlyThisAppLacks"]) or "none"))
    L.append("")
L.append("\n## Claim vetting\n")
classes = ["capability", "aspect", "unsubstantiated", "not_shipped", "fix", "ui_tweak", "vague", "out_of_scope"]
L.append("| App | Claims | Kept (capability+aspect) | " + " | ".join(classes) + " |\n|---|---|---|" + "---|" * len(classes))
for a in APPS:
    v = vs[a]
    L.append(f"| {NAMES[a]} | {v['total']} | {v['kept']} | " + " | ".join(str(v.get(k, 0)) for k in classes) + " |")
open(os.path.join(OUT, "scores.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

# ------------------------------------------------------------------ merge-log.md
G = []
G.append(open(os.path.join(HERE, "merge-log-intro.md"), encoding="utf-8").read())
G.append("\n## Every canonical feature and what was merged into it\n")
G.append("Format: app — `claim-index` original claim name (role). Roles: core = scored member; aspect = a setting or "
         "variant shown under the feature; also = the claim belongs to another feature but its quote also proves this one. "
         "SPLYT indices starting with `i` come from the 2026-10-09 feature index. Claims marked ✗ were not counted (class in brackets).\n")
for c in cats:
    G.append(f"\n### {c}\n")
    for f in M.FEATURES:
        if M.CATEGORIES[f["cat"]] != c:
            continue
        fid = f["id"]
        vals = " · ".join(f"{NAMES[a]} {matrix[fid][a]['value']}" for a in APPS)
        G.append(f"#### {f['name']} (`{fid}`)\n{f['definition']}\n\n_Result:_ {vals}\n")
        for a in APPS:
            parts = []
            for i, role in candidates(fid, a):
                cl = claim_cls(a, i)
                mark = "" if cl in COUNTED else f" ✗ [{cl}]"
                parts.append(f"`{label(a, i)}` {claims[a][i]['feature']} ({role}){mark}")
            if parts:
                G.append(f"- **{NAMES[a]}**: " + "; ".join(parts))
        notes = [(a, matrix[fid][a]) for a in APPS if matrix[fid][a]["value"] in ("no", "partial") or (fid, a) in M.OVERRIDES]
        for a, cell in notes:
            if cell["note"]:
                G.append(f"- _Decision — {NAMES[a]} = {cell['value']}:_ {cell['note']}"
                         + (f" Source: {cell['url']}" if cell.get("url") else ""))
        G.append("")
G.append("\n## Claims we didn't count\n")
G.append("Every claim was classified (full list in `data/vetting.json`). Only `capability` and `aspect` claims can make a cell 'yes'. "
         "`not_shipped` can make it 'partial'. `unsubstantiated` never scores above 'unknown' unless other evidence exists, "
         "and `fix`, `ui_tweak`, `vague` and `out_of_scope` (pricing/tier limits) never count.\n")
for a in APPS:
    v = vs[a]
    rej = [x for x in vetting if x["app"] == a and x["class"] not in COUNTED]
    G.append(f"### {NAMES[a]}\n{v['total']} claims; kept {v['kept']}; not counted {len(rej)} — "
             + ", ".join(f"{k}: {v[k]}" for k in classes[2:] if v.get(k)) + "\n")
    for x in rej:
        G.append(f"- `{x['claimIndex']}` {x['feature']} — **{x['class']}**: {x['reason']}")
    G.append("")
G.append("\n## Where vetting changed a value compared with a naive mapping\n")
G.append("A naive mapping marks an app 'yes' whenever any claim of its maps to the feature. These cells differ:\n")
for d in diffs:
    G.append(f"- {fname[d['feature']]} — {NAMES[d['app']]}: naive {d['naive']} → **{d['vetted']}**. {d['note'] or ''}")
G.append("\n## Removed features\n")
for a in APPS:
    for r in removed[a]:
        G.append(f"- **{NAMES[a]}** — {r['feature']}: \"{r['quote']}\" ({r['url']}{', ' + r['date'] if r.get('date') else ''})")
G.append("\nHow they were used: SPLYT food logging → `nutrition-logging` = no. Fitbod offline video → `offline-videos` = no "
         "(GIF removal does not affect `exercise-demos`, which Fitbod still has as video). Fitbod Fitbit auto-posting → "
         "`fitbit` = partial. Removals of things no app still claims (SPLYT Bluetooth machine pairing, voice personas, "
         "hands-free voice chat, demo mode, watch tutorial; Hevy HevyGPT, Facebook sign-in, direct Google Fit; Strong "
         "direct MyFitnessPal, Google Fit; Gravl reset-all-weights, free colour picker; Fitbod per-session goal override) "
         "did not create features, because a feature only exists in this list if some app currently claims it.\n")
open(os.path.join(ROOT, "MERGE-LOG.md"), "w", encoding="utf-8").write("\n".join(G) + "\n")

print("features", total, "errors", len(errors), "unmapped", len(unmapped), "diffs", len(diffs))
for e in errors:
    print("ERR", e)
for u in unmapped:
    print("UNMAPPED", u)
if errors or unmapped:
    sys.exit(1)
