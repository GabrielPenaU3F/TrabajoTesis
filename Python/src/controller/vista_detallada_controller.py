from src.core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider
from src.messages.mensaje import Mensaje
from src.view.instrucciones_vista_detallada_view import InstruccionesVistaDetalladaView


class VistaDetalladaController:

    def __init__(self, view):
        self.view = view
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()
        self.vista_detallada_subject = SubjectProvider.provide_vista_detallada_subject()
        self.pantalla_instrucciones_vista_detallada_subject = SubjectProvider.\
            provide_pantalla_instrucciones_vista_detallada_subject()
        self.pantalla_instrucciones_vista_detallada_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje("ActivarBotonVistaDetallada")
        self.vista_detallada_subject.on_next(mensaje_activar_boton)
        self.view.root.withdraw()
        self.view.root.destroy()

    def on_calcular(self):
        pass

    def on_mostrar_instrucciones(self):
        self.desactivar_boton_instrucciones()
        InstruccionesVistaDetalladaView()

    def desactivar_boton_instrucciones(self):
        self.view.desactivar_boton_instrucciones()

    def activar_boton_instrucciones(self):
        self.view.activar_boton_instrucciones()

    def procesar(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()
