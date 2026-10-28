import pytest
import allure
from playwright.sync_api import Page,expect
@allure.feature("cart box")
@allure.story("verify cart box")

@allure.feature("Daraz Seller")
@allure.feature("verify valid seller")

@allure.feature("Daraz Login")
@allure.story("Verify login page")

@allure.severity(allure.severity_level.CRITICAL)

def test_valid_login(page:Page):
    page.goto("https://www.daraz.com.np/#?")
    page.get_by_role("link",name="Login",exact=True).click()
    page.get_by_placeholder("please enter your Phone or Email").fill("mamtadhami891@gmail.com")
    page.get_by_placeholder("please enter your password").fill("ilovebtsv@7")
    page.locator(".iweb-button-mask").click()
    page.locator('input[type="search"]').fill("earbuds")
    page.keyboard.press("Enter")
    page.locator('[type="product"]').first.click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to cart").click()
    
def test_valid_seller(page:Page):
    page.goto("https://www.daraz.com.np/#?")
    page.get_by_role("link",name="Become a Seller",exact=True).click()
    
    def test_cartbox(page:Page):
        page.goto("https://www.daraz.com.np/#?")
        page.locator("#myAccountTrigger").click()
    
    
    
    
    
    
    