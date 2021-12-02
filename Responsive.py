import time
from math import ceil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

class ResponsiveTester:
    def __init__(self, urls):
        self.service = Service("C:\\Users\\jjang\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.service)
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480, 760, 1040, 1200, 1936]

    def screenshot(self, url):
        self.browser.get(url)
        time.sleep(3)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.TAB * 2)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        for size in self.sizes:
            self.browser.set_window_size(size, 1056)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script("return document.body.scrollHeight;")
            total_section = ceil(scroll_size/1056)
            for section in range(total_section):
                self.browser.execute_script(f"window.scrollTo(0,{(section*1056)}+1)")
                self.browser.save_screenshot(f"screenshots1/{size}x{section}.png")
                time.sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshot(url)

tester = ResponsiveTester(["https://www.goal.com/en/news/1", "https://www.google.com"])
tester.start()
