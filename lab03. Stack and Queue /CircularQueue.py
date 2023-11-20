from Queue import Queue


class CircularQueue(Queue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def get_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
