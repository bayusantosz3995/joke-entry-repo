#!/usr/bin/env python3
"""Entry for the-joke-about-the-demo-20261121-0551 competition.
Writes a joke to /output/entry.txt"""

import os

joke = "Why did the coding agent cross the road? To prove it wasn't just a fancy autocomplete with anxiety."

os.makedirs('/output', exist_ok=True)

with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(joke)

print(f"Wrote joke to /output/entry.txt ({len(joke)} chars)")
