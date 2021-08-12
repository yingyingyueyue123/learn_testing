# coding=utf-8

"""
Test Fixture 通常用来做测试用例的准备或者清理工作。
比如测试开始前的数据准备或者测试结束后的数据清理等。Python 通过 setUp()、tearDown()、
setUpClass()、tearDownClass() 这 4 个钩子函数（Hook）来实现测试的准备和清理工作。
"""
import unittest


# 测试类必须要继承TestCase类
class TestSample(unittest.TestCase):

    # 类共享的fixture，在整个测试类执行过程中仅仅执行一次，需加装饰器@classmethod
    @classmethod
    def setUpClass(cls):
        print('整个测试类只执行一次 -- Start')

    # 测试用例fixture
    def setUp(self):
        print('每个测试开始前执行一次')

    # 测试用例默认以test开头
    def test_equal(self):
        self.assertEqual(1, 1)

    def test_not_equal(self):
        self.assertNotEqual(1, 0)

    # 测试用例fixture
    def tearDown(self):
        print('每个测试结束后执行一次')

    # 类共享的fixture，在整个测试类执行过程中仅仅执行一次，需加装饰器@classmethod
    @classmethod
    def tearDownClass(cls):
        print('整个测试类只执行一次 -- End')


if __name__ == '__main__':
    unittest.main()
