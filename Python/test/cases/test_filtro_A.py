import unittest
from core.domain.filtros.filtro_pasabanda import Filtro


class FiltroATest(unittest.TestCase):

    def test_que_la_ganancia_del_filtro_sea_0dB_en_1kHz(self):
        fs = 48000
        filtro = Filtro(fs=fs, tipo='A', representacion_output='ba')
        w, h = filtro.get_respuesta_frecuencial(24000)
        # TODO: Revisar hasta donde está definida
        '''
        # Plotear respuesta en frecuencia
        pyplot.semilogx(w * fs / (2 * numpy.pi), h)
        pyplot.show()
        '''
        self.assertAlmostEqual(0, h[1000], places=2)
