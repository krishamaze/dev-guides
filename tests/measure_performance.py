
import asyncio
from playwright.async_api import async_playwright
import http.server
import socketserver
import threading
import os
import time

PORT = 8011
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # Silence logging

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

async def measure_performance(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Block external resources
        await page.route("**/*", lambda route: route.abort()
            if any(domain in route.request.url for domain in ["fonts.googleapis.com", "fonts.gstatic.com"])
            else route.continue_())

        # Inject script to count offsetTop accesses
        await page.add_init_script("""
            window.offsetTopCount = 0;
            const originalOffsetTop = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetTop').get;
            Object.defineProperty(HTMLElement.prototype, 'offsetTop', {
                get: function() {
                    window.offsetTopCount++;
                    return originalOffsetTop.apply(this);
                }
            });
        """)

        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=10000)

            # Simulate scrolling
            for i in range(20):
                await page.evaluate(f"window.scrollTo(0, {i * 100})")
                await asyncio.sleep(0.05)

            count = await page.evaluate("window.offsetTopCount")
            return count
        except Exception as e:
            print(f"Error during measurement: {e}")
            return None
        finally:
            await browser.close()

async def main():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Give server time to start
    await asyncio.sleep(2)

    url = f"http://localhost:{PORT}/guides/oracle-free-server/index.html"
    print(f"Measuring performance for {url}...")

    initial_count = await measure_performance(url)
    print(f"offsetTop count: {initial_count}")

if __name__ == "__main__":
    asyncio.run(main())
