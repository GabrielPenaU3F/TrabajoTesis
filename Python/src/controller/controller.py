from abc import ABC

from src.core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider


class Controller(ABC):

    def __init__(self, view):
        self.master = None
        self.view = view
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()

    def on_cerrar_ventana(self):
        self.view.ocultar_vista()

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



