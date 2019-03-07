import math

import numpy
from scipy import signal

from src.exception.excepciones import FiltroException


class Filtro:

    def __init__(self, *args, fs, tipo, representacion):
        self.fs = fs
        self.tipos_filtro = {
            "Cheby2": self.construir_filtro_chebyshev_tipo_2,
            "A": self.construir_filtro_A
        }
        self.representaciones = ["ba", "sos", "zpk", "kernel"]
        if not self.representaciones.__contains__(representacion): raise FiltroException("Representación inválida")
        self.representacion = representacion
        self.filtro = self.construir_filtro(args, tipo=tipo)


    def construir_filtro_chebyshev_tipo_2(self, args):
        f_inferior = args[0]
        f_superior = args[1]
        margen = 0.5  # Parámetro ajustable, en Hz
        frec_nyquist = self.fs / 2
        margen_norm = margen / frec_nyquist
        f_inferior_norm = f_inferior / frec_nyquist
        f_superior_norm = f_superior / frec_nyquist
        wpass_i = f_inferior_norm
        wpass_f = f_superior_norm
        wstop_i = f_inferior_norm - margen_norm
        wstop_f = f_superior_norm + margen_norm
        gpass = 1  # Máxima pérdida tolerada en la banda de paso. Parámetro ajustable, en dB
        gstop = 60  # Mínima atenuación requerida fuera de la banda de paso. Parámetro ajustable, en dB

        caract_filtro = signal.cheb2ord(wp=(wpass_i, wpass_f), ws=(wstop_i, wstop_f), gpass=gpass, gstop=gstop,
                                        analog=False)
        orden = caract_filtro[0]  # Mínimo orden de filtro necesario
        wnat = caract_filtro[1]  # Frecuencia natural Chebyshev del filtro

        if self.representacion == "sos":
            return signal.cheby2(orden + 1, 60, wnat, btype='bandpass', output='sos')

    def construir_filtro_A(self, args):
        zeros = [0, 0, 0, 0]
        polos = [-2 * math.pi * 20.60,
                 -2 * math.pi * 20.60,
                 -2 * math.pi * 107.7,
                 -2 * math.pi * 737.9,
                 -2 * math.pi * 12200,
                 -2 * math.pi * 12200,
        ]
        k = 1.2588*math.pow(12200, 2)*math.pow(2*math.pi, 2)
        zeros_digital, polos_digital, k_digital = signal.bilinear_zpk(zeros, polos, k, self.fs)
        if self.representacion == "ba":
            return signal.zpk2tf(zeros_digital, polos_digital, k_digital)

    def construir_filtro(self, args, tipo):
        return self.tipos_filtro.get(tipo)(args)

    def get_filtro(self):
        return self.filtro

    def get_respuesta_frecuencial(self, n):

        w, h = 0, 0
        if self.representacion == "sos":
            w, h = signal.sosfreqz(sos=self.get_filtro(), worN=n)
        elif self.representacion == "ba":
            b, a = self.get_filtro()
            w, h = signal.freqz(b, a, worN=n)
        elif self.representacion == "zpk":
            z, p, k = self.get_filtro()
            w, h = signal.freqz_zpk(z, p, k, worN=n)

        db = 20 * numpy.log10(numpy.abs(h))
        return w, db