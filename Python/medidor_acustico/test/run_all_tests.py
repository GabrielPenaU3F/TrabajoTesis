import unittest
from src_path import setear_src_path
from suites.suite_full import SuiteFull


setear_src_path()

suite = SuiteFull()
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite.get_suite())

