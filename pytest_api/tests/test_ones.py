"""
代码解析
1.首先，创建了一个 .py 文件在 lagouAPITest 下的 tests 文件夹中，名为 test_ones.py.

2.接着，定义了一个方法 cookie_to_selenium_format 用来进行 cookie 解析和转换。

为什么要定义这个方法？ 因为通过接口 requests.Session() 发送请求拿到的 cookies 格式，与通过浏览器（self.driver.get_cookies()）拿到的 cookies 格式是不一样的。接口请求拿到的 cookie 要想在浏览器里使用，必须转换成浏览器支持的格式。

cookie_to_selenium_format 是一个通用的方法，你同样可以将其用到其他网站。

3.其次，创建了一个测试类 TestOneAI，并设置了 setup 和 teardown 操作。

setup_method 用于测试开始前初始化 requests.Session() 实例，以及 WebDriver 实例，并且指定了接口请求使用的接口地址和通过 UI 直接访问的页面地址。teardown_method 用于测试结束后关闭 Session，以及 WebDriver 实例。

4.然后，创建了我们的测试方法 test_merge_api_ui。

在这个测试方法里，我首先是要 self.s，即 requests.Session() 进行接口登录；登录成功后，我解析获取到的 cookies，并通过刚刚提到的函数 cookie_to_selenium_format 转换为 Selenium/webDriver 可以识别的 cookie 格式；然后把拿到的每一个 cookie，使用 Selenium 里的 add_cookie 方法塞到浏览器的 Driver 里。因为这些 cookies 中保留了登录的信息，所以当此操作完成后，我再使用浏览器进行页面操作，就无须登录了。

由此，API 测试和 UI 测试就融合了。在后续测试中，我可以按照需要或者直接发送接口请求，或者通过 UI 访问，就都不会出错了。因为登录信息已经在 self.s.cookies 和 self.driver 里保存了。
"""

# -*- coding: utf-8 -*-

import json

import requests

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


# 把获取的cookie转换成Selenium/WebDriver能识别的格式

def cookie_to_selenium_format(cookie):
    cookie_selenium_mapping = {'path': '', 'secure': '', 'name': '', 'value': '', 'expires': ''}

    cookie_dict = {}

    if getattr(cookie, 'domain_initial_dot'):

        cookie_dict['domain'] = '.' + getattr(cookie, 'domain')

    else:

        cookie_dict['domain'] = getattr(cookie, 'domain')

    for k in list(cookie_selenium_mapping.keys()):
        key = k

        value = getattr(cookie, k)

        cookie_dict[key] = value

    return cookie_dict


class TestOneAI:

    # 在pytest里，针对一个类方法的setup为setup_method,

    # setup_method作用同unittest里的setUp()

    def setup_method(self, method):

        self.s = requests.Session()

        self.login_url = 'https://ones.ai/project/api/project/auth/login'

        self.home_page = 'https://ones.ai/project/#/home/project'

        self.header = {

            "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",

            "content-type": "application/json"}

        self.driver = webdriver.Chrome()

    # 使用了pytest里的参数化

    @pytest.mark.parametrize('login_data, project_name',
                             [({"password": "zhenshimima", "email": "zhangyuexinglong@163.com"}, {"project_name": "zy"})])
    def test_merge_api_ui(self, login_data, project_name):

        # 接口登录

        result = self.s.post(self.login_url, data=json.dumps(login_data), headers=self.header)

        # 断言登录成功

        assert result.status_code == 200

        assert json.loads(result.text)["user"]["email"].lower() == login_data["email"]

        # 根据实际情况解析cookies，此处需结合业务场景

        all_cookies = self.s.cookies._cookies[".ones.ai"]["/"]

        # 删除所有cookies

        self.driver.get(self.home_page)

        self.driver.delete_all_cookies()

        # 把接口登录后的cookie塞到Selenium driver里去，传递登录状态

        for k, v in all_cookies.items():
            self.driver.add_cookie(cookie_to_selenium_format(v))

        # 再次访问目标页面，此时登录状态已经传递过来了

        self.driver.get(self.home_page)

        # 查找项目元素，获取元素的值，并进行断言

        # 注意，此时我浏览器操作就不需再登录了

        try:

            element = WebDriverWait(self.driver, 30).until(

                EC.presence_of_element_located((By.CSS_SELECTOR, '[class="company-title-text"]')))

            # 断言我的项目存在

            assert element.get_attribute("innerHTML") == project_name["project_name"]

        except TimeoutError:

            raise TimeoutError('Run time out')

    # 在pytest里，针对一个类方法的teardown为teardown_method,

    # teardown_method作用同unittest里的dearDown()

    def teardown_method(self, method):

        self.s.close()

        self.driver.quit()
