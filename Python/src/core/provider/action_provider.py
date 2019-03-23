from core.action.aplicar_filtro_A_action import AplicarFiltroAAction
from core.action.aplicar_filtro_media_movil_action import AplicarFiltroMediaMovilAction
from core.action.aplicar_filtro_octava_action import AplicarFiltroOctavaAction
from core.action.aplicar_filtro_tercio_de_octava_action import AplicarFiltroTercioDeOctavaAction
from core.action.calcular_curvatura_action import CalcularCurvaturaAction
from core.action.calcular_energia_total_action import CalcularEnergiaTotalAction
from core.action.calcular_raiz_cuadrada_de_senal_en_db_action import CalcularRaizCuadradaDeSenalEnDbAction
from core.action.calcular_rt_action import CalcularRTAction
from core.action.diferenciar_senal_action import DiferenciarSenalAction
from core.action.eliminar_latencia_action import EliminarLatenciaAction
from core.action.eliminar_segmento_inicial_constante_action import EliminarSegmentoInicialConstanteAction
from core.action.estimar_limite_superior_por_metodo_de_lundeby_action import \
    EstimarLimiteSuperiorPorMetodoDeLundebyAction
from core.action.integrar_senal_action import IntegrarSenalAction
from core.action.medir_respuesta_impulsional_action import MedirRespuestaImpulsionalAction
from core.action.obtener_curva_de_decaimiento_action import ObtenerCurvaDeDecaimientoAction
from core.action.ponderar_periodos_mls_action import PonderarPeriodosMLSAction
from core.action.realizar_convolucion_action import RealizarConvolucionAction
from core.action.realizar_correlacion_action import RealizarCorrelacionAction
from core.action.recortar_segmento_de_senal_en_tiempo_action import RecortarSegmentoDeSenalEnTiempoAction
from core.action.recortar_segmento_de_senal_entre_amplitudes_action import RecortarSegmentoDeSenalEntreAmplitudesAction
from core.action.transformar_a_escala_logaritmica_normalizada_action import \
    TransformarAEscalaLogaritmicaNormalizadaAction
from core.action.transformar_fourier_action import TransformarFourierAction


