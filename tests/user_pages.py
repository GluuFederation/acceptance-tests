from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from .pages import BasePage
from .locators import GroupSelectors, AddGroupSelectors


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







