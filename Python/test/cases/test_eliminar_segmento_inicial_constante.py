import unittest

import numpy
import math

from src.core.provider.action_provider import ActionProvider
from src.core.domain.senal_en_tiempo import SenalEnTiempo


class TestEliminarSegmentoInicialConstante(unittest.TestCase):

    eliminar_segmento_inicial_constante_action = None

    @classmethod
    def setUpClass(cls):
        cls.eliminar_segmento_inicial_constante_action = ActionProvider.provide_eliminar_segmento_inicial_constante_action()

    def test_que_elimine_correctamente_un_segmento_inicial_constante(self):
        dominio_temporal = numpy.arange(0, 5, 1)
        valores = [0, 0, 0, 1, 3]
        tolerancia = math.pow(10, -7)
        esperado = [0, 1, 3]

        self.assertListEqual(esperado, TestEliminarSegmentoInicialConstante.eliminar_segmento_inicial_constante_action
                             .execute(SenalEnTiempo(dominio_temporal, valores), tolerancia).get_valores())

    def test_que_no_elimine_un_segmento_constante_que_no_esta_al_inicio(self):
        dominio_temporal = numpy.arange(0, 10, 1)
        valores = [1, 3, 1]
        valores.extend(numpy.zeros(7))
        tolerancia = math.pow(10, -7)

        self.assertListEqual(valores, TestEliminarSegmentoInicialConstante.eliminar_segmento_inicial_constante_action
                             .execute(SenalEnTiempo(dominio_temporal, valores), tolerancia).get_valores())

    def test_que_elimine_correctamente_un_segmento_inicial_inferior_a_la_tolerancia(self):
        dominio_temporal = numpy.arange(0, 5, 1)
        valores = [0, 0.01, 0.02, 1, 3]
        tolerancia = 0.1
        esperado = [0.02, 1, 3]

        self.assertListEqual(esperado, TestEliminarSegmentoInicialConstante.eliminar_segmento_inicial_constante_action
                             .execute(SenalEnTiempo(dominio_temporal, valores), tolerancia).get_valores())



