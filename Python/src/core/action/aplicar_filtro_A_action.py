from scipy import signal

from src.core.domain.filtros.filtro import Filtro
from src.core.domain.senal_audio import SenalAudio


class AplicarFiltroAAction:

    def execute(self, senal):
        fs = senal.get_fs()
        filtro = Filtro(fs=fs, tipo='A', representacion='ba')
        filtro_ba = filtro.get_filtro()
        valores_filtrados = signal.lfilter(filtro_ba[0], filtro_ba[1], senal.get_valores())
        return SenalAudio(fs, senal.get_dominio_temporal(), valores_filtrados)
