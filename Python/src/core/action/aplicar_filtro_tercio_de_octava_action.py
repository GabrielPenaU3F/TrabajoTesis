from src.core.domain.filtros.filtro_tercio_octava import FiltroTercioOctava
from src.core.provider.service_provider import ServiceProvider


class AplicarFiltroTercioDeOctavaAction:

    def __init__(self):
        self.filtrado_pasabanda_service = ServiceProvider.provide_filtrado_pasabanda_service()

    def execute(self, senal, frecuencia_central):

        filtro = FiltroTercioOctava(frecuencia_central)
        return filtro.filtrar(senal)
