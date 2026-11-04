from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto(f"file://{os.path.abspath('test_frontend.html')}")
    page.wait_for_timeout(1000)

    # 1. Test System Tray Icon interaction
    page.locator("#trayIconBtn").click()
    page.wait_for_timeout(500)

    # Close tray menu by clicking outside or again
    page.locator("#trayIconBtn").click()
    page.wait_for_timeout(500)

    # 2. Click the execute pipeline button
    page.locator("#executeBtn").click()
    page.wait_for_timeout(1000)

    # 3. Wait for progress and completion
    page.wait_for_timeout(14000)

    # 4. Take screenshot of the completed dashboard state
    page.screenshot(path="./verification/screenshots/verification.png", full_page=True)
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    os.makedirs("./verification/videos", exist_ok=True)
    os.makedirs("./verification/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="./verification/videos",
            viewport={'width': 1200, 'height': 1200}
        )
        page = context.new_page()

        # Handle dialogs
        page.on("dialog", lambda dialog: dialog.accept())

        # Mock binary file
        with open("mock.exe", "w") as f:
            f.write("mock binary")

        page.goto(f"file://{os.path.abspath('test_frontend.html')}")
        page.locator("#binaryFile").set_input_files("mock.exe")

        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
            if os.path.exists("mock.exe"):
                os.remove("mock.exe")
