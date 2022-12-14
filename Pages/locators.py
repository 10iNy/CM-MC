from selenium.webdriver.common.by import By
#from conftest import user_ID

class BasePageLocators():
    USERS_PAGE = (By.CSS_SELECTOR, "[href = '/icm/']")
    CARDS_PAGE = (By.CSS_SELECTOR, "[href='/icm/CardRepository']")
    AUDIT_PAGE = (By.CSS_SELECTOR, "[href='/icm/Audit']")
    CONFIGURATION_PAGE = (By.CSS_SELECTOR, "[href='/icm/Configuration/PolicyList']")
    AGENTS_PAGE = (By.CSS_SELECTOR, "[href*='FindAgent']")
    CUSTOM_LOG_PAGE = (By.CSS_SELECTOR, "[href*='CustomLog']")

class CardPanelLocators():
    REVOKE_CARD = (By.CSS_SELECTOR, ".nav-pills #revokeCard")
    BUTTON_REVOKE = (By.CSS_SELECTOR, "button#revoke")
    DROPDOWN_PRINT = (By.CSS_SELECTOR, "tr .dropdown-toggle")
    PRINT_CERTIFICATE = (By.CSS_SELECTOR, "li #printCertificate")
    PRINT_CERTIFICATE_REQUEST = (By.CSS_SELECTOR, "li #printCertificateRequest")
    CARD_STATUS = (By.CSS_SELECTOR, "span .label.label-default")
    WITHDRAW_CARD = (By.CSS_SELECTOR, "li #withdrawCard")
    BUTTON_WITHDRAW = (By.CSS_SELECTOR, "button#withdraw")

class UsersPageLocators():
    userID = "a019718e-1cc8-4ee7-96cc-cebc08506ed5_0588eab6-3964-4598-958c-38bbd36f6bb6"
    SEARCH_FILTER = (By.CSS_SELECTOR, "[name = 'Filter']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#user > form > div > div.col-xs-1 > button")
    TEST_USER = (By.CSS_SELECTOR, f"[href*='userId={userID}']")
    USSUE_CARD = (By.CSS_SELECTOR, "#commonCardActions > #issueCard")
    CHECK_BOX_TEMPLATE_MSCA = (By.CSS_SELECTOR, "[value='748db9d4-e7b0-4749-9d2a-e51651bd88c0']")
    CHECK_BOX_TEMPLATE_CPCA = (By.CSS_SELECTOR, "[value='6aa69b75-1634-4af1-b2b3-4952cc081cc7']")
    NEXT = (By.CSS_SELECTOR, "#next")
    ISSUE = (By.CSS_SELECTOR, "button#issue")
    CARD_PANEL = (By.CSS_SELECTOR,"[id*=panel]")
    READER_OPTION = (By.CSS_SELECTOR, "#reader > option")
    READER = (By.CSS_SELECTOR, "select#reader")
class ConfigPageLocators():
    POLICY_LIST = (By.CSS_SELECTOR, "[href*='PolicyList']")
    POLICY_LINK_LIST = (By.CSS_SELECTOR, "[href*='PolicyLinkList']")
    LICENSE_LIST = (By.CSS_SELECTOR, "[href*='LicenseList']")
    CARD_TYPE_LIST = (By.CSS_SELECTOR, "[href*='CardTypeList']")
    ROLE_LIST = (By.CSS_SELECTOR, "[href*='RoleList']")
    TAG_LIST = (By.CSS_SELECTOR, "[href*='TagList']")
    PRINT_TEMPLATE_LIST = (By.CSS_SELECTOR, "[href*='PrintTemplateList']")
    CUSTOM_LOG_DICTIONARY_LIST = (By.CSS_SELECTOR, "[href*='CustomLogDictionaryList']")
    CUSTOM_LOG_TEMPLATE_LIST = (By.CSS_SELECTOR, "[href*='CustomLogTemplateList']")
    ABOUT = (By.CSS_SELECTOR, "[href*='About']")

class PolicyListLocators():
    FIRST_POLICY = (By.CSS_SELECTOR, "[href*='policyId=1']")

