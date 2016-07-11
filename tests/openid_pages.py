from selenium.common.exceptions import NoSuchElementException

from .pages import BasePage
from .locators import ScopeSelectors


class ScopesPage(BasePage):
    def search(self, term):
        search_input = self.driver.find_element(*ScopeSelectors.SEARCH_BOX)
        search_input.clear()
        search_input.send_keys(term)
        self.driver.find_element(*ScopeSelectors.SEARCH_BUTTON).click()
