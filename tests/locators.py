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
    NAME_INPUT = (By.ID, 'j_idt116:displayName:displayNameIdInput')
    TYPE_SELECT = (By.ID, 'j_idt116:visibility:visibilityId')
    DESCRIPTION = (By.ID, 'j_idt116:description:descriptionId')
    ADD_BUTTON = (By.NAME, 'j_idt116:j_idt204')
    ADD_MEMBER_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Add member"]')
    CANCEL_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Cancel"]')
    DELETE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Delete"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')
    SEARCH_INPUT = (By.XPATH, '//input[contains(@id, "searchPattern:searchMemberPatternId")]')
    MEMBER_ROWS = (By.XPATH, '//tr[contains(@id, "memberListId")]')
    USER_OK_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Ok"][contains(@id, "member")]')
    SELECTED_MEMBERS_SPAN = (By.ID, 'j_idt116:members:selectedMembersId')
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'
    DELETE_OK_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Ok"][contains(@id, "deleteConfirmation")]')


class ManagePeopleSelectors(object):
    """A class to hold the selectors for the `Manage People` page"""
    ADD_PERSON_BUTTON = (By.ID, 'j_idt115')
    SEARCH_BOX = (By.XPATH, '//input[@type="text"][contains(@id, "search")]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Search"]')
    USER_LIST_TABLE = (By.ID, 'personsFormId:personsListId')
    ERROR_SPAN = (By.XPATH, '//span[@class="error"]')


class UpdateUserSelectors(object):
    """A class to hold the `Update User` page selectors"""
    USERNAME = (By.ID, 'j_idt119:j_idt203:0:j_idt205:0:j_idt206:custIdInput')
    FIRST_NAME = (By.ID, 'j_idt119:j_idt203:1:j_idt205:0:j_idt206:custIdInput')
    DISPLAY_NAME = (By.ID, 'j_idt119:j_idt203:2:j_idt205:0:j_idt206:custIdInput')
    LAST_NAME = (By.ID, 'j_idt119:j_idt203:3:j_idt205:0:j_idt206:custIdInput')
    EMAIL = (By.ID, 'j_idt119:j_idt203:4:j_idt205:0:j_idt206:custIdInput')
    ADD_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Add"]')
    CANCEL_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Cancel"]')

