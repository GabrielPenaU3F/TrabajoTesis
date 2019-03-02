import queue
import threading
from concurrent.futures.thread import ThreadPoolExecutor

from src.core.domain.medicion import Medicion
from src.core.provider.action_provider import ActionProvider
from src.core.domain.archivos.escritor_de_archivos_de_audio import EscritorDeArchivosDeAudio
from src.core.domain.archivos.lector_de_archivos_de_audio import LectorDeArchivosDeAudio
from src.core.provider.repository_provider import RepositoryProvider
from src.exception.excepciones import LundebyException
from src.view.instrucciones_view import InstruccionesView


class MainController:

    def __init__(self, view):
        self.medicion = None
        self.view = view
        self.string_repository = RepositoryProvider.provide_string_repository()
        self.medir_respuesta_impulsional_action = ActionProvider.provide_medir_respuesta_impulsional_action()
        self.obtener_curva_decaimiento_action = ActionProvider.provide_obtener_curva_de_decaimiento_action()
        self.calcular_rt_action = ActionProvider.provide_calcular_rt_action()
        self.thread_queue = queue.Queue()
        self.thread_medicion = threading.Thread()

    def on_mostrar_instrucciones(self):
        InstruccionesView()

    def on_efectuar_medicion(self):

        metodo_medicion = self.view.radiob_metodo_var.get()
        try:
            #self.mylabel.config(text='Running loop')
            self.thread_medicion = threading.Thread(target=self.medir, args=(metodo_medicion,))
            self.thread_medicion.start()

        except LundebyException:
            self.view.mostrar_error_lundeby(self.string_repository.get_mensaje_error_lundeby())

    def medir(self, metodo):

        fs = 48000

        respuesta_impulsional = self.medir_respuesta_impulsional_action.execute(metodo, fs)
        curva_decaimiento = self.obtener_curva_decaimiento_action.execute(respuesta_impulsional, fs)
        edt = self.calcular_rt_action.execute(curva_decaimiento, rt='EDT')
        t20 = self.calcular_rt_action.execute(curva_decaimiento, rt='T20')
        t30 = self.calcular_rt_action.execute(curva_decaimiento, rt='T30')

        self.thread_queue.put(Medicion(respuesta_impulsional, curva_decaimiento, edt, t20, t30))

    def mostrar_medicion_en_vista(self):

        self.view.graficar_respuesta_impulsional(
            self.medicion.get_respuesta_impulsional().get_dominio_temporal(),
            self.medicion.get_respuesta_impulsional().get_valores())

        self.view.graficar_curva_decaimiento(
            self.medicion.get_curva_decaimiento().get_dominio_temporal(),
            self.medicion.get_curva_decaimiento().get_valores())

        self.view.mostrar_tiempos_de_reverberacion(
            self.medicion.get_edt(), self.medicion.get_t20(), self.medicion.get_t30())

    # TODO: Terminar estos dos métodos. Falta definir el formato de los archivos

    def on_cargar_archivo(self):
        archivo = LectorDeArchivosDeAudio().cargar_archivo()

    def on_guardar_archivo(self):
        if self.medicion:
            nombre_archivo = EscritorDeArchivosDeAudio().guardar_archivo()

    def actualizar(self):
        if not self.thread_queue.empty():
            self.medicion = self.thread_queue.get()
            self.mostrar_medicion_en_vista()





