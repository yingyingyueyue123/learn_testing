"""
动态查找测试用例运行
unittest.TestLoader.discover(start_dir, pattern='test*.py', top_level_dir=None)
unittest 允许你从某个文件夹开始，递归查找所有符合筛选条件的测试用例，并且返回一个包含这些测试用例的 TestSuite 对象，
start_dir：起始文件夹的路径；
pattern（匹配模式）：默认搜索所有以“test”开头的测试文件，并把这些文件里的以“test”开头的测试用例挑选出来；
top_level_dir（根目录）：测试模块必须从根目录导入，如果 start_dir 的位置不是根目录，那么必须显式指定 top_level_dir。
"""
# coding=utf-8

import os

import unittest

if __name__ == "__main__":
    loader = unittest.defaultTestLoader
    # 生成测试用suite
    suite = loader.discover(os.path.join(os.path.dirname(__file__), 'tests'), top_level_dir=os.path.dirname(__file__))

    # 指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)

    # 运行suite
    runner.run(suite)
