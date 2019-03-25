from controller.pantalla_espera_controller import PantallaEsperaController
from core.provider.subject_provider import SubjectProvider


class PantallaEsperaMedirController(PantallaEsperaController):

    def __init__(self, view):
        super().__init__(view, SubjectProvider.provide_pantalla_espera_medir_subject())
        self.master = "VistaPantallaEsperaMedir"
