from selenium.webdriver.common.by import By
from Core.base_page import BasePage
from Pages.Login_page import Login_page

class HomePage(BasePage):
    url = "https://www.amazon.in/"
    Sign_Link = (By.ID, "nav-link-accountList")

    def open_page(self):
        self.open(self.url)

    def click_login(self):
        self.click(self.Sign_Link)
        return Login_page(self.driver)