# Projektstand — Whitehead: The Concept of Nature (Interactive Edition)

**Version:** v0.5 · **Datum:** 2026-11-28 (Abend) · **Repo:** https://github.com/jonason92/whitehead-concept-of-nature · **Live:** https://editions.sajon.net (Custom Domain, HTTPS enforced)

## Meilensteine

1. **Datenmodell** (2026-11-25): 3 Layer — corpus / concepts / modules. pid-Schema `ch{n}-p{XXX}`.
2. **Korpus & Konzeptgraph-Daten** (2026-11-26): 464 Absätze, 9 Kapitel; concepts v1.1 (58 Records).
3. **Foundation-Repo öffentlich** (2026-11-26): Commit `48cb4df`. MIT + CC BY 4.0 + PD-Notice (PG #18835).
4. **Website geboren** (2026-11-27): Hub + Bifurkations-Explorer (`6644d93`).
5. **Vollausbau Module II–V + Corpus Reader** (2026-11-28): `875bc85`, `78d9124`, `6fbcd52`.
6. **Custom Domain + Root-Hosting** (2026-11-28): editions.sajon.net via CNAME (Infomaniak DNS), Site aus Repo-Root, `/src/` als Dev-Spiegel.
7. **Parser v1.2: Paginierung + Notes** (2026-11-28): orig_pages (178 Absätze), Notes als eigenständige Sektionen (note1 Greek Point, note2 Significance) — Korrektur der Missklassifikation als ch9-p024ff, ch9 endet bei p023, Migration via `former_ch9_pids` dokumentiert; Gesamtdeckung stabil 464 (458+6).
8. **Annotations-MVP im Reader** (2026-11-28): native Auswahl-Annotationen (Text+Tag), localStorage, JSON-Export/Import (`5d3a84e`).
9. **Konzeptgraph v1.0 online** (2026-11-28): Generator `tools/build_concept_graph.py` (regelbasierte Kanten mit Provenance, 105 Kanten/106 Einträge, Varianten-Cluster c1, dangling-ref-Fix c3 dokumentiert); Frontend D3 force, nach Iterationen: v1.0a CDN → v1.0b Hybrid-Kapitelbänder + Live-Sim + Drag + self-hosted D3 (vendor/) → v1.0c Drag-Bugfix (`4ca0ab7`).
10. **Proton-Drive Checkpoint 3** (2026-11-28): `/media/SajonGmbH/DATA/PROTON-DRIVE LOCAL/whitehead_checkpoint_2026-11-28/` inkl. SHA256SUMS.

## Editorisches Prinzip (neu, beschlossen 2026-11-28): „Vollzug vor Bestand"

Der Konzeptgraph ist als **Kartengerät** bewährt (Navigation, Zitierbarkeit, maschinenlesbare Struktur), aber ausdrücklich **kein Denkgerät**. Er visualisiert Bestand, nicht Vollzug — und wird deshalb nicht weiter ausgebaut. Priorität künftiger Arbeit: Visualisierungen des *Vollzugs* (Argumentations-Partituren, Konflikt-Karten, kuratierte Lese-Pfade). Die fünf interaktiven Module sind die proto-tauglicheren philosophischen Instrumente. — Angestoßen durch Kritik-Bemerkung des Projektleiters (jonah_Zen) im Arbeitschat.

## Offene intellektuelle Schuld (work in progress)

**[WIP]** Detaillierte Antwort von jonah_Zen auf die Design-Diskussion „Vollzug vor Bestand / fruchtbare Visualisierung philosophischer Texte" (Argumentations-Partituren, Konflikt-Karten, Lese-Pfade, Arbeitsgeräte-teilung als Differenzbegriff zur Arbeitsteilung) — **in Vorbereitung**, pledged im Chat, 2026-11-28. Wird bei Eingang in concepts v1.2 / modules v0.2 und ggf. als eigener Design-Text (docs/) eingearbeitet.

## Aktuelle Website (`/` Root; `src/` Dev-Spiegel)

| Seite | Funktion | Status |
|---|---|---|
| index.html | Hub, 7 Karten, bilingual | live |
| bifurcation.html | Modul I: Pole, Feuer-Kippstelle, Variant-Pfade | live |
| passage.html | Modul II: Dauer/Moment, Scholem-Randnotiz | live |
| abstraction.html | Modul III: Zoom, Greek-Point-Notiz | live |
| congruence.html | Modul IV: Axiome vs. Poincaré | live |
| ingression.html | Modul V: Blauer Mantel, Spiegeltest | live |
| reader.html | VI: Lesemodus, pid-Anker, Orig.-Seiten, Annotationen | live |
| graph.html | VII: Konzeptgraph (Kartengerät, s.o.) | live |

Infrastruktur: Vanilla HTML/CSS/JS; D3 self-hosted (vendor/d3.min.js); fetch() der Datenlayer aus `data/`; `data/concept_graph_v1.0.json` neu.

## Offene Arbeiten

- [ ] Eingang der WIP-Antwort (s.o.) → Design-Runde „fruchtbare Visualisierung"
- [ ] Konzeptgraph-Nutzung als Servicedienst einfrieren (kein weiterer Ausbau)
- [ ] concepts v1.2 / modules v0.2: Erweiterungen auf Basis der Design-Runde
- [ ] Parser v1.3: Titel-Kapitalisierung (Kosmetik), ggf. Index als Suchoption
- [ ] Zeno-Registrierungen für jonason92/Sajon-GmbH-Projekte (GitHub + Codeberg)
- [ ] Proton-Drive-Connector (geplant, ersetzt manuelle Checkpoints)

## Commits (Chronologie 2026-11-28)

`6fbcd52` Reader+Hub → `e23e6a5` docs v0.4 → `1eccaf9` CNAME → `50249b3` Root-Hosting → `8e0abfc` Parser v1.2 orig_pages → `b5ddd40` Notes als Sektionen → `5d3a84e` Annotations-MVP → `adef0c3` Graph v1.0a → `67c49a2` Graph v1.0b → `4ca0ab7` Graph v1.0c (Drag-Fix).
