import math
import unittest

import numpy
from numpy import mean, std
from core.domain.generadores_de_senales.generador_ruido import GeneradorRuido


class RuidoTest(unittest.TestCase):

    generador_ruido = None

    @classmethod
    def setUpClass(cls):
        cls.generador_ruido = GeneradorRuido()

    def test_que_el_ruido_blanco_sea_aproximadamente_gaussiano(self):

        mu = 0
        sigma = 1
        ruido_blanco = RuidoTest.generador_ruido.generar_ruido_blanco(48000, 6, mu, sigma)

        numpy.testing.assert_almost_equal(mean(ruido_blanco.get_valores()), 0, decimal=2)
        numpy.testing.assert_almost_equal(std(ruido_blanco.get_valores()), 1, decimal=2)

    def test_que_el_espectro_del_ruido_blanco_sea_no_nulo_en_toda_f(self):

        mu = 0
        sigma = 1
        ruido_blanco = RuidoTest.generador_ruido.generar_ruido_blanco(48000, 6, mu, sigma)
        espectro = ruido_blanco.get_modulos_frecuencia()
        nulos = 0
        for i in range(len(espectro)):
            if espectro[i] < math.pow(10, -3):
                nulos += 1

        self.assertEqual(0, nulos)
