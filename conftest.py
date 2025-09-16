
from selene import browser
import pytest

@pytest.fixture()
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

@pytest.fixture()
def open_browser(browser_size):
    browser.open('https://demoqa.com/automation-practice-form')

    yield browser
    browser.quit()

