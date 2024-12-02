from part_2 import springs_options
from part_2 import count_options as count_2
from part_1 import count_options as count_1
from utils.utils import read_file, int_line

for line in read_file(False):
    springs, damaged_num = line.split(" ")
    print(springs)
    damaged_num = int_line(damaged_num)
    count1 = count_1(springs, damaged_num)
    count2 = count_2(springs, damaged_num)
    if count1 != count2:
        print(springs, damaged_num, count1, count2)
    assert count1 == count2

# assert len(springs_options("???.###", [1,1,3])) == 1
#
# assert len(springs_options(".??..??...?##.", [1,1,3])) == 4
#
# assert len(springs_options("?#?#?#?#?#?#?#?", [1,3,1,6])) == 1
#
# assert len(springs_options("????.#...#...", [4,1,1])) == 1
#
# assert len(springs_options("????.######..#####.", [1,6,5])) == 4
#
# assert len(springs_options("?###????????", [3,2,1])) == 10