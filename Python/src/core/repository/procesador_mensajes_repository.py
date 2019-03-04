from src.core.domain.procesador_mensajes import ProcesadorMensajes


class ProcesadorMensajesRepository:

    procesador_mensajes = None

    def __init__(self):
        self.procesador_mensajes = ProcesadorMensajes()

    def get_procesador_mensajes(self):
        return self.procesador_mensajes
