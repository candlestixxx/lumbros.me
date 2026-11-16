"""
Add Dual-Screen Digital Human Life Simulator, The Entire Soul Calculator,
and Bonus Shadertoy World-Shading & Dimensional Spectrum Enlightenment Studio
to Lumbros.me.

Strictly adhering to WordPress safety: ZERO raw '&&' inside script tags.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

print(f"Current homepage size: {len(home)} characters")

# Define HTML for Dual-Screen Life Simulator & Soul Calculator + Bonus Shadertoy Studio
DUAL_SCREEN_AND_SHADERTOY_HTML = '''
      <!-- =========================================================================
           PART 2: DUAL-SCREEN DIGITAL HUMAN LIFE SIMULATOR & THE ENTIRE SOUL CALCULATOR
           POWERED BY NEURAL AI CO-PILOT // FROM SINGLE WOMAN TO WORKING MOTHER, MARRIED & NETWORKS
           ========================================================================= -->
      <div class="soul-simulator-wrapper" id="soul-simulator-experience" style="margin-top: 40px; border-top: 2px solid rgba(0,255,102,0.3); padding-top: 30px;">
        
        <div style="text-align: center; margin-bottom: 25px;">
          <div style="display: inline-block; background: rgba(0,255,102,0.12); border: 1px solid #00ff66; padding: 4px 14px; border-radius: 4px; font-size: 0.75rem; font-weight: 800; color: #00ff66; letter-spacing: 2px; margin-bottom: 8px;">
            ⟬ DUAL-SCREEN INTERACTIVE SIMULATOR ⟭
          </div>
          <h3 style="color: #ffffff; font-size: 1.35rem; font-weight: 800; margin: 0 0 8px 0; letter-spacing: 1px;">
            DIGITAL HUMAN LIFE CHOICES &amp; THE ENTIRE SOUL CALCULATOR
          </h3>
          <p style="color: #8ce4a7; font-size: 0.8rem; max-width: 860px; margin: 0 auto; line-height: 1.5;">
            Step into the dual-screen cockpit. On <strong>Screen A</strong>, an animated digital human navigates real-world dilemmas across daily life (single woman career autonomy, working mother sacrifice, married partnership, and personal networks) guided by the best AI tool. On <strong>Screen B</strong>, <strong>The Entire Soul Calculator</strong> models your multivariate equilibrium across Mind, Body, Soul, and Life Capital anchored at the <strong>532nm Emerald Green Center</strong>.
          </p>
        </div>

        <!-- Dual-Screen Cockpit Grid -->
        <div class="dual-screen-cockpit-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(460px, 1fr)); gap: 24px; margin-bottom: 35px;">
          
          <!-- SCREEN A: DIGITAL HUMAN BIOMETRIC ANIMATION & DAILY LIFE CHOICES -->
          <div class="cockpit-screen screen-left" style="background: rgba(4,14,24,0.85); border: 1px solid rgba(0,255,102,0.35); border-radius: 8px; padding: 20px; box-shadow: 0 0 25px rgba(0,255,102,0.08); display: flex; flex-direction: column;">
            
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0,255,102,0.25); padding-bottom: 12px; margin-bottom: 15px;">
              <div>
                <span style="background: #00e5ff; color: #030a12; font-weight: 900; font-size: 0.7rem; padding: 2px 7px; border-radius: 3px;">SCREEN A</span>
                <span style="color: #ffffff; font-weight: 800; font-size: 0.95rem; margin-left: 8px; letter-spacing: 1px;">DIGITAL HUMAN LIFE SIMULATOR</span>
              </div>
              <div style="font-size: 0.7rem; color: #00ff66; font-family: 'Share Tech Mono', monospace;">
                AI CO-PILOT: <span style="color: #00e5ff; font-weight: 800;">ACTIVE</span>
              </div>
            </div>

            <!-- Persona Selector Tabs -->
            <div style="margin-bottom: 15px;">
              <div style="font-size: 0.72rem; color: #8ce4a7; margin-bottom: 6px; font-weight: 700; letter-spacing: 1px;">
                SELECT HUMAN ARCHETYPE &amp; LIFE PHASE:
              </div>
              <div class="persona-tab-group" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px;">
                <button type="button" class="persona-btn active" data-persona="single_woman" style="background: rgba(0,255,102,0.15); border: 1px solid #00ff66; color: #ffffff; padding: 7px 10px; font-size: 0.72rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  👩 SINGLE WOMAN // CAREER &amp; INDEPENDENCE
                </button>
                <button type="button" class="persona-btn" data-persona="working_mother" style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.3); color: #8ce4a7; padding: 7px 10px; font-size: 0.72rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  🤱 WORKING MOTHER // FAMILY PILLAR
                </button>
                <button type="button" class="persona-btn" data-persona="married" style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.3); color: #8ce4a7; padding: 7px 10px; font-size: 0.72rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  💍 MARRIED // JOINT PARTNERSHIP
                </button>
                <button type="button" class="persona-btn" data-persona="networks" style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.3); color: #8ce4a7; padding: 7px 10px; font-size: 0.72rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  🌐 SOCIAL NETWORKS &amp; CASUAL TIES
                </button>
              </div>
            </div>

            <!-- Digital Human Biometric Avatar Canvas Frame -->
            <div style="position: relative; width: 100%; height: 260px; background: #01060c; border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; overflow: hidden; margin-bottom: 16px;">
              <canvas id="digital-human-canvas" width="600" height="260" style="display: block; width: 100%; height: 100%;"></canvas>
              
              <!-- Floating Biometric Telemetry Overlay -->
              <div style="position: absolute; top: 10px; left: 12px; pointer-events: none; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; line-height: 1.4; color: #8ce4a7; background: rgba(2,8,16,0.8); padding: 5px 9px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.2);">
                <div>CHAKRA ANCHOR: <span style="color: #00ff66; font-weight: 800;">532nm HEART CENTER</span></div>
                <div>AURA COHERENCE: <span id="human-aura-status" style="color: #00e5ff;">94.8% [RESONANT]</span></div>
                <div>NERVOUS REGULATION: <span id="human-vagal-status" style="color: #00ff66;">PARASYMPATHETIC SYNC</span></div>
              </div>

              <div style="position: absolute; bottom: 8px; right: 12px; pointer-events: none; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: #ffaa00; background: rgba(2,8,16,0.8); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(255,170,0,0.2);">
                STRESS VECTORS: <span id="human-stress-val" style="color: #00ff66; font-weight: 800;">LOW (14%)</span>
              </div>
            </div>

            <!-- Interactive Daily Dilemma Card -->
            <div class="dilemma-card" style="background: rgba(10,24,38,0.7); border: 1px solid rgba(0,229,255,0.3); border-radius: 6px; padding: 14px; margin-bottom: 14px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span id="dilemma-category-badge" style="background: rgba(0,229,255,0.15); color: #00e5ff; font-size: 0.68rem; font-weight: 800; padding: 2px 7px; border-radius: 3px; letter-spacing: 1px;">
                  DILEMMA // CAREER VS FREEDOM
                </span>
                <span id="dilemma-cycle-badge" style="color: #8ce4a7; font-size: 0.68rem;">CYCLE: 01 / 04</span>
              </div>
              <h4 id="dilemma-title" style="color: #ffffff; font-size: 0.92rem; font-weight: 800; margin: 0 0 6px 0;">
                High-Stakes Promotion vs. Creative Sovereignty &amp; Dating
              </h4>
              <p id="dilemma-narrative" style="color: #b8e2c8; font-size: 0.78rem; line-height: 1.5; margin: 0 0 12px 0;">
                A tier-1 technology firm offers you an executive VP role with an +80% compensation bump. However, it requires 65-hour weeks and constant intercontinental travel, severely straining a budding romantic relationship, your weekly painting studio time, and proximity to aging parents.
              </p>

              <!-- Neural AI Co-Pilot Breakdown -->
              <div style="background: rgba(0,0,0,0.4); border-left: 3px solid #00ff66; padding: 8px 12px; border-radius: 0 4px 4px 0; margin-bottom: 12px;">
                <div style="color: #00ff66; font-size: 0.7rem; font-weight: 800; margin-bottom: 3px;">
                  🧠 THE BEST AI TOOL // NEURAL ORACLE ANALYSIS:
                </div>
                <div id="ai-oracle-advice" style="font-size: 0.72rem; color: #d0f8df; line-height: 1.4;">
                  "Immediate financial liquidity increases, but somatic nervous strain spikes by 68%. Relational intimacy and family proximity will decay without strict non-negotiable boundaries. Consider negotiating hybrid terms or launching sovereign advisory."
                </div>
              </div>

              <!-- Interactive Decision Buttons -->
              <div class="dilemma-choices-container" style="display: flex; flex-direction: column; gap: 8px;">
                <button type="button" class="dilemma-choice-btn choice-a" data-choice="a" style="background: rgba(0,255,102,0.12); border: 1px solid rgba(0,255,102,0.4); color: #ffffff; padding: 8px 12px; font-size: 0.75rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  <span style="color: #00ff66; font-weight: 900;">[CHOICE A]</span> <span id="choice-a-text">Negotiate Hybrid Advisory: Retain creative autonomy, protect family dinner &amp; budding intimacy. (+Soul, +Peace)</span>
                </button>
                <button type="button" class="dilemma-choice-btn choice-b" data-choice="b" style="background: rgba(255,170,0,0.1); border: 1px solid rgba(255,170,0,0.3); color: #ffffff; padding: 8px 12px; font-size: 0.75rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  <span style="color: #ffaa00; font-weight: 900;">[CHOICE B]</span> <span id="choice-b-text">Accept Full 65hr VP Role: Maximize immediate capital &amp; prestige, pause personal dating for 18mo. (+Cash, -Vitality)</span>
                </button>
                <button type="button" class="dilemma-choice-btn choice-c" data-choice="c" style="background: rgba(0,229,255,0.1); border: 1px solid rgba(0,229,255,0.3); color: #ffffff; padding: 8px 12px; font-size: 0.75rem; font-weight: 700; border-radius: 4px; cursor: pointer; text-align: left; transition: all 0.2s ease;">
                  <span style="color: #00e5ff; font-weight: 900;">[CHOICE C]</span> <span id="choice-c-text">Launch Independent Studio: Form cooperative network, invite close friends, accept lean year. (+Sovereignty)</span>
                </button>
              </div>
            </div>

            <!-- Choice Consequence Alert Stream -->
            <div id="choice-consequence-stream" style="font-family: 'Share Tech Mono', monospace; font-size: 0.7rem; color: #8ce4a7; background: rgba(0,0,0,0.35); padding: 6px 10px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.15);">
              ⟦ TRANSMISSION ⟧ Biometric avatar active. Awaiting your first daily life decision...
            </div>

          </div>


          <!-- SCREEN B: THE ENTIRE SOUL CALCULATOR -->
          <div class="cockpit-screen screen-right" style="background: rgba(4,14,24,0.85); border: 1px solid rgba(0,229,255,0.35); border-radius: 8px; padding: 20px; box-shadow: 0 0 25px rgba(0,229,255,0.08); display: flex; flex-direction: column;">
            
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0,229,255,0.25); padding-bottom: 12px; margin-bottom: 15px;">
              <div>
                <span style="background: #00ff66; color: #030a12; font-weight: 900; font-size: 0.7rem; padding: 2px 7px; border-radius: 3px;">SCREEN B</span>
                <span style="color: #ffffff; font-weight: 800; font-size: 0.95rem; margin-left: 8px; letter-spacing: 1px;">THE ENTIRE SOUL CALCULATOR</span>
              </div>
              <div style="font-size: 0.7rem; color: #00e5ff; font-family: 'Share Tech Mono', monospace;">
                FORMULA: <span style="color: #00ff66; font-weight: 800;">(M·B·S·C)¼ ⊙ 532nm</span>
              </div>
            </div>

            <!-- Master Resonance Holographic Gauge Card -->
            <div style="background: rgba(2,10,18,0.9); border: 1px solid rgba(0,255,102,0.3); border-radius: 6px; padding: 14px; margin-bottom: 16px; text-align: center; position: relative;">
              <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 15px;">
                
                <!-- Circular Radial Gauge Canvas -->
                <div style="position: relative; width: 140px; height: 140px;">
                  <canvas id="soul-gauge-canvas" width="280" height="280" style="width: 140px; height: 140px; display: block;"></canvas>
                  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center;">
                    <div id="master-soul-percent" style="font-size: 1.4rem; font-weight: 900; color: #00ff66; line-height: 1; font-family: 'Share Tech Mono', monospace;">88%</div>
                    <div style="font-size: 0.6rem; color: #8ce4a7; letter-spacing: 1px;">EQUILIBRIUM</div>
                  </div>
                </div>

                <!-- Master Metrics Summary -->
                <div style="text-align: left; max-width: 260px;">
                  <div style="font-size: 0.7rem; color: #8ce4a7; margin-bottom: 4px;">HARMONIC SPECTRUM STATUS:</div>
                  <div id="master-soul-status" style="color: #ffffff; font-weight: 800; font-size: 0.95rem; margin-bottom: 6px;">
                    532nm GREEN COMMONS COHERENCE
                  </div>
                  <div style="font-size: 0.72rem; color: #b8e2c8; line-height: 1.4; margin-bottom: 8px;">
                    Sight prescription &amp; polarity calibrated. Mind, body, and soul vectors synchronized with relational capital.
                  </div>
                  <div style="font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: #00e5ff;">
                    PRESCRIPTION FACTOR: <span id="soul-rx-factor" style="color: #00ff66;">20/20 [OPTIMAL]</span>
                  </div>
                </div>

              </div>
            </div>

            <!-- The 4 Fundamental Pillars Grid -->
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 16px;">
              
              <!-- PILLAR 1: MIND -->
              <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,229,255,0.25); border-radius: 6px; padding: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                  <span style="color: #00e5ff; font-weight: 800; font-size: 0.75rem;">1. MIND (Ψ_mind)</span>
                  <span id="val-pillar-mind" style="color: #ffffff; font-weight: 800; font-size: 0.78rem;">86%</span>
                </div>
                <div style="background: rgba(0,0,0,0.5); height: 6px; border-radius: 3px; overflow: hidden; margin-bottom: 6px;">
                  <div id="bar-pillar-mind" style="width: 86%; height: 100%; background: linear-gradient(90deg, #00e5ff, #00ff66); transition: width 0.4s ease;"></div>
                </div>
                <div style="font-size: 0.65rem; color: #8ce4a7; line-height: 1.3;">
                  Mental clarity: High &bull; Cognitive load: 24% &bull; Focus bandwidth: 4.2 GHz
                </div>
              </div>

              <!-- PILLAR 2: BODY -->
              <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                  <span style="color: #00ff66; font-weight: 800; font-size: 0.75rem;">2. BODY (Φ_body)</span>
                  <span id="val-pillar-body" style="color: #ffffff; font-weight: 800; font-size: 0.78rem;">82%</span>
                </div>
                <div style="background: rgba(0,0,0,0.5); height: 6px; border-radius: 3px; overflow: hidden; margin-bottom: 6px;">
                  <div id="bar-pillar-body" style="width: 82%; height: 100%; background: linear-gradient(90deg, #aeea00, #00ff66); transition: width 0.4s ease;"></div>
                </div>
                <div style="font-size: 0.65rem; color: #8ce4a7; line-height: 1.3;">
                  Circadian vitality: 82% &bull; Vagal tone: Calm &bull; Sleep recovery: 7.8 hrs
                </div>
              </div>

              <!-- PILLAR 3: SOUL -->
              <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(213,0,249,0.25); border-radius: 6px; padding: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                  <span style="color: #d500f9; font-weight: 800; font-size: 0.75rem;">3. SOUL (Ω_soul)</span>
                  <span id="val-pillar-soul" style="color: #ffffff; font-weight: 800; font-size: 0.78rem;">94%</span>
                </div>
                <div style="background: rgba(0,0,0,0.5); height: 6px; border-radius: 3px; overflow: hidden; margin-bottom: 6px;">
                  <div id="bar-pillar-soul" style="width: 94%; height: 100%; background: linear-gradient(90deg, #d500f9, #00ff66); transition: width 0.4s ease;"></div>
                </div>
                <div style="font-size: 0.65rem; color: #8ce4a7; line-height: 1.3;">
                  532nm center lock: 99% &bull; Spiritual peace: High &bull; Unconditional love: Active
                </div>
              </div>

              <!-- PILLAR 4: LIFE CAPITAL -->
              <div style="background: rgba(5,15,25,0.7); border: 1px solid rgba(255,170,0,0.25); border-radius: 6px; padding: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                  <span style="color: #ffaa00; font-weight: 800; font-size: 0.75rem;">4. LIFE CAPITAL (Γ_cap)</span>
                  <span id="val-pillar-capital" style="color: #ffffff; font-weight: 800; font-size: 0.78rem;">89%</span>
                </div>
                <div style="background: rgba(0,0,0,0.5); height: 6px; border-radius: 3px; overflow: hidden; margin-bottom: 6px;">
                  <div id="bar-pillar-capital" style="width: 89%; height: 100%; background: linear-gradient(90deg, #ffaa00, #00ff66); transition: width 0.4s ease;"></div>
                </div>
                <div style="font-size: 0.65rem; color: #8ce4a7; line-height: 1.3;">
                  Family/partner trust: 92% &bull; Lifelong friends: 86% &bull; Time freedom: 88%
                </div>
              </div>

            </div>

            <!-- Fine-Tuning Calibration Sliders -->
            <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(0,255,102,0.15); border-radius: 6px; padding: 12px; margin-bottom: 14px;">
              <div style="font-size: 0.72rem; color: #8ce4a7; font-weight: 700; margin-bottom: 8px;">
                SOUL VARIABLE FINE-TUNING &amp; REAL-TIME EXPERIMENTATION:
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 8px;">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 2px;">
                    <span>COGNITIVE FOCUS:</span>
                    <span id="slider-focus-val" style="color: #00e5ff;">85%</span>
                  </div>
                  <input type="range" id="slider-focus" min="10" max="100" value="85" style="width: 100%; accent-color: #00e5ff; cursor: pointer;">
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 2px;">
                    <span>RELATIONAL TRUST:</span>
                    <span id="slider-trust-val" style="color: #ffaa00;">90%</span>
                  </div>
                  <input type="range" id="slider-trust" min="10" max="100" value="90" style="width: 100%; accent-color: #ffaa00; cursor: pointer;">
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 2px;">
                    <span>532nm GREEN LOCK:</span>
                    <span id="slider-green-val" style="color: #00ff66;">98%</span>
                  </div>
                  <input type="range" id="slider-green" min="10" max="100" value="98" style="width: 100%; accent-color: #00ff66; cursor: pointer;">
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 2px;">
                    <span>TIME SOVEREIGNTY:</span>
                    <span id="slider-time-val" style="color: #d500f9;">84%</span>
                  </div>
                  <input type="range" id="slider-time" min="10" max="100" value="84" style="width: 100%; accent-color: #d500f9; cursor: pointer;">
                </div>
              </div>
            </div>

            <!-- Soul Prescription Action Rail -->
            <div style="display: flex; gap: 8px; margin-top: auto;">
              <button type="button" id="btn-recalibrate-soul" style="flex: 1; background: #00ff66; color: #02070f; border: none; font-size: 0.75rem; font-weight: 800; padding: 8px 12px; border-radius: 4px; cursor: pointer; box-shadow: 0 0 10px rgba(0,255,102,0.3); transition: all 0.2s ease;">
                ⚡ RECALIBRATE TO 532nm EQUILIBRIUM
              </button>
              <button type="button" id="btn-reset-soul" style="background: rgba(255,255,255,0.08); color: #8ce4a7; border: 1px solid rgba(255,255,255,0.2); font-size: 0.75rem; font-weight: 700; padding: 8px 12px; border-radius: 4px; cursor: pointer;">
                ↺ RESET
              </button>
            </div>

          </div>

        </div>

      </div>


      <!-- =========================================================================
           PART 3: BONUS SHADERTOY WORLD-SHADING & ENLIGHTENMENT SANDBOX
           HOMAGE TO BEAUTYPI (IÑIGO QUÍLEZ & POL JEREMIAS) // ARCHITECTED BY LUM
           PROCEDURAL 3D/4D WORLD MODELING ACROSS THE 12-COLOR INVISIBLE SPECTRUM & EULER WAVES
           ========================================================================= -->
      <div class="shadertoy-bonus-sandbox-wrapper" id="shadertoy-bonus-studio" style="margin-top: 30px; border-top: 2px solid rgba(0,229,255,0.3); padding-top: 30px;">
        
        <div style="text-align: center; margin-bottom: 20px;">
          <div style="display: inline-block; background: rgba(0,229,255,0.12); border: 1px solid #00e5ff; padding: 4px 14px; border-radius: 4px; font-size: 0.75rem; font-weight: 800; color: #00e5ff; letter-spacing: 2px; margin-bottom: 8px;">
            ⟬ BONUS CREATIVE STUDIO // SHADERTOY WORLD MODELER ⟭
          </div>
          <h3 style="color: #ffffff; font-size: 1.35rem; font-weight: 800; margin: 0 0 8px 0; letter-spacing: 1px;">
            PROCEDURAL WORLD-SHADING &amp; DIMENSIONAL ENLIGHTENMENT
          </h3>
          <p style="color: #8ce4a7; font-size: 0.8rem; max-width: 880px; margin: 0 auto; line-height: 1.5;">
            Shade and sculpt the world through procedural mathematics. Modulate <strong>Euler standing waves (e^{i&theta;} = cos&theta; + i sin&theta;)</strong>, project <strong>4D hyper-torus dimensional warps</strong> into 3D, and illuminate planetary matter across any of the <strong>12 invisible optical spectrum layers</strong> anchored at <strong>532nm Emerald Green</strong>.
          </p>
        </div>

        <!-- Homage & Science Banner -->
        <div style="background: rgba(5,15,28,0.7); border: 1px solid rgba(0,255,102,0.25); border-radius: 6px; padding: 12px 16px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
          <div style="font-size: 0.74rem; color: #b8e2c8; line-height: 1.4;">
            <strong style="color: #00ff66;">CONCEIVED &amp; ARCHITECTED BY LUM (LUMBROS KOURLOS)</strong> &bull; Deep artistic homage to <strong>I&ntilde;igo Qu&iacute;lez</strong> &amp; <strong>Pol Jeremias</strong> (founders of Beautypi &amp; Shadertoy) for pioneering real-time procedural raymarching and world modeling.
          </div>
          <div style="font-family: 'Share Tech Mono', monospace; font-size: 0.7rem; color: #00e5ff;">
            MATHEMATICS: <span style="color: #00ff66;">e^{i&pi;} + 1 = 0 &bull; &lambda;_0 = 532nm</span>
          </div>
        </div>

        <!-- Shading Modeling Studio Console -->
        <div style="background: #02070f; border: 1px solid rgba(0,229,255,0.35); border-radius: 8px; overflow: hidden; box-shadow: 0 0 30px rgba(0,229,255,0.08); margin-bottom: 20px;">
          
          <!-- Top Studio Toolbar -->
          <div style="background: rgba(8,20,34,0.9); border-bottom: 1px solid rgba(0,229,255,0.25); padding: 10px 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="background: #00e5ff; color: #000; font-weight: 900; font-size: 0.7rem; padding: 2px 7px; border-radius: 3px;">GLSL ENGINE</span>
              <span style="color: #ffffff; font-weight: 700; font-size: 0.85rem;">WORLD-SHADING VIEWPORT</span>
            </div>
            
            <!-- Dimensional Mode Selector -->
            <div class="shader-mode-tabs" style="display: flex; gap: 6px; flex-wrap: wrap;">
              <button type="button" class="shader-dim-btn active" data-mode="sphere_3d" style="background: #00ff66; color: #030912; border: none; font-size: 0.7rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                🌍 3D SPHERE EARTH
              </button>
              <button type="button" class="shader-dim-btn" data-mode="euler_waves" style="background: rgba(0,229,255,0.15); color: #00e5ff; border: 1px solid rgba(0,229,255,0.4); font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                🌊 EULER STANDING WAVE
              </button>
              <button type="button" class="shader-dim-btn" data-mode="hyper_warp" style="background: rgba(0,229,255,0.15); color: #00e5ff; border: 1px solid rgba(0,229,255,0.4); font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                🌀 4D HYPER-WARP
              </button>
              <button type="button" class="shader-dim-btn" data-mode="voronoi_net" style="background: rgba(0,229,255,0.15); color: #00e5ff; border: 1px solid rgba(0,229,255,0.4); font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; cursor: pointer;">
                🕸️ CONSCIOUSNESS MESH
              </button>
            </div>
          </div>

          <!-- 12-Color Spectral Shading Swatches Selector Bar -->
          <div style="background: rgba(4,12,20,0.95); border-bottom: 1px solid rgba(0,255,102,0.2); padding: 8px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; font-size: 0.7rem;">
              <span style="color: #8ce4a7; font-weight: 700;">SHADE PLANET IN SPECTRUM WAVELENGTH:</span>
              <span id="active-shader-wl-display" style="color: #00ff66; font-family: 'Share Tech Mono', monospace; font-weight: 800;">
                ACTIVE: 532nm EMERALD GREEN (CENTER OF EQUILIBRIUM)
              </span>
            </div>
            
            <div class="shader-spectral-swatches" style="display: grid; grid-template-columns: repeat(14, 1fr); gap: 4px;">
              <button type="button" class="shader-swatch-btn" data-wl="660" data-color="#ff1744" title="660nm Crimson Underpass" style="background: #ff1744; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="630" data-color="#ff5722" title="630nm Coral Pulse" style="background: #ff5722; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="600" data-color="#ff9100" title="600nm Amber Tenement" style="background: #ff9100; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="580" data-color="#ffc400" title="580nm Gold Suburb" style="background: #ffc400; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="560" data-color="#c6ff00" title="560nm Lime Soil" style="background: #c6ff00; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn active" data-wl="532" data-color="#00ff66" title="532nm Green Commons (Center)" style="background: #00ff66; height: 26px; border: 2px solid #ffffff; box-shadow: 0 0 8px #00ff66; border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="515" data-color="#00e676" title="515nm Mint Master-Plan" style="background: #00e676; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="495" data-color="#00e5ff" title="495nm Cyan Tech Incubator" style="background: #00e5ff; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="470" data-color="#2979ff" title="470nm Cobalt Wall St" style="background: #2979ff; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="440" data-color="#651fff" title="440nm Indigo Capitol" style="background: #651fff; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="420" data-color="#d500f9" title="420nm Violet Offshore" style="background: #d500f9; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="410" data-color="#ff4081" title="410nm Magenta Bunker" style="background: #ff4081; height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="rainbow" data-color="rainbow" title="Full 12-Color Dispersion" style="background: linear-gradient(90deg, #ff1744, #ffaa00, #00ff66, #00e5ff, #d500f9); height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
              <button type="button" class="shader-swatch-btn" data-wl="monochrome" data-color="#ffffff" title="Polarity White/Dark Light" style="background: linear-gradient(90deg, #050a10, #ffffff); height: 26px; border: 1px solid rgba(255,255,255,0.3); border-radius: 3px; cursor: pointer;"></button>
            </div>
          </div>

          <!-- Interactive WebGL / Procedural Viewport Canvas -->
          <div style="position: relative; width: 100%; height: 380px; background: #010408; overflow: hidden;">
            <canvas id="shadertoy-world-canvas" width="1000" height="380" style="display: block; width: 100%; height: 100%; cursor: grab;"></canvas>
            
            <!-- Real-Time Shader Telemetry HUD -->
            <div style="position: absolute; top: 12px; left: 16px; pointer-events: none; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; line-height: 1.4; color: #8ce4a7; background: rgba(3,10,18,0.85); padding: 6px 12px; border-radius: 4px; border: 1px solid rgba(0,255,102,0.25);">
              <div>RAYMARCHER: <span style="color: #00ff66; font-weight: 800;">ACTIVE (GLSL FRAG)</span></div>
              <div>EULER PHASE: <span id="telemetry-euler-phase" style="color: #00e5ff;">&theta; = 1.414 rad</span></div>
              <div>DIMENSION: <span id="telemetry-dim-factor" style="color: #d500f9;">3.40D HYPER-SURFACE</span></div>
              <div>PHOTOTHERAPY: <span id="telemetry-phototherapy-state" style="color: #00ff66;">532nm LOCK [ACTIVE]</span></div>
            </div>

            <!-- Drag Prompt Overlay -->
            <div style="position: absolute; bottom: 10px; right: 16px; pointer-events: none; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: #00e5ff; background: rgba(3,10,18,0.85); padding: 4px 10px; border-radius: 4px; border: 1px solid rgba(0,229,255,0.25);">
              <span>🖱️ DRAG TO ROTATE WORLD // SCROLL TO WARP</span>
            </div>
          </div>

          <!-- Mathematical Controls Panel -->
          <div style="background: rgba(6,16,28,0.95); border-top: 1px solid rgba(0,229,255,0.25); padding: 14px 16px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 12px;">
              
              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 3px;">
                  <span>EULER PHASE SHIFT (&theta;):</span>
                  <span id="slider-shader-euler-val" style="color: #00e5ff;">&pi; / 2</span>
                </div>
                <input type="range" id="slider-shader-euler" min="0" max="628" value="157" style="width: 100%; accent-color: #00e5ff; cursor: pointer;">
              </div>

              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 3px;">
                  <span>DIMENSIONAL WARP FACTOR (D):</span>
                  <span id="slider-shader-warp-val" style="color: #d500f9;">3.20D</span>
                </div>
                <input type="range" id="slider-shader-warp" min="30" max="45" value="32" style="width: 100%; accent-color: #d500f9; cursor: pointer;">
              </div>

              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 3px;">
                  <span>HARMONIC WAVE FREQUENCY (&omega;):</span>
                  <span id="slider-shader-freq-val" style="color: #00ff66;">8.0 Hz</span>
                </div>
                <input type="range" id="slider-shader-freq" min="1" max="24" value="8" style="width: 100%; accent-color: #00ff66; cursor: pointer;">
              </div>

              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: #b8e2c8; margin-bottom: 3px;">
                  <span>ROTATION &amp; ORBIT VELOCITY:</span>
                  <span id="slider-shader-rot-val" style="color: #ffaa00;">1.2x</span>
                </div>
                <input type="range" id="slider-shader-rot" min="0" max="30" value="12" style="width: 100%; accent-color: #ffaa00; cursor: pointer;">
              </div>

            </div>

            <!-- Preset Action Pills -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
              <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                <span style="font-size: 0.7rem; color: #8ce4a7; line-height: 26px; font-weight: 700;">PRESETS:</span>
                <button type="button" class="shader-preset-btn" data-preset="emerald_earth" style="background: rgba(0,255,102,0.15); border: 1px solid #00ff66; color: #00ff66; font-size: 0.68rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; cursor: pointer;">
                  532nm Emerald Earth
                </button>
                <button type="button" class="shader-preset-btn" data-preset="euler_quantum" style="background: rgba(0,229,255,0.15); border: 1px solid #00e5ff; color: #00e5ff; font-size: 0.68rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; cursor: pointer;">
                  Euler Quantum Sphere
                </button>
                <button type="button" class="shader-preset-btn" data-preset="hyper_klein" style="background: rgba(213,0,249,0.15); border: 1px solid #d500f9; color: #d500f9; font-size: 0.68rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; cursor: pointer;">
                  4D Klein Dimensional Fold
                </button>
                <button type="button" class="shader-preset-btn" data-preset="rainbow_prism" style="background: rgba(255,170,0,0.15); border: 1px solid #ffaa00; color: #ffaa00; font-size: 0.68rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; cursor: pointer;">
                  12-Color Prism Radiance
                </button>
              </div>

              <div>
                <button type="button" id="btn-toggle-shader-code" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.25); color: #ffffff; font-size: 0.7rem; font-weight: 700; padding: 5px 10px; border-radius: 4px; cursor: pointer;">
                  &lt;/&gt; VIEW GLSL MATHEMATICAL SOURCE
                </button>
              </div>
            </div>

            <!-- Collapsible GLSL Source Drawer -->
            <div id="shader-code-drawer" style="display: none; margin-top: 12px; background: #010408; border: 1px solid rgba(0,255,102,0.2); border-radius: 4px; padding: 12px; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: #8ce4a7; line-height: 1.5; overflow-x: auto; max-height: 220px;">
              <pre style="margin: 0;"><code>// LUM (LUMBROS KOURLOS) // PROCEDURAL WORLD-SHADING GLSL KERNEL
// HOMAGE TO BEAUTYPI (IÑIGO QUÍLEZ &amp; POL JEREMIAS)
// EULER STANDING WAVE: e^{i*theta} = cos(theta) + i*sin(theta)

uniform float u_time;
uniform vec2 u_resolution;
uniform float u_wavelength;       // 12-Color Invisible Spectrum (532nm Center)
uniform float u_euler_phase;      // Standing wave phase
uniform float u_dimension_warp;   // 3.0D to 4.5D hyperspace projection
uniform float u_wave_freq;        // Harmonic frequency

vec3 spectralRadiance(float lambda) {
    // 532nm Emerald Green Equilibrium Function
    float x = clamp((lambda - 400.0) / 300.0, 0.0, 1.0);
    return 0.5 + 0.5 * cos(6.28318 * (x * vec3(1.0, 0.8, 0.5) + vec3(0.0, 0.33, 0.67)));
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord - 0.5 * u_resolution.xy) / u_resolution.y;
    vec3 col = vec3(0.02, 0.04, 0.08); // Deep Void Space
    
    // Euler standing wave perturbation
    float r = length(uv);
    float wave = sin(u_euler_phase + r * u_wave_freq) * cos(atan(uv.y, uv.x) * 3.0);
    
    // 4D Dimensional Warp projection
    float warp = pow(r, u_dimension_warp - 2.0);
    
    // Raymarched Sphere Surface with Phototherapy Glow
    if (r &lt; 0.7 + 0.08 * wave) {
        vec3 N = vec3(uv / 0.7, sqrt(max(0.0, 1.0 - dot(uv/0.7, uv/0.7))));
        float diff = max(0.0, dot(N, normalize(vec3(1.0, 1.0, 1.0))));
        vec3 specColor = spectralRadiance(u_wavelength);
        col = mix(specColor * 0.3, specColor * 1.2, diff + 0.3 * wave);
        col += pow(max(0.0, dot(reflect(-normalize(vec3(1.0,1.0,1.0)), N), vec3(0,0,1))), 16.0) * specColor;
    }
    
    fragColor = vec4(col, 1.0);
}</code></pre>
            </div>

          </div>

        </div>

      </div>
'''

# Check if already present
if 'id="soul-simulator-experience"' in home:
    print("WARNING: soul-simulator-experience already found in homepage.html! Skipping duplicate insertion.")
else:
    # Target location: right before `<!-- Footer Note -->\n      <div class="tribute-footer-signature">` in section spectrum-monopoly
    pattern = r'(\s*<!-- Footer Note -->\s*<div class="tribute-footer-signature">\s*<span>⟦ LUMBROS\.ME // THE NEW MONOPOLY)'
    match = re.search(pattern, home)
    if not match:
        # Fallback to before </section> of spectrum-monopoly
        pattern = r'(</section>\s*<!-- =+\s*END SECTION: SPECTRUM MONOPOLY)'
        match = re.search(pattern, home)
        if match:
            print("Found fallback injection point before </section> of spectrum-monopoly.")
            home = home[:match.start()] + DUAL_SCREEN_AND_SHADERTOY_HTML + '\n\n' + home[match.start():]
        else:
            print("ERROR: Could not find insertion point for spectrum monopoly HTML!")
            exit(1)
    else:
        print("Found primary injection point before monopoly footer note.")
        home = home[:match.start()] + DUAL_SCREEN_AND_SHADERTOY_HTML + '\n\n' + home[match.start():]

print(f"HTML injected. New size: {len(home)}")

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print("Saved homepage.html with HTML structure.")
