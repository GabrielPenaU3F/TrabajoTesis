from collections import OrderedDict
from threading import Thread

import pyexcel

from core.domain.archivos.dialogo_exportar_medicion import DialogoExportarMedicion
from core.domain.archivos.escritor_de_archivos import EscritorDeArchivos
from core.domain.mensaje import Mensaje
from core.provider.queue_provider import QueueProvider
from exception.excepciones import IOException


class EscritorDeArchivosOdsXls(EscritorDeArchivos):

    def __init__(self):
        self.queue = QueueProvider.provide_thread_queue()

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
                book = OrderedDict()
                book["Respuesta impulsional"] = self.generar_sheet_senal(ri)
                book["Curva de decaimiento"] = self.generar_sheet_senal(cd)
                book["Tiempos de reverberación"] = self.generar_sheet_rts(edt, t20, t30, curvatura)
                book_excel = pyexcel.get_book(bookdict=book)

                thread_exportar = Thread(target=self.escribir_book, args=(book_excel, archivo.name,), daemon=False)
                thread_exportar.start()

            else:
                raise IOException("No se pudo escribir el archivo")

    def escribir_book(self, book, path):
        from core.domain.coordinador_de_vistas import CoordinadorDeVistas
        CoordinadorDeVistas.mostrar_vista("VistaPantallaEsperaExportar")
        book.save_as(path)
        self.queue.put(Mensaje(destinatario="VistaPrincipal", mensaje="ExportacionCompleta"))


    def generar_sheet_senal(self, senal):
        sheet = []
        sheet.append(["Datos muestreados a: ", senal.get_fs()])
        sheet.append([""])
        valores_senal = senal.get_valores()
        for i in range(len(valores_senal)):
            sheet.append([valores_senal[i]])
        return sheet

    def generar_sheet_rts(self, edt, t20, t30, curvatura):
        sheet = []
        sheet.append(["", "RT", "r", "ξ"])
        sheet.append([""])
        sheet.append(["EDT", edt.get_rt(), edt.get_coef_correlacion(), edt.get_xi()])
        sheet.append(["T20", t20.get_rt(), t20.get_coef_correlacion(), t20.get_xi()])
        sheet.append(["T30", t30.get_rt(), t30.get_coef_correlacion(), t30.get_xi()])
        sheet.append([""])
        sheet.append(["Curvatura", curvatura])
        return sheet


