import pytest
import allure
from playwright.sync_api import Page,expect


@allure.feature("demoQa login")
@allure.story("verify login page")

def test_valid_login(page: Page):
    page.goto("https://demoqa.com/login")
    page.locator("#userName").fill("Mamta Dhami")
    page.locator("#password").fill("ilovebtsv@7")
    
    page.locator("#login").click()
   
    expect(page.locator("#output")).to_contain_text("Invalid username or password")
print("invalid login test passed")
    
