import math
import unittest

from matplotlib import pyplot

from src.core.domain.generadores_de_senales.generador_ruido import GeneradorRuido
from src.core.provider.action_provider import ActionProvider


class FiltrosOctavaYTercioOctavaTest(unittest.TestCase):

        aplicar_filtro_octava_action = None
        aplicar_filtro_tercio_de_octava_action = None

        @classmethod
        def setUpClass(cls):
            cls.aplicar_filtro_octava_action = ActionProvider.provide_aplicar_filtro_octava_action()
            cls.aplicar_filtro_tercio_de_octava_action = ActionProvider.provide_aplicar_filtro_tercio_de_octava_action()

        def test_que_el_filtro_de_octava_centrada_en_63_hertz_funcione_correctamente(self):
            fs = 48000
            ruido_blanco = GeneradorRuido().generar_ruido_blanco(fs, 6, 0, 1)
            espectro_ruido = ruido_blanco.get_modulos_frecuencia()
            ruido_filtrado = self.aplicar_filtro_octava_action.execute(ruido_blanco, 63)
            espectro_filtrado = ruido_filtrado.get_modulos_frecuencia()

            frecuencia_inicial = 44.19
            frecuencia_final = 88.39

            maximo = max(ruido_blanco.get_modulos_frecuencia())

            nulos_incorrectos = 0
            muestra_en_f_inicial = int(ruido_blanco.get_longitud() * frecuencia_inicial / ruido_blanco.get_fs())
            muestra_en_f_final = int(ruido_blanco.get_longitud() * frecuencia_final / ruido_blanco.get_fs())
            for f in range(muestra_en_f_inicial, muestra_en_f_final):
                if abs(espectro_filtrado[f] - espectro_ruido[f]) \
                        > 0.8 * maximo:
                    nulos_incorrectos += 1

            nonulos_incorrectos = 0
            for f in range(0, muestra_en_f_inicial):

                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            muestra_nyquist = int((ruido_blanco.get_longitud() * ruido_blanco.get_fs()/2) / ruido_blanco.get_fs())
            # El +6 es porque el ripple del filtro hace que el test falle en las muestras inmediatas siguientes
            # al final de la banda
            for f in range(muestra_en_f_final + 6, muestra_nyquist):
                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            '''
            f = ruido_filtrado.get_dominio_frecuencial()
            pyplot.plot(f, espectro_filtrado)
            pyplot.show()
            '''

            self.assertEqual(0, nulos_incorrectos)
            self.assertEqual(0, nonulos_incorrectos)

        def test_que_el_filtro_de_tercio_de_octava_centrado_en_63_hertz_funcione_correctamente(self):
            fs = 48000
            ruido_blanco = GeneradorRuido().generar_ruido_blanco(fs, 6, 0, 1)
            espectro_ruido = ruido_blanco.get_modulos_frecuencia()
            ruido_filtrado = self.aplicar_filtro_tercio_de_octava_action.execute(ruido_blanco, 63)
            espectro_filtrado = ruido_filtrado.get_modulos_frecuencia()

            frecuencia_inicial = 56.57
            frecuencia_final = 71.27

            maximo = max(ruido_blanco.get_modulos_frecuencia())

            nulos_incorrectos = 0
            muestra_en_f_inicial = int(ruido_blanco.get_longitud() * frecuencia_inicial / ruido_blanco.get_fs())
            muestra_en_f_final = int(ruido_blanco.get_longitud() * frecuencia_final / ruido_blanco.get_fs())
            for f in range(muestra_en_f_inicial, muestra_en_f_final):
                if abs(espectro_filtrado[f] - espectro_ruido[f]) \
                        > 0.8 * maximo:
                    nulos_incorrectos += 1

            nonulos_incorrectos = 0
            # El -4 es porque el ripple del filtro hace que el test falle en las muestras inmediatas anteriores
            # al final de la banda
            for f in range(0, muestra_en_f_inicial - 4):
                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            muestra_nyquist = int((ruido_blanco.get_longitud() * ruido_blanco.get_fs()/2) / ruido_blanco.get_fs())
            # El +6 es porque el ripple del filtro hace que el test falle en las muestras inmediatas siguientes
            # al final de la banda
            for f in range(muestra_en_f_final + 6, muestra_nyquist):
                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            '''
            f = ruido_filtrado.get_dominio_frecuencial()
            pyplot.plot(f, espectro_filtrado)
            pyplot.show()
            '''

            self.assertEqual(0, nulos_incorrectos)
            self.assertEqual(0, nonulos_incorrectos)


