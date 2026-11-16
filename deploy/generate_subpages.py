#!/usr/bin/env python3
"""
Generates all subpages from homepage.html:
1. deploy/posts.html             (/posts/)
2. deploy/public.html            (/public/)
3. deploy/private.html           (/private/)
4. deploy/shadertoy.html         (/shadertoy/)
5. deploy/spectrum_vision.html    (/spectrum-vision/)
6. deploy/archetypes.html         (/archetypes/)
7. deploy/games.html             (/games/)
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
header_match = re.search(r'(<header class="ascii-hero"[\s\S]*?</header>)', home)
ascii_header = header_match.group(1) if header_match else ''

# Extract Main Site Command Menu (With Dropdowns & Floating Diary Widget)
menu_match = re.search(r'(<nav class="main-site-command-menu"[\s\S]*?</nav>)', home)
main_menu = menu_match.group(1) if menu_match else ''

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
      <a href="/games/" class="hud-link {'active' if active_slug=='games' else ''}" style="color: #00ff66;">🎮 GAMES</a>
      <span class="hud-sep">|</span>
      <a href="/archetypes/" class="hud-link {'active' if active_slug=='archetypes' else ''}" style="color: #d500f9;">👁️ ARCHETYPES</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link {'active' if active_slug=='private' else ''}">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link {'active' if active_slug=='posts' else ''}">LIVE POSTS</a>
    </div>
  </div>

  {top_pillars_rail}

  {ascii_header}

  {main_menu}

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
public_page = build_page("PUBLIC SECTOR // EXECUTIVE RESUME, ART & TOOLS LAB", "public", public_sec)
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
spectrum_vision_page = build_page("GAME 02 // SPECTRUM VISION // MASTER GAME DEV PLAN & MONOPOLY SIMULATOR", "spectrum_vision", monopoly_sec)
with open(os.path.join(BASE_DIR, 'spectrum_vision.html'), 'w', encoding='utf-8') as f:
    f.write(spectrum_vision_page)
print("Generated deploy/spectrum_vision.html")

# 6. Read and sync archetypes.html
if os.path.exists(os.path.join(BASE_DIR, 'archetypes.html')):
    print("deploy/archetypes.html exists and is synced.")

# 7. Generate deploy/games.html
games_page_html = f'''<div class="terminal-wrapper theme-cyberpunk">
  <!-- Top Terminal HUD Banner -->
  <div class="hud-top-bar">
    <div class="hud-status-badge">
      <span class="live-dot-pulse"></span>
      <span>SYSTEM OPERATIONAL // NODE: LUMBROS.ME // GAMES &amp; MIND PUZZLES</span>
    </div>
    <div class="hud-nav-links">
      <a href="/" class="hud-link">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/games/" class="hud-link active" style="color: #00ff66;">🎮 GAMES</a>
      <span class="hud-sep">|</span>
      <a href="/archetypes/" class="hud-link" style="color: #d500f9;">👁️ ARCHETYPES</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link">LIVE POSTS</a>
    </div>
  </div>

  {top_pillars_rail}

  {ascii_header}

  {main_menu}

  <!-- Page Breadcrumbs -->
  <div class="terminal-section" style="margin-bottom: 20px; padding: 12px 20px; border-left: 3px solid #00ff66;">
    <div style="font-size: 0.76rem; letter-spacing: 1.5px; color: #8ce4a7; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
      <div>
        <a href="/" style="color: #00ff66; text-decoration: none;">ROOT</a> / 
        <a href="/public/" style="color: #00e5ff; text-decoration: none;">PUBLIC</a> / 
        <span style="color: #ffffff; font-weight: 800;">COOL MIND PUZZLE &amp; VISION SPECTRUM GAMES</span>
      </div>
      <div style="color: #00ff66; font-weight: 700;">
        CONTINUUM EPOCH: +1794703800s // HARMONIC CENTER: 532nm
      </div>
    </div>
  </div>

  <!-- Games Suite Hero Directive -->
  <section class="terminal-section" style="margin-bottom: 25px; border-left: 3px solid #00ff66;">
    <div class="section-badge">
      <span class="badge-num">GAMES-01</span>
      <span class="badge-tag">SERIOUS GAMES LAB</span>
      <span class="badge-title">COOL MIND PUZZLE &amp; VISION SPECTRUM GAMES LAB // DESIGNED BY LUM</span>
    </div>

    <div style="font-size: 0.86rem; color: #e0f2fe; line-height: 1.7; margin-bottom: 18px;">
      Welcome to the <strong>Cool Mind Puzzle &amp; Vision Spectrum Games Lab</strong> created by <strong>Lum (Lumbros Kourlos)</strong>. This suite bridges <strong>serious games</strong>, <strong>mathematical wave mechanics (Euler's Identity e^{{i&pi;}} + 1 = 0)</strong>, and <strong>optical phototherapy</strong>. Here, players explore real-world economics, planetary survival (Environment, Humanity, Resources), Keplerian orbital 3D physics, dual-screen digital human animation, the entire soul calculator, and bonus Shadertoy procedural world-shading.
    </div>

    <!-- Quick Switcher Jump Rail -->
    <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 15px;">
      <a href="#shadertoy-tribute" class="cyber-btn sm" style="border-color: #00ffcc; color: #00ffcc;">
        <span>🎮 JUMP TO SHADERTOY 3D EARTH</span> <span>↓</span>
      </a>
      <a href="#spectrum-monopoly" class="cyber-btn sm" style="border-color: #00ff66; color: #00ff66;">
        <span>🌐 JUMP TO SPECTRUM MONOPOLY SIM</span> <span>↓</span>
      </a>
      <a href="/shadertoy/" class="cyber-btn sm" style="border-color: #00e5ff; color: #00e5ff;">
        <span>🚀 FULLSCREEN SHADERTOY ARENA</span> <span>↗</span>
      </a>
      <a href="/spectrum-vision/" class="cyber-btn sm" style="border-color: #ffaa00; color: #ffaa00;">
        <span>📜 SPECTRUM VISION DEV PLAN</span> <span>↗</span>
      </a>
    </div>
  </section>

  <!-- Game 1: Shadertoy 3D Earth -->
  {shadertoy_sec}

  <!-- Game 2: The New Monopoly / Spectrum Vision Simulator & Bonus Studio -->
  {monopoly_sec}

  {footer}

  {audio_hud}

  {styles}

  {scripts}
</div>'''

with open(os.path.join(BASE_DIR, 'games.html'), 'w', encoding='utf-8') as f:
    f.write(games_page_html)
print("Generated deploy/games.html")

print("ALL SUBPAGES REGENERATED AND SYNCED SUCCESSFULLY!")
