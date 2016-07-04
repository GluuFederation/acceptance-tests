"""
Title: Test admin login after gluu-server installation.
Component: oxTrust

"""
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage


class LoginTestCase(unittest.TestCase):
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
        self.browser.get(url)

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
        h1 = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Welcome', h1.text)
        user_menu = self.browser.find_element_by_class_name('user-menu')
        assert user_menu is not None

        # Step 4: Logout
        self.browser.get(url+"/identity/logout")

    def test_login_wrong_credential(self):
        """Admin login FAILS for wrong password.
        """
        # Step 1: Open the homepage of the installation
        self.browser.get(url)
        # Step 2: Enter the username and the password in the login box
        loginpage = LoginPage(self.browser)
        loginpage.login(user, "wrong_password_234124")

        # Step 3: User sees an error message
        self.assertIn('Please use correct username', loginpage.message())
