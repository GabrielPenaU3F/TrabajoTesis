from abc import ABC, abstractmethod
from tkinter import filedialog


class EscritorDeArchivos(ABC):

    @abstractmethod
    def guardar_archivo(self, medicion):
        pass

    def abrir_dialogo(self, dialogo):
        return filedialog.asksaveasfile(mode="wb",
                                        title=dialogo.get_titulo(),
                                        defaultextension=dialogo.get_extension_default(),
                                        filetypes=(dialogo.get_tipos_archivo()))
