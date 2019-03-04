import threading

from src.core.domain.medidor_acustico import MedidorAcustico
from src.core.domain.archivos.escritor_de_archivos_de_audio import EscritorDeArchivosDeAudio
from src.core.domain.archivos.lector_de_archivos_de_audio import LectorDeArchivosDeAudio
from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider
from src.exception.excepciones import LundebyException
from src.messages.mensaje import Mensaje
from src.view.instrucciones_view import InstruccionesView
from src.view.pantalla_espera_view import PantallaEsperaView


class MainController:

    def __init__(self, view):
        self.string_repository = RepositoryProvider.provide_string_repository()
        self.medicion = None
        self.pantalla_espera = None
        self.view = view
        self.medidor = MedidorAcustico()
        self.thread_queue = RepositoryProvider.provide_queue_repository().get_queue_general()
        self.thread_medicion = threading.Thread()
        self.procesador_mensajes = RepositoryProvider.provide_procesador_mensajes_repository().get_procesador_mensajes()
        self.cierre_pantalla_espera_subject = SubjectProvider.provide_cierre_pantalla_espera_subject()

    def on_mostrar_instrucciones(self):
        InstruccionesView()

    def on_efectuar_medicion(self):

        metodo_medicion = self.view.radiob_metodo_var.get()

        try:
            self.medidor.medir(metodo_medicion)
            self.bloquear_controles()
            self.lanzar_pantalla_espera()
        except Exception:
            self.view.mostrar_error_lundeby(self.string_repository.get_mensaje_error_lundeby())

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
            mensaje = self.thread_queue.get()
            metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
            metodo_a_ejecutar(mensaje)

    def lanzar_pantalla_espera(self):
        PantallaEsperaView()

    def finalizar_medicion(self, mensaje):
        self.medicion = mensaje.get_contenido()
        self.mostrar_medicion_en_vista()
        self.thread_queue.task_done()
        mensaje_cerrar_pantalla_espera = Mensaje("CerrarPantallaEspera")
        self.cierre_pantalla_espera_subject.on_next(mensaje_cerrar_pantalla_espera)
        self.desbloquear_controles()

    def bloquear_controles(self):
        self.view.bloquear_controles()

    def desbloquear_controles(self):
        self.view.desbloquear_controles()





