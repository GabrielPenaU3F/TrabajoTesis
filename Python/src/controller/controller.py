from abc import ABC

from src.core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider


class Controller(ABC):

    def __init__(self, view):
        self.view = view
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()

    def on_cerrar_ventana(self):
        self.view.ocultar_vista()

    def procesar(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()

