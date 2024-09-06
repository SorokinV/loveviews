wait_time = 5

import time
from locators import Locator
from locators import Where

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
    time.sleep(10)
    driver.quit()




