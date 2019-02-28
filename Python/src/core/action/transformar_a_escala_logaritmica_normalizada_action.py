import numpy

from src.core.domain.senal_audio import SenalAudio


class TransformarAEscalaLogaritmicaNormalizadaAction:

    def execute(self, senal):
        valores_senal = senal.get_valores()
        valor_max = max(valores_senal)
        valores_norm = [valores_senal[i] / valor_max for i in range(len(valores_senal))]
        valores_db = 20 * numpy.log10(valores_norm)
        return SenalAudio(senal.get_fs(), senal.get_dominio_temporal(), valores_db)
