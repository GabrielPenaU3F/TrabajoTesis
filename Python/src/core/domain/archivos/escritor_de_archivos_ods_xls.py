from collections import OrderedDict
import pyexcel_io
import pyexcel_ods

from src.core.domain.archivos.dialogo_exportar_medicion import DialogoExportarMedicion
from src.core.domain.archivos.escritor_de_archivos import EscritorDeArchivos
from src.exception.excepciones import IOException


class EscritorDeArchivosOdsXls(EscritorDeArchivos):

    def guardar_archivo(self, medicion):

        dialogo = DialogoExportarMedicion()
        with self.abrir_dialogo(dialogo) as archivo:
            if archivo:
                data = OrderedDict()
                data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
                data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
                pyexcel_ods.save_data(archivo, data)

            else:
                raise IOException("No se pudo escribir el archivo")



