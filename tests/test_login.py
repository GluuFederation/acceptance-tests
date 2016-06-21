from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from nose.tools import assert_in


def test_login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)

    driver.get('https://gluu.example.com')
    userElement = driver.find_element_by_id('loginForm:username')
    userElement.clear()
    userElement.send_keys('admin')
    passElement = driver.find_element_by_id('loginForm:password')
    passElement.clear()
    passElement.send_keys('oxTrust')
    passElement.send_keys(Keys.RETURN)

    if driver.find_element_by_id('authorizeForm'):
        allowBtn = driver.find_element_by_id('authorizeForm:allowButton')
        allowBtn.click()

    h1 = driver.find_element_by_tag_name('h1')

    assert_in('Welcome', h1.text)

    driver.quit()
