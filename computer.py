from component import Address
from core import Printable
from io import StringIO

class Computer(Printable):
    def __init__(self, name):
        self.name = name
        self.addresses = []
        self.components = []

    def add_address(self, addr):
        if isinstance(addr, str):
            self.addresses.append(Address(addr))
        else:
            self.addresses.append(addr)
        return self

    def add_component(self, comp):
        self.components.append(comp)
        return self

    def print_me(self, os: StringIO, prefix="", is_last=False):
        connector = "\\-" if is_last else "+-"
        os.write(f"{prefix}{connector}Host: {self.name}\n")
        new_prefix = prefix + ("  " if is_last else "| ")
        items = self.addresses + self.components
        for i, item in enumerate(items):
            item_is_last = (i == len(items) - 1)
            item.print_me(os, new_prefix, item_is_last)

    def clone(self):
        new_comp = Computer(self.name)
        new_comp.addresses = [a.clone() for a in self.addresses]
        new_comp.components = [c.clone() for c in self.components]
        return new_comp
