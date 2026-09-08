import time

from playwright.sync_api import Page, expect

# added test to check UI elements, js alerts, frame elements and table data receiving

def test_ui_checks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
 
def handle_dialog(dialog):
    print(dialog.message)
    time.sleep(2)
    dialog.accept()
    
def test_javascript_alerts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise/")
    
    page.get_by_placeholder("Enter Your Name").fill("John")
    page.on("dialog", lambda dialog: handle_dialog(dialog))
    page.get_by_role("button", name="Alert").click()
    
    page.get_by_placeholder("Enter Your Name").fill("Will")
    page.on("dialog", lambda dialog: handle_dialog(dialog)) 
    page.get_by_role("button", name="Confirm").click()
    
    # JavaScript alerts are not handled by HTML 

def test_frame_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise/")
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")

# check the rice price is equal to 37
def test_web_tables(page: Page):
    # identify the price column
    # identify the rice row 
    # extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    priceColVal = 0 
    # identify the price column
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColVal = index
            print(f"index of column Price {priceColVal}")
            break
        
    # identify the rice row 
    rice_row = page.locator("tr").filter(has_text="Rice")
    # extract the price of the rice
    expect(rice_row.locator("td").nth(priceColVal)).to_contain_text("37")
    
def test_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise/")
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Top").click()
            
    