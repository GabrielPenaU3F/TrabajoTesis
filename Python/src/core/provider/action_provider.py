from src.core.action.calcular_energia_total_action import CalcularEnergiaTotalAction
from src.core.action.eliminar_segmento_inicial_constante_action import EliminarSegmentoInicialConstanteAction
from src.core.action.recortar_segmento_de_senal_en_tiempo_action import RecortarSegmentoDeSenalEnTiempoAction
from src.core.action.recortar_segmento_de_senal_entre_amplitudes_action import RecortarSegmentoDeSenalEntreAmplitudesAction
from src.core.action.transformar_fourier_action import TransformarFourierAction


class ActionProvider:

    recortar_segmento_de_senal_entre_amplitudes_action = None
    recortar_segmento_de_senal_en_tiempo_action = None
    transformar_fourier_action = None
    eliminar_segmento_inicial_constante_action = None
    calcular_energia_total_action = None

    @classmethod
    def provide_recortar_segmento_de_senal_entre_amplitudes_action(cls):
        if cls.recortar_segmento_de_senal_entre_amplitudes_action is None:
            cls.recortar_segmento_de_senal_entre_amplitudes_action = RecortarSegmentoDeSenalEntreAmplitudesAction()

        return cls.recortar_segmento_de_senal_entre_amplitudes_action

    @classmethod
    def provide_recortar_segmento_de_senal_en_tiempo_action(cls):
        if cls.recortar_segmento_de_senal_en_tiempo_action is None:
            cls.recortar_segmento_de_senal_en_tiempo_action = RecortarSegmentoDeSenalEnTiempoAction()

        return cls.recortar_segmento_de_senal_en_tiempo_action

    @classmethod
    def provide_transformar_fourier_action(cls):
        if cls.transformar_fourier_action is None:
            cls.transformar_fourier_action = TransformarFourierAction()

        return cls.transformar_fourier_action

    @classmethod
    def provide_eliminar_segmento_inicial_constante_action(cls):
        if cls.eliminar_segmento_inicial_constante_action is None:
            cls.eliminar_segmento_inicial_constante_action = EliminarSegmentoInicialConstanteAction()

        return cls.eliminar_segmento_inicial_constante_action

    @classmethod
    def provide_calcular_energia_total_action(cls):
        if cls.calcular_energia_total_action is None:
            cls.calcular_energia_total_action = CalcularEnergiaTotalAction()

        return cls.calcular_energia_total_action
