from playwright.sync_api import Page, Playwright

def test_playwrightBasic(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()


    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")



#This can be used when by default we want to open chromium in headless mode
def test_playWrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


