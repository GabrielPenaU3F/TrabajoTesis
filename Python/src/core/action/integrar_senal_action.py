from src.core.provider.service_provider import ServiceProvider


class IntegrarSenalAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal, indice_inicio, indice_fin):
        return self.operaciones_service.integrar_senal(senal, indice_inicio, indice_fin)
