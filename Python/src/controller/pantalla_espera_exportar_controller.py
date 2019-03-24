from controller.controller import Controller
from core.provider.subject_provider import SubjectProvider


class PantallaEsperaExportarController(Controller):

    def __init__(self, view):
        super().__init__(view)
        self.master = "VistaPantallaEsperaExportar"
        self.pantalla_espera_exportar_subject = SubjectProvider.provide_pantalla_espera_exportar_subject()
        self.pantalla_espera_exportar_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))
