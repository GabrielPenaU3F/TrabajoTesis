import math
import unittest
from core.domain.generadores_de_senales.generador_ess import GeneradorESS
from core.provider.action_provider import ActionProvider


class ESSTest(unittest.TestCase):

    realizar_convolucion_action = None

    @classmethod
    def setUpClass(cls):
        cls.realizar_convolucion_action = ActionProvider.provide_realizar_convolucion_action()

    def test_que_el_filtro_inverso_ess_produzca_una_delta_al_aplicarse_a_dicha_senal(self):
        fs = 48000
        duracion = 3
        f1 = 20
        f2 = 22050
        senal_ess = GeneradorESS().generar_senal_ess(fs, duracion, f1, f2)
        filtro_inverso = GeneradorESS().generar_filtro_inverso_ess(fs, duracion, f1, f2)

        delta = ESSTest.realizar_convolucion_action.execute(senal_ess, filtro_inverso).get_valores()
        max_delta = max(delta)
        maximos = 0
        nulos = 0
        for i in range(len(delta)):
            if delta[i] == max_delta:
                maximos += 1
            elif abs(max_delta - delta[i]) < math.pow(10, 5):
                nulos += 1

        self.assertEqual(1, maximos)
        self.assertEqual(round(len(delta)/2) - 1, delta.index(max_delta))
        self.assertEqual(len(delta) - 1, nulos)


