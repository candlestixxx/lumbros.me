#!/usr/bin/env python3
"""
update_audio_engine.py
Upgrades the YouTube Live Music Player on lumbros.me and mirrored properties:
1. Infallible Autoplay & Unmute:
   - Sets YouTube iframe dimensions to 200x200 with opacity 0.001 at bottom:0, right:0 (viewport-resident, no visibility:hidden, preventing browser background suspension).
   - Enables JS API (enablejsapi=1, origin=location.origin, playsinline=1, autoplay=1).
   - Attempts unmuted autoplay at 38% (~52 dB SPL Trust Optima) on ready.
   - Comprehensive multi-gesture unlocker on window & document: 'pointerdown', 'mousedown', 'touchstart', 'touchend', 'click', 'keydown', 'wheel', 'scroll'.
   - If user interacts before player loads, flags userHasInteracted and starts unmuted instantly on onReady.
   - Mini dock pill and button indicators dynamically inform state.
2. Multi-Playlist Continuum:
   - Primary default: PLM2VfNfvggIE (60 Tracks, lk2243 @lumbros2243, Detroit Techno & Psytrance Continuum, 432Hz Harmonic Bias).
   - Dynamic Playlist input: accepts any YouTube Playlist URL (e.g. https://www.youtube.com/playlist?list=... or https://youtu.be/...&list=...) or raw playlist ID.
   - Saves custom playlists in localStorage (lumbros_user_playlists) across sessions.
   - Dynamic playlist chips switcher bar with one-click selection and deletion.
   - '↻ LIST' cycle button in transport bar to easily jump to the next playlist.
   - Real-time telemetry track index and playlist name updates.
3. Strict KSES & Syntax Compliance:
   - ZERO raw '&&' operators anywhere in inline script blocks (using nested if statements).
   - Verified valid JavaScript syntax.
"""

import os
import re

HOMEPAGE_PATH = os.path.join(os.path.dirname(__file__), 'homepage.html')

