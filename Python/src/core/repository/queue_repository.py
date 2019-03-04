import queue


class QueueRepository:

    queue = None

    def __init__(self):
        self.queue = queue.Queue()

    def get_queue_general(self):
        return self.queue
