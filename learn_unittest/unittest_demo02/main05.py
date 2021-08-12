"""
测试方法的默认查找方式
"""
# coding=utf-8

import os

import unittest

if __name__ == "__main__":

    loader = unittest.defaultTestLoader

    # 设置仅运行以equal开头的测试用例
    loader.testMethodPrefix = 'equal'

    suite = loader.discover(start_dir=os.path.join(os.path.dirname(__file__), "tests"), pattern='*.py', top_level_dir=os.path.dirname(__file__))

    runner = unittest.TextTestRunner(verbosity=2)

    runner.run(suite)
