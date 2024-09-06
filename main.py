import time
import locators
from locators import Locator
from locators import Where
from selenium import webdriver

from selenium.webdriver.common.by import By



def test_login(ddriver):
    driver = ddriver
    driver.get(Where.main_pass)
    print('\n',Locator.locator3[0],Locator.locator3[1])
    elms = driver.find_elements(Locator.locator3[0],Locator.locator3[1])
    #elms = driver.find_elements(By.XPATH, '//main')
    print(len(elms))
    for elm in elms:
        print(elm.get_attribute('class'))
    print(driver.current_url)
    assert 'irisqul' in driver.current_url

def main():
    return