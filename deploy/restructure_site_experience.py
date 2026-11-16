#!/usr/bin/env python3
"""
Restructures Lumbros.me according to the user's architectural vision:
1. Compact Top "Choose Your Spectrum Experience" invitation & skills display:
   - Removes the large 14KB archetype module from the top deck so it does NOT take up so much vertical space
   - Keeps the sleek Acuity gauge (20/200 -> 20/20 -> 20/10), polarity toggle, and 12-color preview
   - Links cleanly to the dedicated Archetypes page
2. Dedicated Standalone Page: Psychological Archetype Spectrum Resonance Matrix (/archetypes/)
3. Dedicated Standalone Public Page: COOL MIND PUZZLE & VISION SPECTRUM GAMES (/games/)
4. New Main Menu immediately after the United Beats intro company logo (3D ASCII Header):
   - Menu options for Public Pages (Games, Resume, Platforms), Private Pages (Vault), Archetypes
5. Live Diary & Real-Time Comments Section on the Menu Bar:
   - Deep black box
   - Invisible 12-color spectrum layer over the black box
   - 2 parallel lines of circles (12 vertical pairs) that harmonically & rhythmically float
   - Mouse hover reflects whatever position & color it is hovering over on the invisible spectrum
   - Rhythmic floating standing-wave motion to balance and keep user engaged
6. Ensures 0 raw '&&' inside script tags (100% WordPress entity safe)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# ---------------------------------------------------------------------------
# 1. Extract the Psychological Archetype Module before removing it
# ---------------------------------------------------------------------------
pos_arch_start = home.find('<!-- Module 3: Psychological Archetype')
pos_arch_end = home.find('<!-- Scanline & Ambient Overlay -->', pos_arch_start)

archetype_html_content = ""
if pos_arch_start != -1 and pos_arch_end != -1:
    archetype_html_content = home[pos_arch_start:pos_arch_end].strip()
    print(f"Extracted Psychological Archetype Module ({len(archetype_html_content)} chars)")

# ---------------------------------------------------------------------------
# 2. Make the Top "Choose Your Spectrum Experience" Deck Compact & Sleek
# ---------------------------------------------------------------------------
# Replace the huge archetype block in homepage with a compact invitation footer
compact_archetype_link = '''        <!-- Compact Archetype Portal Strip -->
        <div class="compact-archetype-invite-strip" style="grid-column: 1 / -1; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; background: rgba(5,14,24,0.7); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 10px 16px; margin-top: 10px;">
          <div style="font-size: 0.76rem; color: #b8e2c8;">
            <span style="color: #00ff66; font-weight: 800;">12 PSYCHOLOGICAL ARCHETYPES:</span> Common human key images &amp; cognitive geometry are now in a dedicated resonance chamber.
          </div>
          <div>
            <a href="/archetypes/" class="cyber-btn sm" style="border-color: #00ff66; color: #00ff66; text-decoration: none; font-size: 0.72rem; padding: 4px 12px; font-weight: 800;">
              <span>ENTER ARCHETYPE RESONANCE MATRIX</span> <span>↗</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>'''

if pos_arch_start != -1 and pos_arch_end != -1:
    home = home[:pos_arch_start] + compact_archetype_link + '\n\n  ' + home[pos_arch_end:]
    print("Streamlined top vision deck into compact format in homepage.html!")

# ---------------------------------------------------------------------------
# 3. Build the Rhythmic Floating Harmonic Spectrum Diary & Comments Widget
# ---------------------------------------------------------------------------
diary_spectrum_widget_html = '''
    <!-- =======================================================================
         RHYTHMIC FLOATING HARMONIC SPECTRUM DIARY & COMMENTS WIDGET
         BLACK BOX // INVISIBLE 12-COLOR SPECTRUM // 2 PARALLEL LINES OF CIRCLES
         ======================================================================= -->
    <div class="diary-spectrum-dock" id="diary-spectrum-dock">
      <div class="diary-dock-top">
        <div class="diary-title-group">
          <span class="live-dot-pulse"></span>
          <span class="diary-dock-title">LIVE TRANSMISSION DIARY &amp; COMMENTS</span>
          <span class="diary-dock-tag">[HARMONIC OSCILLATOR]</span>
        </div>
        <div class="diary-telemetry-text" id="diary-spectrum-telemetry">
          HOVER OVER INVISIBLE SPECTRUM FIELD // HARMONIC WAVE RHYTHM // CLICK TO TRANSMIT
        </div>
      </div>

      <!-- The Black Box with Invisible Spectrum & 2 Parallel Lines of Floating Circles -->
      <a href="/posts/" class="diary-blackbox-track" id="diary-blackbox-track" title="Click to Read Lum's Live Transmission Diary &amp; Post Comments">
        
        <!-- Invisible 12-Color Spectrum Backplane (12 Equal Columns from 660nm to 410nm) -->
        <div class="invisible-spectrum-backplane" id="invisible-spectrum-backplane">
          <div class="spectrum-zone" data-idx="0" data-wl="660nm" data-name="Crimson Ground" data-color="#ff1744"></div>
          <div class="spectrum-zone" data-idx="1" data-wl="630nm" data-name="Coral Pulse" data-color="#ff5722"></div>
          <div class="spectrum-zone" data-idx="2" data-wl="600nm" data-name="Amber Tone" data-color="#ff9100"></div>
          <div class="spectrum-zone" data-idx="3" data-wl="580nm" data-name="Gold Harmony" data-color="#ffc400"></div>
          <div class="spectrum-zone" data-idx="4" data-wl="560nm" data-name="Lime Wave" data-color="#c6ff00"></div>
          <div class="spectrum-zone center-zone" data-idx="5" data-wl="532nm" data-name="Emerald Center ★" data-color="#00ff66"></div>
          <div class="spectrum-zone" data-idx="6" data-wl="515nm" data-name="Mint Focus" data-color="#00e676"></div>
          <div class="spectrum-zone" data-idx="7" data-wl="495nm" data-name="Cyan Dispersion" data-color="#00e5ff"></div>
          <div class="spectrum-zone" data-idx="8" data-wl="470nm" data-name="Cobalt Resonance" data-color="#2979ff"></div>
          <div class="spectrum-zone" data-idx="9" data-wl="440nm" data-name="Indigo Depth" data-color="#651fff"></div>
          <div class="spectrum-zone" data-idx="10" data-wl="420nm" data-name="Violet Horizon" data-color="#d500f9"></div>
          <div class="spectrum-zone" data-idx="11" data-wl="410nm" data-name="Magenta Zenith" data-color="#ff4081"></div>
        </div>

        <!-- 2 Parallel Lines of Circles (Floating Harmonic Dots) -->
        <div class="harmonic-circles-container" id="harmonic-circles-container">
          <!-- Line 1: Upper Parallel Row (12 Circles) -->
          <div class="parallel-circles-line top-line" id="circles-top-line">
            <span class="harmonic-circle dot-0" data-idx="0"></span>
            <span class="harmonic-circle dot-1" data-idx="1"></span>
            <span class="harmonic-circle dot-2" data-idx="2"></span>
            <span class="harmonic-circle dot-3" data-idx="3"></span>
            <span class="harmonic-circle dot-4" data-idx="4"></span>
            <span class="harmonic-circle dot-5 is-center" data-idx="5"></span>
            <span class="harmonic-circle dot-6" data-idx="6"></span>
            <span class="harmonic-circle dot-7" data-idx="7"></span>
            <span class="harmonic-circle dot-8" data-idx="8"></span>
            <span class="harmonic-circle dot-9" data-idx="9"></span>
            <span class="harmonic-circle dot-10" data-idx="10"></span>
            <span class="harmonic-circle dot-11" data-idx="11"></span>
          </div>

          <!-- Line 2: Lower Parallel Row (12 Circles) -->
          <div class="parallel-circles-line bottom-line" id="circles-bottom-line">
            <span class="harmonic-circle dot-0" data-idx="0"></span>
            <span class="harmonic-circle dot-1" data-idx="1"></span>
            <span class="harmonic-circle dot-2" data-idx="2"></span>
            <span class="harmonic-circle dot-3" data-idx="3"></span>
            <span class="harmonic-circle dot-4" data-idx="4"></span>
            <span class="harmonic-circle dot-5 is-center" data-idx="5"></span>
            <span class="harmonic-circle dot-6" data-idx="6"></span>
            <span class="harmonic-circle dot-7" data-idx="7"></span>
            <span class="harmonic-circle dot-8" data-idx="8"></span>
            <span class="harmonic-circle dot-9" data-idx="9"></span>
            <span class="harmonic-circle dot-10" data-idx="10"></span>
            <span class="harmonic-circle dot-11" data-idx="11"></span>
          </div>
        </div>

        <!-- Central Equilibrium Indicator -->
        <div class="center-meridian-indicator">
          <span class="meridian-dot"></span>
          <span class="meridian-text">532nm CENTER</span>
        </div>
      </a>
    </div>
'''

# ---------------------------------------------------------------------------
# 4. Build the New Main Navigation Menu (Placed after the United Beats Logo)
# ---------------------------------------------------------------------------
main_menu_html = f'''  <!-- =========================================================================
       NEW MAIN SITE NAVIGATION MENU (LOCATED AFTER THE UNITED BEATS LOGO)
       PUBLIC & PRIVATE PAGES // COOL MIND PUZZLES & SPECTRUM GAMES // LIVE DIARY
       ========================================================================= -->
  <nav class="main-site-command-menu" id="main-site-command-menu" aria-label="Main Navigation Menu">
    <div class="menu-rail-container">
      
      <!-- Primary Command Navigation Links Track -->
      <div class="menu-primary-links-row">
        
        <!-- Root System -->
        <a href="/" class="menu-pill-btn pill-root active" title="Return to Root HyperNexus">
          <span class="pill-icon">⌂</span>
          <span class="pill-label">ROOT SYSTEM</span>
        </a>

        <!-- Public Pages Dropdown Hub -->
        <div class="menu-dropdown-wrapper">
          <a href="/public/" class="menu-pill-btn pill-public" title="Public Pages &amp; Open Releases">
            <span class="pill-icon">🌐</span>
            <span class="pill-label">PUBLIC PAGES ▾</span>
          </a>
          <div class="menu-dropdown-flyout">
            <a href="/games/" class="flyout-link highlight-green">
              <span class="flyout-icon">🎮</span>
              <div>
                <div class="flyout-title">COOL MIND PUZZLE &amp; VISION SPECTRUM GAMES</div>
                <div class="flyout-sub">Shadertoy 3D Earth &bull; Monopoly &bull; Euler WSM</div>
              </div>
            </a>
            <a href="/public/" class="flyout-link">
              <span class="flyout-icon">📄</span>
              <div>
                <div class="flyout-title">EXECUTIVE RESUME &amp; STATEMENTS</div>
                <div class="flyout-sub">Lumbros Kourlos &bull; Systems Architecture &bull; Physics</div>
              </div>
            </a>
            <a href="/public/" class="flyout-link">
              <span class="flyout-icon">🏢</span>
              <div>
                <div class="flyout-title">PRODUCTION SYSTEMS &amp; REPOSITORIES</div>
                <div class="flyout-sub">United Beats &bull; HyperNexus &bull; Candlestixxx GitHub</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Featured Public Item: Cool Mind Puzzle & Vision Spectrum Games -->
        <a href="/games/" class="menu-pill-btn pill-games highlight-neon-pulse" title="Play Serious Games &amp; Mind Puzzles Built by Lum">
          <span class="pill-icon">🎮</span>
          <span class="pill-label">COOL MIND PUZZLE &amp; VISION SPECTRUM GAMES</span>
          <span class="pill-badge-play">PLAY NOW</span>
        </a>

        <!-- Psychological Archetype Spectrum Resonance Matrix (Dedicated Page) -->
        <a href="/archetypes/" class="menu-pill-btn pill-archetypes" title="Explore the 12 Psychological Archetypes &amp; Optical Resonance Matrix">
          <span class="pill-icon">👁️</span>
          <span class="pill-label">PSYCH ARCHETYPES</span>
        </a>

        <!-- Private Pages Dropdown Hub -->
        <div class="menu-dropdown-wrapper">
          <a href="/private/" class="menu-pill-btn pill-private" title="Private Classified Vault &amp; Ciphers">
            <span class="pill-icon">🔐</span>
            <span class="pill-label">PRIVATE PAGES ▾</span>
          </a>
          <div class="menu-dropdown-flyout">
            <a href="/private/" class="flyout-link">
              <span class="flyout-icon">🗝️</span>
              <div>
                <div class="flyout-title">4096-BIT RADIAL VECTOR CIPHER VAULT</div>
                <div class="flyout-sub">Classified Cryptographic Keys &bull; Radial Vector Storage</div>
              </div>
            </a>
          </div>
        </div>

      </div>

      <!-- Integrated Live Diary Rhythmic Harmonic Spectrum Widget -->
      {diary_spectrum_widget_html}

    </div>
  </nav>
'''

# ---------------------------------------------------------------------------
# 5. Insert the New Main Navigation Menu after the ASCII Hero Header Logo
# ---------------------------------------------------------------------------
header_close_tag = '</header>'
if header_close_tag in home:
    # Check if main-site-command-menu is already present
    if 'main-site-command-menu' not in home:
        home = home.replace(header_close_tag, header_close_tag + '\n\n' + main_menu_html, 1)
        print("Injected New Main Navigation Menu after the United Beats ASCII header logo!")

# ---------------------------------------------------------------------------
# 6. Add CSS for Menu & Rhythmic Floating Harmonic Spectrum Widget
# ---------------------------------------------------------------------------
menu_and_widget_css = '''
  /* =========================================================================
     MAIN SITE NAVIGATION MENU & RHYTHMIC FLOATING SPECTRUM DIARY WIDGET
     ========================================================================= */
  .main-site-command-menu {
    position: relative;
    z-index: 100;
    margin: 15px auto 25px auto;
    max-width: 1200px;
    padding: 0 10px;
  }
  .menu-rail-container {
    background: rgba(4, 10, 18, 0.94);
    border: 1px solid rgba(0, 255, 102, 0.35);
    border-radius: 8px;
    padding: 14px 18px;
    box-shadow: 0 0 30px rgba(0, 255, 102, 0.12);
  }
  .menu-primary-links-row {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 14px;
    border-bottom: 1px solid rgba(0, 255, 102, 0.2);
    padding-bottom: 12px;
  }
  .menu-pill-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    background: rgba(0, 20, 35, 0.8);
    border: 1px solid rgba(0, 229, 255, 0.3);
    border-radius: 4px;
    color: #e0f2fe;
    text-decoration: none;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 1px;
    transition: all 0.2s ease;
  }
  .menu-pill-btn:hover {
    background: rgba(0, 255, 102, 0.18);
    border-color: #00ff66;
    color: #00ff66;
    box-shadow: 0 0 12px rgba(0, 255, 102, 0.3);
  }
  .menu-pill-btn.active {
    background: rgba(0, 255, 102, 0.25);
    border-color: #00ff66;
    color: #00ff66;
  }
  .menu-pill-btn.highlight-neon-pulse {
    border-color: #00ff66;
    color: #00ff66;
    background: linear-gradient(90deg, rgba(0,255,102,0.12) 0%, rgba(0,229,255,0.12) 100%);
    box-shadow: 0 0 10px rgba(0, 255, 102, 0.25);
  }
  .pill-badge-play {
    background: #00ff66;
    color: #040a12;
    font-size: 0.62rem;
    font-weight: 900;
    padding: 1px 6px;
    border-radius: 3px;
    letter-spacing: 1px;
    margin-left: 4px;
  }
  /* Dropdowns */
  .menu-dropdown-wrapper {
    position: relative;
    display: inline-block;
  }
  .menu-dropdown-flyout {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    min-width: 280px;
    background: rgba(5, 14, 24, 0.98);
    border: 1px solid #00ff66;
    border-radius: 6px;
    padding: 8px 0;
    box-shadow: 0 8px 30px rgba(0,0,0,0.8), 0 0 15px rgba(0,255,102,0.25);
    z-index: 999;
  }
  .menu-dropdown-wrapper:hover .menu-dropdown-flyout {
    display: block;
  }
  .flyout-link {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 14px;
    color: #e0f2fe;
    text-decoration: none;
    border-bottom: 1px solid rgba(0,255,102,0.1);
    transition: background 0.2s ease;
  }
  .flyout-link:hover {
    background: rgba(0, 255, 102, 0.15);
    color: #00ff66;
  }
  .flyout-title {
    font-size: 0.72rem;
    font-weight: 800;
    color: #ffffff;
  }
  .flyout-sub {
    font-size: 0.65rem;
    color: #8ce4a7;
  }

  /* Live Diary Spectrum Dock Widget */
  .diary-spectrum-dock {
    margin-top: 10px;
    background: #020509;
    border: 1px solid rgba(0, 229, 255, 0.35);
    border-radius: 6px;
    padding: 10px 14px;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.9);
  }
  .diary-dock-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 8px;
  }
  .diary-title-group {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .diary-dock-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.78rem;
    font-weight: 800;
    color: #00ff66;
    letter-spacing: 1.5px;
  }
  .diary-dock-tag {
    font-size: 0.65rem;
    color: #00e5ff;
    font-weight: 700;
  }
  .diary-telemetry-text {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem;
    color: #8ce4a7;
  }

  /* The Black Box Track */
  .diary-blackbox-track {
    position: relative;
    display: block;
    height: 52px;
    background: #000000;
    border: 1px solid rgba(0, 255, 102, 0.4);
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    text-decoration: none;
    box-shadow: inset 0 0 25px rgba(0,0,0,1);
  }
  .invisible-spectrum-backplane {
    position: absolute;
    inset: 0;
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    opacity: 0.08;
    pointer-events: auto;
  }
  .invisible-spectrum-backplane:hover {
    opacity: 0.22;
  }
  .spectrum-zone {
    height: 100%;
    border-right: 1px solid rgba(255,255,255,0.05);
  }
  .spectrum-zone.center-zone {
    background: rgba(0, 255, 102, 0.15);
    border-left: 1px solid rgba(0,255,102,0.4);
    border-right: 1px solid rgba(0,255,102,0.4);
  }

  /* 2 Parallel Lines of Circles (Harmonic Floating Dots) */
  .harmonic-circles-container {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 4px 0;
    pointer-events: none;
  }
  .parallel-circles-line {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    align-items: center;
    justify-items: center;
    width: 100%;
  }
  .harmonic-circle {
    display: block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(0, 255, 102, 0.5);
    border: 1px solid #00ff66;
    box-shadow: 0 0 6px rgba(0, 255, 102, 0.4);
    transition: transform 0.1s ease, background 0.15s ease, box-shadow 0.15s ease;
  }
  .harmonic-circle.is-center {
    width: 12px;
    height: 12px;
    background: #00ff66;
    box-shadow: 0 0 10px #00ff66;
  }

  /* Center Meridian Indicator */
  .center-meridian-indicator {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    align-items: center;
    gap: 4px;
    background: rgba(5, 15, 25, 0.85);
    border: 1px solid #00ff66;
    border-radius: 3px;
    padding: 1px 6px;
    pointer-events: none;
  }
  .meridian-dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #00ff66;
    box-shadow: 0 0 6px #00ff66;
  }
  .meridian-text {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    font-weight: 800;
    color: #00ff66;
    letter-spacing: 1px;
  }
'''

if '/* MAIN SITE NAVIGATION MENU & RHYTHMIC FLOATING SPECTRUM DIARY WIDGET */' not in home:
    style_end = '</style>'
    home = home.replace(style_end, menu_and_widget_css + '\n  ' + style_end, 1)
    print("Injected CSS for Menu & Rhythmic Floating Spectrum Diary Widget!")

# ---------------------------------------------------------------------------
# 7. Add JavaScript Engine for Rhythmic Floating Dots & Hover Reflection
# ---------------------------------------------------------------------------
# Zero raw '&&'
widget_js_engine = '''
    // =========================================================================
    // RHYTHMIC FLOATING HARMONIC SPECTRUM DIARY WIDGET JAVASCRIPT ENGINE
    // 2 PARALLEL LINES OF 12 CIRCLES // HARMONIC SINE WAVE // HOVER REFLECTION
    // =========================================================================
    (function initDiarySpectrumWidget() {
      var track = document.getElementById('diary-blackbox-track');
      if (!track) return;
      var telemetry = document.getElementById('diary-spectrum-telemetry');

      var spectrumWavelengths = [
        { name: '01. CRIMSON GROUND', wl: '660nm', hex: '#ff1744' },
        { name: '02. CORAL PULSE', wl: '630nm', hex: '#ff5722' },
        { name: '03. AMBER TONE', wl: '600nm', hex: '#ff9100' },
        { name: '04. GOLD HARMONY', wl: '580nm', hex: '#ffc400' },
        { name: '05. LIME WAVE', wl: '560nm', hex: '#c6ff00' },
        { name: '06. EMERALD CENTER ★', wl: '532nm', hex: '#00ff66' },
        { name: '07. MINT FOCUS', wl: '515nm', hex: '#00e676' },
        { name: '08. CYAN DISPERSION', wl: '495nm', hex: '#00e5ff' },
        { name: '09. COBALT RESONANCE', wl: '470nm', hex: '#2979ff' },
        { name: '10. INDIGO DEPTH', wl: '440nm', hex: '#651fff' },
        { name: '11. VIOLET HORIZON', wl: '420nm', hex: '#d500f9' },
        { name: '12. MAGENTA ZENITH', wl: '410nm', hex: '#ff4081' }
      ];

      var topDots = document.querySelectorAll('#circles-top-line .harmonic-circle');
      var bottomDots = document.querySelectorAll('#circles-bottom-line .harmonic-circle');
      var hoveredCol = -1;
      var animTime = 0;

      // Real-time sinusoidal breathing animation
      function animateHarmonicCircles() {
        requestAnimationFrame(animateHarmonicCircles);
        animTime += 0.04;

        for (var i = 0; i < 12; i++) {
          var phase = animTime + i * 0.523; // 2pi / 12 ~ 0.523
          var floatTop = Math.sin(phase) * 5;
          var floatBottom = -Math.sin(phase) * 5;

          var tDot = topDots[i];
          var bDot = bottomDots[i];

          if (tDot) {
            tDot.style.transform = 'translateY(' + floatTop.toFixed(2) + 'px)';
          }
          if (bDot) {
            bDot.style.transform = 'translateY(' + floatBottom.toFixed(2) + 'px)';
          }

          // If not hovered, restore harmonic baseline color
          if (hoveredCol === -1) {
            var lyr = spectrumWavelengths[i];
            if (tDot) {
              tDot.style.background = lyr.hex;
              tDot.style.borderColor = lyr.hex;
              tDot.style.boxShadow = '0 0 6px ' + lyr.hex;
            }
            if (bDot) {
              bDot.style.background = lyr.hex;
              bDot.style.borderColor = lyr.hex;
              bDot.style.boxShadow = '0 0 6px ' + lyr.hex;
            }
          }
        }
      }
      animateHarmonicCircles();

      // Mouse Hover over Invisible Spectrum Field
      track.addEventListener('pointermove', function(e) {
        var rect = track.getBoundingClientRect();
        var relX = e.clientX - rect.left;
        var colWidth = rect.width / 12;
        var col = Math.floor(relX / colWidth);
        if (col < 0) col = 0;
        if (col > 11) col = 11;
        hoveredCol = col;

        var cur = spectrumWavelengths[col];
        if (telemetry) {
          telemetry.innerHTML = 'NODE ' + (col + 1) + ' [' + cur.wl + ' - ' + cur.name + '] // TRANSMISSION DIARY &amp; COMMENTS // CLICK TO TRANSMIT';
          telemetry.style.color = cur.hex;
        }

        // Highlight hovered column circles brilliantly
        for (var i = 0; i < 12; i++) {
          var t = topDots[i];
          var b = bottomDots[i];
          var lyr = spectrumWavelengths[i];

          if (i === col) {
            if (t) {
              t.style.background = cur.hex;
              t.style.borderColor = '#ffffff';
              t.style.boxShadow = '0 0 16px ' + cur.hex + ', 0 0 24px #ffffff';
            }
            if (b) {
              b.style.background = cur.hex;
              b.style.borderColor = '#ffffff';
              b.style.boxShadow = '0 0 16px ' + cur.hex + ', 0 0 24px #ffffff';
            }
          } else {
            if (t) {
              t.style.background = 'rgba(' + (i === 5 ? '0,255,102' : '100,120,140') + ', 0.3)';
              t.style.borderColor = 'rgba(255,255,255,0.2)';
              t.style.boxShadow = 'none';
            }
            if (b) {
              b.style.background = 'rgba(' + (i === 5 ? '0,255,102' : '100,120,140') + ', 0.3)';
              b.style.borderColor = 'rgba(255,255,255,0.2)';
              b.style.boxShadow = 'none';
            }
          }
        }
      });

      track.addEventListener('pointerleave', function() {
        hoveredCol = -1;
        if (telemetry) {
          telemetry.innerHTML = 'HOVER OVER INVISIBLE SPECTRUM FIELD // HARMONIC WAVE RHYTHM // CLICK TO TRANSMIT';
          telemetry.style.color = '#8ce4a7';
        }
      });
    })();
'''

if 'initDiarySpectrumWidget' not in home:
    script_end = '</script>'
    home = home.replace(script_end, widget_js_engine + '\n  ' + script_end, 1)
    print("Injected JavaScript for Diary Spectrum Widget into homepage.html!")

# Save homepage.html
with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)
print("SUCCESS: Updated homepage.html with compact top deck and new main menu!")

# ---------------------------------------------------------------------------
# 8. Generate Standalone Psychological Archetypes Page: deploy/archetypes.html
# ---------------------------------------------------------------------------
# Extract styles, scripts, header, and footer from updated homepage
style_match = re.search(r'(<style>[\s\S]*?</style>)', home)
styles = style_match.group(1) if style_match else ''

script_match = re.search(r'(<script>[\s\S]*?</script>)', home)
scripts = script_match.group(1) if script_match else ''

header_match = re.search(r'(<header class="ascii-hero"[\s\S]*?</header>)', home)
ascii_header = header_match.group(1) if header_match else ''

menu_match = re.search(r'(<nav class="main-site-command-menu"[\s\S]*?</nav>)', home)
main_menu = menu_match.group(1) if menu_match else ''

footer_match = re.search(r'(<footer class="terminal-footer">[\s\S]*?</footer>)', home)
footer = footer_match.group(1) if footer_match else ''

audio_hud_match = re.search(r'(<!-- YouTube Audio Engine -->[\s\S]*?<!-- End YouTube Audio Engine -->)', home)
audio_hud = audio_hud_match.group(1) if audio_hud_match else ''

archetypes_page_html = f'''<div class="terminal-wrapper theme-cyberpunk">
  <!-- Top Terminal HUD Banner -->
  <div class="hud-top-bar">
    <div class="hud-status-badge">
      <span class="live-dot-pulse"></span>
      <span>SYSTEM OPERATIONAL // NODE: LUMBROS.ME // ARCHETYPES</span>
    </div>
    <div class="hud-nav-links">
      <a href="/" class="hud-link">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/games/" class="hud-link" style="color: #00ff66;">🎮 GAMES</a>
      <span class="hud-sep">|</span>
      <a href="/archetypes/" class="hud-link active" style="color: #d500f9;">👁️ ARCHETYPES</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link">LIVE POSTS</a>
    </div>
  </div>

  {ascii_header}

  {main_menu}

  <!-- Page Breadcrumbs -->
  <div class="terminal-section" style="margin-bottom: 20px; padding: 12px 20px; border-left: 3px solid #d500f9;">
    <div style="font-size: 0.76rem; letter-spacing: 1.5px; color: #8ce4a7; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
      <div>
        <a href="/" style="color: #00ff66; text-decoration: none;">ROOT</a> / 
        <span style="color: #ffffff; font-weight: 800;">PSYCHOLOGICAL ARCHETYPE SPECTRUM RESONANCE MATRIX</span>
      </div>
      <div style="color: #d500f9; font-weight: 700;">
        CONTINUUM EPOCH: +1794703800s // 12 HUMAN KEY IMAGES
      </div>
    </div>
  </div>

  <!-- Dedicated Psychological Archetypes Section -->
  <section class="terminal-section" style="margin-bottom: 25px; border-left: 3px solid #d500f9;">
    <div class="section-badge">
      <span class="badge-num">PSYCH-01</span>
      <span class="badge-tag">COGNITIVE GEOMETRY</span>
      <span class="badge-title">12 SPECTRUM ARCHETYPES // HUMAN RESONANCE MATRIX</span>
    </div>

    <div style="font-size: 0.84rem; color: #e0f2fe; line-height: 1.7; margin-bottom: 20px;">
      The <strong>Psychological Archetype Spectrum Resonance Matrix</strong> connects the 12 primary colors of the optical spectrum to fundamental human cognitive archetypes and key symbols. Anchored at the <strong>532nm Emerald Green center</strong> (The Compass Rose), choosing your archetype recalibrates your interface contrast and visual resonance across all tools.
    </div>

    {archetype_html_content}
  </section>

  {footer}

  {audio_hud}

  {styles}

  {scripts}
</div>'''

with open(os.path.join(BASE_DIR, 'archetypes.html'), 'w', encoding='utf-8') as f:
    f.write(archetypes_page_html)
print("SUCCESS: Generated deploy/archetypes.html!")

# ---------------------------------------------------------------------------
# 9. Generate Standalone Games Page: deploy/games.html
# ---------------------------------------------------------------------------
# "COOL MIND PUZZLE & VISION SPECTRUM GAMES"
shadertoy_sec_match = re.search(r'(<section id="shadertoy-tribute"[\s\S]*?</section>)', home)
shadertoy_sec = shadertoy_sec_match.group(1) if shadertoy_sec_match else ''

monopoly_sec_match = re.search(r'(<section id="spectrum-monopoly"[\s\S]*?</section>)', home)
monopoly_sec = monopoly_sec_match.group(1) if monopoly_sec_match else ''

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
      Welcome to the <strong>Cool Mind Puzzle &amp; Vision Spectrum Games Lab</strong> created by <strong>Lum (Lumbros Kourlos)</strong>. This suite bridges <strong>serious games</strong>, <strong>mathematical wave mechanics (Euler's Identity e^{{i&pi;}} + 1 = 0)</strong>, and <strong>optical phototherapy</strong>. Here, players explore real-world economics, planetary survival (Environment, Humanity, Resources), Keplerian orbital 3D physics, and mind-expanding cognitive puzzles.
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

  <!-- Game 2: The New Monopoly / Spectrum Vision Simulator -->
  {monopoly_sec}

  {footer}

  {audio_hud}

  {styles}

  {scripts}
</div>'''

with open(os.path.join(BASE_DIR, 'games.html'), 'w', encoding='utf-8') as f:
    f.write(games_page_html)
print("SUCCESS: Generated deploy/games.html!")

# ---------------------------------------------------------------------------
# 10. Update deploy/deploy_page.py with archetypes and games
# ---------------------------------------------------------------------------
with open(os.path.join(BASE_DIR, 'deploy_page.py'), 'r', encoding='utf-8') as f:
    deploy_code = f.read()

if 'archetypes' not in deploy_code:
    target_deploy = "# 6. Spectrum Vision Game Dev Plan & Monopoly Simulator Page"
    new_deploy_entries = '''# 7. Dedicated Psychological Archetypes Page
archetypes_id = deploy_single_page('archetypes', 'UNITED BEATS // PSYCHOLOGICAL ARCHETYPE SPECTRUM MATRIX', 'archetypes.html')

# 8. Cool Mind Puzzle & Vision Spectrum Games Page
games_id = deploy_single_page('games', 'UNITED BEATS // COOL MIND PUZZLE & VISION SPECTRUM GAMES', 'games.html')

# 6. Spectrum Vision Game Dev Plan & Monopoly Simulator Page'''
    deploy_code = deploy_code.replace(target_deploy, new_deploy_entries)
    
    with open(os.path.join(BASE_DIR, 'deploy_page.py'), 'w', encoding='utf-8') as f:
        f.write(deploy_code)
    print("SUCCESS: Updated deploy/deploy_page.py to register /archetypes/ and /games/!")

print("ALL RESTRUCTURING OPERATIONS COMPLETE!")
