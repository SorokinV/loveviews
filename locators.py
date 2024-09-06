from selenium.webdriver.common.by import By

class Locator:
    locator2 = (By.XPATH, '//*[@id="js-contribution-activity"]/div[2]/div/div/div[2]/details/summary/span[2]/span[2]')
    locator3 = (By.XPATH, '//span[@class="Details-content--closed float-right"]')
    locator4 = (By.XPATH, '//span[@class="d-inline-block float-right"]')
    locator1 = (By.XPATH, '//main')


##<span class="Details-content--closed float-right" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:51861420,&quot;target&quot;:&quot;TIMELINE_CATEGORY_ROLLUP_EXPAND&quot;,&quot;user_id&quot;:177808467,&quot;originating_url&quot;:&quot;https://github.com/irisqul?action=show&amp;controller=profiles&amp;tab=contributions&amp;user_id=irisqul&quot;}}" data-hydro-click-hmac="f0ff594a7d194fc932aff610dfe0b41d7195d4fc435f30b5e22fb7f064b719d2"></span>
class Where:
    main_passx= 'https://github.com/irisqul'
    main_pass = 'https://github.com/irisqul?tab=overview&from=2024-07-01&to=2024-08-30'
