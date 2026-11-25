import pytest
from Core.driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, firefox, edge, safari",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    browser_driver = DriverFactory.get_driver(browser)
    yield browser_driver
    browser_driver.quit()