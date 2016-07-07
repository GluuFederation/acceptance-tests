"""
Title: Test pages under the Users menu.
Component: oxTrust

"""
import time
import unittest
import uuid

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
        cls.group_name = str(uuid.uuid4())[0:8]

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_01_search_and_listing(self):
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
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Click the Add Groups Button
        self.browser.find_element_by_link_text('Add Group').click()

        # Step 3: Enter the value for `Display name`, Visibility type, and description
        ag_page = AddGroupPage(self.browser)
        ag_page.fill_details('Test Group', AddGroupSelectors.PUBLIC, 'Test Description')
        # Step 4: Click `Add` to create the group and verify its listing
        self.browser.find_element(*AddGroupSelectors.ADD_BUTTON).click()

        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()
        mp = ManageGroupsPage(self.browser)
        mp.search('Test')
        try:
            self.browser.find_element(*GroupSelectors.GROUPS_TABLE)
            self.browser.find_element_by_link_text('Test Group')
        except NoSuchElementException:
            self.fail('The "Test Group" is not present when searched for `Test`')

    def test_03_update_group(self):
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Search for Test Group and open the `Add Group` page
        mp = ManageGroupsPage(self.browser)
        mp.search('Test')
        self.browser.find_element_by_link_text('Test Group').click()

        # Step 3: Update the Group name, visibility and description
        ag_page = AddGroupPage(self.browser)
        ag_page.fill_details(self.group_name, AddGroupSelectors.PRIVATE, 'Updated Description')
        self.browser.find_element(*AddGroupSelectors.UPDATE_BUTTON).click()

        # Step 4: Verify that the new details have been updated
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()
        mp = ManageGroupsPage(self.browser)
        mp.search(self.group_name)
        try:
            self.browser.find_element(*GroupSelectors.GROUPS_TABLE)
            self.browser.find_element_by_link_text(self.group_name)
        except NoSuchElementException:
            self.fail('The "'+self.group_name+'" group is not present when searched')

    def test_04_add_user_to_group(self):
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Search for the group and open its `add group` page
        mp = ManageGroupsPage(self.browser)
        mp.search(self.group_name)
        self.browser.find_element_by_link_text(self.group_name).click()

        # Step 4: Add the admin as a member of the group and check it's listed
        ag_page = AddGroupPage(self.browser)
        ag_page.add_member('admin')
        time.sleep(2)
        self.assertIn('Default Admin User', self.browser.find_element(*AddGroupSelectors.SELECTED_MEMBERS_SPAN).text)

        # Step 5: Update the group and verify the user is persisted
        self.browser.find_element(*AddGroupSelectors.UPDATE_BUTTON).click()
        self.assertIn('Default Admin User', self.browser.find_element(*AddGroupSelectors.SELECTED_MEMBERS_SPAN).text)

    def test_05_remove_user_from_group(self):  # TODO
        self.assertTrue(True)

    def test_06_delete_group(self):
        # Step 1: Navigate to the Manage Groups Page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()

        # Step 2: Search for the group and open its `add group` page
        mp = ManageGroupsPage(self.browser)
        mp.search(self.group_name)
        self.browser.find_element_by_link_text(self.group_name).click()
        # Step 3: Delete the group
        ag_page = AddGroupPage(self.browser)
        ag_page.delete_group()

        #self.browser.refresh()
        self.browser.find_element(*MenuItems.MANAGE_GROUPS).click()
        mp = ManageGroupsPage(self.browser)
        mp.search(self.group_name)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_link_text(self.group_name)

