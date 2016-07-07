"""
Title: Test pages under the Users menu.
Component: oxTrust

"""
import time
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

    def test_01_search_and_listing(self):
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

    def test_02_add_group(self):
        """New group created using `Add Group` button"""
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Click the Add Groups Button
        self.browser.find_element_by_link_text('Add Group').click()

        # Step 3: Enter the value for `Display name`, Visibility type, and description
        ag_page = AddGroupPage(self.browser)
        ag_page.fill_details('Test Group', AddGroupSelectors.PUBLIC, 'Test Description')
        # Step 4: Add the admin as a member of the group and check it's listed
        ag_page.add_member('admin')
        time.sleep(2)
        self.assertIn('Default Admin User', self.browser.find_element(*AddGroupSelectors.SELECTED_MEMBERS_SPAN).text)

        # Step 5: Click `Add` to create the group and verify its listing
        self.browser.find_element(*AddGroupSelectors.ADD_BUTTON).click()

        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()
        mp = ManageGroupsPage(self.browser)
        mp.search('Test')
        try:
            self.browser.find_element(*GroupSelectors.GROUPS_TABLE)
            self.browser.find_element_by_link_text('Test Group')
        except NoSuchElementException:
            self.fail('The "Test Group" is not present when searched for `Test`')

    def test_03_update_group(self):
        """Update the details of an existing group"""
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Search for Test Group and open the `Add Group` page
        mp = ManageGroupsPage(self.browser)
        mp.search('Test')
        self.browser.find_element_by_link_text('Test Group').click()

        # Step 3: Update the Group name, visibility and description
        ag_page = AddGroupPage(self.browser)
        ag_page.fill_details('Updated Group', AddGroupSelectors.PRIVATE, 'Updated Description')
        self.browser.find_element(*AddGroupSelectors.UPDATE_BUTTON).click()

        # Step 4: Verify that the new details have been updated
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()
        mp = ManageGroupsPage(self.browser)
        mp.search('Updated')
        try:
            self.browser.find_element(*GroupSelectors.GROUPS_TABLE)
            self.browser.find_element_by_link_text('Updated Group')
        except NoSuchElementException:
            self.fail('The "Updated Group" is not present when searched for `Updated`')

    def test_04_delete_group(self):
        """Delete users group."""
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Search for the group and open its `add group` page
        mp = ManageGroupsPage(self.browser)
        mp.search('Updated')
        self.browser.find_element_by_link_text('Updated Group').click()
        # Step 3: Delete the group
        ag_page = AddGroupPage(self.browser)
        ag_page.delete_group()

        # Step 4: Confirm the group is deleted
        mp = ManageGroupsPage(self.browser)
        mp.search('Updated')
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_link_text('Updated Group')


