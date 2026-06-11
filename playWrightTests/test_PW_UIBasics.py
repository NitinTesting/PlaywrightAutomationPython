import pytest
from playwright.sync_api import Playwright, Page, expect


def test_Ui_basic(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    username = page.locator("#username")
    password = page.get_by_label("Password:")
    username.fill("rahulshettyacademy")
    password.fill("Learning@830$3mK2")
    box = password.bounding_box()
    w = box.get("width")
    h = box.get("height")

    user = page.get_by_role("combobox")
    user.select_option("consult")
    page.get_by_label("User", exact=True).click()
    page.locator("#okayBtn").click()
    sign_in = page.get_by_role("button", name="Sign In")
    sign_in.click()

@pytest.mark.nitin
def test_childWindow_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    blinkingTxt = page.locator(".blinkingText")
    with page.expect_popup() as new_page_info:
        blinkingTxt.first.click()
        newPage = new_page_info.value
    visibleEmail = newPage.locator(".red a")
    visibleEmailText = visibleEmail.text_content()
    domain = visibleEmailText.split("@")[1]
    user_name = domain.split(".")[0]
    print(user_name)
    newPage.close()
    username = page.locator("#username")
    password = page.get_by_label("Password:")
    username.fill(user_name)
    password.fill("Learning@830$3mK2")
    page.screenshot(path="scshot.png")
    sign_in = page.get_by_role("button", name="Sign In")
    sign_in.click()


def test_alertsAndPopups(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    def actionOnDealog(dialog):
        print("message on promt is: {}".format(dialog.message))
        dialog.accept()
    def actionOnDealogDismiss(dialog):
        print("message on promt is: {}".format(dialog.message))
        dialog.dismiss()

    page.on("dialog", actionOnDealog)
    page.locator("#confirmbtn").click()
    page.on("dialog", actionOnDealogDismiss)
    page.locator("#alertbtn").click()

@pytest.mark.nitin
def test_show_hide(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    displayedText = page.locator("#displayed-text")
    expect(displayedText).to_be_visible()
    hideTextBtn = page.locator("#hide-textbox")
    showTextBtn = page.locator("#show-textbox")
    hideTextBtn.click()
    expect(displayedText).to_be_hidden()
    showTextBtn.click()
    expect(displayedText).to_be_visible()

@pytest.mark.dropdown
def test_selectDropdown(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    example_dropdown = page.locator("#dropdown-class-example")
    drop = example_dropdown.locator("option").all_text_contents()
    # print(len(drop))
    # for option in drop:
    #     print(f"|{option.strip()}|")
    assert drop == ["Select","Option1", "Option2", "Option3"]
    example_dropdown.select_option(label="Option2")
    expect(example_dropdown).to_have_value("option2")
    example_dropdown.screenshot(path="dropdown.png")

@pytest.mark.sanity
def test_radio_checkbox(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    option = page.locator("#checkBoxOption2")
    option.check()
    expect(option).to_be_checked()
    option.uncheck()
    # option.click()
    expect(option).not_to_be_checked()
    radioOption3 = page.locator("[value='radio3']")
    radioOption3.check()
    expect(radioOption3).to_be_checked()
    radioOption1 = page.locator("[value='radio1']")
    radioOption1.check()
    expect(radioOption3).not_to_be_checked()


@pytest.mark.tables
def test_verify_user_age(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # #identify the column index
    table = page.locator(".tableFixHead #product")
    headings = table.locator("th")
    count = headings.count()
    req_index = 0
    for i in range(count):
        if headings.nth(i).text_content() == "Amount":
            req_index = i
    print(req_index)
    all_rows = table.locator("tr")
    req_row = all_rows.filter(has_text="Smith")
    req_columns = req_row.locator("td").nth(req_index)
    value = req_columns.text_content()
    print(value)

@pytest.mark.tabel1
def test_instructor_price(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    header_columns = page.locator("[name='courses'] th")
    headers_count = header_columns.count()
    price_header_id = 0
    for i in range(headers_count):
        if header_columns.nth(i).text_content() == "Price":
            price_header_id = i
    print(price_header_id)

    rows = page.locator("[name='courses'] tr")
    row = rows.filter(has_text="JMETER")
    each_row = row.locator("td")
    price_value = each_row.nth(price_header_id).text_content()
    print(price_value)






