import math

import numpy

from src.domain.senal_audio import SenalAudio


class GeneradorMLS:

    def generar_senal_mls(self, n_bits, periodos, fs):

        valores = []
        for i in range(periodos):
            periodo = self.generar_periodo(n_bits)
            valores += periodo
        return SenalAudio(fs, valores)

    def generar_periodo(self, n_bits):
        largo_periodo = int(math.pow(2, n_bits) - 1)
        senal = numpy.random.randint(2, size=largo_periodo)
        for i in range(len(senal)):
            if senal[i] == 0:
                senal[i] = -1
        return list(senal.astype(dtype=numpy.float64))
