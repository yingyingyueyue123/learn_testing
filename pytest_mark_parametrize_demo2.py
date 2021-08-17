# -*- coding: utf-8 -*-

# test_baidu.py

import time

import pytest

from selenium import webdriver


@pytest.mark.baidu
class TestBaidu:

    def setup_method(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(30)

        self.base_url = "http://www.baidu.com/"

    @pytest.mark.parametrize('search_string, expect_string', [('iTesting', 'iTesting'), ('helloqa.com', 'iTesting')])
    def test_baidu_search(self, search_string, expect_string):
        driver = self.driver

        driver.get(self.base_url + "/")

        driver.find_element_by_id("kw").send_keys(search_string)

        driver.find_element_by_id("su").click()

        time.sleep(2)

        search_results = driver.find_element_by_xpath('//*[@id="1"]/div/h3/a').get_attribute('innerHTML')

        assert (expect_string in search_results) is True

    def teardown_method(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(["-m", "baidu", "-s", "-v", "-k", "test_baidu_search", "test_baidu.py"])
