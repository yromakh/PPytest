import re
import time

from playwright.sync_api import Page, expect

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com/ncr")
    
# only for chromium headless mode, 1 single context
def test_playwrightShortCut(page):
    page.goto("https://google.com/ncr")
    
# sites for practice 
def test_open_practice_site(page: Page):
    page.goto("https://rahulshettyacademy.com/practice")
    
def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("Learning@830$3mK2")
    
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    
    expect(page.get_by_role("heading", name="Shop Name")).to_be_visible()
    # assert "Shop Name" in page.title()
    time.sleep(5)

def test_user_is_redirected_to_interview_page_successfully(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Free Access to InterviewQues/").click()
    page1 = page1_info.value
    expect(page1.get_by_role("heading", name="Documents request")).to_be_visible()
    
    time.sleep(5)
    