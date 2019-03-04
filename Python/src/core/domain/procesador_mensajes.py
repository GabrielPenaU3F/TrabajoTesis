class ProcesadorMensajes:

    def __init__(self):
        self.mensajes = {
            "MedicionCompleta": "finalizar_medicion",
            "CerrarPantallaEspera": "cerrar",
            "LundebyException": "mostrar_error_lundeby"
        }

    def get_mensaje(self, clave_mensaje):
        return self.mensajes.get(clave_mensaje)