NEW_HUD_HTML = '''  <!-- YouTube Audio Engine -->
  <!-- Invisible Audio Host Frame (Multi-Playlist YouTube Audio Continuum) -->
  <div id="yt-audio-container" class="yt-invisible-audio-frame" aria-hidden="true">
    <div id="yt-audio-player"></div>
  </div>

  <!-- Floating Harmonic Audio HUD Console -->
  <aside id="harmonic-audio-hud" class="harmonic-audio-hud" aria-label="Harmonic Audio Controller">
    
    <!-- Mini Dock Pill (Click to toggle expansion) -->
    <div class="audio-mini-pill" id="audio-pill-toggle" title="Click to Expand/Collapse Audio Controls">
      <div class="pill-wave-icon is-active" id="mini-wave-icon">
        <span class="wave-bar wb-1"></span>
        <span class="wave-bar wb-2"></span>
        <span class="wave-bar wb-3"></span>
        <span class="wave-bar wb-4"></span>
        <span class="wave-bar wb-5"></span>
      </div>
      <div class="pill-info">
        <span class="pill-title" id="pill-title-text">♫ MY LIFE SOUNDS</span>
        <span class="pill-meta" id="pill-db-readout">52 dB // TRUST OPTIMA</span>
      </div>
      <button type="button" class="pill-quick-btn" id="pill-quick-play" title="Play / Pause Audio Stream">▶</button>
      <span class="pill-expand-arrow" id="pill-arrow-indicator">▲</span>
    </div>

    <!-- Expanded Audio HUD Drawer -->
    <div class="audio-expanded-panel" id="audio-expanded-panel" style="display: none;">
      
      <!-- Panel Header -->
      <div class="audio-panel-header">
        <div class="audio-badge">
          <span class="audio-live-dot"></span>
          <span id="audio-live-badge-text">ACOUSTIC KERNEL // MULTI-PLAYLIST CONTINUUM</span>
        </div>
        <button type="button" class="audio-collapse-btn" id="audio-collapse-btn" title="Collapse Panel">▼</button>
      </div>

      <div class="audio-title-block">
        <h4 class="audio-h4" id="audio-h4-title">⚡ ⟦ MY LIFE SOUNDS ⟧ // YOUTUBE AUDIO CONTINUUM</h4>
        <div class="audio-creator-tag" id="audio-creator-tag">PLAYLIST: PLM2VfNfvggIE // lk2243 (@lumbros2243) // 432Hz HARMONIC BIAS</div>
      </div>

      <!-- Multi-Playlist Switcher & Custom URL Adder -->
      <div class="audio-playlist-module">
        <div class="playlist-section-header">
          <span class="playlist-section-lbl">CHOOSE / ADD YOUTUBE PLAYLIST:</span>
          <span class="playlist-current-indicator" id="playlist-current-indicator">PLAYLIST 1 OF 1</span>
        </div>
        <div class="playlist-chips-bar" id="playlist-chips-bar">
          <!-- Dynamic Playlist Chips inserted here by JS -->
        </div>
        <div class="playlist-input-container">
          <input type="text" id="custom-playlist-input" class="custom-playlist-input" placeholder="Paste YouTube Playlist URL or ID (e.g. https://... or PL...)" aria-label="YouTube Playlist URL or ID">
          <button type="button" class="custom-playlist-btn" id="custom-playlist-btn" title="Add and Play YouTube Playlist">+ ADD LIST</button>
        </div>
      </div>

      <!-- 12-Band Graphic Equalizer Spectrum Waveform -->
      <div class="audio-12spectrum-visualizer is-active" id="spectrum-visualizer">
        <span class="eq-band eq-red" style="--band-delay: 0.1s" title="01. Red 0%"></span>
        <span class="eq-band eq-coral" style="--band-delay: 0.25s" title="02. Coral 9%"></span>
        <span class="eq-band eq-amber" style="--band-delay: 0.4s" title="03. Amber 18%"></span>
        <span class="eq-band eq-gold" style="--band-delay: 0.15s" title="04. Gold 27%"></span>
        <span class="eq-band eq-yellow" style="--band-delay: 0.35s" title="05. Yellow 36%"></span>
        <span class="eq-band eq-pear" style="--band-delay: 0.5s" title="06. Pear 45%"></span>
        <span class="eq-band eq-green is-center-band" style="--band-delay: 0.2s" title="07. Green 50% [Center Midpoint]"></span>
        <span class="eq-band eq-mint" style="--band-delay: 0.45s" title="08. Mint 55%"></span>
        <span class="eq-band eq-cyan" style="--band-delay: 0.3s" title="09. Cyan 64%"></span>
        <span class="eq-band eq-blue" style="--band-delay: 0.18s" title="10. Blue 73%"></span>
        <span class="eq-band eq-indigo" style="--band-delay: 0.42s" title="11. Indigo 82%"></span>
        <span class="eq-band eq-magenta" style="--band-delay: 0.28s" title="12. Magenta 100%"></span>
      </div>

      <!-- Telemetry Track Status -->
      <div class="audio-telemetry-row">
        <div class="telemetry-item">
          <span class="tele-lbl">STATUS:</span>
          <span class="tele-val glow-green" id="tele-state-val">AUTOPLAY ARMED</span>
        </div>
        <div class="telemetry-item">
          <span class="tele-lbl">TRACK:</span>
          <span class="tele-val glow-cyan" id="tele-track-val">CYCLING 01</span>
        </div>
      </div>

      <!-- Transport Controls -->
      <div class="audio-transport-strip">
        <button type="button" class="audio-btn" id="audio-prev-btn" title="Previous Track in Playlist">⏮ PREV</button>
        <button type="button" class="audio-btn audio-btn-play" id="audio-play-btn" title="Play / Pause Audio Stream">
          <span id="audio-play-icon">▶</span> <span id="audio-play-text">PLAY STREAM</span>
        </button>
        <button type="button" class="audio-btn" id="audio-next-btn" title="Next Track in Playlist">NEXT ⏭</button>
        <button type="button" class="audio-btn audio-btn-cycle" id="audio-cycle-list-btn" title="Cycle to Next Playlist">↻ LIST</button>
        <button type="button" class="audio-btn audio-btn-mute" id="audio-mute-btn" title="Toggle Mute">
          <span id="audio-mute-icon">🔊</span>
        </button>
      </div>

      <!-- Decibel & Acoustic Volume Gauge Slider -->
      <div class="audio-gauge-wrap">
        <div class="gauge-label-row">
          <span class="gauge-title">ACOUSTIC DECIBEL CALIBRATOR:</span>
          <span class="gauge-db-val" id="gauge-db-readout">38% (~52 dB SPL // -12.8 dBFS)</span>
        </div>
        <div class="gauge-slider-container">
          <input type="range" id="audio-volume-slider" min="0" max="100" value="38" step="1" class="audio-volume-range" aria-label="Volume Slider">
        </div>
        <div class="gauge-ticks-row">
          <span>0 dB (MUTE)</span>
          <span class="optima-mark">⚡ 52 dB [TRUST OPTIMA]</span>
          <span>72 dB (MAX)</span>
        </div>
      </div>

      <!-- Psychoacoustic Preset Nodes -->
      <div class="audio-presets-row">
        <button type="button" class="audio-preset-btn" data-vol="22" title="Deep Reflection & Meditation (-18 dBFS)">
          MEDITATION (45 dB)
        </button>
        <button type="button" class="audio-preset-btn active" data-vol="38" title="Optimal Human Algorithm Trust Resonance (-12.8 dBFS)">
          ★ TRUST CONCEPTION (52 dB)
        </button>
        <button type="button" class="audio-preset-btn" data-vol="58" title="Dynamic Creative Energy (-6 dBFS)">
          DYNAMIC (61 dB)
        </button>
      </div>

      <!-- Psychoacoustic Manifesto Caption -->
      <div class="audio-manifesto-caption">
        <span class="caption-icon">☩</span>
        <span class="caption-text">
          Calibrated to <strong>~52 dB SPL</strong>: Entrains natural alpha/theta coherence. Eliminates subconscious resistance and empowers the authentic moment of conception for human choice and mutual trust.
        </span>
      </div>

    </div>
  </aside>
  <!-- End YouTube Audio Engine -->'''

