from controller.controller import Controller
from core.provider.subject_provider import SubjectProvider
from core.domain.mensaje import Mensaje


class InstruccionesController(Controller):

    def __init__(self, view):
        super().__init__(view)
        self.master = "VistaInstrucciones"
        self.pantalla_principal_subject = SubjectProvider.provide_pantalla_principal_subject()

    def on_aceptar(self):
        self.on_cerrar_ventana()

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje(destinatario="VistaPrincipal", mensaje="ActivarBotonInstrucciones")
        self.pantalla_principal_subject.on_next(mensaje_activar_boton)
        self.view.ocultar_vista()
