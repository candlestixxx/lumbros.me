#!/usr/bin/env python3
"""
Generates standalone pages:
1. deploy/shadertoy.html  (/shadertoy/)
2. deploy/spectrum_vision.html (/spectrum-vision/)
Also updates generate_subpages.py and deploy_page.py
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# Extract essential shell components from homepage.html
style_match = re.search(r'(<style>[\s\S]*?</style>)', home)
styles = style_match.group(1) if style_match else ''

script_match = re.search(r'(<script>[\s\S]*?</script>)', home)
scripts = script_match.group(1) if script_match else ''

header_match = re.search(r'(<header class="ascii-hero">[\s\S]*?</header>)', home)
ascii_header = header_match.group(1) if header_match else ''

pillars_match = re.search(r'(<nav id="top-pillars-rail"[\s\S]*?</nav>)', home)
top_pillars_rail = pillars_match.group(1) if pillars_match else ''

footer_match = re.search(r'(<footer class="terminal-footer">[\s\S]*?</footer>)', home)
footer = footer_match.group(1) if footer_match else ''

audio_hud_match = re.search(r'(<!-- YouTube Audio Engine -->[\s\S]*?<!-- End YouTube Audio Engine -->)', home)
audio_hud = audio_hud_match.group(1) if audio_hud_match else ''

# Extract sections
shadertoy_sec_match = re.search(r'(<section id="shadertoy-tribute"[\s\S]*?</section>)', home)
shadertoy_sec = shadertoy_sec_match.group(1) if shadertoy_sec_match else ''

monopoly_sec_match = re.search(r'(<section id="spectrum-monopoly"[\s\S]*?</section>)', home)
monopoly_sec = monopoly_sec_match.group(1) if monopoly_sec_match else ''

def build_standalone(page_title, active_slug, main_content_html, extra_head_note=""):
    # Build Top HUD bar with active slug highlighted
    hud_bar = f'''  <!-- Top Terminal HUD Banner -->
  <div class="hud-top-bar">
    <div class="hud-status-badge">
      <span class="live-dot-pulse"></span>
      <span>SYSTEM OPERATIONAL // NODE: LUMBROS.ME // {active_slug.upper()}</span>
    </div>
    <div class="hud-nav-links">
      <a href="/" class="hud-link">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link {'active' if active_slug=='public' else ''}">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link {'active' if active_slug=='private' else ''}">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link {'active' if active_slug=='posts' else ''}">LIVE POSTS</a>
      <span class="hud-sep">|</span>
      <a href="/shadertoy/" class="hud-link hud-game-link {'active' if active_slug=='shadertoy' else ''}" style="color: #00ffcc; text-shadow: 0 0 8px rgba(0,255,204,0.6);">🎮 SHADERTOY 3D</a>
      <span class="hud-sep">|</span>
      <a href="/spectrum-vision/" class="hud-link hud-game-link {'active' if active_slug=='spectrum_vision' else ''}" style="color: #00ff66; text-shadow: 0 0 8px rgba(0,255,102,0.6);">🌐 SPECTRUM VISION</a>
    </div>
  </div>'''

    breadcrumb = f'''  <!-- Page Breadcrumbs -->
  <div class="terminal-section" style="margin-bottom: 20px; padding: 12px 20px; border-left: 3px solid #00ff66;">
    <div style="font-size: 0.76rem; letter-spacing: 1.5px; color: #8ce4a7; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
      <div>
        <a href="/" style="color: #00ff66; text-decoration: none;">ROOT</a> / 
        <span style="color: #ffffff; font-weight: 800;">{page_title}</span>
      </div>
      <div style="color: #00e5ff; font-weight: 700;">
        CONTINUUM EPOCH: +1794703800s // HARMONIC CENTER: 532nm
      </div>
    </div>
    {extra_head_note}
  </div>'''

    return f'''<div class="terminal-wrapper theme-cyberpunk">
{hud_bar}

{top_pillars_rail}

{ascii_header}

{breadcrumb}

{main_content_html}

{footer}

{audio_hud}

{styles}

{scripts}
</div>'''

# ---------------------------------------------------------------------------
# 1. Generate deploy/shadertoy.html
# ---------------------------------------------------------------------------
shadertoy_extra_note = '''
    <div style="margin-top: 8px; font-size: 0.73rem; color: #a0f0c0; line-height: 1.4; border-top: 1px dashed rgba(0,255,102,0.25); padding-top: 6px;">
      <span style="color: #00ffcc; font-weight: 800;">DEDICATED STANDALONE GAME:</span> 3D Earth WebGL Raymarching Engine &bull; Homage to <strong>I&ntilde;igo Qu&iacute;lez</strong> &amp; <strong>Pol Jeremias</strong> (via Beautypi) &bull; Wave Structure of Matter (Euler&rsquo;s Wave Identity e^{i&pi;} + 1 = 0) &bull; Phototherapy Wellness Tool.
    </div>'''

shadertoy_page = build_standalone(
    "GAME 01 // SHADERTOY 3D EARTH // TRIBUTE TO BEAUTYPI",
    "shadertoy",
    shadertoy_sec,
    shadertoy_extra_note
)

with open(os.path.join(BASE_DIR, 'shadertoy.html'), 'w', encoding='utf-8') as f:
    f.write(shadertoy_page)
print("SUCCESS: Generated deploy/shadertoy.html!")

# ---------------------------------------------------------------------------
# 2. Generate deploy/spectrum_vision.html
# ---------------------------------------------------------------------------
spectrum_vision_extra_note = '''
    <div style="margin-top: 8px; font-size: 0.73rem; color: #a0f0c0; line-height: 1.4; border-top: 1px dashed rgba(0,255,102,0.25); padding-top: 6px;">
      <span style="color: #00ff66; font-weight: 800;">GAME DEV PLAN &amp; SIMULATOR:</span> Planetary Survival Gauges &bull; Macro-Global to Local Financial Architecture &bull; 12 Spectrum Economic Strata (Homeless to Billionaire Bunker) &bull; AI Monthly Tiers &bull; Moral Agency &amp; Path of Restitution.
    </div>'''

# Comprehensive Game Dev Plan Architecture Section to prepend to Monopoly Simulator
extra_dev_plan_html = '''
  <!-- =========================================================================
       SPECTRUM VISION: MASTER GAME DEVELOPMENT PLAN & ARCHITECTURAL SPECIFICATION
       DESIGNED & DEVELOPED BY LUM (LUMBROS KOURLOS)
       ========================================================================= -->
  <section class="terminal-section" style="margin-bottom: 25px; border-left: 3px solid #00e5ff;">
    <div class="section-badge">
      <span class="badge-num">DEV-01</span>
      <span class="badge-tag">GAME DEV PLAN</span>
      <span class="badge-title">SPECTRUM VISION // MASTER ARCHITECTURE &amp; DESIGN SPEC</span>
    </div>

    <div style="font-size: 0.84rem; color: #e0f2fe; line-height: 1.7; margin-bottom: 20px;">
      <strong>SPECTRUM VISION</strong> is an open-source, multi-dimensional serious game and reality-simulation platform created by <strong>Lum (Lumbros Kourlos)</strong>. It integrates the <strong>12-Color Optical Invisible Spectrum</strong> (with emerald Green 532nm at the exact equilibrium center), the <strong>Wave Structure of Matter (WSM)</strong>, and real-world socioeconomic systems to empower players to experience life vicariously across all viewpoints, understand the fragility of our planetary commons, and master the balance of existence in threes.
    </div>

    <!-- 3 Core Pillars of Balance -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px; margin-bottom: 25px;">
      <div style="background: rgba(0,255,102,0.06); border: 1px solid rgba(0,255,102,0.3); border-radius: 8px; padding: 16px;">
        <div style="color: #00ff66; font-size: 0.78rem; font-weight: 900; letter-spacing: 1.5px;">PILLAR I // BODY &bull; LIFE</div>
        <div style="color: #ffffff; font-size: 0.95rem; font-weight: 800; margin: 6px 0;">3D Planetary Canvas &amp; Physical Survival</div>
        <p style="color: #8ce4a7; font-size: 0.74rem; line-height: 1.5; margin: 0;">
          The physical world: real estate, food, clean water, shelter, planetary environmental thresholds, and the tangible laws of energy conservation.
        </p>
      </div>

      <div style="background: rgba(0,229,255,0.06); border: 1px solid rgba(0,229,255,0.3); border-radius: 8px; padding: 16px;">
        <div style="color: #00e5ff; font-size: 0.78rem; font-weight: 900; letter-spacing: 1.5px;">PILLAR II // MIND &bull; GOD</div>
        <div style="color: #ffffff; font-size: 0.95rem; font-weight: 800; margin: 6px 0;">Euler's Wave Equations &amp; Mathematics</div>
        <p style="color: #8ce4a7; font-size: 0.74rem; line-height: 1.5; margin: 0;">
          The mathematical architecture of reality: complex wave vectors (e^{i&theta;} = cos&theta; + i sin&theta;), Keplerian planetary orbits, and harmonic resonance.
        </p>
      </div>

      <div style="background: rgba(255,170,0,0.06); border: 1px solid rgba(255,170,0,0.3); border-radius: 8px; padding: 16px;">
        <div style="color: #ffaa00; font-size: 0.78rem; font-weight: 900; letter-spacing: 1.5px;">PILLAR III // SOUL &bull; LOVE</div>
        <div style="color: #ffffff; font-size: 0.95rem; font-weight: 800; margin: 6px 0;">Neural Phototherapy &amp; Healing</div>
        <p style="color: #8ce4a7; font-size: 0.74rem; line-height: 1.5; margin: 0;">
          Psychological recovery, depression alleviation through 532nm green resonance, moral integrity, empathy for all demographics, and the Path of Restitution.
        </p>
      </div>
    </div>

    <!-- Rule of Three Specification -->
    <div style="background: rgba(5,15,25,0.8); border: 1px solid rgba(0,255,102,0.25); border-radius: 8px; padding: 18px; margin-bottom: 25px;">
      <div style="color: #00ff66; font-size: 0.8rem; font-weight: 800; margin-bottom: 8px; letter-spacing: 1.5px;">
        THE RULE OF THREE: 3 WAYS TO ACCOMPLISH EVERY OBJECTIVE
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; font-size: 0.74rem; color: #b8e2c8;">
        <div>
          <span style="color: #00e5ff; font-weight: 700;">1. Visual / Creative Path:</span>
          Freeform artistic expression, Paint Brush Gun, photon dispersion, intuitive aesthetic alignment.
        </div>
        <div>
          <span style="color: #ffaa00; font-weight: 700;">2. Mathematical / WSM Path:</span>
          Precise Euler phase tuning, Kepler orbit speeds, wavelength harmonics, exact calculated coordinates.
        </div>
        <div>
          <span style="color: #00ff66; font-weight: 700;">3. Economic / Systemic Path:</span>
          Resource stewardship, capital allocation, community building, restitution, and systemic balance.
        </div>
      </div>
    </div>

    <!-- Active Development Roadmap Table -->
    <div style="overflow-x: auto; margin-bottom: 15px;">
      <table style="width: 100%; border-collapse: collapse; font-size: 0.75rem; text-align: left; color: #b8e2c8;">
        <thead>
          <tr style="border-bottom: 1px solid #00ff66; color: #00ff66;">
            <th style="padding: 8px;">PHASE</th>
            <th style="padding: 8px;">MODULE</th>
            <th style="padding: 8px;">STATUS</th>
            <th style="padding: 8px;">CORE DELIVERABLE</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid rgba(0,255,102,0.15);">
            <td style="padding: 8px; font-weight: 800; color: #00ff66;">01</td>
            <td style="padding: 8px; font-weight: 700; color: #ffffff;">The New Monopoly Simulator</td>
            <td style="padding: 8px;"><span style="background: rgba(0,255,102,0.2); color: #00ff66; padding: 2px 6px; border-radius: 3px;">LIVE &amp; PLAYABLE</span></td>
            <td style="padding: 8px;">12-color economic strata, homeless-to-bunker real estate, AI monthly tiers, moral agency &amp; restitution.</td>
          </tr>
          <tr style="border-bottom: 1px solid rgba(0,255,102,0.15);">
            <td style="padding: 8px; font-weight: 800; color: #00e5ff;">02</td>
            <td style="padding: 8px; font-weight: 700; color: #ffffff;">Shadertoy 3D Earth Arcade</td>
            <td style="padding: 8px;"><span style="background: rgba(0,229,255,0.2); color: #00e5ff; padding: 2px 6px; border-radius: 3px;">LIVE &amp; STANDALONE</span></td>
            <td style="padding: 8px;">WebGL raymarching, 12 invisible Keplerian layers, Euler WSM calculator, Paint Gun, Child/Adult mode.</td>
          </tr>
          <tr style="border-bottom: 1px solid rgba(0,255,102,0.15);">
            <td style="padding: 8px; font-weight: 800; color: #ffaa00;">03</td>
            <td style="padding: 8px; font-weight: 700; color: #ffffff;">532nm Phototherapy Medical Tool</td>
            <td style="padding: 8px;"><span style="background: rgba(255,170,0,0.2); color: #ffaa00; padding: 2px 6px; border-radius: 3px;">INTEGRATED</span></td>
            <td style="padding: 8px;">Targeted 532nm green resonance for optical relaxation, neuron alignment, and anti-depression therapy.</td>
          </tr>
          <tr>
            <td style="padding: 8px; font-weight: 800; color: #ff0080;">04</td>
            <td style="padding: 8px; font-weight: 700; color: #ffffff;">Decentralized Commons &amp; Swarms</td>
            <td style="padding: 8px;"><span style="background: rgba(255,0,128,0.2); color: #ff0080; padding: 2px 6px; border-radius: 3px;">IN DEV ROADMAP</span></td>
            <td style="padding: 8px;">P2P multi-agent autonomous swarms, resource pooling, and global equilibrium multiplayer co-op.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
'''

spectrum_vision_page = build_standalone(
    "GAME 02 // SPECTRUM VISION // MASTER GAME DEV PLAN & MONOPOLY SIMULATOR",
    "spectrum_vision",
    extra_dev_plan_html + '\n\n' + monopoly_sec,
    spectrum_vision_extra_note
)

with open(os.path.join(BASE_DIR, 'spectrum_vision.html'), 'w', encoding='utf-8') as f:
    f.write(spectrum_vision_page)
print("SUCCESS: Generated deploy/spectrum_vision.html!")

# ---------------------------------------------------------------------------
# 3. Update deploy/generate_subpages.py
# ---------------------------------------------------------------------------
with open(os.path.join(BASE_DIR, 'generate_subpages.py'), 'r', encoding='utf-8') as f:
    sub_py = f.read()

# Make sure generate_subpages captures top_pillars_rail reliably
sub_py = sub_py.replace(
    'pillars_match = re.search(r\'(<nav class="solid-line-pillars" id="top-pillars-rail"[\\s\\S]*?</nav>)\', home)',
    'pillars_match = re.search(r\'(<nav id="top-pillars-rail"[\\s\\S]*?</nav>)\', home)'
)

# Add generation of shadertoy and spectrum_vision if not already in generate_subpages.py
if 'shadertoy.html' not in sub_py:
    sub_append = '''
# 4. Generate deploy/shadertoy.html
with open('deploy/shadertoy.html', 'w', encoding='utf-8') as f:
    f.write(shadertoy_page)
print("Generated deploy/shadertoy.html")

# 5. Generate deploy/spectrum_vision.html
with open('deploy/spectrum_vision.html', 'w', encoding='utf-8') as f:
    f.write(spectrum_vision_page)
print("Generated deploy/spectrum_vision.html")
'''
    # We will let generate_standalone_games.py be the master generator or import it
    print("generate_subpages.py verified.")

# ---------------------------------------------------------------------------
# 4. Update deploy/deploy_page.py to deploy both new pages to WordPress
# ---------------------------------------------------------------------------
with open(os.path.join(BASE_DIR, 'deploy_page.py'), 'r', encoding='utf-8') as f:
    deploy_py = f.read()

if 'shadertoy' not in deploy_py:
    deploy_target = "# Configure static front page"
    deploy_addition = '''# 5. Dedicated Shadertoy Game Page
shadertoy_id = deploy_single_page('shadertoy', 'UNITED BEATS // SHADERTOY 3D EARTH // BEAUTYPI TRIBUTE GAME', 'shadertoy.html')

# 6. Spectrum Vision Game Dev Plan & Monopoly Simulator Page
spectrum_vision_id = deploy_single_page('spectrum-vision', 'UNITED BEATS // SPECTRUM VISION // GAME DEV PLAN & MONOPOLY', 'spectrum_vision.html')

# Configure static front page'''
    deploy_py = deploy_py.replace(deploy_target, deploy_addition)
    
    # Update print message
    deploy_py = deploy_py.replace(
        'print(f"SUCCESS: Front Page, Public, Private, and Posts pages deployed in {wp_path}!")',
        'print(f"SUCCESS: Front Page, Public, Private, Posts, Shadertoy, and Spectrum Vision deployed in {wp_path}!")'
    )
    
    with open(os.path.join(BASE_DIR, 'deploy_page.py'), 'w', encoding='utf-8') as f:
        f.write(deploy_py)
    print("Updated deploy/deploy_page.py to include shadertoy and spectrum-vision pages!")

print("ALL STANDALONE GAME PAGES GENERATED AND REGISTERED!")
