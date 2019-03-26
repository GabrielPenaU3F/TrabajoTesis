import unittest
import math
import numpy
from src.core.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal
from src.core.domain.senal_audio import SenalAudio
from src.exception.excepciones import *


class TestSenalAudio(unittest.TestCase):

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
        valores = GeneradorSenoidal().generar_valores_senoide(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertListEqual(valores, senal.get_valores())

    def test_que_una_senal_senoidal_en_0_valga_0(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senoide(10, fs)
        senal = SenalAudio(fs, valores)

        self.assertEqual(0, senal.get_valor_en(0))

    def test_que_el_retenedor_de_orden_cero_producza_que_una_senoidal_en_cero_coma_cinco_valga_seno_de_cero_coma_cuatro(self):
        fs = 5
        valores = GeneradorSenoidal().generar_valores_senoide(10, fs)
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

    def test_que_el_dominio_frecuencial_vaya_de_0_hasta_la_frecuencia_de_muestreo(self):
        fs = 48000
        duracion = 10
        senoide_220Hz = GeneradorSenoidal().generar_senoide(fs, duracion, 220, 1, 0)
        espaciado_en_frecuencia = 1/duracion
        dominio_frecuencial_esperado = list(numpy.arange(0, fs, espaciado_en_frecuencia))

        self.assertListEqual(dominio_frecuencial_esperado, senoide_220Hz.get_dominio_frecuencial())

    def test_que_la_senoide_pura_tenga_unicamente_su_frecuencia_fundamental(self):
        '''
        La idea de este test es mostrar que una senoide pura, en el dominio de la frecuencia,
        contiene únicamente energía en su frecuencia fundamental, mientras que las otras son nulas (esto
        en el caso ideal. En la versión digital real, hay siempre un ruido subyacente, de manera que aquí
        "nulo" significa que el contenido real lo supera en un cierto delta. En este caso, se eligió
        delta = 10^-7, el menor orden de magnitud posible tal que el ruido no es detectado.
        '''
        fs = 48000
        duracion = 10
        frecuencia_fundamental = 220
        senoide_220Hz = GeneradorSenoidal().generar_senoide(fs, duracion, frecuencia_fundamental, 1, 0)
        modulos_frecuencia = senoide_220Hz.get_modulos_frecuencia()
        maximo = max(modulos_frecuencia)
        delta = math.pow(10, -7)
        valores_no_nulos = 0
        for i in range(len(modulos_frecuencia)):
            if modulos_frecuencia[i]/maximo > delta: valores_no_nulos += 1

        # Son dos, que representan la frecuencia fundamental f0 y su réplica fs - f0
        self.assertEqual(2, valores_no_nulos)
        self.assertEqual(True, senoide_220Hz.get_dominio_frecuencial()[frecuencia_fundamental]/maximo > delta)
        self.assertEqual(True, senoide_220Hz.get_dominio_frecuencial()[fs - frecuencia_fundamental]/maximo > delta)

    def test_que_la_energia_de_una_senal_nula_sea_nula(self):
        fs = 48000
        valores = numpy.zeros(48000)
        senal = SenalAudio(fs, valores)

        self.assertEqual(0, senal.get_energia_total())

    def test_que_la_energia_de_una_senoide_con_frecuencia_angular_unitaria_y_un_unico_periodo_sea_pi(self):
        fs = 48000
        frecuencia = 1/(2*math.pi)
        senoide = GeneradorSenoidal().generar_senoide(fs, 2*math.pi, frecuencia, 1, 0)

        self.assertAlmostEqual(math.pi, senoide.get_energia_total(), int(math.pow(10, -7)))

    '''
    def test_que_el_indice_en_t_cero_sea_cero(self):
        fs = 48000
        dominio_temporal = numpy.linspace(0, 1, 48000, endpoint=False)
        y = [1 for i in range(len(dominio_temporal))]
        senal = SenalAudio(fs, dominio_temporal, y)

        self.assertEqual(0, senal.get_indice_en_t(0))

    def test_que_el_indice_en_t_uno_menos_Ts_sea_fs_menos_Ts(self):
        fs = 10
        dominio_temporal = numpy.linspace(0, 1, fs, endpoint=False)
        y = [1 for i in range(len(dominio_temporal))]
        senal = SenalAudio(fs, dominio_temporal, y)

        self.assertEqual(fs, senal.get_indice_en_t(1 - 1/fs))

    def test_que_el_indice_en_t_cero_coma_55_sea_5(self):
        fs = 10
        dominio_temporal = numpy.linspace(0, 1, fs, endpoint=False)
        y = [1 for i in range(len(dominio_temporal))]
        senal = SenalAudio(fs, dominio_temporal, y)

        self.assertEqual(5, senal.get_indice_en_t(0.55))

    def test_que_no_pueda_obtener_el_indice_de_una_senal_en_donde_no_esta_definida(self):
        fs = 48000
        dominio_temporal = numpy.linspace(0, 1, 48000, endpoint=False)
        y = [1 for i in range(len(dominio_temporal))]
        senal = SenalAudio(fs, dominio_temporal, y)

        self.assertRaises(IndiceSenalException, senal.get_indice_en_t, 3)
        
    '''


