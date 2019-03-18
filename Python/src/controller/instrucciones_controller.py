from src.controller.controller import Controller
from src.core.provider.subject_provider import SubjectProvider
from src.messages.mensaje import Mensaje


class InstruccionesController(Controller):

    def __init__(self, view):
        super().__init__(view)
        self.pantalla_instrucciones_subject = SubjectProvider.provide_pantalla_instrucciones_subject()

    def on_aceptar(self):
        self.on_cerrar_ventana()

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje("ActivarBotonInstrucciones")
        self.pantalla_instrucciones_subject.on_next(mensaje_activar_boton)
        self.view.ocultar_vista()
