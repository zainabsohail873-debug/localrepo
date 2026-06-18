from webbrowser import Edge

from playwright.sync_api import sync_playwright

def test_google():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        print("Page Title:", page.title())
        print("Current URL:", page.url)

        browser.close()


from playwright.sync_api import sync_playwright

EDGE_Path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=EDGE_Path,
        headless=False
    )

    page = browser.new_page()
    page.goto("https://www.google.com")

    print("Page Title:", page.title())
    print("Current URL:", page.url)
    page.wait_for_timeout(5000)

    browser.close()
    

