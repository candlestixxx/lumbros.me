#!/usr/bin/env python3
"""
Upgrades Spectrum Monopoly Game with:
1. Interactive Dual-Viewport Engine:
   - 2-D Infinite Coordinate Box with 12 Invisible Spectrum Layers & 121 Sub-Matrix Cells
   - Rotating 3-D Spherical Globe with 12 Invisible Orbital Layers (Green 532nm at exact center equator)
   - Dual-Dock Split Mode (2D + 3D side-by-side)
2. Illumination through Invisible Layers:
   - Objects, properties, letters, shapes, or words reflect whatever color is in their underlying layer
3. Motion Trail Hue Engine:
   - Glowing chromatic motion trail that follows moving tokens, drawn shapes, or orbital objects across layers
4. Design Tools for User:
   - Paint Brush Gun (blast words, shapes, photons across 2D/3D layers)
   - Real Estate Stamp (place Tents, Homesteads, Suburbs, Towers, Bunkers onto layers)
   - Token Navigation & Dice Roller integration
   - Trail Persistence & Rotation Speed Sliders
5. 100% WordPress-safe JavaScript (ZERO raw '&&' inside script tags)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

# ---------------------------------------------------------------------------
# Visual Stage HTML Component to insert above the 12-Tile Board
# ---------------------------------------------------------------------------
visual_stage_html = '''
            <!-- =============================================================
                 THE 2-D & 3-D INVISIBLE 12-COLOR & 121-MATRIX VISUAL ENGINE
                 MOTION TRAIL HUE // OBJECT ILLUMINATION // GREEN 532nm CENTER
                 ============================================================= -->
            <div class="mono-spectrum-stage-box" style="margin-bottom: 22px; background: rgba(5,14,24,0.92); border: 1px solid rgba(0,255,102,0.35); border-radius: 8px; padding: 16px; box-shadow: 0 0 25px rgba(0,255,102,0.12);">
              
              <!-- Stage Header & Mode Switcher -->
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 14px; border-bottom: 1px solid rgba(0,255,102,0.2); padding-bottom: 10px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span class="live-dot-pulse" style="background: #00ff66;"></span>
                  <span style="font-family: 'Share Tech Mono', monospace; font-size: 0.84rem; color: #00ff66; font-weight: 800; letter-spacing: 1.5px;">
                    SPECTRUM VIEWPORT // 2-D INFINITE BOX &amp; 3-D ROTATING SPHERE
                  </span>
                </div>

                <!-- Viewport Mode Buttons -->
                <div class="stage-mode-btn-group" style="display: flex; gap: 6px;">
                  <button type="button" class="stage-view-btn active" id="btn-view-2d" data-mode="2d" style="background: rgba(0,255,102,0.2); color: #00ff66; border: 1px solid #00ff66; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                    2-D INFINITE BOX
                  </button>
                  <button type="button" class="stage-view-btn" id="btn-view-3d" data-mode="3d" style="background: rgba(0,229,255,0.1); color: #00e5ff; border: 1px solid rgba(0,229,255,0.4); font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                    3-D ROTATING SPHERE
                  </button>
                  <button type="button" class="stage-view-btn" id="btn-view-dual" data-mode="dual" style="background: rgba(255,170,0,0.1); color: #ffaa00; border: 1px solid rgba(255,170,0,0.4); font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                    DUAL SPLIT VIEW
                  </button>
                </div>
              </div>

              <!-- Interactive Drawing & Stamp Toolstrip -->
              <div class="stage-toolstrip" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px; background: rgba(0,15,30,0.6); padding: 8px 12px; border-radius: 6px; border: 1px solid rgba(0,229,255,0.2);">
                <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                  <span style="font-size: 0.72rem; color: #8ce4a7; font-weight: 700;">TOOL:</span>
                  <button type="button" class="stage-tool-btn active" id="btn-tool-brush" data-tool="brush" style="background: rgba(0,255,102,0.25); color: #00ff66; border: 1px solid #00ff66; font-size: 0.7rem; font-weight: 700; padding: 3px 8px; border-radius: 3px; cursor: pointer;">
                    🖌️ PAINT GUN / SHAPES
                  </button>
                  <button type="button" class="stage-tool-btn" id="btn-tool-stamp" data-tool="stamp" style="background: rgba(0,229,255,0.1); color: #00e5ff; border: 1px solid rgba(0,229,255,0.3); font-size: 0.7rem; font-weight: 700; padding: 3px 8px; border-radius: 3px; cursor: pointer;">
                    🏠 STAMP PROPERTY
                  </button>
                  <select id="select-stamp-type" style="background: #05101a; color: #00e5ff; border: 1px solid rgba(0,229,255,0.4); font-size: 0.68rem; padding: 2px 6px; border-radius: 3px;">
                    <option value="tent">⛺ Unhoused Camp / Tent (Stratum 01)</option>
                    <option value="homestead">🏡 Rural Homestead &amp; Aquifer (Stratum 05)</option>
                    <option value="commons" selected>★ Green Commons Sanctuary (Stratum 06 - 532nm)</option>
                    <option value="suburb">🏘️ Suburban Master-Planned Home (Stratum 07)</option>
                    <option value="tower">🏢 Urban AI Skyscraper (Stratum 08-09)</option>
                    <option value="bunker">🛡️ Subterranean Billionaire Bunker (Stratum 11-12)</option>
                  </select>
                </div>

                <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
                  <div style="display: flex; align-items: center; gap: 6px; font-size: 0.7rem; color: #b8e2c8;">
                    <span>TRAIL HUE:</span>
                    <input type="range" id="slider-trail-hue" min="1" max="10" value="8" style="width: 70px; accent-color: #00ff66; cursor: pointer;">
                  </div>
                  <div style="display: flex; align-items: center; gap: 6px; font-size: 0.7rem; color: #b8e2c8;">
                    <span>ORBIT ROTATION:</span>
                    <input type="range" id="slider-orbit-speed" min="0" max="10" value="4" style="width: 70px; accent-color: #00e5ff; cursor: pointer;">
                  </div>
                  <button type="button" id="btn-clear-canvas-trails" style="background: rgba(255,60,60,0.15); color: #ff5555; border: 1px solid rgba(255,60,60,0.4); font-size: 0.68rem; font-weight: 700; padding: 3px 8px; border-radius: 3px; cursor: pointer;">
                    ↺ CLEAR TRAILS
                  </button>
                </div>
              </div>

              <!-- Dual-Engine Interactive Canvas -->
              <div style="position: relative; width: 100%; border: 1px solid rgba(0,255,102,0.3); border-radius: 6px; overflow: hidden; background: #02060b;">
                <canvas id="mono-spectrum-canvas" width="1000" height="420" style="display: block; width: 100%; height: auto; cursor: crosshair;"></canvas>

                <!-- Floating Canvas Telemetry HUD -->
                <div style="position: absolute; bottom: 8px; left: 12px; right: 12px; display: flex; justify-content: space-between; align-items: center; pointer-events: none; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: #8ce4a7; background: rgba(5,14,24,0.75); padding: 4px 10px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.2);">
                  <div id="mono-canvas-coords">
                    LAYER: <span style="color: #00ff66; font-weight: 800;">06 [532nm GREEN HARMONIC CENTER]</span> | SUB-MATRIX: <span style="color: #00e5ff;">121-CELL GRID</span>
                  </div>
                  <div id="mono-canvas-trail-status">
                    MOTION TRAIL HUE: <span style="color: #00ff66;">ACTIVE PERSISTENCE</span> | ROTATION: <span style="color: #00e5ff;">KEPLERIAN SYNC</span>
                  </div>
                </div>
              </div>

              <!-- Scientific Explanatory Strip -->
              <div style="margin-top: 10px; font-size: 0.72rem; color: #8ce4a7; line-height: 1.5; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                <div>
                  <strong>HOW TO PLAY:</strong> Draw or blast shapes across the canvas. As your stroke travels across the <strong>12 invisible layers</strong>, it lights up in that layer's wavelength and leaves a glowing <strong>spectrum motion trail</strong>. In 3D mode, watch the 12 spherical bands rotate with Green in the center!
                </div>
                <div>
                  <span style="color: #00ff66; font-weight: 800;">[GREEN EQUILIBRIUM = SURVIVAL VICTORY]</span>
                </div>
              </div>

            </div>
'''

# ---------------------------------------------------------------------------
# JavaScript Engine for the 2D & 3D Invisible Spectrum Canvas
# ---------------------------------------------------------------------------
# Strictly NO raw '&&' inside script
canvas_js_engine = '''
    // =========================================================================
    // SPECTRUM MONOPOLY: 2-D INFINITE BOX & 3-D ROTATING SPHERICAL CANVAS ENGINE
    // 12 INVISIBLE SPECTRUM LAYERS // 121-CELL HARMONIC MATRIX // MOTION TRAIL HUES
    // =========================================================================
    (function initMonoSpectrumCanvas() {
      var canvas = document.getElementById('mono-spectrum-canvas');
      if (!canvas) return;
      var ctx = canvas.getContext('2d');
      if (!ctx) return;

      // 12-Color Invisible Optical Spectrum Wavelengths & Colors
      // Green 532nm is exactly at index 5 (Stratum 06 - The Center of Balance)
      var spectrumLayers = [
        { name: 'Stratum 01 // Underpass', wl: '660nm', hex: '#ff1744', rgb: [255, 23, 68] },
        { name: 'Stratum 02 // Nomad Camp', wl: '630nm', hex: '#ff5722', rgb: [255, 87, 34] },
        { name: 'Stratum 03 // Public Tenement', wl: '600nm', hex: '#ff9100', rgb: [255, 145, 0] },
        { name: 'Stratum 04 // Suburb Zone', wl: '580nm', hex: '#ffc400', rgb: [255, 196, 0] },
        { name: 'Stratum 05 // Rural Homestead', wl: '560nm', hex: '#c6ff00', rgb: [198, 255, 0] },
        { name: 'Stratum 06 // GREEN COMMONS ★', wl: '532nm', hex: '#00ff66', rgb: [0, 255, 102] }, // CENTER
        { name: 'Stratum 07 // Master-Planned', wl: '515nm', hex: '#00e676', rgb: [0, 230, 118] },
        { name: 'Stratum 08 // Tech Incubator', wl: '495nm', hex: '#00e5ff', rgb: [0, 229, 255] },
        { name: 'Stratum 09 // Wall St Core', wl: '470nm', hex: '#2979ff', rgb: [41, 121, 255] },
        { name: 'Stratum 10 // Capitol Lobby', wl: '440nm', hex: '#651fff', rgb: [101, 31, 255] },
        { name: 'Stratum 11 // Offshore Shell', wl: '420nm', hex: '#d500f9', rgb: [213, 0, 249] },
        { name: 'Stratum 12 // Billionaire Bunker', wl: '410nm', hex: '#ff4081', rgb: [255, 64, 129] }
      ];

      // Generate 121-Cell Spherical Fibonacci Lattice Points
      var numPoints = 121;
      var spherePoints = [];
      var phi = Math.PI * (3 - Math.sqrt(5)); // Golden angle
      for (var i = 0; i < numPoints; i++) {
        var y = 1 - (i / (numPoints - 1)) * 2; // -1 (South) to +1 (North)
        var radius = Math.sqrt(Math.max(0, 1 - y * y));
        var theta = phi * i;
        var x = Math.cos(theta) * radius;
        var z = Math.sin(theta) * radius;
        // Map Y (-1 to +1) to 12 layers, so y=0 is layer 5 (532nm Green center)
        var layerIdx = Math.floor(((y + 1) / 2) * 11.99);
        spherePoints.push({
          x: x, y: y, z: z,
          layerIdx: layerIdx,
          trail: []
        });
      }

      // State
      var currentMode = '2d'; // '2d', '3d', or 'dual'
      var currentTool = 'brush'; // 'brush' or 'stamp'
      var selectedStamp = 'commons';
      var trailHueStrength = 0.8;
      var orbitSpeed = 0.008;
      var sphereRotation = 0;
      var isPointerDown = false;
      var userStrokes = []; // User-drawn shapes with motion trails
      var placedObjects = []; // User stamped real estate items

      // Player Token Tracker on the Visual Board
      var playerToken = {
        currentTile: 3,
        x: 250,
        y: 210,
        targetX: 250,
        targetY: 210,
        trail: []
      };

      // Handle Resize / Retina
      function resizeCanvas() {
        var rect = canvas.getBoundingClientRect();
        var dpr = window.devicePixelRatio || 1;
        canvas.width = Math.floor(rect.width * dpr);
        canvas.height = Math.floor(420 * dpr);
        ctx.scale(dpr, dpr);
      }
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);

      // Mode Buttons
      var btn2d = document.getElementById('btn-view-2d');
      var btn3d = document.getElementById('btn-view-3d');
      var btnDual = document.getElementById('btn-view-dual');

      function setActiveModeBtn(activeBtn) {
        var btns = [btn2d, btn3d, btnDual];
        for (var b = 0; b < btns.length; b++) {
          if (btns[b]) {
            btns[b].style.background = 'rgba(0,255,102,0.1)';
            btns[b].style.borderColor = 'rgba(0,255,102,0.3)';
          }
        }
        if (activeBtn) {
          activeBtn.style.background = 'rgba(0,255,102,0.3)';
          activeBtn.style.borderColor = '#00ff66';
        }
      }

      if (btn2d) {
        btn2d.addEventListener('click', function() {
          currentMode = '2d';
          setActiveModeBtn(btn2d);
        });
      }
      if (btn3d) {
        btn3d.addEventListener('click', function() {
          currentMode = '3d';
          setActiveModeBtn(btn3d);
        });
      }
      if (btnDual) {
        btnDual.addEventListener('click', function() {
          currentMode = 'dual';
          setActiveModeBtn(btnDual);
        });
      }

      // Tool Buttons
      var btnBrush = document.getElementById('btn-tool-brush');
      var btnStamp = document.getElementById('btn-tool-stamp');
      var selStamp = document.getElementById('select-stamp-type');

      if (btnBrush) {
        btnBrush.addEventListener('click', function() {
          currentTool = 'brush';
          btnBrush.style.background = 'rgba(0,255,102,0.25)';
          btnBrush.style.borderColor = '#00ff66';
          if (btnStamp) {
            btnStamp.style.background = 'rgba(0,229,255,0.1)';
            btnStamp.style.borderColor = 'rgba(0,229,255,0.3)';
          }
        });
      }
      if (btnStamp) {
        btnStamp.addEventListener('click', function() {
          currentTool = 'stamp';
          btnStamp.style.background = 'rgba(0,229,255,0.25)';
          btnStamp.style.borderColor = '#00e5ff';
          if (btnBrush) {
            btnBrush.style.background = 'rgba(0,255,102,0.1)';
            btnBrush.style.borderColor = 'rgba(0,255,102,0.3)';
          }
        });
      }
      if (selStamp) {
        selStamp.addEventListener('change', function() {
          selectedStamp = selStamp.value;
        });
      }

      // Sliders & Clear
      var sliderTrail = document.getElementById('slider-trail-hue');
      if (sliderTrail) {
        sliderTrail.addEventListener('input', function() {
          trailHueStrength = parseFloat(sliderTrail.value) / 10;
        });
      }

      var sliderOrbit = document.getElementById('slider-orbit-speed');
      if (sliderOrbit) {
        sliderOrbit.addEventListener('input', function() {
          orbitSpeed = (parseFloat(sliderOrbit.value) / 10) * 0.02;
        });
      }

      var btnClear = document.getElementById('btn-clear-canvas-trails');
      if (btnClear) {
        btnClear.addEventListener('click', function() {
          userStrokes = [];
          placedObjects = [];
          for (var p = 0; p < spherePoints.length; p++) {
            spherePoints[p].trail = [];
          }
          playerToken.trail = [];
        });
      }

      // Pointer Interactivity (Draw & Stamp)
      function getCanvasPos(evt) {
        var rect = canvas.getBoundingClientRect();
        return {
          x: evt.clientX - rect.left,
          y: evt.clientY - rect.top
        };
      }

      canvas.addEventListener('pointerdown', function(e) {
        isPointerDown = true;
        var pos = getCanvasPos(e);
        if (currentTool === 'stamp') {
          addPlacedObject(pos.x, pos.y, selectedStamp);
        } else {
          addUserStroke(pos.x, pos.y);
        }
      });

      canvas.addEventListener('pointermove', function(e) {
        var pos = getCanvasPos(e);
        updateTelemetry(pos.x, pos.y);
        if (isPointerDown) {
          if (currentTool === 'brush') {
            addUserStroke(pos.x, pos.y);
          }
        }
      });

      window.addEventListener('pointerup', function() {
        isPointerDown = false;
      });

      function updateTelemetry(x, y) {
        var w = canvas.getBoundingClientRect().width;
        var layerIdx = Math.floor((x / w) * 12);
        if (layerIdx < 0) layerIdx = 0;
        if (layerIdx > 11) layerIdx = 11;
        var layer = spectrumLayers[layerIdx];
        var hudEl = document.getElementById('mono-canvas-coords');
        if (hudEl) {
          hudEl.innerHTML = 'LAYER: <span style="color:' + layer.hex + '; font-weight:800;">' + layer.name + ' [' + layer.wl + ']</span> | SUB-MATRIX: <span style="color:#00e5ff;">121-CELL LATTICE</span>';
        }
      }

      function addUserStroke(x, y) {
        var w = canvas.getBoundingClientRect().width;
        var layerIdx = Math.floor((x / w) * 12);
        if (layerIdx < 0) layerIdx = 0;
        if (layerIdx > 11) layerIdx = 11;
        userStrokes.push({
          x: x,
          y: y,
          vx: (Math.random() - 0.5) * 1.5,
          vy: (Math.random() - 0.5) * 1.5,
          layerIdx: layerIdx,
          life: 1.0,
          decay: 0.006 + (1 - trailHueStrength) * 0.02
        });
        if (userStrokes.length > 250) {
          userStrokes.shift();
        }
      }

      function addPlacedObject(x, y, type) {
        var w = canvas.getBoundingClientRect().width;
        var layerIdx = Math.floor((x / w) * 12);
        if (layerIdx < 0) layerIdx = 0;
        if (layerIdx > 11) layerIdx = 11;
        var icon = '★';
        if (type === 'tent') icon = '⛺';
        if (type === 'homestead') icon = '🏡';
        if (type === 'commons') icon = '★';
        if (type === 'suburb') icon = '🏘️';
        if (type === 'tower') icon = '🏢';
        if (type === 'bunker') icon = '🛡️';

        placedObjects.push({
          x: x,
          y: y,
          type: type,
          icon: icon,
          layerIdx: layerIdx,
          pulse: 0
        });
      }

      // External Hook: When Monopoly Token Moves
      window.syncMonopolyTokenPosition = function(tileNum) {
        playerToken.currentTile = tileNum;
        var w = canvas.getBoundingClientRect().width;
        var h = 420;
        var layerWidth = w / 12;
        playerToken.targetX = (tileNum - 1 + 0.5) * layerWidth;
        playerToken.targetY = h * 0.5 + Math.sin(tileNum) * (h * 0.25);
      };

      // -----------------------------------------------------------------------
      // Main Animation Render Loop
      // -----------------------------------------------------------------------
      function renderLoop() {
        requestAnimationFrame(renderLoop);
        var w = canvas.getBoundingClientRect().width;
        var h = 420;

        // Clear canvas with trail fade
        ctx.fillStyle = 'rgba(2, 6, 11, ' + (0.15 + (1 - trailHueStrength) * 0.4) + ')';
        ctx.fillRect(0, 0, w, h);

        sphereRotation += orbitSpeed;

        if (currentMode === '2d') {
          render2DPlane(0, 0, w, h);
        } else if (currentMode === '3d') {
          render3DSphere(w * 0.5, h * 0.5, Math.min(w, h) * 0.42);
        } else if (currentMode === 'dual') {
          var halfW = w * 0.5;
          render2DPlane(0, 0, halfW, h);
          ctx.strokeStyle = 'rgba(0,255,102,0.3)';
          ctx.beginPath();
          ctx.moveTo(halfW, 0);
          ctx.lineTo(halfW, h);
          ctx.stroke();
          render3DSphere(halfW + halfW * 0.5, h * 0.5, Math.min(halfW, h) * 0.42);
        }

        // Draw Player Token & Trail across layers
        renderPlayerToken(w, h);
      }

      // -----------------------------------------------------------------------
      // Viewport A: 2-D Infinite Coordinate Plane & Invisible Spectrum Layers
      // -----------------------------------------------------------------------
      function render2DPlane(ox, oy, viewW, viewH) {
        var layerW = viewW / 12;

        // Draw 12 Invisible Spectrum Layer Columns (subtle glowing boundary grids)
        for (var c = 0; c < 12; c++) {
          var lx = ox + c * layerW;
          var lyr = spectrumLayers[c];

          // Stratum 06 (532nm Green Center) gets glowing harmonic indicator
          if (c === 5) {
            ctx.fillStyle = 'rgba(0, 255, 102, 0.04)';
            ctx.fillRect(lx, oy, layerW, viewH);
          }

          // Subtle layer grid boundary line
          ctx.strokeStyle = 'rgba(' + lyr.rgb[0] + ',' + lyr.rgb[1] + ',' + lyr.rgb[2] + ', 0.12)';
          ctx.lineWidth = (c === 5) ? 2 : 1;
          ctx.beginPath();
          ctx.moveTo(lx, oy);
          ctx.lineTo(lx, oy + viewH);
          ctx.stroke();

          // Subtle vertical label at bottom
          ctx.fillStyle = 'rgba(' + lyr.rgb[0] + ',' + lyr.rgb[1] + ',' + lyr.rgb[2] + ', 0.4)';
          ctx.font = '10px monospace';
          ctx.fillText(lyr.wl, lx + 4, oy + viewH - 12);
        }

        // Draw 121-Submatrix Grid Lines (11 horizontal divisions)
        var rowH = viewH / 11;
        for (var r = 1; r < 11; r++) {
          var ry = oy + r * rowH;
          ctx.strokeStyle = 'rgba(0, 229, 255, 0.05)';
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(ox, ry);
          ctx.lineTo(ox + viewW, ry);
          ctx.stroke();
        }

        // Render User Strokes & Chromatic Motion Trail Hues
        for (var s = userStrokes.length - 1; s >= 0; s--) {
          var strk = userStrokes[s];
          strk.x += strk.vx;
          strk.y += strk.vy;
          strk.life -= strk.decay;

          if (strk.life <= 0) {
            userStrokes.splice(s, 1);
            continue;
          }

          // Lookup underlying invisible layer color for current position!
          var colIdx = Math.floor((strk.x / viewW) * 12);
          if (colIdx < 0) colIdx = 0;
          if (colIdx > 11) colIdx = 11;
          var curLayer = spectrumLayers[colIdx];

          // Draw Illuminated Particle with Motion Trail Glow
          ctx.fillStyle = 'rgba(' + curLayer.rgb[0] + ',' + curLayer.rgb[1] + ',' + curLayer.rgb[2] + ',' + strk.life + ')';
          ctx.shadowColor = curLayer.hex;
          ctx.shadowBlur = 12 * trailHueStrength;
          ctx.beginPath();
          ctx.arc(strk.x, strk.y, 4 * strk.life + 1, 0, Math.PI * 2);
          ctx.fill();
          ctx.shadowBlur = 0;
        }

        // Render Placed Real Estate Assets
        for (var p = 0; p < placedObjects.length; p++) {
          var obj = placedObjects[p];
          if (obj.x >= ox) if (obj.x <= ox + viewW) {
            var oLayer = spectrumLayers[obj.layerIdx];
            obj.pulse += 0.04;
            var scale = 1 + Math.sin(obj.pulse) * 0.12;

            ctx.font = Math.floor(16 * scale) + 'px sans-serif';
            ctx.textAlign = 'center';
            ctx.shadowColor = oLayer.hex;
            ctx.shadowBlur = 14;
            ctx.fillStyle = oLayer.hex;
            ctx.fillText(obj.icon, obj.x, obj.y);
            ctx.shadowBlur = 0;

            // Small caption
            ctx.font = '9px monospace';
            ctx.fillStyle = 'rgba(255,255,255,0.7)';
            ctx.fillText(oLayer.wl, obj.x, obj.y + 14);
          }
        }
      }

      // -----------------------------------------------------------------------
      // Viewport B: 3-D Rotating Spherical Globe & 12 Orbital Layers
      // -----------------------------------------------------------------------
      function render3DSphere(cx, cy, r) {
        // Draw Outer Equatorial Ring
        ctx.strokeStyle = 'rgba(0, 255, 102, 0.2)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();

        // 12 Spherical Latitude Layer Slices (Green at Equator)
        for (var l = 0; l < 12; l++) {
          var lyr = spectrumLayers[l];
          var latY = (1 - (l / 11) * 2) * r; // From -r to +r
          var latRad = Math.sqrt(Math.max(0, r * r - latY * latY));

          // Draw Latitude Ring
          ctx.strokeStyle = (l === 5) ? 'rgba(0, 255, 102, 0.45)' : 'rgba(' + lyr.rgb[0] + ',' + lyr.rgb[1] + ',' + lyr.rgb[2] + ', 0.15)';
          ctx.lineWidth = (l === 5) ? 2 : 1;
          ctx.beginPath();
          ctx.ellipse(cx, cy + latY * 0.85, latRad, latRad * 0.32, 0, 0, Math.PI * 2);
          ctx.stroke();
        }

        // Draw 121-Point Rotating Fibonacci Spherical Lattice
        for (var p = 0; p < spherePoints.length; p++) {
          var pt = spherePoints[p];

          // 3D Rotation along Y-axis
          var cosRot = Math.cos(sphereRotation);
          var sinRot = Math.sin(sphereRotation);
          var rotX = pt.x * cosRot - pt.z * sinRot;
          var rotZ = pt.x * sinRot + pt.z * cosRot;
          var rotY = pt.y;

          // Depth sorting / Projection
          var fov = 2.5;
          var pZ = rotZ + fov;
          if (pZ > 0.1) {
            var screenX = cx + (rotX / pZ) * r * 1.8;
            var screenY = cy + (rotY / pZ) * r * 1.8;
            var lyr = spectrumLayers[pt.layerIdx];

            // Point alpha based on Z depth
            var alpha = (rotZ + 1) / 2; // 0 (back) to 1 (front)
            if (alpha > 0.15) {
              // Add to spherical trail
              pt.trail.push({ x: screenX, y: screenY, alpha: alpha });
              if (pt.trail.length > Math.floor(6 * trailHueStrength)) {
                pt.trail.shift();
              }

              // Draw Motion Trail Hue
              for (var t = 0; t < pt.trail.length; t++) {
                var tr = pt.trail[t];
                ctx.fillStyle = 'rgba(' + lyr.rgb[0] + ',' + lyr.rgb[1] + ',' + lyr.rgb[2] + ',' + (tr.alpha * 0.25) + ')';
                ctx.fillRect(tr.x - 1, tr.y - 1, 2, 2);
              }

              // Draw Lattice Node
              ctx.fillStyle = 'rgba(' + lyr.rgb[0] + ',' + lyr.rgb[1] + ',' + lyr.rgb[2] + ',' + alpha + ')';
              ctx.beginPath();
              ctx.arc(screenX, screenY, (pt.layerIdx === 5 ? 2.5 : 1.8) * alpha, 0, Math.PI * 2);
              ctx.fill();
            }
          }
        }

        // Center Green Meridian Pulse
        ctx.fillStyle = '#00ff66';
        ctx.font = '10px monospace';
        ctx.textAlign = 'center';
        ctx.fillText('EQUATOR // 532nm CENTER', cx, cy + 4);
      }

      // -----------------------------------------------------------------------
      // Player Token Render with Multi-Spectral Motion Trail Hue
      // -----------------------------------------------------------------------
      function renderPlayerToken(w, h) {
        // Smoothly interpolate token towards target
        playerToken.x += (playerToken.targetX - playerToken.x) * 0.1;
        playerToken.y += (playerToken.targetY - playerToken.y) * 0.1;

        // Current tile layer color
        var curTileIdx = playerToken.currentTile - 1;
        if (curTileIdx < 0) curTileIdx = 0;
        if (curTileIdx > 11) curTileIdx = 11;
        var lyr = spectrumLayers[curTileIdx];

        // Append to motion trail
        playerToken.trail.push({
          x: playerToken.x,
          y: playerToken.y,
          color: lyr.hex,
          rgb: lyr.rgb,
          alpha: 1.0
        });
        if (playerToken.trail.length > 20) {
          playerToken.trail.shift();
        }

        // Draw Motion Trail Hue
        for (var i = 0; i < playerToken.trail.length; i++) {
          var tr = playerToken.trail[i];
          tr.alpha -= 0.04;
          if (tr.alpha > 0) {
            ctx.fillStyle = 'rgba(' + tr.rgb[0] + ',' + tr.rgb[1] + ',' + tr.rgb[2] + ',' + tr.alpha * 0.4 + ')';
            ctx.beginPath();
            ctx.arc(tr.x, tr.y, 8 * (i / playerToken.trail.length), 0, Math.PI * 2);
            ctx.fill();
          }
        }

        // Draw Token Body (Glowing Avatar Icon)
        ctx.shadowColor = lyr.hex;
        ctx.shadowBlur = 18;
        ctx.fillStyle = lyr.hex;
        ctx.beginPath();
        ctx.arc(playerToken.x, playerToken.y, 9, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#050b14';
        ctx.beginPath();
        ctx.arc(playerToken.x, playerToken.y, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }

      // Start the Animation Engine
      renderLoop();

      // Hook dice roll buttons to update canvas token
      var rollBtn = document.getElementById('btn-mono-roll');
      if (rollBtn) {
        rollBtn.addEventListener('click', function() {
          // Allow existing click handler to update playerState.currentTile, then sync
          setTimeout(function() {
            var tileNum = 1;
            var tileDisplay = document.getElementById('mono-current-tile-name');
            if (tileDisplay) {
              var m = tileDisplay.innerText.match(/TILE\s*0?(\d+)/i);
              if (m) {
                tileNum = parseInt(m[1], 10);
              }
            }
            if (window.syncMonopolyTokenPosition) {
              window.syncMonopolyTokenPosition(tileNum);
            }
          }, 50);
        });
      }

      // Initial token sync
      window.syncMonopolyTokenPosition(3);
    })();
'''

# ---------------------------------------------------------------------------
# Perform the Injection into deploy/homepage.html
# ---------------------------------------------------------------------------
with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home_content = f.read()

# 1. Insert visual_stage_html right before the 12-tile board in Section 0x09.5
target_tile_marker = '<!-- Spectrum 12-Tile Interactive Board Grid -->'
if target_tile_marker in home_content:
    if 'mono-spectrum-stage-box' not in home_content:
        home_content = home_content.replace(
            target_tile_marker,
            visual_stage_html + '\n\n            ' + target_tile_marker,
            1
        )
        print("Injected 2D/3D Canvas Visual Stage into Section 0x09.5!")

# 2. Append canvas_js_engine to the existing Monopoly JavaScript engine
end_js_marker = '// END SPECTRUM MONOPOLY GAME ENGINE'
if end_js_marker in home_content:
    if 'initMonoSpectrumCanvas' not in home_content:
        home_content = home_content.replace(
            end_js_marker,
            canvas_js_engine + '\n    ' + end_js_marker,
            1
        )
        print("Injected 2D/3D Canvas JavaScript Engine into homepage.html!")

# Save homepage.html
with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home_content)

print("SUCCESS: Updated homepage.html with 2D/3D Spectrum Monopoly Canvas!")
