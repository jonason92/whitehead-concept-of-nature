# Projektstand — Whitehead: The Concept of Nature (Interactive Edition)

**Version:** v0.4 · **Datum:** 2026-11-28 · **Repo:** https://github.com/jonason92/whitehead-concept-of-nature

## Meilensteine

1. **Datenmodell** (2026-11-25): 3 Layer — corpus / concepts / modules. pid-Schema `ch{n}-p{XXX}`.
2. **Korpus & Konzeptgraph** (2026-11-26): 464 Absätze, 9 Kapitel; concepts v1.1 (58 Records, Typologie thesis/method/entity/relation/principle(+distinction), Varianten-Mechanik `part_of_variant_of` + `var_expandable`).
3. **Foundation-Repo öffentlich** (2026-11-26): Commit `48cb4df`. MIT (Tools) + CC BY 4.0 (Daten) + PD-Notice (Text PG #18835).
4. **Website geboren** (2026-11-27): erster vertikaler Prototyp — Hub `index.html` + Bifurkations-Explorer (Commit `6644d93`).
5. **Vollausbau Module II–V + Corpus Reader** (2026-11-28): Commits `875bc85`, `78d9124`, `6fbcd52`.

## Aktueller Zustand der Website (`src/`)

| Seite | Modul | Interaktionen | Sonderstimme |
|---|---|---|---|
| bifurcation.html | I — Bifurkations-Explorer | Drag&Drop Pole, Feuer-Kippstelle, pid-Modals, Variant-Pfade | konservativ/dreifaltig-Wahlpfad |
| passage.html | II — Passage of Nature | Dual-Slider Dauer/Zeitsystem, Dauer/Moment-Ansichten | Scholem-Randnotiz (Toggle) |
| abstraction.html | III — Extensive Abstraction | Nested-Event-Zoom, q(e)-Konvergenzbalken | Greek-Point-Notiz (Euklid) |
| congruence.html | IV — Kongruenz | Segment-Transport, Russell-Axiom-Karten | Poincaré-Konventionalismus (Toggle) |
| ingression.html | V — Objekt-Ingression | Blauton-Regler, Rollen-Karten, Spiegel-/Bifurkations-Test | — |
| reader.html | VI — Corpus Reader | lineare Kapitel-Lektüre, TOC, Hash-Jump | pid-Anker je Absatz (Zitierfähigkeit) |

Gemeinsame Infrastruktur: Vanilla HTML/CSS/JS, fetch() der Datenlayer, bilingual EN/DE (localStorage `wcn-lang`), pid-Modal lädt aus `data/corpus.json` (Pfad `../data/` — kompatibel mit GitHub Pages Subfolder-Hosting, Entry-URL `/src/index.html`).

## Editorische Prinzipien (unverändert)

- Reproduzierbarkeit bis auf Absatzebene (pid-Adressierung); keine Black Boxes.
- Kein vorzeitiges Konsolidieren: „temporale Unordnung" bewusst geduldet; Widersprüche als parallele Lesarten (Theoriedorf).
- Sonderstimmen (Scholem, Greek Point, Poincaré) sind Toggles außerhalb des Konzeptgraphen — Kontrapunkte, keine Fusion.

## Arbeitsprozess / Werkzeugnotizen

- Datei-Brücke etabliert: fs_write nach `/media/SajonGmbH/DATA/*_tmp.html` + cp in `~/sajon/repo_wcon/src/` (umgeht lange Heredoc-Freigabehürden).
- Git: credential.helper zweifach in global config blockierte Pushes → repo-lokal `git config credential.helper store`; nach Token-Rotation einmalige Neueingabe im Terminal (nicht im Chat).
- Garble-Protokoll: `theimplicit` → `the implicit` gefixt (`78d9124`).

## Offene Arbeiten

- [ ] GitHub Pages aktivieren (Settings → Pages → main; Entry `/src/index.html`); danach Fetch-Verhalten unter Live-URL verifizieren.
- [ ] Lokaler Browsertest aller 6 Seiten + pid-Modals + Sprachumschalter.
- [ ] Parser v1.2: pagenum-Spans (Original-Paginierung) in Absatz-Records; Appendices (S. 197); Titel-Kapitalisierung.
- [ ] Konzeptgraph-Übersicht (D3.js) als siebte Seite.
- [ ] Tiptap-Annotations-Ebene auf Reader-Basis.
- [ ] Proton Drive Checkpoint 2 (manuell, bis Drive-Connector existiert).
- [ ] Später: Zeno-Registrierungen für jonason92-/Sajon-GmbH-Projekte (GitHub + Codeberg).

## Commits (Chronologie)

`48cb4df` Foundation → `6644d93` Prototyp Hub+Modul I → `875bc85` Modul II → `78d9124` Module III–V → `6fbcd52` Corpus Reader + Hub READY-Status.
