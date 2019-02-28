from src.core.provider.service_provider import ServiceProvider
from src.core.domain.senal_audio import SenalAudio
from src.exception.excepciones import AlineacionException


class EliminarLatenciaAction:

    def __init__(self):
        self.operaciones_sobre_senales_service = ServiceProvider.provide_operaciones_sobre_senales_service()
        self.operaciones_sobre_arrays_service = ServiceProvider.provide_operaciones_sobre_arrays_service()

    def execute(self, *args):
        senal_de_referencia = args[0]
        senal_con_latencia = args[1]
        fs = senal_de_referencia.get_fs()
        if len(args) == 2:
            ventana_en_segundos = self.operaciones_sobre_arrays_service.obtener_longitud_del_array_mas_corto(
                senal_de_referencia.get_valores(), senal_con_latencia.get_valores()) * (1/fs)
        elif len(args) == 3:
            ventana_en_segundos = args[2]
        else: raise AlineacionException("El método de eliminar latencia solo puede recibir dos o tres parámetros")

        return self.operaciones_sobre_senales_service.eliminar_latencia_entre_senales(
            senal_de_referencia, senal_con_latencia, ventana_en_segundos)
