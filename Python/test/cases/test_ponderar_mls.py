import math
import unittest

from src.core.provider.action_provider import ActionProvider
from src.core.domain.generadores_de_senales.generador_mls import GeneradorMLS
from src.core.domain.senal_audio import SenalAudio


class PonderarMLSTest(unittest.TestCase):

    ponderar_periodos_mls_action = None

    @classmethod
    def setUpClass(cls):
        cls.ponderar_periodos_mls_action = ActionProvider.provide_ponderar_periodos_mls_action()

    def test_que_la_longitud_de_la_senal_ponderada_con_los_periodos_intactos_sea_correcta(self):
        fs = 48000
        n_bits = 17
        periodos = 8
        senal_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs)
        longitud_esperada = math.pow(2, 17) - 1
        valores_ponderados = PonderarMLSTest.ponderar_periodos_mls_action.execute(senal_mls, n_bits)

        self.assertEqual(longitud_esperada, len(valores_ponderados))

    def test_que_la_longitud_de_la_senal_ponderada_con_algunas_muestras_menos_sea_correcta(self):
        fs = 48000
        n_bits = 17
        periodos = 8
        valores_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs).get_valores().copy()
        for i in range(1000):
            valores_mls.pop()
        senal_mls_truncada = SenalAudio(fs, valores_mls)
        longitud_esperada = math.pow(2, 17) - 1
        valores_ponderados = PonderarMLSTest.ponderar_periodos_mls_action.execute(senal_mls_truncada, n_bits)

        self.assertEqual(longitud_esperada, len(valores_ponderados))

