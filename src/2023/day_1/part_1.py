from utils.utils import read_file
import re

def main(example=False):
    res = 0
    for line in read_file(example):
        numbers = re.findall(r'\d+', line)
        res += int(numbers[0][0] + numbers[-1][-1])

    print(res)
    return res


assert main(True) == 142
main()
