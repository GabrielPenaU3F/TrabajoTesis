import math

import numpy
from matplotlib import pyplot
from scipy import signal

from src.core.domain.senal_audio import SenalAudio


class AplicarFiltroPasabandaAction:

    def execute(self, senal, f_inferior, f_superior):

        fs = senal.get_fs()
        margen = 0.5  # Parámetro ajustable, en Hz
        frec_nyquist = senal.get_fs()/2
        margen_norm = margen/frec_nyquist
        f_inferior_norm = f_inferior/frec_nyquist
        f_superior_norm = f_superior/frec_nyquist
        wpass_i = f_inferior_norm
        wpass_f = f_superior_norm
        wstop_i = f_inferior_norm - margen_norm
        wstop_f = f_superior_norm + margen_norm
        gpass = 1 #  Máxima pérdida tolerada en la banda de paso. Parámetro ajustable, en dB
        gstop = 60 #  Mínima atenuación requerida fuera de la banda de paso. Parámetro ajustable, en dB

        caract_filtro = signal.cheb2ord(wp=(wpass_i, wpass_f), ws=(wstop_i, wstop_f), gpass=gpass, gstop=gstop, analog=False)
        orden = caract_filtro[0]  # Mínimo orden de filtro necesario
        wnat = caract_filtro[1]  # Frecuencia natural Chebyshev del filtro

        filtro_sos = signal.cheby2(orden+1, 60, wnat, btype='bandpass', output='sos')

        ''' Plotear la respuesta en frecuencia del filtro:
        w, h = signal.sosfreqz(sos=filtro_sos, worN=senal.get_longitud())
        db = 20 * numpy.log10(numpy.abs(h))
        pyplot.plot(w / numpy.pi, db)
        pyplot.show()
        '''

        valores_filtrados = signal.sosfilt(filtro_sos, senal.get_valores())
        return SenalAudio(fs, senal.get_dominio_temporal(), valores_filtrados)
