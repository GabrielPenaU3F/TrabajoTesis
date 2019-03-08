from rx.subjects import Subject


class SubjectProvider:

    pantalla_espera_subject = None
    pantalla_instrucciones_subject = None
    vista_detallada_subject = None

    @classmethod
    def provide_pantalla_espera_subject(cls):
        if cls.pantalla_espera_subject is None:
            cls.pantalla_espera_subject = Subject()

        return cls.pantalla_espera_subject

    @classmethod
    def provide_pantalla_instrucciones_subject(cls):

        if cls.pantalla_instrucciones_subject is None:
            cls.pantalla_instrucciones_subject = Subject()

        return cls.pantalla_instrucciones_subject

    @classmethod
    def provide_vista_detallada_subject(cls):

        if cls.vista_detallada_subject is None:
            cls.vista_detallada_subject = Subject()

        return cls.vista_detallada_subject
