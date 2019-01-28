import numpy

from src.domain.senal_en_frecuencia import SenalEnFrecuencia
from src.domain.senal_en_tiempo import SenalEnTiempo


class OperacionesSobreSenalesService:

    def transformar_fourier(self, senal_en_tiempo, fs):
        valores_tiempo = senal_en_tiempo.get_valores()
        duracion = len(valores_tiempo) / fs
        espaciado_en_frecuencia = 1 / duracion
        dominio_frecuencial = list(numpy.arange(0, fs, espaciado_en_frecuencia))
        valores_frecuencia = numpy.fft.fft(valores_tiempo)
        return SenalEnFrecuencia(dominio_frecuencial, valores_frecuencia)

    def evaluar_diferencias_finitas_hacia_adelante(self, senal_en_tiempo):
        valores = senal_en_tiempo.get_valores()
        valores.append(0)  # Para que la señal derivada tenga la misma longitud que la original
        valores_derivados = []
        for i in range(len(valores) - 1):
            diferencia_finita = valores[i+1] - valores[i]
            valores_derivados.append(diferencia_finita)
        return SenalEnTiempo(senal_en_tiempo.get_dominio_temporal(), valores_derivados)
