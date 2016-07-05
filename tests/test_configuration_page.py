"""
Title: Test Configuration Pages.
Component: oxTrust

"""
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage, OrganizationConfigPage
from .locators import MenuItems


class OrgConfigTestCase(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_whitepages(self):
        """WhitePages are enabled and disabled from the config page.
        """
        # Step 1: Login to oxTrust as the admin
        self.browser.get(url)
        lp = LoginPage(self.browser)
        lp.login(user, password)

        # Step 2: Navigate to the organization config page
        self.browser.find_element(*MenuItems.CONFIG).click()
        self.browser.find_element(*MenuItems.ORG_CONF).click()

        # Step 3: Enable WhitePages and verify its enabled
        orgConfPage = OrganizationConfigPage(self.browser)
        orgConfPage.enable_white_pages()

        self.browser.find_element(*MenuItems.PERSONAL).click()
        whitePagesLink = self.browser.find_element(*MenuItems.WHITE_PAGES)
        self.assertIsNotNone(whitePagesLink)
        whitePagesLink.click()

        h1 = self.browser.find_element_by_tag_name('h1')
        self.assertIn('White Pages', h1.text)

        # Step 4: Disable the White Pages and verify
        self.browser.find_element(*MenuItems.CONFIG).click()
        self.browser.find_element(*MenuItems.ORG_CONF).click()
        orgConfPage = OrganizationConfigPage(self.browser)
        orgConfPage.disable_white_pages()

        self.browser.find_element(*MenuItems.PERSONAL).click()
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element(*MenuItems.WHITE_PAGES)
