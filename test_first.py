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


from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()
        
        page.goto("https://iprouk-testing.azurewebsites.net/login")
        
        page.get_by_label("Username/Mobile No.").fill("923040217492")
        page.get_by_label("Password", exact=True).fill("1122")
        page.get_by_role("button", name="Log in").click()
        
        page.wait_for_load_state("networkidle")
        page.get_by_text("Pharmacy", exact=True).click()
        
        page.wait_for_load_state("networkidle")
        page.get_by_text("Zainab Zaib").click()
        page.wait_for_timeout(1000)
        
        page.click(".js-logout-btn")
        
        page.wait_for_load_state("networkidle")
        if page.get_by_label("Username/Mobile No.").is_visible():
            print("Status: Success")
        
        browser.close()

if __name__ == "__main__":
    run_test()