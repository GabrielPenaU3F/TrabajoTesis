import unittest

import math
from src.domain.senal_audio import SenalAudio
from src.exception.exceptions import *

# Usar NUMPY para mejorar los test


class SenalAudioTest(unittest.TestCase):

    def test_que_la_longitud_de_una_senal_nula_sea_correcta(self):
        fs = 5
        valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        senal = SenalAudio(fs, valores)

        self.assertEqual(10, senal.get_longitud())

    def test_que_la_duracion_de_una_senal_nula_sea_correcta(self):
        fs = 5
        valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        senal = SenalAudio(fs, valores)

        self.assertEqual(2, senal.get_duracion())

    def test_que_el_dominio_temporal_de_una_senal_nula_sea_correcto(self):
        fs = 5
        valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        senal = SenalAudio(fs, valores)
        dominio_temporal = [0, 1/5, 2/5, 3/5, 4/5, 1, 6/5, 7/5, 8/5, 9/5]

        self.assertListEqual(dominio_temporal, senal.get_dominio_temporal())

    def test_que_los_valores_de_una_senal_nula_sean_correctos(self):
        fs = 5
        valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        senal = SenalAudio(fs, valores)

        self.assertListEqual(valores, senal.get_valores())

    def test_que_los_valores_de_una_senal_senoidal_sean_correctos(self):
        fs = 5
        valores = self.generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertListEqual(valores, senal.get_valores())

    def test_que_una_senal_senoidal_en_0_valga_0(self):
        fs = 5
        valores = self.generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertEqual(0, senal.get_valor_en(0))

    def test_que_el_retenedor_de_orden_cero_producza_que_una_senoidal_en_cero_coma_cinco_valga_seno_de_cero_coma_cuatro(self):
        fs = 5
        valores = self.generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertEqual(math.sin(0.4), senal.get_valor_en(0.5))

    def test_que_al_recortar_senal_senoidal_el_dominio_temporal_sea_correcto(self):
        fs = 5
        valores = self.generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)
        senal_entre_1_y_2 = senal.recortar_segmento(1, 2)
        dominio_temporal_esperado = [1, 6/5, 7/5, 8/5, 9/5]

        self.assertListEqual(dominio_temporal_esperado, senal_entre_1_y_2.get_dominio_temporal())

    def test_que_al_recortar_senal_senoidal_los_valores_sean_correctos(self):
        fs = 5
        valores = self.generar_valores_senal_senoidal(10, fs)
        senal = SenalAudio(fs, valores)
        senal_entre_1_y_2 = senal.recortar_segmento(1, 2)
        valores_esperados = [math.sin(1), math.sin(6 / 5), math.sin(7 / 5), math.sin(8 / 5), math.sin(9 / 5)]

        self.assertListEqual(valores_esperados, senal_entre_1_y_2.get_valores())

    def test_que_una_senal_nula_se_cree_correctamente_con_dominio_y_valores(self):
        fs = 5
        dominio = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8]
        valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    def generar_valores_senal_senoidal(self, longitud, fs):
        dominio_temporal = []
        for t in range(longitud):
            dominio_temporal.append(t/fs)
        valores = []
        for t in dominio_temporal:
            valores.append(math.sin(t))
        return valores
