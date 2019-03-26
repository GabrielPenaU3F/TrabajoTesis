from src.core.domain.filtros.filtro_octava import FiltroOctava
from src.core.provider.service_provider import ServiceProvider


class AplicarFiltroOctavaAction:

    def __init__(self):
        self.filtrado_pasabanda_service = ServiceProvider.provide_filtrado_pasabanda_service()

    def execute(self, senal, frecuencia_central):

        filtro = FiltroOctava(frecuencia_central)
        return filtro.filtrar(senal)
