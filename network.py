from core import Printable
from io import StringIO
from computer import Computer

class Network(Printable):
    def __init__(self, name):
        self.name = name
        self.computers = []

    def add_computer(self, comp: Computer):
        self.computers.append(comp)
        return self

    def find_computer(self, name):
        for c in self.computers:
            if c.name == name:
                return c
        return None

    def print_me(self, os: StringIO, prefix="", is_last=False):
        os.write(f"Network: {self.name}\n")
        for i, comp in enumerate(self.computers):
            comp_is_last = (i == len(self.computers) - 1)
            comp.print_me(os, "", comp_is_last)

    def clone(self):
        new_net = Network(self.name)
        new_net.computers = [c.clone() for c in self.computers]
        return new_net
