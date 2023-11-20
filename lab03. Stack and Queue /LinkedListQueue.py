from Queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue(Queue):
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def get_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data
