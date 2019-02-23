import unittest

import numpy

from src.core.provider.service_provider import ServiceProvider
from src.core.domain.senal_en_tiempo import SenalEnTiempo


class DiferenciarSenalTest(unittest.TestCase):

    operaciones_service = None

    @classmethod
    def setUpClass(cls):
        cls.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()


    def test_que_diferencie_correctamente_un_vector_escalera(self):
        dominio_temporal = numpy.arange(0, 5, 1)
        escalera = numpy.arange(0, 5, 1)
        esperado = [1, 1, 1, 1, -4]

        self.assertListEqual(esperado, DiferenciarSenalTest.operaciones_service.
                             evaluar_diferencias_finitas_hacia_adelante(SenalEnTiempo(dominio_temporal, escalera))
                             .get_valores())


