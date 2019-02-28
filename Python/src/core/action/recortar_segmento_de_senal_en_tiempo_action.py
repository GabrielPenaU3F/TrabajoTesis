from src.core.provider.service_provider import ServiceProvider


class RecortarSegmentoDeSenalEnTiempoAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    '''
    Existe siempre la posibilidad de que los tiempos elegidos para recortar
    no coincidan exactamente con las muestras, ya que la señal es discreta.
    Esta función siempre achicará para adentro, es decir, recortará desde
    los dos tiempos muestreados más cercanos a los solicitados que se encuentren
    dentro del intervalo considerado. Esto ocasionará que se pierda información.
    Con una frecuencia de muestreo mayor, menos información se perderá. Con los
    48000Hz estándar de procesamiento de audio, perder 1/48000 de información
    temporal es prácticamente insignificante.
    '''
    def execute(self, senal, t_inicio, t_final):
        return self.operaciones_service.recortar_en_tiempo(senal, t_inicio, t_final)

