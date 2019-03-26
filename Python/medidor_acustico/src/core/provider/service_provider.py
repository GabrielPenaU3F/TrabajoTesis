from src.core.service.estadistica_service import EstadisticaService
from src.core.service.filtrado_pasabanda_service import FiltradoPasabandaService
from src.core.service.operaciones_sobre_arrays_service import OperacionesSobreArraysService
from src.core.service.operaciones_sobre_senales_service import OperacionesSobreSenalesService
from src.core.service.recortar_senales_service import RecortarSenalesService
from src.core.service.rt_service import RTService


class ServiceProvider:

    filtrado_pasabanda_service = None
    recortar_senales_service = None
    estadistica_service = None
    operaciones_sobre_senales_service = None
    operaciones_sobre_arrays_service = None
    rt_service = None

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
    def provide_estadistica_service(cls):

        if cls.estadistica_service is None:
            cls.estadistica_service = EstadisticaService()

        return cls.estadistica_service

    @classmethod
    def provide_rt_service(cls):

        if cls.rt_service is None:
            cls.rt_service = RTService()

        return cls.rt_service

    @classmethod
    def provide_recortar_senales_service(cls):

        if cls.recortar_senales_service is None:
            cls.recortar_senales_service = RecortarSenalesService()

        return cls.recortar_senales_service

    @classmethod
    def provide_filtrado_pasabanda_service(cls):

        if cls.filtrado_pasabanda_service is None:
            cls.filtrado_pasabanda_service = FiltradoPasabandaService()

        return cls.filtrado_pasabanda_service

