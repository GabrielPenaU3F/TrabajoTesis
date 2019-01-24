import numpy

from src.domain.senal_en_frecuencia import SenalEnFrecuencia


class TransformarFourierAction:

    def execute(self, senal_en_tiempo, fs):
        valores_tiempo = senal_en_tiempo.get_valores()
        duracion = len(valores_tiempo)/fs
        espaciado_en_frecuencia = 1/duracion
        dominio_frecuencial = list(numpy.arange(0, fs, espaciado_en_frecuencia))
        valores_frecuencia = numpy.fft.fft(valores_tiempo)
        return SenalEnFrecuencia(dominio_frecuencial, valores_frecuencia)
