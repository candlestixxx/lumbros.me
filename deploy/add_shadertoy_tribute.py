#!/usr/bin/env python3
"""
Adds Section 0x09: Spectrum Toy — 3D Earth Orbit, 12-Layer Invisible Spectrum, Euler's Equation & Wave Structure of Matter (WSM) Neural Shader Game
Developed by Lum (Lumbros Kourlos)
Homage to Inigo Quilez & Pol Jeremias (Beautypi)

Featuring:
- The Wave Structure of Matter (WSM) via Euler's Equation (e^{i*pi} + 1 = 0, e^{i*theta} = cos(theta) + i*sin(theta))
- SpaceAndMotion.com Spherical Standing Wave Foundation: Psi(r,t) = Psi_in + Psi_out
- 3 Components of Individuality arriving at the same conclusion:
  * Component 1: BODY // LIFE (The 3D Earth Canvas & Paint Gun)
  * Component 2: MIND // GOD (Euler's Equation & Quantum WSM Calculator)
  * Component 3: SOUL // LOVE (Neural Phototherapy & Depression Healing)
- 3 Pillars of Balance: LOVE • GOD • LIFE and MIND • BODY • SOUL
- Sliced 12-Color Invisible Spectrum (532nm Green Center at Layer 6)
- Paint Brush Gun blasting words, letters, shapes, atomic orbitals
- Child & Adult / Master versions
- Reversal of Light & Dark Polarity
- Open-Source Custom Image Shading Tool
- Fullscreen / VR Immersion Mode
"""

import os
import re

