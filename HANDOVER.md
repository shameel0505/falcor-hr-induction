# Falcor HR Induction & Broadcast Suite - Official Project Handover Document

**Organization:** Falcor Engineering & Contracting LLC, Abu Dhabi, UAE  
**Project:** Enterprise HR Induction Presentation, Interactive Multilingual Teleprompter Console, and Broadcast Video Suite  
**Date:** November 2026  
**Repository Branch:** `main`  
**Location:** `/Users/shameel/Desktop/hr_induction/falcor-hr-induction`  

---

## 1. Executive Summary

This repository contains the complete, production-ready multimedia onboarding and training suite for **Falcor Engineering & Contracting LLC**. The suite transforms the static corporate orientation deck into a synchronized, broadcast-grade presentation system supporting:

1. **Interactive HTML5/CSS3 1080p Presentation Player (`index.html`)**: 21 corporate slides featuring executive cards, verified client logos (ADNOC, ADDC, Abu Dhabi Airports), organizational hierarchy, work timing protocols, safety & HSE directives, and UAE Labour Law statutory entitlements.
2. **Live 4-Language Architectural Subtitle Blade**: Real-time spoken sentence subtitles in **Arabic (RTL)**, **Hindi**, **Tamil**, and **Malayalam**, updating dynamically as the narration plays.
3. **Rolling Teleprompter Subtitles Engine (`app.js`)**: Real-time word-level karaoke tracking with smooth horizontal viewport auto-scrolling and audio synchronization.
4. **Interactive Presenter Transport Console**: Scrubber, play/pause, volume/mute, speed toggle (1.0x / 1.25x / 1.5x), slide counter, and keyboard shortcuts.
5. **Full Neural Narration Audio Suite (`audio/`)**: 21 high-definition voiceover files (`slide_01.mp3` to `slide_21.mp3`) matching official corporate scripts.
6. **Master 1080p Broadcast Video (`Falcor_HR_Orientation_Broadcast_Master.mp4`)**: Pristine, high-fidelity H.264/AAC video combining all 21 slides.
7. **Slide 1 Live Broadcast Video (`videos/slide_01_video.mp4`)**: Sample cinema recording demonstrating real-time 4-language subtitle blade synchronization.
8. **Executive PDF Review Deck (`Falcor_HR_Orientation_Review_Deck.pdf`)**: 21-slide high-resolution printable/shareable review deck.
9. **Original Source Deck (`Falcor_HR_Orientation_v10_2_Final - ppt_18.11.26.pptx`)**: Preserved for reference and asset extraction.

---

## 2. Complete Deliverables Inventory

| Category | Primary File(s) | Description |
| :--- | :--- | :--- |
| **Interactive Player** | `index.html` | Master 1080p responsive canvas containing all 21 slides and console UI |
| **Styling & Layout** | `style.css`, `enrichment.css` | Corporate branding (`#033A49`, `#13788A`, `#FA880B`), typography, card layouts, blade styles |
| **Controller Engine** | `app.js` | Audio playback, subtitle synchronization, rolling prompter, transport handlers |
| **Master Video** | `Falcor_HR_Orientation_Broadcast_Master.mp4` | 1080p full orientation broadcast video (~19.6 MB, ~8.3 minutes) |
| **Slide 1 Live Video**| `videos/slide_01_video.mp4` | 1080p rendered clip showing live 4-language subtitle transitions |
| **Review Deck** | `Falcor_HR_Orientation_Review_Deck.pdf` | High-resolution 21-slide vector/graphic PDF presentation (~4.8 MB) |
| **Source PPTX** | `Falcor_HR_Orientation_v10_2_Final - ppt_18.11.26.pptx` | Original source PowerPoint presentation deck |
| **Audio Suite** | `audio/slide_01.mp3` – `slide_21.mp3` | 21 high-definition neural MP3 narrations |
| **Slide Frames** | `frames/slide_01.png` – `slide_21.png` | 21 high-resolution still slide frames |
| **Slide Video Clips** | `clips/clip_01.mp4` – `clip_21.mp4` | 21 pre-rendered 1080p slide video clips |
| **Brand Assets** | `assets/`, `falcor_logo_color.png`, `falcor_logo_white.png` | Client logos (ADNOC, ADDC, Airports), leader portraits, division icons |
| **Translations Data** | `exact_speech_translations.json` | Sentence-by-sentence cues for all 21 slides in AR, HI, TA, ML |
| **Timings Data** | `exact_speech_timings.json`, `audio_durations.json` | Word-level and slide-level duration metrics |
| **Dev Launchers** | `run_dev.py`, `start_dev.sh`, `start_dev.bat` | One-click cross-platform local development server launchers |
| **Pipeline Scripts** | `render_master_video.py`, `generate_hr_audio.py` | Automated video compilation and neural voiceover generation scripts |

---

## 3. Quick-Start Guide (New Machine Setup)

