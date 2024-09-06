wait_time = 5

import locators
from locators import where

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()  # создали объект для опций

service = Service(ChromeDriverManager().install())

@pytest.fixture
def ddriver():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def login(ddriver):
    driver = ddriver
    driver.get(where.main_pass)

    elm = driver.find_element(*locators.locator1)
    assert elm is not None


