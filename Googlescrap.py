import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# (find_element(By.CLASS_NAME, 클래스이름)) By 모듈 import 필요
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class GoogleKeywordScreenshooter:
    def __init__(self, keyword, screenshots_dir):
        # deprecated please pass in a service object in Selenium Python 문제
        self.service = Service("C:\\Users\\jjang\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.service)
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        # 해당 부분 알아보기
        self.browser.maximize_window()
        self.browser.get("https://www.google.com")
        # 페이지 로딩을 위한 대기
        time.sleep(7)
        # 팝업창 없애기 위한 탭키 프레스 + 엔터
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.TAB * 7)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        # find_element_by_class_name 문제 (find_element(By.CLASS_NAME, 클래스이름))
        search_bar = self.browser.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
            #페이지 로딩대기
            unnecessary = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))
            self.browser.execute_script(unnecessary)
        except Exception:
            pass
            '''
            #맥시멈 페이지 넘버 출력
            number = browser.find_element(By.CLASS_NAME, "AaVjTc")
            print(number.text)
            '''
        # 검색결과 태그확인 (web element 확인-> 자식요소 접근가능)
        search_results = self.browser.find_elements(By.CLASS_NAME, "g")
        # 검색결과 스크린샷 찍기
        for index, search_result in enumerate(search_results):
            class_name = search_result.get_attribute("class")
            if "VjDLd mnr-c g-blk" not in class_name:
                search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")

    def finish(self):
        self.browser.quit()

# 검색결과들 타이틀 확인
'''for search_result in search_results:
    title = search_result.find_element(By.TAG_NAME, "h3")
    if title:
        print(title.text)
'''

