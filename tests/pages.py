from locators import LoginPageSelectors as LPS, OrgConfPageSelectors as OCPS

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


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
