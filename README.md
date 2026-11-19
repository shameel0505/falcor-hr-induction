# Falcor HR Induction - Master Presentation & Broadcast Video Suite

Comprehensive enterprise onboarding presentation, interactive teleprompter console, and synchronized 4-language broadcast video suite built for **Falcor Engineering & Contracting LLC, UAE**.

---

## 🌟 Key Features

1. **21 High-Impact Corporate Slides (`index.html`)**
   - Engineered with modern CSS Grid, Obsidian Tech aesthetic, and Falcor corporate branding (`#0B0F19`, `#2563EB`, `#06B6D4`, `#10B981`).
   - Detailed visual layouts including Client Trust Grid (ADNOC, ADDC, Abu Dhabi Airports), Work Schedules, Leave Policies, Safety & Ethics, and UAE Labor Law entitlements.

2. **Real-time Rolling Teleprompter Subtitles (`app.js`)**
   - Live word-by-word karaoke tracking synchronized with speech audio.
   - Smooth horizontal auto-scroll centering active spoken words in the focal viewing window.
   - Visual states for past words (muted blue), active word (glowing white badge), and future words (soft translucent gray).

3. **Synchronized 4-Language Narration Subtitles (`exact_speech_translations.json`)**
   - Full sentence-by-sentence spoken translations (not slide summaries) for all 21 slides in:
     - 🇦🇪 **Arabic (`ar`)** with native RTL layout and Amiri/Noto typography
     - 🇮🇳 **Hindi (`hi`)** in Devanagari typography
     - 🇮🇳 **Tamil (`ta`)** in Tamil typography
     - 🇮🇳 **Malayalam (`ml`)** in Malayalam typography
   - Seamless one-click language switcher (`EN`, `AR`, `HI`, `TA`, `ML`, or `ALL` 4-quadrant simultaneous view).

4. **Interactive Presenter Transport Console**
   - Transport controls: Play/Pause, Seek Scrubber, Mute/Unmute, Speed Selector (`1.0x`, `1.25x`, `1.5x`), Previous/Next Slide, and Slide Counter (`01 / 21`).
   - Keyboard shortcuts: `Space` (Play/Pause), `Arrow Right` / `Arrow Left` (Next/Prev Slide), `M` (Mute).

5. **Broadcast Master Video Generation Pipeline (`render_master_video.py`)**
   - Programmatically loops high-resolution slide frames with exact audio duration synchronization.
   - Scales to crystal-clear 1080p (`-vf scale=1920:-1`) using `libx264` (`crf=17`, `preset=fast`, `tune=stillimage`) and AAC 192k 48kHz audio.
   - Concatenates all 21 clips into `Falcor_HR_Orientation_Broadcast_Master.mp4`.

---

## 📁 Repository Directory Structure

```text
hr induction/
├── index.html                           # Main responsive presentation & interactive console
├── app.js                               # Controller: Audio playback, rolling prompter & translations
├── style.css                            # Core layout, glassmorphism, responsive grid & typography
├── enrichment.css                       # Obsidian slide blades, schedule cards & badge styling
├── exact_speech_translations.json       # Sentence-by-sentence translations (AR, HI, TA, ML) with timestamps
├── exact_speech_timings.json            # Word-level speech timestamps for real-time tracking
├── audio_durations.json                 # Exact duration measurements for all 21 slides
├── all_slides_extracted.json            # Extracted slide metadata and text content
│
├── render_master_video.py               # Automated FFmpeg 1080p render & concatenation script
├── test_rolling_narration.py            # Playwright automated test suite for rolling prompter & translations
├── build_app_js.py                      # Generator script that compiles translations and words into app.js
├── generate_hr_audio.py                 # Azure/Edge-TTS neural audio generation script
│
├── audio/                               # High-definition neural MP3 narrations (slide_01.mp3 to slide_21.mp3)
├── frames/                              # High-resolution slide graphics (slide_01.png to slide_21.png)
├── clips/                               # Rendered 1080p MP4 clips per slide (clip_01.mp4 to clip_21.mp4)
├── assets/                              # Brand logos, icons, and client vectors
│
├── Falcor_HR_Orientation_Broadcast_Master.mp4  # Final concatenated 1080p broadcast video (~19 MB)
└── Falcor_HR_Orientation_v10_2_Final - ppt_18.11.26.pptx # Source presentation deck
```

