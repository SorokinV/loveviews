import time
import locators
from locators import Locator
from locators import Where
from selenium import webdriver


def test_login(ddriver):
    driver = ddriver
    driver.get(Where.main_pass)
    print('\n',Locator.locator1[0],Locator.locator1[1])
    elms = driver.find_elements(Locator.locator1[0],Locator.locator1[1])
    for elm in elms:
        print(elm.get_attribute('class'))
    print(driver.current_url)
    assert 'irisqul' in driver.current_url

def main():
    return