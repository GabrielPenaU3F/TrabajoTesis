from scipy import signal

from core.domain.filtros.filtro_pasabanda import Filtro
from core.domain.senal_audio import SenalAudio


class FiltradoPasabandaService:

    def aplicar_filtro_pasabanda(self, senal, tipo, output, banda):
        fs = senal.get_fs()
        filtro = Filtro(banda, fs=fs, tipo=tipo, representacion_output=output)


        ''' Plotear la respuesta en frecuencia del filtro:
        w, h = signal.sosfreqz(sos=filtro_sos, worN=senal.get_longitud())
        db = 20 * numpy.log10(numpy.abs(h))
        pyplot.plot(w / numpy.pi, db)
        pyplot.show()
        '''

        filtro_sos = filtro.get_filtro()
        valores_filtrados = signal.sosfilt(filtro_sos, senal.get_valores())
        return SenalAudio(fs, senal.get_dominio_temporal(), valores_filtrados)
