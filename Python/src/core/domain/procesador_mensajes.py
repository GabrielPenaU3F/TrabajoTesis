class ProcesadorMensajes:

    def __init__(self):
        self.mensajes = {
            "MedicionCompleta": "finalizar_medicion",
            "CerrarPantallaEspera": "cerrar"
        }

    def get_mensaje(self, clave_mensaje):
        return self.mensajes.get(clave_mensaje)
