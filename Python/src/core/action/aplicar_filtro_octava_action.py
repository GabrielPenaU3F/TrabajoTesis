from src.core.domain.filtros.filtro_octava import FiltroOctava


class AplicarFiltroOctavaAction:

    def __init__(self):
        from src.core.provider.action_provider import ActionProvider
        self.aplicar_filtro_pasabanda_action = ActionProvider.provide_aplicar_filtro_pasabanda_action()

    def execute(self, senal, frecuencia_central):

        filtro = FiltroOctava(frecuencia_central)
        return self.aplicar_filtro_pasabanda_action.execute(senal, filtro.get_banda())
