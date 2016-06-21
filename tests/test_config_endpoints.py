"""
Title: Test the various URL endpoints for Metadata and Config values
Component:
"""
import unittest

from selenium import webdriver

from .config import url


class MetadataTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_oidc_endpoint(self):
        self.browser.get(url+"/.well-known/openid-configuration")
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('issuer', body.text)
        self.assertIn('authorization_endpoint', body.text)

    def test_webkeys(self):
        self.browser.get(url+"/oxauth/seam/resource/restv1/oxauth/jwks")
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('keys', body.text)
        self.assertIn('kid', body.text)

    def test_uma_endpoint(self):
        self.browser.get(url+"/.well-known/uma-configuration")
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('issuer', body.text)
        self.assertIn('uma_profiles_supported', body.text)
        self.assertIn('aat_profiles_supported', body.text)
        self.assertIn('pat_profiles_supported', body.text)
