import time
import datetime as dt

import locators
from locators import Locator
from locators import Where

from selenium import webdriver
from selenium.webdriver.common.by import By

def one_slice(slice_last):
    sstring = '&from'+dt.datetime.strftime(slice_last,'%Y-%m-%d')
    slice_last = slice_last + dt.timedelta(days=10)
    sstring += '&to'+dt.datetime.strftime(slice_last,'%Y-%m-%d')
    slice_last = slice_last + dt.timedelta(days=1)
    return slice_last,sstring

def all_slices(slice_first):
    slice_first = dt.datetime.strptime('2024-01-01','%Y-%m-%d')
    next_slice = slice_first
    while True:
        next_slice, sstring = one_slice(next_slice)
        yield  next_slice,'?tab=overview'+sstring
        if next_slice>dt.datetime.now():
            break
    return 0,''

def ttest_login(dt_first):
    dt_next = dt_first
    dts = all_slices(dt_next)
    for dt_next,sstring in dts:
        print(dt_next,sstring)
    return

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

ttest_login(dt.datetime.strptime('2024-01-01','%Y-%m-%d'))

def main():
    return