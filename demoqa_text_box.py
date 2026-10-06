import pytest
import allure
from playwright.sync_api import Page, expect


@allure.feature("DemoQA Textbox")
@allure.story("Verify valid Full Name")
def test_valid_name(page: Page):
    page.goto("https://demoqa.com/text-box")

    page.locator("#userName").fill("Mamta Dhami")
    page.locator("#userEmail").fill("mamtadhami891@gmail.com")
    page.locator("#currentAddress").fill("Dhangadhi,Jugeda")
    page.locator("#permanentAddress").fill("Bajhang,Dewal")
    page.locator("#submit").click()
    
    expect(page.locator("#output")).to_contain_text("Name:Mamta Dhami")
    print("submit successsful")
    