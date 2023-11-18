from collections import deque
from Stack import Stack


class DequeStack(Stack):
    def __init__(self, capacity):
        self.items = deque()
        self.capacity = capacity

    def push(self, item):
        if self.isFull():
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) >= self.capacity

    def top(self):
        if self.isEmpty():
            raise IndexError("top from empty stack")
        return self.items[-1]
