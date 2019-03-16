from src.core.domain.binding_evento import BindingEvento


class BindingEventosRepository:

    def __init__(self):
        self.bindings = {
            "ArrastrarVentana": BindingEvento("<Configure>", "on_arrastrar_ventana")
        }

    def get_binding(self, clave_binding):
        return self.bindings.get(clave_binding)

    def get_eventos(self):
        return self.bindings.keys()
