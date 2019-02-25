from src.core.provider.service_provider import ServiceProvider


class RealizarCorrelacionAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal_1, senal_2):
        return self.operaciones_service.realizar_correlacion(senal_1, senal_2)
