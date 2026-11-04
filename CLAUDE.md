# NAST

A browser racing game in one self-contained file (`index.html`), plus the track editor (`editor.html`). No build step.

## Adding a track from the editor's track code

The user designs tracks in the editor and pastes its **track code** (JSON, `"format": "gatebreaker-track"`). To build one
into the game:

1. Add an entry to `const TRACKS = [...]` in `index.html` (follow the existing entries): an `id` (kebab-case of the
   name), `name`, `setting`, a `seed` (any small number not already used), and the code's `points`, `shortcuts`,
   `elevation`, `barricades`, `jumps`, `gaps`, `holes`, `loops` and `landmarks` as they are. The track format is documented in
   the comment above `const TRACKS` ("the circuits").
2. **Landmarks**: every entry in `landmarks` (`{at: [x, y], r, desc}`) needs its art, or it is not drawn. Draw each one
   to match its `desc`: add an entry to `LANDMARK_ART` (see the "landmarks" section of `index.html` for the format:
   slices stacked at rising heights, `size`, `height`, `n`, `slice(g, k, n, S, R, L)`, and an optional per-frame
   `over(...)` for lights or anything that moves), and set `art: '<its id>'` on the landmark in the track entry.
   Keep it in the game's pixel-art style: flat colours, lit from the upper left, sized to the landmark's `r`. Check it
   in a screenshot on its track before finishing.
3. Refresh the editor's list of game tracks: `LIBRARY` in `editor.html` (between the `/*LIB*/` markers) is every game
   track in track-code form, `km` included; regenerate it from the game's `TRACKS` rather than editing it by hand.
4. Republish the artifacts: the editor if it changed, and the game. The game is published without its recorded music
   (with it, it is about 48 MB, past the artifact size limit): build that copy with
   `python3 tools/build-artifact.py <scratchpad>/nast-artifact.html` and publish that file to the game's artifact
   (https://claude.ai/artifact/6Ys7bjkutpbCGF79s4Rie3). It plays the synthesized themes instead.

A track pasted into the game itself (Tracks > Paste track code) races the same, but its landmarks have no art and are
left out.

## Pilot lines from the editor's code

The editor's **Edit pilot lines** panel exports **pilot lines code** (JSON, `"format": "nast-pilot-lines"`): only what
was changed, as `pilots: {Name: {event: [lines]}}`. To build it into the game, replace those entries in `const CHAT`
in `index.html` (each event's lines joined with `|`; the events are listed above it, in "pilot chatter"), then
regenerate the editor's copy of the game's lines, `PILOT_LINES` in `editor.html` (between the `/*CHAT*/` markers),
from the game's `CHAT` and `ROSTER` rather than by hand. Republish both artifacts. Pasted into the game itself
(Options > Pilot lines > Paste code), the lines are used in that browser only.
