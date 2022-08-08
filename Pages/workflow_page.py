from .config_page import ConfigPage
from .policy_page import PolicyPage
from .locators import ConfigPageLocators
from .locators import WorkflowPageLocators
class WorkflowPage(PolicyPage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def should_be_add_card_automatically_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.ADD_CARD_AUTOMATICALLY_CHECKBOX), "Add card automatically checkbox is not presented"

    def should_be_reset_pin_enabled_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.RESET_PIN_ENABLED_CHECKBOX), "Reset pin enabled checkbox is not presented"

    def should_be_offline_unblock_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.OFFLINE_UNBLOCK_CHECKBOX), "Offline unblock checkbox is not presented"

    def should_be_authenticate_user_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.AUTHENTICATE_USER_CHECKBOX), "Authenticate_ user checkbox is not presented"

    def should_be_cancel_card_updating_enabled_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.CANCEL_CARD_UPDATING_ENABLED_CHECKBOX), "Cancel card updating enabled checkbox is not presented"

    def should_be_user_can_add_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_ADD_CARD_CHECKBOX), "User can add card checkbox is not presented"

    def should_be_user_can_assign_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_ASSIGN_CARD_CHECKBOX), "User can assign card checkbox is not presented"

    def should_be_user_can_revoke_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_REVOKE_CARD_CHECKBOX), "User can revoke card checkbox is not presented"

    def should_be_user_can_enable_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_ENABLE_CARD_CHECKBOX), "User can enable card checkbox is not presented"

    def should_be_user_can_dusable_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_DISABLE_CARD_CHECKBOX), "User can disable card checkbox is not presented"

    def should_be_user_can_clear_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_CLEAR_CARD_CHECKBOX), "User can clear card checkbox is not presented"

    def should_be_user_can_reset_pin_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_RESET_PIN_CHECKBOX), "User can reset PIN checkbox is not presented"

    def should_be_user_can_update_card_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_UPDATE_CARD_CHECKBOX), "User can update card checkbox is not presented"

    def should_be_user_can_select_optional_certificates_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.USER_CAN_SELECT_OPTIONAL_CERTIFICATES_CHECKBOX), "User can select optional certificates checkbox is not presented"

    def should_be_edit_catalog_data_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.EDIT_CATALOG_DATA_CHECKBOX), "Edit catalog data checkbox is not presented"

    def should_be_answer_security_questions_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.ANSWER_SECURITY_QUESTIONS_CHECKBOX), "Answer security questions checkbox is not presented"

    def should_be_can_change_security_questions_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.CAN_CHANGE_SECURITY_QUESTIONS_CHECKBOX), "can change security auestions checkbox is not presented"

    def should_be_certificate_tracing_checkbox(self):
        assert self.is_element_present(*WorkflowPageLocators.CERTIFICATE_TRACING_CHECKBOX), "Certificate tracing checkbox is not presented"
