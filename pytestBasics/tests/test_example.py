import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
# {"username":"Nqatest@gmail.com","password":"testQA@1111"}
def test_login_basic(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("//input[@type='email']").fill("Nqatest@gmail.com")
    page.locator("//input[@type='password']").fill("testQA@1111")
    page.locator("//input[@id='login']").click()
    page.get_by