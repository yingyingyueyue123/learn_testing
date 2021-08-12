# coding=utf-8
"""

import os

import unittest

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests"), pattern='*.py',
                                                top_level_dir=os.path.dirname(__file__))

    runner = unittest.TextTestRunner(verbosity=2)

    runner.run(suite)
"""

import unittest
import os

from learn_testing.unittest_web.test_web_demo1.common.html_reporter import GenerateReport

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests"),
                                                pattern='*.py', top_level_dir=os.path.dirname(__file__))

    html_report = GenerateReport()

    html_report.generate_report(suite)
