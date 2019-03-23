from abc import ABC
from core.provider.repository_provider import RepositoryProvider
from core.provider.service_provider import ServiceProvider


class FiltroBanda(ABC):

    def __init__(self):
        self.filtrado_pasabanda_service = ServiceProvider.provide_filtrado_pasabanda_service()
        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()
        self.banda = None
        # Estos parámetros podrían, eventualmente, ser modificables por el usuario
        self.output = 'sos'
        self.tipo = 'Cheby2'

    def get_banda(self):
        return self.banda

    def filtrar(self, senal):
        return self.filtrado_pasabanda_service.aplicar_filtro_pasabanda(senal, self.tipo, self.output, self.banda)

