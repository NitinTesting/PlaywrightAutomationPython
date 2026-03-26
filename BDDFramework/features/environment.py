from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

#runs before all
def before_all(context):
    context.playwright = sync_playwright().start()
    load_dotenv()

def before_scenario(context, scenario):
    print("Starting the scenario{}".format(scenario.name))
    context.browser = context.playwright.chromium.launch(headless=False)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

def after_scenario(context, scenario):
    context.page.close()
