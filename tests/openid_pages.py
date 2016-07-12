from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from .pages import BasePage
from .locators import ScopeSelectors, AddScopeSelectors


class ScopesPage(BasePage):
    def search(self, term):
        search_input = self.driver.find_element(*ScopeSelectors.SEARCH_BOX)
        search_input.clear()
        search_input.send_keys(term)
        self.driver.find_element(*ScopeSelectors.SEARCH_BUTTON).click()


class AddScopePage(BasePage):
    def fill_details(self, name, description, scope_type, default):
        """Fills the details in the Add Scope form.

        Args:
            name (string) - Name of the scope
            description (string) - Description of the scope
            scope_type - Either of AddScopeSelectors.LDAP, DYNAMIC, OPENID
            default_scope (boolean) - True or False
        """
        name_input = self.driver.find_element(*AddScopeSelectors.NAME)
        name_input.clear()
        name_input.send_keys(name)

        desc_input = self.driver.find_element(*AddScopeSelectors.DESCRIPTION)
        desc_input.clear()
        desc_input.send_keys(description)

        type_select = Select(self.driver.find_element(*AddScopeSelectors.SCOPE_TYPE))
        type_select.select_by_value(scope_type)

        default_select = Select(self.driver.find_element(*AddScopeSelectors.DEFAULT_SCOPE))
        default_select.select_by_value(str(default).upper())

    def add_empty_scope(self, name, description, scope_type, default):
        self.fill_details(name, description, scope_type, default)
        self.driver.find_element(*AddScopeSelectors.ADD_BUTTON).click()
