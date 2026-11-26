# Whitehead: The Concept of Nature - Interactive Edition

An open-science transformation of Alfred North Whitehead's
*The Concept of Nature* (Tarner Lectures, Trinity College Cambridge,
November 1919; Cambridge University Press 1920) into an interactive,
source-reproducible knowledge landscape of philosophical natural-informatics.

Repository: https://github.com/jonason92/whitehead-concept-of-nature
Maintainer: Jonas Haessig (Sajon GmbH, Bern) - https://sajon.net

## Core principles

1. **Reproducibility down to paragraph level** - every claim, every concept
   record, every interactive module references a paragraph ID (`pid`,
   format ch{n}-p{XXX}) that resolves to the original 1920 text.
2. **Source criticism** - the corpus was parsed from Project Gutenberg
   eBook #18835 (public domain), with documented errata and provenance
   of all editorial decisions.
3. **No interpretation monopolies** - the concept graph is a "theory village":
   conflicting readings (conservative vs. detailed variants, marginalia
   like the Scholem counterpoint) coexist instead of being resolved.

## Repository structure

```
data/    - three-layer data model (single source of truth)
tools/   - parser and maintenance scripts
docs/    - project state documents, checkpoint READMEs
src/     - website (to be built)
```

## Data model (three layers)

- **Layer 1 (corpus)**: full text split into 464 paragraphs with stable IDs.
- **Layer 2 (concepts)**: 58 concept records across Chapters I-IX, typed as
  thesis / principle / entity / relation / method, with `definition_pid`
  and `key_support_pids` linking each record into the corpus.
- **Layer 3 (modules)**: 5 interactive modules. Each module carries a
  philosophical claim, anchored by `claim_pid` and support pids - meaning
  every interactive feature on the website is traceable to the source text.

## Source & license

- Text source: Project Gutenberg #18835, public domain (1920 edition)
- Parser and tools: MIT license (see LICENSE)
- Concept graph and module definitions: CC BY 4.0 (see LICENSE)

## Development methodology

This project deliberately embraces temporal non-consolidiation: naming
conventions emerge from the material instead of being fixed upfront.
The git history is the honest time-trail of that process.
