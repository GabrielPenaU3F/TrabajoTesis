from src.controller.pantalla_con_graficas_controller import PantallaConGraficasController
from src.core.domain.medidor_acustico import MedidorAcustico
from src.core.domain.archivos.escritor_de_archivos_de_medicion import EscritorDeArchivosDeMedicion
from src.core.domain.archivos.lector_de_archivos_de_medicion import LectorDeArchivosDeMedicion
from src.core.provider.queue_provider import QueueProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider
from src.core.domain.mensaje import Mensaje


class MainController(PantallaConGraficasController):

    def __init__(self, view):
        super().__init__(view)
        self.master = "VistaPrincipal"
        self.string_repository = RepositoryProvider.provide_string_repository()
        self.medicion_repository = RepositoryProvider.provide_medicion_repository()
        self.medidor = MedidorAcustico()
        self.pantalla_espera_subject = SubjectProvider.provide_pantalla_espera_subject()
        self.pantalla_instrucciones_subject = SubjectProvider.provide_pantalla_instrucciones_subject()
        self.pantalla_instrucciones_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))
        self.vista_detallada_subject = SubjectProvider.provide_vista_detallada_subject()
        self.vista_detallada_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

    def on_mostrar_instrucciones(self):
        self.desactivar_boton_instrucciones()
        from src.core.domain.coordinador_de_vistas import CoordinadorDeVistas
        CoordinadorDeVistas.mostrar_vista("VistaInstrucciones")

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

    def on_cargar_archivo(self):
        medicion = LectorDeArchivosDeMedicion().cargar_archivo()
        self.medicion_repository.put_medicion(medicion)
        self.mostrar_medicion_en_vista()
        self.desbloquear_controles()

    def on_guardar_archivo(self):
        if self.hay_medicion():
            EscritorDeArchivosDeMedicion().guardar_archivo(self.medicion_repository.get_medicion())

    def lanzar_pantalla_espera(self):
        from src.core.domain.coordinador_de_vistas import CoordinadorDeVistas
        CoordinadorDeVistas().mostrar_vista("VistaPantallaEspera")

    def finalizar_medicion(self, paquete):
        self.unbindear_evento_root("Configure")
        self.medicion_repository.put_medicion(paquete)
        self.mostrar_medicion_en_vista()
        self.restaurar_pantalla_principal()

    def restaurar_pantalla_principal(self):
        mensaje_cerrar_pantalla_espera = Mensaje("VistaPantallaEspera", "CerrarPantallaEspera")
        self.pantalla_espera_subject.on_next(mensaje_cerrar_pantalla_espera)
        self.desbloquear_controles()

    def mostrar_error_lundeby(self):
        self.view.mostrar_error_lundeby(self.string_repository.get_mensaje_error_lundeby())
        self.restaurar_pantalla_principal()

    def desactivar_boton_instrucciones(self):
        self.view.desactivar_boton_instrucciones()

    def activar_boton_instrucciones(self):
        self.view.activar_boton_instrucciones()

    def on_abrir_vista_detallada(self):
        self.desactivar_boton_vista_detallada()
        from src.core.domain.coordinador_de_vistas import CoordinadorDeVistas
        CoordinadorDeVistas.mostrar_vista("VistaDetallada")

    def desactivar_boton_vista_detallada(self):
        self.view.desactivar_boton_vista_detallada()

    def activar_boton_vista_detallada(self):
        self.view.activar_boton_vista_detallada()

    def hay_medicion(self):
        return self.medicion_repository.hay_medicion()

    def on_cerrar_ventana(self):
        quit()





