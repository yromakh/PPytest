from page_objects.dashboard import DashboardPage

class LoginPage:
    def __init__(self, page):
        self._page = page
        
    def navigate(self):
        self._page.goto("https://rahulshettyacademy.com/client/")
        
    def login(self, _user_name, _user_password):
        self._page.get_by_placeholder("email@example.com").fill(_user_name)
        self._page.get_by_role("textbox", name="enter your passsword").fill(_user_password)    
        self._page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self._page)
        return dashboard_page