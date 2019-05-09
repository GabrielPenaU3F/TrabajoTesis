import unittest

from test.suites.suite import Suite


class SuiteFull(Suite):

    def __init__(self):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        super().__init__(suite, loader)

