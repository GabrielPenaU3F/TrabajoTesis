from src.action.recortar_segmento_de_senal_en_tiempo_action import RecortarSegmentoDeSenalEnTiempoAction
from src.action.recortar_segmento_de_senal_entre_amplitudes_action import RecortarSegmentoDeSenalEntreAmplitudesAction
from src.action.transformar_fourier_action import TransformarFourierAction


class ActionProvider:

    recortar_segmento_de_senal_entre_amplitudes_action = None
    recortar_segmento_de_senal_en_tiempo_action = None
    transformar_fourier_action = None

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
