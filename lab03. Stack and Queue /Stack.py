from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def isFull(self):
        pass

    @abstractmethod
    def top(self):
        pass
