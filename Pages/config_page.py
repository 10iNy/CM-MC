from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ConfigPageLocators
from .locators import PolicyListLocators
from .base_page import BasePage
import time
class ConfigPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def log_in(self, login, password):
        time.sleep(5)
        try:
            #promt = self.browser.switch_to.alert
            #promt.send_keys(login)
            #promt.send_keys(KEY.TAB)
            time.sleep(1)
            #promt.send_keys(password)
            #promt.send_keys(KEY.ENTER)
            #promt.accept()
        except NoAlertPresentException:
            print("No alert presented")

    def go_to_policy_page(self):
        link = self.browser.find_element(*PolicyListLocators.FIRST_POLICY)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
