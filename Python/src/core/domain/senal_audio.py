import math

from src.core.domain.contenido_temporal import ContenidoTemporal
from src.core.domain.punto_senal_tiempo import PuntoSenalTiempo
from src.exception.excepciones import *


class SenalAudio:

    def __init__(self, *args):

        if len(args) == 2:
            fs = args[0]
            valores = list(args[1])
            self.longitud = len(valores)
            self.duracion = self.longitud/fs
            self.fs = fs
            dominio_temporal = self.construir_dominio_temporal(fs, len(valores))
            self.contenido_temporal = self.construir_senal(dominio_temporal, valores)

        elif len(args) == 3:
            fs = args[0]
            dominio_temporal = list(args[1])
            valores = list(args[2])
            self.validar_parametros(fs, dominio_temporal, valores)
            self.longitud = len(valores)
            self.duracion = self.longitud/fs
            self.fs = fs
            self.contenido_temporal = self.construir_senal(dominio_temporal, valores)

        else: raise CantidadDeParametrosException("La señal de audio puede recibir únicamente 2 o 3 parámetros")

        self.contenido_frecuencial = None
        self.energia_total = None

    def validar_parametros(self, fs, dominio_temporal, valores):
        if len(dominio_temporal) != len(valores):
            raise ValidacionParametrosSenalException("El dominio y los valores tienen longitudes distintas")
        elif sorted(dominio_temporal) != dominio_temporal:
            raise ValidacionParametrosSenalException("El dominio temporal ingresado no es válido")

        elif self.validar_congruencia_fs_y_dominio_temporal(fs, dominio_temporal) is False:
            raise ValidacionParametrosSenalException("La frecuencia de muestreo y el dominio temporal ingresados son "
                                                     "incongruentes")

    def construir_dominio_temporal(self, fs, longitud):
        dominio_temporal = []
        for t in range(longitud):
            dominio_temporal.append(t / fs)
        return dominio_temporal

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
        return self.contenido_temporal.get_dominio_temporal()

    def get_valores(self):
        return self.contenido_temporal.get_valores()

    def get_dominio_frecuencial(self):
        self.construir_contenido_frecuencial()
        return self.contenido_frecuencial.get_dominio_frecuencial()

    def get_modulos_frecuencia(self):
        self.construir_contenido_frecuencial()
        return self.contenido_frecuencial.get_modulos()

    def get_fases_frecuencia(self):
        self.construir_contenido_frecuencial()
        return self.contenido_frecuencial.get_fase_valores()

    def construir_contenido_frecuencial(self):
        if self.contenido_frecuencial is None:
            from src.core.provider.action_provider import ActionProvider
            accion_transformar = ActionProvider.provide_transformar_fourier_action()
            self.contenido_frecuencial = accion_transformar.execute(self)

    def get_modulo_frecuencia_en(self, f):
        self.construir_contenido_frecuencial()
        muestra_correspondiente = math.floor(f * self.longitud / self.fs)
        return abs(self.contenido_frecuencial.get_muestra(muestra_correspondiente))
    '''
    Se observa en este método que la señal se modela como un valor constante
    entre muestra y muestra, con amplitud igual a la muestra de la izquierda
    de cada intervalo. Es decir, un retenedor de orden cero (ZOH).
    '''
    def get_valor_en(self, t):
        muestra_correspondiente = math.floor(t * self.fs)
        return self.contenido_temporal.get_muestra(muestra_correspondiente)



    '''
    def obtener_t_inmediato_anterior(self, t):
        for k in self.senal_en_tiempo.get_dominio_temporal():
            if (k + 1/self.fs) > t: return k

    def obtener_t_inmediato_siguiente(self, t):
        for k in self.senal_en_tiempo.get_dominio_temporal():
            if (t - 1/self.fs) < k: return k

    '''

    def validar_congruencia_fs_y_dominio_temporal(self, fs, dominio_temporal):
        for t in range(1, len(dominio_temporal)):
            # Tolerancia ajustable
            if not abs((dominio_temporal[t] - dominio_temporal[t - 1]) - (1/fs)) < math.pow(10, -1)/fs:
                return False
        return True

    def get_energia_total(self):
        if self.energia_total is None:
            from src.core.provider.action_provider import ActionProvider
            self.energia_total = ActionProvider.provide_calcular_energia_total_action().execute(self)
        return self.energia_total

    def construir_senal(self, dominio_temporal, valores):
        senal = []
        for i in range(len(valores)):
            senal.append(PuntoSenalTiempo(dominio_temporal[i], valores[i]))
        return ContenidoTemporal(senal)


