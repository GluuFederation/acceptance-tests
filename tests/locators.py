from selenium.webdriver.common.by import By


class LoginPageSelectors(object):
    """A class to hold the locators for the Login Page"""
    USERNAME_INPUT = (By.ID, 'loginForm:username')
    PASSWORD_INPUT = (By.ID, 'loginForm:password')
    MESSAGES = (By.ID, 'messages')

