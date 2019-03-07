import math

from src.core.domain.banda_de_frecuencia import BandaDeFrecuencia
from src.core.domain.filtros.filtro_banda import FiltroBanda


class FiltroOctava(FiltroBanda):

    def __init__(self, f_central):
        super().__init__()
        self.frecuencias_centrales = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        if self.frecuencias_centrales.__contains__(f_central):
            self.banda = self.construir_banda(f_central)

    def construir_banda(self, f_central):
        f_inicial = f_central/math.sqrt(2)
        f_final = 2*f_inicial
        return BandaDeFrecuencia(f_inicial, f_final)

    def get_banda(self):
        return self.banda
