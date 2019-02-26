import numpy

from src.core.domain.senal_en_tiempo import SenalEnTiempo


class TransformarAEscalaLogaritmicaNormalizadaAction:

    def execute(self, senal):
        dominio_temporal = senal.get_dominio_temporal().copy()
        valores = senal.get_valores()
        valores_norm = [valores[i] / max(valores) for i in range(len(valores))]
        valores_db = 20 * numpy.log10(valores_norm)
        return SenalEnTiempo(dominio_temporal, valores_db)
