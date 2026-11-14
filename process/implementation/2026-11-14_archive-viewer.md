# Read-only archive viewer · 14 November 2026

David requested an organized, conventional documentation interface with a dark background, tabs and database-like browsing, following the Fermi Explorer reference. He then requested implementation and preparation for use. This is a separate, explicit extension to the previously authorized public AlbaView archive.

Files: `index.html`, `assets/archive.css`, `assets/archive.js`, `.nojekyll`.

The viewer reads the existing public JSON directly and adds no separate source catalog. It provides door/section selection, accent-insensitive search, paginated tables, source details, source links, notes from Books, exact-ID correspondences and provenance. Links preserve the door, section, tab, search and selected record in the URL fragment. The UI is Spanish and preserves all original source wording.

Other doors are shown with an explicit missing-corpus state. Checks retain their recorded text and do not imply completed validation. The global statistics describe the archive snapshot, not just the selected section. Full history remains available in GitHub.

The viewer has no runtime third-party libraries or build step. Text is inserted as text nodes; external source links allow only HTTP(S). Narrow screens use a horizontal section selector, scrollable tabs and scrollable tables. Dialogs support Escape and return focus to the originating control.

GitHub Pages can publish the repository root from main. Activation and the live URL require independent verification; code presence is not proof of deployment. No changes were made to Rarity Funnel's immersive website, navigation kit or approved content. Drive-to-GitHub automatic synchronization remains inactive.
