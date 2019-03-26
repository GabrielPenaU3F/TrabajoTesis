from abc import ABC, abstractmethod

from scipy import signal


class FiltroStrategy(ABC):

    transformaciones = {}

    def generar_output_filtro(self, *args, input):
        return self.transformaciones.get(input)(*args)

    @abstractmethod
    def generar_transformaciones(self):
        pass

    @abstractmethod
    def get_respuesta_frecuencial(self, cantidad_muestras, filtro):
        pass

class NumDemStrategy(FiltroStrategy):

    def __init__(self):
        self.transformaciones = self.generar_transformaciones()

    def generar_transformaciones(self):
        return {
            'zpk': signal.zpk2tf,
            'sos': signal.sos2tf,
        }

    def get_respuesta_frecuencial(self, cantidad_muestras, filtro):
        b = filtro[0]
        a = filtro[1]
        return signal.freqz(b, a, worN=cantidad_muestras)


class SOSStrategy(FiltroStrategy):

    def __init__(self):
        self.transformaciones = self.generar_transformaciones()

    def generar_transformaciones(self):
        return {
            'ba': signal.tf2sos,
            'zpk': signal.zpk2sos,
        }

    def get_respuesta_frecuencial(self, cantidad_muestras, filtro):
        return signal.sosfreqz(sos=filtro, worN=cantidad_muestras)


class ZPKStrategy(FiltroStrategy):

    def __init__(self):
        self.transformaciones = self.generar_transformaciones()

    def generar_transformaciones(self):
        return {
            'ba': signal.tf2zpk,
            'sos': signal.sos2zpk,
        }

    def get_respuesta_frecuencial(self, cantidad_muestras, filtro):
        z = filtro[0]
        p = filtro[1]
        k = filtro[2]
        return signal.freqz_zpk(z, p, k, worN=cantidad_muestras)
