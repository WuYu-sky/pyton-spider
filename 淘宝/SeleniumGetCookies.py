from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
import requests
from requests.cookies import RequestsCookieJar
from fake_useragent import UserAgent


class SeleniumGetCookies:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        self.session = requests.Session()
        self.session.headers.update(headers)

        option = webdriver.ChromeOptions()
        option.add_argument('--headless')    # 无头模式
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                        Object.defineProperty(navigator, 'webdriver', {
                          get: () => undefined
                        })
                      """
        })

        self.driver.maximize_window()
        self.driver.get('https://www.taobao.com/?spm=a230r.1.0.0.2dbc56bcMjHM4u')

    def login(self):
        # 点击登录
        wait.WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '.site-nav-sign > a'))
        self.driver.find_element(By.CSS_SELECTOR, '.site-nav-sign > a').click()

        # 输入账号密码登录
        self.driver.find_element(By.CSS_SELECTOR, '#fm-login-id').send_keys(self.user)
        self.driver.find_element(By.CSS_SELECTOR, '#fm-login-password').send_keys(self.pwd)
        self.driver.find_element(By.CSS_SELECTOR, '.fm-btn > button').click()

    def inspect_login(self):
        wait.WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, '.site-nav-user > a'))
        user = self.driver.find_element(By.CSS_SELECTOR, '.site-nav-user > a').text
        if user == 'tb784384880':
            print('登录成功')
            return True
        else:
            print('登录失败')
            return False

    def load_to_requests(self):
        selenium_cookies = self.driver.get_cookies()
        tmp_cookies = RequestsCookieJar()
        for item in selenium_cookies:
            tmp_cookies.set(item["name"], item["value"])

        self.session.cookies.update(tmp_cookies)

    def run(self):
        self.login()
        if self.inspect_login():
            self.load_to_requests()
            self.driver.close()
            self.driver.quit()
            return self.session
        else:
            return False



if __name__ == '__main__':
    urls = ['?id=664768328917&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=664768328917&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=653911975707&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=653911975707&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633122382954&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633122382954&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633122374396&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633122374396&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=642440337216&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=642440337216&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=631289418577&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=631289418577&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633364667229&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633364667229&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=636757119009&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=636757119009&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=636773659862&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=636773659862&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=654461333141&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=654461333141&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=632545660325&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=632545660325&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=637810224087&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=637810224087&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=650971454698&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=650971454698&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=632219109136&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=632219109136&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=646571555648&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=646571555648&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=645871261418&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=645871261418&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=641593311423&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=641593311423&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=668871246066&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=668871246066&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=668248064954&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=668248064954&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=635851716924&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=635851716924&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=641363377586&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=641363377586&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=668694453304&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=668694453304&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=669470934293&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=669470934293&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633143955054&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=633143955054&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=637705645269&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=637705645269&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=645947880926&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=645947880926&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=646968509357&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=646968509357&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=645872025427&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=645872025427&rn=2f25e8cdab07b690ca704d7fe15430f2&abbucket=7', '?id=631289418577&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=631289418577&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=632219109136&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=632219109136&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=632545660325&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=632545660325&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633122374396&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633122374396&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633122382954&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633122382954&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633143955054&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633143955054&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633364667229&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=633364667229&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=635851716924&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=635851716924&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=636757119009&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=636757119009&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=636773659862&rn=2f25e8cdab07b690ca704d7fe15430f2', '?id=636773659862&rn=2f25e8cdab07b690ca704d7fe15430f2']
    print(len(urls))
    urls = set(urls)
    print(len(urls))