from controller.controller import Controller
from core.provider.subject_provider import SubjectProvider


class PantallaEsperaController(Controller):

    def __init__(self, view):
        super().__init__(view)
        self.master = "VistaPantallaEspera"
        self.pantalla_espera_subject = SubjectProvider.provide_pantalla_espera_subject()
        self.pantalla_espera_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

