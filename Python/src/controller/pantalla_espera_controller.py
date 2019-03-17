from src.core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider
from src.core.provider.subject_provider import SubjectProvider


class PantallaEsperaController:

    def __init__(self, view):
        self.view = view
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()
        self.pantalla_espera_subject = SubjectProvider.provide_pantalla_espera_subject()
        self.pantalla_espera_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

    def cerrar(self):
        self.view.ocultar_vista()

    def procesar(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()
