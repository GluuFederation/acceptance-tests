"""
Title: Test pages under the Users menu.
Component: oxTrust

"""
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from .config import url, user, password
from .pages import LoginPage
from .user_pages import ManageGroupsPage, AddGroupPage
from .locators import MenuItems, GroupSelectors, AddGroupSelectors


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

    def test_add_groups(self):
        """New groups are created using `Add Group` button"""
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Click the Add Groups Button
        self.browser.find_element_by_link_text('Add Group').click()

        # Step 3: Enter the value for `Display name`, Visibility type, and description
        ag_page = AddGroupPage(self.browser)
        ag_page.fill_details('Test Group', AddGroupSelectors.PUBLIC, 'Test Description')
        # Step 4: Add the admin as a member of the group
        ag_page.add_member('admin')
        # Step 5: Verify that the admin is added to the members list
        self.assertIn('Default Admin User', self.browser.find_element_by_tag_name('body').text)
        # Step 6: Click `Add` to create the group
        self.browser.find_element(*AddGroupSelectors.ADD_BUTTON).click()
