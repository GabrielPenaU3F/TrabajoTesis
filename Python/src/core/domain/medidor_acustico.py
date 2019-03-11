import threading

from src.core.domain.medicion import Medicion
from src.core.provider.action_provider import ActionProvider
from src.core.provider.queue_provider import QueueProvider
from src.exception.excepciones import LundebyException
from src.messages.mensaje import Mensaje


class MedidorAcustico:

    def __init__(self):
        self.thread_queue = QueueProvider.provide_queue_general()
        self.medir_respuesta_impulsional_action = ActionProvider.provide_medir_respuesta_impulsional_action()
        self.obtener_curva_decaimiento_action = ActionProvider.provide_obtener_curva_de_decaimiento_action()
        self.calcular_rt_action = ActionProvider.provide_calcular_rt_action()

    def medir(self, metodo):

        thread_medicion = threading.Thread(target=self.ejecutar_thread_medicion, args=(metodo,))
        thread_medicion.start()

    def ejecutar_thread_medicion(self, metodo):

        try:
            fs = 48000
            respuesta_impulsional = self.medir_respuesta_impulsional_action.execute(metodo, fs)
            curva_decaimiento = self.obtener_curva_decaimiento_action.execute(respuesta_impulsional, fs)
            edt = self.calcular_rt_action.execute(curva_decaimiento, rt='EDT')
            t20 = self.calcular_rt_action.execute(curva_decaimiento, rt='T20')
            t30 = self.calcular_rt_action.execute(curva_decaimiento, rt='T30')

            medicion = Medicion(respuesta_impulsional, curva_decaimiento, edt, t20, t30)

            mensaje = Mensaje("MedicionCompleta", medicion)
            self.thread_queue.put(mensaje)
            return None
        except LundebyException:
            mensaje = Mensaje("LundebyException")
            self.thread_queue.put(mensaje)
            return None
