class Stack:
    def push(self, item):
        raise NotImplementedError("This method should be implemented by subclasses")

    def pop(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def peek(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def is_empty(self):
        raise NotImplementedError("This method should be implemented by subclasses")
