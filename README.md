# NAST · Nebular Armed Speeder Tournament

A browser racing game. Everything is self-contained HTML: open a file in a browser, no build step.

| File | What it is |
| --- | --- |
| `index.html` | The game |
| `speeder-models.html` | The six speeders as low-poly 3D models (three.js from cdnjs) |
| `soundtrack.html` | The soundtrack, synthesized live with Web Audio |
| `editor.html` | The track editor: draw a track, check it, and copy its track code (paste it into the game with **Paste track code**) |

## Music

The soundtrack is recorded tracks embedded in `index.html`, all by DavidKBD from the *Electric Pulse* pack:
the menu plays “Electric Dreams of Infinity”, and each world has its own race theme (“Electric Pulse”, “Digital
Horizon”, “Cyber Lights”, “Retrochrome Nights”, “Neon Arcadia Awakening”, “Time Warp”, “Quantum Ripples of
Sound”). **Options > Soundtrack > Synth** switches
back to the original themes, synthesized live with Web Audio (they also stand in if a browser can't decode a track).

With the music in it, `index.html` is about 48 MB: past the 16 MB a claude.ai artifact can hold, so play it from the
file itself.
