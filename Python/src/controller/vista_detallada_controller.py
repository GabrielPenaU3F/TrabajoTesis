from src.core.provider.subject_provider import SubjectProvider
from src.messages.mensaje import Mensaje


class VistaDetalladaController:

    def __init__(self, view):
        self.view = view
        self.vista_detallada_subject = SubjectProvider.provide_vista_detallada_subject()

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje("ActivarBotonVistaDetallada")
        self.vista_detallada_subject.on_next(mensaje_activar_boton)
        self.view.root.destroy()

    def on_calcular(self):
        pass

    def on_mostrar_instrucciones(self):
        pass
