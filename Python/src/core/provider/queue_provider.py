import queue


class QueueProvider:

    vista_detallada_queue = None
    main_queue = None

    @classmethod
    def provide_main_queue(cls):

        if cls.main_queue is None:
            cls.main_queue = queue.Queue()

        return cls.main_queue

    @classmethod
    def provide_vista_detallada_queue(cls):

        if cls.vista_detallada_queue is None:
            cls.vista_detallada_queue = queue.Queue()

        return cls.vista_detallada_queue
