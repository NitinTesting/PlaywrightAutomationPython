from playwright.sync_api import Page, Playwright

def test_broken_link(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    api_context = playwright.request.new_context()
    page.goto("https://www.zeeclick.com/")
    links = page.locator("a[href]").all()
    for link in links:
        href = link.get_attribute("href")
        if href == "#":
            continue
        else:
            response = api_context.get(href)
            if response.status == 404:
                print(f"{href}: has status as {response.status}")