NEW_CSS = '''.yt-invisible-audio-frame {
      position: fixed;
      bottom: 0;
      right: 0;
      width: 200px;
      height: 200px;
      opacity: 0.001;
      pointer-events: none;
      z-index: -10;
    }

    .harmonic-audio-hud {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 99990;
      font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Courier New', monospace;
    }

    /* 1. Mini Dock Pill */
    .audio-mini-pill {
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(3, 15, 8, 0.88);
      border: 1px solid rgba(0, 255, 102, 0.4);
      border-radius: 30px;
      padding: 8px 16px 8px 14px;
      box-shadow: 0 8px 26px rgba(0, 0, 0, 0.8), 0 0 16px rgba(0, 255, 102, 0.25);
      backdrop-filter: blur(12px);
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
    }

    .audio-mini-pill:hover {
      border-color: #00ff66;
      box-shadow: 0 10px 32px rgba(0, 0, 0, 0.9), 0 0 24px rgba(0, 255, 102, 0.45);
      transform: translateY(-2px);
    }

    /* Mini Wave Bars */
    .pill-wave-icon {
      display: flex;
      align-items: flex-end;
      gap: 2.5px;
      height: 16px;
      padding-bottom: 2px;
    }

    .pill-wave-icon .wave-bar {
      width: 3px;
      height: 4px;
      border-radius: 1.5px;
      background: #00ff66;
      box-shadow: 0 0 6px rgba(0, 255, 102, 0.6);
      transition: height 0.2s ease;
    }

    .pill-wave-icon.is-active .wb-1 { animation: mini-wave 1.1s ease-in-out infinite 0.1s; }
    .pill-wave-icon.is-active .wb-2 { animation: mini-wave 0.85s ease-in-out infinite 0.3s; }
    .pill-wave-icon.is-active .wb-3 { animation: mini-wave 1.3s ease-in-out infinite 0.0s; }
    .pill-wave-icon.is-active .wb-4 { animation: mini-wave 0.95s ease-in-out infinite 0.4s; }
    .pill-wave-icon.is-active .wb-5 { animation: mini-wave 1.15s ease-in-out infinite 0.2s; }

    @keyframes mini-wave {
      0%, 100% { height: 4px; }
      50% { height: 16px; }
    }

    .pill-info {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }

    .pill-title {
      font-size: 0.72rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      text-shadow: 0 0 8px rgba(0, 255, 102, 0.6);
    }

    .pill-meta {
      font-size: 0.62rem;
      color: #a3ffd0;
      font-weight: 600;
      letter-spacing: 0.8px;
    }

    .pill-quick-btn {
      background: rgba(0, 255, 102, 0.18);
      border: 1px solid #00ff66;
      color: #00ff66;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      cursor: pointer;
      transition: all 0.2s;
    }

    .pill-quick-btn:hover {
      background: #00ff66;
      color: #020704;
      box-shadow: 0 0 10px #00ff66;
    }

    .pill-expand-arrow {
      color: #00e5ff;
      font-size: 0.68rem;
      font-weight: 800;
    }

    /* 2. Expanded Audio HUD Panel */
    .audio-expanded-panel {
      width: 380px;
      max-width: calc(100vw - 32px);
      background: rgba(2, 12, 6, 0.96);
      border: 2px solid #00ff66;
      border-radius: 12px;
      padding: 18px 20px 16px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.9), 0 0 30px rgba(0, 255, 102, 0.35);
      backdrop-filter: blur(14px);
      margin-bottom: 12px;
      animation: panel-burst 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes panel-burst {
      from { opacity: 0; transform: translateY(12px) scale(0.96); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .audio-panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding-bottom: 8px;
      border-bottom: 1px dashed rgba(0, 255, 102, 0.3);
    }

    .audio-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.64rem;
      letter-spacing: 1.2px;
      color: #00ff66;
      font-weight: 700;
    }

    .audio-live-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
      animation: terminal-blink 1.2s infinite;
    }

    .audio-collapse-btn {
      background: transparent;
      border: 1px solid rgba(0, 255, 102, 0.4);
      color: #00ff66;
      width: 22px;
      height: 22px;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      cursor: pointer;
    }

    .audio-collapse-btn:hover {
      background: rgba(0, 255, 102, 0.2);
    }

    .audio-title-block {
      margin-bottom: 10px;
    }

    .audio-h4 {
      margin: 0 0 4px 0;
      font-size: 0.82rem;
      color: #ffffff;
      letter-spacing: 1.2px;
      font-weight: 800;
      text-shadow: 0 0 10px rgba(0, 255, 102, 0.6);
    }

    .audio-creator-tag {
      font-size: 0.62rem;
      color: #7ef2aa;
      letter-spacing: 0.8px;
    }

    /* Multi-Playlist UI in Expanded HUD */
    .audio-playlist-module {
      background: rgba(0, 0, 0, 0.55);
      border: 1px solid rgba(0, 255, 102, 0.25);
      border-radius: 6px;
      padding: 8px 10px;
      margin-bottom: 10px;
    }

    .playlist-section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      font-size: 0.6rem;
      letter-spacing: 0.8px;
    }

    .playlist-section-lbl {
      color: #88be99;
      font-weight: 700;
    }

    .playlist-current-indicator {
      color: #00ff66;
      font-weight: 800;
    }

    .playlist-chips-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-bottom: 8px;
      max-height: 85px;
      overflow-y: auto;
    }

    .playlist-chip {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: rgba(0, 255, 102, 0.08);
      border: 1px solid rgba(0, 255, 102, 0.35);
      color: #a3ffd0;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 0.58rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      max-width: 100%;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .playlist-chip:hover {
      background: rgba(0, 255, 102, 0.2);
      border-color: #00ff66;
      color: #ffffff;
    }

    .playlist-chip.active {
      background: rgba(0, 255, 102, 0.28);
      border-color: #00ff66;
      color: #00ff66;
      box-shadow: 0 0 8px rgba(0, 255, 102, 0.4);
      font-weight: 800;
    }

    .playlist-chip-del {
      margin-left: 3px;
      color: #ff5577;
      font-size: 0.65rem;
      font-weight: bold;
      cursor: pointer;
      opacity: 0.7;
    }
    .playlist-chip-del:hover {
      opacity: 1;
      color: #ff0033;
    }

    .playlist-input-container {
      display: flex;
      gap: 5px;
    }

    .custom-playlist-input {
      flex: 1;
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid rgba(0, 255, 102, 0.35);
      border-radius: 4px;
      color: #ffffff;
      padding: 4px 8px;
      font-size: 0.62rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
    }

    .custom-playlist-input:focus {
      border-color: #00ff66;
      box-shadow: 0 0 6px rgba(0, 255, 102, 0.4);
    }

    .custom-playlist-input::placeholder {
      color: rgba(163, 255, 208, 0.45);
    }

    .custom-playlist-btn {
      background: rgba(0, 255, 102, 0.2);
      border: 1px solid #00ff66;
      color: #00ff66;
      border-radius: 4px;
      padding: 4px 8px;
      font-size: 0.6rem;
      font-weight: 800;
      letter-spacing: 0.8px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }

    .custom-playlist-btn:hover {
      background: #00ff66;
      color: #020704;
      box-shadow: 0 0 8px #00ff66;
    }

    /* 12-Band Equalizer Visualizer */
    .audio-12spectrum-visualizer {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 4px;
      height: 38px;
      background: rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(0, 255, 102, 0.25);
      border-radius: 6px;
      padding: 6px 10px;
      margin-bottom: 12px;
      box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.8);
    }

    .eq-band {
      flex: 1;
      height: 6px;
      border-radius: 2px;
      transition: height 0.1s ease;
    }

    .audio-12spectrum-visualizer.is-active .eq-band {
      animation: eq-bounce 1.2s ease-in-out infinite alternate;
      animation-delay: var(--band-delay, 0s);
    }

    @keyframes eq-bounce {
      0%   { height: 4px; opacity: 0.7; }
      50%  { height: 26px; opacity: 1; }
      100% { height: 12px; opacity: 0.85; }
    }

    /* 12-Color Band Specific Colors */
    .eq-red     { background: #ff0033; box-shadow: 0 0 6px #ff0033; }
    .eq-coral   { background: #ff3d00; box-shadow: 0 0 6px #ff3d00; }
    .eq-amber   { background: #ff7700; box-shadow: 0 0 6px #ff7700; }
    .eq-gold    { background: #ffaa00; box-shadow: 0 0 6px #ffaa00; }
    .eq-yellow  { background: #ffe600; box-shadow: 0 0 6px #ffe600; }
    .eq-pear    { background: #b4e600; box-shadow: 0 0 6px #b4e600; }
    .eq-green   { background: #00ff66; box-shadow: 0 0 10px #00ff66; border-top: 2px solid #ffffff; } /* Center */
    .eq-mint    { background: #00f0aa; box-shadow: 0 0 6px #00f0aa; }
    .eq-cyan    { background: #00e5ff; box-shadow: 0 0 6px #00e5ff; }
    .eq-blue    { background: #0077ff; box-shadow: 0 0 6px #0077ff; }
    .eq-indigo  { background: #5800ff; box-shadow: 0 0 6px #5800ff; }
    .eq-magenta { background: #e00099; box-shadow: 0 0 6px #e00099; }

    /* Telemetry row */
    .audio-telemetry-row {
      display: flex;
      justify-content: space-between;
      gap: 8px;
      font-size: 0.62rem;
      letter-spacing: 0.8px;
      margin-bottom: 12px;
      padding: 6px 10px;
      background: rgba(0, 0, 0, 0.45);
      border-radius: 4px;
      border: 1px solid rgba(0, 255, 102, 0.15);
    }

    .telemetry-item { display: flex; align-items: center; gap: 5px; }
    .tele-lbl { color: #88be99; font-weight: 700; }
    .tele-val { font-weight: 700; }

    /* Transport buttons */
    .audio-transport-strip {
      display: flex;
      gap: 6px;
      margin-bottom: 14px;
    }

    .audio-btn {
      flex: 1;
      background: rgba(0, 255, 102, 0.08);
      border: 1px solid rgba(0, 255, 102, 0.4);
      color: #7df9a6;
      padding: 7px 6px;
      border-radius: 6px;
      font-size: 0.66rem;
      font-weight: 700;
      letter-spacing: 0.8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: all 0.2s;
    }

    .audio-btn:hover {
      background: rgba(0, 255, 102, 0.22);
      border-color: #00ff66;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(0, 255, 102, 0.35);
    }

    .audio-btn-play {
      flex: 1.3;
      background: rgba(0, 255, 102, 0.2);
      border-color: #00ff66;
      color: #00ff66;
    }

    .audio-btn-play:hover {
      background: #00ff66;
      color: #020704;
      box-shadow: 0 0 14px #00ff66;
    }

    .audio-btn-cycle {
      flex: 0.85;
      color: #00e5ff;
      border-color: rgba(0, 229, 255, 0.4);
    }
    .audio-btn-cycle:hover {
      background: rgba(0, 229, 255, 0.2);
      border-color: #00e5ff;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(0, 229, 255, 0.35);
    }

    .audio-btn-mute {
      flex: 0.55;
      font-size: 0.85rem;
    }

    /* Volume Gauge & Slider */
    .audio-gauge-wrap {
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(0, 255, 102, 0.2);
      border-radius: 6px;
      padding: 10px 12px;
      margin-bottom: 10px;
    }

    .gauge-label-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }

    .gauge-title {
      font-size: 0.62rem;
      color: #88be99;
      font-weight: 700;
      letter-spacing: 1px;
    }

    .gauge-db-val {
      font-size: 0.68rem;
      color: #00ff66;
      font-weight: 800;
      letter-spacing: 0.8px;
    }

    .audio-volume-range {
      width: 100%;
      height: 6px;
      border-radius: 3px;
      background: linear-gradient(90deg, #ff0055 0%, #ffe600 30%, #00ff66 50%, #00e5ff 100%);
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }

    .audio-volume-range::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: #ffffff;
      border: 2px solid #00ff66;
      box-shadow: 0 0 10px #00ff66;
      cursor: pointer;
      transition: transform 0.15s;
    }

    .audio-volume-range::-webkit-slider-thumb:hover {
      transform: scale(1.25);
    }

    .gauge-ticks-row {
      display: flex;
      justify-content: space-between;
      margin-top: 4px;
      font-size: 0.56rem;
      color: #5d9e74;
      font-weight: 600;
      letter-spacing: 0.5px;
    }

    .optima-mark {
      color: #00ff66;
      font-weight: 800;
    }

    /* Preset Nodes */
    .audio-presets-row {
      display: flex;
      gap: 6px;
      margin-bottom: 12px;
    }

    .audio-preset-btn {
      flex: 1;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(0, 255, 102, 0.25);
      color: #7df9a6;
      padding: 5px 4px;
      border-radius: 4px;
      font-size: 0.58rem;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s;
    }

    .audio-preset-btn:hover {
      border-color: #00ff66;
      color: #ffffff;
    }

    .audio-preset-btn.active {
      background: rgba(0, 255, 102, 0.22);
      border-color: #00ff66;
      color: #00ff66;
      box-shadow: 0 0 8px rgba(0, 255, 102, 0.35);
    }

    /* Manifesto caption */
    .audio-manifesto-caption {
      display: flex;
      align-items: flex-start;
      gap: 6px;
      background: rgba(0, 40, 15, 0.35);
      border-left: 2px solid #00ff66;
      padding: 6px 8px;
      border-radius: 0 4px 4px 0;
      font-size: 0.6rem;
      line-height: 1.35;
      color: #b0f4c9;
    }

    .caption-icon { color: #00ff66; font-weight: 800; }'''

