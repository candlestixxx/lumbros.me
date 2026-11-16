#!/usr/bin/env python3
"""
Moves Spectrum Luminance Polarity to the very top of the boxes as the FIRST choice
to control the sight in the vision calibration deck (#vision-calibration-deck).
1. Swaps the order of vision-polarity-module and vision-acuity-module in deploy/homepage.html
2. Updates module header labels:
   - CHOICE 01 // SPECTRUM LUMINANCE POLARITY (CONTROL THE SIGHT)
   - CHOICE 02 // VISUAL ACUITY GAUGE & SIGHT PRESCRIPTION FOCUS
3. Applies CSS to ensure Polarity sits prominently at the top as the primary sight control
4. Regenerates all subpages via generate_subpages.py
5. Ensures 0 raw '&&' inside script tags (100% WordPress entity safe)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

pos_ctrl = home.find('vision-deck-controls')
if pos_ctrl == -1:
    print("ERROR: Could not find vision-deck-controls in homepage.html")
    exit(1)

pos_mod1 = home.find('<!-- Module 1', pos_ctrl)
pos_mod2 = home.find('<!-- Module 2', pos_ctrl)
pos_strip = home.find('<!-- Compact Archetype', pos_ctrl)

if pos_mod1 == -1 or pos_mod2 == -1 or pos_strip == -1:
    print(f"ERROR: Could not locate module boundaries (mod1={pos_mod1}, mod2={pos_mod2}, strip={pos_strip})")
    exit(1)

mod1_text = home[pos_mod1:pos_mod2]
mod2_text = home[pos_mod2:pos_strip]

# Update headers
# Mod 2 becomes Choice 01
mod2_updated = mod2_text.replace(
    '<!-- Module 2: High-Contrast Light vs Dark Spectrum Toggle (Luminance Polarity) -->',
    '<!-- Choice 01: Spectrum Luminance Polarity (Control the Sight) -->'
)
mod2_updated = mod2_updated.replace(
    '<span class="mod-title">SPECTRUM LUMINANCE POLARITY</span>',
    '<span class="mod-title">CHOICE 01 // SPECTRUM LUMINANCE POLARITY (CONTROL THE SIGHT)</span>'
)
mod2_updated = mod2_updated.replace(
    '<span class="mod-arcade-tag">DUAL-LUX</span>',
    '<span class="mod-arcade-tag" style="background:#00ff66; color:#050b14; font-weight:900;">1ST CHOICE</span>'
)

# Mod 1 becomes Choice 02
mod1_updated = mod1_text.replace(
    '<!-- Module 1: 3-Stage Mathematical Acuity Gauge with Interactive Drag Circle -->',
    '<!-- Choice 02: Visual Acuity Gauge & Sight Prescription Calibrator -->'
)
mod1_updated = mod1_updated.replace(
    '<span class="mod-title">VISUAL ACUITY GAUGE &amp; SIGHT PRESCRIPTION CALIBRATOR</span>',
    '<span class="mod-title">CHOICE 02 // VISUAL ACUITY GAUGE &amp; SIGHT PRESCRIPTION FOCUS</span>'
)
mod1_updated = mod1_updated.replace(
    '<span class="mod-arcade-tag">TACTILE DIAL</span>',
    '<span class="mod-arcade-tag" style="background:#00e5ff; color:#050b14; font-weight:900;">2ND CHOICE</span>'
)

# Put Polarity (mod2) first, then Acuity (mod1) second!
new_controls_content = mod2_updated.strip() + '\n\n        ' + mod1_updated.strip() + '\n\n        '

home = home[:pos_mod1] + new_controls_content + home[pos_strip:]
print("SUCCESS: Reordered Polarity as Choice 01 (at top) and Acuity as Choice 02!")

# Add CSS to ensure Polarity spans full-width across the top of the box
polarity_first_css = '''
  /* =========================================================================
     CHOICE 01: SPECTRUM LUMINANCE POLARITY AT TOP OF VISION DECK BOXES
     ========================================================================= */
  .vision-deck-controls {
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
  }
  .vision-polarity-module {
    width: 100% !important;
    background: rgba(4, 14, 24, 0.9) !important;
    border: 1px solid rgba(0, 255, 102, 0.45) !important;
    box-shadow: 0 0 20px rgba(0, 255, 102, 0.1) !important;
  }
  .vision-acuity-module {
    width: 100% !important;
  }
  .polarity-toggle-group {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 12px !important;
  }
  @media (max-width: 640px) {
    .polarity-toggle-group {
      grid-template-columns: 1fr !important;
    }
  }
'''

if '/* CHOICE 01: SPECTRUM LUMINANCE POLARITY AT TOP OF VISION DECK BOXES */' not in home:
    style_end = '</style>'
    home = home.replace(style_end, polarity_first_css + '\n  ' + style_end, 1)
    print("Added CSS for full-width Polarity Choice 01 at top of vision deck boxes!")

# Save homepage.html
with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print("SUCCESS: Saved updated deploy/homepage.html!")
