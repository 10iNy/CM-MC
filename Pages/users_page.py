from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ConfigPageLocators
from .locators import UsersPageLocators
from.locators import CardPanelLocators
from .locators import SmevForm

from .config_page import ConfigPage
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
class UserPage(BasePage):

    def __init__(self, browser, url, timeout=60):
        self.browser = browser
        self.url = url

    def should_be_card_panel(self):
        assert self.is_element_present(*UsersPageLocators.CARD_PANEL), \
           "Card panel is not present."

    def should_not_be_card_panel(self):
        assert self.is_not_element_present(*UsersPageLocators.CARD_PANEL), \
           "Card panel is present."
    def go_to_user_profile(self):
        self.browser.find_element(*UsersPageLocators.SEARCH_FILTER).send_keys('*')
        search_button = self.browser.find_element(*UsersPageLocators.SEARCH_BUTTON)
        search_button.click()
        test_user = self.browser.find_element(*UsersPageLocators.TEST_USER)
        test_user.click()
    def ussue_card_to_user_with_msca(self, how, what):
        self.browser.find_element(*UsersPageLocators.USSUE_CARD).click()
        self.browser.find_element(how, what).click()
        self.browser.find_element(*UsersPageLocators.NEXT).click()
        button = self.element_is_clickable(*UsersPageLocators.ISSUE)
        button.click()
    def revoke_card(self):
        self.browser.find_element(*CardPanelLocators.REVOKE_CARD).click()
        self.browser.find_element(*CardPanelLocators.BUTTON_REVOKE).click()
        self.should_be_revoke_card()

    def withdraw_card(self):
        self.browser.find_element(*CardPanelLocators.WITHDRAW_CARD).click()
        button = self.browser.find_element(*CardPanelLocators.BUTTON_WITHDRAW)
        button.click()
        card_panel = self.browser.find_element(*UsersPageLocators.CARD_PANEL)
        self.element_is_disappeared(card_panel)

    def print_certificate(self):
        self.browser.find_element(*CardPanelLocators.DROPDOWN_PRINT).click()
        self.browser.find_element(*CardPanelLocators.PRINT_CERTIFICATE).click()

    def print_request(self):
        self.browser.find_element(*CardPanelLocators.DROPDOWN_PRINT).click()
        self.browser.find_element(*CardPanelLocators.PRINT_CERTIFICATE_REQUEST).click()

    def should_be_revoke_card(self):
        status = self.browser.find_element(*CardPanelLocators.CARD_STATUS).text
        assert status == "Отозвано", f"Устройство имеет статус {status}"

    def ussue_card_to_user_with_cpca(self, how, what):
        self.browser.find_element(*UsersPageLocators.USSUE_CARD).click()
        self.browser.find_element(how, what).click()
        self.browser.find_element(*UsersPageLocators.NEXT).click()
        self.filling_fields()
        self.should_be_connected_card()
        #self.browser.find_element(*UsersPageLocators.NEXT).click()
        button = self.element_is_clickable(*UsersPageLocators.ISSUE)
        button.click()

    def filling_fields(self):
        self.is_element_present(*SmevForm.SMEV_FORM)
        check = self.browser.find_element(*SmevForm.LASTNAME)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('Шилков')
        check = self.browser.find_element(*SmevForm.FIRSTNAME)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('Антонио')
        check = self.browser.find_element(*SmevForm.MIDDLENAME)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('Петровичен')

        check = self.browser.find_element(*SmevForm.GENDER)
        self.browser.find_element(*SmevForm.GENDER_MALE).click()

        check = self.browser.find_element(*SmevForm.BIRTHDATE)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('12.01.1985')

        check = self.browser.find_element(*SmevForm.BIRTHPLACE)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('2 родильное отделение по г. Окуловка')

        check = self.browser.find_element(*SmevForm.SNILS)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('00100100112')

        check = self.browser.find_element(*SmevForm.INN)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('012345678912')

        check = self.browser.find_element(*SmevForm.FULL_NUMBER)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('0123012345')

        check = self.browser.find_element(*SmevForm.ISSUE_DATE)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('01.01.2011')

        check = self.browser.find_element(*SmevForm.ISSUER)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('Олег Евгеньевич')

        check = self.browser.find_element(*SmevForm.ISSUER_CODE)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('012012')

        check = self.browser.find_element(*SmevForm.STATE_DROP_DOWN)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.click()
            self.browser.find_element(*SmevForm.STATE_53).click()

        check = self.browser.find_element(*SmevForm.LOCATION)
        check_value = check.get_attribute("value")
        if check_value == "":
            check.send_keys('Великий Новгород')

        check = self.browser.find_element(*SmevForm.STREET)
        check.send_keys('ул. Ломоносова, д. 23/18')
        self.browser.find_element(*SmevForm.NEXT).click()

    def should_be_connected_card(self):
        self.is_element_present(*UsersPageLocators.READER)
        device = self.browser.find_element(*UsersPageLocators.READER_OPTION)
        assert device != None, "Card not connected."