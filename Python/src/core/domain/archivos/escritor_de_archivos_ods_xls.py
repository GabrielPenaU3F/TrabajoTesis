from collections import OrderedDict

import pyexcel_ods3

from core.domain.archivos.dialogo_exportar_medicion import DialogoExportarMedicion
from core.domain.archivos.escritor_de_archivos import EscritorDeArchivos
from exception.excepciones import IOException


class EscritorDeArchivosOdsXls(EscritorDeArchivos):

    def guardar_archivo(self, medicion):

        dialogo = DialogoExportarMedicion()
        with self.abrir_dialogo(dialogo) as archivo:
            if archivo:
                ri = medicion.get_respuesta_impulsional()
                cd = medicion.get_curva_decaimiento()
                edt = medicion.get_edt()
                t20 = medicion.get_t20()
                t30 = medicion.get_t30()
                curvatura = medicion.get_curvatura()
                data = OrderedDict()
                hoja_ri = {"Respuesta impulsional": []}

                hoja_ri["Respuesta impulsional"].append(["Datos muestreados a: ", ri.get_fs()])
                hoja_ri["Respuesta impulsional"].append(["", "", ""])
                valores_ri = ri.get_valores()
                for i in range(65000):
                    hoja_ri["Respuesta impulsional"].append([valores_ri[i]])
                data.update(hoja_ri)
                #data.update({"Curva de decaimiento": [["Datos muestreados a: ", cd.get_fs()],
                 #                                     ["", "", ""],
                  #                                    cd.get_valores()]})
                #data.update({"Tiempo de reverberación": []})
                pyexcel_ods3.save_data(archivo, data)

            else:
                raise IOException("No se pudo escribir el archivo")