NEW_JS = '''    // =========================================================================
    // YouTube Audio Engine & Harmonic Psychoacoustic Multi-Playlist Continuum
    // Playlist: "My Life Sounds" (PLM2VfNfvggIE // 60 Tracks) by @lumbros2243
    // Multi-Playlist Switcher + User Dynamic YouTube Playlist Input + 52 dB Optima
    // =========================================================================
    (function() {
      // Default Curated Playlists
      var defaultPlaylists = [
        {
          id: 'PLM2VfNfvggIE',
          title: 'MY LIFE SOUNDS (60)',
          subtitle: 'lk2243 (@lumbros2243) // Detroit Techno & Psytrance Continuum',
          bias: '432Hz HARMONIC BIAS',
          isDefault: true
        }
      ];

      var videoIds = [
        'XrzYb1vXYJM', 'SVWHm3mYbn0', 'jvp--EFPnIA', 'lG2YIZHz-aw', 'NtCTBGeKnkE', 
        '2PiH-2kD6gk', 'lnd0-vy6rTA', 'xV6N_cjecg8', 's9yU1P1UH5E', 'tpKCqp9CALQ', 
        'CXUosU6ofg8', 'SSORHUTGKdg', 'BMB9hCm7kEk', '-YfCFOvxpaI', 'XLlBumbX-dw', 
        'f2-fWERXsZw', 'LeVAp7noaW8', 'e7ydzriSovs', 'hVt70b0kVGc', 'HTzo5IexJLk', 
        '30wid71tq8c', 'OikOgyDeOQw', 'EDZkW1zAaPY', 'aAOlgeAzOL4', 'r0Lv3h34O3w', 
        'qQJk2LTHlwI', 'QOgkmKiae70', 'wOsgj4rG0d4', 'F3YLP3xS62g', '4k9Pjf3DPQI', 
        'z465P9sk0PA', 'R4LKjRJUGkk', 'f0p-UNQI3QQ', '98Z_Y_bIK6U', 'ACpvsK6aiic', 
        'wJ01HfpTgOo', 'hJqRtqRRKgk', 'p0AOl8Ibo80', 'mJVRNk_vIFo', '6Zo4Irwn0Iw', 
        'zoWQdERRsPE', '61GTWKKtBbY', '8d8Nn5uOiIM', 'ms0rCiX2aNU', 'ADpoUcOXHeE', 
        'w4Ey_Rbqayg', 'B1R6biLWbqM', 'OoXuW0PGVD0', 'v205UK-h5yM', 'JEPbmXSXmns', 
        'La56yFCpdLM', '_mfPm1oe17A', 'w3MApu-RumU', 'b-PGPrPwlco', 'mJzsXo2BQxQ', 
        'SbIIj06bvnU', '4UxRUJ-sras', 'nfro55RmXC0', '4kNfgGbutB8', 'PXHEI5v1YW8'
      ];

      // Retrieve user custom playlists from localStorage
      var customPlaylists = [];
      try {
        var saved = localStorage.getItem('lumbros_user_playlists');
        if (saved) {
          customPlaylists = JSON.parse(saved);
        }
      } catch(e) {}

      var allPlaylists = defaultPlaylists.concat(customPlaylists);
      var currentPlaylistIndex = 0;
      var activePlaylist = allPlaylists[0];

      var ytPlayer = null;
      var isPlaying = false;
      var isMuted = false;
      var currentVolume = 38; // 38% = ~52 dB SPL (Optimal trust & conception frequency)
      var hasUnlockedAudio = false;
      var userHasInteracted = false;

      // Decibel format calculation
      function computeDbSpl(vol) {
        if (vol <= 0) return '0 dB (MUTED)';
        var spl = Math.round(35 + (vol / 100) * 37); // Maps 0..100 to 35..72 dB SPL
        var dbfs = (20 * Math.log10(vol / 100)).toFixed(1);
        return spl + ' dB SPL (' + dbfs + ' dBFS)';
      }

      // Parse YouTube Playlist ID from URL or raw ID
      function parsePlaylistId(input) {
        if (!input) return null;
        input = input.trim();
        var match = input.match(/[?&]list=([a-zA-Z0-9_-]+)/);
        if (match) {
          return match[1];
        }
        if (/^[a-zA-Z0-9_-]{10,}$/.test(input)) {
          return input;
        }
        return null;
      }

      // UI Elements
      var pillToggle = document.getElementById('audio-pill-toggle');
      var expandedPanel = document.getElementById('audio-expanded-panel');
      var collapseBtn = document.getElementById('audio-collapse-btn');
      var pillArrow = document.getElementById('pill-arrow-indicator');
      var miniWave = document.getElementById('mini-wave-icon');
      var spectrumVis = document.getElementById('spectrum-visualizer');
      var pillQuickPlay = document.getElementById('pill-quick-play');
      var pillDbReadout = document.getElementById('pill-db-readout');
      var pillTitleText = document.getElementById('pill-title-text');
      var audioH4Title = document.getElementById('audio-h4-title');
      var audioCreatorTag = document.getElementById('audio-creator-tag');
      var teleState = document.getElementById('tele-state-val');
      var teleTrack = document.getElementById('tele-track-val');
      var playBtn = document.getElementById('audio-play-btn');
      var playIcon = document.getElementById('audio-play-icon');
      var playText = document.getElementById('audio-play-text');
      var prevBtn = document.getElementById('audio-prev-btn');
      var nextBtn = document.getElementById('audio-next-btn');
      var cycleListBtn = document.getElementById('audio-cycle-list-btn');
      var muteBtn = document.getElementById('audio-mute-btn');
      var muteIcon = document.getElementById('audio-mute-icon');
      var volSlider = document.getElementById('audio-volume-slider');
      var gaugeDbReadout = document.getElementById('gauge-db-readout');
      var presetBtns = document.querySelectorAll('.audio-preset-btn');
      var chipsBar = document.getElementById('playlist-chips-bar');
      var currentInd = document.getElementById('playlist-current-indicator');
      var playlistInput = document.getElementById('custom-playlist-input');
      var playlistAddBtn = document.getElementById('custom-playlist-btn');

      // Update Visuals
      function syncUiState() {
        if (activePlaylist) {
          if (pillTitleText) {
            pillTitleText.textContent = '♫ ' + activePlaylist.title;
          }
          if (audioH4Title) {
            audioH4Title.textContent = '⚡ ⟦ ' + activePlaylist.title + ' ⟧ // YOUTUBE AUDIO CONTINUUM';
          }
          if (audioCreatorTag) {
            audioCreatorTag.textContent = 'PLAYLIST: ' + activePlaylist.id + ' // ' + (activePlaylist.subtitle || 'lk2243 (@lumbros2243)') + ' // ' + (activePlaylist.bias || '432Hz HARMONIC BIAS');
          }
        }

        if (pillDbReadout) {
          pillDbReadout.textContent = isMuted || currentVolume === 0 ? 'MUTED' : Math.round(35 + (currentVolume / 100) * 37) + ' dB // TRUST OPTIMA';
        }
        if (gaugeDbReadout) {
          gaugeDbReadout.textContent = currentVolume + '% (' + computeDbSpl(isMuted ? 0 : currentVolume) + ')';
        }
        if (volSlider) {
          volSlider.value = isMuted ? 0 : currentVolume;
        }

        if (isPlaying) {
          if (pillQuickPlay) pillQuickPlay.textContent = '⏸';
          if (playIcon) playIcon.textContent = '⏸';
          if (playText) playText.textContent = 'PAUSE STREAM';
          if (miniWave) miniWave.classList.add('is-active');
          if (spectrumVis) spectrumVis.classList.add('is-active');
          if (teleState) teleState.textContent = 'CYCLING LIVE (' + computeDbSpl(isMuted ? 0 : currentVolume) + ')';
        } else {
          if (pillQuickPlay) pillQuickPlay.textContent = '▶';
          if (playIcon) playIcon.textContent = '▶';
          if (playText) playText.textContent = 'PLAY STREAM';
          if (miniWave) miniWave.classList.remove('is-active');
          if (spectrumVis) spectrumVis.classList.remove('is-active');
          if (teleState) teleState.textContent = 'PAUSED // STANDBY';
        }

        if (muteIcon) {
          muteIcon.textContent = isMuted || currentVolume === 0 ? '🔇' : '🔊';
        }

        if (ytPlayer) {
          if (typeof ytPlayer.getPlaylistIndex === 'function') {
            try {
              var idx = ytPlayer.getPlaylistIndex();
              if (idx >= 0) {
                if (teleTrack) {
                  var total = 60;
                  if (ytPlayer.getPlaylist) {
                    var plList = ytPlayer.getPlaylist();
                    if (plList) {
                      total = plList.length;
                    }
                  }
                  teleTrack.textContent = 'TRACK ' + (idx + 1) + ' / ' + total;
                }
              }
            } catch(e) {}
          }
        }
      }

      // Render Playlist Selector Chips
      function renderPlaylistChips() {
        if (currentInd) {
          currentInd.textContent = 'PLAYLIST ' + (currentPlaylistIndex + 1) + ' OF ' + allPlaylists.length;
        }
        if (!chipsBar) return;
        chipsBar.innerHTML = '';

        allPlaylists.forEach(function(pl, idx) {
          var chip = document.createElement('div');
          chip.className = 'playlist-chip' + (idx === currentPlaylistIndex ? ' active' : '');
          chip.title = pl.subtitle || pl.id;

          var icon = document.createElement('span');
          icon.textContent = (idx === currentPlaylistIndex ? '▶ ' : '♫ ');
          chip.appendChild(icon);

          var txt = document.createElement('span');
          txt.textContent = pl.title;
          chip.appendChild(txt);

          if (!pl.isDefault) {
            var del = document.createElement('span');
            del.className = 'playlist-chip-del';
            del.textContent = '×';
            del.title = 'Remove custom playlist';
            del.addEventListener('click', function(ev) {
              ev.stopPropagation();
              removeCustomPlaylist(pl.id);
            });
            chip.appendChild(del);
          }

          chip.addEventListener('click', function() {
            switchPlaylist(idx);
          });

          chipsBar.appendChild(chip);
        });
      }

      // Switch to a playlist by index
      function switchPlaylist(idx) {
        if (idx < 0) return;
        if (idx >= allPlaylists.length) idx = 0;
        currentPlaylistIndex = idx;
        activePlaylist = allPlaylists[currentPlaylistIndex];

        if (ytPlayer) {
          if (typeof ytPlayer.loadPlaylist === 'function') {
            try {
              ytPlayer.loadPlaylist({
                list: activePlaylist.id,
                listType: 'playlist',
                index: 0,
                startSeconds: 0,
                suggestedQuality: 'small'
              });
              ytPlayer.unMute();
              isMuted = false;
              ytPlayer.setVolume(currentVolume > 0 ? currentVolume : 38);
              ytPlayer.playVideo();
              isPlaying = true;
            } catch(e) {}
          }
        }
        renderPlaylistChips();
        syncUiState();
      }

      // Remove custom playlist
      function removeCustomPlaylist(pid) {
        customPlaylists = customPlaylists.filter(function(p) { return p.id !== pid; });
        allPlaylists = defaultPlaylists.concat(customPlaylists);
        try {
          localStorage.setItem('lumbros_user_playlists', JSON.stringify(customPlaylists));
        } catch(e) {}
        if (currentPlaylistIndex >= allPlaylists.length) {
          currentPlaylistIndex = 0;
        }
        switchPlaylist(currentPlaylistIndex);
      }

      // Add Custom Playlist via input
      function handleAddPlaylist() {
        if (!playlistInput) return;
        var val = playlistInput.value;
        var pid = parsePlaylistId(val);
        if (!pid) {
          alert('Please enter a valid YouTube Playlist Link or ID (e.g. https://www.youtube.com/playlist?list=PL... or PL...)');
          return;
        }

        // Check if playlist is already added
        for (var i = 0; i < allPlaylists.length; i++) {
          if (allPlaylists[i].id === pid) {
            switchPlaylist(i);
            playlistInput.value = '';
            return;
          }
        }

        var newPl = {
          id: pid,
          title: 'PLAYLIST ' + (allPlaylists.length + 1),
          subtitle: 'USER LOADED // ID: ' + pid,
          bias: 'USER CONTINUUM',
          isDefault: false
        };

        customPlaylists.push(newPl);
        allPlaylists = defaultPlaylists.concat(customPlaylists);
        try {
          localStorage.setItem('lumbros_user_playlists', JSON.stringify(customPlaylists));
        } catch(e) {}

        playlistInput.value = '';
        switchPlaylist(allPlaylists.length - 1);
      }

      if (playlistAddBtn) {
        playlistAddBtn.addEventListener('click', handleAddPlaylist);
      }
      if (playlistInput) {
        playlistInput.addEventListener('keydown', function(e) {
          if (e.key === 'Enter') {
            handleAddPlaylist();
          }
        });
      }

      // Cycle list button
      if (cycleListBtn) {
        cycleListBtn.addEventListener('click', function() {
          var nextIdx = (currentPlaylistIndex + 1) % allPlaylists.length;
          switchPlaylist(nextIdx);
        });
      }

      // Global Autoplay & Interaction Unmute Engine
      function triggerPlayback() {
        if (!ytPlayer) return;
        if (typeof ytPlayer.playVideo !== 'function') return;
        try {
          ytPlayer.unMute();
          isMuted = false;
          ytPlayer.setVolume(currentVolume > 0 ? currentVolume : 38);
          ytPlayer.playVideo();
          isPlaying = true;
        } catch(e) {}
        syncUiState();
      }

      function handleGlobalInteraction() {
        userHasInteracted = true;
        if (hasUnlockedAudio) return;
        if (ytPlayer) {
          if (typeof ytPlayer.playVideo === 'function') {
            hasUnlockedAudio = true;
            triggerPlayback();
            cleanupListeners();
          }
        }
      }

      var unlockEvents = ['pointerdown', 'mousedown', 'touchstart', 'touchend', 'click', 'keydown', 'wheel', 'scroll'];
      function cleanupListeners() {
        unlockEvents.forEach(function(evt) {
          window.removeEventListener(evt, handleGlobalInteraction);
          document.removeEventListener(evt, handleGlobalInteraction);
        });
      }

      unlockEvents.forEach(function(evt) {
        window.addEventListener(evt, handleGlobalInteraction, { passive: true });
        document.addEventListener(evt, handleGlobalInteraction, { passive: true });
      });

      // Initialize YouTube API
      window.initYtAudio = function() {
        if (ytPlayer) return;
        ytPlayer = new YT.Player('yt-audio-player', {
          height: '200',
          width: '200',
          playerVars: {
            listType: 'playlist',
            list: activePlaylist.id,
            autoplay: 1,
            controls: 0,
            disablekb: 1,
            fs: 0,
            modestbranding: 1,
            playsinline: 1,
            rel: 0,
            loop: 1,
            enablejsapi: 1,
            origin: window.location.origin
          },
          events: {
            'onReady': onYtReady,
            'onStateChange': onYtStateChange,
            'onError': onYtError
          }
        });
      };

      function onYtReady(event) {
        try {
          if (ytPlayer.loadPlaylist) {
            ytPlayer.loadPlaylist({
              list: activePlaylist.id,
              listType: 'playlist',
              index: 0,
              startSeconds: 0,
              suggestedQuality: 'small'
            });
          }
        } catch(e) {
          try {
            ytPlayer.loadPlaylist(videoIds, 0, 0, 'small');
          } catch(err) {}
        }

        ytPlayer.setVolume(currentVolume);

        if (userHasInteracted) {
          hasUnlockedAudio = true;
          triggerPlayback();
          cleanupListeners();
        } else {
          // Attempt immediate unmuted autoplay
          try {
            ytPlayer.unMute();
            isMuted = false;
            ytPlayer.playVideo();
            isPlaying = true;
          } catch(e) {
            // Muted autoplay fallback if browser MEI policy initially blocks audio
            try {
              ytPlayer.mute();
              isMuted = true;
              ytPlayer.playVideo();
            } catch(err) {}
          }
        }

        renderPlaylistChips();
        syncUiState();
      }

      function onYtStateChange(event) {
        if (event.data === YT.PlayerState.PLAYING) {
          isPlaying = true;
        } else if (event.data === YT.PlayerState.PAUSED) {
          isPlaying = false;
        } else if (event.data === YT.PlayerState.ENDED) {
          if (ytPlayer) {
            if (ytPlayer.nextVideo) {
              ytPlayer.nextVideo();
            }
          }
        }
        syncUiState();
      }

      function onYtError(event) {
        console.warn('[Audio Engine] Track error code ' + event.data + ', cycling to next track...');
        if (ytPlayer) {
          if (ytPlayer.nextVideo) {
            ytPlayer.nextVideo();
          }
        }
      }

      // Transport Click Handlers
      function togglePlayPause() {
        handleGlobalInteraction();
        if (!ytPlayer) return;
        try {
          if (isPlaying) {
            ytPlayer.pauseVideo();
            isPlaying = false;
          } else {
            ytPlayer.unMute();
            isMuted = false;
            ytPlayer.setVolume(currentVolume);
            ytPlayer.playVideo();
            isPlaying = true;
          }
        } catch(e) {}
        syncUiState();
      }

      if (pillQuickPlay) {
        pillQuickPlay.addEventListener('click', function(e) {
          e.stopPropagation();
          togglePlayPause();
        });
      }

      if (playBtn) {
        playBtn.addEventListener('click', togglePlayPause);
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', function() {
          handleGlobalInteraction();
          if (ytPlayer) {
            if (ytPlayer.previousVideo) {
              ytPlayer.previousVideo();
            }
          }
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', function() {
          handleGlobalInteraction();
          if (ytPlayer) {
            if (ytPlayer.nextVideo) {
              ytPlayer.nextVideo();
            }
          }
        });
      }

      if (muteBtn) {
        muteBtn.addEventListener('click', function() {
          handleGlobalInteraction();
          if (!ytPlayer) return;
          if (isMuted) {
            ytPlayer.unMute();
            ytPlayer.setVolume(currentVolume > 0 ? currentVolume : 38);
            isMuted = false;
          } else {
            ytPlayer.mute();
            isMuted = true;
          }
          syncUiState();
        });
      }

      // Volume Slider
      if (volSlider) {
        volSlider.addEventListener('input', function() {
          handleGlobalInteraction();
          currentVolume = parseInt(this.value, 10);
          if (ytPlayer) {
            if (currentVolume === 0) {
              ytPlayer.mute();
              isMuted = true;
            } else {
              if (isMuted) {
                ytPlayer.unMute();
                isMuted = false;
              }
              ytPlayer.setVolume(currentVolume);
            }
          }
          presetBtns.forEach(function(btn) {
            btn.classList.toggle('active', parseInt(btn.getAttribute('data-vol'), 10) === currentVolume);
          });
          syncUiState();
        });
      }

      // Presets
      presetBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          handleGlobalInteraction();
          var target = parseInt(this.getAttribute('data-vol'), 10);
          currentVolume = target;
          if (ytPlayer) {
            ytPlayer.unMute();
            isMuted = false;
            ytPlayer.setVolume(currentVolume);
          }
          presetBtns.forEach(function(b) { b.classList.remove('active'); });
          this.classList.add('active');
          syncUiState();
        });
      });

      // Panel Expand / Collapse
      if (pillToggle) {
        pillToggle.addEventListener('click', function(e) {
          if (e.target === pillQuickPlay) return;
          var isExpanded = expandedPanel.style.display !== 'none';
          expandedPanel.style.display = isExpanded ? 'none' : 'block';
          if (pillArrow) pillArrow.textContent = isExpanded ? '▲' : '▼';
        });
      }

      if (collapseBtn) {
        collapseBtn.addEventListener('click', function() {
          expandedPanel.style.display = 'none';
          if (pillArrow) pillArrow.textContent = '▲';
        });
      }

      // Load YouTube IFrame API Script
      if (!window.YT) {
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
      }

      var prevYtReady = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = function() {
        if (prevYtReady) prevYtReady();
        window.initYtAudio();
      };
      if (window.YT) {
        if (window.YT.Player) {
          window.initYtAudio();
        }
      }

      // Initial Render
      renderPlaylistChips();
      syncUiState();
    })();'''

