# Falcor HR Induction & Broadcast Suite - Comprehensive Summary of Work Done

**Project:** Falcor Engineering & Contracting LLC - HR Induction Presentation & Broadcast Suite  
**Date:** November 19, 2026  
**Repository Branch:** `main` (Git Initialized & Committed)  
**Primary Directory:** `hr induction/`  

---

## 1. Executive Summary

This project transforms the Falcor corporate HR orientation into an enterprise-grade, synchronized multimedia broadcast suite. It features:
1. **An interactive 21-slide HTML5/CSS presentation** built with modern Obsidian dark-glass aesthetics.
2. **A real-time rolling teleprompter** that tracks spoken narration word-by-word with karaoke-style highlighting and smooth horizontal auto-scrolling.
3. **Synchronized 4-language spoken sentence subtitles** in Arabic (RTL), Hindi, Tamil, and Malayalam, updating in real time as each sentence is voiced.
4. **A presenter console** with full audio transport controls (play/pause, seek, speed toggle, mute, and language selector).
5. **An automated FFmpeg video rendering pipeline** that compiles all 21 slides and audio tracks into a master 1080p broadcast video (`Falcor_HR_Orientation_Broadcast_Master.mp4`).
6. **A brand-new Git repository** with all code, assets, audio, clips, and documentation committed cleanly to `main` for immediate pickup on another computer.

---

## 2. Issues Diagnosed & Resolved from Previous Work

| Area | Previous Issue | Diagnosis | Solution Implemented |
| :--- | :--- | :--- | :--- |
| **File Encoding** | Arabic, Hindi, Tamil, and Malayalam text rendered as mojibake / corrupted glyphs. | Scripts modified `index.html` using default Windows ANSI/CP1252 encoding instead of UTF-8. | Rebuilt modification scripts to explicitly enforce `encoding='utf-8'`. Restored all non-Latin typography cleanly. |
| **Slide Content** | Slides 1, 6, and 11 had placeholder bullets or missing detail sections. | Incomplete slide content extraction from the source PPTX. | Enriched Slide 1 with orientation highlights, Slide 6 with office vs site biometric schedules, and Slide 11 with full UAE Labor Law leave entitlements. |
| **Audio Synchronization** | Slide slide durations in `data-duration` attributes drifted from actual narration. | Estimates differed by up to 2–4 seconds per slide from actual audio lengths. | Extracted exact durations from all 21 MP3 files via FFmpeg and updated `data-duration` in `index.html` and `audio_durations.json`. |
| **Video Rendering Crash** | FFmpeg crashed with `Cannot allocate memory` (Exit code -12). | Rendering raw 4K (3840×2160) still frames into H.264 video exceeded local buffer memory. | Added `-vf scale=1920:-1` downscale in `render_master_video.py`. Successfully rendered all 21 clips and concatenated the 18.73 MB master video. |
| **Subtitles Functionality** | Subtitles were static slide summaries rather than live spoken narration. | Subtitles did not track audio cues in real time. | Generated exact sentence-by-sentence cues (`exact_speech_translations.json`) and real-time rolling word tracker (`app.js`). |

---

## 3. Core Features & Architecture Delivered

### A. Real-Time Rolling Teleprompter Subtitles
- Located inside the lower architectural blade of `index.html`.
- Powered by `app.js` via `updateRollingNarration(currentTime)`.
- **Word-Level State Engine:** Words are flagged as `.past-word` (muted slate blue), `.active-word` (illuminated white badge with glow), or `.future-word` (translucent gray).
- **Continuous Teleprompter Motion:** As words become active, the viewport horizontally translates (`translateX`) to keep the active word centered at the 30% focal line.

### B. Synchronized 4-Language Spoken Translations
- Defined in `exact_speech_translations.json` and compiled directly into `app.js`.
- Translates each **spoken sentence** directly as it is heard, rather than presenting a high-level summary:
  - 🇦🇪 **Arabic (`ar`)**: Full Right-to-Left (`dir="rtl"`) layout, Amiri typography, natural Emirati corporate phrasing.
  - 🇮🇳 **Hindi (`hi`)**: Devanagari script, clear professional terminology.
  - 🇮🇳 **Tamil (`ta`)**: Native Tamil typography, natural grammatical phrasing.
  - 🇮🇳 **Malayalam (`ml`)**: Native Malayalam typography, natural spoken phrasing.
- **Presenter Language Switcher:** Allows toggling between `EN`, `AR`, `HI`, `TA`, `ML`, or an `ALL` 4-quadrant simultaneous grid.

