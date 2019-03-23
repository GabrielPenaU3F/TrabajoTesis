from core.provider.service_provider import ServiceProvider


class IntegrarSenalAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal, t_inicio, t_fin):
        return self.operaciones_service.integrar_senal(senal, t_inicio, t_fin)
