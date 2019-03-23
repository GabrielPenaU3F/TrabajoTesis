import traceback
from tkinter import filedialog

from core.domain.archivos.dialogo_guardar_medicion import DialogoGuardarMedicion
from core.domain.archivos.escritor_de_archivos import EscritorDeArchivos
from exception.excepciones import IOException


class EscritorDeArchivosDeMedicion(EscritorDeArchivos):

    def guardar_archivo(self, medicion):
        dialogo = DialogoGuardarMedicion()
        with self.abrir_dialogo(dialogo) as archivo:

            if archivo:
                string_archivo = self.formatear_medicion(medicion)
                archivo.write(string_archivo.encode('cp037'))  # IBM037 codec

            else:
                raise IOException("No se pudo escribir el archivo")

    def string_valor(self, valor):
        return "$" + str(valor)

    def string_lista_valores(self, valores):
        string_ri = "$"
        for i in range(len(valores)):
            string_ri += str(valores[i]) + ","
        string_ri = string_ri[:-1]
        return string_ri

    def string_rt(self, rt):
        string_rt = "$"
        string_rt += str(rt.get_rt()) + ","
        string_rt += str(rt.get_coef_correlacion()) + ","
        string_rt += str(rt.get_xi())
        return string_rt

    def formatear_medicion(self, medicion):
        ri = medicion.get_respuesta_impulsional()
        cd = medicion.get_curva_decaimiento()
        string_archivo = ""
        string_archivo += self.string_valor(ri.get_fs())
        string_archivo += self.string_lista_valores(ri.get_valores())
        string_archivo += self.string_lista_valores(cd.get_valores())
        string_archivo += self.string_rt(medicion.get_edt())
        string_archivo += self.string_rt(medicion.get_t20())
        string_archivo += self.string_rt(medicion.get_t30())
        string_archivo += self.string_valor(medicion.get_curvatura())
        return string_archivo
