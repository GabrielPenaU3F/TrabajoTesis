import numpy

from src.core.provider.action_provider import ActionProvider
from src.core.domain.archivos.escritor_de_archivos_de_audio import EscritorDeArchivosDeAudio
from src.core.domain.archivos.lector_de_archivos_de_audio import LectorDeArchivosDeAudio
from src.view.instrucciones_view import InstruccionesView


class MainController:

    def __init__(self, view):
        self.respuesta_impulsional = None
        self.view = view
        self.medir_respuesta_impulsional_action = ActionProvider.provide_medir_respuesta_impulsional_action()

    def on_mostrar_instrucciones(self):
        InstruccionesView()

    def on_efectuar_medicion(self):
        respuesta_impulsional = self.medir_respuesta_impulsional_action.execute(self.view.radiob_metodo_var.get())
        self.respuesta_impulsional = respuesta_impulsional
        self.view.graficar_respuesta_impulsional(
            respuesta_impulsional.get_dominio_temporal(), respuesta_impulsional.get_valores())

    # TODO: Terminar estos dos métodos. Falta definir el formato de los archivos

    def on_cargar_archivo(self):
        archivo = LectorDeArchivosDeAudio().cargar_archivo()

    def on_guardar_archivo(self):
        if self.respuesta_impulsional:
            nombre_archivo = EscritorDeArchivosDeAudio().guardar_archivo()



