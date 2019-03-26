import math

import numpy

from src.exception.excepciones import FiltroException
from src.core.domain.filtros.filtro_strategy import *


class Filtro:

    def __init__(self, *args, fs, tipo, representacion_output):
        self.fs = fs
        self.tipos_filtro = {
            "Cheby2": self.construir_filtro_chebyshev_tipo_2,
            "A": self.construir_filtro_A
        }
        self.strategies_transformacion_output = {
            "ba": NumDemStrategy(),
            "sos": SOSStrategy(),
            "zpk": ZPKStrategy(),
        }
        if not self.strategies_transformacion_output.__contains__(representacion_output):
            raise FiltroException("Representación inválida")
        self.representacion_output = representacion_output
        self.filtro = self.construir_filtro(args, tipo=tipo)

    def construir_filtro_chebyshev_tipo_2(self, args):
        banda = args[0]
        f_inferior = banda.get_frecuencia_inicial()
        f_superior = banda.get_frecuencia_final()
        margen = self.determinar_margen(f_superior)
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

        filtro = signal.cheby2(orden + 1, 60, wnat, btype='bandpass', output=self.representacion_output)
        return filtro

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
        return self.strategies_transformacion_output.get(self.representacion_output).\
            generar_output_filtro(zeros_digital, polos_digital, k_digital, input='zpk')

    def construir_filtro(self, args, tipo):
        return self.tipos_filtro.get(tipo)(args)

    def get_filtro(self):
        return self.filtro

    def get_respuesta_frecuencial(self, cantidad_muestras):

        filtro = self.get_filtro()
        w, h = self.strategies_transformacion_output.get(self.representacion_output).\
            get_respuesta_frecuencial(cantidad_muestras, filtro)
        db = 20 * numpy.log10(numpy.abs(h))
        return w, db

    '''
        El márgen indica la longitud en hertz que hay entre las frecuenicas stop y pass.
        A bajas frecuencias, utilizar un margen pequeño no supone problemas; sin embargo,
        a medida que la frecuencia crece, es necesario tomar un margen mayor o de lo contrario
        el filtro se vuelve irrealizable en la práctica (en algunas de las pruebas, los cálculos
        involucraron valores de exponente 40000 que Python no es capaz de representar). Por esto,
        se implementa esta función que determina el márgen adecuado para los cálculos en
        base a las restricciones conocidas, a saber:
            - Para frecuencias de 1122 (octava de 1000Hz) o menores, un márgen de 0.5Hz es aceptable
            - Para frecuencias altas no cercanas la límite basta con un márgen de 10Hz
            - Para la frecuencia superior más alta posible, 22627Hz, se requiere como mínimo un márgen
             de 25Hz
    '''
    def determinar_margen(self, f_superior):
        if f_superior <= 1122:
            return 0.5
        elif 1122 < f_superior <= 11314:
            return 10
        else:
            return 25
