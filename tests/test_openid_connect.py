import unittest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import url, user, password
from .pages import LoginPage
from .openid_pages import ScopesPage, AddScopePage
from .locators import MenuItems, ScopeSelectors, AddScopeSelectors


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

        sp.search('uma')
        try:
            self.browser.find_element_by_partial_link_text('uma_authorization')
            self.browser.find_element_by_partial_link_text('uma_protection')
        except NoSuchElementException:
            self.fail('Scope search listing failed for term "uma"')

    def test_02_add_scope(self):
        # Step 1: Click "Add Scope" to open the add scope form
        self.browser.find_element(*ScopeSelectors.ADD_SCOPE_BUTTON).click()

        # Step 2: Fill in the details and click "Add"
        as_page = AddScopePage(self.browser)
        as_page.add_empty_scope('Test Scope', 'A Scope for Acceptance testing', AddScopeSelectors.OPENID, True)

        # Step 3: Verify successful of addition
        try:
            self.browser.find_element_by_id('scopeForm:inum')
        except NoSuchElementException:
            self.fail('Openid Test Scope was not added')

    def test_03_add_claims_to_scope(self):
        # Step 1: Add claims
        as_page = AddScopePage(self.browser)
        as_page.add_claims()

        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        update_button = wait.until(EC.element_to_be_clickable(AddScopeSelectors.UPDATE_BUTTON))
        update_button.click()
        # Step 2: Verify
        claims = self.browser.find_element(*AddScopeSelectors.CLAIMS_SPAN)
        self.assertIn('Email', claims.text)
        self.assertIn('Home Address', claims.text)

    def test_04_remove_claims_from_scope(self):
        as_page = AddScopePage(self.browser)
        as_page.remove_claims()
        self.browser.find_element(*AddScopeSelectors.UPDATE_BUTTON).click()

        claims = self.browser.find_element(*AddScopeSelectors.CLAIMS_SPAN)
        self.assertNotIn('Email', claims.text)
        self.assertNotIn('Home Address', claims.text)

    def test_05_delete_scope(self):
        self.browser.find_element(*AddScopeSelectors.DELETE_BUTTON).click()
        self.browser.find_element(*AddScopeSelectors.DELETE_CONFIRM_OK).click()

        sp = ScopesPage(self.browser)
        sp.search('Test')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_link_text('Test Scope')
