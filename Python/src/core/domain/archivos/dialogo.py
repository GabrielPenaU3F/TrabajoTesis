from abc import ABC, abstractmethod


class Dialogo(ABC):

    def __init__(self, modo, titulo, extension_default, tipos_archivo):
        self.modo = modo
        self.titulo = titulo
        self.extension_default = extension_default
        self.tipos_archivo = tipos_archivo

    @abstractmethod
    def construir_tipos_archivo(self):
        pass

    def get_titulo(self):
        return self.titulo

    def get_extension_default(self):
        return self.extension_default

    def get_tipos_archivo(self):
        return self.tipos_archivo

    def get_modo(self):
        return self.modo
