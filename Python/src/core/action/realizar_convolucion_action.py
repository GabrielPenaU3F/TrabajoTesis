import numpy

from src.core.domain.senal_en_tiempo import SenalEnTiempo
from src.core.provider.service_provider import ServiceProvider
from scipy import signal

class RealizarConvolucionAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    def execute(self, senal_1, senal_2):
        return self.operaciones_service.realizar_convolucion(senal_1, senal_2)
