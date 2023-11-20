from Queue import Queue


class ArrayQueue(Queue):
    def __init__(self, max_size=None):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return self.max_size is not None and len(self.queue) == self.max_size

    def get_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]
