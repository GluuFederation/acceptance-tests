import time

from selenium.webdriver.support.ui import Select

from .pages import BasePage
from .locators import ScopeSelectors, AddScopeSelectors, ClientSelectors, \
        AddClientSelectors


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

    def add_claims(self):
        self.driver.find_element(*AddScopeSelectors.ADD_CLAIM_BUTTON).click()
        search_input = self.driver.find_element(*AddScopeSelectors.SEARCH_BOX)
        search_input.clear()
        search_input.send_keys('address')
        self.driver.find_element(*AddScopeSelectors.SEARCH_BUTTON).click()
        checks = self.driver.find_elements(*AddScopeSelectors.CHECKBOX)
        for check in checks:
            check.click()
        self.driver.find_element(*AddScopeSelectors.OK_BUTTON).click()

    def remove_claims(self):
        # Somehow looping this doesn't seem to work
        self.driver.find_element(*AddScopeSelectors.CLAIM_REMOVE).click()
        time.sleep(0.2)
        self.driver.find_element(*AddScopeSelectors.CLAIM_REMOVE).click()
        time.sleep(0.2)
        self.driver.find_element(*AddScopeSelectors.CLAIM_REMOVE).click()
        time.sleep(0.2)
        self.driver.find_element(*AddScopeSelectors.CLAIM_REMOVE).click()


class ClientPage(BasePage):
    def search(self, term):
        search_box = self.driver.find_element(*ClientSelectors.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(term)
        self.driver.find_element(*ClientSelectors.SEARCH_BUTTON).click()


class AddClientPage(BasePage):
    def fill_details(self):
        pass
