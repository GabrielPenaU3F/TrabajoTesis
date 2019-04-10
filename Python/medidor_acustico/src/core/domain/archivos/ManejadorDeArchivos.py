from abc import ABC, abstractmethod


class ManejadorDeArchivos(ABC):

    @abstractmethod
    def abrir_dialogo(self, dialogo):
        pass
