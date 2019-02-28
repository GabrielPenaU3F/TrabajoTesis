import math
import unittest

from src.core.domain.generadores_de_senales.generador_mls import GeneradorMLS


class MLSTest(unittest.TestCase):

    def test_que_la_senal_mls_solo_tenga_unos_y_menos_unos(self):
        fs = 48000
        n_bits = 17
        periodos = 8
        senal_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs)
        valores_mls = senal_mls.get_valores()
        cuenta = 0
        for i in valores_mls:
            if i != 1 and i != -1:
                cuenta += 1
        self.assertEqual(0, cuenta)

    def test_que_la_longitud_de_un_periodo_sea_la_esperada(self):
        fs = 48000
        n_bits = 17
        periodos = 1
        senal_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs)
        longitud_esperada = math.pow(2, 17) - 1

        self.assertEqual(longitud_esperada, senal_mls.get_longitud())

    def test_que_la_longitud_de_ocho_periodos_sea_la_esperada(self):
        fs = 48000
        n_bits = 17
        periodos = 8
        senal_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs)
        longitud_esperada = 8 * (math.pow(2, 17) - 1)

        self.assertEqual(longitud_esperada, senal_mls.get_longitud())