class PolicyLocators():
    COMMON_SETTINGS = (By.CSS_SELECTOR, "[href*='Policy?']")
    PKI_SETTINGS = (By.CSS_SELECTOR, "[href*='PkiSettings?']")
    MS_CA_LIST = (By.CSS_SELECTOR, "[href*='MsCAList?']")
    MS_CERT_TEMPLATE_LIST = (By.CSS_SELECTOR, "[href*='MsCertTemplateList?']")
    CP2_CA_LIST = (By.CSS_SELECTOR, "[href*='Cp2CAList?']")
    CP2_CERT_TEMPLATE_LIST = (By.CSS_SELECTOR, "[href*='Cp2CertTemplateList?']")
    VD_CA_LIST = (By.CSS_SELECTOR, "[href*='VdCAList?']")
    VD_CERT_TEMPLATE_LIST = (By.CSS_SELECTOR, "[href*='VdCertTemplateList?']")
    COMMON_CERTIFICATE_LIST = (By.CSS_SELECTOR, "[href*='CommonCertificateList?']")
    SMEV_CP_GATEWAY_SETTINGS = (By.CSS_SELECTOR, "[href*='SmevCpGatewaySettings?']")
    WORKFLOW_SETTINGS = (By.CSS_SELECTOR, "[href*='WorkflowSettings']")
    ISSUANCE_SETTINGS = (By.CSS_SELECTOR, "[href*='IssuanceSettings?']")
    CARD_INITIALIZATION_SETTINGS = (By.CSS_SELECTOR, "[href*='CardInitializationSettings?']")
    ALLOWED_CARD_TYPE_LIST = (By.CSS_SELECTOR, "[href*='AllowedCardTypeList?']")
    AUTHENTICATION_SETTINGS = (By.CSS_SELECTOR, "[href*='AuthenticationSettings?']")
    SECURITY_AUESTION_LIST = (By.CSS_SELECTOR, "[href*='SecurityQuestionList?']")
    AGENT_CARD_BINDINGS_SETTINGS = (By.CSS_SELECTOR, "[href*='AgentCardBindingSettings?']")
    AGENT_CARD_TASK_MSG_SETTINGS = (By.CSS_SELECTOR, "[href*='AgentCardTaskMsgSettings?']")
    CARD_PRINTER_SETTINGS = (By.CSS_SELECTOR, "[href*='CardPrinterSettings?']")
    CARD_DESIGN_TEMPLATES = (By.CSS_SELECTOR, "[href*='CardDesignTemplate?']")
    NOTIFICATION_SETTINGS = (By.CSS_SELECTOR, "[href*='NotificationSettings?']")
    RECIPIENT_GROUP_LIST = (By.CSS_SELECTOR, "[href*='RecipientGroupList?']")
    ADMIN_NOTIFICATION_LIST = (By.CSS_SELECTOR, "[href*='AdminNotificationList?']")
    USER_NOTIFICATION_LIST = (By.CSS_SELECTOR, "[href*='UserNotificationList?']")
    ADMIN_NOTIFICATION_TEMPLATES = (By.CSS_SELECTOR, "[href*='AdminNotificationTemplates?']")
    USER_NOTIFICATION_TEMPLATES = (By.CSS_SELECTOR, "[href*='UserNotificationTemplates?']")

class WorkflowPageLocators():
    ADD_CARD_AUTOMATICALLY_CHECKBOX = (By.CSS_SELECTOR, "#AddCardAutomatically")
    RESET_PIN_ENABLED_CHECKBOX = (By.CSS_SELECTOR, "#ResetPinEnabled")
    OFFLINE_UNBLOCK_CHECKBOX = (By.CSS_SELECTOR, "#OfflineUnlockEnabled")
    AUTHENTICATE_USER_CHECKBOX = (By.CSS_SELECTOR, "#AuthenticateUser")
    CANCEL_CARD_UPDATING_ENABLED_CHECKBOX = (By.CSS_SELECTOR, "#CancelCardUpdatingEnabled")
    USER_CAN_ADD_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanAddCard")
    USER_CAN_ASSIGN_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanAssignCard")
    USER_CAN_REVOKE_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanRevokeCard  ")
    USER_CAN_ENABLE_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanEnableCard")
    USER_CAN_DISABLE_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanDisableCard")
    USER_CAN_CLEAR_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanClearCard")
    USER_CAN_RESET_PIN_CHECKBOX = (By.CSS_SELECTOR, "#UserCanResetPin")
    USER_CAN_UPDATE_CARD_CHECKBOX = (By.CSS_SELECTOR, "#UserCanUpdateCard")
    USER_CAN_SELECT_OPTIONAL_CERTIFICATES_CHECKBOX = (By.CSS_SELECTOR, "#UserCanSelectOptionalCertificates")
    EDIT_CATALOG_DATA_CHECKBOX = (By.CSS_SELECTOR, "#AllowEditCatalogDataForSmev")
    ANSWER_SECURITY_QUESTIONS_CHECKBOX = (By.CSS_SELECTOR, "#AnswerSecurityQuestions")
    CAN_CHANGE_SECURITY_QUESTIONS_CHECKBOX = (By.CSS_SELECTOR, "#CanChangeSecurityQuestions")
    CERTIFICATE_TRACING_CHECKBOX = (By.CSS_SELECTOR, "#CertificateTracingEnabled")

class SmevForm():
    SMEV_FORM = (By.CSS_SELECTOR, "div #commonCardActionContainer")
    LASTNAME = (By.CSS_SELECTOR, "#LastName")
    FIRSTNAME = (By.CSS_SELECTOR, "#FirstName")
    MIDDLENAME = (By.CSS_SELECTOR, "#MiddleName")
    GENDER = (By.CSS_SELECTOR, "#Gender")
    GENDER_MALE = (By.CSS_SELECTOR, "#Gender > [value='Male']")
    BIRTHDATE = (By.CSS_SELECTOR, "#BirthDate")
    BIRTHPLACE = (By.CSS_SELECTOR, "#BirthPlace")
    SNILS = (By.CSS_SELECTOR, "#Snils")
    INN = (By.CSS_SELECTOR, "#Inn")
    FULL_NUMBER = (By.CSS_SELECTOR, "#IdentyfyingDocument_FullNumber")
    ISSUE_DATE = (By.CSS_SELECTOR, "#IdentyfyingDocument_IssueDate")
    ISSUER = (By.CSS_SELECTOR, "#IdentyfyingDocument_Issuer")
    ISSUER_CODE = (By.CSS_SELECTOR, "#IdentyfyingDocument_IssuerCode")
    STATE_DROP_DOWN = (By.CSS_SELECTOR, ".filter-option-inner-inner")
    STATE_53 = (By.CSS_SELECTOR, "#bs-select-1-53")
    LOCATION = (By.CSS_SELECTOR, "#Address_Location")
    STREET = (By.CSS_SELECTOR, "#Address_Street")
    NEXT = (By.CSS_SELECTOR, ".form-group [type='submit']")