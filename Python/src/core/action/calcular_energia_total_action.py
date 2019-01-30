import math

from src.core.provider.service_provider import ServiceProvider


class CalcularEnergiaTotalAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal_en_tiempo):
        return self.operaciones_service.calcular_energia_total_de_senal(senal_en_tiempo)
