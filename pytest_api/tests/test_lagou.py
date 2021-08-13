# coding=utf-8

import json

import requests


class TestLaGou:

    # 在pytest里，针对一个类方法的setup为setup_method,

    # setup_method作用同unittest里的setUp()

    def setup_method(self, method):
        self.s = requests.Session()

        self.url = 'https://www.lagou.com'

    def test_visit_lagou(self):
        result = self.s.get(self.url)

        assert result.status_code == 200

        assert '拉勾' in result.text

    def test_get_new_message(self):
        # 此处需要一个方法登录获取登录的cookie

        message_url = 'https://gate.lagou.com/v1/entry/message/newMessageList'

        cookie = {

            'cookie': '_ga=GA1.2.975149547.1597507593; gate_login_token=a4124d4588a4a9d4bbc5b6d617f02615fc09b5e4917408aa63e89ccffdac3010'}

        headers = {'x-l-req-header': '{deviceType: 9}'}

        # 直接带登录态发送请求

        result = self.s.get(message_url, cookies=cookie, headers=headers)

        assert result.status_code == 200

        assert json.loads(result.content)['message'] == '成功'

    # 在pytest里，针对一个类方法的teardown为teardown_method,

    # teardown_method作用同unittest里的dearDown()

    def teardown_method(self, method):
        self.s.close()
