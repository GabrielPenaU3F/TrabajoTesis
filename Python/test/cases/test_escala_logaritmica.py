import unittest
import numpy
from core.domain.senal_audio import SenalAudio
from core.provider.action_provider import ActionProvider


class EscalaLogaritmicaTest(unittest.TestCase):

    transformar_action = None

    @classmethod
    def setUpClass(cls):
        cls.transformar_action = ActionProvider.provide_transformar_a_escala_logaritmica_normalizada_action()

    def test_que_la_escala_de_decibeles_se_genere_correctamente_para_una_senal_de_prueba_simple(self):
        fs = 5
        dominio_temporal = numpy.linspace(0, 1, fs, endpoint=False)
        valores = [10000, 1000, 100, 10, 1]
        #En decibeles, deberia decrecer linealmente de a 20
        senal = SenalAudio(fs, dominio_temporal, valores)

        senal_db = EscalaLogaritmicaTest.transformar_action.execute(senal).get_valores()
        decrecimiento_de_a_20 = True
        for i in range(len(senal_db) - 1):
            if senal_db[i+1] - senal_db[i] != -20:
                decrecimiento_de_a_20 = False

        self.assertEqual(True, decrecimiento_de_a_20)
