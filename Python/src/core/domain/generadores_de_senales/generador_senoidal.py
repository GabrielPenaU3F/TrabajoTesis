import math

import numpy

from src.core.domain.senal_audio import SenalAudio


class GeneradorSenoidal():

    def generar_valores_senoide(self, longitud, fs):
        dominio_temporal = []
        for t in range(longitud):
            dominio_temporal.append(t / fs)
        valores = []
        for t in dominio_temporal:
            valores.append(math.sin(t))
        return valores

    def generar_senoide(self, fs, duracion, frecuencia, amplitud, fase_inicial):
        dominio_temporal = list(numpy.arange(0, duracion, 1/fs))
        valores = []
        for t in dominio_temporal:
            frec_angular = 2*math.pi*frecuencia
            valores.append(amplitud * math.sin(frec_angular*t + fase_inicial))
        return SenalAudio(fs, dominio_temporal, valores)

