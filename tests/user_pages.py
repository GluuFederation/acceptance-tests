from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from .pages import BasePage
from .locators import GroupSelectors, AddGroupSelectors, ManagePeopleSelectors,\
        UpdateUserSelectors


class ManageGroupsPage(BasePage):
    """The Users -> Manage Groups page"""

    def check_search_button(self):
        """Use the search button to list the available user groups"""
        searchButton = self.driver.find_element(*GroupSelectors.SEARCH_BUTTON)
        searchButton.click()

        try:
            self.driver.find_element(*GroupSelectors.GROUPS_TABLE)
            return True
        except NoSuchElementException:
            return False

    def search(self, term):
        """Perform search operation for the given term"""
        searchBox = self.driver.find_element(*GroupSelectors.SEARCH_BOX)
        searchBox.clear()
        searchBox.send_keys(term)
        self.driver.find_element(*GroupSelectors.SEARCH_BUTTON).click()


class AddGroupPage(BasePage):
    """The Users -> Manage Groups -> Add Group page"""

    def fill_details(self, group_name, visibility, description):
        """Fills the `Add Group` page inputs

        Args:
            group_name (string): name for the group
            visibility : locators.py AddGroupSelectors.PUBLIC or
                         AddGroupSelectors.PRIVATE
            description (string): description of the group
        """
        name = self.driver.find_element(*AddGroupSelectors.NAME_INPUT)
        name.clear()
        name.send_keys(group_name)
        select = Select(self.driver.find_element(*AddGroupSelectors.TYPE_SELECT))
        select.select_by_value(visibility)
        desc = self.driver.find_element(*AddGroupSelectors.DESCRIPTION)
        desc.clear()
        desc.send_keys(description)

    def add_member(self, username):
        # Step 1: Click the `Add Member` button
        self.driver.find_element(*AddGroupSelectors.ADD_MEMBER_BUTTON).click()

        # Step 2: Enter the username and search
        searchbox = self.driver.find_element(*AddGroupSelectors.SEARCH_INPUT)
        searchbox.send_keys(username)
        self.driver.find_element(*AddGroupSelectors.SEARCH_BUTTON).click()

        # Step 3: Select the user with UID as provided
        rows = self.driver.find_elements(*AddGroupSelectors.MEMBER_ROWS)
        for row in rows:
            if username in row.text:
                rowid = row.get_attribute('id')
                checkbox = self.driver.find_element_by_xpath('//input[@type="checkbox"][contains(@name, "'+rowid+'")]')
                checkbox.click()

        # Step 4: Click OK
        self.driver.find_element(*AddGroupSelectors.USER_OK_BUTTON).click()

    def delete_group(self):
        self.driver.find_element(*AddGroupSelectors.DELETE_BUTTON).click()
        self.driver.find_element(*AddGroupSelectors.DELETE_OK_BUTTON).click()


class ManagePeoplePage(BasePage):
    def search(self, query):
        search_box = self.driver.find_element(*ManagePeopleSelectors.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(query)
        self.driver.find_element(*ManagePeopleSelectors.SEARCH_BUTTON).click()


class UpdateUserPage(BasePage):
    def fill_details(self, user, first, last, display, email):
        username = self.driver.find_element(*UpdateUserSelectors.USERNAME)
        username.clear()
        username.send_keys(user)
        first_name = self.driver.find_element(*UpdateUserSelectors.FIRST_NAME)
        first_name.clear()
        first_name.send_keys(first)
        display_name = self.driver.find_element(*UpdateUserSelectors.DISPLAY_NAME)
        display_name.clear()
        display_name.send_keys(display)
        last_name = self.driver.find_element(*UpdateUserSelectors.LAST_NAME)
        last_name.clear()
        last_name.send_keys(last)
        email_input = self.driver.find_element(*UpdateUserSelectors.EMAIL)
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.driver.find_element(*UpdateUserSelectors.PASSWORD)
        password_input.clear()
        password_input.send_keys("password")

    def add_user(self, user, first, last, display, email):
        self.fill_details(user, first, last, display, email)
        self.driver.find_element(*UpdateUserSelectors.ADD_BUTTON).click()

    def update_user(self, username, first, last, display):
        first_name = self.driver.find_element_by_xpath('//input[@value="User"]')
        first_name.clear()
        first_name.send_keys(first)
        display_name = self.driver.find_element_by_xpath('//input[@value="User {}"]'.format(username))
        display_name.clear()
        display_name.send_keys(display)
        last_name = self.driver.find_element_by_xpath('//input[@value="{}"]'.format(username))
        last_name.clear()
        last_name.send_keys(last)
        self.driver.find_element(*UpdateUserSelectors.UPDATE_BUTTON).click()
