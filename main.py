import time
import locators
from locators import Locator
from locators import Where
from selenium import webdriver

from selenium.webdriver.common.by import By



def test_login(ddriver):
    driver = ddriver
    driver.get(Where.main_pass)
    elms = driver.find_elements(*Locator.locator0)
    print('\n',len(elms))
    for elm in elms:
        #print(elm.get_attribute('innerHTML'))
        #print(elm.get_attribute('outerHTML'))
        ttext = elm.get_attribute('data-hovercard-url')
        lltext = ttext.split('/')
        if ('sprint' in lltext[2].lower()) and ('5' in lltext[2].lower()):
            print(lltext[1:3])
    print(driver.current_url)
    assert 'irisqul' in driver.current_url

def main():
    return