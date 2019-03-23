from view.instrucciones_view import InstruccionesView
from view.main_view import MainView
from view.pantalla_espera_view import PantallaEsperaView
from view.vista_detallada.instrucciones_vista_detallada_view import InstruccionesVistaDetalladaView
from view.vista_detallada.vista_detallada_view import VistaDetalladaView


class CoordinadorDeVistas:

    vistas = {
        "VistaPrincioal": None,
        "VistaDetallada": None,
        "VistaInstrucciones": None,
        "VistaDetalladaInstrucciones": None,
        "VistaPantallaEspera": None
    }

    @classmethod
    def desplegar_vistas(cls):
        cls.vistas["VistaPrincipal"] = MainView().get_vista()
        cls.vistas["VistaInstrucciones"] = InstruccionesView().get_vista()
        cls.vistas["VistaPantallaEspera"] = PantallaEsperaView().get_vista()
        cls.vistas["VistaDetallada"] = VistaDetalladaView().get_vista()
        cls.vistas["VistaDetalladaInstrucciones"] = InstruccionesVistaDetalladaView().get_vista()

        cls.mostrar_vista("VistaPrincipal")

    @classmethod
    def mostrar_vista(cls, clave_vista):
        cls.vistas[clave_vista].mostrar_vista()
