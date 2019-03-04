from src.core.repository.procesador_mensajes_repository import ProcesadorMensajesRepository
from src.core.repository.queue_repository import QueueRepository
from src.core.repository.string_repository import StringRepository


class RepositoryProvider:

    string_repository = None
    queue_repository = None
    procesador_mensajes_repository = None

    @classmethod
    def provide_string_repository(cls):

        if cls.string_repository is None:
            cls.string_repository = StringRepository()

        return cls.string_repository

    @classmethod
    def provide_queue_repository(cls):

        if cls.queue_repository is None:
            cls.queue_repository = QueueRepository()

        return cls.queue_repository

    @classmethod
    def provide_procesador_mensajes_repository(cls):

        if cls.procesador_mensajes_repository is None:
            cls.procesador_mensajes_repository = ProcesadorMensajesRepository()

        return cls.procesador_mensajes_repository

