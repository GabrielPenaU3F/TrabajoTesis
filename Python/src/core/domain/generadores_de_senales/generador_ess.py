import math

import numpy

from src.core.domain.senal_audio import SenalAudio
from src.core.domain.senal_en_tiempo import SenalEnTiempo


class GeneradorESS:

    def generar_senal_ess(self, fs, duracion, frecuencia_inicial, frecuencia_final):

        '''
        La señal ESS está dada por la expresión:

            s(t) = sin[K.(exp(t/L) - 1)] = sin[(2pi.f1.T/R).(exp(tR/T) - 1)]

        Las constantes K, L, R son como sigue:

            K = 2pi.f1.L
            L = T/R
            R = ln(f2/f1)

        Se indican las dos notaciones equivalentes porque en distintas fuentes
        aparecen ambas.

        Esta señal es una senoide cuya frecuencia fundamental crece
        exponencialmente. Su contenido frecuencial está comprendido en la
        banda entre f1 y f2.
        '''

        R = math.log(frecuencia_final / frecuencia_inicial)
        L = duracion / R
        K = 2 * math.pi * frecuencia_inicial * L

        dominio_temporal = list(numpy.arange(0, duracion, 1/fs))
        valores = []
        for t in dominio_temporal:
            valores.append(math.sin(K * (math.exp(t / L) - 1)))

        return SenalAudio(fs, dominio_temporal, valores)

    def generar_filtro_inverso_ess(self, fs, duracion, frecuencia_inicial, frecuencia_final):
        '''
            El filtro inverso es tal que al pasar la señal por él, se obtiene
            como resultado una delta
            Está dado por la función

                h(t) = s_i(t)/k

            Donde s_i(t) es la señal ESS invertida en el tiempo, y k es como
            sigue

                k = exp(tR/T)
                R = ln(f2/f1)

            El resultado es una versión con amplitud modulada de la señal ESS
            invertida en el tiempo.
        '''

        R = math.log(frecuencia_inicial / frecuencia_inicial)

        ess = self.generar_senal_ess(fs, duracion, frecuencia_inicial, frecuencia_final)
        ess_invertida = list(numpy.fliplr([ess.get_valores()])[0])
        dominio_temporal = ess.get_dominio_temporal()
        filtro = []
        for t in range(len(dominio_temporal)):
            k = math.exp(t * R / duracion)
            filtro.append(ess_invertida[t] / k)

        return SenalEnTiempo(dominio_temporal, filtro)
