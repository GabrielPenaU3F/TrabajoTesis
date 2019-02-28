import unittest

from src.core.provider.action_provider import ActionProvider
from src.core.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal
from src.core.domain.senal_audio import SenalAudio, AlineacionException


class AlinearSenalesTest(unittest.TestCase):

    eliminar_latencia_action = None

    @classmethod
    def setUpClass(cls):
        cls.eliminar_latencia_action = ActionProvider.provide_eliminar_latencia_action()

    def test_que_alinee_correctamente_una_senal_y_su_version_con_delay(self):
        fs = 5
        senal = SenalAudio(fs, [1, 0, 1, 2, 1])
        senal_a_truncar = SenalAudio(fs, [0, 0, 0, 1, 0, 1, 2, 1])
        senal_resultante = AlinearSenalesTest.eliminar_latencia_action.execute(senal, senal_a_truncar)\
            .get_valores()

        self.assertListEqual(senal.get_valores(), senal_resultante)

    def test_que_alinee_correctamente_una_senal_y_su_version_con_pequeno_ruido_antes(self):
        fs = 5
        senal = SenalAudio(fs, [1, 0, 1, 2, 1])
        senal_a_truncar = SenalAudio(fs, [0.001, -0.001, 0.003, 1, 0, 1, 2, 1])
        senal_resultante = AlinearSenalesTest.eliminar_latencia_action.execute(
            senal, senal_a_truncar).get_valores()

        self.assertListEqual(senal.get_valores(), senal_resultante)

    def test_que_alinee_correctamente_una_senal_de_10_segundos_y_su_version_con_pequeno_ruido_antes(self):
        fs = 48000
        frecuencia = 200
        senoide = GeneradorSenoidal().generar_senoide(fs, 10, frecuencia, 1, 0)
        ruido = [0.001, -0.001, 0.003, 0.002, 0.01]
        senoide_a_truncar = SenalAudio(fs, ruido + senoide.get_valores().copy())
        senal_resultante = AlinearSenalesTest.eliminar_latencia_action.execute(
            senoide, senoide_a_truncar, 0.100).get_valores()

        self.assertListEqual(senoide.get_valores(), senal_resultante)

    def test_que_no_modifique_senales_ya_alineadas(self):
        fs = 48000
        frecuencia = 200
        senoide = GeneradorSenoidal().generar_senoide(fs, 10, frecuencia, 1, 0)
        senoide_a_truncar = GeneradorSenoidal().generar_senoide(fs, 10, frecuencia, 1, 0)
        senal_resultante = AlinearSenalesTest.eliminar_latencia_action.execute(
            senoide, senoide_a_truncar, 0.100).get_valores()

        self.assertListEqual(senoide.get_valores(), senal_resultante)

    def test_que_lance_excepcion_si_la_ventana_es_mas_larga_que_alguna_senal(self):
        fs = 48000
        frecuencia = 200
        senoide = GeneradorSenoidal().generar_senoide(fs, 2, frecuencia, 1, 0)
        senoide_a_truncar = GeneradorSenoidal().generar_senoide(fs, 2, frecuencia, 1, 0)

        self.assertRaises(AlineacionException, AlinearSenalesTest.eliminar_latencia_action.
                          execute, senoide, senoide_a_truncar, 5)
