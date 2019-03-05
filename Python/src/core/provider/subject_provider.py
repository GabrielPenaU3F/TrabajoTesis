from rx.subjects import Subject


class SubjectProvider:

    pantalla_espera_subject = None

    @classmethod
    def provide_pantalla_espera_subject(cls):
        if cls.pantalla_espera_subject is None:
            cls.pantalla_espera_subject = Subject()

        return cls.pantalla_espera_subject
