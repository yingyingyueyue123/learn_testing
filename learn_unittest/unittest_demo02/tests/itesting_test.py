# itesting_test.py

# coding=utf-8


import unittest


# 测试类必须要继承TestCase类

class ITestingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('整个测试类只执行一次 -- Start')

    def setUp(self):
        print('每个测试开始前执行一次')

    # 测试用例默认以test开头

    def equal_test(self):
        self.assertEqual(1, 1)

    def test_not_equal(self):
        self.assertNotEqual(1, 0)

    def tearDown(self):
        print('每个测试结束后执行一次')

    @classmethod
    def tearDownClass(cls):
        print('整个测试类只执行一次 --')
