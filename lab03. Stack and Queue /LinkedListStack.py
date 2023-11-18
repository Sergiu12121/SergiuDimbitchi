from Stack import Stack


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack(Stack):
    def __init__(self, capacity):
        self.head = None
        self.size = 0
        self.capacity = capacity

    def push(self, item):
        if self.isFull():
            raise OverflowError("Stack is full")
        new_node = LinkedListNode(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return self.size >= self.capacity

    def top(self):
        if self.isEmpty():
            raise IndexError("top from empty stack")
        return self.head.value
