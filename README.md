# Rarity Funnel · Process

An archive of Rarity Funnel’s sources, findings, and development process, organized by door and journey section.

## Explore

The repository now includes a read-only archive viewer (`index.html`) with a dark documentation interface, search, door/section navigation and tabs for sources, findings, checks, book–experience correspondences and provenance. The viewer reads the existing JSON files directly. Source wording is preserved in Spanish.

**[Open the public archive](https://rarityfunnel.github.io/rarity-funnel-process/).** GitHub Pages was activated from `main` / `/(root)` and verified live on 14 November 2026. [The initial deployment succeeded](https://github.com/RarityFunnel/rarity-funnel-process/actions/runs/43622679561) for viewer commit `26d5d87db78f1efc8c298b8d5f66564f07bc8983`. No custom domain or extra data service is required. Source-data updates committed to this branch are included in subsequent Pages deployments. This does not synchronize Drive with GitHub.

Viewer links use URL fragments, for example `#door=albaview&section=04&tab=sources`; individual source cards can also be linked. The immersive website can use the public archive URL for its source access. Adding that link to the immersive website is a separate task and has not been performed by this repository update. [Browser validation record](process/tests/2026-11-14_archive-viewer.md).

- [AlbaView: twelve journey sections](doors/albaview/README.md)
- [LineageMoment](doors/lineage-moment/README.md) · [PresentFront](doors/present-front/README.md) · [Sanity Portrait](doors/sanity-portrait/README.md)
- [Global experience](global-experience/README.md)
- [Unified source cards](catalog/source-cards.json) · [References](catalog/references.json)
- [Book–experience correspondences](catalog/book-experience-crosswalk.json)
- [Update policy](process/UPDATE_POLICY.md) · [Provenance](provenance.json) · [Coverage](catalog/coverage.json)

## First archival batch · 14 November 2026

This is a **partial AlbaView source archive** joining the available Books documentation of 13 November with the source data embedded in experience delivery r16/v06/e14 of 12 November. A delivery number is a version identifier, not evidence of approval.

It contains 87 source cards, 143 deduplicated reference records, 99 book source-apparatus records and a crosswalk for 320 book records. Of these, 287 have exact IDs in the checked embedded journey and 17 have ID references in its separate final module; 16 have no exact match in these checked paths. These are documentary matches, not a new scientific audit or a runtime test.

Source cards preserve their claims, contributions, limitations and reference notes. References to papers are **not copies of the papers**. The repository does not yet contain the complete corpus for all four doors, the full book, the full script, or the website build.

## Additional public references · 14 November 2026

The common catalog now contains 147 records: the original 143 card-reference records and four external references for editorial research. The 87 experience cards and 320 book records are unchanged. [Public bibliographic metadata and consultation limits](originals/public-references/2026-11-14/explanation-reading-metadata.json). These references do not establish that any experience text has changed or that Rarity Funnel has been experimentally validated.

## Maintenance

Every source or process change must update the relevant snapshots, catalog, section links and change record. A change counts as backed up only after the resulting commit is read back and its files verified. Books and Immersive Experience retain responsibility for their originals; RF coordinates this replica. [Full policy](process/UPDATE_POLICY.md).

Automatic synchronization is not active. A policy file alone does not run a synchronization service.

Project records retain their original language. No blanket license is assigned to third-party sources. See [publication scope](process/PUBLICATION_SCOPE.md).
