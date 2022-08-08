from Pages.policy_page import PolicyPage
from Pages.config_page import  ConfigPage
from Pages.workflow_page import WorkflowPage
from Pages.users_page import UserPage
import pytest
import time
from selenium.webdriver.common.by import By

from Pages.locators import UsersPageLocators
class TestCheckboxes:
    @pytest.mark.new
    def test_guest_could_see_eighteen_checkbox(self, browser):
        #login = "biro\adm"
        #password = "Q1w2e3r4"
        link = "https://rucmserver.biro.local/icm"
        page = WorkflowPage(browser, link)
        page.open()
        time.sleep(6)
        page.go_to_configuration_page()
        page.go_to_policy_page()
        page.go_to_workflow_page()
        page.should_be_add_card_automatically_checkbox()
        page.should_be_reset_pin_enabled_checkbox()
        page.should_be_offline_unblock_checkbox()
        page.should_be_authenticate_user_checkbox()
        page.should_be_cancel_card_updating_enabled_checkbox()
        page.should_be_user_can_add_card_checkbox()
        page.should_be_user_can_assign_card_checkbox()
        page.should_be_user_can_revoke_card_checkbox()
        page.should_be_user_can_enable_card_checkbox()
        page.should_be_user_can_dusable_card_checkbox()
        page.should_be_user_can_clear_card_checkbox()
        page.should_be_user_can_reset_pin_checkbox()
        page.should_be_user_can_update_card_checkbox()
        page.should_be_user_can_select_optional_certificates_checkbox()
        page.should_be_edit_catalog_data_checkbox()
        page.should_be_answer_security_questions_checkbox()
        page.should_be_can_change_security_questions_checkbox()
        page.should_be_certificate_tracing_checkbox()

    def test_guest_could_see_add_card_automatically_checkbox(self, browser):
        link = "https://rucmserver.biro.local/icm/Configuration/PolicyList"
        page = WorkflowPage(browser, link)
        page.open()
        page.go_to_policy_page()
        page.go_to_workflow_page()
        page.should_be_add_card_automatically_checkbox()
    @pytest.mark.print
    def test_print_subject(self, browser):
        link = "https://rucmserver.biro.local/icm"
        page = UserPage(browser, link)
        page.open()
        time.sleep(10)
        #page.log_in("biro\/adm", "Q1w2e3r4")
        #time.sleep(10)
        page.go_to_user_profile()
        page.ussue_card_to_user(*UsersPageLocators.CHECK_BOX_TEMPLATE_MSCA)
        page.should_be_card_panel()
        page.print_certificate()
        page.revoke_card()
        page.withdraw_card()

    @pytest.mark.issuance_msca
    def test_card_issuance_with_msca(self, browser):
        link = "https://rucmserver.biro.local/icm"
        page = UserPage(browser, link)
        page.open()
        time.sleep(5)
        page.go_to_user_profile()
        page.ussue_card_to_user_with_msca(*UsersPageLocators.CHECK_BOX_TEMPLATE_MSCA)
        page.should_be_card_panel()

    @pytest.mark.issuance_cpca
    def test_card_issuance_with_cpca(self, browser):
        link = "https://rucmserver.biro.local/icm"
        page = UserPage(browser, link)
        page.open()
        page.go_to_user_profile()
        page.ussue_card_to_user_with_cpca(*UsersPageLocators.CHECK_BOX_TEMPLATE_CPCA)
        page.should_be_card_panel()
    @pytest.mark.withdraw
    def test_card_withdraw(self, browser):
        link = "https://rucmserver.biro.local/icm"
        page = UserPage(browser, link)
        page.open()
        page.go_to_user_profile()
        page.should_be_card_panel()
        page.revoke_card()
        page.withdraw_card()