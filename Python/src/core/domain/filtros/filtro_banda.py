from abc import ABC

from src.core.provider.repository_provider import RepositoryProvider


class FiltroBanda(ABC):

    def __init__(self):
        from src.core.provider.action_provider import ActionProvider
        self.aplicar_filtro_pasabanda_action = ActionProvider.provide_aplicar_filtro_pasabanda_action()
        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()
        self.banda = None

    def get_banda(self):
        return self.banda
