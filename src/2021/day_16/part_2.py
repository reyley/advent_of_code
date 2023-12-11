from typing import Tuple

from utils.utils import read_file

class Packet:
    sum_versions = 0
    def __init__(self, version):
        self.version = version
        self.type = 0
        self.size = 0
        self.value = None

    @classmethod
    def generate(cls, line, i) -> Tuple[int, "Packet"]:
        if i == 0:
            cls.sum_versions = 0
        version = cls.binary_number(line[i:i+3])
        typ = cls.binary_number(line[i+3:i+6])
        i += 6
        p = None
        if typ == 4:
            p = LiteralPacket(version, line, i)
        else:
            p = OpPacket(version, typ, line, i)
        cls.sum_versions += p.version
        return i + p.size, p

    @staticmethod
    def binary_number(str_n):
        return int(str_n, 2)

class LiteralPacket(Packet):
    def __init__(self, version, line, idx):
        super().__init__(version)
        self.type = 4
        self.value = self.get_value(line, idx)

    def get_value(self, line, i):
        done = False
        n_str = ""
        start = i
        while not done:
            done = line[i] == "0"
            n_str += line[i + 1: i + 5]
            i = i + 5
        self.size = i - start
        return self.binary_number(n_str)


class OpPacket(Packet):
    def __init__(self, version, typ, line, index):
        super().__init__(version)
        self.type = typ
        self.subpackets = self.create_subpackets(line, index)
        self.value = self.get_value()

    def create_subpackets(self, line, i):
        start = i
        packets = []
        if line[i] == "0":
            num_bytes = self.binary_number(line[i+1:i+16])
            i +=  16
            start_bytes = i
            while i - start_bytes < num_bytes:
                i, p = Packet.generate(line, i)
                packets.append(p)
        else:
            num_packets = self.binary_number(line[i + 1:i + 12])
            i += 12
            for _ in range(num_packets):
                i, p = Packet.generate(line, i)
                packets.append(p)
        self.size = i - start
        return packets

    def get_value(self):
        op = self.op()
        values = [p.value for p in self.subpackets]
        return op(values)

    def op(self):
        if self.type == 0:
            return sum
        if self.type == 1:
            return OpPacket.product
        if self.type == 2:
            return min
        if self.type == 3:
            return max
        if self.type == 5:
            return OpPacket.gt
        if self.type == 6:
            return OpPacket.lt
        if self.type == 7:
            return OpPacket.eq

    @staticmethod
    def product(arr):
        p = 1
        for x in arr:
            p *= x
        return p

    @staticmethod
    def gt(arr):
        return 1 if arr[0] > arr[1] else 0

    @staticmethod
    def lt(arr):
        return 1 if arr[0] < arr[1] else 0

    @staticmethod
    def eq(arr):
        return 1 if arr[0] == arr[1] else 0


def hex_to_binary(hex_string):
    binary_string = ''.join(['{0:04b}'.format(int(d, 16)) for d in hex_string])
    return binary_string

def main(example=False):
    for line in read_file(example):
        i, p = Packet.generate(hex_to_binary(line), 0)
        res = p.value
    print(res)
    return res


assert main(True) == 1
main()
