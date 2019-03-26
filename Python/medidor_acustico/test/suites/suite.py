from abc import ABC


class Suite(ABC):

    def __init__(self, suite, loader):
        self.suite = suite
        self.suite.addTests(loader.discover('cases'))

    def get_suite(self):
        return self.suite
