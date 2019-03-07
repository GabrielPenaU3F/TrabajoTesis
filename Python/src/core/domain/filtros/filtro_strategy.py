from abc import ABC, abstractmethod

from scipy import signal


class Strategy(ABC):

    transformaciones = {}

    def generar_output_filtro(self, *args, input):
        return self.transformaciones.get(input)(*args)

    @abstractmethod
    def generar_transformaciones(self):
        pass


class NumDemStrategy(Strategy):

    def __init__(self):
        self.transformaciones = self.generar_transformaciones()

    def generar_transformaciones(self):
        return {
            'zpk': signal.zpk2tf,
            'sos': signal.sos2tf,
        }


class SOSStrategy(Strategy):

    def __init__(self):
        self.transformaciones = self.generar_transformaciones()

    def generar_transformaciones(self):
        return {
            'ba': signal.tf2sos,
            'zpk': signal.zpk2sos,
        }


class ZPKStrategy(Strategy):

    def __init__(self):
        self.transformaciones = self.generar_transformaciones()

    def generar_transformaciones(self):
        return {
            'ba': signal.tf2zpk,
            'sos': signal.sos2zpk,
        }
