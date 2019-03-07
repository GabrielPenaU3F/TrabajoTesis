import math

from src.core.domain.banda_de_frecuencia import BandaDeFrecuencia
from src.core.domain.filtros.filtro_banda import FiltroBanda


class FiltroTercioOctava(FiltroBanda):

    def __init__(self, f_central):
        super().__init__()
        self.frecuencias_centrales = [20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200,
                                      250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000,
                                      2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000,
                                      20000]
        if self.frecuencias_centrales.__contains__(f_central):
            self.banda = self.construir_banda(f_central)

    def construir_banda(self, f_central):
        f_inicial = f_central / math.pow(2, 1/6)
        f_final = math.pow(2, 1/3) * f_inicial
        return BandaDeFrecuencia(f_inicial, f_final)

    def get_banda(self):
        return self.banda
