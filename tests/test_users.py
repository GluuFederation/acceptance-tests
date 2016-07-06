"""
Title: Test pages under the Users menu.
Component: oxTrust

"""
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage
from .user_pages import ManageGroupsPage
from .locators import MenuItems, GroupSelectors


class GroupsTestCase(unittest.TestCase):
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

    def test_manage_groups_listing(self):
        """Manage Groups page search works as expected"""
        # Step 1: Navigate to the Manage Groups page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Click the search and verify that the default group is listed
        mp = ManageGroupsPage(self.browser)
        self.assertTrue(mp.check_search_button())

        # Step 3: Search for Gluu and verify that the Gluu Manager group is listed
        mp.search('Gluu')
        try:
            self.browser.find_element(*GroupSelectors.GROUPS_TABLE)
        except NoSuchElementException:
            self.fail('The "Gluu Manager Group" was not populated when searched for `Gluu`')
