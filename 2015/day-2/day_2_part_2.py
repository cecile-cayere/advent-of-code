import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2015/day-2/input.txt')
content = split_string(content, "\n")

result = 0

for present in content:
    split = split_string(present, "x")
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])

    smallest_side = l+w

    if(w+h < smallest_side):
        smallest_side = w+h
    if(h+l < smallest_side):
        smallest_side = h+l

    result = result + (2 * smallest_side) + (l * w * h)

print(result)