import allure
from playwright.sync_api import sync_playwright


@allure.title("Verify Google Search Box")
@allure.description("Verify that the Google search box is visible.")
def test_google_search_box():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.google.com")

        search_box = page.get_by_role("combobox", name="Search")

        assert search_box.is_visible()

        browser.close()