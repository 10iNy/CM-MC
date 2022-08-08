from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .locators import ConfigPageLocators
from .locators import BasePageLocators
class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def log_in(self, login, password):
        alert = self.browser.switch_to.alert
        login = "adm"
        password = "Q1w2e3r4"
        alert.send_keys(login)
        alert.send_keys(password)
        alert.accept()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=60):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return True
        return False

    def element_is_disappeared(self, element, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.staleness_of(element))
        except TimeoutException:
            return False
        return True

    def element_is_clickable(self, how, what):

        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((how, what)))

    def go_to_users_page(self):
        link = self.browser.find_element(*BasePageLocators.USERS_PAGE)
        link.click()

    def go_to_cards_page(self):
        link = self.browser.find_element(*BasePageLocators.CARDS_PAGE)
        link.click()

    def go_to_audit_page(self):
        link = self.browser.find_element(*BasePageLocators.AUDIT_PAGE)
        link.click()

    def go_to_configuration_page(self):
        link = self.browser.find_element(*BasePageLocators.CONFIGURATION_PAGE)
        link.click()

    def go_to_agents_page(self):
        link = self.browser.find_element(*BasePageLocators.AGENTS_PAGE)
        link.click()

    def go_to_custom_log_page(self):
        link = self.browser.find_element(*BasePageLocators.CUSTOM_LOG_PAGE)
        link.click()