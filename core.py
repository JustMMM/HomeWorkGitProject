from abc import ABC, abstractmethod
from io import StringIO

class Printable(ABC):
    @abstractmethod
    def print_me(self, os: StringIO, prefix="", is_last=False):
        pass

    @abstractmethod
    def clone(self):
        pass

class BasicCollection(Printable):
    def __init__(self):
        self.items = []

    def add(self, elem):
        self.items.append(elem)
        return self

    def find(self, name):
        for item in self.items:
            if hasattr(item, "name") and item.name == name:
                return item
        return None

    def print_me(self, os: StringIO, prefix="", is_last=False):
        for i, item in enumerate(self.items):
            is_last_item = (i == len(self.items) - 1)
            item.print_me(os, prefix, is_last_item)

    def clone(self):
        new_collection = BasicCollection()
        new_collection.items = [item.clone() for item in self.items]
        return new_collection
