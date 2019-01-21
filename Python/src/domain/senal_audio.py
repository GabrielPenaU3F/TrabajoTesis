from src.exception.exceptions import *


class SenalAudio:

    def __init__(self, *args):

        if len(args) == 2:
            fs = args[0]
            valores = args[1]
            self.longitud = len(valores)
            self.duracion = self.longitud/fs
            self.fs = fs
            dominio_temporal = self.construir_dominio_temporal(fs, self.longitud)
            self.senal_en_tiempo = self.construir_senal_en_tiempo(dominio_temporal, valores)

        elif len(args) == 3:
            fs = args[0]
            dominio_temporal = args[1]
            valores = args[2]
            if len(dominio_temporal) != len(valores):
                raise ValidacionParametrosSenalException("El dominio y los valores tienen longitudes distintas")
            self.longitud = len(valores)
            self.duracion = self.longitud/fs
            self.fs = fs
            self.senal_en_tiempo = self.construir_senal_en_tiempo(dominio_temporal, valores)

        else: raise CantidadDeParametrosException("La señal de audio puede recibir únicamente 2 o 3 parámetros")

    def construir_dominio_temporal(self, fs, longitud):
        dominio_temporal = []
        for t in range(longitud):
            dominio_temporal.append(t / fs)
        return dominio_temporal

    def construir_senal_en_tiempo(self, dominio_temporal, valores):
        senal_en_tiempo = {}
        for t in range(len(dominio_temporal)):
            senal_en_tiempo[dominio_temporal[t]] = valores[t]
        return senal_en_tiempo

    def construir_valores_senal_nula(self, longitud):
        valores = []
        for t in range(longitud):
            valores.append(0)
        return valores

    def get_fs(self):
        return self.fs

    def get_duracion(self):
        return self.duracion

    def get_longitud(self):
        return self.longitud

    def get_dominio_temporal(self):
        return list(self.senal_en_tiempo.keys())

    def get_valores(self):
        return list(self.senal_en_tiempo.values())

    '''
    Se observa en este método que la señal se modela como un valor constante
    entre muestra y muestra, con amplitud igual a la muestra de la izquierda
    de cada intervalo. Es decir, un retenedor de orden cero (ZOH).
    '''
    def get_valor_en(self, t):
        if self.senal_en_tiempo.__contains__(t): return self.senal_en_tiempo.get(t)
        return self.obtener_valor_inmediato_anterior(t)

    def obtener_valor_inmediato_anterior(self, t):
        for k in self.senal_en_tiempo:
            if (k + 1/self.fs) > t: return self.senal_en_tiempo.get(k)


    '''
    Existe siempre la posibilidad de que los tiempos elegidos para recortar
    no coincidan exactamente con las muestras, ya que la señal es discreta.
    Esta función siempre achicará para adentro, es decir, recortará desde
    los dos tiempos muestreados más cercanos a los solicitados que se encuentren
    dentro del intervalo considerado. Esto ocasionará que se pierda información.
    Con una frecuencia de muestreo mayor, menos información se perderá. Con los 
    44100Hz estándar de procesamiento de audio, perder 1/44100 de información
    temporal es prácticamente insignificante.
    '''
    def recortar_segmento(self, tiempo_inicio, tiempo_final):

        dominio_temporal = self.get_dominio_temporal()
        nuevo_dominio = []
        nuevos_valores = []
        for t in dominio_temporal:
            if not (t < tiempo_inicio or t > tiempo_final):
                nuevo_dominio.append(t)
                nuevos_valores.append(self.senal_en_tiempo.get(t))

        return SenalAudio(self.fs, nuevo_dominio, nuevos_valores)

    '''
    def obtener_t_inmediato_anterior(self, t):
        for k in self.senal_en_tiempo:
            if (k + 1/self.fs) > t: return k

    def obtener_t_inmediato_siguiente(self, t):
        for k in self.senal_en_tiempo:
            if (t - 1/self.fs) < k: return k
    '''
