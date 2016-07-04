from locators import LoginPageSelectors as LPS

from selenium.webdriver.common.keys import Keys


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

