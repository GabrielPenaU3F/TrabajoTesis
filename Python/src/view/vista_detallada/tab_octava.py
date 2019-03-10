from src.view.vista_detallada.tab import Tab


class TabOctava(Tab):

    def __init__(self, view, tab_control):
        self.titulo_tab = "Vista por bandas de octava"
        self.titulo_bandas_text = "Bandas de octava"
        super().__init__(view, tab_control)

    def obtener_bandas(self):
        return self.bandas_estandar_repository.get_frecuencias_centrales_octavas()


