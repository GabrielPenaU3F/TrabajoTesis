import math
import unittest

import numpy
from matplotlib import pyplot
from scipy import signal

from src.core.domain.generadores_de_senales.generador_ruido import GeneradorRuido
from src.core.domain.senal_audio import SenalAudio
from src.core.provider.action_provider import ActionProvider


class FiltroPasabandaTest(unittest.TestCase):

    aplicar_filtro_pasabanda_action = None

    @classmethod
    def setUpClass(cls):
        cls.aplicar_filtro_pasabanda_action = ActionProvider.provide_aplicar_filtro_pasabanda_action()


    def test_que_una_suma_de_senoides_al_ser_filtradas_resulte_en_una_unica_senoide(self):
        fs = 48000
        t = numpy.linspace(0, 3, 3*fs, endpoint=False)
        valores = numpy.sin(2*numpy.pi*100*t) + numpy.sin(2*numpy.pi*1000*t)
        senal = SenalAudio(fs, t, valores)
        maximo_original = max(senal.get_modulos_frecuencia())
        senal_filtrada = FiltroPasabandaTest.aplicar_filtro_pasabanda_action.execute(senal, 50, 150)

        numpy.testing.assert_allclose(senal_filtrada.get_modulo_frecuencia_en(100), maximo_original, rtol=math.pow(10, -2))
        numpy.testing.assert_allclose(senal_filtrada.get_modulo_frecuencia_en(1000), 0, atol=maximo_original*math.pow(10, -3))

    def test_que_una_senal_de_ruido_blanco_se_filtre_correctamente_entre_100_y_1000_hertz(self):
        ruido_blanco = GeneradorRuido().generar_ruido_blanco(48000, 3, 0, 1)
        ruido_filtrado = FiltroPasabandaTest.aplicar_filtro_pasabanda_action.execute(ruido_blanco, 100, 1000)
        espectro_ruido = ruido_blanco.get_modulos_frecuencia()
        espectro_filtrado = ruido_filtrado.get_modulos_frecuencia()

        ''' Plotear los espectros
        f = ruido_filtrado.get_dominio_frecuencial()
        pyplot.plot(f, espectro_ruido, f, espectro_filtrado)
        pyplot.show()
        '''

        maximo = max(ruido_blanco.get_modulos_frecuencia())

        nulos_incorrectos = 0
        for f in range(100, 1000):
            muestra_en_f = int(ruido_blanco.get_longitud()*f/ruido_blanco.get_fs())
            if abs(espectro_filtrado[muestra_en_f] - espectro_ruido[muestra_en_f]) \
                    > 0.8*maximo:
                nulos_incorrectos += 1
        nonulos_incorrectos = 0
        for f in range(0, 100):
            muestra_en_f = int(ruido_blanco.get_longitud() * f / ruido_blanco.get_fs())
            if abs(espectro_filtrado[muestra_en_f]) > math.pow(10, -1)*maximo:
                nonulos_incorrectos += 1

        for f in range(1001, 24000):
            muestra_en_f = int(ruido_blanco.get_longitud()*f/ruido_blanco.get_fs())
            if abs(espectro_filtrado[muestra_en_f]) > math.pow(10, -1)*maximo:
                nonulos_incorrectos += 1

        self.assertEqual(0, nulos_incorrectos)
        self.assertEqual(0, nonulos_incorrectos)
