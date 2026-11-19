# -*- coding: utf-8 -*-
import os
import time
from playwright.sync_api import sync_playwright

WORKSPACE = r"C:\Users\m.shameel\Downloads\it_induction_ppt\hr induction"
SHOTS_DIR = r"C:\Users\m.shameel\.gemini\antigravity-cli\brain\75e0257b-7d41-4749-92fb-a5f17bbb9b78\scratch\rolling_narration_shots"
os.makedirs(SHOTS_DIR, exist_ok=True)

html_url = "file:///" + os.path.join(WORKSPACE, "index.html").replace("\\", "/")

with sync_playwright() as p:
    print("Launching Chromium...", flush=True)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("console", lambda msg: print(f"[Browser Console] {msg.type}: {msg.text}") if msg.type == "error" else None)

    print("Navigating to page...", flush=True)
    page.goto(html_url, wait_until="domcontentloaded")
    page.wait_for_timeout(1000)

    print("=== Step 1: Initial Load Verification ===", flush=True)
    assert len(errors) == 0, f"JS Errors on initial load: {errors}"
    print(f"JS Errors: {len(errors)} (Clean!)", flush=True)

    # Verify elements
    has_track = page.evaluate("() => !!document.getElementById('narration-track')")
    has_viewport = page.evaluate("() => !!document.querySelector('.rolling-narration-viewport')")
    word_count = page.evaluate("() => document.querySelectorAll('#narration-track .k-word').length")
    print(f"Has Narration Track: {has_track}, Viewport: {has_viewport}, Total Words Loaded: {word_count}")
    assert word_count > 0, "No words rendered in narration track"

    # Step 2: Test Continuous Rolling Simulation at Multiple Timestamps
    print("\n=== Step 2: Testing Rolling Narration Progression ===")
    page.evaluate("() => window.showSlide(1, false)")
    page.wait_for_timeout(300)
    timestamps = [0.0, 1.2, 3.5, 7.0, 12.0]
    for ts in timestamps:
        page.evaluate(f"(t) => window.updateRollingNarration(t)", ts)
        # Give RAF/transition a moment
        page.wait_for_timeout(250)
        
        active_word = page.evaluate("() => { const el = document.querySelector('#narration-track .k-word.active-word'); return el ? el.textContent : null; }")
        track_transform = page.evaluate("() => document.getElementById('narration-track').style.transform")
        focused_text = page.evaluate("() => document.getElementById('focused-trans-text').textContent")
        
        print(f"Time {ts:4.1f}s -> Active Word: '{active_word}' | Track Transform: '{track_transform}' | Arabic Trans: '{focused_text[:30]}...'")

    # Take screenshot of Slide 1 with rolling prompter at time 7.0s
    page.evaluate("() => window.updateRollingNarration(7.0)")
    page.wait_for_timeout(300)
    shot_s1 = os.path.join(SHOTS_DIR, "slide_01_rolling_active.png")
    page.screenshot(path=shot_s1)
    print(f"\nCaptured rolling snapshot: {shot_s1}")

    # Step 3: Test Slide 3 (with ADNOC/ADDC/Airport logos)
    print("\n=== Step 3: Testing Slide 3 Client Logos ===")
    page.evaluate("() => window.showSlide(3, false)")
    page.wait_for_timeout(500)
    s3_words = page.evaluate("() => document.querySelectorAll('#narration-track .k-word').length")
    print(f"Slide 3 Narration Word Count: {s3_words}")
    shot_s3 = os.path.join(SHOTS_DIR, "slide_03_clients.png")
    page.screenshot(path=shot_s3)
    print(f"Captured Slide 3 snapshot: {shot_s3}")

    # Step 4: Test Slide 21 (Dark Obsidian Glass Theme)
    print("\n=== Step 4: Testing Slide 21 Dark Glass Console ===")
    page.evaluate("() => window.showSlide(21, false)")
    page.wait_for_timeout(500)
    is_dark_active = page.evaluate("() => document.body.classList.contains('dark-slide-active')")
    print(f"Slide 21 Dark Class Active: {is_dark_active}")
    shot_s21 = os.path.join(SHOTS_DIR, "slide_21_dark_rolling.png")
    page.screenshot(path=shot_s21)
    print(f"Captured Slide 21 snapshot: {shot_s21}")

    # Step 5: Test Language Switcher
    print("\n=== Step 5: Testing Language Switcher in Rolling Mode ===")
    for lang in ["hi", "ta", "ml", "all", "ar"]:
        page.click(f".lang-tab[data-lang='{lang}']")
        page.wait_for_timeout(200)
        tag = page.evaluate("() => document.getElementById('focused-trans-tag').textContent")
        print(f"Selected {lang.upper()} -> Tag: {tag}")

    assert len(errors) == 0, f"JS Errors occurred during test: {errors}"
    print("\n=== ALL TESTS PASSED WITH 0 ERRORS! ===")
    browser.close()
