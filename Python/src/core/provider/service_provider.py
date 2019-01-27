from src.core.service.operaciones_sobre_senales_service import OperacionesSobreSenalesService


class ServiceProvider:

    operaciones_sobre_senales_service = None

    @classmethod
    def provide_operaciones_sobre_senales_service(cls):

        if cls.operaciones_sobre_senales_service is None:
            cls.operaciones_sobre_senales_service = OperacionesSobreSenalesService()

        return cls.operaciones_sobre_senales_service
