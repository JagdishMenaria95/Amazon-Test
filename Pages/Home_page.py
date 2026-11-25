from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Core.base_page import BasePage
from Pages.Login_page import LoginPage

class HomePage(BasePage):
    url = "https://www.amazon.in/"
    SIGN_IN_LINK = (By.ID, "nav-link-accountList")
    ACCOUNT_GREETING = (By.ID, "nav-link-accountList-nav-line-1")

    def open_page(self):
        self.open(self.url)

    def click_login(self):
        self.click(self.SIGN_IN_LINK)
        return LoginPage(self.driver)

    def is_logged_in(self, timeout=15):
        def _greeting_updated(driver):
            try:
                text = driver.find_element(*self.ACCOUNT_GREETING).text.strip().lower()
                return bool(text) and "sign in" not in text
            except (NoSuchElementException, StaleElementReferenceException):
                return False

        try:
            WebDriverWait(self.driver, timeout).until(_greeting_updated)
            return True
        except TimeoutException:
            return False