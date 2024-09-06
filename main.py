import time
import locators
from locators import Locator
from locators import Where
from selenium import webdriver


def test_login(ddriver):
    driver = ddriver
    driver.get(Where.main_pass)
    print('\n',Locator.locator1[0],Locator.locator1[1])
    #elm = driver.find_element(Locator.locator1[0],Locator.locator1[1])
    print(driver.current_url)
    assert 'irisqul' in driver.current_url

def main():
    return