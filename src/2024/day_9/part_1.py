from math import ceil

from utils.utils import *


def add_file_to_output(file_num, how_many, output_idx, output_sum, output=None):
    end_idx = output_idx + how_many
    while output_idx < end_idx:
        if output is not None:
            output.append(file_num)
        output_sum += output_idx * file_num
        output_idx += 1
    return output_idx, output_sum


def process_line(line, num_files):
    end_file_index = len(line) - 1
    end_file_number = num_files - 1
    end_file_left = int(line[-1])
    output = None  # to debug
    output_sum = 0
    output_idx = 0
    file_num = 0
    for i in range(0, len(line), 2):
        if i == end_file_index:
            output_idx, output_sum = add_file_to_output(end_file_number, end_file_left, output_idx, output_sum, output)
            break
        how_many = int(line[i])
        how_much_free_space = int(line[i+1])
        output_idx, output_sum = add_file_to_output(file_num, how_many, output_idx, output_sum, output)
        while how_much_free_space >= end_file_left:
            how_much_free_space -= end_file_left
            output_idx, output_sum = add_file_to_output(end_file_number, end_file_left, output_idx, output_sum, output)
            end_file_index -= 2
            end_file_number -= 1
            end_file_left = int(line[end_file_index])
            if end_file_index == i:
                break
        if end_file_index == i:
            break
        output_idx, output_sum = add_file_to_output(end_file_number, how_much_free_space, output_idx, output_sum, output)
        end_file_left -= how_much_free_space
        file_num += 1
    print(output)
    return output_sum


def main(example=False):
    for line in read_file(example):
        num_files = ceil(len(line) / 2)
        res = process_line(line, num_files)
    # res = 0
    print(res)
    return res


assert main(True) == 1928
main()
