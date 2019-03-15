import sys

from src.core.domain.medidor_acustico import MedidorAcustico
from src.core.domain.archivos.escritor_de_archivos_de_audio import EscritorDeArchivosDeAudio
from src.core.domain.archivos.lector_de_archivos_de_audio import LectorDeArchivosDeAudio
from src.core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider
from src.core.provider.queue_provider import QueueProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider
from src.messages.mensaje import Mensaje
from src.view.instrucciones_view import InstruccionesView
from src.view.pantalla_espera_view import PantallaEsperaView
from src.view.vista_detallada.vista_detallada_view import VistaDetalladaView


class MainController:

    def __init__(self, view):
        self.string_repository = RepositoryProvider.provide_string_repository()
        self.medicion_repository = RepositoryProvider.provide_medicion_repository()
        self.pantalla_espera = None
        self.view = view
        self.medidor = MedidorAcustico()
        self.main_queue = QueueProvider.provide_main_queue()
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()
        self.pantalla_espera_subject = SubjectProvider.provide_pantalla_espera_subject()
        self.pantalla_instrucciones_subject = SubjectProvider.provide_pantalla_instrucciones_subject()
        self.pantalla_instrucciones_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))
        self.vista_detallada_subject = SubjectProvider.provide_vista_detallada_subject()
        self.vista_detallada_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

    def on_mostrar_instrucciones(self):
        self.desactivar_boton_instrucciones()
        InstruccionesView()

    def on_efectuar_medicion(self):

        metodo_medicion = self.view.radiob_metodo_var.get()
        self.medidor.medir(metodo_medicion)
        self.bloquear_controles()
        self.lanzar_pantalla_espera()

    def mostrar_medicion_en_vista(self):

        medicion = self.medicion_repository.get_medicion()
        self.view.graficar_respuesta_impulsional(
            medicion.get_respuesta_impulsional().get_dominio_temporal(),
            medicion.get_respuesta_impulsional().get_valores())

        self.view.graficar_curva_decaimiento(
            medicion.get_curva_decaimiento().get_dominio_temporal(),
            medicion.get_curva_decaimiento().get_valores())

        self.view.mostrar_tiempos_de_reverberacion(
            medicion.get_edt().get_rt(), medicion.get_t20().get_rt(), medicion.get_t30().get_rt())

    # TODO: Terminar estos dos métodos. Falta definir el formato de los archivos

    def on_cargar_archivo(self):
        archivo = LectorDeArchivosDeAudio().cargar_archivo()

    def on_guardar_archivo(self):
        if self.hay_medicion():
            nombre_archivo = EscritorDeArchivosDeAudio().guardar_archivo()

    def actualizar(self):
        if not self.main_queue.empty():
            mensaje = self.main_queue.get()
            metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
            metodo_a_ejecutar(mensaje)

    def lanzar_pantalla_espera(self):
        PantallaEsperaView()

    def finalizar_medicion(self, mensaje):
        self.medicion_repository.put_medicion(mensaje.get_contenido())
        self.mostrar_medicion_en_vista()
        self.main_queue.task_done()
        self.restaurar_pantalla_principal()

    def restaurar_pantalla_principal(self):
        mensaje_cerrar_pantalla_espera = Mensaje("CerrarPantallaEspera")
        self.pantalla_espera_subject.on_next(mensaje_cerrar_pantalla_espera)
        self.desbloquear_controles()

    def mostrar_error_lundeby(self, mensaje):
        self.view.mostrar_error_lundeby(self.string_repository.get_mensaje_error_lundeby())
        self.main_queue.task_done()
        self.restaurar_pantalla_principal()

    def bloquear_controles(self):
        self.view.bloquear_controles()

    def desbloquear_controles(self):
        self.view.desbloquear_controles()

    def desactivar_boton_instrucciones(self):
        self.view.desactivar_boton_instrucciones()

    def activar_boton_instrucciones(self):
        self.view.activar_boton_instrucciones()

    def procesar(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()

    def on_abrir_vista_detallada(self):
        self.desactivar_boton_vista_detallada()
        VistaDetalladaView()

    def desactivar_boton_vista_detallada(self):
        self.view.desactivar_boton_vista_detallada()

    def activar_boton_vista_detallada(self):
        self.view.activar_boton_vista_detallada()

    def hay_medicion(self):
        return self.medicion_repository.hay_medicion()

    def on_cerrar_ventana(self):
        quit()





