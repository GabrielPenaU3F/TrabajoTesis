from random import gauss

import numpy

from core.domain.senal_audio import SenalAudio


class GeneradorRuido:

    def generar_ruido_blanco(self, fs, duracion, mu, sigma):
        t = numpy.linspace(0, duracion, duracion*fs, endpoint=False)
        valores = [gauss(mu, sigma) for i in range(len(t))]
        return SenalAudio(fs, t, valores)
