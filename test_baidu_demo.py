"""
执行：pytest test_baidu_demo.py --alluredir=./result/1
生成测试报告：allure serve ./result/1
"""
import allure
import pytest
from selenium import webdriver
import time


@allure.testcase("用例管理地址")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://baidu.com")
        driver.maximize_window()
        time.sleep(2)
    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./p.png")
        allure.attach.file("./p.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()
