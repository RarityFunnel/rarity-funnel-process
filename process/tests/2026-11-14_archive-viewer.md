# Archive viewer validation · 14 November 2026

## Completed before publication

- JavaScript syntax: `node --check assets/archive.js` passed.
- Archive relationship validation: `python tests/validate_archive.py` passed: 12 sections, 87 source cards, 143 reference records, 320 book rows and 99 source-check notes.
- Every section card matches the same card in the common catalog, with original text unchanged.
- Four existing cards have no section association: `forma-origen`, `pop3-candidata`, `rareza`, `reloj-vivo`. They remain accessible under “Sin sección asignada”; no association was invented.
- File lengths and SHA-256 hashes are validated against `provenance.json`. The script reports the current manifest count.

## Initial hosting attempts

Before HTTPS hosting was available, the local browser process could not start in this environment; the available cloud browser could not reach the local HTTP server and does not allow file URLs. These attempts were not passed browser tests.

GitHub Pages activation was a separate repository setting. David subsequently activated publication from `main` / `/(root)` in his GitHub session.

## Confirmed HTTPS deployment and browser validation

- Date: 14 November 2026.
- Live URL: https://rarityfunnel.github.io/rarity-funnel-process/
- Tested viewer commit: `26d5d87db78f1efc8c298b8d5f66564f07bc8983`.
- GitHub Actions run: https://github.com/RarityFunnel/rarity-funnel-process/actions/runs/43622679561 — completed, success.
- Desktop browser rendered the dark documentation layout, sidebar, statistics, search field, tabs and table without visible overlap.
- All five tabs opened with their expected contents: Fuentes, Hallazgos, Comprobaciones, Correspondencias and Historial. Comprobaciones showed the 99 retained notes and their pending-status qualification; Correspondencias showed 320 rows and the documentary-match qualification.
- All 12 section filters worked. Source-card counts by section: `5, 7, 0, 30, 10, 3, 6, 7, 8, 8, 16, 2`. Counts overlap because a card may belong to multiple sections. Section 03 correctly retained an empty state rather than invented sources.
- The unassigned group displayed exactly the four preserved cards.
- Searching `litio` within section 04 returned two cards. An unmatched query displayed the empty-results state; clearing filters restored the complete selection.
- The lithium source dialog displayed its original assertion, contribution, limits, source identifiers and DOI links. Links were inspected in the rendered dialog; this test did not audit the external papers.
- The individual-record URL opened the lithium dialog and restored it after a reload once the data had loaded. Escape closed the dialog. An immediate non-waiting visibility probe during the first reload was false; the subsequent explicit visible-state checks passed on navigation and reload.
- The Correspondencias next-page control displayed rows 21–40 and page 2 of 16. ArrowRight from its tab opened Historial.
- Selecting LineageMoment showed the explicit missing-corpus state.
- Browser error output inspected during these checks contained extension metadata errors, not a reported viewer error.

Limitations: narrow-screen/mobile rendering and every individual external source destination were not tested in this session. These checks validate the documentation viewer's observed behavior, not scientific claims, the immersive website, canonical approval or Drive synchronization. The later documentation-only commit records these results without changing the tested viewer code or source data.
