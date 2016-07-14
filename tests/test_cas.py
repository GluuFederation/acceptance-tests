import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage


class CASLoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_login_success(self):
        """Admin can login with the password.
        """
        # Step 1: Open the homepage of the installation
        self.browser.get(url+"/cas/login")

        # Step 2: Enter the username and the password in the login box
        loginpage = LoginPage(self.browser)
        loginpage.login(user, password)

        # Step 2.1: If authorization is requested authorize the application
        try:
            self.browser.find_element_by_id('authorizeForm')
            allowBtn = self.browser.find_element_by_id('authorizeForm:allowButton')
            allowBtn.click()
        except NoSuchElementException:
            pass

        # Step 3: Assert that the login is sucessful
        msgdiv = self.browser.find_element_by_id('msg')
        self.assertIn('Log In Successful', msgdiv.text)

        # Step 4: Logout
        self.browser.get(url+"/cas/logout")
        msgdiv = self.browser.find_element_by_id('msg')
        self.assertIn('Logout successful', msgdiv.text)


