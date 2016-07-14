from selenium.webdriver.common.by import By


class LoginPageSelectors(object):
    """A class to hold the locators for the Login Page"""
    USERNAME_INPUT = (By.ID, 'loginForm:username')
    PASSWORD_INPUT = (By.ID, 'loginForm:password')
    MESSAGES = (By.ID, 'messages')


class OrgConfPageSelectors(object):
    """A class to hold the selectors for the Organization Configuration Page"""
    ENABLED_VALUE = 'ENABLED'
    ENABLED_TEXT = 'Enabled'
    DISABLED_VALUE = 'DISABLED'
    DISABLED_TEXT = 'Disabled'

    WHITE_PAGES_SELECT = (By.ID, 'organizationForm:whitePages:whitePagesId')
    PASSWORD_RESET_SELECT = (By.ID, 'organizationForm:passwordReset:passwordResetId')
    SCIM_SELECT = (By.ID, 'organizationForm:scimEnabledState:scimEnabledStateId')
    PROFILE_EDIT_SELECT = (By.ID, 'organizationForm:profileManagment:profileManagmentStateId')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')


class MenuItems(object):
    """A class to hold the selectors for the menu item links"""
    ORG_CONF = (By.PARTIAL_LINK_TEXT, 'Organization Configuration')
    WHITE_PAGES = (By.PARTIAL_LINK_TEXT, 'White Pages')
    CONFIG = (By.PARTIAL_LINK_TEXT, 'Configuration')
    PERSONAL = (By.PARTIAL_LINK_TEXT, 'Personal')
    PROFILE = (By.PARTIAL_LINK_TEXT, 'Profile')
    USERS = (By.PARTIAL_LINK_TEXT, 'Users')
    MANAGE_GROUPS = (By.PARTIAL_LINK_TEXT, 'Manage Groups')
    MANAGE_PEOPLE = (By.PARTIAL_LINK_TEXT, 'Manage People')
    IMPORT_PEOPLE = (By.PARTIAL_LINK_TEXT, 'Import People')
    OPENID_CONNECT = (By.PARTIAL_LINK_TEXT, 'OpenID Connect')
    SCOPES = (By.PARTIAL_LINK_TEXT, 'Scopes')
    CLIENTS = (By.PARTIAL_LINK_TEXT, 'Clients')


class ProfilePageSelectors(object):
    """A class to hold the selectors for the Profile page"""
    ATTR_BOX = (By.ID, 'personForm:attributeTabPanelGroupId')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')


