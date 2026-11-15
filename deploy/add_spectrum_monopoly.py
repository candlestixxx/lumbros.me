#!/usr/bin/env python3
"""
Adds Section 0x09.5 & Standalone Page: SPECTRUM MONOPOLY — THE REAL-WORLD FINANCIAL SIMULATOR
Designed & Developed by Lum (Lumbros Kourlos)
Homage to Inigo Quilez & Pol Jeremias (Beautypi)

Simulates the real global, international, national, and local financial system:
- 12 Spectrum Economic Strata: From homeless to rural homesteads, suburbs, urban high-rises, and billionaire bunkers
- Environment, Human Flourishing, and Natural Resources planetary survival gauges
- Vicarious Character Creator: 0 wealth, working class, adoption, race, demographics, public vs private schools (1-12th)
- Modern AI Subscription choices: Free vs $20/mo Pro vs $200/mo Autonomous Agent Swarms
- Moral Spectrum: Honorable business integrity vs Shadow clear-net money laundering, shell companies & predatory speculation
- The Path of Restitution: Rebuilding life and community back to the 532nm Green Center of balance
"""

import os
import re

BASE_DIR = os.path.dirname(__file__)
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')
MONOPOLY_PATH = os.path.join(BASE_DIR, 'monopoly.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home_content = f.read()

# 1. Clean existing Monopoly Section if present
print("Preparing to add Spectrum Monopoly Game...")
home_content = re.sub(r'<!-- ===+\s*SECTION: SPECTRUM MONOPOLY[\s\S]*?<!-- ===+\s*END SECTION: SPECTRUM MONOPOLY -->', '', home_content)
home_content = re.sub(r'/\* ===+\s*SPECTRUM MONOPOLY STYLES[\s\S]*?/\* ===+\s*END SPECTRUM MONOPOLY STYLES \*/', '', home_content)
home_content = re.sub(r'// ===+\s*SPECTRUM MONOPOLY GAME ENGINE[\s\S]*?// ===+\s*END SPECTRUM MONOPOLY GAME ENGINE', '', home_content)

# 2. Build Spectrum Monopoly HTML Section Markup
monopoly_section_html = '''  <!-- =========================================================================
       SECTION: SPECTRUM MONOPOLY — THE REAL-WORLD FINANCIAL & PLANETARY LIFE SIMULATOR
       DEVELOPED BY LUM (LUMBROS KOURLOS) // MACRO-GLOBAL TO LOCAL ECONOMIC ENGINE
       ========================================================================= -->
  <section id="spectrum-monopoly" class="terminal-section monopoly-section spectrum-layer" data-layer-seq="9.5">
    <div class="layer-spectrum-matrix" aria-hidden="true">
      <svg class="matrix-svg" viewBox="0 0 1200 360" preserveAspectRatio="none">
        <rect x="100" y="40" width="1000" height="280" fill="none" stroke="#00ff66" stroke-width="1.5" stroke-dasharray="10 6" class="geo-archetype"></rect>
        <line x1="100" y1="180" x2="1100" y2="180" stroke="#00e5ff" stroke-width="1" class="geo-line"></line>
        <circle cx="600" cy="180" r="85" fill="none" stroke="#00ff66" stroke-width="2" class="geo-ring"></circle>
        <circle cx="600" cy="180" r="45" fill="none" stroke="#ffaa00" stroke-width="1.5" class="geo-ring"></circle>
        <circle cx="600" cy="180" r="6" fill="#00ff66" class="geo-node"></circle>
      </svg>
      <div class="matrix-grid-pattern"></div>
    </div>

    <!-- Section Badge -->
    <div class="section-badge">
      <span>[ SECTION 0x09.5 ]</span> // SPECTRUM MONOPOLY: REAL-WORLD CAPITAL &amp; PLANETARY SURVIVAL SIMULATOR
    </div>

    <!-- Section Headline -->
    <h2 class="section-title unicode-headline">
      ⟬ 𝐓𝐇𝐄 𝐍𝐄𝐖 𝐌𝐎𝐍𝐎𝐏𝐎𝐋𝐘 : 𝐆𝐋𝐎𝐁𝐀𝐋 𝐂𝐀𝐏𝐈𝐓𝐀𝐋, 𝐋𝐈𝐅𝐄 𝐂𝐇𝐎𝐈𝐂𝐄𝐒 &amp; 𝐓𝐇𝐄 𝐏𝐋𝐀𝐍𝐄𝐓𝐀𝐑𝐘 𝐁𝐀𝐋𝐀𝐍𝐂𝐄 ⟭
    </h2>

    <div class="monopoly-frame">
      <div class="twin-vertical-scanline-rail-left" aria-hidden="true"></div>
      <div class="twin-vertical-scanline-rail-right" aria-hidden="true"></div>

      <!-- Header Manifesto -->
      <div class="monopoly-header-bar">
        <div class="monopoly-brand">
          <span class="monopoly-logo-chip">MONOPOLY v2.0</span>
          <span class="monopoly-brand-sub">DESIGNED &amp; DEVELOPED BY LUM // 12-SPECTRUM FINANCIAL SIMULATOR</span>
        </div>
        <div class="monopoly-tag-group">
          <span class="mono-tag">GLOBAL • NATIONAL • LOCAL</span>
          <span class="mono-tag highlight">BALANCE POINT: 532nm GREEN COMMONS</span>
        </div>
      </div>

      <!-- Philosophical Mission -->
      <div class="monopoly-intro-card">
        <p class="monopoly-intro-text">
          Traditional Monopoly was built on a single predatory flaw: one player hoards all wealth while everyone else goes bankrupt.
          In the <strong>Real-World Spectrum Monopoly</strong>, humanity, natural resources, and the environment are inextricably bound.
          Whether you start unhoused on the streets, blue-collar working class, adopted, or in a billionaire luxury bunker—your choices compound through 
          <strong>education (Public vs Private K-12)</strong>, <strong>modern AI subscriptions (Free vs $20/mo vs $200/mo Agent Swarms)</strong>, and 
          <strong>moral cross-roads (Honorable Business vs Clear-Net Laundering &amp; Speculation)</strong>.
          If the Environment or Community Flourishing collapses to zero, even the bunker fails. True victory is achieving <strong>Systemic Equilibrium at the 532nm Green Center</strong>.
        </p>
      </div>

      <!-- Planetary Survival Tripartite Gauges -->
      <div class="planetary-gauges-deck">
        <div class="gauge-card env-gauge">
          <div class="gauge-title-row">
            <span class="gauge-icon">🌿</span>
            <span class="gauge-label">ENVIRONMENTAL HEALTH</span>
            <span class="gauge-value" id="mono-env-val">82%</span>
          </div>
          <div class="gauge-track">
            <div class="gauge-fill" id="mono-env-fill" style="width: 82%;"></div>
          </div>
          <div class="gauge-meta">CLEAN WATER • SOIL VIABILITY • CARBON EQUILIBRIUM</div>
        </div>

        <div class="gauge-card human-gauge">
          <div class="gauge-title-row">
            <span class="gauge-icon">🤝</span>
            <span class="gauge-label">HUMAN FLOURISHING</span>
            <span class="gauge-value" id="mono-human-val">76%</span>
          </div>
          <div class="gauge-track">
            <div class="gauge-fill" id="mono-human-fill" style="width: 76%;"></div>
          </div>
          <div class="gauge-meta">MENTAL HEALTH • CIVIC TRUST • PUBLIC EDUCATION</div>
        </div>

        <div class="gauge-card resource-gauge">
          <div class="gauge-title-row">
            <span class="gauge-icon">⚡</span>
            <span class="gauge-label">RESOURCE SUSTAINABILITY</span>
            <span class="gauge-value" id="mono-res-val">79%</span>
          </div>
          <div class="gauge-track">
            <div class="gauge-fill" id="mono-res-fill" style="width: 79%;"></div>
          </div>
          <div class="gauge-meta">ENERGY RESERVES • MATERIAL REUSE • FOOD SECURITY</div>
        </div>
      </div>

      <!-- =====================================================================
           THE MAIN SIMULATION INTERFACE
           ===================================================================== -->
      <div class="monopoly-engine-grid">

        <!-- Column 1: Character Origin & Life Vector Controls -->
        <div class="mono-col character-setup-col">
          <div class="mono-panel-box">
            <div class="panel-header">
              <span class="panel-dot"></span>
              <span class="panel-title">CHARACTER ORIGIN // VICARIOUS LIVED EXPERIENCE</span>
            </div>

            <!-- Origin Presets -->
            <div class="setup-group">
              <label class="setup-label">STARTING VECTOR (WALK IN ANY SHOES):</label>
              <div class="origin-presets-grid">
                <button type="button" class="origin-btn active" data-origin="unhoused">
                  <span>⛺ UNHOUSED SOVEREIGN ($0)</span>
                </button>
                <button type="button" class="origin-btn" data-origin="working">
                  <span>🔨 WORKING CLASS ($1,200)</span>
                </button>
                <button type="button" class="origin-btn" data-origin="adopted">
                  <span>🌱 ADOPTED HUSTLER ($3,500)</span>
                </button>
                <button type="button" class="origin-btn" data-origin="middle">
                  <span>🏡 SUBURBAN AVERAGE ($25,000)</span>
                </button>
                <button type="button" class="origin-btn" data-origin="bunker">
                  <span>🏰 BUNKER DYNAST ($2.5M)</span>
                </button>
              </div>
            </div>

            <!-- Education & Schooling -->
            <div class="setup-group">
              <label class="setup-label">EDUCATION PATHWAY (K-12 TO MASTERY):</label>
              <select id="mono-education-select" class="mono-select">
                <option value="public_k12" selected>Public K-12 (Community Grit, Zero Debt)</option>
                <option value="private_elite">Elite Private Prep (High Network, $85K Tuition Debt)</option>
                <option value="trade_apprentice">Vocational Trade Apprenticeship (Electric/Plumbing)</option>
                <option value="self_taught_net">Self-Taught Open Net Hacker (High Adaptability)</option>
              </select>
            </div>

            <!-- Modern AI Subscription Leverage -->
            <div class="setup-group">
              <label class="setup-label">AI ENGINE SUBSCRIPTION MODEL:</label>
              <select id="mono-ai-select" class="mono-select">
                <option value="free_tier">Free Open-Source Models ($0/mo // Manual Overhead)</option>
                <option value="pro_tier" selected>Pro AI Assistant Tier ($20/mo // 3x Leverage)</option>
                <option value="swarm_tier">Autonomous Agent Swarm ($200/mo // 12x Leverage)</option>
                <option value="luddite">Zero-Tech Sovereign (Immune to Hacks, High Physical Labor)</option>
              </select>
            </div>

            <!-- Core Anchor Values -->
            <div class="setup-group">
              <label class="setup-label">SPIRITUAL &amp; PHILOSOPHICAL ANCHOR:</label>
              <select id="mono-spirit-select" class="mono-select">
                <option value="church_faith" selected>Church &amp; Spiritual Fellowship (High Community Trust)</option>
                <option value="materialist">Materialist Wealth Maximizer (Fast Capital, Higher Stress)</option>
                <option value="eco_steward">Ecological Custodian (Preserves Natural Resources)</option>
                <option value="sovereign_nomad">Free-Roaming Sovereign Traveler (Zero Fixed Overhead)</option>
              </select>
            </div>

            <button type="button" class="mono-randomize-btn" id="btn-mono-randomize">
              <span>🎲 RANDOMIZE NEW DESTINY</span>
            </button>
          </div>

          <!-- Current Financial Ledger Card -->
          <div class="mono-panel-box ledger-box">
            <div class="panel-header">
              <span class="panel-dot yellow"></span>
              <span class="panel-title">LIVE FINANCIAL LEDGER &amp; KARMA</span>
            </div>
            <div class="ledger-metrics-grid">
              <div class="ledger-item">
                <span class="ledger-label">LIQUID CASH:</span>
                <span class="ledger-val" id="ledger-cash">$1,200</span>
              </div>
              <div class="ledger-item">
                <span class="ledger-label">DEBT / LEVERAGE:</span>
                <span class="ledger-val negative" id="ledger-debt">-$14,500</span>
              </div>
              <div class="ledger-item">
                <span class="ledger-label">NET MONTHLY FLOW:</span>
                <span class="ledger-val positive" id="ledger-flow">+$240/mo</span>
              </div>
              <div class="ledger-item">
                <span class="ledger-label">CREDIT SCORE:</span>
                <span class="ledger-val" id="ledger-credit">680 (Fair)</span>
              </div>
              <div class="ledger-item full-width">
                <span class="ledger-label">HARMONY INDEX (532nm GREEN CENTER):</span>
                <div class="karma-bar">
                  <div class="karma-fill" id="ledger-karma-fill" style="width: 72%;"></div>
                </div>
                <span class="karma-text" id="ledger-karma-text">72% ALIGNED WITH UNIVERSAL ORDER</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Column 2: The 12-Spectrum Board & Live Action Simulator -->
        <div class="mono-col board-action-col">
          <div class="mono-panel-box board-visual-box">
            <div class="panel-header">
              <span class="panel-dot green"></span>
              <span class="panel-title">THE 12 SPECTRUM ECONOMIC STRATA // REAL ESTATE MAP</span>
              <span class="board-turn-counter" id="mono-turn-counter">YEAR 1 (TURN 1)</span>
            </div>

            <!-- Spectrum 12-Tile Interactive Board Grid -->
            <div class="spectrum-tiles-board">
              <div class="board-tile tile-1" data-tile="1">
                <div class="tile-bar red"></div>
                <div class="tile-name">01. URBAN UNDERPASS</div>
                <div class="tile-cost">$0 / Rent Free</div>
                <div class="tile-owner" id="tile-owner-1">PUBLIC COMMONS</div>
              </div>
              <div class="board-tile tile-2" data-tile="2">
                <div class="tile-bar crimson"></div>
                <div class="tile-name">02. PUBLIC SCHOOL ZONE</div>
                <div class="tile-cost">$120K / $950 Rent</div>
                <div class="tile-owner" id="tile-owner-2">AVAILABLE</div>
              </div>
              <div class="board-tile tile-3" data-tile="3">
                <div class="tile-bar orange"></div>
                <div class="tile-name">03. WORKING-CLASS SUBURB</div>
                <div class="tile-cost">$240K / $1.8K Rent</div>
                <div class="tile-owner" id="tile-owner-3">AVAILABLE</div>
              </div>
              <div class="board-tile tile-4" data-tile="4">
                <div class="tile-bar amber"></div>
                <div class="tile-name">04. RURAL SOIL &amp; AQUIFER</div>
                <div class="tile-cost">$320K / Food Haven</div>
                <div class="tile-owner" id="tile-owner-4">AVAILABLE</div>
              </div>
              <div class="board-tile tile-5" data-tile="5">
                <div class="tile-bar yellow"></div>
                <div class="tile-name">05. SUBURBAN MASTER-PLAN</div>
                <div class="tile-cost">$540K / $3.4K Rent</div>
                <div class="tile-owner" id="tile-owner-5">AVAILABLE</div>
              </div>
              <div class="board-tile tile-6 center-tile" data-tile="6">
                <div class="tile-bar emerald"></div>
                <div class="tile-name">06. GREEN COMMONS ★</div>
                <div class="tile-cost">532nm CENTER</div>
                <div class="tile-owner" id="tile-owner-6">COMMUNITY TRUST</div>
              </div>
              <div class="board-tile tile-7" data-tile="7">
                <div class="tile-bar aqua"></div>
                <div class="tile-name">07. TECH INCUBATOR CORE</div>
                <div class="tile-cost">$850K / High-Rise</div>
                <div class="tile-owner" id="tile-owner-7">AVAILABLE</div>
              </div>
              <div class="board-tile tile-8" data-tile="8">
                <div class="tile-bar cyan"></div>
                <div class="tile-name">08. WALL ST &amp; CLEAR BANK</div>
                <div class="tile-cost">$1.6M / Debt Engine</div>
                <div class="tile-owner" id="tile-owner-8">AVAILABLE</div>
              </div>
              <div class="board-tile tile-9" data-tile="9">
                <div class="tile-bar cobalt"></div>
                <div class="tile-name">09. OFFSHORE CLOUD HAVEN</div>
                <div class="tile-cost">$3.2M / Encrypted</div>
                <div class="tile-owner" id="tile-owner-9">AVAILABLE</div>
              </div>
              <div class="board-tile tile-10" data-tile="10">
                <div class="tile-bar indigo"></div>
                <div class="tile-name">10. POLITICAL CAPITOL</div>
                <div class="tile-cost">$6.5M / Lobby Hub</div>
                <div class="tile-owner" id="tile-owner-10">AVAILABLE</div>
              </div>
              <div class="board-tile tile-11" data-tile="11">
                <div class="tile-bar violet"></div>
                <div class="tile-name">11. DOOMSDAY BUNKER</div>
                <div class="tile-cost">$15M / Subterranean</div>
                <div class="tile-owner" id="tile-owner-11">AVAILABLE</div>
              </div>
              <div class="board-tile tile-12" data-tile="12">
                <div class="tile-bar alabaster"></div>
                <div class="tile-name">12. GLOBAL SANCTUARY</div>
                <div class="tile-cost">PLANETARY TRUST</div>
                <div class="tile-owner" id="tile-owner-12">ALL HUMANS</div>
              </div>
            </div>

            <!-- Current Location Badge -->
            <div class="current-tile-display">
              <span class="cur-tile-label">CURRENT LOCATION:</span>
              <span class="cur-tile-name" id="mono-current-tile-name">TILE 03: WORKING-CLASS BLUE-COLLAR SUBURB</span>
            </div>

            <!-- Interactive Decision & Turn Rail -->
            <div class="mono-action-console">
              <button type="button" class="action-btn roll-btn" id="btn-mono-roll">
                <span>🎲 ADVANCE LIFE &amp; ROLL (1-6)</span>
              </button>
              <button type="button" class="action-btn buy-btn" id="btn-mono-buy">
                <span>🏢 ACQUIRE REAL ESTATE DEED</span>
              </button>
              <button type="button" class="action-btn moral-btn" id="btn-mono-moral-choice">
                <span>⚖️ FACE REAL-WORLD MORAL CROSSROADS</span>
              </button>
              <button type="button" class="action-btn rest-btn" id="btn-mono-restitution">
                <span>🕊️ RESTITUTION TO GREEN COMMONS</span>
              </button>
            </div>

            <!-- Event Dialogue & Stacking Choices Drawer -->
            <div class="mono-event-dialogue" id="mono-event-box">
              <div class="event-headline" id="event-headline">LIFE EVENT // YEAR 1: CAREER VELOCITY</div>
              <p class="event-body" id="event-body">
                You work in the industrial district. A local multifamily apartment building in Tile 03 is up for auction. 
                Will you partner with neighborhood families to form a cooperative land trust (Honorable), or take out an aggressive private loan to evict current tenants and double rents?
              </p>
              <div class="event-choices-row" id="event-choices-row">
                <button type="button" class="choice-btn honorable" id="btn-choice-honorable">
                  <span>✔ CHOICE A: HONORABLE COOPERATIVE TRUST (+Flourishing, Stable Return)</span>
                </button>
                <button type="button" class="choice-btn shadow" id="btn-choice-shadow">
                  <span>⚠️ CHOICE B: CLEAR-NET SPECULATION &amp; SHELL FLIP (+$45K Cash, -Humanity)</span>
                </button>
              </div>
            </div>

            <!-- Story Log Stream -->
            <div class="mono-story-log">
              <div class="log-title">TRANSMISSION FEED &amp; STACKING CHOICES LOG:</div>
              <div class="log-entries" id="mono-log-entries">
                <div class="log-entry">⟦ SYSTEM ⟧ Character initialized as Working Class Hustler in Tile 03. AI Pro Tier active ($20/mo).</div>
                <div class="log-entry">⟦ MACRO ⟧ Environment at 82%, Human Index at 76%. Balance held at Green Commons.</div>
              </div>
            </div>

          </div>
        </div>

      </div>

      <!-- Footer Note -->
      <div class="tribute-footer-signature">
        <span>⟦ LUMBROS.ME // THE NEW MONOPOLY // DESIGNED BY LUM // ECONOMIC EQUILIBRIUM THROUGH MATHEMATICS &amp; GOD ⟧</span>
      </div>

    </div>
  </section>
  <!-- =========================================================================
       END SECTION: SPECTRUM MONOPOLY
       ========================================================================= -->
'''

# 3. Build Spectrum Monopoly CSS Styles
monopoly_css = '''
    /* =========================================================================
       SPECTRUM MONOPOLY STYLES // DESIGNED BY LUM
       ========================================================================= */
    .monopoly-section {
      margin-bottom: 50px;
      position: relative;
    }
    .monopoly-frame {
      position: relative;
      background: rgba(0, 20, 10, 0.85);
      border: 2px solid #00ff66;
      border-radius: 14px;
      padding: 28px;
      box-shadow: 0 0 50px rgba(0, 255, 102, 0.2), inset 0 0 35px rgba(0, 255, 102, 0.08);
      overflow: hidden;
      backdrop-filter: blur(12px);
    }
    .monopoly-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      padding: 14px 20px;
      background: rgba(0, 40, 20, 0.7);
      border: 1px solid #1f6b3d;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .monopoly-brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .monopoly-logo-chip {
      background: linear-gradient(135deg, #00ff66, #ffaa00);
      color: #00150a;
      font-weight: 900;
      font-size: 0.85rem;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 1px;
    }
    .monopoly-brand-sub {
      color: #00e5ff;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 1.5px;
    }
    .monopoly-tag-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .mono-tag {
      background: rgba(0, 50, 25, 0.6);
      border: 1px solid #1a5c34;
      color: #8ce4a7;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 1px;
    }
    .mono-tag.highlight {
      border-color: #00ff66;
      color: #00ff66;
      background: #003314;
    }

    .monopoly-intro-card {
      background: rgba(0, 30, 15, 0.55);
      border-left: 4px solid #00ff66;
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 24px;
    }
    .monopoly-intro-text {
      color: #d8f5e5;
      font-size: 0.96rem;
      line-height: 1.65;
      margin: 0;
    }

    /* Planetary Survival Gauges */
    .planetary-gauges-deck {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 26px;
    }
    @media (max-width: 900px) {
      .planetary-gauges-deck { grid-template-columns: 1fr; }
    }
    .gauge-card {
      background: rgba(0, 25, 12, 0.8);
      border: 1px solid #1a5c34;
      border-radius: 8px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      transition: all 0.2s;
    }
    .gauge-card:hover {
      border-color: #00ff66;
      transform: translateY(-2px);
    }
    .gauge-title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.76rem;
      font-weight: 800;
    }
    .gauge-label { color: #ffffff; letter-spacing: 1px; }
    .gauge-value { color: #00ff66; font-size: 0.88rem; font-weight: 900; }
    .gauge-track {
      background: #00150a;
      height: 10px;
      border-radius: 5px;
      overflow: hidden;
      border: 1px solid #14442a;
    }
    .gauge-fill {
      height: 100%;
      background: linear-gradient(90deg, #008736, #00ff66);
      transition: width 0.5s ease;
    }
    .gauge-meta {
      font-size: 0.65rem;
      color: #8ce4a7;
      letter-spacing: 1px;
    }

    /* Main Grid */
    .monopoly-engine-grid {
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: 22px;
      margin-bottom: 24px;
    }
    @media (max-width: 1050px) {
      .monopoly-engine-grid { grid-template-columns: 1fr; }
    }

    .mono-panel-box {
      background: rgba(0, 25, 12, 0.75);
      border: 1px solid #1a5c34;
      border-radius: 10px;
      padding: 18px;
      margin-bottom: 18px;
    }
    .panel-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
      font-size: 0.78rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
    }
    .panel-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
    }
    .panel-dot.yellow { background: #ffaa00; box-shadow: 0 0 8px #ffaa00; }
    .panel-dot.green { background: #00ff66; box-shadow: 0 0 8px #00ff66; }

    .setup-group {
      margin-bottom: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .setup-label {
      font-size: 0.7rem;
      color: #8ce4a7;
      font-weight: 700;
      letter-spacing: 1px;
    }
    .origin-presets-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 6px;
    }
    .origin-btn {
      text-align: left;
      background: rgba(0, 35, 18, 0.7);
      border: 1px solid #1f6b3d;
      color: #d8f5e5;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .origin-btn:hover { border-color: #00ff66; color: #ffffff; }
    .origin-btn.active {
      background: #00ff66;
      color: #00150a;
      border-color: #00ff66;
      box-shadow: 0 0 10px rgba(0, 255, 102, 0.4);
    }
    .mono-select {
      background: #001a0a;
      border: 1px solid #1a5c34;
      color: #ffffff;
      padding: 7px 10px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 700;
      font-family: inherit;
    }
    .mono-randomize-btn {
      width: 100%;
      margin-top: 10px;
      background: linear-gradient(135deg, #008736, #00ff66);
      color: #00150a;
      border: none;
      padding: 9px;
      border-radius: 6px;
      font-weight: 900;
      font-size: 0.78rem;
      letter-spacing: 1px;
      cursor: pointer;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.3);
      transition: all 0.2s;
    }
    .mono-randomize-btn:hover {
      box-shadow: 0 0 18px rgba(0, 255, 102, 0.6);
      transform: translateY(-1px);
    }

    /* Ledger */
    .ledger-metrics-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }
    .ledger-item {
      background: rgba(0, 20, 10, 0.6);
      border: 1px solid #164627;
      padding: 8px 10px;
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .ledger-item.full-width {
      grid-column: span 2;
    }
    .ledger-label {
      font-size: 0.66rem;
      color: #8ce4a7;
      font-weight: 700;
      letter-spacing: 1px;
    }
    .ledger-val {
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.84rem;
      font-weight: 900;
      color: #ffffff;
    }
    .ledger-val.positive { color: #00ff66; }
    .ledger-val.negative { color: #ff5566; }
    .karma-bar {
      height: 8px;
      background: #00150a;
      border-radius: 4px;
      overflow: hidden;
      margin: 4px 0 2px 0;
    }
    .karma-fill {
      height: 100%;
      background: linear-gradient(90deg, #ffaa00, #00ff66);
      transition: width 0.4s ease;
    }
    .karma-text {
      font-size: 0.68rem;
      color: #00ff66;
      font-weight: 800;
    }

    /* 12 Spectrum Tiles Board */
    .spectrum-tiles-board {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-bottom: 16px;
    }
    @media (max-width: 750px) {
      .spectrum-tiles-board { grid-template-columns: repeat(2, 1fr); }
    }
    .board-tile {
      background: rgba(0, 30, 15, 0.7);
      border: 1px solid #1a5c34;
      border-radius: 6px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      gap: 3px;
      transition: all 0.2s;
    }
    .board-tile:hover {
      border-color: #00ff66;
      transform: translateY(-2px);
    }
    .board-tile.active-location {
      border-color: #00ff66;
      box-shadow: 0 0 14px rgba(0, 255, 102, 0.5);
      background: rgba(0, 50, 25, 0.85);
    }
    .board-tile.center-tile {
      border: 1.5px solid #00ff66;
      background: rgba(0, 45, 20, 0.85);
    }
    .tile-bar {
      height: 5px;
      border-radius: 2px;
      margin-bottom: 2px;
    }
    .tile-bar.red { background: #ff0033; }
    .tile-bar.crimson { background: #ff2255; }
    .tile-bar.orange { background: #ff7700; }
    .tile-bar.amber { background: #ffaa00; }
    .tile-bar.yellow { background: #ffff00; }
    .tile-bar.emerald { background: #00ff66; box-shadow: 0 0 6px #00ff66; }
    .tile-bar.aqua { background: #00ffcc; }
    .tile-bar.cyan { background: #00ccff; }
    .tile-bar.cobalt { background: #0066ff; }
    .tile-bar.indigo { background: #4400ff; }
    .tile-bar.violet { background: #8800ff; }
    .tile-bar.alabaster { background: #ffffff; }

    .tile-name {
      font-size: 0.68rem;
      font-weight: 800;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .tile-cost {
      font-size: 0.62rem;
      color: #8ce4a7;
      font-family: 'Courier New', Courier, monospace;
    }
    .tile-owner {
      font-size: 0.6rem;
      color: #00e5ff;
      font-weight: 700;
    }

    .current-tile-display {
      background: rgba(0, 35, 18, 0.8);
      border: 1px solid #1f6b3d;
      padding: 8px 14px;
      border-radius: 6px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }
    .cur-tile-label { font-size: 0.72rem; color: #8ce4a7; font-weight: 800; }
    .cur-tile-name { font-size: 0.8rem; color: #00ff66; font-weight: 900; }

    /* Action Rail */
    .mono-action-console {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-bottom: 16px;
    }
    @media (max-width: 850px) {
      .mono-action-console { grid-template-columns: 1fr 1fr; }
    }
    .action-btn {
      background: rgba(0, 40, 20, 0.75);
      border: 1px solid #238048;
      color: #ffffff;
      padding: 9px 10px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 800;
      cursor: pointer;
      letter-spacing: 0.5px;
      transition: all 0.2s;
    }
    .action-btn:hover {
      background: #00ff66;
      color: #00150a;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.4);
    }
    .action-btn.roll-btn {
      background: linear-gradient(135deg, #008736, #00ff66);
      color: #00150a;
      font-weight: 900;
    }
    .action-btn.moral-btn {
      border-color: #ffaa00;
      color: #ffaa00;
    }
    .action-btn.moral-btn:hover {
      background: #ffaa00;
      color: #00150a;
    }

    /* Event Dialogue */
    .mono-event-dialogue {
      background: rgba(0, 20, 10, 0.9);
      border: 1.5px solid #00e5ff;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 16px;
    }
    .event-headline {
      font-size: 0.8rem;
      font-weight: 900;
      color: #00e5ff;
      letter-spacing: 1.5px;
      margin-bottom: 8px;
    }
    .event-body {
      color: #d8f5e5;
      font-size: 0.84rem;
      line-height: 1.5;
      margin: 0 0 14px 0;
    }
    .event-choices-row {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    .choice-btn {
      flex: 1;
      padding: 9px 12px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.2s;
    }
    .choice-btn.honorable {
      background: #003314;
      border: 1px solid #00ff66;
      color: #00ff66;
    }
    .choice-btn.honorable:hover {
      background: #00ff66;
      color: #00150a;
    }
    .choice-btn.shadow {
      background: #331500;
      border: 1px solid #ff7700;
      color: #ff9933;
    }
    .choice-btn.shadow:hover {
      background: #ff7700;
      color: #000000;
    }

    /* Story Log */
    .mono-story-log {
      background: #000d06;
      border: 1px solid #14442a;
      border-radius: 8px;
      padding: 12px 14px;
      max-height: 140px;
      overflow-y: auto;
    }
    .log-title {
      font-size: 0.68rem;
      font-weight: 800;
      color: #8ce4a7;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }
    .log-entries {
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-family: 'Courier New', Courier, monospace;
      font-size: 0.72rem;
      color: #64ffda;
    }

    /* Light Mode Overrides */
    body[data-theme="light"] .monopoly-frame {
      background: #ffffff !important;
      border-color: #008736 !important;
      box-shadow: 0 6px 25px rgba(0, 100, 40, 0.12) !important;
    }
    body[data-theme="light"] .monopoly-header-bar,
    body[data-theme="light"] .current-tile-display {
      background: #eefbf4 !important;
      border-color: #a3dfbd !important;
    }
    body[data-theme="light"] .monopoly-brand-sub,
    body[data-theme="light"] .cur-tile-name {
      color: #007799 !important;
    }
    body[data-theme="light"] .monopoly-intro-card {
      background: #f4fcf7 !important;
      border-left-color: #00aa44 !important;
    }
    body[data-theme="light"] .monopoly-intro-text,
    body[data-theme="light"] .event-body {
      color: #1a3a28 !important;
    }
    body[data-theme="light"] .gauge-card,
    body[data-theme="light"] .mono-panel-box,
    body[data-theme="light"] .board-tile {
      background: #f7fdf9 !important;
      border-color: #b8e6cd !important;
    }
    body[data-theme="light"] .gauge-label,
    body[data-theme="light"] .tile-name {
      color: #0a2615 !important;
    }
    body[data-theme="light"] .origin-btn {
      background: #eefbf3 !important;
      border-color: #72cca0 !important;
      color: #006622 !important;
    }
    body[data-theme="light"] .mono-select {
      background: #ffffff !important;
      color: #00150a !important;
      border-color: #94d4b1 !important;
    }
    body[data-theme="light"] .action-btn {
      background: #e8f8ef !important;
      border-color: #8ed2ad !important;
      color: #0e3b1f !important;
    }
    body[data-theme="light"] .mono-event-dialogue {
      background: #f4fcf7 !important;
      border-color: #007799 !important;
    }
    body[data-theme="light"] .mono-story-log {
      background: #eefbf4 !important;
      border-color: #a3dfbd !important;
    }
    body[data-theme="light"] .log-entries {
      color: #004d1f !important;
    }
    /* =========================================================================
       END SPECTRUM MONOPOLY STYLES
       ========================================================================= */
'''

# 4. Build Spectrum Monopoly JavaScript Game Engine
monopoly_js = '''
    // =========================================================================
    // SPECTRUM MONOPOLY GAME ENGINE // DESIGNED & DEVELOPED BY LUM
    // =========================================================================
    (function initSpectrumMonopoly() {
      var turn = 1;
      var currentTileIdx = 3; // Starts at Tile 3 (Working Class Blue Collar)
      var playerState = {
        origin: 'working',
        cash: 1200,
        debt: 14500,
        cashFlow: 240,
        credit: 680,
        karma: 72,
        aiTier: 'pro_tier',
        education: 'public_k12',
        spirit: 'church_faith',
        deeds: []
      };

      var planetaryState = {
        env: 82,
        human: 76,
        res: 79
      };

      var tilesData = [
        { id: 1, name: '01. URBAN UNDERPASS', cost: 0, rent: 0, owner: 'PUBLIC COMMONS' },
        { id: 2, name: '02. PUBLIC SCHOOL ZONE', cost: 120000, rent: 950, owner: 'AVAILABLE' },
        { id: 3, name: '03. WORKING-CLASS SUBURB', cost: 240000, rent: 1800, owner: 'AVAILABLE' },
        { id: 4, name: '04. RURAL SOIL & AQUIFER', cost: 320000, rent: 2200, owner: 'AVAILABLE' },
        { id: 5, name: '05. SUBURBAN MASTER-PLAN', cost: 540000, rent: 3400, owner: 'AVAILABLE' },
        { id: 6, name: '06. GREEN COMMONS ★', cost: 0, rent: 0, owner: 'COMMUNITY TRUST' },
        { id: 7, name: '07. TECH INCUBATOR CORE', cost: 850000, rent: 5200, owner: 'AVAILABLE' },
        { id: 8, name: '08. WALL ST & CLEAR BANK', cost: 1600000, rent: 9800, owner: 'AVAILABLE' },
        { id: 9, name: '09. OFFSHORE CLOUD HAVEN', cost: 3200000, rent: 18000, owner: 'AVAILABLE' },
        { id: 10, name: '10. POLITICAL CAPITOL', cost: 6500000, rent: 35000, owner: 'AVAILABLE' },
        { id: 11, name: '11. DOOMSDAY BUNKER', cost: 15000000, rent: 0, owner: 'AVAILABLE' },
        { id: 12, name: '12. GLOBAL SANCTUARY', cost: 0, rent: 0, owner: 'ALL HUMANS' }
      ];

      // DOM Elements
      var cashEl = document.getElementById('ledger-cash');
      var debtEl = document.getElementById('ledger-debt');
      var flowEl = document.getElementById('ledger-flow');
      var creditEl = document.getElementById('ledger-credit');
      var karmaFillEl = document.getElementById('ledger-karma-fill');
      var karmaTextEl = document.getElementById('ledger-karma-text');
      var curTileNameEl = document.getElementById('mono-current-tile-name');
      var turnCounterEl = document.getElementById('mono-turn-counter');
      var envValEl = document.getElementById('mono-env-val');
      var envFillEl = document.getElementById('mono-env-fill');
      var humanValEl = document.getElementById('mono-human-val');
      var humanFillEl = document.getElementById('mono-human-fill');
      var resValEl = document.getElementById('mono-res-val');
      var resFillEl = document.getElementById('mono-res-fill');
      var eventHeadlineEl = document.getElementById('event-headline');
      var eventBodyEl = document.getElementById('event-body');
      var logEntriesEl = document.getElementById('mono-log-entries');

      function updateLedgerUI() {
        if (cashEl) cashEl.textContent = '$' + playerState.cash.toLocaleString();
        if (debtEl) debtEl.textContent = (playerState.debt > 0 ? '-$' : '$') + Math.abs(playerState.debt).toLocaleString();
        if (flowEl) flowEl.textContent = (playerState.cashFlow >= 0 ? '+$' : '-$') + Math.abs(playerState.cashFlow).toLocaleString() + '/mo';
        if (creditEl) creditEl.textContent = playerState.credit + (playerState.credit >= 720 ? ' (Excellent)' : (playerState.credit >= 640 ? ' (Fair)' : ' (Subprime)'));
        if (karmaFillEl) karmaFillEl.style.width = playerState.karma + '%';
        if (karmaTextEl) karmaTextEl.textContent = playerState.karma + '% ALIGNED WITH UNIVERSAL ORDER';

        // Planetary Gauges
        if (envValEl) envValEl.textContent = planetaryState.env + '%';
        if (envFillEl) envFillEl.style.width = planetaryState.env + '%';
        if (humanValEl) humanValEl.textContent = planetaryState.human + '%';
        if (humanFillEl) humanFillEl.style.width = planetaryState.human + '%';
        if (resValEl) resValEl.textContent = planetaryState.res + '%';
        if (resFillEl) resFillEl.style.width = planetaryState.res + '%';

        // Current Tile Highlighting
        var activeTile = tilesData[currentTileIdx - 1];
        if (curTileNameEl) if (activeTile) {
          curTileNameEl.textContent = activeTile.name;
        }

        for (var i = 1; i <= 12; i++) {
          var tEl = document.querySelector('.board-tile[data-tile="' + i + '"]');
          if (tEl) {
            if (i === currentTileIdx) tEl.classList.add('active-location');
            else tEl.classList.remove('active-location');
          }
        }
      }

      function addLog(msg) {
        if (!logEntriesEl) return;
        var div = document.createElement('div');
        div.className = 'log-entry';
        div.textContent = '⟦ YEAR ' + turn + ' ⟧ ' + msg;
        logEntriesEl.insertBefore(div, logEntriesEl.firstChild);
      }

      // Roll Dice
      var rollBtn = document.getElementById('btn-mono-roll');
      if (rollBtn) {
        rollBtn.addEventListener('click', function() {
          var roll = Math.floor(Math.random() * 6) + 1;
          currentTileIdx = ((currentTileIdx - 1 + roll) % 12) + 1;
          turn++;
          if (turnCounterEl) turnCounterEl.textContent = 'YEAR ' + turn;

          // Apply Cash Flow
          playerState.cash += playerState.cashFlow;

          // Natural planetary drift
          planetaryState.env = Math.max(10, Math.min(100, planetaryState.env - 1));
          planetaryState.human = Math.max(10, Math.min(100, planetaryState.human + (playerState.karma > 60 ? 1 : -1)));

          addLog('Advanced ' + roll + ' strata to ' + tilesData[currentTileIdx - 1].name + '. Cash flow applied: +$' + playerState.cashFlow);
          triggerTileEvent(currentTileIdx);
          updateLedgerUI();
        });
      }

      function triggerTileEvent(tileNum) {
        if (!eventHeadlineEl) return;
        if (!eventBodyEl) return;

        if (tileNum === 4) {
          eventHeadlineEl.textContent = 'RURAL FOOD & WATER CRISIS // MACRO LEVEL EVENT';
          eventBodyEl.textContent = 'Drought strikes Layer 04. Regional aquifer water permits are scarce. Will you invest in community rainwater catchment (Honorable) or monopolize deep-well extraction to charge emergency rates (Shadow)?';
        } else if (tileNum === 6) {
          eventHeadlineEl.textContent = 'GREEN COMMONS EQUILIBRIUM (532nm) // HARMONIC CENTER';
          eventBodyEl.textContent = 'You arrived at the Green Commons. Community land trust offers regenerative housing and shared food reserves. Mental health is restored; planetary sustainability rises!';
          playerState.karma = Math.min(100, playerState.karma + 10);
          planetaryState.human = Math.min(100, planetaryState.human + 6);
          planetaryState.env = Math.min(100, planetaryState.env + 4);
        } else if (tileNum === 8) {
          eventHeadlineEl.textContent = 'CLEAR-NET FINANCIAL SPECULATION // WALL ST DESK';
          eventBodyEl.textContent = 'Investment banker offers access to a high-yield fractional mortgage syndicate. Will you structure ethical low-interest credit for local workers, or purchase predatory subprime debt bundles?';
        } else if (tileNum === 11) {
          eventHeadlineEl.textContent = 'THE SUBTERRANEAN BUNKER ENCLAVE // DOOMSDAY WEALTH';
          eventBodyEl.textContent = 'A billionaire offers you shelter access in exchange for liquid capital. But the surrounding community lacks basic health care. Isolation or solidarity?';
        } else {
          eventHeadlineEl.textContent = 'REAL ESTATE & CAREER CHOICE // ' + tilesData[tileNum - 1].name;
          eventBodyEl.textContent = 'You navigate this economic zone. New opportunities arise to expand your network, deploy AI tools, or support community resilience.';
        }
      }

      // Honorable vs Shadow Choice Handlers
      var btnChoiceHon = document.getElementById('btn-choice-honorable');
      var btnChoiceShad = document.getElementById('btn-choice-shadow');

      if (btnChoiceHon) {
        btnChoiceHon.addEventListener('click', function() {
          playerState.karma = Math.min(100, playerState.karma + 8);
          playerState.cashFlow += 180;
          planetaryState.human = Math.min(100, planetaryState.human + 3);
          planetaryState.env = Math.min(100, planetaryState.env + 2);
          addLog('CHOSE HONORABLE PATH: Built cooperative equity. Karma +8%, Human Flourishing +3%.');
          updateLedgerUI();
        });
      }

      if (btnChoiceShad) {
        btnChoiceShad.addEventListener('click', function() {
          playerState.cash += 45000;
          playerState.karma = Math.max(10, playerState.karma - 18);
          planetaryState.human = Math.max(10, planetaryState.human - 6);
          planetaryState.env = Math.max(10, planetaryState.env - 4);
          addLog('CHOSE SHADOW SPECULATION: Liquid cash +$45,000, Karma -18%, Community Trust degraded.');
          updateLedgerUI();
        });
      }

      // Restitution Action
      var restBtn = document.getElementById('btn-mono-restitution');
      if (restBtn) {
        restBtn.addEventListener('click', function() {
          if (playerState.cash >= 5000) {
            playerState.cash -= 5000;
            playerState.karma = Math.min(100, playerState.karma + 15);
            planetaryState.human = Math.min(100, planetaryState.human + 5);
            planetaryState.env = Math.min(100, planetaryState.env + 4);
            addLog('RESTITUTION: Donated $5,000 to the 532nm Green Commons. Karma +15%, balance restored!');
          } else {
            addLog('RESTITUTION: Dedicated voluntary labor to community soil & school restoration. Karma +5%.');
            playerState.karma = Math.min(100, playerState.karma + 5);
          }
          updateLedgerUI();
        });
      }

      // Origin Selector Buttons
      var originBtns = document.querySelectorAll('.origin-btn');
      originBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          originBtns.forEach(function(b) { b.classList.remove('active'); });
          btn.classList.add('active');
          var origin = btn.getAttribute('data-origin');
          playerState.origin = origin;

          if (origin === 'unhoused') {
            playerState.cash = 0; playerState.debt = 0; playerState.cashFlow = 40; playerState.credit = 520;
            currentTileIdx = 1;
          } else if (origin === 'working') {
            playerState.cash = 1200; playerState.debt = 14500; playerState.cashFlow = 240; playerState.credit = 680;
            currentTileIdx = 3;
          } else if (origin === 'adopted') {
            playerState.cash = 3500; playerState.debt = 6000; playerState.cashFlow = 420; playerState.credit = 710;
            currentTileIdx = 2;
          } else if (origin === 'middle') {
            playerState.cash = 25000; playerState.debt = 45000; playerState.cashFlow = 850; playerState.credit = 740;
            currentTileIdx = 5;
          } else if (origin === 'bunker') {
            playerState.cash = 2500000; playerState.debt = 0; playerState.cashFlow = 18000; playerState.credit = 820;
            currentTileIdx = 11;
          }

          addLog('Assumed new identity: ' + origin.toUpperCase() + '. Starting at ' + tilesData[currentTileIdx - 1].name);
          updateLedgerUI();
        });
      });

      // AI Selector
      var aiSelect = document.getElementById('mono-ai-select');
      if (aiSelect) {
        aiSelect.addEventListener('change', function() {
          var val = aiSelect.value;
          playerState.aiTier = val;
          if (val === 'free_tier') {
            addLog('AI Model: Free Open-Source. Overhead: $0/mo.');
          } else if (val === 'pro_tier') {
            playerState.cashFlow += 120;
            addLog('AI Model: Pro Assistant ($20/mo). Productivity +120/mo.');
          } else if (val === 'swarm_tier') {
            playerState.cashFlow += 850;
            addLog('AI Model: Autonomous Agent Swarm ($200/mo). Productivity +$850/mo.');
          }
          updateLedgerUI();
        });
      }

      // Randomize Destiny Button
      var randBtn = document.getElementById('btn-mono-randomize');
      if (randBtn) {
        randBtn.addEventListener('click', function() {
          var origins = ['unhoused', 'working', 'adopted', 'middle', 'bunker'];
          var randOrigin = origins[Math.floor(Math.random() * origins.length)];
          var btn = document.querySelector('.origin-btn[data-origin="' + randOrigin + '"]');
          if (btn) btn.click();
        });
      }

      // Initial UI Sync
      updateLedgerUI();
    })();
    // =========================================================================
    // END SPECTRUM MONOPOLY GAME ENGINE
    // =========================================================================
'''

# 5. Insert Section into homepage.html right after Section 0x09
target_marker = '<!-- =========================================================================\n       SUB MENU DOCK AT BOTTOM OF PAGE: ROOT SECTOR MATRIX & TIME CONTINUUM'
if target_marker not in home_content:
    target_marker = '<section id="pillars-architecture"'

home_content = home_content.replace(target_marker, monopoly_section_html + '\n\n  ' + target_marker, 1)

# Append CSS
style_closing = '</style>'
home_content = home_content.replace(style_closing, monopoly_css + '\n  ' + style_closing, 1)

# Append JS
script_closing = '</script>'
last_script_idx = home_content.rfind(script_closing)
if last_script_idx != -1:
    home_content = home_content[:last_script_idx] + monopoly_js + '\n  ' + home_content[last_script_idx:]

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home_content)

print(f"SUCCESS: Injected Spectrum Monopoly Section into {HOMEPAGE_PATH}!")
