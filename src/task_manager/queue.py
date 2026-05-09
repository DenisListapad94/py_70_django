class EmptyQueueError(Exception):
    pass

class Queue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO,LIFO]
    def __init__(self, strategy: str = FIFO):
        self.strategy = strategy
        self.storage = []
        if self.strategy not in self.STRATEGIES:
            raise TypeError

    def add(self, item):
        if self.strategy == self.FIFO:
            self.storage.insert(0,item)

    def remove(self):
        if self.strategy == self.FIFO:
            if not self.storage:
                raise EmptyQueueError
            return self.storage.pop()
