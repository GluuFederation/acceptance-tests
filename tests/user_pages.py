from locators import GroupSelectors
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from .pages import BasePage


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
        searchBox.send_keys(term)
        self.driver.find_element(*GroupSelectors.SEARCH_BUTTON).click()

