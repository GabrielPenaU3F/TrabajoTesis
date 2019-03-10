from src.core.repository.bandas_estandar_repository import BandasEstandarRepository
from src.core.repository.medicion_repository import MedicionRepository
from src.core.repository.procesador_mensajes_repository import ProcesadorMensajesRepository
from src.core.repository.queue_repository import QueueRepository
from src.core.repository.string_repository import StringRepository


class RepositoryProvider:

    medicion_repository = None
    string_repository = None
    queue_repository = None
    procesador_mensajes_repository = None
    bandas_estandar_repository = None

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

    @classmethod
    def provide_bandas_estandar_repository(cls):
        if cls.bandas_estandar_repository is None:
            cls.bandas_estandar_repository = BandasEstandarRepository()

        return cls.bandas_estandar_repository

    @classmethod
    def provide_medicion_repository(cls):
        if cls.medicion_repository is None:
            cls.medicion_repository = MedicionRepository()

        return cls.medicion_repository

