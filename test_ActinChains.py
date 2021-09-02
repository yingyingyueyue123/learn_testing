test_TouchActions.py# coding=utf-8
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActions():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        time.sleep(3)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('http://www.baidu.com')
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_id('dragger')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element).perform()
        time.sleep(3)

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('//input[@type="textbox"]')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
