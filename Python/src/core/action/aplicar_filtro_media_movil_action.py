import numpy
from scipy import signal

from src.core.domain.senal_en_tiempo import SenalEnTiempo
from src.exception.excepciones import FiltradoImposibleException


class AplicarFiltroMediaMovilAction:

    def execute(self, senal, longitud):

        if longitud > len(senal.get_valores()):
            raise FiltradoImposibleException("La longitud del kernel es mayor que la de la señal")

        if longitud % 2 == 0:
            longitud += 1

        kernel = numpy.ones(longitud) / longitud
        dominio_temporal = senal.get_dominio_temporal().copy()
        valores = senal.get_valores()
        return SenalEnTiempo(dominio_temporal, list(signal.fftconvolve(valores, kernel, 'same')))
