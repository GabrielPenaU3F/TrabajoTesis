import math
import unittest

import numpy

from src.core.domain.archivos.escritor_de_archivos_de_medicion import EscritorDeArchivosDeMedicion
from src.core.domain.medicion import Medicion
from src.core.domain.senal_audio import SenalAudio
from src.core.domain.tiempo_reverberacion import TiempoReverberacion


class TestEscritorArchivos(unittest.TestCase):

    escritor = None

    @classmethod
    def setUpClass(cls):
        cls.escritor = EscritorDeArchivosDeMedicion()

    def test_que_un_valor_se_formatee_correctamente(self):
        valor = 2
        valor_formateado = "$2"
        self.assertEqual(valor_formateado, self.escritor.string_valor(valor))

    def test_que_una_lista_de_valores_se_formatee_correctamente(self):
        valores = [2, 3, 4, 5]
        valores_formateados = "$2,3,4,5"
        self.assertEqual(valores_formateados, self.escritor.string_lista_valores(valores))

    def test_que_un_RT_se_formatee_correctamente(self):
        rt = TiempoReverberacion(0.6, 0.999, 4)
        rt_formateado = "$0.6,0.999,4"
        self.assertEqual(rt_formateado, self.escritor.string_rt(rt))

    def test_que_una_medicion_completa_se_formatee_correctmaente(self):
        fs = 1
        valores_ri = [1, 2, 3, 4, 5]
        valores_cd = [1, 2, 3]
        edt = TiempoReverberacion(0.6, 0.99, 4)
        t20 = TiempoReverberacion(0.7, 0.995, 9)
        t30 = TiempoReverberacion(0.78, 0.96, 8)
        curvatura = 1
        ri = SenalAudio(fs, valores_ri)
        cd = SenalAudio(fs, valores_cd)
        medicion = Medicion(ri, cd, edt, t20, t30, curvatura, nivel=False)

        medicion_formateada = "$1$1,2,3,4,5$1,2,3$0.6,0.99,4$0.7,0.995,9$0.78,0.96,8$1"
        self.assertEqual(medicion_formateada, self.escritor.formatear_medicion(medicion))

