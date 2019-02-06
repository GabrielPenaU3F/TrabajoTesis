import numpy

from src.core.provider.action_provider import ActionProvider
from src.domain.archivos.escritor_de_archivos_de_audio import EscritorDeArchivosDeAudio
from src.domain.archivos.lector_de_archivos_de_audio import LectorDeArchivosDeAudio
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
        fs = 44100
        longitud_temporal = len(respuesta_impulsional)/fs
        dominio_temporal = numpy.linspace(0, longitud_temporal, len(respuesta_impulsional), endpoint=False)
        self.view.graficar_respuesta_impulsional(dominio_temporal, respuesta_impulsional)

    # TODO: Terminar estos dos métodos. Falta definir el formato de los archivos

    def on_cargar_archivo(self):
        archivo = LectorDeArchivosDeAudio().cargar_archivo()

    def on_guardar_archivo(self):
        if self.respuesta_impulsional:
            nombre_archivo = EscritorDeArchivosDeAudio().guardar_archivo()



