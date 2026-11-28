#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_concept_graph.py v1.0

Generates data/concept_graph_v1.0_<date>.json from concepts_v1.1.
Every edge has a rule provenance; no relationship is implied without an
explicit, documented rule. Known data fixes applied at graph level are
recorded in meta.fixes_applied.

Edge vocabulary (rule-based, curated):
  related      -> symmetrical edge "adjacent"      (both records name each other or one-sided mention kept one-sided, documented)
  contrast     -> directed edge "contrasts_with"
  variant      -> cluster: part_of_variant_of sub-records are NOT separate nodes;
                  they are collapsed into the base node with variant_count>1
  related dangle fix: c3_convergence_moments -> c3_moment (decision recorded in v0.x changelog, applied late; documented in meta.fixes_applied)

Deterministic layout: force simulation in the frontend uses seeded initial
positions (hash of node id), so the organic layout is reproducible.
"""
import json, hashlib, sys
from collections import defaultdict

SRC = "data/concepts_v1.1_2026-11-26.json"
OUT = sys.argv[1] if len(sys.argv) > 1 else "data/concept_graph_v1.0.json"

d = json.load(open(SRC, encoding="utf-8"))
recs = d["concepts"]
byid = {r["id"]: r for r in recs}

def rec_chapter(r):
    return int(r["id"].split("_")[0][1:])

def hpos(seed: str) -> float:
    """deterministic pseudo-position from id hash (stable across reloads)"""
    return int(hashlib.sha1(seed.encode()).hexdigest()[:8], 16)

# --- collapse variants ------------------------------------------------------
subs = [r for r in recs if r.get("part_of_variant_of")]
sub_ids = {r["id"] for r in subs}
clusters = defaultdict(list)
for r in subs:
    clusters[r["part_of_variant_of"]].append(r["id"])

visible = [r for r in recs if r["id"] not in sub_ids]

nodes = []
for r in visible:
    n = {
        "id": r["id"], "term": r["term"], "type": r["type"],
        "chapter": rec_chapter(r),
        "definition_pid": r.get("definition_pid"),
        "key_support_pids": r.get("key_support_pids", []),
        "summary": r.get("summary"),
        "editorial_status": r.get("editorial_status"),
    }
    if r["id"] in clusters:
        n["variant_cluster"] = {
            "base": r["id"],
            "members": clusters[r["id"]],
            "member_terms": [byid[m]["term"] for m in clusters[r["id"]]],
        }
    nodes.append(n)

node_ids = {n["id"] for n in nodes}

edges = []
edge_provenance = []

# --- rule 1: contrast -> contrasts_with ------------------------------------
for r in recs:
    for t in r.get("contrast", []):
        target = t
        if target not in byid:
            continue
        # if target collapsed into cluster, redirect to base
        if target in sub_ids:
            continue  # no contrast currently points at sub-records; kept for safety
        if r["id"] in sub_ids:
            src = r["part_of_variant_of"]  # variant member edges route through base
        else:
            src = r["id"]
        if src == target:
            continue
        edges.append({"source": src, "target": target, "kind": "contrasts_with"})
        edge_provenance.append({
            "rule": "contrast-field -> contrasts_with",
            "source_record": r["id"], "target_record": target,
        })

# --- rule 2: related -> adjacent -------------------------------------------
# The dangling ref c3_convergence_moments -> c3_moment is fixed at graph level
FIXES = [("c3_passage_of_nature", "c3_convergence_moments", "c3_moment")]
fix_map = {(s, f): t for s, f, t in FIXES}

seen = set()
for r in recs:
    if r["id"] in sub_ids:
        continue  # member edges suppressed: cluster lives inside base node
    for t in r.get("related", []):
        tgt = t
        key = (r["id"], t)
        if key in fix_map:
            tgt = fix_map[key]
            edge_provenance.append({
                "rule": "related-field -> adjacent (redirected dangling ref)",
                "source_record": r["id"], "raw_target": t, "applied_fix": tgt,
            })
        if tgt not in byid or tgt in sub_ids:
            if tgt not in byid:
                edge_provenance.append({
                    "rule": "related-field -> adjacent (SKIPPED dangling ref, kept in log)",
                    "source_record": r["id"], "raw_target": t,
                })
            continue
        e = tuple(sorted([r["id"], tgt]))
        if e in seen:
            continue
        seen.add(e)
        edges.append({"source": e[0], "target": e[1], "kind": "adjacent"})
        edge_provenance.append({
            "rule": "related-field -> adjacent",
            "source_record": r["id"], "target_record": tgt,
        })

# --- rule 3: cross-chapter edges flagged -----------------------------------
for e in edges:
    s_ch = rec_chapter(byid[e["source"]])
    t_ch = rec_chapter(byid[e["target"]])
    e["cross_chapter"] = s_ch != t_ch

# --- deterministic seeds for force layout ---------------------------------
for n in nodes:
    n["seed_x"] = (hpos(n["id"]) % 1000) / 1000.0
    n["seed_y"] = (hpos(n["id"] + "|y") % 1000) / 1000.0

graph = {
    "meta": {
        "generated_from": SRC,
        "generator": "tools/build_concept_graph.py v1.0",
        "generated_at": "2026-11-28",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "edge_vocabulary": {
            "adjacent": "symmetric; both concepts co-referenced in concepts records (related-field)",
            "contrasts_with": "directed; explicit contrast-field in concepts records",
        },
        "variant_clusters": {k: v for k, v in clusters.items()},
        "collapsed_nodes": sorted(sub_ids),
        "fixes_applied": [
            {"fix": "dangling related-ref redirected", "record": "c3_passage_of_nature",
             "from": "c3_convergence_moments", "to": "c3_moment",
             "provenance": "editorial decision recorded in concepts changelog v0.x; applied late to graph level"}
        ],
        "layout": "force-directed in frontend with deterministic seeds (seed_x/seed_y from sha1 of node id); organic but reproducible",
        "skipped_dangling_refs": [p for p in edge_provenance if "SKIPPED" in p["rule"]],
    },
    "nodes": nodes,
    "edges": edges,
    "edge_provenance": edge_provenance,
}

json.dump(graph, open(OUT, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"[OK] {OUT}: {len(nodes)} nodes, {len(edges)} edges "
      f"(adjacent={sum(1 for e in edges if e['kind']=='adjacent')}, "
      f"contrasts_with={sum(1 for e in edges if e['kind']=='contrasts_with')})")
print(f"     variant clusters: {list(clusters.keys())}")
print(f"     provenance entries: {len(edge_provenance)}")
