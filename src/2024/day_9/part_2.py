import heapq
from math import ceil

from utils.utils import *


class FreeSpace:
    free_space_by_size = defaultdict(list)

    def __init__(self, size, prev=None):
        self.size = size
        self.min_number = prev.number if prev else None
        self.prev = prev
        self.next = None
        if self.min_number is not None:
            heapq.heappush(self.free_space_by_size[self.size],(self.min_number, self))

    @classmethod
    def get(cls, size):
        try:
            return cls.free_space_by_size[size][0][1]
        except:
            return None

    @classmethod
    def pop(cls, size, number):
        free_space = cls.get(size)
        for s in range(size + 1, 10):
            s_free_space = cls.get(s)
            if s_free_space:
                if free_space:
                    free_space = s_free_space if s_free_space.min_number < free_space.min_number else free_space
                else:
                    free_space = s_free_space
        if free_space and free_space.min_number < number:
            return heapq.heappop(cls.free_space_by_size[free_space.size])[1]
        return None

    def resize(self, new_size):
        self.size = new_size
        if new_size == 0:
            return
        heapq.heappush(self.free_space_by_size[new_size], (self.min_number, self))

    def __repr__(self):
        return f"free({self.size}, {self.min_number})"


class File:
    files: dict[int,"File"] = dict()

    def __init__(self, size, number, free_space):
        if number == 0:
            self.reset()
        self.size = size
        self.number = number
        self.moved = False
        self.prev = None
        self.next = FreeSpace(free_space, self)

    @classmethod
    def reset(cls):
        cls.files = dict()
        FreeSpace.free_space_by_size = defaultdict(list)

    def add_to_files(self):
        assert len(self.files) == self.number
        prev = None
        if self.number > 0:
            prev = self.files[self.number-1]
            if prev.next:  # has free space
                prev = prev.next
                prev.next = self
        self.files[self.number] = self
        self.prev = prev

    def __repr__(self):
        return f"{self.number}({self.size})"


def add_file_to_output(node: FreeSpace | File, output_idx, output_sum, output=None):
    if isinstance(node, FreeSpace):
        if output is not None:
            output.extend(["."] * node.size)
        return output_idx + node.size, output_sum
    how_many = node.size
    file_num = node.number
    end_idx = output_idx + how_many
    while output_idx < end_idx:
        if output is not None:
            output.append(file_num)
        output_sum += output_idx * file_num
        output_idx += 1
    return output_idx, output_sum


def process_files(last_file):
    cur_num = last_file.number
    while cur_num >= 0:
        cur_node = File.files[cur_num]
        cur_num -= 1
        # print(f"{cur_node=}")
        if isinstance(cur_node, File):
            free_space: FreeSpace | None = FreeSpace.pop(cur_node.size, cur_node.number)
            if free_space:
                # print(f"{free_space=}")
                free_space.resize(free_space.size - cur_node.size)
                # removing cur_node
                cur_node_next = cur_node.next
                cur_node_prev = cur_node.prev
                new_free_space = FreeSpace(cur_node.size)
                new_free_space.min_number = cur_node.number
                new_free_space.prev = cur_node_prev
                cur_node_prev.next = new_free_space
                new_free_space.next = cur_node_next
                cur_node_next.prev = new_free_space

                # adding cur_node before free_space and removing free space if 0
                free_space_prev = free_space.prev
                free_space_prev.next = cur_node
                cur_node.prev = free_space_prev
                cur_node.next = free_space if free_space.size else free_space.next
                cur_node.next.prev = cur_node
                cur_node.prev = free_space_prev

    # process output

    start = File.files[0]
    cur_node = start
    output = []  # to debug
    output_sum = 0
    output_idx = 0
    while cur_node:
        output_idx, output_sum = add_file_to_output(cur_node, output_idx, output_sum, output)
        cur_node = cur_node.next
    print(output)
    return output_sum


def main(example=False):
    file = None
    for line in read_file(example):
        file_num = 0
        for i in range(0, len(line), 2):
            file_size = int(line[i])
            free_space = int(line[i + 1]) if i < len(line) - 1 else 0
            file = File(file_size, file_num, free_space)
            file.add_to_files()
            file_num += 1
    res = process_files(file)
    # res = 0
    print(res)
    return res


assert main(True) == 2858
main()
