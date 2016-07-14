import unittest
import urllib2
import ssl

from selenium import webdriver

from .config import url, user, password


class SAMLTestCase(unittest.TestCase):
    def test_01_shibboleth_metadata_xml(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        response = urllib2.urlopen(url+"/idp/shibboleth", context=ctx)
        xmldata = response.read()
        self.assertIn('SAML:2.0:metadata', xmldata)
        self.assertIn('shibboleth:metadata', xmldata)
