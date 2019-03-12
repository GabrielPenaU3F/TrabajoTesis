import threading

from src.core.domain.medicion import Medicion
from src.core.provider.action_provider import ActionProvider
from src.core.provider.queue_provider import QueueProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.exception.excepciones import LundebyException
from src.messages.mensaje import Mensaje


class MedidorAcustico:

    def __init__(self):
        self.main_queue = QueueProvider.provide_main_queue()
        self.vista_detallada_queue = QueueProvider.provide_vista_detallada_queue()
        self.medir_respuesta_impulsional_action = ActionProvider.provide_medir_respuesta_impulsional_action()
        self.obtener_curva_decaimiento_action = ActionProvider.provide_obtener_curva_de_decaimiento_action()
        self.calcular_rt_action = ActionProvider.provide_calcular_rt_action()
        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()
        self.aplicar_filtro_octava_action = ActionProvider.provide_aplicar_filtro_octava_action()
        self.aplicar_filtro_tercio_octava_action = ActionProvider.provide_aplicar_filtro_tercio_de_octava_action()

    def medir(self, metodo):

        thread_medicion = threading.Thread(target=self.efectuar_medicion, args=(metodo,))
        thread_medicion.start()

    def efectuar_medicion(self, metodo):

        fs = 48000
        respuesta_impulsional = self.medir_respuesta_impulsional_action.execute(metodo, fs)
        try:
            medicion = self.obtener_medicion_completa(respuesta_impulsional, fs)
            mensaje = Mensaje("MedicionCompleta", medicion)
            self.main_queue.put(mensaje)
            return None
        except LundebyException:
            mensaje = Mensaje("LundebyException")
            self.main_queue.put(mensaje)
            return None

    def efectuar_calculo(self, respuesta_impulsional, fs):
        try:
            medicion = self.obtener_medicion_completa(respuesta_impulsional, fs)
            mensaje = Mensaje("CalculoCompleto", medicion)
            self.vista_detallada_queue.put(mensaje)
            return None
        except LundebyException:
            mensaje = Mensaje("LundebyException")
            self.vista_detallada_queue.put(mensaje)
            return None

    def obtener_medicion_completa(self, respuesta_impulsional, fs):
        curva_decaimiento = self.obtener_curva_decaimiento_action.execute(respuesta_impulsional, fs)
        edt = self.calcular_rt_action.execute(curva_decaimiento, rt='EDT')
        t20 = self.calcular_rt_action.execute(curva_decaimiento, rt='T20')
        t30 = self.calcular_rt_action.execute(curva_decaimiento, rt='T30')
        return Medicion(respuesta_impulsional, curva_decaimiento, edt, t20, t30)

    def calcular_parametros_acusticos(self, respuesta_impulsional, fs):
        thread_calculo = threading.Thread(target=self.efectuar_calculo, args=(respuesta_impulsional, fs))
        thread_calculo.start()

    def obtener_medicion_en_octava(self, medicion, f_central):
        respuesta_impulsional_filtrada = self.aplicar_filtro_octava_action.execute(
            medicion.get_respuesta_impulsional(), f_central)
        self.calcular_parametros_acusticos(respuesta_impulsional_filtrada, respuesta_impulsional_filtrada.get_fs())

    def obtener_medicion_en_tercio_octava(self, medicion, f_central):
        respuesta_impulsional_filtrada = self.aplicar_filtro_tercio_octava_action.execute(
            medicion.get_respuesta_impulsional(), f_central)
        self.calcular_parametros_acusticos(respuesta_impulsional_filtrada, respuesta_impulsional_filtrada.get_fs())
