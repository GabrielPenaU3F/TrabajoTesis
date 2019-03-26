import math
import unittest
import numpy
from src.core.domain.senal_audio import SenalAudio
from src.core.provider.action_provider import ActionProvider


class IntegrarSenalTest(unittest.TestCase):

    integrar_senal_action = None

    @classmethod
    def setUpClass(cls):
        cls.integrar_senal_action = ActionProvider.provide_integrar_senal_action()

    def test_que_la_integral_de_un_triangulo_de_base_2_y_altura_1_sea_1(self):
        fs = 5000
        x = numpy.linspace(0, 2, 10000, endpoint=False)
        y = numpy.linspace(0, 1, 10000, endpoint=False)
        senal = SenalAudio(fs, x, y)
        area = IntegrarSenalTest.integrar_senal_action.execute(senal, 0, senal.get_duracion())

        self.assertAlmostEqual(1, area, delta=math.pow(10, -3))

    def test_que_la_integral_de_una_funcion_constante_1_entre_2_y_4_sea_2(self):
        fs = 10000
        x = numpy.linspace(0, 5, 50000, endpoint=False)
        y = [1 for i in range(len(x))]
        senal = SenalAudio(fs, x, y)
        area = IntegrarSenalTest.integrar_senal_action.execute(senal, 2, 4)

        self.assertAlmostEqual(2, area, delta=math.pow(10, -4))

