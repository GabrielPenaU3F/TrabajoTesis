from src.core.domain.senal_en_tiempo import SenalEnTiempo


class RecortarSegmentoDeSenalEnTiempoAction:

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
    def execute(self, senal_en_tiempo, tiempo_inicio, tiempo_final):
        dominio_temporal = senal_en_tiempo.get_dominio_temporal()
        nuevo_dominio = []
        nuevos_valores = []
        for t in dominio_temporal:
            if not (t < tiempo_inicio or t > tiempo_final):
                nuevo_dominio.append(t)
                nuevos_valores.append(senal_en_tiempo.get_valor_en(t))

        return SenalEnTiempo(nuevo_dominio, nuevos_valores)

