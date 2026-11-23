from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Core.base_page import BasePage
from Tests.test_login import LoginPage

class HomePage(BasePage):
    url = "https://www.amazon.in/"
    Sign_Link = (By.XPATH, "//*[@id='nav-link-accountList']")

    def open_page(self):
        self.open(self.url)

    def click_login(self):
        self.click(self.Sign_Link)
        return LoginPage(self.driver)

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 15).until(lambda d: "Sign In" not in d.find_element(*self.Sign_In_Link).text.lower())
            return True
        except TimeoutException:
            return False