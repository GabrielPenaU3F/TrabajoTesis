import queue


class QueueProvider:

    thread_queue = None

    @classmethod
    def provide_thread_queue(cls):

        if cls.thread_queue is None:
            cls.thread_queue = queue.Queue()

        return cls.thread_queue

