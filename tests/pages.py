from locators import LoginPageSelectors as LPS, OrgConfPageSelectors as OCPS, \
        ProfilePageSelectors as PPS

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """The login page and its actions"""

    def login(self, username, password):
        userInput = self.driver.find_element(*LPS.USERNAME_INPUT)
        userInput.clear()
        userInput.send_keys(username)
        passInput = self.driver.find_element(*LPS.PASSWORD_INPUT)
        passInput.clear()
        passInput.send_keys(password)
        passInput.send_keys(Keys.RETURN)

    def message(self):
        return self.driver.find_element(*LPS.MESSAGES).text


class HomePage(BasePage):
    """The home page dashboard"""

    pass


class OrganizationConfigPage(BasePage):
    """The Organization Configuration Page"""

    def enable_white_pages(self):
        select = Select(self.driver.find_element(*OCPS.WHITE_PAGES_SELECT))
        select.select_by_value(OCPS.ENABLED_VALUE)
        self.driver.find_element(*OCPS.UPDATE_BUTTON).click()

    def disable_white_pages(self):
        select = Select(self.driver.find_element(*OCPS.WHITE_PAGES_SELECT))
        select.select_by_value(OCPS.DISABLED_VALUE)
        self.driver.find_element(*OCPS.UPDATE_BUTTON).click()

    def enable_self_password_reset(self):
        select = Select(self.driver.find_element(*OCPS.PASSWORD_RESET_SELECT))
        select.select_by_value(OCPS.ENABLED_VALUE)
        self.driver.find_element(*OCPS.UPDATE_BUTTON).click()

    def disable_self_password_reset(self):
        select = Select(self.driver.find_element(*OCPS.PASSWORD_RESET_SELECT))
        select.select_by_value(OCPS.DISABLED_VALUE)
        self.driver.find_element(*OCPS.UPDATE_BUTTON).click()

    def enable_profile_editing(self):
        select = Select(self.driver.find_element(*OCPS.PROFILE_EDIT_SELECT))
        select.select_by_value(OCPS.ENABLED_VALUE)
        self.driver.find_element(*OCPS.UPDATE_BUTTON).click()

    def disable_profile_editing(self):
        select = Select(self.driver.find_element(*OCPS.PROFILE_EDIT_SELECT))
        select.select_by_value(OCPS.DISABLED_VALUE)
        self.driver.find_element(*OCPS.UPDATE_BUTTON).click()


class ProfilePage(BasePage):
    def is_editable(self):
        """Returns boolean if the profile has edit options or not"""
        try:
            # The Attribute Box and the Update button confirm editability
            self.driver.find_element(*PPS.ATTR_BOX)
            self.driver.find_element(*PPS.UPDATE_BUTTON)
            return True
        except NoSuchElementException:
            return False
