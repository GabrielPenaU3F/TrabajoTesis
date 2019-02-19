import math

import numpy

from src.domain.generadores_de_senales.generador_mls import GeneradorMLS
from src.domain.lectograbador_de_audio import LectograbadorDeAudio


class MedirRespuestaImpulsionalAction:

    def __init__(self):
        self.metodos_de_medicion = {
            "MLS": self.medir_por_mls,
            "ESS": self.medir_por_ess
        }
        from src.core.provider.action_provider import ActionProvider
        self.eliminar_latencia_action = ActionProvider.provide_eliminar_latencia_action()
        self.ponderar_periodos_mls_action = ActionProvider.provide_ponderar_periodos_mls_action()

    def execute(self, metodo):
        return self.metodos_de_medicion.get(metodo)()

    def medir_por_mls(self):
        n_bits = 17
        fs = 48000
        periodos = 8
        # Estos parámetros podrían eventualmente modificarse
        senal_mls = GeneradorMLS().generar_senal_mls(n_bits, periodos, fs)
        audio = LectograbadorDeAudio().reproducir_y_grabar_audio(senal_mls)

        periodo_mls_generado = senal_mls.get_valores()[0:int(math.pow(2, n_bits) - 1)]
        # Una ventana de 100ms debería bastar
        senal_grabada_sin_latencia = self.eliminar_latencia_action.execute(senal_mls, audio, 0.100)
        senal_grabada_ponderada = self.ponderar_periodos_mls_action.execute(senal_grabada_sin_latencia, n_bits)

        respuesta_impulsional = list(numpy.correlate(periodo_mls_generado, senal_grabada_ponderada, "full"))
        return respuesta_impulsional

    # TODO: Implementar metodo ESS
    def medir_por_ess(self):
        pass
