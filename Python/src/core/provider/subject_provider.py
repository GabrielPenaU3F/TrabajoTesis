from rx.subjects import Subject

class SubjectProvider:

    cierre_pantalla_espera_subject = None

    @classmethod
    def provide_cierre_pantalla_espera_subject(cls):
        if cls.cierre_pantalla_espera_subject is None:
            cls.cierre_pantalla_espera_subject = Subject()

        return cls.cierre_pantalla_espera_subject
