import math
import numpy

from src.core.domain.senal_en_frecuencia import SenalEnFrecuencia
from src.core.domain.senal_en_tiempo import SenalEnTiempo
from src.exception.excepciones import AlineacionException


class OperacionesSobreSenalesService:

    def __init__(self):
        from src.core.provider.service_provider import ServiceProvider
        self.operaciones_sobre_arrays_service = ServiceProvider.provide_operaciones_sobre_arrays_service()

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

    def calcular_periodo_muestral(self, senal_en_tiempo):
        return senal_en_tiempo.get_dominio_temporal()[1] - senal_en_tiempo.get_dominio_temporal()[0]

    def calcular_energia_total_de_senal(self, senal_en_tiempo):
        Ts = self.calcular_periodo_muestral(senal_en_tiempo)
        return self.calcular_energia_total(senal_en_tiempo.get_valores(), Ts)

    def calcular_energia_total(self, valores, Ts):
        energia = 0
        for valor in valores:
            energia += math.pow(valor, 2) * Ts
        return energia


    '''
    La eliminación del delay se hace por un algoritmo de tipo iterativo.
    Se define una heurística para evaluar cuando dos señales son más parecidas:
    tomamos como referencia la suma total de las diferencias punto a punto
    entre los valores de ambas señales. Las señales se consideran alineadas
    en la posición en que dicha diferencia es mínima. El análisis se hace solo
    sobre una pequeña ventana, cuya duración debe ser pequeña, ya que es muy 
    costoso en tiempo de cómputo. Obviamente, dicha ventana debe ser bastante
    más grande que el delay a eliminar, lo que requiere conocimiento de la
    duración del mismo. Ya que las latencias producidas en la grabación
    son mínimas, esto no resultará problemático.
    '''
    def eliminar_latencia_entre_senales(self, senal_de_referencia, senal_con_latencia, Ts, ventana_en_segundos):

        ventana_en_cantidad_de_muestras = int(ventana_en_segundos/Ts)
        if ventana_en_cantidad_de_muestras > self.operaciones_sobre_arrays_service.obtener_longitud_del_array_mas_corto(
                senal_de_referencia.get_valores(), senal_con_latencia.get_valores()):
            raise AlineacionException("La ventana debe ser mas corta que las señales a alinear")

        valores_con_latencia = senal_con_latencia.get_valores().copy()[0:ventana_en_cantidad_de_muestras]
        valores_referencia = senal_de_referencia.get_valores().copy()[0:ventana_en_cantidad_de_muestras]
        iteraciones = len(valores_con_latencia) - 1

        puntos_heuristicos = []
        for i in range(iteraciones):
            heuristico = self.calcular_heuristico(valores_referencia, valores_con_latencia)
            puntos_heuristicos.append(heuristico)
            valores_con_latencia.pop(0)

        posicion_inicial_truncada = puntos_heuristicos.index(min(puntos_heuristicos))
        nuevos_valores = senal_con_latencia.get_valores().copy()
        for i in range(posicion_inicial_truncada):
            nuevos_valores.pop(0)

        nuevo_dominio = list(numpy.arange(0, len(nuevos_valores)*Ts, Ts))
        return SenalEnTiempo(nuevo_dominio, nuevos_valores)

    def calcular_heuristico(self, valores_referencia, valores_con_latencia):
        heuristico = 0
        factor_ajuste = max(valores_referencia)/max(valores_con_latencia)
        valores_con_latencia_ajustados = []
        for i in range(len(valores_con_latencia)):
            valores_con_latencia_ajustados.append(valores_con_latencia[i] * factor_ajuste)
        longitud = self.operaciones_sobre_arrays_service.obtener_longitud_del_array_mas_corto(
            valores_con_latencia, valores_referencia)
        for i in range(longitud):
            diferencia = abs(valores_referencia[i] - valores_con_latencia[i])
            heuristico += diferencia
        return heuristico

