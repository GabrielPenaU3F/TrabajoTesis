import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.discover('./cases'))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
