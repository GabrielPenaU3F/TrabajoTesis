from src.view.main_view import MainView
from src.view.vista_detallada.vista_detallada_view import VistaDetalladaView


class CoordinadorDeVistas:

    vistas = {
        "VistaPrincioal": None,
        "VistaDetallada": None
    }

    @classmethod
    def desplegar_vistas(cls):
        cls.vistas["VistaPrincipal"] = MainView().get_vista()
        cls.vistas["VistaDetallada"] = VistaDetalladaView().get_vista()

        cls.mostrar_vista("VistaPrincipal")

    @classmethod
    def mostrar_vista(cls, clave_vista):
        cls.vistas[clave_vista].mostrar_vista()
