import sys
sys.path.append('../advent-of-code')
from utils import *
import re

content = get_file_content('2024/day-03/input.txt')
content = split_string(content, "\n")

pattern = re.compile("(mul\([1-9]?[0-9]?[0-9]?,[1-9]?[0-9]?[0-9]?\))")
sum = 0

for line in content:
    for match in re.finditer(pattern, line):
        str = match.group()
        numbers = split_string(split_string(split_string(str, "mul(")[1], ")")[0], ",")
        sum = sum + (int(numbers[0]) * int(numbers[1]))

print(sum)