"""
Title: Test Configuration Pages.
Component: oxTrust

"""
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage, OrganizationConfigPage, ProfilePage
from .locators import MenuItems


class OrgConfigTestCase(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)
        cls.browser.get(url)
        lp = LoginPage(cls.browser)
        lp.login(user, password)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_whitepages(self):
        """WhitePages are enabled and disabled from the config page.
        """
        # Step 1: Navigate to the organization config page
        self.browser.find_element(*MenuItems.CONFIG).click()
        self.browser.find_element(*MenuItems.ORG_CONF).click()

        # Step 2: Enable WhitePages and verify its enabled
        orgConfPage = OrganizationConfigPage(self.browser)
        orgConfPage.enable_white_pages()

        self.browser.find_element(*MenuItems.PERSONAL).click()
        whitePagesLink = self.browser.find_element(*MenuItems.WHITE_PAGES)
        self.assertIsNotNone(whitePagesLink)
        whitePagesLink.click()

        h1 = self.browser.find_element_by_tag_name('h1')
        self.assertIn('White Pages', h1.text)

        # Step 3: Disable the White Pages and verify
        self.browser.find_element(*MenuItems.CONFIG).click()
        self.browser.find_element(*MenuItems.ORG_CONF).click()
        orgConfPage = OrganizationConfigPage(self.browser)
        orgConfPage.disable_white_pages()

        self.browser.find_element(*MenuItems.PERSONAL).click()
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element(*MenuItems.WHITE_PAGES)

    def test_profile_editing(self):
        """Profile Editing enable/disable is working.
        """
        # Step 1: Navigate to the Organization Config page
        self.browser.find_element(*MenuItems.CONFIG).click()
        self.browser.find_element(*MenuItems.ORG_CONF).click()

        # Step 2: Enable profile editing and verify its enabled
        orgConfPage = OrganizationConfigPage(self.browser)
        orgConfPage.enable_profile_editing()

        self.browser.find_element(*MenuItems.PERSONAL).click()
        self.browser.find_element(*MenuItems.PROFILE).click()

        profile_page = ProfilePage(self.browser)
        self.assertTrue(profile_page.is_editable())

        # Step 3: Navigate to the Organization Config page
        self.browser.find_element(*MenuItems.CONFIG).click()
        self.browser.find_element(*MenuItems.ORG_CONF).click()

        # Step 4: Disable Profile editing and verify its disabled
        orgConfPage = OrganizationConfigPage(self.browser)
        orgConfPage.disable_profile_editing()

        self.browser.find_element(*MenuItems.PERSONAL).click()
        self.browser.find_element(*MenuItems.PROFILE).click()

        profile_page = ProfilePage(self.browser)
        self.assertFalse(profile_page.is_editable())
