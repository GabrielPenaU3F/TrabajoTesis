from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider


class PantallaEsperaController:

    def __init__(self, view):
        self.view = view
        self.procesador_mensajes = RepositoryProvider.provide_procesador_mensajes_repository().get_procesador_mensajes()
        self.cierre_pantalla_espera_subject = SubjectProvider.provide_cierre_pantalla_espera_subject()
        self.cierre_pantalla_espera_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

    def cerrar(self):
        self.view.cerrar()

    def procesar(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()
