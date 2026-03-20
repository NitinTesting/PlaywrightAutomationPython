import pytest
from pytest_playwright.pytest_playwright import browser

file_name = "playWrightTests/test_end2end.py"
test_case = "test_endToEnd_scenario"
test_browser = "chromium"

config_singleTest = [
        "-v",
        "-s",
        "--browser={}".format(test_browser),
        "--headed",
        "--tracing=on",
        "--html=report.html",
        "{}::{}".format(file_name,test_case)   # 👈 your test folder
    ]

if __name__ == "__main__":
    pytest.main(config_singleTest)