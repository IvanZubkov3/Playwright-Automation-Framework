from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in non-headless mode for debugging
        page = browser.new_page()
        page.goto("https://www.google.com")

        # Handle Google consent pop-up (if it appears)
        try:
            if page.is_visible("button:has-text('Accept all')"):  # Adjust selector if needed
                page.click("button:has-text('Accept all')")
        except:
            print("No consent pop-up detected")

        # Ensure the search input is visible
        page.wait_for_selector("textarea[name=q]", timeout=10000)

        # Fill the search box and submit
        page.fill("textarea[name=q]", "Playwright Python")
        page.press("textarea[name=q]", "Enter")

        # Wait for search results to load
        page.wait_for_selector("#search", timeout=10000)

        # Verify results are displayed
        assert page.is_visible("#search"), "Search results not found"

        browser.close()
