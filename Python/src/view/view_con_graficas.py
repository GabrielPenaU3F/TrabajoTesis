from abc import abstractmethod

from view.view import View


class ViewConGraficas(View):

    def __init__(self, controller, root):
        super().__init__(root, controller)
        self.flag_redibujar = ''
        self.solicitud_de_redibujo = False
        self.x_posicion_cursor = None
        self.y_posicion_cursor = None

    @abstractmethod
    def redibujar_canvas(self):
        pass

    @abstractmethod
    def ocultar_graficas(self):
        pass

    def refrescar(self):
        if self.ventana_activa:
            self.controller.revisar_queue()
            self.root.update_idletasks()
            if self.flag_redibujar == '' and self.solicitud_de_redibujo:
                self.redibujar_canvas()
            self.controller.bindear_evento_root("Configure")

        self.root.after(100, self.refrescar)

    def on_arrastrar_ventana(self, evento):
        if evento.widget is self.root:
            self.ocultar_graficas()
            if self.flag_redibujar != '':
                self.root.after_cancel(self.flag_redibujar)
            self.flag_redibujar = self.root.after(100, self.activar_redibujar)

    def on_configure(self, evento):

        if self.x_posicion_cursor is None or self.y_posicion_cursor is None:
            self.x_posicion_cursor = evento.x
            self.y_posicion_cursor = evento.y

        if self.ventana_movida(evento.x, evento.y):
            self.on_arrastrar_ventana(evento)

    def activar_redibujar(self):
        self.flag_redibujar = ''

    def ventana_movida(self, x, y):
        return self.x_posicion_cursor != x or self.y_posicion_cursor != y

    def bindear_evento_root(self, binding):
        metodo_a_bindear = getattr(self, binding.get_nombre_funcion_binding())
        self.root.bind(binding.get_evento(), metodo_a_bindear)

    def unbindear_evento_root(self, binding):
        self.root.unbind(binding.get_evento())

    def bindear_eventos_root(self):
        self.controller.bindear_eventos_root()





