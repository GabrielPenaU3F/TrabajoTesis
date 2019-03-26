import unittest

from src_path import setear_src_path


def construir_test_suite():
    suite = unittest.TestSuite()
    suite.addTests(loader.discover('cases'))
    return suite


#setear_src_path()
loader = unittest.TestLoader()
suite = construir_test_suite()
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
