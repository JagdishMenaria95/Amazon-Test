import os

from Pages.Home_page import HomePage


def test_existing_customer_login(driver):
    number = os.getenv("AMAZON_NUMBER", "8005879400")
    password = os.getenv("AMAZON_PASSWORD", "Test@123")

    home = HomePage(driver)
    home.open_page()

    login_page = home.click_login()
    login_page.login(number, password)

    assert home.is_logged_in(), (
        "Expected Amazon home page to display a logged-in user greeting"
    )