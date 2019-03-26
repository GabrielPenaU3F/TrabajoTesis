import unittest
import numpy
from src.core.domain.senal_audio import SenalAudio
from src.core.provider.action_provider import ActionProvider


class DiferenciarSenalTest(unittest.TestCase):

    diferenciar_action = None

    @classmethod
    def setUpClass(cls):
        cls.diferenciar_action = ActionProvider.provide_diferenciar_senal_action()


    def test_que_diferencie_correctamente_un_vector_escalera(self):
        fs = 5
        dominio_temporal = numpy.linspace(0, 1, 5, endpoint=False)
        escalera = numpy.linspace(0, 1, 5, endpoint=False)
        esperado = [1/fs, 1/fs, 1/fs, 1/fs, -4/fs]

        numpy.testing.assert_almost_equal(DiferenciarSenalTest.diferenciar_action.execute(
            SenalAudio(fs, dominio_temporal, escalera)).get_valores(), esperado, decimal=10)


