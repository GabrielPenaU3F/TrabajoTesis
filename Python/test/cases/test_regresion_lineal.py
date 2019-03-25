import math
import unittest
from core.provider.service_provider import ServiceProvider
from exception.excepciones import RegresionException


class RegresionLinealTest(unittest.TestCase):

    estadistica_service = None

    @classmethod
    def setUpClass(cls):
        cls.estadistica_service = ServiceProvider.provide_estadistica_service()

    def test_que_los_parametros_estimados_sean_1_y_2(self):

        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [1.9999, 3.0001, 4.0001, 4.9999, 5.9999, 7.0001, 8.0001, 8.9999, 10, 11.0001]

        recta = RegresionLinealTest.estadistica_service.efectuar_regresion_lineal(x, y)
        self.assertAlmostEqual(1, recta.get_pendiente(), delta=math.pow(10, -4))
        self.assertAlmostEqual(2, recta.get_ordenada(), delta=math.pow(10, -4))

    def test_que_si_fijo_la_ordenada_a_cero_la_pendiente_sea_8_coma_3333(self):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [1.9999, 3.0001, 4.0001, 4.9999, 5.9999, 7.0001, 8.0001, 8.9999, 10, 11.0001]

        recta = RegresionLinealTest.estadistica_service.efectuar_regresion_lineal(x, y, True)
        self.assertAlmostEqual(8.3333, recta.get_pendiente(), delta=math.pow(10, -4))
        self.assertEqual(0, recta.get_ordenada())

    def test_que_si_los_datos_son_incorrectos_lance_excepcion(self):
        x = [0, 1, 2]
        y = [0, 1]

        self.assertRaises(RegresionException, RegresionLinealTest.estadistica_service.efectuar_regresion_lineal, x, y)
