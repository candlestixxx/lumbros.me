#!/usr/bin/env python3
"""
Generates all subpages from homepage.html:
1. deploy/posts.html           (/posts/)
2. deploy/public.html          (/public/)
3. deploy/private.html         (/private/)
4. deploy/shadertoy.html       (/shadertoy/)
5. deploy/spectrum_vision.html  (/spectrum-vision/)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# Extract <style>...</style> block
style_match = re.search(r'(<style>[\s\S]*?</style>)', home)
styles = style_match.group(1) if style_match else ''

# Extract <script>...</script> block
script_match = re.search(r'(<script>[\s\S]*?</script>)', home)
scripts = script_match.group(1) if script_match else ''

# Extract ASCII Header
header_match = re.search(r'(<header class="ascii-hero">[\s\S]*?</header>)', home)
ascii_header = header_match.group(1) if header_match else ''

# Extract Top Pillars Navigation Rail
pillars_match = re.search(r'(<nav id="top-pillars-rail"[\s\S]*?</nav>)', home)
top_pillars_rail = pillars_match.group(1) if pillars_match else ''

# Extract Public Section
public_match = re.search(r'(<section id="public-pages"[\s\S]*?</section>)', home)
public_sec = public_match.group(1) if public_match else ''

# Extract Private Section
private_match = re.search(r'(<section id="private-pages"[\s\S]*?</section>)', home)
private_sec = private_match.group(1) if private_match else ''

# Extract Live Posts Section
posts_match = re.search(r'(<section id="live-posts"[\s\S]*?</section>)', home)
posts_sec = posts_match.group(1) if posts_match else ''

# Extract Shadertoy Section
shadertoy_match = re.search(r'(<section id="shadertoy-tribute"[\s\S]*?</section>)', home)
shadertoy_sec = shadertoy_match.group(1) if shadertoy_match else ''

# Extract Spectrum Monopoly Section
monopoly_match = re.search(r'(<section id="spectrum-monopoly"[\s\S]*?</section>)', home)
monopoly_sec = monopoly_match.group(1) if monopoly_match else ''

# Extract Footer
footer_match = re.search(r'(<footer class="terminal-footer">[\s\S]*?</footer>)', home)
footer = footer_match.group(1) if footer_match else ''

# Extract YouTube Audio Engine
audio_hud_match = re.search(r'(<!-- YouTube Audio Engine -->[\s\S]*?<!-- End YouTube Audio Engine -->)', home)
audio_hud = audio_hud_match.group(1) if audio_hud_match else ''

def build_page(page_title, active_slug, main_content_html, extra_badge=""):
    return f'''<div class="terminal-wrapper theme-cyberpunk">
  <!-- Top Terminal HUD Banner -->
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
  </div>

  {top_pillars_rail}

  {ascii_header}

  <!-- Page Breadcrumbs -->
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
    {extra_badge}
  </div>

  {main_content_html}

  {footer}

  {audio_hud}

  {styles}

  {scripts}
</div>'''

# 1. Generate deploy/posts.html
posts_page = build_page("LIVE POSTS // TRANSMISSION DIARY & REAL-TIME COMMENTS", "posts", posts_sec)
with open(os.path.join(BASE_DIR, 'posts.html'), 'w', encoding='utf-8') as f:
    f.write(posts_page)
print("Generated deploy/posts.html")

# 2. Generate deploy/public.html
public_page = build_page("PUBLIC SECTOR // OPEN ARCHIVES & ROTATING PROJECTS", "public", public_sec)
with open(os.path.join(BASE_DIR, 'public.html'), 'w', encoding='utf-8') as f:
    f.write(public_page)
print("Generated deploy/public.html")

# 3. Generate deploy/private.html
private_page = build_page("PRIVATE SECTOR // CLASSIFIED CIPHER VAULT", "private", private_sec)
with open(os.path.join(BASE_DIR, 'private.html'), 'w', encoding='utf-8') as f:
    f.write(private_page)
print("Generated deploy/private.html")

# 4. Generate deploy/shadertoy.html
shadertoy_extra = '''
    <div style="margin-top: 8px; font-size: 0.73rem; color: #a0f0c0; line-height: 1.4; border-top: 1px dashed rgba(0,255,102,0.25); padding-top: 6px;">
      <span style="color: #00ffcc; font-weight: 800;">DEDICATED STANDALONE GAME:</span> 3D Earth WebGL Raymarching Engine &bull; Homage to <strong>I&ntilde;igo Qu&iacute;lez</strong> &amp; <strong>Pol Jeremias</strong> (via Beautypi) &bull; Wave Structure of Matter (Euler&rsquo;s Wave Identity e^{i&pi;} + 1 = 0) &bull; Phototherapy Wellness Tool.
    </div>'''
shadertoy_page = build_page("GAME 01 // SHADERTOY 3D EARTH // BEAUTYPI TRIBUTE", "shadertoy", shadertoy_sec, shadertoy_extra)
with open(os.path.join(BASE_DIR, 'shadertoy.html'), 'w', encoding='utf-8') as f:
    f.write(shadertoy_page)
print("Generated deploy/shadertoy.html")

# 5. Generate deploy/spectrum_vision.html
dev_plan_html = '''  <!-- =========================================================================
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
          <tr style="border-bottom: 1px solid rgba(0,229,255,0.15);">
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
  </section>'''

spectrum_vision_extra = '''
    <div style="margin-top: 8px; font-size: 0.73rem; color: #a0f0c0; line-height: 1.4; border-top: 1px dashed rgba(0,255,102,0.25); padding-top: 6px;">
      <span style="color: #00ff66; font-weight: 800;">GAME DEV PLAN &amp; SIMULATOR:</span> Planetary Survival Gauges &bull; Macro-Global to Local Financial Architecture &bull; 12 Spectrum Economic Strata (Homeless to Billionaire Bunker) &bull; AI Monthly Tiers &bull; Moral Agency &amp; Path of Restitution.
    </div>'''

spectrum_vision_page = build_page("GAME 02 // SPECTRUM VISION // MASTER GAME DEV PLAN & MONOPOLY SIMULATOR", "spectrum_vision", dev_plan_html + '\n\n' + monopoly_sec, spectrum_vision_extra)
with open(os.path.join(BASE_DIR, 'spectrum_vision.html'), 'w', encoding='utf-8') as f:
    f.write(spectrum_vision_page)
print("Generated deploy/spectrum_vision.html")
print("ALL SUBPAGES GENERATED SUCCESSFULLY!")
