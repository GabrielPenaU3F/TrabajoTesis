import math
import unittest
from time import process_time
import numpy
from src.core.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal
from src.core.domain.senal_audio import SenalAudio
from src.core.provider.action_provider import ActionProvider


class TestRecortarSegmentoDeSenal(unittest.TestCase):

    recortar_en_amplitud_action = None
    recortar_en_tiempo_action = None

    @classmethod
    def setUpClass(cls):
        cls.recortar_en_tiempo_action = ActionProvider.provide_recortar_segmento_de_senal_en_tiempo_action()
        cls.recortar_en_amplitud_action = ActionProvider.provide_recortar_segmento_de_senal_entre_amplitudes_action()

    def test_que_al_recortar_senal_senoidal_el_dominio_temporal_sea_correcto(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senoide(10, fs)
        senal = SenalAudio(fs, valores)
        senal_entre_1_y_2 = TestRecortarSegmentoDeSenal.recortar_en_tiempo_action.execute(senal, 1, 2)
        dominio_temporal_esperado = [1, 6/5, 7/5, 8/5, 9/5]

        self.assertListEqual(dominio_temporal_esperado, senal_entre_1_y_2.get_dominio_temporal())

    def test_que_al_recortar_senal_senoidal_los_valores_sean_correctos(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senoide(10, fs)
        senal = SenalAudio(fs, valores)
        senal_entre_1_y_2 = TestRecortarSegmentoDeSenal.recortar_en_tiempo_action.execute(senal, 1, 2)
        valores_esperados = [math.sin(1), math.sin(6 / 5), math.sin(7 / 5), math.sin(8 / 5), math.sin(9 / 5)]

        self.assertListEqual(valores_esperados, senal_entre_1_y_2.get_valores())

    def test_que_recorte_correctamente_una_escalera_entre_amplitudes_2_y_5(self):
        fs = 8
        dominio = numpy.linspace(0, 1, 8, endpoint=False)
        valores = [0, 1, 2, 3, 4, 5, 6, 7]
        senal = SenalAudio(fs, dominio, valores)

        self.assertListEqual([2, 3, 4, 5],
                             TestRecortarSegmentoDeSenal.recortar_en_amplitud_action.execute(senal, 2, 5).get_valores())

    def test_que_recorte_correctamente_una_escalera_entre_menos3_y_menos8(self):
        fs = 11
        dominio = numpy.linspace(0, 1, 11, endpoint=None)
        valores = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        senal = SenalAudio(fs, dominio, valores)

        numpy.testing.assert_almost_equal([3/11, 4/11, 5/11, 6/11, 7/11, 8/11],
                                          TestRecortarSegmentoDeSenal.recortar_en_amplitud_action.execute(
                                              senal, -8, -3).get_dominio_temporal(), decimal=10)
        self.assertListEqual([-3, -4, -5, -6, -7, -8],
                             TestRecortarSegmentoDeSenal.recortar_en_amplitud_action.execute(
                                 senal, -8, -3).get_valores())

    def test_que_recorte_en_amplitud_una_senal_larga_en_un_tiempo_adecuado(self):
        fs = 48000
        dominio = numpy.linspace(0, 6, fs*6, endpoint=False)
        valores = numpy.linspace(0, 1000000, fs*6, endpoint=False)
        senal_larga = SenalAudio(fs, dominio, valores)

        t_inicio = process_time()
        TestRecortarSegmentoDeSenal.recortar_en_amplitud_action.execute(senal_larga, 60000, 80000)
        t_fin = process_time()

        t_procesamiento = t_fin - t_inicio
        self.assertEqual(True, t_procesamiento < 1)

    def test_que_recorte_correctamente_entre_3_y_5_una_senal_que_sube_y_luego_baja(self):
        fs = 11
        dominio = numpy.linspace(0, 1, 11, endpoint=None)
        valores = [0, 1, 2, 3, 4, 4, 4, 5, 6, 4, 4]
        senal = SenalAudio(fs, dominio, valores)

        numpy.testing.assert_almost_equal([3/11, 4/11, 5/11, 6/11, 7/11],
                                          TestRecortarSegmentoDeSenal.recortar_en_amplitud_action.execute(
                                              senal, 3, 5).get_dominio_temporal(), decimal=10)
        self.assertListEqual([3, 4, 4, 4, 5],
                             TestRecortarSegmentoDeSenal.recortar_en_amplitud_action.execute(
                                 senal, 3, 5).get_valores())
