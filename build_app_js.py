import json
import os

with open('exact_speech_translations.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

with open('audio_durations.json', 'r', encoding='utf-8') as f:
    durations = json.load(f)

translations_json_str = json.dumps(translations, ensure_ascii=False, indent=2)
durations_json_str = json.dumps(durations, ensure_ascii=False, indent=2)

app_js_content = f"""// Falcor HR Induction - Master Broadcast Presentation Controller
// Live Moving Subtitles Engine & Interactive Presenter Console
(function () {{
  const TOTAL_SLIDES = 21;
  let currentSlide = 1;
  let isPlaying = false;
  let isMuted = false;
  let activeCueIndex = -1;
  let animFrameId = null;

  // Embedded exact cue timestamps & 4-language translations
  const TRANSLATIONS = {translations_json_str};

  // Pre-calculated audio durations (seconds)
  const DURATIONS = {durations_json_str};

  // Audio Player Instance
  const audio = new Audio();
  audio.preload = "auto";

  // DOM Elements
  const subSpokenEn = document.getElementById('sub-spoken-en');
  const subLangAr = document.getElementById('sub-lang-ar');
  const subLangHi = document.getElementById('sub-lang-hi');
  const subLangTa = document.getElementById('sub-lang-ta');
  const subLangMl = document.getElementById('sub-lang-ml');
  const subTimecode = document.getElementById('sub-timecode');
  const subConsole = document.getElementById('broadcast-console');

  const btnPlayPause = document.getElementById('btn-play-pause');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnMute = document.getElementById('btn-mute');
  const scrubberWrap = document.getElementById('scrubber-wrap');
  const scrubberFill = document.getElementById('scrubber-fill');
  const scrubberHandle = document.getElementById('scrubber-handle');
  const slideCounter = document.getElementById('slide-counter');

  function formatTime(seconds) {{
    if (isNaN(seconds) || seconds < 0) seconds = 0;
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
  }}

  function showSlide(slideNum, shouldPlay = true) {{
    if (slideNum < 1) slideNum = 1;
    if (slideNum > TOTAL_SLIDES) slideNum = TOTAL_SLIDES;

    currentSlide = slideNum;
    window.currentSlide = slideNum;
    activeCueIndex = -1;

    // Switch slide display
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide) => slide.classList.remove('active'));

    const targetSlide = document.getElementById(`slide-${{slideNum}}`);
    if (targetSlide) {{
      targetSlide.classList.add('active');
    }}

    // Update Counter
    if (slideCounter) {{
      slideCounter.textContent = `SLIDE ${{String(slideNum).padStart(2, '0')}} / ${{TOTAL_SLIDES}}`;
    }}

    // Setup initial subtitle cue
    const slideCues = TRANSLATIONS[String(slideNum)] || [];
    if (slideCues.length > 0) {{
      renderCue(slideCues[0]);
    }}

    // Setup Audio
    const padNum = String(slideNum).padStart(2, '0');
    audio.src = `audio/slide_${{padNum}}.mp3`;
    audio.currentTime = 0;

    const totalDur = DURATIONS[String(slideNum)] || 20;
    if (subTimecode) {{
      subTimecode.textContent = `00:00 / ${{formatTime(totalDur)}}`;
    }}
    if (scrubberFill) scrubberFill.style.width = '0%';
    if (scrubberHandle) scrubberHandle.style.left = '0%';

    if (shouldPlay) {{
      audio.play().then(() => {{
        isPlaying = true;
        updatePlayPauseUI();
        startTracking();
      }}).catch(err => {{
        console.log('[Falcor Audio] Autoplay deferred until user interaction');
        isPlaying = false;
        updatePlayPauseUI();
      }});
    }} else {{
      audio.pause();
      isPlaying = false;
      updatePlayPauseUI();
    }}

    console.log(`[Falcor HR] Active Slide: ${{slideNum}} / ${{TOTAL_SLIDES}}`);
  }}

  function renderCue(cue) {{
    if (!cue) return;
    if (subSpokenEn) subSpokenEn.textContent = cue.en || "";
    if (subLangAr) subLangAr.textContent = cue.ar || "";
    if (subLangHi) subLangHi.textContent = cue.hi || "";
    if (subLangTa) subLangTa.textContent = cue.ta || "";
    if (subLangMl) subLangMl.textContent = cue.ml || "";

    if (subConsole) {{
      subConsole.classList.remove('sub-updating');
      void subConsole.offsetWidth; // Force CSS reflow
      subConsole.classList.add('sub-updating');
    }}
  }}

  function startTracking() {{
    if (animFrameId) cancelAnimationFrame(animFrameId);

    function tick() {{
      if (isPlaying) {{
        const curTime = audio.currentTime;
        const totalDur = DURATIONS[String(currentSlide)] || (audio.duration || 20);

        // Update Scrubber
        const pct = Math.min(100, Math.max(0, (curTime / totalDur) * 100));
        if (scrubberFill) scrubberFill.style.width = `${{pct}}%`;
        if (scrubberHandle) scrubberHandle.style.left = `${{pct}}%`;

        // Update Timecode
        if (subTimecode) {{
          subTimecode.textContent = `${{formatTime(curTime)}} / ${{formatTime(totalDur)}}`;
        }}

        // Match Speech Cue
        const slideCues = TRANSLATIONS[String(currentSlide)] || [];
        let matchedIndex = -1;
        for (let i = 0; i < slideCues.length; i++) {{
          if (curTime >= slideCues[i].start && curTime < slideCues[i].end) {{
            matchedIndex = i;
            break;
          }}
        }}

        if (matchedIndex === -1 && slideCues.length > 0) {{
          if (curTime >= slideCues[slideCues.length - 1].end) {{
            matchedIndex = slideCues.length - 1;
          }} else if (curTime < slideCues[0].start) {{
            matchedIndex = 0;
          }}
        }}

        if (matchedIndex !== -1 && matchedIndex !== activeCueIndex) {{
          activeCueIndex = matchedIndex;
          renderCue(slideCues[matchedIndex]);
        }}

        animFrameId = requestAnimationFrame(tick);
      }}
    }}
    animFrameId = requestAnimationFrame(tick);
  }}

  function togglePlayPause() {{
    if (audio.paused) {{
      audio.play().then(() => {{
        isPlaying = true;
        updatePlayPauseUI();
        startTracking();
      }}).catch(err => console.warn(err));
    }} else {{
      audio.pause();
      isPlaying = false;
      updatePlayPauseUI();
      if (animFrameId) cancelAnimationFrame(animFrameId);
    }}
  }}

  function updatePlayPauseUI() {{
    if (!btnPlayPause) return;
    const iconPlay = btnPlayPause.querySelector('.icon-play');
    const iconPause = btnPlayPause.querySelector('.icon-pause');
    if (iconPlay && iconPause) {{
      if (isPlaying) {{
        iconPlay.style.display = 'none';
        iconPause.style.display = 'block';
      }} else {{
        iconPlay.style.display = 'block';
        iconPause.style.display = 'none';
      }}
    }}
  }}

  function toggleMute() {{
    isMuted = !isMuted;
    audio.muted = isMuted;
    if (btnMute) {{
      const volOn = btnMute.querySelector('.icon-vol-on');
      const volMute = btnMute.querySelector('.icon-vol-mute');
      if (volOn && volMute) {{
        volOn.style.display = isMuted ? 'none' : 'block';
        volMute.style.display = isMuted ? 'block' : 'none';
      }}
    }}
  }}

  function seekTo(percentage) {{
    const totalDur = DURATIONS[String(currentSlide)] || (audio.duration || 20);
    audio.currentTime = (percentage / 100) * totalDur;
    if (!isPlaying) {{
      startTracking();
    }}
  }}

  function nextSlide() {{
    if (currentSlide < TOTAL_SLIDES) {{
      showSlide(currentSlide + 1, isPlaying);
    }}
  }}

  function prevSlide() {{
    if (currentSlide > 1) {{
      showSlide(currentSlide - 1, isPlaying);
    }}
  }}

  // Audio Event Listeners
  audio.addEventListener('ended', () => {{
    isPlaying = false;
    updatePlayPauseUI();
    if (currentSlide < TOTAL_SLIDES) {{
      setTimeout(() => {{
        nextSlide();
        audio.play().then(() => {{
          isPlaying = true;
          updatePlayPauseUI();
          startTracking();
        }}).catch(() => {{}});
      }}, 1200);
    }}
  }});

  // Scrubber click handler
  if (scrubberWrap) {{
    scrubberWrap.addEventListener('click', (e) => {{
      const rect = scrubberWrap.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const pct = Math.max(0, Math.min(100, (clickX / rect.width) * 100));
      seekTo(pct);
    }});
  }}

  // Button clicks
  if (btnPlayPause) btnPlayPause.addEventListener('click', togglePlayPause);
  if (btnPrev) btnPrev.addEventListener('click', prevSlide);
  if (btnNext) btnNext.addEventListener('click', nextSlide);
  if (btnMute) btnMute.addEventListener('click', toggleMute);

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {{
    switch (e.key) {{
      case ' ':
        e.preventDefault();
        togglePlayPause();
        break;
      case 'ArrowRight':
      case 'PageDown':
        e.preventDefault();
        nextSlide();
        break;
      case 'ArrowLeft':
      case 'PageUp':
        e.preventDefault();
        prevSlide();
        break;
      case 'Home':
        e.preventDefault();
        showSlide(1, isPlaying);
        break;
      case 'End':
        e.preventDefault();
        showSlide(TOTAL_SLIDES, isPlaying);
        break;
      case 'm':
      case 'M':
        toggleMute();
        break;
    }}
  }});

  // Global API exposed for automation & Playwright
  window.showSlide = showSlide;
  window.nextSlide = nextSlide;
  window.prevSlide = prevSlide;
  window.togglePlayPause = togglePlayPause;
  window.getTotalSlides = () => TOTAL_SLIDES;
  window.getCurrentSlide = () => currentSlide;
  window.getAudio = () => audio;

  // Initialize on slide 1
  document.addEventListener('DOMContentLoaded', () => {{
    updatePlayPauseUI();
    showSlide(1, false);
  }});

  if (document.readyState === 'complete' || document.readyState === 'interactive') {{
    updatePlayPauseUI();
    showSlide(1, false);
  }}
}})();
"""

out_dir = r"C:\Users\m.shameel\.gemini\antigravity-cli\brain\75e0257b-7d41-4749-92fb-a5f17bbb9b78\scratch"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "generated_app.js")
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(app_js_content)

print(f"Generated successfully to {out_file}!")
