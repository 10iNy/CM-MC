from .config_page import ConfigPage
from .locators import PolicyLocators
class PolicyPage(ConfigPage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_common_page(self):
        link = self.browser.find_element(*PolicyLocators.COMMON_SETTINGS)
        link.click()

    def go_to_PKI_settings_page(self):
        link = self.browser.find_element(*PolicyLocators.PKI_SETTINGS)
        link.click()

    def go_to_MSCA_page(self):
        link = self.browser.find_element(*PolicyLocators.MS_CA_LIST)
        link.click()

    def go_to_MSCA_cert_template_page(self):
        link = self.browser.find_element(*PolicyLocators.MS_CERT_TEMPLATE_LIST)
        link.click()

    def go_to_CPCA_page(self):
        link = self.browser.find_element(*PolicyLocators.CP2_CA_LIST)
        link.click()

    def go_to_CPCA_cert_template_page(self):
        link = self.browser.find_element(*PolicyLocators.CP2_CERT_TEMPLATE_LIST)
        link.click()

    def go_to_VDCA_page(self):
        link = self.browser.find_element(*PolicyLocators.VD_CA_LIST)
        link.click()

    def go_to_VDCA_cert_template_page(self):
        link = self.browser.find_element(*PolicyLocators.VD_CERT_TEMPLATE_LIST)
        link.click()

    def go_to_common_certificate_page(self):
        link = self.browser.find_element(*PolicyLocators.COMMON_CERTIFICATE_LIST)
        link.click()

    def go_to_SMEV_page(self):
        link = self.browser.find_element(*PolicyLocators.SMEV_CP_GATEWAY_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_issuance_page(self):
        link = self.browser.find_element(*PolicyLocators.ISSUANCE_SETTINGS)
        link.click()

    def go_to_card_initialization_page(self):
        link = self.browser.find_element(*PolicyLocators.CARD_INITIALIZATION_SETTINGS)
        link.click()

    def go_to_allow_cards_page(self):
        link = self.browser.find_element(*PolicyLocators.ALLOWED_CARD_TYPE_LIST)
        link.click()

    def go_to_authentication_page(self):
        link = self.browser.find_element(*PolicyLocators.AUTHENTICATION_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

    def go_to_workflow_page(self):
        link = self.browser.find_element(*PolicyLocators.WORKFLOW_SETTINGS)
        link.click()

