# coding=utf-8

from ddt import ddt, data, file_data, unpack

from selenium import webdriver

import unittest

import time


# ddt一定是装饰在TestCase的子类上

@ddt
class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)

        self.base_url = "http://www.baidu.com/"

    # data表示data是直接提供的。

    # unpack表示，对于每一组数据，如果它的值是list或者tuple，那么就分拆成独立的参数。

    @data(['iTesting', 'iTesting'], ['helloqa.com', 'iTesting'])
    @unpack
    def test_baidu_search(self, search_string, expect_string):
        driver = self.driver

        driver.get(self.base_url + "/")

        driver.find_element_by_id("kw").send_keys(search_string)

        driver.find_element_by_id("su").click()

        time.sleep(2)

        search_results = driver.find_element_by_xpath('//*[@id="1"]/div/h3/a').get_attribute('innerHTML')

        print(search_results)

        self.assertEqual(expect_string in search_results, True)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
