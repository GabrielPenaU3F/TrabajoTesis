from abc import ABC

from core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider
from core.provider.queue_provider import QueueProvider


class Controller(ABC):

    def __init__(self, view):
        self.master = None
        self.view = view
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()
        self.queue = QueueProvider.provide_thread_queue()

    def on_cerrar_ventana(self):
        self.view.ocultar_vista()

    def revisar_queue(self):

        if not self.queue.empty():

            mensaje = self.queue.get()
            if mensaje.get_destinatario() == self.master:
                self.procesar(mensaje)
                self.queue.task_done()
            else:
                self.queue.put(mensaje)

    def procesar(self, mensaje):

        if mensaje.get_destinatario() == self.master:

            if mensaje.get_paquete() is not None:
                self.procesar_mensaje_paquete(mensaje)
            else:
                self.procesar_mensaje_simple(mensaje)

    def procesar_mensaje_simple(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()

    def procesar_mensaje_paquete(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar(mensaje.get_paquete())

    def get_master(self):
        return self.master



