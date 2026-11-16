#!/usr/bin/env python3
"""
Applies targeted copy updates:
1. Adds 'ENJOY!' after '⟦ CHOOSE YOUR SPECTRUM EXPERIENCE ⟧'
2. Adds 'PSYTRANCE' next to 'DETROIT TECHNO' in the billboard footer note
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CHOOSE YOUR SPECTRUM EXPERIENCE
target_title = '⟦ CHOOSE YOUR SPECTRUM EXPERIENCE ⟧'
replacement_title = '⟦ CHOOSE YOUR SPECTRUM EXPERIENCE ⟧ — ENJOY!'

if target_title in text:
    text = text.replace(target_title, replacement_title, 1)
    print("SUCCESS: Added 'ENJOY!' after 'CHOOSE YOUR SPECTRUM EXPERIENCE'!")
else:
    print("WARNING: target_title not found in homepage.html")

# 2. Add PSYTRANCE next to DETROIT TECHNO
target_detroit = 'DETROIT TECHNO // BINARY PASSION'
replacement_detroit = 'DETROIT TECHNO // PSYTRANCE // BINARY PASSION'

if target_detroit in text:
    text = text.replace(target_detroit, replacement_detroit, 1)
    print("SUCCESS: Added 'PSYTRANCE' next to 'DETROIT TECHNO'!")
else:
    print("WARNING: target_detroit not found in homepage.html")

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: deploy/homepage.html updated.")
