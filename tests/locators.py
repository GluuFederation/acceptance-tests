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


class ProfilePageSelectors(object):
    """A class to hold the selectors for the Profile page"""
    ATTR_BOX = (By.ID, 'personForm:attributeTabPanelGroupId')
    UPDATE_BUTTON = (By.XPATH, '//input[@type="submit"][@value="Update"]')
