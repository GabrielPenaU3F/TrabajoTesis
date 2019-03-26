from src.core.repository.bandas_estandar_repository import BandasEstandarRepository
from src.core.repository.binding_eventos_repository import BindingEventosRepository
from src.core.repository.medicion_repository import MedicionRepository
from src.core.repository.string_repository import StringRepository


class RepositoryProvider:

    binding_eventos_repository = None
    medicion_repository = None
    string_repository = None
    bandas_estandar_repository = None

    @classmethod
    def provide_string_repository(cls):

        if cls.string_repository is None:
            cls.string_repository = StringRepository()

        return cls.string_repository

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

    @classmethod
    def provide_binding_eventos_repository(cls):
        if cls.binding_eventos_repository is None:
            cls.binding_eventos_repository = BindingEventosRepository()

        return cls.binding_eventos_repository

