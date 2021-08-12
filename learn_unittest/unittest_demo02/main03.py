"""
按需组装测试用例
"""
# coding=utf-8

import unittest

# 这里导入TestToRun这个测试类

from learn_unittest.unittest_demo02.tests.test_to_run import TestToRun

from learn_unittest.unittest_demo02.tests.itesting_test import ITestingTest

if __name__ == "__main__":
    # 定义一个测试用例集
    suite = unittest.TestSuite()

    # 把导入进来的TestToRun这个测试类下面的测试方法加入测试用例
    suite.addTest(TestToRun('testAssertNotEqual'))
    suite.addTest(ITestingTest('test_not_equal'))

    # 指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)

    # 运行测试
    runner.run(suite)
