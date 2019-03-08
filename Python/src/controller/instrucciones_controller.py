from src.core.provider.subject_provider import SubjectProvider
from src.messages.mensaje import Mensaje


class InstruccionesController:

    def __init__(self, view):
        self.view = view
        self.pantalla_instrucciones_subject = SubjectProvider.provide_pantalla_instrucciones_subject()

    def on_aceptar(self):
        self.on_cerrar_ventana()

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje("ActivarBotonInstrucciones")
        self.pantalla_instrucciones_subject.on_next(mensaje_activar_boton)
        self.view.root.destroy()
