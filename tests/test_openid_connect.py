import unittest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import url, user, password
from .pages import LoginPage
from .openid_pages import ScopesPage, AddScopePage, ClientPage, AddClientPage
from .locators import MenuItems, ScopeSelectors, AddScopeSelectors, \
        ClientSelectors, AddClientSelectors


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

    def test_03_update_scope_details(self):
        # Step 1: Navigate to the Scopes page
        self.browser.find_element(*MenuItems.SCOPES).click()

        # Step 2: Search and list the required scope
        sp = ScopesPage(self.browser)
        sp.search('Test')

        # Step 3: Open the Add scope page and update the detials
        self.browser.find_element_by_link_text('Test Scope').click()
        as_page = AddScopePage(self.browser)
        as_page.fill_details('Updated Scope', 'An Updated Scope for Acceptance testing', AddScopeSelectors.DYNAMIC, False)
        self.browser.find_element(*AddScopeSelectors.UPDATE_BUTTON).click()

        # Step 4: Verify update was successful
        self.browser.find_element(*MenuItems.SCOPES).click()
        sp = ScopesPage(self.browser)
        sp.search('Updated')

        try:
            self.browser.find_element_by_link_text('Updated Scope').click()
        except NoSuchElementException:
            self.fail('The scope was not updated.')

    def test_04_add_claims_to_scope(self):
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

    def test_05_remove_claims_from_scope(self):
        # Step 1: Click and 
        as_page = AddScopePage(self.browser)
        as_page.remove_claims()
        self.browser.find_element(*AddScopeSelectors.UPDATE_BUTTON).click()

        claims = self.browser.find_element(*AddScopeSelectors.CLAIMS_SPAN)
        self.assertNotIn('Email', claims.text)
        self.assertNotIn('Home Address', claims.text)

    def test_06_delete_scope(self):
        self.browser.find_element(*AddScopeSelectors.DELETE_BUTTON).click()
        self.browser.find_element(*AddScopeSelectors.DELETE_CONFIRM_OK).click()

        sp = ScopesPage(self.browser)
        sp.search('Updated')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_link_text('Updated Scope')


class ClientsTestCase(unittest.TestCase):
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

    def test_01_search_and_listing_clients(self):
        # Step 1: Navigate to the OpenID Connect Clients page
        self.browser.find_element(*MenuItems.OPENID_CONNECT).click()
        self.browser.find_element(*MenuItems.CLIENTS).click()

        # Step 2: Search
        cl_page = ClientPage(self.browser)
        cl_page.search('')

        try:
            self.browser.find_element_by_partial_link_text('oxTrust')
        except NoSuchElementException:
            self.fail('Client Search fails to bring oxTrust')

    def test_02_add_new_client(self):
        # Step 1: Click the Add Client Button
        self.browser.find_element(*ClientSelectors.ADD_CLIENT_BUTTON).click()

        # Step 2: Create a new client
        ac_page = AddClientPage(self.browser)
        ac_page.fill_details('Test Client', 'secret')
        self.browser.find_element(*AddClientSelectors.ADD_BUTTON).click()

        # Step 3: Verify the client has been added
        self.browser.find_element(*MenuItems.CLIENTS).click()
        cl_page = ClientPage(self.browser)
        cl_page.search('Test')
        try:
            self.browser.find_element_by_partial_link_text('Test Client')
        except NoSuchElementException:
            self.fail('Adding a OpenID Client via WebUI failed.')

    def test_03_update_client(self):
        # Step 1: Open the update client page
        self.browser.find_element_by_partial_link_text('Test Client').click()

        # Step 2: Update general details
        ac_page = AddClientPage(self.browser)
        ac_page.update_details('Updated Client')

        # Step 3: Verify the client has been updated
        self.browser.find_element(*MenuItems.CLIENTS).click()
        cl_page = ClientPage(self.browser)
        cl_page.search('Updated')
        try:
            self.browser.find_element_by_partial_link_text('Updated Client')
        except NoSuchElementException:
            self.fail('Updated a OpenID Client via WebUI failed.')

    def test_04_delete_client(self):
        # Step 1: Open the update client page
        self.browser.find_element_by_partial_link_text('Updated Client').click()

        # Step 2: Update general details
        ac_page = AddClientPage(self.browser)
        ac_page.delete_client()

        # Step 3: Confirm deletion of client
        time.sleep(1)
        cl_page = ClientPage(self.browser)
        cl_page.search('Updated')
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_partial_link_text('Updated Client')
