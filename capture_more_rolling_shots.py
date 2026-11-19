# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

WORKSPACE = r"C:\Users\m.shameel\Downloads\it_induction_ppt\hr induction"
SHOTS_DIR = r"C:\Users\m.shameel\.gemini\antigravity-cli\brain\75e0257b-7d41-4749-92fb-a5f17bbb9b78\scratch\rolling_narration_shots"
html_url = "file:///" + os.path.join(WORKSPACE, "index.html").replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(html_url, wait_until="domcontentloaded")
    page.wait_for_timeout(500)

    for slide in [4, 8, 13, 19]:
        page.evaluate(f"() => window.showSlide({slide}, false)")
        page.wait_for_timeout(200)
        # Advance rolling narration to mid-slide
        page.evaluate("() => window.updateRollingNarration(4.0)")
        page.wait_for_timeout(300)
        
        shot_path = os.path.join(SHOTS_DIR, f"slide_{slide:02d}_rolling.png")
        page.screenshot(path=shot_path)
        print(f"Captured {shot_path}")

    browser.close()
