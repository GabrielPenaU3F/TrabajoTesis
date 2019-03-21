class ProcesadorMensajes:

    def __init__(self):
        self.mensajes = {
            "MedicionCompleta": "finalizar_medicion",
            "CerrarPantallaEspera": "on_cerrar_ventana",
            "LundebyException": "mostrar_error_lundeby",
            "ActivarBotonInstrucciones": "activar_boton_instrucciones",
            "ActivarBotonVistaDetallada": "activar_boton_vista_detallada",
            "CalculoCompleto": "finalizar_calculo",
            "CargaCompleta": "desplegar_medicion",
            "DispositivoInaccesible": "mostrar_error_dispositivo_inaccesible"
        }

    def get_mensaje(self, clave_mensaje):
        return self.mensajes.get(clave_mensaje)
