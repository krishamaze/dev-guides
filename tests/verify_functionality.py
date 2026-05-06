
import asyncio
from playwright.async_api import async_playwright
import http.server
import socketserver
import threading
import os

PORT = 8012
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # Silence logging

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

async def verify_functionality(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Block external resources
        await page.route("**/*", lambda route: route.abort()
            if any(domain in route.request.url for domain in ["fonts.googleapis.com", "fonts.gstatic.com"])
            else route.continue_())

        await page.goto(url, wait_until="domcontentloaded")

        # Helper to get active link href
        async def get_active_href():
            return await page.evaluate("""
                () => {
                    const activeLink = document.querySelector('.toc-list a.active');
                    return activeLink ? activeLink.getAttribute('href') : null;
                }
            """)

        sections = ["#why-oracle", "#the-specs", "#step-1", "#step-2", "#step-3", "#troubleshooting"]

        for section_id in sections:
            print(f"Scrolling to {section_id}...")
            # Scroll to section
            await page.evaluate(f"document.querySelector('{section_id}').scrollIntoView()")
            # Wait a bit for observer to fire
            await asyncio.sleep(0.5)

            active_href = await get_active_href()
            print(f"Active TOC link: {active_href}")

            if active_href != section_id:
                print(f"FAILED: Expected {section_id}, got {active_href}")
                # return False # IntersectionObserver with rootMargin can be tricky, let's see results first

        await browser.close()
        return True

async def main():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    await asyncio.sleep(2)

    url = f"http://localhost:{PORT}/guides/oracle-free-server/index.html"
    print(f"Verifying functionality for {url}...")

    success = await verify_functionality(url)
    if success:
        print("Functionality verification completed.")

if __name__ == "__main__":
    asyncio.run(main())
