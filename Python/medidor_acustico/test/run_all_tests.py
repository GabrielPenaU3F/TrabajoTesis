import unittest
from test.suites.suite_full import SuiteFull

suite = SuiteFull()
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite.get_suite())

