from src.core.domain.procesador_mensajes import ProcesadorMensajes


class ProcesadorMensajesProvider:

    procesador_mensajes = None

    @classmethod
    def provide_procesador_mensajes(cls):

        if cls.procesador_mensajes is None:
            cls.procesador_mensajes = ProcesadorMensajes()

        return cls.procesador_mensajes
