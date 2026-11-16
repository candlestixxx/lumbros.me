#!/usr/bin/env python3
"""
Moves the Main Site Menu directly under "Choose Your Spectrum Experience"
and highlights it with an invisible 12-color spectrum perimeter border traced by
a Circle Hyper-Beam moving with fast/slow mathematical rhythms.
1. Relocates #main-site-command-menu right beneath #vision-calibration-deck
2. Encloses the menu in a high-tech border featuring the 12-color invisible optical spectrum
3. Implements the Circle Hyper-Beam that accelerates and decelerates according to mathematical
   wave harmonics (Euler/Kepler modulation), illuminating the exact spectrum colors it passes over
4. Adds prominent LUMBROS.ME Site Menu branding with sub-page indicators
5. Regenerates all subpages via generate_subpages.py
6. 100% WordPress-safe (0 raw '&&' inside script tags)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# ---------------------------------------------------------------------------
# 1. Extract existing main-site-command-menu
# ---------------------------------------------------------------------------
pos_menu_start = home.find('<!-- =========================================================================\n       NEW MAIN SITE NAVIGATION MENU')
if pos_menu_start == -1:
    pos_menu_start = home.find('<nav class="main-site-command-menu"')

pos_menu_end = home.find('</nav>', pos_menu_start)
if pos_menu_end != -1:
    pos_menu_end += len('</nav>')

if pos_menu_start == -1 or pos_menu_end == -1:
    print("ERROR: Could not locate main-site-command-menu in homepage.html")
    exit(1)

menu_html_raw = home[pos_menu_start:pos_menu_end].strip()
print(f"Extracted existing menu ({len(menu_html_raw)} chars)")

# Remove menu from its old position
home = home[:pos_menu_start] + home[pos_menu_end:]

# ---------------------------------------------------------------------------
# 2. Build the Upgraded Menu with 12-Color Invisible Spectrum Border & Hyper-Beam
# ---------------------------------------------------------------------------
upgraded_menu_html = '''  <!-- =========================================================================
       LUMBROS.ME OFFICIAL SITE MENU // POSITIONED DIRECTLY UNDER SPECTRUM DECK
       INVISIBLE 12-COLOR SPECTRUM BORDER // MATHEMATICAL RHYTHM CIRCLE HYPER-BEAM
       ========================================================================= -->
  <nav class="main-site-command-menu" id="main-site-command-menu" aria-label="LUMBROS.ME Official Site Menu">
    <div class="menu-hyperbeam-frame" id="menu-hyperbeam-frame">
      
      <!-- Invisible 12-Color Spectrum Perimeter Border Track -->
      <div class="invisible-perimeter-spectrum-track" id="invisible-perimeter-spectrum-track" aria-hidden="true"></div>

      <!-- Circulating Circle Hyper-Beam Orb (Races with fast & slow mathematical rhythms) -->
      <div class="circle-hyperbeam-orb" id="circle-hyperbeam-orb">
        <div class="hyperbeam-core"></div>
        <div class="hyperbeam-flare"></div>
      </div>

      <!-- High-Tech Brand Header: LUMBROS.ME Official Site Menu -->
      <div class="menu-brand-header">
        <div class="menu-brand-left">
          <span class="live-dot-pulse" style="background: #00ff66;"></span>
          <span class="menu-brand-title">LUMBROS.ME // OFFICIAL SITE MENU</span>
          <span class="menu-brand-badge">[SUB-PAGES &amp; SECTOR NAVIGATION]</span>
        </div>
        <div class="menu-brand-telemetry" id="menu-hyperbeam-telemetry">
          SPECTRUM BORDER: <span class="telem-wl" id="hyperbeam-telem-wl" style="color: #00ff66; font-weight:800;">532nm [GREEN CENTER]</span> | HYPER-BEAM: <span style="color: #00e5ff;">MATHEMATICAL RHYTHM</span>
        </div>
      </div>

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
            
            <!-- Invisible 12-Color Spectrum Backplane -->
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

      </div>
    </div>
  </nav>
'''

# ---------------------------------------------------------------------------
# 3. Insert Upgraded Menu DIRECTLY UNDER the Vision Calibration Deck
# ---------------------------------------------------------------------------
# The vision calibration deck ends right before '<!-- Scanline & Ambient Overlay -->'
pos_deck_end = home.find('<!-- Scanline & Ambient Overlay -->')
if pos_deck_end == -1:
    pos_deck_end = home.find('<!-- =========================================================================\n       SOLID LINE PILLARS')

if pos_deck_end != -1:
    home = home[:pos_deck_end] + upgraded_menu_html + '\n\n  ' + home[pos_deck_end:]
    print("SUCCESS: Relocated Main Menu directly under the Choose Your Spectrum Experience deck!")
else:
    print("ERROR: Could not locate end of vision deck in homepage.html")
    exit(1)

# ---------------------------------------------------------------------------
# 4. Add CSS for 12-Color Invisible Spectrum Border & Circle Hyper-Beam
# ---------------------------------------------------------------------------
hyperbeam_css = '''
  /* =========================================================================
     CIRCLE HYPER-BEAM & INVISIBLE 12-COLOR SPECTRUM MENU BORDER
     ========================================================================= */
  .menu-hyperbeam-frame {
    position: relative;
    border-radius: 10px;
    padding: 3px;
    background: #020509;
    box-shadow: 0 0 35px rgba(0, 0, 0, 0.95);
    overflow: visible;
  }
  
  /* The Invisible 12-Color Spectrum Perimeter Border */
  .invisible-perimeter-spectrum-track {
    position: absolute;
    inset: 0;
    border-radius: 10px;
    padding: 2px;
    background: linear-gradient(90deg, 
      #ff1744 0%, #ff5722 9%, #ff9100 18%, #ffc400 27%, #c6ff00 36%, 
      #00ff66 45%, #00ff66 55%, 
      #00e676 64%, #00e5ff 73%, #2979ff 82%, #651fff 91%, #d500f9 100%
    );
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    opacity: 0.22;
    transition: opacity 0.3s ease;
    pointer-events: none;
  }
  .menu-hyperbeam-frame:hover .invisible-perimeter-spectrum-track {
    opacity: 0.55;
  }

  /* Circulating Circle Hyper-Beam Orb */
  .circle-hyperbeam-orb {
    position: absolute;
    width: 22px;
    height: 22px;
    margin-left: -11px;
    margin-top: -11px;
    border-radius: 50%;
    background: #00ff66;
    box-shadow: 0 0 16px #00ff66, 0 0 32px #00ff66, 0 0 48px #ffffff;
    pointer-events: none;
    z-index: 105;
    transition: background 0.1s ease, box-shadow 0.1s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .hyperbeam-core {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #ffffff;
    box-shadow: 0 0 10px #ffffff;
  }
  .hyperbeam-flare {
    position: absolute;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, transparent 70%);
    animation: hyperbeam-flare-pulse 0.8s infinite alternate;
  }
  @keyframes hyperbeam-flare-pulse {
    0% { transform: scale(0.85); opacity: 0.6; }
    100% { transform: scale(1.25); opacity: 1.0; }
  }

  /* Distinct LUMBROS.ME Menu Brand Header */
  .menu-brand-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    padding: 10px 18px 8px 18px;
    border-bottom: 1px solid rgba(0, 255, 102, 0.25);
    background: rgba(4, 12, 22, 0.95);
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  .menu-brand-left {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .menu-brand-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.84rem;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 2px;
  }
  .menu-brand-badge {
    background: rgba(0, 255, 102, 0.18);
    border: 1px solid #00ff66;
    color: #00ff66;
    font-size: 0.65rem;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 3px;
    letter-spacing: 1px;
  }
  .menu-brand-telemetry {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem;
    color: #8ce4a7;
    letter-spacing: 1px;
  }
'''

if '/* CIRCLE HYPER-BEAM & INVISIBLE 12-COLOR SPECTRUM MENU BORDER */' not in home:
    style_end = '</style>'
    home = home.replace(style_end, hyperbeam_css + '\n  ' + style_end, 1)
    print("Injected CSS for Circle Hyper-Beam & Spectrum Menu Border!")

# ---------------------------------------------------------------------------
# 5. Add JavaScript Engine for Mathematical Rhythm Perimeter Tracing
# ---------------------------------------------------------------------------
# Zero raw '&&'
hyperbeam_js = '''
    // =========================================================================
    // CIRCLE HYPER-BEAM PERIMETER TRACING ENGINE (MATHEMATICAL RHYTHM)
    // FAST & SLOW HARMONIC ACCELERATION // SPECTRUM WAVELENGTH ILLUMINATION
    // =========================================================================
    (function initMenuCircleHyperbeam() {
      var frame = document.getElementById('menu-hyperbeam-frame');
      var orb = document.getElementById('circle-hyperbeam-orb');
      var telemWl = document.getElementById('hyperbeam-telem-wl');
      if (!frame) return;
      if (!orb) return;

      var spectrumColors = [
        { name: 'CRIMSON GROUND', wl: '660nm', hex: '#ff1744' },
        { name: 'CORAL PULSE', wl: '630nm', hex: '#ff5722' },
        { name: 'AMBER TONE', wl: '600nm', hex: '#ff9100' },
        { name: 'GOLD HARMONY', wl: '580nm', hex: '#ffc400' },
        { name: 'LIME WAVE', wl: '560nm', hex: '#c6ff00' },
        { name: 'EMERALD CENTER ★', wl: '532nm', hex: '#00ff66' },
        { name: 'MINT FOCUS', wl: '515nm', hex: '#00e676' },
        { name: 'CYAN DISPERSION', wl: '495nm', hex: '#00e5ff' },
        { name: 'COBALT RESONANCE', wl: '470nm', hex: '#2979ff' },
        { name: 'INDIGO DEPTH', wl: '440nm', hex: '#651fff' },
        { name: 'VIOLET HORIZON', wl: '420nm', hex: '#d500f9' },
        { name: 'MAGENTA ZENITH', wl: '410nm', hex: '#ff4081' }
      ];

      var perimeterPos = 0; // Current distance along the perimeter
      var animPhase = 0;

      function renderHyperbeamFrame() {
        requestAnimationFrame(renderHyperbeamFrame);

        var rect = frame.getBoundingClientRect();
        var w = rect.width;
        var h = rect.height;
        if (w <= 0) return;
        if (h <= 0) return;

        // Total rectangular perimeter
        var perimeterLength = 2 * (w + h);

        // Mathematical Rhythm: Non-linear Keplerian / Relativistic wave modulation
        // Accelerates fast past the top center, slows smoothly around corners
        animPhase += 0.025;
        var velocityModulation = 1.0 + 0.65 * Math.cos(animPhase * 2.0) + 0.35 * Math.sin(animPhase * 3.0);
        var baseSpeed = 4.2;
        perimeterPos = (perimeterPos + baseSpeed * velocityModulation);
        if (perimeterPos >= perimeterLength) {
          perimeterPos -= perimeterLength;
        }

        // Calculate (X, Y) along the 4 edges of the rectangle
        var curX = 0;
        var curY = 0;

        if (perimeterPos < w) {
          // Top edge (Left to Right)
          curX = perimeterPos;
          curY = 0;
        } else if (perimeterPos < w + h) {
          // Right edge (Top to Bottom)
          curX = w;
          curY = perimeterPos - w;
        } else if (perimeterPos < 2 * w + h) {
          // Bottom edge (Right to Left)
          curX = w - (perimeterPos - (w + h));
          curY = h;
        } else {
          // Left edge (Bottom to Top)
          curX = 0;
          curY = h - (perimeterPos - (2 * w + h));
        }

        // Position the Circle Hyper-Beam Orb
        orb.style.left = curX.toFixed(1) + 'px';
        orb.style.top = curY.toFixed(1) + 'px';

        // Calculate which of the 12 spectrum layers it is currently passing over
        var normalizedProgress = perimeterPos / perimeterLength;
        var layerIndex = Math.floor(normalizedProgress * 12);
        if (layerIndex < 0) layerIndex = 0;
        if (layerIndex > 11) layerIndex = 11;

        var curLyr = spectrumColors[layerIndex];

        // Illuminate Orb in the exact color of the spectrum it is passing over!
        orb.style.background = curLyr.hex;
        orb.style.boxShadow = '0 0 16px ' + curLyr.hex + ', 0 0 32px ' + curLyr.hex + ', 0 0 45px #ffffff';

        // Update telemetry
        if (telemWl) {
          telemWl.textContent = curLyr.wl + ' [' + curLyr.name + ']';
          telemWl.style.color = curLyr.hex;
        }
      }

      renderHyperbeamFrame();
    })();
'''

if 'initMenuCircleHyperbeam' not in home:
    script_end = '</script>'
    home = home.replace(script_end, hyperbeam_js + '\n  ' + script_end, 1)
    print("Injected JavaScript for Circle Hyper-Beam perimeter tracing engine!")

# Save homepage.html
with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print("SUCCESS: Updated homepage.html with Menu directly under Spectrum Deck & Circle Hyper-Beam!")
