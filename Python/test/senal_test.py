import unittest

import math
import numpy

from src.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal
from src.domain.senal_audio import SenalAudio
from src.exception.exceptions import *


class SenalAudioTest(unittest.TestCase):

    def test_que_la_longitud_de_una_senal_nula_sea_correcta(self):
        fs = 5
        valores = numpy.zeros(10)
        senal = SenalAudio(fs, valores)

        self.assertEqual(10, senal.get_longitud())

    def test_que_la_duracion_de_una_senal_nula_sea_correcta(self):
        fs = 5
        valores = numpy.zeros(10)
        senal = SenalAudio(fs, valores)

        self.assertEqual(2, senal.get_duracion())

    def test_que_el_dominio_temporal_de_una_senal_nula_sea_correcto(self):
        fs = 5
        valores = numpy.zeros(10)
        senal = SenalAudio(fs, valores)
        dominio_temporal = [0, 1/5, 2/5, 3/5, 4/5, 1, 6/5, 7/5, 8/5, 9/5]

        self.assertListEqual(dominio_temporal, senal.get_dominio_temporal())

    def test_que_los_valores_de_una_senal_nula_sean_correctos(self):
        fs = 5
        valores = list(numpy.zeros(10))
        senal = SenalAudio(fs, valores)

        self.assertListEqual(valores, senal.get_valores())

    def test_que_los_valores_de_una_senal_senoidal_sean_correctos(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertListEqual(valores, senal.get_valores())

    def test_que_una_senal_senoidal_en_0_valga_0(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertEqual(0, senal.get_valor_en(0))

    def test_que_el_retenedor_de_orden_cero_producza_que_una_senoidal_en_cero_coma_cinco_valga_seno_de_cero_coma_cuatro(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertEqual(math.sin(0.4), senal.get_valor_en(0.5))

    def test_que_una_senal_nula_se_cree_correctamente_con_dominio_y_valores(self):
        fs = 5
        dominio = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8]
        valores = list(numpy.zeros(10))
        senal = SenalAudio(fs, dominio, valores)

        self.assertListEqual(dominio, senal.get_dominio_temporal())
        self.assertListEqual(valores, senal.get_valores())

    def test_que_lance_exception_si_creo_senal_con_4_parametros(self):
        a = 1
        b = 2
        c = 3
        d = 4

        self.assertRaises(CantidadDeParametrosException, SenalAudio, a, b, c, d)

    def test_que_lance_excepcion_si_creo_senal_con_dominio_y_valores_de_diferente_largo(self):
        fs = 5
        dominio = [1, 2, 3]
        valores = [2, 3, 4, 5, 6]

        self.assertRaises(ValidacionParametrosSenalException, SenalAudio, fs, dominio, valores)

    def test_que_lance_excepcion_si_creo_senal_con_dominio_desordenado(self):
        fs = 5
        dominio = [0, 0.4, 0.2, 0.1, 10, 1, 1.2, 1.4, 1.6, 1.8]
        valores = numpy.zeros(10)

        self.assertRaises(ValidacionParametrosSenalException, SenalAudio, fs, dominio, valores)

    def test_que_lance_excepcion_si_creo_senal_con_frecuencia_de_muestreo_y_dominio_temporal_incongruentes(self):
        fs = 5
        dominio = [0, 0.2, 0.4, 0.6, 0.9, 1, 1.2, 1.4, 1.6, 1.8]
        valores = numpy.zeros(10)

        self.assertRaises(ValidacionParametrosSenalException, SenalAudio, fs, dominio, valores)

