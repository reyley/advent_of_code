from utils.utils import read_file
import re

word_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

def replace_numbers(line):
    new_line = ""
    for i, char in enumerate(line):
        if char.isdigit():
            new_line += char
        for word, num in word_numbers.items():
            if line[i:].startswith(word):
                new_line += num
    return new_line

def main(example=False):
    res = 0
    for line in read_file(example):
        line = replace_numbers(line)
        numbers = re.findall(r'\d+', line)
        res += int(numbers[0][0] + numbers[-1][-1])

    print(res)
    return res


assert main(True) == 281
main()
