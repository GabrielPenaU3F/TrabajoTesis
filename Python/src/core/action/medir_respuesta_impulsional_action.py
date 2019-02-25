import math

import numpy

from src.core.domain.generadores_de_senales.generador_ess import GeneradorESS
from src.core.domain.generadores_de_senales.generador_mls import GeneradorMLS
from src.core.domain.lectograbador_de_audio import LectograbadorDeAudio
from src.core.domain.senal_en_tiempo import SenalEnTiempo


class MedirRespuestaImpulsionalAction:

    def __init__(self):
        self.metodos_de_medicion = {
            "MLS": self.medir_por_mls,
            "ESS": self.medir_por_ess
        }
        from src.core.provider.action_provider import ActionProvider
        self.eliminar_latencia_action = ActionProvider.provide_eliminar_latencia_action()
        self.ponderar_periodos_mls_action = ActionProvider.provide_ponderar_periodos_mls_action()
        self.realizar_convolucion_action = ActionProvider.provide_realizar_convolucion_action()
        self.realizar_correlacion_action = ActionProvider.provide_realizar_correlacion_action()

    def execute(self, metodo):
        return self.metodos_de_medicion.get(metodo)()

    def medir_por_mls(self):
        n_bits = 17
        fs = 48000
        periodos = 8

        senal_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs)
        audio = LectograbadorDeAudio().reproducir_y_grabar_audio(senal_mls)

        periodo_mls_generado = senal_mls.get_valores()[0:int(math.pow(2, n_bits) - 1)]
        # Una ventana de 100ms debería bastar
        senal_grabada_sin_latencia = self.eliminar_latencia_action.execute(senal_mls, audio, 0.100)
        senal_grabada_ponderada = self.ponderar_periodos_mls_action.execute(senal_grabada_sin_latencia, n_bits)
        dominio_temporal = numpy.linspace(
            0, len(senal_grabada_ponderada)/fs, len(senal_grabada_ponderada))

        respuesta_impulsional = self.realizar_correlacion_action.execute(
            SenalEnTiempo(dominio_temporal, senal_grabada_ponderada),
            SenalEnTiempo(dominio_temporal, periodo_mls_generado)).get_valores()
        respuesta_impulsional_lineal = respuesta_impulsional[respuesta_impulsional.index(
            max(respuesta_impulsional)):]
        dominio_temporal = numpy.linspace(
            0, len(respuesta_impulsional_lineal)/fs, len(respuesta_impulsional_lineal), endpoint=False)

        return SenalEnTiempo(dominio_temporal, respuesta_impulsional_lineal)

    def medir_por_ess(self):
        fs = 48000
        duracion = 6
        frecuencia_inicial = 20
        frecuencia_final = 22050

        senal_ess = GeneradorESS().generar_senal_ess(fs, duracion, frecuencia_inicial, frecuencia_final)
        audio = LectograbadorDeAudio().reproducir_y_grabar_audio(senal_ess)
        filtro_inverso = GeneradorESS().generar_filtro_inverso_ess(fs, duracion, frecuencia_inicial, frecuencia_final)

        respuesta_impulsional = self.realizar_convolucion_action.execute(audio, filtro_inverso)
        valores = respuesta_impulsional.get_valores()
        valores_lineales = valores[valores.index(max(valores)):]
        dominio_temporal = list(numpy.linspace(0, len(valores_lineales)/fs, len(valores_lineales), endpoint=False))
        return SenalEnTiempo(dominio_temporal, valores_lineales)