---

## 🚀 Setup & Usage Instructions (New Computer)

### 1. Prerequisites
- **Python 3.10+**
- **Node.js 18+** (optional, for local development server)
- **FFmpeg**: Required for video rendering (`pip install imageio-ffmpeg` supplies bundled FFmpeg binary automatically).

### 2. Install Python Dependencies
```bash
pip install imageio-ffmpeg edge-tts playwright
playwright install chromium
```

### 3. Run the Interactive Presentation & Presenter Console
You can view the deck directly in any modern browser:
```bash
# Option A: Simple Python Local Server
python -m http.server 8000

# Open in browser:
# http://localhost:8000/
```
Or simply double-click and open `index.html` in Chrome / Edge.

### 4. Render / Re-render the Master Broadcast Video
To compile all slides and audio into individual 1080p clips and concatenate them into the master broadcast video:
```bash
python render_master_video.py
```
*Output: `Falcor_HR_Orientation_Broadcast_Master.mp4`*

### 5. Run Automated Tests
To run headless browser tests verifying rolling teleprompter progression, active word highlighting, and multi-language translation switching:
```bash
python test_rolling_narration.py
```

---

## 🎨 Design Palette Reference

| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Dark Obsidian** | `#0B0F19` / `#111827` | Deep contrast background & card base |
| **Falcor Cobalt** | `#2563EB` | Primary accents, buttons & active border glow |
| **Cyan Horizon** | `#06B6D4` | Secondary accents, highlights & audio waveforms |
| **Emerald UAE** | `#10B981` | Success states, leave approvals & completed indicators |
| **Pure White** | `#FFFFFF` | Primary headings & active prompter text |
| **Slate Gray** | `#94A3B8` | Body text & upcoming prompter words |

---

## 📜 Slide Breakdown (21 Slides)

1. **Welcome to Falcor** - Orientation Overview, Purpose & Vision
2. **Company Background** - Foundation, UAE Roots & Engineering Growth
3. **Clients & Projects** - Key Client Relationships (ADNOC, ADDC, Abu Dhabi Airports)
4. **Values & Culture** - Safety, Integrity, Excellence & Teamwork
5. **Organizational Structure** - Leadership, Divisions & Reporting Lines
6. **Work Timings & Attendance** - Office vs Site Schedules, Biometrics & Grace Periods
7. **Dress Code & Professional Conduct** - Office Attire, Site PPE & Grooming
8. **Probation Period** - 6-Month Review, KPI Evaluations & Confirmation
9. **Salary & Benefits** - WPS Bank Transfers, Overtime Rules & Increments
10. **Medical Insurance** - Daman Network Tiers, Card Issuance & Claims
11. **Leave Policy** - 30 Calendar Days Annual Leave, Sick Leave & Public Holidays
12. **Workplace Health & Safety** - Zero Harm Policy, Site PPE & Incident Reporting
13. **IT & Data Security** - SSO, Acceptable Use, Email Conduct & Device Protection
14. **Communication Channels** - Official Emails, Slack/Teams & Reporting Lines
15. **Performance Appraisals** - Annual Evaluations, Goals & Promotion Criteria
16. **Disciplinary Procedures** - Warnings, Labor Law Compliance & Fair Hearings
17. **Grievance Redressal** - Open Door Policy & Confidential HR Support
18. **Training & Development** - Skill Building, Certifications & Career Growth
19. **End of Service Benefits** - UAE Labor Law Gratuity Calculations & Exit Formalities
20. **Important Contacts** - HR, Admin, IT & Emergency Helpdesk Directory
21. **Closing & Q&A** - Welcome Aboard & Next Steps

---
*Built with ❤️ for Falcor Engineering & Contracting LLC.*