class ActionProvider:

    calcular_curvatura_action = None
    aplicar_filtro_tercio_de_octava_action = None
    aplicar_filtro_octava_action = None
    aplicar_filtro_A_action = None
    calcular_raiz_cuadrada_de_senal_en_db_action = None
    diferenciar_senal_action = None
    estimar_limite_superior_por_metodo_de_lundeby_action = None
    transformar_a_escala_logaritmica_normalizada_action = None
    realizar_correlacion_action = None
    realizar_convolucion_action = None
    recortar_segmento_de_senal_entre_amplitudes_action = None
    recortar_segmento_de_senal_en_tiempo_action = None
    transformar_fourier_action = None
    eliminar_segmento_inicial_constante_action = None
    calcular_energia_total_action = None
    eliminar_latencia_action = None
    ponderar_periodos_mls_action = None
    medir_respuesta_impulsional_action = None
    aplicar_filtro_media_movil_action = None
    integrar_senal_action = None
    obtener_curva_de_decaimiento_action = None
    calcular_rt_action = None
    aplicar_filtro_pasabanda_action = None

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

    @classmethod
    def provide_eliminar_latencia_action(cls):
        if cls.eliminar_latencia_action is None:
            cls.eliminar_latencia_action = EliminarLatenciaAction()

        return cls.eliminar_latencia_action

    @classmethod
    def provide_ponderar_periodos_mls_action(cls):
        if cls.ponderar_periodos_mls_action is None:
            cls.ponderar_periodos_mls_action = PonderarPeriodosMLSAction()

        return cls.ponderar_periodos_mls_action

    @classmethod
    def provide_medir_respuesta_impulsional_action(cls):
        if cls.medir_respuesta_impulsional_action is None:
            cls.medir_respuesta_impulsional_action = MedirRespuestaImpulsionalAction()

        return cls.medir_respuesta_impulsional_action

    @classmethod
    def provide_realizar_convolucion_action(cls):
        if cls.realizar_convolucion_action is None:
            cls.realizar_convolucion_action = RealizarConvolucionAction()

        return cls.realizar_convolucion_action

    @classmethod
    def provide_aplicar_filtro_media_movil_action(cls):
        if cls.aplicar_filtro_media_movil_action is None:
            cls.aplicar_filtro_media_movil_action = AplicarFiltroMediaMovilAction()

        return cls.aplicar_filtro_media_movil_action

    @classmethod
    def provide_realizar_correlacion_action(cls):
        if cls.realizar_correlacion_action is None:
            cls.realizar_correlacion_action = RealizarCorrelacionAction()

        return cls.realizar_correlacion_action

    @classmethod
    def provide_integrar_senal_action(cls):
        if cls.integrar_senal_action is None:
            cls.integrar_senal_action = IntegrarSenalAction()

        return cls.integrar_senal_action

    @classmethod
    def provide_transformar_a_escala_logaritmica_normalizada_action(cls):
        if cls.transformar_a_escala_logaritmica_normalizada_action is None:
            cls.transformar_a_escala_logaritmica_normalizada_action = TransformarAEscalaLogaritmicaNormalizadaAction()

        return cls.transformar_a_escala_logaritmica_normalizada_action

    @classmethod
    def provide_estimar_limite_superior_por_metodo_de_lundeby_action(cls):
        if cls.estimar_limite_superior_por_metodo_de_lundeby_action is None:
            cls.estimar_limite_superior_por_metodo_de_lundeby_action = EstimarLimiteSuperiorPorMetodoDeLundebyAction()

        return cls.estimar_limite_superior_por_metodo_de_lundeby_action

    @classmethod
    def provide_obtener_curva_de_decaimiento_action(cls):
        if cls.obtener_curva_de_decaimiento_action is None:
            cls.obtener_curva_de_decaimiento_action = ObtenerCurvaDeDecaimientoAction()

        return cls.obtener_curva_de_decaimiento_action

    @classmethod
    def provide_diferenciar_senal_action(cls):
        if cls.diferenciar_senal_action is None:
            cls.diferenciar_senal_action = DiferenciarSenalAction()

        return cls.diferenciar_senal_action

    @classmethod
    def provide_calcular_raiz_cuadrada_de_senal_en_db_action(cls):
        if cls.calcular_raiz_cuadrada_de_senal_en_db_action is None:
            cls.calcular_raiz_cuadrada_de_senal_en_db_action = CalcularRaizCuadradaDeSenalEnDbAction()

        return cls.calcular_raiz_cuadrada_de_senal_en_db_action

    @classmethod
    def provide_calcular_rt_action(cls):
        if cls.calcular_rt_action is None:
            cls.calcular_rt_action = CalcularRTAction()

        return cls.calcular_rt_action

    @classmethod
    def provide_aplicar_filtro_A_action(cls):
        if cls.aplicar_filtro_A_action is None:
            cls.aplicar_filtro_A_action = AplicarFiltroAAction()

        return cls.aplicar_filtro_A_action

    @classmethod
    def provide_aplicar_filtro_octava_action(cls):
        if cls.aplicar_filtro_octava_action is None:
            cls.aplicar_filtro_octava_action = AplicarFiltroOctavaAction()

        return cls.aplicar_filtro_octava_action

    @classmethod
    def provide_aplicar_filtro_tercio_de_octava_action(cls):
        if cls.aplicar_filtro_tercio_de_octava_action is None:
            cls.aplicar_filtro_tercio_de_octava_action = AplicarFiltroTercioDeOctavaAction()

        return cls.aplicar_filtro_tercio_de_octava_action

    @classmethod
    def provide_calcular_curvatura_action(cls):
        if cls.calcular_curvatura_action is None:
            cls.calcular_curvatura_action = CalcularCurvaturaAction()

        return cls.calcular_curvatura_action