### System Requirements
- **Web Browser**: Any modern browser (Google Chrome, Microsoft Edge, Safari, Mozilla Firefox).
- **Python (Optional for Rendering)**: Python 3.10+ with `ffmpeg` installed.

### Option A: Immediate Offline Viewing (No Installs Needed)
1. Double-click `index.html` in file explorer/Finder, or
2. Right-click `index.html` → Open With → Google Chrome / Microsoft Edge.
*All styles, assets, fonts, and local audio will function directly.*

### Option B: Local Development Server (Recommended)
Running through an HTTP server ensures full audio autoplay and smooth asset streaming.

**On macOS / Linux:**
```bash
./start_dev.sh
```
*Or manually:*
```bash
python3 run_dev.py
```

**On Windows:**
Double-click `start_dev.bat` or run:
```cmd
python run_dev.py
```

*The launcher will automatically find an available port (default `8000`) and launch your default browser to `http://localhost:8000/`.*

---

## 4. Interactive Presenter Console & Controls

### Keyboard Shortcuts
| Key | Action |
| :--- | :--- |
| **`Space`** | Play / Pause audio narration |
| **`→` (Right Arrow) / `PageDown`** | Next Slide (automatically pauses/plays audio for new slide) |
| **`←` (Left Arrow) / `PageUp`** | Previous Slide |
| **`Home`** | Jump to Slide 01 |
| **`End`** | Jump to Slide 21 |
| **`M`** | Mute / Unmute narration audio |

### On-Screen Controls
- **Scrubber Bar**: Click anywhere on the progress bar to seek immediately to that point in the narration.
- **Speed Selector (`1.0x` / `1.25x` / `1.5x`)**: Click to cycle audio playback speed without pitch distortion.
- **Language Switcher**: Click `AR`, `HI`, `TA`, `ML`, or `ALL 4-LANG` on slides with focused subtitles.
- **Slide Counter**: Displays current slide index (`SLIDE 01 / 21`).

---

## 5. Slide-by-Slide Content Matrix (21 Slides)

1. **Slide 01 · Welcome to Falcor**: Orientation overview, 3 core pillars (Heritage, How We Work, Employment Rights), 48-hour onboarding milestone.
2. **Slide 02 · About Falcor (History & Scale)**: 1979 foundation, 1,500+ professionals, ISO benchmark, 4 core business divisions (Supply, EPC, Maintenance, Manpower).
3. **Slide 03 · Who We Work For (Client Benchmark)**: ADNOC Group, ADDC, Abu Dhabi Airports. Golden rule: collective accountability and strict client compliance.
4. **Slide 04 · Leadership & Facilities**: Chairman Mr. Sam Mebarek, CEO Mr. Mehdi Mebarek, COO Mr. Muralidharan Swaminathan, Director Mr. Jignesh Patel, Sales Director Mr. Jamal. Addax Tower HQ & Mussafah Central Workshop.
5. **Slide 05 · Dress Code & Professional Appearance**: Formal business Mon–Thu, smart casual Friday, mandatory formal client attire, site PPE & coveralls.
6. **Slide 06 · Working Time, Attendance & Overtime**: 08:00–17:00 (40 hrs/wk), 1-hour lunch break (Slots 12:00–13:00 / 13:00–14:00), Ramadan 6-hr day, Sunday 10 AM timesheet deadline, overtime protocols.
7. **Slide 07 · Workplace Standards & Housekeeping**: Clean desk policy, pantry etiquette, meeting room clearance, zero tolerance for harassment/racism, smoke-free office.
8. **Slide 08 · Safety: HSE Induction & Evacuation**: 6-step evacuation protocol, floor wardens, first aiders, assembly points, stop-work authority.
9. **Slide 09 · Emergency Contacts & Incident Reporting**: Civil emergency numbers (997 Fire, 998 Ambulance, 999 Police), common office hazard controls, 24-hr reporting window.
10. **Slide 10 · Client Sites (ADNOC & Government)**: Client site induction mandatory, gate passes, zero tolerance for mobile phones/cameras in operational zones, PPE compliance.
11. **Slide 11 · Integrity, Gifts & Confidentiality**: Non-Disclosure Agreement (NDA), zero cash/gifts/favours policy, anti-bribery, social media guidelines.
12. **Slide 12 · Probation Period & First Months**: 1–3 months standard (max 6 months), 14 days written notice, SMART performance goals set in Weeks 1–4.
13. **Slide 13 · Leave Policy at a Glance**: 30 calendar days annual leave, 90 days sick leave (15 full / 30 half / 45 unpaid), 60 days maternity, paternity, bereavement, pilgrimage leave.
14. **Slide 14 · Returning from Leave on Time**: Reporting back on Day 1, proof required for delays, consequences of unauthorized absence.
15. **Slide 15 · Salary, Benefits & Loans**: Last working day WPS electronic bank transfer, monthly pay slips, project overtime allowances, company personal loan facilities.
16. **Slide 16 · Employee Welfare & Workers' Rights**: 100% WPS salary protection, no recruitment fees, retained personal documents, workmen's compensation, MOHRE helpline (600 590000).
17. **Slide 17 · Performance Management Cycle**: January SMART goal setting, June mid-year review, December annual evaluation, merit increments & promotions.
18. **Slide 18 · Disciplinary Procedure & Penalties**: 4-stage due process (notification, investigation, Disciplinary Committee hearing, defense). 3 penalty levels.
19. **Slide 19 · Separation & End of Service Benefits (EOSB)**: Resignation notice, UAE Labour Law gratuity calculation (21 days/yr for years 1–5, 30 days/yr after), visa cancellation & final settlement.
20. **Slide 20 · Speaking Up & Support Directory**: 3-step grievance redressal (7-day resolution window), contact details for HR (`hr@falcor-eng.com`), Admin (`a.rajan@falcor-eng.com`), and emergency helpdesk.
21. **Slide 21 · Life at Falcor (Closing)**: Teamwork, camaraderie, open-door culture, safety excellence, Employee Handbook link (`falcor.ae/careers`), welcome aboard message.

