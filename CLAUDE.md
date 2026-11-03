# NAST

A browser racing game in one self-contained file (`index.html`), plus the track editor (`editor.html`). No build step.

## Adding a track from the editor's track code

The user designs tracks in the editor and pastes its **track code** (JSON, `"format": "gatebreaker-track"`). To build one
into the game:

1. Add an entry to `const TRACKS = [...]` in `index.html` (follow the existing entries): an `id` (kebab-case of the
   name), `name`, `setting`, a `seed` (any small number not already used), and the code's `points`, `shortcuts`,
   `elevation`, `barricades`, `jumps`, `gaps`, `loops` and `landmarks` as they are. The track format is documented in
   the comment above `const TRACKS` ("the circuits").
2. **Landmarks**: every entry in `landmarks` (`{at: [x, y], r, desc}`) needs its art, or it is not drawn. Draw each one
   to match its `desc`: add an entry to `LANDMARK_ART` (see the "landmarks" section of `index.html` for the format:
   slices stacked at rising heights, `size`, `height`, `n`, `slice(g, k, n, S, R, L)`, and an optional per-frame
   `over(...)` for lights or anything that moves), and set `art: '<its id>'` on the landmark in the track entry.
   Keep it in the game's pixel-art style: flat colours, lit from the upper left, sized to the landmark's `r`. Check it
   in a screenshot on its track before finishing.
3. Refresh the editor's list of game tracks: `LIBRARY` in `editor.html` (between the `/*LIB*/` markers) is every game
   track in track-code form, `km` included; regenerate it from the game's `TRACKS` rather than editing it by hand.
4. Republish the editor artifact if it changed. (The game itself, at about 36 MB with its embedded music, is past
   the artifact size limit and is played from the file, so it is no longer republished.)

A track pasted into the game itself (Tracks > Paste track code) races the same, but its landmarks have no art and are
left out.
