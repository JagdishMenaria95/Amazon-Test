from selenium.webdriver.common.by import By
from Pages.Home_page import HomePage
from Core.base_page import BasePage

class LoginPage(BasePage):
    url = "https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    Number = (By.ID, "ap_email_login")
    Password = (By.XPATH, "//*[@id='ap_password']")
    Continue = (By.XPATH, "//*[@id='continue']/span/input")
    login_button = (By.ID, "signInSubxmit")

    def open_page(self):
        self.open(self.url)

    def get_number_value(self):
        return self.get_value(self.Number)

    def login(self, Number, Password):
        self.enter_text(self.Number, "8005879400")
        self.click(self.wait_for_password)
        self.enter_text(self.Password, "Test@123")
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.ERROR)

    def test_existing_customer_login(driver):
        number = "8005879400"
        password = "Test@123"
        home = HomePage(driver)
        home.open_page()
        login_page = home.click_login()
        login_page.login(number, password)
        assert home.is_logged_in()