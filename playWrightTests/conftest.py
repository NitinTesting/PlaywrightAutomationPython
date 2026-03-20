import pytest
from playwright.sync_api import Page, Browser, Expect, Playwright
from Data.data import Data

from page_objects.poController import PoController

webContext = None
@pytest.fixture
def setupChromeBrowser(playwright:Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    return context

@pytest.fixture()
def setupFirefoxBrowser(playwright:Playwright):
    browser = playwright.firefox.launch(headless = False)
    context = browser.new_context()

    return context


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="adding browser"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client/#/auth/login", help="adding server"
    )

@pytest.fixture()
def browserInstance(playwright, request):
    global browser
    browser_name = request.config.getoption("--browser_name")
    url = request.config.getoption("--url_name")
    print(browser_name)
    if browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    poController = PoController(page)
    loginPage = poController.getLoginPage()
    credentials = Data.credentials
    loginPage.login(credentials["username"], credentials["password"], url)
    # "https://rahulshettyacademy.com/client/#/auth/login"
    yield page
    context.close()
    browser.close()



