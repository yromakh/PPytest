from playwright.sync_api import Page, expect

def test_ui_validation_dynamic_script(page: Page):
    # iphone X, Nokia Edge -> verify 2 items are displayed on 'Checkout ( 0 )' button
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("Learning@830$3mK2")    
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    
    # when 'locator' is used then 'filter' function is used to find/filter a proper value
    iphone_product = page.locator("app-card").filter(has_text="iphone X")   
    nokia_edge_product = page.locator("app-card").filter(has_text="Nokia Edge") 
    
    # when 'get_by_role/text/label/title' etc. is used then filtering is used inside the function itself
    iphone_product.get_by_role("button", name="Add").click()
    nokia_edge_product.get_by_role("button", name="Add").click()  
    expect(page.get_by_text("Checkout ( 2 )")).to_be_visible()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    
def test_child_window_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    with page.expect_popup() as new_page_info:
        # new page is triggered
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues").click() 
        # page.get_by_text("Free Access to InterviewQues").click() 
        
        childPage = new_page_info.value
        text = childPage.locator(".im-para.red").text_content()
        print(text)
        # expect(childPage.locator(".im-para.red")).to_contain_text("mentor@rahulshettyacademy.com")
        words = str(text).split("at")
        print(words[1])
        email = words[1].strip().split()[0].strip()
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
    