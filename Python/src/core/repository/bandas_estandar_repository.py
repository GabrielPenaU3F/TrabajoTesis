import math

from src.core.domain.banda_de_frecuencia import BandaDeFrecuencia
from src.exception.excepciones import FiltroException


class BandasEstandarRepository:

    def __init__(self):
        frecuencias_centrales_octavas = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        frecuencias_centrales_tercios_octavas = [20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200,
                                                 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000,
                                                 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000,
                                                 20000]
        self.bandas_octava = self.construir_bandas_octava(frecuencias_centrales_octavas)
        self.bandas_tercio_octava = self.construir_bandas_tercio_octava(frecuencias_centrales_tercios_octavas)



    def get_banda_octava(self, f_central):
        if self.bandas_octava.keys().__contains__(f_central):
            return self.bandas_octava.get(f_central)
        else:
            raise FiltroException("La banda de octava centrada en dicha frecuencia no es estándar")


    def get_banda_tercio_octava(self, f_central):
        if self.bandas_tercio_octava.keys().__contains__(f_central):
            return self.bandas_tercio_octava.get(f_central)
        else:
            raise FiltroException("La banda de tercio de octava centrada en dicha frecuencia no es estándar")

    def construir_bandas_octava(self, frecuencias_centrales_octavas):
        bandas_octava = {}
        for centro_banda_octava in frecuencias_centrales_octavas:
            f_inicial = centro_banda_octava / math.sqrt(2)
            f_final = 2 * f_inicial
            bandas_octava[centro_banda_octava] = BandaDeFrecuencia(f_inicial, f_final)
        return bandas_octava

    def construir_bandas_tercio_octava(self, frecuencias_centrales_tercios_octavas):
        bandas_tercio_octava = {}
        for centro_banda_tercio_octava in frecuencias_centrales_tercios_octavas:
            f_inicial = centro_banda_tercio_octava / math.pow(2, 1 / 6)
            f_final = math.pow(2, 1 / 3) * f_inicial
            bandas_tercio_octava[centro_banda_tercio_octava] = BandaDeFrecuencia(f_inicial, f_final)
        return bandas_tercio_octava