### C. 21 Corporate Slides Delivered (`index.html` & `enrichment.css`)
1. **Welcome to Falcor:** Corporate vision, onboarding roadmap, feature badges.
2. **Company Background:** UAE foundation, growth milestones, engineering capabilities.
3. **Clients & Strategic Projects:** Trust grid featuring ADNOC, ADDC, Abu Dhabi Airports, and major infrastructure clients.
4. **Corporate Values & Culture:** Safety First, Integrity, Excellence, and Teamwork.
5. **Organizational Structure:** Leadership hierarchy, engineering divisions, and reporting channels.
6. **Work Timings & Attendance:** Office (08:00–17:00) vs Site (07:00–16:00), biometric punch-in, and grace periods.
7. **Dress Code & PPE:** Office business casual, site mandatory safety PPE requirements.
8. **Probation Period:** 6-month evaluation timeline, KPI reviews, and permanent confirmation criteria.
9. **Salary & WPS Banking:** Ministry of Human Resources WPS electronic salary transfer, pay cycle, and overtime rules.
10. **Medical Insurance:** Daman network tiers, policy issuance, dependents, and reimbursement procedures.
11. **Leave Policies:** 30 calendar days annual leave, sick leave tiers, public holidays, and exit/re-entry permits.
12. **Workplace Health & Safety:** Zero Harm policy, hazard identification, and emergency incident protocols.
13. **IT & Cyber Security:** SSO authentication, Acceptable Use Policy, anti-phishing, and device encryption.
14. **Communication Channels:** Official emails, ticketing desk, Slack/Teams, and hierarchy protocols.
15. **Performance Management:** Annual KPI evaluations, 360-degree feedback, and merit increments.
16. **Disciplinary Code:** Progressive warning system, UAE Labor Law compliance, and investigation procedures.
17. **Grievance Redressal:** Open-door policy, confidential reporting channels, and HR review timelines.
18. **Training & Professional Growth:** Internal masterclasses, HSE certifications, and career ladders.
19. **End of Service Benefits (EOSB):** UAE Labor Law gratuity calculations, leave encashment, and visa cancellation steps.
20. **Key Contacts Directory:** Direct extension numbers and emails for HR, Admin, Payroll, IT, and Emergency response.
21. **Closing & Onboarding Next Steps:** Welcome to the team, buddy assignment, and initial workstation setup.

### D. Automated 1080p Video Render Pipeline
- **Script:** `hr induction/render_master_video.py`
- Converts 21 slide frames and MP3 audio into individual slide video clips in `clips/` using:
  ```bash
  ffmpeg -loop 1 -i slide_XX.png -i slide_XX.mp3 -vf scale=1920:-1 -c:v libx264 -preset fast -crf 17 -c:a aac -b:a 192k -shortest clip_XX.mp4
  ```
- Losslessly concatenates all clips into:
  `hr induction/Falcor_HR_Orientation_Broadcast_Master.mp4` (18.73 MB, 1080p, pristine audio sync).

---

## 4. Git Repository & Moving to Another Computer

A fresh Git repository has been initialized inside `hr induction/` on branch `main` and committed with the complete project state.

### Commit Details:
- **Commit Hash:** `e4a2db2`
- **Branch:** `main`
- **Files Committed:** 202 files (60.45 MB total)
- **Commit Message:**
  ```text
  feat(hr-induction): initial release with rolling teleprompter, 4-language synced translations, and broadcast video
  ```

### How to Transfer to Your Other Computer

#### Option A: Push to GitHub (Recommended)
1. On your GitHub account (`shameel002`), create a new repository (e.g. `falcor-hr-induction`).
2. Run the following commands inside `hr induction`:
   ```bash
   cd "C:\Users\m.shameel\Downloads\it_induction_ppt\hr induction"
   git remote add origin https://github.com/shameel002/falcor-hr-induction.git
   git push -u origin main
   ```
3. On your other computer, simply run:
   ```bash
   git clone https://github.com/shameel002/falcor-hr-induction.git
   cd falcor-hr-induction
   ```

#### Option B: Direct Copy via USB / Cloud Drive / Git Bundle
If you prefer not using GitHub right away, you can export a single portable Git bundle:
```bash
cd "C:\Users\m.shameel\Downloads\it_induction_ppt\hr induction"
git bundle create falcor_hr_induction.bundle --all
```
Copy `falcor_hr_induction.bundle` (or the entire `hr induction` folder) to your other computer. To clone from the bundle:
```bash
git clone falcor_hr_induction.bundle falcor-hr-induction
```

---

## 5. Quick-Start Commands on the New Computer

```bash
# 1. Install dependencies
pip install imageio-ffmpeg edge-tts playwright
playwright install chromium

# 2. Run the live presentation & rolling prompter in browser
python -m http.server 8000
# Open http://localhost:8000/ in Chrome or Edge

# 3. Re-render the broadcast video anytime
python render_master_video.py

# 4. Run automated headless test suite
python test_rolling_narration.py
```

---

## 6. Key Project Files Reference

| File | Size | Purpose |
| :--- | :--- | :--- |
| `index.html` | 88 KB | Master responsive presentation player and presentation markup |
| `app.js` | 100 KB | Teleprompter engine, audio sync, language switcher & transport controls |
| `style.css` | 30 KB | Core layout, responsive grid, Obsidian palette & typography |
| `enrichment.css` | 26 KB | Enhanced slide elements, client grids, timeline blades & badges |
| `exact_speech_translations.json` | 82 KB | Sentence-by-sentence translations (AR, HI, TA, ML) with timestamps |
| `exact_speech_timings.json` | 15 KB | Word-level speech timing data for teleprompter highlighting |
| `audio_durations.json` | 329 B | Exact audio lengths for slides 1–21 |
| `render_master_video.py` | 3.5 KB | Automated 1080p FFmpeg clip render and master video concat script |
| `test_rolling_narration.py` | 4.5 KB | Playwright test verifying rolling prompter & translation switching |
| `Falcor_HR_Orientation_Broadcast_Master.mp4` | 18.7 MB | Master 1080p broadcast video with synchronized narration |
| `README.md` | 5.5 KB | Comprehensive project documentation and developer guide |
| `.gitignore` | 350 B | Git ignore configuration for caches, temporary outputs, and bytecode |
| `audio/` | ~7 MB | 21 high-definition MP3 neural voiceover files |
| `frames/` | ~7 MB | 21 high-resolution slide visual frames |
| `clips/` | ~29 MB | 21 rendered 1080p individual slide MP4 video clips |