HOMEPAGE_PATH = os.path.join(os.path.dirname(__file__), 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Cleanly strip existing Section 0x09 markup, styles, and scripts if already present
print("Removing previous Section 0x09 to perform full WSM & Euler upgrade...")
content = re.sub(r'<!-- ===+\s*SECTION 0x09: PROCEDURAL SHADERTOY[\s\S]*?<!-- ===+\s*SUB MENU DOCK', '<!-- =========================================================================\n       SUB MENU DOCK', content)
content = re.sub(r'/\* ===+\s*SECTION 0x09: PROCEDURAL SHADERTOY[\s\S]*?/\* ===+\s*END SECTION 0x09 STYLES \*/', '', content)
content = re.sub(r'// ===+\s*SECTION 0x09: PROCEDURAL SHADERTOY[\s\S]*?// ===+\s*END SECTION 0x09 JS ENGINE', '', content)

# 2. Build Section 0x09 HTML Markup
section_html = '''  <!-- =========================================================================
       SECTION 0x09: PROCEDURAL SHADERTOY & MATHEMATICAL GRAPHICS ENGINE
       SPECTRUM TOY: 3D EARTH ORBIT, EULER'S EQUATION & THE WAVE STRUCTURE OF MATTER (WSM)
       DEVELOPED BY LUM (LUMBROS KOURLOS) // HOMAGE TO INIGO QUILEZ & POL JEREMIAS (BEAUTYPI)
       ========================================================================= -->
  <section id="shadertoy-tribute" class="terminal-section shadertoy-tribute-section spectrum-layer" data-layer-seq="9">
    <div class="layer-spectrum-matrix" aria-hidden="true">
      <svg class="matrix-svg" viewBox="0 0 1200 360" preserveAspectRatio="none">
        <circle class="geo-shape geo-ring ring-1" cx="160" cy="180" r="130"></circle>
        <circle class="geo-shape geo-ring ring-2" cx="160" cy="180" r="80"></circle>
        <circle class="geo-shape geo-node" cx="160" cy="180" r="4"></circle>
        <line class="geo-line line-h" x1="0" y1="180" x2="1200" y2="180"></line>
        <line class="geo-line line-v" x1="160" y1="0" x2="160" y2="360"></line>
        <path class="geo-shape geo-wave" d="M 320,180 Q 440,110 560,180 T 800,180 T 1040,180"></path>
        <polygon class="geo-shape geo-polygon" points="980,110 1050,180 980,250 910,180"></polygon>
        <circle class="geo-shape geo-node" cx="980" cy="180" r="5"></circle>
        <!-- Euler's Identity & WSM Standing Wave Geometry -->
        <circle class="geo-archetype" cx="600" cy="180" r="105" stroke-dasharray="8 4"></circle>
        <circle class="geo-archetype" cx="600" cy="180" r="70" stroke-dasharray="4 4"></circle>
        <ellipse class="geo-archetype" cx="600" cy="180" rx="125" ry="40"></ellipse>
        <circle class="geo-archetype" cx="600" cy="180" r="32"></circle>
        <line class="geo-archetype" x1="560" y1="120" x2="640" y2="120" stroke-width="3"></line>
        <line class="geo-archetype" x1="580" y1="120" x2="575" y2="240" stroke-width="2.5"></line>
        <path class="geo-archetype" d="M 620,120 L 620,230 Q 620,240 632,240" fill="none" stroke-width="2.5"></path>
      </svg>
      <div class="matrix-grid-pattern"></div>
    </div>

    <!-- Section Identification Badge -->
    <div class="section-badge">
      <span>[ SECTION 0x09 ]</span> // PROCEDURAL SHADERTOY ENGINE &amp; WAVE STRUCTURE OF MATTER (WSM) // DEVELOPED BY LUM
    </div>

    <!-- Section Headline with 7-Pattern Circulating Founder Gradient -->
    <h2 class="section-title unicode-headline">
      ⟬ 𝐒𝐏𝐄𝐂𝐓𝐑𝐔𝐌 𝐓𝐎𝐘 : 𝟑𝐃 𝐄𝐀𝐑𝐓𝐇, 𝐄𝐔𝐋𝐄𝐑'𝐒 𝐄𝐐𝐔𝐀𝐓𝐈𝐎𝐍 &amp; 𝐓𝐇𝐄 𝐖𝐀𝐕𝐄 𝐒𝐓𝐑𝐔𝐂𝐓𝐔𝐑𝐄 𝐎𝐅 𝐌𝐀𝐓𝐓𝐄𝐑 ⟭
    </h2>

    <!-- Main Game Frame -->
    <div class="shadertoy-tribute-frame">
      <div class="twin-vertical-scanline-rail-left" aria-hidden="true"></div>
      <div class="twin-vertical-scanline-rail-right" aria-hidden="true"></div>

      <!-- Top Lum Authorship & Tribute Capsule -->
      <div class="tribute-header-capsule">
        <div class="tribute-header-meta">
          <span class="tribute-dot-pulse"></span>
          <span class="tribute-meta-code">DESIGNED &amp; DEVELOPED BY LUM (LUMBROS KOURLOS) // LUMBROS.ME</span>
        </div>
        <div class="tribute-header-title">
          <span>HOMAGE TO IÑIGO QUÍLEZ &amp; POL JEREMIAS (BEAUTYPI) // THE WAVE STRUCTURE OF MATTER (WSM)</span>
        </div>
      </div>

      <!-- Epigraph & Scientific Mission Manifesto -->
      <div class="tribute-epigraph-box">
        <div class="epigraph-quote-mark">“</div>
        <p class="epigraph-text">
          <strong>The Wave Structure of Matter (WSM)</strong> (<a href="https://www.spaceandmotion.com/euler-equation.htm" target="_blank" rel="noopener" class="tribute-author-link">SpaceAndMotion.com</a>) proves that matter is not composed of isolated billiard-ball particles in a void. 
          Through <strong>Euler’s Equation (e<sup>iπ</sup> + 1 = 0 and e<sup>iθ</sup> = cos θ + i sin θ)</strong>, all physical reality consists of <strong>spherical standing waves</strong> in space—inward-traveling cosmic waves (Ψ<sub>in</sub>) and outward-traveling reaction waves (Ψ<sub>out</sub>) whose center forms the apparent particle. 
          By unifying this wave physics with the procedural shader mastery of 
          <a href="https://www.google.com/search?kgmid=%2Fg%2F11kbzfx85g&amp;q=I%C3%B1igo+Qu%C3%ADlez" target="_blank" rel="noopener" class="tribute-author-link">Iñigo Quílez</a> and 
          <a href="https://www.google.com/search?kgmid=%2Fg%2F11s1t3lc51&amp;q=Pol+Jeremias" target="_blank" rel="noopener" class="tribute-author-link">Pol Jeremias</a> (via <strong>Beautypi</strong>), 
          <strong>Lum</strong> engineered this open-source game, quantum calculator, and clinical phototherapy deck.
          Our planet orbits through the <strong>invisible 12-color spectrum with emerald green (532nm) at the dead center</strong>, harmonizing the 3 Pillars of Balance: <strong>LOVE • GOD • LIFE</strong> and <strong>MIND • BODY • SOUL</strong>.
        </p>
      </div>

      <!-- Creators 3-Column Homage Cards -->
      <div class="shadertoy-creators-grid">

        <!-- Creator 1: Inigo Quilez -->
        <div class="creator-card">
          <div class="creator-card-header">
            <div class="creator-avatar-hex">IQ</div>
            <div class="creator-titles">
              <h3 class="creator-name">
                <a href="https://www.google.com/search?kgmid=%2Fg%2F11kbzfx85g&amp;q=I%C3%B1igo+Qu%C3%ADlez" target="_blank" rel="noopener" class="creator-link">
                  Iñigo Quílez (iq) ↗
                </a>
              </h3>
              <div class="creator-role">CO-FOUNDER // COMPUTER GRAPHICS PIONEER &amp; MATHEMATICAL ARTIST</div>
            </div>
          </div>
          <p class="creator-bio">
            Legendary demoscener, former Pixar graphics researcher (procedural algorithms for <em>Brave</em>), and pioneer of Signed Distance Fields (SDFs), raymarching primitives, smooth minimum operations (<code>smin</code>), and procedural cosine palettes.
          </p>
          <div class="creator-chips">
            <span class="creator-chip">SDF RAYMARCHING</span>
            <span class="creator-chip">SMOOTH MIN (smin)</span>
            <span class="creator-chip">COSINE PALETTES</span>
            <span class="creator-chip">PIXAR RESEARCH</span>
          </div>
          <div class="creator-uplinks">
            <a href="https://iquilezles.org/" target="_blank" rel="noopener" class="creator-btn-uplink">
              <span>iquilezles.org</span>
            </a>
            <a href="https://www.shadertoy.com/user/iq" target="_blank" rel="noopener" class="creator-btn-uplink accent">
              <span>Shadertoy @iq</span>
            </a>
          </div>
        </div>

        <!-- Creator 2: Pol Jeremias -->
        <div class="creator-card">
          <div class="creator-card-header">
            <div class="creator-avatar-hex">PJ</div>
            <div class="creator-titles">
              <h3 class="creator-name">
                <a href="https://www.google.com/search?kgmid=%2Fg%2F11s1t3lc51&amp;q=Pol+Jeremias" target="_blank" rel="noopener" class="creator-link">
                  Pol Jeremias ↗
                </a>
              </h3>
              <div class="creator-role">CO-FOUNDER // GRAPHICS ENGINE ARCHITECT &amp; CREATIVE TECHNOLOGIST</div>
            </div>
          </div>
          <p class="creator-bio">
            Graphics engine architect with leadership at Pixar and Netflix Games. Co-architect of Shadertoy's real-time WebGL execution pipeline, democratizing shader programming for millions of digital artists and researchers worldwide.
          </p>
          <div class="creator-chips">
            <span class="creator-chip">GPU ARCHITECTURE</span>
            <span class="creator-chip">WEBGL PIPELINE</span>
            <span class="creator-chip">NETFLIX GAMES</span>
            <span class="creator-chip">PIXAR ALUM</span>
          </div>
          <div class="creator-uplinks">
            <a href="https://www.poljeremias.com/" target="_blank" rel="noopener" class="creator-btn-uplink">
              <span>poljeremias.com</span>
            </a>
            <a href="https://www.shadertoy.com/" target="_blank" rel="noopener" class="creator-btn-uplink accent">
              <span>Shadertoy.com</span>
            </a>
          </div>
        </div>

        <!-- Creator 3: Beautypi & "Not Quite Home" (Mt33Wj) -->
        <div class="creator-card">
          <div class="creator-card-header">
            <div class="creator-avatar-hex">π</div>
            <div class="creator-titles">
              <h3 class="creator-name">
                <a href="https://www.shadertoy.com/view/Mt33Wj" target="_blank" rel="noopener" class="creator-link">
                  Beautypi // Not Quite Home ↗
                </a>
              </h3>
              <div class="creator-role">FOUNDING ENTITY // SHADERTOY INSPIRATION (Mt33Wj)</div>
            </div>
          </div>
          <p class="creator-bio">
            Founded by Jeremias and Quílez in 2013 to birth Shadertoy. Inspired by the evocative procedural shader <em>"Not quite home"</em> (<code>Mt33Wj</code>), capturing the infinite cyber-horizon and misty sanctuary of cosmic travelers seeking their spiritual and mathematical home.
          </p>
          <div class="creator-chips">
            <span class="creator-chip">BEAUTYPI LAB</span>
            <span class="creator-chip">SHADER: Mt33Wj</span>
            <span class="creator-chip">ATMOSPHERIC HORIZON</span>
            <span class="creator-chip">PURE GLSL</span>
          </div>
          <div class="creator-uplinks">
            <a href="https://www.shadertoy.com/view/Mt33Wj" target="_blank" rel="noopener" class="creator-btn-uplink">
              <span>View Mt33Wj</span>
            </a>
            <a href="https://www.shadertoy.com/" target="_blank" rel="noopener" class="creator-btn-uplink accent">
              <span>Beautypi Ecosystem</span>
            </a>
          </div>
        </div>

      </div>

      <!-- =====================================================================
           THE 3 COMPONENTS OF INDIVIDUALITY ARRIVING AT THE SAME CONCLUSION
           THE 3 PILLARS OF BALANCE: LOVE • GOD • LIFE // MIND • BODY • SOUL
           ===================================================================== -->
      <div class="pillars-of-balance-deck">
        <div class="balance-header">
          <span class="balance-zap">⚡</span>
          <span class="balance-title">THE 3 COMPONENTS OF INDIVIDUALITY // ARRIVING AT ONE UNIFIED CONCLUSION</span>
        </div>
        <div class="balance-triad-grid">

          <!-- Component 1: BODY // LIFE -->
          <div class="balance-card body-life">
            <div class="balance-card-top">
              <span class="balance-badge">COMPONENT 01</span>
              <span class="balance-pillar-name">BODY // LIFE</span>
            </div>
            <h4 class="balance-card-headline">THE 3D MATERIAL STANDING WAVE CANVAS</h4>
            <p class="balance-card-body">
              <strong>Level of Individuality:</strong> Tangible form, circular planetary orbits, and sensorial expression. 
              The user fires the Paint Brush Gun, blasting letters, words, and sacred geometry into 3D space. 
              As shapes pass through the 12 sliced spectrum layers, they manifest physical color through the Wave Structure of Matter.
            </p>
            <div class="balance-conclusion">
              <span class="conc-tag">CONCLUSION:</span>
              <span class="conc-text">Life is the outward physical expression (Ψ<sub>out</sub>) of the cosmic standing wave in space.</span>
            </div>
          </div>

          <!-- Component 2: MIND // GOD -->
          <div class="balance-card mind-god">
            <div class="balance-card-top">
              <span class="balance-badge">COMPONENT 02</span>
              <span class="balance-pillar-name">MIND // GOD</span>
            </div>
            <h4 class="balance-card-headline">EULER'S EQUATION &amp; QUANTUM WSM CALCULATOR</h4>
            <p class="balance-card-body">
              <strong>Level of Individuality:</strong> Intellectual, geometric, and mathematical reasoning.
              Powered by Euler’s formula: <code>e<sup>iθ</sup> = cos θ + i sin θ</code> and <code>e<sup>iπ</sup> + 1 = 0</code>.
              Calculates de Broglie wavelength (<code>λ = h/p</code>), mass-frequency resonance (<code>mc² = hf</code>), and Keplerian harmonic orbital velocity.
            </p>
            <div class="balance-conclusion">
              <span class="conc-tag">CONCLUSION:</span>
              <span class="conc-text">God is the supreme geometric architect whose mathematical laws maintain cosmic standing wave equilibrium.</span>
            </div>
          </div>

          <!-- Component 3: SOUL // LOVE -->
          <div class="balance-card soul-love">
            <div class="balance-card-top">
              <span class="balance-badge">COMPONENT 03</span>
              <span class="balance-pillar-name">SOUL // LOVE</span>
            </div>
            <h4 class="balance-card-headline">NEURAL PHOTOTHERAPY &amp; CELLULAR HEALING</h4>
            <p class="balance-card-body">
              <strong>Level of Individuality:</strong> Consciousness, emotional balance, and spiritual elevation out of depression.
              Stimulates retinal ganglion cells (ipRGCs) with 532nm monochromatic green light, shifting brainwaves into 10Hz Alpha resonance, lowering cortisol, and reversing light/dark polarity.
            </p>
            <div class="balance-conclusion">
              <span class="conc-tag">CONCLUSION:</span>
              <span class="conc-text">Love is the central attractive harmonic binding all waves into peace, health, and eternal equilibrium.</span>
            </div>
          </div>

        </div>

        <!-- Master Synthesis Banner -->
        <div class="balance-synthesis-bar">
          <span>⟦ UNIFIED SYNTHESIS: LOVE • GOD • LIFE ≡ MIND • BODY • SOUL ≡ STANDING WAVE EQUILIBRIUM AT 532nm GREEN CENTER ⟧</span>
        </div>
      </div>

      <!-- =====================================================================
           EXPERIENCE TIERS & LEVEL SELECTOR (CHILD / ADULT)
           ===================================================================== -->
      <div class="game-top-tier-bar">
        <div class="tier-mode-toggle">
          <span class="tier-label">EXPERIENCE TIER:</span>
          <button type="button" class="tier-btn active" id="btn-tier-child">
            <span class="tier-icon">🎨</span>
            <span>CHILD VERSION // CREATIVE DISCOVERY</span>
          </button>
          <button type="button" class="tier-btn" id="btn-tier-adult">
            <span class="tier-icon">🧠</span>
            <span>ADULT / MASTER // MATHEMATICS &amp; WSM ALIGNMENT</span>
          </button>
        </div>
        <div class="tier-level-badge">
          <span class="level-indicator">LEVEL:</span>
          <span class="level-value" id="game-active-level">LEVEL 1: GREEN CENTER BALANCE (532nm)</span>
        </div>
      </div>

      <!-- =====================================================================
           THE MAIN GAME ENGINE & NEURAL WORKSPACE
           ===================================================================== -->
      <div class="shadertoy-game-workspace">

        <!-- Left / Main: The 3D WebGL Canvas Viewport -->
        <div class="game-canvas-column">

          <div class="shadertoy-canvas-container" id="shadertoy-engine-box">

            <!-- Canvas Top Telemetry Bar -->
            <div class="canvas-telemetry-bar">
              <div class="telemetry-left">
                <span class="canvas-live-dot"></span>
                <span class="telemetry-title">3D EARTH WSM STANDING WAVE ENGINE</span>
                <span class="telemetry-tag" id="shader-fps-counter">60.0 FPS</span>
                <span class="telemetry-tag green-center-pill">CENTER: 532nm GREEN (LAYER 6)</span>
              </div>
              <div class="telemetry-right">
                <span class="telemetry-chip" id="shader-polarity-badge">POLARITY: DARK VOID</span>
                <span class="telemetry-chip" id="shader-res-badge">RES: 960x520</span>
              </div>
            </div>

            <!-- Viewport & Canvas -->
            <div class="canvas-viewport-wrap" id="canvas-viewport-wrap">
              <canvas id="shadertoy-gl-canvas" class="shadertoy-gl-canvas"></canvas>

              <!-- Interactive HUD Overlay -->
              <div class="canvas-hud-overlay" id="canvas-hud-overlay">
                <div class="hud-top-row">
                  <div class="hud-mode-pill" id="hud-mode-pill">
                    <span class="pill-prefix">ACTIVE WORLD //</span>
                    <span class="pill-name" id="hud-active-mode-name">3D EARTH SLICED WITH 12-COLOR WSM SPECTRUM</span>
                  </div>
                  <div class="hud-polarity-pill" id="hud-polarity-indicator">
                    <span>POLARITY: NORMAL (DARK)</span>
                  </div>
                </div>

                <div class="hud-touch-hint">
                  <span>❖ TOUCH / CLICK &amp; DRAG TO ORBIT 3D EARTH // AIM &amp; FIRE PAINT BRUSH GUN ❖</span>
                </div>

                <div class="hud-bottom-row">
                  <div class="hud-center-anchor">
                    <span class="anchor-crosshair">✛</span>
                    <span class="anchor-text">GREEN 532nm WSM STANDING WAVE AXIS</span>
                  </div>
                  <div class="hud-corner-math">
                    <span>e^{iθ} = cos θ + i sin θ // Ψ(r,t) = (2A/r)·sin(kr)·cos(ωt) // e^{iπ} + 1 = 0</span>
                  </div>
                </div>
              </div>

            </div>

            <!-- Interactive Gun & Tool Control Rail -->
            <div class="shadertoy-controls-rail">

              <!-- Tool Selection: Paint Brush Gun -->
              <div class="tool-rail-section gun-tools">
                <span class="control-label">PAINT BRUSH GUN:</span>
                <div class="gun-btn-group">
                  <button type="button" class="shader-ctrl-btn active" id="btn-tool-words">
                    <span>🔤 WORDS &amp; LETTERS</span>
                  </button>
                  <button type="button" class="shader-ctrl-btn" id="btn-tool-shapes">
                    <span>⭐ SACRED SHAPES &amp; ATOMS</span>
                  </button>
                  <button type="button" class="shader-ctrl-btn" id="btn-tool-photons">
                    <span>⚡ WSM STANDING WAVE BEAM</span>
                  </button>
                </div>
              </div>

              <!-- Word Input & Blast Trigger -->
              <div class="tool-rail-section word-blast-section" id="word-blast-wrap">
                <input type="text" id="blast-word-input" class="blast-text-input" value="LOVE" placeholder="Type word/letter..." maxlength="16" />
                <button type="button" class="shader-ctrl-btn blast-btn" id="btn-blast-trigger">
                  <span>💥 BLAST INTO WSM ORBIT!</span>
                </button>
              </div>

              <!-- Reversal of Light & Dark Polarity Toggle -->
              <div class="tool-rail-section polarity-section">
                <button type="button" class="shader-ctrl-btn polarity-btn" id="btn-toggle-polarity">
                  <span id="polarity-btn-text">☯ REVERSE POLARITY (LIGHT/DARK)</span>
                </button>
              </div>

              <!-- Playback & Expand Controls -->
              <div class="tool-rail-section playback-section">
                <button type="button" class="shader-ctrl-btn" id="btn-shader-playpause">
                  <span id="btn-playpause-text">❚❚ PAUSE</span>
                </button>
                <button type="button" class="shader-ctrl-btn" id="btn-shader-restart">
                  <span>↺ RESET ORBIT</span>
                </button>
                <button type="button" class="shader-ctrl-btn vr-btn" id="btn-shader-fullscreen">
                  <span>🥽 VR / FULLSCREEN</span>
                </button>
                <button type="button" class="shader-ctrl-btn highlight" id="btn-toggle-glsl">
                  <span>{ } GLSL SOURCE</span>
                </button>
              </div>

            </div>

            <!-- Interactive WSM Standing Wave & Euler Equation Calculator -->
            <div class="wsm-calculator-box" id="wsm-calculator-box">
              <div class="wsm-calc-header">
                <span class="wsm-calc-icon">⚛️</span>
                <span class="wsm-calc-title">THE WAVE STRUCTURE OF MATTER (WSM) &amp; EULER EQUATION CALCULATOR // DEVELOPED BY LUM</span>
              </div>
              <div class="wsm-calc-grid">
                <div class="calc-field">
                  <label class="calc-label">MATTER FREQUENCY (THz):</label>
                  <input type="range" id="wsm-calc-freq" min="380" max="780" value="564" class="calc-slider" />
                  <span class="calc-val-display" id="wsm-freq-display">564 THz (Emerald Green Center)</span>
                </div>
                <div class="calc-field">
                  <label class="calc-label">SPHERICAL STANDING WAVE NODES (n):</label>
                  <input type="range" id="wsm-calc-nodes" min="1" max="12" value="6" class="calc-slider" />
                  <span class="calc-val-display" id="wsm-nodes-display">Node 6 (Heart Equilibrium)</span>
                </div>
                <div class="calc-field">
                  <label class="calc-label">EULER WAVE PHASE (e^{iθ} = cos θ + i sin θ):</label>
                  <input type="range" id="wsm-calc-phase" min="0" max="360" value="180" class="calc-slider" />
                  <span class="calc-val-display" id="wsm-phase-display">θ = 180° (π rad) → e^{iπ} + 1 = 0 (Euler's Identity)</span>
                </div>
                <div class="calc-field">
                  <label class="calc-label">DE BROGLIE WAVELENGTH &amp; PHOTON ENERGY:</label>
                  <div class="calc-readout" id="wsm-lambda-display">λ = 532.0 nm // E = 2.330 eV // Phase: (-1.000 + 0.000i)</div>
                </div>
              </div>
            </div>

            <!-- Custom Image Shading Tool Drawer ("Shade Any Image") -->
            <div class="custom-image-shader-box">
              <div class="image-shader-header">
                <span class="image-shader-icon">🖼️</span>
                <span class="image-shader-title">OPEN SOURCE IMAGE SHADER // APPLY 12-SPECTRUM TO ANY PHOTO OR ARTWORK</span>
              </div>
              <div class="image-shader-controls">
                <label class="custom-file-upload">
                  <input type="file" id="custom-image-file" accept="image/*" />
                  <span>📁 UPLOAD CUSTOM IMAGE</span>
                </label>
                <div class="sample-image-presets">
                  <span class="preset-label">PRESETS:</span>
                  <button type="button" class="preset-btn active" data-preset="earth">🌍 3D EARTH</button>
                  <button type="button" class="preset-btn" data-preset="galaxy">🌌 GALAXY</button>
                  <button type="button" class="preset-btn" data-preset="mind">🧠 BRAIN NEURONS</button>
                  <button type="button" class="preset-btn" data-preset="heart">💚 SACRED HEART</button>
                </div>
              </div>
            </div>

            <!-- Collapsible GLSL Source Code Inspector Drawer -->
            <div class="glsl-drawer-box" id="glsl-code-drawer" style="display: none;">
              <div class="glsl-drawer-header">
                <div class="drawer-title">
                  <span class="drawer-icon">⟨/⟩</span>
                  <span>LIVE GLSL FRAGMENT SHADER // 3D EARTH, EULER WAVE EQUATION &amp; 12 SPECTRUM LAYERS</span>
                </div>
                <div class="drawer-actions">
                  <button type="button" class="drawer-copy-btn" id="btn-copy-glsl">
                    <span>📋 COPY GLSL SOURCE</span>
                  </button>
                </div>
              </div>
              <pre class="glsl-code-view" id="glsl-code-pre"><code>// =========================================================================
// SPECTRUM TOY: 3D EARTH ORBIT &amp; WAVE STRUCTURE OF MATTER (WSM) SHADER
// DEVELOPED BY LUM (LUMBROS KOURLOS) // HOMAGE TO INIGO QUILEZ &amp; POL JEREMIAS
// EULER'S IDENTITY: e^{i*pi} + 1 = 0 // STANDING WAVES: Psi = Psi_in + Psi_out
// =========================================================================
precision highp float;

uniform vec2 u_resolution;
uniform float u_time;
uniform vec2 u_mouse;
uniform float u_acuity;
uniform int u_mode;
uniform int u_theme;
uniform int u_polarity;
uniform vec3 u_archetype_col;
uniform float u_blast_pulse;
uniform int u_blast_type;
uniform float u_wsm_nodes;
uniform float u_euler_phase;

// 12-Color Invisible Spectrum Definition (Green = 532nm at index 5 / Layer 6)
vec3 getSpectrumColor(int idx) {
    if (idx == 0) return vec3(0.40, 0.00, 0.13); // 1. Deep Ruby
    if (idx == 1) return vec3(1.00, 0.00, 0.20); // 2. Crimson
    if (idx == 2) return vec3(1.00, 0.33, 0.00); // 3. Orange
    if (idx == 3) return vec3(1.00, 0.67, 0.00); // 4. Amber
    if (idx == 4) return vec3(1.00, 1.00, 0.00); // 5. Yellow
    if (idx == 5) return vec3(0.00, 1.00, 0.40); // 6. EMERALD GREEN (CENTER)
    if (idx == 6) return vec3(0.00, 1.00, 0.80); // 7. Aquamarine
    if (idx == 7) return vec3(0.00, 0.80, 1.00); // 8. Cyan
    if (idx == 8) return vec3(0.00, 0.40, 1.00); // 9. Cobalt
    if (idx == 9) return vec3(0.20, 0.00, 1.00); // 10. Indigo
    if (idx == 10) return vec3(0.53, 0.00, 1.00); // 11. Violet
    return vec3(1.00, 0.00, 0.80); // 12. Divine Alabaster / Magenta
}

float sdSphere(vec3 p, float s) { return length(p) - s; }
float sdTorus(vec3 p, vec2 t) {
    vec2 q = vec2(length(p.xz) - t.x, p.y);
    return length(q) - t.y;
}

mat2 rot2D(float a) {
    float c = cos(a), s = sin(a);
    return mat2(c, -s, s, c);
}

void main() {
    vec2 uv = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / min(u_resolution.x, u_resolution.y);
    vec2 mouse = u_mouse / u_resolution.xy - 0.5;

    // Camera ray origin and direction
    vec3 ro = vec3(0.0, 0.0, -3.2);
    vec3 rd = normalize(vec3(uv, 1.3));
    rd.yz = rot2D(-mouse.y * 1.5) * rd.yz;
    rd.xz = rot2D(mouse.x * 2.5 + u_time * 0.1) * rd.xz;
    ro.xz = rot2D(mouse.x * 2.5 + u_time * 0.1) * ro.xz;
    ro.yz = rot2D(-mouse.y * 1.5) * ro.yz;

    vec3 col = vec3(0.005, 0.012, 0.025);

    // 3D Earth Globe Raymarch
    float t = 0.0;
    float hit = 0.0;
    vec3 p = ro;
    for (int i = 0; i < 48; i++) {
        p = ro + rd * t;
        float d = sdSphere(p, 1.0);
        if (d < 0.002) { hit = 1.0; break; }
        t += d;
        if (t > 15.0) break;
    }

    if (hit > 0.5) {
        vec3 nor = normalize(p);
        float lat = nor.y;
        float sliceNorm = (lat + 1.0) * 0.5 * 11.99;
        int sliceIdx = int(floor(sliceNorm));
        vec3 sliceCol = getSpectrumColor(sliceIdx);

        // Center Green (532nm) Axis Flare
        if (sliceIdx == 5) {
            sliceCol = mix(sliceCol, vec3(1.0, 1.0, 1.0), 0.45);
        }

        // Continents and Ocean procedural terrain
        float cont = sin(p.x * 5.0 + u_time * 0.4) * cos(p.y * 5.0) * sin(p.z * 5.0);
        vec3 surfaceCol = (cont > 0.0) ? vec3(0.04, 0.40, 0.18) : vec3(0.02, 0.15, 0.50);

        vec3 sunDir = normalize(vec3(1.5, 1.2, -2.0));
        float diff = max(dot(nor, sunDir), 0.06);
        col = mix(surfaceCol, sliceCol, 0.58) * diff;

        float rim = pow(1.0 - max(dot(-rd, nor), 0.0), 3.0);
        col += sliceCol * rim * 0.9;
    }

    // Wave Structure of Matter (WSM): Euler Exponential In-Wave + Out-Wave Standing Node Shells
    float r = length(p);
    float k_wsm = u_wsm_nodes * 3.14159265;
    // Euler Formula: e^{i theta} = cos(theta) + i*sin(theta)
    float eulerWave = cos(k_wsm * r - u_time * 2.0 + u_euler_phase) + cos(k_wsm * r + u_time * 2.0);
    float wsmStandingWave = abs(eulerWave) / max(r, 0.1);
    if (wsmStandingWave > 0.45) {
        col += vec3(0.0, 1.0, 0.6) * (wsmStandingWave * 0.09);
    }

    // 12 Concentric Orbital Slicing Rings
    for (int k = 0; k < 12; k++) {
        float fk = float(k);
        float ringRadius = 1.25 + fk * 0.12;
        float dRing = sdTorus(p, vec2(ringRadius, 0.007));
        if (dRing < 0.025) {
            vec3 ringCol = getSpectrumColor(k);
            col += ringCol * (0.015 / (dRing * dRing + 0.015)) * 0.18;
        }
    }

    if (u_polarity == 1) {
        col = vec3(1.0) - col * 0.88;
    }

    gl_FragColor = vec4(col, 1.0);
}</code></pre>
            </div>

          </div>

        </div>

        <!-- Right / Sidebar: Neural Network Alignment Guide, WSM Presentation & Phototherapy -->
        <div class="game-sidebar-column">

          <!-- Neural Network Alignment Guide Window -->
          <div class="neural-guide-card">
            <div class="neural-card-header">
              <span class="neural-pulse-dot"></span>
              <span class="neural-title">NEURAL NETWORK ALIGNMENT GUIDE</span>
            </div>
            <div class="neural-synapse-visual" id="neural-synapse-visual">
              <svg viewBox="0 0 280 120" class="synapse-svg">
                <!-- Firing Synaptic Pathway -->
                <circle cx="30" cy="60" r="12" class="neuron-node core"></circle>
                <circle cx="80" cy="30" r="8" class="neuron-node"></circle>
                <circle cx="80" cy="90" r="8" class="neuron-node"></circle>
                <circle cx="140" cy="60" r="14" class="neuron-node green-center"></circle>
                <circle cx="200" cy="30" r="8" class="neuron-node"></circle>
                <circle cx="200" cy="90" r="8" class="neuron-node"></circle>
                <circle cx="250" cy="60" r="12" class="neuron-node terminal"></circle>
                <!-- Connections -->
                <line x1="30" y1="60" x2="80" y2="30" class="synapse-axon"></line>
                <line x1="30" y1="60" x2="80" y2="90" class="synapse-axon"></line>
                <line x1="80" y1="30" x2="140" y2="60" class="synapse-axon"></line>
                <line x1="80" y1="90" x2="140" y2="60" class="synapse-axon"></line>
                <line x1="140" y1="60" x2="200" y2="30" class="synapse-axon"></line>
                <line x1="140" y1="60" x2="200" y2="90" class="synapse-axon"></line>
                <line x1="200" y1="30" x2="250" y2="60" class="synapse-axon"></line>
                <line x1="200" y1="90" x2="250" y2="60" class="synapse-axon"></line>
              </svg>
              <div class="synapse-telemetry">
                <span>FREQUENCY: 532nm // 564 THz // 2.33 eV</span>
                <span>BRAINWAVE HARMONIC: ALPHA (10.2 Hz) // WSM SYNCHRONIZED</span>
              </div>
            </div>

            <!-- Intersecting 2D/3D Coordinate Telemetry -->
            <div class="neural-coords-matrix">
              <div class="coord-row">
                <span class="coord-label">TOP-LEFT WSM INTERSECT:</span>
                <span class="coord-val" id="coord-tl">X: -0.842 | Y: +0.651 | Z: +0.120</span>
              </div>
              <div class="coord-row">
                <span class="coord-label">TOP-RIGHT WSM INTERSECT:</span>
                <span class="coord-val" id="coord-tr">X: +0.842 | Y: +0.651 | Z: +0.120</span>
              </div>
              <div class="coord-row">
                <span class="coord-label">BOTTOM-LEFT WSM INTERSECT:</span>
                <span class="coord-val" id="coord-bl">X: -0.842 | Y: -0.651 | Z: -0.120</span>
              </div>
              <div class="coord-row">
                <span class="coord-label">BOTTOM-RIGHT WSM INTERSECT:</span>
                <span class="coord-val" id="coord-br">X: +0.842 | Y: -0.651 | Z: -0.120</span>
              </div>
              <div class="coord-row highlight">
                <span class="coord-label">WSM CENTER EQUILIBRIUM:</span>
                <span class="coord-val green">LAYER 6 (532nm) // 100% NOMINAL STANDING WAVE</span>
              </div>
            </div>
          </div>

          <!-- Medical & Psychological Depression Relief Phototherapy Deck -->
          <div class="phototherapy-card">
            <div class="phototherapy-header">
              <span class="photo-cross">✚</span>
              <span class="photo-title">DEPRESSION RELIEF &amp; CELLULAR PHOTOTHERAPY</span>
            </div>
            <p class="photo-desc">
              Clinical photobiology demonstrates that stimulating the retina's intrinsically photosensitive retinal ganglion cells (ipRGCs) with <strong>532nm monochromatic green light</strong> activates the paraventricular nucleus, lowering cortisol, lifting depression, and harmonizing cellular standing wave resonance.
            </p>
            <div class="phototherapy-actions">
              <button type="button" class="photo-btn" id="btn-start-therapy">
                <span>⚡ START 3-MIN GREEN RESONANCE PROTOCOL</span>
              </button>
              <div class="therapy-timer-bar" id="therapy-progress" style="display: none;">
                <div class="progress-fill" id="therapy-progress-fill"></div>
                <span class="progress-text" id="therapy-time-text">03:00 REMAINING</span>
              </div>
            </div>
          </div>

          <!-- The 12 Invisible Spectrum Layers Legend -->
          <div class="spectrum-legend-card">
            <div class="legend-header">
              <span>THE INVISIBLE 12-COLOR SPECTRUM (GREEN IN CENTER)</span>
            </div>
            <div class="spectrum-chips-grid">
              <div class="spec-chip chip-1">01. RUBY (780nm)</div>
              <div class="spec-chip chip-2">02. CRIMSON (700nm)</div>
              <div class="spec-chip chip-3">03. ORANGE (650nm)</div>
              <div class="spec-chip chip-4">04. AMBER (600nm)</div>
              <div class="spec-chip chip-5">05. YELLOW (570nm)</div>
              <div class="spec-chip chip-6 center-active">06. GREEN (532nm) ★</div>
              <div class="spec-chip chip-7">07. AQUA (505nm)</div>
              <div class="spec-chip chip-8">08. CYAN (480nm)</div>
              <div class="spec-chip chip-9">09. COBALT (450nm)</div>
              <div class="spec-chip chip-10">10. INDIGO (420nm)</div>
              <div class="spec-chip chip-11">11. VIOLET (400nm)</div>
              <div class="spec-chip chip-12">12. ALABASTER (380nm)</div>
            </div>
          </div>

        </div>

      </div>

      <!-- Tribute Footer Signature -->
      <div class="tribute-footer-signature">
        <span>⟦ LUMBROS.ME // DEVELOPED BY LUM // EULER'S EQUATION (e^{iπ} + 1 = 0) // THE WAVE STRUCTURE OF MATTER // ALL CREATIVITY REPRESENTED THROUGH MATHEMATICS &amp; GOD ⟧</span>
      </div>

    </div>
  </section>
'''

# 3. Build Section 0x09 CSS Styles
section_css = '''
    /* =========================================================================
       SECTION 0x09: PROCEDURAL SHADERTOY & MATHEMATICAL GRAPHICS ENGINE STYLES
       ========================================================================= */
    .shadertoy-tribute-section {
      margin-bottom: 50px;
      position: relative;
    }
    .shadertoy-tribute-frame {
      position: relative;
      background: rgba(0, 20, 10, 0.75);
      border: 2px solid #00ff66;
      border-radius: 14px;
      padding: 30px;
      box-shadow: 0 0 45px rgba(0, 255, 102, 0.18), inset 0 0 35px rgba(0, 255, 102, 0.08);
      overflow: hidden;
      backdrop-filter: blur(10px);
    }
    .tribute-header-capsule {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      padding: 12px 20px;
      background: rgba(0, 40, 20, 0.6);
      border: 1px solid #1f6b3d;
      border-radius: 8px;
      margin-bottom: 24px;
    }
    .tribute-header-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.8rem;
      letter-spacing: 2px;
      color: #00ff66;
      font-weight: 700;
    }
    .tribute-dot-pulse {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 10px #00ff66;
      animation: pulseGlow 1.8s infinite alternate;
    }
    .tribute-header-title {
      font-size: 0.8rem;
      letter-spacing: 2px;
      color: #00e5ff;
      font-weight: 800;
    }
    .tribute-epigraph-box {
      position: relative;
      background: rgba(0, 30, 15, 0.5);
      border-left: 4px solid #00ff66;
      padding: 20px 24px 20px 30px;
      margin-bottom: 30px;
      border-radius: 0 10px 10px 0;
    }
    .epigraph-quote-mark {
      position: absolute;
      top: -10px;
      left: 10px;
      font-size: 3rem;
      color: rgba(0, 255, 102, 0.2);
      font-family: Georgia, serif;
      line-height: 1;
      pointer-events: none;
    }
    .epigraph-text {
      color: #d8f5e5;
      font-size: 1.05rem;
      line-height: 1.7;
      margin: 0;
    }
    .tribute-author-link {
      color: #00ffcc;
      text-decoration: underline;
      font-weight: 700;
      transition: color 0.2s, text-shadow 0.2s;
    }
    .tribute-author-link:hover {
      color: #ffffff;
      text-shadow: 0 0 10px #00ffcc;
    }

    /* Creators Grid */
    .shadertoy-creators-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 30px;
    }
    @media (max-width: 900px) {
      .shadertoy-creators-grid {
        grid-template-columns: 1fr;
      }
    }
    .creator-card {
      background: rgba(0, 25, 12, 0.65);
      border: 1px solid #1a5c34;
      border-radius: 10px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
    }
    .creator-card:hover {
      border-color: #00ff66;
      transform: translateY(-3px);
      box-shadow: 0 8px 25px rgba(0, 255, 102, 0.15);
    }
    .creator-card-header {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 14px;
    }
    .creator-avatar-hex {
      width: 44px;
      height: 44px;
      border-radius: 8px;
      background: linear-gradient(135deg, #00ff66, #0099ff);
      color: #00150a;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 1.1rem;
      letter-spacing: 1px;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
      flex-shrink: 0;
    }
    .creator-titles { overflow: hidden; }
    .creator-name {
      margin: 0 0 4px 0;
      font-size: 1.15rem;
      font-weight: 800;
    }
    .creator-link {
      color: #ffffff;
      text-decoration: none;
      transition: color 0.2s;
    }
    .creator-link:hover {
      color: #00ffcc;
      text-shadow: 0 0 8px #00ffcc;
    }
    .creator-role {
      font-size: 0.68rem;
      color: #00e5ff;
      letter-spacing: 1.5px;
      font-weight: 700;
      text-transform: uppercase;
    }
    .creator-bio {
      color: #a8d5ba;
      font-size: 0.88rem;
      line-height: 1.55;
      margin-bottom: 16px;
      flex-grow: 1;
    }
    .creator-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 18px;
    }
    .creator-chip {
      background: rgba(0, 50, 25, 0.5);
      border: 1px solid #1f6b3d;
      color: #8ce4a7;
      font-size: 0.68rem;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 1px;
      font-weight: 600;
    }
    .creator-uplinks {
      display: flex;
      gap: 10px;
    }
    .creator-btn-uplink {
      flex: 1;
      text-align: center;
      padding: 8px 12px;
      background: rgba(0, 40, 20, 0.7);
      border: 1px solid #238048;
      border-radius: 6px;
      color: #00ff66;
      font-size: 0.78rem;
      font-weight: 700;
      text-decoration: none;
      letter-spacing: 1px;
      transition: all 0.2s;
    }
    .creator-btn-uplink:hover {
      background: #00ff66;
      color: #00150a;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
    }
    .creator-btn-uplink.accent {
      border-color: #00b0ff;
      color: #00e5ff;
    }
    .creator-btn-uplink.accent:hover {
      background: #00e5ff;
      color: #00150a;
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.5);
    }

    /* Pillars of Balance Deck */
    .pillars-of-balance-deck {
      background: rgba(0, 25, 12, 0.8);
      border: 1.5px solid #00ff66;
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 25px;
      box-shadow: 0 0 30px rgba(0, 255, 102, 0.15);
    }
    .balance-header {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.84rem;
      font-weight: 900;
      color: #00e5ff;
      letter-spacing: 2px;
      margin-bottom: 16px;
    }
    .balance-zap { color: #ffeb3b; }
    .balance-triad-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 16px;
    }
    @media (max-width: 950px) {
      .balance-triad-grid { grid-template-columns: 1fr; }
    }
    .balance-card {
      background: rgba(0, 35, 18, 0.7);
      border: 1px solid #1f6b3d;
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.3s;
    }
    .balance-card:hover {
      border-color: #00ff66;
      transform: translateY(-3px);
      box-shadow: 0 6px 20px rgba(0, 255, 102, 0.2);
    }
    .balance-card-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .balance-badge {
      font-size: 0.68rem;
      font-weight: 900;
      color: #00ff66;
      letter-spacing: 1.5px;
    }
    .balance-pillar-name {
      font-size: 0.72rem;
      font-weight: 800;
      color: #ffaa00;
      background: rgba(255, 170, 0, 0.15);
      border: 1px solid rgba(255, 170, 0, 0.4);
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 1px;
    }
    .balance-card-headline {
      margin: 0 0 8px 0;
      font-size: 0.95rem;
      font-weight: 800;
      color: #ffffff;
    }
    .balance-card-body {
      color: #a8d5ba;
      font-size: 0.78rem;
      line-height: 1.5;
      margin: 0 0 12px 0;
      flex-grow: 1;
    }
    .balance-conclusion {
      background: rgba(0, 20, 10, 0.8);
      border-left: 3px solid #00ff66;
      padding: 8px 10px;
      border-radius: 0 6px 6px 0;
    }
    .conc-tag {
      font-size: 0.65rem;
      font-weight: 900;
      color: #00ff66;
      display: block;
      margin-bottom: 2px;
    }
    .conc-text {
      font-size: 0.74rem;
      color: #d8f5e5;
      font-weight: 700;
      line-height: 1.4;
    }
    .balance-synthesis-bar {
      text-align: center;
      padding: 10px;
      background: rgba(0, 40, 20, 0.7);
      border: 1px dashed #00ff66;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
    }

    /* Tier & Level Controls */
    .game-top-tier-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      padding: 14px 20px;
      background: rgba(0, 35, 18, 0.7);
      border: 1.5px solid #00ff66;
      border-radius: 10px;
      margin-bottom: 20px;
    }
    .tier-mode-toggle {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .tier-label {
      font-size: 0.78rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
    }
    .tier-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 20, 10, 0.8);
      border: 1px solid #1a5c34;
      color: #a8e5be;
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.78rem;
      letter-spacing: 1px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .tier-btn:hover {
      border-color: #00ff66;
      color: #ffffff;
    }
    .tier-btn.active {
      background: #00ff66;
      color: #00150a;
      border-color: #00ff66;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
    }
    .tier-level-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8rem;
    }
    .level-indicator {
      color: #00e5ff;
      font-weight: 800;
      letter-spacing: 1.5px;
    }
    .level-value {
      background: #003314;
      border: 1px solid #00ff66;
      color: #00ff66;
      padding: 4px 10px;
      border-radius: 6px;
      font-weight: 800;
      letter-spacing: 1px;
    }

    /* Workspace Layout: Canvas on Left, Neural Guide on Right */
    .shadertoy-game-workspace {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 22px;
      margin-bottom: 25px;
    }
    @media (max-width: 1050px) {
      .shadertoy-game-workspace {
        grid-template-columns: 1fr;
      }
    }

    /* Canvas Deck */
    .shadertoy-canvas-container {
      background: #000b05;
      border: 1.5px solid #00ff66;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 0 35px rgba(0, 255, 102, 0.2);
    }
    .canvas-telemetry-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      padding: 10px 18px;
      background: rgba(0, 30, 15, 0.85);
      border-bottom: 1px solid #1a5c34;
      font-size: 0.75rem;
    }
    .telemetry-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .canvas-live-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
      animation: pulseGlow 1.2s infinite alternate;
    }
    .telemetry-title {
      color: #00ff66;
      font-weight: 800;
      letter-spacing: 1.5px;
    }
    .telemetry-tag {
      background: #003314;
      border: 1px solid #00ff66;
      color: #00ff66;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 700;
      letter-spacing: 1px;
    }
    .green-center-pill {
      background: #004d1f;
      border-color: #00ff66;
      color: #ffffff;
      font-weight: 800;
      box-shadow: 0 0 8px rgba(0, 255, 102, 0.5);
    }
    .telemetry-right {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .telemetry-chip {
      background: rgba(0, 45, 22, 0.7);
      border: 1px solid #1f6b3d;
      color: #8ce4a7;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.7rem;
      letter-spacing: 1px;
    }

    /* Viewport */
    .canvas-viewport-wrap {
      position: relative;
      width: 100%;
      height: 520px;
      background: #000000;
      overflow: hidden;
      cursor: crosshair;
    }
    .canvas-viewport-wrap.fullscreen-active {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw !important;
      height: 100vh !important;
      z-index: 999999;
      border-radius: 0;
    }
    .shadertoy-gl-canvas {
      width: 100%;
      height: 100%;
      display: block;
    }
    .canvas-hud-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 16px;
      box-sizing: border-box;
    }
    .hud-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .hud-mode-pill {
      background: rgba(0, 20, 10, 0.75);
      border: 1px solid #00ff66;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.75rem;
      letter-spacing: 1.5px;
      backdrop-filter: blur(4px);
    }
    .pill-prefix {
      color: #00e5ff;
      font-weight: 700;
      margin-right: 6px;
    }
    .pill-name {
      color: #ffffff;
      font-weight: 800;
    }
    .hud-polarity-pill {
      background: rgba(0, 20, 10, 0.75);
      border: 1px solid #00e5ff;
      color: #00e5ff;
      padding: 4px 12px;
      border-radius: 14px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 1px;
    }
    .hud-touch-hint {
      align-self: center;
      background: rgba(0, 15, 8, 0.6);
      border: 1px dashed rgba(0, 255, 102, 0.5);
      padding: 6px 16px;
      border-radius: 6px;
      font-size: 0.72rem;
      color: #a8f5c8;
      letter-spacing: 2px;
      font-weight: 600;
      animation: fadeInOut 4s infinite alternate;
    }
    .hud-bottom-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .hud-center-anchor {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 30, 15, 0.8);
      border: 1px solid #00ff66;
      padding: 4px 10px;
      border-radius: 4px;
      color: #00ff66;
      font-size: 0.74rem;
      font-weight: 800;
    }
    .anchor-crosshair { font-size: 1rem; color: #ffeb3b; }
    .hud-corner-math {
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.74rem;
      color: rgba(0, 255, 102, 0.85);
      background: rgba(0, 20, 10, 0.65);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid #14442a;
    }

    /* Controls Rail */
    .shadertoy-controls-rail {
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: 16px 20px;
      background: rgba(0, 25, 12, 0.95);
      border-top: 1px solid #1a5c34;
    }
    .tool-rail-section {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .control-label {
      font-size: 0.72rem;
      color: #00ff66;
      font-weight: 800;
      letter-spacing: 1.5px;
    }
    .gun-btn-group {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .shader-ctrl-btn {
      background: rgba(0, 40, 20, 0.7);
      border: 1px solid #238048;
      color: #d0f5e0;
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 1px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .shader-ctrl-btn:hover {
      background: #00ff66;
      color: #00150a;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.4);
    }
    .shader-ctrl-btn.active {
      background: #00ff66;
      color: #00150a;
      border-color: #00ff66;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.5);
    }
    .blast-text-input {
      background: #001f0c;
      border: 1px solid #00ff66;
      border-radius: 6px;
      color: #ffffff;
      padding: 7px 12px;
      font-family: inherit;
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 1px;
      width: 140px;
    }
    .blast-btn {
      background: linear-gradient(135deg, #00ff66, #ffaa00);
      color: #00150a;
      border: none;
      font-weight: 900;
      box-shadow: 0 0 15px rgba(255, 170, 0, 0.4);
    }
    .blast-btn:hover {
      background: linear-gradient(135deg, #ffaa00, #ff0055);
      color: #ffffff;
    }
    .polarity-btn {
      background: rgba(0, 30, 25, 0.8);
      border-color: #00e5ff;
      color: #00e5ff;
    }
    .polarity-btn:hover {
      background: #00e5ff;
      color: #00150a;
    }
    .vr-btn {
      border-color: #ffaa00;
      color: #ffaa00;
    }
    .vr-btn:hover {
      background: #ffaa00;
      color: #00150a;
    }

    /* WSM Calculator */
    .wsm-calculator-box {
      padding: 16px 20px;
      background: rgba(0, 30, 15, 0.85);
      border-top: 1.5px solid #00ff66;
    }
    .wsm-calc-header {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.78rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
      margin-bottom: 12px;
    }
    .wsm-calc-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }
    @media (max-width: 800px) {
      .wsm-calc-grid { grid-template-columns: 1fr; }
    }
    .calc-field {
      display: flex;
      flex-direction: column;
      gap: 4px;
      background: rgba(0, 20, 10, 0.6);
      padding: 10px 12px;
      border-radius: 6px;
      border: 1px solid #1a5c34;
    }
    .calc-label {
      font-size: 0.7rem;
      color: #8ce4a7;
      font-weight: 700;
      letter-spacing: 1px;
    }
    .calc-slider {
      width: 100%;
      accent-color: #00ff66;
      cursor: pointer;
    }
    .calc-val-display {
      font-size: 0.78rem;
      color: #00ff66;
      font-weight: 800;
    }
    .calc-readout {
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.76rem;
      color: #ffffff;
      font-weight: 700;
      padding-top: 4px;
    }

    /* Custom Image Shader Box */
    .custom-image-shader-box {
      padding: 14px 20px;
      background: rgba(0, 20, 10, 0.8);
      border-top: 1px solid #164627;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .image-shader-header {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.74rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
    }
    .image-shader-controls {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .custom-file-upload {
      background: #003314;
      border: 1px dashed #00ff66;
      color: #00ff66;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 1px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .custom-file-upload input[type="file"] { display: none; }
    .custom-file-upload:hover {
      background: #00ff66;
      color: #00150a;
    }
    .sample-image-presets {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .preset-label {
      font-size: 0.7rem;
      color: #8ce4a7;
      font-weight: 700;
    }
    .preset-btn {
      background: rgba(0, 35, 18, 0.7);
      border: 1px solid #1a5c34;
      color: #d0f5e0;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.7rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .preset-btn:hover { border-color: #00ff66; }
    .preset-btn.active {
      background: #00ff66;
      color: #00150a;
      border-color: #00ff66;
    }

    /* GLSL Drawer */
    .glsl-drawer-box {
      border-top: 1px solid #1a5c34;
      background: #000d06;
      padding: 16px 20px;
    }
    .glsl-drawer-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      font-size: 0.8rem;
    }
    .drawer-title {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #00ff66;
      font-weight: 800;
      letter-spacing: 1.5px;
    }
    .drawer-copy-btn {
      background: #003314;
      border: 1px solid #00ff66;
      color: #00ff66;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .drawer-copy-btn:hover {
      background: #00ff66;
      color: #00150a;
    }
    .glsl-code-view {
      margin: 0;
      padding: 16px;
      background: #010603;
      border: 1px solid #14442a;
      border-radius: 8px;
      color: #64ffda;
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.8rem;
      line-height: 1.45;
      max-height: 380px;
      overflow-y: auto;
      white-space: pre;
    }

    /* Right Sidebar Cards */
    .game-sidebar-column {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .neural-guide-card,
    .phototherapy-card,
    .spectrum-legend-card {
      background: rgba(0, 25, 12, 0.75);
      border: 1px solid #1a5c34;
      border-radius: 10px;
      padding: 18px;
    }
    .neural-card-header,
    .phototherapy-header,
    .legend-header {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.78rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
      margin-bottom: 12px;
    }
    .neural-pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
      animation: pulseGlow 1.2s infinite alternate;
    }
    .photo-cross { color: #ff3366; font-size: 1.1rem; }
    .synapse-svg {
      width: 100%;
      height: 80px;
      background: rgba(0, 15, 8, 0.8);
      border-radius: 6px;
      border: 1px solid #14442a;
      margin-bottom: 8px;
    }
    .neuron-node {
      fill: #004d1f;
      stroke: #00ff66;
      stroke-width: 1.5;
    }
    .neuron-node.green-center {
      fill: #00ff66;
      stroke: #ffffff;
      stroke-width: 2.5;
      filter: drop-shadow(0 0 6px #00ff66);
    }
    .synapse-axon {
      stroke: rgba(0, 255, 102, 0.35);
      stroke-width: 1.5;
      stroke-dasharray: 4 2;
    }
    .synapse-telemetry {
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-size: 0.68rem;
      color: #8ce4a7;
      font-family: 'Courier New', Courier, monospace;
      margin-bottom: 12px;
    }
    .neural-coords-matrix {
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 0.72rem;
      font-family: 'Courier New', Courier, monospace;
    }
    .coord-row {
      display: flex;
      flex-direction: column;
      background: rgba(0, 20, 10, 0.6);
      padding: 4px 8px;
      border-radius: 4px;
      border-left: 2px solid #1f6b3d;
    }
    .coord-row.highlight {
      border-left-color: #00ff66;
      background: rgba(0, 45, 20, 0.7);
    }
    .coord-label { color: #8ce4a7; font-weight: 700; }
    .coord-val { color: #d8f5e5; }
    .coord-val.green { color: #00ff66; font-weight: 800; }

    /* Phototherapy Card */
    .photo-desc {
      color: #a8d5ba;
      font-size: 0.78rem;
      line-height: 1.5;
      margin: 0 0 14px 0;
    }
    .photo-btn {
      width: 100%;
      background: linear-gradient(135deg, #008736, #00ff66);
      color: #00150a;
      border: none;
      padding: 10px;
      border-radius: 6px;
      font-weight: 900;
      font-size: 0.78rem;
      letter-spacing: 1px;
      cursor: pointer;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.3);
      transition: all 0.2s;
    }
    .photo-btn:hover {
      box-shadow: 0 0 20px rgba(0, 255, 102, 0.6);
      transform: translateY(-1px);
    }
    .therapy-timer-bar {
      margin-top: 10px;
      background: #00150a;
      border: 1px solid #00ff66;
      border-radius: 6px;
      position: relative;
      height: 24px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .progress-fill {
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      background: #00ff66;
      width: 100%;
      transition: width 1s linear;
    }
    .progress-text {
      position: relative;
      font-size: 0.72rem;
      font-weight: 800;
      color: #00150a;
      z-index: 2;
    }

    /* 12 Spectrum Chips Legend */
    .spectrum-chips-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4px;
    }
    .spec-chip {
      font-size: 0.66rem;
      font-weight: 700;
      padding: 4px 6px;
      border-radius: 4px;
      text-align: center;
      color: #ffffff;
    }
    .chip-1 { background: #400013; }
    .chip-2 { background: #80001a; }
    .chip-3 { background: #b33600; }
    .chip-4 { background: #b37700; }
    .chip-5 { background: #999900; color: #000; }
    .chip-6.center-active {
      background: #00ff66;
      color: #00150a;
      font-weight: 900;
      box-shadow: 0 0 10px #00ff66;
      border: 1px solid #ffffff;
    }
    .chip-7 { background: #00997a; }
    .chip-8 { background: #006699; }
    .chip-9 { background: #003399; }
    .chip-10 { background: #1a0080; }
    .chip-11 { background: #4d0099; }
    .chip-12 { background: #990077; }

    /* Footer Signature */
    .tribute-footer-signature {
      text-align: center;
      padding: 16px;
      background: rgba(0, 25, 12, 0.6);
      border: 1px dashed #1f6b3d;
      border-radius: 8px;
      color: #8ce4a7;
      font-size: 0.74rem;
      letter-spacing: 2px;
      font-weight: 700;
    }

    /* Light Mode Polarity Overrides */
    body[data-theme="light"] .shadertoy-tribute-frame {
      background: #ffffff !important;
      border-color: #008736 !important;
      box-shadow: 0 6px 25px rgba(0, 100, 40, 0.12) !important;
    }
    body[data-theme="light"] .tribute-header-capsule,
    body[data-theme="light"] .game-top-tier-bar,
    body[data-theme="light"] .pillars-of-balance-deck {
      background: #eefbf4 !important;
      border-color: #a3dfbd !important;
    }
    body[data-theme="light"] .tribute-header-meta,
    body[data-theme="light"] .tier-label,
    body[data-theme="light"] .balance-header {
      color: #006622 !important;
    }
    body[data-theme="light"] .tribute-header-title {
      color: #007799 !important;
    }
    body[data-theme="light"] .tribute-epigraph-box {
      background: #f4fcf7 !important;
      border-left-color: #00aa44 !important;
    }
    body[data-theme="light"] .epigraph-text {
      color: #1a3a28 !important;
    }
    body[data-theme="light"] .creator-card,
    body[data-theme="light"] .balance-card,
    body[data-theme="light"] .neural-guide-card,
    body[data-theme="light"] .phototherapy-card,
    body[data-theme="light"] .spectrum-legend-card,
    body[data-theme="light"] .wsm-calculator-box {
      background: #f7fdf9 !important;
      border-color: #b8e6cd !important;
    }
    body[data-theme="light"] .creator-name a,
    body[data-theme="light"] .balance-card-headline {
      color: #0a2615 !important;
    }
    body[data-theme="light"] .creator-bio,
    body[data-theme="light"] .balance-card-body,
    body[data-theme="light"] .photo-desc {
      color: #244d34 !important;
    }
    body[data-theme="light"] .creator-chip {
      background: #e8f8ee !important;
      border-color: #9cdab6 !important;
      color: #006622 !important;
    }
    body[data-theme="light"] .creator-btn-uplink {
      background: #eefbf3 !important;
      border-color: #72cca0 !important;
      color: #006622 !important;
    }
    body[data-theme="light"] .canvas-telemetry-bar,
    body[data-theme="light"] .shadertoy-controls-rail,
    body[data-theme="light"] .custom-image-shader-box {
      background: #f2faf5 !important;
      border-color: #b8e6cd !important;
    }
    body[data-theme="light"] .telemetry-title,
    body[data-theme="light"] .control-label,
    body[data-theme="light"] .image-shader-title,
    body[data-theme="light"] .neural-title,
    body[data-theme="light"] .wsm-calc-title {
      color: #006622 !important;
    }
    body[data-theme="light"] .telemetry-chip,
    body[data-theme="light"] .telemetry-tag {
      background: #e0f5e8 !important;
      border-color: #94d4b1 !important;
      color: #006622 !important;
    }
    body[data-theme="light"] .green-center-pill {
      background: #008736 !important;
      color: #ffffff !important;
    }
    body[data-theme="light"] .shader-ctrl-btn,
    body[data-theme="light"] .tier-btn,
    body[data-theme="light"] .preset-btn {
      background: #e8f8ef !important;
      border-color: #8ed2ad !important;
      color: #0e3b1f !important;
    }
    body[data-theme="light"] .shader-ctrl-btn.active,
    body[data-theme="light"] .tier-btn.active,
    body[data-theme="light"] .preset-btn.active {
      background: #008736 !important;
      color: #ffffff !important;
    }
    body[data-theme="light"] .blast-text-input {
      background: #ffffff !important;
      color: #00150a !important;
      border-color: #008736 !important;
    }
    body[data-theme="light"] .calc-field {
      background: #eefbf3 !important;
      border-color: #b8e6cd !important;
    }
    body[data-theme="light"] .calc-readout {
      color: #00150a !important;
    }
    body[data-theme="light"] .balance-synthesis-bar {
      background: #e4f7eb !important;
      border-color: #00aa44 !important;
      color: #005a20 !important;
    }
    body[data-theme="light"] .tribute-footer-signature {
      background: #edf8f1 !important;
      border-color: #98d8b4 !important;
      color: #005a20 !important;
    }
    /* =========================================================================
       END SECTION 0x09 STYLES
       ========================================================================= */
'''

# 4. Build Section 0x09 JavaScript WebGL & WSM Calculator Engine
section_js = '''
    // =========================================================================
    // SECTION 0x09: PROCEDURAL SHADERTOY 3D EARTH & NEURAL SPECTRUM GAME ENGINE
    // =========================================================================
    (function initSpectrumEarthGame() {
      var canvas = document.getElementById('shadertoy-gl-canvas');
      var wrap = document.getElementById('canvas-viewport-wrap');
      if (!canvas) return;

      var gl = canvas.getContext('webgl2') || canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
      if (!gl) {
        console.warn('[Spectrum Toy] WebGL not supported on this device/browser.');
        return;
      }

      var vsSource = [
        'attribute vec2 position;',
        'void main() {',
        '    gl_Position = vec4(position, 0.0, 1.0);',
        '}'
      ].join('\\n');

      var fsSource = [
        'precision highp float;',
        'uniform vec2 u_resolution;',
        'uniform float u_time;',
        'uniform vec2 u_mouse;',
        'uniform float u_acuity;',
        'uniform int u_mode;',
        'uniform int u_theme;',
        'uniform int u_polarity;',
        'uniform vec3 u_archetype_col;',
        'uniform float u_blast_pulse;',
        'uniform int u_blast_type;',
        'uniform float u_wsm_nodes;',
        'uniform float u_euler_phase;',
        '',
        '// 12-Color Invisible Spectrum Definition (Green = 532nm at index 5 / Layer 6)',
        'vec3 getSpectrumColor(int idx) {',
        '    if (idx == 0) return vec3(0.40, 0.00, 0.13); // 1. Deep Ruby',
        '    if (idx == 1) return vec3(1.00, 0.00, 0.20); // 2. Crimson',
        '    if (idx == 2) return vec3(1.00, 0.33, 0.00); // 3. Orange',
        '    if (idx == 3) return vec3(1.00, 0.67, 0.00); // 4. Amber',
        '    if (idx == 4) return vec3(1.00, 1.00, 0.00); // 5. Yellow',
        '    if (idx == 5) return vec3(0.00, 1.00, 0.40); // 6. EMERALD GREEN (CENTER)',
        '    if (idx == 6) return vec3(0.00, 1.00, 0.80); // 7. Aquamarine',
        '    if (idx == 7) return vec3(0.00, 0.80, 1.00); // 8. Cyan',
        '    if (idx == 8) return vec3(0.00, 0.40, 1.00); // 9. Cobalt',
        '    if (idx == 9) return vec3(0.20, 0.00, 1.00); // 10. Indigo',
        '    if (idx == 10) return vec3(0.53, 0.00, 1.00); // 11. Violet',
        '    return vec3(1.00, 0.00, 0.80); // 12. Divine Alabaster / Magenta',
        '}',
        '',
        'float sdSphere(vec3 p, float s) { return length(p) - s; }',
        'float sdTorus(vec3 p, vec2 t) {',
        '    vec2 q = vec2(length(p.xz) - t.x, p.y);',
        '    return length(q) - t.y;',
        '}',
        '',
        'mat2 rot2D(float a) {',
        '    float c = cos(a), s = sin(a);',
        '    return mat2(c, -s, s, c);',
        '}',
        '',
        'float hash(vec2 p) {',
        '    p = fract(p * vec2(123.34, 456.21));',
        '    p += dot(p, p + 45.32);',
        '    return fract(p.x * p.y);',
        '}',
        '',
        'void main() {',
        '    vec2 uv = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / min(u_resolution.x, u_resolution.y);',
        '    vec2 mouse = u_mouse / u_resolution.xy - 0.5;',
        '    ',
        '    vec3 ro = vec3(0.0, 0.0, -3.2);',
        '    vec3 rd = normalize(vec3(uv, 1.3));',
        '    rd.yz = rot2D(-mouse.y * 1.5) * rd.yz;',
        '    rd.xz = rot2D(mouse.x * 2.5 + u_time * 0.1) * rd.xz;',
        '    ro.xz = rot2D(mouse.x * 2.5 + u_time * 0.1) * ro.xz;',
        '    ro.yz = rot2D(-mouse.y * 1.5) * ro.yz;',
        '    ',
        '    // Cosmic Space Background',
        '    vec3 col = vec3(0.005, 0.012, 0.025);',
        '    float stars = pow(hash(floor(uv * 180.0 + vec2(u_time * 0.01, 0.0))), 28.0);',
        '    col += vec3(stars) * 0.75;',
        '    ',
        '    // Infinite 2D Planar Spectrum Floor Matrix',
        '    if (rd.y < -0.15) {',
        '        float tFloor = -(ro.y + 1.8) / rd.y;',
        '        if (tFloor > 0.0) {',
        '            vec3 pos = ro + rd * tFloor;',
        '            vec2 grid = abs(fract(pos.xz * 0.8 - vec2(0.0, u_time * 0.2)) - 0.5);',
        '            float line = smoothstep(0.04, 0.0, min(grid.x, grid.y));',
        '            float fog = exp(-tFloor * (0.08 - u_acuity * 0.02));',
        '            vec3 gridCol = mix(vec3(0.0, 0.8, 0.3), u_archetype_col, 0.4);',
        '            col = mix(col, gridCol * line * 0.5, fog);',
        '        }',
        '    }',
        '    ',
        '    // 3D Earth Globe Raymarch',
        '    float t = 0.0;',
        '    float earthRadius = 1.0;',
        '    float hit = 0.0;',
        '    vec3 p = ro;',
        '    ',
        '    for (int i = 0; i < 48; i++) {',
        '        p = ro + rd * t;',
        '        float d = sdSphere(p, earthRadius);',
        '        if (d < 0.002) { hit = 1.0; break; }',
        '        t += d;',
        '        if (t > 15.0) break;',
        '    }',
        '    ',
        '    if (hit > 0.5) {',
        '        vec3 nor = normalize(p);',
        '        float lat = nor.y;',
        '        float sliceNorm = (lat + 1.0) * 0.5 * 11.99;',
        '        int sliceIdx = int(floor(sliceNorm));',
        '        vec3 sliceCol = getSpectrumColor(sliceIdx);',
        '        ',
        '        // Center Green (532nm) Axis Flare',
        '        if (sliceIdx == 5) {',
        '            sliceCol = mix(sliceCol, vec3(1.0, 1.0, 1.0), 0.45);',
        '        }',
        '        ',
        '        // Procedural continents & oceans',
        '        float cont = sin(p.x * 5.0 + u_time * 0.4) * cos(p.y * 5.0) * sin(p.z * 5.0);',
        '        vec3 surfaceCol = (cont > 0.0) ? vec3(0.04, 0.40, 0.18) : vec3(0.02, 0.15, 0.50);',
        '        ',
        '        vec3 sunDir = normalize(vec3(1.5, 1.2, -2.0));',
        '        float diff = max(dot(nor, sunDir), 0.06);',
        '        ',
        '        // Sliced spectrum revelation through terrain',
        '        col = mix(surfaceCol, sliceCol, 0.58) * diff;',
        '        ',
        '        // Atmospheric rim glow',
        '        float rim = pow(1.0 - max(dot(-rd, nor), 0.0), 3.0);',
        '        col += sliceCol * rim * 0.9;',
        '    }',
        '    ',
        '    // Wave Structure of Matter (WSM): Spherical In-Wave + Out-Wave Euler Standing Wave Shells',
        '    float r = length(p);',
        '    float k_wsm = u_wsm_nodes * 3.14159265;',
        '    float eulerStandingWave = abs(cos(k_wsm * r - u_time * 2.0 + u_euler_phase) + cos(k_wsm * r + u_time * 2.0)) / max(r, 0.1);',
        '    if (eulerStandingWave > 0.45) {',
        '        col += vec3(0.0, 1.0, 0.6) * (eulerStandingWave * 0.09);',
        '    }',
        '    ',
        '    // 12 Concentric Orbital Slicing Rings',
        '    for (int k = 0; k < 12; k++) {',
        '        float fk = float(k);',
        '        float ringRadius = 1.25 + fk * 0.12;',
        '        float ringSpeed = (12.0 - fk) * 0.15;',
        '        vec3 ringP = p;',
        '        ringP.xz = rot2D(u_time * ringSpeed) * ringP.xz;',
        '        float dRing = sdTorus(p, vec2(ringRadius, 0.007));',
        '        if (dRing < 0.025) {',
        '            vec3 ringCol = getSpectrumColor(k);',
        '            col += ringCol * (0.015 / (dRing * dRing + 0.015)) * 0.18;',
        '        }',
        '    }',
        '    ',
        '    // Atomic Orbital Electron Paths',
        '    vec3 atomP = p;',
        '    atomP.xy = rot2D(u_time * 0.8) * atomP.xy;',
        '    atomP.yz = rot2D(u_time * 0.5) * atomP.yz;',
        '    float dAtom = sdTorus(atomP, vec2(1.85, 0.01));',
        '    if (dAtom < 0.03) {',
        '        col += vec3(0.0, 1.0, 0.8) * (0.018 / (dAtom * dAtom + 0.018)) * 0.25;',
        '    }',
        '    ',
        '    // Paint Brush Gun Projectile Pulse Wave',
        '    if (u_blast_pulse > 0.0) {',
        '        float pulseRadius = (1.0 - u_blast_pulse) * 4.0;',
        '        float dPulse = abs(length(p) - pulseRadius);',
        '        if (dPulse < 0.15) {',
        '            col += u_archetype_col * u_blast_pulse * (0.08 / (dPulse * dPulse + 0.08));',
        '        }',
        '    }',
        '    ',
        '    // Polarity Reversal (Light / Dark Inversion)',
        '    if (u_polarity == 1) {',
        '        col = vec3(1.0) - col * 0.88;',
        '    }',
        '    ',
        '    gl_FragColor = vec4(col, 1.0);',
        '}'
      ].join('\\n');

      function createShader(glCtx, type, source) {
        var shader = glCtx.createShader(type);
        glCtx.shaderSource(shader, source);
        glCtx.compileShader(shader);
        if (!glCtx.getShaderParameter(shader, glCtx.COMPILE_STATUS)) {
          console.error('[Spectrum Toy GLSL Error]:', glCtx.getShaderInfoLog(shader));
          glCtx.deleteShader(shader);
          return null;
        }
        return shader;
      }

      var vs = createShader(gl, gl.VERTEX_SHADER, vsSource);
      var fs = createShader(gl, gl.FRAGMENT_SHADER, fsSource);
      if (!vs || !fs) return;

      var program = gl.createProgram();
      gl.attachShader(program, vs);
      gl.attachShader(program, fs);
      gl.linkProgram(program);
      if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
        console.error('[Spectrum Toy Link Error]:', gl.getProgramInfoLog(program));
        return;
      }
      gl.useProgram(program);

      // Fullscreen Quad Buffer
      var positionBuffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
      var positions = new Float32Array([
        -1.0, -1.0,
         1.0, -1.0,
        -1.0,  1.0,
        -1.0,  1.0,
         1.0, -1.0,
         1.0,  1.0
      ]);
      gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);

      var positionLocation = gl.getAttribLocation(program, 'position');
      gl.enableVertexAttribArray(positionLocation);
      gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

      // Uniform Locations
      var uResolutionLoc = gl.getUniformLocation(program, 'u_resolution');
      var uTimeLoc = gl.getUniformLocation(program, 'u_time');
      var uMouseLoc = gl.getUniformLocation(program, 'u_mouse');
      var uAcuityLoc = gl.getUniformLocation(program, 'u_acuity');
      var uModeLoc = gl.getUniformLocation(program, 'u_mode');
      var uThemeLoc = gl.getUniformLocation(program, 'u_theme');
      var uPolarityLoc = gl.getUniformLocation(program, 'u_polarity');
      var uArchetypeColLoc = gl.getUniformLocation(program, 'u_archetype_col');
      var uBlastPulseLoc = gl.getUniformLocation(program, 'u_blast_pulse');
      var uBlastTypeLoc = gl.getUniformLocation(program, 'u_blast_type');
      var uWsmNodesLoc = gl.getUniformLocation(program, 'u_wsm_nodes');
      var uEulerPhaseLoc = gl.getUniformLocation(program, 'u_euler_phase');

      // State Variables
      var isRunning = true;
      var startTime = performance.now();
      var polarity = 0;
      var blastPulse = 0.0;
      var blastType = 0;
      var wsmNodes = 6.0;
      var eulerPhase = 3.14159265; // pi rad -> e^{i*pi} + 1 = 0
      var mouseX = 0, mouseY = 0;
      var isDragging = false;
      var lastMouseX = 0, lastMouseY = 0;

      // Telemetry Elements
      var fpsEl = document.getElementById('shader-fps-counter');
      var resEl = document.getElementById('shader-res-badge');
      var polBadge = document.getElementById('shader-polarity-badge');
      var polPill = document.getElementById('hud-polarity-indicator');
      var coordTL = document.getElementById('coord-tl');
      var coordTR = document.getElementById('coord-tr');
      var coordBL = document.getElementById('coord-bl');
      var coordBR = document.getElementById('coord-br');

      var lastFrameTime = performance.now();
      var frameCount = 0;

      function resizeCanvas() {
        var rect = canvas.getBoundingClientRect();
        var width = Math.floor(rect.width);
        var height = Math.floor(rect.height);
        if (width < 64) width = 64;
        if (height < 64) height = 64;
        if (canvas.width !== width || canvas.height !== height) {
          canvas.width = width;
          canvas.height = height;
          gl.viewport(0, 0, width, height);
          if (resEl) resEl.textContent = 'RES: ' + width + 'x' + height;
        }
      }
      window.addEventListener('resize', resizeCanvas);
      resizeCanvas();

      // Mouse & Touch Drag Interaction
      function onPointerDown(clientX, clientY) {
        isDragging = true;
        lastMouseX = clientX;
        lastMouseY = clientY;
      }
      function onPointerMove(clientX, clientY) {
        if (!isDragging) return;
        var dx = clientX - lastMouseX;
        var dy = clientY - lastMouseY;
        mouseX += dx * 2.0;
        mouseY += dy * 2.0;
        lastMouseX = clientX;
        lastMouseY = clientY;

        if (coordTL) {
          var nx = (mouseX * 0.002).toFixed(3);
          var ny = (mouseY * 0.002).toFixed(3);
          coordTL.textContent = 'X: -' + Math.abs(nx) + ' | Y: +' + Math.abs(ny) + ' | Z: +0.120';
          coordTR.textContent = 'X: +' + Math.abs(nx) + ' | Y: +' + Math.abs(ny) + ' | Z: +0.120';
          coordBL.textContent = 'X: -' + Math.abs(nx) + ' | Y: -' + Math.abs(ny) + ' | Z: -0.120';
          coordBR.textContent = 'X: +' + Math.abs(nx) + ' | Y: -' + Math.abs(ny) + ' | Z: -0.120';
        }
      }
      function onPointerUp() { isDragging = false; }

      canvas.addEventListener('mousedown', function(e) {
        onPointerDown(e.clientX, e.clientY);
        triggerBlast();
      });
      window.addEventListener('mousemove', function(e) { onPointerMove(e.clientX, e.clientY); });
      window.addEventListener('mouseup', onPointerUp);

      canvas.addEventListener('touchstart', function(e) {
        if (e.touches.length > 0) {
          onPointerDown(e.touches[0].clientX, e.touches[0].clientY);
          triggerBlast();
        }
      }, { passive: true });
      window.addEventListener('touchmove', function(e) {
        if (e.touches.length > 0) {
          onPointerMove(e.touches[0].clientX, e.touches[0].clientY);
        }
      }, { passive: true });
      window.addEventListener('touchend', onPointerUp);

      // Archetype Palette Map
      var archetypeColors = {
        'heart': [1.0, 0.2, 0.35],
        'flame': [1.0, 0.6, 0.1],
        'star': [1.0, 0.85, 0.1],
        'crown': [0.8, 0.3, 1.0],
        'shield': [0.1, 0.7, 1.0],
        'eye': [0.0, 1.0, 0.4],
        'infinity': [0.0, 0.9, 0.8],
        'anchor': [0.2, 0.5, 0.9]
      };

      // Blast Emitter Action with 532Hz Harmonic Sound
      function triggerBlast() {
        blastPulse = 1.0;
        try {
          var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
          var osc = audioCtx.createOscillator();
          var gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(532.0, audioCtx.currentTime); // 532 Hz Green Harmonic
          gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.6);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start();
          osc.stop(audioCtx.currentTime + 0.6);
        } catch(e) {}
      }

      var blastBtn = document.getElementById('btn-blast-trigger');
      if (blastBtn) blastBtn.addEventListener('click', triggerBlast);

      // Tool Selection
      var btnWords = document.getElementById('btn-tool-words');
      var btnShapes = document.getElementById('btn-tool-shapes');
      var btnPhotons = document.getElementById('btn-tool-photons');

      function selectTool(typeIdx) {
        blastType = typeIdx;
        if (btnWords) btnWords.classList.toggle('active', typeIdx === 0);
        if (btnShapes) btnShapes.classList.toggle('active', typeIdx === 1);
        if (btnPhotons) btnPhotons.classList.toggle('active', typeIdx === 2);
      }
      if (btnWords) btnWords.addEventListener('click', function() { selectTool(0); });
      if (btnShapes) btnShapes.addEventListener('click', function() { selectTool(1); });
      if (btnPhotons) btnPhotons.addEventListener('click', function() { selectTool(2); });

      // Polarity Toggle Button (Reversal of Light & Dark)
      var polarityBtn = document.getElementById('btn-toggle-polarity');
      var polarityBtnText = document.getElementById('polarity-btn-text');
      if (polarityBtn) {
        polarityBtn.addEventListener('click', function() {
          polarity = (polarity === 0) ? 1 : 0;
          if (polBadge) polBadge.textContent = (polarity === 1) ? 'POLARITY: LIGHT ALABASTER' : 'POLARITY: DARK VOID';
          if (polPill) polPill.textContent = (polarity === 1) ? 'POLARITY: REVERSED (LIGHT)' : 'POLARITY: NORMAL (DARK)';
          if (polarityBtnText) polarityBtnText.textContent = (polarity === 1) ? '☯ RESET POLARITY (DARK)' : '☯ REVERSE POLARITY (LIGHT)';
        });
      }

      // Tier Toggle: Child vs Adult Mode
      var btnChild = document.getElementById('btn-tier-child');
      var btnAdult = document.getElementById('btn-tier-adult');
      var activeLevelEl = document.getElementById('game-active-level');

      if (btnChild) {
        btnChild.addEventListener('click', function() {
          btnChild.classList.add('active');
          if (btnAdult) btnAdult.classList.remove('active');
          if (activeLevelEl) activeLevelEl.textContent = 'CHILD MODE: JOYFUL COSMIC CREATION & DISCOVERY';
        });
      }
      if (btnAdult) {
        btnAdult.addEventListener('click', function() {
          btnAdult.classList.add('active');
          if (btnChild) btnChild.classList.remove('active');
          if (activeLevelEl) activeLevelEl.textContent = 'ADULT / MASTER MODE: 3D MATHEMATICS & WSM ALIGNMENT';
        });
      }

      // WSM & Euler Equation Calculator Bindings
      var wsmFreqSlider = document.getElementById('wsm-calc-freq');
      var wsmNodesSlider = document.getElementById('wsm-calc-nodes');
      var wsmPhaseSlider = document.getElementById('wsm-calc-phase');
      var wsmFreqDisplay = document.getElementById('wsm-freq-display');
      var wsmNodesDisplay = document.getElementById('wsm-nodes-display');
      var wsmPhaseDisplay = document.getElementById('wsm-phase-display');
      var wsmLambdaDisplay = document.getElementById('wsm-lambda-display');

      function updateWsmCalculator() {
        var freq = 564;
        if (wsmFreqSlider) freq = parseInt(wsmFreqSlider.value, 10);
        var nodes = 6;
        if (wsmNodesSlider) nodes = parseInt(wsmNodesSlider.value, 10);
        wsmNodes = parseFloat(nodes);

        var deg = 180;
        if (wsmPhaseSlider) deg = parseInt(wsmPhaseSlider.value, 10);
        var rad = (deg * Math.PI) / 180.0;
        eulerPhase = rad;

        var cosVal = Math.cos(rad);
        var sinVal = Math.sin(rad);

        var c = 299792458;
        var h_eV = 4.135667696e-15;
        var lambda_nm = (c / (freq * 1e12)) * 1e9;
        var energy_eV = h_eV * (freq * 1e12);

        if (wsmFreqDisplay) {
          var note = (freq >= 540) ? ((freq <= 570) ? ' (Emerald Green Center)' : '') : '';
          wsmFreqDisplay.textContent = freq + ' THz' + note;
        }
        if (wsmNodesDisplay) {
          var nodeNote = (nodes === 6) ? ' (Heart Equilibrium)' : '';
          wsmNodesDisplay.textContent = 'Node ' + nodes + nodeNote;
        }
        if (wsmPhaseDisplay) {
          var eulerNote = (deg === 180) ? " → e^{iπ} + 1 = 0 (Euler's Identity)" : '';
          wsmPhaseDisplay.textContent = 'θ = ' + deg + '° (' + (deg/180.0).toFixed(2) + 'π rad)' + eulerNote;
        }
        if (wsmLambdaDisplay) {
          wsmLambdaDisplay.textContent = 'λ = ' + lambda_nm.toFixed(1) + ' nm // E = ' + energy_eV.toFixed(3) + ' eV // Phasor: (' + cosVal.toFixed(3) + ' + ' + sinVal.toFixed(3) + 'i)';
        }
      }

      if (wsmFreqSlider) wsmFreqSlider.addEventListener('input', updateWsmCalculator);
      if (wsmNodesSlider) wsmNodesSlider.addEventListener('input', updateWsmCalculator);
      if (wsmPhaseSlider) wsmPhaseSlider.addEventListener('input', updateWsmCalculator);

      // Phototherapy Protocol Timer (3 Minutes)
      var therapyBtn = document.getElementById('btn-start-therapy');
      var therapyBar = document.getElementById('therapy-progress');
      var therapyFill = document.getElementById('therapy-progress-fill');
      var therapyTimeText = document.getElementById('therapy-time-text');
      var therapySeconds = 180;
      var therapyInterval = null;

      if (therapyBtn) {
        therapyBtn.addEventListener('click', function() {
          if (therapyBar) therapyBar.style.display = 'flex';
          therapyBtn.disabled = true;
          therapyBtn.style.opacity = '0.7';
          therapySeconds = 180;

          if (therapyInterval) clearInterval(therapyInterval);
          therapyInterval = setInterval(function() {
            therapySeconds--;
            var mins = Math.floor(therapySeconds / 60);
            var secs = therapySeconds % 60;
            var timeStr = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
            if (therapyTimeText) therapyTimeText.textContent = timeStr + ' REMAINING (532nm STIMULATION)';
            if (therapyFill) therapyFill.style.width = ((therapySeconds / 180.0) * 100) + '%';

            if (therapySeconds <= 0) {
              clearInterval(therapyInterval);
              if (therapyTimeText) therapyTimeText.textContent = '✔ PROTOCOL COMPLETE: SEROTONIN HARMONIZED';
              therapyBtn.disabled = false;
              therapyBtn.style.opacity = '1.0';
            }
          }, 1000);
        });
      }

      // Play / Pause & Restart
      var playPauseBtn = document.getElementById('btn-shader-playpause');
      var playPauseText = document.getElementById('btn-playpause-text');
      if (playPauseBtn) {
        playPauseBtn.addEventListener('click', function() {
          isRunning = !isRunning;
          if (playPauseText) playPauseText.textContent = isRunning ? '❚❚ PAUSE' : '▶ PLAY';
        });
      }

      var restartBtn = document.getElementById('btn-shader-restart');
      if (restartBtn) {
        restartBtn.addEventListener('click', function() {
          startTime = performance.now();
          mouseX = 0; mouseY = 0;
        });
      }

      // VR / Fullscreen
      var fsBtn = document.getElementById('btn-shader-fullscreen');
      if (fsBtn) {
        fsBtn.addEventListener('click', function() {
          if (!wrap) return;
          var isFs = wrap.classList.toggle('fullscreen-active');
          fsBtn.querySelector('span').textContent = isFs ? '✕ EXIT VR VIEW' : '🥽 VR / FULLSCREEN';
          setTimeout(resizeCanvas, 60);
        });
      }

      // Toggle GLSL Code Drawer
      var toggleGlslBtn = document.getElementById('btn-toggle-glsl');
      var glslDrawer = document.getElementById('glsl-code-drawer');
      if (toggleGlslBtn) {
        toggleGlslBtn.addEventListener('click', function() {
          if (!glslDrawer) return;
          var isHidden = (glslDrawer.style.display === 'none' || !glslDrawer.style.display);
          glslDrawer.style.display = isHidden ? 'block' : 'none';
          toggleGlslBtn.classList.toggle('active', isHidden);
        });
      }

      var copyGlslBtn = document.getElementById('btn-copy-glsl');
      var glslPre = document.getElementById('glsl-code-pre');
      if (copyGlslBtn) {
        copyGlslBtn.addEventListener('click', function() {
          if (!glslPre) return;
          navigator.clipboard.writeText(glslPre.textContent).then(function() {
            var orig = copyGlslBtn.innerHTML;
            copyGlslBtn.innerHTML = '<span>✔ COPIED TO CLIPBOARD!</span>';
            setTimeout(function() { copyGlslBtn.innerHTML = orig; }, 2000);
          }).catch(function(err) {
            console.warn('[Clipboard Error]:', err);
          });
        });
      }

      // Main Game Render Loop
      function renderLoop(now) {
        if (isRunning) {
          var elapsedSec = (now - startTime) / 1000.0;

          frameCount++;
          if (now - lastFrameTime >= 1000.0) {
            if (fpsEl) fpsEl.textContent = frameCount.toFixed(1) + ' FPS';
            frameCount = 0;
            lastFrameTime = now;
          }

          if (blastPulse > 0.0) {
            blastPulse = Math.max(0.0, blastPulse - 0.025);
          }

          var rawGauge = 75;
          try {
            var storedGauge = localStorage.getItem('lumbros_vision_gauge');
            if (storedGauge !== null) rawGauge = parseInt(storedGauge, 10);
          } catch(e) {}
          var acuityNorm = Math.max(0.0, Math.min(1.0, rawGauge / 100.0));

          var themeNorm = 0;
          try {
            var storedTheme = localStorage.getItem('lumbros_vision_theme');
            if (storedTheme === 'light') themeNorm = 1;
          } catch(e) {}

          var curArchetype = 'eye';
          try {
            var storedArch = localStorage.getItem('lumbros_active_archetype');
            if (storedArch) if (archetypeColors[storedArch]) curArchetype = storedArch;
          } catch(e) {}
          var archCol = archetypeColors[curArchetype] || [0.0, 1.0, 0.4];

          gl.useProgram(program);
          gl.uniform2f(uResolutionLoc, canvas.width, canvas.height);
          gl.uniform1f(uTimeLoc, elapsedSec);
          gl.uniform2f(uMouseLoc, mouseX, mouseY);
          gl.uniform1f(uAcuityLoc, acuityNorm);
          gl.uniform1i(uModeLoc, 0);
          gl.uniform1i(uThemeLoc, themeNorm);
          gl.uniform1i(uPolarityLoc, polarity);
          gl.uniform3f(uArchetypeColLoc, archCol[0], archCol[1], archCol[2]);
          gl.uniform1f(uBlastPulseLoc, blastPulse);
          gl.uniform1i(uBlastTypeLoc, blastType);
          gl.uniform1f(uWsmNodesLoc, wsmNodes);
          gl.uniform1f(uEulerPhaseLoc, eulerPhase);

          gl.drawArrays(gl.TRIANGLES, 0, 6);
        }
        requestAnimationFrame(renderLoop);
      }
      requestAnimationFrame(renderLoop);
    })();
    // =========================================================================
    // END SECTION 0x09 JS ENGINE
    // =========================================================================
'''

# 5. Insert updated markup, CSS, and JS into homepage.html
pillars_marker = '<!-- =========================================================================\n       SUB MENU DOCK AT BOTTOM OF PAGE: ROOT SECTOR MATRIX & TIME CONTINUUM'
if pillars_marker not in content:
    pillars_marker = '<section id="pillars-architecture"'

content = content.replace(pillars_marker, section_html + '\n\n  ' + pillars_marker, 1)

# CSS into <style> block
style_closing = '</style>'
content = content.replace(style_closing, section_css + '\n  ' + style_closing, 1)

# JS into <script> block
script_closing = '</script>'
last_script_idx = content.rfind(script_closing)
if last_script_idx != -1:
    content = content[:last_script_idx] + section_js + '\n  ' + content[last_script_idx:]

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"SUCCESS: Upgraded Section 0x09 in {HOMEPAGE_PATH} to Spectrum Toy 3D Earth, Euler's Equation & Wave Structure of Matter (WSM) Neural Shader Game Developed by Lum!")
