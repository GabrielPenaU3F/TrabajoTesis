import math
import unittest

from src.action.recortar_segmento_de_senal_entre_amplitudes_action import RecortarSegmentoDeSenalEntreAmplitudesAction
from src.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal
from src.domain.senal_audio import SenalAudio
from src.domain.senal_en_tiempo import SenalEnTiempo
from src.provider.action_provider import ActionProvider


class RecortarSegmentoDeSenalEntreAmplitudesTest(unittest.TestCase):

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
        senal_entre_1_y_2 = RecortarSegmentoDeSenalEntreAmplitudesTest.recortar_en_tiempo_action.execute(senal, 1, 2)
        dominio_temporal_esperado = [1, 6/5, 7/5, 8/5, 9/5]

        self.assertListEqual(dominio_temporal_esperado, senal_entre_1_y_2.get_dominio_temporal())

    def test_que_al_recortar_senal_senoidal_los_valores_sean_correctos(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senoide(10, fs)
        senal = SenalAudio(fs, valores)
        senal_entre_1_y_2 = RecortarSegmentoDeSenalEntreAmplitudesTest.recortar_en_tiempo_action.execute(senal, 1, 2)
        valores_esperados = [math.sin(1), math.sin(6 / 5), math.sin(7 / 5), math.sin(8 / 5), math.sin(9 / 5)]

        self.assertListEqual(valores_esperados, senal_entre_1_y_2.get_valores())

    def test_que_recorte_correctamente_una_escalera_entre_2_y_5(self):
        dominio = [0, 1, 2, 3, 4, 5, 6, 7]
        valores = [0, 1, 2, 3, 4, 5, 6, 7]
        senal_en_tiempo = SenalEnTiempo(dominio, valores)

        self.assertListEqual([2, 3, 4, 5], RecortarSegmentoDeSenalEntreAmplitudesTest.recortar_en_amplitud_action.execute(senal_en_tiempo, 2, 5).get_dominio_temporal())
        self.assertListEqual([2, 3, 4, 5], RecortarSegmentoDeSenalEntreAmplitudesTest.recortar_en_amplitud_action.execute(senal_en_tiempo, 2, 5).get_valores())

    def test_que_recorte_correctamente_una_escalera_entre_menos3_y_menos8(self):
        dominio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valores = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        senal_en_tiempo = SenalEnTiempo(dominio, valores)

        self.assertListEqual([3, 4, 5, 6, 7, 8], RecortarSegmentoDeSenalEntreAmplitudesTest.recortar_en_amplitud_action.execute(senal_en_tiempo, -8, -3).get_dominio_temporal())
        self.assertListEqual([-3, -4, -5, -6, -7, -8], RecortarSegmentoDeSenalEntreAmplitudesTest.recortar_en_amplitud_action.execute(senal_en_tiempo, -8, -3).get_valores())

