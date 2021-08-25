# conftest.py

import pytest

from selenium import webdriver

import requests


@pytest.fixture(scope="session")
# 此方法名可以是你登录的业务代码，也可以是其他，这里暂命名为login

def login():
    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    base_url = "http://www.baidu.com/"

    s = requests.Session()

    yield driver, s, base_url

    print('turn off browser driver')

    driver.quit()

    print('turn off requests driver')

    s.close()


@pytest.fixture(scope="function", autouse=True)
def connect_db():
    print('connecting db')

    # 此处写你的链接db的业务逻辑

    pass
