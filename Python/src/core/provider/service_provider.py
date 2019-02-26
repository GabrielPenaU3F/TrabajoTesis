from src.core.service.estadistica_service import EstadisticaService
from src.core.service.operaciones_sobre_arrays_service import OperacionesSobreArraysService
from src.core.service.operaciones_sobre_senales_service import OperacionesSobreSenalesService


class ServiceProvider:

    estadistica_service = None
    operaciones_sobre_senales_service = None
    operaciones_sobre_arrays_service = None

    @classmethod
    def provide_operaciones_sobre_senales_service(cls):

        if cls.operaciones_sobre_senales_service is None:
            cls.operaciones_sobre_senales_service = OperacionesSobreSenalesService()

        return cls.operaciones_sobre_senales_service

    @classmethod
    def provide_operaciones_sobre_arrays_service(cls):

        if cls.operaciones_sobre_arrays_service is None:
            cls.operaciones_sobre_arrays_service = OperacionesSobreArraysService()

        return cls.operaciones_sobre_arrays_service

    @classmethod
    def provice_estadistica_service(cls):

        if cls.estadistica_service is None:
            cls.estadistica_service = EstadisticaService()

        return cls.estadistica_service
