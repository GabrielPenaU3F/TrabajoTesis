import queue


class QueueProvider:

    queue_general = None

    @classmethod
    def provide_queue_general(cls):

        if cls.queue_general is None:
            cls.queue_general = queue.Queue()

        return cls.queue_general
