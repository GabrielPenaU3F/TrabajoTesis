from src.core.domain.archivos.dialogo import Dialogo


class DialogoGuardarMedicion(Dialogo):

    def __init__(self):
        titulo = "Guardar archivo"
        extension_default = ".ram"
        tipos_archivo = self.construir_tipos_archivo()
        super().__init__(titulo, extension_default, tipos_archivo)

    def construir_tipos_archivo(self):
        tipos_archivo = [("Archivos RAM", ".ram"), ("Todos los archivos", ".*")]
        return tipos_archivo
