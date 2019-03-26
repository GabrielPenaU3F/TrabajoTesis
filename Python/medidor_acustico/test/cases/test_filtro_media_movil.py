import unittest
import numpy
from src.core.domain.senal_audio import SenalAudio
from src.core.provider.action_provider import ActionProvider
from src.exception.excepciones import FiltroException


class FiltroMediaMovilTest(unittest.TestCase):

    aplicar_filtro_media_movil_action = None

    @classmethod
    def setUpClass(cls):
        cls.aplicar_filtro_media_movil_action = ActionProvider.provide_aplicar_filtro_media_movil_action()

    def test_que_el_filtro_de_la_media_movil_no_modifique_una_senal_constante_salvo_en_los_extremos(self):

        fs = 1
        valores_prueba = [10 for x in range(100)]
        dominio_temporal = numpy.linspace(0, 99, 100, endpoint=False)
        senal_prueba = SenalAudio(fs, dominio_temporal, valores_prueba)
        senal_filtrada = FiltroMediaMovilTest.aplicar_filtro_media_movil_action.execute(senal_prueba, 11)
        valores_filtrados = senal_filtrada.get_valores()
        resultado_esperado = [5.454545, 6.363636, 7.272727, 8.181818, 9.090909]
        resultado_esperado = numpy.concatenate((resultado_esperado, [10 for x in range(90)]))
        resultado_esperado = numpy.concatenate((resultado_esperado, [9.090909, 8.181818, 7.272727, 6.363636, 5.454545]))

        numpy.testing.assert_almost_equal(valores_filtrados, resultado_esperado, decimal=6)

    def test_que_el_filtro_de_la_media_movil_no_modifique_el_dominio_temporal(self):
        fs = 1
        valores_prueba = numpy.linspace(0, 99, 100, endpoint=False)
        dominio_temporal = numpy.linspace(0, 99, 100, endpoint=False)
        senal_prueba = SenalAudio(fs, dominio_temporal, valores_prueba)
        senal_filtrada = FiltroMediaMovilTest.aplicar_filtro_media_movil_action.execute(senal_prueba, 11)
        dominio_filtrado = senal_filtrada.get_dominio_temporal()

        self.assertListEqual(dominio_filtrado, list(dominio_temporal))

    def test_que_el_filtro_de_la_media_movil_con_n_10_produzca_el_mismo_resultado_que_con_n_11(self):
        fs = 1
        valores_prueba = [10 for x in range(100)]
        dominio_temporal = numpy.linspace(0, 99, 100, endpoint=False)
        senal_prueba = SenalAudio(fs, dominio_temporal, valores_prueba)
        senal_filtrada = FiltroMediaMovilTest.aplicar_filtro_media_movil_action.execute(senal_prueba, 10)
        valores_filtrados = senal_filtrada.get_valores()
        resultado_esperado = [5.454545, 6.363636, 7.272727, 8.181818, 9.090909]
        resultado_esperado = numpy.concatenate((resultado_esperado, [10 for x in range(90)]))
        resultado_esperado = numpy.concatenate((resultado_esperado, [9.090909, 8.181818, 7.272727, 6.363636, 5.454545]))

        numpy.testing.assert_almost_equal(valores_filtrados, resultado_esperado, decimal=6)

    def test_que_el_filtro_de_la_media_movil_no_permita_una_longitud_mas_larga_que_la_de_la_senal(self):
        fs = 1
        valores_prueba = numpy.linspace(0, 99, 100, endpoint=False)
        dominio_temporal = numpy.linspace(0, 99, 100, endpoint=False)
        senal_prueba = SenalAudio(fs, dominio_temporal, valores_prueba)

        self.assertRaises(FiltroException,
                          FiltroMediaMovilTest.aplicar_filtro_media_movil_action.execute, senal_prueba, 111)

    def test_que_el_filtro_de_la_media_movil_filtre_correctamente_una_senal_de_prueba(self):
        fs = 10
        valores_prueba = [2, 3, 1, 5, 2, 1, 1, 7, 2, 6]
        dominio_temporal = numpy.linspace(0, 1, 10, endpoint=False)
        senal_prueba = SenalAudio(fs, dominio_temporal, valores_prueba)
        senal_filtrada = FiltroMediaMovilTest.aplicar_filtro_media_movil_action.execute(senal_prueba, 3)
        valores_filtrados = senal_filtrada.get_valores()
        resultado_esperado = [5/3, 2, 3, 8/3, 8/3, 4/3, 3, 10/3, 5, 8/3]

        numpy.testing.assert_almost_equal(valores_filtrados, resultado_esperado, decimal=6)
