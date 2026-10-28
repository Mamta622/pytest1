import pytest
import allure
from playwright.sync_api import Page,expect

@allure.feature("new enrollment")
@allure.story("create a new user")
@allure.severity(allure.severity_level.CRITICAL)
def test_enrollment(page: Page):
   page.goto("https://qa-enroll.corenroll.com/") 
   page.locator("#zip").fill("20002")
   page.locator("#gender").select_option(value="1")
                                         
   page.locator("#tier").select_option(value="IO")
   page.get_by_placeholder("mm/dd/yyy").fill("11/25/1990")
   page.get_by_role("button",name="submit").click()
   
   