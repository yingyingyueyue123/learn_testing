# -*- coding: utf-8 -*-

import json

import requests

from selenium import webdriver

from page_objects import PageObject, PageElement



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



class BasePage(PageObject):

    def __init__(self, login_credential, target_page):

        self.login_url = 'https://ones.ai/project/api/project/auth/login'

        self.header = {

            "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",

            "content-type": "application/json"}

        self.s = requests.Session()

        self.driver = webdriver.Chrome()

        self._api_login(login_credential, target_page)

    def _api_login(self, login_credential, target_page):

        target_url = json.loads(json.dumps(target_page))

        try:

            result = self.s.post(self.login_url, data=json.dumps(login_credential), headers=self.header)

            assert result.status_code == 200

            assert json.loads(result.text)["user"]["email"].lower() == login_credential["email"]

        except Exception:

            raise Exception("Login Failed, please check!")

        all_cookies = self.s.cookies._cookies[".ones.ai"]["/"]

        self.driver.get(target_url["target_page"])

        self.driver.delete_all_cookies()

        for k, v in all_cookies.items():

            self.driver.add_cookie(cookie_to_selenium_format(v))

        self.driver.get(target_url["target_page"])

        return self.driver
