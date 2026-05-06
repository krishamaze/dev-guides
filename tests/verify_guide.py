import os
from playwright.sync_api import sync_playwright, expect

def test_guide_functionality():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Grant clipboard permissions
        context = browser.new_context()
        context.grant_permissions(['clipboard-read', 'clipboard-write'])
        page = context.new_page()

        # Block external resources
        page.route("**/*.{fnt,woff,woff2}", lambda route: route.abort())
        page.route("https://fonts.googleapis.com/**", lambda route: route.abort())
        page.route("https://fonts.gstatic.com/**", lambda route: route.abort())

        # Get absolute path to the guide
        current_dir = os.getcwd()
        file_path = f"file://{current_dir}/guides/oracle-free-server/index.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="domcontentloaded")

        # Test Copy Button
        copy_btn = page.locator(".copy-btn").first
        code_block = page.locator(".code-block").first
        expected_code = code_block.locator("code").text_content()

        print(f"Initial button text: {copy_btn.text_content()}")

        # Click copy button
        copy_btn.click()

        # Check if text changed to "Copied" (might be "✓ Copied!" in some versions, but base has "Copied")
        btn_text = copy_btn.text_content()
        print(f"Button text after click: {btn_text}")
        assert "Copied" in btn_text
        assert "copied" in copy_btn.get_attribute("class")

        # Verify clipboard
        clipboard_text = page.evaluate("navigator.clipboard.readText()")
        print(f"Clipboard text: {clipboard_text}")
        assert clipboard_text == expected_code

        # Test TOC highlighting
        sections = page.locator("section[id]")
        # Scroll to second section
        second_section = sections.nth(1)
        second_section_id = second_section.get_attribute("id")
        print(f"Scrolling to section: {second_section_id}")

        # In baseline, it uses scroll listener with offsetTop - 100
        # Let's scroll so it's definitely the current section
        page.evaluate(f"window.scrollTo(0, document.getElementById('{second_section_id}').offsetTop - 50)")
        page.wait_for_timeout(1000) # Wait for scroll event to fire and JS to run

        active_links = page.locator(".toc-list a.active")
        count = active_links.count()
        print(f"Number of active links: {count}")
        for i in range(count):
             print(f"Active TOC link {i}: {active_links.nth(i).get_attribute('href')}")

        if count > 0:
            active_href = active_links.first.get_attribute("href")
            assert active_href == f"#{second_section_id}"
        else:
            print("No active links found!")
            assert False

        # Take a screenshot
        os.makedirs("verification", exist_ok=True)
        page.screenshot(path="verification/baseline_guide.png")
        print("Baseline screenshot saved.")

        browser.close()

if __name__ == "__main__":
    test_guide_functionality()
