"""
Title: Test pages under the Users menu.
Component: oxTrust

"""
import time
import unittest
import uuid
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import url, user, password
from .pages import LoginPage
from .user_pages import ManageGroupsPage, AddGroupPage, ManagePeoplePage, \
        UpdateUserPage
from .locators import MenuItems, GroupSelectors, AddGroupSelectors, \
        ManagePeopleSelectors, UpdateUserSelectors, ImportPeopleSelectors



class GroupsTestCase(unittest.TestCase):
    """Tests for the Users -> Manage Groups page"""
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
        self.fail('TODO: Test not written')

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

        # Step 4: Verify deletion
        # adding explicit wait as there seems to be a page load delay here
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable(GroupSelectors.SEARCH_BUTTON))

        mp = ManageGroupsPage(self.browser)
        mp.search(self.group_name)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_link_text(self.group_name)


class ManagePeopleTestCase(unittest.TestCase):
    """Tests for the Users -> Manage People page"""
    @classmethod
    def setupClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)
        cls.browser.get(url)
        lp = LoginPage(cls.browser)
        lp.login(user, password)
        cls.username = str(uuid.uuid4())[0:6]

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_01_search_for_users(self):
        # Step 1: Navigate to the `Manage People` page
        self.browser.find_element(*MenuItems.USERS).click()
        self.browser.find_element(*MenuItems.MANAGE_PEOPLE).click()

        # Step 2: Search
        mp = ManagePeoplePage(self.browser)
        mp.search('ad')

        try:
            self.browser.find_element(*ManagePeopleSelectors.USER_LIST_TABLE)
            self.browser.find_element_by_link_text('admin')
        except NoSuchElementException:
            self.fail('Search result for user `ad` failed to show up')

        mp.search('a')
        error = self.browser.find_element(*ManagePeopleSelectors.ERROR_SPAN)
        self.assertIn('Length of search string should be between 2 and 30', error.text)

        mp.search('')
        error = self.browser.find_element(*ManagePeopleSelectors.ERROR_SPAN)
        self.assertIn('value is required', error.text)

    def test_02_add_person(self):
        self.browser.find_element(*ManagePeopleSelectors.ADD_PERSON_BUTTON).click()
        up = UpdateUserPage(self.browser)
        # Params: user, first, last, display, email
        up.add_user(self.username, "User", self.username, "User "+self.username, self.username+"@test.org")

        try:
            self.browser.find_element(*UpdateUserSelectors.UPDATE_BUTTON)
        except NoSuchElementException:
            self.fail('New user was not added.')

        # TODO create users with other attributes apart from the defalut few

    def test_03_update_user(self):
        # Step 1: Navigate to the `Manage People` page
        self.browser.find_element(*MenuItems.MANAGE_PEOPLE).click()
        # Step 2: Search
        mp = ManagePeoplePage(self.browser)
        mp.search(self.username)

        # Step 3: Update the user
        self.browser.find_element_by_link_text(self.username).click()
        up = UpdateUserPage(self.browser)
        up.update_user(self.username, "Updated User", self.username, "Updated User "+self.username)

        # Step 4: Verify updation
        self.browser.find_element(*MenuItems.MANAGE_PEOPLE).click()
        mp = ManagePeoplePage(self.browser)
        mp.search(self.username)

        try:
            self.browser.find_element_by_link_text("Updated User "+self.username)
        except NoSuchElementException:
            self.fail("User data updation wasn't sucessful")

    def test_04_delete_user(self):
        # Step 1: Search and find the user
        mp = ManagePeoplePage(self.browser)
        mp.search(self.username)
        self.browser.find_element_by_link_text("Updated User "+self.username).click()

        # Step 2: Delete the user
        self.browser.find_element(*UpdateUserSelectors.DELETE_BUTTON).click()
        self.browser.find_element(*UpdateUserSelectors.DELETE_CONFIRM_OK).click()

        # Step 3: Verify deletion
        mp.search(self.username)
        self.assertIn('No Search Result Found', self.browser.find_element(*ManagePeopleSelectors.SEARCH_RESULT_FORM).text)

    def test_05_import_users(self):
        # Step 1: Navigate to the import people page
        self.browser.find_element(*MenuItems.IMPORT_PEOPLE).click()
        # Step 2: Set the document to upload
        file_input = self.browser.find_element(*ImportPeopleSelectors.FILE_INPUT)
        directory = os.path.dirname(os.path.realpath(__file__))
        file_input.send_keys(os.path.join(directory, "data", "sample_users.xls"))
        # Step 3: Validate the document
        self.browser.find_element(*ImportPeopleSelectors.VALIDATE_BUTTON).click()
        # Step 4: Import and verify
        try:
            wait = WebDriverWait(self.browser, 10)
            import_button = wait.until(EC.element_to_be_clickable(ImportPeopleSelectors.IMPORT_BUTTON))
            import_button.click()
        except TimeoutException:
            self.fail("File validation failed. Watch browser for error.")

        mp = ManagePeoplePage(self.browser)
        mp.search("user")
        try:
            self.browser.find_element_by_link_text("user1")
            self.browser.find_element_by_link_text("user2")
            self.browser.find_element_by_link_text("user3")
        except NoSuchElementException:
            self.fail("Import Failed")

        # Extra: Cleanup the imported users
        users = ['user1', 'user2', 'user3']
        for u in users:
            mp = ManagePeoplePage(self.browser)
            mp.search(u)
            self.browser.find_element_by_link_text(u).click()
            self.browser.find_element(*UpdateUserSelectors.DELETE_BUTTON).click()
            self.browser.find_element(*UpdateUserSelectors.DELETE_CONFIRM_OK).click()
        time.sleep(0.3) # Wait for the last delete operation to complete
