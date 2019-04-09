from abc import abstractmethod
from tkinter import filedialog

from src.core.domain.archivos.ManejadorDeArchivos import ManejadorDeArchivos
from src.exception.excepciones import IOException


class EscritorDeArchivos(ManejadorDeArchivos):

    @abstractmethod
    def guardar_archivo(self, medicion):
        pass

    def abrir_dialogo(self, dialogo):
        archivo = filedialog.asksaveasfile(mode=dialogo.get_modo(),
                                           title=dialogo.get_titulo(),
                                           defaultextension=dialogo.get_extension_default(),
                                           filetypes=(dialogo.get_tipos_archivo()))
        if archivo is None:
            raise IOException("No se pudo escribir el archivo")

        return archivo
