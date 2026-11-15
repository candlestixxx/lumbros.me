#!/usr/bin/env python3
"""
Updates the Public Pages Section (#public-pages) in homepage.html and public.html:
1. Executive Resume & Professional Statement for Lum (Lumbros Kourlos)
2. Interactive Showcase of Tools, Games & Mathematical/Artistic Calculators Built by Lum:
   - Shadertoy 3D Earth // Beautypi Tribute Game (/shadertoy/)
   - The New Monopoly // Spectrum Vision & Planetary Survival Simulator (/spectrum-vision/)
   - Optical Vision Spectrum & Acuity Prescription Calculator (#vision-calibration-deck)
   - 4096-Bit Radial Vector Cipher Engine (/private/)
3. Production Systems & Enterprise Architectures (United Beats, HyperNexus, GitHub, 1974 Chip Matrix)
4. Expandable Modular Pipeline for future games and calculators coming behind this release
5. 100% WordPress-safe (0 raw '&&' inside script tags)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# ---------------------------------------------------------------------------
# Build the Comprehensive Public Section HTML Markup
# ---------------------------------------------------------------------------
enhanced_public_section = r'''  <!-- =========================================================================
       SECTION: PUBLIC SECTOR // LUM (LUMBROS KOURLOS) EXECUTIVE RESUME,
       PROFESSIONAL STATEMENT & INTERACTIVE TOOLS, GAMES & CALCULATORS LAB
       ========================================================================= -->
  <section id="public-pages" class="terminal-section spectrum-layer" data-layer-seq="11">
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
        <polygon class="geo-archetype geo-compass-vec" points="600,110 615,165 670,180 615,195 600,250 585,195 530,180 585,165"></polygon>
        <circle class="geo-archetype" cx="600" cy="180" r="35" stroke-dasharray="4 4"></circle>
      </svg>
      <div class="matrix-grid-pattern"></div>
    </div>

    <!-- Section Badge -->
    <div class="section-badge">
      <span class="badge-num">[ SECTOR 0x01 ]</span>
      <span class="badge-tag">PUBLIC SECTOR</span>
      <span class="badge-title">EXECUTIVE RESUME // ARTISTIC PORTFOLIO // INTERACTIVE LAB</span>
    </div>

    <h2 class="section-title unicode-headline">
      ⟦ 𝗣𝗨𝗕𝗟𝗜𝗖_𝗦𝗘𝗖𝗧𝗢𝗥 // 𝗟𝗨𝗠 (𝗟𝗨𝗠𝗕𝗥𝗢𝗦 𝗞𝗢𝗨𝗥𝗟𝗢𝗦): 𝗥𝗘𝗦𝗨𝗠𝗘, 𝗠𝗔𝗧𝗛, 𝗔𝗥𝗧 &amp; 𝗧𝗢𝗢𝗟𝗦 ⟧
    </h2>

    <!-- Executive Professional Statement & Bio Callout -->
    <div class="terminal-callout" style="border-left: 3px solid #00ff66; background: rgba(5, 15, 25, 0.88); margin-bottom: 25px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px; border-bottom: 1px solid rgba(0,255,102,0.2); padding-bottom: 10px;">
        <div>
          <span style="color: #00ff66; font-weight: 900; font-size: 0.82rem; letter-spacing: 2px;">EXECUTIVE RESUME &amp; VISION STATEMENT</span>
          <span style="color: #ffffff; font-weight: 700; font-size: 1.05rem; margin-left: 10px;">LUMBROS KOURLOS (LUM)</span>
        </div>
        <div style="display: flex; gap: 8px;">
          <span class="status-pill green">FOUNDER &amp; ARCHITECT</span>
          <span class="status-pill cyan">CREATIVE TECHNOLOGIST</span>
        </div>
      </div>

      <p class="lead-text" style="color: #d1fae5; font-size: 0.86rem; line-height: 1.7; margin-bottom: 16px;">
        Welcome to the public archive and active laboratory of <strong>Lumbros Kourlos</strong>. My life's work bridges <strong>enterprise systems architecture</strong>, <strong>computational mathematics</strong>, <strong>analog audio synthesis</strong>, and <strong>serious game development</strong>. Everything cataloged here is built from the core philosophy that the universe balances in threes (<strong>Love &bull; God &bull; Life &equiv; Mind &bull; Body &bull; Soul</strong>) and communicates through the <strong>12-Color Optical Invisible Spectrum</strong> anchored at the <strong>532nm emerald green harmonic center</strong>.
      </p>

      <!-- Core Competency & Architectural Matrix -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-top: 15px;">
        <div style="background: rgba(0,255,102,0.06); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #00ff66; font-size: 0.74rem; font-weight: 800; letter-spacing: 1px;">01. SYSTEMS &amp; INFRASTRUCTURE</div>
          <div style="color: #ffffff; font-size: 0.82rem; font-weight: 700; margin: 4px 0;">Distributed Linux Cloud</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Hetzner Bare Metal, Nginx Reverse Proxies, PHP 8.4-FPM, Sovereign Database Replication &amp; SSL Hardening.</div>
        </div>

        <div style="background: rgba(0,229,255,0.06); border: 1px solid rgba(0,229,255,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #00e5ff; font-size: 0.74rem; font-weight: 800; letter-spacing: 1px;">02. MATHEMATICS &amp; SHADERS</div>
          <div style="color: #ffffff; font-size: 0.82rem; font-weight: 700; margin: 4px 0;">Euler WSM Wave Mechanics</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">WebGL Raymarching, Spherical Standing Waves (e^{i\theta} = cos\theta + i sin\theta), 2D/3D Canvas Engines &amp; Phototherapy.</div>
        </div>

        <div style="background: rgba(255,170,0,0.06); border: 1px solid rgba(255,170,0,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #ffaa00; font-size: 0.74rem; font-weight: 800; letter-spacing: 1px;">03. SERIOUS GAME DESIGN</div>
          <div style="color: #ffffff; font-size: 0.82rem; font-weight: 700; margin: 4px 0;">Macro-Economic Simulators</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Planetary Survival Gauges (Environment, Humans, Resources), Homeless-to-Bunker Real Estate &amp; Restitution Engines.</div>
        </div>

        <div style="background: rgba(213,0,249,0.06); border: 1px solid rgba(213,0,249,0.25); border-radius: 6px; padding: 12px;">
          <div style="color: #d500f9; font-size: 0.74rem; font-weight: 800; letter-spacing: 1px;">04. AI SWARMS &amp; AUDIO</div>
          <div style="color: #ffffff; font-size: 0.82rem; font-weight: 700; margin: 4px 0;">MCP Agents &amp; Spatial Sound</div>
          <div style="color: #8ce4a7; font-size: 0.72rem; line-height: 1.4;">Autonomous Multi-Agent Workflows, Model Context Protocol, 1974 Analog Silicon Synthesis &amp; WebSockets Audio.</div>
        </div>
      </div>
    </div>

    <!-- =======================================================================
         CATEGORY A: FLAGSHIP TOOLS, GAMES & CALCULATORS BUILT BY LUM (MATH + ART)
         ======================================================================= -->
    <div style="margin-top: 35px; margin-bottom: 20px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; border-bottom: 2px solid #00ff66; padding-bottom: 8px;">
        <div>
          <span style="background: #00ff66; color: #000; font-weight: 900; font-size: 0.72rem; padding: 3px 8px; border-radius: 3px; letter-spacing: 1.5px;">FLAGSHIP LAB</span>
          <span style="color: #ffffff; font-weight: 800; font-size: 1.15rem; margin-left: 10px; letter-spacing: 2px;">INTERACTIVE TOOLS, GAMES &amp; CALCULATORS BUILT BY LUM</span>
        </div>
        <div style="color: #8ce4a7; font-size: 0.74rem; font-weight: 700;">
          [4 ACTIVE SUITES // EXPANDING REGISTRY]
        </div>
      </div>
      <p style="color: #a0f0c0; font-size: 0.78rem; line-height: 1.5; margin-top: 8px;">
        Below are the interactive serious games, visual mathematical tools, and scientific calculators built by Lum. Each combines computational depth with artistic visual learning, designed to illuminate the invisible spectrum and empower human equilibrium. More pages and tools are actively being added to this suite.
      </p>
    </div>

    <div class="public-projects-grid">

      <!-- Tool/Game 1: Shadertoy 3D Earth // Beautypi Tribute -->
      <article class="cyber-card public-proj-card" style="border-top: 3px solid #00ffcc;">
        <div class="card-glow-bar" style="background: #00ffcc;"></div>
        <div class="card-meta">
          <span class="proj-id" style="color: #00ffcc;">GAME-01 // WSM &amp; SHADERTOY</span>
          <span class="status-pill cyan">DEDICATED GAME</span>
        </div>
        <h3 class="proj-title" style="color: #ffffff;">Shadertoy 3D Earth &amp; Phototherapy Game</h3>
        <div class="proj-tagline" style="color: #00ffcc;">Homage to I&ntilde;igo Qu&iacute;lez &amp; Pol Jeremias (Beautypi) // "Not Quite Home"</div>
        <p class="proj-desc">
          An open-source WebGL serious game featuring a 3D Earth globe orbiting in deep space, sliced by 12 invisible Keplerian spectrum layers. Built with the <strong>Wave Structure of Matter (WSM)</strong> and <strong>Euler's Wave Identity</strong> ($e^{i\pi} + 1 = 0$). Includes dual Child/Adult modes, a paint-brush photon gun blasting sacred geometry and words into orbit, an image shader drawer, and a clinical 532nm phototherapy station for depression recovery.
        </p>
        <div class="proj-specs">
          <span>◈ WebGL Raymarching Shader</span>
          <span>◈ Euler WSM Physics Engine</span>
          <span>◈ 532nm Phototherapy Tool</span>
          <span>◈ Dual Child / Adult Modes</span>
        </div>
        <div class="proj-footer">
          <a href="/shadertoy/" class="cyber-btn sm" style="border-color: #00ffcc; color: #00ffcc;">
            <span>LAUNCH DEDICATED GAME</span> <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Tool/Game 2: The New Monopoly // Spectrum Vision Simulator -->
      <article class="cyber-card public-proj-card" style="border-top: 3px solid #00ff66;">
        <div class="card-glow-bar" style="background: #00ff66;"></div>
        <div class="card-meta">
          <span class="proj-id" style="color: #00ff66;">GAME-02 // SPECTRUM MONOPOLY</span>
          <span class="status-pill green">ACTIVE SIMULATOR</span>
        </div>
        <h3 class="proj-title" style="color: #ffffff;">The New Monopoly // Planetary Life Simulator</h3>
        <div class="proj-tagline" style="color: #00ff66;">2D Infinite Box &amp; 3D Rotating Globe // Macro-Global to Local Economics</div>
        <p class="proj-desc">
          A real-world economic and environmental serious game built by Lum. Models the global financial system across 12 invisible spectrum strata, with an interactive <strong>2D Infinite Coordinate Box</strong> and <strong>Rotating 3D Spherical Globe</strong> emitting glowing chromatic motion trail hues. Features live planetary gauges (Environment, Humanity, Resources), homeless-to-bunker real estate, K-12 public/private school paths, AI monthly subscription leverage ($0 to $200/mo), clear-net money laundering, and the Path of Restitution to the 532nm Green Commons.
        </p>
        <div class="proj-specs">
          <span>◈ 2D Infinite Canvas + 3D Globe</span>
          <span>◈ Chromatic Motion Trail Hues</span>
          <span>◈ 12-Color Real Estate Strata</span>
          <span>◈ Moral Agency &amp; Restitution</span>
        </div>
        <div class="proj-footer">
          <a href="/spectrum-vision/" class="cyber-btn sm" style="border-color: #00ff66; color: #00ff66;">
            <span>LAUNCH SIMULATOR &amp; DEV PLAN</span> <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Tool/Game 3: Optical Vision Spectrum & Acuity Prescription Calculator -->
      <article class="cyber-card public-proj-card" style="border-top: 3px solid #ffaa00;">
        <div class="card-glow-bar" style="background: #ffaa00;"></div>
        <div class="card-meta">
          <span class="proj-id" style="color: #ffaa00;">CALC-01 // CLINICAL OPTICS</span>
          <span class="status-pill amber">MATHEMATICAL TOOL</span>
        </div>
        <h3 class="proj-title" style="color: #ffffff;">Optical Vision Spectrum &amp; Acuity Calculator</h3>
        <div class="proj-tagline" style="color: #ffaa00;">20/200 &rarr; 20/20 &rarr; 20/10 Acuity &amp; Weber Contrast Calibration</div>
        <p class="proj-desc">
          A clinical and mathematical optical calibration engine built by Lum to optimize reading focus, eliminate eye fatigue, and adapt displays to individual prescription profiles. Formulates Weber contrast dynamics, 3-stage mathematical acuity steps (Macro 20/200, Equilibrium 20/20, Hyper-Acuity 20/10), and dark-to-light spectrum polarity reversals anchored at the 532nm photopic peak.
        </p>
        <div class="proj-specs">
          <span>◈ Weber Contrast Metric</span>
          <span>◈ 3-Stage Prescription Gauge</span>
          <span>◈ Polarity Inversion Engine</span>
          <span>◈ Anti-Fatigue Micro-Vector</span>
        </div>
        <div class="proj-footer">
          <a href="#vision-calibration-deck" class="cyber-btn sm" style="border-color: #ffaa00; color: #ffaa00;">
            <span>ENGAGE CALIBRATOR DECK</span> <span>↓</span>
          </a>
        </div>
      </article>

      <!-- Tool/Game 4: 4096-Bit Radial Vector Cipher Engine -->
      <article class="cyber-card public-proj-card" style="border-top: 3px solid #d500f9;">
        <div class="card-glow-bar" style="background: #d500f9;"></div>
        <div class="card-meta">
          <span class="proj-id" style="color: #d500f9;">CIPHER-01 // CRYPTOGRAPHY</span>
          <span class="status-pill red">RESTRICTED VAULT</span>
        </div>
        <h3 class="proj-title" style="color: #ffffff;">4096-Bit Radial Vector Cipher Engine</h3>
        <div class="proj-tagline" style="color: #d500f9;">Polar Modular Hashing &amp; Geometric Cryptographic Vault</div>
        <p class="proj-desc">
          A sovereign mathematical encryption tool mapping textual passphrases into 4096-bit polar geometric vectors ($\rho = \sqrt{x^2+y^2}, \theta = \arctan(y/x)$). Protects private research, classified audio stems, and patent specifications with tamper-evident mathematical vector verification and instant lockout defenses.
        </p>
        <div class="proj-specs">
          <span>◈ Polar Coordinate Hashing</span>
          <span>◈ 4096-Bit Vector Matrix</span>
          <span>◈ Geometric Passphrase Lock</span>
          <span>◈ Sovereign Key Derivation</span>
        </div>
        <div class="proj-footer">
          <a href="/private/" class="cyber-btn sm" style="border-color: #d500f9; color: #d500f9;">
            <span>ACCESS CIPHER VAULT</span> <span>↗</span>
          </a>
        </div>
      </article>

    </div>

    <!-- =======================================================================
         CATEGORY B: PRODUCTION SYSTEMS & ENTERPRISE ARCHITECTURE
         ======================================================================= -->
    <div style="margin-top: 40px; margin-bottom: 20px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; border-bottom: 2px solid #00e5ff; padding-bottom: 8px;">
        <div>
          <span style="background: #00e5ff; color: #000; font-weight: 900; font-size: 0.72rem; padding: 3px 8px; border-radius: 3px; letter-spacing: 1.5px;">SYSTEMS ARCHITECTURE</span>
          <span style="color: #ffffff; font-weight: 800; font-size: 1.15rem; margin-left: 10px; letter-spacing: 2px;">ENTERPRISE CLOUD, AUDIO &amp; SILICON PLATFORMS</span>
        </div>
        <div style="color: #8ce4a7; font-size: 0.74rem; font-weight: 700;">
          [PRODUCTION NODES]
        </div>
      </div>
    </div>

    <div class="public-projects-grid">

      <!-- Project 1: United Beats Audio-Synapse Core -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-UB-01</span>
          <span class="status-pill green">ACTIVE ROTATION</span>
        </div>
        <h3 class="proj-title">United Beats Audio-Synapse Core</h3>
        <div class="proj-tagline">Spatial Sound Engine &amp; Multi-Tenant Harmonic Routing</div>
        <p class="proj-desc">
          A zero-latency digital sound architecture marrying analog 1974 audio synthesis principles with modern web sockets. Routes spatialized audio stems across distributed nodes while preserving raw analog warmth and dynamic range.
        </p>
        <div class="proj-specs">
          <span>◈ Audio WebSockets</span>
          <span>◈ 12-Tone Harmonic Matrix</span>
          <span>◈ Web Audio API / Rust Core</span>
        </div>
        <div class="proj-footer">
          <a href="https://unitedbeats.online" target="_blank" rel="noopener" class="cyber-btn sm">
            <span>VISIT UNITEDBEATS.ONLINE</span> <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Project 2: HyperNexus Control Plane -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-HN-02</span>
          <span class="status-pill green">PRODUCTION CONTROL PLANE</span>
        </div>
        <h3 class="proj-title">HyperNexus Universal API Gateway</h3>
        <div class="proj-tagline">TormentNexus Powered Model Context Protocol (MCP) Router</div>
        <p class="proj-desc">
          Universal multi-tenant routing layer allowing AI agents, real estate MLS feeds, and enterprise CRMs to execute dynamic tenant context switches without database cross-contamination or cold starts.
        </p>
        <div class="proj-specs">
          <span>◈ MCP Protocol v1</span>
          <span>◈ Polar Radial Storage</span>
          <span>◈ Sub-millisecond Dispatch</span>
        </div>
        <div class="proj-footer">
          <a href="#architecture" class="cyber-btn sm">
            <span>INSPECT TOPOLOGY</span> <span>↓</span>
          </a>
        </div>
      </article>

      <!-- Project 3: Candlestixxx GitHub Ecosystem -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-CTX-03</span>
          <span class="status-pill green">OPEN SOURCE REPOSITORIES</span>
        </div>
        <h3 class="proj-title">candlestixxx Code Ecosystem</h3>
        <div class="proj-tagline">Open-Source Monorepos, WordPress Engines &amp; UI Shaders</div>
        <p class="proj-desc">
          Directly synchronizing Lumbros's production work across Hetzner, GitHub, and local workstations. Includes full WordPress headless configs, Nginx reverse proxy optimizations, and custom cyber shaders.
        </p>
        <div class="proj-specs">
          <span>◈ GitHub / candlestixxx</span>
          <span>◈ Nginx 1.24 + PHP 8.4</span>
          <span>◈ Bash &amp; PowerShell Sync</span>
        </div>
        <div class="proj-footer">
          <a href="https://github.com/candlestixxx" target="_blank" rel="noopener" class="cyber-btn sm">
            <span>VIEW CANDLESTIXXX GITHUB</span> <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Project 4: 1974 Chip Matrix -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">CHIP-1974</span>
          <span class="status-pill green">HARDWARE ARCHITECTURE</span>
        </div>
        <h3 class="proj-title">1974 Alpha Brain &amp; 4 Silicon Chips</h3>
        <div class="proj-tagline">Discrete Arithmetic Logic Units &amp; Sovereign Neural Compute</div>
        <p class="proj-desc">
          Architectural schematic uniting the 1974 Alpha Brain with 4 specialized silicon micro-architectures: Alpha HyperNexus Matrix, Beta Vector Coprocessor, Gamma Sovereign Crypto Core, and Delta Analog Wave Modulator.
        </p>
        <div class="proj-specs">
          <span>◈ Discrete 1974 Logic</span>
          <span>◈ Quad-Core Silicon Matrix</span>
          <span>◈ Sovereign Instruction Set</span>
        </div>
        <div class="proj-footer">
          <a href="#digital-billboard" class="cyber-btn sm">
            <span>EXPLORE CHIP MATRIX</span> <span>↓</span>
          </a>
        </div>
      </article>

    </div>

    <!-- =======================================================================
         CATEGORY C: UPCOMING PIPELINE REGISTRY (EXPANDABLE SUITE)
         ======================================================================= -->
    <div style="margin-top: 35px; background: rgba(5,14,24,0.7); border: 1px dashed rgba(0,255,102,0.3); border-radius: 8px; padding: 18px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
        <div style="color: #00ff66; font-weight: 800; font-size: 0.8rem; letter-spacing: 1.5px;">
          EXPANDABLE MODULAR REGISTRY // FUTURE PAGES &amp; TOOLS COMING TO LUMBROS.ME
        </div>
        <div style="color: #00e5ff; font-size: 0.72rem; font-weight: 700;">
          STATUS: IN ACTIVE STAGING
        </div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-size: 0.72rem; color: #8ce4a7;">
        <div style="background: rgba(0,255,102,0.04); padding: 8px 12px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.15);">
          <strong style="color: #ffffff;">PIPELINE 01:</strong> WSM Standing Wave Particle Synthesizer (Euler harmonic visualizer)
        </div>
        <div style="background: rgba(0,229,255,0.04); padding: 8px 12px; border-radius: 4px; border: 1px solid rgba(0,229,255,0.15);">
          <strong style="color: #ffffff;">PIPELINE 02:</strong> Neuro-Acoustic 532nm Solfeggio Frequency Generator (Binaural healing suite)
        </div>
        <div style="background: rgba(255,170,0,0.04); padding: 8px 12px; border-radius: 4px; border: 1px solid rgba(255,170,0,0.15);">
          <strong style="color: #ffffff;">PIPELINE 03:</strong> Decentralized Sovereign Agent Commons (Multiplayer P2P economy)
        </div>
      </div>
    </div>

  </section>
'''

# ---------------------------------------------------------------------------
# Replace Section in homepage.html using match indices (avoids re.sub escape issues)
# ---------------------------------------------------------------------------
pattern = r'<section id="public-pages"[\s\S]*?</section>'
match = re.search(pattern, home)
if match:
    home = home[:match.start()] + enhanced_public_section.strip() + home[match.end():]
    print("Replaced #public-pages section in deploy/homepage.html")
else:
    print("ERROR: Could not find <section id='public-pages'> in homepage.html")

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print("SUCCESS: Updated homepage.html with organized Executive Resume, Portfolio & Tools Lab!")
