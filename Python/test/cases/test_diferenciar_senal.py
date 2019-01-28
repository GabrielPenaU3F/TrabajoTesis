import unittest

from src.core.provider.service_provider import ServiceProvider


class DiferenciarSenalTest(unittest.TestCase):

    operaciones_service = None

    @classmethod
    def setUpClass(cls):
        cls.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()


