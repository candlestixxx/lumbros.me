"""
Script to inject JavaScript engines for:
1. Digital Human Life Simulator (Screen A)
2. The Entire Soul Calculator (Screen B)
3. Bonus Shadertoy World-Shading & Dimensional Spectrum Modeler
into deploy/homepage.html.

STRICT WORDPRESS SAFETY RULE: ZERO raw '&&' inside script tags.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

JS_ENGINES = '''
    // =========================================================================
    // DUAL-SCREEN DIGITAL HUMAN LIFE SIMULATOR & THE ENTIRE SOUL CALCULATOR
    // POWERED BY NEURAL AI CO-PILOT // FROM SINGLE WOMAN TO WORKING MOTHER & NETWORKS
    // ARCHITECTED BY LUM (LUMBROS KOURLOS) // ANCHORED AT 532nm EMERALD CENTER
    // =========================================================================

    // PART A: DIGITAL HUMAN BIOMETRIC ANIMATION & DAILY LIFE CHOICES ENGINE
    (function initDigitalHumanSimulator() {
      var canvas = document.getElementById('digital-human-canvas');
      if (!canvas) return;
      var ctx = canvas.getContext('2d');
      if (!ctx) return;

      var currentPersona = 'single_woman';
      var currentCycleIdx = 0;
      var animTime = 0;
      var auraHue = 140; // 140 deg is emerald green (532nm)
      var auraIntensity = 1.0;
      var stressLevel = 14;
      var heartCoherence = 94.8;

      // 4 Personas with Multi-Layered Dilemmas
      var personaDilemmas = {
        single_woman: [
          {
            category: 'DILEMMA // CAREER VELOCITY VS. INTIMACY & INDEPENDENCE',
            title: 'Executive VP Promotion vs. Creative Sovereignty & Dating',
            narrative: 'A global tech titan offers you an executive VP role with an +80% compensation bump. However, it requires 65-hour weeks and constant travel, severely straining a budding romantic relationship, your weekly painting studio time, and proximity to aging parents.',
            oracleAdvice: '"Immediate capital spikes, but somatic nervous strain surges by 68%. Relational intimacy and family proximity will decay without strict non-negotiable boundaries. Consider negotiating hybrid terms or launching sovereign advisory."',
            choices: {
              a: { text: 'Negotiate Hybrid Advisory: Retain creative autonomy, protect family dinner & budding intimacy. (+Soul, +Peace)', dMind: 5, dBody: 4, dSoul: 8, dCap: 7, log: 'Negotiated hybrid terms. Autonomy protected; intimate relationship blooms; parents supported.' },
              b: { text: 'Accept Full 65hr VP Role: Maximize capital & corporate prestige, pause dating for 18mo. (+Cash, -Vitality)', dMind: -8, dBody: -12, dSoul: -6, dCap: -5, log: 'Took the VP seat. Cash surged, but 65hr weeks triggered circadian burnout and relationship distance.' },
              c: { text: 'Launch Independent Studio: Form cooperative network, invite close friends, accept lean year. (+Sovereignty)', dMind: 6, dBody: 2, dSoul: 9, dCap: 6, log: 'Formed independent studio. Lean year of building sovereign freedom with trusted collaborators.' }
            }
          },
          {
            category: 'DILEMMA // BOUNDARIES WITH CASUAL DATING & NETWORKS',
            title: 'High-Net-Worth Casual Suitor vs. Uncompromised Self-Worth',
            narrative: 'A wealthy acquaintance from your professional network offers lavish lifestyle subsidies and luxury travel, but expects emotional exclusivity without vulnerability, equal partnership, or spiritual alignment.',
            oracleAdvice: '"Transactional arrangements erode self-worth and 532nm heart coherence over time. Sovereign self-reliance builds authentic magnetic attraction and lasting life capital."',
            choices: {
              a: { text: 'Set Absolute Clear Boundary: Politely decline transactional dynamics, honor your emotional sacredness.', dMind: 4, dBody: 3, dSoul: 10, dCap: 5, log: 'Politely declined transactional suitor. Deep inner peace and sovereign self-respect established.' },
              b: { text: 'Enter Conditional Arrangement: Enjoy luxury networking while privately guarding emotional core.', dMind: -5, dBody: -4, dSoul: -9, dCap: -4, log: 'Accepted conditional dinners. Emotional dissonance clouded your creative clarity.' },
              c: { text: 'Channel Energy into Lifelong Sisterhood: Host an intimate dinner with genuine friends who nurture your soul.', dMind: 6, dBody: 5, dSoul: 8, dCap: 9, log: 'Invested into lifelong friends. Deep vulnerability and authentic shared laughter restored vitality.' }
            }
          }
        ],
        working_mother: [
          {
            category: 'DILEMMA // MATERNAL SACRIFICE VS. CAREER SURVIVAL',
            title: 'Child High Fever on Executive Pitch Morning',
            narrative: 'Your 4-year-old wakes up with a 103°F fever on the morning of a make-or-break presentation to board directors. The company culture frowns on last-minute remote requests, and your private backup nanny is unavailable.',
            oracleAdvice: '"A child&rsquo;s physiological distress is non-negotiable. Careers can recover from honest communication; maternal trust broken in vulnerability leaves lasting somatic scars."',
            choices: {
              a: { text: 'Stay at Child\'s Bedside: Brief trusted deputy to deliver slides, notify CEO with calm transparency.', dMind: 3, dBody: 2, dSoul: 12, dCap: 9, log: 'Stayed by your child. Deputy stepped up; CEO respected your transparent integrity.' },
              b: { text: 'Administer Antipyretic & Rush to Meeting: Leave child with neighbor for 3 hours, sprint through pitch.', dMind: -10, dBody: -8, dSoul: -12, dCap: -6, log: 'Delivered pitch with intense inner panic. Board approved proposal, but guilt weighed heavily on your heart.' },
              c: { text: 'Pivot Meeting to Video from Bedroom: Balance soothing child with crisp professional delivery.', dMind: 2, dBody: -2, dSoul: 6, dCap: 5, log: 'Delivered presentation remotely with child asleep beside you. Genuine human leadership resonated with directors.' }
            }
          },
          {
            category: 'DILEMMA // FAMILY RUNWAY VS. OVERWHELMING OVERHEAD',
            title: '40% Childcare Cost Hike vs. Midnight Freelancing',
            narrative: 'Montessori daycare tuition spikes 35% this semester. To avoid depleting your family safety cushion, you are tempted to take night freelance contracts from 9 PM to 1 AM, sacrificing all rest and intimate partner connection.',
            oracleAdvice: '"Chronic maternal sleep deprivation collapses mitochondrial health. Seek cooperative family childcare sharing before trading sleep for currency."',
            choices: {
              a: { text: 'Form Neighborhood Co-Op Childcare Pod: Partner with 3 trusted local mothers to rotate weekday afternoons.', dMind: 5, dBody: 6, dSoul: 7, dCap: 9, log: 'Built neighborhood childcare pod. Saved $1,400/mo while deepening community bonds and children\'s friendships.' },
              b: { text: 'Grind Midnight Contracts: Work 20 extra hours weekly to preserve private school placement at all costs.', dMind: -9, dBody: -14, dSoul: -7, dCap: -8, log: 'Burnt the candle at both ends. Exhaustion triggered immune drop, but bank balance stayed green.' },
              c: { text: 'Simplify Household Living: Reallocate discretionary budget, cook communal family meals, protect rest.', dMind: 4, dBody: 5, dSoul: 8, dCap: 6, log: 'Simplified household expenses. Reduced financial stress and protected evening bedtime reading.' }
            }
          }
        ],
        married: [
          {
            category: 'DILEMMA // PARTNERSHIP RHYTHMS & MORTGAGE TENSION',
            title: 'Mortgage Inflation Rut vs. Honest Emotional Recalibration',
            narrative: 'Rising mortgage interest and dual corporate stress have turned your marriage into an administrative chore checklist. Communication is curt, and intimate connection has dwindled to silence.',
            oracleAdvice: '"Financial stress without emotional vulnerability creates chronic defensive armor. Prioritize honest, compassionate dialogue over transactional blame."',
            choices: {
              a: { text: 'Unplug Devices for Weekend Dialogue: Walk in nature, lay all financial fears on the table without blame.', dMind: 6, dBody: 5, dSoul: 9, dCap: 10, log: 'Shared vulnerable fears on quiet nature trail. Rebuilt profound marital trust and aligned long-term financial goals.' },
              b: { text: 'Suppress Emotions & Work Harder: Pour energy into overtime work, hoping higher savings will fix tension.', dMind: -6, dBody: -8, dSoul: -8, dCap: -6, log: 'Overworked to out-earn the mortgage. Material wealth grew, but emotional chasm widened.' },
              c: { text: 'Downsize or Restructure Liabilities: Mutually agree to sell excess assets, reducing monthly burn by $1,200.', dMind: 7, dBody: 4, dSoul: 7, dCap: 8, log: 'Restructured family balance sheet together. Reduced fixed overhead and rediscovered joy in simple shared moments.' }
            }
          },
          {
            category: 'DILEMMA // FAMILY BOUNDARIES & CONDITIONAL SUPPORT',
            title: 'Substantial In-Law Home Gift vs. Unspoken Control',
            narrative: 'Affluent in-laws offer a $150,000 cash gift toward a home purchase, but subtly expect weekly unannounced visits, holiday veto power, and parenting intervention.',
            oracleAdvice: '"Financial gifts with unstated sovereignty clauses cost more in emotional peace than their dollar value. United spousal consensus is your primary shield."',
            choices: {
              a: { text: 'United Spousal Stand: Gratefully accept on explicit, loving boundary terms agreed upon in advance.', dMind: 5, dBody: 3, dSoul: 8, dCap: 7, log: 'Set clear boundaries together. Established loving respect without sacrificing family autonomy.' },
              b: { text: 'Accept with Zero Boundaries: Prioritize luxury house now, endure private resentment during family visits.', dMind: -7, dBody: -5, dSoul: -9, dCap: -7, log: 'Accepted money without terms. Constant boundary violations sparked recurring spousal arguments.' },
              c: { text: 'Decline with Warmth: Buy modest home independently, preserve absolute peace and family sovereignty.', dMind: 6, dBody: 4, dSoul: 9, dCap: 9, log: 'Purchased smaller home independently. Savoring the priceless peace of unencumbered sovereign freedom.' }
            }
          }
        ],
        networks: [
          {
            category: 'DILEMMA // SOCIAL CAPITAL & TRUSTED FRIENDS',
            title: 'Old Friend Loan Request vs. Flashy Acquaintance Pitch',
            narrative: 'A loyal childhood friend faces medical hardship and asks for modest financial help. On the same day, a charismatic business acquaintance urges you to invest that same capital into a speculative crypto-syndicate.',
            oracleAdvice: '"Speculative hype dissipates; loyalty proven in a friend\'s valley yields generational relational trust. Always invest in human hearts over algorithmic promises."',
            choices: {
              a: { text: 'Direct Restitution to Friend: Gift the funds outright as a loving non-reciprocal contribution.', dMind: 4, dBody: 3, dSoul: 12, dCap: 10, log: 'Gifted emergency funds to loyal friend. Relational trust and 532nm soul resonance peaked.' },
              b: { text: 'Chase Speculative Syndicate: Put capital into high-risk acquaintance venture seeking quick 5x flip.', dMind: -8, dBody: -6, dSoul: -10, dCap: -8, log: 'Invested into speculative syndicate. Project stalled in volatility; friend felt abandoned.' },
              c: { text: 'Balance Support & Boundaries: Lend partial medical support, introduce friend to community mutual aid.', dMind: 5, dBody: 2, dSoul: 7, dCap: 7, log: 'Organized community mutual aid. Broadened social safety net while protecting personal emergency reserves.' }
            }
          }
        ]
      };

      // 7 Primary Chakras mapped along spinal meridian
      var chakraNodes = [
        { name: 'Root (Muladhara)', wl: '660nm', yRel: 0.82, col: '#ff1744', radius: 4.5 },
        { name: 'Sacral (Svadhisthana)', wl: '600nm', yRel: 0.72, col: '#ff9100', radius: 4.5 },
        { name: 'Solar Plexus (Manipura)', wl: '580nm', yRel: 0.62, col: '#ffc400', radius: 4.5 },
        { name: 'Heart (Anahata) ★', wl: '532nm', yRel: 0.48, col: '#00ff66', radius: 8.0, isHeart: true },
        { name: 'Throat (Vishuddha)', wl: '495nm', yRel: 0.36, col: '#00e5ff', radius: 5.0 },
        { name: 'Third Eye (Ajna)', wl: '440nm', yRel: 0.24, col: '#2979ff', radius: 5.0 },
        { name: 'Crown (Sahasrara)', wl: '410nm', yRel: 0.14, col: '#d500f9', radius: 6.0 }
      ];

      // Particle system for glowing aura & spinal flow
      var particles = [];
      for (var p = 0; p < 45; p++) {
        particles.push({
          x: (Math.random() - 0.5) * 160,
          y: Math.random() * 220,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -0.3 - Math.random() * 0.6,
          life: Math.random() * 100,
          maxLife: 100 + Math.random() * 60,
          size: 1 + Math.random() * 2.5
        });
      }

      function renderDigitalHuman() {
        requestAnimationFrame(renderDigitalHuman);
        animTime += 0.04;

        var w = canvas.width;
        var h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        var centerX = w * 0.5;
        var baseY = h * 0.88;
        var figureHeight = h * 0.76;

        // Background subtle grid
        ctx.strokeStyle = 'rgba(0, 255, 102, 0.04)';
        ctx.lineWidth = 1;
        for (var gx = 20; gx < w; gx += 30) {
          ctx.beginPath();
          ctx.moveTo(gx, 0);
          ctx.lineTo(gx, h);
          ctx.stroke();
        }

        // Draw Radiating Harmonic Aura
        var auraGrad = ctx.createRadialGradient(centerX, baseY - figureHeight * 0.52, 10, centerX, baseY - figureHeight * 0.52, 140 * auraIntensity);
        var pulse = 0.15 * Math.sin(animTime * 1.5);
        var baseAlpha = 0.12 + pulse;
        if (baseAlpha < 0.02) baseAlpha = 0.02;
        auraGrad.addColorStop(0, 'hsla(' + auraHue + ', 100%, 55%, ' + (baseAlpha * 1.8) + ')');
        auraGrad.addColorStop(0.5, 'hsla(' + auraHue + ', 85%, 45%, ' + baseAlpha + ')');
        auraGrad.addColorStop(1, 'hsla(' + auraHue + ', 70%, 30%, 0)');
        
        ctx.fillStyle = auraGrad;
        ctx.beginPath();
        ctx.arc(centerX, baseY - figureHeight * 0.52, 140 * auraIntensity, 0, Math.PI * 2);
        ctx.fill();

        // Aura Particles floating upward
        for (var pi = 0; pi < particles.length; pi++) {
          var pt = particles[pi];
          pt.x += pt.vx;
          pt.y += pt.vy;
          pt.life++;
          if (pt.life > pt.maxLife) {
            pt.x = (Math.random() - 0.5) * 80;
            pt.y = baseY - 20;
            pt.life = 0;
          }
          var pAlpha = (1 - pt.life / pt.maxLife) * 0.5;
          ctx.fillStyle = 'hsla(' + auraHue + ', 90%, 65%, ' + pAlpha + ')';
          ctx.beginPath();
          ctx.arc(centerX + pt.x, pt.y, pt.size, 0, Math.PI * 2);
          ctx.fill();
        }

        // Draw Luminous Biometric Human Wireframe
        ctx.save();
        ctx.strokeStyle = 'rgba(0, 229, 255, 0.6)';
        ctx.lineWidth = 1.5;
        ctx.shadowColor = '#00ff66';
        ctx.shadowBlur = 8;

        // Head ellipse
        var headY = baseY - figureHeight * 0.88;
        ctx.beginPath();
        ctx.ellipse(centerX, headY, 14, 18, 0, 0, Math.PI * 2);
        ctx.stroke();

        // Spine (central neural axis)
        var hipY = baseY - figureHeight * 0.22;
        ctx.beginPath();
        ctx.moveTo(centerX, headY + 18);
        ctx.lineTo(centerX, hipY);
        ctx.stroke();

        // Shoulders & Chest line
        var shoulderY = headY + 34;
        ctx.beginPath();
        ctx.moveTo(centerX - 36, shoulderY);
        ctx.lineTo(centerX + 36, shoulderY);
        ctx.stroke();

        // Arms & Hands
        var elbowY = shoulderY + 40;
        var handY = elbowY + 38;
        // Left arm
        ctx.beginPath();
        ctx.moveTo(centerX - 36, shoulderY);
        ctx.lineTo(centerX - 46, elbowY);
        ctx.lineTo(centerX - 38, handY);
        ctx.stroke();
        // Right arm
        ctx.beginPath();
        ctx.moveTo(centerX + 36, shoulderY);
        ctx.lineTo(centerX + 46, elbowY);
        ctx.lineTo(centerX + 38, handY);
        ctx.stroke();

        // Pelvis / Hip line
        ctx.beginPath();
        ctx.moveTo(centerX - 24, hipY);
        ctx.lineTo(centerX + 24, hipY);
        ctx.stroke();

        // Legs
        var kneeY = hipY + 54;
        var footY = baseY - 4;
        // Left leg
        ctx.beginPath();
        ctx.moveTo(centerX - 18, hipY);
        ctx.lineTo(centerX - 22, kneeY);
        ctx.lineTo(centerX - 24, footY);
        ctx.stroke();
        // Right leg
        ctx.beginPath();
        ctx.moveTo(centerX + 18, hipY);
        ctx.lineTo(centerX + 22, kneeY);
        ctx.lineTo(centerX + 24, footY);
        ctx.stroke();

        ctx.restore();

        // Draw 7 Chakras / 12 Harmonic Nodes
        for (var ci = 0; ci < chakraNodes.length; ci++) {
          var ch = chakraNodes[ci];
          var cy = headY + (hipY - headY) * ch.yRel;
          var cr = ch.radius;

          if (ch.isHeart) {
            // Heart Center (532nm Emerald Green) beats with dynamic pulse
            var heartPulse = 1.0 + 0.35 * Math.sin(animTime * 3.5);
            cr = ch.radius * heartPulse;

            // Heart glow ring
            ctx.strokeStyle = 'rgba(0, 255, 102, 0.4)';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.arc(centerX, cy, cr * 1.9, 0, Math.PI * 2);
            ctx.stroke();

            // ECG Heartbeat wave snippet
            ctx.strokeStyle = '#00ff66';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(centerX - 22, cy);
            ctx.lineTo(centerX - 8, cy);
            ctx.lineTo(centerX - 4, cy - 6);
            ctx.lineTo(centerX, cy + 8);
            ctx.lineTo(centerX + 4, cy - 10);
            ctx.lineTo(centerX + 8, cy);
            ctx.lineTo(centerX + 22, cy);
            ctx.stroke();
          }

          // Inner solid node
          ctx.fillStyle = ch.col;
          ctx.beginPath();
          ctx.arc(centerX, cy, cr, 0, Math.PI * 2);
          ctx.fill();

          // Outer shimmering ring
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.arc(centerX, cy, cr + 2, 0, Math.PI * 2);
          ctx.stroke();
        }
      }

      renderDigitalHuman();

      // UI Sync Helpers
      function syncDilemmaCardUI() {
        var dilemmas = personaDilemmas[currentPersona];
        if (!dilemmas) return;
        var d = dilemmas[currentCycleIdx % dilemmas.length];
        if (!d) return;

        var catEl = document.getElementById('dilemma-category-badge');
        var cycEl = document.getElementById('dilemma-cycle-badge');
        var titEl = document.getElementById('dilemma-title');
        var narEl = document.getElementById('dilemma-narrative');
        var advEl = document.getElementById('ai-oracle-advice');
        var chAEl = document.getElementById('choice-a-text');
        var chBEl = document.getElementById('choice-b-text');
        var chCEl = document.getElementById('choice-c-text');

        if (catEl) catEl.innerText = d.category;
        if (cycEl) cycEl.innerText = 'CYCLE: 0' + ((currentCycleIdx % dilemmas.length) + 1) + ' / 0' + dilemmas.length;
        if (titEl) titEl.innerText = d.title;
        if (narEl) narEl.innerText = d.narrative;
        if (advEl) advEl.innerHTML = d.oracleAdvice;
        if (chAEl) chAEl.innerText = d.choices.a.text;
        if (chBEl) chBEl.innerText = d.choices.b.text;
        if (chCEl) chCEl.innerText = d.choices.c.text;
      }

      // Persona Tab Buttons
      var personaBtns = document.querySelectorAll('.persona-btn');
      personaBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          personaBtns.forEach(function(b) {
            b.classList.remove('active');
            b.style.background = 'rgba(5,15,25,0.7)';
            b.style.borderColor = 'rgba(0,229,255,0.3)';
            b.style.color = '#8ce4a7';
          });
          btn.classList.add('active');
          btn.style.background = 'rgba(0,255,102,0.15)';
          btn.style.borderColor = '#00ff66';
          btn.style.color = '#ffffff';

          currentPersona = btn.getAttribute('data-persona');
          currentCycleIdx = 0;
          syncDilemmaCardUI();

          var stream = document.getElementById('choice-consequence-stream');
          if (stream) {
            stream.innerText = '⟦ SYSTEM ⟧ Switched perspective to ' + currentPersona.replace('_', ' ').toUpperCase() + '. AI Co-Pilot recalibrated.';
          }
        });
      });

      // Interactive Choice Buttons Handler
      var choiceBtns = document.querySelectorAll('.dilemma-choice-btn');
      choiceBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          var choiceKey = btn.getAttribute('data-choice');
          var dilemmas = personaDilemmas[currentPersona];
          if (!dilemmas) return;
          var d = dilemmas[currentCycleIdx % dilemmas.length];
          if (!d) return;
          var outcome = d.choices[choiceKey];
          if (!outcome) return;

          // Visual biometric reactions
          if (choiceKey === 'a') {
            auraHue = 140; // Emerald Green 532nm
            auraIntensity = 1.35;
            stressLevel = Math.max(10, stressLevel - 8);
            heartCoherence = Math.min(99.4, heartCoherence + 4.2);
          } else if (choiceKey === 'b') {
            auraHue = 25; // Amber/Red
            auraIntensity = 0.85;
            stressLevel = Math.min(85, stressLevel + 18);
            heartCoherence = Math.max(55.0, heartCoherence - 14.5);
          } else if (choiceKey === 'c') {
            auraHue = 190; // Cyan/Blue
            auraIntensity = 1.15;
            stressLevel = Math.max(12, stressLevel - 4);
            heartCoherence = Math.min(96.0, heartCoherence + 2.5);
          }

          // Telemetry HUD updates
          var auraStat = document.getElementById('human-aura-status');
          var stressVal = document.getElementById('human-stress-val');
          if (auraStat) {
            if (choiceKey === 'a') auraStat.innerHTML = '<span style="color:#00ff66;">98.2% [532nm LOCK]</span>';
            if (choiceKey === 'b') auraStat.innerHTML = '<span style="color:#ffaa00;">64.5% [STRAIN WARNING]</span>';
            if (choiceKey === 'c') auraStat.innerHTML = '<span style="color:#00e5ff;">92.0% [SOVEREIGN HARMONY]</span>';
          }
          if (stressVal) {
            stressVal.innerText = stressLevel + '% (' + (stressLevel > 40 ? 'ELEVATED' : 'LOW') + ')';
            stressVal.style.color = stressLevel > 40 ? '#ff5555' : '#00ff66';
          }

          // Log stream update
          var stream = document.getElementById('choice-consequence-stream');
          if (stream) {
            stream.innerHTML = '<strong>⟦ CHOICE LOG ⟧</strong> ' + outcome.log;
          }

          // Recalculate Screen B Soul Calculator!
          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(outcome.dMind, outcome.dBody, outcome.dSoul, outcome.dCap);
          }

          // Advance to next cycle
          currentCycleIdx++;
          setTimeout(syncDilemmaCardUI, 1200);
        });
      });

      // Initial sync
      syncDilemmaCardUI();
    })();


    // PART B: THE ENTIRE SOUL CALCULATOR ENGINE
    (function initSoulCalculatorEngine() {
      var gaugeCanvas = document.getElementById('soul-gauge-canvas');
      if (!gaugeCanvas) return;
      var gCtx = gaugeCanvas.getContext('2d');
      if (!gCtx) return;

      var pillars = {
        mind: 86,
        body: 82,
        soul: 94,
        capital: 89
      };

      var rxMultiplier = 1.0; // 20/20 default
      var currentWavelength = 532; // 532nm Emerald Green anchor

      function computeMasterSoulScore() {
        var geometricMean = Math.pow(pillars.mind * pillars.body * pillars.soul * pillars.capital, 0.25);
        var wlOffset = Math.abs(currentWavelength - 532);
        var wlPenalty = 1.0 - (wlOffset / 650.0);
        var finalScore = Math.round(geometricMean * wlPenalty * rxMultiplier);
        if (finalScore > 100) finalScore = 100;
        if (finalScore < 0) finalScore = 0;
        return finalScore;
      }

      function drawSoulGauge() {
        var score = computeMasterSoulScore();
        var w = gaugeCanvas.width;
        var h = gaugeCanvas.height;
        gCtx.clearRect(0, 0, w, h);

        var cx = w * 0.5;
        var cy = h * 0.5;
        var r = 110;

        // Background track ring
        gCtx.lineWidth = 14;
        gCtx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        gCtx.beginPath();
        gCtx.arc(cx, cy, r, 0.75 * Math.PI, 2.25 * Math.PI);
        gCtx.stroke();

        // Active glowing progress arc
        var endAngle = 0.75 * Math.PI + (score / 100.0) * (1.5 * Math.PI);
        var grad = gCtx.createLinearGradient(0, h, w, 0);
        grad.addColorStop(0, '#00e5ff');
        grad.addColorStop(0.5, '#00ff66');
        grad.addColorStop(1, '#d500f9');

        gCtx.strokeStyle = grad;
        gCtx.lineWidth = 14;
        gCtx.lineCap = 'round';
        gCtx.shadowColor = '#00ff66';
        gCtx.shadowBlur = 12;
        gCtx.beginPath();
        gCtx.arc(cx, cy, r, 0.75 * Math.PI, endAngle);
        gCtx.stroke();
        gCtx.shadowBlur = 0;

        // Update percent and status text in HTML
        var pctEl = document.getElementById('master-soul-percent');
        var statEl = document.getElementById('master-soul-status');
        if (pctEl) pctEl.innerText = score + '%';
        if (statEl) {
          if (score >= 90) {
            statEl.innerHTML = '<span style="color:#00ff66;">★ 532nm TRANSCENDENT EQUILIBRIUM</span>';
          } else if (score >= 75) {
            statEl.innerHTML = '<span style="color:#00e5ff;">532nm GREEN COMMONS COHERENCE</span>';
          } else {
            statEl.innerHTML = '<span style="color:#ffaa00;">RECALIBRATION REQUIRED</span>';
          }
        }
      }

      function syncPillarsUI() {
        var valMind = document.getElementById('val-pillar-mind');
        var barMind = document.getElementById('bar-pillar-mind');
        var valBody = document.getElementById('val-pillar-body');
        var barBody = document.getElementById('bar-pillar-body');
        var valSoul = document.getElementById('val-pillar-soul');
        var barSoul = document.getElementById('bar-pillar-soul');
        var valCap = document.getElementById('val-pillar-capital');
        var barCap = document.getElementById('bar-pillar-capital');

        if (valMind) valMind.innerText = pillars.mind + '%';
        if (barMind) barMind.style.width = pillars.mind + '%';
        if (valBody) valBody.innerText = pillars.body + '%';
        if (barBody) barBody.style.width = pillars.body + '%';
        if (valSoul) valSoul.innerText = pillars.soul + '%';
        if (barSoul) barSoul.style.width = pillars.soul + '%';
        if (valCap) valCap.innerText = pillars.capital + '%';
        if (barCap) barCap.style.width = pillars.capital + '%';

        drawSoulGauge();
      }

      // Global hook for Screen A decisions to adjust Screen B Soul Calculator
      window.adjustSoulCalculator = function(dM, dB, dS, dC) {
        pillars.mind = Math.min(100, Math.max(10, pillars.mind + dM));
        pillars.body = Math.min(100, Math.max(10, pillars.body + dB));
        pillars.soul = Math.min(100, Math.max(10, pillars.soul + dS));
        pillars.capital = Math.min(100, Math.max(10, pillars.capital + dC));
        syncPillarsUI();
      };

      // Connect Sliders
      var sFocus = document.getElementById('slider-focus');
      var sTrust = document.getElementById('slider-trust');
      var sGreen = document.getElementById('slider-green');
      var sTime = document.getElementById('slider-time');

      if (sFocus) {
        sFocus.addEventListener('input', function() {
          var val = parseInt(sFocus.value, 10);
          var lbl = document.getElementById('slider-focus-val');
          if (lbl) lbl.innerText = val + '%';
          pillars.mind = val;
          syncPillarsUI();
        });
      }

      if (sTrust) {
        sTrust.addEventListener('input', function() {
          var val = parseInt(sTrust.value, 10);
          var lbl = document.getElementById('slider-trust-val');
          if (lbl) lbl.innerText = val + '%';
          pillars.capital = val;
          syncPillarsUI();
        });
      }

      if (sGreen) {
        sGreen.addEventListener('input', function() {
          var val = parseInt(sGreen.value, 10);
          var lbl = document.getElementById('slider-green-val');
          if (lbl) lbl.innerText = val + '%';
          pillars.soul = val;
          syncPillarsUI();
        });
      }

      if (sTime) {
        sTime.addEventListener('input', function() {
          var val = parseInt(sTime.value, 10);
          var lbl = document.getElementById('slider-time-val');
          if (lbl) lbl.innerText = val + '%';
          pillars.body = val;
          syncPillarsUI();
        });
      }

      // Recalibrate Button
      var recalBtn = document.getElementById('btn-recalibrate-soul');
      if (recalBtn) {
        recalBtn.addEventListener('click', function() {
          pillars.mind = 92;
          pillars.body = 88;
          pillars.soul = 98;
          pillars.capital = 94;
          currentWavelength = 532;
          if (sFocus) sFocus.value = 92;
          if (sTrust) sTrust.value = 94;
          if (sGreen) sGreen.value = 98;
          if (sTime) sTime.value = 88;
          var lF = document.getElementById('slider-focus-val'); if (lF) lF.innerText = '92%';
          var lT = document.getElementById('slider-trust-val'); if (lT) lT.innerText = '94%';
          var lG = document.getElementById('slider-green-val'); if (lG) lG.innerText = '98%';
          var lTi = document.getElementById('slider-time-val'); if (lTi) lTi.innerText = '88%';
          syncPillarsUI();
        });
      }

      // Reset Button
      var resetBtn = document.getElementById('btn-reset-soul');
      if (resetBtn) {
        resetBtn.addEventListener('click', function() {
          pillars.mind = 80;
          pillars.body = 75;
          pillars.soul = 85;
          pillars.capital = 80;
          syncPillarsUI();
        });
      }

      // Hook prescription choice from Step 02
      var rxButtons = document.querySelectorAll('.rx-btn');
      rxButtons.forEach(function(rb) {
        rb.addEventListener('click', function() {
          var rx = rb.getAttribute('data-rx');
          var rxBadge = document.getElementById('soul-rx-factor');
          if (rx === '20/10') {
            rxMultiplier = 1.05;
            if (rxBadge) rxBadge.innerText = '20/10 [HYPER-CLARITY +5%]';
          } else if (rx === '20/200') {
            rxMultiplier = 0.92;
            if (rxBadge) rxBadge.innerText = '20/200 [ADAPTIVE SOFT FILTER]';
          } else {
            rxMultiplier = 1.0;
            if (rxBadge) rxBadge.innerText = '20/20 [OPTIMAL]';
          }
          drawSoulGauge();
        });
      });

      // Initial Render
      syncPillarsUI();
    })();


    // PART C: BONUS SHADERTOY 3D WORLD-SHADING & ENLIGHTENMENT SANDBOX ENGINE
    (function initShadertoyBonusStudio() {
      var canvas = document.getElementById('shadertoy-world-canvas');
      if (!canvas) return;

      var currentMode = 'sphere_3d'; // 'sphere_3d', 'euler_waves', 'hyper_warp', 'voronoi_net'
      var currentWavelength = 532;   // 532nm Emerald Green center
      var eulerPhase = 1.57;          // pi / 2
      var dimensionWarp = 3.2;        // 3.2D
      var waveFreq = 8.0;             // 8 Hz
      var rotSpeed = 1.2;
      var rotAngleY = 0;
      var rotAngleX = 0.2;
      var isDragging = false;
      var lastMouseX = 0;
      var lastMouseY = 0;
      var animTime = 0;

      // 12-Color Spectral Table
      var spectralTable = {
        660: [255, 23, 68],
        630: [255, 87, 34],
        600: [255, 145, 0],
        580: [255, 196, 0],
        560: [198, 255, 0],
        532: [0, 255, 102], // Emerald Green center
        515: [0, 230, 118],
        495: [0, 229, 255],
        470: [41, 121, 255],
        440: [101, 31, 255],
        420: [213, 0, 249],
        410: [255, 64, 129]
      };

      // Mouse drag rotation handlers
      canvas.addEventListener('mousedown', function(e) {
        isDragging = true;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
        canvas.style.cursor = 'grabbing';
      });

      window.addEventListener('mouseup', function() {
        isDragging = false;
        canvas.style.cursor = 'grab';
      });

      window.addEventListener('mousemove', function(e) {
        if (!isDragging) return;
        var dx = e.clientX - lastMouseX;
        var dy = e.clientY - lastMouseY;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
        rotAngleY += dx * 0.008;
        rotAngleX += dy * 0.008;
      });

      // High Performance Canvas 2D Procedural Raytracer & Dimensional Modeler
      var ctx = canvas.getContext('2d');
      if (!ctx) return;

      function renderShaderWorld() {
        requestAnimationFrame(renderShaderWorld);
        animTime += 0.02 * rotSpeed;
        rotAngleY += 0.005 * rotSpeed;

        var w = canvas.width;
        var h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        var cx = w * 0.5;
        var cy = h * 0.5;
        var sphereRadius = Math.min(w, h) * 0.36;

        // Space Void Background with dynamic starfield
        ctx.fillStyle = '#010408';
        ctx.fillRect(0, 0, w, h);

        // Get RGB for active wavelength
        var activeRgb = [0, 255, 102];
        if (currentWavelength === 'rainbow') {
          var hue = (animTime * 40) % 360;
          activeRgb = [
            Math.round(128 + 127 * Math.sin(animTime)),
            Math.round(128 + 127 * Math.sin(animTime + 2.09)),
            Math.round(128 + 127 * Math.sin(animTime + 4.18))
          ];
        } else if (currentWavelength === 'monochrome') {
          activeRgb = [240, 245, 255];
        } else if (spectralTable[currentWavelength]) {
          activeRgb = spectralTable[currentWavelength];
        }

        var rgbStr = activeRgb[0] + ', ' + activeRgb[1] + ', ' + activeRgb[2];

        // Atmospheric Exterior Phototherapy Corona Glow
        var coronaGrad = ctx.createRadialGradient(cx, cy, sphereRadius * 0.85, cx, cy, sphereRadius * 1.55);
        coronaGrad.addColorStop(0, 'rgba(' + rgbStr + ', 0.35)');
        coronaGrad.addColorStop(0.6, 'rgba(' + rgbStr + ', 0.12)');
        coronaGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = coronaGrad;
        ctx.beginPath();
        ctx.arc(cx, cy, sphereRadius * 1.55, 0, Math.PI * 2);
        ctx.fill();

        // 3D Sphere Base & Illumination
        var sphereGrad = ctx.createRadialGradient(cx - sphereRadius * 0.3, cy - sphereRadius * 0.3, sphereRadius * 0.1, cx, cy, sphereRadius);
        sphereGrad.addColorStop(0, 'rgba(' + Math.min(255, activeRgb[0] + 80) + ', ' + Math.min(255, activeRgb[1] + 80) + ', ' + Math.min(255, activeRgb[2] + 80) + ', 0.95)');
        sphereGrad.addColorStop(0.5, 'rgba(' + activeRgb[0] + ', ' + activeRgb[1] + ', ' + activeRgb[2] + ', 0.75)');
        sphereGrad.addColorStop(0.85, 'rgba(' + Math.floor(activeRgb[0] * 0.4) + ', ' + Math.floor(activeRgb[1] * 0.4) + ', ' + Math.floor(activeRgb[2] * 0.4) + ', 0.85)');
        sphereGrad.addColorStop(1, '#02060c');

        ctx.save();
        ctx.beginPath();
        ctx.arc(cx, cy, sphereRadius, 0, Math.PI * 2);
        ctx.clip();

        // Fill Base Shaded Sphere
        ctx.fillStyle = sphereGrad;
        ctx.fillRect(cx - sphereRadius, cy - sphereRadius, sphereRadius * 2, sphereRadius * 2);

        // MODE 1: 3D EARTH & ROTATING LATITUDE/LONGITUDE BANDS
        if (currentMode === 'sphere_3d') {
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
          ctx.lineWidth = 1;

          // Parallels of latitude
          for (var lat = -60; lat <= 60; lat += 20) {
            var latRad = (lat * Math.PI) / 180;
            var latY = cy + Math.sin(latRad) * sphereRadius * Math.cos(rotAngleX);
            var latRx = Math.cos(latRad) * sphereRadius;
            var latRy = latRx * 0.32 * Math.sin(rotAngleX);

            ctx.beginPath();
            ctx.ellipse(cx, latY, latRx, Math.abs(latRy) + 1, 0, 0, Math.PI * 2);
            ctx.stroke();
          }

          // Meridians of longitude rotating around Y axis
          for (var lon = 0; lon < 12; lon++) {
            var lonAngle = rotAngleY + (lon * Math.PI) / 6;
            var lonWidth = Math.cos(lonAngle) * sphereRadius;
            ctx.strokeStyle = lon % 2 === 0 ? 'rgba(' + rgbStr + ', 0.45)' : 'rgba(255, 255, 255, 0.15)';
            ctx.beginPath();
            ctx.ellipse(cx, cy, Math.abs(lonWidth), sphereRadius, 0, 0, Math.PI * 2);
            ctx.stroke();
          }

          // Continent / Energy Hotspots
          for (var spot = 0; spot < 8; spot++) {
            var sAngle = rotAngleY * 1.5 + spot * 0.8;
            var sx = cx + Math.cos(sAngle) * sphereRadius * 0.7;
            var sy = cy + Math.sin(sAngle * 0.7) * sphereRadius * 0.5;
            ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
            ctx.beginPath();
            ctx.arc(sx, sy, 3.5, 0, Math.PI * 2);
            ctx.fill();
          }
        }

        // MODE 2: EULER STANDING WAVES (e^{i*theta} = cos + i*sin)
        if (currentMode === 'euler_waves') {
          ctx.lineWidth = 2;
          for (var ring = 1; ring <= 14; ring++) {
            var rNorm = ring / 14.0;
            var rPixels = rNorm * sphereRadius;
            // Standing wave equation: sin(eulerPhase + r * waveFreq)
            var standingAmp = Math.sin(eulerPhase + rNorm * waveFreq - animTime * 2.0);
            var ringAlpha = Math.abs(standingAmp);
            ctx.strokeStyle = 'rgba(' + rgbStr + ', ' + (0.15 + ringAlpha * 0.7) + ')';
            ctx.beginPath();
            ctx.arc(cx, cy, rPixels * (1.0 + standingAmp * 0.08), 0, Math.PI * 2);
            ctx.stroke();
          }
        }

        // MODE 3: 4D HYPER-WARP (Klein Fold Projection)
        if (currentMode === 'hyper_warp') {
          ctx.lineWidth = 1.5;
          var warpPower = dimensionWarp - 2.0; // 1.2 to 2.5
          for (var hf = 0; hf < 16; hf++) {
            var hAngle = rotAngleY + (hf * Math.PI) / 8;
            var hRadius = sphereRadius * Math.pow((hf + 1) / 16.0, 1.0 / warpPower);
            ctx.strokeStyle = 'rgba(' + rgbStr + ', ' + (0.2 + 0.05 * hf) + ')';
            ctx.beginPath();
            ctx.ellipse(cx, cy, hRadius, hRadius * 0.45 * Math.sin(hAngle), hAngle, 0, Math.PI * 2);
            ctx.stroke();
          }
        }

        // MODE 4: VORONOI CONSCIOUSNESS MESH
        if (currentMode === 'voronoi_net') {
          ctx.strokeStyle = 'rgba(' + rgbStr + ', 0.4)';
          ctx.lineWidth = 1.2;
          var vNodes = [];
          for (var vn = 0; vn < 24; vn++) {
            var vTheta = vn * 0.785 + rotAngleY;
            var vDist = sphereRadius * (0.25 + 0.65 * Math.sin(vn * 1.3));
            vNodes.push({
              x: cx + Math.cos(vTheta) * vDist,
              y: cy + Math.sin(vTheta) * vDist * Math.cos(rotAngleX)
            });
          }
          // Connect nearby nodes
          for (var i = 0; i < vNodes.length; i++) {
            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(vNodes[i].x, vNodes[i].y, 2.5, 0, Math.PI * 2);
            ctx.fill();
            for (var j = i + 1; j < vNodes.length; j++) {
              var distSq = Math.pow(vNodes[i].x - vNodes[j].x, 2) + Math.pow(vNodes[i].y - vNodes[j].y, 2);
              if (distSq < 11000) {
                ctx.beginPath();
                ctx.moveTo(vNodes[i].x, vNodes[i].y);
                ctx.lineTo(vNodes[j].x, vNodes[j].y);
                ctx.stroke();
              }
            }
          }
        }

        ctx.restore();

        // Outer Keplerian Photon Orbit Ring with trailing photon blast
        ctx.strokeStyle = 'rgba(' + rgbStr + ', 0.5)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.ellipse(cx, cy, sphereRadius * 1.32, sphereRadius * 0.42, 0.35, 0, Math.PI * 2);
        ctx.stroke();

        // Orbiting photon beacon
        var orbAngle = animTime * 2.5;
        var ox = cx + Math.cos(orbAngle) * sphereRadius * 1.32 * Math.cos(0.35) - Math.sin(orbAngle) * sphereRadius * 0.42 * Math.sin(0.35);
        var oy = cy + Math.cos(orbAngle) * sphereRadius * 1.32 * Math.sin(0.35) + Math.sin(orbAngle) * sphereRadius * 0.42 * Math.cos(0.35);

        ctx.fillStyle = '#ffffff';
        ctx.shadowColor = 'rgb(' + rgbStr + ')';
        ctx.shadowBlur = 15;
        ctx.beginPath();
        ctx.arc(ox, oy, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }

      renderShaderWorld();

      // Hook Mode Tab Buttons
      var modeBtns = document.querySelectorAll('.shader-dim-btn');
      modeBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          modeBtns.forEach(function(b) {
            b.classList.remove('active');
            b.style.background = 'rgba(0,229,255,0.15)';
            b.style.borderColor = 'rgba(0,229,255,0.4)';
            b.style.color = '#00e5ff';
          });
          btn.classList.add('active');
          btn.style.background = '#00ff66';
          btn.style.color = '#030912';

          currentMode = btn.getAttribute('data-mode');

          var dimHud = document.getElementById('telemetry-dim-factor');
          if (dimHud) {
            if (currentMode === 'sphere_3d') dimHud.innerText = '3.0D SPHERICAL GEOMETRY';
            if (currentMode === 'euler_waves') dimHud.innerText = 'e^{iθ} STANDING RESONATOR';
            if (currentMode === 'hyper_warp') dimHud.innerText = dimensionWarp + 'D HYPER-SURFACE';
            if (currentMode === 'voronoi_net') dimHud.innerText = 'CONSCIOUSNESS MESH';
          }
        });
      });

      // Hook 12-Color Spectral Swatches
      var swatchBtns = document.querySelectorAll('.shader-swatch-btn');
      swatchBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          swatchBtns.forEach(function(b) {
            b.classList.remove('active');
            b.style.border = '1px solid rgba(255,255,255,0.3)';
            b.style.boxShadow = 'none';
          });
          btn.classList.add('active');
          btn.style.border = '2px solid #ffffff';
          btn.style.boxShadow = '0 0 10px #00ff66';

          var wl = btn.getAttribute('data-wl');
          if (wl === 'rainbow' || wl === 'monochrome') {
            currentWavelength = wl;
          } else {
            currentWavelength = parseInt(wl, 10);
          }

          var wlDisplay = document.getElementById('active-shader-wl-display');
          var photoHud = document.getElementById('telemetry-phototherapy-state');
          if (wlDisplay) {
            if (currentWavelength === 532) {
              wlDisplay.innerHTML = 'ACTIVE: <span style="color:#00ff66;">532nm EMERALD GREEN (CENTER OF EQUILIBRIUM ★)</span>';
            } else if (currentWavelength === 'rainbow') {
              wlDisplay.innerHTML = 'ACTIVE: <span style="color:#00e5ff;">FULL 12-COLOR CONTINUUM DISPERSION</span>';
            } else if (currentWavelength === 'monochrome') {
              wlDisplay.innerHTML = 'ACTIVE: <span style="color:#ffffff;">WHITE / DARK LUMINANCE POLARITY</span>';
            } else {
              wlDisplay.innerHTML = 'ACTIVE: <span style="color:#00e5ff;">' + currentWavelength + 'nm SPECTRAL LAYER</span>';
            }
          }
          if (photoHud) {
            if (currentWavelength === 532) {
              photoHud.innerHTML = '<span style="color:#00ff66;">532nm LOCK [ACTIVE]</span>';
            } else {
              photoHud.innerHTML = '<span style="color:#ffaa00;">MODULATING (' + currentWavelength + 'nm)</span>';
            }
          }
        });
      });

      // Hook Mathematical Sliders
      var sEuler = document.getElementById('slider-shader-euler');
      var sWarp = document.getElementById('slider-shader-warp');
      var sFreq = document.getElementById('slider-shader-freq');
      var sRot = document.getElementById('slider-shader-rot');

      if (sEuler) {
        sEuler.addEventListener('input', function() {
          eulerPhase = (parseInt(sEuler.value, 10) / 100.0);
          var lbl = document.getElementById('slider-shader-euler-val');
          var thHud = document.getElementById('telemetry-euler-phase');
          if (lbl) lbl.innerText = eulerPhase.toFixed(2) + ' rad';
          if (thHud) thHud.innerText = 'θ = ' + eulerPhase.toFixed(3) + ' rad';
        });
      }

      if (sWarp) {
        sWarp.addEventListener('input', function() {
          dimensionWarp = (parseInt(sWarp.value, 10) / 10.0);
          var lbl = document.getElementById('slider-shader-warp-val');
          var dmHud = document.getElementById('telemetry-dim-factor');
          if (lbl) lbl.innerText = dimensionWarp.toFixed(2) + 'D';
          if (dmHud) dmHud.innerText = dimensionWarp.toFixed(2) + 'D HYPER-SURFACE';
        });
      }

      if (sFreq) {
        sFreq.addEventListener('input', function() {
          waveFreq = parseInt(sFreq.value, 10);
          var lbl = document.getElementById('slider-shader-freq-val');
          if (lbl) lbl.innerText = waveFreq.toFixed(1) + ' Hz';
        });
      }

      if (sRot) {
        sRot.addEventListener('input', function() {
          rotSpeed = (parseInt(sRot.value, 10) / 10.0);
          var lbl = document.getElementById('slider-shader-rot-val');
          if (lbl) lbl.innerText = rotSpeed.toFixed(1) + 'x';
        });
      }

      // Presets
      var presetBtns = document.querySelectorAll('.shader-preset-btn');
      presetBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          var preset = btn.getAttribute('data-preset');
          if (preset === 'emerald_earth') {
            currentMode = 'sphere_3d';
            currentWavelength = 532;
            waveFreq = 8.0;
            dimensionWarp = 3.0;
          } else if (preset === 'euler_quantum') {
            currentMode = 'euler_waves';
            currentWavelength = 495;
            eulerPhase = 3.14;
            waveFreq = 16.0;
          } else if (preset === 'hyper_klein') {
            currentMode = 'hyper_warp';
            currentWavelength = 420;
            dimensionWarp = 4.2;
            waveFreq = 12.0;
          } else if (preset === 'rainbow_prism') {
            currentMode = 'sphere_3d';
            currentWavelength = 'rainbow';
            rotSpeed = 1.8;
          }

          // Trigger UI button sync
          var sw = document.querySelector('.shader-swatch-btn[data-wl="' + currentWavelength + '"]');
          if (sw) sw.click();
          var mb = document.querySelector('.shader-dim-btn[data-mode="' + currentMode + '"]');
          if (mb) mb.click();
        });
      });

      // Toggle GLSL Code Drawer
      var codeToggleBtn = document.getElementById('btn-toggle-shader-code');
      var codeDrawer = document.getElementById('shader-code-drawer');
      if (codeToggleBtn) {
        if (codeDrawer) {
          codeToggleBtn.addEventListener('click', function() {
            var isHidden = codeDrawer.style.display === 'none';
            codeDrawer.style.display = isHidden ? 'block' : 'none';
            codeToggleBtn.innerText = isHidden ? '✕ HIDE GLSL SOURCE' : '</> VIEW GLSL MATHEMATICAL SOURCE';
          });
        }
      }

    })();
'''

# Check for existing initDigitalHumanSimulator to avoid duplicates
if 'initDigitalHumanSimulator' in home:
    print("WARNING: initDigitalHumanSimulator already present in homepage.html! Skipping duplicate injection.")
else:
    # Target location: right before `// END SPECTRUM MONOPOLY GAME ENGINE`
    pattern = r'(\s*// END SPECTRUM MONOPOLY GAME ENGINE)'
    match = re.search(pattern, home)
    if not match:
        print("ERROR: Could not find `// END SPECTRUM MONOPOLY GAME ENGINE` in homepage.html!")
        exit(1)
    
    print("Found insertion point before `// END SPECTRUM MONOPOLY GAME ENGINE`.")
    home = home[:match.start()] + '\n' + JS_ENGINES + '\n' + home[match.start():]

# Strict check for WordPress entity safety: zero raw '&&' inside <script> tags
print("Performing strict WordPress entity safety verification (checking for raw '&&')...")
script_blocks = re.findall(r'<script[\s\S]*?</script>', home)
raw_amp_found = False
for i, sb in enumerate(script_blocks):
    if '&&' in sb:
        print(f"CRITICAL ERROR: Found raw '&&' in script block {i}!")
        # Print lines around the error
        lines = sb.split('\n')
        for line in lines:
            if '&&' in line:
                print(f"  Line: {line.strip()}")
        raw_amp_found = True

if raw_amp_found:
    print("Aborting write due to raw '&&' in script tags.")
    exit(1)

print("SUCCESS: 0 raw '&&' found in all script blocks! Safe for WordPress.")

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print(f"Saved updated homepage.html. Final size: {len(home)} characters.")
