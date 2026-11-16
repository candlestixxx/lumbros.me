#!/usr/bin/env python3
"""
Adds the Interactive Ocular Alignment Game of Success to the Vision Calibration Deck:
1. Explains clearly how light and dark themes both operate within the invisible 12-color
   spectrum that everyone sees invisibly come to light.
2. Formulates Choice 01 (Luminance Polarity) and Choice 02 (Sight Prescription 20/200, 20/20, 20/10)
   as the foundational choices to control sight.
3. Adds the "INTERACTIVE GAME OF SUCCESS":
   - Real-time Ocular Alignment Target Reticle
   - Ocular Harmony Meter (0% to 100% Equilibrium)
   - Celebratory visual achievement flare when the user aligns their individual balance
   - In-game rewards linked directly to The New Monopoly and Shadertoy 3D Earth
4. 100% WordPress-safe (0 raw '&&' inside script tags)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

# ---------------------------------------------------------------------------
# 1. Update Choice 01 with the Enlightened Sovereign Control Manifesto
# ---------------------------------------------------------------------------
polarity_old_header = '<span class="mod-title">CHOICE 01 // SPECTRUM LUMINANCE POLARITY (CONTROL THE SIGHT)</span>'
polarity_new_header = '<span class="mod-title">CHOICE 01 // SPECTRUM LUMINANCE POLARITY: CONTROL LIGHT &amp; DARK</span>'

if polarity_old_header in home:
    home = home.replace(polarity_old_header, polarity_new_header, 1)

# Add educational directive callout inside Choice 01 if not present
educational_callout = '''          <!-- Sovereign Light & Dark Spectrum Guidance -->
          <div class="spectrum-enlightenment-banner" style="background: rgba(0,255,102,0.06); border: 1px dashed rgba(0,255,102,0.3); border-radius: 6px; padding: 10px 14px; margin-bottom: 12px; font-size: 0.75rem; color: #d1fae5; line-height: 1.5;">
            <strong style="color: #00ff66;">YOU CONTROL LIGHT &amp; DARK WITHIN THE SPECTRUM:</strong> Both Light and Dark modes operate inside the universal <strong>12-color optical spectrum</strong> that everyone perceives invisibly. While the spectrum operates silently behind all matter, toggling your luminance polarity brings those invisible wavelengths directly into the visible light of day — choosing between radiant neon lasers across an obsidian void, or pure jewel-tone frequencies over zero-glare optical alabaster.
          </div>
'''

if 'spectrum-enlightenment-banner' not in home:
    home = home.replace(
        '<div class="polarity-toggle-group">',
        educational_callout + '          <div class="polarity-toggle-group">',
        1
    )
    print("Injected educational Light/Dark Spectrum guidance banner into Choice 01!")

# ---------------------------------------------------------------------------
# 2. Update Choice 02 (Sight Prescription & Individual Balance)
# ---------------------------------------------------------------------------
acuity_old_header = '<span class="mod-title">CHOICE 02 // VISUAL ACUITY GAUGE &amp; SIGHT PRESCRIPTION FOCUS</span>'
acuity_new_header = '<span class="mod-title">CHOICE 02 // SIGHT PRESCRIPTION &amp; INDIVIDUAL BALANCE (20/200 • 20/20 • 20/10)</span>'

if acuity_old_header in home:
    home = home.replace(acuity_old_header, acuity_new_header, 1)

# ---------------------------------------------------------------------------
# 3. Add the Interactive Game of Success (Ocular Alignment Lock Component)
# ---------------------------------------------------------------------------
alignment_game_html = '''
        <!-- ===================================================================
             THE INTERACTIVE OCULAR ALIGNMENT GAME OF SUCCESS
             MATCH INDIVIDUAL BALANCE // HARMONIC LOCK // IN-GAME POWER-UP REWARD
             =================================================================== -->
        <div class="vision-module alignment-game-module" id="alignment-game-module" style="background: rgba(4,14,24,0.92); border: 1px solid rgba(0,229,255,0.4); border-radius: 6px; padding: 14px; box-shadow: 0 0 25px rgba(0,229,255,0.12);">
          <div class="module-header-game">
            <span class="mod-icon-laser">🎯</span>
            <span class="mod-title">STEP 03 // THE OCULAR HARMONIC ALIGNMENT GAME (TEST YOUR INDIVIDUAL BALANCE)</span>
            <span class="mod-arcade-tag" style="background:#00e5ff; color:#040a14; font-weight:900;">ACTIVE GAME</span>
          </div>

          <!-- Alignment Directive -->
          <div style="font-size: 0.76rem; color: #b8e2c8; line-height: 1.5; margin-bottom: 12px;">
            Adjust your prescription dial above. As you dial into your individual vision balance, your ocular frequency synchronizes with the <strong>532nm Green Equilibrium Center</strong>. Lock your sight into 100% balance to achieve instant ocular strain relief and unlock your in-game power-up!
          </div>

          <!-- Interactive Alignment Arena -->
          <div class="alignment-arena-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; align-items: center;">
            
            <!-- Target Reticle & Visual Lock Circle -->
            <div style="position: relative; height: 110px; background: #02060b; border: 1px solid rgba(0,255,102,0.3); border-radius: 6px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <!-- Concentric Radar Target Rings -->
              <div class="target-ring ring-3" style="position: absolute; width: 90px; height: 90px; border: 1px dashed rgba(0,255,102,0.25); border-radius: 50%;"></div>
              <div class="target-ring ring-2" style="position: absolute; width: 60px; height: 60px; border: 1px solid rgba(0,229,255,0.3); border-radius: 50%;"></div>
              <div class="target-ring ring-1" style="position: absolute; width: 30px; height: 30px; border: 1px solid #00ff66; border-radius: 50%;"></div>
              
              <!-- Crosshair Lines -->
              <div style="position: absolute; width: 100%; height: 1px; background: rgba(0,255,102,0.2);"></div>
              <div style="position: absolute; height: 100%; width: 1px; background: rgba(0,255,102,0.2);"></div>

              <!-- Live Ocular Alignment Pip -->
              <div id="ocular-target-pip" style="position: absolute; width: 16px; height: 16px; border-radius: 50%; background: #00ff66; box-shadow: 0 0 14px #00ff66; transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); display: flex; align-items: center; justify-content: center;">
                <span style="display: block; width: 4px; height: 4px; border-radius: 50%; background: #ffffff;"></span>
              </div>
            </div>

            <!-- Alignment Telemetry & Victory Status -->
            <div style="background: rgba(0,20,35,0.7); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 10px 14px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 0.7rem; color: #8ce4a7; font-weight: 700;">HARMONIC BALANCE METER:</span>
                <span id="alignment-score-badge" style="font-family: 'Share Tech Mono', monospace; font-size: 0.82rem; font-weight: 900; color: #00ff66;">100% [PERFECT LOCK]</span>
              </div>

              <!-- Meter Progress Bar -->
              <div style="height: 10px; background: rgba(0,0,0,0.6); border: 1px solid rgba(0,255,102,0.3); border-radius: 5px; overflow: hidden; margin-bottom: 8px;">
                <div id="alignment-progress-fill" style="height: 100%; width: 100%; background: linear-gradient(90deg, #ff9100 0%, #00e5ff 50%, #00ff66 100%); transition: width 0.2s ease;"></div>
              </div>

              <div id="alignment-victory-text" style="font-size: 0.74rem; color: #ffffff; line-height: 1.4; font-weight: 700;">
                ✨ SIGHT EQUILIBRIUM ACHIEVED // 532nm GREEN HARMONIC CENTER LOCKED
              </div>
            </div>

          </div>

          <!-- Unlocked Game Reward Banner -->
          <div id="alignment-reward-banner" style="margin-top: 12px; background: linear-gradient(135deg, rgba(0,255,102,0.12) 0%, rgba(0,229,255,0.08) 100%); border: 1px solid #00ff66; border-radius: 6px; padding: 10px 14px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div>
              <span style="background: #00ff66; color: #040a14; font-weight: 900; font-size: 0.65rem; padding: 2px 6px; border-radius: 3px; letter-spacing: 1px;">TROPHY UNLOCKED</span>
              <span style="color: #ffffff; font-weight: 800; font-size: 0.82rem; margin-left: 8px;">SPECTRUM VISION MASTER BADGE (+150 KARMA IN MONOPOLY)</span>
              <div style="font-size: 0.7rem; color: #a0f0c0; margin-top: 2px;">
                Your calibrated eyesight has eliminated ocular strain. Carry this balanced sight into the games below!
              </div>
            </div>
            <div>
              <a href="#spectrum-monopoly" class="cyber-btn sm" style="border-color: #00ff66; color: #00ff66; font-weight: 800; text-decoration: none; padding: 5px 12px;">
                <span>COMMENCE MONOPOLY WITH SIGHT BOOST</span> <span>↓</span>
              </a>
            </div>
          </div>

        </div>
'''

# Insert the alignment game module right before the compact archetype invite strip
if 'alignment-game-module' not in home:
    home = home.replace(
        '<!-- Compact Archetype Portal Strip -->',
        alignment_game_html + '\n\n        <!-- Compact Archetype Portal Strip -->',
        1
    )
    print("Injected Interactive Ocular Alignment Game module into homepage.html!")

# ---------------------------------------------------------------------------
# 4. Add JavaScript Logic to Power the Alignment Game of Success
# ---------------------------------------------------------------------------
alignment_game_js = '''
    // =========================================================================
    // INTERACTIVE OCULAR ALIGNMENT GAME OF SUCCESS JAVASCRIPT ENGINE
    // REAL-TIME RETICLE LOCK // 100% SIGHT HARMONY // IN-GAME TROPHY TRIGGER
    // =========================================================================
    (function initOcularAlignmentGame() {
      var targetPip = document.getElementById('ocular-target-pip');
      var scoreBadge = document.getElementById('alignment-score-badge');
      var progressFill = document.getElementById('alignment-progress-fill');
      var victoryText = document.getElementById('alignment-victory-text');
      var rewardBanner = document.getElementById('alignment-reward-banner');

      // Hook into gauge updates
      window.updateOcularAlignmentScore = function(gaugeVal) {
        // gaugeVal: 0 (20/200) to 100 (20/10), with 75 being 20/20 Plano Center
        // Any choice (20/200, 20/20, 20/10) is a valid calibrated prescription!
        // We calculate distance to nearest calibrated node: 0, 75, or 100
        var distTo200 = Math.abs(gaugeVal - 0);
        var distTo20 = Math.abs(gaugeVal - 75);
        var distTo10 = Math.abs(gaugeVal - 100);
        var minDist = Math.min(distTo200, distTo20, distTo10);

        // Alignment score from 70% to 100%
        var score = Math.max(70, Math.floor(100 - minDist * 1.2));
        if (minDist <= 3) score = 100;

        if (scoreBadge) {
          scoreBadge.textContent = score + '% ' + (score === 100 ? '[PERFECT HARMONIC LOCK]' : '[CALIBRATING]');
          scoreBadge.style.color = (score >= 95 ? '#00ff66' : (score >= 85 ? '#00e5ff' : '#ffaa00'));
        }

        if (progressFill) {
          progressFill.style.width = score + '%';
        }

        // Move target reticle pip smoothly towards center (0, 0)
        if (targetPip) {
          var offsetX = (minDist * 0.8) * (gaugeVal > 75 ? 1 : -1);
          var offsetY = (minDist * 0.4) * (gaugeVal % 2 === 0 ? 1 : -1);
          if (score === 100) {
            offsetX = 0;
            offsetY = 0;
            targetPip.style.boxShadow = '0 0 24px #00ff66, 0 0 35px #ffffff';
            targetPip.style.background = '#00ff66';
          } else {
            targetPip.style.boxShadow = '0 0 10px #00e5ff';
            targetPip.style.background = '#00e5ff';
          }
          targetPip.style.transform = 'translate(' + offsetX.toFixed(1) + 'px, ' + offsetY.toFixed(1) + 'px)';
        }

        // Victory text feedback
        if (victoryText) {
          if (score === 100) {
            victoryText.innerHTML = '✨ SIGHT EQUILIBRIUM ACHIEVED // 532nm GREEN HARMONIC CENTER LOCKED';
            victoryText.style.color = '#00ff66';
            if (rewardBanner) rewardBanner.style.opacity = '1';
          } else {
            victoryText.innerHTML = '◄ DIAL TO 20/200, 20/20 OR 20/10 TO ACHIEVE PERFECT OCULAR LOCK ►';
            victoryText.style.color = '#8ce4a7';
          }
        }
      };

      // Initial score calculation
      window.updateOcularAlignmentScore(75);

      // Hook preset buttons
      var presetBtns = document.querySelectorAll('.acuity-node-btn');
      for (var b = 0; b < presetBtns.length; b++) {
        presetBtns[b].addEventListener('click', function() {
          var gVal = parseInt(this.getAttribute('data-gauge') || '75', 10);
          setTimeout(function() {
            window.updateOcularAlignmentScore(gVal);
          }, 30);
        });
      }
    })();
'''

if 'initOcularAlignmentGame' not in home:
    script_end = '</script>'
    home = home.replace(script_end, alignment_game_js + '\n  ' + script_end, 1)
    print("Injected JavaScript for Ocular Alignment Game into homepage.html!")

# Save homepage.html
with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print("SUCCESS: Updated homepage.html with Interactive Ocular Alignment Game!")
