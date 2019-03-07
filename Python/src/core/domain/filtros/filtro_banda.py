from abc import ABC, abstractmethod


class FiltroBanda(ABC):

    def __init__(self):
        from src.core.provider.action_provider import ActionProvider
        self.aplicar_filtro_pasabanda_action = ActionProvider.provide_aplicar_filtro_pasabanda_action()
        self.frecuencias_centrales = []
        self.banda = None

    @abstractmethod
    def construir_banda(self, f_central):
        pass
