import sys
sys.path.append('../advent-of-code')
from utils import *
import re

content = get_file_content('2024/day-03/input.txt')
content = split_string(content, "\n")

pattern = re.compile("(mul\([1-9]?[0-9]?[0-9]?,[1-9]?[0-9]?[0-9]?\))|(do\(\))|(don't\(\))")
sum = 0
is_activated = True

for line in content:
    for match in re.finditer(pattern, line):
        str = match.group()
        
        if(str == "do()"):
            is_activated = True
        elif(str == "don't()"):
            is_activated = False
        else:
            if(is_activated):
                str = split_string(str, "mul(")
                str = split_string(str[1], ")")
                numbers = split_string(str[0], ",")
        
                sum = sum + (int(numbers[0]) * int(numbers[1]))

print(sum)