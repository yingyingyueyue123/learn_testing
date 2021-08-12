"""
破除默认 pattern，随心所欲命名测试文件
unittest 有默认的查找 pattern 如下：
查找测试文件，默认查找“test*.py”；
查找测试用例，默认查找“test*”。
我们可以通过更改查找 pattern 的方式来执行所有的测试用例，
"""
# coding=utf-8

import os

import unittest

if __name__ == "__main__":

    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests"),
                                                pattern='*.py', top_level_dir=os.path.dirname(__file__))

    runner = unittest.TextTestRunner(verbosity=2)

    runner.run(suite)

