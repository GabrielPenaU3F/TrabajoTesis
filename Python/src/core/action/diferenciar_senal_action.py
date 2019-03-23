from core.provider.service_provider import ServiceProvider


class DiferenciarSenalAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal):
        return self.operaciones_service.evaluar_diferencias_finitas_hacia_adelante(senal)
