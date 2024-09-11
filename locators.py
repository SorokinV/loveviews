from selenium.webdriver.common.by import By

class Locator:
    locator0 = (By.XPATH, '//span[@data-hovercard-type="repository"]')
    locatorw1 = (By.XPATH, '//*[@id="js-contribution-activity"]/div[2]')
class owner_repos:
    PullRequestTab = (By.ID, 'pull-requests-tab')
    Opened = (By.XPATH,'//a[@data-ga-click="Pull Requests, Table state, Open"]')
    OpenedW = (By.XPATH, '//span[@aria-label="Open Pull Request"]')

    Closed = (By.XPATH,'//a[@data-ga-click="Pull Requests, Table state, Closed"]')
    ClosedW = (By.XPATH, '//span[@aria-label="Closed Pull Request"]')

    OCWait = (By.CLASS_NAME,'table-list-header-toggle states flex-auto pl-0')
    PRhref = (By.XPATH, "//a[@data-hovercard-type='pull_request']")
    Issues = (By.XPATH, "//div[@aria-label='Issues']" )
    Blank0 = (By.XPATH, "//h3[text()='No results matched your search.']" )
    Blank1 = (By.XPATH, '//h3/text="There aren'+"'"+'t any open pull requests."')
    locatorCC= (By.XPATH, '//span[@id="commits_tab_counter"]')

class Where:
    main_pass = 'https://github.com/irisqul'

#//*[@id="js-contribution-activity"]/div[2]
#<a class="d-block d-md-none position-absolute top-0 bottom-0 left-0 right-0"
#aria-label="Link to Issue. Update README.md" href="/Vv-jpg-png/pproba1/pull/1"
#data-turbo-frame="repo-content-turbo-frame"></a>
#<a id="issue_1_link"
#class="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"
#data-hovercard-type="pull_request"
#data-hovercard-url="/Vv-jpg-png/pproba1/pull/1/hovercard"
#href="/Vv-jpg-png/pproba1/pull/1"
#data-turbo-frame="repo-content-turbo-frame">
#Update README.md</a>

#<span id="commits_tab_counter" title="4"
#data-view-component="true"
#class="Counter js-updateable-pull-request-commits-count">4</span>