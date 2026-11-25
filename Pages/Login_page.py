from selenium.webdriver.common.by import By

from Core.base_page import BasePage


class LoginPage(BasePage):
    URL = (
        "https://www.amazon.in/ap/signin"
        "?openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin"
        "&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
        "&openid.assoc_handle=inflex"
        "&openid.mode=checkid_setup"
        "&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
        "&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    )

    EMAIL_OR_PHONE_INPUT = (By.CSS_SELECTOR, "#ap_email_login, #ap_email")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input#continue, #continue input[type='submit']")
    PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "#auth-error-message-box .a-alert-content, .a-alert-error .a-alert-content",
    )

    def open_page(self):
        self.open(self.URL)

    def get_number_value(self):
        return self.get_value(self.EMAIL_OR_PHONE_INPUT)

    def enter_number(self, number):
        self.enter_text(self.EMAIL_OR_PHONE_INPUT, number)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def enter_password(self, password):
        self.wait_for_visible(self.PASSWORD_INPUT)
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def login(self, number, password):
        self.enter_number(number)
        self.click_continue()
        self.enter_password(password)
        self.click_sign_in()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)