#!/usr/bin/env python3
"""Build the claude.ai artifact copy of the game: index.html without the recorded music (which would put it far past
the artifact's 16 MB limit). The game then plays its synthesized themes and hides the Soundtrack option.

    python3 tools/build-artifact.py OUT.html

The recordings are the <script>NAST_REC... blocks after the loading screen; BOOT.TOTAL (the loading bar's total) is
recounted for what is left."""
import re, sys

src = open('index.html', encoding='utf-8').read()
out, n = re.subn(r"<script>NAST_REC = window\.NAST_REC \|\| \{\}; NAST_REC\.\w+ = '[^']*'; BOOT\.step\('[^']*'\);</script>\n", '', src)
if not n:
    sys.exit('no recordings found: has the music block format changed?')
# the loading bar's total: what is still counted (the preview videos' block, three.js, the game script)
counted = 0
for m in re.finditer(r'<script>(.*?)</script>', out, re.S):
    body = m.group(1)
    if 'BOOT.step(' in body and 'var BOOT' not in body and len(body) > 1000: counted += len(body)
three = re.search(r'BOOT\.got \+= (\d+); BOOT\.step\(', out)
main = re.search(r"<script>\n'use strict';\nBOOT\.got \+= document\.currentScript\.text\.length;(.*?)</script>", out, re.S)
total = counted + (int(three.group(1)) if three else 0) + (len(main.group(0)) if main else 0)
out = re.sub(r'TOTAL: \d+, got: 0', 'TOTAL: %d, got: 0' % total, out, count=1)
open(sys.argv[1], 'w', encoding='utf-8').write(out)
print('%d recordings left out; %.1f MB (was %.1f MB)' % (n, len(out.encode()) / 1e6, len(src.encode()) / 1e6))
