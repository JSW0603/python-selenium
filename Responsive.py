import time
from math import ceil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\jjang\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
browser = webdriver.Chrome(service=service)

browser.get("https://www.goal.com/en/news/1")
browser.maximize_window()

time.sleep(3)

actions = ActionChains(browser)
actions.send_keys(Keys.TAB * 2)
actions.send_keys(Keys.ENTER)
actions.perform()

sizes = [480, 760, 1040, 1200, 1936]
for size in sizes:
    browser.set_window_size(size, 1056)
    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    scroll_size = browser.execute_script("return document.body.scrollHeight;")
    total_section = ceil(scroll_size/1056)
    for section in range(total_section):
        browser.execute_script(f"window.scrollTo(0,{(section*1056)}+1)")
        browser.save_screenshot(f"screenshots1/{size}x{section}.png")
        time.sleep(2)

browser.quit()