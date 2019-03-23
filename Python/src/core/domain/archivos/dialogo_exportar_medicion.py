from core.domain.archivos.dialogo import Dialogo


class DialogoExportarMedicion(Dialogo):

    def __init__(self):
        modo = "wb"
        titulo = "Exportar"
        extension_default = ".xlsx"
        tipos_archivo = self.construir_tipos_archivo()
        super().__init__(modo, titulo, extension_default, tipos_archivo)

    def construir_tipos_archivo(self):
        tipos_archivo = [("Hoja de cálculo de Microsoft Excel", ".xlsx"),
                         ("Hoja de cálculo de OpenDocument", ".ods"),
                         ("Todos los archivos", ".*")]
        return tipos_archivo
