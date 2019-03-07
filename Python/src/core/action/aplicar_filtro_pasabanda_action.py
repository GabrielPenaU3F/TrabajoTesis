import math

import numpy
from matplotlib import pyplot
from scipy import signal

from src.core.domain.filtro import Filtro
from src.core.domain.senal_audio import SenalAudio


class AplicarFiltroPasabandaAction:

    def execute(self, senal, f_inferior, f_superior):

        fs = senal.get_fs()
        filtro = Filtro(f_inferior, f_superior, fs=fs, tipo='Cheby2', representacion='sos')


        ''' Plotear la respuesta en frecuencia del filtro:
        w, h = signal.sosfreqz(sos=filtro_sos, worN=senal.get_longitud())
        db = 20 * numpy.log10(numpy.abs(h))
        pyplot.plot(w / numpy.pi, db)
        pyplot.show()
        '''

        filtro_sos = filtro.get_filtro()
        valores_filtrados = signal.sosfilt(filtro_sos, senal.get_valores())
        return SenalAudio(fs, senal.get_dominio_temporal(), valores_filtrados)
