import locators
from locators import owner_repos
import time

wait_time = 10
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def xxowner(driver, name, repos):
    connect_str = f'https://github.com/{name}/{repos}/'
    print(connect_str)
    driver.get(connect_str)
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((owner_repos.PullRequestTab[0],owner_repos.PullRequestTab[1])))
    driver.find_element(*owner_repos.PullRequestTab).click()
    WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((owner_repos.Closed[0],owner_repos.Closed[1])))

    driver.find_element(*owner_repos.Closed).click()
    WebDriverWait(driver,wait_time).until(EC.any_of(EC.presence_of_element_located((owner_repos.ClosedW[0],owner_repos.ClosedW[1])),
            EC.presence_of_element_located((owner_repos.Blank0[0],owner_repos.Blank0[1]))))

    elms = driver.find_elements(*owner_repos.PRhref)
    lles = [elm.get_attribute('href') for elm in elms]

    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((owner_repos.PullRequestTab[0],owner_repos.PullRequestTab[1])))
    driver.find_element(*owner_repos.PullRequestTab).click()
    WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((owner_repos.Opened[0],owner_repos.Opened[1])))

    driver.find_element(*owner_repos.Opened).click()
    WebDriverWait(driver,wait_time).until(EC.any_of(EC.presence_of_element_located((owner_repos.OpenedW[0],owner_repos.OpenedW[1])),
            EC.presence_of_element_located((owner_repos.Blank0[0],owner_repos.Blank0[1])),
            EC.presence_of_element_located((owner_repos.Blank1[0],owner_repos.Blank1[1]))))

    elms = driver.find_elements(*owner_repos.PRhref)
    lles.extend([elm.get_attribute('href') for elm in elms])

    print(len(lles), lles)

    commits = 0
    for elm in lles:
        driver.get(elm)

        #print(driver.current_url)
        WebDriverWait(driver, wait_time).until(EC.url_to_be((elm)))

        commit = driver.find_element(*owner_repos.Commits)
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((owner_repos.Commits[0], owner_repos.Commits[1])))
        commit = int(commit.get_attribute('title'))
        #commits = int(commits)
        commits += commit
        print(commits, commit, driver.current_url)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()  # создали объект для опций
service = Service(ChromeDriverManager().install())

import traceback
import pickle
def login():

    full_list, brief_list = [], []
    f = open('datas', 'rb')
    full_list = pickle.load(f)
    brief_list = pickle.load(f)
    f.close()

    #print(full_list)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        for counter, llist in enumerate(brief_list):
            if counter>5:
                break
            if llist[0]=='Yandex-Practicum' or llist[0]=='NelliSm':
                continue
            xxowner(driver,llist[0], llist[1])
            #xxowner(driver,'Vv-jpg-png','Sprint5x')
            #xxowner(driver,'Vv-jpg-png','pproba1')
    except TimeoutException:
        print(f'Плохо {driver.current_url}')
        #traceback.print_list()
        pass
    finally:
        driver.quit()


login()

