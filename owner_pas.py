import locators
from locators import owner_repos
import time

wait_time = 10
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def xxowner(driver, name, repos):
    connect_str = f'https://github.com/{name}/{repos}/'
    driver.get(connect_str)
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((owner_repos.PullRequestTab[0],owner_repos.PullRequestTab[1])))
    driver.find_element(*owner_repos.PullRequestTab).click()
    WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((owner_repos.Closed[0],owner_repos.Closed[1])))

    driver.find_element(*owner_repos.Closed).click()
    WebDriverWait(driver,wait_time).until(EC.any_of(EC.presence_of_element_located((owner_repos.ClosedW[0],owner_repos.ClosedW[1])),
            EC.presence_of_element_located((owner_repos.Blank0[0],owner_repos.Blank0[1])),
            EC.presence_of_element_located((owner_repos.Blank1[0],owner_repos.Blank1[1]))))

    elms = driver.find_elements(*owner_repos.PRhref)
    for elm in elms:
        print(elm.text)
    lles = [elm.get_attribute('href') for elm in elms]

    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((owner_repos.PullRequestTab[0],owner_repos.PullRequestTab[1])))
    driver.find_element(*owner_repos.PullRequestTab).click()
    WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((owner_repos.Opened[0],owner_repos.Opened[1])))

    driver.find_element(*owner_repos.Opened).click()
    WebDriverWait(driver,wait_time).until(EC.any_of(EC.presence_of_element_located((owner_repos.ClosedW[0],owner_repos.ClosedW[1])),
            EC.presence_of_element_located((owner_repos.Blank0[0],owner_repos.Blank0[1])),
            EC.presence_of_element_located((owner_repos.Blank1[0],owner_repos.Blank1[1]))))

    elms = driver.find_elements(*owner_repos.PRhref)
    lles.extend([elm.get_attribute('href') for elm in elms])
    print(len(lles))
    print(lles)

    '''
    for elm in elms:
        print(driver.current_url)
        print(elm.get_attribute('href'))
        
        elm.click()
        
        commits = driver.find_element(*owner_repos.locatorCC)
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((owner_repos.locatorCC[0], owner_repos.locatorCC[1])))
        commits = commits.get_attribute('title')
        commits = int(commits)
        print(commits)
        driver.back()
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((owner_repos.locatorPW[0], owner_repos.locatorPW[1])))
     '''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()  # создали объект для опций
service = Service(ChromeDriverManager().install())

def login():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        #xxowner(driver,'Vv-jpg-png','Sprint5x')
        xxowner(driver,'Vv-jpg-png','pproba1')
    except TimeoutException:
        print(f'Плохо {driver.current_url}')
    finally:
        driver.quit()


login()

