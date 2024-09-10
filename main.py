import time
import datetime as dt

import locators
from locators import Locator
from locators import Where

from selenium import webdriver
from selenium.webdriver.common.by import By

def one_slice(slice_last):
    sstring = '&from='+dt.datetime.strftime(slice_last,'%Y-%m-%d')
    slice_last = slice_last + dt.timedelta(days=10)
    sstring += '&to='+dt.datetime.strftime(slice_last,'%Y-%m-%d')
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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()  # создали объект для опций
service = Service(ChromeDriverManager().install())

def ttest_login(dt_first):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        dt_next = dt_first
        flls, lls = [], []
        ii = -1
        for dt_next,sstring in all_slices(dt_next):
            ii +=1
            if ii==1:
                break
            #print(dt_next,sstring)
            driver.get(Where.main_pass+'/'+sstring+' ')
            elms = driver.find_elements(*Locator.locator0)
            #print('\n',len(elms))
            for elm in elms:
                #print(elm.get_attribute('innerHTML'))
                #print(elm.get_attribute('outerHTML'))
                ttext = elm.get_attribute('data-hovercard-url')
                lltext = ttext.split('/')
                flls.append((lltext[1:3]))
                #print(flls)
                if ('rint' in lltext[2].lower()) and ('5' in lltext[2].lower()):
                    print(lltext[1:3])
                    lls.append((lltext[1:3]))
            time.sleep(30)
        print(flls)
        print(lls)
        #print(driver.current_url)
        #assert 'irisqul' in driver.current_url
    finally:
        driver.quit()

ttest_login(dt.datetime.strptime('2024-01-01','%Y-%m-%d'))

def main():
    return