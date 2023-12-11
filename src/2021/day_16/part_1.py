from typing import Tuple

from utils.utils import read_file

class Packet:
    sum_versions = 0
    def __init__(self, version):
        self.version = version
        self.type = 0
        self.size = 0

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

def hex_to_binary(hex_string):
    binary_string = ''.join(['{0:04b}'.format(int(d, 16)) for d in hex_string])
    return binary_string

def main(example=False):
    for line in read_file(example):
        p = Packet.generate(hex_to_binary(line), 0)
        pass
    res = Packet.sum_versions
    print(res)
    return res


assert main(True) == 31
main()
