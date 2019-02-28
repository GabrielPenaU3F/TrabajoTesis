from src.core.provider.service_provider import ServiceProvider


class EliminarSegmentoInicialConstanteAction:

    def __init__(self):
        self.operaciones_service = ServiceProvider.provide_operaciones_sobre_senales_service()

    '''
    def execute(self, senal_en_tiempo, tolerancia):
        valores_senal_derivada = self.operaciones_service.evaluar_diferencias_finitas_hacia_adelante(senal_en_tiempo).get_valores()
        nuevo_dominio = senal_en_tiempo.get_dominio_temporal().copy()
        nuevos_valores = senal_en_tiempo.get_valores().copy()
        for i in range(len(valores_senal_derivada)):
            if abs(valores_senal_derivada[i]) < tolerancia:
                nuevo_dominio.pop(0)
                nuevos_valores.pop(0)
            else: break
        return SenalEnTiempo(nuevo_dominio, nuevos_valores)
    '''
