import time
import locators
from locators import Locator
from locators import Where
from selenium import webdriver


def ttest_login(ddriver):
    driver = ddriver
    driver.get(Where.main_pass)

    elm = driver.find_element(*Locator.locator1)
    print(driver.curl_url)
    assert elm is not None

def main():
    print(f'-{Locator.locator1})')
    return