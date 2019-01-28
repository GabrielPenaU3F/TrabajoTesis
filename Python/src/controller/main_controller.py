from src.domain.archivos.escritor_de_archivos_de_audio import EscritorDeArchivosDeAudio
from src.domain.archivos.lector_de_archivos_de_audio import LectorDeArchivosDeAudio
from src.view.instrucciones_view import InstruccionesView


class MainController:

    def __init__(self, view):
        self.respuesta_impulsional = None
        self.on_guardar_archivo = None
        self.view = view

    def on_mostrar_instrucciones(self):
        InstruccionesView()

    # TODO: Terminar estos dos métodos. Falta definir el formato de los archivos

    def on_cargar_archivo(self):
        archivo = LectorDeArchivosDeAudio().cargar_archivo()

    def on_guardar_archivo(self):
        if self.respuesta_impulsional:
            nombre_archivo = EscritorDeArchivosDeAudio().guardar_archivo()



