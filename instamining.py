import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service("C:\\Users\\jjang\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
browser = webdriver.Chrome(service=service)

browser.maximize_window()
browser.get("https://www.naver.com/")
time.sleep(4)

id_input = browser.find_element(By.NAME, "username")
id_input.send_keys("jjangsw0603@gmail.com")
id_input.send_keys(Keys.TAB)
pw_input = browser.find_element(By.NAME, "password")
pw_input.send_keys("")
pw_input.send_keys(Keys.ENTER)
time.sleep(4)

actions = ActionChains(browser)
actions.send_keys(Keys.TAB*2)
actions.send_keys(Keys.ENTER).perform()
time.sleep(4)

actions = ActionChains(browser)
actions.send_keys(Keys.TAB*2)
actions.send_keys(Keys.ENTER).perform()
time.sleep(4)

browser.get("https://www.instagram.com/explore/tags/macbookpro/")
time.sleep(4)
browser.quit()
