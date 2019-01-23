from src.action.recortar_segmento_de_senal_en_tiempo_action import RecortarSegmentoDeSenalEnTiempoAction
from src.action.recortar_segmento_de_senal_entre_amplitudes_action import RecortarSegmentoDeSenalEntreAmplitudesAction


class ActionProvider:

    recortar_segmento_de_senal_entre_amplitudes_action = None
    recortar_segmento_de_senal_en_tiempo_action = None

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
