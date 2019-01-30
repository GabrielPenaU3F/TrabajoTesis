import math
import unittest

import numpy

from src.core.provider.service_provider import ServiceProvider
from src.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal
from src.domain.senal_audio import SenalAudio, AlineacionException


class AlinearSenalesTest(unittest.TestCase):

    operaciones_service = None

    @classmethod
    def setUpClass(cls):
        cls.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def test_que_alinee_correctamente_una_senal_y_su_version_con_delay(self):
        fs = 5
        senal = SenalAudio(fs, [1, 0, 1, 2, 1])
        senal_a_truncar = SenalAudio(fs, [0, 0, 0, 1, 0, 1, 2, 1])
        senal_resultante = AlinearSenalesTest.operaciones_service.eliminar_delay_entre_senales(senal, senal_a_truncar)\
            .get_valores()

        self.assertListEqual(senal.get_valores(), senal_resultante)

    def test_que_alinee_correctamente_una_senal_y_su_version_con_pequeno_ruido_antes(self):
        fs = 5
        senal = SenalAudio(fs, [1, 0, 1, 2, 1])
        senal_a_truncar = SenalAudio(fs, [0.001, -0.001, 0.003, 1, 0, 1, 2, 1])
        senal_resultante = AlinearSenalesTest.operaciones_service.eliminar_delay_entre_senales(
            senal, senal_a_truncar).get_valores()

        self.assertListEqual(senal.get_valores(), senal_resultante)

    def test_que_alinee_correctamente_una_senal_de_10_segundos_y_su_version_con_pequeno_ruido_antes(self):
        fs = 44100
        frecuencia = 200
        senoide = GeneradorSenoidal().generar_senoide(fs, 10, frecuencia, 1, 0)
        ruido = [0.001, -0.001, 0.003, 0.002, 0.01]
        senoide_a_truncar = SenalAudio(fs, ruido + senoide.get_valores().copy())
        senal_resultante = AlinearSenalesTest.operaciones_service.eliminar_delay_entre_senales(
            senoide, senoide_a_truncar, 0.100).get_valores()

        self.assertListEqual(senoide.get_valores(), senal_resultante)

    def test_que_no_modifique_senales_ya_alineadas(self):
        fs = 44100
        frecuencia = 200
        senoide = GeneradorSenoidal().generar_senoide(fs, 10, frecuencia, 1, 0)
        senoide_a_truncar = GeneradorSenoidal().generar_senoide(fs, 10, frecuencia, 1, 0)
        senal_resultante = AlinearSenalesTest.operaciones_service.eliminar_delay_entre_senales(
            senoide, senoide_a_truncar, 0.100).get_valores()

        self.assertListEqual(senoide.get_valores(), senal_resultante)

    def test_que_lance_excepcion_si_la_ventana_es_mas_larga_que_alguna_senal(self):
        fs = 44100
        frecuencia = 200
        senoide = GeneradorSenoidal().generar_senoide(fs, 2, frecuencia, 1, 0)
        senoide_a_truncar = GeneradorSenoidal().generar_senoide(fs, 2, frecuencia, 1, 0)

        self.assertRaises(AlineacionException, AlinearSenalesTest.operaciones_service.
                          eliminar_delay_entre_senales, senoide, senoide_a_truncar, 5)
