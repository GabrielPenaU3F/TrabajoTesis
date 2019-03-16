class BindingEvento:

    def __init__(self, evento, nombre_funcion_binding):
        self.evento = evento
        self.nombre_funcion_binding = nombre_funcion_binding

    def get_evento(self):
        return self.evento

    def get_nombre_funcion_binding(self):
        return self.nombre_funcion_binding
