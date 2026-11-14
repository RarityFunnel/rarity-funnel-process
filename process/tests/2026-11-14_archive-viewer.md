# Archive viewer validation · 14 November 2026

## Completed before publication

- JavaScript syntax: `node --check assets/archive.js` passed.
- Archive relationship validation: `python tests/validate_archive.py` passed: 12 sections, 87 source cards, 143 reference records, 320 book rows and 99 source-check notes.
- Every section card matches the same card in the common catalog, with original text unchanged.
- Four existing cards have no section association: `forma-origen`, `pop3-candidata`, `rareza`, `reloj-vivo`. They remain accessible under “Sin sección asignada”; no association was invented.
- File lengths and SHA-256 hashes are validated against `provenance.json`. The script reports the current manifest count.

## Browser and hosting status

Interactive browser validation remains pending until the viewer can be hosted over HTTPS. The local browser process could not start in this environment; the available cloud browser could not reach the local HTTP server and does not allow file URLs. These attempts are not passed browser tests.

The GitHub connector supports source publication. GitHub Pages activation is a separate repository setting; the available browser is not signed in to GitHub. No live Pages deployment is claimed by this record.

After activation, verify the default table, all five tabs, section filters including the unassigned group, search and empty results, record links, dialog close and keyboard navigation, pagination, narrow-screen layout and unavailable-door states. Update this record with observed results.
