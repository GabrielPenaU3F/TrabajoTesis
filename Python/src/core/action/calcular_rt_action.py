from core.provider.service_provider import ServiceProvider


class CalcularRTAction:

    def __init__(self):
        self.rt_service = ServiceProvider.provide_rt_service()

    def execute(self, curva_decaimiento, rt):
        return self.rt_service.calcular_rt(curva_decaimiento, rt)
