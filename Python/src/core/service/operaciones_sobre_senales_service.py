import math
import numpy
from scipy import signal

from src.core.domain.contenido_frecuencial import ContenidoFrecuencial
from src.core.domain.punto_senal_frecuencia import PuntoSenalFrecuencia
from src.core.domain.senal_audio import SenalAudio
from src.exception.excepciones import AlineacionException


class OperacionesSobreSenalesService:

    def __init__(self):
        from src.core.provider.service_provider import ServiceProvider
        self.operaciones_sobre_arrays_service = ServiceProvider.provide_operaciones_sobre_arrays_service()

    def transformar_fourier(self, senal):
        fs = senal.get_fs()
        valores_tiempo = senal.get_valores()
        dominio_frecuencial = list(numpy.linspace(0, fs, len(valores_tiempo), endpoint=False))
        valores_frecuencia = numpy.fft.fft(valores_tiempo)
        return ContenidoFrecuencial(
            [PuntoSenalFrecuencia(dominio_frecuencial[i], valores_frecuencia[i])
             for i in range(len(dominio_frecuencial))])

    def evaluar_diferencias_finitas_hacia_adelante(self, senal):
        valores = senal.get_valores()
        valores.append(0)  # Para que la señal derivada tenga la misma longitud que la original
        valores_derivados = []
        for i in range(len(valores) - 1):
            diferencia_finita = valores[i+1] - valores[i]
            valores_derivados.append(diferencia_finita)
        return SenalAudio(senal.get_fs(), senal.get_dominio_temporal(), valores_derivados)

    def calcular_energia_total_de_senal(self, senal):
        energia = 0
        dx = 1/senal.get_fs()
        for valor in senal.get_valores():
            energia += math.pow(valor, 2) * dx
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
    def eliminar_latencia_entre_senales(self, senal_de_referencia, senal_con_latencia, ventana_en_segundos):

        Ts = 1/senal_de_referencia.get_fs()
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

        nuevo_dominio = list(numpy.linspace(0, len(nuevos_valores)*Ts, len(nuevos_valores), endpoint=False))
        return SenalAudio(1/Ts, nuevo_dominio, nuevos_valores)

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

    def realizar_convolucion(self, senal_1, senal_2):
        convolucion = list(signal.fftconvolve(senal_1.get_valores(), senal_2.get_valores(), 'full'))
        fs = senal_1.get_fs()
        dominio_temporal = numpy.linspace(0, len(convolucion)/fs, len(convolucion), endpoint=False)
        return SenalAudio(fs, dominio_temporal, convolucion)

    def realizar_correlacion(self, senal_1, senal_2):
        correlacion = list(signal.correlate(senal_1.get_valores(), senal_2.get_valores(), 'full'))
        fs = senal_1.get_fs()
        dominio_temporal = numpy.linspace(0, len(correlacion)/fs, len(correlacion), endpoint=False)
        return SenalAudio(dominio_temporal, correlacion)

    def integrar_senal(self, senal, t_inicio, t_fin):
        dx = 1/senal.get_fs()
        valores = senal.get_valores()
        integral = 0
        senal_recortada = self.recortar_en_tiempo(senal, t_inicio, t_fin)
        for i in range(senal_recortada.get_longitud()):
            integral += valores[i] * dx

        return integral

    def recortar_en_tiempo(self, senal, t_inicio, t_fin):
        dominio_temporal = senal.get_dominio_temporal()
        valores = senal.get_valores()
        nuevo_dominio = []
        nuevos_valores = []
        for i in range(len(dominio_temporal)):
            if t_inicio <= dominio_temporal[i] <= t_fin:
                nuevo_dominio.append(dominio_temporal[i])
                nuevos_valores.append(valores[i])

        return SenalAudio(senal.get_fs(), nuevo_dominio, nuevos_valores)