class GroupSelectors(object):
    """A class to hold the selectors for the `Manage Groups` page"""
    SEARCH_BOX = (By.XPATH, '//input[@type="text"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    GROUPS_TABLE = (By.ID, 'groupsFormId:groupsListId')


class AddGroupSelectors(object):
    """A class to hold the selectors for the `Add Group` page"""
    NAME_INPUT = (By.ID, 'j_idt118:displayName:displayNameIdInput')
    TYPE_SELECT = (By.ID, 'j_idt118:visibility:visibilityId')
    DESCRIPTION = (By.ID, 'j_idt118:description:descriptionId')
    ADD_BUTTON = (By.NAME, 'j_idt118:j_idt206')
    ADD_MEMBER_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Add member"]')
    CANCEL_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Cancel"]')
    DELETE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Delete"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')
    SEARCH_INPUT = (By.XPATH, '//input[contains(@id, "searchPattern:searchMemberPatternId")]')
    MEMBER_ROWS = (By.XPATH, '//tr[contains(@id, "memberListId")]')
    USER_OK_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Ok"][contains(@id, "member")]')
    SELECTED_MEMBERS_SPAN = (By.ID, 'j_idt118:members:selectedMembersId')
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'
    DELETE_OK_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Ok"][contains(@id, "deleteConfirmation")]')


class ManagePeopleSelectors(object):
    """A class to hold the selectors for the `Manage People` page"""
    ADD_PERSON_BUTTON = (By.ID, 'j_idt117')
    SEARCH_BOX = (By.XPATH, '//input[@type="text"][contains(@id, "search")]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    USER_LIST_TABLE = (By.ID, 'personsFormId:personsListId')
    ERROR_SPAN = (By.XPATH, '//span[@class="error"]')
    SEARCH_RESULT_FORM = (By.ID, 'personsFormId')


class UpdateUserSelectors(object):
    """A class to hold the `Update User` page selectors"""
    USERNAME = (By.ID, 'j_idt121:j_idt204:0:j_idt206:0:j_idt207:custIdInput')
    FIRST_NAME = (By.ID, 'j_idt121:j_idt204:1:j_idt206:0:j_idt207:custIdInput')
    DISPLAY_NAME = (By.ID, 'j_idt121:j_idt204:2:j_idt206:0:j_idt207:custIdInput')
    LAST_NAME = (By.ID, 'j_idt121:j_idt204:3:j_idt206:0:j_idt207:custIdInput')
    EMAIL = (By.ID, 'j_idt121:j_idt204:4:j_idt206:0:j_idt207:custIdInput')
    PASSWORD = (By.ID, 'j_idt121:j_idt204:5:j_idt206:0:j_idt207:custIdInput')
    STATUS = (By.ID, 'j_idt121:j_idt204:6:j_idt206:0:j_idt207:statusId')

    ADD_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Add"]')
    CANCEL_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Cancel"]')
    CHANGE_PW_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Change Password"]')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')
    DELETE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Delete"]')
    DELETE_CONFIRM_OK = (By.XPATH, '//input[@type="submit"][@value="Ok"]')


class ImportPeopleSelectors(object):
    """A class to hold the selectors for the Import People page"""
    FILE_INPUT = (By.XPATH, '//input[@type="file"]')
    IMPORT_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Import"]')
    VALIDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Validate"]')


class ScopeSelectors(object):
    """A class to hold the selectors for the OpenID Connect Scopes page"""
    SEARCH_BOX = (By.XPATH, '//input[@type="text"][contains(@id, "searchPatternId")]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    ADD_SCOPE_BUTTON = (By.LINK_TEXT, 'Add Scope')


class AddScopeSelectors(object):
    """A class to hold the selectors of the Add Scope page of OpenID Connect"""
    NAME = (By.ID, 'scopeForm:displayName:displayNameIdInput')
    DESCRIPTION = (By.ID, 'scopeForm:description:descriptionId')
    SCOPE_TYPE = (By.NAME, 'scopeForm:j_idt162:j_idt173')
    DEFAULT_SCOPE = (By.NAME, 'scopeForm:j_idt179:j_idt190')
    OPENID = 'OPENID'
    LDAP = 'LDAP'
    DYNAMIC = 'DYNAMIC'
    ADD_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Add"]')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')
    DELETE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Delete"]')
    ADD_CLAIM_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Add Claim"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    CHECKBOX = (By.XPATH, '//input[@type="checkbox"][contains(@name, "claim")]')
    OK_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Ok"][contains(@id, "claim")]')
    CLAIMS_SPAN = (By.ID, 'scopeForm:claims:selectedClaimsId')
    CLAIM_REMOVE = (By.XPATH, '//a[contains(@id, "scopeForm:claims")]')
    SEARCH_BOX = (By.XPATH, '//input[@type="text"][contains(@name, "searchPattern")]')
    DELETE_CONFIRM_OK = (By.XPATH, '//input[@type="submit"][contains(@id, "deleteConfirmation")]')


class ClientSelectors(object):
    """A class to hold the selectors of the OpenID Connect Clients page"""
    SEARCH_BOX = (By.XPATH, '//input[@type="text"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    ADD_CLIENT_BUTTON = (By.LINK_TEXT, 'Add Client')


class AddClientSelectors(object):
    """A class to hold the selectors of the Add client page"""
    pass
