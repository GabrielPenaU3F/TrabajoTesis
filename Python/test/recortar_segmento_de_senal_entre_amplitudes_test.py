import unittest

from src.action.recortar_segmento_de_senal_entre_amplitudes_action import RecortarSegmentoDeSenalEntreAmplitudesAction
from src.domain.senal_en_tiempo import SenalEnTiempo


class RecortarSegmentoDeSenalEntreAmplitudesTest(unittest.TestCase):

    action = None

    @classmethod
    def setUpClass(cls):
        cls.action = RecortarSegmentoDeSenalEntreAmplitudesAction()

    def test_que_recorte_correctamente_una_escalera_entre_2_y_5(self):
        dominio = [0, 1, 2, 3, 4, 5, 6, 7]
        valores = [0, 1, 2, 3, 4, 5, 6, 7]
        senal_en_tiempo = SenalEnTiempo(dominio, valores)

        self.assertListEqual([2, 3, 4, 5], RecortarSegmentoDeSenalEntreAmplitudesTest.action.execute(senal_en_tiempo, 2, 5).get_dominio_temporal())
        self.assertListEqual([2, 3, 4, 5], RecortarSegmentoDeSenalEntreAmplitudesTest.action.execute(senal_en_tiempo, 2, 5).get_valores())

    def test_que_recorte_correctamente_una_escalera_entre_menos3_y_menos8(self):
        dominio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valores = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        senal_en_tiempo = SenalEnTiempo(dominio, valores)

        self.assertListEqual([3, 4, 5, 6, 7, 8], RecortarSegmentoDeSenalEntreAmplitudesTest.action.execute(senal_en_tiempo, -8, -3).get_dominio_temporal())
        self.assertListEqual([-3, -4, -5, -6, -7, -8], RecortarSegmentoDeSenalEntreAmplitudesTest.action.execute(senal_en_tiempo, -8, -3).get_valores())

