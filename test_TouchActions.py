import time

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchActions():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        # option.debugger_address="/localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get('http://www.baidu.com')
        ele = self.driver.find_element_by_id('kw')
        ele_search = self.driver.find_element_by_id('su')
        ele.send_keys("selenium")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        # action.perform()
        time.sleep(3)
        action.scroll_from_element(ele, 0, 1000).perform()
        time.sleep(3)

