from src.core.domain.archivos.dialogo import Dialogo


class DialogoCargarMedicion(Dialogo):

    def __init__(self):
        modo = "rb"
        titulo = "Seleccionar archivo"
        extension_default = ".ram"
        tipos_archivo = self.construir_tipos_archivo()
        super().__init__(modo, titulo, extension_default, tipos_archivo)

    def construir_tipos_archivo(self):
        tipos_archivo = [("Archivos RAM", ".ram"), ("Todos los archivos", ".*")]
        return tipos_archivo
