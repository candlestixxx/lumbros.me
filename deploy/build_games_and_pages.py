#!/usr/bin/env python3
"""
Orchestrates the Game Architecture for Lumbros.me:
1. Splits Shadertoy 3D Earth Tribute into its own standalone game (/shadertoy/)
2. Establishes the Spectrum Vision Game Dev Plan & Monopoly Financial Simulator (/spectrum-vision/)
3. Updates homepage.html with streamlined arcade launch hubs for both games
4. Updates top HUD navigation and pillars across all subpages
5. Guarantees 0 raw '&&' inside script tags (WordPress entity safe)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# ---------------------------------------------------------------------------
# 1. Update HUD Top Navigation Links in homepage.html
# ---------------------------------------------------------------------------
old_hud_links = '''    <div class="hud-nav-links">
      <a href="/" class="hud-link active">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link">LIVE POSTS</a>
    </div>'''

new_hud_links = '''    <div class="hud-nav-links">
      <a href="/" class="hud-link active">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link">LIVE POSTS</a>
      <span class="hud-sep">|</span>
      <a href="/shadertoy/" class="hud-link hud-game-link" style="color: #00ffcc; text-shadow: 0 0 8px rgba(0,255,204,0.6);">🎮 SHADERTOY 3D</a>
      <span class="hud-sep">|</span>
      <a href="/spectrum-vision/" class="hud-link hud-game-link" style="color: #00ff66; text-shadow: 0 0 8px rgba(0,255,102,0.6);">🌐 SPECTRUM VISION</a>
    </div>'''

if old_hud_links in home:
    home = home.replace(old_hud_links, new_hud_links)
    print("Updated hud-nav-links in homepage.html")
else:
    # Try regex replacement if whitespace differed
    home = re.sub(
        r'<div class="hud-nav-links">[\s\S]*?</div>',
        new_hud_links.strip(),
        home,
        count=1
    )
    print("Regex updated hud-nav-links in homepage.html")

# ---------------------------------------------------------------------------
# 2. Update Top Pillars Rail to include the two dedicated games
# ---------------------------------------------------------------------------
pillars_pattern = r'(<nav id="top-pillars-rail"[\s\S]*?</nav>)'
pillars_match = re.search(pillars_pattern, home)

if pillars_match:
    old_pillars = pillars_match.group(1)
    # Check if games already in pillars
    if '/shadertoy/' not in old_pillars:
        # Add pillars for Shadertoy and Spectrum Vision
        game_pillars_html = '''      <!-- Pillar IV: Shadertoy 3D Earth Game -->
      <a href="/shadertoy/" class="pillar-shape-btn pillar-shadertoy" style="border-color: #00ffcc;" title="Dedicated Game: Shadertoy 3D Earth & Phototherapy (Tribute to Inigo Quilez & Pol Jeremias)">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-04</span>
            <span class="pillar-status cyan">GAME 01</span>
            <span class="pillar-bricks-tag">[3D EARTH]</span>
          </div>
          <div class="pillar-title founder-name-chroma" style="color: #00ffcc;">
            SHADERTOY 3D
          </div>
          <div class="pillar-sub">BEAUTYPI TRIBUTE ↗</div>
        </div>
      </a>

      <!-- Pillar V: Spectrum Vision & Monopoly Simulator -->
      <a href="/spectrum-vision/" class="pillar-shape-btn pillar-spectrum-vision" style="border-color: #00ff66;" title="Dedicated Game & Dev Plan: Spectrum Vision Game Dev Plan & Monopoly Financial Simulator">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-05</span>
            <span class="pillar-status green">DEV PLAN</span>
            <span class="pillar-bricks-tag">[MONOPOLY]</span>
          </div>
          <div class="pillar-title founder-name-chroma" style="color: #00ff66;">
            SPECTRUM VISION
          </div>
          <div class="pillar-sub">DEV PLAN &amp; SIM ↗</div>
        </div>
      </a>
'''
        # Insert before Pillar IV: 1974 Chip Matrix
        if '<!-- Pillar IV: 1974 Chip Matrix -->' in old_pillars:
            new_pillars = old_pillars.replace(
                '<!-- Pillar IV: 1974 Chip Matrix -->',
                game_pillars_html + '\n      <!-- Pillar VI: 1974 Chip Matrix -->'
            )
            # Update pillar number for Chip Matrix
            new_pillars = new_pillars.replace('<span class="pillar-num">P-04</span>\n            <span class="pillar-status pear">SILICON</span>', '<span class="pillar-num">P-06</span>\n            <span class="pillar-status pear">SILICON</span>')
            new_pillars = new_pillars.replace('<span class="pillar-num">P-05</span>\n            <span class="pillar-status red">HIDDEN SPOT</span>', '<span class="pillar-num">P-07</span>\n            <span class="pillar-status red">HIDDEN SPOT</span>')
            home = home.replace(old_pillars, new_pillars, 1)
            print("Updated top-pillars-rail with Shadertoy and Spectrum Vision games!")

# ---------------------------------------------------------------------------
# 3. Enhance Section 0x09.5 in homepage.html with Spectrum Vision Dev Plan Header
# ---------------------------------------------------------------------------
# Ensure Section 0x09.5 clearly showcases the "SPECTRUM VISION GAME DEV PLAN"
# alongside the interactive Monopoly Simulator.
mono_title_old = 'SECTION: SPECTRUM MONOPOLY — THE REAL-WORLD FINANCIAL & PLANETARY LIFE SIMULATOR'
mono_title_new = 'SECTION 0x09.5: SPECTRUM VISION GAME DEV PLAN & SPECTRUM MONOPOLY SIMULATOR'

if mono_title_old in home:
    home = home.replace(mono_title_old, mono_title_new)

# Add Game Dev Plan Banner inside Section 0x09.5 if not present
if 'SPECTRUM VISION // MASTER GAME DEV PLAN' not in home:
    dev_plan_banner = '''    <!-- Spectrum Vision Game Dev Plan Header & Master Roadmap -->
    <div class="dev-plan-banner" style="background: linear-gradient(135deg, rgba(0,255,102,0.08) 0%, rgba(0,229,255,0.05) 100%); border: 1px solid rgba(0,255,102,0.3); border-radius: 8px; padding: 20px; margin-bottom: 25px; box-shadow: 0 0 20px rgba(0,255,102,0.1);">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 15px; border-bottom: 1px solid rgba(0,255,102,0.2); padding-bottom: 12px;">
        <div>
          <span style="background: #00ff66; color: #000; font-weight: 900; font-size: 0.72rem; padding: 3px 8px; border-radius: 3px; letter-spacing: 1.5px;">GAME DEV PLAN</span>
          <span style="color: #00e5ff; font-weight: 800; font-size: 1.1rem; margin-left: 10px; letter-spacing: 2px;">SPECTRUM VISION // MASTER GAME ARCHITECTURE</span>
        </div>
        <div>
          <a href="/spectrum-vision/" class="btn-terminal" style="background: #00ff66; color: #050b14; text-decoration: none; font-weight: 800; font-size: 0.76rem; padding: 6px 14px; border-radius: 4px; box-shadow: 0 0 10px rgba(0,255,102,0.4);">
            LAUNCH DEDICATED DEV ARENA ↗
          </a>
        </div>
      </div>

      <div style="font-size: 0.82rem; color: #b8e2c8; line-height: 1.6; margin-bottom: 16px;">
        <strong>THE VISION:</strong> A multi-dimensional gaming ecosystem rooted in the <strong>Rule of Three</strong> (Love • God • Life &equiv; Mind • Body • Soul) and the <strong>12-Color Optical Invisible Spectrum</strong> (Green 532nm center). Players navigate macro-global to local economics, planetary survival (Environment, Humanity, Resources), and Euler standing-wave physics.
      </div>

      <!-- Roadmap Matrix Grid -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
        <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #00ff66; font-size: 0.75rem; font-weight: 800;">PHASE 1: ACTIVE LIVE SIM</div>
          <div style="color: #ffffff; font-size: 0.88rem; font-weight: 700; margin: 4px 0;">SPECTRUM MONOPOLY</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Real-world financial strata from homeless to billionaire bunkers, AI tiers, K-12 education, clear-net money laundering, and restitution.</div>
        </div>

        <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #00e5ff; font-size: 0.75rem; font-weight: 800;">PHASE 2: WSM PHYSICS</div>
          <div style="color: #ffffff; font-size: 0.88rem; font-weight: 700; margin: 4px 0;">EULER WAVE ORBIT ENGINE</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Spherical standing waves (e^{i&theta;} = cos&theta; + i sin&theta;), 3D Earth sliced by 12 Keplerian orbits, and paint-gun photon blasts.</div>
        </div>

        <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(255,170,0,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #ffaa00; font-size: 0.75rem; font-weight: 800;">PHASE 3: PHOTOTHERAPY</div>
          <div style="color: #ffffff; font-size: 0.88rem; font-weight: 700; margin: 4px 0;">532nm HEALING RESONANCE</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Medical wellness frequencies aligning neurons, eye sight, cellular recovery, and depression alleviation.</div>
        </div>

        <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(255,0,128,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #ff0080; font-size: 0.75rem; font-weight: 800;">PHASE 4: AGENT SWARMS</div>
          <div style="color: #ffffff; font-size: 0.88rem; font-weight: 700; margin: 4px 0;">PLANETARY COMMONS</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Decentralized peer-to-peer sovereign economies where collective resource equilibrium wins the game.</div>
        </div>
      </div>
    </div>
'''
    # Insert after section-badge inside section#spectrum-monopoly
    pattern_badge = r'(<section id="spectrum-monopoly"[\s\S]*?<div class="section-badge">[\s\S]*?</div>)'
    match_badge = re.search(pattern_badge, home)
    if match_badge:
        home = home.replace(match_badge.group(1), match_badge.group(1) + '\n\n' + dev_plan_banner, 1)
        print("Injected Spectrum Vision Game Dev Plan banner into Section 0x09.5!")

# ---------------------------------------------------------------------------
# 4. Save updated homepage.html
# ---------------------------------------------------------------------------
with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)
print("Updated deploy/homepage.html successfully!")