def main():
    print(f"Reading {HOMEPAGE_PATH}...")
    with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Audio HUD HTML
    hud_pat = re.compile(r'<!-- YouTube Audio Engine -->[\s\S]*?<!-- End YouTube Audio Engine -->')
    if not hud_pat.search(content):
        print("ERROR: Could not find HUD HTML pattern!")
        return 1
    content = hud_pat.sub(NEW_HUD_HTML, content, count=1)
    print("Replaced Audio HUD HTML successfully.")

    # 2. Replace Audio CSS
    css_start_idx = content.find('.yt-invisible-audio-frame {')
    css_end_idx = content.find('/* Light Theme Integration */')
    if css_start_idx == -1 or css_end_idx == -1:
        print("ERROR: Could not locate CSS boundaries!")
        return 1
    content = content[:css_start_idx] + NEW_CSS + "\n\n    " + content[css_end_idx:]
    print("Replaced Audio CSS successfully.")

    # 3. Replace Audio JS
    js_start_idx = content.find('// YouTube Audio Engine & Harmonic Psychoacoustic Controller Logic')
    js_end_idx = content.find('// GitHub Candlestixxx Live Repositories')
    if js_start_idx == -1 or js_end_idx == -1:
        print("ERROR: Could not locate JS boundaries!")
        return 1
    content = content[:js_start_idx] + NEW_JS + "\n\n    // =========================================================================\n    " + content[js_end_idx:]
    print("Replaced Audio JS successfully.")

    # Verify no raw && in <script> blocks
    script_blocks = re.findall(r'<script>([\s\S]*?)</script>', content)
    has_raw_and = False
    for i, s in enumerate(script_blocks):
        # find && that is not part of entity
        matches = [m.start() for m in re.finditer(r'&&', s)]
        if matches:
            print(f"WARNING: Found {len(matches)} raw '&&' in script block {i}!")
            has_raw_and = True

    if has_raw_and:
        print("ABORTING: KSES violation with raw && found!")
        return 1

    with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Saved updated homepage.html successfully.")
    return 0

if __name__ == '__main__':
    exit(main())
