from core.provider.service_provider import ServiceProvider


class RecortarSegmentoDeSenalEntreAmplitudesAction:

    def __init__(self):
        self.recortar_service = ServiceProvider.provide_recortar_senales_service()

    def execute(self, senal, a_inf, a_sup):
        return self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(senal, a_inf, a_sup)

