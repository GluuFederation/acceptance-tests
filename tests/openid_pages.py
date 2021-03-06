import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    def fill_details(self, name, secret):
        # fills in the only required values, everything else is left to be the defaults
        name_input = self.driver.find_element(*AddClientSelectors.NAME)
        name_input.clear()
        name_input.send_keys(name)
        secret_input = self.driver.find_element(*AddClientSelectors.SECRET)
        secret_input.clear()
        secret_input.send_keys(secret)
        persist_select = Select(self.driver.find_element(*AddClientSelectors.PERSIST_AUTH))
        persist_select.select_by_value(str(True).upper())
        logout_select = Select(self.driver.find_element(*AddClientSelectors.LOGOUT))
        logout_select.select_by_value(str(True).upper())

    def update_details(self, name):
        name_input = self.driver.find_element(*AddClientSelectors.NAME)
        name_input.clear()
        name_input.send_keys(name)
        self.driver.find_element(*AddClientSelectors.UPDATE_BUTTON).click()

    def delete_client(self):
        self.driver.find_element(*AddClientSelectors.DELETE_BUTTON).click()
        self.driver.find_element(*AddClientSelectors.CONFIRM_OK).click()

    def add_logout_uri(self, uri):
        self.driver.find_element(*AddClientSelectors.ADD_LOGOUT_URI).click()
        wait = WebDriverWait(self.driver, 10)
        uri_input = wait.until(EC.element_to_be_clickable(AddClientSelectors.LOGOUT_URI_INPUT))
        uri_input.clear()
        uri_input.send_keys(uri)
        self.driver.find_element(*AddClientSelectors.LOGOUT_URI_OK).click()
