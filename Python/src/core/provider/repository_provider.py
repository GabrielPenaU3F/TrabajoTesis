from src.core.repository.string_repository import StringRepository


class RepositoryProvider:

    string_repository = None

    @classmethod
    def provide_string_repository(cls):

        if cls.string_repository is None:
            cls.string_repository = StringRepository()

        return cls.string_repository