---

## 6. How to Re-render or Update Video & Audio

### Re-rendering the Master Broadcast Video
If you update slide frames, styling, or audio durations, re-render the master video:
```bash
python render_master_video.py
```
*The script automatically detects system `ffmpeg` (or `imageio-ffmpeg`), renders 21 clips at 1080p with `libx264` (`crf=17`, `preset=fast`, `tune=stillimage`) and AAC 192kbps audio, and concatenates them into `Falcor_HR_Orientation_Broadcast_Master.mp4`.*

### Re-generating Voiceover Audio (Azure/Edge-TTS)
To regenerate or adjust narration speed/voice across all slides:
```bash
pip install edge-tts
python generate_hr_audio.py
```
*Outputs new `.mp3` files into `audio/` and recalculates exact durations into `audio_durations.json`.*

### Updating Translations or Cues
All multilingual subtitles are maintained in:
`exact_speech_translations.json`
To recompile translations into `app.js`:
```bash
python build_app_js.py
```

---

## 7. Design System & Corporate Brand Tokens

| Token | Hex / Value | Usage |
| :--- | :--- | :--- |
| **Falcor Deep Teal** | `#033A49` | Primary headings, dark accents, executive branding |
| **Falcor Seafoam** | `#13788A` | Sub-headings, active borders, blade gutters |
| **Falcor Amber/Gold** | `#FA880B` | Highlight ribbons, important badges, warning accents |
| **Dark Obsidian** | `#0B0F19` / `#03252E`| Slide 21 backdrop, dark-glass prompter blades |
| **Light Canvas** | `#F8FAFC` | Main presentation slide background |
| **Card White** | `#FFFFFF` | Executive card backgrounds with soft drop shadows |
| **Primary Typography** | `'Lato', sans-serif` | Clean, geometric corporate sans-serif |
| **Arabic Typography** | `'Noto Sans Arabic', sans-serif` | Natural Emirati corporate typography (RTL) |
| **Hindi Typography** | `'Noto Sans Devanagari', sans-serif` | Clean Devanagari script |
| **Tamil Typography** | `'Noto Sans Tamil', sans-serif` | Balanced Tamil typography |
| **Malayalam Typography**| `'Noto Sans Malayalam', sans-serif` | Balanced Malayalam typography |

> [!IMPORTANT]
> **Readability Standard**: All body copy, list items, and subtitles are strictly maintained at or above **16px** (titles at 32px–66px) to ensure crisp legibility on 1080p screens, projection displays, and broadcast recordings.

---

## 8. Handover Verification & Quality Checklist

- [x] **Git Repository**: Initialized, all files committed cleanly on `main`, zero uncommitted changes.
- [x] **UTF-8 Encoding**: Verified across all files. Arabic, Hindi, Tamil, and Malayalam glyphs render crisply without mojibake.
- [x] **Cross-Platform Compatibility**: Tested on macOS and Windows; path handling dynamically resolves relative to script location.
- [x] **Audio Duration Synchronization**: All 21 slide durations match measured audio lengths in `audio_durations.json`.
- [x] **Subtitles & Teleprompter**: Tested with Playwright and browser simulation; sentence cues and rolling prompter track audio accurately.
- [x] **Broadcast Master Video**: Fully rendered and verified at 1920×1080, 25 fps, AAC stereo.
- [x] **PDF Review Deck**: Verified 21-slide high-resolution export (`Falcor_HR_Orientation_Review_Deck.pdf`).

---

*Handover prepared for Falcor Engineering & Contracting LLC.*  
*For questions or future enhancements, refer to `README.md` or contact the Falcor HR & IT Development Team.*
