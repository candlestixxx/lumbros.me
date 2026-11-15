#!/usr/bin/env python3
"""
Adds Section 0x09: Procedural Shadertoy & Mathematical Graphics Engine
Honoring Iñigo Quílez and Pol Jeremias (Beautypi) with inspiration from "Not quite home" (Mt33Wj)
"""

import os
import re

HOMEPAGE_PATH = os.path.join(os.path.dirname(__file__), 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if section 0x09 already added
if 'id="shadertoy-tribute"' in content:
    print("Section 0x09 already present, removing old version for fresh install...")
    content = re.sub(r'<!-- ===+\s*SECTION 0x09: PROCEDURAL SHADERTOY[\s\S]*?<!-- ===+\s*SUB MENU DOCK', '<!-- =========================================================================\n       SUB MENU DOCK', content)

# 1. Section 0x09 HTML Markup
section_html = '''  <!-- =========================================================================
       SECTION 0x09: PROCEDURAL SHADERTOY & MATHEMATICAL GRAPHICS ENGINE
       TRIBUTE TO THE CREATORS OF SHADERTOY: IÑIGO QUÍLEZ & POL JEREMIAS (BEAUTYPI)
       INSPIRATION: "NOT QUITE HOME" (SHADERTOY Mt33Wj)
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
        <!-- Mathematical SDF Raymarching & Pi Glyph Homage -->
        <circle class="geo-archetype" cx="600" cy="180" r="65" stroke-dasharray="6 4"></circle>
        <circle class="geo-archetype" cx="600" cy="180" r="35"></circle>
        <line class="geo-archetype" x1="560" y1="135" x2="640" y2="135" stroke-width="3"></line>
        <line class="geo-archetype" x1="580" y1="135" x2="575" y2="225" stroke-width="2.5"></line>
        <path class="geo-archetype" d="M 620,135 L 620,215 Q 620,225 632,225" fill="none" stroke-width="2.5"></path>
      </svg>
      <div class="matrix-grid-pattern"></div>
    </div>

    <!-- Section Identification Badge -->
    <div class="section-badge">
      <span>[ SECTION 0x09 ]</span> // PROCEDURAL SHADERTOY &amp; MATHEMATICAL GRAPHICS ENGINE
    </div>

    <!-- Section Headline with 7-Pattern Circulating Founder Gradient -->
    <h2 class="section-title unicode-headline">
      ⟬ 𝐒𝐇𝐀𝐃𝐄𝐑𝐓𝐎𝐘 𝐇𝐎𝐌𝐀𝐆𝐄 : 𝐍𝐎𝐓 𝐐𝐔𝐈𝐓𝐄 𝐇𝐎𝐌𝐄 &amp; 𝐓𝐇𝐄 𝐏𝐔𝐑𝐄 𝐌𝐀𝐓𝐇 𝐔𝐍𝐈𝐕𝐄𝐑𝐒𝐄 ⟭
    </h2>

    <!-- Tribute Card Frame -->
    <div class="shadertoy-tribute-frame">
      <div class="twin-vertical-scanline-rail-left" aria-hidden="true"></div>
      <div class="twin-vertical-scanline-rail-right" aria-hidden="true"></div>

      <!-- Top Tribute Header Capsule -->
      <div class="tribute-header-capsule">
        <div class="tribute-header-meta">
          <span class="tribute-dot-pulse"></span>
          <span class="tribute-meta-code">BEAUTYPI LABS // EST. 2013 // BARCELONA &amp; SAN FRANCISCO</span>
        </div>
        <div class="tribute-header-title">
          <span>TRIBUTE TO THE ARCHITECTS OF REAL-TIME PROCEDURAL ART</span>
        </div>
      </div>

      <!-- Manifesto Epigraph -->
      <div class="tribute-epigraph-box">
        <div class="epigraph-quote-mark">“</div>
        <p class="epigraph-text">
          Before <strong>Shadertoy</strong>, computer graphics required multi-gigabyte engines, polygon meshes, and pre-baked textures. 
          <a href="https://www.google.com/search?kgmid=%2Fg%2F11kbzfx85g&amp;q=I%C3%B1igo+Qu%C3%ADlez" target="_blank" rel="noopener" class="tribute-author-link">Iñigo Quílez</a> 
          and 
          <a href="https://www.google.com/search?kgmid=%2Fg%2F11s1t3lc51&amp;q=Pol+Jeremias" target="_blank" rel="noopener" class="tribute-author-link">Pol Jeremias</a> 
          (via <strong>Beautypi</strong>) proved to the world that an entire cosmos—its light, terrain, atmospheric scattering, and sacred geometry—can be evaluated in real time from a single fragment of mathematical code running across each ray of light.
          Here on <em>lumbros.me</em>, where <strong>artistic design, ideas, and creativity are represented through mathematics and God</strong>, we salute their pioneering genius.
        </p>
      </div>

      <!-- Creators 3-Column Homage Grid -->
      <div class="shadertoy-creators-grid">

        <!-- Creator 1: Iñigo Quílez -->
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
            Legendary demoscene icon and former Pixar computer graphics researcher (procedural vegetation algorithms for <em>Brave</em>). Pioneer of 2D/3D Signed Distance Fields (SDFs), raymarching primitives, smooth minimum formulas (<code>smin</code>), and procedural cosine palettes.
          </p>
          <div class="creator-chips">
            <span class="creator-chip">SDF RAYMARCHING</span>
            <span class="creator-chip">PIXAR RESEARCH</span>
            <span class="creator-chip">SMOOTH MIN (smin)</span>
            <span class="creator-chip">COSINE PALETTES</span>
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
            Computer graphics architect with leadership roles at Pixar and Netflix Games. Co-architect of Beautypi and Shadertoy's real-time WebGL execution pipeline, democratizing fragment shader programming and GPU performance for millions of creators worldwide.
          </p>
          <div class="creator-chips">
            <span class="creator-chip">GPU ARCHITECTURE</span>
            <span class="creator-chip">WEBGL PIONEER</span>
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

        <!-- Creator 3: Beautypi & "Not Quite Home" -->
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
            Founded in 2013 by Jeremias and Quílez to launch Shadertoy. Inspired by the evocative procedural shader <em>"Not quite home"</em> (<code>Mt33Wj</code>), capturing the infinite cyber-horizon and misty digital sanctuary of travelers navigating between code, soul, and home.
          </p>
          <div class="creator-chips">
            <span class="creator-chip">BEAUTYPI LAB</span>
            <span class="creator-chip">SHADER: Mt33Wj</span>
            <span class="creator-chip">ATMOSPHERIC HORIZON</span>
            <span class="creator-chip">SACRED VOID</span>
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

      <!-- Live WebGL Interactive Shader Canvas Deck -->
      <div class="shadertoy-canvas-container" id="shadertoy-engine-box">

        <!-- Canvas Top Telemetry Bar -->
        <div class="canvas-telemetry-bar">
          <div class="telemetry-left">
            <span class="canvas-live-dot"></span>
            <span class="telemetry-title">LIVE WEBGL 2.0 FRAGMENT PIPELINE</span>
            <span class="telemetry-tag" id="shader-fps-counter">60.0 FPS</span>
          </div>
          <div class="telemetry-right">
            <span class="telemetry-chip">UNIFORMS: iTime, iResolution, iMouse, iAcuity</span>
            <span class="telemetry-chip" id="shader-res-badge">CANVAS: 960x420</span>
          </div>
        </div>

        <!-- The Canvas Viewport -->
        <div class="canvas-viewport-wrap" id="canvas-viewport-wrap">
          <canvas id="shadertoy-gl-canvas" class="shadertoy-gl-canvas"></canvas>

          <!-- Interactive HUD Overlay -->
          <div class="canvas-hud-overlay" id="canvas-hud-overlay">
            <div class="hud-mode-pill" id="hud-mode-pill">
              <span class="pill-prefix">ACTIVE SHADER //</span>
              <span class="pill-name" id="hud-active-mode-name">MODE 01: NOT QUITE HOME (ATMOSPHERIC HORIZON)</span>
            </div>
            <div class="hud-touch-hint">
              <span>❖ DRAG / TOUCH TO ORBIT CAMERA &amp; TILT PERSPECTIVE ❖</span>
            </div>
            <div class="hud-corner-math">
              <span>f(x,y,t) = ℛ(ro, rd) · smin(d₁, d₂, k)</span>
            </div>
          </div>
        </div>

        <!-- Interactive Control Console -->
        <div class="shadertoy-controls-rail">

          <!-- Shader Mode Selection -->
          <div class="control-group mode-selector-group">
            <span class="control-label">SHADER MODE:</span>
            <div class="btn-group-toggle">
              <button type="button" class="shader-ctrl-btn active" id="btn-mode-0" data-mode="0">
                <span>01. NOT QUITE HOME</span>
              </button>
              <button type="button" class="shader-ctrl-btn" id="btn-mode-1" data-mode="1">
                <span>02. SDF CATHEDRAL</span>
              </button>
              <button type="button" class="shader-ctrl-btn" id="btn-mode-2" data-mode="2">
                <span>03. 12-SPECTRUM HARMONICS</span>
              </button>
            </div>
          </div>

          <!-- Playback and Performance Controls -->
          <div class="control-group playback-group">
            <button type="button" class="shader-ctrl-btn" id="btn-shader-playpause">
              <span id="btn-playpause-text">❚❚ PAUSE</span>
            </button>
            <button type="button" class="shader-ctrl-btn" id="btn-shader-restart">
              <span>↺ RESET TIME</span>
            </button>
            <button type="button" class="shader-ctrl-btn" id="btn-shader-res-toggle">
              <span id="res-scale-text">RES: 1.0x</span>
            </button>
            <button type="button" class="shader-ctrl-btn" id="btn-shader-fullscreen">
              <span>⛶ EXPAND</span>
            </button>
            <button type="button" class="shader-ctrl-btn highlight" id="btn-toggle-glsl">
              <span>{ } VIEW GLSL SOURCE</span>
            </button>
          </div>

        </div>

        <!-- Collapsible GLSL Source Code Inspector Drawer -->
        <div class="glsl-drawer-box" id="glsl-code-drawer" style="display: none;">
          <div class="glsl-drawer-header">
            <div class="drawer-title">
              <span class="drawer-icon">⟨/⟩</span>
              <span>LIVE GLSL FRAGMENT SHADER CODE // SHADERTOY SPECIFICATION</span>
            </div>
            <div class="drawer-actions">
              <button type="button" class="drawer-copy-btn" id="btn-copy-glsl">
                <span>📋 COPY GLSL SOURCE</span>
              </button>
            </div>
          </div>
          <pre class="glsl-code-view" id="glsl-code-pre"><code>precision highp float;

uniform vec2 u_resolution;
uniform float u_time;
uniform vec2 u_mouse;
uniform float u_acuity;
uniform int u_mode;
uniform int u_theme;
uniform vec3 u_archetype_col;

// Inigo Quilez Procedural Cosine Color Palette Formula
vec3 iqPalette(in float t, in vec3 a, in vec3 b, in vec3 c, in vec3 d) {
    return a + b * cos(6.2831853 * (c * t + d));
}

// Inigo Quilez Signed Distance Functions
float sdSphere(vec3 p, float s) { return length(p) - s; }
float sdBox(vec3 p, vec3 b) {
    vec3 d = abs(p) - b;
    return min(max(d.x, max(d.y, d.z)), 0.0) + length(max(d, 0.0));
}
float sdTorus(vec3 p, vec2 t) {
    vec2 q = vec2(length(p.xz) - t.x, p.y);
    return length(q) - t.y;
}

// Inigo Quilez Smooth Minimum (Polynomial smin)
float smin(float a, float b, float k) {
    float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);
    return mix(b, a, h) - k * h * (1.0 - h);
}

mat2 rot2D(float a) {
    float c = cos(a), s = sin(a);
    return mat2(c, -s, s, c);
}

// Mode 0: "Not Quite Home" Atmospheric Horizon & Sacred Cyber Sanctuary
vec4 renderNotQuiteHome(vec2 uv, vec2 mouse) {
    vec3 ro = vec3(0.0, 1.0, -3.5);
    vec3 rd = normalize(vec3(uv, 1.3));
    rd.yz = rot2D(-mouse.y * 0.8 + 0.2) * rd.yz;
    rd.xz = rot2D(mouse.x * 1.5 + u_time * 0.05) * rd.xz;
    
    vec3 col = vec3(0.0);
    float horizon = rd.y;
    vec3 skyHorizon = mix(vec3(0.01, 0.03, 0.05), vec3(0.08, 0.02, 0.14), clamp(1.0 - abs(horizon) * 2.5, 0.0, 1.0));
    skyHorizon += u_archetype_col * 0.15 * exp(-abs(horizon) * 6.0);
    
    if (rd.y < -0.01) {
        float tFloor = -(ro.y + 0.4) / rd.y;
        if (tFloor > 0.0) {
            vec3 pos = ro + rd * tFloor;
            vec2 grid = abs(fract(pos.xz * 1.2 - vec2(0.0, u_time * 0.8)) - 0.5);
            float line = smoothstep(0.04, 0.0, min(grid.x, grid.y));
            float fog = exp(-tFloor * (0.12 - u_acuity * 0.04));
            vec3 floorCol = mix(vec3(0.02, 0.06, 0.04), mix(vec3(0.0, 1.0, 0.4), u_archetype_col, 0.5), line * 0.85);
            col = mix(skyHorizon, floorCol, fog);
        }
    } else {
        col = skyHorizon;
    }
    
    // Distant Spire of Solitude
    float t = 0.0;
    for (int i = 0; i < 48; i++) {
        vec3 p = ro + rd * t;
        float dTower = sdBox(p - vec3(0.0, 1.2, 8.0), vec3(0.35, 2.2, 0.35));
        float dRing = sdTorus(p - vec3(0.0, 1.8 + sin(u_time * 1.5) * 0.3, 8.0), vec2(0.9, 0.06));
        float dDist = min(dTower, dRing);
        if (dDist < 0.01) {
            vec3 objCol = mix(vec3(0.0, 0.9, 0.5), vec3(1.0, 0.8, 0.2), sin(p.y * 3.0 + u_time) * 0.5 + 0.5);
            col = mix(col, objCol, exp(-t * 0.08) * 0.9);
            break;
        }
        t += dDist * 0.85;
        if (t > 25.0) break;
    }
    
    float sunDist = length(uv - vec2(0.0, 0.15 + mouse.y * 0.3));
    col += mix(vec3(0.2, 1.0, 0.5), vec3(1.0, 0.9, 0.4), sin(u_time * 0.8) * 0.5 + 0.5) * (0.035 / (sunDist * sunDist + 0.035)) * 0.6;
    return vec4(col, 1.0);
}

void main() {
    vec2 uv = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / min(u_resolution.x, u_resolution.y);
    vec2 mouse = u_mouse / u_resolution.xy - 0.5;
    gl_FragColor = renderNotQuiteHome(uv, mouse);
}</code></pre>
        </div>

      </div>

      <!-- Tribute Footer Signature -->
      <div class="tribute-footer-signature">
        <span>⟦ SHADERTOY.COM // BEAUTYPI // IÑIGO QUÍLEZ // POL JEREMIAS // ALL CREATIVITY REPRESENTED THROUGH MATHEMATICS &amp; GOD ⟧</span>
      </div>

    </div>
  </section>
'''

# 2. Section 0x09 CSS Styles
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
      margin-bottom: 35px;
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
    .creator-titles {
      overflow: hidden;
    }
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

    /* Live WebGL Canvas Deck */
    .shadertoy-canvas-container {
      background: #000b05;
      border: 1.5px solid #00ff66;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 0 35px rgba(0, 255, 102, 0.2);
      margin-bottom: 24px;
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

    /* Canvas Viewport */
    .canvas-viewport-wrap {
      position: relative;
      width: 100%;
      height: 480px;
      background: #000000;
      overflow: hidden;
      cursor: grab;
    }
    .canvas-viewport-wrap:active {
      cursor: grabbing;
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
    .hud-mode-pill {
      align-self: flex-start;
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
    .hud-touch-hint {
      align-self: center;
      background: rgba(0, 15, 8, 0.6);
      border: 1px dashed rgba(0, 255, 102, 0.4);
      padding: 6px 16px;
      border-radius: 6px;
      font-size: 0.72rem;
      color: #a8f5c8;
      letter-spacing: 2px;
      font-weight: 600;
      animation: fadeInOut 4s infinite alternate;
    }
    @keyframes fadeInOut {
      0% { opacity: 0.35; }
      100% { opacity: 0.85; }
    }
    .hud-corner-math {
      align-self: flex-end;
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.76rem;
      color: rgba(0, 255, 102, 0.75);
      background: rgba(0, 20, 10, 0.65);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid #14442a;
    }

    /* Control Rail */
    .shadertoy-controls-rail {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      padding: 14px 18px;
      background: rgba(0, 25, 12, 0.95);
      border-top: 1px solid #1a5c34;
    }
    .control-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .control-label {
      font-size: 0.72rem;
      color: #00ff66;
      font-weight: 800;
      letter-spacing: 1.5px;
    }
    .btn-group-toggle {
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
    .shader-ctrl-btn.highlight {
      border-color: #00e5ff;
      color: #00e5ff;
    }
    .shader-ctrl-btn.highlight:hover {
      background: #00e5ff;
      color: #00150a;
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.5);
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
      font-size: 0.82rem;
      line-height: 1.5;
      max-height: 360px;
      overflow-y: auto;
      white-space: pre;
    }

    /* Tribute Signature */
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

    /* Light Theme Polarity Enforcements */
    body[data-theme="light"] .shadertoy-tribute-frame {
      background: #ffffff !important;
      border-color: #008736 !important;
      box-shadow: 0 6px 25px rgba(0, 100, 40, 0.12) !important;
    }
    body[data-theme="light"] .tribute-header-capsule {
      background: #eefbf4 !important;
      border-color: #a3dfbd !important;
    }
    body[data-theme="light"] .tribute-header-meta {
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
    body[data-theme="light"] .tribute-author-link {
      color: #006622 !important;
    }
    body[data-theme="light"] .creator-card {
      background: #f7fdf9 !important;
      border-color: #b8e6cd !important;
    }
    body[data-theme="light"] .creator-name a {
      color: #0a2615 !important;
    }
    body[data-theme="light"] .creator-bio {
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
    body[data-theme="light"] .shadertoy-canvas-container {
      border-color: #008736 !important;
    }
    body[data-theme="light"] .canvas-telemetry-bar,
    body[data-theme="light"] .shadertoy-controls-rail {
      background: #f2faf5 !important;
      border-color: #b8e6cd !important;
    }
    body[data-theme="light"] .telemetry-title,
    body[data-theme="light"] .control-label {
      color: #006622 !important;
    }
    body[data-theme="light"] .telemetry-chip,
    body[data-theme="light"] .telemetry-tag {
      background: #e0f5e8 !important;
      border-color: #94d4b1 !important;
      color: #006622 !important;
    }
    body[data-theme="light"] .shader-ctrl-btn {
      background: #e8f8ef !important;
      border-color: #8ed2ad !important;
      color: #0e3b1f !important;
    }
    body[data-theme="light"] .shader-ctrl-btn.active {
      background: #008736 !important;
      color: #ffffff !important;
    }
    body[data-theme="light"] .tribute-footer-signature {
      background: #edf8f1 !important;
      border-color: #98d8b4 !important;
      color: #005a20 !important;
    }
'''

# 3. Section 0x09 JavaScript Engine
section_js = '''
    // =========================================================================
    // SECTION 0x09: PROCEDURAL SHADERTOY WEBGL ENGINE (NOT QUITE HOME HOMAGE)
    // =========================================================================
    (function initShadertoyHomage() {
      var canvas = document.getElementById('shadertoy-gl-canvas');
      var wrap = document.getElementById('canvas-viewport-wrap');
      if (!canvas) return;

      var gl = canvas.getContext('webgl2') || canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
      if (!gl) {
        console.warn('[Shadertoy Engine] WebGL not supported on this device/browser.');
        return;
      }

      // Vertex Shader Source
      var vsSource = [
        'attribute vec2 position;',
        'void main() {',
        '    gl_Position = vec4(position, 0.0, 1.0);',
        '}'
      ].join('\\n');

      // Fragment Shader Source
      var fsSource = [
        'precision highp float;',
        'uniform vec2 u_resolution;',
        'uniform float u_time;',
        'uniform vec2 u_mouse;',
        'uniform float u_acuity;',
        'uniform int u_mode;',
        'uniform int u_theme;',
        'uniform vec3 u_archetype_col;',
        '',
        '// Inigo Quilez Procedural Cosine Color Palette',
        'vec3 iqPalette(in float t, in vec3 a, in vec3 b, in vec3 c, in vec3 d) {',
        '    return a + b * cos(6.2831853 * (c * t + d));',
        '}',
        '',
        '// Inigo Quilez Signed Distance Functions',
        'float sdSphere(vec3 p, float s) { return length(p) - s; }',
        'float sdBox(vec3 p, vec3 b) {',
        '    vec3 d = abs(p) - b;',
        '    return min(max(d.x, max(d.y, d.z)), 0.0) + length(max(d, 0.0));',
        '}',
        'float sdTorus(vec3 p, vec2 t) {',
        '    vec2 q = vec2(length(p.xz) - t.x, p.y);',
        '    return length(q) - t.y;',
        '}',
        '',
        '// Inigo Quilez Smooth Minimum',
        'float smin(float a, float b, float k) {',
        '    float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);',
        '    return mix(b, a, h) - k * h * (1.0 - h);',
        '}',
        '',
        'mat2 rot2D(float a) {',
        '    float c = cos(a);',
        '    float s = sin(a);',
        '    return mat2(c, -s, s, c);',
        '}',
        '',
        'float hash(vec2 p) {',
        '    p = fract(p * vec2(123.34, 456.21));',
        '    p += dot(p, p + 45.32);',
        '    return fract(p.x * p.y);',
        '}',
        '',
        '// Mode 0: Not Quite Home (Atmospheric Horizon & Sacred Sanctuary)',
        'vec4 renderNotQuiteHome(vec2 uv, vec2 mouse) {',
        '    vec3 ro = vec3(0.0, 1.0, -3.5);',
        '    vec3 rd = normalize(vec3(uv, 1.3));',
        '    rd.yz = rot2D(-mouse.y * 0.8 + 0.2) * rd.yz;',
        '    rd.xz = rot2D(mouse.x * 1.5 + u_time * 0.05) * rd.xz;',
        '    ',
        '    vec3 col = vec3(0.0);',
        '    float horizon = rd.y;',
        '    vec3 skyDark = vec3(0.01, 0.03, 0.05);',
        '    vec3 skyDusk = vec3(0.08, 0.02, 0.14);',
        '    vec3 skyHorizon = mix(skyDark, skyDusk, clamp(1.0 - abs(horizon) * 2.5, 0.0, 1.0));',
        '    skyHorizon += u_archetype_col * 0.15 * exp(-abs(horizon) * 6.0);',
        '    ',
        '    if (rd.y < -0.01) {',
        '        float tFloor = -(ro.y + 0.4) / rd.y;',
        '        if (tFloor > 0.0) {',
        '            vec3 pos = ro + rd * tFloor;',
        '            vec2 grid = abs(fract(pos.xz * 1.2 - vec2(0.0, u_time * 0.8)) - 0.5);',
        '            float line = smoothstep(0.04, 0.0, min(grid.x, grid.y));',
        '            float fog = exp(-tFloor * (0.12 - u_acuity * 0.04));',
        '            vec3 gridColor = mix(vec3(0.0, 1.0, 0.4), u_archetype_col, 0.5);',
        '            vec3 floorCol = mix(vec3(0.02, 0.06, 0.04), gridColor, line * 0.85);',
        '            float scan = sin(pos.z * 4.0 - u_time * 3.0) * 0.5 + 0.5;',
        '            floorCol += u_archetype_col * scan * 0.25 * line;',
        '            col = mix(skyHorizon, floorCol, fog);',
        '        }',
        '    } else {',
        '        col = skyHorizon;',
        '    }',
        '    ',
        '    // Spire on the Horizon',
        '    float t = 0.0;',
        '    float maxDist = 25.0;',
        '    for (int i = 0; i < 48; i++) {',
        '        vec3 p = ro + rd * t;',
        '        float dTower = sdBox(p - vec3(0.0, 1.2, 8.0), vec3(0.35, 2.2, 0.35));',
        '        float dRing = sdTorus(p - vec3(0.0, 1.8 + sin(u_time * 1.5) * 0.3, 8.0), vec2(0.9, 0.06));',
        '        float dDist = min(dTower, dRing);',
        '        if (dDist < 0.01) {',
        '            vec3 objCol = mix(vec3(0.0, 0.9, 0.5), vec3(1.0, 0.8, 0.2), sin(p.y * 3.0 + u_time) * 0.5 + 0.5);',
        '            float fog = exp(-t * 0.08);',
        '            col = mix(col, objCol, fog * 0.9);',
        '            break;',
        '        }',
        '        t += dDist * 0.85;',
        '        if (t > maxDist) break;',
        '    }',
        '    ',
        '    float sunDist = length(uv - vec2(0.0, 0.15 + mouse.y * 0.3));',
        '    float sunGlow = 0.035 / (sunDist * sunDist + 0.035);',
        '    col += mix(vec3(0.2, 1.0, 0.5), vec3(1.0, 0.9, 0.4), sin(u_time * 0.8) * 0.5 + 0.5) * sunGlow * 0.6;',
        '    float stars = pow(hash(floor(uv * 120.0 + vec2(u_time * 0.02, 0.0))), 25.0);',
        '    col += vec3(stars) * clamp(rd.y, 0.0, 1.0) * 0.7;',
        '    return vec4(col, 1.0);',
        '}',
        '',
        '// Mode 1: SDF Cathedral (Inigo Quilez Raymarcher)',
        'vec4 renderSDFCathedral(vec2 uv, vec2 mouse) {',
        '    vec3 ro = vec3(0.0, 0.0, -3.2);',
        '    vec3 rd = normalize(vec3(uv, 1.2));',
        '    rd.yz = rot2D(-mouse.y * 1.2) * rd.yz;',
        '    rd.xz = rot2D(mouse.x * 2.0 + u_time * 0.4) * rd.xz;',
        '    ro.xz = rot2D(mouse.x * 2.0 + u_time * 0.4) * ro.xz;',
        '    ro.yz = rot2D(-mouse.y * 1.2) * ro.yz;',
        '    ',
        '    float t = 0.0;',
        '    float maxDist = 20.0;',
        '    float d = 0.0;',
        '    int stepsTaken = 0;',
        '    for (int i = 0; i < 64; i++) {',
        '        vec3 p = ro + rd * t;',
        '        float dBox = sdBox(p, vec3(0.75));',
        '        float dTorus = sdTorus(p, vec2(1.15, 0.12));',
        '        float dSphere = sdSphere(p, 0.95 + 0.15 * sin(u_time * 2.0));',
        '        float blend = smin(dBox, dTorus, 0.25);',
        '        d = smin(blend, dSphere, 0.2);',
        '        if (d < 0.002) { stepsTaken = i; break; }',
        '        if (t > maxDist) { stepsTaken = i; break; }',
        '        t += d * (0.8 + u_acuity * 0.15);',
        '    }',
        '    ',
        '    vec3 col = vec3(0.01, 0.03, 0.05);',
        '    if (t < maxDist) {',
        '        vec3 p = ro + rd * t;',
        '        vec2 e = vec2(0.003, 0.0);',
        '        vec3 nor = normalize(vec3(',
        '            smin(smin(sdBox(p + e.xyy, vec3(0.75)), sdTorus(p + e.xyy, vec2(1.15, 0.12)), 0.25), sdSphere(p + e.xyy, 0.95), 0.2) -',
        '            smin(smin(sdBox(p - e.xyy, vec3(0.75)), sdTorus(p - e.xyy, vec2(1.15, 0.12)), 0.25), sdSphere(p - e.xyy, 0.95), 0.2),',
        '            smin(smin(sdBox(p + e.yxy, vec3(0.75)), sdTorus(p + e.yxy, vec2(1.15, 0.12)), 0.25), sdSphere(p + e.yxy, 0.95), 0.2) -',
        '            smin(smin(sdBox(p - e.yxy, vec3(0.75)), sdTorus(p - e.yxy, vec2(1.15, 0.12)), 0.25), sdSphere(p - e.yxy, 0.95), 0.2),',
        '            smin(smin(sdBox(p + e.yyx, vec3(0.75)), sdTorus(p + e.yyx, vec2(1.15, 0.12)), 0.25), sdSphere(p + e.yyx, 0.95), 0.2) -',
        '            smin(smin(sdBox(p - e.yyx, vec3(0.75)), sdTorus(p - e.yyx, vec2(1.15, 0.12)), 0.25), sdSphere(p - e.yyx, 0.95), 0.2)',
        '        ));',
        '        vec3 keyLight = normalize(vec3(1.0, 1.5, -1.0));',
        '        vec3 fillLight = normalize(vec3(-1.0, 0.5, 1.0));',
        '        float dif = max(dot(nor, keyLight), 0.0);',
        '        float fill = max(dot(nor, fillLight), 0.0) * 0.4;',
        '        float ao = 1.0 - (float(stepsTaken) / 64.0) * 0.7;',
        '        vec3 matCol = iqPalette(dot(nor, vec3(0.0, 1.0, 0.0)) * 0.5 + 0.5 + u_time * 0.1,',
        '                                vec3(0.5, 0.5, 0.5), vec3(0.5, 0.5, 0.5), vec3(1.0, 1.0, 1.0), vec3(0.0, 0.33, 0.67));',
        '        matCol = mix(matCol, u_archetype_col, 0.4);',
        '        vec3 ref = reflect(rd, nor);',
        '        float spec = pow(max(dot(ref, keyLight), 0.0), 32.0);',
        '        col = matCol * (dif + fill + 0.15) * ao + vec3(spec * 0.8);',
        '        float rim = pow(1.0 - max(dot(-rd, nor), 0.0), 3.0);',
        '        col += mix(vec3(0.0, 1.0, 0.5), vec3(0.0, 0.8, 1.0), rim) * rim * 0.6;',
        '    }',
        '    return vec4(col, 1.0);',
        '}',
        '',
        '// Mode 2: 12-Spectrum Photonic Harmonics',
        'vec4 renderSpectrumHarmonics(vec2 uv, vec2 mouse) {',
        '    vec2 p = uv * 3.0 + mouse * 2.0;',
        '    float waveAccum = 0.0;',
        '    float dist = length(p);',
        '    for (int i = 1; i <= 12; i++) {',
        '        float fi = float(i);',
        '        float angle = fi * (6.2831853 / 12.0);',
        '        vec2 dir = vec2(cos(angle), sin(angle));',
        '        float w = dot(p, dir) * (1.5 + fi * 0.35) - u_time * (1.2 + fi * 0.12);',
        '        waveAccum += sin(w) / fi;',
        '    }',
        '    float intensity = abs(waveAccum) * 0.8;',
        '    vec3 col = iqPalette(intensity + u_time * 0.15,',
        '                         vec3(0.5, 0.5, 0.5), vec3(0.5, 0.5, 0.5), vec3(1.0, 1.0, 1.0), vec3(0.0, 0.2, 0.5));',
        '    col = mix(col, u_archetype_col, 0.45);',
        '    float core = 0.05 / (dist * dist + 0.05);',
        '    col += vec3(1.0, 1.0, 0.9) * core * 0.5;',
        '    return vec4(col, 1.0);',
        '}',
        '',
        'void main() {',
        '    vec2 uv = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / min(u_resolution.x, u_resolution.y);',
        '    vec2 mouse = u_mouse / u_resolution.xy - 0.5;',
        '    vec4 finalColor;',
        '    if (u_mode == 0) {',
        '        finalColor = renderNotQuiteHome(uv, mouse);',
        '    } else if (u_mode == 1) {',
        '        finalColor = renderSDFCathedral(uv, mouse);',
        '    } else {',
        '        finalColor = renderSpectrumHarmonics(uv, mouse);',
        '    }',
        '    if (u_theme == 1) {',
        '        finalColor.rgb = mix(finalColor.rgb, vec3(1.0) - finalColor.rgb * 0.8, 0.25);',
        '    }',
        '    gl_FragColor = finalColor;',
        '}'
      ].join('\\n');

      function createShader(glCtx, type, source) {
        var shader = glCtx.createShader(type);
        glCtx.shaderSource(shader, source);
        glCtx.compileShader(shader);
        if (!glCtx.getShaderParameter(shader, glCtx.COMPILE_STATUS)) {
          console.error('[Shadertoy GLSL Error]:', glCtx.getShaderInfoLog(shader));
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
        console.error('[Shadertoy Link Error]:', gl.getProgramInfoLog(program));
        return;
      }
      gl.useProgram(program);

      // Fullscreen Quad Geometry
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
      var uArchetypeColLoc = gl.getUniformLocation(program, 'u_archetype_col');

      // State
      var isRunning = true;
      var startTime = performance.now();
      var pausedTime = 0;
      var activeMode = 0;
      var resScale = 1.0;
      var mouseX = 0, mouseY = 0;
      var isDragging = false;
      var lastMouseX = 0, lastMouseY = 0;

      // FPS Calculation
      var lastFrameTime = performance.now();
      var frameCount = 0;
      var fpsEl = document.getElementById('shader-fps-counter');
      var resEl = document.getElementById('shader-res-badge');

      function resizeCanvas() {
        var rect = canvas.getBoundingClientRect();
        var width = Math.floor(rect.width * resScale);
        var height = Math.floor(rect.height * resScale);
        if (width < 64) width = 64;
        if (height < 64) height = 64;
        if (canvas.width !== width || canvas.height !== height) {
          canvas.width = width;
          canvas.height = height;
          gl.viewport(0, 0, width, height);
          if (resEl) resEl.textContent = 'CANVAS: ' + width + 'x' + height;
        }
      }
      window.addEventListener('resize', resizeCanvas);
      resizeCanvas();

      // Mouse & Touch Drag Interactions
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
      }
      function onPointerUp() {
        isDragging = false;
      }

      canvas.addEventListener('mousedown', function(e) {
        onPointerDown(e.clientX, e.clientY);
      });
      window.addEventListener('mousemove', function(e) {
        onPointerMove(e.clientX, e.clientY);
      });
      window.addEventListener('mouseup', onPointerUp);

      canvas.addEventListener('touchstart', function(e) {
        if (e.touches.length > 0) {
          onPointerDown(e.touches[0].clientX, e.touches[0].clientY);
        }
      }, { passive: true });
      window.addEventListener('touchmove', function(e) {
        if (e.touches.length > 0) {
          onPointerMove(e.touches[0].clientX, e.touches[0].clientY);
        }
      }, { passive: true });
      window.addEventListener('touchend', onPointerUp);

      // Archetype Color Palette Map
      var archetypeColors = {
        'heart': [1.0, 0.2, 0.35],
        'flame': [1.0, 0.6, 0.1],
        'star': [1.0, 0.85, 0.1],
        'crown': [0.8, 0.3, 1.0],
        'shield': [0.1, 0.7, 1.0],
        'eye': [0.0, 1.0, 0.6],
        'infinity': [0.0, 0.9, 0.8],
        'anchor': [0.2, 0.5, 0.9]
      };

      // Main Render Loop
      function renderLoop(now) {
        if (isRunning) {
          var elapsedSec = (now - startTime) / 1000.0;

          // Compute FPS
          frameCount++;
          if (now - lastFrameTime >= 1000.0) {
            if (fpsEl) fpsEl.textContent = frameCount.toFixed(1) + ' FPS';
            frameCount = 0;
            lastFrameTime = now;
          }

          // Get Acuity and Archetype from Spectrum Engine storage
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
          gl.uniform1i(uModeLoc, activeMode);
          gl.uniform1i(uThemeLoc, themeNorm);
          gl.uniform3f(uArchetypeColLoc, archCol[0], archCol[1], archCol[2]);

          gl.drawArrays(gl.TRIANGLES, 0, 6);
        }
        requestAnimationFrame(renderLoop);
      }
      requestAnimationFrame(renderLoop);

      // UI Control Bindings
      var modeNames = [
        'MODE 01: NOT QUITE HOME (ATMOSPHERIC HORIZON)',
        'MODE 02: SDF CATHEDRAL (INIGO QUILEZ RAYMARCHING)',
        'MODE 03: 12-SPECTRUM PHOTONIC HARMONICS'
      ];
      var hudModeNameEl = document.getElementById('hud-active-mode-name');

      function setMode(modeIdx) {
        activeMode = modeIdx;
        [0, 1, 2].forEach(function(i) {
          var b = document.getElementById('btn-mode-' + i);
          if (b) {
            if (i === modeIdx) b.classList.add('active');
            else b.classList.remove('active');
          }
        });
        if (hudModeNameEl) hudModeNameEl.textContent = modeNames[modeIdx] || '';
      }

      var b0 = document.getElementById('btn-mode-0');
      var b1 = document.getElementById('btn-mode-1');
      var b2 = document.getElementById('btn-mode-2');
      if (b0) b0.addEventListener('click', function() { setMode(0); });
      if (b1) b1.addEventListener('click', function() { setMode(1); });
      if (b2) b2.addEventListener('click', function() { setMode(2); });

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
        });
      }

      var resToggleBtn = document.getElementById('btn-shader-res-toggle');
      var resScaleText = document.getElementById('res-scale-text');
      if (resToggleBtn) {
        resToggleBtn.addEventListener('click', function() {
          if (resScale === 1.0) resScale = 1.5;
          else if (resScale === 1.5) resScale = 0.5;
          else resScale = 1.0;
          if (resScaleText) resScaleText.textContent = 'RES: ' + resScale.toFixed(1) + 'x';
          resizeCanvas();
        });
      }

      var fsBtn = document.getElementById('btn-shader-fullscreen');
      if (fsBtn) {
        fsBtn.addEventListener('click', function() {
          if (!wrap) return;
          var isFs = wrap.classList.toggle('fullscreen-active');
          fsBtn.querySelector('span').textContent = isFs ? '✕ EXIT FULL' : '⛶ EXPAND';
          setTimeout(resizeCanvas, 60);
        });
      }

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
    })();
'''

# 4. Insert Section 0x09 before Section 0x10 (Pillars Architecture)
pillars_marker = '<!-- =========================================================================\n       SECTION: THE ARCHITECTURAL PILLARS & STACKABLE BRICKS OF LUMBROS.ME'
if pillars_marker not in content:
    pillars_marker = '<section id="pillars-architecture"'

if pillars_marker in content:
    content = content.replace(pillars_marker, section_html + '\n\n  ' + pillars_marker, 1)
    print("Successfully inserted Section 0x09 markup!")
else:
    print("Warning: pillars_marker not found, searching for closing main sections...")
    # fallback insertion before sub-dock
    sub_dock_marker = '<section id="sub-dock"'
    content = content.replace(sub_dock_marker, section_html + '\n\n  ' + sub_dock_marker, 1)

# 5. Insert CSS into <style> block
style_closing = '</style>'
content = content.replace(style_closing, section_css + '\n  ' + style_closing, 1)
print("Successfully inserted Section 0x09 CSS rules!")

# 6. Insert JavaScript into <script> block
script_closing = '</script>'
# Find the last </script> tag
last_script_idx = content.rfind(script_closing)
if last_script_idx != -1:
    content = content[:last_script_idx] + section_js + '\n  ' + content[last_script_idx:]
    print("Successfully inserted Section 0x09 JavaScript WebGL Engine!")

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"COMPLETE: Updated {HOMEPAGE_PATH} with Section 0x09 Shadertoy Tribute Engine!")
