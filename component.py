from core import Printable
from io import StringIO
import copy

class Component(Printable):
    def __init__(self, numeric_val=0):
        self.numeric_val = numeric_val

class Address(Printable):
    def __init__(self, addr):
        self.address = addr

    def print_me(self, os: StringIO, prefix="", is_last=False):
        connector = "\\-" if is_last else "+-"
        os.write(f"{prefix}{connector}{self.address}\n")

    def clone(self):
        return Address(self.address)

class CPU(Component):
    def __init__(self, cores, mhz):
        super().__init__()
        self.cores = cores
        self.mhz = mhz

    def print_me(self, os: StringIO, prefix="", is_last=False):
        connector = "\\-" if is_last else "+-"
        os.write(f"{prefix}{connector}CPU, {self.cores} cores @ {self.mhz}MHz\n")

    def clone(self):
        return CPU(self.cores, self.mhz)

class Memory(Component):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def print_me(self, os: StringIO, prefix="", is_last=False):
        connector = "\\-" if is_last else "+-"
        os.write(f"{prefix}{connector}Memory, {self.size} MiB\n")

    def clone(self):
        return Memory(self.size)

class Disk(Component):
    SSD = 0
    MAGNETIC = 1

    def __init__(self, storage_type, size):
        super().__init__()
        self.storage_type = storage_type
        self.size = size
        self.partitions = []

    def add_partition(self, size, name):
        self.partitions.append((size, name))
        return self

    def print_me(self, os: StringIO, prefix="", is_last=False):
        connector = "\\-" if is_last else "+-"
        os.write(f"{prefix}{connector}HDD, {self.size} GiB\n")
        new_prefix = prefix + ("  " if is_last else "| ")
        for i, (size, name) in enumerate(self.partitions):
            part_connector = "\\-" if i == len(self.partitions) - 1 else "+-"
            os.write(f"{new_prefix}{part_connector}[{i}]: {size} GiB, {name}\n")

    def clone(self):
        new_disk = Disk(self.storage_type, self.size)
        new_disk.partitions = copy.deepcopy(self.partitions)
        return new_disk
