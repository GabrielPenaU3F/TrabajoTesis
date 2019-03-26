import math
import unittest
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


            # Los +8 y -6 spm porque el ripple del filtro hace que el test falle en las muestras inmediatas anteriores
            # y siguientes al final de la banda
            nonulos_incorrectos = 0
            for f in range(0, muestra_en_f_inicial - 6):

                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            muestra_nyquist = int((ruido_blanco.get_longitud() * ruido_blanco.get_fs()/2) / ruido_blanco.get_fs())
            for f in range(muestra_en_f_final + 8, muestra_nyquist):
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
            # El -6 es porque el ripple del filtro hace que el test falle en las muestras inmediatas anteriores
            # al final de la banda
            for f in range(0, muestra_en_f_inicial - 6):
                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            muestra_nyquist = int((ruido_blanco.get_longitud() * ruido_blanco.get_fs()/2) / ruido_blanco.get_fs())
            # El +8 es porque el ripple del filtro hace que el test falle en las muestras inmediatas siguientes
            # al final de la banda
            for f in range(muestra_en_f_final + 8, muestra_nyquist):
                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            '''
            f = ruido_filtrado.get_dominio_frecuencial()
            pyplot.plot(f, espectro_filtrado)
            pyplot.show()
            '''

            self.assertEqual(0, nulos_incorrectos)
            self.assertEqual(0, nonulos_incorrectos)

        def test_que_un_filtro_de_octava_en_frecuencia_1000_no_arroje_nan(self):
            fs = 48000
            ruido_blanco = GeneradorRuido().generar_ruido_blanco(fs, 6, 0, 1)
            ruido_filtrado = self.aplicar_filtro_octava_action.execute(ruido_blanco, 1000)
            valores_ruido = ruido_filtrado.get_valores()

            nans = 0
            for valor in valores_ruido:
                if math.isnan(valor):
                    nans += 1

            self.assertEqual(0, nans)

        def test_que_un_filtro_de_octava_en_alta_frecuencia_no_arroje_nan(self):
            fs = 48000
            ruido_blanco = GeneradorRuido().generar_ruido_blanco(fs, 6, 0, 1)
            ruido_filtrado = self.aplicar_filtro_octava_action.execute(ruido_blanco, 16000)
            valores_ruido = ruido_filtrado.get_valores()

            nans = 0
            for valor in valores_ruido:
                if math.isnan(valor):
                    nans += 1

            self.assertEqual(0, nans)

        def test_que_un_filtro_de_tercio_de_octava_en_baja_frecuencia_no_arroje_nans(self):
            fs = 48000
            ruido_blanco = GeneradorRuido().generar_ruido_blanco(fs, 6, 0, 1)
            ruido_filtrado = self.aplicar_filtro_tercio_de_octava_action.execute(ruido_blanco, 20)
            valores_ruido = ruido_filtrado.get_valores()

            nans = 0
            for valor in valores_ruido:
                if math.isnan(valor):
                    nans += 1

            self.assertEqual(0, nans)

        def test_que_el_filtro_de_octava_centrado_en_8_kHz_funcione_correctamente(self):
            fs = 48000
            ruido_blanco = GeneradorRuido().generar_ruido_blanco(fs, 6, 0, 1)
            espectro_ruido = ruido_blanco.get_modulos_frecuencia()
            ruido_filtrado = self.aplicar_filtro_octava_action.execute(ruido_blanco, 8000)
            espectro_filtrado = ruido_filtrado.get_modulos_frecuencia()

            frecuencia_inicial = 5657
            frecuencia_final = 11314

            maximo = max(ruido_blanco.get_modulos_frecuencia())

            nulos_incorrectos = 0
            muestra_en_f_inicial = int(ruido_blanco.get_longitud() * frecuencia_inicial / ruido_blanco.get_fs())
            muestra_en_f_final = int(ruido_blanco.get_longitud() * frecuencia_final / ruido_blanco.get_fs())
            for f in range(muestra_en_f_inicial, muestra_en_f_final):
                if abs(espectro_filtrado[f] - espectro_ruido[f]) \
                        > 0.8 * maximo:
                    nulos_incorrectos += 1

            # Los +170 y -170 son porque el ripple del filtro hace que el test falle en las muestras
            # inmediatas anteriores y siguientes al final de la banda. Obviamente, la región de ripple debe
            # ser mucho más grande cuando la frecuencia es mayor, ya que la restricción del filtro se suaviza.
            nonulos_incorrectos = 0
            for f in range(0, muestra_en_f_inicial - 170):

                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            muestra_nyquist = int((ruido_blanco.get_longitud() * ruido_blanco.get_fs() / 2) / ruido_blanco.get_fs())
            for f in range(muestra_en_f_final + 170, muestra_nyquist):
                if abs(espectro_filtrado[f]) > math.pow(10, -1) * maximo:
                    nonulos_incorrectos += 1

            '''
            f = ruido_filtrado.get_dominio_frecuencial()
            pyplot.plot(f, espectro_filtrado)
            pyplot.show()
            '''

            self.assertEqual(0, nulos_incorrectos)
            self.assertEqual(0, nonulos_incorrectos)

