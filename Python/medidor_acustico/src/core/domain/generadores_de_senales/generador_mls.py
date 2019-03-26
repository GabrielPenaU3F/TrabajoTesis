import numpy
from scipy import signal

from src.core.domain.senal_audio import SenalAudio


class GeneradorMLS:

    def generar_senal_mls(self, n_bits, periodos, fs):

        valores = []
        for i in range(periodos):
            periodo = self.generar_periodo(n_bits)
            valores += periodo
        return SenalAudio(fs, valores)

    def generar_periodo(self, n_bits):
        senal = signal.max_len_seq(n_bits)[0] * 2 - 1  # +1 y -1
        return list(senal.astype(dtype=numpy.float64))
