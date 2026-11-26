# Whitehead-Projekt: Interaktive philosophische Naturinformatik-Website
## Stand: 2026-11-26 (v0.3)

### Ziel
Transformation von Whiteheads "The Concept of Nature" in eine interaktive,
quellenreproduzierbare Wissenslandschaft. Grundsätze: Reproduzierbarkeit
bis auf Absatzebene (pid-Adressierung), Quellenkritik, keine Black Boxes,
bewusste Nicht-Konsolidierung als temporales Gestaltungsprinzip.

### Meilensteine
- M1 (2026-09-16): Parser-Lauf, 464 Absätze, 9 Kapitel, Probenkontrolle bestanden
- M2 (2026-11-26): Konzeptgraph Kap. I-IV, 27 Records (concepts_v0.7)
- M3 (2026-11-26): Checkpoint-Ordner mit SHA256-Prüfsummen erstellt

### Konzeptgraph (concepts_v0.7_2026-11-26.json, 27 Records)
- Kap. I (7+3 Detail): nature closed, sense-awareness, homogeneous thought,
  fact/factors/entities, event, situation, substratum critique
  (Variante 2: habit/matter-history/wrong-turn-diagnosis)
- Kap. II (5): bifurcation thesis, apparent/causal nature, rescue attempts,
  psychological addition, fire problem
- Kap. III (6): duration, simultaneity/instantaneousness, passage of nature,
  abstractive set, moment, materialistic trinity gap
- Kap. IV (6): simple location rationale, ideal simplicity/intrinsic character,
  abstractive set extended, covering/equality, abstractive element,
  event-particle/punct
- Mechanik: var_expandable-Flag (True nur c1_substratum_critique);
  distinction als Subtyp von principle; Artefakt-Assertions in Scrub

### Argumentationszüge (Arbeitshypothesen aus Kodierung)
- Zug A (erkennnistheoretisch): nature closed -> sense-awareness ->
  fact/factors/entities -> duration
- Zug B (ereignisontologisch): event -> situation -> duration/passage
- Zug C (diagnostisch-historisch): substratum -> bifurcation -> trinity gap

### Offene Arbeiten
1. Proton-Drive-Upload des Checkpoints (manuell, kein Connector)
2. Kapitel V-IX-Runden (selbes Verfahren: Scan -> Records -> versionierte v0.x)
3. modules.json (Bifurkations-Explorer, Extensive-Abstraction-Zoom, Time/Passage,
   Kongruenz, Objekt-Ingression)
4. Website-Architektur: Astro/Hugo + D3.js-Graph + Tiptap-Annotations-Ebene;
   Deployment auf Infomaniak
5. Parser v1.2: Seitenzahl-Marker (pagenum-Spans) + Appendices (S.197)

### Infrastruktur
- Deepin-Desktop-PC (SajonGmbH-PC), Python 3.12.13 + venv, ~/sajon/whitehead/
- Lumo-Connectors aktiv: Shell + Dateisystem (lokale Arbeitsschleife)
- Proton Drive als Backup-Ebene (manueller Upload), Infomaniak = Deployment-Ziel
