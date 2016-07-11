import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage
from .openid_pages import ScopesPage
from .locators import MenuItems


class OpenidTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_01_oidc_endpoint(self):
        self.browser.get(url+"/.well-known/openid-configuration")
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('issuer', body.text)
        self.assertIn('authorization_endpoint', body.text)

    def test_02_webkeys(self):
        self.browser.get(url+"/oxauth/seam/resource/restv1/oxauth/jwks")
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('keys', body.text)
        self.assertIn('kid', body.text)


class ScopesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)
        cls.browser.get(url)
        lp = LoginPage(cls.browser)
        lp.login(user, password)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_01_search_and_list_scopes(self):
        # Step 1: Navigate to the Scopes Page
        self.browser.find_element(*MenuItems.OPENID_CONNECT).click()
        self.browser.find_element(*MenuItems.SCOPES).click()

        # Step 2: Verify the search is listing the scopes
        sp = ScopesPage(self.browser)
        sp.search('')

        try:
            self.browser.find_element_by_partial_link_text('openid')
            self.browser.find_element_by_partial_link_text('profile')
        except NoSuchElementException:
            self.fail('Scope search listing failed')
